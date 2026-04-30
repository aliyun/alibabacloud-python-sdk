# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class TableInstructionsVO(DaraModel):
    def __init__(
        self,
        asset_created_gmt: str = None,
        asset_description: str = None,
        asset_modified_gmt: str = None,
        db_id: int = None,
        db_type: str = None,
        summary: str = None,
        table_name: str = None,
    ):
        self.asset_created_gmt = asset_created_gmt
        self.asset_description = asset_description
        self.asset_modified_gmt = asset_modified_gmt
        self.db_id = db_id
        self.db_type = db_type
        self.summary = summary
        self.table_name = table_name

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

        if self.db_type is not None:
            result['DbType'] = self.db_type

        if self.summary is not None:
            result['Summary'] = self.summary

        if self.table_name is not None:
            result['TableName'] = self.table_name

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

        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')

        if m.get('Summary') is not None:
            self.summary = m.get('Summary')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        return self

