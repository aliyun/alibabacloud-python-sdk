# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListUserRatePlanInstancesRequest(DaraModel):
    def __init__(
        self,
        check_remaining_site_quota: str = None,
        instance_id: str = None,
        page_number: int = None,
        page_size: int = None,
        plan_name_en: str = None,
        plan_type: str = None,
        remaining_expire_days: int = None,
        sort_by: str = None,
        sort_order: str = None,
        status: str = None,
        subscribe_type: str = None,
    ):
        # Specifies whether to filter for rate plan instances that have a remaining site quota. Valid values:
        # 
        # - **true**: Returns only rate plan instances that have a remaining site quota.
        # 
        # - **false**: Returns all rate plan instances for the user.
        self.check_remaining_site_quota = check_remaining_site_quota
        # The ID of the rate plan instance to query.
        self.instance_id = instance_id
        # The page number. The default value is **1**. The value must be in the range of **1 to 100,000**.
        self.page_number = page_number
        # The number of entries to return on each page.
        self.page_size = page_size
        self.plan_name_en = plan_name_en
        self.plan_type = plan_type
        self.remaining_expire_days = remaining_expire_days
        # The sort field. By default, results are sorted by creation time. Valid values:
        # 
        # - **CreateTime**: Sorts by creation time.
        # 
        # - **ExpireTime**: Sorts by expiration time.
        self.sort_by = sort_by
        # The sort order. The default is descending. Valid values:
        # 
        # - **asc**: Sorts in ascending order.
        # 
        # - **desc**: Sorts in descending order.
        self.sort_order = sort_order
        # The status of the rate plan instance. Valid values:
        # 
        # - **online**: The instance is in service.
        # 
        # - **offline**: The instance has expired and is unavailable.
        # 
        # - **disable**: The instance is released.
        # 
        # - **overdue**: The instance is overdue.
        self.status = status
        self.subscribe_type = subscribe_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_remaining_site_quota is not None:
            result['CheckRemainingSiteQuota'] = self.check_remaining_site_quota

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.plan_name_en is not None:
            result['PlanNameEn'] = self.plan_name_en

        if self.plan_type is not None:
            result['PlanType'] = self.plan_type

        if self.remaining_expire_days is not None:
            result['RemainingExpireDays'] = self.remaining_expire_days

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order

        if self.status is not None:
            result['Status'] = self.status

        if self.subscribe_type is not None:
            result['SubscribeType'] = self.subscribe_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckRemainingSiteQuota') is not None:
            self.check_remaining_site_quota = m.get('CheckRemainingSiteQuota')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PlanNameEn') is not None:
            self.plan_name_en = m.get('PlanNameEn')

        if m.get('PlanType') is not None:
            self.plan_type = m.get('PlanType')

        if m.get('RemainingExpireDays') is not None:
            self.remaining_expire_days = m.get('RemainingExpireDays')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SubscribeType') is not None:
            self.subscribe_type = m.get('SubscribeType')

        return self

