d = read.csv('../scrapyProject/data.csv')

d$dollar_per_day = as.numeric(d$dollar_per_day)
summary(d)
