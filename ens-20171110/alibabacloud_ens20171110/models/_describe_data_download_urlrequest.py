# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDataDownloadURLRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        data_name: str = None,
        data_version: str = None,
        expire_timeout: int = None,
        server_filter_strategy: str = None,
    ):
        # The ID of the application.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The name of the data file.
        # 
        # This parameter is required.
        self.data_name = data_name
        # The version number of the data file.
        # 
        # This parameter is required.
        self.data_version = data_version
        # This parameter is reserved.
        self.expire_timeout = expire_timeout
        # The condition that you want to use to filter file servers. You can specify multiple canary release policies. By default, all resources are queried.
        self.server_filter_strategy = server_filter_strategy

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.data_name is not None:
            result['DataName'] = self.data_name

        if self.data_version is not None:
            result['DataVersion'] = self.data_version

        if self.expire_timeout is not None:
            result['ExpireTimeout'] = self.expire_timeout

        if self.server_filter_strategy is not None:
            result['ServerFilterStrategy'] = self.server_filter_strategy

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('DataName') is not None:
            self.data_name = m.get('DataName')

        if m.get('DataVersion') is not None:
            self.data_version = m.get('DataVersion')

        if m.get('ExpireTimeout') is not None:
            self.expire_timeout = m.get('ExpireTimeout')

        if m.get('ServerFilterStrategy') is not None:
            self.server_filter_strategy = m.get('ServerFilterStrategy')

        return self

