# Analysis (60 points)

The analysis portion of this assignment is similar to the analysis in part 1. To receive all points for this portion of the assignment, you need to:
- Choose and perform the analysis by selecting from the options below. You can mix and match sub-options within each option, so long as the total points add up to 60.
- Report all your findings, supplemented by visual aids where appropriate.
- Provide clear and concise reasoning when suggesting improvements or use-cases.
- Limit your report to **500 words** (tables and visual aids excluded).

## **Option 1: Sensitivity Analysis (60 points)**

### **Overview**
Assess the robustness of your models by introducing different levels of variability to understand how external changes affect your model's performance.

### **Instructions**
1. **Data Noise (20 points)**
   - Introduce random noise to your dataset. Methods include:
     * Randomly swapping words within questions or documents.
     * Introducing typographical errors.
     * Adding or removing words from documents.
     * etc.
   - Report changes in the performance of each model (DenseEncoder, SparseEncoder, CrossEncoder) on the noisy data.
   - Do not retrain the models for this part.
2. **Dataset Size (20 points)**
   - Test your models using subsets of your dataset (e.g., 25%, 50%, 75%).
   - Analyze how model performance (MRR@10, R@1000) changes with varying dataset sizes.
3. **Your Creativity (20 points)**
   - Propose a third type of variability to test your models.
   - Justify the importance of testing this variability and design the experiment.
   - Report changes in performance for each model (DenseEncoder, SparseEncoder, CrossEncoder, and your variant) due to this variability.
   - Discuss the implications of your findings.

### **Example Results Table**

| Model | MRR@10 (Original) | R@1000 (Original) | MRR@10 (Noisy) | R@1000 (Noisy) | MRR@10 (Reduced Data) | R@1000 (Reduced Data) |
|-------|-------------------|-------------------|----------------|----------------|------------------------|------------------------|

---

## **Option 2: Improving ranking quality (60 points)**

### **Overview**
Explore ways to improve ranking quality as measured by relevance metrics. 

### **Instructions**
1. **Hyperparameters and design choices (20 points)**
   - List 10 hyperparameters or design choices in your implementation. No credit will be awarded for hyperparams/choices that are already configurable arguments like `--train_batch_size` and `--pretrained`.
   - Choose a precision-oriented metric and a recall-oriented metric to improve in the next parts. For each, describe a scenario where the metric should be preferred over other choices.
2. **Improving a precision-oriented metric (20 points)**
   - Propose an approach to improve the precision-oriented metric you selected and justify your choice of this approach. You may use any type of neural IR model that you implemented in the assignment. To receive full credit, your approach cannot simply be a straightforward hyperparameter modification (e.g., training for longer).
   - Implement the approach and save the results to `output/your_creativity/test_run_P.trec`. This file will be used to populate the leaderboard.
   - Evaluate this run file using the metric you selected. Compare the results to the base model you're improving and discuss whether your approach was successful. To receive full credit, some improvement is necessary.
3. **Improving recall (20 points)**
   - Propose an approach to improve the recall-oriented metric you selected and justify your choice of this approach. You may use any type of neural IR model that you implemented in the assignment. To receive full credit, your approach cannot simply be a straightforward hyperparameter modification (e.g., training for longer).
   - Implement the approach and save the results to `output/your_creativity/test_run_R.trec`. This file will be used to populate the leaderboard.
   - Evaluate this run file using the metric you selected. Compare the results to the base model you're improving and discuss whether your approach was successful. To receive full credit, some improvement is necessary.

---

## **Option 3: Error Analysis (60 points)**

### **Overview**
Examine the types of errors made by the models, understand their underlying causes, and propose rectifications.

### **Instructions**
1. **Model Disagreements (20 points)**
   - Identify disagreements among the DenseEncoder, SparseEncoder, and CrossEncoder using the following steps:
     * Run identical sets of queries through all three models and identify queries where the top results differ.
     * Create a dataset containing these differing queries and their corresponding results.
     * Conduct feature analysis to identify common features or characteristics among the differing results.
   - Analyze the reasons and implications for such disagreements.
2. **Error Categorization (20 points)**
   - Categorize the errors made by the models as follows:
     * Take a random sample of queries where models produced incorrect results.
     * Develop at least three distinct types of error categories (e.g., 'semantic misunderstanding,' 'keyword mismatch,' 'out-of-context retrieval').
     * Classify incorrect queries based on these categories.
3. **Reasoning and Improvements (20 points)**
   - Discuss potential causes for each identified error type.
   - Suggest possible model or data modifications to reduce these errors.

---
