# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DatasourceConfigUnified(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        legacy_raw: str = None,
        legacy_type: str = None,
        product_category: str = None,
        region_id: str = None,
        type: str = None,
    ):
        self.instance_id = instance_id
        self.legacy_raw = legacy_raw
        self.legacy_type = legacy_type
        self.product_category = product_category
        self.region_id = region_id
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.legacy_raw is not None:
            result['legacyRaw'] = self.legacy_raw

        if self.legacy_type is not None:
            result['legacyType'] = self.legacy_type

        if self.product_category is not None:
            result['productCategory'] = self.product_category

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('legacyRaw') is not None:
            self.legacy_raw = m.get('legacyRaw')

        if m.get('legacyType') is not None:
            self.legacy_type = m.get('legacyType')

        if m.get('productCategory') is not None:
            self.product_category = m.get('productCategory')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

