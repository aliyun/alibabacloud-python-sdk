# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_gpdb20160503 import models as main_models
from darabonba.model import DaraModel

class GetSupabaseProjectSpecResponseBody(DaraModel):
    def __init__(
        self,
        items: List[main_models.GetSupabaseProjectSpecResponseBodyItems] = None,
        request_id: str = None,
        zone_ids: List[str] = None,
    ):
        # The list of Supabase project specifications.
        self.items = items
        # The request ID.
        self.request_id = request_id
        # The list of zone IDs that support creating Supabase projects.
        self.zone_ids = zone_ids

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.zone_ids is not None:
            result['ZoneIds'] = self.zone_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.GetSupabaseProjectSpecResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ZoneIds') is not None:
            self.zone_ids = m.get('ZoneIds')

        return self

class GetSupabaseProjectSpecResponseBodyItems(DaraModel):
    def __init__(
        self,
        free: bool = None,
        spec: str = None,
        visible: bool = None,
    ):
        # Indicates whether the specification is free.
        self.free = free
        # The specification code.
        self.spec = spec
        # Indicates whether the specification is visible.
        self.visible = visible

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.free is not None:
            result['Free'] = self.free

        if self.spec is not None:
            result['Spec'] = self.spec

        if self.visible is not None:
            result['Visible'] = self.visible

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Free') is not None:
            self.free = m.get('Free')

        if m.get('Spec') is not None:
            self.spec = m.get('Spec')

        if m.get('Visible') is not None:
            self.visible = m.get('Visible')

        return self

