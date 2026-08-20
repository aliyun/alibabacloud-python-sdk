# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetInspectionReportRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        report_type: str = None,
        task_id: str = None,
    ):
        # The instance ID. If this parameter is not specified, the entire report is returned. If this parameter is specified, only the content for the specified instance is returned.
        self.instance_id = instance_id
        self.report_type = report_type
        # The inspection report ID.
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
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.report_type is not None:
            result['ReportType'] = self.report_type

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('ReportType') is not None:
            self.report_type = m.get('ReportType')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

