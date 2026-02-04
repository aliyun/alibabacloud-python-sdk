# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dcdn20180115 import models as main_models
from darabonba.model import DaraModel

class DescribeDcdnWafFilterInfoResponseBody(DaraModel):
    def __init__(
        self,
        content: List[main_models.DescribeDcdnWafFilterInfoResponseBodyContent] = None,
        request_id: str = None,
    ):
        # The returned information.
        self.content = content
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.content:
            for v1 in self.content:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Content'] = []
        if self.content is not None:
            for k1 in self.content:
                result['Content'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.content = []
        if m.get('Content') is not None:
            for k1 in m.get('Content'):
                temp_model = main_models.DescribeDcdnWafFilterInfoResponseBodyContent()
                self.content.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDcdnWafFilterInfoResponseBodyContent(DaraModel):
    def __init__(
        self,
        defense_scene: str = None,
        fields: List[main_models.DescribeDcdnWafFilterInfoResponseBodyContentFields] = None,
    ):
        # The type of the protection policy. The value of this parameter is the same as that of the DefenseScenes parameter in the request.
        self.defense_scene = defense_scene
        # The information about the match condition.
        self.fields = fields

    def validate(self):
        if self.fields:
            for v1 in self.fields:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.defense_scene is not None:
            result['DefenseScene'] = self.defense_scene

        result['Fields'] = []
        if self.fields is not None:
            for k1 in self.fields:
                result['Fields'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefenseScene') is not None:
            self.defense_scene = m.get('DefenseScene')

        self.fields = []
        if m.get('Fields') is not None:
            for k1 in m.get('Fields'):
                temp_model = main_models.DescribeDcdnWafFilterInfoResponseBodyContentFields()
                self.fields.append(temp_model.from_map(k1))

        return self

class DescribeDcdnWafFilterInfoResponseBodyContentFields(DaraModel):
    def __init__(
        self,
        extend_field: str = None,
        logical_symbol: List[main_models.DescribeDcdnWafFilterInfoResponseBodyContentFieldsLogicalSymbol] = None,
        match_field: str = None,
    ):
        # The description of the match field. This parameter is not returned or is empty if no match fields are found.
        self.extend_field = extend_field
        # The information about the logical symbol.
        self.logical_symbol = logical_symbol
        # The match field.
        self.match_field = match_field

    def validate(self):
        if self.logical_symbol:
            for v1 in self.logical_symbol:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.extend_field is not None:
            result['ExtendField'] = self.extend_field

        result['LogicalSymbol'] = []
        if self.logical_symbol is not None:
            for k1 in self.logical_symbol:
                result['LogicalSymbol'].append(k1.to_map() if k1 else None)

        if self.match_field is not None:
            result['MatchField'] = self.match_field

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExtendField') is not None:
            self.extend_field = m.get('ExtendField')

        self.logical_symbol = []
        if m.get('LogicalSymbol') is not None:
            for k1 in m.get('LogicalSymbol'):
                temp_model = main_models.DescribeDcdnWafFilterInfoResponseBodyContentFieldsLogicalSymbol()
                self.logical_symbol.append(temp_model.from_map(k1))

        if m.get('MatchField') is not None:
            self.match_field = m.get('MatchField')

        return self

class DescribeDcdnWafFilterInfoResponseBodyContentFieldsLogicalSymbol(DaraModel):
    def __init__(
        self,
        attributes: int = None,
        description: str = None,
        max_length: int = None,
        regexp: main_models.DescribeDcdnWafFilterInfoResponseBodyContentFieldsLogicalSymbolRegexp = None,
        symbol: str = None,
        tip: str = None,
        type: str = None,
    ):
        # The configurable attributes, which are bit-field variables that are shown in the following list.\\
        # For example, 1(00000001) indicates that case sensitivity can be enabled and stream match cannot be enabled, and 3(00000011) indicates that case sensitivity and stream match can be enabled.
        # 
        # *   Bit (low to high) - Description
        # *   1 - Case sensitivity
        # *   2 - Stream match
        self.attributes = attributes
        # The logical symbol that is displayed in the Dynamic Content Delivery Network (DCDN) console.
        self.description = description
        # The maximum number of match items that can be returned. The value of this parameter varies based on the value of the Type parameter. Valid values:
        # 
        # *   If **multi** is returned for the Type parameter, the value of this parameter indicates the maximum number of match items.
        # *   If **single** is returned for the Type parameter, the value of this parameter is 1.
        # *   If **none** is returned for the Type parameter, the value of this parameter is 0.
        self.max_length = max_length
        # The information about the regular expression.
        self.regexp = regexp
        # The logical symbol that is passed to the backend.
        self.symbol = symbol
        # The tips that are displayed in the match item.
        self.tip = tip
        # The number of match items. Valid values:
        # 
        # *   multi: You can specify multiple match items.
        # *   single: You can specify only a match item.
        # *   none: no match items.
        self.type = type

    def validate(self):
        if self.regexp:
            self.regexp.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attributes is not None:
            result['Attributes'] = self.attributes

        if self.description is not None:
            result['Description'] = self.description

        if self.max_length is not None:
            result['MaxLength'] = self.max_length

        if self.regexp is not None:
            result['Regexp'] = self.regexp.to_map()

        if self.symbol is not None:
            result['Symbol'] = self.symbol

        if self.tip is not None:
            result['Tip'] = self.tip

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('MaxLength') is not None:
            self.max_length = m.get('MaxLength')

        if m.get('Regexp') is not None:
            temp_model = main_models.DescribeDcdnWafFilterInfoResponseBodyContentFieldsLogicalSymbolRegexp()
            self.regexp = temp_model.from_map(m.get('Regexp'))

        if m.get('Symbol') is not None:
            self.symbol = m.get('Symbol')

        if m.get('Tip') is not None:
            self.tip = m.get('Tip')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class DescribeDcdnWafFilterInfoResponseBodyContentFieldsLogicalSymbolRegexp(DaraModel):
    def __init__(
        self,
        err_msg: str = None,
        pattern: str = None,
    ):
        # The error message returned when no items match the regular expression.
        self.err_msg = err_msg
        # The regular expression.
        self.pattern = pattern

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg

        if self.pattern is not None:
            result['Pattern'] = self.pattern

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')

        if m.get('Pattern') is not None:
            self.pattern = m.get('Pattern')

        return self

