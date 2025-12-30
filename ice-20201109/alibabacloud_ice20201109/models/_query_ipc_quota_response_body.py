# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class QueryIpcQuotaResponseBody(DaraModel):
    def __init__(
        self,
        ipc_quota_infos: List[main_models.QueryIpcQuotaResponseBodyIpcQuotaInfos] = None,
        request_id: str = None,
        total: str = None,
    ):
        self.ipc_quota_infos = ipc_quota_infos
        self.request_id = request_id
        self.total = total

    def validate(self):
        if self.ipc_quota_infos:
            for v1 in self.ipc_quota_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['IpcQuotaInfos'] = []
        if self.ipc_quota_infos is not None:
            for k1 in self.ipc_quota_infos:
                result['IpcQuotaInfos'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ipc_quota_infos = []
        if m.get('IpcQuotaInfos') is not None:
            for k1 in m.get('IpcQuotaInfos'):
                temp_model = main_models.QueryIpcQuotaResponseBodyIpcQuotaInfos()
                self.ipc_quota_infos.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class QueryIpcQuotaResponseBodyIpcQuotaInfos(DaraModel):
    def __init__(
        self,
        capability: str = None,
        consumed_quota: int = None,
        date_time: str = None,
        max_quota: int = None,
    ):
        self.capability = capability
        self.consumed_quota = consumed_quota
        self.date_time = date_time
        self.max_quota = max_quota

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.capability is not None:
            result['Capability'] = self.capability

        if self.consumed_quota is not None:
            result['ConsumedQuota'] = self.consumed_quota

        if self.date_time is not None:
            result['DateTime'] = self.date_time

        if self.max_quota is not None:
            result['MaxQuota'] = self.max_quota

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Capability') is not None:
            self.capability = m.get('Capability')

        if m.get('ConsumedQuota') is not None:
            self.consumed_quota = m.get('ConsumedQuota')

        if m.get('DateTime') is not None:
            self.date_time = m.get('DateTime')

        if m.get('MaxQuota') is not None:
            self.max_quota = m.get('MaxQuota')

        return self

