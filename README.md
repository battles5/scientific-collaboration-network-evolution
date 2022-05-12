# Social network of scientific collaborations evolution model

## Introduction
The co-authorship network of scientists represents a prototype of complex evolving networks.
I propose a simple model that captures the network’s time evolution and a numerical simulation to uncover the behavior of
quantities that could not be predicted analytically. The combined numerical and analytical results
underline the important role internal links play in determining the observed scaling behavior and
network topology. The results and methodologies developed in the context of the co-authorship
network could be useful for a systematic study of other complex evolving networks as well,
such as the world wide web, Internet, or other social networks.

## Network model
In order to build the model, we denote by ***k<sub>i</sub>(t)*** the number of links node ***i*** has at time ***t***; by ***T(t)*** and ***N(t)*** the
total number of links and total number of nodes at time ***t***, respectively.
In addition, we assume that all nodes present in the system are active, i.e., they can author
further papers. We consider also that new researchers join the field at a constant rate, leading to

<img src="https://latex.codecogs.com/svg.image?\large&space;N(t)=\beta&space;t" title="https://latex.codecogs.com/svg.image?\large N(t)=\beta t" />

The average number of links per node in the system at time t is thus given by

<img src="https://latex.codecogs.com/svg.image?\large&space;\left<k\right>=\frac{T(t)}{N(t)}" title="https://latex.codecogs.com/svg.image?\large \left<k\right>=\frac{T(t)}{N(t)}" />

Now, we define the rules that govern our evolving network model, capturing the basic mechanism governing the evolution of the co-authorship
network:
1. Nodes join the network at a constant rate.
2. Incoming nodes link to the already present nodes following **preferential attachment**.
3. Nodes already present in the network form new internal links following preferential attachment.
4. We neglect the aging of nodes, and assume that all nodes and links present in the system are active, able to initiate and receive new links.

In the model, we assume that the number of authors on a paper, ***m***, is constant. In
reality ***m*** is a stochastic variable, as the number of authors varies from paper to paper: making ***m*** a stochastic variable is not expected to change the scaling behavior.

Taking into account that new links join the system with a constant rate, **β**, the continuum equation for the evolution of the number of links node i has can be written as:

<img src="https://latex.codecogs.com/svg.image?\large&space;k_{i}(t)=b\sqrt{\frac{t}{t_{i}}}\sqrt{\left&space;(&space;\frac{2&plus;\alpha&space;t}{2&plus;\alpha&space;t_{i}}&space;\right&space;)^{3}}" title="https://latex.codecogs.com/svg.image?\large k_{i}(t)=b\sqrt{\frac{t}{t_{i}}}\sqrt{\left ( \frac{2+\alpha t}{2+\alpha t_{i}} \right )^{3}}" />

This will be the **Master Equation**.