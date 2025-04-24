words_to_remove = {'a', 'the', 'an'}
with open('infile.txt','r') as inf,open('outfile.txt','w') as outf:
    for line in inf:
        words = line.split()
        for word in words:
            if word.lower() in words_to_remove:
                words.remove(word)
        outf.write(' '.join(words) + '\n')
print("Processed file saved as:",outf.name)
