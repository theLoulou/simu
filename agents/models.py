from django.db import models
from django.shortcuts import redirect
import csv, copy
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
    results = models.PositiveIntegerField(default=0)


    def is_lost(self, iteration):
        if iteration<1 :
            return False
        res=self.results
        if iteration==1:
            res2 = self.Ag_breedC
        else:
            res2 = (res >> (iteration-2))
        if (1 & ~(res >> (iteration-1))) and (res2 & 1):
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
        if ((res >> (iteration-1)) & 1) and (1 & ~(res2)):
            return True
        else: 
            return False

    
    def is_regained(self, iteration):
        if iteration<2 :
            return False
        if self.is_gained(iteration=iteration):
            if iteration==2:
                if (self.Ag_breedC & 1)==True:
                    return True
                else: 
                    return False
            else:
                if ((self.results >> (iteration-3)) & 1):
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
            res=int(self.results)
            if ((res >> (iteration-1)) & 1): return True
            else: return False


    def run(self, brand_factor): 
        try:
            self.results = 0
            if self.auto_renew==True:
                    if self.Ag_breedC==True:
                        self.results = 65535
                    else:
                        self.results = 0
                    self.save()
                    return True
            answer=0
            breed=self.Ag_breedC
            pay = self.Payment
            ap= float(self.attribute_price)
            app = float(self.attribute_promotion)
            ifs = self.inertia_switch
            sg = self.social_grade
            ab = float(self.attribute_brand)
            bf = float(brand_factor)
            for i in range(1, 16):
                    rand=random.random() * 3
                    affinity = (pay/ap) + (rand * app * ifs)
                    if (i!=1): 
                        breed=((answer >> (i-2)) & 1)
                    if (breed==False and affinity<(sg * ab * bf)): #for iteration i, set results on 1
                        answer = answer + 2**(i-1)
            self.results = int(answer)
            self.save()
            return True   
        except:
            return redirect('errorDB')        


