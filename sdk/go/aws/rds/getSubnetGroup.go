// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package rds

import (
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Use this data source to get information about an RDS subnet group.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-aws/sdk/v3/go/aws/rds"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		_, err := rds.LookupSubnetGroup(ctx, &rds.LookupSubnetGroupArgs{
// 			Name: "my-test-database-subnet-group",
// 		}, nil)
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
func LookupSubnetGroup(ctx *pulumi.Context, args *LookupSubnetGroupArgs, opts ...pulumi.InvokeOption) (*LookupSubnetGroupResult, error) {
	var rv LookupSubnetGroupResult
	err := ctx.Invoke("aws:rds/getSubnetGroup:getSubnetGroup", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getSubnetGroup.
type LookupSubnetGroupArgs struct {
	// The name of the RDS database subnet group.
	Name string `pulumi:"name"`
}

// A collection of values returned by getSubnetGroup.
type LookupSubnetGroupResult struct {
	// The Amazon Resource Name (ARN) for the DB subnet group.
	Arn string `pulumi:"arn"`
	// Provides the description of the DB subnet group.
	Description string `pulumi:"description"`
	// The provider-assigned unique ID for this managed resource.
	Id   string `pulumi:"id"`
	Name string `pulumi:"name"`
	// Provides the status of the DB subnet group.
	Status string `pulumi:"status"`
	// Contains a list of subnet identifiers.
	SubnetIds []string `pulumi:"subnetIds"`
	// Provides the VPC ID of the subnet group.
	VpcId string `pulumi:"vpcId"`
}