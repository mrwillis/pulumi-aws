# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'CustomPluginLocationArgs',
    'CustomPluginLocationS3Args',
]

@pulumi.input_type
class CustomPluginLocationArgs:
    def __init__(__self__, *,
                 s3: pulumi.Input['CustomPluginLocationS3Args']):
        """
        :param pulumi.Input['CustomPluginLocationS3Args'] s3: Information of the plugin file stored in Amazon S3. See below.
        """
        pulumi.set(__self__, "s3", s3)

    @property
    @pulumi.getter
    def s3(self) -> pulumi.Input['CustomPluginLocationS3Args']:
        """
        Information of the plugin file stored in Amazon S3. See below.
        """
        return pulumi.get(self, "s3")

    @s3.setter
    def s3(self, value: pulumi.Input['CustomPluginLocationS3Args']):
        pulumi.set(self, "s3", value)


@pulumi.input_type
class CustomPluginLocationS3Args:
    def __init__(__self__, *,
                 bucket_arn: pulumi.Input[str],
                 file_key: pulumi.Input[str],
                 object_version: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] bucket_arn: The Amazon Resource Name (ARN) of an S3 bucket.
        :param pulumi.Input[str] file_key: The file key for an object in an S3 bucket.
        :param pulumi.Input[str] object_version: The version of an object in an S3 bucket.
        """
        pulumi.set(__self__, "bucket_arn", bucket_arn)
        pulumi.set(__self__, "file_key", file_key)
        if object_version is not None:
            pulumi.set(__self__, "object_version", object_version)

    @property
    @pulumi.getter(name="bucketArn")
    def bucket_arn(self) -> pulumi.Input[str]:
        """
        The Amazon Resource Name (ARN) of an S3 bucket.
        """
        return pulumi.get(self, "bucket_arn")

    @bucket_arn.setter
    def bucket_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "bucket_arn", value)

    @property
    @pulumi.getter(name="fileKey")
    def file_key(self) -> pulumi.Input[str]:
        """
        The file key for an object in an S3 bucket.
        """
        return pulumi.get(self, "file_key")

    @file_key.setter
    def file_key(self, value: pulumi.Input[str]):
        pulumi.set(self, "file_key", value)

    @property
    @pulumi.getter(name="objectVersion")
    def object_version(self) -> Optional[pulumi.Input[str]]:
        """
        The version of an object in an S3 bucket.
        """
        return pulumi.get(self, "object_version")

    @object_version.setter
    def object_version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "object_version", value)


