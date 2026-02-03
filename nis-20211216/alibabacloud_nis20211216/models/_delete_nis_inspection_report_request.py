# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteNisInspectionReportRequest(DaraModel):
    def __init__(
        self,
        inspection_report_id: str = None,
    ):
        # This parameter is required.
        self.inspection_report_id = inspection_report_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.inspection_report_id is not None:
            result['InspectionReportId'] = self.inspection_report_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InspectionReportId') is not None:
            self.inspection_report_id = m.get('InspectionReportId')

        return self

