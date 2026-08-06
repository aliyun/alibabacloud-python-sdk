# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class ListDataAssetsRequest(DaraModel):
    def __init__(
        self,
        asset_domain_id: int = None,
        category_uuid: str = None,
        data_asset_ids: List[str] = None,
        data_asset_type: str = None,
        env_type: str = None,
        name: str = None,
        page_number: int = None,
        page_size: int = None,
        project_id: int = None,
        tags: List[main_models.ListDataAssetsRequestTags] = None,
    ):
        # The ID of the asset domain.
        self.asset_domain_id = asset_domain_id
        # The ID of the asset category.
        self.category_uuid = category_uuid
        # The list of unique data asset IDs.
        self.data_asset_ids = data_asset_ids
        # The Asset Type of the data asset. Valid values:
        # 
        # - ACS::DataWorks::Table: data table.
        # 
        # - ACS::DataWorks::Task: scheduling node.
        self.data_asset_type = data_asset_type
        # The workspace environment to which the data asset belongs. Valid values:
        # - Dev: development environment.
        # - Prod: production environment.
        self.env_type = env_type
        # The name of the asset. Fuzzy search by name is supported.
        self.name = name
        # The page number. Pages start from 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Default value: 10. Maximum value: 100.
        self.page_size = page_size
        # The ID of the workspace.
        self.project_id = project_id
        # The list of tags associated with data assets. Tags are used as query filters:
        # - Multiple values have an OR relationship. For example, `["key1:v1", "key2:v1", "key3:v1"]` queries data assets that contain any one of the specified tags.
        # - If this parameter is not specified or is left empty, no tag-based filtering is applied.
        self.tags = tags

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.asset_domain_id is not None:
            result['AssetDomainId'] = self.asset_domain_id

        if self.category_uuid is not None:
            result['CategoryUuid'] = self.category_uuid

        if self.data_asset_ids is not None:
            result['DataAssetIds'] = self.data_asset_ids

        if self.data_asset_type is not None:
            result['DataAssetType'] = self.data_asset_type

        if self.env_type is not None:
            result['EnvType'] = self.env_type

        if self.name is not None:
            result['Name'] = self.name

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssetDomainId') is not None:
            self.asset_domain_id = m.get('AssetDomainId')

        if m.get('CategoryUuid') is not None:
            self.category_uuid = m.get('CategoryUuid')

        if m.get('DataAssetIds') is not None:
            self.data_asset_ids = m.get('DataAssetIds')

        if m.get('DataAssetType') is not None:
            self.data_asset_type = m.get('DataAssetType')

        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.ListDataAssetsRequestTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class ListDataAssetsRequestTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The custom tag key specified by the user.
        # 
        # The tag key can be up to 64 characters in length, cannot start with `dw:`, and supports only letters, digits, and the following special characters: `-@#*<>|[]()+=&%$!~`.
        self.key = key
        # The tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

