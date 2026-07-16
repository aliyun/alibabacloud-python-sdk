# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_eventbridge20200401 import models as main_models
from darabonba.model import DaraModel

class QueryAttachment(DaraModel):
    def __init__(
        self,
        query: str = None,
        result: main_models.ExecutionResult = None,
    ):
        self.query = query
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.query is not None:
            result['Query'] = self.query

        if self.result is not None:
            result['Result'] = self.result.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Query') is not None:
            self.query = m.get('Query')

        if m.get('Result') is not None:
            temp_model = main_models.ExecutionResult()
            self.result = temp_model.from_map(m.get('Result'))

        return self

