# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class VodPackagingAsset(DaraModel):
    def __init__(
        self,
        asset_name: str = None,
        content_id: str = None,
        create_time: str = None,
        group_name: str = None,
        input: main_models.VodPackagingAssetInput = None,
    ):
        self.asset_name = asset_name
        self.content_id = content_id
        self.create_time = create_time
        self.group_name = group_name
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

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

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

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('Input') is not None:
            temp_model = main_models.VodPackagingAssetInput()
            self.input = temp_model.from_map(m.get('Input'))

        return self

class VodPackagingAssetInput(DaraModel):
    def __init__(
        self,
        media: str = None,
        type: str = None,
    ):
        self.media = media
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

