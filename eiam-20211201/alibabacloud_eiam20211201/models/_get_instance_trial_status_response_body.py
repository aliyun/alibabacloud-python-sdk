# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetInstanceTrialStatusResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        trial_status: bool = None,
    ):
        self.request_id = request_id
        self.trial_status = trial_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.trial_status is not None:
            result['TrialStatus'] = self.trial_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TrialStatus') is not None:
            self.trial_status = m.get('TrialStatus')

        return self

