# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DetachDataQualityRulesFromEvaluationTaskRequest(DaraModel):
    def __init__(
        self,
        data_quality_evaluation_task_id: int = None,
        data_quality_rule_ids: List[int] = None,
        project_id: int = None,
    ):
        # The ID of the data quality monitoring task that is associated with the rule.
        # 
        # This parameter is required.
        self.data_quality_evaluation_task_id = data_quality_evaluation_task_id
        # The IDs of the monitoring rules.
        # 
        # This parameter is required.
        self.data_quality_rule_ids = data_quality_rule_ids
        # The ID of the DataWorks workspace. You can log on to the [DataWorks console](https://workbench.data.aliyun.com/console) and go to the workspace configuration page to obtain the workspace ID.
        # 
        # This parameter is required.
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_quality_evaluation_task_id is not None:
            result['DataQualityEvaluationTaskId'] = self.data_quality_evaluation_task_id

        if self.data_quality_rule_ids is not None:
            result['DataQualityRuleIds'] = self.data_quality_rule_ids

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataQualityEvaluationTaskId') is not None:
            self.data_quality_evaluation_task_id = m.get('DataQualityEvaluationTaskId')

        if m.get('DataQualityRuleIds') is not None:
            self.data_quality_rule_ids = m.get('DataQualityRuleIds')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        return self

