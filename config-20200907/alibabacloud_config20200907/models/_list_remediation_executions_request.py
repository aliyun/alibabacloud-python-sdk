# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListRemediationExecutionsRequest(DaraModel):
    def __init__(
        self,
        config_rule_id: str = None,
        execution_status: str = None,
        max_results: int = None,
        next_token: str = None,
    ):
        # The rule ID.
        # 
        # This parameter is required.
        self.config_rule_id = config_rule_id
        # The status of the remediation. Valid values:
        # 
        # *   Success
        # *   Failed
        self.execution_status = execution_status
        # The maximum number of entries to return for a single request. Valid values: 10 to 100.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request. You must specify the token that is obtained from the previous query as the value of NextToken.
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_rule_id is not None:
            result['ConfigRuleId'] = self.config_rule_id

        if self.execution_status is not None:
            result['ExecutionStatus'] = self.execution_status

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigRuleId') is not None:
            self.config_rule_id = m.get('ConfigRuleId')

        if m.get('ExecutionStatus') is not None:
            self.execution_status = m.get('ExecutionStatus')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        return self

