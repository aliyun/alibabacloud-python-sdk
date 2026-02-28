# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateErRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        er_id: str = None,
        er_name: str = None,
        region_id: str = None,
    ):
        # The description of the document.
        self.description = description
        # Lingjun HUB Instance ID
        # 
        # This parameter is required.
        self.er_id = er_id
        # Parameter
        self.er_name = er_name
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.er_id is not None:
            result['ErId'] = self.er_id

        if self.er_name is not None:
            result['ErName'] = self.er_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ErId') is not None:
            self.er_id = m.get('ErId')

        if m.get('ErName') is not None:
            self.er_name = m.get('ErName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

