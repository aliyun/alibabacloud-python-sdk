# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreatePlayingListOAuth2ShrinkRequest(DaraModel):
    def __init__(
        self,
        device_info_shrink: str = None,
        open_create_playing_list_request_shrink: str = None,
    ):
        # Device identification information
        # 
        # This parameter is required.
        self.device_info_shrink = device_info_shrink
        # Business parameters
        # 
        # This parameter is required.
        self.open_create_playing_list_request_shrink = open_create_playing_list_request_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.device_info_shrink is not None:
            result['DeviceInfo'] = self.device_info_shrink

        if self.open_create_playing_list_request_shrink is not None:
            result['OpenCreatePlayingListRequest'] = self.open_create_playing_list_request_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')

        if m.get('OpenCreatePlayingListRequest') is not None:
            self.open_create_playing_list_request_shrink = m.get('OpenCreatePlayingListRequest')

        return self

