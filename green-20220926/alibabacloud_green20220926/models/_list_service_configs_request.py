# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListServiceConfigsRequest(DaraModel):
    def __init__(
        self,
        classify: str = None,
        region_id: str = None,
        resource_type: str = None,
        use_status: str = None,
    ):
        # Category.
        self.classify = classify
        # Region ID.
        self.region_id = region_id
        # Resource type.
        self.resource_type = resource_type
        # Usage status.
        self.use_status = use_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.classify is not None:
            result['Classify'] = self.classify

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.use_status is not None:
            result['UseStatus'] = self.use_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Classify') is not None:
            self.classify = m.get('Classify')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('UseStatus') is not None:
            self.use_status = m.get('UseStatus')

        return self

