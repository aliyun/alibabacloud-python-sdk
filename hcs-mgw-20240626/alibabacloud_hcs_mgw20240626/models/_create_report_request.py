# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_hcs_mgw20240626 import models as main_models
from darabonba.model import DaraModel

class CreateReportRequest(DaraModel):
    def __init__(
        self,
        create_report: main_models.CreateReportInfo = None,
    ):
        # The details for creating the migration report.
        self.create_report = create_report

    def validate(self):
        if self.create_report:
            self.create_report.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_report is not None:
            result['CreateReport'] = self.create_report.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateReport') is not None:
            temp_model = main_models.CreateReportInfo()
            self.create_report = temp_model.from_map(m.get('CreateReport'))

        return self

