# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListMultimodalSearchTaskRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        dataset_ids: List[str] = None,
        input_field: str = None,
        model_mode: str = None,
        page_number: int = None,
        page_size: int = None,
        source_region_id: str = None,
    ):
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        self.dataset_ids = dataset_ids
        self.input_field = input_field
        self.model_mode = model_mode
        self.page_number = page_number
        self.page_size = page_size
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

        if self.dataset_ids is not None:
            result['DatasetIds'] = self.dataset_ids

        if self.input_field is not None:
            result['InputField'] = self.input_field

        if self.model_mode is not None:
            result['ModelMode'] = self.model_mode

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.source_region_id is not None:
            result['SourceRegionId'] = self.source_region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('DatasetIds') is not None:
            self.dataset_ids = m.get('DatasetIds')

        if m.get('InputField') is not None:
            self.input_field = m.get('InputField')

        if m.get('ModelMode') is not None:
            self.model_mode = m.get('ModelMode')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SourceRegionId') is not None:
            self.source_region_id = m.get('SourceRegionId')

        return self

