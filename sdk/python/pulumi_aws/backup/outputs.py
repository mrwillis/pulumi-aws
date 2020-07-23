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
    'PlanRule',
    'PlanRuleCopyAction',
    'PlanRuleCopyActionLifecycle',
    'PlanRuleLifecycle',
    'SelectionSelectionTag',
]

@pulumi.output_type
class PlanRule(dict):
    @property
    @pulumi.getter(name="completionWindow")
    def completion_window(self) -> Optional[float]:
        """
        The amount of time AWS Backup attempts a backup before canceling the job and returning an error.
        """
        ...

    @property
    @pulumi.getter(name="copyActions")
    def copy_actions(self) -> Optional[List['outputs.PlanRuleCopyAction']]:
        """
        Configuration block(s) with copy operation settings. Detailed below.
        """
        ...

    @property
    @pulumi.getter
    def lifecycle(self) -> Optional['outputs.PlanRuleLifecycle']:
        """
        The lifecycle defines when a protected resource is copied over to a backup vault and when it expires.  Fields documented above.
        """
        ...

    @property
    @pulumi.getter(name="recoveryPointTags")
    def recovery_point_tags(self) -> Optional[Mapping[str, str]]:
        """
        Metadata that you can assign to help organize the resources that you create.
        """
        ...

    @property
    @pulumi.getter(name="ruleName")
    def rule_name(self) -> str:
        """
        An display name for a backup rule.
        """
        ...

    @property
    @pulumi.getter
    def schedule(self) -> Optional[str]:
        """
        A CRON expression specifying when AWS Backup initiates a backup job.
        """
        ...

    @property
    @pulumi.getter(name="startWindow")
    def start_window(self) -> Optional[float]:
        """
        The amount of time in minutes before beginning a backup.
        """
        ...

    @property
    @pulumi.getter(name="targetVaultName")
    def target_vault_name(self) -> str:
        """
        The name of a logical container where backups are stored.
        """
        ...

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class PlanRuleCopyAction(dict):
    @property
    @pulumi.getter(name="destinationVaultArn")
    def destination_vault_arn(self) -> str:
        """
        An Amazon Resource Name (ARN) that uniquely identifies the destination backup vault for the copied backup.
        """
        ...

    @property
    @pulumi.getter
    def lifecycle(self) -> Optional['outputs.PlanRuleCopyActionLifecycle']:
        """
        The lifecycle defines when a protected resource is copied over to a backup vault and when it expires.  Fields documented above.
        """
        ...

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class PlanRuleCopyActionLifecycle(dict):
    @property
    @pulumi.getter(name="coldStorageAfter")
    def cold_storage_after(self) -> Optional[float]:
        """
        Specifies the number of days after creation that a recovery point is moved to cold storage.
        """
        ...

    @property
    @pulumi.getter(name="deleteAfter")
    def delete_after(self) -> Optional[float]:
        """
        Specifies the number of days after creation that a recovery point is deleted. Must be 90 days greater than `cold_storage_after`.
        """
        ...

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class PlanRuleLifecycle(dict):
    @property
    @pulumi.getter(name="coldStorageAfter")
    def cold_storage_after(self) -> Optional[float]:
        """
        Specifies the number of days after creation that a recovery point is moved to cold storage.
        """
        ...

    @property
    @pulumi.getter(name="deleteAfter")
    def delete_after(self) -> Optional[float]:
        """
        Specifies the number of days after creation that a recovery point is deleted. Must be 90 days greater than `cold_storage_after`.
        """
        ...

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class SelectionSelectionTag(dict):
    @property
    @pulumi.getter
    def key(self) -> str:
        """
        The key in a key-value pair.
        """
        ...

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        An operation, such as `StringEquals`, that is applied to a key-value pair used to filter resources in a selection.
        """
        ...

    @property
    @pulumi.getter
    def value(self) -> str:
        """
        The value in a key-value pair.
        """
        ...

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

