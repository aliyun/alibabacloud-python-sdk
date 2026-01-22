# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDatabaseDescriptionRequest(DaraModel):
    def __init__(
        self,
        dbinstance_name: str = None,
        db_description: str = None,
        db_name: str = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.dbinstance_name = dbinstance_name
        # This parameter is required.
        self.db_description = db_description
        # This parameter is required.
        self.db_name = db_name
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name

        if self.db_description is not None:
            result['DbDescription'] = self.db_description

        if self.db_name is not None:
            result['DbName'] = self.db_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')

        if m.get('DbDescription') is not None:
            self.db_description = m.get('DbDescription')

        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

