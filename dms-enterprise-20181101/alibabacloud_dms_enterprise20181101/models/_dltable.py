# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any, List

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class DLTable(DaraModel):
    def __init__(
        self,
        catalog_name: str = None,
        create_time: int = None,
        creator_id: int = None,
        db_id: int = None,
        db_name: str = None,
        description: str = None,
        last_access_time: int = None,
        location: str = None,
        modifier_id: int = None,
        name: str = None,
        owner: str = None,
        owner_type: str = None,
        parameters: Dict[str, Any] = None,
        partition_keys: List[main_models.DLColumn] = None,
        retention: int = None,
        storage_descriptor: main_models.DLStorageDescriptor = None,
        table_type: str = None,
        view_expanded_text: str = None,
        view_original_text: str = None,
    ):
        self.catalog_name = catalog_name
        self.create_time = create_time
        self.creator_id = creator_id
        self.db_id = db_id
        self.db_name = db_name
        self.description = description
        self.last_access_time = last_access_time
        self.location = location
        self.modifier_id = modifier_id
        self.name = name
        self.owner = owner
        self.owner_type = owner_type
        self.parameters = parameters
        self.partition_keys = partition_keys
        self.retention = retention
        self.storage_descriptor = storage_descriptor
        self.table_type = table_type
        self.view_expanded_text = view_expanded_text
        self.view_original_text = view_original_text

    def validate(self):
        if self.partition_keys:
            for v1 in self.partition_keys:
                 if v1:
                    v1.validate()
        if self.storage_descriptor:
            self.storage_descriptor.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.catalog_name is not None:
            result['CatalogName'] = self.catalog_name

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id

        if self.db_id is not None:
            result['DbId'] = self.db_id

        if self.db_name is not None:
            result['DbName'] = self.db_name

        if self.description is not None:
            result['Description'] = self.description

        if self.last_access_time is not None:
            result['LastAccessTime'] = self.last_access_time

        if self.location is not None:
            result['Location'] = self.location

        if self.modifier_id is not None:
            result['ModifierId'] = self.modifier_id

        if self.name is not None:
            result['Name'] = self.name

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.owner_type is not None:
            result['OwnerType'] = self.owner_type

        if self.parameters is not None:
            result['Parameters'] = self.parameters

        result['PartitionKeys'] = []
        if self.partition_keys is not None:
            for k1 in self.partition_keys:
                result['PartitionKeys'].append(k1.to_map() if k1 else None)

        if self.retention is not None:
            result['Retention'] = self.retention

        if self.storage_descriptor is not None:
            result['StorageDescriptor'] = self.storage_descriptor.to_map()

        if self.table_type is not None:
            result['TableType'] = self.table_type

        if self.view_expanded_text is not None:
            result['ViewExpandedText'] = self.view_expanded_text

        if self.view_original_text is not None:
            result['ViewOriginalText'] = self.view_original_text

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogName') is not None:
            self.catalog_name = m.get('CatalogName')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')

        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')

        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('LastAccessTime') is not None:
            self.last_access_time = m.get('LastAccessTime')

        if m.get('Location') is not None:
            self.location = m.get('Location')

        if m.get('ModifierId') is not None:
            self.modifier_id = m.get('ModifierId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('OwnerType') is not None:
            self.owner_type = m.get('OwnerType')

        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')

        self.partition_keys = []
        if m.get('PartitionKeys') is not None:
            for k1 in m.get('PartitionKeys'):
                temp_model = main_models.DLColumn()
                self.partition_keys.append(temp_model.from_map(k1))

        if m.get('Retention') is not None:
            self.retention = m.get('Retention')

        if m.get('StorageDescriptor') is not None:
            temp_model = main_models.DLStorageDescriptor()
            self.storage_descriptor = temp_model.from_map(m.get('StorageDescriptor'))

        if m.get('TableType') is not None:
            self.table_type = m.get('TableType')

        if m.get('ViewExpandedText') is not None:
            self.view_expanded_text = m.get('ViewExpandedText')

        if m.get('ViewOriginalText') is not None:
            self.view_original_text = m.get('ViewOriginalText')

        return self

