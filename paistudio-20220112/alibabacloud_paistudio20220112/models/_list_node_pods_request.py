# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListNodePodsRequest(DaraModel):
    def __init__(
        self,
        gpuindexes: str = None,
        oversold_types: str = None,
        resource_group_id: str = None,
    ):
        # The GPU index number.
        self.gpuindexes = gpuindexes
        # The resource type used by the pod.
        self.oversold_types = oversold_types
        # The ID of the resource group to which the node belongs.
        # 
        # This parameter is required.
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gpuindexes is not None:
            result['GPUIndexes'] = self.gpuindexes

        if self.oversold_types is not None:
            result['OversoldTypes'] = self.oversold_types

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GPUIndexes') is not None:
            self.gpuindexes = m.get('GPUIndexes')

        if m.get('OversoldTypes') is not None:
            self.oversold_types = m.get('OversoldTypes')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        return self

