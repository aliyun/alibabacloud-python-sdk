# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_imm20200930 import models as main_models
from darabonba.model import DaraModel

class ListBindingsResponseBody(DaraModel):
    def __init__(
        self,
        bindings: List[main_models.Binding] = None,
        next_token: str = None,
        request_id: str = None,
    ):
        # The bindings between the dataset and OSS buckets.
        self.bindings = bindings
        # *   The pagination token that is used in the next request to retrieve a new page of results if the total number of results exceeds the value of the MaxResults parameter.
        # *   The next request returns remaining results starting from the position marked by the NextToken parameter value.
        # *   This parameter has a non-empty value only when not all bindings are returned.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.bindings:
            for v1 in self.bindings:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Bindings'] = []
        if self.bindings is not None:
            for k1 in self.bindings:
                result['Bindings'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.bindings = []
        if m.get('Bindings') is not None:
            for k1 in m.get('Bindings'):
                temp_model = main_models.Binding()
                self.bindings.append(temp_model.from_map(k1))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

