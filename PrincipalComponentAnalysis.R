
path<- ("C:/Users/20215667/Downloads/DataSetPCA.csv")
dataPCA<-read.csv(path)
dataPCA
save(dataPCA, file = "C:/Users/20215667/OneDrive - TU Eindhoven/Desktop/DataSetPCA.RData")

load("C:/Users/20215667/OneDrive - TU Eindhoven/Desktop/DataSetPCA.RData")
summary(dataPCA)
# compute correlation matrix
Correlation_Matrix = cor(dataPCA[,c("Empresas","Neg..Temp","Poblacion","Precip","SO2","Viento")], use="complete")
Correlation_Matrix
# Scatter plot between variables
scatterplotMatrix(~Empresas+Neg..Temp+Poblacion+Precip+SO2+Viento, regLine=FALSE, smooth=FALSE, 
  diagonal=list(method="density"), data=dataPCA)
# principal component analysis
data.pc <- princomp(~Empresas+Neg..Temp+Poblacion+Precip+SO2+Viento, cor=TRUE, data=dataPCA)
cat("\nComponent variances:\n")
# compute the standard deviations(unscale) given by each component
data.pc$sd^2
cat("\n")
summary(data.pc, loadings=TRUE)
# compute eigenvectors and eigen values which coincide with the correlation matrix and unscaled standard deviations
cat("\nCompute eigenvector and eigenvalues") 
eigen(Correlation_Matrix)
# computing scores
data.pc$scores[,1:3]
SO2<-unlist(file["SO2"])
# plot SO2 with respect to the three principal components
par(mfrow=c(1,3))
plot(data.pc$score[,1],SO2,xlab="PC1")
plot(data.pc$score[,2],SO2,xlab="PC2")
plot(data.pc$score[,3],SO2,xlab="PC3")
# Fitting regresion model
RegressionModel<-lm(SO2~data.pc$scores[,1]+data.pc$scores[,2]+data.pc$scores[,3])
summary(RegressionModel)
# Visualize values residuals between predicted and actual values
par(mfrow=c(1,1))
plot(fitted(RegressionModel), residuals(RegressionModel))
#add horizontal line at 0
abline(h = 0, lty = 2)
# Fitting regresion model only using first principal component
RegressionModel2<-lm(SO2~data.pc$scores[,1])
summary(RegressionModel2)
# plot SO2 with respect to the first principal component
par(mfrow=c(1,1))
plot(data.pc$score[,1],SO2,xlab="PC1")

