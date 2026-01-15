# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateMultimodalDatasetEmbeddingRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        dataset_id: str = None,
        model: str = None,
        model_mode: str = None,
    ):
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # This parameter is required.
        self.dataset_id = dataset_id
        self.model = model
        self.model_mode = model_mode

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

        if self.model is not None:
            result['Model'] = self.model

        if self.model_mode is not None:
            result['ModelMode'] = self.model_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('DatasetId') is not None:
            self.dataset_id = m.get('DatasetId')

        if m.get('Model') is not None:
            self.model = m.get('Model')

        if m.get('ModelMode') is not None:
            self.model_mode = m.get('ModelMode')

        return self

