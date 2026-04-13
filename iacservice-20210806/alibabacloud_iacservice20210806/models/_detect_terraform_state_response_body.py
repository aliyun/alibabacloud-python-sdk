# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DetectTerraformStateResponseBody(DaraModel):
    def __init__(
        self,
        detection_id: str = None,
        request_id: str = None,
    ):
        self.detection_id = detection_id
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.detection_id is not None:
            result['detectionId'] = self.detection_id

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('detectionId') is not None:
            self.detection_id = m.get('detectionId')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

