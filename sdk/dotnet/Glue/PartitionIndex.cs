// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.Glue
{
    /// <summary>
    /// ## Example Usage
    /// 
    /// ```csharp
    /// using Pulumi;
    /// using Aws = Pulumi.Aws;
    /// 
    /// class MyStack : Stack
    /// {
    ///     public MyStack()
    ///     {
    ///         var exampleCatalogDatabase = new Aws.Glue.CatalogDatabase("exampleCatalogDatabase", new Aws.Glue.CatalogDatabaseArgs
    ///         {
    ///             Name = "example",
    ///         });
    ///         var exampleCatalogTable = new Aws.Glue.CatalogTable("exampleCatalogTable", new Aws.Glue.CatalogTableArgs
    ///         {
    ///             Name = "example",
    ///             DatabaseName = exampleCatalogDatabase.Name,
    ///             Owner = "my_owner",
    ///             Retention = 1,
    ///             TableType = "VIRTUAL_VIEW",
    ///             ViewExpandedText = "view_expanded_text_1",
    ///             ViewOriginalText = "view_original_text_1",
    ///             StorageDescriptor = new Aws.Glue.Inputs.CatalogTableStorageDescriptorArgs
    ///             {
    ///                 BucketColumns = 
    ///                 {
    ///                     "bucket_column_1",
    ///                 },
    ///                 Compressed = false,
    ///                 InputFormat = "SequenceFileInputFormat",
    ///                 Location = "my_location",
    ///                 NumberOfBuckets = 1,
    ///                 OutputFormat = "SequenceFileInputFormat",
    ///                 StoredAsSubDirectories = false,
    ///                 Parameters = 
    ///                 {
    ///                     { "param1", "param1_val" },
    ///                 },
    ///                 Columns = 
    ///                 {
    ///                     new Aws.Glue.Inputs.CatalogTableStorageDescriptorColumnArgs
    ///                     {
    ///                         Name = "my_column_1",
    ///                         Type = "int",
    ///                         Comment = "my_column1_comment",
    ///                     },
    ///                     new Aws.Glue.Inputs.CatalogTableStorageDescriptorColumnArgs
    ///                     {
    ///                         Name = "my_column_2",
    ///                         Type = "string",
    ///                         Comment = "my_column2_comment",
    ///                     },
    ///                 },
    ///                 SerDeInfo = new Aws.Glue.Inputs.CatalogTableStorageDescriptorSerDeInfoArgs
    ///                 {
    ///                     Name = "ser_de_name",
    ///                     Parameters = 
    ///                     {
    ///                         { "param1", "param_val_1" },
    ///                     },
    ///                     SerializationLibrary = "org.apache.hadoop.hive.serde2.columnar.ColumnarSerDe",
    ///                 },
    ///                 SortColumns = 
    ///                 {
    ///                     new Aws.Glue.Inputs.CatalogTableStorageDescriptorSortColumnArgs
    ///                     {
    ///                         Column = "my_column_1",
    ///                         SortOrder = 1,
    ///                     },
    ///                 },
    ///                 SkewedInfo = new Aws.Glue.Inputs.CatalogTableStorageDescriptorSkewedInfoArgs
    ///                 {
    ///                     SkewedColumnNames = 
    ///                     {
    ///                         "my_column_1",
    ///                     },
    ///                     SkewedColumnValueLocationMaps = 
    ///                     {
    ///                         { "my_column_1", "my_column_1_val_loc_map" },
    ///                     },
    ///                     SkewedColumnValues = 
    ///                     {
    ///                         "skewed_val_1",
    ///                     },
    ///                 },
    ///             },
    ///             PartitionKeys = 
    ///             {
    ///                 new Aws.Glue.Inputs.CatalogTablePartitionKeyArgs
    ///                 {
    ///                     Name = "my_column_1",
    ///                     Type = "int",
    ///                     Comment = "my_column_1_comment",
    ///                 },
    ///                 new Aws.Glue.Inputs.CatalogTablePartitionKeyArgs
    ///                 {
    ///                     Name = "my_column_2",
    ///                     Type = "string",
    ///                     Comment = "my_column_2_comment",
    ///                 },
    ///             },
    ///             Parameters = 
    ///             {
    ///                 { "param1", "param1_val" },
    ///             },
    ///         });
    ///         var examplePartitionIndex = new Aws.Glue.PartitionIndex("examplePartitionIndex", new Aws.Glue.PartitionIndexArgs
    ///         {
    ///             DatabaseName = exampleCatalogDatabase.Name,
    ///             TableName = exampleCatalogTable.Name,
    ///             PartitionIndex = new Aws.Glue.Inputs.PartitionIndexPartitionIndexArgs
    ///             {
    ///                 IndexName = "example",
    ///                 Keys = 
    ///                 {
    ///                     "my_column_1",
    ///                     "my_column_2",
    ///                 },
    ///             },
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// 
    /// ## Import
    /// 
    /// Glue Partition Indexes can be imported with their catalog ID (usually AWS account ID), database name, table name, and index name, e.g.
    /// 
    /// ```sh
    ///  $ pulumi import aws:glue/partitionIndex:PartitionIndex example 123456789012:MyDatabase:MyTable:index-name
    /// ```
    /// </summary>
    [AwsResourceType("aws:glue/partitionIndex:PartitionIndex")]
    public partial class PartitionIndex : Pulumi.CustomResource
    {
        /// <summary>
        /// The catalog ID where the table resides.
        /// </summary>
        [Output("catalogId")]
        public Output<string> CatalogId { get; private set; } = null!;

        /// <summary>
        /// Name of the metadata database where the table metadata resides. For Hive compatibility, this must be all lowercase.
        /// </summary>
        [Output("databaseName")]
        public Output<string> DatabaseName { get; private set; } = null!;

        /// <summary>
        /// Configuration block for a partition index. See `partition_index` below.
        /// </summary>
        [Output("partitionIndex")]
        public Output<Outputs.PartitionIndexPartitionIndex> PartitionIndexConfig { get; private set; } = null!;

        /// <summary>
        /// Name of the table. For Hive compatibility, this must be entirely lowercase.
        /// </summary>
        [Output("tableName")]
        public Output<string> TableName { get; private set; } = null!;


        /// <summary>
        /// Create a PartitionIndex resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public PartitionIndex(string name, PartitionIndexArgs args, CustomResourceOptions? options = null)
            : base("aws:glue/partitionIndex:PartitionIndex", name, args ?? new PartitionIndexArgs(), MakeResourceOptions(options, ""))
        {
        }

        private PartitionIndex(string name, Input<string> id, PartitionIndexState? state = null, CustomResourceOptions? options = null)
            : base("aws:glue/partitionIndex:PartitionIndex", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing PartitionIndex resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static PartitionIndex Get(string name, Input<string> id, PartitionIndexState? state = null, CustomResourceOptions? options = null)
        {
            return new PartitionIndex(name, id, state, options);
        }
    }

    public sealed class PartitionIndexArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The catalog ID where the table resides.
        /// </summary>
        [Input("catalogId")]
        public Input<string>? CatalogId { get; set; }

        /// <summary>
        /// Name of the metadata database where the table metadata resides. For Hive compatibility, this must be all lowercase.
        /// </summary>
        [Input("databaseName", required: true)]
        public Input<string> DatabaseName { get; set; } = null!;

        /// <summary>
        /// Configuration block for a partition index. See `partition_index` below.
        /// </summary>
        [Input("partitionIndex", required: true)]
        public Input<Inputs.PartitionIndexPartitionIndexArgs> PartitionIndexConfig { get; set; } = null!;

        /// <summary>
        /// Name of the table. For Hive compatibility, this must be entirely lowercase.
        /// </summary>
        [Input("tableName", required: true)]
        public Input<string> TableName { get; set; } = null!;

        public PartitionIndexArgs()
        {
        }
    }

    public sealed class PartitionIndexState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The catalog ID where the table resides.
        /// </summary>
        [Input("catalogId")]
        public Input<string>? CatalogId { get; set; }

        /// <summary>
        /// Name of the metadata database where the table metadata resides. For Hive compatibility, this must be all lowercase.
        /// </summary>
        [Input("databaseName")]
        public Input<string>? DatabaseName { get; set; }

        /// <summary>
        /// Configuration block for a partition index. See `partition_index` below.
        /// </summary>
        [Input("partitionIndex")]
        public Input<Inputs.PartitionIndexPartitionIndexGetArgs>? PartitionIndexConfig { get; set; }

        /// <summary>
        /// Name of the table. For Hive compatibility, this must be entirely lowercase.
        /// </summary>
        [Input("tableName")]
        public Input<string>? TableName { get; set; }

        public PartitionIndexState()
        {
        }
    }
}