# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_qualitycheck20190115 import models as main_models
from darabonba.model import DaraModel

class GetQualityCheckSchemeResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetQualityCheckSchemeResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        messages: List[str] = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.messages = messages
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

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.messages is not None:
            result['Messages'] = self.messages

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
            temp_model = main_models.GetQualityCheckSchemeResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Messages') is not None:
            self.messages = m.get('Messages')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetQualityCheckSchemeResponseBodyData(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        create_user_name: str = None,
        data_type: int = None,
        description: str = None,
        init_score: str = None,
        name: str = None,
        rule_ids: List[str] = None,
        rule_list: List[main_models.RulesInfo] = None,
        scheme_check_type_list: List[main_models.GetQualityCheckSchemeResponseBodyDataSchemeCheckTypeList] = None,
        scheme_id: int = None,
        scheme_template_id: int = None,
        status: int = None,
        template_type: int = None,
        type: int = None,
        update_time: str = None,
        update_user_name: str = None,
        version: int = None,
    ):
        self.create_time = create_time
        self.create_user_name = create_user_name
        self.data_type = data_type
        self.description = description
        self.init_score = init_score
        self.name = name
        self.rule_ids = rule_ids
        self.rule_list = rule_list
        self.scheme_check_type_list = scheme_check_type_list
        self.scheme_id = scheme_id
        self.scheme_template_id = scheme_template_id
        self.status = status
        self.template_type = template_type
        self.type = type
        self.update_time = update_time
        self.update_user_name = update_user_name
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

        if self.init_score is not None:
            result['InitScore'] = self.init_score

        if self.name is not None:
            result['Name'] = self.name

        if self.rule_ids is not None:
            result['RuleIds'] = self.rule_ids

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

        if self.scheme_template_id is not None:
            result['SchemeTemplateId'] = self.scheme_template_id

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

        if m.get('InitScore') is not None:
            self.init_score = m.get('InitScore')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RuleIds') is not None:
            self.rule_ids = m.get('RuleIds')

        self.rule_list = []
        if m.get('RuleList') is not None:
            for k1 in m.get('RuleList'):
                temp_model = main_models.RulesInfo()
                self.rule_list.append(temp_model.from_map(k1))

        self.scheme_check_type_list = []
        if m.get('SchemeCheckTypeList') is not None:
            for k1 in m.get('SchemeCheckTypeList'):
                temp_model = main_models.GetQualityCheckSchemeResponseBodyDataSchemeCheckTypeList()
                self.scheme_check_type_list.append(temp_model.from_map(k1))

        if m.get('SchemeId') is not None:
            self.scheme_id = m.get('SchemeId')

        if m.get('SchemeTemplateId') is not None:
            self.scheme_template_id = m.get('SchemeTemplateId')

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

class GetQualityCheckSchemeResponseBodyDataSchemeCheckTypeList(DaraModel):
    def __init__(
        self,
        check_name: str = None,
        check_type: int = None,
        enable: int = None,
        scheme_id: int = None,
        score: int = None,
        source_score: int = None,
    ):
        self.check_name = check_name
        self.check_type = check_type
        self.enable = enable
        self.scheme_id = scheme_id
        self.score = score
        self.source_score = source_score

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

        if self.scheme_id is not None:
            result['SchemeId'] = self.scheme_id

        if self.score is not None:
            result['Score'] = self.score

        if self.source_score is not None:
            result['SourceScore'] = self.source_score

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckName') is not None:
            self.check_name = m.get('CheckName')

        if m.get('CheckType') is not None:
            self.check_type = m.get('CheckType')

        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('SchemeId') is not None:
            self.scheme_id = m.get('SchemeId')

        if m.get('Score') is not None:
            self.score = m.get('Score')

        if m.get('SourceScore') is not None:
            self.source_score = m.get('SourceScore')

        return self

