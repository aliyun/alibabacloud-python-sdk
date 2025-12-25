# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class TableKnowledgeInfo(DaraModel):
    def __init__(
        self,
        asset_description: str = None,
        asset_modified_gmt: str = None,
        column_list: List[main_models.ColumnKnowledgeInfo] = None,
        description: str = None,
        summary: str = None,
        table_name: str = None,
    ):
        self.asset_description = asset_description
        self.asset_modified_gmt = asset_modified_gmt
        self.column_list = column_list
        self.description = description
        self.summary = summary
        self.table_name = table_name

    def validate(self):
        if self.column_list:
            for v1 in self.column_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.asset_description is not None:
            result['AssetDescription'] = self.asset_description

        if self.asset_modified_gmt is not None:
            result['AssetModifiedGmt'] = self.asset_modified_gmt

        result['ColumnList'] = []
        if self.column_list is not None:
            for k1 in self.column_list:
                result['ColumnList'].append(k1.to_map() if k1 else None)

        if self.description is not None:
            result['Description'] = self.description

        if self.summary is not None:
            result['Summary'] = self.summary

        if self.table_name is not None:
            result['TableName'] = self.table_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssetDescription') is not None:
            self.asset_description = m.get('AssetDescription')

        if m.get('AssetModifiedGmt') is not None:
            self.asset_modified_gmt = m.get('AssetModifiedGmt')

        self.column_list = []
        if m.get('ColumnList') is not None:
            for k1 in m.get('ColumnList'):
                temp_model = main_models.ColumnKnowledgeInfo()
                self.column_list.append(temp_model.from_map(k1))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Summary') is not None:
            self.summary = m.get('Summary')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        return self

