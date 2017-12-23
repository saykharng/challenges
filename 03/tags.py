from collections import Counter
from difflib import SequenceMatcher
from itertools import product
import re
import pdb

IDENTICAL = 1.0
TOP_NUMBER = 10
RSS_FEED = 'rss.xml'
SIMILAR = 0.87
TAG_HTML = re.compile(r'<category>([^<]+)</category>')
tag_html = '<.*?>'


def get_tags():
    """Find all tags (TAG_HTML) in RSS_FEED.
    Replace dash with whitespace.
    Hint: use TAG_HTML.findall"""
    with open(RSS_FEED) as rss:
        for line in rss:result = TAG_HTML.findall(line.lower())

    for item in result:
        if '-' in item:result[result.index(item)] = ' '.join(item.split('-'))
    all_tags = [item for item in result]
    #print(all_tags)
    return all_tags

def get_top_tags(tags):
    """Get the TOP_NUMBER of most common tags
    Hint: use most_common method of Counter (already imported)"""
    all_tags = Counter()
    for item in tags:
        all_tags[item] += 1
    #pdb.set_trace()
    result = all_tags.most_common(TOP_NUMBER)
    return result


def get_similarities(tags):
    """Find set of tags pairs with similarity ratio of > SIMILAR
    Hint 1: compare each tag, use for in for, or product from itertools (already imported)
    Hint 2: use SequenceMatcher (imported) to calculate the similarity ratio
    Bonus: for performance gain compare the first char of each tag in pair and continue if not the same"""
    #pdb.set_trace()
    for item in product(tags, tags):
        if item[0] == item[1] or item[0][0] != item[1][0]:
            continue
        item = sorted(tuple(item))
        seq_obj = SequenceMatcher(None, item[0], item[1])
        item_ratio = seq_obj.ratio()
        #print('test')
        if item_ratio > SIMILAR:
            yield item

if __name__ == "__main__":
    tags = get_tags()
    top_tags = get_top_tags(tags)
    print('* Top {} tags:'.format(TOP_NUMBER))
    for tag, count in top_tags:
        print('{:<20} {}'.format(tag, count))
    similar_tags = dict(get_similarities(tags))
    print()
    print('* Similar tags:')
    for singular, plural in similar_tags.items():

        print('{:<20} {}'.format(singular, plural))
