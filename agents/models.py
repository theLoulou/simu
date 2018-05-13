from django.db import models
from django.utils import timezone
import random

class Ag(models.Model):
    Ag_breedC = models.BooleanField()
    policy_ID = models.DecimalField(max_digits=15, decimal_places=1)
    age = models.PositiveSmallIntegerField()
    social_grade = models.PositiveSmallIntegerField()
    Payment = models.PositiveSmallIntegerField()
    attribute_brand = models.DecimalField(max_digits=3, decimal_places=1)
    attribute_price = models.DecimalField(max_digits=3, decimal_places=1)
    attribute_promotion = models.DecimalField(max_digits=3, decimal_places=1)
    auto_renew = models.BooleanField()
    inertia_switch = models.PositiveSmallIntegerField()
    results = models.PositiveSmallIntegerField(default=0)


    def is_lost(self, iteration):
        if iteration<1 :
            return False
        res=self.results
        if iteration==1:
            res2 = self.Ag_breedC
        else:
            res2 = (res >> (iteration-2))
        if ((res >> (iteration-1)) ^ 1) and (res2 ^ 0):
            return True
        else: 
            return False	

    def is_gained(self, iteration):
        if iteration<1 :
            return False
        res=self.results
        if iteration==1:
            res2 = self.Ag_breedC
        else:
            res2 = (res >> (iteration-2))
        if ((res >> (iteration-1)) ^ 0) and (res2 ^ 1):
            return True
        else: 
            return False

    
    def is_regained(self, iteration):
        if iteration<2 :
            return False
        if self.is_gained(iteration=iteration):
            if iteration==2:
                res=self.Ag_breedC
            else:
                res=(self.results >> (iteration-3))
            if (res ^ 0):
                return True
            else: 
                return False
        else: return False


    def is_true(self, iteration): #return true if Breed_C for iteration
        if (iteration < 0) or (iteration > 15):
            return False
        elif iteration==0:
            if self.Ag_breedC==True: return True
            else: return False
        else:
            res=self.results
            
            if ((res >> (iteration-1)) ^ 0): return True
            else: return False


    def run(self, brand_factor): 
        try:
            self.results=0
            for i in range(1, 16):
                if self.auto_renew==True:
                    if self.Ag_breedC==True:
                        self.results=65535
                    else:
                        self.results=0
                    return True
                else:
                    rand=random.random() * 3
                    affinity = self.Payment/self.attribute_price + (rand * self.attribute_promotion * self.inertia_switch)
                    if (i==1): breed=self.Ag_breedC
                    else:
                        res = self.results
                        
                        breed=bool((res >> (i-2)) ^ 0)
                    #if (breed==True and affinity<(self.social_grade * self.attribute_brand)): #for iteration i, set results on 0 -> we do nothing since self.results = 0 already for this 

                    if (breed==False and affinity<(self.social_grade * self.attribute_brand * brand_factor)): #for iteration i, set results on 1
                        self.results = self.results + 2**(i-1)
            return True    
        except:
            return False        


