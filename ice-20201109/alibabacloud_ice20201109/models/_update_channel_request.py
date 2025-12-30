# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateChannelRequest(DaraModel):
    def __init__(
        self,
        access_policy: bool = None,
        access_token: str = None,
        channel_name: str = None,
        filler_source_location_name: str = None,
        filler_source_name: str = None,
        out_put_config_list: str = None,
    ):
        # Specifies whether to enable access control.
        self.access_policy = access_policy
        # The token for accessing the channel.
        self.access_token = access_token
        # The name of the channel.
        # 
        # This parameter is required.
        self.channel_name = channel_name
        # The source location of the filler slate.
        self.filler_source_location_name = filler_source_location_name
        # The name of the filler slate.
        self.filler_source_name = filler_source_name
        # The channel output configurations.
        # 
        # This parameter is required.
        self.out_put_config_list = out_put_config_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_policy is not None:
            result['AccessPolicy'] = self.access_policy

        if self.access_token is not None:
            result['AccessToken'] = self.access_token

        if self.channel_name is not None:
            result['ChannelName'] = self.channel_name

        if self.filler_source_location_name is not None:
            result['FillerSourceLocationName'] = self.filler_source_location_name

        if self.filler_source_name is not None:
            result['FillerSourceName'] = self.filler_source_name

        if self.out_put_config_list is not None:
            result['OutPutConfigList'] = self.out_put_config_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessPolicy') is not None:
            self.access_policy = m.get('AccessPolicy')

        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')

        if m.get('ChannelName') is not None:
            self.channel_name = m.get('ChannelName')

        if m.get('FillerSourceLocationName') is not None:
            self.filler_source_location_name = m.get('FillerSourceLocationName')

        if m.get('FillerSourceName') is not None:
            self.filler_source_name = m.get('FillerSourceName')

        if m.get('OutPutConfigList') is not None:
            self.out_put_config_list = m.get('OutPutConfigList')

        return self

