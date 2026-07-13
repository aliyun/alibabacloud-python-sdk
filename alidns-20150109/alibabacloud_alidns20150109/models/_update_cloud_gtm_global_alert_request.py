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
        # - `zh-CN`: Chinese
        # 
        # - `en-US`: English
        self.accept_language = accept_language
        # A list of alert configurations.
        self.alert_config = alert_config
        # A list of alert notification groups.
        self.alert_group = alert_group
        # A client-generated token to ensure request idempotence. This token must be unique for each request, contain only ASCII characters, and be no more than 64 characters in length.
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
        qps_threshold: int = None,
        sms_notice: bool = None,
        threshold: int = None,
    ):
        # Whether to send a DingTalk notification when an alert is triggered. Valid values:
        # 
        # - `true`: A DingTalk notification is sent.
        # 
        # - `false`: Do not send a DingTalk notification.
        self.dingtalk_notice = dingtalk_notice
        # Whether to send an email notification when an alert is triggered. Valid values:
        # 
        # - `true`: An email notification is sent.
        # 
        # - `false` or `null`: Do not send an email notification.
        self.email_notice = email_notice
        # The alert event type. Valid values:
        # 
        # - `addr_alert`: An address becomes unavailable.
        # 
        # - `addr_resume`: An address becomes available.
        # 
        # - `addr_pool_unavailable`: An address pool becomes unavailable.
        # 
        # - `addr_pool_available`: An address pool becomes available.
        self.notice_type = notice_type
        # The alert threshold for queries per second (QPS).
        self.qps_threshold = qps_threshold
        # Whether to send a text message notification when an alert is triggered. Valid values:
        # 
        # - `true`: A text message notification is sent.
        # 
        # - `false` or `null`: Do not send a text message notification.
        # 
        # Text message notifications are available only on the China site.
        self.sms_notice = sms_notice
        # The alert threshold.
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

        if self.qps_threshold is not None:
            result['QpsThreshold'] = self.qps_threshold

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

        if m.get('QpsThreshold') is not None:
            self.qps_threshold = m.get('QpsThreshold')

        if m.get('SmsNotice') is not None:
            self.sms_notice = m.get('SmsNotice')

        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')

        return self

