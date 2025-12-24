# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteLiveMessageGroupMessageResponseBody(DaraModel):
    def __init__(
        self,
        group_id: str = None,
        message_id: str = None,
        request_id: str = None,
    ):
        # The group ID.
        self.group_id = group_id
        # The ID of the deleted or non-existent message.
        self.message_id = message_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.message_id is not None:
            result['MessageId'] = self.message_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

