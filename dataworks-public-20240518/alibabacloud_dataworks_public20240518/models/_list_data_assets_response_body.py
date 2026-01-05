# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class ListDataAssetsResponseBody(DaraModel):
    def __init__(
        self,
        paging_info: main_models.ListDataAssetsResponseBodyPagingInfo = None,
        request_id: str = None,
    ):
        # The pagination information.
        self.paging_info = paging_info
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.paging_info:
            self.paging_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.paging_info is not None:
            result['PagingInfo'] = self.paging_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PagingInfo') is not None:
            temp_model = main_models.ListDataAssetsResponseBodyPagingInfo()
            self.paging_info = temp_model.from_map(m.get('PagingInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListDataAssetsResponseBodyPagingInfo(DaraModel):
    def __init__(
        self,
        data_assets: List[main_models.ListDataAssetsResponseBodyPagingInfoDataAssets] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The data assets.
        self.data_assets = data_assets
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.data_assets:
            for v1 in self.data_assets:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DataAssets'] = []
        if self.data_assets is not None:
            for k1 in self.data_assets:
                result['DataAssets'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_assets = []
        if m.get('DataAssets') is not None:
            for k1 in m.get('DataAssets'):
                temp_model = main_models.ListDataAssetsResponseBodyPagingInfoDataAssets()
                self.data_assets.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListDataAssetsResponseBodyPagingInfoDataAssets(DaraModel):
    def __init__(
        self,
        data_asset_tag_mappings: List[main_models.ListDataAssetsResponseBodyPagingInfoDataAssetsDataAssetTagMappings] = None,
        env_type: str = None,
        id: str = None,
        name: str = None,
        project_id: int = None,
        type: str = None,
    ):
        # The mappings between data assets and tags.
        self.data_asset_tag_mappings = data_asset_tag_mappings
        # The environment of the workspace to which the data asset belongs. Valid values:
        # 
        # *   Dev: development environment
        # *   Prod: production environment
        self.env_type = env_type
        # The data asset ID.
        self.id = id
        # The name of the data asset.
        self.name = name
        # The DataWorks workspace ID.
        self.project_id = project_id
        # The type of the data asset. Valid values:
        # 
        # *   ACS::DataWorks::Table
        # *   ACS::DataWorks::Task
        self.type = type

    def validate(self):
        if self.data_asset_tag_mappings:
            for v1 in self.data_asset_tag_mappings:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DataAssetTagMappings'] = []
        if self.data_asset_tag_mappings is not None:
            for k1 in self.data_asset_tag_mappings:
                result['DataAssetTagMappings'].append(k1.to_map() if k1 else None)

        if self.env_type is not None:
            result['EnvType'] = self.env_type

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_asset_tag_mappings = []
        if m.get('DataAssetTagMappings') is not None:
            for k1 in m.get('DataAssetTagMappings'):
                temp_model = main_models.ListDataAssetsResponseBodyPagingInfoDataAssetsDataAssetTagMappings()
                self.data_asset_tag_mappings.append(temp_model.from_map(k1))

        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class ListDataAssetsResponseBodyPagingInfoDataAssetsDataAssetTagMappings(DaraModel):
    def __init__(
        self,
        auto_trace_enabled: bool = None,
        creator: str = None,
        data_asset_id: str = None,
        key: str = None,
        tag_source: str = None,
        value: str = None,
    ):
        # Indicates whether the lineage-based automatic backtrack feature is enabled for the mapping.
        self.auto_trace_enabled = auto_trace_enabled
        # The creator of the mapping between the data asset and the tag.
        self.creator = creator
        # The data asset ID.
        self.data_asset_id = data_asset_id
        # The tag key.
        self.key = key
        # The way in which the mapping between the data asset and the tag is created. Valid values:
        # 
        # *   System
        # *   UserDefined
        self.tag_source = tag_source
        # The tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_trace_enabled is not None:
            result['AutoTraceEnabled'] = self.auto_trace_enabled

        if self.creator is not None:
            result['Creator'] = self.creator

        if self.data_asset_id is not None:
            result['DataAssetId'] = self.data_asset_id

        if self.key is not None:
            result['Key'] = self.key

        if self.tag_source is not None:
            result['TagSource'] = self.tag_source

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoTraceEnabled') is not None:
            self.auto_trace_enabled = m.get('AutoTraceEnabled')

        if m.get('Creator') is not None:
            self.creator = m.get('Creator')

        if m.get('DataAssetId') is not None:
            self.data_asset_id = m.get('DataAssetId')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('TagSource') is not None:
            self.tag_source = m.get('TagSource')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

