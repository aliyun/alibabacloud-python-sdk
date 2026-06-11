# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class AddContextsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        results: List[main_models.AddContextsResponseBodyResults] = None,
    ):
        # The unique ID for the request.
        self.request_id = request_id
        # An array of objects containing the results of the write operation.
        self.results = results

    def validate(self):
        if self.results:
            for v1 in self.results:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['requestId'] = self.request_id

        result['results'] = []
        if self.results is not None:
            for k1 in self.results:
                result['results'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        self.results = []
        if m.get('results') is not None:
            for k1 in m.get('results'):
                temp_model = main_models.AddContextsResponseBodyResults()
                self.results.append(temp_model.from_map(k1))

        return self

class AddContextsResponseBodyResults(DaraModel):
    def __init__(
        self,
        context_id: str = None,
        status: str = None,
    ):
        # The ID of the written record or event.
        self.context_id = context_id
        # The write status. Can be "accepted", "queued", or "created".
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.context_id is not None:
            result['contextId'] = self.context_id

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('contextId') is not None:
            self.context_id = m.get('contextId')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

