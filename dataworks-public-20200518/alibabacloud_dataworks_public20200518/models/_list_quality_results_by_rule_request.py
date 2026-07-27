# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListQualityResultsByRuleRequest(DaraModel):
    def __init__(
        self,
        end_date: str = None,
        page_number: int = None,
        page_size: int = None,
        project_id: int = None,
        project_name: str = None,
        rule_id: int = None,
        start_date: str = None,
    ):
        # The end of the time range to query. Specify the time in the yyyy-MM-dd HH:mm:ss format.
        # 
        # You must configure this parameter together with the StartDate parameter. The time range to query cannot exceed 7 days.
        # 
        # This parameter is required.
        self.end_date = end_date
        # The page number.
        # 
        # This parameter is required.
        self.page_number = page_number
        # The number of entries per page. Default value: 10. Maximum value: 20.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The ID of the DataWorks workspace.
        self.project_id = project_id
        # The name of the compute engine or data source for which you want to perform data quality monitoring.
        # 
        # This parameter is required.
        self.project_name = project_name
        # The ID of the monitoring rule. You can use the rule ID and a partition filter to query the monitoring results of the rule.
        # 
        # This parameter is required.
        self.rule_id = rule_id
        # The beginning of the time range to query. Specify the time in the yyyy-MM-dd HH:mm:ss format.
        # 
        # You must configure this parameter together with the EndDate parameter. The time range to query cannot exceed 7 days.
        # 
        # This parameter is required.
        self.start_date = start_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_date is not None:
            result['EndDate'] = self.end_date

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.start_date is not None:
            result['StartDate'] = self.start_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')

        return self

