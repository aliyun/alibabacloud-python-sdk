# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudapi20160714 import models as main_models
from darabonba.model import DaraModel

class DescribePurchasedApiGroupsResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        purchased_api_group_attributes: main_models.DescribePurchasedApiGroupsResponseBodyPurchasedApiGroupAttributes = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned on each page.
        self.page_size = page_size
        # The attributes of the API group.
        self.purchased_api_group_attributes = purchased_api_group_attributes
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.purchased_api_group_attributes:
            self.purchased_api_group_attributes.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.purchased_api_group_attributes is not None:
            result['PurchasedApiGroupAttributes'] = self.purchased_api_group_attributes.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PurchasedApiGroupAttributes') is not None:
            temp_model = main_models.DescribePurchasedApiGroupsResponseBodyPurchasedApiGroupAttributes()
            self.purchased_api_group_attributes = temp_model.from_map(m.get('PurchasedApiGroupAttributes'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribePurchasedApiGroupsResponseBodyPurchasedApiGroupAttributes(DaraModel):
    def __init__(
        self,
        purchased_api_group_attribute: List[main_models.DescribePurchasedApiGroupsResponseBodyPurchasedApiGroupAttributesPurchasedApiGroupAttribute] = None,
    ):
        self.purchased_api_group_attribute = purchased_api_group_attribute

    def validate(self):
        if self.purchased_api_group_attribute:
            for v1 in self.purchased_api_group_attribute:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['PurchasedApiGroupAttribute'] = []
        if self.purchased_api_group_attribute is not None:
            for k1 in self.purchased_api_group_attribute:
                result['PurchasedApiGroupAttribute'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.purchased_api_group_attribute = []
        if m.get('PurchasedApiGroupAttribute') is not None:
            for k1 in m.get('PurchasedApiGroupAttribute'):
                temp_model = main_models.DescribePurchasedApiGroupsResponseBodyPurchasedApiGroupAttributesPurchasedApiGroupAttribute()
                self.purchased_api_group_attribute.append(temp_model.from_map(k1))

        return self

class DescribePurchasedApiGroupsResponseBodyPurchasedApiGroupAttributesPurchasedApiGroupAttribute(DaraModel):
    def __init__(
        self,
        billing_type: str = None,
        description: str = None,
        expire_time: str = None,
        group_id: str = None,
        group_name: str = None,
        invoke_times_max: int = None,
        invoke_times_now: int = None,
        purchased_time: str = None,
        region_id: str = None,
        status: str = None,
    ):
        # The billing method.
        self.billing_type = billing_type
        # The description of the API group.
        self.description = description
        # The time when the API group expires.
        self.expire_time = expire_time
        # The ID of the API group.
        self.group_id = group_id
        # The name of the API group.
        self.group_name = group_name
        # The maximum number of calls.
        self.invoke_times_max = invoke_times_max
        # The current number of calls.
        self.invoke_times_now = invoke_times_now
        # The time when the API group was purchased.
        self.purchased_time = purchased_time
        # The ID of the region where the API group is located.
        self.region_id = region_id
        # The status of the API group.
        # 
        # *   **NORMAL**: The API group is normal.
        # *   **DELETE**: The API group is deleted.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.billing_type is not None:
            result['BillingType'] = self.billing_type

        if self.description is not None:
            result['Description'] = self.description

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.invoke_times_max is not None:
            result['InvokeTimesMax'] = self.invoke_times_max

        if self.invoke_times_now is not None:
            result['InvokeTimesNow'] = self.invoke_times_now

        if self.purchased_time is not None:
            result['PurchasedTime'] = self.purchased_time

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillingType') is not None:
            self.billing_type = m.get('BillingType')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('InvokeTimesMax') is not None:
            self.invoke_times_max = m.get('InvokeTimesMax')

        if m.get('InvokeTimesNow') is not None:
            self.invoke_times_now = m.get('InvokeTimesNow')

        if m.get('PurchasedTime') is not None:
            self.purchased_time = m.get('PurchasedTime')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

