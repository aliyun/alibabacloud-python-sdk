# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PrecheckResourceCountShrinkRequest(DaraModel):
    def __init__(
        self,
        resource_type: str = None,
        tag_resource_matchers_shrink: str = None,
    ):
        self.resource_type = resource_type
        # This parameter is required.
        self.tag_resource_matchers_shrink = tag_resource_matchers_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.tag_resource_matchers_shrink is not None:
            result['TagResourceMatchers'] = self.tag_resource_matchers_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('TagResourceMatchers') is not None:
            self.tag_resource_matchers_shrink = m.get('TagResourceMatchers')

        return self

