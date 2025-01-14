// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

// Export members:
export * from "./getAuthorizationToken";
export * from "./getCredentials";
export * from "./getImage";
export * from "./getRepository";
export * from "./lifecyclePolicy";
export * from "./lifecyclePolicyDocument";
export * from "./pullThroughCacheRule";
export * from "./registryPolicy";
export * from "./registryScanningConfiguration";
export * from "./replicationConfiguration";
export * from "./repository";
export * from "./repositoryPolicy";

// Import resources to register:
import { LifecyclePolicy } from "./lifecyclePolicy";
import { PullThroughCacheRule } from "./pullThroughCacheRule";
import { RegistryPolicy } from "./registryPolicy";
import { RegistryScanningConfiguration } from "./registryScanningConfiguration";
import { ReplicationConfiguration } from "./replicationConfiguration";
import { Repository } from "./repository";
import { RepositoryPolicy } from "./repositoryPolicy";

const _module = {
    version: utilities.getVersion(),
    construct: (name: string, type: string, urn: string): pulumi.Resource => {
        switch (type) {
            case "aws:ecr/lifecyclePolicy:LifecyclePolicy":
                return new LifecyclePolicy(name, <any>undefined, { urn })
            case "aws:ecr/pullThroughCacheRule:PullThroughCacheRule":
                return new PullThroughCacheRule(name, <any>undefined, { urn })
            case "aws:ecr/registryPolicy:RegistryPolicy":
                return new RegistryPolicy(name, <any>undefined, { urn })
            case "aws:ecr/registryScanningConfiguration:RegistryScanningConfiguration":
                return new RegistryScanningConfiguration(name, <any>undefined, { urn })
            case "aws:ecr/replicationConfiguration:ReplicationConfiguration":
                return new ReplicationConfiguration(name, <any>undefined, { urn })
            case "aws:ecr/repository:Repository":
                return new Repository(name, <any>undefined, { urn })
            case "aws:ecr/repositoryPolicy:RepositoryPolicy":
                return new RepositoryPolicy(name, <any>undefined, { urn })
            default:
                throw new Error(`unknown resource type ${type}`);
        }
    },
};
pulumi.runtime.registerResourceModule("aws", "ecr/lifecyclePolicy", _module)
pulumi.runtime.registerResourceModule("aws", "ecr/pullThroughCacheRule", _module)
pulumi.runtime.registerResourceModule("aws", "ecr/registryPolicy", _module)
pulumi.runtime.registerResourceModule("aws", "ecr/registryScanningConfiguration", _module)
pulumi.runtime.registerResourceModule("aws", "ecr/replicationConfiguration", _module)
pulumi.runtime.registerResourceModule("aws", "ecr/repository", _module)
pulumi.runtime.registerResourceModule("aws", "ecr/repositoryPolicy", _module)
