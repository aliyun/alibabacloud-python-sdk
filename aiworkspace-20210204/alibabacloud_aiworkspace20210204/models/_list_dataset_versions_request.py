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
        # The dataset tag keys, which are used to filter datasets. Datasets whose tag keys or tag values contain a specified string are filtered.
        self.label_keys = label_keys
        # The dataset tag values, which are used to filter datasets. Datasets whose tag keys or tag values contain a specified string are filtered.
        self.label_values = label_values
        # The order in which the entries are sorted by the specific field on the returned page. Default value: ASC. Valid values:
        # 
        # *   ASC: ascending order
        # *   DESC: descending order.
        self.order = order
        # The page number. Pages start from page 1. Default value: 1.
        # 
        # This parameter is required.
        self.page_number = page_number
        # The number of entries per page. Default value: 10.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The dataset properties. Valid values:
        # 
        # *   DIRECTORY
        # *   FILE
        self.properties = properties
        # The field used to sort the results in queries by page. Default value: GmtCreateTime.
        # Valid values:
        # 
        # *   SourceType
        # *   DataSourceType
        # *   DataSize
        # *   DataCount
        # *   Property
        # *   GmtCreateTime: The results are sorted by creation time. This is the default value.
        # *   GmtModifiedTime: The results are sorted by modification time.
        # *   DatasetId
        self.sort_by = sort_by
        # The data source ID.
        # 
        # *   If SourceType is set to USER, the value of SourceId is a custom string.
        # *   If SourceType is set to ITAG, the value of SourceId is the ID of the labeling job of iTAG.
        # *   If SourceType is set to PAI_PUBLIC_DATASET, SourceId is empty by default.
        self.source_id = source_id
        # The source type. Valid values:
        # 
        # *   PAI-PUBLIC-DATASET: a public dataset of Platform for AI (PAI).
        # *   ITAG: a dataset generated from a labeling job of iTAG.
        # *   USER: a dataset registered by a user.
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

