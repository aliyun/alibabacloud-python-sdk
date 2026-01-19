# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeApisByTrafficControlRequest(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        security_token: str = None,
        traffic_control_id: str = None,
    ):
        # The number of the page to return. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries to return on each page. Maximum value: 100. Default value: 10.
        self.page_size = page_size
        # The security token included in the WebSocket request header. The system uses this token to authenticate the request.
        self.security_token = security_token
        # The ID of the throttling policy that you want to query.
        # 
        # This parameter is required.
        self.traffic_control_id = traffic_control_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        if self.traffic_control_id is not None:
            result['TrafficControlId'] = self.traffic_control_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        if m.get('TrafficControlId') is not None:
            self.traffic_control_id = m.get('TrafficControlId')

        return self

