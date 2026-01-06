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
        # The pagination token that is used to retrieve the next page. You do not need to specify this parameter for the first request. You must specify the pagination token in the result of the previous query. If the pagination token is 0, no next page exists. You can obtain the pagination token that is used to retrieve the next page in the value of the **NextPageToken** field.
        self.next_page_token = next_page_token
        # The runs.
        self.runs = runs
        # The total number of entries returned. By default, this parameter is not returned.
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

