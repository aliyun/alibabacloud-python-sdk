# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateProjectDefaultQuotaRequest(DaraModel):
    def __init__(
        self,
        quota: str = None,
    ):
        # The default computing quota that is used to allocate computing resources, the jobs that are initiated by this project consume the computing resources in the default quota.
        self.quota = quota

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.quota is not None:
            result['quota'] = self.quota

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('quota') is not None:
            self.quota = m.get('quota')

        return self

