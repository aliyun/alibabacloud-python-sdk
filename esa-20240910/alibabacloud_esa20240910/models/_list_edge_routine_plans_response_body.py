# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class ListEdgeRoutinePlansResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        plan_info: List[main_models.ListEdgeRoutinePlansResponseBodyPlanInfo] = None,
        request_id: str = None,
        total_count: int = None,
        total_page: int = None,
    ):
        # The page number. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Valid values: 1 to 500.
        self.page_size = page_size
        # The plans.
        self.plan_info = plan_info
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count
        # The total number of pages returned.
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
                temp_model = main_models.ListEdgeRoutinePlansResponseBodyPlanInfo()
                self.plan_info.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')

        return self

class ListEdgeRoutinePlansResponseBodyPlanInfo(DaraModel):
    def __init__(
        self,
        billing_mode: str = None,
        er_routine_code_version_quota: str = None,
        er_routine_quota: str = None,
        er_routine_route_site_count_quota: str = None,
        payment_method: str = None,
        plan_name: str = None,
    ):
        # The billing method. Valid values:
        # 
        # *   PREPAY: subscription.
        # *   POSTPAY: pay-as-you-go.
        self.billing_mode = billing_mode
        # The maximum number of versions that each routine supports.
        self.er_routine_code_version_quota = er_routine_code_version_quota
        # The maximum of routines that can be created.
        self.er_routine_quota = er_routine_quota
        # The maximum number of websites with which each routine can be associated.
        self.er_routine_route_site_count_quota = er_routine_route_site_count_quota
        # The payment method. Valid values:
        # 
        # *   er_free
        # *   er_pay
        self.payment_method = payment_method
        # The plan name.
        self.plan_name = plan_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.billing_mode is not None:
            result['BillingMode'] = self.billing_mode

        if self.er_routine_code_version_quota is not None:
            result['ErRoutineCodeVersionQuota'] = self.er_routine_code_version_quota

        if self.er_routine_quota is not None:
            result['ErRoutineQuota'] = self.er_routine_quota

        if self.er_routine_route_site_count_quota is not None:
            result['ErRoutineRouteSiteCountQuota'] = self.er_routine_route_site_count_quota

        if self.payment_method is not None:
            result['PaymentMethod'] = self.payment_method

        if self.plan_name is not None:
            result['PlanName'] = self.plan_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillingMode') is not None:
            self.billing_mode = m.get('BillingMode')

        if m.get('ErRoutineCodeVersionQuota') is not None:
            self.er_routine_code_version_quota = m.get('ErRoutineCodeVersionQuota')

        if m.get('ErRoutineQuota') is not None:
            self.er_routine_quota = m.get('ErRoutineQuota')

        if m.get('ErRoutineRouteSiteCountQuota') is not None:
            self.er_routine_route_site_count_quota = m.get('ErRoutineRouteSiteCountQuota')

        if m.get('PaymentMethod') is not None:
            self.payment_method = m.get('PaymentMethod')

        if m.get('PlanName') is not None:
            self.plan_name = m.get('PlanName')

        return self

