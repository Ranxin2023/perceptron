###perceptron###
#   Ranxin Li   #
#   Jun. 1st. 2022  #
#   ECS 170, SQ, 2022   #
import copy
#
#main function of this program
#input:
#   Threshold: the number of threshold
#   Adjustment: the number added or subtracted from weights
#   weights: a list of numbers for weight
#   examples: a list for which each one contains a boolean and a list of 0 or 1
#   passes: number of passes for the total traverse
#Returned:
#   return_dict: a dictionary which contains initial conditions and each passes' inputs, predition, answer and adjusted_weights
def perceptron(Threshold, Adjustment, weights, examples,passes):
    return_dict=dict()
    init_dict=dict()
    init_dict['weights']=weights
    init_dict['threshold']=Threshold
    init_dict['adjustment']=Adjustment
    return_dict['init']=init_dict
    prediction=[0]*len(examples)
    flags=[False]*len(examples)
    for i in range(passes):
        pass_list=list()
        for example in examples:
            each_case=dict()
            prediction=makeprediction(weights, example[1], Threshold)
            weights_copy=adjustweights(Adjustment, prediction, example[1], weights,example[0])
            each_case['inputs']=example[1]
            each_case['prediction']=prediction
            each_case['answer']=example[0]
            each_case['adjusted_weights']=weights_copy
            weights=weights_copy
            pass_list.append(each_case)
        return_dict[i+1]=pass_list
    return return_dict

#This function calculate the predicted number and judges whether it overpasses the threshold or not
#input:
#   weights: a list of numbers for weight
#   inputs: a list containing 0 or 1
#   Threshold: the number of threshold
#Returned:
#   True if the predicted number larger than or equal to the threshold
#   False if the predicated number less than the threshold
def makeprediction(weights, inputs, Threshold):
    sumofpredication=0
    for i in range(len(weights)):
        sumofpredication+=(weights[i]*inputs[i])
    if sumofpredication>Threshold:
        return True
    else:
        return False
    
#This function adjust the weight to make the examples all correct
#Add adjustment if the prediction is False and the answer is True
#Subtract adjustment if the prediction is True and the answer is False
#Inputs:
#   Adjustment: the number to adjust the weight
#   prediction: judge whether the calculated predicated number is over the threshold or not
#   inputs: a list of 0 or 1
#   weights: a list of weight
#   answer: True or False for each situation
#Returned:
#   weights_copy: a copy of weight after being adjusted
def adjustweights(Adjustment, prediction,  inputs, weights, answer):
    weights_copy=copy.deepcopy(weights)
    if answer==True:
        if not prediction:
            for i in range(len(weights)):
                if inputs[i]==1:
                    weights_copy[i]+=Adjustment
    if answer==False:
        if prediction:
            for i in range(len(weights)):
                if inputs[i]==1:
                    weights_copy[i]-=Adjustment
    return weights_copy

