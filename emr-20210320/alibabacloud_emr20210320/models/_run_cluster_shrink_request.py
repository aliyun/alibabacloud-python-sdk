# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RunClusterShrinkRequest(DaraModel):
    def __init__(
        self,
        application_configs_shrink: str = None,
        applications_shrink: str = None,
        bootstrap_scripts_shrink: str = None,
        client_token: str = None,
        cluster_name: str = None,
        cluster_type: str = None,
        deletion_protection: bool = None,
        deploy_mode: str = None,
        description: str = None,
        node_attributes_shrink: str = None,
        node_groups_shrink: str = None,
        payment_type: str = None,
        promotions_shrink: str = None,
        region_id: str = None,
        release_version: str = None,
        resource_group_id: str = None,
        security_mode: str = None,
        subscription_config_shrink: str = None,
        tags_shrink: str = None,
    ):
        # The application configurations. The number of array elements N can range from 1 to 1000.
        self.application_configs_shrink = application_configs_shrink
        # The list of applications. The number of array elements N can range from 1 to 100.
        # 
        # This parameter is required.
        self.applications_shrink = applications_shrink
        # The array of bootstrap scripts. The number of array elements N can range from 1 to 10.
        self.bootstrap_scripts_shrink = bootstrap_scripts_shrink
        # A client token to ensure the idempotence of the request. Multiple calls with the same client token return the same result and create only one cluster.
        self.client_token = client_token
        # The cluster name. The name must be 1 to 128 characters in length. It must start with a letter or a Chinese character. It cannot start with http\\:// or https\\://. It can contain Chinese characters, letters, digits, colons (:), underscores (_), periods (.), or hyphens (-).
        # 
        # This parameter is required.
        self.cluster_name = cluster_name
        # The cluster type. Valid values:
        # 
        # - DATALAKE: new data lake.
        # 
        # - OLAP: data analytics.
        # 
        # - DATAFLOW: real-time data stream.
        # 
        # - DATASERVING: DataService Studio.
        # 
        # - CUSTOM: custom cluster.
        # 
        # - HADOOP: legacy data lake. This value is not recommended. Use the new data lake cluster type instead.
        # 
        # If you create an EMR cluster for the first time after 17:00 (UTC+8) on December 19, 2022, you cannot select HADOOP, DATA_SCIENCE, PRESTO, or ZOOKEEPER as the cluster type.
        # 
        # This parameter is required.
        self.cluster_type = cluster_type
        # Specifies whether to enable deletion protection for the cluster. Valid values:
        # 
        # - true: Enables deletion protection.
        # 
        # - false: Disables deletion protection.
        # 
        # Default value: false.
        self.deletion_protection = deletion_protection
        # The deployment mode of applications in the cluster. Valid values:
        # 
        # - NORMAL (default): non-high availability deployment. The cluster has one master node.
        # 
        # - HA: high availability (HA) deployment. This deployment mode requires at least three master nodes.
        self.deploy_mode = deploy_mode
        # The description of the cluster.
        self.description = description
        # The node attributes. These are the basic attributes of all ECS nodes in the cluster.
        self.node_attributes_shrink = node_attributes_shrink
        # The array of node group configurations. The number of array elements N can range from 1 to 100.
        # 
        # This parameter is required.
        self.node_groups_shrink = node_groups_shrink
        # The billing method. Valid values:
        # 
        # - PayAsYouGo: pay-as-you-go.
        # 
        # - Subscription: subscription.
        # 
        # Default value: PayAsYouGo.
        self.payment_type = payment_type
        self.promotions_shrink = promotions_shrink
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The EMR release version. You can find the EMR release version on the EMR cluster purchase page.
        # 
        # This parameter is required.
        self.release_version = release_version
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The Kerberos security mode of the cluster. Valid values:
        # 
        # - NORMAL (default): normal mode. Kerberos is disabled.
        # 
        # - KERBEROS: Kerberos mode. Kerberos is enabled.
        self.security_mode = security_mode
        # The subscription configurations. This parameter is required if you set PaymentType to Subscription.
        self.subscription_config_shrink = subscription_config_shrink
        # The tags. The number of array elements N can range from 0 to 20.
        self.tags_shrink = tags_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_configs_shrink is not None:
            result['ApplicationConfigs'] = self.application_configs_shrink

        if self.applications_shrink is not None:
            result['Applications'] = self.applications_shrink

        if self.bootstrap_scripts_shrink is not None:
            result['BootstrapScripts'] = self.bootstrap_scripts_shrink

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name

        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type

        if self.deletion_protection is not None:
            result['DeletionProtection'] = self.deletion_protection

        if self.deploy_mode is not None:
            result['DeployMode'] = self.deploy_mode

        if self.description is not None:
            result['Description'] = self.description

        if self.node_attributes_shrink is not None:
            result['NodeAttributes'] = self.node_attributes_shrink

        if self.node_groups_shrink is not None:
            result['NodeGroups'] = self.node_groups_shrink

        if self.payment_type is not None:
            result['PaymentType'] = self.payment_type

        if self.promotions_shrink is not None:
            result['Promotions'] = self.promotions_shrink

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.release_version is not None:
            result['ReleaseVersion'] = self.release_version

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.security_mode is not None:
            result['SecurityMode'] = self.security_mode

        if self.subscription_config_shrink is not None:
            result['SubscriptionConfig'] = self.subscription_config_shrink

        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationConfigs') is not None:
            self.application_configs_shrink = m.get('ApplicationConfigs')

        if m.get('Applications') is not None:
            self.applications_shrink = m.get('Applications')

        if m.get('BootstrapScripts') is not None:
            self.bootstrap_scripts_shrink = m.get('BootstrapScripts')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')

        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')

        if m.get('DeletionProtection') is not None:
            self.deletion_protection = m.get('DeletionProtection')

        if m.get('DeployMode') is not None:
            self.deploy_mode = m.get('DeployMode')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('NodeAttributes') is not None:
            self.node_attributes_shrink = m.get('NodeAttributes')

        if m.get('NodeGroups') is not None:
            self.node_groups_shrink = m.get('NodeGroups')

        if m.get('PaymentType') is not None:
            self.payment_type = m.get('PaymentType')

        if m.get('Promotions') is not None:
            self.promotions_shrink = m.get('Promotions')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ReleaseVersion') is not None:
            self.release_version = m.get('ReleaseVersion')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SecurityMode') is not None:
            self.security_mode = m.get('SecurityMode')

        if m.get('SubscriptionConfig') is not None:
            self.subscription_config_shrink = m.get('SubscriptionConfig')

        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')

        return self

