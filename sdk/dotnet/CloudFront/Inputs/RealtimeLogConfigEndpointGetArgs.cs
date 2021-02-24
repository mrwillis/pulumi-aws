// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.CloudFront.Inputs
{

    public sealed class RealtimeLogConfigEndpointGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The Amazon Kinesis data stream configuration.
        /// </summary>
        [Input("kinesisStreamConfig", required: true)]
        public Input<Inputs.RealtimeLogConfigEndpointKinesisStreamConfigGetArgs> KinesisStreamConfig { get; set; } = null!;

        /// <summary>
        /// The type of data stream where real-time log data is sent. The only valid value is `Kinesis`.
        /// </summary>
        [Input("streamType", required: true)]
        public Input<string> StreamType { get; set; } = null!;

        public RealtimeLogConfigEndpointGetArgs()
        {
        }
    }
}