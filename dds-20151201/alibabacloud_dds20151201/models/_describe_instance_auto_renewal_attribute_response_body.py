# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dds20151201 import models as main_models
from darabonba.model import DaraModel

class DescribeInstanceAutoRenewalAttributeResponseBody(DaraModel):
    def __init__(
        self,
        items: main_models.DescribeInstanceAutoRenewalAttributeResponseBodyItems = None,
        items_numbers: int = None,
        page_number: int = None,
        page_record_count: int = None,
        request_id: str = None,
    ):
        # Details about returned entries.
        self.items = items
        # The total number of entries returned.
        self.items_numbers = items_numbers
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries that were returned on the current page.
        self.page_record_count = page_record_count
        # The ID of the request.
        self.request_id = request_id

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

        if self.items_numbers is not None:
            result['ItemsNumbers'] = self.items_numbers

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Items') is not None:
            temp_model = main_models.DescribeInstanceAutoRenewalAttributeResponseBodyItems()
            self.items = temp_model.from_map(m.get('Items'))

        if m.get('ItemsNumbers') is not None:
            self.items_numbers = m.get('ItemsNumbers')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeInstanceAutoRenewalAttributeResponseBodyItems(DaraModel):
    def __init__(
        self,
        item: List[main_models.DescribeInstanceAutoRenewalAttributeResponseBodyItemsItem] = None,
    ):
        self.item = item

    def validate(self):
        if self.item:
            for v1 in self.item:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Item'] = []
        if self.item is not None:
            for k1 in self.item:
                result['Item'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.item = []
        if m.get('Item') is not None:
            for k1 in m.get('Item'):
                temp_model = main_models.DescribeInstanceAutoRenewalAttributeResponseBodyItemsItem()
                self.item.append(temp_model.from_map(k1))

        return self

class DescribeInstanceAutoRenewalAttributeResponseBodyItemsItem(DaraModel):
    def __init__(
        self,
        auto_renew: str = None,
        dbinstance_type: str = None,
        db_instance_id: str = None,
        duration: str = None,
        region_id: str = None,
    ):
        # Indicates whether auto-renewal is enabled for the instance. Valid values:
        # 
        # *   **true**: Auto-renewal is enabled for the instance.
        # *   **false**: Auto-renewal is disabled for the instance.
        self.auto_renew = auto_renew
        # The category of the instance. Valid values:
        # 
        # *   **replicate**: the standalone or replica set instance
        # *   **sharding**: the sharded cluster instance
        self.dbinstance_type = dbinstance_type
        # The ID of the instance.
        self.db_instance_id = db_instance_id
        # The auto-renewal period. Unit: months.
        # 
        # > * This parameter is ruturned only when the returned value of the **AutoRenew** parameter is **true**.
        # > * You can call the [ModifyInstanceAutoRenewalAttribute](https://help.aliyun.com/document_detail/145979.html) operation to modify the auto-renewal period.
        self.duration = duration
        # The region ID of the instance.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew

        if self.dbinstance_type is not None:
            result['DBInstanceType'] = self.dbinstance_type

        if self.db_instance_id is not None:
            result['DbInstanceId'] = self.db_instance_id

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')

        if m.get('DBInstanceType') is not None:
            self.dbinstance_type = m.get('DBInstanceType')

        if m.get('DbInstanceId') is not None:
            self.db_instance_id = m.get('DbInstanceId')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

