# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_csas20230120 import models as main_models
from darabonba.model import DaraModel

class RecoveryContent(DaraModel):
    def __init__(
        self,
        auth_report_interval: main_models.AuthReportInterval = None,
        recovery_actions: List[str] = None,
    ):
        self.auth_report_interval = auth_report_interval
        # This parameter is required.
        self.recovery_actions = recovery_actions

    def validate(self):
        if self.auth_report_interval:
            self.auth_report_interval.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_report_interval is not None:
            result['AuthReportInterval'] = self.auth_report_interval.to_map()

        if self.recovery_actions is not None:
            result['RecoveryActions'] = self.recovery_actions

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthReportInterval') is not None:
            temp_model = main_models.AuthReportInterval()
            self.auth_report_interval = temp_model.from_map(m.get('AuthReportInterval'))

        if m.get('RecoveryActions') is not None:
            self.recovery_actions = m.get('RecoveryActions')

        return self

