#Generator matrix for the [23, 12, 7] binary Golay code
#Formed by removing one coordinate from the generator matrix of the extended binary Golay code
golay_generator_matrix = [
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
]

#Generator matrix for the [24, 12, 8] extended binary Golay code
extended_golay_generator_matrix = [
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1]
]

#This function generates a list of all code words by linearly combining all elements of the
#generator matrix
def generate_all_code_words(generator_matrix):
    #We know that the elements of the generator matrix are code words
    code_words = generator_matrix.copy()
    
    #We continue until all code words are added
    while True:
        #Flag value for whether or not a code word was added on this iteration
        code_word_added = False

        #Loop through each element of the generator matrix
        for i in range(len(generator_matrix)):
            #Then loop through each element already added to the code
            for j in range(len(code_words)):
                #Allocate memory for a new code word
                code_word = []

                #Add the element of the generator matrix to a code word that has already been
                #added to the code
                for k in range(len(generator_matrix[i])):
                    code_word.append((generator_matrix[i][k] + code_words[j][k]) % 2)
                
                #If the sum of the two code words has not already been added, add it.  Since a
                #new code word was added, we expect there may be more code words to account for
                #so we keep iterating
                if code_word not in code_words:
                    code_words.append(code_word)
                    code_word_added = True
        
        #If by the time we have looped through the entire generator matrix we find that we have
        #not added a new code word, we know for sure that we have found all linear combinations
        #of the rows of the generator matrix (i.e. the entire code).
        if not(code_word_added):
            break

    #After we generate the entire code, return it as a list
    return code_words

#Given a code word of a code, this function calculates the code word's weight
def weight(code_word):
    #We initialize the weight as 0
    weight = 0

    #We loop through the elements of the code word and count all nonzero elements
    for bit in code_word:
        if not(bit == 0):
            #Each time we cound a nonzero element, we increment the weight by 1
            weight = weight + 1
    
    #After incrementing the weight each time a nonzero element is found, we return
    #the resulting sum, which is exactly the weight of the code word.
    return weight

#Given the code words of a code, this function calculates the code's weight distribution
def calculate_weight_distribution(code):
    #Allocate space for the weight distribution, formatted as a list
    weight_distribution = []
    
    #We add zeros to the weight distribution according to the length of the code words of the code.
    #Much like the above weight function, we will increment these zero values later
    for i in range(len(code[0])):
        weight_distribution.append(0)

    #Loop through the code words of the code
    for code_word in code:
        #Calculate the weight of each code word
        code_word_weight = weight(code_word)

        #Suppose the weight of the code word is i.  Then we increment the ith element of the weight
        #distribution.
        if not(code_word_weight == 0):
            weight_distribution[code_word_weight - 1] = weight_distribution[code_word_weight - 1] + 1
        else:
            weight_distribution[code_word_weight] = weight_distribution[code_word_weight - 1] + 1

    #After incrementing, we return the weight distribution of the code.
    return weight_distribution

#Given two code words of a code, this function calculates their inner product
def inner_product(u, v):
    #Initialize the inner product to be 0
    inner_product = 0
    
    #Loop through each position in the code words.  We expect the code words to be
    #equal in length, but in case they are not, we would simply append zeroes to the
    #end of one of them.  Since this product would inevitably be zero itself for all
    #of the extra positions, we simply loop up to the minimum length of either of the
    #code words passed in.  This should sufficiently account for this edge case.
    for i in range(min(len(u), len(v))):
        #Increment the inner product by the sum of each code word's ith coordinate
        inner_product = inner_product + u[i]*u[i]
    
    #After incremeneting the inner product, take the inner product mod 2 according to
    #the algebra of F_2
    inner_product = inner_product % 2

    #Return the inner product
    return inner_product

#Given a generator matrix, it takes the inner prodct of each row of the generator
#matrix according to the algebraic structure of F_2
def check_self_dual(generator_matrix):
    #Loop through each element of the generator matrix
    for i in range(len(generator_matrix)):
        #We only need to consider each of the n choose 2 pairs once since the inner product
        #is symmetric
        for j in range(i+1, len(generator_matrix)):
            #We take the inner product
            inner = inner_product(generator_matrix[i], generator_matrix[j])
            
            #Since the numpy inner product function considers the reals, we take 
            if not(inner == 0):
                return False
    return True

#Question 3
print("The weight distribution of the [23, 12, 7] binary Golay code:")
print(calculate_weight_distribution(generate_all_code_words(golay_generator_matrix)))

#Question 4
print("Is the [24, 12, 8] binary Golay code self-dual?")
print(check_self_dual(extended_golay_generator_matrix))