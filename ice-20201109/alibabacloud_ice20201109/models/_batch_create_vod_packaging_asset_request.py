# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class BatchCreateVodPackagingAssetRequest(DaraModel):
    def __init__(
        self,
        assets: List[main_models.BatchCreateVodPackagingAssetRequestAssets] = None,
        group_name: str = None,
    ):
        # The assets that you want to ingest.
        self.assets = assets
        # The name of the packaging group.
        self.group_name = group_name

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

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.assets = []
        if m.get('Assets') is not None:
            for k1 in m.get('Assets'):
                temp_model = main_models.BatchCreateVodPackagingAssetRequestAssets()
                self.assets.append(temp_model.from_map(k1))

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        return self

class BatchCreateVodPackagingAssetRequestAssets(DaraModel):
    def __init__(
        self,
        asset_name: str = None,
        content_id: str = None,
        input: main_models.BatchCreateVodPackagingAssetRequestAssetsInput = None,
    ):
        # The name of the asset. The name must be unique and can be up to 128 characters in length. Letters, digits, underscores (_), and hyphens (-) are supported.
        self.asset_name = asset_name
        # The content ID in the digital rights management (DRM) system. The maximum length is 256 characters. Letters, digits, underscores (_), and hyphens (-) are supported.
        self.content_id = content_id
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

        if self.content_id is not None:
            result['ContentId'] = self.content_id

        if self.input is not None:
            result['Input'] = self.input.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssetName') is not None:
            self.asset_name = m.get('AssetName')

        if m.get('ContentId') is not None:
            self.content_id = m.get('ContentId')

        if m.get('Input') is not None:
            temp_model = main_models.BatchCreateVodPackagingAssetRequestAssetsInput()
            self.input = temp_model.from_map(m.get('Input'))

        return self

class BatchCreateVodPackagingAssetRequestAssetsInput(DaraModel):
    def __init__(
        self,
        media: str = None,
        type: str = None,
    ):
        # The URL of the media file. You can only specify a M3U8 file stored in Object Storage Service (OSS).
        self.media = media
        # The input type. Only OSS is supported.
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

