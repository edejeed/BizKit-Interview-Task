# BizKit-Interview-Task


#Improve the Matching Algorithm

The current algorithm has a time complexity of O(n * m),this approach could become slow if fave_numbers_1 and fave_numbers_2 have a large number of elements.

You can optimize the matching algorithm using sets, which provide faster lookups and improve the overall efficiency. 
This modification converts fave_numbers_1 into a set, which has an average time complexity of O(1) for lookups. Therefore, the overall time complexity of this optimized algorithm becomes O(m), where m is the length of fave_numbers_2. This will significantly improve the speed of your matching algorithm, especially when dealing with larger lists of favorite numbers. However, he trade-off here is memory usage; using sets requires more memory compared to lists. 


# Bonus Challenge

To return the search results sorted based on the priority of how they were matched (id, name, age, occupation), you can modify the search_users function to include a sorting mechanism. 
