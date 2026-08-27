# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteChatSessionResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        deleted: bool = None,
        hard_delete: bool = None,
        message: str = None,
        request_id: str = None,
        session_id: str = None,
    ):
        # The error code.
        self.code = code
        # Indicates whether the session is deleted.
        self.deleted = deleted
        # Indicates whether the session is hard-deleted.
        self.hard_delete = hard_delete
        # The status code description.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The unique identifier of the function session.
        self.session_id = session_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.deleted is not None:
            result['deleted'] = self.deleted

        if self.hard_delete is not None:
            result['hardDelete'] = self.hard_delete

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.session_id is not None:
            result['sessionId'] = self.session_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('deleted') is not None:
            self.deleted = m.get('deleted')

        if m.get('hardDelete') is not None:
            self.hard_delete = m.get('hardDelete')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')

        return self

