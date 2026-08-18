# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListNodePoolComponentsRequest(DaraModel):
    def __init__(
        self,
        image_id: str = None,
        image_type: str = None,
        instance_types: List[str] = None,
        max_results: int = None,
        next_token: str = None,
        nodepool_id: str = None,
        nodepool_type: str = None,
    ):
        self.image_id = image_id
        self.image_type = image_type
        self.instance_types = instance_types
        self.max_results = max_results
        self.next_token = next_token
        self.nodepool_id = nodepool_id
        self.nodepool_type = nodepool_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image_id is not None:
            result['image_id'] = self.image_id

        if self.image_type is not None:
            result['image_type'] = self.image_type

        if self.instance_types is not None:
            result['instance_types'] = self.instance_types

        if self.max_results is not None:
            result['max_results'] = self.max_results

        if self.next_token is not None:
            result['next_token'] = self.next_token

        if self.nodepool_id is not None:
            result['nodepool_id'] = self.nodepool_id

        if self.nodepool_type is not None:
            result['nodepool_type'] = self.nodepool_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('image_id') is not None:
            self.image_id = m.get('image_id')

        if m.get('image_type') is not None:
            self.image_type = m.get('image_type')

        if m.get('instance_types') is not None:
            self.instance_types = m.get('instance_types')

        if m.get('max_results') is not None:
            self.max_results = m.get('max_results')

        if m.get('next_token') is not None:
            self.next_token = m.get('next_token')

        if m.get('nodepool_id') is not None:
            self.nodepool_id = m.get('nodepool_id')

        if m.get('nodepool_type') is not None:
            self.nodepool_type = m.get('nodepool_type')

        return self

