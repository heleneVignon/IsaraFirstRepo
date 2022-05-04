# Exemples
getwd()
x <- c(4,5,7,4,3,9)
x
x*2
mean(x)
y <- x*3+2
y

plot(x,y)

read.table("casino.csv")
casino <- read.csv2("casino.csv")
casino[1,2]
casino

#install.packages("dplyr")
yes
library("dplyr")
library(dplyr)
casino
filter(casino, Couleur_voiture=="bleu")
select(casino,Score,Gain)
# avoir les lignes bleus 
casino[casino$Couleur_voiture=='bleu',1:2]
# que les colonnes score et gain 

#avec dplyr
casino_bleu <- filter(casino, Couleur_voiture=="bleu")
select(casino_bleu,Score,Gain)

casino %>%
  filter(casino, Couleur_voiture=="bleu")%>%
  select(Score,Gain)%>%
  mutate(rapport=Gain/Score)

