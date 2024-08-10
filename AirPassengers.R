# Load dataset AirPassengers in R
AirPassengers <-read.csv('AirPassengers.csv')
head(AirPassengers, 5)
y<-c(AirPassengers[,2])
n<-length(y)
#cat(y,n)
#x<-c(AirPassengers[,1][2:5])
x<-c(1:n)
#cat(x)

# Take first differences to remove the trend 
AirPassengers_1stdiff=diff(y,differences=1)

# Take second differences to remove the trend 
AirPassengers_2stdiff=diff(y,differences=2)

# Filter via moving averages to remove the seasonality 
AirPassengers_ma=filter(y,filter=c(1/24,rep(1/12,11),1/24),sides=2)

# Plots

par(mfrow=c(4,1), cex.lab=1.2,cex.main=1.2)
plot(x,y, xlab = "months", ylab="number of passengers", main="number passengers per month")
plot(AirPassengers_1stdiff,xlab = "months", ylab="difference orden 1", main="First order differences") # plot the first differences (removes trend, highlights seasonality)
plot(AirPassengers_2stdiff,xlab = "months", ylab="difference orden 2", main="Second order differences") # plot the filtered series via moving averages (removes the seasonality, highlights the trend)
plot(AirPassengers_ma, xlab = "months", ylab="Moving averages", main="Moving averages") # plot the first differences (removes trend, highlights seasonality)