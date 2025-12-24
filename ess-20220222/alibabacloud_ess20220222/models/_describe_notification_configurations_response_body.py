# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ess20220222 import models as main_models
from darabonba.model import DaraModel

class DescribeNotificationConfigurationsResponseBody(DaraModel):
    def __init__(
        self,
        notification_configuration_models: List[main_models.DescribeNotificationConfigurationsResponseBodyNotificationConfigurationModels] = None,
        request_id: str = None,
    ):
        # The notification settings.
        self.notification_configuration_models = notification_configuration_models
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.notification_configuration_models:
            for v1 in self.notification_configuration_models:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['NotificationConfigurationModels'] = []
        if self.notification_configuration_models is not None:
            for k1 in self.notification_configuration_models:
                result['NotificationConfigurationModels'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.notification_configuration_models = []
        if m.get('NotificationConfigurationModels') is not None:
            for k1 in m.get('NotificationConfigurationModels'):
                temp_model = main_models.DescribeNotificationConfigurationsResponseBodyNotificationConfigurationModels()
                self.notification_configuration_models.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeNotificationConfigurationsResponseBodyNotificationConfigurationModels(DaraModel):
    def __init__(
        self,
        message_encoding: str = None,
        notification_arn: str = None,
        notification_types: List[str] = None,
        scaling_group_id: str = None,
        time_zone: str = None,
    ):
        self.message_encoding = message_encoding
        # The Alibaba Cloud Resource Name (ARN) of the notification recipient. The value is in one of the following formats:
        # 
        # *   If you specify CloudMonitor as the notification recipient, the value is in the acs:ess:{region-id}:{account-id}:cloudmonitor format.
        # *   If you specify a Simple Message Queue (SMQ, formerly MNS) as the notification recipient, the value is in the acs:mns:{region-id}:{account-id}:queue/{queuename} format.
        # *   If you specify an SMQ topic as the notification recipient, the value is in the acs:mns:{region-id}:{account-id}:topic/{topicname} format.
        # 
        # The variables in the preceding value formats have the following meanings:
        # 
        # *   region-id: the region ID of your scaling group.
        # *   account-id: the ID of your Alibaba Cloud account.
        # *   queuename: the name of the SMQ queue.
        # *   topicname: the name of the SMQ topic.
        self.notification_arn = notification_arn
        # The types of the notifications.
        self.notification_types = notification_types
        # The ID of the scaling group.
        self.scaling_group_id = scaling_group_id
        # The time zone of the notification. The value must be in UTC. For example, a value of UTC+8 indicates that the time is 8 hours ahead of Coordinated Universal Time, and a value of UTC-7 indicates that the time is 7 hours behind Coordinated Universal Time.
        self.time_zone = time_zone

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.message_encoding is not None:
            result['MessageEncoding'] = self.message_encoding

        if self.notification_arn is not None:
            result['NotificationArn'] = self.notification_arn

        if self.notification_types is not None:
            result['NotificationTypes'] = self.notification_types

        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id

        if self.time_zone is not None:
            result['TimeZone'] = self.time_zone

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MessageEncoding') is not None:
            self.message_encoding = m.get('MessageEncoding')

        if m.get('NotificationArn') is not None:
            self.notification_arn = m.get('NotificationArn')

        if m.get('NotificationTypes') is not None:
            self.notification_types = m.get('NotificationTypes')

        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')

        if m.get('TimeZone') is not None:
            self.time_zone = m.get('TimeZone')

        return self

