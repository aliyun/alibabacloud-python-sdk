# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class GetBuildRiskDefineRuleConfigResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetBuildRiskDefineRuleConfigResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response code. The status code **200** indicates that the request was successful. Other status codes indicate that the request failed. You can identify the cause of the failure based on the status code.
        self.code = code
        # The data returned.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**
        # *   **false**
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
            temp_model = main_models.GetBuildRiskDefineRuleConfigResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetBuildRiskDefineRuleConfigResponseBodyData(DaraModel):
    def __init__(
        self,
        id: int = None,
        rule_count: int = None,
        rule_tree: List[main_models.GetBuildRiskDefineRuleConfigResponseBodyDataRuleTree] = None,
        selected_count: int = None,
    ):
        # The configuration ID for scanning image build command risks.
        self.id = id
        # The total number of check items.
        self.rule_count = rule_count
        # The details of all check items.
        self.rule_tree = rule_tree
        # The number of selected check items.
        self.selected_count = selected_count

    def validate(self):
        if self.rule_tree:
            for v1 in self.rule_tree:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.rule_count is not None:
            result['RuleCount'] = self.rule_count

        result['RuleTree'] = []
        if self.rule_tree is not None:
            for k1 in self.rule_tree:
                result['RuleTree'].append(k1.to_map() if k1 else None)

        if self.selected_count is not None:
            result['SelectedCount'] = self.selected_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('RuleCount') is not None:
            self.rule_count = m.get('RuleCount')

        self.rule_tree = []
        if m.get('RuleTree') is not None:
            for k1 in m.get('RuleTree'):
                temp_model = main_models.GetBuildRiskDefineRuleConfigResponseBodyDataRuleTree()
                self.rule_tree.append(temp_model.from_map(k1))

        if m.get('SelectedCount') is not None:
            self.selected_count = m.get('SelectedCount')

        return self

class GetBuildRiskDefineRuleConfigResponseBodyDataRuleTree(DaraModel):
    def __init__(
        self,
        class_key: str = None,
        class_name: str = None,
        rule_list: List[main_models.GetBuildRiskDefineRuleConfigResponseBodyDataRuleTreeRuleList] = None,
    ):
        # The check item type.
        self.class_key = class_key
        # The name of the check item type.
        self.class_name = class_name
        # The check items of the type.
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
        if self.class_key is not None:
            result['ClassKey'] = self.class_key

        if self.class_name is not None:
            result['ClassName'] = self.class_name

        result['RuleList'] = []
        if self.rule_list is not None:
            for k1 in self.rule_list:
                result['RuleList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClassKey') is not None:
            self.class_key = m.get('ClassKey')

        if m.get('ClassName') is not None:
            self.class_name = m.get('ClassName')

        self.rule_list = []
        if m.get('RuleList') is not None:
            for k1 in m.get('RuleList'):
                temp_model = main_models.GetBuildRiskDefineRuleConfigResponseBodyDataRuleTreeRuleList()
                self.rule_list.append(temp_model.from_map(k1))

        return self

class GetBuildRiskDefineRuleConfigResponseBodyDataRuleTreeRuleList(DaraModel):
    def __init__(
        self,
        rule_key: str = None,
        rule_name: str = None,
        selected: bool = None,
    ):
        # The check item.
        self.rule_key = rule_key
        # The name of the check item.
        self.rule_name = rule_name
        # Indicates whether the check item is selected. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.selected = selected

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.rule_key is not None:
            result['RuleKey'] = self.rule_key

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.selected is not None:
            result['Selected'] = self.selected

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RuleKey') is not None:
            self.rule_key = m.get('RuleKey')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('Selected') is not None:
            self.selected = m.get('Selected')

        return self

