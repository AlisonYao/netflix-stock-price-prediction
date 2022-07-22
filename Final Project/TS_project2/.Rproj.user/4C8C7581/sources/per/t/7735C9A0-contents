# read file & check head
res = scan("/Users/zhuang/Desktop/TS_project2/RES.txt", what="list")
head(res)

# clean up data & convert data type
res = res[-c(1,2)]
res = as.numeric(res)
head(res)

# check different ARCH models
library(tseries)
for (i in 1:10){
  print(paste0('model ARCH(', i, ')'))
  model = garch(res, c(0,i), trace=F)
  print(summary(model))
  print(logLik(model))
}

# ARCH(0) model has to be manually calculated
# model = garch(res, c(0,0), trace=F) is going to give an error
N = 4989
print(paste0('log Lik.', -0.5 * N * (1 + log(2 * pi * mean(res ^ 2)))))

# compared with GARCH(1,1) model
model=garch(res,c(1,1), trace=F)
print(summary(model))
print(logLik(model))

# calc h_t
ht = model$fit[,1]^2
ht[1:5] # has NA
# ht = ht[-c(1)]
write(c('ht', '*', ht), '/Users/zhuang/Desktop/TS_project2/htfile.txt', 1)
ht = scan("/Users/zhuang/Desktop/TS_project2/htfile.txt", what="list")
