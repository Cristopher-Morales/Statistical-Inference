# create contingecy table 
.Table <- matrix(c(28,53,30,45,64,24,35,20,13), 3, 3, byrow=TRUE)
# provide row and columns names
dimnames(.Table) <- list("Resultado PSU"=c("Bueno", "Regular", "Malo"), 
  "Tipo preuniversitario"=c("No preuniversitario", "Preuniversitario normal", "Preuniversitario intensivo"))
# print table
.Table  # Counts
# perfom chi-square test for statistical independency 
.Test <- chisq.test(.Table, correct=FALSE)
# print results
.Test
#save table in RData format for future used
save(.Table, file = "C:/Users/20215667/OneDrive - TU Eindhoven/Desktop/ChiCuadradoContingencia.RData")
# in case you want to reload the table, follow this routine
load("C:/Users/20215667/OneDrive - TU Eindhoven/Desktop/ChiCuadradoContingencia.RData")
.Table <- as.data.frame(.Table)
names(.Table) <- make.names(names(.Table))

