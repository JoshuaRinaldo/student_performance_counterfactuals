# Student Study Habit Counterfactuals using [DiCE](https://github.com/interpretml/DiCE/tree/main)

## Introduction
Can we use Machine Learning to optimize student study habits?

This repository contains a proof-of-concept where we use synthetic data to
train a model that predicts academic performance based on study habits. We
then predict a given student's score and use counterfactuals to provide
examples where their score is higher.

The goal of providing counterfactuals is to give students actionable feedback
on how to improve their academic performance.

## Usage

The model that was trained in [`student_performance_counterfactuals.ipynb`](student_performance_counterfactuals.ipynb).
can be containerized and served as a flask app.

If you would like to run this model locally without running the training
notebook, follow these instructions:

1. Ensure some container runtime ([docker](https://www.docker.com/),
[podman](https://podman.io/), [colima](https://github.com/abiosoft/colima)) is
installed on your machine and functional.

2. Clone this repository and `cd` into it.

3. Run `docker build .`, which will build the image. Take note of the image's
   tag or specify a tag with the `-t` argument.

4. Run a container based on that image, exposing port `5000` of the container:
   `docker run -it -p 5000:5000 -d <image_tag>`.

5. Send a request to the container. Here is an example using `curl`:

```
curl -H 'Content-Type: application/json' \
      -d '{"Hours Studied": 4,"Extracurricular Activities": 1,"Sleep Hours": 6,"Sample Question Papers Practiced": 2}' \
      -X POST \
      http://127.0.0.1:5000/counterfactual
```
