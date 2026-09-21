# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class GetWafFilterResponseBody(DaraModel):
    def __init__(
        self,
        filter: main_models.GetWafFilterResponseBodyFilter = None,
        request_id: str = None,
    ):
        # The matching engine configuration information returned.
        self.filter = filter
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.filter:
            self.filter.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.filter is not None:
            result['Filter'] = self.filter.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Filter') is not None:
            temp_model = main_models.GetWafFilterResponseBodyFilter()
            self.filter = temp_model.from_map(m.get('Filter'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetWafFilterResponseBodyFilter(DaraModel):
    def __init__(
        self,
        fields: List[main_models.GetWafFilterResponseBodyFilterFields] = None,
        phase: str = None,
        target: str = None,
        type: str = None,
    ):
        # The list that describes match objects and their properties.
        self.fields = fields
        # The phase in which WAF processes the request.
        self.phase = phase
        # The target value of the matching engine.
        self.target = target
        # The rule type.
        self.type = type

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
        result['Fields'] = []
        if self.fields is not None:
            for k1 in self.fields:
                result['Fields'].append(k1.to_map() if k1 else None)

        if self.phase is not None:
            result['Phase'] = self.phase

        if self.target is not None:
            result['Target'] = self.target

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.fields = []
        if m.get('Fields') is not None:
            for k1 in m.get('Fields'):
                temp_model = main_models.GetWafFilterResponseBodyFilterFields()
                self.fields.append(temp_model.from_map(k1))

        if m.get('Phase') is not None:
            self.phase = m.get('Phase')

        if m.get('Target') is not None:
            self.target = m.get('Target')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class GetWafFilterResponseBodyFilterFields(DaraModel):
    def __init__(
        self,
        enable: bool = None,
        key: str = None,
        label: str = None,
        logics: List[main_models.GetWafFilterResponseBodyFilterFieldsLogics] = None,
        min_plan: str = None,
        selector: main_models.GetWafFilterResponseBodyFilterFieldsSelector = None,
        sub: bool = None,
        sub_tip: str = None,
        subs: List[main_models.GetWafFilterResponseBodyFilterFieldsSubs] = None,
    ):
        # Indicates whether the current plan supports this match object.
        self.enable = enable
        # The parameter of the match object used internally by the system.
        self.key = key
        # The display label of the match object.
        self.label = label
        # The list of logical operator properties that define the logical conditions used for matching.
        self.logics = logics
        # The minimum plan that supports this match object, displayed when the current plan does not support it.
        self.min_plan = min_plan
        # The selector object that defines how to select the match object.
        self.selector = selector
        # Indicates whether the match object contains subfields.
        self.sub = sub
        # The hint provided to users about how to enter subfields.
        self.sub_tip = sub_tip
        # The enumerated sub-item list (dropdown subfields for grouped fields such as ali.websdk). Top-level match objects populate this list. Sub-items that are flat fields can be used directly as the left-hand side of an expression.
        self.subs = subs

    def validate(self):
        if self.logics:
            for v1 in self.logics:
                 if v1:
                    v1.validate()
        if self.selector:
            self.selector.validate()
        if self.subs:
            for v1 in self.subs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable is not None:
            result['Enable'] = self.enable

        if self.key is not None:
            result['Key'] = self.key

        if self.label is not None:
            result['Label'] = self.label

        result['Logics'] = []
        if self.logics is not None:
            for k1 in self.logics:
                result['Logics'].append(k1.to_map() if k1 else None)

        if self.min_plan is not None:
            result['MinPlan'] = self.min_plan

        if self.selector is not None:
            result['Selector'] = self.selector.to_map()

        if self.sub is not None:
            result['Sub'] = self.sub

        if self.sub_tip is not None:
            result['SubTip'] = self.sub_tip

        result['Subs'] = []
        if self.subs is not None:
            for k1 in self.subs:
                result['Subs'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Label') is not None:
            self.label = m.get('Label')

        self.logics = []
        if m.get('Logics') is not None:
            for k1 in m.get('Logics'):
                temp_model = main_models.GetWafFilterResponseBodyFilterFieldsLogics()
                self.logics.append(temp_model.from_map(k1))

        if m.get('MinPlan') is not None:
            self.min_plan = m.get('MinPlan')

        if m.get('Selector') is not None:
            temp_model = main_models.GetWafFilterResponseBodyFilterFieldsSelector()
            self.selector = temp_model.from_map(m.get('Selector'))

        if m.get('Sub') is not None:
            self.sub = m.get('Sub')

        if m.get('SubTip') is not None:
            self.sub_tip = m.get('SubTip')

        self.subs = []
        if m.get('Subs') is not None:
            for k1 in m.get('Subs'):
                temp_model = main_models.GetWafFilterResponseBodyFilterFieldsSubs()
                self.subs.append(temp_model.from_map(k1))

        return self

class GetWafFilterResponseBodyFilterFieldsSubs(DaraModel):
    def __init__(
        self,
        enable: bool = None,
        key: str = None,
        label: str = None,
        logics: List[main_models.GetWafFilterResponseBodyFilterFieldsSubsLogics] = None,
        min_plan: str = None,
    ):
        # Indicates whether the current plan supports this match object.
        self.enable = enable
        # The parameter of the sub-item match object.
        self.key = key
        # The display label of the sub-item match object.
        self.label = label
        # The list of logical operator properties applicable to the sub-item (same structure as the parent Logics).
        self.logics = logics
        # The minimum plan that supports this match object, displayed when the current plan does not support it.
        self.min_plan = min_plan

    def validate(self):
        if self.logics:
            for v1 in self.logics:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable is not None:
            result['Enable'] = self.enable

        if self.key is not None:
            result['Key'] = self.key

        if self.label is not None:
            result['Label'] = self.label

        result['Logics'] = []
        if self.logics is not None:
            for k1 in self.logics:
                result['Logics'].append(k1.to_map() if k1 else None)

        if self.min_plan is not None:
            result['MinPlan'] = self.min_plan

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Label') is not None:
            self.label = m.get('Label')

        self.logics = []
        if m.get('Logics') is not None:
            for k1 in m.get('Logics'):
                temp_model = main_models.GetWafFilterResponseBodyFilterFieldsSubsLogics()
                self.logics.append(temp_model.from_map(k1))

        if m.get('MinPlan') is not None:
            self.min_plan = m.get('MinPlan')

        return self

class GetWafFilterResponseBodyFilterFieldsSubsLogics(DaraModel):
    def __init__(
        self,
        attributes: int = None,
        enable: bool = None,
        kind: str = None,
        min_plan: str = None,
        negative: bool = None,
        operator: str = None,
        symbol: str = None,
        tip: str = None,
        type: str = None,
        validator: main_models.GetWafFilterResponseBodyFilterFieldsSubsLogicsValidator = None,
    ):
        # The field attributes.
        self.attributes = attributes
        # Indicates whether the current plan supports this match operator.
        self.enable = enable
        # The type of the value input field. Valid values:
        # * select:single: single-select input field
        # * select:multi: multi-select input field
        # * input:single: single input field
        # * input:multi: multi input field
        self.kind = kind
        # The minimum plan that supports this match operator, displayed when the current plan does not support it.
        self.min_plan = min_plan
        # Indicates whether the match result is negated.
        self.negative = negative
        # The display label of the match operator.
        self.operator = operator
        # The parameter of the match operator used internally by the system.
        self.symbol = symbol
        # The input hint that helps users provide valid values required by the rule.
        self.tip = tip
        # The type of the value. Valid values:
        # * integer: integer
        # * integer_slice: integer array
        # * string: string
        # * string_slice: string array
        self.type = type
        # The validator object that defines the validation rules for values.
        self.validator = validator

    def validate(self):
        if self.validator:
            self.validator.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attributes is not None:
            result['Attributes'] = self.attributes

        if self.enable is not None:
            result['Enable'] = self.enable

        if self.kind is not None:
            result['Kind'] = self.kind

        if self.min_plan is not None:
            result['MinPlan'] = self.min_plan

        if self.negative is not None:
            result['Negative'] = self.negative

        if self.operator is not None:
            result['Operator'] = self.operator

        if self.symbol is not None:
            result['Symbol'] = self.symbol

        if self.tip is not None:
            result['Tip'] = self.tip

        if self.type is not None:
            result['Type'] = self.type

        if self.validator is not None:
            result['Validator'] = self.validator.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')

        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('Kind') is not None:
            self.kind = m.get('Kind')

        if m.get('MinPlan') is not None:
            self.min_plan = m.get('MinPlan')

        if m.get('Negative') is not None:
            self.negative = m.get('Negative')

        if m.get('Operator') is not None:
            self.operator = m.get('Operator')

        if m.get('Symbol') is not None:
            self.symbol = m.get('Symbol')

        if m.get('Tip') is not None:
            self.tip = m.get('Tip')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Validator') is not None:
            temp_model = main_models.GetWafFilterResponseBodyFilterFieldsSubsLogicsValidator()
            self.validator = temp_model.from_map(m.get('Validator'))

        return self

class GetWafFilterResponseBodyFilterFieldsSubsLogicsValidator(DaraModel):
    def __init__(
        self,
        err_msg: str = None,
        length: main_models.WafQuotaInteger = None,
        pattern: str = None,
        range: main_models.WafQuotaInteger = None,
    ):
        # The error message returned when validation fails.
        self.err_msg = err_msg
        # The length limit of the value.
        self.length = length
        # The regular expression pattern for the value, used for string validation.
        self.pattern = pattern
        # The numeric range of the value, used for number validation.
        self.range = range

    def validate(self):
        if self.length:
            self.length.validate()
        if self.range:
            self.range.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg

        if self.length is not None:
            result['Length'] = self.length.to_map()

        if self.pattern is not None:
            result['Pattern'] = self.pattern

        if self.range is not None:
            result['Range'] = self.range.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')

        if m.get('Length') is not None:
            temp_model = main_models.WafQuotaInteger()
            self.length = temp_model.from_map(m.get('Length'))

        if m.get('Pattern') is not None:
            self.pattern = m.get('Pattern')

        if m.get('Range') is not None:
            temp_model = main_models.WafQuotaInteger()
            self.range = temp_model.from_map(m.get('Range'))

        return self

class GetWafFilterResponseBodyFilterFieldsSelector(DaraModel):
    def __init__(
        self,
        data: List[main_models.GetWafFilterResponseBodyFilterFieldsSelectorData] = None,
        kind: str = None,
    ):
        # The list of available data when the selector kind is data.
        self.data = data
        # The kind of the selector, such as whether it is used for selecting data items or other purposes.
        self.kind = kind

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.kind is not None:
            result['Kind'] = self.kind

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.GetWafFilterResponseBodyFilterFieldsSelectorData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Kind') is not None:
            self.kind = m.get('Kind')

        return self

class GetWafFilterResponseBodyFilterFieldsSelectorData(DaraModel):
    def __init__(
        self,
        label: str = None,
        value: str = None,
    ):
        # The display label of the available data.
        self.label = label
        # The parameter value of the available data.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.label is not None:
            result['Label'] = self.label

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetWafFilterResponseBodyFilterFieldsLogics(DaraModel):
    def __init__(
        self,
        attributes: int = None,
        enable: bool = None,
        kind: str = None,
        min_plan: str = None,
        negative: bool = None,
        operator: str = None,
        symbol: str = None,
        tip: str = None,
        type: str = None,
        validator: main_models.GetWafFilterResponseBodyFilterFieldsLogicsValidator = None,
    ):
        # The configurable attributes, such as whether the match is case-sensitive.
        self.attributes = attributes
        # Indicates whether the current plan supports this match operator.
        self.enable = enable
        # The type of the value input field. Valid values:
        # * select:single: single-select input field
        # * select:multi: multi-select input field
        # * input:single: single input field
        # * input:multi: multi input field
        self.kind = kind
        # The minimum plan that supports this match operator, displayed when the current plan does not support it.
        self.min_plan = min_plan
        # Indicates whether the match result is negated.
        self.negative = negative
        # The display label of the match operator.
        self.operator = operator
        # The parameter of the match operator used internally by the system.
        self.symbol = symbol
        # The input hint that helps users provide valid values required by the rule.
        self.tip = tip
        # The type of the value. Valid values:
        # * integer: integer
        # * integer_slice: integer array
        # * string: string
        # * string_slice: string array
        self.type = type
        # The validator object that defines the validation rules for values.
        self.validator = validator

    def validate(self):
        if self.validator:
            self.validator.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attributes is not None:
            result['Attributes'] = self.attributes

        if self.enable is not None:
            result['Enable'] = self.enable

        if self.kind is not None:
            result['Kind'] = self.kind

        if self.min_plan is not None:
            result['MinPlan'] = self.min_plan

        if self.negative is not None:
            result['Negative'] = self.negative

        if self.operator is not None:
            result['Operator'] = self.operator

        if self.symbol is not None:
            result['Symbol'] = self.symbol

        if self.tip is not None:
            result['Tip'] = self.tip

        if self.type is not None:
            result['Type'] = self.type

        if self.validator is not None:
            result['Validator'] = self.validator.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')

        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('Kind') is not None:
            self.kind = m.get('Kind')

        if m.get('MinPlan') is not None:
            self.min_plan = m.get('MinPlan')

        if m.get('Negative') is not None:
            self.negative = m.get('Negative')

        if m.get('Operator') is not None:
            self.operator = m.get('Operator')

        if m.get('Symbol') is not None:
            self.symbol = m.get('Symbol')

        if m.get('Tip') is not None:
            self.tip = m.get('Tip')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Validator') is not None:
            temp_model = main_models.GetWafFilterResponseBodyFilterFieldsLogicsValidator()
            self.validator = temp_model.from_map(m.get('Validator'))

        return self

class GetWafFilterResponseBodyFilterFieldsLogicsValidator(DaraModel):
    def __init__(
        self,
        err_msg: str = None,
        length: main_models.WafQuotaInteger = None,
        pattern: str = None,
        range: main_models.WafQuotaInteger = None,
    ):
        # The error message returned when validation fails.
        self.err_msg = err_msg
        # The length limit of the value.
        self.length = length
        # The regular expression pattern for the value, used for string validation.
        self.pattern = pattern
        # The numeric range of the value, used for number validation.
        self.range = range

    def validate(self):
        if self.length:
            self.length.validate()
        if self.range:
            self.range.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg

        if self.length is not None:
            result['Length'] = self.length.to_map()

        if self.pattern is not None:
            result['Pattern'] = self.pattern

        if self.range is not None:
            result['Range'] = self.range.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')

        if m.get('Length') is not None:
            temp_model = main_models.WafQuotaInteger()
            self.length = temp_model.from_map(m.get('Length'))

        if m.get('Pattern') is not None:
            self.pattern = m.get('Pattern')

        if m.get('Range') is not None:
            temp_model = main_models.WafQuotaInteger()
            self.range = temp_model.from_map(m.get('Range'))

        return self

