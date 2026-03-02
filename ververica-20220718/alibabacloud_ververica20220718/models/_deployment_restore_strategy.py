# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeploymentRestoreStrategy(DaraModel):
    def __init__(
        self,
        allow_non_restored_state: bool = None,
        job_start_time_in_ms: int = None,
        kind: str = None,
        savepoint_id: str = None,
    ):
        # Specifies whether to allow specific operator states to be skipped. This parameter is required only when a Python deployment or a JAR deployment is resumed with state data.
        self.allow_non_restored_state = allow_non_restored_state
        # The time point at which the deployment is started without states. You must enter a 13-digit timestamp. If you set the kind parameter to NONE, you can configure this parameter to allow all source tables for which the startTime parameter is configured to read data from the specified time point.
        self.job_start_time_in_ms = job_start_time_in_ms
        # The type of the start offset. Valid values:
        # 
        # *   NONE: The deployment is started without states.
        # *   LATEST_SAVEPOINT: The deployment is started from the latest savepoint.
        # *   FROM_SAVEPOINT: The deployment is started from the specified savepoint.
        # *   LATEST_STATE: The deployment is started from the latest state of the deployment.
        self.kind = kind
        # The ID of the savepoint for starting the deployment. This parameter is required when the kind parameter is set to FROM_SAVEPOINT.
        self.savepoint_id = savepoint_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allow_non_restored_state is not None:
            result['allowNonRestoredState'] = self.allow_non_restored_state

        if self.job_start_time_in_ms is not None:
            result['jobStartTimeInMs'] = self.job_start_time_in_ms

        if self.kind is not None:
            result['kind'] = self.kind

        if self.savepoint_id is not None:
            result['savepointId'] = self.savepoint_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('allowNonRestoredState') is not None:
            self.allow_non_restored_state = m.get('allowNonRestoredState')

        if m.get('jobStartTimeInMs') is not None:
            self.job_start_time_in_ms = m.get('jobStartTimeInMs')

        if m.get('kind') is not None:
            self.kind = m.get('kind')

        if m.get('savepointId') is not None:
            self.savepoint_id = m.get('savepointId')

        return self

