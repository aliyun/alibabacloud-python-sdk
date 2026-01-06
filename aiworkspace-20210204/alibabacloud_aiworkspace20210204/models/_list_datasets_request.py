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
        self.accessibility = accessibility
        # The storage types of the data source. Multiple data source types are separated by commas (,). Valid values:
        # 
        # *   NAS: File Storage NAS (NAS).
        # *   OSS: Object Storage Service (OSS).
        self.data_source_types = data_source_types
        # The dataset types. Multiple dataset types are separated by commas (,). Valid values:
        # 
        # *   Video: video
        # *   COMMON: common
        # *   TEXT: text
        # *   PIC: picture
        # *   AUDIO: audio
        self.data_types = data_types
        self.edition = edition
        # The dataset tag, which is used to filter datasets. Datasets whose tag key or tag value contains a specified string are filtered.
        self.label = label
        # The dataset name. Fuzzy search based on the dataset name is supported.
        self.name = name
        # The order of specific fields of the entries on the returned page. Valid values: ASC and DESC. Default value: ASC.
        # 
        # *   ASC: The entries are sorted in ascending order.
        # *   DESC: The entries are sorted in descending order.
        self.order = order
        # The page number. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Default value: 10.
        self.page_size = page_size
        # The dataset properties. Multiple properties are separated by commas (,). Valid values:
        # 
        # *   DIRECTORY
        # *   FILE
        self.properties = properties
        # The dataset provider. If the value pai is returned, the dataset is a public dataset provided by PAI.
        self.provider = provider
        self.share_scope = share_scope
        # The field used for sorting.
        self.sort_by = sort_by
        # The ID of the iTAG labeled dataset that is used as the source dataset.
        self.source_dataset_id = source_dataset_id
        # The data source ID.
        # 
        # *   If SourceType is set to USER, the value of SourceId is a custom string.
        # *   If SourceType is set to ITAG, the value of SourceId is the ID of the labeling job of iTAG.
        # *   If SourceType is set to PAI_PUBLIC_DATASET, SourceId is empty by default.
        self.source_id = source_id
        # The source types. Multiple source types are separated by commas (,). Valid values:
        # 
        # *   PAI-PUBLIC-DATASET: a public dataset of Platform for AI (PAI).
        # *   ITAG: a dataset generated from a labeling job of iTAG.
        # *   USER: a dataset registered by a user.
        self.source_types = source_types
        # The ID of the workspace to which the dataset belongs. You can call [ListWorkspaces](https://help.aliyun.com/document_detail/449124.html) to obtain the workspace ID. If you do not specify this parameter, the default workspace is used. If the default workspace does not exist, an error is reported.
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

