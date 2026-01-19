# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeTrafficControlsRequest(DaraModel):
    def __init__(
        self,
        api_id: str = None,
        group_id: str = None,
        page_number: int = None,
        page_size: int = None,
        security_token: str = None,
        stage_name: str = None,
        traffic_control_id: str = None,
        traffic_control_name: str = None,
    ):
        # The specified API ID. This parameter must be specified together with GroupId and StageName.
        self.api_id = api_id
        # The specified group ID. This parameter must be specified together with ApiId and StageName.
        self.group_id = group_id
        # The number of the page to return. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries to return on each page. Maximum value: 100. Default value: 10.
        self.page_size = page_size
        # The security token included in the WebSocket request header. The system uses this token to authenticate the request.
        self.security_token = security_token
        # The environment name. This parameter must be specified together with GroupId and ApiId. Valid values:********
        # 
        # *   **RELEASE**
        # *   **TEST**
        self.stage_name = stage_name
        # The ID of the throttling policy.
        self.traffic_control_id = traffic_control_id
        # The name of the throttling policy.
        self.traffic_control_name = traffic_control_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_id is not None:
            result['ApiId'] = self.api_id

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        if self.stage_name is not None:
            result['StageName'] = self.stage_name

        if self.traffic_control_id is not None:
            result['TrafficControlId'] = self.traffic_control_id

        if self.traffic_control_name is not None:
            result['TrafficControlName'] = self.traffic_control_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')

        if m.get('TrafficControlId') is not None:
            self.traffic_control_id = m.get('TrafficControlId')

        if m.get('TrafficControlName') is not None:
            self.traffic_control_name = m.get('TrafficControlName')

        return self

