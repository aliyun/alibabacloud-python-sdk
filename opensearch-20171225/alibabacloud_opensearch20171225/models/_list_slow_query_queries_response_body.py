# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_opensearch20171225 import models as main_models
from darabonba.model import DaraModel

class ListSlowQueryQueriesResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: main_models.ListSlowQueryQueriesResponseBodyResult = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The return result.
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
            temp_model = main_models.ListSlowQueryQueriesResponseBodyResult()
            self.result = temp_model.from_map(m.get('result'))

        return self

class ListSlowQueryQueriesResponseBodyResult(DaraModel):
    def __init__(
        self,
        app_query: str = None,
        end: int = None,
        index: int = None,
        start: int = None,
    ):
        # The content of the optimization suggestion for the query.
        self.app_query = app_query
        # The end of the time range that was queried.
        self.end = end
        # The ID of the optimization suggestion.
        self.index = index
        # The beginning of the time range that was queried.
        self.start = start

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_query is not None:
            result['appQuery'] = self.app_query

        if self.end is not None:
            result['end'] = self.end

        if self.index is not None:
            result['index'] = self.index

        if self.start is not None:
            result['start'] = self.start

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appQuery') is not None:
            self.app_query = m.get('appQuery')

        if m.get('end') is not None:
            self.end = m.get('end')

        if m.get('index') is not None:
            self.index = m.get('index')

        if m.get('start') is not None:
            self.start = m.get('start')

        return self

