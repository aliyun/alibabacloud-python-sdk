# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_imm20200930 import models as main_models
from darabonba.model import DaraModel

class ListDatasetsResponseBody(DaraModel):
    def __init__(
        self,
        datasets: List[main_models.Dataset] = None,
        next_token: str = None,
        request_id: str = None,
    ):
        # The datasets.
        self.datasets = datasets
        # The pagination token. If the total number of datasets is greater than the value of MaxResults, you must specify this parameter. This parameter has a value only if not all the datasets that meet the conditions are returned.
        # 
        # Pass this value as the value of NextToken in the next call to query subsequent datasets.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.datasets:
            for v1 in self.datasets:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Datasets'] = []
        if self.datasets is not None:
            for k1 in self.datasets:
                result['Datasets'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.datasets = []
        if m.get('Datasets') is not None:
            for k1 in m.get('Datasets'):
                temp_model = main_models.Dataset()
                self.datasets.append(temp_model.from_map(k1))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

