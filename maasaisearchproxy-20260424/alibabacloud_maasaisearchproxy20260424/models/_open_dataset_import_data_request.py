# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from darabonba.model import DaraModel

class OpenDatasetImportDataRequest(DaraModel):
    def __init__(
        self,
        dataset_id: int = None,
        records: List[Dict[str, Any]] = None,
    ):
        # This parameter is required.
        self.dataset_id = dataset_id
        # This parameter is required.
        self.records = records

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dataset_id is not None:
            result['datasetId'] = self.dataset_id

        if self.records is not None:
            result['records'] = self.records

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('datasetId') is not None:
            self.dataset_id = m.get('datasetId')

        if m.get('records') is not None:
            self.records = m.get('records')

        return self

