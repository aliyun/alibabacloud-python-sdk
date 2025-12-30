# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UploadOSSMultimodalDatasetRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        dataset_id: str = None,
        oss_url: str = None,
    ):
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        self.dataset_id = dataset_id
        self.oss_url = oss_url

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

        if self.oss_url is not None:
            result['OssUrl'] = self.oss_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('DatasetId') is not None:
            self.dataset_id = m.get('DatasetId')

        if m.get('OssUrl') is not None:
            self.oss_url = m.get('OssUrl')

        return self

