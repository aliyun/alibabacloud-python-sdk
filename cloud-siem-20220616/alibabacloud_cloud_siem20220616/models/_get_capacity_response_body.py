# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cloud_siem20220616 import models as main_models
from darabonba.model import DaraModel

class GetCapacityResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetCapacityResponseBodyData = None,
        request_id: str = None,
    ):
        # The information about the storage capacity.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.GetCapacityResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetCapacityResponseBodyData(DaraModel):
    def __init__(
        self,
        agent_managed_asset_quota: int = None,
        agent_managed_asset_used: int = None,
        exist_log_store: bool = None,
        preserved_capacity: int = None,
        used_capacity: float = None,
    ):
        self.agent_managed_asset_quota = agent_managed_asset_quota
        self.agent_managed_asset_used = agent_managed_asset_used
        # Indicates whether the Logstores for the threat analysis feature exist on the user side. Valid values:
        # 
        # *   true: The logs are in the normal state. The log analysis feature is available.
        # *   false: The logs are being cleared. The log analysis feature is unavailable.
        self.exist_log_store = exist_log_store
        # The purchased storage capacity of the threat analysis feature. Unit: GB.
        self.preserved_capacity = preserved_capacity
        # The billable storage capacity of the threat analysis feature. Unit: GB.
        self.used_capacity = used_capacity

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_managed_asset_quota is not None:
            result['AgentManagedAssetQuota'] = self.agent_managed_asset_quota

        if self.agent_managed_asset_used is not None:
            result['AgentManagedAssetUsed'] = self.agent_managed_asset_used

        if self.exist_log_store is not None:
            result['ExistLogStore'] = self.exist_log_store

        if self.preserved_capacity is not None:
            result['PreservedCapacity'] = self.preserved_capacity

        if self.used_capacity is not None:
            result['UsedCapacity'] = self.used_capacity

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentManagedAssetQuota') is not None:
            self.agent_managed_asset_quota = m.get('AgentManagedAssetQuota')

        if m.get('AgentManagedAssetUsed') is not None:
            self.agent_managed_asset_used = m.get('AgentManagedAssetUsed')

        if m.get('ExistLogStore') is not None:
            self.exist_log_store = m.get('ExistLogStore')

        if m.get('PreservedCapacity') is not None:
            self.preserved_capacity = m.get('PreservedCapacity')

        if m.get('UsedCapacity') is not None:
            self.used_capacity = m.get('UsedCapacity')

        return self

