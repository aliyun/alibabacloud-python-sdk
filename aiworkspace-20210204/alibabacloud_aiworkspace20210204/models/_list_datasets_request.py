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
        # Specifies the dataset\\"s visibility.
        # 
        # - `PUBLIC`: The dataset is publicly accessible.
        # 
        # - `PRIVATE`: The dataset is privately accessible.
        self.accessibility = accessibility
        # The data source type. To specify multiple types, separate them with commas (,). Valid values:
        # 
        # - `NAS`: The data source is NAS.
        # 
        # - `OSS`: The data source is OSS.
        self.data_source_types = data_source_types
        # The data type of the dataset. To specify multiple data types, separate them with commas (,). Valid values:
        # 
        # - `VIDEO`: video.
        # 
        # - `COMMON`: general.
        # 
        # - `TEXT`: text.
        # 
        # - `PIC`: image.
        # 
        # - `AUDIO`: audio.
        self.data_types = data_types
        # A comma-separated list of dataset IDs.
        self.dataset_ids = dataset_ids
        # The dataset edition. Valid values:
        # 
        # - `BASIC`: Basic edition. Does not support file metadata management.
        # 
        # - `ADVANCED`: Advanced edition. This edition is supported only for OSS datasets. Each version can manage metadata for up to 1 million files.
        # 
        # - `LOGICAL`: Logical edition. This edition is supported only for OSS datasets and is suitable for most use cases. Each version can manage metadata for up to 1 million files. You must use an SDK with this edition.
        self.edition = edition
        # A label used to filter datasets. The operation returns datasets whose label key or value contains the specified string.
        self.label = label
        # The dataset name. Fuzzy search is supported.
        self.name = name
        # The sort order for the results, based on the `SortBy` parameter. The default is `ASC`.
        # 
        # - `ASC`: ascending order.
        # 
        # - `DESC`: descending order.
        self.order = order
        # The page number for the paged query. Starts at 1. The default is 1.
        self.page_number = page_number
        # The number of datasets to return per page. The default is 10.
        self.page_size = page_size
        # The dataset properties. To specify multiple properties, separate them with commas (,). Valid values:
        # 
        # - `DIRECTORY`: A folder.
        # 
        # - `FILE`: A file.
        self.properties = properties
        # The dataset provider. Set this parameter to `pai` to query public datasets on the PAI platform.
        self.provider = provider
        # A filter for shared datasets.
        # 
        # - `TO_ME`: Returns only datasets shared with you.
        # 
        # - `BY_ME`: Returns only datasets that you have shared with others and displays details of the sharing configuration.
        # 
        # - If this parameter is omitted or empty, the operation returns all datasets in the current workspace, including those shared with you.
        self.share_scope = share_scope
        # The sort field.
        self.sort_by = sort_by
        # The source dataset ID for an iTAG annotation set.
        self.source_dataset_id = source_dataset_id
        # The source ID. The value of this parameter varies based on the `SourceTypes` value:
        # 
        # - If `SourceTypes` is `USER`, you can specify a custom value for `SourceId`.
        # 
        # - If `SourceTypes` is `ITAG`, `SourceId` is the ID of the iTAG task.
        # 
        # - If `SourceTypes` is `PAI_PUBLIC_DATASET`, this parameter is empty by default.
        self.source_id = source_id
        # The source type. To specify multiple types, separate them with commas (,).
        self.source_types = source_types
        # The ID of the workspace that contains the dataset. For information about how to obtain the workspace ID, see [ListWorkspaces](https://help.aliyun.com/document_detail/449124.html).
        # If this parameter is not specified, the default workspace is used. An error is returned if the default workspace does not exist.
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

