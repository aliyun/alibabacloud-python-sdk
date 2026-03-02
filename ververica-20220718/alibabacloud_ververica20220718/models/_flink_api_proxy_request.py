# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class FlinkApiProxyRequest(DaraModel):
    def __init__(
        self,
        flink_api_path: str = None,
        namespace: str = None,
        resource_id: str = None,
        resource_type: str = None,
    ):
        # The path of the Flink UI.
        # 
        # This parameter is required.
        self.flink_api_path = flink_api_path
        # The name of the namespace.
        # 
        # This parameter is required.
        self.namespace = namespace
        # The resource ID.
        # 
        # This parameter is required.
        self.resource_id = resource_id
        # The type of the resource. Valid values:
        # 
        # *   jobs
        # *   sessionclusters
        # 
        # This parameter is required.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.flink_api_path is not None:
            result['flinkApiPath'] = self.flink_api_path

        if self.namespace is not None:
            result['namespace'] = self.namespace

        if self.resource_id is not None:
            result['resourceId'] = self.resource_id

        if self.resource_type is not None:
            result['resourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('flinkApiPath') is not None:
            self.flink_api_path = m.get('flinkApiPath')

        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')

        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')

        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')

        return self

