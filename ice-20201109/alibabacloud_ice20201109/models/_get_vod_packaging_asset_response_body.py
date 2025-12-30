# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class GetVodPackagingAssetResponseBody(DaraModel):
    def __init__(
        self,
        asset: main_models.GetVodPackagingAssetResponseBodyAsset = None,
        request_id: str = None,
    ):
        # The information about the asset.
        self.asset = asset
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.asset:
            self.asset.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.asset is not None:
            result['Asset'] = self.asset.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Asset') is not None:
            temp_model = main_models.GetVodPackagingAssetResponseBodyAsset()
            self.asset = temp_model.from_map(m.get('Asset'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetVodPackagingAssetResponseBodyAsset(DaraModel):
    def __init__(
        self,
        asset_name: str = None,
        content_id: str = None,
        create_time: str = None,
        egress_endpoints: List[main_models.GetVodPackagingAssetResponseBodyAssetEgressEndpoints] = None,
        group_name: str = None,
        input: main_models.GetVodPackagingAssetResponseBodyAssetInput = None,
    ):
        # The name of the asset.
        self.asset_name = asset_name
        # The content ID in the DRM system. The maximum length is 256 characters. Letters, digits, underscores (_), and hyphens (-) are supported.
        self.content_id = content_id
        # The time when the asset was created. It follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.create_time = create_time
        # The egress endpoints, each corresponding to a packaging configuration.
        self.egress_endpoints = egress_endpoints
        # The name of the packaging group.
        self.group_name = group_name
        # The asset input configurations.
        self.input = input

    def validate(self):
        if self.egress_endpoints:
            for v1 in self.egress_endpoints:
                 if v1:
                    v1.validate()
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

        result['EgressEndpoints'] = []
        if self.egress_endpoints is not None:
            for k1 in self.egress_endpoints:
                result['EgressEndpoints'].append(k1.to_map() if k1 else None)

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

        self.egress_endpoints = []
        if m.get('EgressEndpoints') is not None:
            for k1 in m.get('EgressEndpoints'):
                temp_model = main_models.GetVodPackagingAssetResponseBodyAssetEgressEndpoints()
                self.egress_endpoints.append(temp_model.from_map(k1))

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('Input') is not None:
            temp_model = main_models.GetVodPackagingAssetResponseBodyAssetInput()
            self.input = temp_model.from_map(m.get('Input'))

        return self

class GetVodPackagingAssetResponseBodyAssetInput(DaraModel):
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

class GetVodPackagingAssetResponseBodyAssetEgressEndpoints(DaraModel):
    def __init__(
        self,
        configuration_name: str = None,
        status: str = None,
        url: str = None,
    ):
        # The name of the packaging configuration.
        self.configuration_name = configuration_name
        # The asset status. Valid values:
        # 
        # *   Queuing: The asset is waiting for packaging.
        # *   Playable: The asset is packaged and playable.
        # *   Failed: The asset fails to be packaged.
        self.status = status
        # The playback URL. If the asset fails to be packaged, no playback URL is returned.
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.configuration_name is not None:
            result['ConfigurationName'] = self.configuration_name

        if self.status is not None:
            result['Status'] = self.status

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigurationName') is not None:
            self.configuration_name = m.get('ConfigurationName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

