# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, List

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class DLPartition(DaraModel):
    def __init__(
        self,
        catalog_name: str = None,
        create_time: int = None,
        db_name: str = None,
        last_access_time: int = None,
        parameters: Dict[str, str] = None,
        sd: main_models.DLStorageDescriptor = None,
        table_name: str = None,
        values: List[str] = None,
    ):
        self.catalog_name = catalog_name
        self.create_time = create_time
        self.db_name = db_name
        self.last_access_time = last_access_time
        self.parameters = parameters
        self.sd = sd
        self.table_name = table_name
        self.values = values

    def validate(self):
        if self.sd:
            self.sd.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.catalog_name is not None:
            result['CatalogName'] = self.catalog_name

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.db_name is not None:
            result['DbName'] = self.db_name

        if self.last_access_time is not None:
            result['LastAccessTime'] = self.last_access_time

        if self.parameters is not None:
            result['Parameters'] = self.parameters

        if self.sd is not None:
            result['Sd'] = self.sd.to_map()

        if self.table_name is not None:
            result['TableName'] = self.table_name

        if self.values is not None:
            result['Values'] = self.values

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogName') is not None:
            self.catalog_name = m.get('CatalogName')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')

        if m.get('LastAccessTime') is not None:
            self.last_access_time = m.get('LastAccessTime')

        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')

        if m.get('Sd') is not None:
            temp_model = main_models.DLStorageDescriptor()
            self.sd = temp_model.from_map(m.get('Sd'))

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        if m.get('Values') is not None:
            self.values = m.get('Values')

        return self

