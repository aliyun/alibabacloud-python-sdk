# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class KopilotListConversationChatMessagesRequest(DaraModel):
    def __init__(
        self,
        before_turn_id: int = None,
        page_size: int = None,
        region_id: str = None,
        session_id: str = None,
    ):
        self.before_turn_id = before_turn_id
        self.page_size = page_size
        # This parameter is required.
        self.region_id = region_id
        self.session_id = session_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.before_turn_id is not None:
            result['BeforeTurnId'] = self.before_turn_id

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeforeTurnId') is not None:
            self.before_turn_id = m.get('BeforeTurnId')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        return self

