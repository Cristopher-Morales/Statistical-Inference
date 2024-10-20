path<-"C:/Users/20215667/OneDrive - TU Eindhoven/Desktop/AjusteDistribucionContinua.csv"
# reading contents of csv file 
content <- read.csv(path) 
# save to RData format
save(content, file = "C:/Users/20215667/OneDrive - TU Eindhoven/Desktop/AjusteDistribucionContinua.RData")
# load RData file
load("C:/Users/20215667/OneDrive - TU Eindhoven/Desktop/AjusteDistribucionContinua.RData")
# data frame that conaints observed frecuency
n_obs<- content[, "frecuencia.observada", drop=FALSE]
n_obs
# compute probilities under the assumption of exponential distribution, note that lamba=1/2.5
p<-pexp(c(1,2,3,4,5), rate=1/2.5, lower.tail=TRUE)
# Create vector of probabilities of classes p[i]=Prob(t_{i-1}<=T<=t_{i})
p_new<-numeric(length(p)+1)
p_new
for (i in 1:6){
if (i==1) {p_new[i]=p[i]}
else if (i>=2 & i<=5){p_new[i]=p[i]-p[i-1]}
else {p_new[i]=1.0-p[i-1]}
}
#print vector with class probabilitites
p_new
# check that their sum is 1.0
result<-sum(p_new)
result
# fit chisquare test
chi_square_test <- chisq.test(x = n_obs, p = p_new)
# check preliminary results
chi_square_test

