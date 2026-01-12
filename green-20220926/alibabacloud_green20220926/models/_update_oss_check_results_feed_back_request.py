# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateOssCheckResultsFeedBackRequest(DaraModel):
    def __init__(
        self,
        feedback: str = None,
        query_request_id: str = None,
        region_id: str = None,
        service_code: str = None,
        task_id: str = None,
    ):
        self.feedback = feedback
        self.query_request_id = query_request_id
        self.region_id = region_id
        self.service_code = service_code
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.feedback is not None:
            result['Feedback'] = self.feedback

        if self.query_request_id is not None:
            result['QueryRequestId'] = self.query_request_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.service_code is not None:
            result['ServiceCode'] = self.service_code

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Feedback') is not None:
            self.feedback = m.get('Feedback')

        if m.get('QueryRequestId') is not None:
            self.query_request_id = m.get('QueryRequestId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

