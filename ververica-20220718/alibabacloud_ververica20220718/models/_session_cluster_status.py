# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ververica20220718 import models as main_models
from darabonba.model import DaraModel

class SessionClusterStatus(DaraModel):
    def __init__(
        self,
        current_session_cluster_status: str = None,
        failure: main_models.SessionClusterFailureInfo = None,
        running: main_models.SessionClusterRunningInfo = None,
    ):
        self.current_session_cluster_status = current_session_cluster_status
        self.failure = failure
        self.running = running

    def validate(self):
        if self.failure:
            self.failure.validate()
        if self.running:
            self.running.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_session_cluster_status is not None:
            result['currentSessionClusterStatus'] = self.current_session_cluster_status

        if self.failure is not None:
            result['failure'] = self.failure.to_map()

        if self.running is not None:
            result['running'] = self.running.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('currentSessionClusterStatus') is not None:
            self.current_session_cluster_status = m.get('currentSessionClusterStatus')

        if m.get('failure') is not None:
            temp_model = main_models.SessionClusterFailureInfo()
            self.failure = temp_model.from_map(m.get('failure'))

        if m.get('running') is not None:
            temp_model = main_models.SessionClusterRunningInfo()
            self.running = temp_model.from_map(m.get('running'))

        return self

