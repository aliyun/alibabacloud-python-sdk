# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_adb20211201 import models as main_models
from darabonba.model import DaraModel

class DescribeAutoRenewalAttributeResponseBody(DaraModel):
    def __init__(
        self,
        items: main_models.DescribeAutoRenewalAttributeResponseBodyItems = None,
        page_number: int = None,
        page_record_count: int = None,
        request_id: str = None,
        total_record_count: int = None,
    ):
        # The list of auto-renewal details.
        self.items = items
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned on each page.
        self.page_record_count = page_record_count
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
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
            temp_model = main_models.DescribeAutoRenewalAttributeResponseBodyItems()
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

class DescribeAutoRenewalAttributeResponseBodyItems(DaraModel):
    def __init__(
        self,
        auto_renewal_attribute: List[main_models.DescribeAutoRenewalAttributeResponseBodyItemsAutoRenewalAttribute] = None,
    ):
        self.auto_renewal_attribute = auto_renewal_attribute

    def validate(self):
        if self.auto_renewal_attribute:
            for v1 in self.auto_renewal_attribute:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AutoRenewalAttribute'] = []
        if self.auto_renewal_attribute is not None:
            for k1 in self.auto_renewal_attribute:
                result['AutoRenewalAttribute'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.auto_renewal_attribute = []
        if m.get('AutoRenewalAttribute') is not None:
            for k1 in m.get('AutoRenewalAttribute'):
                temp_model = main_models.DescribeAutoRenewalAttributeResponseBodyItemsAutoRenewalAttribute()
                self.auto_renewal_attribute.append(temp_model.from_map(k1))

        return self

class DescribeAutoRenewalAttributeResponseBodyItemsAutoRenewalAttribute(DaraModel):
    def __init__(
        self,
        auto_renewal_enabled: bool = None,
        auto_renewal_period: int = None,
        auto_renewal_period_unit: str = None,
        auto_renewal_status: str = None,
        dbcluster_id: str = None,
        region_id: str = None,
    ):
        # Indicates whether auto-renewal is enabled for the cluster. Valid values:
        # 
        # *   **true**: Enables.
        # *   **false**: Disables.
        self.auto_renewal_enabled = auto_renewal_enabled
        # The auto-renewal duration.
        self.auto_renewal_period = auto_renewal_period
        # The unit of auto-renewal duration. Valid values:
        # 
        # *   **Year**
        # *   **Month**
        self.auto_renewal_period_unit = auto_renewal_period_unit
        # The renewal method. Valid values:
        # 
        # *   **AutoRenewal**: The cluster is automatically renewed.
        # *   **Normal**: The cluster is manually renewed. Before the cluster expires, the system sends you a reminder by SMS message.
        # *   **NotRenewal**: The cluster is not renewed. Reminders are only sent three days before cluster expiration.
        self.auto_renewal_status = auto_renewal_status
        # The cluster ID.
        self.dbcluster_id = dbcluster_id
        # The region ID.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_renewal_enabled is not None:
            result['AutoRenewalEnabled'] = self.auto_renewal_enabled

        if self.auto_renewal_period is not None:
            result['AutoRenewalPeriod'] = self.auto_renewal_period

        if self.auto_renewal_period_unit is not None:
            result['AutoRenewalPeriodUnit'] = self.auto_renewal_period_unit

        if self.auto_renewal_status is not None:
            result['AutoRenewalStatus'] = self.auto_renewal_status

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoRenewalEnabled') is not None:
            self.auto_renewal_enabled = m.get('AutoRenewalEnabled')

        if m.get('AutoRenewalPeriod') is not None:
            self.auto_renewal_period = m.get('AutoRenewalPeriod')

        if m.get('AutoRenewalPeriodUnit') is not None:
            self.auto_renewal_period_unit = m.get('AutoRenewalPeriodUnit')

        if m.get('AutoRenewalStatus') is not None:
            self.auto_renewal_status = m.get('AutoRenewalStatus')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

