# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteQualityRuleRequest(DaraModel):
    def __init__(
        self,
        project_id: int = None,
        project_name: str = None,
        rule_id: int = None,
    ):
        # The ID of the DataWorks workspace. You can log on to the DataWorks console and go to the Workspace Management page to obtain the workspace ID.
        self.project_id = project_id
        # The name of the compute engine or data source.
        # 
        # This parameter is required.
        self.project_name = project_name
        # The ID of the data quality rule.
        # 
        # This parameter is required.
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        return self

