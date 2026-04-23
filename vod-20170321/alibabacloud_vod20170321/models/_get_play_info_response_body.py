# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vod20170321 import models as main_models
from darabonba.model import DaraModel

class GetPlayInfoResponseBody(DaraModel):
    def __init__(
        self,
        play_info_list: main_models.GetPlayInfoResponseBodyPlayInfoList = None,
        request_id: str = None,
        video_base: main_models.GetPlayInfoResponseBodyVideoBase = None,
    ):
        self.play_info_list = play_info_list
        # The ID of the request.
        self.request_id = request_id
        # The basic information about the audio or video file.
        self.video_base = video_base

    def validate(self):
        if self.play_info_list:
            self.play_info_list.validate()
        if self.video_base:
            self.video_base.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.play_info_list is not None:
            result['PlayInfoList'] = self.play_info_list.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.video_base is not None:
            result['VideoBase'] = self.video_base.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PlayInfoList') is not None:
            temp_model = main_models.GetPlayInfoResponseBodyPlayInfoList()
            self.play_info_list = temp_model.from_map(m.get('PlayInfoList'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('VideoBase') is not None:
            temp_model = main_models.GetPlayInfoResponseBodyVideoBase()
            self.video_base = temp_model.from_map(m.get('VideoBase'))

        return self

class GetPlayInfoResponseBodyVideoBase(DaraModel):
    def __init__(
        self,
        cover_url: str = None,
        creation_time: str = None,
        dan_mu_url: str = None,
        duration: str = None,
        media_type: str = None,
        status: str = None,
        storage_class: str = None,
        title: str = None,
        video_id: str = None,
    ):
        # The thumbnail URL of the audio or video file.
        self.cover_url = cover_url
        # The time when the audio or video file was created. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.creation_time = creation_time
        # The URL of the masked live comment data.
        self.dan_mu_url = dan_mu_url
        # The duration of the audio or video file. Unit: seconds.
        self.duration = duration
        # The type of the media file. Valid values:
        # 
        # *   **video**
        # *   **audio**
        self.media_type = media_type
        # The status of the media file. For more information about the value range and description, see the [Status](~~52839#title-vqg-8cz-7p8~~) table.
        self.status = status
        # The storage class of the audio file. Valid values:
        # 
        # *   **Standard**: All media resources are stored as Standard objects.
        # *   **IA**: All media resources are stored as IA objects.
        # *   **Archive**: All media resources are stored as Archive objects.
        # *   **ColdArchive**: All media resources are stored as Cold Archive objects.
        # *   **SourceIA**: Only the source files are IA objects.
        # *   **SourceArchive**: Only the source files are Archive objects.
        # *   **SourceColdArchive**: Only the source file is stored as a Cold Archive object.
        # *   **Changing**: The storage class of the video file is being changed.
        # *   **SourceChanging**: The storage class of the source file is being changed.
        self.storage_class = storage_class
        # The title of the audio or video file.
        self.title = title
        # The ID of the media file.
        self.video_id = video_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cover_url is not None:
            result['CoverURL'] = self.cover_url

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.dan_mu_url is not None:
            result['DanMuURL'] = self.dan_mu_url

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.media_type is not None:
            result['MediaType'] = self.media_type

        if self.status is not None:
            result['Status'] = self.status

        if self.storage_class is not None:
            result['StorageClass'] = self.storage_class

        if self.title is not None:
            result['Title'] = self.title

        if self.video_id is not None:
            result['VideoId'] = self.video_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CoverURL') is not None:
            self.cover_url = m.get('CoverURL')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('DanMuURL') is not None:
            self.dan_mu_url = m.get('DanMuURL')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('MediaType') is not None:
            self.media_type = m.get('MediaType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StorageClass') is not None:
            self.storage_class = m.get('StorageClass')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')

        return self

class GetPlayInfoResponseBodyPlayInfoList(DaraModel):
    def __init__(
        self,
        play_info: List[main_models.GetPlayInfoResponseBodyPlayInfoListPlayInfo] = None,
    ):
        self.play_info = play_info

    def validate(self):
        if self.play_info:
            for v1 in self.play_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['PlayInfo'] = []
        if self.play_info is not None:
            for k1 in self.play_info:
                result['PlayInfo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.play_info = []
        if m.get('PlayInfo') is not None:
            for k1 in m.get('PlayInfo'):
                temp_model = main_models.GetPlayInfoResponseBodyPlayInfoListPlayInfo()
                self.play_info.append(temp_model.from_map(k1))

        return self

class GetPlayInfoResponseBodyPlayInfoListPlayInfo(DaraModel):
    def __init__(
        self,
        bit_depth: int = None,
        bitrate: str = None,
        codec_name: str = None,
        creation_time: str = None,
        definition: str = None,
        duration: str = None,
        encrypt: int = None,
        encrypt_mode: str = None,
        encrypt_type: str = None,
        format: str = None,
        fps: str = None,
        hdrtype: str = None,
        height: int = None,
        job_ext: str = None,
        job_id: str = None,
        job_type: int = None,
        modification_time: str = None,
        narrow_band_type: str = None,
        play_url: str = None,
        size: int = None,
        specification: str = None,
        status: str = None,
        stream_type: str = None,
        watermark_id: str = None,
        width: int = None,
    ):
        self.bit_depth = bit_depth
        self.bitrate = bitrate
        self.codec_name = codec_name
        self.creation_time = creation_time
        self.definition = definition
        self.duration = duration
        self.encrypt = encrypt
        self.encrypt_mode = encrypt_mode
        self.encrypt_type = encrypt_type
        self.format = format
        self.fps = fps
        self.hdrtype = hdrtype
        self.height = height
        self.job_ext = job_ext
        self.job_id = job_id
        self.job_type = job_type
        self.modification_time = modification_time
        self.narrow_band_type = narrow_band_type
        self.play_url = play_url
        self.size = size
        self.specification = specification
        self.status = status
        self.stream_type = stream_type
        self.watermark_id = watermark_id
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bit_depth is not None:
            result['BitDepth'] = self.bit_depth

        if self.bitrate is not None:
            result['Bitrate'] = self.bitrate

        if self.codec_name is not None:
            result['CodecName'] = self.codec_name

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.definition is not None:
            result['Definition'] = self.definition

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.encrypt is not None:
            result['Encrypt'] = self.encrypt

        if self.encrypt_mode is not None:
            result['EncryptMode'] = self.encrypt_mode

        if self.encrypt_type is not None:
            result['EncryptType'] = self.encrypt_type

        if self.format is not None:
            result['Format'] = self.format

        if self.fps is not None:
            result['Fps'] = self.fps

        if self.hdrtype is not None:
            result['HDRType'] = self.hdrtype

        if self.height is not None:
            result['Height'] = self.height

        if self.job_ext is not None:
            result['JobExt'] = self.job_ext

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.job_type is not None:
            result['JobType'] = self.job_type

        if self.modification_time is not None:
            result['ModificationTime'] = self.modification_time

        if self.narrow_band_type is not None:
            result['NarrowBandType'] = self.narrow_band_type

        if self.play_url is not None:
            result['PlayURL'] = self.play_url

        if self.size is not None:
            result['Size'] = self.size

        if self.specification is not None:
            result['Specification'] = self.specification

        if self.status is not None:
            result['Status'] = self.status

        if self.stream_type is not None:
            result['StreamType'] = self.stream_type

        if self.watermark_id is not None:
            result['WatermarkId'] = self.watermark_id

        if self.width is not None:
            result['Width'] = self.width

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BitDepth') is not None:
            self.bit_depth = m.get('BitDepth')

        if m.get('Bitrate') is not None:
            self.bitrate = m.get('Bitrate')

        if m.get('CodecName') is not None:
            self.codec_name = m.get('CodecName')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('Definition') is not None:
            self.definition = m.get('Definition')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('Encrypt') is not None:
            self.encrypt = m.get('Encrypt')

        if m.get('EncryptMode') is not None:
            self.encrypt_mode = m.get('EncryptMode')

        if m.get('EncryptType') is not None:
            self.encrypt_type = m.get('EncryptType')

        if m.get('Format') is not None:
            self.format = m.get('Format')

        if m.get('Fps') is not None:
            self.fps = m.get('Fps')

        if m.get('HDRType') is not None:
            self.hdrtype = m.get('HDRType')

        if m.get('Height') is not None:
            self.height = m.get('Height')

        if m.get('JobExt') is not None:
            self.job_ext = m.get('JobExt')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')

        if m.get('ModificationTime') is not None:
            self.modification_time = m.get('ModificationTime')

        if m.get('NarrowBandType') is not None:
            self.narrow_band_type = m.get('NarrowBandType')

        if m.get('PlayURL') is not None:
            self.play_url = m.get('PlayURL')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('Specification') is not None:
            self.specification = m.get('Specification')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StreamType') is not None:
            self.stream_type = m.get('StreamType')

        if m.get('WatermarkId') is not None:
            self.watermark_id = m.get('WatermarkId')

        if m.get('Width') is not None:
            self.width = m.get('Width')

        return self

