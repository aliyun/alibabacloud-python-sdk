# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class ListVodPackagingAssetsResponseBody(DaraModel):
    def __init__(
        self,
        assets: List[main_models.ListVodPackagingAssetsResponseBodyAssets] = None,
        page_no: int = None,
        page_size: int = None,
        request_id: str = None,
        sort_by: str = None,
        total_count: int = None,
    ):
        # The VOD packaging assets.
        self.assets = assets
        # The page number. Default value: 1.
        self.page_no = page_no
        # The number of entries per page. Default value: 10.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The sorting order of the assets based on the time when they were ingested. Valid values:
        # 
        # *   desc: descending order.
        # *   asc: ascending order.
        self.sort_by = sort_by
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.assets:
            for v1 in self.assets:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Assets'] = []
        if self.assets is not None:
            for k1 in self.assets:
                result['Assets'].append(k1.to_map() if k1 else None)

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.assets = []
        if m.get('Assets') is not None:
            for k1 in m.get('Assets'):
                temp_model = main_models.ListVodPackagingAssetsResponseBodyAssets()
                self.assets.append(temp_model.from_map(k1))

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListVodPackagingAssetsResponseBodyAssets(DaraModel):
    def __init__(
        self,
        asset_name: str = None,
        create_time: str = None,
        description: str = None,
        group_name: str = None,
        input: main_models.ListVodPackagingAssetsResponseBodyAssetsInput = None,
    ):
        # The name of the VOD packaging asset.
        self.asset_name = asset_name
        # The time when the asset was ingested. It follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.create_time = create_time
        # The asset description.
        self.description = description
        # The name of the packaging group.
        self.group_name = group_name
        # The asset input configurations.
        self.input = input

    def validate(self):
        if self.input:
            self.input.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.asset_name is not None:
            result['AssetName'] = self.asset_name

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.input is not None:
            result['Input'] = self.input.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssetName') is not None:
            self.asset_name = m.get('AssetName')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('Input') is not None:
            temp_model = main_models.ListVodPackagingAssetsResponseBodyAssetsInput()
            self.input = temp_model.from_map(m.get('Input'))

        return self

class ListVodPackagingAssetsResponseBodyAssetsInput(DaraModel):
    def __init__(
        self,
        media: str = None,
        type: str = None,
    ):
        # The URL of the media file. Only M3U8 files stored in OSS are supported.
        self.media = media
        # The input type. Only Object Storage Service (OSS) is supported.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.media is not None:
            result['Media'] = self.media

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Media') is not None:
            self.media = m.get('Media')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

