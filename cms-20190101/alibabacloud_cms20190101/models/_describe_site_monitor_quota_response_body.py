# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cms20190101 import models as main_models
from darabonba.model import DaraModel

class DescribeSiteMonitorQuotaResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.DescribeSiteMonitorQuotaResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        # The responses code.
        # 
        # >  The status code 200 indicates that the request was successful.
        self.code = code
        # The quota.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
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
            temp_model = main_models.DescribeSiteMonitorQuotaResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeSiteMonitorQuotaResponseBodyData(DaraModel):
    def __init__(
        self,
        second_monitor: bool = None,
        site_monitor_idc_quota: int = None,
        site_monitor_operator_quota_quota: int = None,
        site_monitor_quota_task_used: int = None,
        site_monitor_task_quota: int = None,
        site_monitor_version: str = None,
    ):
        # Indicates whether second-level monitoring is enabled. Valid values:
        # 
        # *   true: Second-level monitoring is enabled.
        # *   false: Second-level monitoring is disabled.
        self.second_monitor = second_monitor
        # The quota of detection points that are provided by Alibaba Cloud. Five detection points are provided for free.
        self.site_monitor_idc_quota = site_monitor_idc_quota
        # The quota of detection points that are not provided by Alibaba Cloud. Default value: 0.
        self.site_monitor_operator_quota_quota = site_monitor_operator_quota_quota
        # The used quota of site monitoring tasks.
        self.site_monitor_quota_task_used = site_monitor_quota_task_used
        # The quota of site monitoring tasks.
        self.site_monitor_task_quota = site_monitor_task_quota
        # The version of site monitoring. Valid values:
        # 
        # *   V1
        # *   V2
        self.site_monitor_version = site_monitor_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.second_monitor is not None:
            result['SecondMonitor'] = self.second_monitor

        if self.site_monitor_idc_quota is not None:
            result['SiteMonitorIdcQuota'] = self.site_monitor_idc_quota

        if self.site_monitor_operator_quota_quota is not None:
            result['SiteMonitorOperatorQuotaQuota'] = self.site_monitor_operator_quota_quota

        if self.site_monitor_quota_task_used is not None:
            result['SiteMonitorQuotaTaskUsed'] = self.site_monitor_quota_task_used

        if self.site_monitor_task_quota is not None:
            result['SiteMonitorTaskQuota'] = self.site_monitor_task_quota

        if self.site_monitor_version is not None:
            result['SiteMonitorVersion'] = self.site_monitor_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecondMonitor') is not None:
            self.second_monitor = m.get('SecondMonitor')

        if m.get('SiteMonitorIdcQuota') is not None:
            self.site_monitor_idc_quota = m.get('SiteMonitorIdcQuota')

        if m.get('SiteMonitorOperatorQuotaQuota') is not None:
            self.site_monitor_operator_quota_quota = m.get('SiteMonitorOperatorQuotaQuota')

        if m.get('SiteMonitorQuotaTaskUsed') is not None:
            self.site_monitor_quota_task_used = m.get('SiteMonitorQuotaTaskUsed')

        if m.get('SiteMonitorTaskQuota') is not None:
            self.site_monitor_task_quota = m.get('SiteMonitorTaskQuota')

        if m.get('SiteMonitorVersion') is not None:
            self.site_monitor_version = m.get('SiteMonitorVersion')

        return self

