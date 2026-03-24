# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateSimQuestionResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        sim_question_id: int = None,
    ):
        self.request_id = request_id
        self.sim_question_id = sim_question_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.sim_question_id is not None:
            result['SimQuestionId'] = self.sim_question_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SimQuestionId') is not None:
            self.sim_question_id = m.get('SimQuestionId')

        return self

