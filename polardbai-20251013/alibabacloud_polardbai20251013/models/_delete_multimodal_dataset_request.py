# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteMultimodalDatasetRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        dataset_id: str = None,
        source_region_id: str = None,
    ):
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # This parameter is required.
        self.dataset_id = dataset_id
        self.source_region_id = source_region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.dataset_id is not None:
            result['DatasetId'] = self.dataset_id

        if self.source_region_id is not None:
            result['SourceRegionId'] = self.source_region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('DatasetId') is not None:
            self.dataset_id = m.get('DatasetId')

        if m.get('SourceRegionId') is not None:
            self.source_region_id = m.get('SourceRegionId')

        return self

