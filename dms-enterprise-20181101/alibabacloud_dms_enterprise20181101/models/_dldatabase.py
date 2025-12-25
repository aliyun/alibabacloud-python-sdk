# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class DLDatabase(DaraModel):
    def __init__(
        self,
        catalog_name: str = None,
        db_id: int = None,
        description: str = None,
        location: str = None,
        name: str = None,
        parameters: Dict[str, Any] = None,
    ):
        self.catalog_name = catalog_name
        self.db_id = db_id
        self.description = description
        self.location = location
        self.name = name
        self.parameters = parameters

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.catalog_name is not None:
            result['CatalogName'] = self.catalog_name

        if self.db_id is not None:
            result['DbId'] = self.db_id

        if self.description is not None:
            result['Description'] = self.description

        if self.location is not None:
            result['Location'] = self.location

        if self.name is not None:
            result['Name'] = self.name

        if self.parameters is not None:
            result['Parameters'] = self.parameters

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogName') is not None:
            self.catalog_name = m.get('CatalogName')

        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Location') is not None:
            self.location = m.get('Location')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')

        return self

