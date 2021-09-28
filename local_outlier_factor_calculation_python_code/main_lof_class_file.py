#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 20:46:39 2020

@author: andy
"""


#from __future__ import division
import warnings


from distance_measure import function_dist_euclidean

class main_lof_class:
    """this is the main class to compute the local outlier factor for test data points"""
    def __init__(self, train_data, feature_scaling=False, distance_function=function_dist_euclidean):
        self.train_data = train_data
        self.feature_scaling = feature_scaling
        self.distance_function = distance_function
        if feature_scaling:
            self.feature_scaling_instances()
    "to compute minimum and maximum of each column/attribute"        
    def compute_min_max(self):
        #initialize min_values to +ve infinite
        #print(len(self.train_data[0])
        min_values = [float("inf")] * len(self.train_data[0]) 
        #initialize min_values to -ve infinite
        max_values = [float("-inf")] * len(self.train_data[0]) 
        for instance in self.train_data:
            #get min value for each column/attribute
            min_values = tuple(map(lambda x,y: min(x,y), min_values,instance)) #n.minimum(min_values, instance)
            #print("min_val"+str(min_values))
            #get max value for each column/attribute
            max_values = tuple(map(lambda x,y: max(x,y), max_values,instance)) #n.maximum(max_values, instance)
            #print("max_val"+str(max_values))
        #get difference of max and min for each column/attribute     
        diff = [dim_max - dim_min for dim_max, dim_min in zip(max_values, min_values)]
        
        if not all(diff):
            problematic_dimensions = ", ".join(str(i+1) for i, v in enumerate(diff) if v == 0)
            warnings.warn("No data variation in dimensions: %s. You should check your data or disable normalization." % problematic_dimensions)

        self.max_attribute_values = max_values
        self.min_attribute_values = min_values

    def feature_scaling_instances(self):
        """feature_scaling  the instances and stores the infromation for rescaling new instances."""
        if not hasattr(self, "max_attribute_values"):
            self.compute_min_max()
        new_instances = []
        for instance in self.train_data:
            new_instances.append(self.feature_scaling_instance(instance)) # (instance - min_values) / (max_values - min_values)
        self.train_data = new_instances

    def feature_scaling_instance(self, instance):

        feature_scaling_instance_andy=tuple(map(lambda value,max,min: (value-min)/(max-min) if max-min > 0 else 0,
                         instance, self.max_attribute_values, self.min_attribute_values))
        #print(feature_scaling_instance_andy)
        return feature_scaling_instance_andy
        

    def method_lof(self, min_pts, instance):
        """The (local) outlier factor of instance captures the degree to which we call instance an outlier.
        min_pts is a parameter that is specifying a minimum number of instances to consider for computing LOF value.
        Returns: local outlier factor
        Signature: (int, (attr1, attr2, ...), ((attr_1_1, ...),(attr_2_1, ...), ...)) -> float"""
        if self.feature_scaling:
            instance = self.feature_scaling_instance(instance)
         
        local_outlier_factor_return=local_outlier_factor(min_pts, instance, self.train_data, distance_function=self.distance_function)
        #print("local_outlier_factor_andy="+str(local_outlier_factor_return))
        return local_outlier_factor_return

from k_distance import k_distance 


def reachability_distance(k, instance1, instance2, train_data, distance_function=function_dist_euclidean):
    """The reachability distance of instance1 with respect to instance2.
    Returns: reachability distance
    Signature: (int, (attr_1_1, ...),(attr_2_1, ...)) -> float"""
    (k_distance_value, neighbours) = k_distance(k, instance2, train_data, distance_function=distance_function)
    return max([k_distance_value, distance_function(instance1, instance2)])

def local_reachability_density(min_pts, instance, train_data, **kwargs):
    """Local reachability density of instance is the inverse of the average reachability
    distance based on the min_pts-nearest neighbors of instance.
    Returns: local reachability density
    Signature: (int, (attr1, attr2, ...), ((attr_1_1, ...),(attr_2_1, ...), ...)) -> float"""
    (k_distance_value, neighbours) = k_distance(min_pts, instance, train_data, **kwargs)
    reachability_distances_array = [0]*len(neighbours) #n.zeros(len(neighbours))
    for i, neighbour in enumerate(neighbours):
        reachability_distances_array[i] = reachability_distance(min_pts, instance, neighbour, train_data, **kwargs)
    if not any(reachability_distances_array):
        warnings.warn("Instance %s (could be feature_scaling done) is identical to all the neighbors. Setting local reachability density to inf." % repr(instance))
        return float("inf")
    else:
        return len(neighbours) / sum(reachability_distances_array)

"""
1. The special syntax *args in function definitions in python is used to pass a
variable number of arguments to a function.

2.
The special syntax **kwargs in function definitions in python is used to pass a 
keyworded, variable-length argument list. We use the name kwargs with the double 
star. The reason is because the double star allows us to pass through keyword 
arguments (and any number of them).
"""
#min_pts=required num of neighbour, instance=test_data_point, train_data=training data, kwargs
def local_outlier_factor(min_pts, instance, train_data, **kwargs):
    """The (local) outlier factor of instance captures the degree to which we call instance an outlier.
    min_pts is a parameter that is specifying a minimum number of instances to consider for computing LOF value.
    Returns: local outlier factor
    Signature: (int, (attr1, attr2, ...), ((attr_1_1, ...),(attr_2_1, ...), ...)) -> float"""
    (k_distance_value, neighbours) = k_distance(min_pts, instance, train_data, **kwargs)
    instance_lrd = local_reachability_density(min_pts, instance, train_data, **kwargs)
    lrd_ratios_array = [0]* len(neighbours)
    for i, neighbour in enumerate(neighbours):
        instances_without_instance = set(train_data)
        instances_without_instance.discard(neighbour)
        neighbour_lrd = local_reachability_density(min_pts, neighbour, instances_without_instance, **kwargs)
        lrd_ratios_array[i] = neighbour_lrd / instance_lrd
    return sum(lrd_ratios_array) / len(neighbours)

def outliers(k, train_data, **kwargs):
    """Simple procedure to identify outliers in the dataset."""
    instances_value_backup = train_data
    
    outliers = []
    for i, instance in enumerate(instances_value_backup):
        train_data = list(instances_value_backup)
        train_data.remove(instance)
        l = main_lof_class(train_data, **kwargs)
        value = l.local_outlier_factor(k, instance)
        if value > 1:
            outliers.append({"lof": value, "instance": instance, "index": i})
    outliers.sort(key=lambda o: o["lof"], reverse=True)
    return outliers