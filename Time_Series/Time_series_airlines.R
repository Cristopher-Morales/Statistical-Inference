# load library needed for time series
library(fpp2)
# load data set
load("C:/Users/20215667/OneDrive - TU Eindhoven/Desktop/time series airlines/airline.RData")
# create time series object
ts.work<-ts(airline$passenger, start=c(1949,1), frequency=12)
# plot time series to perform exploratory data analysis
autoplot(ts.work, ylab = "Number of passengers x 1000", xlab="Time [years]")
# display autocorrelation and partial autocorrelation plots: significant trend
ggtsdisplay(ts.work, ylab = "Number of passengers", xlab="Time [years]")
# plot time series analysis per year along months to visualiza seasonaly effect
ggseasonplot(ts.work,ylab= "Number of passengers",season.labels=TRUE,year.labels=TRUE,col=rainbow(12))
# visualize time series per months 
ggmonthplot(ts.work, ylab = "Number of passengers")
# as trend is significant, we remove trend using first order differencing
ts.work.d1 <- diff(ts.work,differences=1)
# plot first order differencing
ggtsdisplay(ts.work.d1,ylab="first differencing")
# we can compute the number of differencing needed for the current time series
ndiffs(ts.work)
# the ouput is 1, so only one differing operator is needed
# now we can decompose the time series assuming seasonal effect is multiplicative
ts.work.deco <- decompose(ts.work,type="multiplicative")
# plotting decomposition
autoplot(ts.work.deco)
# we observe a crearly positve trend in the time series data
# the remainder seems that have a particular structure
autoplot(ts.work.deco$random)
# we can observe high values which maybe by anomalies within the time series
# we plot the acf and pacf of the random error to analysis whether is random
ggtsdisplay(ts.work.deco$random)
# we can forecast that the error is not random
# we can apply seasonal differencing to the data set
ts.work.sd1 <- diff(ts.work,lag=12,differences=1)
ggtsdisplay(ts.work.sd1)
# from acf anf pacf plots, we can observe that the first six component are significant 
# for MA modelling and one at lag 2 for AR modelling, however 
# it might be a mixed effect in both plots
#####################################################################
#####################################################################
# Forecasting Naive method
#####################################################################
#####################################################################
ts.work.snaive <- snaive(ts.work, h=12)
ts.work.snaive
autoplot(ts.work.snaive)
plot(ts.work.snaive)
with(ts.work.snaive,accuracy(fitted,x))
#####################################################################
#####################################################################
# Holt Winters simple exponential smoothing
#####################################################################
#####################################################################
ts.work.ses <- HoltWinters(ts.work,beta=FALSE,gamma=FALSE)
ts.work.ses
autoplot(ts.work.ses$fitted)
plot(ts.work.ses)
with(ts.work.ses,accuracy(fitted,x))
checkresiduals(ts.work.ses)
# test if non zero autocorrelations
ts.work.ses.forecast<-forecast(ts.work.ses, h=10)
ts.work.ses.forecast
autoplot(ts.work.ses.forecast)
Box.test(ts.work.ses.forecast$residuals,lag=20,type="Ljung-Box")
# p-value <0.05, we reject null hypothesis, there there are non zero residuals
# which are significant
# check if residuals distributes normal using shapiro-wilk test
shapiro.test(ts.work.ses.forecast$residuals)
# p_value>0.05, do no reject null hypothesis, residuals belong to a normal distribution
#
###########################################################################
###########################################################################
# Holt Winters simple exponential smoothing with multiplicative seasonality
###########################################################################
###########################################################################
ts.work.hw <- HoltWinters(ts.work,seasonal = "multiplicative")
ts.work.hw
autoplot(ts.work.hw$fitted)
plot(ts.work.hw)
with(ts.work.hw,accuracy(fitted,x))
checkresiduals(ts.work.hw)
# test if non zero autocorrelations
ts.work.hw.forecast<-forecast(ts.work.hw, h=10)
ts.work.hw.forecast
autoplot(ts.work.hw.forecast)
Box.test(ts.work.hw.forecast$residuals,lag=20,type="Ljung-Box")
# p-value <0.05, we reject null hypothesis, there there are non zero residuals
# which are significant
# check if residuals distributes normal using shapiro-wilk test
shapiro.test(ts.work.hw.forecast$residuals)
# p_value<0.05, reject null hypothesis, residuals do not belong to a normal distribution
###########################################################################
###########################################################################
# automatic exponential smoothing
#####################################################################
#####################################################################
ts.work.ets <- ets(ts.work)
ts.work.ets
autoplot(ts.work.ets)
accuracy(ts.work.ets)
checkresiduals(ts.work.ets)
# p<0.05, reject null hypothesis, non zero residuals in autocorrelation are significant
shapiro.test(ts.work.ets$residuals)
# p>0.05, not reject null hypothesis, residuals are normal distributed
# forecast
ts.work.ets.forecast <- forecast(ts.work.ets,h=10)
autoplot(ts.work.ets.forecast)
####################################################################################
############################ save plots ############################################
####################################################################################
plots.dir.path <- list.files(tempdir(), pattern="rs-graphics", full.names = TRUE)
plots.png.paths <- list.files(plots.dir.path, pattern=".png", full.names = TRUE)
plots.dir.path
for (i in 1:length(plots.png.paths)) {
  file.copy(from=plots.png.paths[i], to="C:/Users/20215667/OneDrive - TU Eindhoven/Desktop/time series airlines")
}
####################################################################################
############################ renaming plots ########################################
####################################################################################
my_path <- "C:/Users/20215667/OneDrive - TU Eindhoven/Desktop/time series airlines/"
file_names_old <- list.files(my_path)
for (i in 1:length(file_names_old)) {
  if (file_names_old[i]!= 'Time_series_airlines.R' & file_names_old[i]!='airline.RData'){
    file_name_new <- paste0("Plots_No_",i,".png")
    file.rename(paste0(my_path, file_names_old[i]),paste0(my_path, file_name_new))
  }
}
