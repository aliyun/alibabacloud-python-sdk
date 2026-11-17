# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SendWorkItemMessageResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        message_id: str = None,
        request_id: str = None,
        session_id: str = None,
        user_message_id: str = None,
        work_item_id: str = None,
    ):
        # The business status code. A value of 200 indicates success. Other values indicate backend error codes.
        self.code = code
        # The error description. This parameter is empty if the request is successful.
        self.message = message
        # The ID of the assistant message. The reply is generated asynchronously in the background.
        self.message_id = message_id
        # The request ID.
        self.request_id = request_id
        # The ID of the existing topic session.
        self.session_id = session_id
        # The ID of the user message.
        self.user_message_id = user_message_id
        # The work item ID in the request. If only conversationId is specified, a compatible ID in the legacy-topic:<conversationId> format is returned.
        self.work_item_id = work_item_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.message is not None:
            result['message'] = self.message

        if self.message_id is not None:
            result['messageId'] = self.message_id

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.session_id is not None:
            result['sessionId'] = self.session_id

        if self.user_message_id is not None:
            result['userMessageId'] = self.user_message_id

        if self.work_item_id is not None:
            result['workItemId'] = self.work_item_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('messageId') is not None:
            self.message_id = m.get('messageId')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')

        if m.get('userMessageId') is not None:
            self.user_message_id = m.get('userMessageId')

        if m.get('workItemId') is not None:
            self.work_item_id = m.get('workItemId')

        return self

