# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetIDEEventDetailRequest(DaraModel):
    def __init__(
        self,
        message_id: str = None,
        project_id: int = None,
    ):
        # The message ID in DataWorks OpenEvent. You can obtain the ID from a received message when an extension point event is triggered.
        # 
        # This parameter is required.
        self.message_id = message_id
        # The DataWorks workspace ID. You can obtain the ID from the message.
        # 
        # This parameter is required.
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.message_id is not None:
            result['MessageId'] = self.message_id

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        return self

