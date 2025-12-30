# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class Channel(DaraModel):
    def __init__(
        self,
        access_policy: bool = None,
        access_token: str = None,
        arn: str = None,
        channel_name: str = None,
        channel_tier: str = None,
        filler_source_location_name: str = None,
        filler_source_name: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        out_put_config_list: List[main_models.ChannelOutPutConfigList] = None,
        playback_mode: str = None,
        state: int = None,
    ):
        self.access_policy = access_policy
        self.access_token = access_token
        self.arn = arn
        self.channel_name = channel_name
        self.channel_tier = channel_tier
        self.filler_source_location_name = filler_source_location_name
        self.filler_source_name = filler_source_name
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.out_put_config_list = out_put_config_list
        self.playback_mode = playback_mode
        self.state = state

    def validate(self):
        if self.out_put_config_list:
            for v1 in self.out_put_config_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_policy is not None:
            result['AccessPolicy'] = self.access_policy

        if self.access_token is not None:
            result['AccessToken'] = self.access_token

        if self.arn is not None:
            result['Arn'] = self.arn

        if self.channel_name is not None:
            result['ChannelName'] = self.channel_name

        if self.channel_tier is not None:
            result['ChannelTier'] = self.channel_tier

        if self.filler_source_location_name is not None:
            result['FillerSourceLocationName'] = self.filler_source_location_name

        if self.filler_source_name is not None:
            result['FillerSourceName'] = self.filler_source_name

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        result['OutPutConfigList'] = []
        if self.out_put_config_list is not None:
            for k1 in self.out_put_config_list:
                result['OutPutConfigList'].append(k1.to_map() if k1 else None)

        if self.playback_mode is not None:
            result['PlaybackMode'] = self.playback_mode

        if self.state is not None:
            result['State'] = self.state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessPolicy') is not None:
            self.access_policy = m.get('AccessPolicy')

        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')

        if m.get('Arn') is not None:
            self.arn = m.get('Arn')

        if m.get('ChannelName') is not None:
            self.channel_name = m.get('ChannelName')

        if m.get('ChannelTier') is not None:
            self.channel_tier = m.get('ChannelTier')

        if m.get('FillerSourceLocationName') is not None:
            self.filler_source_location_name = m.get('FillerSourceLocationName')

        if m.get('FillerSourceName') is not None:
            self.filler_source_name = m.get('FillerSourceName')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        self.out_put_config_list = []
        if m.get('OutPutConfigList') is not None:
            for k1 in m.get('OutPutConfigList'):
                temp_model = main_models.ChannelOutPutConfigList()
                self.out_put_config_list.append(temp_model.from_map(k1))

        if m.get('PlaybackMode') is not None:
            self.playback_mode = m.get('PlaybackMode')

        if m.get('State') is not None:
            self.state = m.get('State')

        return self

class ChannelOutPutConfigList(DaraModel):
    def __init__(
        self,
        channel_name: str = None,
        format: str = None,
        manifest_name: str = None,
        manifest_settings: str = None,
        playback_url: str = None,
        source_group_name: str = None,
    ):
        self.channel_name = channel_name
        self.format = format
        self.manifest_name = manifest_name
        self.manifest_settings = manifest_settings
        self.playback_url = playback_url
        self.source_group_name = source_group_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channel_name is not None:
            result['ChannelName'] = self.channel_name

        if self.format is not None:
            result['Format'] = self.format

        if self.manifest_name is not None:
            result['ManifestName'] = self.manifest_name

        if self.manifest_settings is not None:
            result['ManifestSettings'] = self.manifest_settings

        if self.playback_url is not None:
            result['PlaybackUrl'] = self.playback_url

        if self.source_group_name is not None:
            result['SourceGroupName'] = self.source_group_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelName') is not None:
            self.channel_name = m.get('ChannelName')

        if m.get('Format') is not None:
            self.format = m.get('Format')

        if m.get('ManifestName') is not None:
            self.manifest_name = m.get('ManifestName')

        if m.get('ManifestSettings') is not None:
            self.manifest_settings = m.get('ManifestSettings')

        if m.get('PlaybackUrl') is not None:
            self.playback_url = m.get('PlaybackUrl')

        if m.get('SourceGroupName') is not None:
            self.source_group_name = m.get('SourceGroupName')

        return self

