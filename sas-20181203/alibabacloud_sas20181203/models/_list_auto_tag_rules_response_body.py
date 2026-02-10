# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class ListAutoTagRulesResponseBody(DaraModel):
    def __init__(
        self,
        auto_tag_rule_list: List[main_models.ListAutoTagRulesResponseBodyAutoTagRuleList] = None,
        page_info: main_models.ListAutoTagRulesResponseBodyPageInfo = None,
        request_id: str = None,
    ):
        # The asset auto-tagging rules.
        self.auto_tag_rule_list = auto_tag_rule_list
        # The pagination information.
        self.page_info = page_info
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.auto_tag_rule_list:
            for v1 in self.auto_tag_rule_list:
                 if v1:
                    v1.validate()
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AutoTagRuleList'] = []
        if self.auto_tag_rule_list is not None:
            for k1 in self.auto_tag_rule_list:
                result['AutoTagRuleList'].append(k1.to_map() if k1 else None)

        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.auto_tag_rule_list = []
        if m.get('AutoTagRuleList') is not None:
            for k1 in m.get('AutoTagRuleList'):
                temp_model = main_models.ListAutoTagRulesResponseBodyAutoTagRuleList()
                self.auto_tag_rule_list.append(temp_model.from_map(k1))

        if m.get('PageInfo') is not None:
            temp_model = main_models.ListAutoTagRulesResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListAutoTagRulesResponseBodyPageInfo(DaraModel):
    def __init__(
        self,
        count: int = None,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The number of entries returned on the current page.
        self.count = count
        # The page number.
        self.current_page = current_page
        # The number of entries per page.
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

class ListAutoTagRulesResponseBodyAutoTagRuleList(DaraModel):
    def __init__(
        self,
        ali_uid: int = None,
        create_timestamp: int = None,
        expression: str = None,
        id: int = None,
        modified_timestamp: int = None,
        rule_desc: str = None,
        rule_name: str = None,
        tag_context: str = None,
        tag_type: str = None,
    ):
        # The ID of the Alibaba Cloud account.
        self.ali_uid = ali_uid
        # The timestamp when the rule was created. Unit: milliseconds.
        self.create_timestamp = create_timestamp
        # The expression of the rule.
        self.expression = expression
        # The ID of the rule.
        self.id = id
        # The timestamp when the rule was last updated. Unit: milliseconds.
        self.modified_timestamp = modified_timestamp
        # The description of the rule.
        self.rule_desc = rule_desc
        # The name of the rule.
        self.rule_name = rule_name
        # The tag specified by the operation type of the rule.
        self.tag_context = tag_context
        # The operation type of the rule. Valid values:
        # 
        # *   **group**
        # *   **tag**
        self.tag_type = tag_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid

        if self.create_timestamp is not None:
            result['CreateTimestamp'] = self.create_timestamp

        if self.expression is not None:
            result['Expression'] = self.expression

        if self.id is not None:
            result['Id'] = self.id

        if self.modified_timestamp is not None:
            result['ModifiedTimestamp'] = self.modified_timestamp

        if self.rule_desc is not None:
            result['RuleDesc'] = self.rule_desc

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.tag_context is not None:
            result['TagContext'] = self.tag_context

        if self.tag_type is not None:
            result['TagType'] = self.tag_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')

        if m.get('CreateTimestamp') is not None:
            self.create_timestamp = m.get('CreateTimestamp')

        if m.get('Expression') is not None:
            self.expression = m.get('Expression')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('ModifiedTimestamp') is not None:
            self.modified_timestamp = m.get('ModifiedTimestamp')

        if m.get('RuleDesc') is not None:
            self.rule_desc = m.get('RuleDesc')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('TagContext') is not None:
            self.tag_context = m.get('TagContext')

        if m.get('TagType') is not None:
            self.tag_type = m.get('TagType')

        return self

