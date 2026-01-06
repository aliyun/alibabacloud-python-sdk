# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aiworkspace20210204 import models as main_models
from darabonba.model import DaraModel

class GetDatasetFileMetasStatisticsResponseBody(DaraModel):
    def __init__(
        self,
        dataset_file_metas_stats: List[main_models.DatasetFileMetasStat] = None,
        total_count: int = None,
        request_id: str = None,
    ):
        # The details of the returned aggregation list, including the number of each aggregate item. The list is by default sorted in descending order based on the count number.
        self.dataset_file_metas_stats = dataset_file_metas_stats
        # The returned number. Example: the number of metadata records or the number of user-defined tags.
        self.total_count = total_count
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.dataset_file_metas_stats:
            for v1 in self.dataset_file_metas_stats:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DatasetFileMetasStats'] = []
        if self.dataset_file_metas_stats is not None:
            for k1 in self.dataset_file_metas_stats:
                result['DatasetFileMetasStats'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dataset_file_metas_stats = []
        if m.get('DatasetFileMetasStats') is not None:
            for k1 in m.get('DatasetFileMetasStats'):
                temp_model = main_models.DatasetFileMetasStat()
                self.dataset_file_metas_stats.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

