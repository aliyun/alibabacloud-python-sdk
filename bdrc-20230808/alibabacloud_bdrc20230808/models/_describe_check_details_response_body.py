# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bdrc20230808 import models as main_models
from darabonba.model import DaraModel

class DescribeCheckDetailsResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.DescribeCheckDetailsResponseBodyData = None,
        request_id: str = None,
    ):
        # The data returned.
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
            temp_model = main_models.DescribeCheckDetailsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeCheckDetailsResponseBodyData(DaraModel):
    def __init__(
        self,
        content: List[main_models.DescribeCheckDetailsResponseBodyDataContent] = None,
        max_results: int = None,
        next_token: str = None,
        total_count: int = None,
    ):
        # The collection of records returned by this request.
        self.content = content
        # The maximum number of entries returned in this response.
        self.max_results = max_results
        # The token that is used to retrieve the next page of results. If this parameter is empty, it indicates that all data has been retrieved.
        self.next_token = next_token
        # The total number of entries that meet the query conditions. This parameter is optional and is not returned by default.
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
                temp_model = main_models.DescribeCheckDetailsResponseBodyDataContent()
                self.content.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeCheckDetailsResponseBodyDataContent(DaraModel):
    def __init__(
        self,
        check_status: str = None,
        check_time: int = None,
        detail: str = None,
        product_type: str = None,
        resource_arn: str = None,
        resource_id: str = None,
        resource_name: str = None,
        resource_owner_id: int = None,
        resource_type: str = None,
        rule_id: str = None,
        rule_template: str = None,
    ):
        # The check status. Valid values: NOT_CHECKED, PASSED, FAILED, CHECKING, and CHECK_FAILED.
        self.check_status = check_status
        # The time when the check was performed.
        self.check_time = check_time
        # The check details.
        self.detail = detail
        # The type of the cloud service.
        self.product_type = product_type
        # The globally unique Alibaba Cloud Resource Name (ARN) of the resource.
        self.resource_arn = resource_arn
        # The unique ID of the resource.
        self.resource_id = resource_id
        # The name of the resource.
        self.resource_name = resource_name
        # The ID of the resource owner.
        self.resource_owner_id = resource_owner_id
        # The type of the resource.
        self.resource_type = resource_type
        # The unique ID of the rule.
        self.rule_id = rule_id
        # The rule template.
        self.rule_template = rule_template

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_status is not None:
            result['CheckStatus'] = self.check_status

        if self.check_time is not None:
            result['CheckTime'] = self.check_time

        if self.detail is not None:
            result['Detail'] = self.detail

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        if self.resource_arn is not None:
            result['ResourceArn'] = self.resource_arn

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.rule_template is not None:
            result['RuleTemplate'] = self.rule_template

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckStatus') is not None:
            self.check_status = m.get('CheckStatus')

        if m.get('CheckTime') is not None:
            self.check_time = m.get('CheckTime')

        if m.get('Detail') is not None:
            self.detail = m.get('Detail')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        if m.get('ResourceArn') is not None:
            self.resource_arn = m.get('ResourceArn')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('RuleTemplate') is not None:
            self.rule_template = m.get('RuleTemplate')

        return self

