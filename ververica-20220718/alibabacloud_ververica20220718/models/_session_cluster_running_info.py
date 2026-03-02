# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class SessionClusterRunningInfo(DaraModel):
    def __init__(
        self,
        last_update_time: int = None,
        reference_deployment_ids: List[str] = None,
        started_at: int = None,
    ):
        self.last_update_time = last_update_time
        self.reference_deployment_ids = reference_deployment_ids
        self.started_at = started_at

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.last_update_time is not None:
            result['lastUpdateTime'] = self.last_update_time

        if self.reference_deployment_ids is not None:
            result['referenceDeploymentIds'] = self.reference_deployment_ids

        if self.started_at is not None:
            result['startedAt'] = self.started_at

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('lastUpdateTime') is not None:
            self.last_update_time = m.get('lastUpdateTime')

        if m.get('referenceDeploymentIds') is not None:
            self.reference_deployment_ids = m.get('referenceDeploymentIds')

        if m.get('startedAt') is not None:
            self.started_at = m.get('startedAt')

        return self

