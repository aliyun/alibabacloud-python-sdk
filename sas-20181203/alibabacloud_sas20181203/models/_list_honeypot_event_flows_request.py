# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListHoneypotEventFlowsRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        dealed: str = None,
        lang: str = None,
        page_size: int = None,
        request_id: str = None,
        security_event_id: int = None,
    ):
        # The page number. Default value: **1**.
        self.current_page = current_page
        # The status of the event. Valid values: y, n, and a. The value y indicates handled. The value n indicates unhandled. The value a indicates all.
        self.dealed = dealed
        # The language of the content within the request and response. Default value: **zh**. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang
        # The number of entries per page. Default value: 20. If you leave this parameter empty, 20 entries are returned on each page.
        # 
        # >  We recommend that you do not leave this parameter empty.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The ID of the alert event. The ID of the management account of the ListHoneypotEvents resource directory.
        # 
        # >  You can call the [ListHoneypotEvents](~~ListHoneypotEvents~~) operation to query the IDs of alert events.
        self.security_event_id = security_event_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.dealed is not None:
            result['Dealed'] = self.dealed

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.security_event_id is not None:
            result['SecurityEventId'] = self.security_event_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('Dealed') is not None:
            self.dealed = m.get('Dealed')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SecurityEventId') is not None:
            self.security_event_id = m.get('SecurityEventId')

        return self

