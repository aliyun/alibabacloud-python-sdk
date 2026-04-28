# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_pds20220301 import models as main_models
from darabonba.model import DaraModel

class BatchResponseBody(DaraModel):
    def __init__(
        self,
        responses: List[main_models.BatchResponseBodyResponses] = None,
    ):
        # All responses of the child requests.
        self.responses = responses

    def validate(self):
        if self.responses:
            for v1 in self.responses:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['responses'] = []
        if self.responses is not None:
            for k1 in self.responses:
                result['responses'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.responses = []
        if m.get('responses') is not None:
            for k1 in m.get('responses'):
                temp_model = main_models.BatchResponseBodyResponses()
                self.responses.append(temp_model.from_map(k1))

        return self

class BatchResponseBodyResponses(DaraModel):
    def __init__(
        self,
        body: Dict[str, Any] = None,
        id: str = None,
        status: int = None,
    ):
        # The response parameters of a child request. For more information, see the topic of the corresponding child request.
        self.body = body
        # The ID of the child request. The ID is used to associate a child request with a response.
        self.id = id
        # The returned HTTP status code of a child request. For more information, see the topic of the corresponding child request.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.body is not None:
            result['body'] = self.body

        if self.id is not None:
            result['id'] = self.id

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

