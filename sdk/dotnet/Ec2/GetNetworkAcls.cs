// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.Ec2
{
    public static class GetNetworkAcls
    {
        /// <summary>
        /// {{% examples %}}
        /// ## Example Usage
        /// {{% example %}}
        /// 
        /// The following shows outputing all network ACL ids in a vpc.
        /// 
        /// ```csharp
        /// using Pulumi;
        /// using Aws = Pulumi.Aws;
        /// 
        /// class MyStack : Stack
        /// {
        ///     public MyStack()
        ///     {
        ///         var exampleNetworkAcls = Output.Create(Aws.Ec2.GetNetworkAcls.InvokeAsync(new Aws.Ec2.GetNetworkAclsArgs
        ///         {
        ///             VpcId = @var.Vpc_id,
        ///         }));
        ///         this.Example = exampleNetworkAcls.Apply(exampleNetworkAcls =&gt; exampleNetworkAcls.Ids);
        ///     }
        /// 
        ///     [Output("example")]
        ///     public Output&lt;string&gt; Example { get; set; }
        /// }
        /// ```
        /// 
        /// The following example retrieves a list of all network ACL ids in a VPC with a custom
        /// tag of `Tier` set to a value of "Private".
        /// 
        /// ```csharp
        /// using Pulumi;
        /// using Aws = Pulumi.Aws;
        /// 
        /// class MyStack : Stack
        /// {
        ///     public MyStack()
        ///     {
        ///         var example = Output.Create(Aws.Ec2.GetNetworkAcls.InvokeAsync(new Aws.Ec2.GetNetworkAclsArgs
        ///         {
        ///             VpcId = @var.Vpc_id,
        ///             Tags = 
        ///             {
        ///                 { "Tier", "Private" },
        ///             },
        ///         }));
        ///     }
        /// 
        /// }
        /// ```
        /// 
        /// The following example retrieves a network ACL id in a VPC which associated
        /// with specific subnet.
        /// 
        /// ```csharp
        /// using Pulumi;
        /// using Aws = Pulumi.Aws;
        /// 
        /// class MyStack : Stack
        /// {
        ///     public MyStack()
        ///     {
        ///         var example = Output.Create(Aws.Ec2.GetNetworkAcls.InvokeAsync(new Aws.Ec2.GetNetworkAclsArgs
        ///         {
        ///             VpcId = @var.Vpc_id,
        ///             Filters = 
        ///             {
        ///                 new Aws.Ec2.Inputs.GetNetworkAclsFilterArgs
        ///                 {
        ///                     Name = "association.subnet-id",
        ///                     Values = 
        ///                     {
        ///                         aws_subnet.Test.Id,
        ///                     },
        ///                 },
        ///             },
        ///         }));
        ///     }
        /// 
        /// }
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Task<GetNetworkAclsResult> InvokeAsync(GetNetworkAclsArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetNetworkAclsResult>("aws:ec2/getNetworkAcls:getNetworkAcls", args ?? new GetNetworkAclsArgs(), options.WithDefaults());

        /// <summary>
        /// {{% examples %}}
        /// ## Example Usage
        /// {{% example %}}
        /// 
        /// The following shows outputing all network ACL ids in a vpc.
        /// 
        /// ```csharp
        /// using Pulumi;
        /// using Aws = Pulumi.Aws;
        /// 
        /// class MyStack : Stack
        /// {
        ///     public MyStack()
        ///     {
        ///         var exampleNetworkAcls = Output.Create(Aws.Ec2.GetNetworkAcls.InvokeAsync(new Aws.Ec2.GetNetworkAclsArgs
        ///         {
        ///             VpcId = @var.Vpc_id,
        ///         }));
        ///         this.Example = exampleNetworkAcls.Apply(exampleNetworkAcls =&gt; exampleNetworkAcls.Ids);
        ///     }
        /// 
        ///     [Output("example")]
        ///     public Output&lt;string&gt; Example { get; set; }
        /// }
        /// ```
        /// 
        /// The following example retrieves a list of all network ACL ids in a VPC with a custom
        /// tag of `Tier` set to a value of "Private".
        /// 
        /// ```csharp
        /// using Pulumi;
        /// using Aws = Pulumi.Aws;
        /// 
        /// class MyStack : Stack
        /// {
        ///     public MyStack()
        ///     {
        ///         var example = Output.Create(Aws.Ec2.GetNetworkAcls.InvokeAsync(new Aws.Ec2.GetNetworkAclsArgs
        ///         {
        ///             VpcId = @var.Vpc_id,
        ///             Tags = 
        ///             {
        ///                 { "Tier", "Private" },
        ///             },
        ///         }));
        ///     }
        /// 
        /// }
        /// ```
        /// 
        /// The following example retrieves a network ACL id in a VPC which associated
        /// with specific subnet.
        /// 
        /// ```csharp
        /// using Pulumi;
        /// using Aws = Pulumi.Aws;
        /// 
        /// class MyStack : Stack
        /// {
        ///     public MyStack()
        ///     {
        ///         var example = Output.Create(Aws.Ec2.GetNetworkAcls.InvokeAsync(new Aws.Ec2.GetNetworkAclsArgs
        ///         {
        ///             VpcId = @var.Vpc_id,
        ///             Filters = 
        ///             {
        ///                 new Aws.Ec2.Inputs.GetNetworkAclsFilterArgs
        ///                 {
        ///                     Name = "association.subnet-id",
        ///                     Values = 
        ///                     {
        ///                         aws_subnet.Test.Id,
        ///                     },
        ///                 },
        ///             },
        ///         }));
        ///     }
        /// 
        /// }
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Output<GetNetworkAclsResult> Invoke(GetNetworkAclsInvokeArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetNetworkAclsResult>("aws:ec2/getNetworkAcls:getNetworkAcls", args ?? new GetNetworkAclsInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetNetworkAclsArgs : Pulumi.InvokeArgs
    {
        [Input("filters")]
        private List<Inputs.GetNetworkAclsFilterArgs>? _filters;

        /// <summary>
        /// Custom filter block as described below.
        /// </summary>
        public List<Inputs.GetNetworkAclsFilterArgs> Filters
        {
            get => _filters ?? (_filters = new List<Inputs.GetNetworkAclsFilterArgs>());
            set => _filters = value;
        }

        [Input("tags")]
        private Dictionary<string, string>? _tags;

        /// <summary>
        /// A map of tags, each pair of which must exactly match
        /// a pair on the desired network ACLs.
        /// </summary>
        public Dictionary<string, string> Tags
        {
            get => _tags ?? (_tags = new Dictionary<string, string>());
            set => _tags = value;
        }

        /// <summary>
        /// The VPC ID that you want to filter from.
        /// </summary>
        [Input("vpcId")]
        public string? VpcId { get; set; }

        public GetNetworkAclsArgs()
        {
        }
    }

    public sealed class GetNetworkAclsInvokeArgs : Pulumi.InvokeArgs
    {
        [Input("filters")]
        private InputList<Inputs.GetNetworkAclsFilterInputArgs>? _filters;

        /// <summary>
        /// Custom filter block as described below.
        /// </summary>
        public InputList<Inputs.GetNetworkAclsFilterInputArgs> Filters
        {
            get => _filters ?? (_filters = new InputList<Inputs.GetNetworkAclsFilterInputArgs>());
            set => _filters = value;
        }

        [Input("tags")]
        private InputMap<string>? _tags;

        /// <summary>
        /// A map of tags, each pair of which must exactly match
        /// a pair on the desired network ACLs.
        /// </summary>
        public InputMap<string> Tags
        {
            get => _tags ?? (_tags = new InputMap<string>());
            set => _tags = value;
        }

        /// <summary>
        /// The VPC ID that you want to filter from.
        /// </summary>
        [Input("vpcId")]
        public Input<string>? VpcId { get; set; }

        public GetNetworkAclsInvokeArgs()
        {
        }
    }


    [OutputType]
    public sealed class GetNetworkAclsResult
    {
        public readonly ImmutableArray<Outputs.GetNetworkAclsFilterResult> Filters;
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// A list of all the network ACL ids found. This data source will fail if none are found.
        /// </summary>
        public readonly ImmutableArray<string> Ids;
        public readonly ImmutableDictionary<string, string> Tags;
        public readonly string? VpcId;

        [OutputConstructor]
        private GetNetworkAclsResult(
            ImmutableArray<Outputs.GetNetworkAclsFilterResult> filters,

            string id,

            ImmutableArray<string> ids,

            ImmutableDictionary<string, string> tags,

            string? vpcId)
        {
            Filters = filters;
            Id = id;
            Ids = ids;
            Tags = tags;
            VpcId = vpcId;
        }
    }
}
