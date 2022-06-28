```
.
├── README.md
├── config	<- any config files
├── docker	<- docker images for running project inside containers
├── data | <- contains the (raw/processed) data used for model training
├── models | contains the trained models
├── reports | contains charts and data of the performance of the saved models
├── notebooks	<- jupyter notebooks for exploratory analysis and explanation - excluded from GIT history
└── src 	<- Move main functions to .py modules in src/ directory
    ├── data	<- data prepare and/or preporcess
    ├── evalute	<- evaluating model stage code
    ├── features<- code to compute featurees
    ├── report	<- visualisation ( used in notebooks )
    └── train	<- train model stage code
├── build.sh	
└── run.sh
```
