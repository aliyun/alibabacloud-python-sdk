# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetKvNamespaceResponseBody(DaraModel):
    def __init__(
        self,
        capacity: int = None,
        capacity_string: str = None,
        capacity_used: int = None,
        capacity_used_string: str = None,
        description: str = None,
        namespace: str = None,
        namespace_id: str = None,
        request_id: str = None,
        status: str = None,
    ):
        # The available capacity of the namespace. Unit: bytes.
        self.capacity = capacity
        # The available capacity of the namespace.
        self.capacity_string = capacity_string
        # The used capacity of the namespace. Unit: bytes.
        self.capacity_used = capacity_used
        # The used capacity of the namespace.
        self.capacity_used_string = capacity_used_string
        # The description of the namespace.
        self.description = description
        # The name of the namespace.
        self.namespace = namespace
        # The ID of the namespace.
        self.namespace_id = namespace_id
        # The request ID.
        self.request_id = request_id
        # The status of the namespace. Valid values:
        # 
        # *   **online**: working as expected.
        # *   **delete**: pending deletion.
        # *   **deleting**: being deleted.
        # *   **deleted**: deleted.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.capacity is not None:
            result['Capacity'] = self.capacity

        if self.capacity_string is not None:
            result['CapacityString'] = self.capacity_string

        if self.capacity_used is not None:
            result['CapacityUsed'] = self.capacity_used

        if self.capacity_used_string is not None:
            result['CapacityUsedString'] = self.capacity_used_string

        if self.description is not None:
            result['Description'] = self.description

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')

        if m.get('CapacityString') is not None:
            self.capacity_string = m.get('CapacityString')

        if m.get('CapacityUsed') is not None:
            self.capacity_used = m.get('CapacityUsed')

        if m.get('CapacityUsedString') is not None:
            self.capacity_used_string = m.get('CapacityUsedString')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

