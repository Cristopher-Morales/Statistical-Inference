library(data.table, pos=18)
path<-"C:/Users/20215667/OneDrive - TU Eindhoven/Desktop/AjusteDistribucionDiscreta.csv"
  
# reading contents of csv file 
content <- read.csv(path) 
# save to RData format
save(content, file = "C:/Users/20215667/OneDrive - TU Eindhoven/Desktop/AjusteDistribucionDiscreta.RData")
# load RData file
load("C:/Users/20215667/OneDrive - TU Eindhoven/Desktop/AjusteDistribucionDiscreta.RData")
# data frame that containes number of clients
x<- content[,"Cantidad.de.Clientes", drop=FALSE]
# data frame that conaints observed frecuency
n_obs<- content[, "Frecuencia", drop=FALSE]
# estimating lambda observed
lambda_obs<- sum(x*n_obs)/sum(n_obs)
print(lambda_obs)
# computing expected probabilities assuming poison distribution from 0 to 4
p<- 
local({
  .Table <- data.frame(Probability=dpois(0:4, lambda=lambda_obs))
  print(.Table)
})
# adding last column for x=5 as 1 - sum(probailities), probabilities must sum 1.0
len <- length(p)
p<-rbind(p, c(1.0-sum(p)))
#visualize p
p
# check that probabilities sum 1
result<- sum(p)
result
# transform data frame to vectors
n_obs<-c(unlist(n_obs))
p<-c(unlist(p))
# fit chisquare test
chi_square_test <- chisq.test(x = n_obs, p = p)
# check preliminary results, note that the degrees of freedom df=5, but it should be 4 because we estimated lambda!!
chi_square_test
# correct degrees of freedom to 4 and update p-value
chi_square_test$parameter <- c(df=4)
chi_square_test$p.value <- pchisq(chi_square_test$statistic,df=chi_square_test$parameter,
      lower.tail=FALSE)
# output chi-square test
chi_square_test

