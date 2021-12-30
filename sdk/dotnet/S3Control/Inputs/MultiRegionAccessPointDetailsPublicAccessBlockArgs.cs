// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.S3Control.Inputs
{

    public sealed class MultiRegionAccessPointDetailsPublicAccessBlockArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Whether Amazon S3 should block public ACLs for buckets in this account. Defaults to `true`. Enabling this setting does not affect existing policies or ACLs. When set to `true` causes the following behavior:
        /// * PUT Bucket acl and PUT Object acl calls fail if the specified ACL is public.
        /// * PUT Object calls fail if the request includes a public ACL.
        /// * PUT Bucket calls fail if the request includes a public ACL.
        /// </summary>
        [Input("blockPublicAcls")]
        public Input<bool>? BlockPublicAcls { get; set; }

        /// <summary>
        /// Whether Amazon S3 should block public bucket policies for buckets in this account. Defaults to `true`. Enabling this setting does not affect existing bucket policies. When set to `true` causes Amazon S3 to:
        /// * Reject calls to PUT Bucket policy if the specified bucket policy allows public access.
        /// </summary>
        [Input("blockPublicPolicy")]
        public Input<bool>? BlockPublicPolicy { get; set; }

        /// <summary>
        /// Whether Amazon S3 should ignore public ACLs for buckets in this account. Defaults to `true`. Enabling this setting does not affect the persistence of any existing ACLs and doesn't prevent new public ACLs from being set. When set to `true` causes Amazon S3 to:
        /// * Ignore all public ACLs on buckets in this account and any objects that they contain.
        /// </summary>
        [Input("ignorePublicAcls")]
        public Input<bool>? IgnorePublicAcls { get; set; }

        /// <summary>
        /// Whether Amazon S3 should restrict public bucket policies for buckets in this account. Defaults to `true`. Enabling this setting does not affect previously stored bucket policies, except that public and cross-account access within any public bucket policy, including non-public delegation to specific accounts, is blocked. When set to `true`:
        /// * Only the bucket owner and AWS Services can access buckets with public policies.
        /// </summary>
        [Input("restrictPublicBuckets")]
        public Input<bool>? RestrictPublicBuckets { get; set; }

        public MultiRegionAccessPointDetailsPublicAccessBlockArgs()
        {
        }
    }
}