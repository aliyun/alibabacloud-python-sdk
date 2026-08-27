# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_winnexo20260512 import models as main_models
from darabonba.model import DaraModel

class ReplaceObjectBindingsRequest(DaraModel):
    def __init__(
        self,
        object_bindings: List[main_models.ReplaceObjectBindingsRequestObjectBindings] = None,
        source_id: str = None,
        tenant_id: str = None,
    ):
        # The new list of object bindings (full replacement. Pass an empty list to clear all bindings).
        # 
        # This parameter is required.
        self.object_bindings = object_bindings
        # The ID of the personal FILE data source to be replaced (unique within the tenant).
        # 
        # This parameter is required.
        self.source_id = source_id
        # The tenant ID. This is a common parameter. Pass it explicitly through winnexo-cli using --tenant-id.
        self.tenant_id = tenant_id

    def validate(self):
        if self.object_bindings:
            for v1 in self.object_bindings:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['objectBindings'] = []
        if self.object_bindings is not None:
            for k1 in self.object_bindings:
                result['objectBindings'].append(k1.to_map() if k1 else None)

        if self.source_id is not None:
            result['sourceId'] = self.source_id

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.object_bindings = []
        if m.get('objectBindings') is not None:
            for k1 in m.get('objectBindings'):
                temp_model = main_models.ReplaceObjectBindingsRequestObjectBindings()
                self.object_bindings.append(temp_model.from_map(k1))

        if m.get('sourceId') is not None:
            self.source_id = m.get('sourceId')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

class ReplaceObjectBindingsRequestObjectBindings(DaraModel):
    def __init__(
        self,
        graph_name: str = None,
        object_id: str = None,
        object_type: str = None,
    ):
        # The semantic graph name to which the binding object belongs (object_id is unique within this graph. Required).
        self.graph_name = graph_name
        # The binding object ID.
        self.object_id = object_id
        # The binding object type (such as customer or project).
        self.object_type = object_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.graph_name is not None:
            result['graphName'] = self.graph_name

        if self.object_id is not None:
            result['objectId'] = self.object_id

        if self.object_type is not None:
            result['objectType'] = self.object_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('graphName') is not None:
            self.graph_name = m.get('graphName')

        if m.get('objectId') is not None:
            self.object_id = m.get('objectId')

        if m.get('objectType') is not None:
            self.object_type = m.get('objectType')

        return self

