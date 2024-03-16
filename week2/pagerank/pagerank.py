import os
import random
import re
import sys
import random
from copy import deepcopy

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    res = {}
    if page not in corpus:
        raise ValueError
    links = corpus[page]
    pages = list(corpus.keys())
    # if no links, return a probability distribution that chooses randomly among all pages with equal probability.
    if links == None:
        return {each : 1 / len(corpus) for each in pages}
    for each in pages:
        if each not in links:
            res[each] = (1 - damping_factor) / len(corpus)
        else:
            res[each] = (1 - damping_factor) / len(corpus) + damping_factor / len(links)
    return res


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    pages = list(corpus.keys())
    statistics = {each : 0 for each in pages}
    # first sample
    total = len(pages)
    current = pages[random.randint(0, total - 1)]   # both include
    statistics[current] += 1
    i = 1
    # iterate over all the remains
    while i < n:
        data = transition_model(corpus, current, damping_factor)
        current = random.choices(list(data.keys()), list(data.values()))[0]
        statistics[current] += 1
        i += 1
    # calculate probability
    probability = {page : times / n for page, times in statistics.items()}
    return probability


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    total = len(corpus)
    pages = list(corpus.keys())

    # assigning each page a rank of 1 / N
    old_rank = {each : 1 / total for each in pages}
    new_rank = {}

    # iterate over
    change = 1
    while change >= 0.001:
        for page in pages:
            new = 0
            for link_to in pages:
                # A page that has no links should be interpreted as having one link for every page
                if len(corpus[link_to]) == 0:    # set() != None
                    new += old_rank[link_to] / total
                elif page in corpus[link_to]:
                    new += old_rank[link_to] / len(corpus[link_to])

            new_rank[page] = new * damping_factor + (1 - damping_factor) / total

        change = max([abs(new_rank[x] - old_rank[x]) for x in pages])
        old_rank = new_rank.copy()    

    return new_rank


if __name__ == "__main__":
    main()
