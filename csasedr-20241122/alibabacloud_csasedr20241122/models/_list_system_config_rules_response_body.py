# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_csasedr20241122 import models as main_models
from darabonba.model import DaraModel

class ListSystemConfigRulesResponseBody(DaraModel):
    def __init__(
        self,
        list: List[main_models.ListSystemConfigRulesResponseBodyList] = None,
        page_info: main_models.ListSystemConfigRulesResponseBodyPageInfo = None,
        request_id: str = None,
    ):
        # The rule list.
        self.list = list
        # The paging information displayed during a paged query.
        self.page_info = page_info
        # The unique identifier of the request, which is used to troubleshoot and locate issues.
        self.request_id = request_id

    def validate(self):
        if self.list:
            for v1 in self.list:
                 if v1:
                    v1.validate()
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['List'] = []
        if self.list is not None:
            for k1 in self.list:
                result['List'].append(k1.to_map() if k1 else None)

        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k1 in m.get('List'):
                temp_model = main_models.ListSystemConfigRulesResponseBodyList()
                self.list.append(temp_model.from_map(k1))

        if m.get('PageInfo') is not None:
            temp_model = main_models.ListSystemConfigRulesResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListSystemConfigRulesResponseBodyPageInfo(DaraModel):
    def __init__(
        self,
        count: int = None,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The number of entries on the current page.
        self.count = count
        # The current page number.
        self.current_page = current_page
        # The maximum number of entries to return on each page during paging in a paged query.
        self.page_size = page_size
        # The total number of entries.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListSystemConfigRulesResponseBodyList(DaraModel):
    def __init__(
        self,
        id: int = None,
        platform: str = None,
        rule_name: str = None,
        rule_type: int = None,
        status: str = None,
        switch_id: str = None,
    ):
        # The rule ID.
        self.id = id
        # The platform name of the system rule. Valid values:
        # - **1**: Linux.
        # - **2**: Windows.
        # - **3**: Mac.
        self.platform = platform
        # The rule name.
        self.rule_name = rule_name
        # The rule type.
        self.rule_type = rule_type
        # The switch status of the rule under the specified SelectionKey. Valid values:
        # - **add**: Enabled.
        # - **del**: Disabled.
        self.status = status
        # The switch identifier of the system rule.
        self.switch_id = switch_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.platform is not None:
            result['Platform'] = self.platform

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.rule_type is not None:
            result['RuleType'] = self.rule_type

        if self.status is not None:
            result['Status'] = self.status

        if self.switch_id is not None:
            result['SwitchId'] = self.switch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Platform') is not None:
            self.platform = m.get('Platform')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SwitchId') is not None:
            self.switch_id = m.get('SwitchId')

        return self

