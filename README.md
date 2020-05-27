# The Slot-ification of Baseball: Predicting the Next Pitch in America's Pastime
Flatiron Capstone project by Joe Buzzelli


### Items in Repository (still in flux, skeleton outline for now...)
- /data: Please note, due to size constraints, this repo does not include the data.  The notebooks in steps 1 and 2 will scrape the data for you though.  The folders in the data folder is purely for directory references if you wish to clone the repo and work with the notebooks.
- /presentation_materials: The final and interim presenations of this project
- README.md: this document outlining the repository.
- /Step01_pitcher_data_acquisition_cleaning_EDA: includes all steps required to acquire and clean pitcher data.
- /Step02_batter_data_aquisition_cleaning_EDA: inlcudes all steps required to acquire and clean batter data as well as a batter kmeans cluster analysis.
- /Step03_join_batter_data_to_pitcher_data: includes merging of pitcher and batter data.
- /Step04_model_preprocessing: includes data transformations and train, test, split.
- /Step05_model_selection: includes the assessment of eight models with their default settings, ultimatly selected Random Forest
- /Step06_model_assessment: assesses the model's predictions versus that of a naive model (predicting each pitcher's most frequent pitch).
- /viz: Folder where visualizations are saved.  Repo only contains tuned Random Forest confusion matrix.
- /to_add_tecnical_notebook that hos code highlights


### Prompt
In DC, sports gambling is poised for rapid growth.  The Council of the District of Columbia’s Act 22-594, the Sports Wagering Lottery Amendment Act, passed on January 23rd, 2019 and it sets the scene for Ted Leonsis to augment his current, sports-centric business operations.  The slot-ification of baseball attempts to establish a baseline for the odds to ultimatly be leveraged in a mobile gambling app.  Most frequently, sports gambling depends on the outcome of a game.  Gambling on a per-pitch basis is a 24,980% increase in gambiling opportunities per MLB season.


### Goal
Create a statistical model that will predict the type of pitch a major leage pitcher will throw that outperforms the naive approach of predicting a pitcher's most frequent pitch.


### Data
The data for this experiment derives from the 2019 MLB season and includes:
- Every pitch thrown for pitchers that threw at least 750 pitches
- Running batter statistics for each batter they faced
- A kmeans cluster analysis on the batters added as a feature


### Results
After selecting and tuning the Random Forest model, its predictions outperform the naive approach for fastballs and change-ups.  The naive approach does better with movment pitches (all pitches that are neither fastballs or change-ups).  Given this binning of seven pitches into one group, this was expected and prediciting additional granularity is of interest for future experiments.


### Methodology
1. Acquired 2019 pitch data from baseball savant website for all pitchers who threw 750 pitches or more
2. Acquired data pertaining to every batter these batters faced in 2019
3. Cleaned both data sets, created features, then joined both data sets for modeling
4. Conducted eight models to assess performance
5. Selected best performing model, Random Forest, based on cross validation scores of default models
6. Conducted hyperparameter tuning
7. Assessed model's predicitons against the naive approach of predicting the pither's most frequent pitch


### Next Steps
- Expand modeling to address predicinting different types of movement pitches such as sliders, curveballs, and forkballs
- Add historic pitch selections to the model per pitcher including the last pitch type they threw, as well as the pitch types they selected per scenario per batter historically
- Add data from 2015 through 2019 rather than only 2019