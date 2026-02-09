# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Any

from darabonba.model import DaraModel

class PushTemplateShrinkRequest(DaraModel):
    def __init__(
        self,
        activity_content_state: Any = None,
        activity_event: str = None,
        app_id: str = None,
        channel_id: str = None,
        classification: str = None,
        delivery_type: int = None,
        dismissal_date: int = None,
        expired_seconds: int = None,
        extended_params: str = None,
        mi_channel_id: str = None,
        notify_level_shrink: str = None,
        notify_type: str = None,
        push_action: int = None,
        silent: int = None,
        sms_sign_name: str = None,
        sms_strategy: int = None,
        sms_template_code: str = None,
        sms_template_param: str = None,
        strategy_content: str = None,
        strategy_type: int = None,
        target_msgkey: str = None,
        task_name: str = None,
        template_key_value: str = None,
        template_name: str = None,
        tenant_id: str = None,
        third_channel_category_shrink: str = None,
        transparent_message_payload: Any = None,
        transparent_message_urgency: str = None,
        workspace_id: str = None,
    ):
        self.activity_content_state = activity_content_state
        self.activity_event = activity_event
        # This parameter is required.
        self.app_id = app_id
        self.channel_id = channel_id
        self.classification = classification
        # This parameter is required.
        self.delivery_type = delivery_type
        self.dismissal_date = dismissal_date
        # This parameter is required.
        self.expired_seconds = expired_seconds
        self.extended_params = extended_params
        self.mi_channel_id = mi_channel_id
        self.notify_level_shrink = notify_level_shrink
        self.notify_type = notify_type
        self.push_action = push_action
        self.silent = silent
        self.sms_sign_name = sms_sign_name
        self.sms_strategy = sms_strategy
        self.sms_template_code = sms_template_code
        self.sms_template_param = sms_template_param
        self.strategy_content = strategy_content
        self.strategy_type = strategy_type
        # This parameter is required.
        self.target_msgkey = target_msgkey
        self.task_name = task_name
        self.template_key_value = template_key_value
        # This parameter is required.
        self.template_name = template_name
        self.tenant_id = tenant_id
        self.third_channel_category_shrink = third_channel_category_shrink
        self.transparent_message_payload = transparent_message_payload
        self.transparent_message_urgency = transparent_message_urgency
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.activity_content_state is not None:
            result['ActivityContentState'] = self.activity_content_state

        if self.activity_event is not None:
            result['ActivityEvent'] = self.activity_event

        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id

        if self.classification is not None:
            result['Classification'] = self.classification

        if self.delivery_type is not None:
            result['DeliveryType'] = self.delivery_type

        if self.dismissal_date is not None:
            result['DismissalDate'] = self.dismissal_date

        if self.expired_seconds is not None:
            result['ExpiredSeconds'] = self.expired_seconds

        if self.extended_params is not None:
            result['ExtendedParams'] = self.extended_params

        if self.mi_channel_id is not None:
            result['MiChannelId'] = self.mi_channel_id

        if self.notify_level_shrink is not None:
            result['NotifyLevel'] = self.notify_level_shrink

        if self.notify_type is not None:
            result['NotifyType'] = self.notify_type

        if self.push_action is not None:
            result['PushAction'] = self.push_action

        if self.silent is not None:
            result['Silent'] = self.silent

        if self.sms_sign_name is not None:
            result['SmsSignName'] = self.sms_sign_name

        if self.sms_strategy is not None:
            result['SmsStrategy'] = self.sms_strategy

        if self.sms_template_code is not None:
            result['SmsTemplateCode'] = self.sms_template_code

        if self.sms_template_param is not None:
            result['SmsTemplateParam'] = self.sms_template_param

        if self.strategy_content is not None:
            result['StrategyContent'] = self.strategy_content

        if self.strategy_type is not None:
            result['StrategyType'] = self.strategy_type

        if self.target_msgkey is not None:
            result['TargetMsgkey'] = self.target_msgkey

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        if self.template_key_value is not None:
            result['TemplateKeyValue'] = self.template_key_value

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        if self.third_channel_category_shrink is not None:
            result['ThirdChannelCategory'] = self.third_channel_category_shrink

        if self.transparent_message_payload is not None:
            result['TransparentMessagePayload'] = self.transparent_message_payload

        if self.transparent_message_urgency is not None:
            result['TransparentMessageUrgency'] = self.transparent_message_urgency

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActivityContentState') is not None:
            self.activity_content_state = m.get('ActivityContentState')

        if m.get('ActivityEvent') is not None:
            self.activity_event = m.get('ActivityEvent')

        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')

        if m.get('Classification') is not None:
            self.classification = m.get('Classification')

        if m.get('DeliveryType') is not None:
            self.delivery_type = m.get('DeliveryType')

        if m.get('DismissalDate') is not None:
            self.dismissal_date = m.get('DismissalDate')

        if m.get('ExpiredSeconds') is not None:
            self.expired_seconds = m.get('ExpiredSeconds')

        if m.get('ExtendedParams') is not None:
            self.extended_params = m.get('ExtendedParams')

        if m.get('MiChannelId') is not None:
            self.mi_channel_id = m.get('MiChannelId')

        if m.get('NotifyLevel') is not None:
            self.notify_level_shrink = m.get('NotifyLevel')

        if m.get('NotifyType') is not None:
            self.notify_type = m.get('NotifyType')

        if m.get('PushAction') is not None:
            self.push_action = m.get('PushAction')

        if m.get('Silent') is not None:
            self.silent = m.get('Silent')

        if m.get('SmsSignName') is not None:
            self.sms_sign_name = m.get('SmsSignName')

        if m.get('SmsStrategy') is not None:
            self.sms_strategy = m.get('SmsStrategy')

        if m.get('SmsTemplateCode') is not None:
            self.sms_template_code = m.get('SmsTemplateCode')

        if m.get('SmsTemplateParam') is not None:
            self.sms_template_param = m.get('SmsTemplateParam')

        if m.get('StrategyContent') is not None:
            self.strategy_content = m.get('StrategyContent')

        if m.get('StrategyType') is not None:
            self.strategy_type = m.get('StrategyType')

        if m.get('TargetMsgkey') is not None:
            self.target_msgkey = m.get('TargetMsgkey')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        if m.get('TemplateKeyValue') is not None:
            self.template_key_value = m.get('TemplateKeyValue')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        if m.get('ThirdChannelCategory') is not None:
            self.third_channel_category_shrink = m.get('ThirdChannelCategory')

        if m.get('TransparentMessagePayload') is not None:
            self.transparent_message_payload = m.get('TransparentMessagePayload')

        if m.get('TransparentMessageUrgency') is not None:
            self.transparent_message_urgency = m.get('TransparentMessageUrgency')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

