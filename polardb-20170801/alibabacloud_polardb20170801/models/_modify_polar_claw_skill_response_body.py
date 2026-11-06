# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyPolarClawSkillResponseBody(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        evaluate_status: str = None,
        request_id: str = None,
        risk_detail: str = None,
    ):
        # The application ID.
        self.application_id = application_id
        # The evaluation status.
        self.evaluate_status = evaluate_status
        # The request ID.
        self.request_id = request_id
        # The baseline risk details.
        self.risk_detail = risk_detail

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.evaluate_status is not None:
            result['EvaluateStatus'] = self.evaluate_status

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.risk_detail is not None:
            result['RiskDetail'] = self.risk_detail

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('EvaluateStatus') is not None:
            self.evaluate_status = m.get('EvaluateStatus')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RiskDetail') is not None:
            self.risk_detail = m.get('RiskDetail')

        return self

