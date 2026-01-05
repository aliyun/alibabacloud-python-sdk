# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class Column(DaraModel):
    def __init__(
        self,
        business_metadata: main_models.ColumnBusinessMetadata = None,
        comment: str = None,
        foreign_key: bool = None,
        id: str = None,
        name: str = None,
        partition_key: bool = None,
        position: int = None,
        primary_key: bool = None,
        table_id: str = None,
        type: str = None,
    ):
        self.business_metadata = business_metadata
        self.comment = comment
        self.foreign_key = foreign_key
        self.id = id
        self.name = name
        self.partition_key = partition_key
        self.position = position
        self.primary_key = primary_key
        self.table_id = table_id
        self.type = type

    def validate(self):
        if self.business_metadata:
            self.business_metadata.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.business_metadata is not None:
            result['BusinessMetadata'] = self.business_metadata.to_map()

        if self.comment is not None:
            result['Comment'] = self.comment

        if self.foreign_key is not None:
            result['ForeignKey'] = self.foreign_key

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.partition_key is not None:
            result['PartitionKey'] = self.partition_key

        if self.position is not None:
            result['Position'] = self.position

        if self.primary_key is not None:
            result['PrimaryKey'] = self.primary_key

        if self.table_id is not None:
            result['TableId'] = self.table_id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessMetadata') is not None:
            temp_model = main_models.ColumnBusinessMetadata()
            self.business_metadata = temp_model.from_map(m.get('BusinessMetadata'))

        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('ForeignKey') is not None:
            self.foreign_key = m.get('ForeignKey')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PartitionKey') is not None:
            self.partition_key = m.get('PartitionKey')

        if m.get('Position') is not None:
            self.position = m.get('Position')

        if m.get('PrimaryKey') is not None:
            self.primary_key = m.get('PrimaryKey')

        if m.get('TableId') is not None:
            self.table_id = m.get('TableId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self



class ColumnBusinessMetadata(DaraModel):
    def __init__(
        self,
        description: str = None,
    ):
        self.description = description

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        return self

