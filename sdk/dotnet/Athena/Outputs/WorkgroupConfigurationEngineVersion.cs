// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.Athena.Outputs
{

    [OutputType]
    public sealed class WorkgroupConfigurationEngineVersion
    {
        /// <summary>
        /// The engine version on which the query runs. If `selected_engine_version` is set to `AUTO`, the effective engine version is chosen by Athena.
        /// </summary>
        public readonly string? EffectiveEngineVersion;
        /// <summary>
        /// The requested engine version. Defaults to `AUTO`.
        /// </summary>
        public readonly string? SelectedEngineVersion;

        [OutputConstructor]
        private WorkgroupConfigurationEngineVersion(
            string? effectiveEngineVersion,

            string? selectedEngineVersion)
        {
            EffectiveEngineVersion = effectiveEngineVersion;
            SelectedEngineVersion = selectedEngineVersion;
        }
    }
}