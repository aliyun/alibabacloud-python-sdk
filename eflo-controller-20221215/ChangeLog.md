2025-07-14 Version: 2.5.4
- Update API CreateCluster: add request parameters NodeGroups.$.VirtualGpuEnabled.
- Update API CreateNodeGroup: add request parameters NodeGroup.VirtualGpuEnabled.
- Update API ListNodeGroups: add response parameters Body.Groups.$.VirtualGpuEnabled.


2025-06-20 Version: 2.5.3
- Update API CreateCluster: add request parameters NodeGroups.$.Nodes.$.DataDisk.
- Update API ExtendCluster: add request parameters NodeGroups.$.Nodes.$.DataDisk.


2025-05-30 Version: 2.5.2
- Update API CreateCluster: add request parameters NodeGroups.$.LoginPassword.
- Update API CreateNodeGroup: add request parameters NodeGroup.LoginPassword.
- Update API UpdateNodeGroup: add request parameters LoginPassword.


2025-05-20 Version: 2.5.1
- Update API UpdateNodeGroup: add request parameters ImageId.


2025-04-25 Version: 2.5.0
- Support API CreateVsc.
- Support API DeleteVsc.
- Support API DescribeVsc.
- Support API ListVscs.
- Update API CreateCluster: add request parameters NodeGroups.$.FileSystemMountEnabled.
- Update API CreateCluster: add request parameters NodeGroups.$.KeyPairName.
- Update API CreateNodeGroup: add request parameters NodeGroup.FileSystemMountEnabled.
- Update API CreateNodeGroup: add request parameters NodeGroup.KeyPairName.
- Update API DescribeNode: add response parameters Body.FileSystemMountEnabled.
- Update API ListClusterNodes: add response parameters Body.Nodes.$.FileSystemMountEnabled.
- Update API ListNodeGroups: add response parameters Body.Groups.$.FileSystemMountEnabled.
- Update API UpdateNodeGroup: add request parameters FileSystemMountEnabled.
- Update API UpdateNodeGroup: add request parameters KeyPairName.
- Update API UpdateNodeGroup: add response parameters Body.TaskId.


2025-04-16 Version: 2.4.6
- Generated python 2022-12-15 for eflo-controller.

2025-04-15 Version: 2.4.5
- Update API ListFreeNodes: add request parameters OperatingStates.


2025-04-10 Version: 2.4.4
- Update API CreateCluster: add request parameters NodeGroups.$.SystemDisk.
- Update API CreateNodeGroup: add request parameters NodeGroup.SystemDisk.
- Update API DescribeNode: add response parameters Body.Disks.


2025-04-03 Version: 2.4.3
- Update API ExtendCluster: add request parameters IpAllocationPolicy.$.NodePolicy.$.Hostname.
- Update API ExtendCluster: add request parameters NodeGroups.$.Amount.
- Update API ExtendCluster: add request parameters NodeGroups.$.AutoRenew.
- Update API ExtendCluster: add request parameters NodeGroups.$.ChargeType.
- Update API ExtendCluster: add request parameters NodeGroups.$.Hostnames.
- Update API ExtendCluster: add request parameters NodeGroups.$.LoginPassword.
- Update API ExtendCluster: add request parameters NodeGroups.$.NodeTag.
- Update API ExtendCluster: add request parameters NodeGroups.$.Period.
- Update API ExtendCluster: add request parameters NodeGroups.$.VSwitchId.
- Update API ExtendCluster: add request parameters NodeGroups.$.VpcId.


2025-03-28 Version: 2.4.2
- Generated python 2022-12-15 for eflo-controller.

2025-03-25 Version: 2.4.1
- Update API CreateNodeGroup: add request parameters NodeGroup.UserData.
- Update API DescribeNode: add response parameters Body.UserData.
- Update API ListClusterNodes: add request parameters ResourceGroupId.
- Update API ListClusterNodes: add request parameters Tags.
- Update API ListClusterNodes: add response parameters Body.Nodes.$.CommodityCode.
- Update API ListClusterNodes: add response parameters Body.Nodes.$.ImageName.
- Update API ListClusterNodes: add response parameters Body.Nodes.$.Tags.
- Update API ListClusterNodes: add response parameters Body.Nodes.$.TaskId.
- Update API ListClusters: add request parameters Tags.
- Update API ListClusters: add response parameters Body.Clusters.$.Tags.
- Update API ListFreeNodes: add request parameters Tags.
- Update API ListFreeNodes: add response parameters Body.Nodes.$.CommodityCode.
- Update API ListFreeNodes: add response parameters Body.Nodes.$.OperatingState.
- Update API ListFreeNodes: add response parameters Body.Nodes.$.Tags.
- Update API UpdateNodeGroup: add request parameters UserData.


2025-03-21 Version: 2.4.0
- Support API CreateNodeGroup.
- Support API DeleteNodeGroup.
- Support API DescribeDiagnosticResult.
- Support API UpdateNodeGroup.
- Update API ListClusterNodes: update response param.


2025-03-12 Version: 2.3.1
- Update API ChangeResourceGroup: add param ResourceType.


2025-03-03 Version: 2.3.0
- Support API CloseSession.
- Support API CreateNetTestTask.
- Support API CreateSession.
- Support API DescribeNetTestResult.
- Support API ListDiagnosticResults.
- Support API ListImages.
- Support API ListMachineNetworkInfo.
- Support API ListNetTestResults.
- Support API ListUserClusterTypes.


2025-01-15 Version: 2.2.0
- Support API StopNodes.


2025-01-06 Version: 2.1.0
- Support API CreateDiagnosticTask.
- Support API ListMachineTypes.
- Support API ListNodeGroups.
- Update API RunCommand: add param CommandId.
- Update API RunCommand: add param Launcher.
- Update API RunCommand: add param TerminationMode.
- Update API RunCommand: update param ClientToken.
- Update API RunCommand: update param CommandContent.
- Update API RunCommand: update param ContentEncoding.
- Update API RunCommand: update param Description.
- Update API RunCommand: update param EnableParameter.
- Update API RunCommand: update param Frequency.
- Update API RunCommand: update param Name.
- Update API RunCommand: update param NodeIdList.
- Update API RunCommand: update param Parameters.
- Update API RunCommand: update param RepeatMode.
- Update API RunCommand: update param Timeout.
- Update API RunCommand: update param Username.
- Update API RunCommand: update param WorkingDir.


2025-01-02 Version: 2.0.0
- Update API DescribeInvocations: update response param.


2024-12-18 Version: 1.2.4
- Update API CreateCluster: add param OpenEniJumboFrame.
- Update API DescribeCluster: update response param.


2024-11-08 Version: 1.2.3
- Update API CreateCluster: add param OpenEniJumboFrame.
- Update API DescribeCluster: update response param.


2024-04-07 Version: 1.2.2
- Update API DescribeCluster: update response param.
- Update API ListClusters: update response param.


2024-03-29 Version: 1.2.1
- Update API CreateCluster: update param Networks.


2024-03-12 Version: 1.2.0
- Support API DescribeInvocations.
- Support API DescribeSendFileResults.
- Support API RunCommand.
- Support API SendFile.
- Support API StopInvocation.
- Update API CreateCluster: update param NodeGroups.
- Update API ExtendCluster: update param NodeGroups.
- Update API ReimageNodes: update param Nodes.


2024-01-10 Version: 1.1.3
- Generated python 2022-12-15 for eflo-controller.

2023-11-16 Version: 1.1.2
- Generated python 2022-12-15 for eflo-controller.

2023-11-14 Version: 1.1.1
- Generated python 2022-12-15 for eflo-controller.

2023-11-07 Version: 1.1.0
- Generated python 2022-12-15 for eflo-controller.

2023-10-26 Version: 1.0.7
- Generated python 2022-12-15 for eflo-controller.

2023-08-21 Version: 1.0.6
- Generated python 2022-12-15 for eflo-controller.

2023-08-16 Version: 1.0.5
- Generated python 2022-12-15 for eflo-controller.

2023-06-13 Version: 1.0.4
- Lingjun Controller Initial Version Released.

2023-04-24 Version: 1.0.3
- Lingjun Controller Initial Version Released.

2023-03-28 Version: 1.0.2
- Lingjun Controller Initial Version Released.

2023-03-13 Version: 1.0.1
- Lingjun Controller Initial Version Released.

2023-01-10 Version: 1.0.0
- Lingjun Controller Initial Version Released.

