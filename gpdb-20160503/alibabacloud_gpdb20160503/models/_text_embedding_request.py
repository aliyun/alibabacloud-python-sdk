# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class TextEmbeddingRequest(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        dimension: int = None,
        input: List[str] = None,
        model: str = None,
        owner_id: int = None,
        region_id: str = None,
    ):
        # The cluster ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The number of embedding dimensions. The default value is the number of dimensions supported by the embedding algorithm.
        # 
        # > 
        # 
        # *   The text-embedding-v3 supports 1024, 768, and 512 dimensions. Default value: 1024.
        self.dimension = dimension
        # A list of text content to be embedded. The list length must not exceed 100.
        self.input = input
        # The text embedding model. Valid values:
        # 
        # *   text-embedding-v1:1536 dimensions
        # *   text-embedding-v2:1536 dimensions
        # *   text-embedding-v3 (default):1024, 768, and 512 dimensions
        # *   text2vec: 1024 dimensions
        # *   m3e-base: 768 dimensions
        # *   m3e-small: 512 dimensions
        self.model = model
        self.owner_id = owner_id
        # The region ID of the cluster.
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
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.dimension is not None:
            result['Dimension'] = self.dimension

        if self.input is not None:
            result['Input'] = self.input

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
            self.input = m.get('Input')

        if m.get('Model') is not None:
            self.model = m.get('Model')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

