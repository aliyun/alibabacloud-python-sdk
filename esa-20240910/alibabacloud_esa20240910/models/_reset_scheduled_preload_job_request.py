# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ResetScheduledPreloadJobRequest(DaraModel):
    def __init__(
        self,
        id: str = None,
    ):
        # The scheduled preload job ID.
        # >Notice: The scheduled preload job ID. This parameter is required. You can obtain the ID from the response of CreateScheduledPreloadJob after creating a job, or query existing job IDs by calling GetScheduledPreloadJob or ListScheduledPreloadJobs.
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        return self

