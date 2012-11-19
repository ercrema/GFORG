

groupFormationModel<-function(p,Q=1,M=5,maxN=10,C=0.2)
{

greenstamps<-function(x,Q=1,M,maxN)
{
B=1/(maxN-M)^2
return(Q-B*(x-M)^2)
}
	
#initialise the model:
groupSize<-numeric()
averageGroupfitness<-numeric()
groupSize[1]=1
averageGroupfitness[1]=greenstamps(x=1,Q=Q,M=M,maxN=maxN)
doreject=TRUE
T=maxN
for (t in 1:(T-1))
  {
    doreject=FALSE
    currentFitness<-greenstamps(x=groupSize[t],Q=Q,M=M,maxN=maxN)
    futureFitness<-greenstamps(x=groupSize[t]+1,Q=Q,M=M,maxN=maxN)
    cooperationFitness<-currentFitness-C


    choice<-runif(groupSize[t])<p #decision of each member of the group

    if (any(choice)){doreject=TRUE}  #accept the new member if at least one individual accepts

#calculate fitness of the group members:

    #if the new member is rejected
    if (doreject==TRUE){
      collaborators<-sum(choice)*cooperationFitness #fitness of the cooperators (this can easily be changed so that they share the cost)
      defectors<-(groupSize[t]-sum(choice))*currentFitness #fitness of the defectors
      averageGroupfitness[t]=(collaborators+defectors)/groupSize[t]
      groupSize[t+1]=groupSize[t] #groupsize is unchanged
    }
    #if the new member joins the group
    if (doreject==FALSE){
      groupSize[t+1]=groupSize[t]+1 #groupsize is updaed
      averageGroupfitness[t]<-futureFitness #fitness of everybody
    }   
  }

return(mean(averageGroupfitness))
}




res<-matrix(NA,101,100)
ps<-seq(0,1,0.01)

plot(0,0,xlim=c(0,1),ylim=c(0,1),type="n",xlab="p",ylab="mean fitness")

X<-numeric()
Y<-numeric()

  for (x in 1:101)
  {
res[x,]<-replicate(100, groupFormationModel(p=ps[x],M=5,maxN=10))
points(rep(ps[x],100),res[x,],pch=20,col=rgb(0,0,0,90,maxColorValue=255))
X<-c(X,rep(ps[x],100))
Y<-c(Y,res[x,])
 }

LL<-loess(Y~X)
lines(ps,predict(LL,ps),col="red",lwd=2)



