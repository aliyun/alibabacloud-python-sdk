# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class PushBroadcastRequest(DaraModel):
    def __init__(
        self,
        android_channel: int = None,
        app_id: str = None,
        bind_end_time: int = None,
        bind_period: int = None,
        bind_start_time: int = None,
        channel_id: str = None,
        classification: str = None,
        delivery_type: int = None,
        expired_seconds: int = None,
        extended_params: str = None,
        mi_channel_id: str = None,
        msgkey: str = None,
        notify_level: Dict[str, Any] = None,
        notify_type: str = None,
        push_action: int = None,
        push_status: int = None,
        silent: int = None,
        strategy_content: str = None,
        strategy_type: int = None,
        task_name: str = None,
        template_key_value: str = None,
        template_name: str = None,
        tenant_id: str = None,
        third_channel_category: Dict[str, Any] = None,
        time_mode: int = None,
        transparent_message_payload: Any = None,
        transparent_message_urgency: str = None,
        un_bind_end_time: int = None,
        un_bind_period: int = None,
        un_bind_start_time: int = None,
        workspace_id: str = None,
    ):
        self.android_channel = android_channel
        # This parameter is required.
        self.app_id = app_id
        self.bind_end_time = bind_end_time
        self.bind_period = bind_period
        self.bind_start_time = bind_start_time
        self.channel_id = channel_id
        self.classification = classification
        # This parameter is required.
        self.delivery_type = delivery_type
        # This parameter is required.
        self.expired_seconds = expired_seconds
        self.extended_params = extended_params
        self.mi_channel_id = mi_channel_id
        # This parameter is required.
        self.msgkey = msgkey
        self.notify_level = notify_level
        self.notify_type = notify_type
        self.push_action = push_action
        self.push_status = push_status
        self.silent = silent
        self.strategy_content = strategy_content
        self.strategy_type = strategy_type
        self.task_name = task_name
        self.template_key_value = template_key_value
        # This parameter is required.
        self.template_name = template_name
        self.tenant_id = tenant_id
        self.third_channel_category = third_channel_category
        self.time_mode = time_mode
        self.transparent_message_payload = transparent_message_payload
        self.transparent_message_urgency = transparent_message_urgency
        self.un_bind_end_time = un_bind_end_time
        self.un_bind_period = un_bind_period
        self.un_bind_start_time = un_bind_start_time
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.android_channel is not None:
            result['AndroidChannel'] = self.android_channel

        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.bind_end_time is not None:
            result['BindEndTime'] = self.bind_end_time

        if self.bind_period is not None:
            result['BindPeriod'] = self.bind_period

        if self.bind_start_time is not None:
            result['BindStartTime'] = self.bind_start_time

        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id

        if self.classification is not None:
            result['Classification'] = self.classification

        if self.delivery_type is not None:
            result['DeliveryType'] = self.delivery_type

        if self.expired_seconds is not None:
            result['ExpiredSeconds'] = self.expired_seconds

        if self.extended_params is not None:
            result['ExtendedParams'] = self.extended_params

        if self.mi_channel_id is not None:
            result['MiChannelId'] = self.mi_channel_id

        if self.msgkey is not None:
            result['Msgkey'] = self.msgkey

        if self.notify_level is not None:
            result['NotifyLevel'] = self.notify_level

        if self.notify_type is not None:
            result['NotifyType'] = self.notify_type

        if self.push_action is not None:
            result['PushAction'] = self.push_action

        if self.push_status is not None:
            result['PushStatus'] = self.push_status

        if self.silent is not None:
            result['Silent'] = self.silent

        if self.strategy_content is not None:
            result['StrategyContent'] = self.strategy_content

        if self.strategy_type is not None:
            result['StrategyType'] = self.strategy_type

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        if self.template_key_value is not None:
            result['TemplateKeyValue'] = self.template_key_value

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        if self.third_channel_category is not None:
            result['ThirdChannelCategory'] = self.third_channel_category

        if self.time_mode is not None:
            result['TimeMode'] = self.time_mode

        if self.transparent_message_payload is not None:
            result['TransparentMessagePayload'] = self.transparent_message_payload

        if self.transparent_message_urgency is not None:
            result['TransparentMessageUrgency'] = self.transparent_message_urgency

        if self.un_bind_end_time is not None:
            result['UnBindEndTime'] = self.un_bind_end_time

        if self.un_bind_period is not None:
            result['UnBindPeriod'] = self.un_bind_period

        if self.un_bind_start_time is not None:
            result['UnBindStartTime'] = self.un_bind_start_time

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AndroidChannel') is not None:
            self.android_channel = m.get('AndroidChannel')

        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('BindEndTime') is not None:
            self.bind_end_time = m.get('BindEndTime')

        if m.get('BindPeriod') is not None:
            self.bind_period = m.get('BindPeriod')

        if m.get('BindStartTime') is not None:
            self.bind_start_time = m.get('BindStartTime')

        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')

        if m.get('Classification') is not None:
            self.classification = m.get('Classification')

        if m.get('DeliveryType') is not None:
            self.delivery_type = m.get('DeliveryType')

        if m.get('ExpiredSeconds') is not None:
            self.expired_seconds = m.get('ExpiredSeconds')

        if m.get('ExtendedParams') is not None:
            self.extended_params = m.get('ExtendedParams')

        if m.get('MiChannelId') is not None:
            self.mi_channel_id = m.get('MiChannelId')

        if m.get('Msgkey') is not None:
            self.msgkey = m.get('Msgkey')

        if m.get('NotifyLevel') is not None:
            self.notify_level = m.get('NotifyLevel')

        if m.get('NotifyType') is not None:
            self.notify_type = m.get('NotifyType')

        if m.get('PushAction') is not None:
            self.push_action = m.get('PushAction')

        if m.get('PushStatus') is not None:
            self.push_status = m.get('PushStatus')

        if m.get('Silent') is not None:
            self.silent = m.get('Silent')

        if m.get('StrategyContent') is not None:
            self.strategy_content = m.get('StrategyContent')

        if m.get('StrategyType') is not None:
            self.strategy_type = m.get('StrategyType')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        if m.get('TemplateKeyValue') is not None:
            self.template_key_value = m.get('TemplateKeyValue')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        if m.get('ThirdChannelCategory') is not None:
            self.third_channel_category = m.get('ThirdChannelCategory')

        if m.get('TimeMode') is not None:
            self.time_mode = m.get('TimeMode')

        if m.get('TransparentMessagePayload') is not None:
            self.transparent_message_payload = m.get('TransparentMessagePayload')

        if m.get('TransparentMessageUrgency') is not None:
            self.transparent_message_urgency = m.get('TransparentMessageUrgency')

        if m.get('UnBindEndTime') is not None:
            self.un_bind_end_time = m.get('UnBindEndTime')

        if m.get('UnBindPeriod') is not None:
            self.un_bind_period = m.get('UnBindPeriod')

        if m.get('UnBindStartTime') is not None:
            self.un_bind_start_time = m.get('UnBindStartTime')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

