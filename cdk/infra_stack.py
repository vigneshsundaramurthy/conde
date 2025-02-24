from aws_cdk import (
    aws_ec2 as ec2,
    aws_ecs as ecs,
    aws_ecs_patterns as ecs_patterns
)
import aws_cdk as cdk
import constructs
class InfraStack(cdk.Stack):

    def __init__(self, scope: constructs.Construct, id: str) -> None:
        super().__init__(scope, id)

        vpc = ec2.Vpc(self, "infraVpc", max_azs=2)

        cluster = ecs.Cluster(self, "MyCluster", vpc=vpc)

        ecs_patterns.ApplicationLoadBalancedFargateService(self, "MyFargateService",
            cluster=cluster,
            task_image_options={
                "image": ecs.ContainerImage.from_asset("../"),
                "container_port": 80
            },
            public_load_balancer=True
        )
