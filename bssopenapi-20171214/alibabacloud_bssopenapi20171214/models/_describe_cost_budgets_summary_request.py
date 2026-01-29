# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeCostBudgetsSummaryRequest(DaraModel):
    def __init__(
        self,
        budget_name: str = None,
        budget_status: str = None,
        budget_type: str = None,
        max_results: int = None,
        next_token: str = None,
    ):
        # The name of the budget. Fuzzy match is supported.
        self.budget_name = budget_name
        # The status of the budget. Valid values: overdue and notOverdue. A value of overdue specifies to filter expired budgets. A value of notOverdue specifies to filter budgets that do not expire. By default, if you do not specify this parameter, information about all budgets is to be returned.
        self.budget_status = budget_status
        # The type of the budget. Valid values: cost, byquantity, and asset. A value of cost specifies to filter expense budgets. A value of byquantity specifies to filter budgets calculated based on the resource usage. A value of asset specifies to filter usage or coverage budgets. By default, information about all budgets is returned if you do not specify this parameter.
        self.budget_type = budget_type
        # The number of entries to return on each page. Default value: 10. Maximum value: 10. Minimum value: 1.
        self.max_results = max_results
        # The position in which the query starts. You must set this parameter to null or the token that is obtained from the previous query. Otherwise, an error is returned. If you set the NextToken parameter to null, the query starts from the beginning. The default value is null.
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.budget_name is not None:
            result['BudgetName'] = self.budget_name

        if self.budget_status is not None:
            result['BudgetStatus'] = self.budget_status

        if self.budget_type is not None:
            result['BudgetType'] = self.budget_type

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BudgetName') is not None:
            self.budget_name = m.get('BudgetName')

        if m.get('BudgetStatus') is not None:
            self.budget_status = m.get('BudgetStatus')

        if m.get('BudgetType') is not None:
            self.budget_type = m.get('BudgetType')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        return self

