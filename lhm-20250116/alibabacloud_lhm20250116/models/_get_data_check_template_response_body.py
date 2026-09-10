# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_lhm20250116 import models as main_models
from darabonba.model import DaraModel

class GetDataCheckTemplateResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetDataCheckTemplateResponseBodyData = None,
        err_code: str = None,
        err_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The data body returned by the operation. For the field structure, refer to the child field descriptions below.
        self.data = data
        # The error code. An empty string is returned if the call is successful.
        self.err_code = err_code
        # The error message. An empty string is returned if the call is successful.
        self.err_message = err_message
        # The request ID, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # Indicates whether the call is successful. Valid values: true: The call is successful. false: The call failed. If the call failed, check errCode and errMessage for details.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.err_code is not None:
            result['errCode'] = self.err_code

        if self.err_message is not None:
            result['errMessage'] = self.err_message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = main_models.GetDataCheckTemplateResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')

        if m.get('errMessage') is not None:
            self.err_message = m.get('errMessage')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class GetDataCheckTemplateResponseBodyData(DaraModel):
    def __init__(
        self,
        basic_metric_rules: List[main_models.GetDataCheckTemplateResponseBodyDataBasicMetricRules] = None,
        check_type: int = None,
        check_type_export: str = None,
        check_type_name: int = None,
        complex_metric_rules: List[main_models.GetDataCheckTemplateResponseBodyDataComplexMetricRules] = None,
        ds_engine_rels: List[main_models.GetDataCheckTemplateResponseBodyDataDsEngineRels] = None,
        fulltext_rule: main_models.GetDataCheckTemplateResponseBodyDataFulltextRule = None,
        metric_rules: List[main_models.GetDataCheckTemplateResponseBodyDataMetricRules] = None,
        null_rules: List[main_models.GetDataCheckTemplateResponseBodyDataNullRules] = None,
        template_desc: str = None,
        template_id: str = None,
        template_name: str = None,
        weak_content_rule: main_models.GetDataCheckTemplateResponseBodyDataWeakContentRule = None,
    ):
        # The list of check rules for basic data type metrics. This field is required when checkType is set to 1 (metric comparison).
        self.basic_metric_rules = basic_metric_rules
        # The check rule type. Valid values: 0: data volume comparison. 1: metric comparison. 2: weak content comparison. 3: custom comparison. 4: full-text comparison. 5: null rate comparison.
        self.check_type = check_type
        # The Chinese name of the check type (used in export report fields).
        self.check_type_export = check_type_export
        # The check type name.
        self.check_type_name = check_type_name
        # The list of check rules for composite data type metrics. This field is used when checkType is set to 1 (metric comparison).
        self.complex_metric_rules = complex_metric_rules
        # The list of data source engine relationships (data source engines associated with the template).
        self.ds_engine_rels = ds_engine_rels
        # The full-text comparison rule. This field has a value when checkType is set to 4 (full-text comparison). For the field structure, refer to the child field descriptions below.
        self.fulltext_rule = fulltext_rule
        # The list of metric check rules. This parameter has a value when checkType is set to 1 (metric comparison).
        self.metric_rules = metric_rules
        # The list of null rate check rules. This parameter has a value when checkType is set to 5 (null rate comparison).
        self.null_rules = null_rules
        # The template description.
        self.template_desc = template_desc
        # The check template ID (logical foreign key) that uniquely identifies a check template.
        self.template_id = template_id
        # The name of the check template.
        self.template_name = template_name
        # The weak content check rule. This parameter has a value and is required when checkType is set to 2 (weak content comparison). For the field structure, see the child field descriptions.
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

        if self.check_type_export is not None:
            result['checkTypeExport'] = self.check_type_export

        if self.check_type_name is not None:
            result['checkTypeName'] = self.check_type_name

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

        if self.template_desc is not None:
            result['templateDesc'] = self.template_desc

        if self.template_id is not None:
            result['templateId'] = self.template_id

        if self.template_name is not None:
            result['templateName'] = self.template_name

        if self.weak_content_rule is not None:
            result['weakContentRule'] = self.weak_content_rule.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.basic_metric_rules = []
        if m.get('basicMetricRules') is not None:
            for k1 in m.get('basicMetricRules'):
                temp_model = main_models.GetDataCheckTemplateResponseBodyDataBasicMetricRules()
                self.basic_metric_rules.append(temp_model.from_map(k1))

        if m.get('checkType') is not None:
            self.check_type = m.get('checkType')

        if m.get('checkTypeExport') is not None:
            self.check_type_export = m.get('checkTypeExport')

        if m.get('checkTypeName') is not None:
            self.check_type_name = m.get('checkTypeName')

        self.complex_metric_rules = []
        if m.get('complexMetricRules') is not None:
            for k1 in m.get('complexMetricRules'):
                temp_model = main_models.GetDataCheckTemplateResponseBodyDataComplexMetricRules()
                self.complex_metric_rules.append(temp_model.from_map(k1))

        self.ds_engine_rels = []
        if m.get('dsEngineRels') is not None:
            for k1 in m.get('dsEngineRels'):
                temp_model = main_models.GetDataCheckTemplateResponseBodyDataDsEngineRels()
                self.ds_engine_rels.append(temp_model.from_map(k1))

        if m.get('fulltextRule') is not None:
            temp_model = main_models.GetDataCheckTemplateResponseBodyDataFulltextRule()
            self.fulltext_rule = temp_model.from_map(m.get('fulltextRule'))

        self.metric_rules = []
        if m.get('metricRules') is not None:
            for k1 in m.get('metricRules'):
                temp_model = main_models.GetDataCheckTemplateResponseBodyDataMetricRules()
                self.metric_rules.append(temp_model.from_map(k1))

        self.null_rules = []
        if m.get('nullRules') is not None:
            for k1 in m.get('nullRules'):
                temp_model = main_models.GetDataCheckTemplateResponseBodyDataNullRules()
                self.null_rules.append(temp_model.from_map(k1))

        if m.get('templateDesc') is not None:
            self.template_desc = m.get('templateDesc')

        if m.get('templateId') is not None:
            self.template_id = m.get('templateId')

        if m.get('templateName') is not None:
            self.template_name = m.get('templateName')

        if m.get('weakContentRule') is not None:
            temp_model = main_models.GetDataCheckTemplateResponseBodyDataWeakContentRule()
            self.weak_content_rule = temp_model.from_map(m.get('weakContentRule'))

        return self

class GetDataCheckTemplateResponseBodyDataWeakContentRule(DaraModel):
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
        # The rule ID that uniquely identifies a check rule.
        self.rule_id = rule_id
        # The weak content algorithm name. Valid values: md5 and crc32.
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

class GetDataCheckTemplateResponseBodyDataNullRules(DaraModel):
    def __init__(
        self,
        data_type_group: int = None,
        null_values: str = None,
        rule_id: str = None,
    ):
        # The data type group that identifies the data type category to which the check rule applies. The value is an integer from 0 to 7. For the meaning of each value, refer to the valid values.
        self.data_type_group = data_type_group
        # The null values, stored in JSON format.
        self.null_values = null_values
        # The rule ID that uniquely identifies a check rule.
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

class GetDataCheckTemplateResponseBodyDataMetricRules(DaraModel):
    def __init__(
        self,
        check_methods: str = None,
        data_type_classify: int = None,
        data_type_group: int = None,
        data_type_list: List[str] = None,
        data_types: str = None,
        diff_tolerate_type: int = None,
        diff_tolerate_values: Dict[str, Any] = None,
        enable_decimal_scale: int = None,
        filter_column_name: str = None,
        ignore_decimal_scale_suffix_zero: int = None,
        ignore_numeric_zero: int = None,
        ignore_string_empty: int = None,
        is_count_check: int = None,
        rule_id: str = None,
        set_decimal_scale: int = None,
    ):
        # The check methods (metric calculation methods). Multiple values are separated by commas (,), such as SUM,AVG,MIN,MAX. The values must be within the range allowed by the templatetype.
        self.check_methods = check_methods
        # The data type category. Valid values: 0: primitive data type. 1: composite data type.
        self.data_type_classify = data_type_classify
        # The data type group that identifies the data type category to which the check rule applies. The value is an integer from 0 to 7. For the meaning of each value, refer to the valid values.
        self.data_type_group = data_type_group
        # The list of data types to which the check rule applies. Configure this field as needed.
        self.data_type_list = data_type_list
        # The data types. Configure this field as needed.
        self.data_types = data_types
        # The difference tolerance rate type. Valid values: 0: unified. 1: custom. Default value: 0.
        self.diff_tolerate_type = diff_tolerate_type
        # The difference tolerance rate values. When the type is unified, one value is used. When the type is custom, values are set by the configured tolerance type, such as sum:33,avg:99.
        self.diff_tolerate_values = diff_tolerate_values
        # Specifies whether to enable decimal scale control for DECIMAL type comparison. Valid values: 0: no. 1: yes.
        self.enable_decimal_scale = enable_decimal_scale
        # The filter column names, separated by commas.
        self.filter_column_name = filter_column_name
        # Specifies whether to ignore trailing zeros in decimal places for DECIMAL type comparison. Valid values: 0: no. 1: yes.
        self.ignore_decimal_scale_suffix_zero = ignore_decimal_scale_suffix_zero
        # Specifies whether to ignore zero values for numeric types. Valid values: 0: no. 1: yes.
        self.ignore_numeric_zero = ignore_numeric_zero
        # Specifies whether to ignore empty strings and null for string types. Valid values: 0: no. 1: yes.
        self.ignore_string_empty = ignore_string_empty
        # Specifies whether to enable count (data volume) check. Valid values: 0: no. 1: yes. Default value: 1.
        self.is_count_check = is_count_check
        # The rule ID that uniquely identifies a check rule.
        self.rule_id = rule_id
        # The specific number of decimal places for DECIMAL type comparison.
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

        if self.ignore_decimal_scale_suffix_zero is not None:
            result['ignoreDecimalScaleSuffixZero'] = self.ignore_decimal_scale_suffix_zero

        if self.ignore_numeric_zero is not None:
            result['ignoreNumericZero'] = self.ignore_numeric_zero

        if self.ignore_string_empty is not None:
            result['ignoreStringEmpty'] = self.ignore_string_empty

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

        if m.get('ignoreDecimalScaleSuffixZero') is not None:
            self.ignore_decimal_scale_suffix_zero = m.get('ignoreDecimalScaleSuffixZero')

        if m.get('ignoreNumericZero') is not None:
            self.ignore_numeric_zero = m.get('ignoreNumericZero')

        if m.get('ignoreStringEmpty') is not None:
            self.ignore_string_empty = m.get('ignoreStringEmpty')

        if m.get('isCountCheck') is not None:
            self.is_count_check = m.get('isCountCheck')

        if m.get('ruleId') is not None:
            self.rule_id = m.get('ruleId')

        if m.get('setDecimalScale') is not None:
            self.set_decimal_scale = m.get('setDecimalScale')

        return self

class GetDataCheckTemplateResponseBodyDataFulltextRule(DaraModel):
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
        # The check mode. Valid values: 0: row-level overall comparison. 1: row-level column-by-column comparison. 2: both row-level overall comparison and row-level column-by-column comparison.
        self.check_mode = check_mode
        # The equality comparison type for row-level column-by-column comparison. Valid values: 0: all field types. 1: primitive basic data types. 2: composite data types. 3: custom.
        self.column_equal_cmp_type = column_equal_cmp_type
        # The custom type list for equality comparison during row-level column-by-column comparison. Multiple values are separated by commas.
        self.column_equal_cmp_values = column_equal_cmp_values
        # Specifies whether to enable cosine similarity for row-level column-by-column comparison. Valid values: 0: no. 1: yes.
        self.column_is_cosine = column_is_cosine
        # Specifies whether to ignore differences between null values and empty strings during row-by-row and column-by-column comparison. Valid values: 0: No. 1: Yes.
        self.column_is_ignore_null = column_is_ignore_null
        # Specifies whether to ignore differences between null values and 0 values during row-by-row and column-by-column comparison. Valid values: 0: No. 1: Yes.
        self.column_is_ignore_zero = column_is_ignore_zero
        # Specifies whether to enable sampling during row-by-row and column-by-column comparison. Valid values: 0: No. 1: Yes.
        self.column_is_samples = column_is_samples
        # The sampling method during row-by-row and column-by-column comparison. Valid values: 0: by row. 1: by percentage.
        self.column_samples_type = column_samples_type
        # The sampling value during row-by-row and column-by-column comparison. The meaning depends on the sampling method. When sampling by row, this value represents the number of rows. When sampling by percentage, this value represents the percentage.
        self.column_samples_value = column_samples_value
        # The size comparison type during row-by-row and column-by-column comparison. Valid values: 0: all composite data types. 1: custom.
        self.column_size_cmp_type = column_size_cmp_type
        # The custom type list for size comparison during row-by-row and column-by-column comparison. Multiple values are separated by commas (,).
        self.column_size_cmp_values = column_size_cmp_values
        # Specifies whether to enable the existence check for primary keys or composite primary keys. Valid values: 0: No. 1: Yes.
        self.is_primary_key_check = is_primary_key_check
        # The row-by-row comparison method. Valid values: 0: md5. 1: crc32.
        self.line_check_type = line_check_type
        # Specifies whether to print all columns in the difference details during row-by-row comparison. Valid values: 0: No. 1: Yes.
        self.line_is_print_all = line_is_print_all
        # Specifies whether to enable sampling during row-by-row comparison. Valid values: 0: No. 1: Yes.
        self.line_is_samples = line_is_samples
        # The sampling method during row-by-row comparison. Valid values: 0: by row. 1: by percentage.
        self.line_samples_type = line_samples_type
        # The sampling value during row-by-row comparison. The meaning depends on the sampling method. When sampling by row, this value represents the number of rows. When sampling by percentage, this value represents the percentage.
        self.line_samples_value = line_samples_value
        # The rule ID that uniquely identifies a check rule.
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

class GetDataCheckTemplateResponseBodyDataDsEngineRels(DaraModel):
    def __init__(
        self,
        ds_type: str = None,
        engine_types: List[str] = None,
    ):
        # The data source type, such as Hive or MaxCompute.
        self.ds_type = ds_type
        # The list of covered check engine types, such as Tez or MapReduce. When in string format, multiple values are separated by commas.
        self.engine_types = engine_types

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ds_type is not None:
            result['dsType'] = self.ds_type

        if self.engine_types is not None:
            result['engineTypes'] = self.engine_types

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dsType') is not None:
            self.ds_type = m.get('dsType')

        if m.get('engineTypes') is not None:
            self.engine_types = m.get('engineTypes')

        return self

class GetDataCheckTemplateResponseBodyDataComplexMetricRules(DaraModel):
    def __init__(
        self,
        check_methods: str = None,
        data_type_classify: int = None,
        data_type_group: int = None,
        data_type_list: List[str] = None,
        data_types: str = None,
        diff_tolerate_type: int = None,
        diff_tolerate_values: Dict[str, Any] = None,
        enable_decimal_scale: int = None,
        filter_column_name: str = None,
        ignore_decimal_scale_suffix_zero: int = None,
        ignore_numeric_zero: int = None,
        ignore_string_empty: int = None,
        is_count_check: int = None,
        rule_id: str = None,
        set_decimal_scale: int = None,
    ):
        # The check methods (metric calculation methods). Multiple values are separated by commas, such as SUM,AVG,MIN,MAX. The values must be within the range allowed by the templatetype.
        self.check_methods = check_methods
        # The data type category. Valid values: 0: primitive data type. 1: composite data type.
        self.data_type_classify = data_type_classify
        # The data type group that identifies the data type category to which the check rule applies. The value is an integer from 0 to 7. For the meaning of each value, refer to the valid values.
        self.data_type_group = data_type_group
        # The list of data types to which the check rule applies. Configure this field as needed.
        self.data_type_list = data_type_list
        # The data types. Configure this field as needed.
        self.data_types = data_types
        # The difference tolerance rate type. Valid values: 0: unified. 1: custom. Default value: 0.
        self.diff_tolerate_type = diff_tolerate_type
        # The difference tolerance rate values. When the type is unified, one value is used. When the type is custom, values are set by the configured tolerance type, such as sum:33,avg:99.
        self.diff_tolerate_values = diff_tolerate_values
        # Specifies whether to enable decimal scale control for DECIMAL type comparison. Valid values: 0: no. 1: yes.
        self.enable_decimal_scale = enable_decimal_scale
        # The filter column names, separated by commas.
        self.filter_column_name = filter_column_name
        # Specifies whether to ignore trailing zeros in decimal places for DECIMAL type comparison. Valid values: 0: no. 1: yes.
        self.ignore_decimal_scale_suffix_zero = ignore_decimal_scale_suffix_zero
        # Specifies whether to ignore zero values for numeric types. Valid values: 0: no. 1: yes.
        self.ignore_numeric_zero = ignore_numeric_zero
        # Specifies whether to ignore empty strings and null for string types. Valid values: 0: no. 1: yes.
        self.ignore_string_empty = ignore_string_empty
        # Specifies whether to enable count (data volume) check. Valid values: 0: no. 1: yes. Default value: 1.
        self.is_count_check = is_count_check
        # The rule ID that uniquely identifies a check rule.
        self.rule_id = rule_id
        # The specific number of decimal places for DECIMAL type comparison.
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

        if self.ignore_decimal_scale_suffix_zero is not None:
            result['ignoreDecimalScaleSuffixZero'] = self.ignore_decimal_scale_suffix_zero

        if self.ignore_numeric_zero is not None:
            result['ignoreNumericZero'] = self.ignore_numeric_zero

        if self.ignore_string_empty is not None:
            result['ignoreStringEmpty'] = self.ignore_string_empty

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

        if m.get('ignoreDecimalScaleSuffixZero') is not None:
            self.ignore_decimal_scale_suffix_zero = m.get('ignoreDecimalScaleSuffixZero')

        if m.get('ignoreNumericZero') is not None:
            self.ignore_numeric_zero = m.get('ignoreNumericZero')

        if m.get('ignoreStringEmpty') is not None:
            self.ignore_string_empty = m.get('ignoreStringEmpty')

        if m.get('isCountCheck') is not None:
            self.is_count_check = m.get('isCountCheck')

        if m.get('ruleId') is not None:
            self.rule_id = m.get('ruleId')

        if m.get('setDecimalScale') is not None:
            self.set_decimal_scale = m.get('setDecimalScale')

        return self

class GetDataCheckTemplateResponseBodyDataBasicMetricRules(DaraModel):
    def __init__(
        self,
        check_methods: str = None,
        data_type_classify: int = None,
        data_type_group: int = None,
        data_type_list: List[str] = None,
        data_types: str = None,
        diff_tolerate_type: int = None,
        diff_tolerate_values: Dict[str, Any] = None,
        enable_decimal_scale: int = None,
        filter_column_name: str = None,
        ignore_decimal_scale_suffix_zero: int = None,
        ignore_numeric_zero: int = None,
        ignore_string_empty: int = None,
        is_count_check: int = None,
        rule_id: str = None,
        set_decimal_scale: int = None,
    ):
        # The check methods (metric calculation methods). Multiple values are separated by commas, such as SUM,AVG,MIN,MAX. The values must be within the range allowed by the templatetype.
        self.check_methods = check_methods
        # The data type category. Valid values: 0: primitive data type. 1: composite data type.
        self.data_type_classify = data_type_classify
        # The data type group that identifies the data type category to which the check rule applies. The value is an integer from 0 to 7. For the meaning of each value, refer to the valid values.
        self.data_type_group = data_type_group
        # The list of data types to which the check rule applies. Configure this field as needed.
        self.data_type_list = data_type_list
        # The data types. Configure this field as needed.
        self.data_types = data_types
        # The difference tolerance rate type. Valid values: 0: unified. 1: custom. Default value: 0.
        self.diff_tolerate_type = diff_tolerate_type
        # The difference tolerance rate values. When the type is unified, one value is used. When the type is custom, values are set by the configured tolerance type, such as sum:33,avg:99.
        self.diff_tolerate_values = diff_tolerate_values
        # Specifies whether to enable decimal scale control for DECIMAL type comparison. Valid values: 0: no. 1: yes.
        self.enable_decimal_scale = enable_decimal_scale
        # The filter column names, separated by commas.
        self.filter_column_name = filter_column_name
        # Specifies whether to ignore trailing zeros in decimal places for DECIMAL type comparison. Valid values: 0: no. 1: yes.
        self.ignore_decimal_scale_suffix_zero = ignore_decimal_scale_suffix_zero
        # Specifies whether to ignore zero values for numeric types. Valid values: 0: no. 1: yes.
        self.ignore_numeric_zero = ignore_numeric_zero
        # Specifies whether to ignore empty strings and null for string types. Valid values: 0: no. 1: yes.
        self.ignore_string_empty = ignore_string_empty
        # Specifies whether to enable count (data volume) check. Valid values: 0: no. 1: yes. Default value: 1.
        self.is_count_check = is_count_check
        # The rule ID that uniquely identifies a check rule.
        self.rule_id = rule_id
        # The specific number of decimal places for DECIMAL type comparison.
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

        if self.ignore_decimal_scale_suffix_zero is not None:
            result['ignoreDecimalScaleSuffixZero'] = self.ignore_decimal_scale_suffix_zero

        if self.ignore_numeric_zero is not None:
            result['ignoreNumericZero'] = self.ignore_numeric_zero

        if self.ignore_string_empty is not None:
            result['ignoreStringEmpty'] = self.ignore_string_empty

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

        if m.get('ignoreDecimalScaleSuffixZero') is not None:
            self.ignore_decimal_scale_suffix_zero = m.get('ignoreDecimalScaleSuffixZero')

        if m.get('ignoreNumericZero') is not None:
            self.ignore_numeric_zero = m.get('ignoreNumericZero')

        if m.get('ignoreStringEmpty') is not None:
            self.ignore_string_empty = m.get('ignoreStringEmpty')

        if m.get('isCountCheck') is not None:
            self.is_count_check = m.get('isCountCheck')

        if m.get('ruleId') is not None:
            self.rule_id = m.get('ruleId')

        if m.get('setDecimalScale') is not None:
            self.set_decimal_scale = m.get('setDecimalScale')

        return self

