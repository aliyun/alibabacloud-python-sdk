# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DatasetProxyConfig(DaraModel):
    def __init__(
        self,
        dataset_type: str = None,
        source: str = None,
        source_dataset_id: str = None,
    ):
        # Dataset type. Only LABEL is supported.
        self.dataset_type = dataset_type
        # Dataset source. Only PAI is supported.
        self.source = source
        # Source dataset ID. For information about how to obtain a dataset ID, see [ListDatasets](https://help.aliyun.com/document_detail/457222.html).
        # 
        # This parameter is required.
        self.source_dataset_id = source_dataset_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dataset_type is not None:
            result['DatasetType'] = self.dataset_type

        if self.source is not None:
            result['Source'] = self.source

        if self.source_dataset_id is not None:
            result['SourceDatasetId'] = self.source_dataset_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetType') is not None:
            self.dataset_type = m.get('DatasetType')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('SourceDatasetId') is not None:
            self.source_dataset_id = m.get('SourceDatasetId')

        return self

