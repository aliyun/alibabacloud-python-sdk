# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class ListClientUserDefineRulesResponseBody(DaraModel):
    def __init__(
        self,
        page_info: main_models.ListClientUserDefineRulesResponseBodyPageInfo = None,
        request_id: str = None,
        user_define_rule_list: List[main_models.ListClientUserDefineRulesResponseBodyUserDefineRuleList] = None,
    ):
        # The pagination information.
        self.page_info = page_info
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # An array that consists of the rules.
        self.user_define_rule_list = user_define_rule_list

    def validate(self):
        if self.page_info:
            self.page_info.validate()
        if self.user_define_rule_list:
            for v1 in self.user_define_rule_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['UserDefineRuleList'] = []
        if self.user_define_rule_list is not None:
            for k1 in self.user_define_rule_list:
                result['UserDefineRuleList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageInfo') is not None:
            temp_model = main_models.ListClientUserDefineRulesResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.user_define_rule_list = []
        if m.get('UserDefineRuleList') is not None:
            for k1 in m.get('UserDefineRuleList'):
                temp_model = main_models.ListClientUserDefineRulesResponseBodyUserDefineRuleList()
                self.user_define_rule_list.append(temp_model.from_map(k1))

        return self

class ListClientUserDefineRulesResponseBodyUserDefineRuleList(DaraModel):
    def __init__(
        self,
        action_type: int = None,
        id: int = None,
        name: str = None,
        platform: str = None,
        switch_id: str = None,
        type: int = None,
    ):
        # The action of the rule. Valid values:
        # 
        # *   **0**: allow
        # *   **1**: block
        self.action_type = action_type
        # The ID of the rule.
        self.id = id
        # The name of the rule.
        self.name = name
        # The type of the operating system. Valid values:
        # 
        # *   **windows**: Windows
        # *   **linux**: Linux
        # *   **all**: all types
        self.platform = platform
        # The switch ID of the rule.
        self.switch_id = switch_id
        # The type of the rule. Valid values:
        # 
        # *   **1**: Process hash
        # *   **2**: Command line
        # *   **3**: Process Network
        # *   **4**: File Read and Write
        # *   **5**: Operation on Registry
        # *   **6**: Dynamic-link Library Loading
        # *   **7**: File Renaming
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action_type is not None:
            result['ActionType'] = self.action_type

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.platform is not None:
            result['Platform'] = self.platform

        if self.switch_id is not None:
            result['SwitchId'] = self.switch_id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionType') is not None:
            self.action_type = m.get('ActionType')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Platform') is not None:
            self.platform = m.get('Platform')

        if m.get('SwitchId') is not None:
            self.switch_id = m.get('SwitchId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class ListClientUserDefineRulesResponseBodyPageInfo(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The page number of the returned page.
        self.current_page = current_page
        # The number of entries returned per page.
        self.page_size = page_size
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

