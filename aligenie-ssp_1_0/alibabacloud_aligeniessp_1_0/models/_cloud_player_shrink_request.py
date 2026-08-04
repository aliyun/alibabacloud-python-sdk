# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CloudPlayerShrinkRequest(DaraModel):
    def __init__(
        self,
        cur_play_index: int = None,
        device_info_shrink: str = None,
        play_mode: str = None,
        song_id: str = None,
        song_id_list_shrink: str = None,
        source: str = None,
        user_info_shrink: str = None,
    ):
        # Index of the currently playing song. Starts from 1.
        # 
        # This parameter is required.
        self.cur_play_index = cur_play_index
        # Device identity information
        # 
        # This parameter is required.
        self.device_info_shrink = device_info_shrink
        # Playback pattern
        # 
        # This parameter is required.
        self.play_mode = play_mode
        # Song ID (used to recompute the index when the index is invalid)
        self.song_id = song_id
        # List of song IDs (1–200 songs)
        # 
        # This parameter is required.
        self.song_id_list_shrink = song_id_list_shrink
        # Source of cloud-recommended songs
        # 
        # This parameter is required.
        self.source = source
        # Open user information
        # 
        # This parameter is required.
        self.user_info_shrink = user_info_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cur_play_index is not None:
            result['CurPlayIndex'] = self.cur_play_index

        if self.device_info_shrink is not None:
            result['DeviceInfo'] = self.device_info_shrink

        if self.play_mode is not None:
            result['PlayMode'] = self.play_mode

        if self.song_id is not None:
            result['SongId'] = self.song_id

        if self.song_id_list_shrink is not None:
            result['SongIdList'] = self.song_id_list_shrink

        if self.source is not None:
            result['Source'] = self.source

        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurPlayIndex') is not None:
            self.cur_play_index = m.get('CurPlayIndex')

        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')

        if m.get('PlayMode') is not None:
            self.play_mode = m.get('PlayMode')

        if m.get('SongId') is not None:
            self.song_id = m.get('SongId')

        if m.get('SongIdList') is not None:
            self.song_id_list_shrink = m.get('SongIdList')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')

        return self

