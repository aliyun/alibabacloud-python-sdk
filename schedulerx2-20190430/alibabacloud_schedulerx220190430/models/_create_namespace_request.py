# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateNamespaceRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        region_id: str = None,
        uid: str = None,
    ):
        # The namespace description.
        self.description = description
        # The namespace name.
        # 
        # This parameter is required.
        self.name = name
        # The region ID. For example, `cn-hangzhou` specifies the China (Hangzhou) region.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The namespace UID. This value must be globally unique. We recommend that you use a UUID.
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.uid is not None:
            result['Uid'] = self.uid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Uid') is not None:
            self.uid = m.get('Uid')

        return self

