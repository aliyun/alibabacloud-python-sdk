# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ColumnKnowledgeInfo(DaraModel):
    def __init__(
        self,
        asset_description: str = None,
        asset_modified_gmt: str = None,
        column_name: str = None,
        column_type: str = None,
        description: str = None,
        position: int = None,
    ):
        self.asset_description = asset_description
        self.asset_modified_gmt = asset_modified_gmt
        self.column_name = column_name
        self.column_type = column_type
        self.description = description
        self.position = position

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.asset_description is not None:
            result['AssetDescription'] = self.asset_description

        if self.asset_modified_gmt is not None:
            result['AssetModifiedGmt'] = self.asset_modified_gmt

        if self.column_name is not None:
            result['ColumnName'] = self.column_name

        if self.column_type is not None:
            result['ColumnType'] = self.column_type

        if self.description is not None:
            result['Description'] = self.description

        if self.position is not None:
            result['Position'] = self.position

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssetDescription') is not None:
            self.asset_description = m.get('AssetDescription')

        if m.get('AssetModifiedGmt') is not None:
            self.asset_modified_gmt = m.get('AssetModifiedGmt')

        if m.get('ColumnName') is not None:
            self.column_name = m.get('ColumnName')

        if m.get('ColumnType') is not None:
            self.column_type = m.get('ColumnType')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Position') is not None:
            self.position = m.get('Position')

        return self

