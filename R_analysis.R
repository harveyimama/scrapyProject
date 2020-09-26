###################################
# Harvey Imama
#Scarpy project Multiple linear regression Analysis
##################################

#import all required Libraries
library(caret)
library(car) 
library(MASS)

#Read file extracted from https://nigeria.opendataforafrica.org
d = read.csv('scrapyProject/data.csv')

##############
#Data cleaning
#############

#function to remove commas from numeric feilds and make them truly numeric
convert.numeric <- function(x){
  return (as.numeric(gsub(',','',x)))
}

#apply numeric converter to dataset
d= sapply(d,convert.numeric)

#get a quick view of dataset
summary(final.data )

#Take care of missingness using median inpute
pre = caret::preProcess(d, method = "medianImpute") 
d= predict(pre, d)

#convert to dataframe
final.data =  as.data.frame(d)

#View summary standard deviation and see what features correlate
summary(final.data )
sapply(final.data , sd)
cor(final.data )
plot(final.data)

#build model based on all data
model.sat= lm(literacy_rate ~ ., data = final.data)
summary(model.sat)
plot(model.sat)
influencePlot(model.sat)
vif(model.sat)
avPlots(model.sat)

#Early_marriage  is taken out because of high p-value and 
# almost flat line on the avplot 

model.feature.removal.1= lm(literacy_rate ~ . - early_marriages, data = final.data)
summary(model.feature.removal.1)
plot(model.feature.removal.1)
influencePlot(model.feature.removal.1)
vif(model.feature.removal.1)
avPlots(model.feature.removal.1)

#gdp  is taken out because of high p-value and 
# high vif value

model.feature.removal.2= lm(literacy_rate ~ . - early_marriages -gdp, data = final.data)
summary(model.feature.removal.2)
plot(model.feature.removal.2)
influencePlot(model.feature.removal.2)
vif(model.feature.removal.2)
avPlots(model.feature.removal.2)

#land area is taken out because of high p-value and 
# almost flat line on the avplot 

model.feature.removal.3= lm(literacy_rate ~ . - early_marriages -gdp - land_area, data = final.data)
summary(model.feature.removal.3)
plot(model.feature.removal.3)
influencePlot(model.feature.removal.3)
vif(model.feature.removal.3)
avPlots(model.feature.removal.3)

# Unempoyment rate is taken out because of high p-value and 
# almost flat line on the avplot 

model.feature.removal.4= lm(literacy_rate ~ . - early_marriages -gdp - land_area - unemployment_rate, data = final.data)
summary(model.feature.removal.4)
plot(model.feature.removal.4)
influencePlot(model.feature.removal.4)
vif(model.feature.removal.4)
avPlots(model.feature.removal.4)

#cheking AIC and BIC to see how the models perform next to each other
AIC(model.sat,model.feature.removal.1,model.feature.removal.2
    ,model.feature.removal.3,model.feature.removal.4) 

BIC(model.sat,model.feature.removal.1,model.feature.removal.2
    ,model.feature.removal.3,model.feature.removal.4) 

#stepwise analysis to see if it confirms analysis done above
model.empty = lm(literacy_rate ~ 1, data = final.data) 
model.full = lm(literacy_rate ~ ., data = final.data) 
scope = list(lower = formula(model.empty), upper = formula(model.full))
 
forwardAIC = step(model.empty, scope, direction = "forward", k = 2)
backwardAIC = step(model.full, scope, direction = "backward", k = 2)
bothAIC.empty = step(model.empty, scope, direction = "both", k = 2)
bothAIC.full = step(model.full, scope, direction = "both", k = 2)

# summary shows same behavior as our 4th model which had an R sqaure 
#value of 0.62 and p-value of 4.524e-07
summary(forwardAIC)
summary(backwardAIC)
summary(bothAIC.empty)
summary(bothAIC.full)

forwardBIC = step(model.empty, scope, direction = "forward", k = log(50))
backwardBIC = step(model.full, scope, direction = "backward", k = log(50))
bothBIC.empty = step(model.empty, scope, direction = "both", k = log(50))
bothBIC.full = step(model.full, scope, direction = "both", k = log(50))

summary(forwardBIC)
summary(backwardBIC)
summary(bothBIC.empty)
summary(bothBIC.full)

#creating test data to test teh model
testdata =  data.frame(gdp_per_capital = c(10.5, 9.5, 2.5),
                       dollar_per_day = c(30.5, 47.5, 79.5),
                       population_density = c(175, 355, 875),
                       population = c(7500567, 5547565, 1212985))

#predict literacy rates based on test data 
predict(forwardAIC, testdata, interval = "confidence") 

predict(forwardAIC, testdata, interval = "prediction") 


