install.packages("Hmisc")
library(Hmisc)
library(readr)
library(tidymodels)
library(rpart.plot)
library(dplyr)
library(corrplot)

data <- read.csv("final3.csv")

options(max.print=999999)

data1 <- data %>% select(-X,-LogID, -Unnamed..0,-fullId ,-IdLog, -Number, -X4, -X8, -X21, -X22, -X23, -X24)
summary(data1)
lin1 <- lm(IP_MOR~., data =data1)
summary(lin1)
lin2 <- lm(IP_MOR~average_radius_knot+dist_brd_pith+X2+X15+X17+X19, data =data1)
summary(lin2)

fit = rpart(IP_MOR~X1+X2+X3+X5+X6+X7+X9+X10+X11+X12+X13+X14+X15+X16+X17+X18+X19+X20+X25+X26+X27+X28, data =data1)
summary(fit)
# rpart.plot(fit)

data2 <- data %>% select(IP_MOR,X2,X15,X17,X19,average_radius_knot,Tot_area_knots,dist_brd_pith,n_knots)
colnames(data2)<-c("IP_MOR","hw_dens","eccentr","integral_weight","ext_diam_avg","avg_radius_knot","Tot_area_knots","dist_brd_pith","n_knots")
summary(data2)

fit2 = rpart(IP_MOR~hw_dens+eccentr+integral_weight+ext_diam_avg+avg_radius_knot+Tot_area_knots+dist_brd_pith, data =data2)
summary(fit2)
rpart.plot(fit2)


res<- cor(data2,use="complete.obs")
res

res2 <- rcorr(as.matrix(data2))
res2

# symnum(res, abbr.colnames = FALSE)
# corrplot(res, type = "upper", order = "hclust", 
#          tl.col = "black", tl.srt = 45,number.cex = 0.1,tl.cex=0.5)


