trainlabels = open('trainlabels.txt')
lines_label = trainlabels.readlines()

cls_list_list = []
for x in lines_label :
    cls_list_list.append(x.split())

cls_flat_list = []
for element in cls_list_list :
    for sublist in element : 
        cls_flat_list.append(sublist)

cls_unique = list(dict.fromkeys(cls_flat_list))
cls_unique

#counting number of 1's and 0's in trainlabel.txt
count_cls = []
for i in cls_unique:
    count = 0
    for element in cls_flat_list :
        if element == i :
            count += 1
    count_cls.append(count)
            
count_cls 
        

#count od total docs
n_docs = 0
for element in count_cls:
    n_docs += element 
n_docs

#calculating prior probabilities for each class
prior_prob = []
for x in count_cls :
    prior_prob.append(x/n_docs)
prior_prob

traindata = open('traindata.txt')
lines_data = traindata.readlines()

data_list_list = []
for x in lines_data :
    data_list_list.append(x.split())

data_flat_list = []
for element in data_list_list :
    for sublist in element :
        data_flat_list.append(sublist)

#vocabulary
vocab = list(dict.fromkeys(data_flat_list))

count_vocab_words = []
for x in range(len(cls_unique)):
    count_vocab_words.append([0 for i in range(len(vocab))])

for c in range(len(cls_unique)):
    for index in range(len(cls_flat_list)) :
        if cls_flat_list[index] == cls_unique[c] :
            words = lines_data[index].split()
            for element in range(len(vocab)) :
                count = 0 
                for w in words:
                    if vocab[element] == w :
                        count += 1
                count_vocab_words[c][element] += count            


#total number of words in each class (including repeated words)

count_words_class = []
for index in range(len(cls_unique)) :
    c = 0 
    for l in range(len(count_vocab_words[index])) :
        c += count_vocab_words[index][l]
    count_words_class.append(c)

cond_prob_vocab = [] 
for x in cls_unique:
    cond_prob_vocab.append([0 for a in vocab])

for c in range(len(cls_unique)):
    for x in range(len(vocab)):
        cond_prob_vocab[c][x] = (count_vocab_words[c][x] +1) / ( count_words_class[c] + len(vocab) )


#Checking for accuracy with trainlabel.txt

testdata = open('traindata.txt')
lines_test_data = testdata.readlines()

prob_doc = [0 for i in range(len(cls_unique))]
prod = []
test_labels = []
sort_prob_doc = []
num = 0

for line in lines_test_data :
    for c in range(len(cls_unique)):
        prod.clear()
        words_test = line.split()
        for x in words_test:
            for y in range(len(vocab)):
                if x == vocab[y] :
                    prod.append(cond_prob_vocab[c][y])
        if len(prod) > 0 :
            prob_doc[c] = prior_prob[c]
            for num in prod :
                prob_doc[c] *= num  
    # greatest values of prob is the class which the doc belongs to
    ind_gr_prob = [i for i, j in enumerate(prob_doc) if j == max(prob_doc)]
    test_labels.append(cls_unique[ind_gr_prob[0]])

accurate = 0
inaccurate = 0 
for x in range(len(test_labels)):
    if test_labels[x] == cls_flat_list[x]:
        accurate += 1
    else :
        inaccurate +=1        
print("count of accurate labels for traindata.txt : ",accurate)
print("count of inaccurate labels for traindata.txt :",inaccurate)
print("Accuracy % :",(accurate/(accurate+inaccurate)) * 100)

testdata = open('testdata.txt')
lines_test_data = testdata.readlines()

prob_doc = [0 for i in range(len(cls_unique))]
prod = []
test_labels = []
sort_prob_doc = []
num = 0

for line in lines_test_data :
    for c in range(len(cls_unique)):
        prod.clear()
        words_test = line.split()
        for x in words_test:
            for y in range(len(vocab)):
                if x == vocab[y] :
                    prod.append(cond_prob_vocab[c][y])
        if len(prod) > 0 :
            prob_doc[c] = prior_prob[c]
            for num in prod :
                prob_doc[c] *= num  
    # greatest values of prob is the class which the doc belongs to
    ind_gr_prob = [i for i, j in enumerate(prob_doc) if j == max(prob_doc)]
    test_labels.append(cls_unique[ind_gr_prob[0]])

open("d_test_labels.txt","w").close()
d_test_labels = open("d_test_labels.txt","a")
for x in test_labels:
    x += '\n'
    d_test_labels.write(x)
