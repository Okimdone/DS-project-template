```
To reproduce a Data Science experiment, we need to trak:
- Code
- DataSet
- Results (Metrics/Plots)
- Environment/Dependencies
.
├── README.md
├── config/       	<- any config files (including model [hyper-]parameters)
├── docker/       	<- docker images for running project inside containers
├── data/         	 <- contains the (raw/processed) data used for model training
├── models/       	 contains the trained models
├── reports/      	 contains charts and data of the performance of the saved models
├── notebooks/    	<- jupyter notebooks - excluded from GIT history
└── src/          	<- move main functions to .py modules in src/ directory
    ├── pipelines/	<- contains the main pipelines from data ingestion the model training
    ├── data/     	<- data prepare and/or preporcess
    ├── features/ 	<- code to compute featurees
    ├── train/    	<- train model stage code
    ├── evalute/  	<- evaluating model stage code
    ├── report/   	<- visualisation ( used in notebooks )
    └── utils/    	<- contains any defined utility function (Ex: logging)
├── dvc.yaml
├── build.sh
└── run.sh
```
