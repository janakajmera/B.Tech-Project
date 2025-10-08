# Self-Supervised Learning for Remote Sensin Image Classification

*This will be the last time I am making a floder for this project*

Under the guidance of - How does it matter?
In the end, what **I** do matters.
There is supposed to be a team of 2, but how does even that matter who the other person is.

**Lets start**    
Some questions that need to be answered first:

**What is Self Supervised Learning?**
According to Gemini(The LLM by Google)- 
Self-supervised learning (SSL) is a machine learning paradigm where a model learns to generate its own supervisory signals from unlabeled data instead of relying on manually annotated labels. This approach allows the model to learn meaningful representations of the data by solving a "pretext task,", which **I** also like to call - *pretraining* which is an auxiliary task designed to teach the model about the inherent structure of the data. Once the model has learned these representations, they can be used for a "downstream task," which is the actual problem you want to solve (e.g., classification, segmentation, etc.).

**How is it any different from other paradigms?**
Self-supervised learning (SSL) is a machine learning paradigm that generates its own supervisory signals from unlabeled data. Unlike supervised learning, which requires a massive dataset of human-annotated labels, SSL creates a pretext task that forces a model to learn about the underlying structure and patterns of the data. For example, a model might learn to predict a masked word in a sentence or fill in a missing part of an image. By solving these self-generated tasks, the model develops a robust internal representation of the data. This powerful representation can then be transferred to a downstream task (like image classification or object detection), requiring only a small amount of labeled data for fine-tuning. In essence, SSL is a middle ground between supervised and unsupervised learning, using the abundance of unlabeled data to create a learning process that is both autonomous and highly effective for real-world applications.

I would like to draw an analogy(though some people may not like it). Supervised learning is like being taught by a teacher about some subject. Only the things being taught by a teacher will be asked in the final exams. Self Supervised learning is more like you learn most things in life by your experience from which **you** derive some learning. Like for me, what I have learnt through watching news about geopolitics and stuff. But if I have to give an exam (like UPSC), I will have to refine (or finetune) my learning through the guidance of a teacher. So, according to me, the pretext task is like learning to learn (or rather differentiate) and the downstream task is actual learning for an exam.

*A long and enough explaination*
*And I will keep adding more explainations(and analogies) as needed.*

Now, lets drive into what I will be doing and how.

I want this to be a modular and deployable code. Although this is a research project and **I** have to write a so called **thesis** on this, I certainly do not intend on pursuing research. I want a job. So, modular code will be more useful.

---

## File structure:

BTP/  <!-- Keep the file name whatever you want it to be.-->
├── README.md
├── requirements.txt
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── utils.py
├── Data/
│   ├── raw/
│   ├── processed/
│   ├── external/
├── Notebooks/      <!--Notebooks are for experimentation and whatever code is written here is also written in the modular files-->
│   ├── ResNet-EuroSAT.ipynb    <!--EuroSAT because we are supposed to be working on remote sensing data-->
└── .gitignore

Before we proceed any further, I need to make a virtual environment for python. For the code to be containerized and deployed, a separate virtual environment for python need to be made.
- In my local PC, I did it using pip:
    `` python -m venv .venv `` <!-- the name of the environment file is .venv-->
- To activate it in bash:
    `` source .venv/Scripts/activate ``

- In the remote server, I had conda:
    `` conda create -n .venv ``
- Activate it:
    `` conda activate .venv ``

*Don't forget to add .venv into the gitignore file. Otherwise, it will create problems in deployment.*

All of this needed to be done on the remote DGX server. Why? Its a long story. I don't want to explain it. If you can have access to your a HPC server in your university, its good. If not, just clone the project and move on.

### Setting up the remote DGX server
- I requested the system admin fot access. And I was given along with the IP, Username and a temporary password.
- I used Putty (Yes, civil engineers. We will always borrow names from you. Because we do not have any. ) using SSH to connect and WinSCP for file transfer.
- Search on gemini or ChatGPT about how to do it. I am too tired to write the process.
- When you have set it up, open it and make sure your server or user has either pip or conda for environment creation. My server did not have any. Even the python which was installed was from the age of Adam :joy:
- Anyway. Then clone the repository there in a new folder.
    - Basic git commands:
        - `` git init `` <!--initializes git from your local repository-->
        - `` git add . `` <!--adds all files with changes to the local repository-->
        - `` git commit -m "first commit" `` <!--Commits the changes to the local repository-->
        - `` git branch -M main ``   <!--Perhaps, will come in use later-->
        - `` git remote add origin `` <url> <!--url is the url of your github repository-->
        - `` git push -u origin main ``   <!--Finally, to push the changes to your repository-->
- If you do not know how to use linux then go to hell. There is no place for you here. *East or West, Linux is the best.*

- I also set up a tunnel for jupyter notebooks to be run with the GUI on my pc and the actual kernel on the remote server






