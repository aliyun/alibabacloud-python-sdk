# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_emr20210320 import models as main_models
from darabonba.model import DaraModel

class CreateClusterRequest(DaraModel):
    def __init__(
        self,
        application_configs: List[main_models.ApplicationConfig] = None,
        applications: List[main_models.Application] = None,
        bootstrap_scripts: List[main_models.Script] = None,
        client_token: str = None,
        cluster_name: str = None,
        cluster_type: str = None,
        deletion_protection: bool = None,
        deploy_mode: str = None,
        description: str = None,
        node_attributes: main_models.NodeAttributes = None,
        node_groups: List[main_models.NodeGroupConfig] = None,
        payment_type: str = None,
        region_id: str = None,
        release_version: str = None,
        resource_group_id: str = None,
        security_mode: str = None,
        subscription_config: main_models.SubscriptionConfig = None,
        tags: List[main_models.Tag] = None,
    ):
        # The application configurations. The number of array elements N must be in the range of 1 to 1000.
        self.application_configs = application_configs
        # The list of applications. The number of array elements N must be in the range of 1 to 100.
        # 
        # This parameter is required.
        self.applications = applications
        # The array of bootstrap scripts. The number of array elements N must be in the range of 1 to 10.
        self.bootstrap_scripts = bootstrap_scripts
        # The client token that is used to ensure the idempotence of the request. The results of multiple calls that use the same client token are the same. A maximum of one cluster can be created with the same client token.
        self.client_token = client_token
        # The cluster name. The name must be 1 to 128 characters in length. It must start with a letter or a Chinese character. It cannot start with http\\:// or https\\://. It can contain letters, digits, Chinese characters, colons (:), underscores (_), periods (.), and hyphens (-).
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
        # - DATASERVING: data serving.
        # 
        # - CUSTOM: custom cluster.
        # 
        # - HADOOP: earlier-version data lake. We recommend that you use the new data lake.
        # 
        # If you create an EMR cluster for the first time after 17:00 (UTC+8) on December 19, 2022, you cannot select HADOOP, DATA_SCIENCE, PRESTO, or ZOOKEEPER as the cluster type.
        # 
        # This parameter is required.
        self.cluster_type = cluster_type
        # Specifies whether to enable deletion protection for the cluster. Valid values:
        # 
        # - true: enables deletion protection.
        # 
        # - false: disables deletion protection.
        # 
        # Default value: false.
        self.deletion_protection = deletion_protection
        # The deployment mode of applications in the cluster. Valid values:
        # 
        # - NORMAL (default): non-high availability (HA) deployment. The cluster has one master node.
        # 
        # - HA: HA deployment. An HA deployment requires at least three master nodes.
        self.deploy_mode = deploy_mode
        # The description of the cluster.
        self.description = description
        # The node attributes. This parameter specifies the basic attributes of all Elastic Compute Service (ECS) nodes in the cluster.
        # 
        # This parameter is required.
        self.node_attributes = node_attributes
        # The array of node group configurations. The number of array elements N must be in the range of 1 to 100.
        # 
        # This parameter is required.
        self.node_groups = node_groups
        # The billing method. Valid values:
        # 
        # - PayAsYouGo: pay-as-you-go.
        # 
        # - Subscription: subscription.
        # 
        # Default value: PayAsYouGo.
        self.payment_type = payment_type
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The EMR release version. You can find the EMR release versions on the EMR cluster purchase page.
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
        self.subscription_config = subscription_config
        # The tags. The number of array elements N must be in the range of 0 to 20.
        self.tags = tags

    def validate(self):
        if self.application_configs:
            for v1 in self.application_configs:
                 if v1:
                    v1.validate()
        if self.applications:
            for v1 in self.applications:
                 if v1:
                    v1.validate()
        if self.bootstrap_scripts:
            for v1 in self.bootstrap_scripts:
                 if v1:
                    v1.validate()
        if self.node_attributes:
            self.node_attributes.validate()
        if self.node_groups:
            for v1 in self.node_groups:
                 if v1:
                    v1.validate()
        if self.subscription_config:
            self.subscription_config.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ApplicationConfigs'] = []
        if self.application_configs is not None:
            for k1 in self.application_configs:
                result['ApplicationConfigs'].append(k1.to_map() if k1 else None)

        result['Applications'] = []
        if self.applications is not None:
            for k1 in self.applications:
                result['Applications'].append(k1.to_map() if k1 else None)

        result['BootstrapScripts'] = []
        if self.bootstrap_scripts is not None:
            for k1 in self.bootstrap_scripts:
                result['BootstrapScripts'].append(k1.to_map() if k1 else None)

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

        if self.node_attributes is not None:
            result['NodeAttributes'] = self.node_attributes.to_map()

        result['NodeGroups'] = []
        if self.node_groups is not None:
            for k1 in self.node_groups:
                result['NodeGroups'].append(k1.to_map() if k1 else None)

        if self.payment_type is not None:
            result['PaymentType'] = self.payment_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.release_version is not None:
            result['ReleaseVersion'] = self.release_version

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.security_mode is not None:
            result['SecurityMode'] = self.security_mode

        if self.subscription_config is not None:
            result['SubscriptionConfig'] = self.subscription_config.to_map()

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.application_configs = []
        if m.get('ApplicationConfigs') is not None:
            for k1 in m.get('ApplicationConfigs'):
                temp_model = main_models.ApplicationConfig()
                self.application_configs.append(temp_model.from_map(k1))

        self.applications = []
        if m.get('Applications') is not None:
            for k1 in m.get('Applications'):
                temp_model = main_models.Application()
                self.applications.append(temp_model.from_map(k1))

        self.bootstrap_scripts = []
        if m.get('BootstrapScripts') is not None:
            for k1 in m.get('BootstrapScripts'):
                temp_model = main_models.Script()
                self.bootstrap_scripts.append(temp_model.from_map(k1))

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
            temp_model = main_models.NodeAttributes()
            self.node_attributes = temp_model.from_map(m.get('NodeAttributes'))

        self.node_groups = []
        if m.get('NodeGroups') is not None:
            for k1 in m.get('NodeGroups'):
                temp_model = main_models.NodeGroupConfig()
                self.node_groups.append(temp_model.from_map(k1))

        if m.get('PaymentType') is not None:
            self.payment_type = m.get('PaymentType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ReleaseVersion') is not None:
            self.release_version = m.get('ReleaseVersion')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SecurityMode') is not None:
            self.security_mode = m.get('SecurityMode')

        if m.get('SubscriptionConfig') is not None:
            temp_model = main_models.SubscriptionConfig()
            self.subscription_config = temp_model.from_map(m.get('SubscriptionConfig'))

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.Tag()
                self.tags.append(temp_model.from_map(k1))

        return self

