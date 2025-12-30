# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetSourceLocationRequest(DaraModel):
    def __init__(
        self,
        source_location_name: str = None,
    ):
        # The name of the source location.
        # 
        # This parameter is required.
        self.source_location_name = source_location_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.source_location_name is not None:
            result['SourceLocationName'] = self.source_location_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceLocationName') is not None:
            self.source_location_name = m.get('SourceLocationName')

        return self

