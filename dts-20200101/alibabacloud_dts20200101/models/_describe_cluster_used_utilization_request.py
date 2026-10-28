# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeClusterUsedUtilizationRequest(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        client_token: str = None,
        dedicated_cluster_id: str = None,
        dts_job_id: str = None,
        env: str = None,
        metric_type: str = None,
        owner_id: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        security_token: str = None,
    ):
        # The ID of the Alibaba Cloud account. You do not need to specify this parameter. This parameter will be deprecated soon.
        self.account_id = account_id
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must ensure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The ID of the dedicated cluster. Specify this parameter when **MetricType** is set to **CLUSTER**. Otherwise, specify the node ID.
        # 
        # This parameter is required.
        self.dedicated_cluster_id = dedicated_cluster_id
        # The ID of the migration or synchronization task.
        self.dts_job_id = dts_job_id
        # The environment. Default value: **ALIYUN**.
        self.env = env
        # The type of the resource to query. Valid values:
        # - **CLUSTER** (default): cluster.
        # - **NODE**: node.
        self.metric_type = metric_type
        self.owner_id = owner_id
        # The region ID of the instance.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['AccountId'] = self.account_id

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dedicated_cluster_id is not None:
            result['DedicatedClusterId'] = self.dedicated_cluster_id

        if self.dts_job_id is not None:
            result['DtsJobId'] = self.dts_job_id

        if self.env is not None:
            result['Env'] = self.env

        if self.metric_type is not None:
            result['MetricType'] = self.metric_type

        if self.owner_id is not None:
            result['OwnerID'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DedicatedClusterId') is not None:
            self.dedicated_cluster_id = m.get('DedicatedClusterId')

        if m.get('DtsJobId') is not None:
            self.dts_job_id = m.get('DtsJobId')

        if m.get('Env') is not None:
            self.env = m.get('Env')

        if m.get('MetricType') is not None:
            self.metric_type = m.get('MetricType')

        if m.get('OwnerID') is not None:
            self.owner_id = m.get('OwnerID')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        return self

