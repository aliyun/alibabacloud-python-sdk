# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bdrc20230808 import models as main_models
from darabonba.model import DaraModel

class DescribeRulesResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.DescribeRulesResponseBodyData = None,
        request_id: str = None,
    ):
        # The returned data.
        self.data = data
        # The unique ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.DescribeRulesResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeRulesResponseBodyData(DaraModel):
    def __init__(
        self,
        content: List[main_models.DescribeRulesResponseBodyDataContent] = None,
        max_results: int = None,
        next_token: str = None,
        total_count: int = None,
    ):
        # The list of returned records.
        self.content = content
        # The maximum number of entries returned on the current page.
        self.max_results = max_results
        # The token that is used to retrieve the next page of results. If this parameter is empty, all results have been returned.
        self.next_token = next_token
        # The total number of entries that meet the filter criteria. This parameter is optional and is not returned by default.
        self.total_count = total_count

    def validate(self):
        if self.content:
            for v1 in self.content:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Content'] = []
        if self.content is not None:
            for k1 in self.content:
                result['Content'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.content = []
        if m.get('Content') is not None:
            for k1 in m.get('Content'):
                temp_model = main_models.DescribeRulesResponseBodyDataContent()
                self.content.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeRulesResponseBodyDataContent(DaraModel):
    def __init__(
        self,
        check_failed_resource_count: int = None,
        check_status: str = None,
        check_time: int = None,
        product_type: str = None,
        resource_type: str = None,
        risky_resource_count: int = None,
        rule_id: str = None,
        rule_template: str = None,
        total_resource_count: int = None,
    ):
        # The number of resources for which the check failed.
        self.check_failed_resource_count = check_failed_resource_count
        # The check status. Valid values: NOT_CHECKED (Not checked), PASSED (Passed), FAILED (Failed), CHECKING (Checking), and CHECK_FAILED (Check failed).
        self.check_status = check_status
        # The UNIX timestamp that indicates when the check was performed.
        self.check_time = check_time
        # The product type to which the rule applies.
        self.product_type = product_type
        # The resource type to which the rule applies.
        self.resource_type = resource_type
        # The number of at-risk resources.
        self.risky_resource_count = risky_resource_count
        # The unique ID of the rule.
        self.rule_id = rule_id
        # The rule template.
        self.rule_template = rule_template
        # The total number of resources that were checked.
        self.total_resource_count = total_resource_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_failed_resource_count is not None:
            result['CheckFailedResourceCount'] = self.check_failed_resource_count

        if self.check_status is not None:
            result['CheckStatus'] = self.check_status

        if self.check_time is not None:
            result['CheckTime'] = self.check_time

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.risky_resource_count is not None:
            result['RiskyResourceCount'] = self.risky_resource_count

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.rule_template is not None:
            result['RuleTemplate'] = self.rule_template

        if self.total_resource_count is not None:
            result['TotalResourceCount'] = self.total_resource_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckFailedResourceCount') is not None:
            self.check_failed_resource_count = m.get('CheckFailedResourceCount')

        if m.get('CheckStatus') is not None:
            self.check_status = m.get('CheckStatus')

        if m.get('CheckTime') is not None:
            self.check_time = m.get('CheckTime')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('RiskyResourceCount') is not None:
            self.risky_resource_count = m.get('RiskyResourceCount')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('RuleTemplate') is not None:
            self.rule_template = m.get('RuleTemplate')

        if m.get('TotalResourceCount') is not None:
            self.total_resource_count = m.get('TotalResourceCount')

        return self

