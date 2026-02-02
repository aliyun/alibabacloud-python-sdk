# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_hcs_mgw20240626 import models as main_models
from darabonba.model import DaraModel

class GetReportResponseBody(DaraModel):
    def __init__(
        self,
        get_report_response: main_models.GetReportResp = None,
    ):
        # The details for obtaining the migration report.
        self.get_report_response = get_report_response

    def validate(self):
        if self.get_report_response:
            self.get_report_response.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.get_report_response is not None:
            result['GetReportResponse'] = self.get_report_response.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GetReportResponse') is not None:
            temp_model = main_models.GetReportResp()
            self.get_report_response = temp_model.from_map(m.get('GetReportResponse'))

        return self

