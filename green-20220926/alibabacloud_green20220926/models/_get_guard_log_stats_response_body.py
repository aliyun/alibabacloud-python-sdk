# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_green20220926 import models as main_models
from darabonba.model import DaraModel

class GetGuardLogStatsResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.GetGuardLogStatsResponseBodyData] = None,
        request_id: str = None,
    ):
        # The data.
        self.data = data
        # The ID assigned by the backend to uniquely identify a request. You can use this ID to troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.GetGuardLogStatsResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetGuardLogStatsResponseBodyData(DaraModel):
    def __init__(
        self,
        delivery_region: str = None,
        enable: bool = None,
        log_analysis_config: Dict[str, Any] = None,
        log_store_name: str = None,
        pending_storage: int = None,
        preserve_storage: int = None,
        project: str = None,
        total_storage: int = None,
        ttl: int = None,
        type: str = None,
        uid: str = None,
        used_storage: int = None,
    ):
        # The delivery region.
        self.delivery_region = delivery_region
        # Indicates whether the feature is enabled. Valid values:
        # 
        # - **true**: Enabled.
        # - **false**: Disabled.
        self.enable = enable
        # The log analysis configuration.
        self.log_analysis_config = log_analysis_config
        # The name of the Simple Log Service Logstore.
        self.log_store_name = log_store_name
        # The remaining storage space. Unit: TB.
        self.pending_storage = pending_storage
        # The reserved storage. Unit: bytes.
        self.preserve_storage = preserve_storage
        # The project space.
        self.project = project
        # The total storage space. Unit: TB.
        self.total_storage = total_storage
        # The number of days for which data is retained.
        self.ttl = ttl
        # The type.
        self.type = type
        # UID。
        self.uid = uid
        # The used storage. Unit: bytes.
        self.used_storage = used_storage

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.delivery_region is not None:
            result['DeliveryRegion'] = self.delivery_region

        if self.enable is not None:
            result['Enable'] = self.enable

        if self.log_analysis_config is not None:
            result['LogAnalysisConfig'] = self.log_analysis_config

        if self.log_store_name is not None:
            result['LogStoreName'] = self.log_store_name

        if self.pending_storage is not None:
            result['PendingStorage'] = self.pending_storage

        if self.preserve_storage is not None:
            result['PreserveStorage'] = self.preserve_storage

        if self.project is not None:
            result['Project'] = self.project

        if self.total_storage is not None:
            result['TotalStorage'] = self.total_storage

        if self.ttl is not None:
            result['Ttl'] = self.ttl

        if self.type is not None:
            result['Type'] = self.type

        if self.uid is not None:
            result['Uid'] = self.uid

        if self.used_storage is not None:
            result['UsedStorage'] = self.used_storage

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeliveryRegion') is not None:
            self.delivery_region = m.get('DeliveryRegion')

        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('LogAnalysisConfig') is not None:
            self.log_analysis_config = m.get('LogAnalysisConfig')

        if m.get('LogStoreName') is not None:
            self.log_store_name = m.get('LogStoreName')

        if m.get('PendingStorage') is not None:
            self.pending_storage = m.get('PendingStorage')

        if m.get('PreserveStorage') is not None:
            self.preserve_storage = m.get('PreserveStorage')

        if m.get('Project') is not None:
            self.project = m.get('Project')

        if m.get('TotalStorage') is not None:
            self.total_storage = m.get('TotalStorage')

        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Uid') is not None:
            self.uid = m.get('Uid')

        if m.get('UsedStorage') is not None:
            self.used_storage = m.get('UsedStorage')

        return self

