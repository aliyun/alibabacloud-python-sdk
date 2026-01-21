# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cms20190101 import models as main_models
from darabonba.model import DaraModel

class DescribeMonitorResourceQuotaAttributeResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        resource_quota: main_models.DescribeMonitorResourceQuotaAttributeResponseBodyResourceQuota = None,
    ):
        # The status code.
        # 
        # > The status code 200 indicates that the request was successful.
        self.code = code
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The details about the resource quotas of CloudMonitor.
        self.resource_quota = resource_quota

    def validate(self):
        if self.resource_quota:
            self.resource_quota.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_quota is not None:
            result['ResourceQuota'] = self.resource_quota.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceQuota') is not None:
            temp_model = main_models.DescribeMonitorResourceQuotaAttributeResponseBodyResourceQuota()
            self.resource_quota = temp_model.from_map(m.get('ResourceQuota'))

        return self

class DescribeMonitorResourceQuotaAttributeResponseBodyResourceQuota(DaraModel):
    def __init__(
        self,
        api: main_models.DescribeMonitorResourceQuotaAttributeResponseBodyResourceQuotaApi = None,
        custom_monitor: main_models.DescribeMonitorResourceQuotaAttributeResponseBodyResourceQuotaCustomMonitor = None,
        enterprise_quota: main_models.DescribeMonitorResourceQuotaAttributeResponseBodyResourceQuotaEnterpriseQuota = None,
        event_monitor: main_models.DescribeMonitorResourceQuotaAttributeResponseBodyResourceQuotaEventMonitor = None,
        expire_time: str = None,
        instance_id: str = None,
        log_monitor: main_models.DescribeMonitorResourceQuotaAttributeResponseBodyResourceQuotaLogMonitor = None,
        phone: main_models.DescribeMonitorResourceQuotaAttributeResponseBodyResourceQuotaPhone = None,
        sms: main_models.DescribeMonitorResourceQuotaAttributeResponseBodyResourceQuotaSMS = None,
        site_monitor_browser: main_models.DescribeMonitorResourceQuotaAttributeResponseBodyResourceQuotaSiteMonitorBrowser = None,
        site_monitor_ecs_probe: main_models.DescribeMonitorResourceQuotaAttributeResponseBodyResourceQuotaSiteMonitorEcsProbe = None,
        site_monitor_mobile: main_models.DescribeMonitorResourceQuotaAttributeResponseBodyResourceQuotaSiteMonitorMobile = None,
        site_monitor_operator_probe: main_models.DescribeMonitorResourceQuotaAttributeResponseBodyResourceQuotaSiteMonitorOperatorProbe = None,
        site_monitor_task: main_models.DescribeMonitorResourceQuotaAttributeResponseBodyResourceQuotaSiteMonitorTask = None,
        suit_info: str = None,
    ):
        # The details about the quota of API calls.
        self.api = api
        # The details about the quota for custom monitoring.
        self.custom_monitor = custom_monitor
        # The details about the quota of Hybrid Cloud Monitoring.
        self.enterprise_quota = enterprise_quota
        # The details about the quota for event monitoring.
        self.event_monitor = event_monitor
        # The time when the resource plan expires.
        self.expire_time = expire_time
        # The ID of the resource plan.
        self.instance_id = instance_id
        # The details about the quota for log monitoring.
        self.log_monitor = log_monitor
        # The details about the quota of alert phone calls.
        self.phone = phone
        # The details about the quota of alert text messages.
        self.sms = sms
        # The quota of browser detection tasks.
        self.site_monitor_browser = site_monitor_browser
        # The details about the quota of ECS detection points for site monitoring.
        self.site_monitor_ecs_probe = site_monitor_ecs_probe
        # The quota of mobile detection tasks.
        self.site_monitor_mobile = site_monitor_mobile
        # The details about the quota of carrier detection points for site monitoring.
        self.site_monitor_operator_probe = site_monitor_operator_probe
        # The quota of site monitoring tasks.
        self.site_monitor_task = site_monitor_task
        # The current edition of CloudMonitor. Valid values:
        # 
        # *   free: Free Edition
        # *   pro: Pro Edition
        # *   cms_post: pay-as-you-go
        self.suit_info = suit_info

    def validate(self):
        if self.api:
            self.api.validate()
        if self.custom_monitor:
            self.custom_monitor.validate()
        if self.enterprise_quota:
            self.enterprise_quota.validate()
        if self.event_monitor:
            self.event_monitor.validate()
        if self.log_monitor:
            self.log_monitor.validate()
        if self.phone:
            self.phone.validate()
        if self.sms:
            self.sms.validate()
        if self.site_monitor_browser:
            self.site_monitor_browser.validate()
        if self.site_monitor_ecs_probe:
            self.site_monitor_ecs_probe.validate()
        if self.site_monitor_mobile:
            self.site_monitor_mobile.validate()
        if self.site_monitor_operator_probe:
            self.site_monitor_operator_probe.validate()
        if self.site_monitor_task:
            self.site_monitor_task.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api is not None:
            result['Api'] = self.api.to_map()

        if self.custom_monitor is not None:
            result['CustomMonitor'] = self.custom_monitor.to_map()

        if self.enterprise_quota is not None:
            result['EnterpriseQuota'] = self.enterprise_quota.to_map()

        if self.event_monitor is not None:
            result['EventMonitor'] = self.event_monitor.to_map()

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.log_monitor is not None:
            result['LogMonitor'] = self.log_monitor.to_map()

        if self.phone is not None:
            result['Phone'] = self.phone.to_map()

        if self.sms is not None:
            result['SMS'] = self.sms.to_map()

        if self.site_monitor_browser is not None:
            result['SiteMonitorBrowser'] = self.site_monitor_browser.to_map()

        if self.site_monitor_ecs_probe is not None:
            result['SiteMonitorEcsProbe'] = self.site_monitor_ecs_probe.to_map()

        if self.site_monitor_mobile is not None:
            result['SiteMonitorMobile'] = self.site_monitor_mobile.to_map()

        if self.site_monitor_operator_probe is not None:
            result['SiteMonitorOperatorProbe'] = self.site_monitor_operator_probe.to_map()

        if self.site_monitor_task is not None:
            result['SiteMonitorTask'] = self.site_monitor_task.to_map()

        if self.suit_info is not None:
            result['SuitInfo'] = self.suit_info

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Api') is not None:
            temp_model = main_models.DescribeMonitorResourceQuotaAttributeResponseBodyResourceQuotaApi()
            self.api = temp_model.from_map(m.get('Api'))

        if m.get('CustomMonitor') is not None:
            temp_model = main_models.DescribeMonitorResourceQuotaAttributeResponseBodyResourceQuotaCustomMonitor()
            self.custom_monitor = temp_model.from_map(m.get('CustomMonitor'))

        if m.get('EnterpriseQuota') is not None:
            temp_model = main_models.DescribeMonitorResourceQuotaAttributeResponseBodyResourceQuotaEnterpriseQuota()
            self.enterprise_quota = temp_model.from_map(m.get('EnterpriseQuota'))

        if m.get('EventMonitor') is not None:
            temp_model = main_models.DescribeMonitorResourceQuotaAttributeResponseBodyResourceQuotaEventMonitor()
            self.event_monitor = temp_model.from_map(m.get('EventMonitor'))

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('LogMonitor') is not None:
            temp_model = main_models.DescribeMonitorResourceQuotaAttributeResponseBodyResourceQuotaLogMonitor()
            self.log_monitor = temp_model.from_map(m.get('LogMonitor'))

        if m.get('Phone') is not None:
            temp_model = main_models.DescribeMonitorResourceQuotaAttributeResponseBodyResourceQuotaPhone()
            self.phone = temp_model.from_map(m.get('Phone'))

        if m.get('SMS') is not None:
            temp_model = main_models.DescribeMonitorResourceQuotaAttributeResponseBodyResourceQuotaSMS()
            self.sms = temp_model.from_map(m.get('SMS'))

        if m.get('SiteMonitorBrowser') is not None:
            temp_model = main_models.DescribeMonitorResourceQuotaAttributeResponseBodyResourceQuotaSiteMonitorBrowser()
            self.site_monitor_browser = temp_model.from_map(m.get('SiteMonitorBrowser'))

        if m.get('SiteMonitorEcsProbe') is not None:
            temp_model = main_models.DescribeMonitorResourceQuotaAttributeResponseBodyResourceQuotaSiteMonitorEcsProbe()
            self.site_monitor_ecs_probe = temp_model.from_map(m.get('SiteMonitorEcsProbe'))

        if m.get('SiteMonitorMobile') is not None:
            temp_model = main_models.DescribeMonitorResourceQuotaAttributeResponseBodyResourceQuotaSiteMonitorMobile()
            self.site_monitor_mobile = temp_model.from_map(m.get('SiteMonitorMobile'))

        if m.get('SiteMonitorOperatorProbe') is not None:
            temp_model = main_models.DescribeMonitorResourceQuotaAttributeResponseBodyResourceQuotaSiteMonitorOperatorProbe()
            self.site_monitor_operator_probe = temp_model.from_map(m.get('SiteMonitorOperatorProbe'))

        if m.get('SiteMonitorTask') is not None:
            temp_model = main_models.DescribeMonitorResourceQuotaAttributeResponseBodyResourceQuotaSiteMonitorTask()
            self.site_monitor_task = temp_model.from_map(m.get('SiteMonitorTask'))

        if m.get('SuitInfo') is not None:
            self.suit_info = m.get('SuitInfo')

        return self

class DescribeMonitorResourceQuotaAttributeResponseBodyResourceQuotaSiteMonitorTask(DaraModel):
    def __init__(
        self,
        quota_limit: int = None,
        quota_package: int = None,
        quota_used: int = None,
    ):
        # The total quota of site monitoring tasks.
        self.quota_limit = quota_limit
        # The quota of site monitoring tasks in your resource plan.
        self.quota_package = quota_package
        # The used quota of site monitoring tasks in your resource plan.
        self.quota_used = quota_used

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.quota_limit is not None:
            result['QuotaLimit'] = self.quota_limit

        if self.quota_package is not None:
            result['QuotaPackage'] = self.quota_package

        if self.quota_used is not None:
            result['QuotaUsed'] = self.quota_used

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('QuotaLimit') is not None:
            self.quota_limit = m.get('QuotaLimit')

        if m.get('QuotaPackage') is not None:
            self.quota_package = m.get('QuotaPackage')

        if m.get('QuotaUsed') is not None:
            self.quota_used = m.get('QuotaUsed')

        return self

class DescribeMonitorResourceQuotaAttributeResponseBodyResourceQuotaSiteMonitorOperatorProbe(DaraModel):
    def __init__(
        self,
        quota_limit: int = None,
        quota_package: int = None,
        quota_used: int = None,
    ):
        # The total quota of carrier detection points for site monitoring.
        self.quota_limit = quota_limit
        # The quota of carrier detection points for site monitoring in your resource plan.
        self.quota_package = quota_package
        # The used quota of carrier detection points for site monitoring in your resource plan.
        self.quota_used = quota_used

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.quota_limit is not None:
            result['QuotaLimit'] = self.quota_limit

        if self.quota_package is not None:
            result['QuotaPackage'] = self.quota_package

        if self.quota_used is not None:
            result['QuotaUsed'] = self.quota_used

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('QuotaLimit') is not None:
            self.quota_limit = m.get('QuotaLimit')

        if m.get('QuotaPackage') is not None:
            self.quota_package = m.get('QuotaPackage')

        if m.get('QuotaUsed') is not None:
            self.quota_used = m.get('QuotaUsed')

        return self

class DescribeMonitorResourceQuotaAttributeResponseBodyResourceQuotaSiteMonitorMobile(DaraModel):
    def __init__(
        self,
        quota_limit: int = None,
        quota_package: int = None,
        quota_used: int = None,
    ):
        # The total quota of mobile detection tasks.
        self.quota_limit = quota_limit
        # The quota of mobile detection tasks in your resource plan.
        self.quota_package = quota_package
        # The used quota of mobile detection tasks in your resource plan.
        self.quota_used = quota_used

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.quota_limit is not None:
            result['QuotaLimit'] = self.quota_limit

        if self.quota_package is not None:
            result['QuotaPackage'] = self.quota_package

        if self.quota_used is not None:
            result['QuotaUsed'] = self.quota_used

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('QuotaLimit') is not None:
            self.quota_limit = m.get('QuotaLimit')

        if m.get('QuotaPackage') is not None:
            self.quota_package = m.get('QuotaPackage')

        if m.get('QuotaUsed') is not None:
            self.quota_used = m.get('QuotaUsed')

        return self

class DescribeMonitorResourceQuotaAttributeResponseBodyResourceQuotaSiteMonitorEcsProbe(DaraModel):
    def __init__(
        self,
        quota_limit: int = None,
        quota_package: int = None,
        quota_used: int = None,
    ):
        # The total quota of ECS detection points for site monitoring.
        # 
        # > The value indicates the maximum number of ECS detection points that you can select for a site monitoring task.
        self.quota_limit = quota_limit
        # The quota of ECS detection points for site monitoring in your resource plan.
        self.quota_package = quota_package
        # The used quota of ECS detection points for site monitoring in your resource plan.
        # 
        # > The value indicates the total number of ECS detection points that are used by existing site monitoring tasks.
        self.quota_used = quota_used

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.quota_limit is not None:
            result['QuotaLimit'] = self.quota_limit

        if self.quota_package is not None:
            result['QuotaPackage'] = self.quota_package

        if self.quota_used is not None:
            result['QuotaUsed'] = self.quota_used

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('QuotaLimit') is not None:
            self.quota_limit = m.get('QuotaLimit')

        if m.get('QuotaPackage') is not None:
            self.quota_package = m.get('QuotaPackage')

        if m.get('QuotaUsed') is not None:
            self.quota_used = m.get('QuotaUsed')

        return self

class DescribeMonitorResourceQuotaAttributeResponseBodyResourceQuotaSiteMonitorBrowser(DaraModel):
    def __init__(
        self,
        quota_limit: int = None,
        quota_package: int = None,
        quota_used: int = None,
    ):
        # The total quota of browser detection tasks.
        self.quota_limit = quota_limit
        # The quota of browser detection tasks in your resource plan.
        self.quota_package = quota_package
        # The used quota of browser detection tasks in your resource plan.
        self.quota_used = quota_used

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.quota_limit is not None:
            result['QuotaLimit'] = self.quota_limit

        if self.quota_package is not None:
            result['QuotaPackage'] = self.quota_package

        if self.quota_used is not None:
            result['QuotaUsed'] = self.quota_used

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('QuotaLimit') is not None:
            self.quota_limit = m.get('QuotaLimit')

        if m.get('QuotaPackage') is not None:
            self.quota_package = m.get('QuotaPackage')

        if m.get('QuotaUsed') is not None:
            self.quota_used = m.get('QuotaUsed')

        return self

class DescribeMonitorResourceQuotaAttributeResponseBodyResourceQuotaSMS(DaraModel):
    def __init__(
        self,
        quota_limit: int = None,
        quota_package: int = None,
        quota_used: int = None,
    ):
        # The total quota of alert text messages. Unit: messages.
        self.quota_limit = quota_limit
        # The quota of alert text messages in your resource plan. Unit: messages.
        self.quota_package = quota_package
        # The used quota of alert text messages in your resource plan. Unit: messages.
        self.quota_used = quota_used

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.quota_limit is not None:
            result['QuotaLimit'] = self.quota_limit

        if self.quota_package is not None:
            result['QuotaPackage'] = self.quota_package

        if self.quota_used is not None:
            result['QuotaUsed'] = self.quota_used

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('QuotaLimit') is not None:
            self.quota_limit = m.get('QuotaLimit')

        if m.get('QuotaPackage') is not None:
            self.quota_package = m.get('QuotaPackage')

        if m.get('QuotaUsed') is not None:
            self.quota_used = m.get('QuotaUsed')

        return self

class DescribeMonitorResourceQuotaAttributeResponseBodyResourceQuotaPhone(DaraModel):
    def __init__(
        self,
        quota_limit: int = None,
        quota_package: int = None,
        quota_used: int = None,
    ):
        # The total quota of alert phone calls. Unit: calls.
        self.quota_limit = quota_limit
        # The quota of alert phone calls in your resource plan. Unit: calls.
        self.quota_package = quota_package
        # The used quota of alert phone calls in your resource plan. Unit: calls.
        self.quota_used = quota_used

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.quota_limit is not None:
            result['QuotaLimit'] = self.quota_limit

        if self.quota_package is not None:
            result['QuotaPackage'] = self.quota_package

        if self.quota_used is not None:
            result['QuotaUsed'] = self.quota_used

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('QuotaLimit') is not None:
            self.quota_limit = m.get('QuotaLimit')

        if m.get('QuotaPackage') is not None:
            self.quota_package = m.get('QuotaPackage')

        if m.get('QuotaUsed') is not None:
            self.quota_used = m.get('QuotaUsed')

        return self

class DescribeMonitorResourceQuotaAttributeResponseBodyResourceQuotaLogMonitor(DaraModel):
    def __init__(
        self,
        quota_limit: int = None,
        quota_package: int = None,
        quota_used: int = None,
    ):
        # The total quota of processed log data in log monitoring. Unit: MB/min.
        self.quota_limit = quota_limit
        # The quota of processed log data in log monitoring in your resource plan. Unit: MB/min.
        self.quota_package = quota_package
        # The used quota of processed log data in log monitoring in your resource plan. Unit: MB/min.
        self.quota_used = quota_used

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.quota_limit is not None:
            result['QuotaLimit'] = self.quota_limit

        if self.quota_package is not None:
            result['QuotaPackage'] = self.quota_package

        if self.quota_used is not None:
            result['QuotaUsed'] = self.quota_used

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('QuotaLimit') is not None:
            self.quota_limit = m.get('QuotaLimit')

        if m.get('QuotaPackage') is not None:
            self.quota_package = m.get('QuotaPackage')

        if m.get('QuotaUsed') is not None:
            self.quota_used = m.get('QuotaUsed')

        return self

class DescribeMonitorResourceQuotaAttributeResponseBodyResourceQuotaEventMonitor(DaraModel):
    def __init__(
        self,
        quota_limit: int = None,
        quota_package: int = None,
        quota_used: int = None,
    ):
        # The total quota of events that can be reported in event monitoring. The total quota is the value that is multiplied by 10,000.
        self.quota_limit = quota_limit
        # The quota of events that can be reported in event monitoring in your resource plan. The total quota is the value that is multiplied by 10,000.
        self.quota_package = quota_package
        # The used quota of events that can be reported in event monitoring in your resource plan. The total quota is the value that is multiplied by 10,000.
        self.quota_used = quota_used

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.quota_limit is not None:
            result['QuotaLimit'] = self.quota_limit

        if self.quota_package is not None:
            result['QuotaPackage'] = self.quota_package

        if self.quota_used is not None:
            result['QuotaUsed'] = self.quota_used

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('QuotaLimit') is not None:
            self.quota_limit = m.get('QuotaLimit')

        if m.get('QuotaPackage') is not None:
            self.quota_package = m.get('QuotaPackage')

        if m.get('QuotaUsed') is not None:
            self.quota_used = m.get('QuotaUsed')

        return self

class DescribeMonitorResourceQuotaAttributeResponseBodyResourceQuotaEnterpriseQuota(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        suit_info: str = None,
    ):
        # The ID of the instance monitored by Hybrid Cloud Monitoring.
        self.instance_id = instance_id
        # The description of Hybrid Cloud Monitoring.
        self.suit_info = suit_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.suit_info is not None:
            result['SuitInfo'] = self.suit_info

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('SuitInfo') is not None:
            self.suit_info = m.get('SuitInfo')

        return self

class DescribeMonitorResourceQuotaAttributeResponseBodyResourceQuotaCustomMonitor(DaraModel):
    def __init__(
        self,
        quota_limit: int = None,
        quota_package: int = None,
        quota_used: int = None,
    ):
        # The total quota of the time series for custom monitoring.
        self.quota_limit = quota_limit
        # The quota of the time series for custom monitoring in your resource plan.
        self.quota_package = quota_package
        # The used quota of the time series for custom monitoring in your resource plan.
        self.quota_used = quota_used

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.quota_limit is not None:
            result['QuotaLimit'] = self.quota_limit

        if self.quota_package is not None:
            result['QuotaPackage'] = self.quota_package

        if self.quota_used is not None:
            result['QuotaUsed'] = self.quota_used

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('QuotaLimit') is not None:
            self.quota_limit = m.get('QuotaLimit')

        if m.get('QuotaPackage') is not None:
            self.quota_package = m.get('QuotaPackage')

        if m.get('QuotaUsed') is not None:
            self.quota_used = m.get('QuotaUsed')

        return self

class DescribeMonitorResourceQuotaAttributeResponseBodyResourceQuotaApi(DaraModel):
    def __init__(
        self,
        quota_limit: int = None,
        quota_package: int = None,
        quota_used: int = None,
    ):
        # The total quota of API calls. Unit: 10,000 calls.
        self.quota_limit = quota_limit
        # The quota of API calls in your resource plan. Unit: 10,000 calls.
        self.quota_package = quota_package
        # The used quota of API calls in your resource plan. Unit: calls.
        self.quota_used = quota_used

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.quota_limit is not None:
            result['QuotaLimit'] = self.quota_limit

        if self.quota_package is not None:
            result['QuotaPackage'] = self.quota_package

        if self.quota_used is not None:
            result['QuotaUsed'] = self.quota_used

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('QuotaLimit') is not None:
            self.quota_limit = m.get('QuotaLimit')

        if m.get('QuotaPackage') is not None:
            self.quota_package = m.get('QuotaPackage')

        if m.get('QuotaUsed') is not None:
            self.quota_used = m.get('QuotaUsed')

        return self

