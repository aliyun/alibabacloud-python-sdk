# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribePolarFsQuotaListResponseBody(DaraModel):
    def __init__(
        self,
        page_number: str = None,
        page_record_count: str = None,
        page_size: str = None,
        polar_fs_instance_id: str = None,
        quota_items: List[main_models.DescribePolarFsQuotaListResponseBodyQuotaItems] = None,
        request_id: str = None,
        total_record_count: str = None,
    ):
        self.page_number = page_number
        self.page_record_count = page_record_count
        self.page_size = page_size
        self.polar_fs_instance_id = polar_fs_instance_id
        self.quota_items = quota_items
        # Id of the request
        self.request_id = request_id
        self.total_record_count = total_record_count

    def validate(self):
        if self.quota_items:
            for v1 in self.quota_items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.polar_fs_instance_id is not None:
            result['PolarFsInstanceId'] = self.polar_fs_instance_id

        result['QuotaItems'] = []
        if self.quota_items is not None:
            for k1 in self.quota_items:
                result['QuotaItems'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PolarFsInstanceId') is not None:
            self.polar_fs_instance_id = m.get('PolarFsInstanceId')

        self.quota_items = []
        if m.get('QuotaItems') is not None:
            for k1 in m.get('QuotaItems'):
                temp_model = main_models.DescribePolarFsQuotaListResponseBodyQuotaItems()
                self.quota_items.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')

        return self

class DescribePolarFsQuotaListResponseBodyQuotaItems(DaraModel):
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

