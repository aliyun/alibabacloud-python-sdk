# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bssopenapi20171214 import models as main_models
from darabonba.model import DaraModel

class QueryAvailableInstancesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.QueryAvailableInstancesResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The status code returned.
        self.code = code
        # The data returned.
        self.data = data
        # The message returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request is successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.QueryAvailableInstancesResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryAvailableInstancesResponseBodyData(DaraModel):
    def __init__(
        self,
        instance_list: List[main_models.QueryAvailableInstancesResponseBodyDataInstanceList] = None,
        page_num: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The instances returned.
        self.instance_list = instance_list
        # The page number of the returned page.
        self.page_num = page_num
        # The number of entries returned per page.
        self.page_size = page_size
        # The total number of returned entries.
        self.total_count = total_count

    def validate(self):
        if self.instance_list:
            for v1 in self.instance_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['InstanceList'] = []
        if self.instance_list is not None:
            for k1 in self.instance_list:
                result['InstanceList'].append(k1.to_map() if k1 else None)

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_list = []
        if m.get('InstanceList') is not None:
            for k1 in m.get('InstanceList'):
                temp_model = main_models.QueryAvailableInstancesResponseBodyDataInstanceList()
                self.instance_list.append(temp_model.from_map(k1))

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class QueryAvailableInstancesResponseBodyDataInstanceList(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        end_time: str = None,
        expected_release_time: str = None,
        instance_id: str = None,
        owner_id: int = None,
        product_code: str = None,
        product_type: str = None,
        region: str = None,
        release_time: str = None,
        renew_status: str = None,
        renewal_duration: int = None,
        renewal_duration_unit: str = None,
        seller: str = None,
        seller_id: int = None,
        status: str = None,
        stop_time: str = None,
        sub_status: str = None,
        subscription_type: str = None,
    ):
        # The time when the specified instance was created.
        self.create_time = create_time
        # The time when the instance was expired.
        self.end_time = end_time
        # The time when the specified instance was expected to be released.
        self.expected_release_time = expected_release_time
        # The ID of the instance.
        self.instance_id = instance_id
        # The ID of the instance owner.
        self.owner_id = owner_id
        # The code of the service.
        self.product_code = product_code
        # The type of the service.
        self.product_type = product_type
        # The ID of the region in which the instance resides.
        self.region = region
        # The time when the instance was released.
        self.release_time = release_time
        # The renewal status of the specified instance. Valid values:
        # 
        # *   AutoRenewal: The instance is automatically renewed.
        # *   ManualRenewal: The instance is manually renewed.
        # *   NotRenewal: The instance is not renewed.
        self.renew_status = renew_status
        # The number of auto-renewal cycles.
        self.renewal_duration = renewal_duration
        # The unit of the auto-renewal cycle. Valid values:
        # 
        # *   M: month
        # *   Y: year
        self.renewal_duration_unit = renewal_duration_unit
        # The seller.
        self.seller = seller
        # The ID of the seller.
        self.seller_id = seller_id
        # The status of the instance.
        self.status = status
        # The time when the specified instance was suspended.
        self.stop_time = stop_time
        # The sub-status of the specified instance.
        self.sub_status = sub_status
        # The billing method. Valid values:
        # 
        # *   Subscription: subscription
        # *   PayAsYouGo: pay-as-you-go
        self.subscription_type = subscription_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.expected_release_time is not None:
            result['ExpectedReleaseTime'] = self.expected_release_time

        if self.instance_id is not None:
            result['InstanceID'] = self.instance_id

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        if self.region is not None:
            result['Region'] = self.region

        if self.release_time is not None:
            result['ReleaseTime'] = self.release_time

        if self.renew_status is not None:
            result['RenewStatus'] = self.renew_status

        if self.renewal_duration is not None:
            result['RenewalDuration'] = self.renewal_duration

        if self.renewal_duration_unit is not None:
            result['RenewalDurationUnit'] = self.renewal_duration_unit

        if self.seller is not None:
            result['Seller'] = self.seller

        if self.seller_id is not None:
            result['SellerId'] = self.seller_id

        if self.status is not None:
            result['Status'] = self.status

        if self.stop_time is not None:
            result['StopTime'] = self.stop_time

        if self.sub_status is not None:
            result['SubStatus'] = self.sub_status

        if self.subscription_type is not None:
            result['SubscriptionType'] = self.subscription_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('ExpectedReleaseTime') is not None:
            self.expected_release_time = m.get('ExpectedReleaseTime')

        if m.get('InstanceID') is not None:
            self.instance_id = m.get('InstanceID')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('ReleaseTime') is not None:
            self.release_time = m.get('ReleaseTime')

        if m.get('RenewStatus') is not None:
            self.renew_status = m.get('RenewStatus')

        if m.get('RenewalDuration') is not None:
            self.renewal_duration = m.get('RenewalDuration')

        if m.get('RenewalDurationUnit') is not None:
            self.renewal_duration_unit = m.get('RenewalDurationUnit')

        if m.get('Seller') is not None:
            self.seller = m.get('Seller')

        if m.get('SellerId') is not None:
            self.seller_id = m.get('SellerId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StopTime') is not None:
            self.stop_time = m.get('StopTime')

        if m.get('SubStatus') is not None:
            self.sub_status = m.get('SubStatus')

        if m.get('SubscriptionType') is not None:
            self.subscription_type = m.get('SubscriptionType')

        return self

