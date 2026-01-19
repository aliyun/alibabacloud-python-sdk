# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_xtee20210910 import models as main_models
from darabonba.model import DaraModel

class DescribeAuthRulePageListResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        current_page: int = None,
        page_size: int = None,
        result_object: List[main_models.DescribeAuthRulePageListResponseBodyResultObject] = None,
        total_item: int = None,
        total_page: int = None,
    ):
        # Request ID
        self.request_id = request_id
        # Current page number.
        self.current_page = current_page
        # Page size, default value is 10
        self.page_size = page_size
        # Returned object
        self.result_object = result_object
        # Total items
        self.total_item = total_item
        # Total pages
        self.total_page = total_page

    def validate(self):
        if self.result_object:
            for v1 in self.result_object:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.current_page is not None:
            result['currentPage'] = self.current_page

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        result['resultObject'] = []
        if self.result_object is not None:
            for k1 in self.result_object:
                result['resultObject'].append(k1.to_map() if k1 else None)

        if self.total_item is not None:
            result['totalItem'] = self.total_item

        if self.total_page is not None:
            result['totalPage'] = self.total_page

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('currentPage') is not None:
            self.current_page = m.get('currentPage')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        self.result_object = []
        if m.get('resultObject') is not None:
            for k1 in m.get('resultObject'):
                temp_model = main_models.DescribeAuthRulePageListResponseBodyResultObject()
                self.result_object.append(temp_model.from_map(k1))

        if m.get('totalItem') is not None:
            self.total_item = m.get('totalItem')

        if m.get('totalPage') is not None:
            self.total_page = m.get('totalPage')

        return self

class DescribeAuthRulePageListResponseBodyResultObject(DaraModel):
    def __init__(
        self,
        console_rule_id: int = None,
        create_type: str = None,
        gmt_modified: int = None,
        id: int = None,
        memo: str = None,
        rule_id: str = None,
        rule_name: str = None,
        rule_version_id: int = None,
        status: str = None,
        version: int = None,
    ):
        # Console rule ID.
        self.console_rule_id = console_rule_id
        # Creation type
        self.create_type = create_type
        # Modification time
        self.gmt_modified = gmt_modified
        # Policy primary key ID
        self.id = id
        # Memo
        self.memo = memo
        # Policy ID
        self.rule_id = rule_id
        # Policy name
        self.rule_name = rule_name
        # Policy version primary key ID
        self.rule_version_id = rule_version_id
        # Status.
        self.status = status
        # Version number
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.console_rule_id is not None:
            result['consoleRuleId'] = self.console_rule_id

        if self.create_type is not None:
            result['createType'] = self.create_type

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.id is not None:
            result['id'] = self.id

        if self.memo is not None:
            result['memo'] = self.memo

        if self.rule_id is not None:
            result['ruleId'] = self.rule_id

        if self.rule_name is not None:
            result['ruleName'] = self.rule_name

        if self.rule_version_id is not None:
            result['ruleVersionId'] = self.rule_version_id

        if self.status is not None:
            result['status'] = self.status

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('consoleRuleId') is not None:
            self.console_rule_id = m.get('consoleRuleId')

        if m.get('createType') is not None:
            self.create_type = m.get('createType')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('memo') is not None:
            self.memo = m.get('memo')

        if m.get('ruleId') is not None:
            self.rule_id = m.get('ruleId')

        if m.get('ruleName') is not None:
            self.rule_name = m.get('ruleName')

        if m.get('ruleVersionId') is not None:
            self.rule_version_id = m.get('ruleVersionId')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

