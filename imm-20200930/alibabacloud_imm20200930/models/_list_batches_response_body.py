# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_imm20200930 import models as main_models
from darabonba.model import DaraModel

class ListBatchesResponseBody(DaraModel):
    def __init__(
        self,
        batches: List[main_models.DataIngestion] = None,
        next_token: str = None,
        request_id: str = None,
    ):
        # The batch processing tasks.
        self.batches = batches
        # The pagination token.
        # 
        # The pagination token is used in the next request to retrieve a new page of results if the total number of results exceeds the value of the MaxResults parameter. The next call to the operation returns results lexicographically after the NextToken parameter value.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.batches:
            for v1 in self.batches:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Batches'] = []
        if self.batches is not None:
            for k1 in self.batches:
                result['Batches'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.batches = []
        if m.get('Batches') is not None:
            for k1 in m.get('Batches'):
                temp_model = main_models.DataIngestion()
                self.batches.append(temp_model.from_map(k1))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

