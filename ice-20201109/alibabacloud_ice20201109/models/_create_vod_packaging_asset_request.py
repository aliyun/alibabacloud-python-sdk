# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class CreateVodPackagingAssetRequest(DaraModel):
    def __init__(
        self,
        asset_name: str = None,
        content_id: str = None,
        description: str = None,
        group_name: str = None,
        input: main_models.CreateVodPackagingAssetRequestInput = None,
    ):
        # The name of the asset. The name must be unique and can be up to 128 characters in length. Letters, digits, underscores (_), and hyphens (-) are supported.
        self.asset_name = asset_name
        # The content ID in the digital rights management (DRM) system. The maximum length is 256 characters. Letters, digits, underscores (_), and hyphens (-) are supported.
        self.content_id = content_id
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

        if self.content_id is not None:
            result['ContentId'] = self.content_id

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

        if m.get('ContentId') is not None:
            self.content_id = m.get('ContentId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('Input') is not None:
            temp_model = main_models.CreateVodPackagingAssetRequestInput()
            self.input = temp_model.from_map(m.get('Input'))

        return self

class CreateVodPackagingAssetRequestInput(DaraModel):
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

