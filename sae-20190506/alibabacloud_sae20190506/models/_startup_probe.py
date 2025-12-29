# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sae20190506 import models as main_models
from darabonba.model import DaraModel

class StartupProbe(DaraModel):
    def __init__(
        self,
        failure_threshold: int = None,
        initial_delay_seconds: int = None,
        period_seconds: int = None,
        probe_handler: main_models.ProbeHandler = None,
        timeout_seconds: int = None,
    ):
        self.failure_threshold = failure_threshold
        self.initial_delay_seconds = initial_delay_seconds
        self.period_seconds = period_seconds
        self.probe_handler = probe_handler
        self.timeout_seconds = timeout_seconds

    def validate(self):
        if self.probe_handler:
            self.probe_handler.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.failure_threshold is not None:
            result['FailureThreshold'] = self.failure_threshold

        if self.initial_delay_seconds is not None:
            result['InitialDelaySeconds'] = self.initial_delay_seconds

        if self.period_seconds is not None:
            result['PeriodSeconds'] = self.period_seconds

        if self.probe_handler is not None:
            result['ProbeHandler'] = self.probe_handler.to_map()

        if self.timeout_seconds is not None:
            result['TimeoutSeconds'] = self.timeout_seconds

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FailureThreshold') is not None:
            self.failure_threshold = m.get('FailureThreshold')

        if m.get('InitialDelaySeconds') is not None:
            self.initial_delay_seconds = m.get('InitialDelaySeconds')

        if m.get('PeriodSeconds') is not None:
            self.period_seconds = m.get('PeriodSeconds')

        if m.get('ProbeHandler') is not None:
            temp_model = main_models.ProbeHandler()
            self.probe_handler = temp_model.from_map(m.get('ProbeHandler'))

        if m.get('TimeoutSeconds') is not None:
            self.timeout_seconds = m.get('TimeoutSeconds')

        return self

