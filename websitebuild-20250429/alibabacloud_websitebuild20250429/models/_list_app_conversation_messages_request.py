# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAppConversationMessagesRequest(DaraModel):
    def __init__(
        self,
        conversation_id: str = None,
        max_results: int = None,
        next_token: str = None,
        page_size: int = None,
        site_id: str = None,
        start_create_time: str = None,
    ):
        # Session ID.
        self.conversation_id = conversation_id
        # Number of results per query.
        # 
        # Valid values: 10 to 100. Default Value: 20.
        self.max_results = max_results
        # Token indicating the start of the next query. This value is empty if there is no subsequent query.
        self.next_token = next_token
        # Number of entries per page (10–100).
        self.page_size = page_size
        # Site ID.
        self.site_id = site_id
        # Creation Time of the last entry on the previous page (in ISO 8601 format).
        self.start_create_time = start_create_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.conversation_id is not None:
            result['ConversationId'] = self.conversation_id

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        if self.start_create_time is not None:
            result['StartCreateTime'] = self.start_create_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConversationId') is not None:
            self.conversation_id = m.get('ConversationId')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        if m.get('StartCreateTime') is not None:
            self.start_create_time = m.get('StartCreateTime')

        return self

