# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryDatasetDetailInfoRequest(DaraModel):
    def __init__(
        self,
        dataset_id: str = None,
    ):
        # The ID of the training dataset that you want to remove from the specified custom linguistic model.
        # 
        # This parameter is required.
        self.dataset_id = dataset_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dataset_id is not None:
            result['DatasetId'] = self.dataset_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetId') is not None:
            self.dataset_id = m.get('DatasetId')

        return self

