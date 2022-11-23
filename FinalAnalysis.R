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
# lin <- lm(IP_MOR~., data =data1)
lin <- lm(IP_MOR~average_radius_knot+dist_brd_pith+X2+X15+X17+X19, data =data1)
summary(lin)

data2 <- data %>% select(X2,X15,X17,X19,average_radius_knot,Tot_area_knots,dist_brd_pith,n_knots)
colnames(data2)<-c("hw_dens","eccentr","integral_weight","ext_diam_avg","avg_radius_knot","Tot_area_knots","dist_brd_pith","n_knots")
summary(data2)
res<- cor(data2,use="complete.obs")
res2 <- rcorr(as.matrix(data2))
res2
# flattenCorrMatrix(res2$r, res2$P)
symnum(res, abbr.colnames = FALSE)
corrplot(res, type = "upper", order = "hclust", 
         tl.col = "black", tl.srt = 45,number.cex = 0.1,tl.cex=0.5)

