# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreatePersonalFeishuChatResponseBody(DaraModel):
    def __init__(
        self,
        chat_id: str = None,
        code: str = None,
        directory_id: str = None,
        gmt_create: str = None,
        message: str = None,
        name: str = None,
        request_id: str = None,
        scope: str = None,
        source_id: str = None,
        status: str = None,
    ):
        # The group chat session ID.
        self.chat_id = chat_id
        # The status code.
        self.code = code
        # The directory ID.
        self.directory_id = directory_id
        # The creation time.
        self.gmt_create = gmt_create
        # The status code description.
        self.message = message
        # The skill name.
        self.name = name
        # The request ID.
        self.request_id = request_id
        # The permission scope.
        self.scope = scope
        # The source ID.
        self.source_id = source_id
        # The signing status. Valid values:
        # - CREATED: Created but not signed.
        # - SUCCESS: Signed successfully.
        # - STOP: Terminated.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.chat_id is not None:
            result['chatId'] = self.chat_id

        if self.code is not None:
            result['code'] = self.code

        if self.directory_id is not None:
            result['directoryId'] = self.directory_id

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.message is not None:
            result['message'] = self.message

        if self.name is not None:
            result['name'] = self.name

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.scope is not None:
            result['scope'] = self.scope

        if self.source_id is not None:
            result['sourceId'] = self.source_id

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('chatId') is not None:
            self.chat_id = m.get('chatId')

        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('directoryId') is not None:
            self.directory_id = m.get('directoryId')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('scope') is not None:
            self.scope = m.get('scope')

        if m.get('sourceId') is not None:
            self.source_id = m.get('sourceId')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

