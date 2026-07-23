# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListUserRatePlanInstancesRequest(DaraModel):
    def __init__(
        self,
        check_remaining_site_quota: str = None,
        instance_id: str = None,
        is_shared: bool = None,
        page_number: int = None,
        page_size: int = None,
        plan_name_en: str = None,
        plan_type: str = None,
        remaining_expire_days: int = None,
        resource_owner: int = None,
        sort_by: str = None,
        sort_order: str = None,
        status: str = None,
        subscribe_type: str = None,
    ):
        # Specifies whether to filter plan instances that have remaining site quota. Valid values:
        # 
        # - **true**: Filters plan instances that have remaining site quota.
        # - **false**: Queries all plan instances under the user.
        self.check_remaining_site_quota = check_remaining_site_quota
        # The plan instance ID. You can obtain this value by calling the [ListSites](https://help.aliyun.com/document_detail/2850189.html) operation.
        self.instance_id = instance_id
        self.is_shared = is_shared
        # The page number settings for paging. Default value: **1**. Valid values: **1 to 100000**.
        self.page_number = page_number
        # The number of entries per page for paging. Valid values: 1 to 500.
        self.page_size = page_size
        # The plan name (English).
        self.plan_name_en = plan_name_en
        # The plan type. Valid values:
        # 
        # - normal: fixed edition plan
        # - enterprise: enterprise edition plan
        self.plan_type = plan_type
        # Queries plan instances whose remaining validity period is within the specified number of days. The value must be a positive integer. Unit: days.
        self.remaining_expire_days = remaining_expire_days
        self.resource_owner = resource_owner
        # The sort field. By default, results are sorted by purchase time. Valid values:
        # 
        # - **CreateTime**: Purchase time.
        # - **ExpireTime**: Expiration time.
        self.sort_by = sort_by
        # The sort order. Default value: desc. Valid values:
        # 
        # - **asc**: Ascending order.
        # - **desc**: Descending order.
        self.sort_order = sort_order
        # The instance status. Valid values:
        # - **online**: Normal service status.
        # - **offline**: Expired but not overdue, in an inactive state.
        # - **disable**: Released.
        # - **overdue**: Overdue payment.
        self.status = status
        # The plan subscription type. Valid values:
        # 
        # - Free Edition (Chinese mainland): entranceplan
        # - Free Edition (International): entranceplan_intl
        # - Basic Edition: basicplan
        # - Standard Edition: standardplan
        # - Premium Edition: advancedplan
        # - Enterprise Edition: enterpriseplan
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

        if self.is_shared is not None:
            result['IsShared'] = self.is_shared

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

        if self.resource_owner is not None:
            result['ResourceOwner'] = self.resource_owner

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

        if m.get('IsShared') is not None:
            self.is_shared = m.get('IsShared')

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

        if m.get('ResourceOwner') is not None:
            self.resource_owner = m.get('ResourceOwner')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SubscribeType') is not None:
            self.subscribe_type = m.get('SubscribeType')

        return self

