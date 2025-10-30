# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class TextEmbeddingShrinkRequest(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        dimension: int = None,
        input_shrink: str = None,
        model: str = None,
        owner_id: int = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        self.dimension = dimension
        self.input_shrink = input_shrink
        self.model = model
        self.owner_id = owner_id
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.dimension is not None:
            result['Dimension'] = self.dimension

        if self.input_shrink is not None:
            result['Input'] = self.input_shrink

        if self.model is not None:
            result['Model'] = self.model

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('Dimension') is not None:
            self.dimension = m.get('Dimension')

        if m.get('Input') is not None:
            self.input_shrink = m.get('Input')

        if m.get('Model') is not None:
            self.model = m.get('Model')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

