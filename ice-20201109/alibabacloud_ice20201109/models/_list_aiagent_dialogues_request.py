# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAIAgentDialoguesRequest(DaraModel):
    def __init__(
        self,
        end_time: int = None,
        order: str = None,
        page_number: int = None,
        page_size: int = None,
        round_limit: str = None,
        session_id: str = None,
        start_time: int = None,
    ):
        # Specify the end of the time range to query using a UNIX timestamp accurate to milliseconds.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The sorting order. Valid values: 
        # 
        # - DESC: descending order (default)
        # - ASC: ascending order
        self.order = order
        # The page number. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Default value: 20. Valid values: 1 to 100.
        self.page_size = page_size
        self.round_limit = round_limit
        # The session ID.
        # 
        # This parameter is required.
        self.session_id = session_id
        # Specify the start of the time range to query using a UNIX timestamp accurate to milliseconds.
        # 
        # This parameter is required.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.order is not None:
            result['Order'] = self.order

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.round_limit is not None:
            result['RoundLimit'] = self.round_limit

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RoundLimit') is not None:
            self.round_limit = m.get('RoundLimit')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

