# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyMessagesFeedbacksRequest(DaraModel):
    def __init__(
        self,
        content: str = None,
        message_id: str = None,
        rating: str = None,
        workspace_id: str = None,
    ):
        # The feedback content.
        self.content = content
        # The message ID.
        self.message_id = message_id
        # The rating.
        self.rating = rating
        # The ContextDB workspace ID. Required only for ContextDB Manager App requests.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.message_id is not None:
            result['MessageId'] = self.message_id

        if self.rating is not None:
            result['Rating'] = self.rating

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')

        if m.get('Rating') is not None:
            self.rating = m.get('Rating')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

