# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alidns20150109 import models as main_models
from darabonba.model import DaraModel

class DescribeDnsGtmInstancesResponseBody(DaraModel):
    def __init__(
        self,
        gtm_instances: List[main_models.DescribeDnsGtmInstancesResponseBodyGtmInstances] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_items: int = None,
        total_pages: int = None,
    ):
        # The Global Traffic Manager (GTM) instances.
        self.gtm_instances = gtm_instances
        # The page number. Pages start from page **1**. Default value: **1**.
        self.page_number = page_number
        # The number of entries per page. Maximum value: 100. Default value: 20.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_items = total_items
        # The total number of pages returned.
        self.total_pages = total_pages

    def validate(self):
        if self.gtm_instances:
            for v1 in self.gtm_instances:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['GtmInstances'] = []
        if self.gtm_instances is not None:
            for k1 in self.gtm_instances:
                result['GtmInstances'].append(k1.to_map() if k1 else None)

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
        self.gtm_instances = []
        if m.get('GtmInstances') is not None:
            for k1 in m.get('GtmInstances'):
                temp_model = main_models.DescribeDnsGtmInstancesResponseBodyGtmInstances()
                self.gtm_instances.append(temp_model.from_map(k1))

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

class DescribeDnsGtmInstancesResponseBodyGtmInstances(DaraModel):
    def __init__(
        self,
        config: main_models.DescribeDnsGtmInstancesResponseBodyGtmInstancesConfig = None,
        create_time: str = None,
        create_timestamp: int = None,
        expire_time: str = None,
        expire_timestamp: int = None,
        instance_id: str = None,
        payment_type: str = None,
        resource_group_id: str = None,
        sms_quota: int = None,
        task_quota: int = None,
        used_quota: main_models.DescribeDnsGtmInstancesResponseBodyGtmInstancesUsedQuota = None,
        version_code: str = None,
    ):
        # The configurations of the instance.
        self.config = config
        # The time when the instance was created. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.create_time = create_time
        # The time when the instance was created. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.create_timestamp = create_timestamp
        # The time when the instance expires. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.expire_time = expire_time
        # The time when the instance expires. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.expire_timestamp = expire_timestamp
        # The instance ID.
        self.instance_id = instance_id
        # The billing method of the GTM instance. Valid value:
        # 
        # *   Subscription.
        self.payment_type = payment_type
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The total number of Short Message Service (SMS) notifications.
        self.sms_quota = sms_quota
        # The total number of detection tasks.
        self.task_quota = task_quota
        # The used quota.
        self.used_quota = used_quota
        # The version of the instance.
        self.version_code = version_code

    def validate(self):
        if self.config:
            self.config.validate()
        if self.used_quota:
            self.used_quota.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config is not None:
            result['Config'] = self.config.to_map()

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

        if self.payment_type is not None:
            result['PaymentType'] = self.payment_type

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.sms_quota is not None:
            result['SmsQuota'] = self.sms_quota

        if self.task_quota is not None:
            result['TaskQuota'] = self.task_quota

        if self.used_quota is not None:
            result['UsedQuota'] = self.used_quota.to_map()

        if self.version_code is not None:
            result['VersionCode'] = self.version_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            temp_model = main_models.DescribeDnsGtmInstancesResponseBodyGtmInstancesConfig()
            self.config = temp_model.from_map(m.get('Config'))

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

        if m.get('PaymentType') is not None:
            self.payment_type = m.get('PaymentType')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SmsQuota') is not None:
            self.sms_quota = m.get('SmsQuota')

        if m.get('TaskQuota') is not None:
            self.task_quota = m.get('TaskQuota')

        if m.get('UsedQuota') is not None:
            temp_model = main_models.DescribeDnsGtmInstancesResponseBodyGtmInstancesUsedQuota()
            self.used_quota = temp_model.from_map(m.get('UsedQuota'))

        if m.get('VersionCode') is not None:
            self.version_code = m.get('VersionCode')

        return self

class DescribeDnsGtmInstancesResponseBodyGtmInstancesUsedQuota(DaraModel):
    def __init__(
        self,
        dingtalk_used_count: int = None,
        email_used_count: int = None,
        sms_used_count: int = None,
        task_used_count: int = None,
    ):
        # The total number of sent DingTalk notifications.
        self.dingtalk_used_count = dingtalk_used_count
        # The total number of sent email notifications.
        self.email_used_count = email_used_count
        # The total number of sent SMS notifications.
        self.sms_used_count = sms_used_count
        # The number of created detection tasks.
        self.task_used_count = task_used_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dingtalk_used_count is not None:
            result['DingtalkUsedCount'] = self.dingtalk_used_count

        if self.email_used_count is not None:
            result['EmailUsedCount'] = self.email_used_count

        if self.sms_used_count is not None:
            result['SmsUsedCount'] = self.sms_used_count

        if self.task_used_count is not None:
            result['TaskUsedCount'] = self.task_used_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DingtalkUsedCount') is not None:
            self.dingtalk_used_count = m.get('DingtalkUsedCount')

        if m.get('EmailUsedCount') is not None:
            self.email_used_count = m.get('EmailUsedCount')

        if m.get('SmsUsedCount') is not None:
            self.sms_used_count = m.get('SmsUsedCount')

        if m.get('TaskUsedCount') is not None:
            self.task_used_count = m.get('TaskUsedCount')

        return self

class DescribeDnsGtmInstancesResponseBodyGtmInstancesConfig(DaraModel):
    def __init__(
        self,
        alert_config: List[main_models.DescribeDnsGtmInstancesResponseBodyGtmInstancesConfigAlertConfig] = None,
        alert_group: str = None,
        cname_type: str = None,
        instance_name: str = None,
        public_cname_mode: str = None,
        public_rr: str = None,
        public_user_domain_name: str = None,
        public_zone_name: str = None,
        strategy_mode: str = None,
        ttl: int = None,
    ):
        # The alert notification method.
        self.alert_config = alert_config
        # The alert contact groups. The value is in the JSON format.
        self.alert_group = alert_group
        # The type of the CNAME. Valid value:
        # 
        # *   PUBLIC
        self.cname_type = cname_type
        # The name of the instance.
        self.instance_name = instance_name
        # Specifies whether to use a custom CNAME or a system-assigned CNAME to access GTM over the Internet. Valid values:
        # 
        # *   CUSTOM: a custom CNAME
        # *   SYSTEM_ASSIGN: a system-assigned CNAME. You cannot set PublicCnameMode to this value.
        self.public_cname_mode = public_cname_mode
        # The hostname of the domain name that is used to access GTM over the Internet.
        self.public_rr = public_rr
        # The domain name that is used to access GTM over the Internet.
        self.public_user_domain_name = public_user_domain_name
        # The canonical name (CNAME) that is used to access GTM over the Internet.
        self.public_zone_name = public_zone_name
        # The type of the access policy. Valid values:
        # 
        # *   LATENCY: latency-based access policy
        # *   GEO: geographical location-based access policy
        self.strategy_mode = strategy_mode
        # The global time to live (TTL).
        self.ttl = ttl

    def validate(self):
        if self.alert_config:
            for v1 in self.alert_config:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AlertConfig'] = []
        if self.alert_config is not None:
            for k1 in self.alert_config:
                result['AlertConfig'].append(k1.to_map() if k1 else None)

        if self.alert_group is not None:
            result['AlertGroup'] = self.alert_group

        if self.cname_type is not None:
            result['CnameType'] = self.cname_type

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.public_cname_mode is not None:
            result['PublicCnameMode'] = self.public_cname_mode

        if self.public_rr is not None:
            result['PublicRr'] = self.public_rr

        if self.public_user_domain_name is not None:
            result['PublicUserDomainName'] = self.public_user_domain_name

        if self.public_zone_name is not None:
            result['PublicZoneName'] = self.public_zone_name

        if self.strategy_mode is not None:
            result['StrategyMode'] = self.strategy_mode

        if self.ttl is not None:
            result['Ttl'] = self.ttl

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.alert_config = []
        if m.get('AlertConfig') is not None:
            for k1 in m.get('AlertConfig'):
                temp_model = main_models.DescribeDnsGtmInstancesResponseBodyGtmInstancesConfigAlertConfig()
                self.alert_config.append(temp_model.from_map(k1))

        if m.get('AlertGroup') is not None:
            self.alert_group = m.get('AlertGroup')

        if m.get('CnameType') is not None:
            self.cname_type = m.get('CnameType')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('PublicCnameMode') is not None:
            self.public_cname_mode = m.get('PublicCnameMode')

        if m.get('PublicRr') is not None:
            self.public_rr = m.get('PublicRr')

        if m.get('PublicUserDomainName') is not None:
            self.public_user_domain_name = m.get('PublicUserDomainName')

        if m.get('PublicZoneName') is not None:
            self.public_zone_name = m.get('PublicZoneName')

        if m.get('StrategyMode') is not None:
            self.strategy_mode = m.get('StrategyMode')

        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')

        return self

class DescribeDnsGtmInstancesResponseBodyGtmInstancesConfigAlertConfig(DaraModel):
    def __init__(
        self,
        dingtalk_notice: str = None,
        email_notice: str = None,
        notice_type: str = None,
        sms_notice: str = None,
    ):
        # Indicates whether DingTalk alert notifications are configured. Valid values:
        # 
        # *   true
        # *   false | null
        self.dingtalk_notice = dingtalk_notice
        # Indicates whether email notifications are configured. Valid values:
        # 
        # *   true
        # *   false | null
        self.email_notice = email_notice
        # The type of the alert event. Valid values:
        # 
        # *   ADDR_ALERT: The address is unavailable.
        # *   ADDR_RESUME: The address becomes available.
        # *   ADDR_POOL_GROUP_UNAVAILABLE: The address pool set is unavailable.
        # *   ADDR_POOL_GROUP_AVAILABLE: The address pool set becomes available.
        # *   ACCESS_STRATEGY_POOL_GROUP_SWITCH: Switchover is triggered between the primary and secondary address pools.
        self.notice_type = notice_type
        # Indicates whether SMS notifications are configured. Valid values:
        # 
        # *   true
        # *   false | null
        self.sms_notice = sms_notice

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dingtalk_notice is not None:
            result['DingtalkNotice'] = self.dingtalk_notice

        if self.email_notice is not None:
            result['EmailNotice'] = self.email_notice

        if self.notice_type is not None:
            result['NoticeType'] = self.notice_type

        if self.sms_notice is not None:
            result['SmsNotice'] = self.sms_notice

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DingtalkNotice') is not None:
            self.dingtalk_notice = m.get('DingtalkNotice')

        if m.get('EmailNotice') is not None:
            self.email_notice = m.get('EmailNotice')

        if m.get('NoticeType') is not None:
            self.notice_type = m.get('NoticeType')

        if m.get('SmsNotice') is not None:
            self.sms_notice = m.get('SmsNotice')

        return self

