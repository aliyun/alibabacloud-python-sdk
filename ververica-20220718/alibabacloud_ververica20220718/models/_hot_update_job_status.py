# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ververica20220718 import models as main_models
from darabonba.model import DaraModel

class HotUpdateJobStatus(DaraModel):
    def __init__(
        self,
        failure: main_models.HotUpdateJobFailureInfo = None,
        request_id: str = None,
        status: str = None,
    ):
        # The error message of the dynamical update.
        self.failure = failure
        # The request ID.
        self.request_id = request_id
        # The status of the dynamic update.
        self.status = status

    def validate(self):
        if self.failure:
            self.failure.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.failure is not None:
            result['failure'] = self.failure.to_map()

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('failure') is not None:
            temp_model = main_models.HotUpdateJobFailureInfo()
            self.failure = temp_model.from_map(m.get('failure'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

