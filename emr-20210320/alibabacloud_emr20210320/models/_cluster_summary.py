# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_emr20210320 import models as main_models
from darabonba.model import DaraModel

class ClusterSummary(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        cluster_name: str = None,
        cluster_state: str = None,
        cluster_type: str = None,
        create_time: int = None,
        deletion_protection: bool = None,
        description: str = None,
        emr_default_role: str = None,
        end_time: int = None,
        expire_time: int = None,
        payment_type: str = None,
        ready_time: int = None,
        release_version: str = None,
        resource_group_id: str = None,
        state_change_reason: main_models.ClusterStateChangeReason = None,
        tags: List[main_models.Tag] = None,
    ):
        # The cluster ID.
        self.cluster_id = cluster_id
        # The cluster name.
        self.cluster_name = cluster_name
        # The state of the cluster. Valid values:
        # 
        # - `STARTING`: The cluster is starting.
        # 
        # - `START_FAILED`: The cluster fails to be started.
        # 
        # - `BOOTSTRAPPING`: The cluster is being initialized.
        # 
        # - `RUNNING`: The cluster is running.
        # 
        # - `TERMINATING`: The cluster is being terminated.
        # 
        # - `TERMINATED`: The cluster is terminated.
        # 
        # - `TERMINATED_WITH_ERRORS`: The cluster is terminated with errors.
        # 
        # - `TERMINATE_FAILED`: The cluster fails to be terminated.
        self.cluster_state = cluster_state
        # The cluster type. Valid values:
        # 
        # - `DATALAKE`: data lake.
        # 
        # - `OLAP`: data analytics.
        # 
        # - `DATAFLOW`: real-time dataflow.
        # 
        # - `DATASERVING`: data serving.
        self.cluster_type = cluster_type
        # The time when the cluster was created.
        self.create_time = create_time
        # The release protection feature.
        self.deletion_protection = deletion_protection
        # The description of the cluster.
        self.description = description
        # The EMR service role.
        self.emr_default_role = emr_default_role
        # The time when the cluster was deleted.
        self.end_time = end_time
        # The expiration time.
        self.expire_time = expire_time
        # The billing method. Valid values:
        # 
        # - `PayAsYouGo`: pay-as-you-go.
        # 
        # - `Subscription`: subscription.
        self.payment_type = payment_type
        # The time when the cluster is available.
        self.ready_time = ready_time
        # The E-MapReduce (EMR) release version.
        self.release_version = release_version
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The reason for the failure.
        self.state_change_reason = state_change_reason
        # The list of tags.
        self.tags = tags

    def validate(self):
        if self.state_change_reason:
            self.state_change_reason.validate()
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

        if self.description is not None:
            result['Description'] = self.description

        if self.emr_default_role is not None:
            result['EmrDefaultRole'] = self.emr_default_role

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.payment_type is not None:
            result['PaymentType'] = self.payment_type

        if self.ready_time is not None:
            result['ReadyTime'] = self.ready_time

        if self.release_version is not None:
            result['ReleaseVersion'] = self.release_version

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.state_change_reason is not None:
            result['StateChangeReason'] = self.state_change_reason.to_map()

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

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EmrDefaultRole') is not None:
            self.emr_default_role = m.get('EmrDefaultRole')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('PaymentType') is not None:
            self.payment_type = m.get('PaymentType')

        if m.get('ReadyTime') is not None:
            self.ready_time = m.get('ReadyTime')

        if m.get('ReleaseVersion') is not None:
            self.release_version = m.get('ReleaseVersion')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('StateChangeReason') is not None:
            temp_model = main_models.ClusterStateChangeReason()
            self.state_change_reason = temp_model.from_map(m.get('StateChangeReason'))

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.Tag()
                self.tags.append(temp_model.from_map(k1))

        return self

