# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alidns20150109 import models as main_models
from darabonba.model import DaraModel

class SearchCloudGtmInstancesResponseBody(DaraModel):
    def __init__(
        self,
        instances: main_models.SearchCloudGtmInstancesResponseBodyInstances = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_items: int = None,
        total_pages: int = None,
    ):
        # The instances.
        self.instances = instances
        # Current page number, starting at **1**, default is **1**.
        self.page_number = page_number
        # The number of rows per page when paginating queries, with a maximum value of 100 and a default of 20.
        self.page_size = page_size
        # Unique request identification code.
        self.request_id = request_id
        # Total number of instances found from the search.
        self.total_items = total_items
        # Total number of pages.
        self.total_pages = total_pages

    def validate(self):
        if self.instances:
            self.instances.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instances is not None:
            result['Instances'] = self.instances.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_items is not None:
            result['TotalItems'] = self.total_items

        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Instances') is not None:
            temp_model = main_models.SearchCloudGtmInstancesResponseBodyInstances()
            self.instances = temp_model.from_map(m.get('Instances'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalItems') is not None:
            self.total_items = m.get('TotalItems')

        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')

        return self

class SearchCloudGtmInstancesResponseBodyInstances(DaraModel):
    def __init__(
        self,
        instance: List[main_models.SearchCloudGtmInstancesResponseBodyInstancesInstance] = None,
    ):
        self.instance = instance

    def validate(self):
        if self.instance:
            for v1 in self.instance:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Instance'] = []
        if self.instance is not None:
            for k1 in self.instance:
                result['Instance'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance = []
        if m.get('Instance') is not None:
            for k1 in m.get('Instance'):
                temp_model = main_models.SearchCloudGtmInstancesResponseBodyInstancesInstance()
                self.instance.append(temp_model.from_map(k1))

        return self

class SearchCloudGtmInstancesResponseBodyInstancesInstance(DaraModel):
    def __init__(
        self,
        charge_type: str = None,
        commodity_code: str = None,
        create_time: str = None,
        create_timestamp: int = None,
        expire_time: int = None,
        expire_timestamp: str = None,
        instance_id: str = None,
        instance_name: str = None,
        monitor_task_quota: int = None,
        monthly_email_used: int = None,
        monthly_sms_quota: int = None,
        monthly_sms_used: int = None,
        monthly_webhook_used: int = None,
        schedule_domain_name: str = None,
        update_time: str = None,
        update_timestamp: int = None,
        version_code: str = None,
    ):
        self.charge_type = charge_type
        # The commodity code. Valid values:
        # 
        # *   dns_gtm_public_cn: commodity code on the China site (aliyun.com)
        # *   dns_gtm_public_intl: commodity code on the international site (alibabacloud.com)
        self.commodity_code = commodity_code
        # Instance creation time.
        self.create_time = create_time
        # Instance creation time (timestamp).
        self.create_timestamp = create_timestamp
        # Instance expiration time.
        self.expire_time = expire_time
        # Instance expiration time (timestamp).
        self.expire_timestamp = expire_timestamp
        # The ID of the GTM 3.0 instance.
        self.instance_id = instance_id
        # Schedule instance name.
        self.instance_name = instance_name
        # Monitor probe task quota.
        self.monitor_task_quota = monitor_task_quota
        # Monthly email sending volume.
        self.monthly_email_used = monthly_email_used
        # SMS quota, only supported on the China site. International site does not support SMS.
        self.monthly_sms_quota = monthly_sms_quota
        # Monthly SMS sending volume, only supported by the China site as international sites do not support SMS.
        self.monthly_sms_used = monthly_sms_used
        # Monthly webhook dispatch volume.
        self.monthly_webhook_used = monthly_webhook_used
        # The access domain name, which consists of a hostname and a zone or a subzone.
        self.schedule_domain_name = schedule_domain_name
        # The last modified time of the instance.
        self.update_time = update_time
        # The last modified time of the instance (timestamp).
        self.update_timestamp = update_timestamp
        # Global Traffic Management version 3.0 instance types:
        # - standard: Standard Edition
        # - ultimate: Ultimate Edition
        self.version_code = version_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.create_timestamp is not None:
            result['CreateTimestamp'] = self.create_timestamp

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.expire_timestamp is not None:
            result['ExpireTimestamp'] = self.expire_timestamp

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.monitor_task_quota is not None:
            result['MonitorTaskQuota'] = self.monitor_task_quota

        if self.monthly_email_used is not None:
            result['MonthlyEmailUsed'] = self.monthly_email_used

        if self.monthly_sms_quota is not None:
            result['MonthlySmsQuota'] = self.monthly_sms_quota

        if self.monthly_sms_used is not None:
            result['MonthlySmsUsed'] = self.monthly_sms_used

        if self.monthly_webhook_used is not None:
            result['MonthlyWebhookUsed'] = self.monthly_webhook_used

        if self.schedule_domain_name is not None:
            result['ScheduleDomainName'] = self.schedule_domain_name

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.update_timestamp is not None:
            result['UpdateTimestamp'] = self.update_timestamp

        if self.version_code is not None:
            result['VersionCode'] = self.version_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CreateTimestamp') is not None:
            self.create_timestamp = m.get('CreateTimestamp')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('ExpireTimestamp') is not None:
            self.expire_timestamp = m.get('ExpireTimestamp')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('MonitorTaskQuota') is not None:
            self.monitor_task_quota = m.get('MonitorTaskQuota')

        if m.get('MonthlyEmailUsed') is not None:
            self.monthly_email_used = m.get('MonthlyEmailUsed')

        if m.get('MonthlySmsQuota') is not None:
            self.monthly_sms_quota = m.get('MonthlySmsQuota')

        if m.get('MonthlySmsUsed') is not None:
            self.monthly_sms_used = m.get('MonthlySmsUsed')

        if m.get('MonthlyWebhookUsed') is not None:
            self.monthly_webhook_used = m.get('MonthlyWebhookUsed')

        if m.get('ScheduleDomainName') is not None:
            self.schedule_domain_name = m.get('ScheduleDomainName')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('UpdateTimestamp') is not None:
            self.update_timestamp = m.get('UpdateTimestamp')

        if m.get('VersionCode') is not None:
            self.version_code = m.get('VersionCode')

        return self

