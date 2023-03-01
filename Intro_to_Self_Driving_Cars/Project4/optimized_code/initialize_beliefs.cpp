#include "headers/initialize_beliefs.h"

using namespace std;

// OPTIMIZATION: pass large variables by reference
vector<vector<float>> initialize_beliefs(int height, int width) {

	// OPTIMIZATION: Which of these variables are necessary?
	// OPTIMIZATION: Reserve space in memory for vectors
  	float prob_per_cell = 1.0 / float(height * width);
  
  	vector<vector<float>> newGrid;
	vector<float> newRow;
  
  	newGrid.reserve(height);
  	newRow.reserve(width);

  	// OPTIMIZATION: Is there a way to get the same results 	// without nested for loops?
	for (int i = 0; i < width; i++) {
		newRow.push_back(prob_per_cell);
	}

	for (int i = 0; i < height; i++) {
		newGrid.push_back(newRow);
	}
  
	return newGrid;
}