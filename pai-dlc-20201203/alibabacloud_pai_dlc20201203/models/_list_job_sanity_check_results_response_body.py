# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pai_dlc20201203 import models as main_models
from darabonba.model import DaraModel

class ListJobSanityCheckResultsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        sanity_check_results: List[List[main_models.SanityCheckResultItem]] = None,
        total_count: int = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The sanity check results.
        self.sanity_check_results = sanity_check_results
        # The total number of results that meet the filter conditions.
        self.total_count = total_count

    def validate(self):
        if self.sanity_check_results:
            for v1 in self.sanity_check_results:
                for v2 in v1:
                     if v2:
                        v2.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestID'] = self.request_id

        result['SanityCheckResults'] = []
        if self.sanity_check_results is not None:
            for k1 in self.sanity_check_results:
                l1 = []
                for k2 in k1:
                    l1.append(k2.to_map() if k2 else None)
                result['SanityCheckResults'].append(l1)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestID') is not None:
            self.request_id = m.get('RequestID')

        self.sanity_check_results = []
        if m.get('SanityCheckResults') is not None:
            for k1 in m.get('SanityCheckResults'):
                l1 = []
                for k2 in k1:
                    temp_model = main_models.SanityCheckResultItem()
                    l1.append(temp_model.from_map(k2))
                self.sanity_check_results.append(l1)

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

