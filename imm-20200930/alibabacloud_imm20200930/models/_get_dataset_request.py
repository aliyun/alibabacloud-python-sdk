# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetDatasetRequest(DaraModel):
    def __init__(
        self,
        dataset_name: str = None,
        project_name: str = None,
        with_statistics: bool = None,
    ):
        # The name of the dataset. For more information about how to obtain the dataset name, see [Create a dataset](https://help.aliyun.com/document_detail/478160.html).
        # 
        # This parameter is required.
        self.dataset_name = dataset_name
        # The name of the project. For more information about how to obtain the project name, see [Create a project](https://help.aliyun.com/document_detail/478153.html).
        # 
        # This parameter is required.
        self.project_name = project_name
        # Specifies whether to collect file statistics. Valid values:
        # - true: File statistics are collected. The FileCount and TotalFileSize fields in the Dataset struct are valid.
        # - false: File statistics are not collected. The FileCount and TotalFileSize fields in the Dataset struct may be incorrect or both 0.
        # Default value: false.
        self.with_statistics = with_statistics

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.with_statistics is not None:
            result['WithStatistics'] = self.with_statistics

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('WithStatistics') is not None:
            self.with_statistics = m.get('WithStatistics')

        return self

