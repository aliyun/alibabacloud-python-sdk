# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class ListPostpaidSitePlansResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        plan_info: List[main_models.ListPostpaidSitePlansResponseBodyPlanInfo] = None,
        request_id: str = None,
        total_count: int = None,
        total_page: int = None,
    ):
        # The page number. Default value: 1.
        self.page_number = page_number
        # The page size. Default value: 20. Maximum value: 500. Valid values: any integer from 1 to 500.
        self.page_size = page_size
        # The pay-as-you-go plan details.
        self.plan_info = plan_info
        # The request ID.
        self.request_id = request_id
        # The total number of entries.
        self.total_count = total_count
        # The total number of pages.
        self.total_page = total_page

    def validate(self):
        if self.plan_info:
            for v1 in self.plan_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        result['PlanInfo'] = []
        if self.plan_info is not None:
            for k1 in self.plan_info:
                result['PlanInfo'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.total_page is not None:
            result['TotalPage'] = self.total_page

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        self.plan_info = []
        if m.get('PlanInfo') is not None:
            for k1 in m.get('PlanInfo'):
                temp_model = main_models.ListPostpaidSitePlansResponseBodyPlanInfo()
                self.plan_info.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')

        return self

class ListPostpaidSitePlansResponseBodyPlanInfo(DaraModel):
    def __init__(
        self,
        billing_method: str = None,
        billing_mode: str = None,
        coverages: str = None,
        plan_name: str = None,
        plan_name_cn: str = None,
        plan_type: str = None,
        sale_status: str = None,
        site_quota: str = None,
    ):
        # The billable methods of the plan. Valid values:
        # - dps_month95: monthly 95th percentile billing method.
        self.billing_method = billing_method
        # The payment type. Valid values:
        # 
        # - PREPAY: subscription.
        # - POSTPAY: pay-as-you-go.
        self.billing_mode = billing_mode
        # The acceleration regions to which sites can be added under the plan. Multiple values are separated by commas (,). Valid values:
        # 
        # - domestic: the Chinese mainland.
        # - overseas: global (excluding the Chinese mainland).
        # - global: global (including the Chinese mainland).
        self.coverages = coverages
        # The name of the plan, which serves as a unique identifier in English.
        self.plan_name = plan_name
        # The plan description.
        self.plan_name_cn = plan_name_cn
        # The plan type of the plan instance. Valid values:
        # - normal: fixed edition plan.
        # - enterprise: enterprise edition plan.
        self.plan_type = plan_type
        # The sale status of the plan. Valid values for enterprise edition plans:
        # 
        # - saled: sold.
        # - upgrading: specification change in progress.
        self.sale_status = sale_status
        # The site quantity quota.
        self.site_quota = site_quota

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.billing_method is not None:
            result['BillingMethod'] = self.billing_method

        if self.billing_mode is not None:
            result['BillingMode'] = self.billing_mode

        if self.coverages is not None:
            result['Coverages'] = self.coverages

        if self.plan_name is not None:
            result['PlanName'] = self.plan_name

        if self.plan_name_cn is not None:
            result['PlanNameCn'] = self.plan_name_cn

        if self.plan_type is not None:
            result['PlanType'] = self.plan_type

        if self.sale_status is not None:
            result['SaleStatus'] = self.sale_status

        if self.site_quota is not None:
            result['SiteQuota'] = self.site_quota

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillingMethod') is not None:
            self.billing_method = m.get('BillingMethod')

        if m.get('BillingMode') is not None:
            self.billing_mode = m.get('BillingMode')

        if m.get('Coverages') is not None:
            self.coverages = m.get('Coverages')

        if m.get('PlanName') is not None:
            self.plan_name = m.get('PlanName')

        if m.get('PlanNameCn') is not None:
            self.plan_name_cn = m.get('PlanNameCn')

        if m.get('PlanType') is not None:
            self.plan_type = m.get('PlanType')

        if m.get('SaleStatus') is not None:
            self.sale_status = m.get('SaleStatus')

        if m.get('SiteQuota') is not None:
            self.site_quota = m.get('SiteQuota')

        return self

