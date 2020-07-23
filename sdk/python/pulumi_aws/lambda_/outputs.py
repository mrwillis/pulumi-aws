# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from .. import _utilities, _tables
from . import outputs

__all__ = [
    'AliasRoutingConfig',
    'EventSourceMappingDestinationConfig',
    'EventSourceMappingDestinationConfigOnFailure',
    'FunctionDeadLetterConfig',
    'FunctionEnvironment',
    'FunctionEventInvokeConfigDestinationConfig',
    'FunctionEventInvokeConfigDestinationConfigOnFailure',
    'FunctionEventInvokeConfigDestinationConfigOnSuccess',
    'FunctionFileSystemConfig',
    'FunctionTracingConfig',
    'FunctionVpcConfig',
    'GetFunctionDeadLetterConfigResult',
    'GetFunctionEnvironmentResult',
    'GetFunctionFileSystemConfigResult',
    'GetFunctionTracingConfigResult',
    'GetFunctionVpcConfigResult',
]

@pulumi.output_type
class AliasRoutingConfig(dict):
    @property
    @pulumi.getter(name="additionalVersionWeights")
    def additional_version_weights(self) -> Optional[Mapping[str, float]]:
        """
        A map that defines the proportion of events that should be sent to different versions of a lambda function.
        """
        ...

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class EventSourceMappingDestinationConfig(dict):
    @property
    @pulumi.getter(name="onFailure")
    def on_failure(self) -> Optional['outputs.EventSourceMappingDestinationConfigOnFailure']:
        """
        The destination configuration for failed invocations. Detailed below.
        """
        ...

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class EventSourceMappingDestinationConfigOnFailure(dict):
    @property
    @pulumi.getter(name="destinationArn")
    def destination_arn(self) -> str:
        """
        The Amazon Resource Name (ARN) of the destination resource.
        """
        ...

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class FunctionDeadLetterConfig(dict):
    @property
    @pulumi.getter(name="targetArn")
    def target_arn(self) -> str:
        """
        The ARN of an SNS topic or SQS queue to notify when an invocation fails. If this
        option is used, the function's IAM role must be granted suitable access to write to the target object,
        which means allowing either the `sns:Publish` or `sqs:SendMessage` action on this ARN, depending on
        which service is targeted.
        """
        ...

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class FunctionEnvironment(dict):
    @property
    @pulumi.getter
    def variables(self) -> Optional[Mapping[str, str]]:
        """
        A map that defines environment variables for the Lambda function.
        """
        ...

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class FunctionEventInvokeConfigDestinationConfig(dict):
    @property
    @pulumi.getter(name="onFailure")
    def on_failure(self) -> Optional['outputs.FunctionEventInvokeConfigDestinationConfigOnFailure']:
        """
        Configuration block with destination configuration for failed asynchronous invocations. See below for details.
        """
        ...

    @property
    @pulumi.getter(name="onSuccess")
    def on_success(self) -> Optional['outputs.FunctionEventInvokeConfigDestinationConfigOnSuccess']:
        """
        Configuration block with destination configuration for successful asynchronous invocations. See below for details.
        """
        ...

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class FunctionEventInvokeConfigDestinationConfigOnFailure(dict):
    @property
    @pulumi.getter
    def destination(self) -> str:
        """
        Amazon Resource Name (ARN) of the destination resource. See the [Lambda Developer Guide](https://docs.aws.amazon.com/lambda/latest/dg/invocation-async.html#invocation-async-destinations) for acceptable resource types and associated IAM permissions.
        """
        ...

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class FunctionEventInvokeConfigDestinationConfigOnSuccess(dict):
    @property
    @pulumi.getter
    def destination(self) -> str:
        """
        Amazon Resource Name (ARN) of the destination resource. See the [Lambda Developer Guide](https://docs.aws.amazon.com/lambda/latest/dg/invocation-async.html#invocation-async-destinations) for acceptable resource types and associated IAM permissions.
        """
        ...

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class FunctionFileSystemConfig(dict):
    @property
    @pulumi.getter
    def arn(self) -> str:
        """
        The Amazon Resource Name (ARN) of the Amazon EFS Access Point that provides access to the file system.
        """
        ...

    @property
    @pulumi.getter(name="localMountPath")
    def local_mount_path(self) -> str:
        """
        The path where the function can access the file system, starting with /mnt/.
        """
        ...

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class FunctionTracingConfig(dict):
    @property
    @pulumi.getter
    def mode(self) -> str:
        """
        Can be either `PassThrough` or `Active`. If PassThrough, Lambda will only trace
        the request from an upstream service if it contains a tracing header with
        "sampled=1". If Active, Lambda will respect any tracing header it receives
        from an upstream service. If no tracing header is received, Lambda will call
        X-Ray for a tracing decision.
        """
        ...

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class FunctionVpcConfig(dict):
    @property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> List[str]:
        """
        A list of security group IDs associated with the Lambda function.
        """
        ...

    @property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> List[str]:
        """
        A list of subnet IDs associated with the Lambda function.
        """
        ...

    @property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> Optional[str]:
        ...

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class GetFunctionDeadLetterConfigResult(dict):
    @property
    @pulumi.getter(name="targetArn")
    def target_arn(self) -> str:
        ...


@pulumi.output_type
class GetFunctionEnvironmentResult(dict):
    @property
    @pulumi.getter
    def variables(self) -> Mapping[str, str]:
        ...


@pulumi.output_type
class GetFunctionFileSystemConfigResult(dict):
    @property
    @pulumi.getter
    def arn(self) -> str:
        """
        Unqualified (no `:QUALIFIER` or `:VERSION` suffix) Amazon Resource Name (ARN) identifying your Lambda Function. See also `qualified_arn`.
        """
        ...

    @property
    @pulumi.getter(name="localMountPath")
    def local_mount_path(self) -> str:
        ...


@pulumi.output_type
class GetFunctionTracingConfigResult(dict):
    @property
    @pulumi.getter
    def mode(self) -> str:
        ...


@pulumi.output_type
class GetFunctionVpcConfigResult(dict):
    @property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> List[str]:
        ...

    @property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> List[str]:
        ...

    @property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> str:
        ...

