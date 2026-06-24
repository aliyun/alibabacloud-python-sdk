# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListEvaluationScoreHistoryRequest(DaraModel):
    def __init__(
        self,
        account_id: int = None,
        end_date: str = None,
        evaluation_domain: str = None,
        region_id: str = None,
        start_date: str = None,
    ):
        # The ID of the member accounts. This parameter is applicable only to the multi-account detection pattern.
        self.account_id = account_id
        # The end date of the query. Format: YYYY-MM-DD.
        # 
        # By default, the historical scores from the last 7 days are returned.
        self.end_date = end_date
        self.evaluation_domain = evaluation_domain
        # The region ID.
        self.region_id = region_id
        # The start date of the query. Format: YYYY-MM-DD.
        # 
        # You can query records from the last 180 days.
        self.start_date = start_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['AccountId'] = self.account_id

        if self.end_date is not None:
            result['EndDate'] = self.end_date

        if self.evaluation_domain is not None:
            result['EvaluationDomain'] = self.evaluation_domain

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.start_date is not None:
            result['StartDate'] = self.start_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')

        if m.get('EvaluationDomain') is not None:
            self.evaluation_domain = m.get('EvaluationDomain')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')

        return self

