# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_aligeniessp_1_0 import models as main_models
from darabonba.model import DaraModel

class CreatePlayingListOAuth2Request(DaraModel):
    def __init__(
        self,
        device_info: main_models.CreatePlayingListOAuth2RequestDeviceInfo = None,
        open_create_playing_list_request: main_models.CreatePlayingListOAuth2RequestOpenCreatePlayingListRequest = None,
    ):
        # Device identification information
        # 
        # This parameter is required.
        self.device_info = device_info
        # Business parameters
        # 
        # This parameter is required.
        self.open_create_playing_list_request = open_create_playing_list_request

    def validate(self):
        if self.device_info:
            self.device_info.validate()
        if self.open_create_playing_list_request:
            self.open_create_playing_list_request.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()

        if self.open_create_playing_list_request is not None:
            result['OpenCreatePlayingListRequest'] = self.open_create_playing_list_request.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            temp_model = main_models.CreatePlayingListOAuth2RequestDeviceInfo()
            self.device_info = temp_model.from_map(m.get('DeviceInfo'))

        if m.get('OpenCreatePlayingListRequest') is not None:
            temp_model = main_models.CreatePlayingListOAuth2RequestOpenCreatePlayingListRequest()
            self.open_create_playing_list_request = temp_model.from_map(m.get('OpenCreatePlayingListRequest'))

        return self

class CreatePlayingListOAuth2RequestOpenCreatePlayingListRequest(DaraModel):
    def __init__(
        self,
        content_list: List[main_models.CreatePlayingListOAuth2RequestOpenCreatePlayingListRequestContentList] = None,
        content_type: str = None,
        extend_info: Dict[str, Any] = None,
        index: int = None,
        need_album_continued: bool = None,
        play_from: str = None,
        play_mode: str = None,
    ):
        # Playback objects
        # 
        # This parameter is required.
        self.content_list = content_list
        # Content type for playback
        # 
        # Content: content; Album: album; Playlist: collect
        # 
        # This parameter is required.
        self.content_type = content_type
        # Extension information
        self.extend_info = extend_info
        # Index of the item to play
        # 
        # Can be empty. Default is 0, which means playback starts from the beginning.
        self.index = index
        # Indicates whether album playback should continue from the last played episode. For example, if the last playback stopped at episode 5, whether to resume from episode 5. Default is true.
        self.need_album_continued = need_album_continued
        # Playback source, the unique identifier for configuring playback control capabilities.  
        # 
        # Optional. Default value is "default".
        self.play_from = play_from
        # Playback pattern
        # 
        # Repeat all: Repeat; Shuffle: Shuffle; Repeat one: RepeatOne; Play in order: Normal.
        self.play_mode = play_mode

    def validate(self):
        if self.content_list:
            for v1 in self.content_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ContentList'] = []
        if self.content_list is not None:
            for k1 in self.content_list:
                result['ContentList'].append(k1.to_map() if k1 else None)

        if self.content_type is not None:
            result['ContentType'] = self.content_type

        if self.extend_info is not None:
            result['ExtendInfo'] = self.extend_info

        if self.index is not None:
            result['Index'] = self.index

        if self.need_album_continued is not None:
            result['NeedAlbumContinued'] = self.need_album_continued

        if self.play_from is not None:
            result['PlayFrom'] = self.play_from

        if self.play_mode is not None:
            result['PlayMode'] = self.play_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.content_list = []
        if m.get('ContentList') is not None:
            for k1 in m.get('ContentList'):
                temp_model = main_models.CreatePlayingListOAuth2RequestOpenCreatePlayingListRequestContentList()
                self.content_list.append(temp_model.from_map(k1))

        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')

        if m.get('ExtendInfo') is not None:
            self.extend_info = m.get('ExtendInfo')

        if m.get('Index') is not None:
            self.index = m.get('Index')

        if m.get('NeedAlbumContinued') is not None:
            self.need_album_continued = m.get('NeedAlbumContinued')

        if m.get('PlayFrom') is not None:
            self.play_from = m.get('PlayFrom')

        if m.get('PlayMode') is not None:
            self.play_mode = m.get('PlayMode')

        return self

class CreatePlayingListOAuth2RequestOpenCreatePlayingListRequestContentList(DaraModel):
    def __init__(
        self,
        raw_id: str = None,
        source: str = None,
    ):
        # Third-party ID.  
        # 
        # If the item is content, this is the content ID; if it is an album, this is the album ID.
        # 
        # This parameter is required.
        self.raw_id = raw_id
        # Source
        # 
        # This parameter is required.
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.raw_id is not None:
            result['RawId'] = self.raw_id

        if self.source is not None:
            result['Source'] = self.source

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RawId') is not None:
            self.raw_id = m.get('RawId')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        return self

class CreatePlayingListOAuth2RequestDeviceInfo(DaraModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        id: str = None,
        id_type: str = None,
        organization_id: str = None,
    ):
        # The value corresponding to the encoding type. Enter the Project ID of the project to which the product belongs. You can view it in the Tmall Genie AI Platform console.
        # 
        # This parameter is required.
        self.encode_key = encode_key
        # Encoding type. Enter PROJECT_ID here.
        # 
        # This parameter is required.
        self.encode_type = encode_type
        # Device ID. Enter the value of deviceOpenId or deviceUnionId.
        # 
        # This parameter is required.
        self.id = id
        # The type of device ID:  
        # OPEN_ID: The default device ID.  
        # UNION_ID: The organization-level device ID. You must request an organization in advance on the Open Platform.
        # 
        # This parameter is required.
        self.id_type = id_type
        # Organization ID. Required when IdType is UNION_ID.
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

