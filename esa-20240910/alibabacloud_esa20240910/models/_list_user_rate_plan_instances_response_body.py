# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class ListUserRatePlanInstancesResponseBody(DaraModel):
    def __init__(
        self,
        instance_info: List[main_models.ListUserRatePlanInstancesResponseBodyInstanceInfo] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        total_page: int = None,
    ):
        # The queried plans.
        self.instance_info = instance_info
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count
        # The total number of pages returned.
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
                temp_model = main_models.ListUserRatePlanInstancesResponseBodyInstanceInfo()
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

class ListUserRatePlanInstancesResponseBodyInstanceInfo(DaraModel):
    def __init__(
        self,
        billing_mode: str = None,
        bot_instance_level: str = None,
        bot_request: str = None,
        coverages: str = None,
        create_time: str = None,
        crossborder_traffic: str = None,
        ddos_burstable_domestic_protection: str = None,
        ddos_burstable_overseas_protection: str = None,
        ddos_instance_level: str = None,
        duration: int = None,
        edge_routine_rquest: str = None,
        edge_waf_request: str = None,
        expire_time: str = None,
        instance_id: str = None,
        layer_4traffic: str = None,
        layer_4traffic_intl: str = None,
        plan_name: str = None,
        plan_traffic: str = None,
        plan_type: str = None,
        site_quota: str = None,
        sites: List[main_models.ListUserRatePlanInstancesResponseBodyInstanceInfoSites] = None,
        smart_routing_request: str = None,
        static_request: str = None,
        status: str = None,
        subscribe_type: str = None,
    ):
        # The billing method. Valid values:
        # 
        # *   PREPAY: subscription.
        # *   POSTPAY: pay-as-you-go.
        self.billing_mode = billing_mode
        self.bot_instance_level = bot_instance_level
        self.bot_request = bot_request
        # The service locations for the websites that can be associated with the plan. Multiple values are separated by commas (,). Valid values:
        # 
        # *   domestic: the Chinese mainland.
        # *   overseas: outside the Chinese mainland.
        # *   global: global.
        self.coverages = coverages
        # The time when the plan was purchased.
        self.create_time = create_time
        self.crossborder_traffic = crossborder_traffic
        self.ddos_burstable_domestic_protection = ddos_burstable_domestic_protection
        self.ddos_burstable_overseas_protection = ddos_burstable_overseas_protection
        self.ddos_instance_level = ddos_instance_level
        # The subscription duration of the plan. Unit: month.
        self.duration = duration
        self.edge_routine_rquest = edge_routine_rquest
        self.edge_waf_request = edge_waf_request
        # The time when the plan expires.
        self.expire_time = expire_time
        # The plan ID.
        self.instance_id = instance_id
        self.layer_4traffic = layer_4traffic
        self.layer_4traffic_intl = layer_4traffic_intl
        # The plan name.
        self.plan_name = plan_name
        self.plan_traffic = plan_traffic
        # The plan type. Valid values:
        # 
        # *   normal
        # *   enterprise
        self.plan_type = plan_type
        # The maximum number of websites that can be associated with the plan.
        self.site_quota = site_quota
        # The websites that have been associated with the plan.
        self.sites = sites
        self.smart_routing_request = smart_routing_request
        self.static_request = static_request
        # The plan status. Valid values:
        # 
        # *   online: The plan is in service.
        # *   offline: The plan has expired within an allowable period. In this state, the plan is unavailable.
        # *   disable: The plan is released.
        self.status = status
        self.subscribe_type = subscribe_type

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
        if self.billing_mode is not None:
            result['BillingMode'] = self.billing_mode

        if self.bot_instance_level is not None:
            result['BotInstanceLevel'] = self.bot_instance_level

        if self.bot_request is not None:
            result['BotRequest'] = self.bot_request

        if self.coverages is not None:
            result['Coverages'] = self.coverages

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.crossborder_traffic is not None:
            result['CrossborderTraffic'] = self.crossborder_traffic

        if self.ddos_burstable_domestic_protection is not None:
            result['DdosBurstableDomesticProtection'] = self.ddos_burstable_domestic_protection

        if self.ddos_burstable_overseas_protection is not None:
            result['DdosBurstableOverseasProtection'] = self.ddos_burstable_overseas_protection

        if self.ddos_instance_level is not None:
            result['DdosInstanceLevel'] = self.ddos_instance_level

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.edge_routine_rquest is not None:
            result['EdgeRoutineRquest'] = self.edge_routine_rquest

        if self.edge_waf_request is not None:
            result['EdgeWafRequest'] = self.edge_waf_request

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.layer_4traffic is not None:
            result['Layer4Traffic'] = self.layer_4traffic

        if self.layer_4traffic_intl is not None:
            result['Layer4TrafficIntl'] = self.layer_4traffic_intl

        if self.plan_name is not None:
            result['PlanName'] = self.plan_name

        if self.plan_traffic is not None:
            result['PlanTraffic'] = self.plan_traffic

        if self.plan_type is not None:
            result['PlanType'] = self.plan_type

        if self.site_quota is not None:
            result['SiteQuota'] = self.site_quota

        result['Sites'] = []
        if self.sites is not None:
            for k1 in self.sites:
                result['Sites'].append(k1.to_map() if k1 else None)

        if self.smart_routing_request is not None:
            result['SmartRoutingRequest'] = self.smart_routing_request

        if self.static_request is not None:
            result['StaticRequest'] = self.static_request

        if self.status is not None:
            result['Status'] = self.status

        if self.subscribe_type is not None:
            result['SubscribeType'] = self.subscribe_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillingMode') is not None:
            self.billing_mode = m.get('BillingMode')

        if m.get('BotInstanceLevel') is not None:
            self.bot_instance_level = m.get('BotInstanceLevel')

        if m.get('BotRequest') is not None:
            self.bot_request = m.get('BotRequest')

        if m.get('Coverages') is not None:
            self.coverages = m.get('Coverages')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CrossborderTraffic') is not None:
            self.crossborder_traffic = m.get('CrossborderTraffic')

        if m.get('DdosBurstableDomesticProtection') is not None:
            self.ddos_burstable_domestic_protection = m.get('DdosBurstableDomesticProtection')

        if m.get('DdosBurstableOverseasProtection') is not None:
            self.ddos_burstable_overseas_protection = m.get('DdosBurstableOverseasProtection')

        if m.get('DdosInstanceLevel') is not None:
            self.ddos_instance_level = m.get('DdosInstanceLevel')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('EdgeRoutineRquest') is not None:
            self.edge_routine_rquest = m.get('EdgeRoutineRquest')

        if m.get('EdgeWafRequest') is not None:
            self.edge_waf_request = m.get('EdgeWafRequest')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Layer4Traffic') is not None:
            self.layer_4traffic = m.get('Layer4Traffic')

        if m.get('Layer4TrafficIntl') is not None:
            self.layer_4traffic_intl = m.get('Layer4TrafficIntl')

        if m.get('PlanName') is not None:
            self.plan_name = m.get('PlanName')

        if m.get('PlanTraffic') is not None:
            self.plan_traffic = m.get('PlanTraffic')

        if m.get('PlanType') is not None:
            self.plan_type = m.get('PlanType')

        if m.get('SiteQuota') is not None:
            self.site_quota = m.get('SiteQuota')

        self.sites = []
        if m.get('Sites') is not None:
            for k1 in m.get('Sites'):
                temp_model = main_models.ListUserRatePlanInstancesResponseBodyInstanceInfoSites()
                self.sites.append(temp_model.from_map(k1))

        if m.get('SmartRoutingRequest') is not None:
            self.smart_routing_request = m.get('SmartRoutingRequest')

        if m.get('StaticRequest') is not None:
            self.static_request = m.get('StaticRequest')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SubscribeType') is not None:
            self.subscribe_type = m.get('SubscribeType')

        return self

class ListUserRatePlanInstancesResponseBodyInstanceInfoSites(DaraModel):
    def __init__(
        self,
        site_id: int = None,
        site_name: str = None,
        site_status: str = None,
    ):
        # The website ID.
        self.site_id = site_id
        # The website name.
        self.site_name = site_name
        # The website status. Valid values:
        # 
        # *   pending: The website is to be configured.
        # *   active: The website is active.
        # *   offline: The website is suspended.
        # *   moved: The website has been added and verified by another Alibaba Cloud account.
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

