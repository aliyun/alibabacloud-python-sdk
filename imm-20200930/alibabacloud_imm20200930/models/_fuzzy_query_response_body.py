# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_imm20200930 import models as main_models
from darabonba.model import DaraModel

class FuzzyQueryResponseBody(DaraModel):
    def __init__(
        self,
        files: List[main_models.File] = None,
        next_token: str = None,
        request_id: str = None,
        total_hits: int = None,
    ):
        # The list of file information.
        self.files = files
        # The token used for pagination when the total number of files exceeds the value of MaxResults.
        # 
        # When you list file information next time, set NextToken to this value to return the remaining results.
        # 
        # This parameter is returned only when not all files are returned.
        # 
        # This parameter is required.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # The number of matched records.
        self.total_hits = total_hits

    def validate(self):
        if self.files:
            for v1 in self.files:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Files'] = []
        if self.files is not None:
            for k1 in self.files:
                result['Files'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_hits is not None:
            result['TotalHits'] = self.total_hits

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.files = []
        if m.get('Files') is not None:
            for k1 in m.get('Files'):
                temp_model = main_models.File()
                self.files.append(temp_model.from_map(k1))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalHits') is not None:
            self.total_hits = m.get('TotalHits')

        return self

