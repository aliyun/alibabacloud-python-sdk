# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PublishRecallManagementTableResponseBody(DaraModel):
    def __init__(
        self,
        recall_management_job_id: str = None,
        request_id: str = None,
    ):
        self.recall_management_job_id = recall_management_job_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.recall_management_job_id is not None:
            result['RecallManagementJobId'] = self.recall_management_job_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RecallManagementJobId') is not None:
            self.recall_management_job_id = m.get('RecallManagementJobId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

