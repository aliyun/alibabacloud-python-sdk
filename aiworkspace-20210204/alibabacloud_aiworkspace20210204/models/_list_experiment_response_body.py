# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aiworkspace20210204 import models as main_models
from darabonba.model import DaraModel

class ListExperimentResponseBody(DaraModel):
    def __init__(
        self,
        experiments: List[main_models.Experiment] = None,
        next_page_token: int = None,
        total_count: int = None,
        request_id: str = None,
    ):
        # The list of experiments.
        self.experiments = experiments
        # The pagination token. It can be used in the next request to retrieve a new page of results.
        self.next_page_token = next_page_token
        # The total number of entries.
        self.total_count = total_count
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.experiments:
            for v1 in self.experiments:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Experiments'] = []
        if self.experiments is not None:
            for k1 in self.experiments:
                result['Experiments'].append(k1.to_map() if k1 else None)

        if self.next_page_token is not None:
            result['NextPageToken'] = self.next_page_token

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.experiments = []
        if m.get('Experiments') is not None:
            for k1 in m.get('Experiments'):
                temp_model = main_models.Experiment()
                self.experiments.append(temp_model.from_map(k1))

        if m.get('NextPageToken') is not None:
            self.next_page_token = m.get('NextPageToken')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

