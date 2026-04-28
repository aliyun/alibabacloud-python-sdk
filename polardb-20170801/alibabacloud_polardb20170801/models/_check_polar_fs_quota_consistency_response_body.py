# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class CheckPolarFsQuotaConsistencyResponseBody(DaraModel):
    def __init__(
        self,
        polar_fs_instance_id: str = None,
        quota_item: main_models.CheckPolarFsQuotaConsistencyResponseBodyQuotaItem = None,
        request_id: str = None,
    ):
        self.polar_fs_instance_id = polar_fs_instance_id
        self.quota_item = quota_item
        self.request_id = request_id

    def validate(self):
        if self.quota_item:
            self.quota_item.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.polar_fs_instance_id is not None:
            result['PolarFsInstanceId'] = self.polar_fs_instance_id

        if self.quota_item is not None:
            result['QuotaItem'] = self.quota_item.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolarFsInstanceId') is not None:
            self.polar_fs_instance_id = m.get('PolarFsInstanceId')

        if m.get('QuotaItem') is not None:
            temp_model = main_models.CheckPolarFsQuotaConsistencyResponseBodyQuotaItem()
            self.quota_item = temp_model.from_map(m.get('QuotaItem'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CheckPolarFsQuotaConsistencyResponseBodyQuotaItem(DaraModel):
    def __init__(
        self,
        capacity: int = None,
        inodes: int = None,
        path: str = None,
        used_capacity: int = None,
        used_inodes: int = None,
    ):
        self.capacity = capacity
        # Inodes
        self.inodes = inodes
        self.path = path
        self.used_capacity = used_capacity
        self.used_inodes = used_inodes

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.capacity is not None:
            result['Capacity'] = self.capacity

        if self.inodes is not None:
            result['Inodes'] = self.inodes

        if self.path is not None:
            result['Path'] = self.path

        if self.used_capacity is not None:
            result['UsedCapacity'] = self.used_capacity

        if self.used_inodes is not None:
            result['UsedInodes'] = self.used_inodes

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')

        if m.get('Inodes') is not None:
            self.inodes = m.get('Inodes')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        if m.get('UsedCapacity') is not None:
            self.used_capacity = m.get('UsedCapacity')

        if m.get('UsedInodes') is not None:
            self.used_inodes = m.get('UsedInodes')

        return self

