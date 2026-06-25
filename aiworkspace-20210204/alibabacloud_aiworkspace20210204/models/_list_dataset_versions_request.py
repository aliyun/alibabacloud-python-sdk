# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDatasetVersionsRequest(DaraModel):
    def __init__(
        self,
        label_keys: str = None,
        label_values: str = None,
        order: str = None,
        page_number: int = None,
        page_size: int = None,
        properties: str = None,
        sort_by: str = None,
        source_id: str = None,
        source_types: str = None,
    ):
        # The label keys used to filter the dataset list. Datasets are returned if their label keys contain the specified strings.
        self.label_keys = label_keys
        # The label values used to filter the dataset list. Datasets are returned if their label values contain the specified strings.
        self.label_values = label_values
        # The sort order for the paged query. The default value is ASC. Valid values:
        # 
        # - ASC: Ascending order.
        # 
        # - DESC: Descending order.
        self.order = order
        # The page number. The value starts from 1. The default is 1.
        # 
        # This parameter is required.
        self.page_number = page_number
        # The number of entries to return on each page. The default value is 10.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The dataset properties. Valid values:
        # 
        # - DIRECTORY: Folder.
        # 
        # - FILE: File.
        self.properties = properties
        # The field to use for sorting in a paged query. The default value is GmtCreateTime. Valid values:
        # 
        # - GmtCreateTime (default): Creation time.
        # 
        # - GmtModifiedTime: Modification time.
        # 
        # - SourceType
        # 
        # - DataSourceType
        # 
        # - Property
        # 
        # - DataSize
        # 
        # - DataCount
        self.sort_by = sort_by
        # The ID of the data source.
        # 
        # - If SourceTypes is USER, you can specify a custom ID.
        # 
        # - If SourceTypes is ITAG, this is the ID of the iTAG annotation task.
        # 
        # - If SourceTypes is PAI_PUBLIC_DATASET, this parameter is empty by default.
        self.source_id = source_id
        # The source type. Valid values:
        # 
        # - PAI-PUBLIC-DATASET: A public dataset from PAI.
        # 
        # - ITAG: A dataset generated from the annotation results of the iTAG module.
        # 
        # - USER: A dataset registered by a user.
        self.source_types = source_types

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.label_keys is not None:
            result['LabelKeys'] = self.label_keys

        if self.label_values is not None:
            result['LabelValues'] = self.label_values

        if self.order is not None:
            result['Order'] = self.order

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.properties is not None:
            result['Properties'] = self.properties

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        if self.source_id is not None:
            result['SourceId'] = self.source_id

        if self.source_types is not None:
            result['SourceTypes'] = self.source_types

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LabelKeys') is not None:
            self.label_keys = m.get('LabelKeys')

        if m.get('LabelValues') is not None:
            self.label_values = m.get('LabelValues')

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Properties') is not None:
            self.properties = m.get('Properties')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')

        if m.get('SourceTypes') is not None:
            self.source_types = m.get('SourceTypes')

        return self

