# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListGatewayErrorAccessLogsRequest(DaraModel):
    def __init__(
        self,
        authority: str = None,
        end_time: int = None,
        gateway_request_id: str = None,
        path: str = None,
        response_code: str = None,
        route_name: str = None,
        start_time: int = None,
    ):
        # The domain name filter. This parameter performs an exact match on the authority field in Simple Log Service (SLS).
        self.authority = authority
        # The end time of the query window, in UNIX seconds. The value cannot be later than the current time, and the time span must be less than or equal to 24 hours.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The exact filter for the gateway request ID (x-acs-request-id).
        self.gateway_request_id = gateway_request_id
        # The request path filter.
        self.path = path
        # The specific HTTP error code. Only three-digit numbers in the range of 400 to 599 are accepted. This parameter is required. If it is not provided, the API returns the InvalidParameter.WithDetail(400) error.
        self.response_code = response_code
        # The route name filter.
        self.route_name = route_name
        # The start time of the query window, in UNIX seconds. The value must be greater than or equal to the current time minus 24 hours.
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
        if self.authority is not None:
            result['authority'] = self.authority

        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.gateway_request_id is not None:
            result['gatewayRequestId'] = self.gateway_request_id

        if self.path is not None:
            result['path'] = self.path

        if self.response_code is not None:
            result['responseCode'] = self.response_code

        if self.route_name is not None:
            result['routeName'] = self.route_name

        if self.start_time is not None:
            result['startTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authority') is not None:
            self.authority = m.get('authority')

        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('gatewayRequestId') is not None:
            self.gateway_request_id = m.get('gatewayRequestId')

        if m.get('path') is not None:
            self.path = m.get('path')

        if m.get('responseCode') is not None:
            self.response_code = m.get('responseCode')

        if m.get('routeName') is not None:
            self.route_name = m.get('routeName')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        return self

