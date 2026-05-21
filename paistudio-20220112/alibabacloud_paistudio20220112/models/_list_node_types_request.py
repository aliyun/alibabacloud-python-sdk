# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListNodeTypesRequest(DaraModel):
    def __init__(
        self,
        accelerator_type: str = None,
        gputype: str = None,
        node_types: str = None,
        quota_id: str = None,
        resource_group_ids: str = None,
    ):
        self.accelerator_type = accelerator_type
        self.gputype = gputype
        self.node_types = node_types
        self.quota_id = quota_id
        self.resource_group_ids = resource_group_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accelerator_type is not None:
            result['AcceleratorType'] = self.accelerator_type

        if self.gputype is not None:
            result['GPUType'] = self.gputype

        if self.node_types is not None:
            result['NodeTypes'] = self.node_types

        if self.quota_id is not None:
            result['QuotaId'] = self.quota_id

        if self.resource_group_ids is not None:
            result['ResourceGroupIds'] = self.resource_group_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorType') is not None:
            self.accelerator_type = m.get('AcceleratorType')

        if m.get('GPUType') is not None:
            self.gputype = m.get('GPUType')

        if m.get('NodeTypes') is not None:
            self.node_types = m.get('NodeTypes')

        if m.get('QuotaId') is not None:
            self.quota_id = m.get('QuotaId')

        if m.get('ResourceGroupIds') is not None:
            self.resource_group_ids = m.get('ResourceGroupIds')

        return self

