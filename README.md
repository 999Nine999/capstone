# The Slot-ification of Baseball: Creating Increased Gambling Opportunites in America's Pastime
Flatiron Capstone project by Joe Buzzelli


### Items in Repository (still in flux, skeleton outline for now...)
- /data: 
- /presentation_materials:
- README.md: this document outlining the repository
- /Step01
- /Step0X
- /viz
- /images


### Prompt
In DC, sports gambling is poised for rapid growth.  The Council of the District of Columbia’s Act 22-594, the Sports Wagering Lottery Amendment Act, passed on January 23rd, 2019 and it sets the scene for Ted Leonsis to augment his current, sports-centric business operations.  The slot-ification of baseball attempts to establish a baseline for the odds to ultimatly be leveraged in a mobile gambling app.  Most frequently, sports gambling depends on the outcome of a game.  Gambling on a per-pitch basis is a 24,980% increase in gambiling opportunities per MLB season.


### Goal
Create a statistical model that will predict the type of pitch a major leage pitcher will throw with 75% accuracy.


### Results
Current results are disappointing.  After selecting a Gradient Boosting Classifier, the accuracy shrunk from 68% to 48%, the lower end equalling a dummy model that predicts the most frequent picth type (fastball in the case of Max Scherzer, the pither analyzed in this project).


### Methodology
1. Acquired Max Scherzer's 2019 pitch data from baseball savant website
2. Acquired data pertaining to every batter he faced in 2019
3. Cleaned both data sets, created features, then joined both data sets for modeling
4. Conducted eight models to assess performance
5. Best performing model, Gradient Boosting Classifier, performed best
6. After hyperparameter tuning, GBC models is unusable
7. Repeat steps 4, 5, and 6 to find another model
8. Assess performance using cross validation, grid search, and randomized search
9. Integrate best model into a web app


### Next Steps
- Select a new model
- Consider adding more pitchers into the model
- Continue research on piterh strategies for pitch selection to better integrate applicable windows of time
	- For example, do pitchers typically change their strategies by at bats, innings, games, series?