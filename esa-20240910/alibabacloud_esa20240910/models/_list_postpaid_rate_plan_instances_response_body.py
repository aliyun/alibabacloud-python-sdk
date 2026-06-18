# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class ListPostpaidRatePlanInstancesResponseBody(DaraModel):
    def __init__(
        self,
        instance_info: List[main_models.ListPostpaidRatePlanInstancesResponseBodyInstanceInfo] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        total_page: int = None,
    ):
        # A list of instances.
        self.instance_info = instance_info
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID, used for troubleshooting.
        self.request_id = request_id
        # The total number of entries.
        self.total_count = total_count
        # The total number of pages.
        self.total_page = total_page

    def validate(self):
        if self.instance_info:
            for v1 in self.instance_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['InstanceInfo'] = []
        if self.instance_info is not None:
            for k1 in self.instance_info:
                result['InstanceInfo'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.total_page is not None:
            result['TotalPage'] = self.total_page

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_info = []
        if m.get('InstanceInfo') is not None:
            for k1 in m.get('InstanceInfo'):
                temp_model = main_models.ListPostpaidRatePlanInstancesResponseBodyInstanceInfo()
                self.instance_info.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')

        return self

class ListPostpaidRatePlanInstancesResponseBodyInstanceInfo(DaraModel):
    def __init__(
        self,
        billing_method: str = None,
        billing_mode: str = None,
        coverages: str = None,
        create_time: str = None,
        expected_update_time: str = None,
        instance_id: str = None,
        plan_name: str = None,
        plan_name_cn: str = None,
        plan_type: str = None,
        site_quota: str = None,
        sites: List[main_models.ListPostpaidRatePlanInstancesResponseBodyInstanceInfoSites] = None,
        status: str = None,
    ):
        # The billing method. Valid value:
        # 
        # - `dps_month95`: Monthly 95th percentile.
        self.billing_method = billing_method
        # The billing mode. Valid value:
        # 
        # - `POSTPAY`: pay-as-you-go.
        self.billing_mode = billing_mode
        # The coverage area of the instance. Only sites within this area can be bound to the instance. If multiple areas are supported, they are separated by a comma (`,`). Valid values:
        # 
        # - `domestic`: Chinese mainland.
        # 
        # - `overseas`: Regions outside the Chinese mainland.
        # 
        # - `global`: Global (including the Chinese mainland).
        self.coverages = coverages
        # The time when the instance was created.
        self.create_time = create_time
        # The time of a scheduled configuration change.
        self.expected_update_time = expected_update_time
        # The ID of the instance.
        self.instance_id = instance_id
        # The plan name in English.
        self.plan_name = plan_name
        # The plan name in Chinese.
        self.plan_name_cn = plan_name_cn
        # The type of the plan. Valid values:
        # 
        # - `normal`: Normal plan.
        # 
        # - `enterprise`: Enterprise plan.
        self.plan_type = plan_type
        # The maximum number of sites that can be bound to the instance.
        self.site_quota = site_quota
        # A list of sites bound to the instance.
        self.sites = sites
        # The status of the instance.
        self.status = status

    def validate(self):
        if self.sites:
            for v1 in self.sites:
                 if v1:
                    v1.validate()

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

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.expected_update_time is not None:
            result['ExpectedUpdateTime'] = self.expected_update_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.plan_name is not None:
            result['PlanName'] = self.plan_name

        if self.plan_name_cn is not None:
            result['PlanNameCn'] = self.plan_name_cn

        if self.plan_type is not None:
            result['PlanType'] = self.plan_type

        if self.site_quota is not None:
            result['SiteQuota'] = self.site_quota

        result['Sites'] = []
        if self.sites is not None:
            for k1 in self.sites:
                result['Sites'].append(k1.to_map() if k1 else None)

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillingMethod') is not None:
            self.billing_method = m.get('BillingMethod')

        if m.get('BillingMode') is not None:
            self.billing_mode = m.get('BillingMode')

        if m.get('Coverages') is not None:
            self.coverages = m.get('Coverages')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('ExpectedUpdateTime') is not None:
            self.expected_update_time = m.get('ExpectedUpdateTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PlanName') is not None:
            self.plan_name = m.get('PlanName')

        if m.get('PlanNameCn') is not None:
            self.plan_name_cn = m.get('PlanNameCn')

        if m.get('PlanType') is not None:
            self.plan_type = m.get('PlanType')

        if m.get('SiteQuota') is not None:
            self.site_quota = m.get('SiteQuota')

        self.sites = []
        if m.get('Sites') is not None:
            for k1 in m.get('Sites'):
                temp_model = main_models.ListPostpaidRatePlanInstancesResponseBodyInstanceInfoSites()
                self.sites.append(temp_model.from_map(k1))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class ListPostpaidRatePlanInstancesResponseBodyInstanceInfoSites(DaraModel):
    def __init__(
        self,
        site_id: int = None,
        site_name: str = None,
        site_status: str = None,
    ):
        # The ID of the site.
        self.site_id = site_id
        # The name of the site.
        self.site_name = site_name
        # The status of the site. Valid values:
        # 
        # - `pending`: The site is awaiting configuration.
        # 
        # - `active`: The site is active.
        # 
        # - `offline`: The site is offline.
        # 
        # - `moved`: The site has been replaced.
        self.site_status = site_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.site_id is not None:
            result['SiteId'] = self.site_id

        if self.site_name is not None:
            result['SiteName'] = self.site_name

        if self.site_status is not None:
            result['SiteStatus'] = self.site_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        if m.get('SiteName') is not None:
            self.site_name = m.get('SiteName')

        if m.get('SiteStatus') is not None:
            self.site_status = m.get('SiteStatus')

        return self

