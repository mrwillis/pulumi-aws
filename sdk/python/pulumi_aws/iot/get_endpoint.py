# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime

class GetEndpointResult(object):
    """
    A collection of values returned by getEndpoint.
    """
    def __init__(__self__, endpoint_address=None, id=None):
        if endpoint_address and not isinstance(endpoint_address, basestring):
            raise TypeError('Expected argument endpoint_address to be a basestring')
        __self__.endpoint_address = endpoint_address
        """
        The endpoint. The format of the endpoint is as follows: `IDENTIFIER.iot.REGION.amazonaws.com`.
        """
        if id and not isinstance(id, basestring):
            raise TypeError('Expected argument id to be a basestring')
        __self__.id = id
        """
        id is the provider-assigned unique ID for this managed resource.
        """

def get_endpoint():
    """
    Returns a unique endpoint specific to the AWS account making the call.
    """
    __args__ = dict()

    __ret__ = pulumi.runtime.invoke('aws:iot/getEndpoint:getEndpoint', __args__)

    return GetEndpointResult(
        endpoint_address=__ret__.get('endpointAddress'),
        id=__ret__.get('id'))