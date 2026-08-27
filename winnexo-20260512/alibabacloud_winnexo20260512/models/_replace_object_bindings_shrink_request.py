# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ReplaceObjectBindingsShrinkRequest(DaraModel):
    def __init__(
        self,
        object_bindings_shrink: str = None,
        source_id: str = None,
        tenant_id: str = None,
    ):
        # The new list of object bindings (full replacement. Pass an empty list to clear all bindings).
        # 
        # This parameter is required.
        self.object_bindings_shrink = object_bindings_shrink
        # The ID of the personal FILE data source to be replaced (unique within the tenant).
        # 
        # This parameter is required.
        self.source_id = source_id
        # The tenant ID. This is a common parameter. Pass it explicitly through winnexo-cli using --tenant-id.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.object_bindings_shrink is not None:
            result['objectBindings'] = self.object_bindings_shrink

        if self.source_id is not None:
            result['sourceId'] = self.source_id

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('objectBindings') is not None:
            self.object_bindings_shrink = m.get('objectBindings')

        if m.get('sourceId') is not None:
            self.source_id = m.get('sourceId')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

