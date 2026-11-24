# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeOSSStorageResponseBody(DaraModel):
    def __init__(
        self,
        cold_storage: bool = None,
        policy: str = None,
        request_id: str = None,
        state: str = None,
        storage_usage: str = None,
    ):
        # Indicates whether hot and cold tiered storage is supported. Valid values:
        # 
        # - **true**: Supported.
        # - **false**: Not supported.
        self.cold_storage = cold_storage
        # The parameters of the hot and cold tiered storage policy.
        self.policy = policy
        # The request ID.
        self.request_id = request_id
        # The status of the hot and cold tiered storage. Valid values:
        # 
        # - **CREATING**: Enabling.
        # - **DISABLE**: Disabled.
        # - **ENABLE**: Enabled.
        self.state = state
        # The amount of storage space used by cold data. Unit: GB.
        self.storage_usage = storage_usage

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cold_storage is not None:
            result['ColdStorage'] = self.cold_storage

        if self.policy is not None:
            result['Policy'] = self.policy

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.state is not None:
            result['State'] = self.state

        if self.storage_usage is not None:
            result['StorageUsage'] = self.storage_usage

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ColdStorage') is not None:
            self.cold_storage = m.get('ColdStorage')

        if m.get('Policy') is not None:
            self.policy = m.get('Policy')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('StorageUsage') is not None:
            self.storage_usage = m.get('StorageUsage')

        return self

