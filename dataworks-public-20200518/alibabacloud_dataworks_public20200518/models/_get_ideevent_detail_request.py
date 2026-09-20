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
        # The message ID of the DataWorks open message. After an extension point event is triggered, you can obtain the message ID from the received event message.
        # 
        # <props="china">For the message format, refer to [Message format](https://help.aliyun.com/document_detail/215367.html).
        # 
        # This parameter is required.
        self.message_id = message_id
        # The ID of the DataWorks workspace. You can obtain the workspace ID by parsing the DataWorks open message.
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

