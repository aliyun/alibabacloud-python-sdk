# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PublishMessageResponseBody(DaraModel):
    def __init__(
        self,
        message_body_md5: str = None,
        message_id: str = None,
    ):
        self.message_body_md5 = message_body_md5
        self.message_id = message_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.message_body_md5 is not None:
            result['MessageBodyMD5'] = self.message_body_md5

        if self.message_id is not None:
            result['MessageId'] = self.message_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MessageBodyMD5') is not None:
            self.message_body_md5 = m.get('MessageBodyMD5')

        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')

        return self

