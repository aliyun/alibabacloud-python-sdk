# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class AddDataSourceRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        connection_info: str = None,
        credential: str = None,
        data_source_name: str = None,
        data_source_type: str = None,
        exclude: str = None,
        include: str = None,
        index_level: str = None,
        options: str = None,
        path: List[str] = None,
        schedule: str = None,
        speed_limit: str = None,
    ):
        self.cluster_id = cluster_id
        self.connection_info = connection_info
        self.credential = credential
        # This parameter is required.
        self.data_source_name = data_source_name
        # This parameter is required.
        self.data_source_type = data_source_type
        self.exclude = exclude
        self.include = include
        self.index_level = index_level
        self.options = options
        self.path = path
        self.schedule = schedule
        self.speed_limit = speed_limit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.connection_info is not None:
            result['ConnectionInfo'] = self.connection_info

        if self.credential is not None:
            result['Credential'] = self.credential

        if self.data_source_name is not None:
            result['DataSourceName'] = self.data_source_name

        if self.data_source_type is not None:
            result['DataSourceType'] = self.data_source_type

        if self.exclude is not None:
            result['Exclude'] = self.exclude

        if self.include is not None:
            result['Include'] = self.include

        if self.index_level is not None:
            result['IndexLevel'] = self.index_level

        if self.options is not None:
            result['Options'] = self.options

        if self.path is not None:
            result['Path'] = self.path

        if self.schedule is not None:
            result['Schedule'] = self.schedule

        if self.speed_limit is not None:
            result['SpeedLimit'] = self.speed_limit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ConnectionInfo') is not None:
            self.connection_info = m.get('ConnectionInfo')

        if m.get('Credential') is not None:
            self.credential = m.get('Credential')

        if m.get('DataSourceName') is not None:
            self.data_source_name = m.get('DataSourceName')

        if m.get('DataSourceType') is not None:
            self.data_source_type = m.get('DataSourceType')

        if m.get('Exclude') is not None:
            self.exclude = m.get('Exclude')

        if m.get('Include') is not None:
            self.include = m.get('Include')

        if m.get('IndexLevel') is not None:
            self.index_level = m.get('IndexLevel')

        if m.get('Options') is not None:
            self.options = m.get('Options')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        if m.get('Schedule') is not None:
            self.schedule = m.get('Schedule')

        if m.get('SpeedLimit') is not None:
            self.speed_limit = m.get('SpeedLimit')

        return self

