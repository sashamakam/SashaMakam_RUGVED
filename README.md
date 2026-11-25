# RUGVED Python, computer vision, and ML exercises

Python practice tasks, exploratory data analysis, an OpenCV tracking exercise, and a regression experiment.

| Folder | Contents |
| --- | --- |
| [task1-pythonbasics](task1-pythonbasics) | Standalone Python exercises. |
| [task2-pythonlibraries](task2-pythonlibraries) | A Jupyter notebook for analysis and visualization with pandas and Matplotlib. |
| [task3-OpenCV](task3-OpenCV) | Green-ball tracking using HSV thresholding, contours, and a trajectory trail. |
| [task4-EDAandML](task4-EDAandML) | Vehicle CO₂ emissions regression. The saved 80/20 split reports a test MAE of 3.07 g/km. |

Run a standalone exercise with `python3 task1-pythonbasics/quest1.py`. For the notebooks and OpenCV exercise, install `jupyter numpy pandas matplotlib seaborn scikit-learn opencv-python` in a virtual environment.

The analysis notebooks expect input CSVs, and the tracking script expects `Ball_Tracking.mp4` in its working directory. These inputs are not included.
