# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_opensearch20171225 import models as main_models
from darabonba.model import DaraModel

class ListSlowQueryCategoriesResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: main_models.ListSlowQueryCategoriesResponseBodyResult = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The returned data.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.result is not None:
            result['result'] = self.result.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('result') is not None:
            temp_model = main_models.ListSlowQueryCategoriesResponseBodyResult()
            self.result = temp_model.from_map(m.get('result'))

        return self

class ListSlowQueryCategoriesResponseBodyResult(DaraModel):
    def __init__(
        self,
        analyze_status: str = None,
        end: int = None,
        start: int = None,
    ):
        # The analysis status.
        # 
        # - PENDING: The analysis is being prepared.
        # 
        # - SUCCESS: The analysis is successful.
        # 
        # - RUNNING: The analysis is in progress.
        # 
        # - FAILED: The analysis failed.
        # 
        # - N/A: The analysis status is unknown.
        self.analyze_status = analyze_status
        # The end timestamp.
        self.end = end
        # The start timestamp.
        self.start = start

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.analyze_status is not None:
            result['analyzeStatus'] = self.analyze_status

        if self.end is not None:
            result['end'] = self.end

        if self.start is not None:
            result['start'] = self.start

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('analyzeStatus') is not None:
            self.analyze_status = m.get('analyzeStatus')

        if m.get('end') is not None:
            self.end = m.get('end')

        if m.get('start') is not None:
            self.start = m.get('start')

        return self

