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
        grow_interval: int = None,
        idle_interval: int = None,
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
        # A list of software to install in the cluster. You can specify up to 10 packages.
        self.additional_packages_shrink = additional_packages_shrink
        # The configuration of the custom service component for the cluster. Only one component is supported.
        self.addons_shrink = addons_shrink
        # The version of the E-HPC client. By default, the latest version is used.
        self.client_version = client_version
        # The edition of the cluster. Valid values:
        # 
        # - Standard
        # 
        # - Serverless
        self.cluster_category = cluster_category
        # The security credentials for the cluster.
        self.cluster_credentials_shrink = cluster_credentials_shrink
        # The post-processing script for the cluster.
        self.cluster_custom_configuration_shrink = cluster_custom_configuration_shrink
        # The description of the cluster. The description must be 2 to 128 characters long and can contain letters, Chinese characters, digits, hyphens (-), and underscores (_).
        self.cluster_description = cluster_description
        # The cluster\\"s deployment type. Valid values:
        # 
        # - Integrated: An integrated cluster.
        # 
        # - Hybrid: A hybrid cloud cluster.
        # 
        # - Custom: A custom cluster.
        self.cluster_mode = cluster_mode
        # The name of the cluster. The name must be 2 to 128 characters long and can contain letters, Chinese characters, digits, hyphens (-), and underscores (_).
        self.cluster_name = cluster_name
        # The ID of the VSwitch for the cluster. The VSwitch must be in the VPC specified by `ClusterVpcId`.
        # 
        # Call the [DescribeVpcs](https://help.aliyun.com/document_detail/448581.html) operation to find available VPCs and VSwitches.
        self.cluster_vswitch_id = cluster_vswitch_id
        # The ID of the VPC for the cluster.
        self.cluster_vpc_id = cluster_vpc_id
        # Specifies whether to enable deletion protection for the cluster. This feature prevents the cluster from being deleted via the console or the [DeleteCluster](https://help.aliyun.com/document_detail/424406.html) operation.
        # 
        # - true: Enables deletion protection.
        # 
        # - false: Disables deletion protection.
        # 
        # Default value: false.
        self.deletion_protection = deletion_protection
        self.grow_interval = grow_interval
        self.idle_interval = idle_interval
        # Specifies whether to use an enterprise security group. Valid values:
        # 
        # - true: The system automatically creates and uses an enterprise security group.
        # 
        # - false: The system automatically creates and uses a security group.
        # 
        # For more information about how to select a security group type, see [Security groups and enterprise security groups](https://help.aliyun.com/document_detail/605897.html).
        self.is_enterprise_security_group = is_enterprise_security_group
        # Configuration for the cluster manager node.
        self.manager_shrink = manager_shrink
        # The maximum number of CPU cores that the cluster can manage across all compute nodes. Valid values: 0 to 100,000.
        self.max_core_count = max_core_count
        # The maximum number of compute nodes that the cluster can manage. Valid values: 0 to 5,000.
        self.max_count = max_count
        # Configuration for the cluster queues. You can specify up to 8 queues.
        self.queues_shrink = queues_shrink
        # The ID of the resource group.
        # 
        # Call the [ListResourceGroups](https://help.aliyun.com/document_detail/158855.html) operation to find resource group IDs.
        self.resource_group_id = resource_group_id
        # The ID of the security group for the cluster.
        # 
        # Call the [DescribeSecurityGroups](https://help.aliyun.com/document_detail/25556.html) operation to find available security groups in the current region.
        self.security_group_id = security_group_id
        # Configuration for the cluster\\"s shared storage.
        self.shared_storages_shrink = shared_storages_shrink
        # The list of tags to add to the cluster. You can add up to 20 tags.
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

        if self.grow_interval is not None:
            result['GrowInterval'] = self.grow_interval

        if self.idle_interval is not None:
            result['IdleInterval'] = self.idle_interval

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

        if m.get('GrowInterval') is not None:
            self.grow_interval = m.get('GrowInterval')

        if m.get('IdleInterval') is not None:
            self.idle_interval = m.get('IdleInterval')

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

