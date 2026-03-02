# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class NodeExecutionStatusDTO(DaraModel):
    def __init__(
        self,
        execution_id: str = None,
        namespace: str = None,
        resource_id: str = None,
        status: str = None,
        type: str = None,
        workspace: str = None,
    ):
        self.execution_id = execution_id
        self.namespace = namespace
        self.resource_id = resource_id
        self.status = status
        self.type = type
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.execution_id is not None:
            result['executionId'] = self.execution_id

        if self.namespace is not None:
            result['namespace'] = self.namespace

        if self.resource_id is not None:
            result['resourceId'] = self.resource_id

        if self.status is not None:
            result['status'] = self.status

        if self.type is not None:
            result['type'] = self.type

        if self.workspace is not None:
            result['workspace'] = self.workspace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('executionId') is not None:
            self.execution_id = m.get('executionId')

        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')

        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')

        return self

