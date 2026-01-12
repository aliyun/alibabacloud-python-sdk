# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddImageLibRequest(DaraModel):
    def __init__(
        self,
        comment: str = None,
        lib_name: str = None,
        region_id: str = None,
    ):
        # The remarks of the image library.
        self.comment = comment
        # The name of image library
        self.lib_name = lib_name
        # The region ID.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comment is not None:
            result['Comment'] = self.comment

        if self.lib_name is not None:
            result['LibName'] = self.lib_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('LibName') is not None:
            self.lib_name = m.get('LibName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

