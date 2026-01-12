# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateImageLibRequest(DaraModel):
    def __init__(
        self,
        comment: str = None,
        free_inspection: int = None,
        lib_id: str = None,
        lib_name: str = None,
        region_id: str = None,
    ):
        # Comment information for the library.
        self.comment = comment
        # Exemption from review configuration.
        self.free_inspection = free_inspection
        # Library ID.
        self.lib_id = lib_id
        # Library name.
        self.lib_name = lib_name
        # Region ID.
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

        if self.free_inspection is not None:
            result['FreeInspection'] = self.free_inspection

        if self.lib_id is not None:
            result['LibId'] = self.lib_id

        if self.lib_name is not None:
            result['LibName'] = self.lib_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('FreeInspection') is not None:
            self.free_inspection = m.get('FreeInspection')

        if m.get('LibId') is not None:
            self.lib_id = m.get('LibId')

        if m.get('LibName') is not None:
            self.lib_name = m.get('LibName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

