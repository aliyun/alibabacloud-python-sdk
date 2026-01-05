# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribePendingMaintenanceActionsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        type_list: List[main_models.DescribePendingMaintenanceActionsResponseBodyTypeList] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The details of pending events.
        self.type_list = type_list

    def validate(self):
        if self.type_list:
            for v1 in self.type_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['TypeList'] = []
        if self.type_list is not None:
            for k1 in self.type_list:
                result['TypeList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.type_list = []
        if m.get('TypeList') is not None:
            for k1 in m.get('TypeList'):
                temp_model = main_models.DescribePendingMaintenanceActionsResponseBodyTypeList()
                self.type_list.append(temp_model.from_map(k1))

        return self

class DescribePendingMaintenanceActionsResponseBodyTypeList(DaraModel):
    def __init__(
        self,
        count: int = None,
        task_type: str = None,
    ):
        # The number of pending events.
        self.count = count
        # The task type of pending events. Valid values:
        # 
        # *   **DatabaseSoftwareUpgrading**: database software upgrades
        # *   **DatabaseHardwareMaintenance**: hardware maintenance and upgrades
        # *   **DatabaseStorageUpgrading**: database storage upgrades
        # *   **DatabaseProxyUpgrading**: minor version upgrades of the proxy
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        return self

