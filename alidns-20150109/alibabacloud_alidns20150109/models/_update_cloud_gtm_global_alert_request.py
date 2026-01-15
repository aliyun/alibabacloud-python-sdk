# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alidns20150109 import models as main_models
from darabonba.model import DaraModel

class UpdateCloudGtmGlobalAlertRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        alert_config: List[main_models.UpdateCloudGtmGlobalAlertRequestAlertConfig] = None,
        alert_group: List[str] = None,
        client_token: str = None,
    ):
        # The language of the response. Valid values:
        # 
        # *   zh-CN: Chinese
        # *   en-US: English
        self.accept_language = accept_language
        # The alert configurations.
        self.alert_config = alert_config
        # The alert contact groups.
        self.alert_group = alert_group
        # The client token that is used to ensure the idempotence of the request. You can specify a custom value for this parameter, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token

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
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language

        result['AlertConfig'] = []
        if self.alert_config is not None:
            for k1 in self.alert_config:
                result['AlertConfig'].append(k1.to_map() if k1 else None)

        if self.alert_group is not None:
            result['AlertGroup'] = self.alert_group

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        self.alert_config = []
        if m.get('AlertConfig') is not None:
            for k1 in m.get('AlertConfig'):
                temp_model = main_models.UpdateCloudGtmGlobalAlertRequestAlertConfig()
                self.alert_config.append(temp_model.from_map(k1))

        if m.get('AlertGroup') is not None:
            self.alert_group = m.get('AlertGroup')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        return self

class UpdateCloudGtmGlobalAlertRequestAlertConfig(DaraModel):
    def __init__(
        self,
        dingtalk_notice: bool = None,
        email_notice: bool = None,
        notice_type: str = None,
        sms_notice: bool = None,
        threshold: int = None,
    ):
        # Specifies whether to configure DingTalk notifications. Valid values:
        # 
        # *   true: configures DingTalk notifications. DingTalk notifications are sent when alerts are triggered.
        # *   false: does not configure DingTalk notifications.
        self.dingtalk_notice = dingtalk_notice
        # Specifies whether to configure email notifications. Valid values:
        # 
        # *   true: configures email notifications. Emails are sent when alerts are triggered.
        # *   false｜null: does not configure email notifications.
        self.email_notice = email_notice
        # The type of the alert event. Valid values:
        # 
        # *   addr_alert: The address is unavailable.
        # *   addr_resume: The address becomes available.
        # *   addr_pool_unavailable: The address pool is unavailable.
        # *   addr_pool_available: The address pool becomes available.
        self.notice_type = notice_type
        # Specifies whether to configure text message notifications. Valid values:
        # 
        # *   true: configures text message notifications. Text messages are sent when alerts are triggered.
        # *   false｜null: does not configure text message notifications.
        # 
        # Only the China site (aliyun.com) supports text message notifications.
        self.sms_notice = sms_notice
        self.threshold = threshold

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

        if self.threshold is not None:
            result['Threshold'] = self.threshold

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

        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')

        return self

