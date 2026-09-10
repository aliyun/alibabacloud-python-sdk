# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_lhm20250116 import models as main_models
from darabonba.model import DaraModel

class AddDataCheckTemplateRequest(DaraModel):
    def __init__(
        self,
        basic_metric_rules: List[main_models.AddDataCheckTemplateRequestBasicMetricRules] = None,
        check_type: int = None,
        complex_metric_rules: List[main_models.AddDataCheckTemplateRequestComplexMetricRules] = None,
        ds_engine_rels: List[main_models.AddDataCheckTemplateRequestDsEngineRels] = None,
        fulltext_rule: main_models.AddDataCheckTemplateRequestFulltextRule = None,
        metric_rules: List[main_models.AddDataCheckTemplateRequestMetricRules] = None,
        null_rules: List[main_models.AddDataCheckTemplateRequestNullRules] = None,
        request_id: str = None,
        template_desc: str = None,
        template_name: str = None,
        tenant_id: str = None,
        weak_content_rule: main_models.AddDataCheckTemplateRequestWeakContentRule = None,
    ):
        # The list of metric verification rules for basic data types. This field is required when checkType is set to 1 (metric comparison).
        self.basic_metric_rules = basic_metric_rules
        # The verification rule type. Valid values:
        # - 0: data volume comparison.
        # - 1: metric comparison.
        # - 2: weak content comparison.
        # - 3: custom comparison.
        # - 4: full-text comparison.
        # - 5: null rate comparison.
        self.check_type = check_type
        # The list of check rules for complex data type metrics. Used when checkType is set to 1 (metric comparison).
        self.complex_metric_rules = complex_metric_rules
        # The list of datasource engine relationships (datasource engines associated with the template).
        self.ds_engine_rels = ds_engine_rels
        # The full-text comparison rule. This parameter has a value when checkType is set to 4 (full-text comparison). For the field structure, see the child field descriptions.
        self.fulltext_rule = fulltext_rule
        # The list of metric check rules. This parameter has a value when checkType is set to 1 (metric comparison).
        self.metric_rules = metric_rules
        # The list of null value rate check rules. This parameter has a value when checkType is set to 5 (null value rate comparison).
        self.null_rules = null_rules
        # The request ID, which is used to locate and troubleshoot issues of this call.
        self.request_id = request_id
        # The template description.
        self.template_desc = template_desc
        # The name of the check template.
        self.template_name = template_name
        # The tenant ID.
        self.tenant_id = tenant_id
        # The weak content check rule. This parameter has a value and is required when checkType is set to 2 (weak content comparison). For the field structure, refer to the child field descriptions below.
        self.weak_content_rule = weak_content_rule

    def validate(self):
        if self.basic_metric_rules:
            for v1 in self.basic_metric_rules:
                 if v1:
                    v1.validate()
        if self.complex_metric_rules:
            for v1 in self.complex_metric_rules:
                 if v1:
                    v1.validate()
        if self.ds_engine_rels:
            for v1 in self.ds_engine_rels:
                 if v1:
                    v1.validate()
        if self.fulltext_rule:
            self.fulltext_rule.validate()
        if self.metric_rules:
            for v1 in self.metric_rules:
                 if v1:
                    v1.validate()
        if self.null_rules:
            for v1 in self.null_rules:
                 if v1:
                    v1.validate()
        if self.weak_content_rule:
            self.weak_content_rule.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['basicMetricRules'] = []
        if self.basic_metric_rules is not None:
            for k1 in self.basic_metric_rules:
                result['basicMetricRules'].append(k1.to_map() if k1 else None)

        if self.check_type is not None:
            result['checkType'] = self.check_type

        result['complexMetricRules'] = []
        if self.complex_metric_rules is not None:
            for k1 in self.complex_metric_rules:
                result['complexMetricRules'].append(k1.to_map() if k1 else None)

        result['dsEngineRels'] = []
        if self.ds_engine_rels is not None:
            for k1 in self.ds_engine_rels:
                result['dsEngineRels'].append(k1.to_map() if k1 else None)

        if self.fulltext_rule is not None:
            result['fulltextRule'] = self.fulltext_rule.to_map()

        result['metricRules'] = []
        if self.metric_rules is not None:
            for k1 in self.metric_rules:
                result['metricRules'].append(k1.to_map() if k1 else None)

        result['nullRules'] = []
        if self.null_rules is not None:
            for k1 in self.null_rules:
                result['nullRules'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.template_desc is not None:
            result['templateDesc'] = self.template_desc

        if self.template_name is not None:
            result['templateName'] = self.template_name

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        if self.weak_content_rule is not None:
            result['weakContentRule'] = self.weak_content_rule.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.basic_metric_rules = []
        if m.get('basicMetricRules') is not None:
            for k1 in m.get('basicMetricRules'):
                temp_model = main_models.AddDataCheckTemplateRequestBasicMetricRules()
                self.basic_metric_rules.append(temp_model.from_map(k1))

        if m.get('checkType') is not None:
            self.check_type = m.get('checkType')

        self.complex_metric_rules = []
        if m.get('complexMetricRules') is not None:
            for k1 in m.get('complexMetricRules'):
                temp_model = main_models.AddDataCheckTemplateRequestComplexMetricRules()
                self.complex_metric_rules.append(temp_model.from_map(k1))

        self.ds_engine_rels = []
        if m.get('dsEngineRels') is not None:
            for k1 in m.get('dsEngineRels'):
                temp_model = main_models.AddDataCheckTemplateRequestDsEngineRels()
                self.ds_engine_rels.append(temp_model.from_map(k1))

        if m.get('fulltextRule') is not None:
            temp_model = main_models.AddDataCheckTemplateRequestFulltextRule()
            self.fulltext_rule = temp_model.from_map(m.get('fulltextRule'))

        self.metric_rules = []
        if m.get('metricRules') is not None:
            for k1 in m.get('metricRules'):
                temp_model = main_models.AddDataCheckTemplateRequestMetricRules()
                self.metric_rules.append(temp_model.from_map(k1))

        self.null_rules = []
        if m.get('nullRules') is not None:
            for k1 in m.get('nullRules'):
                temp_model = main_models.AddDataCheckTemplateRequestNullRules()
                self.null_rules.append(temp_model.from_map(k1))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('templateDesc') is not None:
            self.template_desc = m.get('templateDesc')

        if m.get('templateName') is not None:
            self.template_name = m.get('templateName')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        if m.get('weakContentRule') is not None:
            temp_model = main_models.AddDataCheckTemplateRequestWeakContentRule()
            self.weak_content_rule = temp_model.from_map(m.get('weakContentRule'))

        return self

class AddDataCheckTemplateRequestWeakContentRule(DaraModel):
    def __init__(
        self,
        filter_column_expression: str = None,
        filter_column_types: List[str] = None,
        rule_id: str = None,
        weak_content_algorithm: str = None,
    ):
        # The filter column name expression.
        self.filter_column_expression = filter_column_expression
        # The filter column types, separated by vertical bars (|).
        self.filter_column_types = filter_column_types
        # The rule ID that uniquely identifies a verification rule.
        self.rule_id = rule_id
        # The weak content algorithm name: md5 or crc32.
        self.weak_content_algorithm = weak_content_algorithm

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.filter_column_expression is not None:
            result['filterColumnExpression'] = self.filter_column_expression

        if self.filter_column_types is not None:
            result['filterColumnTypes'] = self.filter_column_types

        if self.rule_id is not None:
            result['ruleId'] = self.rule_id

        if self.weak_content_algorithm is not None:
            result['weakContentAlgorithm'] = self.weak_content_algorithm

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('filterColumnExpression') is not None:
            self.filter_column_expression = m.get('filterColumnExpression')

        if m.get('filterColumnTypes') is not None:
            self.filter_column_types = m.get('filterColumnTypes')

        if m.get('ruleId') is not None:
            self.rule_id = m.get('ruleId')

        if m.get('weakContentAlgorithm') is not None:
            self.weak_content_algorithm = m.get('weakContentAlgorithm')

        return self

class AddDataCheckTemplateRequestNullRules(DaraModel):
    def __init__(
        self,
        data_type_group: int = None,
        null_values: str = None,
        rule_id: str = None,
    ):
        # The data type group that identifies the data type category to which the verification rule applies. Valid values: integers from 0 to 7. For the description of each value, see the enumeration values.
        self.data_type_group = data_type_group
        # The null value definitions, stored in JSON format.
        self.null_values = null_values
        # The rule ID that uniquely identifies a verification rule.
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_type_group is not None:
            result['dataTypeGroup'] = self.data_type_group

        if self.null_values is not None:
            result['nullValues'] = self.null_values

        if self.rule_id is not None:
            result['ruleId'] = self.rule_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dataTypeGroup') is not None:
            self.data_type_group = m.get('dataTypeGroup')

        if m.get('nullValues') is not None:
            self.null_values = m.get('nullValues')

        if m.get('ruleId') is not None:
            self.rule_id = m.get('ruleId')

        return self

class AddDataCheckTemplateRequestMetricRules(DaraModel):
    def __init__(
        self,
        check_methods: str = None,
        control_float_precision: int = None,
        data_type_classify: int = None,
        data_type_group: int = None,
        data_type_list: List[str] = None,
        data_types: str = None,
        diff_tolerate_type: int = None,
        diff_tolerate_values: Dict[str, Any] = None,
        enable_decimal_scale: int = None,
        filter_column_name: str = None,
        filter_columns: str = None,
        float_precision: int = None,
        ignore_decimal_diff: int = None,
        ignore_decimal_scale_suffix_zero: int = None,
        ignore_empty_diff: int = None,
        ignore_numeric_zero: int = None,
        ignore_string_empty: int = None,
        ignore_zero_diff: int = None,
        is_count_check: int = None,
        rule_id: str = None,
        set_decimal_scale: int = None,
    ):
        # The check methods (metric calculation methods). Separate multiple values with commas, such as SUM,AVG,MIN,MAX. The values must be within the range allowed by the templatetype.
        self.check_methods = check_methods
        # Specifies whether to control floating-point precision. Valid values: 0 (no) and 1 (yes).
        self.control_float_precision = control_float_precision
        # The data type category. Valid values: 0 (native data type) and 1 (composite data type).
        self.data_type_classify = data_type_classify
        # The data type group that identifies the data type category to which the verification rule applies. Valid values: integers from 0 to 7. For the description of each value, see the enumeration values.
        self.data_type_group = data_type_group
        # The list of data types to which the verification rule applies. Configure this field based on your requirements.
        self.data_type_list = data_type_list
        # The data types. Configure this field based on your requirements.
        self.data_types = data_types
        # The difference tolerance rate type. Valid values: 0 (unified) and 1 (custom). Default value: 0.
        self.diff_tolerate_type = diff_tolerate_type
        # The difference tolerance rate values. For the unified type, specify one value, such as {"SAME": 0}. For the custom type, specify a value for each tolerance type, such as {"SUM": 0.01, "AVG": 0.001}.
        self.diff_tolerate_values = diff_tolerate_values
        # Specifies whether to enable decimal scale control for DECIMAL type comparison. Valid values: 0 (no) and 1 (yes).
        self.enable_decimal_scale = enable_decimal_scale
        # The filter field names, separated by commas (,).
        self.filter_column_name = filter_column_name
        # **[Deprecated]** Use the filterColumnName field instead. This field is retained for backward compatibility.
        self.filter_columns = filter_columns
        # The number of decimal places for floating-point values.
        self.float_precision = float_precision
        # Specifies whether to ignore trailing zero differences in decimal parts. Valid values: 0 (no) and 1 (yes).
        self.ignore_decimal_diff = ignore_decimal_diff
        # Specifies whether to ignore trailing zeros in the decimal scale for DECIMAL type comparison. Valid values: 0 (no) and 1 (yes).
        self.ignore_decimal_scale_suffix_zero = ignore_decimal_scale_suffix_zero
        # Specifies whether to ignore differences between null values and empty strings. Valid values: 0 (no) and 1 (yes).
        self.ignore_empty_diff = ignore_empty_diff
        # Specifies whether to ignore zero values for numeric types. Valid values: 0 (no) and 1 (yes).
        self.ignore_numeric_zero = ignore_numeric_zero
        # Specifies whether to ignore empty strings and null values for string types. Valid values: 0 (no) and 1 (yes).
        self.ignore_string_empty = ignore_string_empty
        # Specifies whether to ignore differences between null values and zero values. Valid values: 0 (no) and 1 (yes).
        self.ignore_zero_diff = ignore_zero_diff
        # Specifies whether to enable count (data volume) verification. Valid values: 0 (no) and 1 (yes). Default value: 1.
        self.is_count_check = is_count_check
        # The rule ID that uniquely identifies a verification rule.
        self.rule_id = rule_id
        # The specific decimal scale value for DECIMAL type comparison.
        self.set_decimal_scale = set_decimal_scale

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_methods is not None:
            result['checkMethods'] = self.check_methods

        if self.control_float_precision is not None:
            result['controlFloatPrecision'] = self.control_float_precision

        if self.data_type_classify is not None:
            result['dataTypeClassify'] = self.data_type_classify

        if self.data_type_group is not None:
            result['dataTypeGroup'] = self.data_type_group

        if self.data_type_list is not None:
            result['dataTypeList'] = self.data_type_list

        if self.data_types is not None:
            result['dataTypes'] = self.data_types

        if self.diff_tolerate_type is not None:
            result['diffTolerateType'] = self.diff_tolerate_type

        if self.diff_tolerate_values is not None:
            result['diffTolerateValues'] = self.diff_tolerate_values

        if self.enable_decimal_scale is not None:
            result['enableDecimalScale'] = self.enable_decimal_scale

        if self.filter_column_name is not None:
            result['filterColumnName'] = self.filter_column_name

        if self.filter_columns is not None:
            result['filterColumns'] = self.filter_columns

        if self.float_precision is not None:
            result['floatPrecision'] = self.float_precision

        if self.ignore_decimal_diff is not None:
            result['ignoreDecimalDiff'] = self.ignore_decimal_diff

        if self.ignore_decimal_scale_suffix_zero is not None:
            result['ignoreDecimalScaleSuffixZero'] = self.ignore_decimal_scale_suffix_zero

        if self.ignore_empty_diff is not None:
            result['ignoreEmptyDiff'] = self.ignore_empty_diff

        if self.ignore_numeric_zero is not None:
            result['ignoreNumericZero'] = self.ignore_numeric_zero

        if self.ignore_string_empty is not None:
            result['ignoreStringEmpty'] = self.ignore_string_empty

        if self.ignore_zero_diff is not None:
            result['ignoreZeroDiff'] = self.ignore_zero_diff

        if self.is_count_check is not None:
            result['isCountCheck'] = self.is_count_check

        if self.rule_id is not None:
            result['ruleId'] = self.rule_id

        if self.set_decimal_scale is not None:
            result['setDecimalScale'] = self.set_decimal_scale

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('checkMethods') is not None:
            self.check_methods = m.get('checkMethods')

        if m.get('controlFloatPrecision') is not None:
            self.control_float_precision = m.get('controlFloatPrecision')

        if m.get('dataTypeClassify') is not None:
            self.data_type_classify = m.get('dataTypeClassify')

        if m.get('dataTypeGroup') is not None:
            self.data_type_group = m.get('dataTypeGroup')

        if m.get('dataTypeList') is not None:
            self.data_type_list = m.get('dataTypeList')

        if m.get('dataTypes') is not None:
            self.data_types = m.get('dataTypes')

        if m.get('diffTolerateType') is not None:
            self.diff_tolerate_type = m.get('diffTolerateType')

        if m.get('diffTolerateValues') is not None:
            self.diff_tolerate_values = m.get('diffTolerateValues')

        if m.get('enableDecimalScale') is not None:
            self.enable_decimal_scale = m.get('enableDecimalScale')

        if m.get('filterColumnName') is not None:
            self.filter_column_name = m.get('filterColumnName')

        if m.get('filterColumns') is not None:
            self.filter_columns = m.get('filterColumns')

        if m.get('floatPrecision') is not None:
            self.float_precision = m.get('floatPrecision')

        if m.get('ignoreDecimalDiff') is not None:
            self.ignore_decimal_diff = m.get('ignoreDecimalDiff')

        if m.get('ignoreDecimalScaleSuffixZero') is not None:
            self.ignore_decimal_scale_suffix_zero = m.get('ignoreDecimalScaleSuffixZero')

        if m.get('ignoreEmptyDiff') is not None:
            self.ignore_empty_diff = m.get('ignoreEmptyDiff')

        if m.get('ignoreNumericZero') is not None:
            self.ignore_numeric_zero = m.get('ignoreNumericZero')

        if m.get('ignoreStringEmpty') is not None:
            self.ignore_string_empty = m.get('ignoreStringEmpty')

        if m.get('ignoreZeroDiff') is not None:
            self.ignore_zero_diff = m.get('ignoreZeroDiff')

        if m.get('isCountCheck') is not None:
            self.is_count_check = m.get('isCountCheck')

        if m.get('ruleId') is not None:
            self.rule_id = m.get('ruleId')

        if m.get('setDecimalScale') is not None:
            self.set_decimal_scale = m.get('setDecimalScale')

        return self

class AddDataCheckTemplateRequestFulltextRule(DaraModel):
    def __init__(
        self,
        check_mode: int = None,
        column_equal_cmp_type: int = None,
        column_equal_cmp_values: str = None,
        column_is_cosine: int = None,
        column_is_ignore_null: int = None,
        column_is_ignore_zero: int = None,
        column_is_samples: int = None,
        column_samples_type: int = None,
        column_samples_value: int = None,
        column_size_cmp_type: int = None,
        column_size_cmp_values: str = None,
        is_primary_key_check: int = None,
        line_check_type: int = None,
        line_is_print_all: int = None,
        line_is_samples: int = None,
        line_samples_type: int = None,
        line_samples_value: int = None,
        rule_id: str = None,
    ):
        # The check mode. Valid values:
        # - 0: row-by-row overall comparison.
        # - 1: row-by-row column-by-column comparison.
        # - 2: both row-by-row overall comparison and row-by-row column-by-column comparison.
        self.check_mode = check_mode
        # The equality comparison type for row-by-row column-by-column comparison. Valid values:
        # - 0: all field types.
        # - 1: native primitive data types.
        # - 2: complex data types.
        # - 3: custom.
        self.column_equal_cmp_type = column_equal_cmp_type
        # The custom type list for equality comparison during row-by-row column-by-column comparison. Separate multiple values with commas.
        self.column_equal_cmp_values = column_equal_cmp_values
        # Specifies whether to enable cosine similarity during row-by-row column-by-column comparison. Valid values:
        # - 0: Disabled.
        # - 1: Enabled.
        self.column_is_cosine = column_is_cosine
        # Specifies whether to ignore differences between null values and empty strings during row-by-row column-by-column comparison. Valid values:
        # - 0: Not ignored.
        # - 1: Ignored.
        self.column_is_ignore_null = column_is_ignore_null
        # Specifies whether to ignore differences between null values and 0 values during row-by-row column-by-column comparison. Valid values:
        # - 0: Not ignored.
        # - 1: Ignored.
        self.column_is_ignore_zero = column_is_ignore_zero
        # Specifies whether to enable sampling during row-by-row column-by-column comparison. Valid values:
        # - 0: Disabled.
        # - 1: Enabled.
        self.column_is_samples = column_is_samples
        # The sampling method for row-by-row column-by-column comparison. Valid values:
        # - 0: by row.
        # - 1: by percentage.
        self.column_samples_type = column_samples_type
        # The sampling value for row-by-row column-by-column comparison. The meaning depends on the sampling method: the number of rows when sampling by row, or the percentage value when sampling by percentage.
        self.column_samples_value = column_samples_value
        # The size comparison type for row-by-row column-by-column comparison. Valid values:
        # - 0: all complex data types.
        # - 1: custom.
        self.column_size_cmp_type = column_size_cmp_type
        # The custom type list for size comparison during row-by-row column-by-column comparison. Separate multiple values with commas.
        self.column_size_cmp_values = column_size_cmp_values
        # Specifies whether to enable primary key or composite primary key existence check. Valid values:
        # - 0: Disabled.
        # - 1: Enabled.
        self.is_primary_key_check = is_primary_key_check
        # The row-by-row comparison method. Valid values:
        # - 0: md5.
        # - 1: crc32.
        self.line_check_type = line_check_type
        # Specifies whether to print all columns in the difference details during row-by-row comparison. Valid values:
        # - 0: Not printed.
        # - 1: Printed.
        self.line_is_print_all = line_is_print_all
        # Specifies whether to enable sampling during row-by-row comparison. Valid values:
        # - 0: Disabled.
        # - 1: Enabled.
        self.line_is_samples = line_is_samples
        # The sampling method for row-by-row comparison. Valid values:
        # - 0: by row.
        # - 1: by percentage.
        self.line_samples_type = line_samples_type
        # The sampling value for row-by-row comparison. The meaning depends on the sampling method: the number of rows when sampling by row, or the percentage value when sampling by percentage.
        self.line_samples_value = line_samples_value
        # The rule ID that uniquely identifies a verification rule.
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_mode is not None:
            result['checkMode'] = self.check_mode

        if self.column_equal_cmp_type is not None:
            result['columnEqualCmpType'] = self.column_equal_cmp_type

        if self.column_equal_cmp_values is not None:
            result['columnEqualCmpValues'] = self.column_equal_cmp_values

        if self.column_is_cosine is not None:
            result['columnIsCosine'] = self.column_is_cosine

        if self.column_is_ignore_null is not None:
            result['columnIsIgnoreNull'] = self.column_is_ignore_null

        if self.column_is_ignore_zero is not None:
            result['columnIsIgnoreZero'] = self.column_is_ignore_zero

        if self.column_is_samples is not None:
            result['columnIsSamples'] = self.column_is_samples

        if self.column_samples_type is not None:
            result['columnSamplesType'] = self.column_samples_type

        if self.column_samples_value is not None:
            result['columnSamplesValue'] = self.column_samples_value

        if self.column_size_cmp_type is not None:
            result['columnSizeCmpType'] = self.column_size_cmp_type

        if self.column_size_cmp_values is not None:
            result['columnSizeCmpValues'] = self.column_size_cmp_values

        if self.is_primary_key_check is not None:
            result['isPrimaryKeyCheck'] = self.is_primary_key_check

        if self.line_check_type is not None:
            result['lineCheckType'] = self.line_check_type

        if self.line_is_print_all is not None:
            result['lineIsPrintAll'] = self.line_is_print_all

        if self.line_is_samples is not None:
            result['lineIsSamples'] = self.line_is_samples

        if self.line_samples_type is not None:
            result['lineSamplesType'] = self.line_samples_type

        if self.line_samples_value is not None:
            result['lineSamplesValue'] = self.line_samples_value

        if self.rule_id is not None:
            result['ruleId'] = self.rule_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('checkMode') is not None:
            self.check_mode = m.get('checkMode')

        if m.get('columnEqualCmpType') is not None:
            self.column_equal_cmp_type = m.get('columnEqualCmpType')

        if m.get('columnEqualCmpValues') is not None:
            self.column_equal_cmp_values = m.get('columnEqualCmpValues')

        if m.get('columnIsCosine') is not None:
            self.column_is_cosine = m.get('columnIsCosine')

        if m.get('columnIsIgnoreNull') is not None:
            self.column_is_ignore_null = m.get('columnIsIgnoreNull')

        if m.get('columnIsIgnoreZero') is not None:
            self.column_is_ignore_zero = m.get('columnIsIgnoreZero')

        if m.get('columnIsSamples') is not None:
            self.column_is_samples = m.get('columnIsSamples')

        if m.get('columnSamplesType') is not None:
            self.column_samples_type = m.get('columnSamplesType')

        if m.get('columnSamplesValue') is not None:
            self.column_samples_value = m.get('columnSamplesValue')

        if m.get('columnSizeCmpType') is not None:
            self.column_size_cmp_type = m.get('columnSizeCmpType')

        if m.get('columnSizeCmpValues') is not None:
            self.column_size_cmp_values = m.get('columnSizeCmpValues')

        if m.get('isPrimaryKeyCheck') is not None:
            self.is_primary_key_check = m.get('isPrimaryKeyCheck')

        if m.get('lineCheckType') is not None:
            self.line_check_type = m.get('lineCheckType')

        if m.get('lineIsPrintAll') is not None:
            self.line_is_print_all = m.get('lineIsPrintAll')

        if m.get('lineIsSamples') is not None:
            self.line_is_samples = m.get('lineIsSamples')

        if m.get('lineSamplesType') is not None:
            self.line_samples_type = m.get('lineSamplesType')

        if m.get('lineSamplesValue') is not None:
            self.line_samples_value = m.get('lineSamplesValue')

        if m.get('ruleId') is not None:
            self.rule_id = m.get('ruleId')

        return self

class AddDataCheckTemplateRequestDsEngineRels(DaraModel):
    def __init__(
        self,
        ds_engine_id: str = None,
        ds_type: str = None,
        engine_types: List[str] = None,
    ):
        # The ID of the datasource engine configuration.
        self.ds_engine_id = ds_engine_id
        # The datasource type, such as Hive or MaxCompute.
        self.ds_type = ds_type
        # The list of covered check engine types, such as Tez or MapReduce. When specified as a string, separate multiple values with commas.
        self.engine_types = engine_types

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ds_engine_id is not None:
            result['dsEngineId'] = self.ds_engine_id

        if self.ds_type is not None:
            result['dsType'] = self.ds_type

        if self.engine_types is not None:
            result['engineTypes'] = self.engine_types

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dsEngineId') is not None:
            self.ds_engine_id = m.get('dsEngineId')

        if m.get('dsType') is not None:
            self.ds_type = m.get('dsType')

        if m.get('engineTypes') is not None:
            self.engine_types = m.get('engineTypes')

        return self

class AddDataCheckTemplateRequestComplexMetricRules(DaraModel):
    def __init__(
        self,
        check_methods: str = None,
        control_float_precision: int = None,
        data_type_classify: int = None,
        data_type_group: int = None,
        data_type_list: List[str] = None,
        data_types: str = None,
        diff_tolerate_type: int = None,
        diff_tolerate_values: Dict[str, Any] = None,
        enable_decimal_scale: int = None,
        filter_column_name: str = None,
        filter_columns: str = None,
        float_precision: int = None,
        ignore_decimal_diff: int = None,
        ignore_decimal_scale_suffix_zero: int = None,
        ignore_empty_diff: int = None,
        ignore_numeric_zero: int = None,
        ignore_string_empty: int = None,
        ignore_zero_diff: int = None,
        is_count_check: int = None,
        rule_id: str = None,
        set_decimal_scale: int = None,
    ):
        # The check methods (metric calculation methods). Separate multiple values with commas, such as SUM,AVG,MIN,MAX. The values must be within the range allowed by the templatetype.
        self.check_methods = check_methods
        # Specifies whether to control floating-point precision. Valid values: 0 (no) and 1 (yes).
        self.control_float_precision = control_float_precision
        # The data type category. Valid values: 0 (native data type) and 1 (composite data type).
        self.data_type_classify = data_type_classify
        # The data type group that identifies the data type category to which the verification rule applies. Valid values: integers from 0 to 7. For the description of each value, see the enumeration values.
        self.data_type_group = data_type_group
        # The list of data types to which the verification rule applies. Configure this field based on your requirements.
        self.data_type_list = data_type_list
        # The data types. Configure this field based on your requirements.
        self.data_types = data_types
        # The difference tolerance rate type. Valid values: 0 (unified) and 1 (custom). Default value: 0.
        self.diff_tolerate_type = diff_tolerate_type
        # The difference tolerance rate values. For the unified type, specify one value, such as {"SAME": 0}. For the custom type, specify a value for each tolerance type, such as {"SUM": 0.01, "AVG": 0.001}.
        self.diff_tolerate_values = diff_tolerate_values
        # Specifies whether to enable decimal scale control for DECIMAL type comparison. Valid values: 0 (no) and 1 (yes).
        self.enable_decimal_scale = enable_decimal_scale
        # The filter field names, separated by commas (,).
        self.filter_column_name = filter_column_name
        # **[Deprecated]** Use the filterColumnName field instead. This field is retained for backward compatibility.
        self.filter_columns = filter_columns
        # The number of decimal places for floating-point values.
        self.float_precision = float_precision
        # Specifies whether to ignore trailing zero differences in decimal parts. Valid values: 0 (no) and 1 (yes).
        self.ignore_decimal_diff = ignore_decimal_diff
        # Specifies whether to ignore trailing zeros in the decimal scale for DECIMAL type comparison. Valid values: 0 (no) and 1 (yes).
        self.ignore_decimal_scale_suffix_zero = ignore_decimal_scale_suffix_zero
        # Specifies whether to ignore differences between null values and empty strings. Valid values: 0 (no) and 1 (yes).
        self.ignore_empty_diff = ignore_empty_diff
        # Specifies whether to ignore zero values for numeric types. Valid values: 0 (no) and 1 (yes).
        self.ignore_numeric_zero = ignore_numeric_zero
        # Specifies whether to ignore empty strings and null values for string types. Valid values: 0 (no) and 1 (yes).
        self.ignore_string_empty = ignore_string_empty
        # Specifies whether to ignore differences between null values and zero values. Valid values: 0 (no) and 1 (yes).
        self.ignore_zero_diff = ignore_zero_diff
        # Specifies whether to enable count (data volume) verification. Valid values: 0 (no) and 1 (yes). Default value: 1.
        self.is_count_check = is_count_check
        # The rule ID that uniquely identifies a verification rule.
        self.rule_id = rule_id
        # The specific decimal scale value for DECIMAL type comparison.
        self.set_decimal_scale = set_decimal_scale

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_methods is not None:
            result['checkMethods'] = self.check_methods

        if self.control_float_precision is not None:
            result['controlFloatPrecision'] = self.control_float_precision

        if self.data_type_classify is not None:
            result['dataTypeClassify'] = self.data_type_classify

        if self.data_type_group is not None:
            result['dataTypeGroup'] = self.data_type_group

        if self.data_type_list is not None:
            result['dataTypeList'] = self.data_type_list

        if self.data_types is not None:
            result['dataTypes'] = self.data_types

        if self.diff_tolerate_type is not None:
            result['diffTolerateType'] = self.diff_tolerate_type

        if self.diff_tolerate_values is not None:
            result['diffTolerateValues'] = self.diff_tolerate_values

        if self.enable_decimal_scale is not None:
            result['enableDecimalScale'] = self.enable_decimal_scale

        if self.filter_column_name is not None:
            result['filterColumnName'] = self.filter_column_name

        if self.filter_columns is not None:
            result['filterColumns'] = self.filter_columns

        if self.float_precision is not None:
            result['floatPrecision'] = self.float_precision

        if self.ignore_decimal_diff is not None:
            result['ignoreDecimalDiff'] = self.ignore_decimal_diff

        if self.ignore_decimal_scale_suffix_zero is not None:
            result['ignoreDecimalScaleSuffixZero'] = self.ignore_decimal_scale_suffix_zero

        if self.ignore_empty_diff is not None:
            result['ignoreEmptyDiff'] = self.ignore_empty_diff

        if self.ignore_numeric_zero is not None:
            result['ignoreNumericZero'] = self.ignore_numeric_zero

        if self.ignore_string_empty is not None:
            result['ignoreStringEmpty'] = self.ignore_string_empty

        if self.ignore_zero_diff is not None:
            result['ignoreZeroDiff'] = self.ignore_zero_diff

        if self.is_count_check is not None:
            result['isCountCheck'] = self.is_count_check

        if self.rule_id is not None:
            result['ruleId'] = self.rule_id

        if self.set_decimal_scale is not None:
            result['setDecimalScale'] = self.set_decimal_scale

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('checkMethods') is not None:
            self.check_methods = m.get('checkMethods')

        if m.get('controlFloatPrecision') is not None:
            self.control_float_precision = m.get('controlFloatPrecision')

        if m.get('dataTypeClassify') is not None:
            self.data_type_classify = m.get('dataTypeClassify')

        if m.get('dataTypeGroup') is not None:
            self.data_type_group = m.get('dataTypeGroup')

        if m.get('dataTypeList') is not None:
            self.data_type_list = m.get('dataTypeList')

        if m.get('dataTypes') is not None:
            self.data_types = m.get('dataTypes')

        if m.get('diffTolerateType') is not None:
            self.diff_tolerate_type = m.get('diffTolerateType')

        if m.get('diffTolerateValues') is not None:
            self.diff_tolerate_values = m.get('diffTolerateValues')

        if m.get('enableDecimalScale') is not None:
            self.enable_decimal_scale = m.get('enableDecimalScale')

        if m.get('filterColumnName') is not None:
            self.filter_column_name = m.get('filterColumnName')

        if m.get('filterColumns') is not None:
            self.filter_columns = m.get('filterColumns')

        if m.get('floatPrecision') is not None:
            self.float_precision = m.get('floatPrecision')

        if m.get('ignoreDecimalDiff') is not None:
            self.ignore_decimal_diff = m.get('ignoreDecimalDiff')

        if m.get('ignoreDecimalScaleSuffixZero') is not None:
            self.ignore_decimal_scale_suffix_zero = m.get('ignoreDecimalScaleSuffixZero')

        if m.get('ignoreEmptyDiff') is not None:
            self.ignore_empty_diff = m.get('ignoreEmptyDiff')

        if m.get('ignoreNumericZero') is not None:
            self.ignore_numeric_zero = m.get('ignoreNumericZero')

        if m.get('ignoreStringEmpty') is not None:
            self.ignore_string_empty = m.get('ignoreStringEmpty')

        if m.get('ignoreZeroDiff') is not None:
            self.ignore_zero_diff = m.get('ignoreZeroDiff')

        if m.get('isCountCheck') is not None:
            self.is_count_check = m.get('isCountCheck')

        if m.get('ruleId') is not None:
            self.rule_id = m.get('ruleId')

        if m.get('setDecimalScale') is not None:
            self.set_decimal_scale = m.get('setDecimalScale')

        return self



class AddDataCheckTemplateRequestBasicMetricRules(DaraModel):
    def __init__(
        self,
        check_methods: str = None,
        control_float_precision: int = None,
        data_type_classify: int = None,
        data_type_group: int = None,
        data_type_list: List[str] = None,
        data_types: str = None,
        diff_tolerate_type: int = None,
        diff_tolerate_values: Dict[str, Any] = None,
        enable_decimal_scale: int = None,
        filter_column_name: str = None,
        filter_columns: str = None,
        float_precision: int = None,
        ignore_decimal_diff: int = None,
        ignore_decimal_scale_suffix_zero: int = None,
        ignore_empty_diff: int = None,
        ignore_numeric_zero: int = None,
        ignore_string_empty: int = None,
        ignore_zero_diff: int = None,
        is_count_check: int = None,
        rule_id: str = None,
        set_decimal_scale: int = None,
    ):
        # The verification methods (metric calculation methods). Separate multiple values with commas (,), such as SUM,AVG,MIN,MAX. The values must be within the range allowed by the templatetype.
        self.check_methods = check_methods
        # Specifies whether to control floating-point precision. Valid values: 0 (no) and 1 (yes).
        self.control_float_precision = control_float_precision
        # The data type category. Valid values: 0 (native data type) and 1 (composite data type).
        self.data_type_classify = data_type_classify
        # The data type group that identifies the data type category to which the verification rule applies. Valid values: integers from 0 to 7. For the description of each value, see the enumeration values.
        self.data_type_group = data_type_group
        # The list of data types to which the verification rule applies. Configure this field based on your requirements.
        self.data_type_list = data_type_list
        # The data types. Configure this field based on your requirements.
        self.data_types = data_types
        # The difference tolerance rate type. Valid values: 0 (unified) and 1 (custom). Default value: 0.
        self.diff_tolerate_type = diff_tolerate_type
        # The difference tolerance rate values. For the unified type, specify one value, such as {"SAME": 0}. For the custom type, specify a value for each tolerance type, such as {"SUM": 0.01, "AVG": 0.001}.
        self.diff_tolerate_values = diff_tolerate_values
        # Specifies whether to enable decimal scale control for DECIMAL type comparison. Valid values: 0 (no) and 1 (yes).
        self.enable_decimal_scale = enable_decimal_scale
        # The filter field names, separated by commas (,).
        self.filter_column_name = filter_column_name
        # **[Deprecated]** Use the filterColumnName field instead. This field is retained for backward compatibility.
        self.filter_columns = filter_columns
        # The number of decimal places for floating-point values.
        self.float_precision = float_precision
        # Specifies whether to ignore trailing zero differences in decimal parts. Valid values: 0 (no) and 1 (yes).
        self.ignore_decimal_diff = ignore_decimal_diff
        # Specifies whether to ignore trailing zeros in the decimal scale for DECIMAL type comparison. Valid values: 0 (no) and 1 (yes).
        self.ignore_decimal_scale_suffix_zero = ignore_decimal_scale_suffix_zero
        # Specifies whether to ignore differences between null values and empty strings. Valid values: 0 (no) and 1 (yes).
        self.ignore_empty_diff = ignore_empty_diff
        # Specifies whether to ignore zero values for numeric types. Valid values: 0 (no) and 1 (yes).
        self.ignore_numeric_zero = ignore_numeric_zero
        # Specifies whether to ignore empty strings and null values for string types. Valid values: 0 (no) and 1 (yes).
        self.ignore_string_empty = ignore_string_empty
        # Specifies whether to ignore differences between null values and zero values. Valid values: 0 (no) and 1 (yes).
        self.ignore_zero_diff = ignore_zero_diff
        # Specifies whether to enable count (data volume) verification. Valid values: 0 (no) and 1 (yes). Default value: 1.
        self.is_count_check = is_count_check
        # The rule ID that uniquely identifies a verification rule.
        self.rule_id = rule_id
        # The specific decimal scale value for DECIMAL type comparison.
        self.set_decimal_scale = set_decimal_scale

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_methods is not None:
            result['checkMethods'] = self.check_methods

        if self.control_float_precision is not None:
            result['controlFloatPrecision'] = self.control_float_precision

        if self.data_type_classify is not None:
            result['dataTypeClassify'] = self.data_type_classify

        if self.data_type_group is not None:
            result['dataTypeGroup'] = self.data_type_group

        if self.data_type_list is not None:
            result['dataTypeList'] = self.data_type_list

        if self.data_types is not None:
            result['dataTypes'] = self.data_types

        if self.diff_tolerate_type is not None:
            result['diffTolerateType'] = self.diff_tolerate_type

        if self.diff_tolerate_values is not None:
            result['diffTolerateValues'] = self.diff_tolerate_values

        if self.enable_decimal_scale is not None:
            result['enableDecimalScale'] = self.enable_decimal_scale

        if self.filter_column_name is not None:
            result['filterColumnName'] = self.filter_column_name

        if self.filter_columns is not None:
            result['filterColumns'] = self.filter_columns

        if self.float_precision is not None:
            result['floatPrecision'] = self.float_precision

        if self.ignore_decimal_diff is not None:
            result['ignoreDecimalDiff'] = self.ignore_decimal_diff

        if self.ignore_decimal_scale_suffix_zero is not None:
            result['ignoreDecimalScaleSuffixZero'] = self.ignore_decimal_scale_suffix_zero

        if self.ignore_empty_diff is not None:
            result['ignoreEmptyDiff'] = self.ignore_empty_diff

        if self.ignore_numeric_zero is not None:
            result['ignoreNumericZero'] = self.ignore_numeric_zero

        if self.ignore_string_empty is not None:
            result['ignoreStringEmpty'] = self.ignore_string_empty

        if self.ignore_zero_diff is not None:
            result['ignoreZeroDiff'] = self.ignore_zero_diff

        if self.is_count_check is not None:
            result['isCountCheck'] = self.is_count_check

        if self.rule_id is not None:
            result['ruleId'] = self.rule_id

        if self.set_decimal_scale is not None:
            result['setDecimalScale'] = self.set_decimal_scale

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('checkMethods') is not None:
            self.check_methods = m.get('checkMethods')

        if m.get('controlFloatPrecision') is not None:
            self.control_float_precision = m.get('controlFloatPrecision')

        if m.get('dataTypeClassify') is not None:
            self.data_type_classify = m.get('dataTypeClassify')

        if m.get('dataTypeGroup') is not None:
            self.data_type_group = m.get('dataTypeGroup')

        if m.get('dataTypeList') is not None:
            self.data_type_list = m.get('dataTypeList')

        if m.get('dataTypes') is not None:
            self.data_types = m.get('dataTypes')

        if m.get('diffTolerateType') is not None:
            self.diff_tolerate_type = m.get('diffTolerateType')

        if m.get('diffTolerateValues') is not None:
            self.diff_tolerate_values = m.get('diffTolerateValues')

        if m.get('enableDecimalScale') is not None:
            self.enable_decimal_scale = m.get('enableDecimalScale')

        if m.get('filterColumnName') is not None:
            self.filter_column_name = m.get('filterColumnName')

        if m.get('filterColumns') is not None:
            self.filter_columns = m.get('filterColumns')

        if m.get('floatPrecision') is not None:
            self.float_precision = m.get('floatPrecision')

        if m.get('ignoreDecimalDiff') is not None:
            self.ignore_decimal_diff = m.get('ignoreDecimalDiff')

        if m.get('ignoreDecimalScaleSuffixZero') is not None:
            self.ignore_decimal_scale_suffix_zero = m.get('ignoreDecimalScaleSuffixZero')

        if m.get('ignoreEmptyDiff') is not None:
            self.ignore_empty_diff = m.get('ignoreEmptyDiff')

        if m.get('ignoreNumericZero') is not None:
            self.ignore_numeric_zero = m.get('ignoreNumericZero')

        if m.get('ignoreStringEmpty') is not None:
            self.ignore_string_empty = m.get('ignoreStringEmpty')

        if m.get('ignoreZeroDiff') is not None:
            self.ignore_zero_diff = m.get('ignoreZeroDiff')

        if m.get('isCountCheck') is not None:
            self.is_count_check = m.get('isCountCheck')

        if m.get('ruleId') is not None:
            self.rule_id = m.get('ruleId')

        if m.get('setDecimalScale') is not None:
            self.set_decimal_scale = m.get('setDecimalScale')

        return self

