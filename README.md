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

### Part I

- Week 1: Getting started with Python
- Week 2: Manipulating data using Pandas and NumPy
- Week 3: Data visualisation techniques
- Week 4: Concept Application I: Solve the Great Energy Prediction problem statements (perform data exploration only)

### Part II

- Week 5: Probability and Statistics
- Week 6: Linear Models
- Week 7: Regularisation
- Week 8: Concept Application I: Complete solving the Great Energy Prediction problem statement

### Part III

- Week 9: EDA and Feature engineering
- Week 10: Classification models
- Week 11: Decision Trees
- Week 12: Concept Application II: Solve COVID-19 visualisation problem statement

### Part IV

- Week 13: Ensemble methods
- Week 14: Clustering Algorithms
- Week 15: Support vector machines
- Week 16: Introduction to NLP

### Part V

- Week 17: Topic modelling
- Week 18: Sentiment analysis
- Week 19: Concept Application III: Solve the problem statement on Quora Insincere Questions Classification
- Week 20: Concept Application III: Solve the problem statement on Quora Insincere Questions Classification (cont.)

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

Tasks are managed using the [GitHub issue tracker](https://github.com/archisha-chandel/RDScML/issues).

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

## Getting Started

1. Install [Anaconda](https://www.anaconda.com/download) or [Miniconda](https://conda.io/miniconda.html).

2. Fork this repository and clone it into your local machine(using git CLI).

3. Setup and activate environment:

```
 $ conda env create -f environment.yml
 $ conda activate rdscml
```


__For Windows:__ Open anaconda prompt and `cd` into the folder where you cloned the repository

```
cd RDScML
```
then type the above commands to activate the environment.


4. Run Jupyter. The notebook will open in your browser at `localhost:8888` by default.

```
 $ jupyter notebook
```
After running this commands you will see the notebook containing the datasets and now you can start working with it.

We recommend everyone start by working on
[#2](https://github.com/archisha-chandel/RDScML/issues/2).


### Getting started with GitHub

The git/GitHub open-source workflow can be rather confusing if you haven't used
it before. To make a contribution to the project, the general steps you need to
take are:

- Install [git](https://git-scm.com/downloads) on your computer
- Fork the repo on Github (ie. make your own personal copy)
- Clone your fork to your local computer
- Set remote origin (https://github.com/<_user_>/PRESC.git) and upstream (https://github.com/archisha-chandel/RDScML.git)
- Create a new branch for every issue or new work that you do.
(To avoid merge conflicts keep your work in a separate folder in the same branch if it contains more than a few files.)
- Commit changes locally on your computer
- Push your changes to your fork on Github
- Submit a pull request (PR) against the main repo from your fork.

A few commands to start with everytime you work with a GIT repository:
- `git fetch upstream master`
- `git checkout FETCH_HEAD -b <new_branch_name>`
- Make changes
- `git status`
This will show the files that have been modified, deleted or created
- `git add .` (To add all the modified files)
	OR
  `git add <file_name>` (To add a specific file)
- `git commit -m '<commit_message>'`
- `git push`
If you get an error message on executing the above command, enter the suggested `git push` command.

Now, click on the link that you see once the `push` command is executed to create a Pull Request. While creating a Pull Request do mention `[ Fixes: #<issue_number> ]` in the description. This will link the issue to the Pull Request for which the latter is created.

Once your Pull Request is merged do `git pull --rebase upstream master`. This will update your fork with local changes and the ones made from upstream. This is to ensure there are no file conflicts.

Here are some resources to learn more about parts of this workflow you are
unfamiliar with:

- [GitHub Guides](https://guides.github.com/)
    * In particular, the [git handbook](https://guides.github.com/introduction/git-handbook/) explains some of the basics of the version control system
    * There is a [page](https://guides.github.com/activities/forking/)
      explaining the forking/pull request workflow you will be using to
      contribute.
- The [Git Book](https://git-scm.com/book/en/v2) is much more detailed but a good reference
    * The [Getting Started](https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control) section is worth reading
    * There are also some [videos](https://git-scm.com/videos) on getting set up
- This [repo](https://github.com/aSquare14/Git-Cheat-Sheet) by a previous
  Outreachy contributor lists many other resources and tutorials.
- This [video tutorial series](https://www.youtube.com/playlist?list=PL6gx4Cwl9DGAKWClAD_iKpNC0bGHxGhcx) on Youtube may also be helpful
- [First Contributions](https://github.com/firstcontributions/first-contributions#first-contributions) is a good place to actually practise and put your understanding to test. Feel free to make mistakes as you go along learning to make your first contribution. 

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
