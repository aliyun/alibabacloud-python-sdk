# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListFunctionRestrictionsRequest(DaraModel):
    def __init__(
        self,
        model_type: str = None,
        region: str = None,
        source: str = None,
    ):
        # The model type.
        self.model_type = model_type
        # The region ID.
        self.region = region
        # The source.
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.model_type is not None:
            result['modelType'] = self.model_type

        if self.region is not None:
            result['region'] = self.region

        if self.source is not None:
            result['source'] = self.source

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('modelType') is not None:
            self.model_type = m.get('modelType')

        if m.get('region') is not None:
            self.region = m.get('region')

        if m.get('source') is not None:
            self.source = m.get('source')

        return self

