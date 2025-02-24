from aws_cdk import (
    aws_codepipeline as codepipeline,
    aws_codepipeline_actions as codepipeline_actions,
    aws_codebuild as codebuild
)

import aws_cdk as cdk
import constructs

class PipelineStack(cdk.Stack):

    def __init__(self, scope: constructs.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        source_output = codepipeline.Artifact()
        build_output = codepipeline.Artifact()

        pipeline = codepipeline.Pipeline(self, "Pipeline",
            stages=[
                codepipeline.StageProps(
                    stage_name="Source",
                    actions=[
                        codepipeline_actions.GitHubSourceAction(
                            action_name="GitHub_Source",
                            owner="vigneshsundaramurthy",
                            repo="conde",
                            oauth_token=cdk.SecretValue.secrets_manager("github-token"),
                            output=source_output
                        )
                    ]
                ),
                codepipeline.StageProps(
                    stage_name="Build",
                    actions=[
                        codepipeline_actions.CodeBuildAction(
                            action_name="Build",
                            project=codebuild.PipelineProject(self, "BuildProject"),
                            input=source_output,
                            outputs=[build_output]
                        )
                    ]
                ),
                codepipeline.StageProps(
                    stage_name="DeployDev",
                    actions=[
                        codepipeline_actions.CloudFormationCreateUpdateStackAction(
                            action_name="DeployDev",
                            stack_name="InfraStack-Dev",
                            template_path=build_output.at_path("InfraStack.template.json"),
                            admin_permissions=True
                        )
                    ]
                ),
                codepipeline.StageProps(
                    stage_name="DeployProd",
                    actions=[
                        codepipeline_actions.CloudFormationCreateUpdateStackAction(
                            action_name="DeployProd",
                            stack_name="InfraStack-Prod",
                            template_path=build_output.at_path("InfraStack.template.json"),
                            admin_permissions=True
                        )
                    ]
                )
            ]
        )
