# Fruit Fly Brain Hackathon 2019

**Wednesday, March 20, 2019** <br>
**750 CEPSR** <br>
**Center for Neural Engineering and Computation** <br>
**Columbia University, New York, NY, USA** <br>

## Overview
The 4th Fruit Fly brain Hackathon (FFBH 2019) will be held on Wednesday, March 20, 2019. The goal of the hackathon is to bring together researchers interested in developing executable models of the fruit fly brain. In this year’s hackathon, we will focus on the FlyBrainLab (FBL), a newly developed interactive computing platform for studying the function of executable circuits constructed from fly brain data. The hackathon is aimed at three main groups of participants: neurobiologists, modelers and software engineers. We welcome researchers working on the fruit fly brain as well as those working on other model organisms to participate and broaden the discussion in the hackathon.

The Fruit Fly Brain Hackathon 2019 is organized in conjunction with the [Columbia Workshop on Brain Circuit, Memory and Computation](http://fruitflybrain.org/workshops.html) on March 21-22, 2019. Participants of the hackathon are welcome to attend the workshop.

## Organizers
Tingkai Liu, Department of Electrical Engineering, Columbia University

Mehmet Kerem Turkcan, Department of Electrical Engineering, Columbia University

Chung-Heng Yeh, Department of Electrical Engineering, Columbia University

Yiyin Zhou, Department of Electrical Engineering, Columbia University

## Registration
Registration is free but all participants have to [register](https://ffbh2019.eventbrite.com/). To help us better organize the event, please provide in the appropriate registration block a brief description of your background and what you would like to learn/achieve during the hackathon. Thank you!

## Lodging and Directions to Venue
Please follow this [link](https://fruitflybrain.org/hackathons.html) for lodging details and directions to the hotel and venue.

## Schedule
Wednesday, March 20th, 2019

| Time | Topic |
|------|-------|
| 09:00 AM - 09:10 AM | [Introduction to the Fruit Fly Brain Hackathon (Chung-Heng Yeh, Columbia University, USA).](https://github.com/fruitflybrain/hackathon19/blob/master/Introduction.ipynb)|
| 09:10 AM - 09:15 AM | Self-introductions by Participants. |
| 09:15 AM - 09:30 AM | [Introduction to FlyBrainLab (Mehmet K. Turkcan, Columbia University, USA).](https://docs.google.com/presentation/d/14z09Kxbo1CAoDz9oR6jNrz_oG72UTXvVp-oUza4kg6k/edit?usp=sharing)|
| 09:30 AM - 12:30 PM | Hacking: Basic Features of FBL.|
| 12:30 PM - 01:30 PM | Lunch Break.|
| 01:30 PM - 01:45 AM | Building Models of Fly Brain Neuropil Using FBL (Yiyin Zhou, Columbia University, USA).|
| 01:45 AM - 02:00 PM | Discussions and Summary of Project Ideas.|
| 02:00 PM - 06:00 PM | Hacking.|


## Computing Resources
Participants only need to bring a laptop to the hackathon to fully explore the capacity of the FFBO. We will host the main FFBO service on an Amazon EC2 instance with limited capacity. For attendees interested in installing FFBO on their own machines, or developing new features, all service packages will be available in the form of [Docker](https://www.docker.com/) images.

### Docker Image
Docker image for a complete install of FFBO and FBL is available [HERE](https://hub.docker.com/r/fruitflybrain/ffbh19). You can simply pull the image onto your system:
    
    docker pull fruitflybrain/ffbh19

Running this docker image with GPU support requires [nvidia-docker](https://github.com/NVIDIA/nvidia-docker) ([Installation Instruction](https://github.com/nvidia/nvidia-docker/wiki/Installation-(version-2.0))). The image has been tested on Ubuntu 16.04 with nvidia-docker v2.0. An [Amazon Machine Image](https://console.aws.amazon.com/ec2/v2/home?region=us-east-1#LaunchInstanceWizard:ami=ami-0221bb3d675af4924) (ami-0221bb3d675af4924 in the US-East-1 region) with Docker and nvidia-docker installed is provided for convience.

To launch a Docker container using the image:

    docker run -d --runtime=nvidia --name flybrainlab -p 10000-10002:10000-10002 -p 10003:22 -it fruitflybrain/ffbh19 bash -c "service ssh start; /opt/orientdb/bin/server.sh &"

The container will be launched in the background. You can now SSH into it with

    ssh -p 10003 ffbh@server-ip
    
and the password is Drosophila. For security reason, please change the password after your first login by

    passwd
    
### Launching FFBO Servers
To launch all FFBO servers, simply run the following shell script in `/home/ffbh/run_scripts` in the following order (we recommand running each script using a tmux session/window):

    sh run_processor.sh
    sh run_nlp.sh
    sh run_neuroarch.sh
    sh run_neurokernel.sh

Please go to http://server-ip:10000 and test a query before using FBL.
    
### Launching FBL
To launch FBL, you can run the shell script `/home/ffbh/run_script/run_fbl.sh`. The jupyter lab will be launched at port `10004` by default. Since the port is not exposed by the Docker container, you can do one of the following:
1. (preferred) Use a SSH tunnel, _i.e_,:

    `ssh -p 10003 -L local_port:localhost:10004 ffbh@server-ip`

   Replace local_port by your choice of port number. You can access the FBL using your browser at http://localhost:local_port.

2. Expose the `10004` port when starting the Docker container, _i.e_,:
    
    `docker run -d --runtime=nvidia --name flybrainlab -p 10000-10002:10000-10002 -p 10003:22 -p 10004:10004 -it fruitflybrain/ffbh19 bash -c "service ssh start; /opt/orientdb/bin/server.sh &"`
    
   and access FBL using your browser at http://server-ip:10004.


## Using Supplied Server
You can install the FBL on your laptop using the instruction here:
https://github.com/FlyBrainLab/flybrainlab

Please note that, for FBLClient, you need to use the branch called [`ffbh19`](https://github.com/FlyBrainLab/FBLClient/tree/ffbh19).

After installation, you need to the following configuration before starting jupyter lab.

The IP address of our server is 18.209.44.42. Please put this into the field `ip` in `FBLClient.ini` in the `FBLClient` repository and change the `[ID][digits]` field to `0`.

Finally, launch `jupyter lab`.



