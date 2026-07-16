# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeCheckDetailsRequest(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        resource_arn: str = None,
        rule_id: str = None,
    ):
        # The maximum number of entries to return on each page. The default value is 10.
        self.max_results = max_results
        # The token that is used to retrieve the next page of results. Set this parameter to the value of NextToken that is returned from the last API call. For more information about how to set this parameter, see the API description.
        self.next_token = next_token
        # The unique identifier of the resource.
        # 
        # This parameter is required.
        self.resource_arn = resource_arn
        # The unique ID of the data protection rule.
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.resource_arn is not None:
            result['ResourceArn'] = self.resource_arn

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('ResourceArn') is not None:
            self.resource_arn = m.get('ResourceArn')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        return self

