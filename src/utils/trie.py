def getRootOfTrie(words):
    root = {}
    for word in words:
        currentNode = root

        for char in word:
            if char in currentNode:
                currentNode = currentNode[char]
                continue

            newDic = {}
            currentNode[char] = newDic
            currentNode = newDic

        currentNode['$'] = '$'
    return root


def hasWord(root, word):
    currNode = root
    for char in word:
        if char in currNode:
            currNode = currNode[char]
            continue
        return False

    if '$' in currNode:
        return True
    return False