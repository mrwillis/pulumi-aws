// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.AppMesh.Outputs
{

    [OutputType]
    public sealed class GatewayRouteSpecGrpcRoute
    {
        /// <summary>
        /// The action to take if a match is determined.
        /// </summary>
        public readonly Outputs.GatewayRouteSpecGrpcRouteAction Action;
        /// <summary>
        /// The criteria for determining a request match.
        /// </summary>
        public readonly Outputs.GatewayRouteSpecGrpcRouteMatch Match;

        [OutputConstructor]
        private GatewayRouteSpecGrpcRoute(
            Outputs.GatewayRouteSpecGrpcRouteAction action,

            Outputs.GatewayRouteSpecGrpcRouteMatch match)
        {
            Action = action;
            Match = match;
        }
    }
}