# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ddoscoo20200101 import models as main_models
from darabonba.model import DaraModel

class DescribeWebPreciseAccessRuleResponseBody(DaraModel):
    def __init__(
        self,
        precise_access_config_list: List[main_models.DescribeWebPreciseAccessRuleResponseBodyPreciseAccessConfigList] = None,
        request_id: str = None,
    ):
        # The precise access control rules for the website.
        self.precise_access_config_list = precise_access_config_list
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.precise_access_config_list:
            for v1 in self.precise_access_config_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['PreciseAccessConfigList'] = []
        if self.precise_access_config_list is not None:
            for k1 in self.precise_access_config_list:
                result['PreciseAccessConfigList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.precise_access_config_list = []
        if m.get('PreciseAccessConfigList') is not None:
            for k1 in m.get('PreciseAccessConfigList'):
                temp_model = main_models.DescribeWebPreciseAccessRuleResponseBodyPreciseAccessConfigList()
                self.precise_access_config_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeWebPreciseAccessRuleResponseBodyPreciseAccessConfigList(DaraModel):
    def __init__(
        self,
        domain: str = None,
        rule_list: List[main_models.DescribeWebPreciseAccessRuleResponseBodyPreciseAccessConfigListRuleList] = None,
    ):
        # The domain name of the website.
        self.domain = domain
        # The list of rules.
        self.rule_list = rule_list

    def validate(self):
        if self.rule_list:
            for v1 in self.rule_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain is not None:
            result['Domain'] = self.domain

        result['RuleList'] = []
        if self.rule_list is not None:
            for k1 in self.rule_list:
                result['RuleList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        self.rule_list = []
        if m.get('RuleList') is not None:
            for k1 in m.get('RuleList'):
                temp_model = main_models.DescribeWebPreciseAccessRuleResponseBodyPreciseAccessConfigListRuleList()
                self.rule_list.append(temp_model.from_map(k1))

        return self

class DescribeWebPreciseAccessRuleResponseBodyPreciseAccessConfigListRuleList(DaraModel):
    def __init__(
        self,
        action: str = None,
        condition_list: List[main_models.DescribeWebPreciseAccessRuleResponseBodyPreciseAccessConfigListRuleListConditionList] = None,
        expire_period: int = None,
        expires: int = None,
        name: str = None,
        owner: str = None,
    ):
        # The action that is performed on requests that match the rule. Valid values:
        # 
        # - **accept**: allows the requests.
        # 
        # - **block**: blocks the requests.
        # 
        # - **challenge**: triggers a JavaScript Challenge for the requests.
        self.action = action
        # The list of match conditions.
        self.condition_list = condition_list
        # The validity period of the rule. This value is a UNIX timestamp. Unit: seconds.
        self.expire_period = expire_period
        # The validity period of the rule. Unit: seconds. This parameter is required only when the **action** of the rule is **block**. Requests that match the rule are blocked within the validity period. A value of **0** indicates that the rule is permanently valid.
        self.expires = expires
        # The name of the rule.
        self.name = name
        # The source of the rule. Valid values:
        # 
        # - **manual** (default): The rule is manually created.
        # 
        # - **clover**: The rule is automatically generated.
        self.owner = owner

    def validate(self):
        if self.condition_list:
            for v1 in self.condition_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['Action'] = self.action

        result['ConditionList'] = []
        if self.condition_list is not None:
            for k1 in self.condition_list:
                result['ConditionList'].append(k1.to_map() if k1 else None)

        if self.expire_period is not None:
            result['ExpirePeriod'] = self.expire_period

        if self.expires is not None:
            result['Expires'] = self.expires

        if self.name is not None:
            result['Name'] = self.name

        if self.owner is not None:
            result['Owner'] = self.owner

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')

        self.condition_list = []
        if m.get('ConditionList') is not None:
            for k1 in m.get('ConditionList'):
                temp_model = main_models.DescribeWebPreciseAccessRuleResponseBodyPreciseAccessConfigListRuleListConditionList()
                self.condition_list.append(temp_model.from_map(k1))

        if m.get('ExpirePeriod') is not None:
            self.expire_period = m.get('ExpirePeriod')

        if m.get('Expires') is not None:
            self.expires = m.get('Expires')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        return self

class DescribeWebPreciseAccessRuleResponseBodyPreciseAccessConfigListRuleListConditionList(DaraModel):
    def __init__(
        self,
        content: str = None,
        content_list: List[str] = None,
        field: str = None,
        header_name: str = None,
        match_method: str = None,
    ):
        # The match content.
        self.content = content
        # The match conditions of the rule. The value is a JSON string. The value contains the following fields:
        # 
        # > If you specify multiple match conditions, the logical relation between these conditions is AND.
        # 
        # - **field**: The match field. This parameter is of the string type.
        # 
        # - **match_method**: The match method. This parameter is of the string type.
        # 
        #   > For more information about the valid values of **field** and **match_method**, see the "Additional information about field and match_method" section in this topic.
        # 
        # - **content**: The match content. This parameter is of the string type.
        # 
        # - **header_name**: The name of the header field. This parameter is of the string type. This parameter is required only when **field** is set to **header**.
        self.content_list = content_list
        # The match field.
        self.field = field
        # The name of the custom HTTP header field.
        # 
        # > This parameter is required only when **Field** is set to **header**.
        self.header_name = header_name
        # The logical operator.
        self.match_method = match_method

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.content_list is not None:
            result['ContentList'] = self.content_list

        if self.field is not None:
            result['Field'] = self.field

        if self.header_name is not None:
            result['HeaderName'] = self.header_name

        if self.match_method is not None:
            result['MatchMethod'] = self.match_method

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('ContentList') is not None:
            self.content_list = m.get('ContentList')

        if m.get('Field') is not None:
            self.field = m.get('Field')

        if m.get('HeaderName') is not None:
            self.header_name = m.get('HeaderName')

        if m.get('MatchMethod') is not None:
            self.match_method = m.get('MatchMethod')

        return self

