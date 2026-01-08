# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetLifecycleRequest(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        limit: int = None,
        order: str = None,
        session_number: int = None,
        start_time: str = None,
        token: str = None,
    ):
        # The end of the time range to query.
        self.end_time = end_time
        # The number of sessions to query.
        self.limit = limit
        # The sorting order of the results. Valid values:
        # 
        # *   ASC: sorted by time in ascending order.
        # *   DESC: sorted by time in descending order.
        self.order = order
        # A session refers to the process of an instance from startup to failure or shutdown. The sessionNumber indicates the offset value for the instance\\"s session sequence.
        self.session_number = session_number
        # The beginning of the time range to query.
        self.start_time = start_time
        # The token used to share the URL.
        self.token = token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.limit is not None:
            result['Limit'] = self.limit

        if self.order is not None:
            result['Order'] = self.order

        if self.session_number is not None:
            result['SessionNumber'] = self.session_number

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.token is not None:
            result['Token'] = self.token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Limit') is not None:
            self.limit = m.get('Limit')

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('SessionNumber') is not None:
            self.session_number = m.get('SessionNumber')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Token') is not None:
            self.token = m.get('Token')

        return self

