# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeInspectionTaskReportRequest(DaraModel):
    def __init__(
        self,
        inspection_ins_id: str = None,
        instance_id: str = None,
        level_summary: str = None,
        security_token: str = None,
        task_id: str = None,
    ):
        # The inspection instance ID.
        self.inspection_ins_id = inspection_ins_id
        # The assistant instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The summary of risk levels for inspection results. You can specify multiple values. Valid values:
        # - Normal: normal
        # - Warning: warning
        # - Error: high-risk
        # - Failed: failed
        self.level_summary = level_summary
        self.security_token = security_token
        # The task ID.
        # 
        # This parameter is required.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.inspection_ins_id is not None:
            result['InspectionInsId'] = self.inspection_ins_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.level_summary is not None:
            result['LevelSummary'] = self.level_summary

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InspectionInsId') is not None:
            self.inspection_ins_id = m.get('InspectionInsId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('LevelSummary') is not None:
            self.level_summary = m.get('LevelSummary')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

