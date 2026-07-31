# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_adb20211201 import models as main_models
from darabonba.model import DaraModel

class GetKnowledgeRecallResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetKnowledgeRecallResponseBodyData = None,
        request_id: str = None,
    ):
        # The returned data.
        self.data = data
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.GetKnowledgeRecallResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetKnowledgeRecallResponseBodyData(DaraModel):
    def __init__(
        self,
        count: int = None,
        message: str = None,
        results: List[Dict[str, Any]] = None,
        trace_id: str = None,
    ):
        # The total number of results.
        self.count = count
        # The prompt message.
        self.message = message
        # The recall results.
        self.results = results
        # The Tracing Analysis ID.
        self.trace_id = trace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.message is not None:
            result['Message'] = self.message

        if self.results is not None:
            result['Results'] = self.results

        if self.trace_id is not None:
            result['TraceId'] = self.trace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Results') is not None:
            self.results = m.get('Results')

        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')

        return self

