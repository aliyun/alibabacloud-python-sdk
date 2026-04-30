# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class TableKnowledgeVO(DaraModel):
    def __init__(
        self,
        asset_created_gmt: str = None,
        asset_description: str = None,
        asset_modified_gmt: str = None,
        db_id: int = None,
        db_name: str = None,
        db_type: str = None,
        description: str = None,
        env_type: str = None,
        hot_level: int = None,
        instance_id: int = None,
        instance_name: str = None,
        level: int = None,
        level_type: str = None,
        logic: bool = None,
        num_rows: int = None,
        schema_name: str = None,
        size: int = None,
        summary: str = None,
        table_id: int = None,
        table_name: str = None,
        title: str = None,
    ):
        self.asset_created_gmt = asset_created_gmt
        self.asset_description = asset_description
        self.asset_modified_gmt = asset_modified_gmt
        self.db_id = db_id
        self.db_name = db_name
        self.db_type = db_type
        self.description = description
        self.env_type = env_type
        self.hot_level = hot_level
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.level = level
        self.level_type = level_type
        self.logic = logic
        self.num_rows = num_rows
        self.schema_name = schema_name
        self.size = size
        self.summary = summary
        self.table_id = table_id
        self.table_name = table_name
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.asset_created_gmt is not None:
            result['AssetCreatedGmt'] = self.asset_created_gmt

        if self.asset_description is not None:
            result['AssetDescription'] = self.asset_description

        if self.asset_modified_gmt is not None:
            result['AssetModifiedGmt'] = self.asset_modified_gmt

        if self.db_id is not None:
            result['DbId'] = self.db_id

        if self.db_name is not None:
            result['DbName'] = self.db_name

        if self.db_type is not None:
            result['DbType'] = self.db_type

        if self.description is not None:
            result['Description'] = self.description

        if self.env_type is not None:
            result['EnvType'] = self.env_type

        if self.hot_level is not None:
            result['HotLevel'] = self.hot_level

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.level is not None:
            result['Level'] = self.level

        if self.level_type is not None:
            result['LevelType'] = self.level_type

        if self.logic is not None:
            result['Logic'] = self.logic

        if self.num_rows is not None:
            result['NumRows'] = self.num_rows

        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name

        if self.size is not None:
            result['Size'] = self.size

        if self.summary is not None:
            result['Summary'] = self.summary

        if self.table_id is not None:
            result['TableId'] = self.table_id

        if self.table_name is not None:
            result['TableName'] = self.table_name

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssetCreatedGmt') is not None:
            self.asset_created_gmt = m.get('AssetCreatedGmt')

        if m.get('AssetDescription') is not None:
            self.asset_description = m.get('AssetDescription')

        if m.get('AssetModifiedGmt') is not None:
            self.asset_modified_gmt = m.get('AssetModifiedGmt')

        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')

        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')

        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')

        if m.get('HotLevel') is not None:
            self.hot_level = m.get('HotLevel')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('LevelType') is not None:
            self.level_type = m.get('LevelType')

        if m.get('Logic') is not None:
            self.logic = m.get('Logic')

        if m.get('NumRows') is not None:
            self.num_rows = m.get('NumRows')

        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('Summary') is not None:
            self.summary = m.get('Summary')

        if m.get('TableId') is not None:
            self.table_id = m.get('TableId')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

