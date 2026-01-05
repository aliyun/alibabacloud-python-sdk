# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDataQualityRulesRequest(DaraModel):
    def __init__(
        self,
        data_quality_evaluation_task_id: int = None,
        name: str = None,
        page_number: int = None,
        page_size: int = None,
        project_id: int = None,
        table_guid: str = None,
    ):
        # The ID of the data quality monitoring task that is associated with the rule.
        self.data_quality_evaluation_task_id = data_quality_evaluation_task_id
        # The name of the rule. Fuzzy match is supported.
        self.name = name
        # The page number. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Default value: 10. Maximum value: 200.
        self.page_size = page_size
        # The DataWorks workspace ID.
        self.project_id = project_id
        # The ID of the table that is limited by the rule in Data Map.
        self.table_guid = table_guid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_quality_evaluation_task_id is not None:
            result['DataQualityEvaluationTaskId'] = self.data_quality_evaluation_task_id

        if self.name is not None:
            result['Name'] = self.name

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.table_guid is not None:
            result['TableGuid'] = self.table_guid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataQualityEvaluationTaskId') is not None:
            self.data_quality_evaluation_task_id = m.get('DataQualityEvaluationTaskId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('TableGuid') is not None:
            self.table_guid = m.get('TableGuid')

        return self

