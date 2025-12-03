2025-12-03 Version: 2.0.0
- Support API AttachVscToMountPoints.
- Support API CreateQosPolicy.
- Support API DeleteQosPolicy.
- Support API DescribeMountPointsVscAttachInfo.
- Support API ListFederations.
- Support API ListQosPolicies.
- Support API ModifyQosPolicy.
- Update API AttachVscMountPoint: add request parameters UseAssumeRoleChkServerPerm.
- Update API AttachVscMountPoint: add request parameters VscName.
- Update API CreateFileSystem: add request parameters DedicatedClusterId.
- Update API CreateMountPoint: add request parameters UsePerformanceMode.
- Update API DeleteUserGroupsMapping: update request parameters GroupNames' type has changed.
- Update API DeleteUserGroupsMapping: update request parameters GroupNames' parseType has changed.
- Update API DescribeVscMountPoints: add response parameters Body.MountPoints.$.Instances.$.Vscs.$.VscName.
- Update API DetachVscMountPoint: add request parameters UseAssumeRoleChkServerPerm.
- Update API GetMountPoint: add response parameters Body.MountPoint.MountPointAlias.
- Update API ListAccessGroups: add request parameters NextToken.
- Update API ListAccessGroups: add response parameters Body.NextToken.
- Update API ListAccessRules: add request parameters NextToken.
- Update API ListAccessRules: add response parameters Body.NextToken.
- Update API ListFileSystems: add request parameters NextToken.
- Update API ListFileSystems: add response parameters Body.NextToken.
- Update API ListMountPoints: add request parameters NextToken.
- Update API ListMountPoints: add response parameters Body.NextToken.
- Update API ListMountPoints: add response parameters Body.MountPoints.$.MountPointAlias.


2024-04-07 Version: 1.0.2
- Update API AttachVscMountPoint: update param InstanceIds.
- Update API CreateVscMountPoint: update param InstanceIds.
- Update API DetachVscMountPoint: update param InstanceIds.


2024-03-29 Version: 1.0.1
- Update API AttachVscMountPoint: update param InstanceIds.
- Update API AttachVscMountPoint: update param VscIds.
- Update API CreateUserGroupsMapping: update response param.
- Update API CreateVscMountPoint: update param InstanceIds.
- Update API DetachVscMountPoint: update param InstanceIds.
- Update API DetachVscMountPoint: update param VscIds.


2022-05-06 Version: 1.0.0
- Initial release.

