# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetAgenticCatalogRequest(DaraModel):
    def __init__(
        self,
        catalog_uuid: str = None,
    ):
        # The catalog UUID. You can obtain it by calling ListAgenticCatalog or SearchAgenticCatalog.
        # 
        # This parameter is required.
        self.catalog_uuid = catalog_uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.catalog_uuid is not None:
            result['CatalogUuid'] = self.catalog_uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogUuid') is not None:
            self.catalog_uuid = m.get('CatalogUuid')

        return self

