# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateGraphResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data_source_id: int = None,
        graph_name: str = None,
        message: str = None,
        request_id: str = None,
        schema_version: str = None,
        sync_status: str = None,
    ):
        # The status code.
        self.code = code
        # The data source ID.
        self.data_source_id = data_source_id
        # The graph name.
        self.graph_name = graph_name
        # The status code description.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The version.
        self.schema_version = schema_version
        # The OSS synchronization and extraction status. Valid values:
        # - -1: Not set (default).
        # - 0: Disabled.
        # - 1: Enabled.
        self.sync_status = sync_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.data_source_id is not None:
            result['dataSourceId'] = self.data_source_id

        if self.graph_name is not None:
            result['graphName'] = self.graph_name

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.schema_version is not None:
            result['schemaVersion'] = self.schema_version

        if self.sync_status is not None:
            result['syncStatus'] = self.sync_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('dataSourceId') is not None:
            self.data_source_id = m.get('dataSourceId')

        if m.get('graphName') is not None:
            self.graph_name = m.get('graphName')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('schemaVersion') is not None:
            self.schema_version = m.get('schemaVersion')

        if m.get('syncStatus') is not None:
            self.sync_status = m.get('syncStatus')

        return self

