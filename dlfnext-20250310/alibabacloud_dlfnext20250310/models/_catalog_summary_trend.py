# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dlfnext20250310 import models as main_models
from darabonba.model import DaraModel

class CatalogSummaryTrend(DaraModel):
    def __init__(
        self,
        api_visit_count: List[main_models.DateSummary] = None,
        file_access_count: List[main_models.DateSummary] = None,
        throughput: List[main_models.DateSummary] = None,
        total_file_count: List[main_models.DateSummary] = None,
        total_file_size_in_bytes: List[main_models.DateSummary] = None,
        total_meta_count: List[main_models.DateSummary] = None,
    ):
        # API visit count trends
        self.api_visit_count = api_visit_count
        # file access count trends
        self.file_access_count = file_access_count
        # Table count trends
        self.throughput = throughput
        # Historical total file count
        self.total_file_count = total_file_count
        # Database count trends
        self.total_file_size_in_bytes = total_file_size_in_bytes
        # Latest snapshot file count
        self.total_meta_count = total_meta_count

    def validate(self):
        if self.api_visit_count:
            for v1 in self.api_visit_count:
                 if v1:
                    v1.validate()
        if self.file_access_count:
            for v1 in self.file_access_count:
                 if v1:
                    v1.validate()
        if self.throughput:
            for v1 in self.throughput:
                 if v1:
                    v1.validate()
        if self.total_file_count:
            for v1 in self.total_file_count:
                 if v1:
                    v1.validate()
        if self.total_file_size_in_bytes:
            for v1 in self.total_file_size_in_bytes:
                 if v1:
                    v1.validate()
        if self.total_meta_count:
            for v1 in self.total_meta_count:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['apiVisitCount'] = []
        if self.api_visit_count is not None:
            for k1 in self.api_visit_count:
                result['apiVisitCount'].append(k1.to_map() if k1 else None)

        result['fileAccessCount'] = []
        if self.file_access_count is not None:
            for k1 in self.file_access_count:
                result['fileAccessCount'].append(k1.to_map() if k1 else None)

        result['throughput'] = []
        if self.throughput is not None:
            for k1 in self.throughput:
                result['throughput'].append(k1.to_map() if k1 else None)

        result['totalFileCount'] = []
        if self.total_file_count is not None:
            for k1 in self.total_file_count:
                result['totalFileCount'].append(k1.to_map() if k1 else None)

        result['totalFileSizeInBytes'] = []
        if self.total_file_size_in_bytes is not None:
            for k1 in self.total_file_size_in_bytes:
                result['totalFileSizeInBytes'].append(k1.to_map() if k1 else None)

        result['totalMetaCount'] = []
        if self.total_meta_count is not None:
            for k1 in self.total_meta_count:
                result['totalMetaCount'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.api_visit_count = []
        if m.get('apiVisitCount') is not None:
            for k1 in m.get('apiVisitCount'):
                temp_model = main_models.DateSummary()
                self.api_visit_count.append(temp_model.from_map(k1))

        self.file_access_count = []
        if m.get('fileAccessCount') is not None:
            for k1 in m.get('fileAccessCount'):
                temp_model = main_models.DateSummary()
                self.file_access_count.append(temp_model.from_map(k1))

        self.throughput = []
        if m.get('throughput') is not None:
            for k1 in m.get('throughput'):
                temp_model = main_models.DateSummary()
                self.throughput.append(temp_model.from_map(k1))

        self.total_file_count = []
        if m.get('totalFileCount') is not None:
            for k1 in m.get('totalFileCount'):
                temp_model = main_models.DateSummary()
                self.total_file_count.append(temp_model.from_map(k1))

        self.total_file_size_in_bytes = []
        if m.get('totalFileSizeInBytes') is not None:
            for k1 in m.get('totalFileSizeInBytes'):
                temp_model = main_models.DateSummary()
                self.total_file_size_in_bytes.append(temp_model.from_map(k1))

        self.total_meta_count = []
        if m.get('totalMetaCount') is not None:
            for k1 in m.get('totalMetaCount'):
                temp_model = main_models.DateSummary()
                self.total_meta_count.append(temp_model.from_map(k1))

        return self

