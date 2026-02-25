# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddTemplateRequest(DaraModel):
    def __init__(
        self,
        audio: str = None,
        container: str = None,
        mux_config: str = None,
        name: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        trans_config: str = None,
        video: str = None,
    ):
        # The audio stream settings. The value must be a JSON object. For more information, see [Audio](https://help.aliyun.com/document_detail/29253.html).
        # 
        # > If you do not specify this parameter, output files do not contain audio streams. This parameter is required if you want to retain the audio streams.
        self.audio = audio
        # The container format. The value must be a JSON object that contains the Format parameter. If you do not specify this parameter, the transcoded media file is in MP4 format by default. This parameter is required if you want to use the transcoding template to generate media files in other formats. For more information, see [Container](https://help.aliyun.com/document_detail/29253.html).
        # 
        # *   Default value: MP4.
        # *   Video transcoding supports the following formats: FLV, MP4, HLS (M3U8 + TS), and MPEG-DASH (MPD + fMP4).
        # 
        # > If the container format is FLV, the video codec cannot be set to H.265.
        # 
        # *   Audio transcoding supports the following formats: MP3, MP4, OGG, FLAC, and M4A.
        # *   Image transcoding supports the GIF and WebP formats.
        # 
        # > 
        # 
        # *   If the container format is GIF, the video codec must be set to GIF.
        # 
        # *   If the container format is WebP, the video codec must be set to WebP.
        self.container = container
        # The segment settings. The value must be a JSON object. For more information, see [MuxConfig](https://help.aliyun.com/document_detail/29253.html). If you do not specify this parameter, media segment files are not generated. This parameter is required if you want to generate media segment files.
        self.mux_config = mux_config
        # The name of the transcoding template. The name can be up to 128 bytes in length.
        # 
        # This parameter is required.
        self.name = name
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The general transcoding settings. The value must be a JSON object. For more information, see [TransConfig](https://help.aliyun.com/document_detail/29253.html). If you do not specify this parameter, the default settings are used. This parameter is required if the default settings cannot meet your business requirements.
        self.trans_config = trans_config
        # The video stream settings. The value must be a JSON object. For more information, see [Video](https://help.aliyun.com/document_detail/29253.html).
        # 
        # > If you do not specify this parameter, output files do not contain video streams. This parameter is required if you want to retain the video streams.
        self.video = video

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audio is not None:
            result['Audio'] = self.audio

        if self.container is not None:
            result['Container'] = self.container

        if self.mux_config is not None:
            result['MuxConfig'] = self.mux_config

        if self.name is not None:
            result['Name'] = self.name

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.trans_config is not None:
            result['TransConfig'] = self.trans_config

        if self.video is not None:
            result['Video'] = self.video

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Audio') is not None:
            self.audio = m.get('Audio')

        if m.get('Container') is not None:
            self.container = m.get('Container')

        if m.get('MuxConfig') is not None:
            self.mux_config = m.get('MuxConfig')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('TransConfig') is not None:
            self.trans_config = m.get('TransConfig')

        if m.get('Video') is not None:
            self.video = m.get('Video')

        return self

