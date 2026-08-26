# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDatasetsRequest(DaraModel):
    def __init__(
        self,
        accessibility: str = None,
        data_source_types: str = None,
        data_types: str = None,
        dataset_ids: str = None,
        edition: str = None,
        label: str = None,
        name: str = None,
        order: str = None,
        page_number: int = None,
        page_size: int = None,
        properties: str = None,
        provider: str = None,
        share_scope: str = None,
        sort_by: str = None,
        source_dataset_id: str = None,
        source_id: str = None,
        source_types: str = None,
        workspace_id: str = None,
    ):
        # The visibility of the dataset.
        # 
        # - PUBLIC: public.
        # - PRIVATE: private.
        self.accessibility = accessibility
        # The data source types. Separate multiple values with commas (,). Valid values:
        # - NAS: Alibaba Cloud Network Attached Storage (NAS).
        # - OSS: Alibaba Cloud Object Storage Service (OSS).
        self.data_source_types = data_source_types
        # The data types of the dataset. Separate multiple values with commas (,). Valid values:
        # - VIDEO: video.
        # - COMMON: common.
        # - TEXT: text.
        # - PIC: image.
        # - AUDIO: audio.
        self.data_types = data_types
        # The dataset IDs. You can specify multiple dataset IDs separated by commas (,).
        self.dataset_ids = dataset_ids
        # The dataset edition. Valid values:
        # 
        # - BASIC: Basic Edition. Does not support dataset file metadata management.
        # - ADVANCED: Advanced Edition. Supported only for OSS type. Each version supports up to 1 million file metadata entries.
        # - LOGICAL: Logical Edition. Supported only for OSS type. Each version supports up to 1 million file metadata entries. Applicable to most scenarios and requires the use of the SDK.
        self.edition = edition
        # The dataset label used to filter the dataset list. Datasets whose label key or value contains the specified string are returned.
        self.label = label
        # The dataset name. Fuzzy match is supported based on the dataset name.
        self.name = name
        # The sorting order for the specified sort field in paging queries. Default value: ASC.
        # - ASC: ascending order.
        # - DESC: descending order.
        self.order = order
        # The page number of the dataset list. Minimum value: 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page settings for paging queries. Default value: 10.
        self.page_size = page_size
        # The dataset properties. Separate multiple values with commas (,). Valid values:
        # - DIRECTORY: folder.
        # - FILE: file.
        self.properties = properties
        # The dataset provider. A value of "pai" indicates that the dataset is a PAI platform public dataset.
        self.provider = provider
        # The sharing filter for datasets:
        # * TO_ME: returns only datasets shared with you.
        # * BY_ME: returns only datasets you shared with others, with sharing configuration details displayed.
        # * If this parameter is not set or is set to empty: returns all datasets in the current workspace, including TO_ME.
        self.share_scope = share_scope
        # The field by which to sort the results.
        self.sort_by = sort_by
        # The source dataset ID of the iTAG annotation set.
        self.source_dataset_id = source_dataset_id
        # The data source ID.
        # - If SourceTypes is set to USER, you can customize the SourceId value.
        # - If SourceTypes is set to ITAG, which indicates a dataset generated from iTAG annotation results, SourceId is the iTAG task ID.
        # - If SourceTypes is set to PAI_PUBLIC_DATASET, which indicates a dataset created from a PAI public dataset, SourceId is empty by default.
        self.source_id = source_id
        # The source types. Separate multiple values with commas (,).
        self.source_types = source_types
        # The ID of the workspace where the dataset resides. For information about how to obtain the workspace ID, see [ListWorkspaces](https://help.aliyun.com/document_detail/449124.html).
        # If you do not specify this parameter, the default workspace is used. If the default workspace does not exist, an error is returned.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accessibility is not None:
            result['Accessibility'] = self.accessibility

        if self.data_source_types is not None:
            result['DataSourceTypes'] = self.data_source_types

        if self.data_types is not None:
            result['DataTypes'] = self.data_types

        if self.dataset_ids is not None:
            result['DatasetIds'] = self.dataset_ids

        if self.edition is not None:
            result['Edition'] = self.edition

        if self.label is not None:
            result['Label'] = self.label

        if self.name is not None:
            result['Name'] = self.name

        if self.order is not None:
            result['Order'] = self.order

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.properties is not None:
            result['Properties'] = self.properties

        if self.provider is not None:
            result['Provider'] = self.provider

        if self.share_scope is not None:
            result['ShareScope'] = self.share_scope

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        if self.source_dataset_id is not None:
            result['SourceDatasetId'] = self.source_dataset_id

        if self.source_id is not None:
            result['SourceId'] = self.source_id

        if self.source_types is not None:
            result['SourceTypes'] = self.source_types

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')

        if m.get('DataSourceTypes') is not None:
            self.data_source_types = m.get('DataSourceTypes')

        if m.get('DataTypes') is not None:
            self.data_types = m.get('DataTypes')

        if m.get('DatasetIds') is not None:
            self.dataset_ids = m.get('DatasetIds')

        if m.get('Edition') is not None:
            self.edition = m.get('Edition')

        if m.get('Label') is not None:
            self.label = m.get('Label')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Properties') is not None:
            self.properties = m.get('Properties')

        if m.get('Provider') is not None:
            self.provider = m.get('Provider')

        if m.get('ShareScope') is not None:
            self.share_scope = m.get('ShareScope')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        if m.get('SourceDatasetId') is not None:
            self.source_dataset_id = m.get('SourceDatasetId')

        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')

        if m.get('SourceTypes') is not None:
            self.source_types = m.get('SourceTypes')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

