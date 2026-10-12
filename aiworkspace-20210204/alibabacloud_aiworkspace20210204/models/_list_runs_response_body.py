# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aiworkspace20210204 import models as main_models
from darabonba.model import DaraModel

class ListRunsResponseBody(DaraModel):
    def __init__(
        self,
        next_page_token: int = None,
        runs: List[main_models.Run] = None,
        total_count: int = None,
        request_id: str = None,
    ):
        # The pagination token. Pass an empty value for the first page query. The query result returns the token for the next page. A token value of 0 indicates that all data has been retrieved. You can obtain the token for the next page from the NextPageToken field in the response.
        self.next_page_token = next_page_token
        # The list of runs.
        self.runs = runs
        # The total number of records that match the request conditions. This is an optional parameter and may not be returned by default.
        self.total_count = total_count
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.runs:
            for v1 in self.runs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.next_page_token is not None:
            result['NextPageToken'] = self.next_page_token

        result['Runs'] = []
        if self.runs is not None:
            for k1 in self.runs:
                result['Runs'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextPageToken') is not None:
            self.next_page_token = m.get('NextPageToken')

        self.runs = []
        if m.get('Runs') is not None:
            for k1 in m.get('Runs'):
                temp_model = main_models.Run()
                self.runs.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

