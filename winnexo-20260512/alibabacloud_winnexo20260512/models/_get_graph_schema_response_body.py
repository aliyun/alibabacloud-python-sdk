# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetGraphSchemaResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        graph_name: str = None,
        message: str = None,
        request_id: str = None,
        schema_id: str = None,
        schema_version: str = None,
        yaml_edit: str = None,
    ):
        # The response status code.
        self.code = code
        # The graph name.
        # 
        # This parameter is required.
        self.graph_name = graph_name
        # The status code description.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The active QueryAgent registered schema ID corresponding to the graph. The value is null if not yet registered.
        self.schema_id = schema_id
        # The version.
        # 
        # This parameter is required.
        self.schema_version = schema_version
        # The raw YAML text of the Graph Schema trimmed by READ permissions, retaining $ref references within the authorized subgraph.
        # 
        # This parameter is required.
        self.yaml_edit = yaml_edit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.graph_name is not None:
            result['graphName'] = self.graph_name

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.schema_id is not None:
            result['schemaId'] = self.schema_id

        if self.schema_version is not None:
            result['schemaVersion'] = self.schema_version

        if self.yaml_edit is not None:
            result['yamlEdit'] = self.yaml_edit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('graphName') is not None:
            self.graph_name = m.get('graphName')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('schemaId') is not None:
            self.schema_id = m.get('schemaId')

        if m.get('schemaVersion') is not None:
            self.schema_version = m.get('schemaVersion')

        if m.get('yamlEdit') is not None:
            self.yaml_edit = m.get('yamlEdit')

        return self

