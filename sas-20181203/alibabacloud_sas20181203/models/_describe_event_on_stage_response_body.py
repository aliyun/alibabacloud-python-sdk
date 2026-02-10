# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeEventOnStageResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        security_event_stage_response: main_models.DescribeEventOnStageResponseBodySecurityEventStageResponse = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The platforms that are supported by the feature of container threat detection.
        self.security_event_stage_response = security_event_stage_response

    def validate(self):
        if self.security_event_stage_response:
            self.security_event_stage_response.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.security_event_stage_response is not None:
            result['SecurityEventStageResponse'] = self.security_event_stage_response.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SecurityEventStageResponse') is not None:
            temp_model = main_models.DescribeEventOnStageResponseBodySecurityEventStageResponse()
            self.security_event_stage_response = temp_model.from_map(m.get('SecurityEventStageResponse'))

        return self

class DescribeEventOnStageResponseBodySecurityEventStageResponse(DaraModel):
    def __init__(
        self,
        security_event_on_stag: Dict[str, Any] = None,
    ):
        # The platform that is supported by the feature of container threat detection. Valid values:
        # 
        # *   **container**
        # *   **linux**
        # *   **windows**
        self.security_event_on_stag = security_event_on_stag

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.security_event_on_stag is not None:
            result['SecurityEventOnStag'] = self.security_event_on_stag

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityEventOnStag') is not None:
            self.security_event_on_stag = m.get('SecurityEventOnStag')

        return self

