# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryAvailableInstancesRequest(DaraModel):
    def __init__(
        self,
        create_time_end: str = None,
        create_time_start: str = None,
        end_time_end: str = None,
        end_time_start: str = None,
        instance_ids: str = None,
        owner_id: int = None,
        page_num: int = None,
        page_size: int = None,
        product_code: str = None,
        product_type: str = None,
        region: str = None,
        renew_status: str = None,
        subscription_type: str = None,
    ):
        # The end time when the specified instance is created. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        self.create_time_end = create_time_end
        # The start time when the specified instance is created. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        self.create_time_start = create_time_start
        # The end of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC. Example: 2016-05-23T12:00:00Z.
        self.end_time_end = end_time_end
        # The beginning of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC. Example: 2016-05-23T12:00:00Z.
        self.end_time_start = end_time_start
        # The ID of the instance. Separate multiple IDs with commas (,). You can specify a maximum of 100 IDs.
        self.instance_ids = instance_ids
        self.owner_id = owner_id
        # The number of the page to return.
        self.page_num = page_num
        # The number of entries to return on each page.
        self.page_size = page_size
        # The code of the service. You can query the service code by calling the **QueryProductList** operation or viewing **Codes of Alibaba Cloud services**.
        # 
        # >This parameter cannot be left empty if the region is specified.
        self.product_code = product_code
        # The type of the service.
        self.product_type = product_type
        # The ID of the region in which the instance resides.
        self.region = region
        # The renewal status of the specified instance. Valid values:
        # 
        # *   AutoRenewal: The instance is automatically renewed.
        # *   ManualRenewal: The instance is manually renewed.
        # *   NotRenewal: The instance is not renewed.
        self.renew_status = renew_status
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
        if self.create_time_end is not None:
            result['CreateTimeEnd'] = self.create_time_end

        if self.create_time_start is not None:
            result['CreateTimeStart'] = self.create_time_start

        if self.end_time_end is not None:
            result['EndTimeEnd'] = self.end_time_end

        if self.end_time_start is not None:
            result['EndTimeStart'] = self.end_time_start

        if self.instance_ids is not None:
            result['InstanceIDs'] = self.instance_ids

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        if self.region is not None:
            result['Region'] = self.region

        if self.renew_status is not None:
            result['RenewStatus'] = self.renew_status

        if self.subscription_type is not None:
            result['SubscriptionType'] = self.subscription_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTimeEnd') is not None:
            self.create_time_end = m.get('CreateTimeEnd')

        if m.get('CreateTimeStart') is not None:
            self.create_time_start = m.get('CreateTimeStart')

        if m.get('EndTimeEnd') is not None:
            self.end_time_end = m.get('EndTimeEnd')

        if m.get('EndTimeStart') is not None:
            self.end_time_start = m.get('EndTimeStart')

        if m.get('InstanceIDs') is not None:
            self.instance_ids = m.get('InstanceIDs')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('RenewStatus') is not None:
            self.renew_status = m.get('RenewStatus')

        if m.get('SubscriptionType') is not None:
            self.subscription_type = m.get('SubscriptionType')

        return self

