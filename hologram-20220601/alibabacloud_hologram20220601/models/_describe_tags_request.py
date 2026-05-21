# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeTagsRequest(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        tags_only: bool = None,
    ):
        self.region_id = region_id
        self.tags_only = tags_only

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.tags_only is not None:
            result['tagsOnly'] = self.tags_only

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('tagsOnly') is not None:
            self.tags_only = m.get('tagsOnly')

        return self

