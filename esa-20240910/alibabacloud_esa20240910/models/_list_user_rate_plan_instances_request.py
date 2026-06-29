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
        # Specifies whether to filter plan instances that have remaining site quota. Valid values:
        # 
        # - **true**: Filters plan instances that have remaining site quota.
        # - **false**: Queries all plan instances under the user.
        self.check_remaining_site_quota = check_remaining_site_quota
        # The plan instance ID. You can obtain the ID by calling the [ListSites](https://help.aliyun.com/document_detail/2850189.html) operation.
        self.instance_id = instance_id
        # The page number to return in a paged query. Default value: **1**. Valid values: **1** to **100000**. Settings for paging take effect only when this parameter is specified.
        self.page_number = page_number
        # The number of entries per page in a paged query. Valid values: 1 to 500. This parameter is used for paging.
        self.page_size = page_size
        # The plan name in English.
        self.plan_name_en = plan_name_en
        # The plan type. Valid values:
        # 
        # - normal: fixed-version plan
        # - enterprise: Enterprise Edition plan.
        self.plan_type = plan_type
        # Queries plan instances whose remaining validity period is within the specified number of days. The value must be a positive integer. Unit: days.
        self.remaining_expire_days = remaining_expire_days
        # The field by which to sort the results. By default, results are sorted by purchase time. Valid values:
        # 
        # - **CreateTime**: purchase time.
        # - **ExpireTime**: expiration time.
        self.sort_by = sort_by
        # The sort order. Default value: desc. Valid values:
        # 
        # - **asc**: ascending order.
        # - **desc**: descending order.
        self.sort_order = sort_order
        # The instance status. Valid values:
        # - **online**: The plan instance is in normal service.
        # - **offline**: The plan instance has expired but has not exceeded the grace period and is not active.
        # - **disable**: The plan instance has been released.
        # - **overdue**: The plan instance has an overdue payment.
        self.status = status
        # The plan subscription type. Valid values:
        # 
        # - entranceplan: Free Edition (Chinese mainland)
        # - entranceplan_intl: Free Edition (International)
        # - basicplan: Basic Edition
        # - standardplan: Standard Edition
        # - advancedplan: Premium Edition
        # - enterpriseplan: Enterprise Edition.
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

