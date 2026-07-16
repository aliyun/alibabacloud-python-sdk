# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetDatasetResourceUrlRequest(DaraModel):
    def __init__(
        self,
        dataset_id: str = None,
        primary_key: str = None,
    ):
        # The dataset ID. You can view this in the dataset list on the console.
        self.dataset_id = dataset_id
        # The primary key value of the data record in the dataset.
        # 
        # This parameter is required.
        self.primary_key = primary_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dataset_id is not None:
            result['datasetId'] = self.dataset_id

        if self.primary_key is not None:
            result['primaryKey'] = self.primary_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('datasetId') is not None:
            self.dataset_id = m.get('datasetId')

        if m.get('primaryKey') is not None:
            self.primary_key = m.get('primaryKey')

        return self

