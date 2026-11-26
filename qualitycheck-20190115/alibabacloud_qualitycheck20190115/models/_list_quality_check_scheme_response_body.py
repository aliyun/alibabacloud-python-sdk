# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_qualitycheck20190115 import models as main_models
from darabonba.model import DaraModel

class ListQualityCheckSchemeResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        count: int = None,
        data: List[main_models.ListQualityCheckSchemeResponseBodyData] = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        result_count_id: str = None,
        success: bool = None,
    ):
        # The result code. A value of **200** indicates success. Other values indicate failure. You can use this field to determine the cause of the failure.
        self.code = code
        # The total number of entries.
        self.count = count
        # The data of the quality check scheme list.
        self.data = data
        # The error message returned when an error occurs. The value is successful when the request is successful.
        self.message = message
        # The current page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # An internal field. Ignore this field.
        self.result_count_id = result_count_id
        # Indicates whether the request is successful. **true** indicates that the request is successful. **false** or **null** indicates that the request fails.
        self.success = success

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
        if self.code is not None:
            result['Code'] = self.code

        if self.count is not None:
            result['Count'] = self.count

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['Message'] = self.message

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result_count_id is not None:
            result['ResultCountId'] = self.result_count_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Count') is not None:
            self.count = m.get('Count')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListQualityCheckSchemeResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResultCountId') is not None:
            self.result_count_id = m.get('ResultCountId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListQualityCheckSchemeResponseBodyData(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        create_user_name: str = None,
        data_type: int = None,
        description: str = None,
        name: str = None,
        rule_list: List[main_models.ListQualityCheckSchemeResponseBodyDataRuleList] = None,
        scheme_check_type_list: List[main_models.ListQualityCheckSchemeResponseBodyDataSchemeCheckTypeList] = None,
        scheme_id: int = None,
        status: int = None,
        template_type: int = None,
        type: int = None,
        update_time: str = None,
        update_user_name: str = None,
        version: int = None,
    ):
        # The creation time.
        self.create_time = create_time
        # The name of the creator.
        self.create_user_name = create_user_name
        # The data type of the quality check scheme. Valid values: 0: text; 1: audio.
        self.data_type = data_type
        # The description.
        self.description = description
        # The name of the quality check scheme.
        self.name = name
        # The list of check items.
        self.rule_list = rule_list
        # The list of quality check dimensions.
        self.scheme_check_type_list = scheme_check_type_list
        # The ID of the quality check scheme.
        self.scheme_id = scheme_id
        # The status of the quality check scheme. Valid values: 0: deleted; 1: published; 2: unpublished; 3: updated and unpublished.
        self.status = status
        # The type of the quality check scheme template. Valid values: 1: built-in; 2: custom.
        self.template_type = template_type
        # The type of the quality check scheme. Valid values: 0: built-in; 1: custom.
        self.type = type
        # The update time.
        self.update_time = update_time
        # The name of the updater.
        self.update_user_name = update_user_name
        # The version of the quality check scheme.
        self.version = version

    def validate(self):
        if self.rule_list:
            for v1 in self.rule_list:
                 if v1:
                    v1.validate()
        if self.scheme_check_type_list:
            for v1 in self.scheme_check_type_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.create_user_name is not None:
            result['CreateUserName'] = self.create_user_name

        if self.data_type is not None:
            result['DataType'] = self.data_type

        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        result['RuleList'] = []
        if self.rule_list is not None:
            for k1 in self.rule_list:
                result['RuleList'].append(k1.to_map() if k1 else None)

        result['SchemeCheckTypeList'] = []
        if self.scheme_check_type_list is not None:
            for k1 in self.scheme_check_type_list:
                result['SchemeCheckTypeList'].append(k1.to_map() if k1 else None)

        if self.scheme_id is not None:
            result['SchemeId'] = self.scheme_id

        if self.status is not None:
            result['Status'] = self.status

        if self.template_type is not None:
            result['TemplateType'] = self.template_type

        if self.type is not None:
            result['Type'] = self.type

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.update_user_name is not None:
            result['UpdateUserName'] = self.update_user_name

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CreateUserName') is not None:
            self.create_user_name = m.get('CreateUserName')

        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        self.rule_list = []
        if m.get('RuleList') is not None:
            for k1 in m.get('RuleList'):
                temp_model = main_models.ListQualityCheckSchemeResponseBodyDataRuleList()
                self.rule_list.append(temp_model.from_map(k1))

        self.scheme_check_type_list = []
        if m.get('SchemeCheckTypeList') is not None:
            for k1 in m.get('SchemeCheckTypeList'):
                temp_model = main_models.ListQualityCheckSchemeResponseBodyDataSchemeCheckTypeList()
                self.scheme_check_type_list.append(temp_model.from_map(k1))

        if m.get('SchemeId') is not None:
            self.scheme_id = m.get('SchemeId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('UpdateUserName') is not None:
            self.update_user_name = m.get('UpdateUserName')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

class ListQualityCheckSchemeResponseBodyDataSchemeCheckTypeList(DaraModel):
    def __init__(
        self,
        check_name: str = None,
        check_type: int = None,
        enable: int = None,
        score: int = None,
        target_type: int = None,
    ):
        # The name of the quality check dimension.
        self.check_name = check_name
        # The type of the quality check dimension.
        self.check_type = check_type
        # The enable status. Valid values: 0: disabled; 1: enabled.
        self.enable = enable
        # The score of the quality check dimension.
        self.score = score
        # An internal field. Ignore this field.
        self.target_type = target_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_name is not None:
            result['CheckName'] = self.check_name

        if self.check_type is not None:
            result['CheckType'] = self.check_type

        if self.enable is not None:
            result['Enable'] = self.enable

        if self.score is not None:
            result['Score'] = self.score

        if self.target_type is not None:
            result['TargetType'] = self.target_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckName') is not None:
            self.check_name = m.get('CheckName')

        if m.get('CheckType') is not None:
            self.check_type = m.get('CheckType')

        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('Score') is not None:
            self.score = m.get('Score')

        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')

        return self

class ListQualityCheckSchemeResponseBodyDataRuleList(DaraModel):
    def __init__(
        self,
        rules: List[main_models.ListQualityCheckSchemeResponseBodyDataRuleListRules] = None,
    ):
        # The rule information. Only one rule is included here and reserved for future extensions.
        self.rules = rules

    def validate(self):
        if self.rules:
            for v1 in self.rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Rules'] = []
        if self.rules is not None:
            for k1 in self.rules:
                result['Rules'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.rules = []
        if m.get('Rules') is not None:
            for k1 in m.get('Rules'):
                temp_model = main_models.ListQualityCheckSchemeResponseBodyDataRuleListRules()
                self.rules.append(temp_model.from_map(k1))

        return self

class ListQualityCheckSchemeResponseBodyDataRuleListRules(DaraModel):
    def __init__(
        self,
        check_type: int = None,
        name: str = None,
        rid: int = None,
        rule_score_type: int = None,
        score_num: int = None,
        score_num_type: int = None,
        score_type: int = None,
        target_type: int = None,
    ):
        # The quality check dimension to which the rule belongs.
        self.check_type = check_type
        # The name of the check item.
        self.name = name
        # The ID of the check item.
        self.rid = rid
        # Specifies whether the score is calculated. Valid values: 1: not calculated; 3: calculated.
        self.rule_score_type = rule_score_type
        # The score.
        self.score_num = score_num
        # The scoring type. Valid values: 0: add or deduct points after the rule is triggered; 1: award a one-time score after the rule is triggered.
        self.score_num_type = score_num_type
        # The score adjustment type. Valid values: 1: add points; 3: deduct points.
        self.score_type = score_type
        # The common scenarios of the check item. Valid values: 10: common check item. 11: SOP flow check item.
        self.target_type = target_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_type is not None:
            result['CheckType'] = self.check_type

        if self.name is not None:
            result['Name'] = self.name

        if self.rid is not None:
            result['Rid'] = self.rid

        if self.rule_score_type is not None:
            result['RuleScoreType'] = self.rule_score_type

        if self.score_num is not None:
            result['ScoreNum'] = self.score_num

        if self.score_num_type is not None:
            result['ScoreNumType'] = self.score_num_type

        if self.score_type is not None:
            result['ScoreType'] = self.score_type

        if self.target_type is not None:
            result['TargetType'] = self.target_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckType') is not None:
            self.check_type = m.get('CheckType')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Rid') is not None:
            self.rid = m.get('Rid')

        if m.get('RuleScoreType') is not None:
            self.rule_score_type = m.get('RuleScoreType')

        if m.get('ScoreNum') is not None:
            self.score_num = m.get('ScoreNum')

        if m.get('ScoreNumType') is not None:
            self.score_num_type = m.get('ScoreNumType')

        if m.get('ScoreType') is not None:
            self.score_type = m.get('ScoreType')

        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')

        return self

