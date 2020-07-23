# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from .. import _utilities, _tables

__all__ = [
    'EventPermissionConditionArgs',
    'EventTargetBatchTargetArgs',
    'EventTargetEcsTargetArgs',
    'EventTargetEcsTargetNetworkConfigurationArgs',
    'EventTargetInputTransformerArgs',
    'EventTargetKinesisTargetArgs',
    'EventTargetRunCommandTargetArgs',
    'EventTargetSqsTargetArgs',
    'LogMetricFilterMetricTransformationArgs',
    'MetricAlarmMetricQueryArgs',
    'MetricAlarmMetricQueryMetricArgs',
]

@pulumi.input_type
class EventPermissionConditionArgs:
    def __init__(__self__, *,
                 key: pulumi.Input[str],
                 type: pulumi.Input[str],
                 value: pulumi.Input[str]):
        """
        :param pulumi.Input[str] key: Key for the condition. Valid values: `aws:PrincipalOrgID`.
        :param pulumi.Input[str] type: Type of condition. Value values: `StringEquals`.
        :param pulumi.Input[str] value: Value for the key.
        """
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "type", type)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> pulumi.Input[str]:
        """
        Key for the condition. Valid values: `aws:PrincipalOrgID`.
        """
        ...

    @key.setter
    def key(self, value: pulumi.Input[str]):
        ...

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        Type of condition. Value values: `StringEquals`.
        """
        ...

    @type.setter
    def type(self, value: pulumi.Input[str]):
        ...

    @property
    @pulumi.getter
    def value(self) -> pulumi.Input[str]:
        """
        Value for the key.
        """
        ...

    @value.setter
    def value(self, value: pulumi.Input[str]):
        ...


@pulumi.input_type
class EventTargetBatchTargetArgs:
    def __init__(__self__, *,
                 job_definition: pulumi.Input[str],
                 job_name: pulumi.Input[str],
                 array_size: Optional[pulumi.Input[float]] = None,
                 job_attempts: Optional[pulumi.Input[float]] = None):
        """
        :param pulumi.Input[str] job_definition: The ARN or name of the job definition to use if the event target is an AWS Batch job. This job definition must already exist.
        :param pulumi.Input[str] job_name: The name to use for this execution of the job, if the target is an AWS Batch job.
        :param pulumi.Input[float] array_size: The size of the array, if this is an array batch job. Valid values are integers between 2 and 10,000.
        :param pulumi.Input[float] job_attempts: The number of times to attempt to retry, if the job fails. Valid values are 1 to 10.
        """
        pulumi.set(__self__, "jobDefinition", job_definition)
        pulumi.set(__self__, "jobName", job_name)
        pulumi.set(__self__, "arraySize", array_size)
        pulumi.set(__self__, "jobAttempts", job_attempts)

    @property
    @pulumi.getter(name="jobDefinition")
    def job_definition(self) -> pulumi.Input[str]:
        """
        The ARN or name of the job definition to use if the event target is an AWS Batch job. This job definition must already exist.
        """
        ...

    @job_definition.setter
    def job_definition(self, value: pulumi.Input[str]):
        ...

    @property
    @pulumi.getter(name="jobName")
    def job_name(self) -> pulumi.Input[str]:
        """
        The name to use for this execution of the job, if the target is an AWS Batch job.
        """
        ...

    @job_name.setter
    def job_name(self, value: pulumi.Input[str]):
        ...

    @property
    @pulumi.getter(name="arraySize")
    def array_size(self) -> Optional[pulumi.Input[float]]:
        """
        The size of the array, if this is an array batch job. Valid values are integers between 2 and 10,000.
        """
        ...

    @array_size.setter
    def array_size(self, value: Optional[pulumi.Input[float]]):
        ...

    @property
    @pulumi.getter(name="jobAttempts")
    def job_attempts(self) -> Optional[pulumi.Input[float]]:
        """
        The number of times to attempt to retry, if the job fails. Valid values are 1 to 10.
        """
        ...

    @job_attempts.setter
    def job_attempts(self, value: Optional[pulumi.Input[float]]):
        ...


@pulumi.input_type
class EventTargetEcsTargetArgs:
    def __init__(__self__, *,
                 task_definition_arn: pulumi.Input[str],
                 group: Optional[pulumi.Input[str]] = None,
                 launch_type: Optional[pulumi.Input[str]] = None,
                 network_configuration: Optional[pulumi.Input['EventTargetEcsTargetNetworkConfigurationArgs']] = None,
                 platform_version: Optional[pulumi.Input[str]] = None,
                 task_count: Optional[pulumi.Input[float]] = None):
        """
        :param pulumi.Input[str] task_definition_arn: The ARN of the task definition to use if the event target is an Amazon ECS cluster.
        :param pulumi.Input[str] group: Specifies an ECS task group for the task. The maximum length is 255 characters.
        :param pulumi.Input[str] launch_type: Specifies the launch type on which your task is running. The launch type that you specify here must match one of the launch type (compatibilities) of the target task. Valid values are EC2 or FARGATE.
        :param pulumi.Input['EventTargetEcsTargetNetworkConfigurationArgs'] network_configuration: Use this if the ECS task uses the awsvpc network mode. This specifies the VPC subnets and security groups associated with the task, and whether a public IP address is to be used. Required if launch_type is FARGATE because the awsvpc mode is required for Fargate tasks.
        :param pulumi.Input[str] platform_version: Specifies the platform version for the task. Specify only the numeric portion of the platform version, such as 1.1.0. This is used only if LaunchType is FARGATE. For more information about valid platform versions, see [AWS Fargate Platform Versions](http://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versions.html).
        :param pulumi.Input[float] task_count: The number of tasks to create based on the TaskDefinition. The default is 1.
        """
        pulumi.set(__self__, "taskDefinitionArn", task_definition_arn)
        pulumi.set(__self__, "group", group)
        pulumi.set(__self__, "launchType", launch_type)
        pulumi.set(__self__, "networkConfiguration", network_configuration)
        pulumi.set(__self__, "platformVersion", platform_version)
        pulumi.set(__self__, "taskCount", task_count)

    @property
    @pulumi.getter(name="taskDefinitionArn")
    def task_definition_arn(self) -> pulumi.Input[str]:
        """
        The ARN of the task definition to use if the event target is an Amazon ECS cluster.
        """
        ...

    @task_definition_arn.setter
    def task_definition_arn(self, value: pulumi.Input[str]):
        ...

    @property
    @pulumi.getter
    def group(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies an ECS task group for the task. The maximum length is 255 characters.
        """
        ...

    @group.setter
    def group(self, value: Optional[pulumi.Input[str]]):
        ...

    @property
    @pulumi.getter(name="launchType")
    def launch_type(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the launch type on which your task is running. The launch type that you specify here must match one of the launch type (compatibilities) of the target task. Valid values are EC2 or FARGATE.
        """
        ...

    @launch_type.setter
    def launch_type(self, value: Optional[pulumi.Input[str]]):
        ...

    @property
    @pulumi.getter(name="networkConfiguration")
    def network_configuration(self) -> Optional[pulumi.Input['EventTargetEcsTargetNetworkConfigurationArgs']]:
        """
        Use this if the ECS task uses the awsvpc network mode. This specifies the VPC subnets and security groups associated with the task, and whether a public IP address is to be used. Required if launch_type is FARGATE because the awsvpc mode is required for Fargate tasks.
        """
        ...

    @network_configuration.setter
    def network_configuration(self, value: Optional[pulumi.Input['EventTargetEcsTargetNetworkConfigurationArgs']]):
        ...

    @property
    @pulumi.getter(name="platformVersion")
    def platform_version(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the platform version for the task. Specify only the numeric portion of the platform version, such as 1.1.0. This is used only if LaunchType is FARGATE. For more information about valid platform versions, see [AWS Fargate Platform Versions](http://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versions.html).
        """
        ...

    @platform_version.setter
    def platform_version(self, value: Optional[pulumi.Input[str]]):
        ...

    @property
    @pulumi.getter(name="taskCount")
    def task_count(self) -> Optional[pulumi.Input[float]]:
        """
        The number of tasks to create based on the TaskDefinition. The default is 1.
        """
        ...

    @task_count.setter
    def task_count(self, value: Optional[pulumi.Input[float]]):
        ...


@pulumi.input_type
class EventTargetEcsTargetNetworkConfigurationArgs:
    def __init__(__self__, *,
                 subnets: pulumi.Input[List[pulumi.Input[str]]],
                 assign_public_ip: Optional[pulumi.Input[bool]] = None,
                 security_groups: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None):
        """
        :param pulumi.Input[List[pulumi.Input[str]]] subnets: The subnets associated with the task or service.
        :param pulumi.Input[bool] assign_public_ip: Assign a public IP address to the ENI (Fargate launch type only). Valid values are `true` or `false`. Default `false`.
        :param pulumi.Input[List[pulumi.Input[str]]] security_groups: The security groups associated with the task or service. If you do not specify a security group, the default security group for the VPC is used.
        """
        pulumi.set(__self__, "subnets", subnets)
        pulumi.set(__self__, "assignPublicIp", assign_public_ip)
        pulumi.set(__self__, "securityGroups", security_groups)

    @property
    @pulumi.getter
    def subnets(self) -> pulumi.Input[List[pulumi.Input[str]]]:
        """
        The subnets associated with the task or service.
        """
        ...

    @subnets.setter
    def subnets(self, value: pulumi.Input[List[pulumi.Input[str]]]):
        ...

    @property
    @pulumi.getter(name="assignPublicIp")
    def assign_public_ip(self) -> Optional[pulumi.Input[bool]]:
        """
        Assign a public IP address to the ENI (Fargate launch type only). Valid values are `true` or `false`. Default `false`.
        """
        ...

    @assign_public_ip.setter
    def assign_public_ip(self, value: Optional[pulumi.Input[bool]]):
        ...

    @property
    @pulumi.getter(name="securityGroups")
    def security_groups(self) -> Optional[pulumi.Input[List[pulumi.Input[str]]]]:
        """
        The security groups associated with the task or service. If you do not specify a security group, the default security group for the VPC is used.
        """
        ...

    @security_groups.setter
    def security_groups(self, value: Optional[pulumi.Input[List[pulumi.Input[str]]]]):
        ...


@pulumi.input_type
class EventTargetInputTransformerArgs:
    def __init__(__self__, *,
                 input_template: pulumi.Input[str],
                 input_paths: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        :param pulumi.Input[str] input_template: Structure containing the template body.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] input_paths: Key value pairs specified in the form of JSONPath (for example, time = $.time)
        """
        pulumi.set(__self__, "inputTemplate", input_template)
        pulumi.set(__self__, "inputPaths", input_paths)

    @property
    @pulumi.getter(name="inputTemplate")
    def input_template(self) -> pulumi.Input[str]:
        """
        Structure containing the template body.
        """
        ...

    @input_template.setter
    def input_template(self, value: pulumi.Input[str]):
        ...

    @property
    @pulumi.getter(name="inputPaths")
    def input_paths(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Key value pairs specified in the form of JSONPath (for example, time = $.time)
        """
        ...

    @input_paths.setter
    def input_paths(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        ...


@pulumi.input_type
class EventTargetKinesisTargetArgs:
    def __init__(__self__, *,
                 partition_key_path: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] partition_key_path: The JSON path to be extracted from the event and used as the partition key.
        """
        pulumi.set(__self__, "partitionKeyPath", partition_key_path)

    @property
    @pulumi.getter(name="partitionKeyPath")
    def partition_key_path(self) -> Optional[pulumi.Input[str]]:
        """
        The JSON path to be extracted from the event and used as the partition key.
        """
        ...

    @partition_key_path.setter
    def partition_key_path(self, value: Optional[pulumi.Input[str]]):
        ...


@pulumi.input_type
class EventTargetRunCommandTargetArgs:
    def __init__(__self__, *,
                 key: pulumi.Input[str],
                 values: pulumi.Input[List[pulumi.Input[str]]]):
        """
        :param pulumi.Input[str] key: Can be either `tag:tag-key` or `InstanceIds`.
        :param pulumi.Input[List[pulumi.Input[str]]] values: If Key is `tag:tag-key`, Values is a list of tag values. If Key is `InstanceIds`, Values is a list of Amazon EC2 instance IDs.
        """
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "values", values)

    @property
    @pulumi.getter
    def key(self) -> pulumi.Input[str]:
        """
        Can be either `tag:tag-key` or `InstanceIds`.
        """
        ...

    @key.setter
    def key(self, value: pulumi.Input[str]):
        ...

    @property
    @pulumi.getter
    def values(self) -> pulumi.Input[List[pulumi.Input[str]]]:
        """
        If Key is `tag:tag-key`, Values is a list of tag values. If Key is `InstanceIds`, Values is a list of Amazon EC2 instance IDs.
        """
        ...

    @values.setter
    def values(self, value: pulumi.Input[List[pulumi.Input[str]]]):
        ...


@pulumi.input_type
class EventTargetSqsTargetArgs:
    def __init__(__self__, *,
                 message_group_id: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] message_group_id: The FIFO message group ID to use as the target.
        """
        pulumi.set(__self__, "messageGroupId", message_group_id)

    @property
    @pulumi.getter(name="messageGroupId")
    def message_group_id(self) -> Optional[pulumi.Input[str]]:
        """
        The FIFO message group ID to use as the target.
        """
        ...

    @message_group_id.setter
    def message_group_id(self, value: Optional[pulumi.Input[str]]):
        ...


@pulumi.input_type
class LogMetricFilterMetricTransformationArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[str],
                 namespace: pulumi.Input[str],
                 value: pulumi.Input[str],
                 default_value: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] name: The name of the CloudWatch metric to which the monitored log information should be published (e.g. `ErrorCount`)
        :param pulumi.Input[str] namespace: The destination namespace of the CloudWatch metric.
        :param pulumi.Input[str] value: What to publish to the metric. For example, if you're counting the occurrences of a particular term like "Error", the value will be "1" for each occurrence. If you're counting the bytes transferred the published value will be the value in the log event.
        :param pulumi.Input[str] default_value: The value to emit when a filter pattern does not match a log event.
        """
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "namespace", namespace)
        pulumi.set(__self__, "value", value)
        pulumi.set(__self__, "defaultValue", default_value)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        The name of the CloudWatch metric to which the monitored log information should be published (e.g. `ErrorCount`)
        """
        ...

    @name.setter
    def name(self, value: pulumi.Input[str]):
        ...

    @property
    @pulumi.getter
    def namespace(self) -> pulumi.Input[str]:
        """
        The destination namespace of the CloudWatch metric.
        """
        ...

    @namespace.setter
    def namespace(self, value: pulumi.Input[str]):
        ...

    @property
    @pulumi.getter
    def value(self) -> pulumi.Input[str]:
        """
        What to publish to the metric. For example, if you're counting the occurrences of a particular term like "Error", the value will be "1" for each occurrence. If you're counting the bytes transferred the published value will be the value in the log event.
        """
        ...

    @value.setter
    def value(self, value: pulumi.Input[str]):
        ...

    @property
    @pulumi.getter(name="defaultValue")
    def default_value(self) -> Optional[pulumi.Input[str]]:
        """
        The value to emit when a filter pattern does not match a log event.
        """
        ...

    @default_value.setter
    def default_value(self, value: Optional[pulumi.Input[str]]):
        ...


@pulumi.input_type
class MetricAlarmMetricQueryArgs:
    def __init__(__self__, *,
                 id: pulumi.Input[str],
                 expression: Optional[pulumi.Input[str]] = None,
                 label: Optional[pulumi.Input[str]] = None,
                 metric: Optional[pulumi.Input['MetricAlarmMetricQueryMetricArgs']] = None,
                 return_data: Optional[pulumi.Input[bool]] = None):
        """
        :param pulumi.Input[str] id: A short name used to tie this object to the results in the response. If you are performing math expressions on this set of data, this name represents that data and can serve as a variable in the mathematical expression. The valid characters are letters, numbers, and underscore. The first character must be a lowercase letter.
        :param pulumi.Input[str] expression: The math expression to be performed on the returned data, if this object is performing a math expression. This expression can use the id of the other metrics to refer to those metrics, and can also use the id of other expressions to use the result of those expressions. For more information about metric math expressions, see Metric Math Syntax and Functions in the [Amazon CloudWatch User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/using-metric-math.html#metric-math-syntax).
        :param pulumi.Input[str] label: A human-readable label for this metric or expression. This is especially useful if this is an expression, so that you know what the value represents.
        :param pulumi.Input['MetricAlarmMetricQueryMetricArgs'] metric: The metric to be returned, along with statistics, period, and units. Use this parameter only if this object is retrieving a metric and not performing a math expression on returned data.
        :param pulumi.Input[bool] return_data: Specify exactly one `metric_query` to be `true` to use that `metric_query` result as the alarm.
        """
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "expression", expression)
        pulumi.set(__self__, "label", label)
        pulumi.set(__self__, "metric", metric)
        pulumi.set(__self__, "returnData", return_data)

    @property
    @pulumi.getter
    def id(self) -> pulumi.Input[str]:
        """
        A short name used to tie this object to the results in the response. If you are performing math expressions on this set of data, this name represents that data and can serve as a variable in the mathematical expression. The valid characters are letters, numbers, and underscore. The first character must be a lowercase letter.
        """
        ...

    @id.setter
    def id(self, value: pulumi.Input[str]):
        ...

    @property
    @pulumi.getter
    def expression(self) -> Optional[pulumi.Input[str]]:
        """
        The math expression to be performed on the returned data, if this object is performing a math expression. This expression can use the id of the other metrics to refer to those metrics, and can also use the id of other expressions to use the result of those expressions. For more information about metric math expressions, see Metric Math Syntax and Functions in the [Amazon CloudWatch User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/using-metric-math.html#metric-math-syntax).
        """
        ...

    @expression.setter
    def expression(self, value: Optional[pulumi.Input[str]]):
        ...

    @property
    @pulumi.getter
    def label(self) -> Optional[pulumi.Input[str]]:
        """
        A human-readable label for this metric or expression. This is especially useful if this is an expression, so that you know what the value represents.
        """
        ...

    @label.setter
    def label(self, value: Optional[pulumi.Input[str]]):
        ...

    @property
    @pulumi.getter
    def metric(self) -> Optional[pulumi.Input['MetricAlarmMetricQueryMetricArgs']]:
        """
        The metric to be returned, along with statistics, period, and units. Use this parameter only if this object is retrieving a metric and not performing a math expression on returned data.
        """
        ...

    @metric.setter
    def metric(self, value: Optional[pulumi.Input['MetricAlarmMetricQueryMetricArgs']]):
        ...

    @property
    @pulumi.getter(name="returnData")
    def return_data(self) -> Optional[pulumi.Input[bool]]:
        """
        Specify exactly one `metric_query` to be `true` to use that `metric_query` result as the alarm.
        """
        ...

    @return_data.setter
    def return_data(self, value: Optional[pulumi.Input[bool]]):
        ...


@pulumi.input_type
class MetricAlarmMetricQueryMetricArgs:
    def __init__(__self__, *,
                 metric_name: pulumi.Input[str],
                 period: pulumi.Input[float],
                 stat: pulumi.Input[str],
                 dimensions: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 namespace: Optional[pulumi.Input[str]] = None,
                 unit: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] metric_name: The name for this metric.
               See docs for [supported metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CW_Support_For_AWS.html).
        :param pulumi.Input[float] period: The period in seconds over which the specified `stat` is applied.
        :param pulumi.Input[str] stat: The statistic to apply to this metric.
               Either of the following is supported: `SampleCount`, `Average`, `Sum`, `Minimum`, `Maximum`
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] dimensions: The dimensions for this metric.  For the list of available dimensions see the AWS documentation [here](http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CW_Support_For_AWS.html).
        :param pulumi.Input[str] namespace: The namespace for this metric. See docs for the [list of namespaces](https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/aws-namespaces.html).
               See docs for [supported metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CW_Support_For_AWS.html).
        :param pulumi.Input[str] unit: The unit for this metric.
        """
        pulumi.set(__self__, "metricName", metric_name)
        pulumi.set(__self__, "period", period)
        pulumi.set(__self__, "stat", stat)
        pulumi.set(__self__, "dimensions", dimensions)
        pulumi.set(__self__, "namespace", namespace)
        pulumi.set(__self__, "unit", unit)

    @property
    @pulumi.getter(name="metricName")
    def metric_name(self) -> pulumi.Input[str]:
        """
        The name for this metric.
        See docs for [supported metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CW_Support_For_AWS.html).
        """
        ...

    @metric_name.setter
    def metric_name(self, value: pulumi.Input[str]):
        ...

    @property
    @pulumi.getter
    def period(self) -> pulumi.Input[float]:
        """
        The period in seconds over which the specified `stat` is applied.
        """
        ...

    @period.setter
    def period(self, value: pulumi.Input[float]):
        ...

    @property
    @pulumi.getter
    def stat(self) -> pulumi.Input[str]:
        """
        The statistic to apply to this metric.
        Either of the following is supported: `SampleCount`, `Average`, `Sum`, `Minimum`, `Maximum`
        """
        ...

    @stat.setter
    def stat(self, value: pulumi.Input[str]):
        ...

    @property
    @pulumi.getter
    def dimensions(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        The dimensions for this metric.  For the list of available dimensions see the AWS documentation [here](http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CW_Support_For_AWS.html).
        """
        ...

    @dimensions.setter
    def dimensions(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        ...

    @property
    @pulumi.getter
    def namespace(self) -> Optional[pulumi.Input[str]]:
        """
        The namespace for this metric. See docs for the [list of namespaces](https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/aws-namespaces.html).
        See docs for [supported metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CW_Support_For_AWS.html).
        """
        ...

    @namespace.setter
    def namespace(self, value: Optional[pulumi.Input[str]]):
        ...

    @property
    @pulumi.getter
    def unit(self) -> Optional[pulumi.Input[str]]:
        """
        The unit for this metric.
        """
        ...

    @unit.setter
    def unit(self, value: Optional[pulumi.Input[str]]):
        ...

