# kMeans_From_Scratch

I implemented the k-means clustering algorithm on Python. This is the most common unsupervised algorithm used to assign each data point to a class when the training data doesn’t include any classes or labels. The algorithm generates its own classes which are called clusters. After deciding on the k value, the first step is to randomly choose k number of centers. Then all data points gets assigned to the closest cluster. Afterwards, the new center of each cluster is computed by calculating the average location of every data point in the cluster. The last two steps are repeated until the centers stop changing locations.

Additionally, the program compares my k-means clustering algorithm with scikit-learn's implementation. There is no difference in how the algorithms work, however you can get different results every time you run the program because of the random initial cluster centers.

# Objective Function - SSE

Accuracy of the algorithm cannot be computed in unsupervised algorithms since there are no classes or labels in the datasets. However, we can evaluate the quality of the clusters with an objective function. This function is called the sum of squared estimate of errors (SSE). It's basically the sum of all data points’ squared distances to their corresponding cluster center. In my implementation, I stopped the algorithm whenever two consecutive iterations resulted in objective function values with a difference lower than 0.1. I could’ve stopped it when the centers stopped moving completely, however this might make the algorithm run for too many iterations, taking too much time.

# Plotting Results

You can see the results of the program for various k values and datasets.

<img width="940" alt="image" src="https://user-images.githubusercontent.com/54302889/146196795-27cac3e0-b9ac-4c8b-9894-bcacd5dfaa2e.png">

<img width="946" alt="image" src="https://user-images.githubusercontent.com/54302889/146196857-944d77ae-d7fd-4d4f-9619-cba9bd6a4d26.png">

<img width="914" alt="image" src="https://user-images.githubusercontent.com/54302889/146196891-b27d8321-e343-4475-9849-f6f02b833f66.png">

<br>

<br>

<img width="954" alt="image" src="https://user-images.githubusercontent.com/54302889/146200392-10dcfa70-896d-4d7d-ae15-1798247987ef.png">

<img width="954" alt="image" src="https://user-images.githubusercontent.com/54302889/146201855-1dd86413-c987-42e6-a652-4c044ba42a10.png">

<img width="909" alt="image" src="https://user-images.githubusercontent.com/54302889/146202421-ae70ec8c-f7ca-4b2a-abaf-b16ebde83f66.png">

<br>

<br>

<img width="973" alt="image" src="https://user-images.githubusercontent.com/54302889/146202638-249b1ca0-b586-481c-ae2c-952ab52f1afa.png">

<img width="970" alt="image" src="https://user-images.githubusercontent.com/54302889/146202928-cba39d14-2009-426a-8697-1eebb9dc6cef.png">

<img width="911" alt="image" src="https://user-images.githubusercontent.com/54302889/146232349-989953ce-96d0-4264-983d-b9863a56b692.png">

<br>

<br>

<img width="965" alt="image" src="https://user-images.githubusercontent.com/54302889/146232685-3993249b-a3c2-4039-8356-54e169ae98d6.png">

<img width="968" alt="image" src="https://user-images.githubusercontent.com/54302889/146232881-966cbeaa-a284-46d7-8cba-3cff159952fc.png">

<img width="915" alt="image" src="https://user-images.githubusercontent.com/54302889/146233090-1e98fc4e-1102-4ffc-907f-eddd3426cf0b.png">
