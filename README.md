# Roadmap to Data Science and Machine Learning (RDScML)
An exhaustive study guide to learn machine learning concepts from scratch. It focuses on preparing an individual through detailed exploration and hands-on implementation of the concepts. The concepts are to be learned by solving the issues that are brilliantly crafted by experienced personnel. The solutions submitted via pull requests will be reviewed carefully and constructive feedback will be given. Post this, there are three major projects:
1. Great Energy Prediction
2. COVID-19 Visualization
3. Quora Insincere Questions Classification

These projects on solving would reflect the detailed knowledge and understanding of three main data science aspects:

1. Algorithmic Knowledge
2. Building Visual Deliverables
3. Natural Language Processing Applications

## Timeline
The following timeline can be followed by any learner. It is highly recommended to study these topics by reading articles on Medium, Towards Data Science, IEEE research papers and other scholarly articles. Popular YouTube channels can also be followed, like
1. Machine Learning Recipes with Josh Gordon
2. Natural Language Processing Zero to Hero by Laurence Moroney
3. Deeplearning.ai
4. Machine Learning- Andrew Ng, Stanford University (full course)
5. StatQuest with Josh Starmer
Week 1-4 covers the basic prerequisite. This can be skipped if you are not a beginner in this field.

#### Part I
Week 1: Getting started with Python

Week 2: Manipulating data using Pandas and NumPy

Week 3: Data visualisation techniques

Week 4: Concept Application I: Solve the Great Energy Prediction problem statements (perform data exploration only)

#### Part II
Week 5: Probability and Statistics

Week 6: Linear Models

Week 7: Regularisation

Week 8: Concept Application I: Complete solving the Great Energy Prediction problem statement

#### Part III
Week 9: EDA and Feature engineering

Week 10: Classification models

Week 11: Decision Trees

Week 12: Concept Application II: Solve COVID-19 visualisation problem statement

#### Part IV

Week 13: Ensemble methods

Week 14: Clustering Algorithms

Week 15: Support vector machines

Week 16: Introduction to NLP

#### Part V

Week 17: Topic modelling

Week 18: Sentiment analysis

Week 19: Concept Application III: Solve the problem statement on Quora Insincere Questions Classification

Week 20: Concept Application III: Solve the problem statement on Quora Insincere Questions Classification (cont.)

## Contribution Guidelines
To keep the project structure and review process manageable at this initial
stage, please structure your contributions using the following steps:

- Create a directory with your username in the [`dev`](./dev) dir
- Structure your code into one or more Python modules in that directory
    * Code should be well-documented. Each function should include a docstring.
- Include a [Jupyter
  notebook](https://jupyter-notebook.readthedocs.io/en/stable/) that
  demonstrates a run of your code showing
  printed output, a graph, etc.
    * Code cells in the notebook should only call functions defined in your
      modules. Please do not include any actual code logic in the notebook
      itself.
    * The notebooks should be well-documented. Ideally, each code cell should
      be preceded by a Markdown cell describing why you have included the code
      cell. It can also include commments on the output generated, eg.
      describing features of a graph. These text cells should be more
      high-level than actual code comments, describing the narrative or thought
      process behind your contribution.

We request that contributions be structured in this way prior to getting
reviewed. If you make subsequent contributions, you can include them in the same
directory and reuse module code, but each contribution should include a separate
demonstration notebook.

If you wish to build on someone else's contribution, you can import code from
their modules into yours. Please do not submit PRs directly modifying code from
other contributions at this point, unless to resolve errors or typos.
### Issues
Tasks are managed using the [GitHub issue tracker](https://github.com/mozilla/PRESC/issues).

- As issues represent general exploratory tasks at this point, they will
  generally not be assigned to a single person.
- If you want to work on a task, drop a comment in the issue.
- You are welcome to make a contribution to an issue even if others are
  already working on it. You may also expand on someone else's work, eg.
  testing out the methodology with different datasets or models.
- As the project matures, we may start filing targeted issues, eg. to fix
  specific bugs, which will get assigned to specific person
- You are also welcome to contribute your own issues if there is a direction you
  would like to explore relating to the project focus.
### Contributions
Contributions can be made by submitting a [pull request](https://help.github.com/articles/using-pull-requests) against this repository. Learn more about [creating a pull request](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).

- We ask each Uplift participant to make a contribution completing
  [#2](https://github.com/archisha-chandel/RDScML/issues/2) (train and test a
  classification/ regression model). This will help you to become familiar with machine
  learning and the tools if you are not already. Please submit as a PR following
  the [guidelines](#contribution-guidelines) above.
    * This task __must__ be completed in order to be considered as a participant on
      this project
- If you would like initial feedback on your contribution before it is ready for
  submission, you may open a PR with "WIP:" at the start of the title and
  request review. This tag ('work in progress') indicates that the PR is not
  ready to be merged. When it is ready for final submission, you can modify the
  title to remove the "WIP:" tag.
- Should you use a separate jupyter notebook for comparing different models? If
  you had a PR merged in to satisfy issue #2 already and are now comparing
  models for another issue, then a new notebook would be helpful. That being
  said, a notebook should satisfy the following criteria:

    a) it should run beginning to end without error

    b) it should be easy to follow and have a clear narrative presenting context,
   data, results, and interpretation. This may mean some redundancy in code, but
   will often mean that your notebook is much more helpful to other people
   looking at it in isolation (including reviewers).

#### Working on an issue:
1. `git remote add upstream git@github.com:archisha-chandel/RDScML.git`, to be done once only.
2. `git pull upstream master`
3. `git branch <name_of_the_branch>` OR `git checkout -b <new_branch_name>`
4. Create a titled .ipynb file which contains the details as explained by the issue or make the changes that you want.
5. `git status`
6. `git add <file_name>`, stage only those files that you want to commit.
7. `git commit -m "<commit_message>"`, eg: git commit -m "solves issue 2" or git commit -m "adds notebook"
8. `git push`

#### Creating a pull request:
- Specify the issue number that the pull request is fixing in the description section:
`Fixes: #<issue_number>`
- Give a suitable title to the pull request.
- Also, add a few statements explaining what the pull request is about.
