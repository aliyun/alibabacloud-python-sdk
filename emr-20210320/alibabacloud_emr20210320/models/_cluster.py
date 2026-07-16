# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_emr20210320 import models as main_models
from darabonba.model import DaraModel

class Cluster(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        cluster_name: str = None,
        cluster_state: str = None,
        cluster_type: str = None,
        create_time: int = None,
        deletion_protection: bool = None,
        deploy_mode: str = None,
        description: str = None,
        emr_default_role: str = None,
        end_time: int = None,
        expire_time: int = None,
        node_attributes: main_models.NodeAttributes = None,
        payment_type: str = None,
        ready_time: int = None,
        region_id: str = None,
        release_version: str = None,
        resource_group_id: str = None,
        security_mode: str = None,
        state_change_reason: main_models.ClusterStateChangeReason = None,
        subscription_config: main_models.SubscriptionConfig = None,
        tags: List[main_models.Tag] = None,
    ):
        # The cluster ID.
        self.cluster_id = cluster_id
        # The cluster name.
        self.cluster_name = cluster_name
        # The cluster state. Valid values:
        # 
        # - `STARTING`: The cluster is starting.
        # 
        # - `START_FAILED`: The cluster failed to start.
        # 
        # - `BOOTSTRAPPING`: The cluster is running bootstrap actions.
        # 
        # - `RUNNING`: The cluster is running.
        # 
        # - `TERMINATING`: The cluster is terminating.
        # 
        # - `TERMINATED`: The cluster is terminated.
        # 
        # - `TERMINATED_WITH_ERRORS`: The cluster terminated due to errors.
        # 
        # - `TERMINATE_FAILED`: The cluster failed to terminate.
        self.cluster_state = cluster_state
        # The cluster type. Valid values:
        # 
        # - `DATALAKE`: New data lake.
        # 
        # - `OLAP`: Data analysis.
        # 
        # - `DATAFLOW`: Real-time data flow.
        # 
        # - `DATASERVING`: Data serving.
        # 
        # - `CUSTOM`: Custom cluster.
        # 
        # - `HADOOP`: Legacy data lake.
        self.cluster_type = cluster_type
        # The time when the cluster was created. The time is a Unix timestamp in milliseconds.
        self.create_time = create_time
        # Indicates whether deletion protection is enabled for the cluster.
        self.deletion_protection = deletion_protection
        # The application deployment mode. Valid values:
        # 
        # - `NORMAL`: Standard deployment.
        # 
        # - `HA`: High-availability deployment.
        self.deploy_mode = deploy_mode
        # The cluster description.
        self.description = description
        # The default role for E-MapReduce.
        self.emr_default_role = emr_default_role
        # The time when the cluster was deleted. The time is a Unix timestamp in milliseconds.
        self.end_time = end_time
        # The time when the cluster is scheduled to expire. The time is a Unix timestamp in milliseconds.
        self.expire_time = expire_time
        # The node attributes.
        self.node_attributes = node_attributes
        # The billing method. Valid values:
        # 
        # - `PayAsYouGo`: Pay-as-you-go.
        # 
        # - `Subscription`: Subscription.
        self.payment_type = payment_type
        # The time when the cluster became ready. The time is a Unix timestamp in milliseconds.
        self.ready_time = ready_time
        # The ID of the region.
        self.region_id = region_id
        # The release version of E-MapReduce.
        self.release_version = release_version
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The security mode of the cluster. Valid values:
        # 
        # - `NORMAL`: Kerberos is disabled.
        # 
        # - `KERBEROS`: Kerberos is enabled.
        self.security_mode = security_mode
        # The reason for the cluster state change.
        self.state_change_reason = state_change_reason
        # The subscription configuration.
        self.subscription_config = subscription_config
        # The cluster tags.
        self.tags = tags

    def validate(self):
        if self.node_attributes:
            self.node_attributes.validate()
        if self.state_change_reason:
            self.state_change_reason.validate()
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
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name

        if self.cluster_state is not None:
            result['ClusterState'] = self.cluster_state

        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.deletion_protection is not None:
            result['DeletionProtection'] = self.deletion_protection

        if self.deploy_mode is not None:
            result['DeployMode'] = self.deploy_mode

        if self.description is not None:
            result['Description'] = self.description

        if self.emr_default_role is not None:
            result['EmrDefaultRole'] = self.emr_default_role

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.node_attributes is not None:
            result['NodeAttributes'] = self.node_attributes.to_map()

        if self.payment_type is not None:
            result['PaymentType'] = self.payment_type

        if self.ready_time is not None:
            result['ReadyTime'] = self.ready_time

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.release_version is not None:
            result['ReleaseVersion'] = self.release_version

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.security_mode is not None:
            result['SecurityMode'] = self.security_mode

        if self.state_change_reason is not None:
            result['StateChangeReason'] = self.state_change_reason.to_map()

        if self.subscription_config is not None:
            result['SubscriptionConfig'] = self.subscription_config.to_map()

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')

        if m.get('ClusterState') is not None:
            self.cluster_state = m.get('ClusterState')

        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DeletionProtection') is not None:
            self.deletion_protection = m.get('DeletionProtection')

        if m.get('DeployMode') is not None:
            self.deploy_mode = m.get('DeployMode')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EmrDefaultRole') is not None:
            self.emr_default_role = m.get('EmrDefaultRole')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('NodeAttributes') is not None:
            temp_model = main_models.NodeAttributes()
            self.node_attributes = temp_model.from_map(m.get('NodeAttributes'))

        if m.get('PaymentType') is not None:
            self.payment_type = m.get('PaymentType')

        if m.get('ReadyTime') is not None:
            self.ready_time = m.get('ReadyTime')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ReleaseVersion') is not None:
            self.release_version = m.get('ReleaseVersion')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SecurityMode') is not None:
            self.security_mode = m.get('SecurityMode')

        if m.get('StateChangeReason') is not None:
            temp_model = main_models.ClusterStateChangeReason()
            self.state_change_reason = temp_model.from_map(m.get('StateChangeReason'))

        if m.get('SubscriptionConfig') is not None:
            temp_model = main_models.SubscriptionConfig()
            self.subscription_config = temp_model.from_map(m.get('SubscriptionConfig'))

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.Tag()
                self.tags.append(temp_model.from_map(k1))

        return self

