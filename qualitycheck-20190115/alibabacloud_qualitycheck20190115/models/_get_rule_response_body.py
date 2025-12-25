# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_qualitycheck20190115 import models as main_models
from darabonba.model import DaraModel

class GetRuleResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetRuleResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetRuleResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetRuleResponseBodyData(DaraModel):
    def __init__(
        self,
        rules: main_models.GetRuleResponseBodyDataRules = None,
    ):
        self.rules = rules

    def validate(self):
        if self.rules:
            self.rules.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.rules is not None:
            result['Rules'] = self.rules.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Rules') is not None:
            temp_model = main_models.GetRuleResponseBodyDataRules()
            self.rules = temp_model.from_map(m.get('Rules'))

        return self

class GetRuleResponseBodyDataRules(DaraModel):
    def __init__(
        self,
        rule_info: List[main_models.GetRuleResponseBodyDataRulesRuleInfo] = None,
    ):
        self.rule_info = rule_info

    def validate(self):
        if self.rule_info:
            for v1 in self.rule_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['RuleInfo'] = []
        if self.rule_info is not None:
            for k1 in self.rule_info:
                result['RuleInfo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.rule_info = []
        if m.get('RuleInfo') is not None:
            for k1 in m.get('RuleInfo'):
                temp_model = main_models.GetRuleResponseBodyDataRulesRuleInfo()
                self.rule_info.append(temp_model.from_map(k1))

        return self

class GetRuleResponseBodyDataRulesRuleInfo(DaraModel):
    def __init__(
        self,
        auto_review: int = None,
        business_category_name_list: main_models.GetRuleResponseBodyDataRulesRuleInfoBusinessCategoryNameList = None,
        comments: str = None,
        create_empid: str = None,
        create_time: str = None,
        end_time: str = None,
        is_delete: int = None,
        is_online: int = None,
        last_update_empid: str = None,
        last_update_time: str = None,
        name: str = None,
        rid: str = None,
        rule_lambda: str = None,
        rule_score_type: int = None,
        score_id: int = None,
        score_name: str = None,
        score_sub_id: int = None,
        score_sub_name: str = None,
        start_time: str = None,
        status: int = None,
        type: int = None,
        weight: str = None,
    ):
        self.auto_review = auto_review
        self.business_category_name_list = business_category_name_list
        self.comments = comments
        self.create_empid = create_empid
        self.create_time = create_time
        self.end_time = end_time
        self.is_delete = is_delete
        self.is_online = is_online
        self.last_update_empid = last_update_empid
        self.last_update_time = last_update_time
        self.name = name
        self.rid = rid
        self.rule_lambda = rule_lambda
        self.rule_score_type = rule_score_type
        self.score_id = score_id
        self.score_name = score_name
        self.score_sub_id = score_sub_id
        self.score_sub_name = score_sub_name
        self.start_time = start_time
        self.status = status
        self.type = type
        self.weight = weight

    def validate(self):
        if self.business_category_name_list:
            self.business_category_name_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_review is not None:
            result['AutoReview'] = self.auto_review

        if self.business_category_name_list is not None:
            result['BusinessCategoryNameList'] = self.business_category_name_list.to_map()

        if self.comments is not None:
            result['Comments'] = self.comments

        if self.create_empid is not None:
            result['CreateEmpid'] = self.create_empid

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.is_delete is not None:
            result['IsDelete'] = self.is_delete

        if self.is_online is not None:
            result['IsOnline'] = self.is_online

        if self.last_update_empid is not None:
            result['LastUpdateEmpid'] = self.last_update_empid

        if self.last_update_time is not None:
            result['LastUpdateTime'] = self.last_update_time

        if self.name is not None:
            result['Name'] = self.name

        if self.rid is not None:
            result['Rid'] = self.rid

        if self.rule_lambda is not None:
            result['RuleLambda'] = self.rule_lambda

        if self.rule_score_type is not None:
            result['RuleScoreType'] = self.rule_score_type

        if self.score_id is not None:
            result['ScoreId'] = self.score_id

        if self.score_name is not None:
            result['ScoreName'] = self.score_name

        if self.score_sub_id is not None:
            result['ScoreSubId'] = self.score_sub_id

        if self.score_sub_name is not None:
            result['ScoreSubName'] = self.score_sub_name

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        if self.weight is not None:
            result['Weight'] = self.weight

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoReview') is not None:
            self.auto_review = m.get('AutoReview')

        if m.get('BusinessCategoryNameList') is not None:
            temp_model = main_models.GetRuleResponseBodyDataRulesRuleInfoBusinessCategoryNameList()
            self.business_category_name_list = temp_model.from_map(m.get('BusinessCategoryNameList'))

        if m.get('Comments') is not None:
            self.comments = m.get('Comments')

        if m.get('CreateEmpid') is not None:
            self.create_empid = m.get('CreateEmpid')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('IsDelete') is not None:
            self.is_delete = m.get('IsDelete')

        if m.get('IsOnline') is not None:
            self.is_online = m.get('IsOnline')

        if m.get('LastUpdateEmpid') is not None:
            self.last_update_empid = m.get('LastUpdateEmpid')

        if m.get('LastUpdateTime') is not None:
            self.last_update_time = m.get('LastUpdateTime')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Rid') is not None:
            self.rid = m.get('Rid')

        if m.get('RuleLambda') is not None:
            self.rule_lambda = m.get('RuleLambda')

        if m.get('RuleScoreType') is not None:
            self.rule_score_type = m.get('RuleScoreType')

        if m.get('ScoreId') is not None:
            self.score_id = m.get('ScoreId')

        if m.get('ScoreName') is not None:
            self.score_name = m.get('ScoreName')

        if m.get('ScoreSubId') is not None:
            self.score_sub_id = m.get('ScoreSubId')

        if m.get('ScoreSubName') is not None:
            self.score_sub_name = m.get('ScoreSubName')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Weight') is not None:
            self.weight = m.get('Weight')

        return self

class GetRuleResponseBodyDataRulesRuleInfoBusinessCategoryNameList(DaraModel):
    def __init__(
        self,
        business_category_name_list: List[str] = None,
    ):
        self.business_category_name_list = business_category_name_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.business_category_name_list is not None:
            result['BusinessCategoryNameList'] = self.business_category_name_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessCategoryNameList') is not None:
            self.business_category_name_list = m.get('BusinessCategoryNameList')

        return self

