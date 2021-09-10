// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.Route53RecoveryControl.Inputs
{

    public sealed class ClusterClusterEndpointArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Cluster endpoint.
        /// </summary>
        [Input("endpoint")]
        public Input<string>? Endpoint { get; set; }

        /// <summary>
        /// Region of the endpoint.
        /// </summary>
        [Input("region")]
        public Input<string>? Region { get; set; }

        public ClusterClusterEndpointArgs()
        {
        }
    }
}