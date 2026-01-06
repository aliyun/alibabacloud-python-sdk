# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class AcceptDataworksEventRequest(DaraModel):
    def __init__(
        self,
        data: Dict[str, Any] = None,
        message_id: str = None,
    ):
        # The event content in the message.
        self.data = data
        # The message ID. You can obtain the ID from the message received when an extension point event is triggered. For more information about the message format, see [Message formats](https://help.aliyun.com/document_detail/436911.html).
        self.message_id = message_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data

        if self.message_id is not None:
            result['MessageId'] = self.message_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')

        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')

        return self

