# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from .. import _utilities, _tables

__all__ = [
    'ClusterClusterCertificateArgs',
]

@pulumi.input_type
class ClusterClusterCertificateArgs:
    def __init__(__self__, *,
                 aws_hardware_certificate: Optional[pulumi.Input[str]] = None,
                 cluster_certificate: Optional[pulumi.Input[str]] = None,
                 cluster_csr: Optional[pulumi.Input[str]] = None,
                 hsm_certificate: Optional[pulumi.Input[str]] = None,
                 manufacturer_hardware_certificate: Optional[pulumi.Input[str]] = None):
        pulumi.set(__self__, "awsHardwareCertificate", aws_hardware_certificate)
        pulumi.set(__self__, "clusterCertificate", cluster_certificate)
        pulumi.set(__self__, "clusterCsr", cluster_csr)
        pulumi.set(__self__, "hsmCertificate", hsm_certificate)
        pulumi.set(__self__, "manufacturerHardwareCertificate", manufacturer_hardware_certificate)

    @property
    @pulumi.getter(name="awsHardwareCertificate")
    def aws_hardware_certificate(self) -> Optional[pulumi.Input[str]]:
        ...

    @aws_hardware_certificate.setter
    def aws_hardware_certificate(self, value: Optional[pulumi.Input[str]]):
        ...

    @property
    @pulumi.getter(name="clusterCertificate")
    def cluster_certificate(self) -> Optional[pulumi.Input[str]]:
        ...

    @cluster_certificate.setter
    def cluster_certificate(self, value: Optional[pulumi.Input[str]]):
        ...

    @property
    @pulumi.getter(name="clusterCsr")
    def cluster_csr(self) -> Optional[pulumi.Input[str]]:
        ...

    @cluster_csr.setter
    def cluster_csr(self, value: Optional[pulumi.Input[str]]):
        ...

    @property
    @pulumi.getter(name="hsmCertificate")
    def hsm_certificate(self) -> Optional[pulumi.Input[str]]:
        ...

    @hsm_certificate.setter
    def hsm_certificate(self, value: Optional[pulumi.Input[str]]):
        ...

    @property
    @pulumi.getter(name="manufacturerHardwareCertificate")
    def manufacturer_hardware_certificate(self) -> Optional[pulumi.Input[str]]:
        ...

    @manufacturer_hardware_certificate.setter
    def manufacturer_hardware_certificate(self, value: Optional[pulumi.Input[str]]):
        ...

