# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribePolarClawSkillAssessmentResponseBody(DaraModel):
    def __init__(
        self,
        assessment_result: str = None,
        request_id: str = None,
    ):
        # The assessment result.
        self.assessment_result = assessment_result
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.assessment_result is not None:
            result['AssessmentResult'] = self.assessment_result

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssessmentResult') is not None:
            self.assessment_result = m.get('AssessmentResult')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

