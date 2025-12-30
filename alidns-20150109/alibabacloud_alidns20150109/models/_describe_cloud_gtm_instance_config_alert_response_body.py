# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alidns20150109 import models as main_models
from darabonba.model import DaraModel

class DescribeCloudGtmInstanceConfigAlertResponseBody(DaraModel):
    def __init__(
        self,
        alert_config: main_models.DescribeCloudGtmInstanceConfigAlertResponseBodyAlertConfig = None,
        alert_group: main_models.DescribeCloudGtmInstanceConfigAlertResponseBodyAlertGroup = None,
        alert_mode: str = None,
        config_id: str = None,
        instance_id: str = None,
        request_id: str = None,
    ):
        # The alert configurations.
        self.alert_config = alert_config
        # The alert contact groups.
        self.alert_group = alert_group
        # The alert configuration mode of the instance. Valid values:
        # 
        # *   global: global alert configuration
        # *   instance_config: custom alert configuration
        self.alert_mode = alert_mode
        # The configuration ID of the access domain name. Two configuration IDs exist when the access domain name is bound to the same GTM instance but an A record and an AAAA record are configured for the access domain name. The configuration ID uniquely identifies a configuration.
        self.config_id = config_id
        # The ID of the GTM 3.0 instance.
        self.instance_id = instance_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.alert_config:
            self.alert_config.validate()
        if self.alert_group:
            self.alert_group.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_config is not None:
            result['AlertConfig'] = self.alert_config.to_map()

        if self.alert_group is not None:
            result['AlertGroup'] = self.alert_group.to_map()

        if self.alert_mode is not None:
            result['AlertMode'] = self.alert_mode

        if self.config_id is not None:
            result['ConfigId'] = self.config_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertConfig') is not None:
            temp_model = main_models.DescribeCloudGtmInstanceConfigAlertResponseBodyAlertConfig()
            self.alert_config = temp_model.from_map(m.get('AlertConfig'))

        if m.get('AlertGroup') is not None:
            temp_model = main_models.DescribeCloudGtmInstanceConfigAlertResponseBodyAlertGroup()
            self.alert_group = temp_model.from_map(m.get('AlertGroup'))

        if m.get('AlertMode') is not None:
            self.alert_mode = m.get('AlertMode')

        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeCloudGtmInstanceConfigAlertResponseBodyAlertGroup(DaraModel):
    def __init__(
        self,
        alert_group: List[str] = None,
    ):
        self.alert_group = alert_group

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_group is not None:
            result['AlertGroup'] = self.alert_group

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertGroup') is not None:
            self.alert_group = m.get('AlertGroup')

        return self

class DescribeCloudGtmInstanceConfigAlertResponseBodyAlertConfig(DaraModel):
    def __init__(
        self,
        alert_config: List[main_models.DescribeCloudGtmInstanceConfigAlertResponseBodyAlertConfigAlertConfig] = None,
    ):
        self.alert_config = alert_config

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.alert_config = []
        if m.get('AlertConfig') is not None:
            for k1 in m.get('AlertConfig'):
                temp_model = main_models.DescribeCloudGtmInstanceConfigAlertResponseBodyAlertConfigAlertConfig()
                self.alert_config.append(temp_model.from_map(k1))

        return self

class DescribeCloudGtmInstanceConfigAlertResponseBodyAlertConfigAlertConfig(DaraModel):
    def __init__(
        self,
        dingtalk_notice: bool = None,
        email_notice: bool = None,
        notice_type: str = None,
        sms_notice: bool = None,
    ):
        # Indicates whether DingTalk notifications are configured. Valid values:
        # 
        # *   true: DingTalk notifications are configured. DingTalk notifications are sent after alerts are triggered.
        # *   false: DingTalk notifications are not configured.
        self.dingtalk_notice = dingtalk_notice
        # Indicates whether email notifications are configured. Valid values:
        # 
        # *   true: Email notifications are configured. Emails are sent after alerts are triggered.
        # *   false: Email notifications are not configured.
        self.email_notice = email_notice
        # The type of the alert event. Valid values:
        # 
        # *   addr_alert: The address is unavailable.
        # *   addr_resume: The address becomes available.
        # *   addr_pool_unavailable: The address pool is unavailable.
        # *   addr_pool_available: The address pool becomes available.
        self.notice_type = notice_type
        # Indicates whether text message notifications are configured. Valid values:
        # 
        # *   true: Text message notifications are configured. Text messages are sent after alerts are triggered.
        # *   false: Text message notifications are not configured.
        # 
        # Only the China site (aliyun.com) supports text message notifications.
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

