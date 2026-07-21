# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ConversationDTO(DaraModel):
    def __init__(
        self,
        chat_data: str = None,
        delete_tag: int = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        message_count: int = None,
        model_ids: str = None,
        title: str = None,
    ):
        # A JSON-formatted string that represents the complete state of the conversation.
        self.chat_data = chat_data
        # The status of the conversation, where 0 means enabled and any non-zero value means disabled.
        self.delete_tag = delete_tag
        # The creation time of the conversation, in ISO 8601 format.
        self.gmt_create = gmt_create
        # The modification time of the conversation, in ISO 8601 format.
        self.gmt_modified = gmt_modified
        # The ID of the conversation.
        self.id = id
        # The total number of messages in the conversation.
        self.message_count = message_count
        # A JSON-formatted string that contains an array of model IDs.
        self.model_ids = model_ids
        # The title of the conversation.
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.chat_data is not None:
            result['chatData'] = self.chat_data

        if self.delete_tag is not None:
            result['deleteTag'] = self.delete_tag

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.id is not None:
            result['id'] = self.id

        if self.message_count is not None:
            result['messageCount'] = self.message_count

        if self.model_ids is not None:
            result['modelIds'] = self.model_ids

        if self.title is not None:
            result['title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('chatData') is not None:
            self.chat_data = m.get('chatData')

        if m.get('deleteTag') is not None:
            self.delete_tag = m.get('deleteTag')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('messageCount') is not None:
            self.message_count = m.get('messageCount')

        if m.get('modelIds') is not None:
            self.model_ids = m.get('modelIds')

        if m.get('title') is not None:
            self.title = m.get('title')

        return self

