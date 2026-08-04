# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aligeniessp_1_0 import models as main_models
from darabonba.model import DaraModel

class CloudPlayerRequest(DaraModel):
    def __init__(
        self,
        cur_play_index: int = None,
        device_info: main_models.CloudPlayerRequestDeviceInfo = None,
        play_mode: str = None,
        song_id: str = None,
        song_id_list: List[str] = None,
        source: str = None,
        user_info: main_models.CloudPlayerRequestUserInfo = None,
    ):
        # Index of the currently playing song. Starts from 1.
        # 
        # This parameter is required.
        self.cur_play_index = cur_play_index
        # Device identity information
        # 
        # This parameter is required.
        self.device_info = device_info
        # Playback pattern
        # 
        # This parameter is required.
        self.play_mode = play_mode
        # Song ID (used to recompute the index when the index is invalid)
        self.song_id = song_id
        # List of song IDs (1–200 songs)
        # 
        # This parameter is required.
        self.song_id_list = song_id_list
        # Source of cloud-recommended songs
        # 
        # This parameter is required.
        self.source = source
        # Open user information
        # 
        # This parameter is required.
        self.user_info = user_info

    def validate(self):
        if self.device_info:
            self.device_info.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cur_play_index is not None:
            result['CurPlayIndex'] = self.cur_play_index

        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()

        if self.play_mode is not None:
            result['PlayMode'] = self.play_mode

        if self.song_id is not None:
            result['SongId'] = self.song_id

        if self.song_id_list is not None:
            result['SongIdList'] = self.song_id_list

        if self.source is not None:
            result['Source'] = self.source

        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurPlayIndex') is not None:
            self.cur_play_index = m.get('CurPlayIndex')

        if m.get('DeviceInfo') is not None:
            temp_model = main_models.CloudPlayerRequestDeviceInfo()
            self.device_info = temp_model.from_map(m.get('DeviceInfo'))

        if m.get('PlayMode') is not None:
            self.play_mode = m.get('PlayMode')

        if m.get('SongId') is not None:
            self.song_id = m.get('SongId')

        if m.get('SongIdList') is not None:
            self.song_id_list = m.get('SongIdList')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('UserInfo') is not None:
            temp_model = main_models.CloudPlayerRequestUserInfo()
            self.user_info = temp_model.from_map(m.get('UserInfo'))

        return self

class CloudPlayerRequestUserInfo(DaraModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        id: str = None,
        id_type: str = None,
        organization_id: str = None,
    ):
        # Encoding key
        # 
        # This parameter is required.
        self.encode_key = encode_key
        # Encoding type
        # 
        # This parameter is required.
        self.encode_type = encode_type
        # Open ID
        # 
        # This parameter is required.
        self.id = id
        # ID Type
        # 
        # This parameter is required.
        self.id_type = id_type
        # Organization ID (can be empty)
        self.organization_id = organization_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key

        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type

        if self.id is not None:
            result['Id'] = self.id

        if self.id_type is not None:
            result['IdType'] = self.id_type

        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')

        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')

        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')

        return self

class CloudPlayerRequestDeviceInfo(DaraModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        id: str = None,
        id_type: str = None,
        organization_id: str = None,
    ):
        # Encoding key
        # 
        # This parameter is required.
        self.encode_key = encode_key
        # Encoding type
        # 
        # This parameter is required.
        self.encode_type = encode_type
        # Open ID
        # 
        # This parameter is required.
        self.id = id
        # ID Type
        # 
        # This parameter is required.
        self.id_type = id_type
        # Organization ID (can be empty)
        self.organization_id = organization_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key

        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type

        if self.id is not None:
            result['Id'] = self.id

        if self.id_type is not None:
            result['IdType'] = self.id_type

        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')

        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')

        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')

        return self

