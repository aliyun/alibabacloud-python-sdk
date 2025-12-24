# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class DescribeUserConnectTimeResponseBody(DaraModel):
    def __init__(
        self,
        count: int = None,
        data: List[main_models.DescribeUserConnectTimeResponseBodyData] = None,
        next_token: str = None,
        request_id: str = None,
    ):
        self.count = count
        self.data = data
        self.next_token = next_token
        self.request_id = request_id

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.DescribeUserConnectTimeResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeUserConnectTimeResponseBodyData(DaraModel):
    def __init__(
        self,
        end_connect_time: str = None,
        end_user_id: str = None,
        oversold_group_id: str = None,
        start_connect_time: str = None,
        user_desktop_id: str = None,
        user_group_id: str = None,
    ):
        self.end_connect_time = end_connect_time
        self.end_user_id = end_user_id
        self.oversold_group_id = oversold_group_id
        self.start_connect_time = start_connect_time
        self.user_desktop_id = user_desktop_id
        self.user_group_id = user_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_connect_time is not None:
            result['EndConnectTime'] = self.end_connect_time

        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id

        if self.oversold_group_id is not None:
            result['OversoldGroupId'] = self.oversold_group_id

        if self.start_connect_time is not None:
            result['StartConnectTime'] = self.start_connect_time

        if self.user_desktop_id is not None:
            result['UserDesktopId'] = self.user_desktop_id

        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndConnectTime') is not None:
            self.end_connect_time = m.get('EndConnectTime')

        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')

        if m.get('OversoldGroupId') is not None:
            self.oversold_group_id = m.get('OversoldGroupId')

        if m.get('StartConnectTime') is not None:
            self.start_connect_time = m.get('StartConnectTime')

        if m.get('UserDesktopId') is not None:
            self.user_desktop_id = m.get('UserDesktopId')

        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')

        return self

