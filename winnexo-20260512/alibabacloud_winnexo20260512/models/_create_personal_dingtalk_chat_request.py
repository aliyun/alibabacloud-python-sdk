# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_winnexo20260512 import models as main_models
from darabonba.model import DaraModel

class CreatePersonalDingtalkChatRequest(DaraModel):
    def __init__(
        self,
        app_token: str = None,
        chat_id: str = None,
        chat_name: str = None,
        description: str = None,
        directory_id: str = None,
        history_start_time: str = None,
        notes: str = None,
        operating_object_name: str = None,
        ops_user_code: str = None,
        ops_user_id: str = None,
        source_tags: str = None,
        tenant_id: str = None,
        update_frequency: main_models.CreatePersonalDingtalkChatRequestUpdateFrequency = None,
    ):
        # The platform application token issued by the console. If specified, the operation is performed as the user specified by opsUserId or opsUserCode.
        self.app_token = app_token
        # The DingTalk group chat session ID.
        # 
        # This parameter is required.
        self.chat_id = chat_id
        # The name of the group chat.
        self.chat_name = chat_name
        # The pipeline description.
        self.description = description
        # The folder ID.
        self.directory_id = directory_id
        # The start time for chat record collection.
        # 
        # This parameter is required.
        self.history_start_time = history_start_time
        # The content of the meeting notes (optional), which is used for auxiliary analysis.
        self.notes = notes
        # The name of the digital employee (the name of the operating object, optional).
        self.operating_object_name = operating_object_name
        # The proxy user code, which is unique within the tenant. This parameter is used only when the application credential is configured as source_uid.
        self.ops_user_code = ops_user_code
        # The proxy user ID, which is the WINNEXO platform user ID. This parameter is used only when the application credential is configured as winnexo_uid.
        self.ops_user_id = ops_user_id
        # The resource tags (optional). The value is a JSON string list, such as ["tagA","tagB"].
        self.source_tags = source_tags
        # The ID of the tenant.
        self.tenant_id = tenant_id
        # The feature update frequency.
        self.update_frequency = update_frequency

    def validate(self):
        if self.update_frequency:
            self.update_frequency.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_token is not None:
            result['appToken'] = self.app_token

        if self.chat_id is not None:
            result['chatId'] = self.chat_id

        if self.chat_name is not None:
            result['chatName'] = self.chat_name

        if self.description is not None:
            result['description'] = self.description

        if self.directory_id is not None:
            result['directoryId'] = self.directory_id

        if self.history_start_time is not None:
            result['historyStartTime'] = self.history_start_time

        if self.notes is not None:
            result['notes'] = self.notes

        if self.operating_object_name is not None:
            result['operatingObjectName'] = self.operating_object_name

        if self.ops_user_code is not None:
            result['opsUserCode'] = self.ops_user_code

        if self.ops_user_id is not None:
            result['opsUserId'] = self.ops_user_id

        if self.source_tags is not None:
            result['sourceTags'] = self.source_tags

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        if self.update_frequency is not None:
            result['updateFrequency'] = self.update_frequency.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appToken') is not None:
            self.app_token = m.get('appToken')

        if m.get('chatId') is not None:
            self.chat_id = m.get('chatId')

        if m.get('chatName') is not None:
            self.chat_name = m.get('chatName')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('directoryId') is not None:
            self.directory_id = m.get('directoryId')

        if m.get('historyStartTime') is not None:
            self.history_start_time = m.get('historyStartTime')

        if m.get('notes') is not None:
            self.notes = m.get('notes')

        if m.get('operatingObjectName') is not None:
            self.operating_object_name = m.get('operatingObjectName')

        if m.get('opsUserCode') is not None:
            self.ops_user_code = m.get('opsUserCode')

        if m.get('opsUserId') is not None:
            self.ops_user_id = m.get('opsUserId')

        if m.get('sourceTags') is not None:
            self.source_tags = m.get('sourceTags')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        if m.get('updateFrequency') is not None:
            temp_model = main_models.CreatePersonalDingtalkChatRequestUpdateFrequency()
            self.update_frequency = temp_model.from_map(m.get('updateFrequency'))

        return self

class CreatePersonalDingtalkChatRequestUpdateFrequency(DaraModel):
    def __init__(
        self,
        cron: str = None,
        enabled: bool = None,
        preset: str = None,
    ):
        # The cron expression for the timed scheduling task.
        self.cron = cron
        # **Specifies whether to enable the feature.**
        self.enabled = enabled
        # The preset mode, which can be ignored.
        self.preset = preset

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cron is not None:
            result['cron'] = self.cron

        if self.enabled is not None:
            result['enabled'] = self.enabled

        if self.preset is not None:
            result['preset'] = self.preset

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cron') is not None:
            self.cron = m.get('cron')

        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        if m.get('preset') is not None:
            self.preset = m.get('preset')

        return self

