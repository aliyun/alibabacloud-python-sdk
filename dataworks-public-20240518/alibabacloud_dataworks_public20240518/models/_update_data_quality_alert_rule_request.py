# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class UpdateDataQualityAlertRuleRequest(DaraModel):
    def __init__(
        self,
        condition: str = None,
        id: int = None,
        notification: main_models.UpdateDataQualityAlertRuleRequestNotification = None,
        project_id: int = None,
        target: main_models.UpdateDataQualityAlertRuleRequestTarget = None,
    ):
        # The alert condition of the data quality monitoring rule.
        self.condition = condition
        # The ID of the alert rule.
        self.id = id
        # Alert notification configurations.
        self.notification = notification
        # The project ID.
        self.project_id = project_id
        # The monitored target of the data quality monitoring rule.
        self.target = target

    def validate(self):
        if self.notification:
            self.notification.validate()
        if self.target:
            self.target.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.condition is not None:
            result['Condition'] = self.condition

        if self.id is not None:
            result['Id'] = self.id

        if self.notification is not None:
            result['Notification'] = self.notification.to_map()

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.target is not None:
            result['Target'] = self.target.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Condition') is not None:
            self.condition = m.get('Condition')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Notification') is not None:
            temp_model = main_models.UpdateDataQualityAlertRuleRequestNotification()
            self.notification = temp_model.from_map(m.get('Notification'))

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('Target') is not None:
            temp_model = main_models.UpdateDataQualityAlertRuleRequestTarget()
            self.target = temp_model.from_map(m.get('Target'))

        return self

class UpdateDataQualityAlertRuleRequestTarget(DaraModel):
    def __init__(
        self,
        ids: List[int] = None,
        type: str = None,
    ):
        # The list of monitored target IDs. Currently, only one ID can be set.
        self.ids = ids
        # The type of the monitored target. Only DataQualityScan is supported.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ids is not None:
            result['Ids'] = self.ids

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ids') is not None:
            self.ids = m.get('Ids')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class UpdateDataQualityAlertRuleRequestNotification(DaraModel):
    def __init__(
        self,
        channels: List[str] = None,
        receivers: List[main_models.UpdateDataQualityAlertRuleRequestNotificationReceivers] = None,
    ):
        # The list of alert channels. You can set both Email and Sms at the same time. In other cases, only one channel can be set.
        # 
        # This parameter is required.
        self.channels = channels
        # The alert recipients.
        self.receivers = receivers

    def validate(self):
        if self.receivers:
            for v1 in self.receivers:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channels is not None:
            result['Channels'] = self.channels

        result['Receivers'] = []
        if self.receivers is not None:
            for k1 in self.receivers:
                result['Receivers'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Channels') is not None:
            self.channels = m.get('Channels')

        self.receivers = []
        if m.get('Receivers') is not None:
            for k1 in m.get('Receivers'):
                temp_model = main_models.UpdateDataQualityAlertRuleRequestNotificationReceivers()
                self.receivers.append(temp_model.from_map(k1))

        return self

class UpdateDataQualityAlertRuleRequestNotificationReceivers(DaraModel):
    def __init__(
        self,
        extension: str = None,
        receiver_type: str = None,
        receiver_values: List[str] = None,
    ):
        # Additional configurations required for the alert recipients. When ReceiverType is DingdingUrl, you can set `{"atAll":true}` to mention all members.
        self.extension = extension
        # The type of alert recipients.
        # 
        # *   AliUid
        # *   WebhookUrl
        # *   DingdingUrl
        # *   WeixinUrl
        # *   FeishuUrl
        # *   TaskOwner
        # *   DataQualityScanOwner
        # *   ShiftSchedule
        # 
        # This parameter is required.
        self.receiver_type = receiver_type
        # The value of alert recipients.
        self.receiver_values = receiver_values

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.extension is not None:
            result['Extension'] = self.extension

        if self.receiver_type is not None:
            result['ReceiverType'] = self.receiver_type

        if self.receiver_values is not None:
            result['ReceiverValues'] = self.receiver_values

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Extension') is not None:
            self.extension = m.get('Extension')

        if m.get('ReceiverType') is not None:
            self.receiver_type = m.get('ReceiverType')

        if m.get('ReceiverValues') is not None:
            self.receiver_values = m.get('ReceiverValues')

        return self

