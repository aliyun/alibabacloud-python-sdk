# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateClusterShrinkRequest(DaraModel):
    def __init__(
        self,
        additional_packages_shrink: str = None,
        addons_shrink: str = None,
        client_version: str = None,
        cluster_category: str = None,
        cluster_credentials_shrink: str = None,
        cluster_custom_configuration_shrink: str = None,
        cluster_description: str = None,
        cluster_mode: str = None,
        cluster_name: str = None,
        cluster_vswitch_id: str = None,
        cluster_vpc_id: str = None,
        deletion_protection: bool = None,
        is_enterprise_security_group: bool = None,
        manager_shrink: str = None,
        max_core_count: int = None,
        max_count: int = None,
        queues_shrink: str = None,
        resource_group_id: str = None,
        security_group_id: str = None,
        shared_storages_shrink: str = None,
        tags_shrink: str = None,
    ):
        # The list of software that you want to install in the cluster. Valid values of N: 0 to 10.
        self.additional_packages_shrink = additional_packages_shrink
        # The configurations of the custom addons in the cluster. Only one addon is supported.
        self.addons_shrink = addons_shrink
        # The client version. By default, the latest version is used.
        self.client_version = client_version
        # The cluster type. Valid values:
        # 
        # *   Standard
        # *   Serverless
        self.cluster_category = cluster_category
        # The access credentials of the cluster.
        self.cluster_credentials_shrink = cluster_credentials_shrink
        # The post-processing script of the cluster.
        self.cluster_custom_configuration_shrink = cluster_custom_configuration_shrink
        # The cluster description. The description must be 1 to 128 characters in length and can contain letters, digits, hyphens (-), and underscores (_).
        self.cluster_description = cluster_description
        # The deployment mode of the cluster. Valid values:
        # 
        # *   Integrated
        # *   Hybrid
        # *   Custom
        self.cluster_mode = cluster_mode
        # The cluster name. The name must be 1 to 128 characters in length and can contain letters, digits, hyphens (-), and underscores (_).
        self.cluster_name = cluster_name
        # The ID of the vSwitch that you want the cluster to use. The vSwitch must reside in the VPC that is specified by the `ClusterVpcId` parameter.
        # 
        # You can call the [DescribeVpcs](https://help.aliyun.com/document_detail/448581.html) operation to query information about the created VPCs and vSwitches.
        self.cluster_vswitch_id = cluster_vswitch_id
        # The ID of the virtual private cloud (VPC) in which the cluster resides.
        self.cluster_vpc_id = cluster_vpc_id
        # Specifies whether to enable deletion protection for the cluster. Deletion protection decides whether the cluster can be deleted in the console or by calling the [DeleteCluster](https://help.aliyun.com/document_detail/424406.html) operation. Valid values:
        # 
        # *   true
        # *   false
        # 
        # Default value: false.
        self.deletion_protection = deletion_protection
        # Specifies whether to use an advanced security group. Valid values:
        # 
        # *   true: automatically creates and uses an advanced security group.
        # *   false: automatically creates and uses a basic security group.
        # 
        # For more information, see [Basic security groups and advanced security groups](https://help.aliyun.com/document_detail/605897.html).
        self.is_enterprise_security_group = is_enterprise_security_group
        # The configurations of the cluster management node.
        self.manager_shrink = manager_shrink
        # The maximum number of vCPUs that can be used by compute nodes in the cluster. Valid values: 0 to 100,000.
        self.max_core_count = max_core_count
        # The maximum number of compute nodes that the cluster can manage. Valid values: 0 to 5,000.
        self.max_count = max_count
        # The queues in the cluster. The number of queues can be 0 to 8.
        self.queues_shrink = queues_shrink
        # The ID of the resource group to which the cluster belongs.
        # 
        # You can call the [ListResourceGroups](https://help.aliyun.com/document_detail/158855.html) operation to obtain the IDs of the resource groups.
        self.resource_group_id = resource_group_id
        # The ID of the security group to which the cluster belongs.
        # 
        # You can call the [DescribeSecurityGroups](https://help.aliyun.com/document_detail/25556.html) operation to query available security groups in the current region.
        self.security_group_id = security_group_id
        # The shared storage resources of the cluster.
        self.shared_storages_shrink = shared_storages_shrink
        # The tags of the cluster.
        self.tags_shrink = tags_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.additional_packages_shrink is not None:
            result['AdditionalPackages'] = self.additional_packages_shrink

        if self.addons_shrink is not None:
            result['Addons'] = self.addons_shrink

        if self.client_version is not None:
            result['ClientVersion'] = self.client_version

        if self.cluster_category is not None:
            result['ClusterCategory'] = self.cluster_category

        if self.cluster_credentials_shrink is not None:
            result['ClusterCredentials'] = self.cluster_credentials_shrink

        if self.cluster_custom_configuration_shrink is not None:
            result['ClusterCustomConfiguration'] = self.cluster_custom_configuration_shrink

        if self.cluster_description is not None:
            result['ClusterDescription'] = self.cluster_description

        if self.cluster_mode is not None:
            result['ClusterMode'] = self.cluster_mode

        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name

        if self.cluster_vswitch_id is not None:
            result['ClusterVSwitchId'] = self.cluster_vswitch_id

        if self.cluster_vpc_id is not None:
            result['ClusterVpcId'] = self.cluster_vpc_id

        if self.deletion_protection is not None:
            result['DeletionProtection'] = self.deletion_protection

        if self.is_enterprise_security_group is not None:
            result['IsEnterpriseSecurityGroup'] = self.is_enterprise_security_group

        if self.manager_shrink is not None:
            result['Manager'] = self.manager_shrink

        if self.max_core_count is not None:
            result['MaxCoreCount'] = self.max_core_count

        if self.max_count is not None:
            result['MaxCount'] = self.max_count

        if self.queues_shrink is not None:
            result['Queues'] = self.queues_shrink

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        if self.shared_storages_shrink is not None:
            result['SharedStorages'] = self.shared_storages_shrink

        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdditionalPackages') is not None:
            self.additional_packages_shrink = m.get('AdditionalPackages')

        if m.get('Addons') is not None:
            self.addons_shrink = m.get('Addons')

        if m.get('ClientVersion') is not None:
            self.client_version = m.get('ClientVersion')

        if m.get('ClusterCategory') is not None:
            self.cluster_category = m.get('ClusterCategory')

        if m.get('ClusterCredentials') is not None:
            self.cluster_credentials_shrink = m.get('ClusterCredentials')

        if m.get('ClusterCustomConfiguration') is not None:
            self.cluster_custom_configuration_shrink = m.get('ClusterCustomConfiguration')

        if m.get('ClusterDescription') is not None:
            self.cluster_description = m.get('ClusterDescription')

        if m.get('ClusterMode') is not None:
            self.cluster_mode = m.get('ClusterMode')

        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')

        if m.get('ClusterVSwitchId') is not None:
            self.cluster_vswitch_id = m.get('ClusterVSwitchId')

        if m.get('ClusterVpcId') is not None:
            self.cluster_vpc_id = m.get('ClusterVpcId')

        if m.get('DeletionProtection') is not None:
            self.deletion_protection = m.get('DeletionProtection')

        if m.get('IsEnterpriseSecurityGroup') is not None:
            self.is_enterprise_security_group = m.get('IsEnterpriseSecurityGroup')

        if m.get('Manager') is not None:
            self.manager_shrink = m.get('Manager')

        if m.get('MaxCoreCount') is not None:
            self.max_core_count = m.get('MaxCoreCount')

        if m.get('MaxCount') is not None:
            self.max_count = m.get('MaxCount')

        if m.get('Queues') is not None:
            self.queues_shrink = m.get('Queues')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('SharedStorages') is not None:
            self.shared_storages_shrink = m.get('SharedStorages')

        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')

        return self

