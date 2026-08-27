# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateGroupDingtalkChatShrinkRequest(DaraModel):
    def __init__(
        self,
        chat_id: str = None,
        chat_name: str = None,
        description: str = None,
        directory_id: str = None,
        group_id: str = None,
        history_start_time: str = None,
        notes: str = None,
        operating_object_name: str = None,
        source_tags: str = None,
        tenant_id: str = None,
        update_frequency_shrink: str = None,
    ):
        # The conversation ID, typically used for JSSDK.
        # 
        # This parameter is required.
        self.chat_id = chat_id
        # The chat name.
        self.chat_name = chat_name
        # The description of the AI assistant.
        self.description = description
        # The directory ID.
        self.directory_id = directory_id
        # The project group ID.
        # 
        # This parameter is required.
        self.group_id = group_id
        # The start time for collecting chat history.
        # 
        # This parameter is required.
        self.history_start_time = history_start_time
        # The meeting notes content (optional). This participates in auxiliary analysis.
        self.notes = notes
        # The name of the digital employee (operating object name, optional).
        self.operating_object_name = operating_object_name
        # The source tags.
        self.source_tags = source_tags
        # The tenant ID. This is a common parameter. In winnexo-cli, pass this value explicitly by using --tenant-id.
        self.tenant_id = tenant_id
        # The feature update frequency.
        self.update_frequency_shrink = update_frequency_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.chat_id is not None:
            result['chatId'] = self.chat_id

        if self.chat_name is not None:
            result['chatName'] = self.chat_name

        if self.description is not None:
            result['description'] = self.description

        if self.directory_id is not None:
            result['directoryId'] = self.directory_id

        if self.group_id is not None:
            result['groupId'] = self.group_id

        if self.history_start_time is not None:
            result['historyStartTime'] = self.history_start_time

        if self.notes is not None:
            result['notes'] = self.notes

        if self.operating_object_name is not None:
            result['operatingObjectName'] = self.operating_object_name

        if self.source_tags is not None:
            result['sourceTags'] = self.source_tags

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        if self.update_frequency_shrink is not None:
            result['updateFrequency'] = self.update_frequency_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('chatId') is not None:
            self.chat_id = m.get('chatId')

        if m.get('chatName') is not None:
            self.chat_name = m.get('chatName')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('directoryId') is not None:
            self.directory_id = m.get('directoryId')

        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')

        if m.get('historyStartTime') is not None:
            self.history_start_time = m.get('historyStartTime')

        if m.get('notes') is not None:
            self.notes = m.get('notes')

        if m.get('operatingObjectName') is not None:
            self.operating_object_name = m.get('operatingObjectName')

        if m.get('sourceTags') is not None:
            self.source_tags = m.get('sourceTags')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        if m.get('updateFrequency') is not None:
            self.update_frequency_shrink = m.get('updateFrequency')

        return self

