<iframe
  width="500" 
  height="500" 
  src="https://www.youtube.com/embed/foyPwFATIC0"
  frameborder="0"
  allowfullscreen>
</iframe>

![](./assets/22_aws_1.png)

![](./assets/22_aws_2.png)

![](./assets/22_aws_3.png)

![](./assets/22_aws_4.png)

- Access key helps to verify the authentication with python code and github actions
  ![](./assets/22_aws_5.png)

- Creating the instance
  ![](./assets/22_aws_6.png)

- Instance without walkthrough
  ![](./assets/22_aws_7.png)

- Instance configuration
  ![](./assets/22_aws_8.png)
- Need to select Ubuntu, t2-medium enough for small projects

- Generate Key Value Pair
  ![](./assets/22_aws_9.png)

![](./assets/22_aws_10.png)

Need to select the key after creating
![](./assets/22_aws_11.png)

- This key helps for the access the instance from the third party instances like putty

Need to enable the HTTPS/HTTP
![](./assets/22_aws_12.png)

- Select 32 gb storage(Rough)
  ![](./assets/22_aws_13.png)

- Instance will create
  ![](./assets/22_aws_14.png)

Connecting to instance
![](./assets/22_aws_15.png)

![](./assets/22_aws_16.png)

![](./assets/22_aws_17.png)

![](./assets/22_aws_18.png)

![](./assets/22_aws_19.png)

![](./assets/22_aws_20.png)

![](./assets/22_aws_21.png)

![](./assets/22_aws_22.png)

![](./assets/22_aws_23.png)

![](./assets/22_aws_24.png)

![](./assets/22_aws_25.png)

![](./assets/22_aws_26.png)

- Executing all the commands in the ec2 instances
- Download commands
  ![](./assets/22_aws_27.png)

- Configure commands
  ![](./assets/22_aws_28.png)

  Dont need to give the runner group, press enter without name
  ![](./assets/22_aws_29.png)

  Name of runner, this is name mentioned in the cicd.yml file,otherwise it will not work
  ![](./assets/22_aws_30.png)

  ![](./assets/22_aws_31.png)

  For the label, we can skip, It is not mandatory
  ![](./assets/22_aws_32.png)

- Configure commands
  ![](./assets/22_aws_33.png)

  It will show,"Listening to Jobs"  
  ![](./assets/22_aws_34.png)

  In Github, Under the Runners, It will show the instance  
  ![](./assets/22_aws_35.png)

  What are secret keys, mentioned in the cicd need to configure
  ![](./assets/22_aws_36.png)

  ![](./assets/22_aws_37.png)

  ![](./assets/22_aws_38.png)

  ![](./assets/22_aws_39.png)

  ![](./assets/22_aws_40.png)

  Configuring aws region
  ![](./assets/22_aws_41.png)

  Pushing to git and check
  ![](./assets/22_aws_42.png)

  ![](./assets/22_aws_43.png)

  ![](./assets/22_aws_44.png)

  open the public DNS in the browser, if not open we need to configure the port mapping
  ![](./assets/22_aws_45.png)

  - port mapping
  - Security, Security Groups, Edit inbound rules
  ![](./assets/22_aws_46.png)

  ![](./assets/22_aws_47.png)

  ![](./assets/22_aws_48.png)

  We declared the port number in the cicd file, need to enter the port value
  ![](./assets/22_aws_49.png)

  ![](./assets/22_aws_50.png)

  ![](./assets/22_aws_51.png)

- Terminating Instance 
  ![](./assets/22_aws_53.png)
  Deleting the IAM User
  ![](./assets/22_aws_54.png)


  
  
  
