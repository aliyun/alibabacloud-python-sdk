# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_winnexo20260512 import models as main_models
from darabonba.model import DaraModel

class GetScheduledTaskPushOptionsResponseBody(DaraModel):
    def __init__(
        self,
        channels: List[main_models.GetScheduledTaskPushOptionsResponseBodyChannels] = None,
        code: str = None,
        empty_hint: str = None,
        message: str = None,
        request_id: str = None,
    ):
        # The list of notification channels.
        self.channels = channels
        # The status code.
        self.code = code
        # The prompt displayed when no third-party accounts are bound.
        self.empty_hint = empty_hint
        # The prompt message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.channels:
            for v1 in self.channels:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['channels'] = []
        if self.channels is not None:
            for k1 in self.channels:
                result['channels'].append(k1.to_map() if k1 else None)

        if self.code is not None:
            result['code'] = self.code

        if self.empty_hint is not None:
            result['emptyHint'] = self.empty_hint

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.channels = []
        if m.get('channels') is not None:
            for k1 in m.get('channels'):
                temp_model = main_models.GetScheduledTaskPushOptionsResponseBodyChannels()
                self.channels.append(temp_model.from_map(k1))

        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('emptyHint') is not None:
            self.empty_hint = m.get('emptyHint')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class GetScheduledTaskPushOptionsResponseBodyChannels(DaraModel):
    def __init__(
        self,
        channel_name: str = None,
        channel_type: str = None,
        im_groups: List[main_models.GetScheduledTaskPushOptionsResponseBodyChannelsImGroups] = None,
        methods: List[main_models.GetScheduledTaskPushOptionsResponseBodyChannelsMethods] = None,
    ):
        # The channel name.
        # 
        # This parameter is required.
        self.channel_name = channel_name
        # The notification method. Valid values:
        # 
        # - **hdm_alarm_sms**: SMS.
        # - **dingtalk**: DingTalk chatbot.
        # - **hdm_alarm_sms_and_email**: SMS and email.
        # - **hdm_alarm_sms,dingtalk**: SMS and DingTalk chatbot.
        # 
        # This parameter is required.
        self.channel_type = channel_type
        # The optional IM groups bound to this channel for the collaboration group. This value is empty when querying personal tasks.
        self.im_groups = im_groups
        # The supported methods: HEAD, GET, POST, PUT, DELETE, PATCH, OPTIONS.
        self.methods = methods

    def validate(self):
        if self.im_groups:
            for v1 in self.im_groups:
                 if v1:
                    v1.validate()
        if self.methods:
            for v1 in self.methods:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channel_name is not None:
            result['channelName'] = self.channel_name

        if self.channel_type is not None:
            result['channelType'] = self.channel_type

        result['imGroups'] = []
        if self.im_groups is not None:
            for k1 in self.im_groups:
                result['imGroups'].append(k1.to_map() if k1 else None)

        result['methods'] = []
        if self.methods is not None:
            for k1 in self.methods:
                result['methods'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('channelName') is not None:
            self.channel_name = m.get('channelName')

        if m.get('channelType') is not None:
            self.channel_type = m.get('channelType')

        self.im_groups = []
        if m.get('imGroups') is not None:
            for k1 in m.get('imGroups'):
                temp_model = main_models.GetScheduledTaskPushOptionsResponseBodyChannelsImGroups()
                self.im_groups.append(temp_model.from_map(k1))

        self.methods = []
        if m.get('methods') is not None:
            for k1 in m.get('methods'):
                temp_model = main_models.GetScheduledTaskPushOptionsResponseBodyChannelsMethods()
                self.methods.append(temp_model.from_map(k1))

        return self

class GetScheduledTaskPushOptionsResponseBodyChannelsMethods(DaraModel):
    def __init__(
        self,
        disabled_reason: str = None,
        enabled: bool = None,
        method: str = None,
        name: str = None,
    ):
        # The reason why the option is grayed out.
        self.disabled_reason = disabled_reason
        # The feature switch. This parameter is optional when type is set to web_search.
        # 
        # This parameter is required.
        self.enabled = enabled
        # The method.
        # 
        # This parameter is required.
        self.method = method
        # The name.
        # 
        # This parameter is required.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.disabled_reason is not None:
            result['disabledReason'] = self.disabled_reason

        if self.enabled is not None:
            result['enabled'] = self.enabled

        if self.method is not None:
            result['method'] = self.method

        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('disabledReason') is not None:
            self.disabled_reason = m.get('disabledReason')

        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        if m.get('method') is not None:
            self.method = m.get('method')

        if m.get('name') is not None:
            self.name = m.get('name')

        return self

class GetScheduledTaskPushOptionsResponseBodyChannelsImGroups(DaraModel):
    def __init__(
        self,
        im_group_id: str = None,
        im_group_name: str = None,
        mapping_id: int = None,
    ):
        # The external IM group ID.
        # 
        # This parameter is required.
        self.im_group_id = im_group_id
        # The external IM group name.
        self.im_group_name = im_group_name
        # The binding record ID of the IM group.
        # 
        # This parameter is required.
        self.mapping_id = mapping_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.im_group_id is not None:
            result['imGroupId'] = self.im_group_id

        if self.im_group_name is not None:
            result['imGroupName'] = self.im_group_name

        if self.mapping_id is not None:
            result['mappingId'] = self.mapping_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('imGroupId') is not None:
            self.im_group_id = m.get('imGroupId')

        if m.get('imGroupName') is not None:
            self.im_group_name = m.get('imGroupName')

        if m.get('mappingId') is not None:
            self.mapping_id = m.get('mappingId')

        return self

