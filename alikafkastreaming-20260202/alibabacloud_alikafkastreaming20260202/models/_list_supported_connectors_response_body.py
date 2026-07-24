# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alikafkastreaming20260202 import models as main_models
from darabonba.model import DaraModel

class ListSupportedConnectorsResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: List[main_models.ListSupportedConnectorsResponseBodyData] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id
        self.success = success

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
        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListSupportedConnectorsResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListSupportedConnectorsResponseBodyData(DaraModel):
    def __init__(
        self,
        connector: str = None,
        description: str = None,
        icon_url: str = None,
        name: str = None,
        sink_sql: str = None,
        source_sql: str = None,
    ):
        self.connector = connector
        self.description = description
        self.icon_url = icon_url
        self.name = name
        self.sink_sql = sink_sql
        self.source_sql = source_sql

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connector is not None:
            result['Connector'] = self.connector

        if self.description is not None:
            result['Description'] = self.description

        if self.icon_url is not None:
            result['IconUrl'] = self.icon_url

        if self.name is not None:
            result['Name'] = self.name

        if self.sink_sql is not None:
            result['SinkSql'] = self.sink_sql

        if self.source_sql is not None:
            result['SourceSql'] = self.source_sql

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Connector') is not None:
            self.connector = m.get('Connector')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('IconUrl') is not None:
            self.icon_url = m.get('IconUrl')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('SinkSql') is not None:
            self.sink_sql = m.get('SinkSql')

        if m.get('SourceSql') is not None:
            self.source_sql = m.get('SourceSql')

        return self

