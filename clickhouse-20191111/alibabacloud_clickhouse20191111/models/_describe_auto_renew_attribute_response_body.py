# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_clickhouse20191111 import models as main_models
from darabonba.model import DaraModel

class DescribeAutoRenewAttributeResponseBody(DaraModel):
    def __init__(
        self,
        items: main_models.DescribeAutoRenewAttributeResponseBodyItems = None,
        page_number: int = None,
        page_record_count: int = None,
        request_id: str = None,
        total_record_count: int = None,
    ):
        self.items = items
        self.page_number = page_number
        self.page_record_count = page_record_count
        self.request_id = request_id
        self.total_record_count = total_record_count

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.items is not None:
            result['Items'] = self.items.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Items') is not None:
            temp_model = main_models.DescribeAutoRenewAttributeResponseBodyItems()
            self.items = temp_model.from_map(m.get('Items'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')

        return self

class DescribeAutoRenewAttributeResponseBodyItems(DaraModel):
    def __init__(
        self,
        auto_renew_attribute: List[main_models.DescribeAutoRenewAttributeResponseBodyItemsAutoRenewAttribute] = None,
    ):
        self.auto_renew_attribute = auto_renew_attribute

    def validate(self):
        if self.auto_renew_attribute:
            for v1 in self.auto_renew_attribute:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AutoRenewAttribute'] = []
        if self.auto_renew_attribute is not None:
            for k1 in self.auto_renew_attribute:
                result['AutoRenewAttribute'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.auto_renew_attribute = []
        if m.get('AutoRenewAttribute') is not None:
            for k1 in m.get('AutoRenewAttribute'):
                temp_model = main_models.DescribeAutoRenewAttributeResponseBodyItemsAutoRenewAttribute()
                self.auto_renew_attribute.append(temp_model.from_map(k1))

        return self

class DescribeAutoRenewAttributeResponseBodyItemsAutoRenewAttribute(DaraModel):
    def __init__(
        self,
        auto_renew_enabled: bool = None,
        dbcluster_id: str = None,
        duration: int = None,
        period_unit: str = None,
        region_id: str = None,
        renewal_status: str = None,
    ):
        self.auto_renew_enabled = auto_renew_enabled
        self.dbcluster_id = dbcluster_id
        self.duration = duration
        self.period_unit = period_unit
        self.region_id = region_id
        self.renewal_status = renewal_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_renew_enabled is not None:
            result['AutoRenewEnabled'] = self.auto_renew_enabled

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.renewal_status is not None:
            result['RenewalStatus'] = self.renewal_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoRenewEnabled') is not None:
            self.auto_renew_enabled = m.get('AutoRenewEnabled')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RenewalStatus') is not None:
            self.renewal_status = m.get('RenewalStatus')

        return self

