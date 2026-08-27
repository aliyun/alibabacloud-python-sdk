# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreatePersonalFeishuChatShrinkRequest(DaraModel):
    def __init__(
        self,
        chat_id: str = None,
        description: str = None,
        directory_id: str = None,
        history_start_time: str = None,
        notes: str = None,
        operating_object_name: str = None,
        source_tags: str = None,
        tenant_id: str = None,
        update_frequency_shrink: str = None,
    ):
        # The group chat session ID.
        # 
        # This parameter is required.
        self.chat_id = chat_id
        # The description of the source.
        self.description = description
        # The directory ID.
        self.directory_id = directory_id
        # The start time for historical messages. Supports YYYY-MM-DD or YYYY-MM-DD HH:MM:SS. If not specified, all visible history is pulled.
        self.history_start_time = history_start_time
        # The meeting notes content (optional). Used for auxiliary analysis.
        self.notes = notes
        # The digital employee name (operating object name, optional).
        self.operating_object_name = operating_object_name
        # The source tags.
        self.source_tags = source_tags
        # The tenant ID to take effect.
        self.tenant_id = tenant_id
        # The update frequency.
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

        if m.get('sourceTags') is not None:
            self.source_tags = m.get('sourceTags')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        if m.get('updateFrequency') is not None:
            self.update_frequency_shrink = m.get('updateFrequency')

        return self

