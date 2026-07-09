# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteReportDefinitionRequest(DaraModel):
    def __init__(
        self,
        nbid: str = None,
        report_task_id: int = None,
    ):
        # The ID of the primary sales channel. If this parameter is left empty, the ID of the sales channel to which the current user belongs is used by default.
        self.nbid = nbid
        # The ID of the bill subscription task.
        # 
        # This parameter is required.
        self.report_task_id = report_task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.nbid is not None:
            result['Nbid'] = self.nbid

        if self.report_task_id is not None:
            result['ReportTaskId'] = self.report_task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Nbid') is not None:
            self.nbid = m.get('Nbid')

        if m.get('ReportTaskId') is not None:
            self.report_task_id = m.get('ReportTaskId')

        return self

