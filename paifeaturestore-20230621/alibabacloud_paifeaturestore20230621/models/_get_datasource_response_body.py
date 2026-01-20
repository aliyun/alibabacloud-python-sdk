# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetDatasourceResponseBody(DaraModel):
    def __init__(
        self,
        config: str = None,
        datasource_id: str = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        name: str = None,
        request_id: str = None,
        type: str = None,
        uri: str = None,
        workspace_id: str = None,
    ):
        self.config = config
        self.datasource_id = datasource_id
        self.gmt_create_time = gmt_create_time
        self.gmt_modified_time = gmt_modified_time
        self.name = name
        self.request_id = request_id
        self.type = type
        self.uri = uri
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config is not None:
            result['Config'] = self.config

        if self.datasource_id is not None:
            result['DatasourceId'] = self.datasource_id

        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time

        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time

        if self.name is not None:
            result['Name'] = self.name

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.type is not None:
            result['Type'] = self.type

        if self.uri is not None:
            result['Uri'] = self.uri

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('DatasourceId') is not None:
            self.datasource_id = m.get('DatasourceId')

        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')

        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Uri') is not None:
            self.uri = m.get('Uri')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

