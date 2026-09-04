# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BatchRemoveOperatingObjectFavoritesShrinkRequest(DaraModel):
    def __init__(
        self,
        graph_name: str = None,
        object_ids_shrink: str = None,
        object_type: str = None,
        operating_object_name: str = None,
        tenant_id: str = None,
    ):
        # The graph name.
        # 
        # This parameter is required.
        self.graph_name = graph_name
        # The list of primary object business IDs.
        # 
        # This parameter is required.
        self.object_ids_shrink = object_ids_shrink
        # The object type, such as customer. This parameter has a value when type is set to mention.
        # 
        # This parameter is required.
        self.object_type = object_type
        # The operating object name.
        # 
        # This parameter is required.
        self.operating_object_name = operating_object_name
        # The tenant ID. This is a common parameter. Pass it explicitly in winnexo-cli by using --tenant-id.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.graph_name is not None:
            result['graphName'] = self.graph_name

        if self.object_ids_shrink is not None:
            result['objectIds'] = self.object_ids_shrink

        if self.object_type is not None:
            result['objectType'] = self.object_type

        if self.operating_object_name is not None:
            result['operatingObjectName'] = self.operating_object_name

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('graphName') is not None:
            self.graph_name = m.get('graphName')

        if m.get('objectIds') is not None:
            self.object_ids_shrink = m.get('objectIds')

        if m.get('objectType') is not None:
            self.object_type = m.get('objectType')

        if m.get('operatingObjectName') is not None:
            self.operating_object_name = m.get('operatingObjectName')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

