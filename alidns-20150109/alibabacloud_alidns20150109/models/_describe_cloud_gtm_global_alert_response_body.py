# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alidns20150109 import models as main_models
from darabonba.model import DaraModel

class DescribeCloudGtmGlobalAlertResponseBody(DaraModel):
    def __init__(
        self,
        alert_config: main_models.DescribeCloudGtmGlobalAlertResponseBodyAlertConfig = None,
        alert_group: main_models.DescribeCloudGtmGlobalAlertResponseBodyAlertGroup = None,
        request_id: str = None,
    ):
        # The alert configurations.
        self.alert_config = alert_config
        # The alert contact groups.
        self.alert_group = alert_group
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

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertConfig') is not None:
            temp_model = main_models.DescribeCloudGtmGlobalAlertResponseBodyAlertConfig()
            self.alert_config = temp_model.from_map(m.get('AlertConfig'))

        if m.get('AlertGroup') is not None:
            temp_model = main_models.DescribeCloudGtmGlobalAlertResponseBodyAlertGroup()
            self.alert_group = temp_model.from_map(m.get('AlertGroup'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeCloudGtmGlobalAlertResponseBodyAlertGroup(DaraModel):
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

class DescribeCloudGtmGlobalAlertResponseBodyAlertConfig(DaraModel):
    def __init__(
        self,
        alert_config: List[main_models.DescribeCloudGtmGlobalAlertResponseBodyAlertConfigAlertConfig] = None,
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
                temp_model = main_models.DescribeCloudGtmGlobalAlertResponseBodyAlertConfigAlertConfig()
                self.alert_config.append(temp_model.from_map(k1))

        return self

class DescribeCloudGtmGlobalAlertResponseBodyAlertConfigAlertConfig(DaraModel):
    def __init__(
        self,
        dingtalk_notice: bool = None,
        email_notice: bool = None,
        notice_type: str = None,
        sms_notice: bool = None,
    ):
        # Indicates whether DingTalk notifications are configured. Valid values:
        # 
        # *   true: DingTalk notifications are configured. DingTalk notifications are sent when alerts are triggered.
        # *   false: DingTalk notifications are not configured.
        self.dingtalk_notice = dingtalk_notice
        # Indicates whether email notifications are configured. Valid values:
        # 
        # *   true: Email notifications are configured. Emails are sent when alerts are triggered.
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
        # *   true: Text message notifications are configured. Text messages are sent when alerts are triggered.
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

