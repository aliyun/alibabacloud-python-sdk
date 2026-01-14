# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_quickbi_public20220101 import models as main_models
from darabonba.model import DaraModel

class SmartqQueryAbilityResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: main_models.SmartqQueryAbilityResponseBodyResult = None,
        success: bool = None,
    ):
        # Request ID.
        self.request_id = request_id
        # Return result.
        self.result = result
        # Whether the operation was successful.
        # 
        # This parameter is required.
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result is not None:
            result['Result'] = self.result.to_map()

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            temp_model = main_models.SmartqQueryAbilityResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class SmartqQueryAbilityResponseBodyResult(DaraModel):
    def __init__(
        self,
        chart_type: str = None,
        conclusion_text: str = None,
        data_list: List[str] = None,
        logic_sql: str = None,
        meta_type: List[main_models.SmartqQueryAbilityResponseBodyResultMetaType] = None,
        values: List[main_models.SmartqQueryAbilityResponseBodyResultValues] = None,
    ):
        # Suggested chart type.
        self.chart_type = chart_type
        # Summary information.
        self.conclusion_text = conclusion_text
        self.data_list = data_list
        # Visualized logical SQL.
        self.logic_sql = logic_sql
        # List of column tuple types.
        self.meta_type = meta_type
        # Array of data value lists.
        self.values = values

    def validate(self):
        if self.meta_type:
            for v1 in self.meta_type:
                 if v1:
                    v1.validate()
        if self.values:
            for v1 in self.values:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.chart_type is not None:
            result['ChartType'] = self.chart_type

        if self.conclusion_text is not None:
            result['ConclusionText'] = self.conclusion_text

        if self.data_list is not None:
            result['DataList'] = self.data_list

        if self.logic_sql is not None:
            result['LogicSql'] = self.logic_sql

        result['MetaType'] = []
        if self.meta_type is not None:
            for k1 in self.meta_type:
                result['MetaType'].append(k1.to_map() if k1 else None)

        result['Values'] = []
        if self.values is not None:
            for k1 in self.values:
                result['Values'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChartType') is not None:
            self.chart_type = m.get('ChartType')

        if m.get('ConclusionText') is not None:
            self.conclusion_text = m.get('ConclusionText')

        if m.get('DataList') is not None:
            self.data_list = m.get('DataList')

        if m.get('LogicSql') is not None:
            self.logic_sql = m.get('LogicSql')

        self.meta_type = []
        if m.get('MetaType') is not None:
            for k1 in m.get('MetaType'):
                temp_model = main_models.SmartqQueryAbilityResponseBodyResultMetaType()
                self.meta_type.append(temp_model.from_map(k1))

        self.values = []
        if m.get('Values') is not None:
            for k1 in m.get('Values'):
                temp_model = main_models.SmartqQueryAbilityResponseBodyResultValues()
                self.values.append(temp_model.from_map(k1))

        return self

class SmartqQueryAbilityResponseBodyResultValues(DaraModel):
    def __init__(
        self,
        row: List[str] = None,
    ):
        # Data values for each row.
        self.row = row

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.row is not None:
            result['Row'] = self.row

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Row') is not None:
            self.row = m.get('Row')

        return self

class SmartqQueryAbilityResponseBodyResultMetaType(DaraModel):
    def __init__(
        self,
        key: str = None,
        type: str = None,
        value: str = None,
    ):
        # Column tuple name.
        self.key = key
        self.type = type
        # Column tuple type.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.type is not None:
            result['Type'] = self.type

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

