# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vod20170321 import models as main_models
from darabonba.model import DaraModel

class BatchGetMediaInfosResponseBody(DaraModel):
    def __init__(
        self,
        forbidden_media_ids: List[str] = None,
        media_infos: List[main_models.BatchGetMediaInfosResponseBodyMediaInfos] = None,
        non_exist_media_ids: List[str] = None,
        non_exist_reference_ids: List[str] = None,
        request_id: str = None,
    ):
        # The IDs of the media assets that do not support the operation typically because you are not authorized to perform the operation. For more information, see [Overview](https://help.aliyun.com/document_detail/113600.html).
        self.forbidden_media_ids = forbidden_media_ids
        # Details about media assets.
        self.media_infos = media_infos
        # The IDs of the media assets that do not exist.
        self.non_exist_media_ids = non_exist_media_ids
        self.non_exist_reference_ids = non_exist_reference_ids
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.media_infos:
            for v1 in self.media_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.forbidden_media_ids is not None:
            result['ForbiddenMediaIds'] = self.forbidden_media_ids

        result['MediaInfos'] = []
        if self.media_infos is not None:
            for k1 in self.media_infos:
                result['MediaInfos'].append(k1.to_map() if k1 else None)

        if self.non_exist_media_ids is not None:
            result['NonExistMediaIds'] = self.non_exist_media_ids

        if self.non_exist_reference_ids is not None:
            result['NonExistReferenceIds'] = self.non_exist_reference_ids

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ForbiddenMediaIds') is not None:
            self.forbidden_media_ids = m.get('ForbiddenMediaIds')

        self.media_infos = []
        if m.get('MediaInfos') is not None:
            for k1 in m.get('MediaInfos'):
                temp_model = main_models.BatchGetMediaInfosResponseBodyMediaInfos()
                self.media_infos.append(temp_model.from_map(k1))

        if m.get('NonExistMediaIds') is not None:
            self.non_exist_media_ids = m.get('NonExistMediaIds')

        if m.get('NonExistReferenceIds') is not None:
            self.non_exist_reference_ids = m.get('NonExistReferenceIds')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class BatchGetMediaInfosResponseBodyMediaInfos(DaraModel):
    def __init__(
        self,
        media_id: str = None,
        media_info: main_models.BatchGetMediaInfosResponseBodyMediaInfosMediaInfo = None,
        mezzanine_info: main_models.BatchGetMediaInfosResponseBodyMediaInfosMezzanineInfo = None,
        play_info_list: List[main_models.BatchGetMediaInfosResponseBodyMediaInfosPlayInfoList] = None,
    ):
        # The ID of the media asset.
        self.media_id = media_id
        # The basic information of the media asset.
        self.media_info = media_info
        # The source file information.
        self.mezzanine_info = mezzanine_info
        # The information about the audio or video stream.
        self.play_info_list = play_info_list

    def validate(self):
        if self.media_info:
            self.media_info.validate()
        if self.mezzanine_info:
            self.mezzanine_info.validate()
        if self.play_info_list:
            for v1 in self.play_info_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.media_id is not None:
            result['MediaId'] = self.media_id

        if self.media_info is not None:
            result['MediaInfo'] = self.media_info.to_map()

        if self.mezzanine_info is not None:
            result['MezzanineInfo'] = self.mezzanine_info.to_map()

        result['PlayInfoList'] = []
        if self.play_info_list is not None:
            for k1 in self.play_info_list:
                result['PlayInfoList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')

        if m.get('MediaInfo') is not None:
            temp_model = main_models.BatchGetMediaInfosResponseBodyMediaInfosMediaInfo()
            self.media_info = temp_model.from_map(m.get('MediaInfo'))

        if m.get('MezzanineInfo') is not None:
            temp_model = main_models.BatchGetMediaInfosResponseBodyMediaInfosMezzanineInfo()
            self.mezzanine_info = temp_model.from_map(m.get('MezzanineInfo'))

        self.play_info_list = []
        if m.get('PlayInfoList') is not None:
            for k1 in m.get('PlayInfoList'):
                temp_model = main_models.BatchGetMediaInfosResponseBodyMediaInfosPlayInfoList()
                self.play_info_list.append(temp_model.from_map(k1))

        return self

class BatchGetMediaInfosResponseBodyMediaInfosPlayInfoList(DaraModel):
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
        template_group_id: str = None,
        template_id: str = None,
        watermark_id: str = None,
        width: int = None,
    ):
        # The color depth. This value is an integer.
        self.bit_depth = bit_depth
        # The bitrate of the media stream. Unit: Kbit/s.
        self.bitrate = bitrate
        # The short name of the codec.
        self.codec_name = codec_name
        # The creation time. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.creation_time = creation_time
        # The quality of the video stream. Valid values:
        # 
        # *   **FD**: low definition
        # *   **LD**: standard definition
        # *   **SD**: high definition
        # *   **HD**: ultra-high definition
        # *   **OD**: original definition
        # *   **2K**
        # *   **4K**
        # *   **SQ**: standard sound quality
        # *   **HQ**: high sound quality
        # *   **AUTO**: adaptive bitrate
        self.definition = definition
        # The duration of the media stream. Unit: seconds.
        self.duration = duration
        # Indicates whether the media stream was encrypted. Valid values:
        # 
        # *   **0**: The media stream is not encrypted.
        # *   **1**: The media stream is encrypted.
        self.encrypt = encrypt
        # The encryption type of the media stream. Valid values:
        # 
        # *   **License**: decryption on local devices.
        # 
        # >  If the encryption type is **License**, only ApsaraVideo Player SDK can be used to play videos.
        self.encrypt_mode = encrypt_mode
        # The encryption type of the media stream. Valid values:
        # 
        # *   **AliyunVoDEncryption**: Alibaba Cloud proprietary cryptography
        # *   **HLSEncryption**: HTTP Live Streaming (HLS) encryption
        # 
        # >  If the encryption type is AliyunVoDEncryption, only ApsaraVideo Player SDK can be used to play videos.
        self.encrypt_type = encrypt_type
        # The format of the media stream.
        # 
        # *   If the media file is a video file, the valid values are **mp4** and **m3u8**.
        # *   If the media asset is an audio-only file, the value is **mp3**.
        self.format = format
        # The frame rate of the media stream. Unit: frames per second (FPS).
        self.fps = fps
        # The HDR type of the media stream. Valid values:
        # 
        # *   HDR
        # *   HDR10
        # *   HLG
        # *   DolbyVision
        # *   HDRVivid
        # *   SDR+
        self.hdrtype = hdrtype
        # The height of the media stream. Unit: pixels.
        self.height = height
        # The custom watermark information of the copyright watermark. This parameter is returned if you set `JobType` to `2`.
        self.job_ext = job_ext
        # The job ID for transcoding the media stream. This ID uniquely identifies a media stream.
        self.job_id = job_id
        # The type of the digital watermark. Valid values:
        # 
        # *   **1**: user-tracing watermark
        # *   **2**: copyright watermark
        self.job_type = job_type
        # The update time. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.modification_time = modification_time
        # The transcoding type. Valid values:
        # 
        # *   **0**: regular transcoding
        # *   **1.0**: Narrowband HD™ 1.0 transcoding
        # *   **2.0**: Narrowband HD™ 2.0 transcoding
        self.narrow_band_type = narrow_band_type
        # The playback URL of the video stream.
        self.play_url = play_url
        # The size of the media stream. Unit: bytes.
        self.size = size
        # The specifications of transcoded audio and video streams. For more information about the valid values, see [Output specifications](~~124671#section-6bv-l0g-opq~~).
        self.specification = specification
        # The status of the audio or video stream. Valid values:
        # 
        # *   **Normal**: The latest transcoded stream in each quality and format is in the Normal status.
        # *   **Invisible**: If multiple streams are transcoded in the same quality and format, the latest transcoded stream is in the Normal status and other streams are in the Invisible status.
        self.status = status
        # The type of the media stream. If the media stream is a video stream, the value is **video**. If the media stream is an audio-only stream, the value is **audio**.
        self.stream_type = stream_type
        # The ID of the transcoding template group.
        self.template_group_id = template_group_id
        # The ID of the transcoding template.
        self.template_id = template_id
        # The ID of the watermark that is associated with the media stream.
        self.watermark_id = watermark_id
        # The width of the media stream. Unit: pixels.
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

        if self.template_group_id is not None:
            result['TemplateGroupId'] = self.template_group_id

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

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

        if m.get('TemplateGroupId') is not None:
            self.template_group_id = m.get('TemplateGroupId')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('WatermarkId') is not None:
            self.watermark_id = m.get('WatermarkId')

        if m.get('Width') is not None:
            self.width = m.get('Width')

        return self

class BatchGetMediaInfosResponseBodyMediaInfosMezzanineInfo(DaraModel):
    def __init__(
        self,
        audio_stream_list: List[main_models.BatchGetMediaInfosResponseBodyMediaInfosMezzanineInfoAudioStreamList] = None,
        bitrate: str = None,
        creation_time: str = None,
        duration: str = None,
        file_md5: str = None,
        file_name: str = None,
        file_url: str = None,
        fps: str = None,
        height: int = None,
        media_id: str = None,
        size: int = None,
        status: str = None,
        video_stream_list: List[main_models.BatchGetMediaInfosResponseBodyMediaInfosMezzanineInfoVideoStreamList] = None,
        width: int = None,
    ):
        # The information about the audio stream.
        self.audio_stream_list = audio_stream_list
        # The bitrate of the file. Unit: Kbit/s.
        self.bitrate = bitrate
        # The time when the source file was created. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.creation_time = creation_time
        # The duration of the file. Unit: seconds.
        self.duration = duration
        self.file_md5 = file_md5
        # The name of the file.
        self.file_name = file_name
        # The OSS URL of the source file.
        self.file_url = file_url
        # The frame rate of the file.
        self.fps = fps
        # The height of the file. Unit: pixels.
        self.height = height
        # The ID of the media asset.
        self.media_id = media_id
        # The size of the file. Unit: bytes.
        self.size = size
        # The state of the file. Valid values:
        # 
        # *   **Uploading**: The file is being uploaded. This is the initial status.
        # *   **Normal**: The file is uploaded.
        # *   **UploadFail**: The file failed to be uploaded.
        # *   **Deleted**: The file is deleted.
        self.status = status
        # The information about the video streams.
        self.video_stream_list = video_stream_list
        # The width of the file. Unit: pixels.
        self.width = width

    def validate(self):
        if self.audio_stream_list:
            for v1 in self.audio_stream_list:
                 if v1:
                    v1.validate()
        if self.video_stream_list:
            for v1 in self.video_stream_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AudioStreamList'] = []
        if self.audio_stream_list is not None:
            for k1 in self.audio_stream_list:
                result['AudioStreamList'].append(k1.to_map() if k1 else None)

        if self.bitrate is not None:
            result['Bitrate'] = self.bitrate

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.file_md5 is not None:
            result['FileMD5'] = self.file_md5

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.file_url is not None:
            result['FileURL'] = self.file_url

        if self.fps is not None:
            result['Fps'] = self.fps

        if self.height is not None:
            result['Height'] = self.height

        if self.media_id is not None:
            result['MediaId'] = self.media_id

        if self.size is not None:
            result['Size'] = self.size

        if self.status is not None:
            result['Status'] = self.status

        result['VideoStreamList'] = []
        if self.video_stream_list is not None:
            for k1 in self.video_stream_list:
                result['VideoStreamList'].append(k1.to_map() if k1 else None)

        if self.width is not None:
            result['Width'] = self.width

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.audio_stream_list = []
        if m.get('AudioStreamList') is not None:
            for k1 in m.get('AudioStreamList'):
                temp_model = main_models.BatchGetMediaInfosResponseBodyMediaInfosMezzanineInfoAudioStreamList()
                self.audio_stream_list.append(temp_model.from_map(k1))

        if m.get('Bitrate') is not None:
            self.bitrate = m.get('Bitrate')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('FileMD5') is not None:
            self.file_md5 = m.get('FileMD5')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('FileURL') is not None:
            self.file_url = m.get('FileURL')

        if m.get('Fps') is not None:
            self.fps = m.get('Fps')

        if m.get('Height') is not None:
            self.height = m.get('Height')

        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.video_stream_list = []
        if m.get('VideoStreamList') is not None:
            for k1 in m.get('VideoStreamList'):
                temp_model = main_models.BatchGetMediaInfosResponseBodyMediaInfosMezzanineInfoVideoStreamList()
                self.video_stream_list.append(temp_model.from_map(k1))

        if m.get('Width') is not None:
            self.width = m.get('Width')

        return self

class BatchGetMediaInfosResponseBodyMediaInfosMezzanineInfoVideoStreamList(DaraModel):
    def __init__(
        self,
        avg_fps: str = None,
        bitrate: str = None,
        codec_long_name: str = None,
        codec_name: str = None,
        codec_tag: str = None,
        codec_tag_string: str = None,
        codec_time_base: str = None,
        dar: str = None,
        duration: str = None,
        fps: str = None,
        hdrtype: str = None,
        has_bframes: str = None,
        height: str = None,
        index: str = None,
        lang: str = None,
        level: str = None,
        num_frames: str = None,
        pix_fmt: str = None,
        profile: str = None,
        rotate: str = None,
        sar: str = None,
        start_time: str = None,
        timebase: str = None,
        width: str = None,
    ):
        # The average frame rate.
        self.avg_fps = avg_fps
        # The bitrate of the file. Unit: Kbit/s.
        self.bitrate = bitrate
        # The full name of the encoding format.
        self.codec_long_name = codec_long_name
        # The short name of the encoding format.
        self.codec_name = codec_name
        # The tag of the encoding format.
        self.codec_tag = codec_tag
        # The tag string of the encoding format.
        self.codec_tag_string = codec_tag_string
        # The time base of the encoder.
        self.codec_time_base = codec_time_base
        # The display aspect ratio (DAR).
        self.dar = dar
        # The duration.
        self.duration = duration
        # The frame rate of the output file.
        self.fps = fps
        # The HDR type of the video stream.
        self.hdrtype = hdrtype
        # Indicates whether the video stream contains bidirectional frames (B-frames).
        self.has_bframes = has_bframes
        # The height of the video stream.
        self.height = height
        # The sequence number of the video stream. The value identifies the position of the video stream in all video streams.
        self.index = index
        # The language.
        self.lang = lang
        # The codec level.
        self.level = level
        # The total number of frames.
        self.num_frames = num_frames
        # The pixel format of the video stream.
        self.pix_fmt = pix_fmt
        # The codec profile.
        self.profile = profile
        # The rotation angle of the video. Valid values: [0,360).
        self.rotate = rotate
        # The sample aspect ratio (SAR).
        self.sar = sar
        # The start time. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.start_time = start_time
        # The time base.
        self.timebase = timebase
        # The horizontal resolution of the video.
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.avg_fps is not None:
            result['AvgFPS'] = self.avg_fps

        if self.bitrate is not None:
            result['Bitrate'] = self.bitrate

        if self.codec_long_name is not None:
            result['CodecLongName'] = self.codec_long_name

        if self.codec_name is not None:
            result['CodecName'] = self.codec_name

        if self.codec_tag is not None:
            result['CodecTag'] = self.codec_tag

        if self.codec_tag_string is not None:
            result['CodecTagString'] = self.codec_tag_string

        if self.codec_time_base is not None:
            result['CodecTimeBase'] = self.codec_time_base

        if self.dar is not None:
            result['Dar'] = self.dar

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.fps is not None:
            result['Fps'] = self.fps

        if self.hdrtype is not None:
            result['HDRType'] = self.hdrtype

        if self.has_bframes is not None:
            result['HasBFrames'] = self.has_bframes

        if self.height is not None:
            result['Height'] = self.height

        if self.index is not None:
            result['Index'] = self.index

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.level is not None:
            result['Level'] = self.level

        if self.num_frames is not None:
            result['NumFrames'] = self.num_frames

        if self.pix_fmt is not None:
            result['PixFmt'] = self.pix_fmt

        if self.profile is not None:
            result['Profile'] = self.profile

        if self.rotate is not None:
            result['Rotate'] = self.rotate

        if self.sar is not None:
            result['Sar'] = self.sar

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.timebase is not None:
            result['Timebase'] = self.timebase

        if self.width is not None:
            result['Width'] = self.width

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvgFPS') is not None:
            self.avg_fps = m.get('AvgFPS')

        if m.get('Bitrate') is not None:
            self.bitrate = m.get('Bitrate')

        if m.get('CodecLongName') is not None:
            self.codec_long_name = m.get('CodecLongName')

        if m.get('CodecName') is not None:
            self.codec_name = m.get('CodecName')

        if m.get('CodecTag') is not None:
            self.codec_tag = m.get('CodecTag')

        if m.get('CodecTagString') is not None:
            self.codec_tag_string = m.get('CodecTagString')

        if m.get('CodecTimeBase') is not None:
            self.codec_time_base = m.get('CodecTimeBase')

        if m.get('Dar') is not None:
            self.dar = m.get('Dar')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('Fps') is not None:
            self.fps = m.get('Fps')

        if m.get('HDRType') is not None:
            self.hdrtype = m.get('HDRType')

        if m.get('HasBFrames') is not None:
            self.has_bframes = m.get('HasBFrames')

        if m.get('Height') is not None:
            self.height = m.get('Height')

        if m.get('Index') is not None:
            self.index = m.get('Index')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('NumFrames') is not None:
            self.num_frames = m.get('NumFrames')

        if m.get('PixFmt') is not None:
            self.pix_fmt = m.get('PixFmt')

        if m.get('Profile') is not None:
            self.profile = m.get('Profile')

        if m.get('Rotate') is not None:
            self.rotate = m.get('Rotate')

        if m.get('Sar') is not None:
            self.sar = m.get('Sar')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Timebase') is not None:
            self.timebase = m.get('Timebase')

        if m.get('Width') is not None:
            self.width = m.get('Width')

        return self

class BatchGetMediaInfosResponseBodyMediaInfosMezzanineInfoAudioStreamList(DaraModel):
    def __init__(
        self,
        bitrate: str = None,
        channel_layout: str = None,
        channels: str = None,
        codec_long_name: str = None,
        codec_name: str = None,
        codec_tag: str = None,
        codec_tag_string: str = None,
        codec_time_base: str = None,
        duration: str = None,
        index: str = None,
        lang: str = None,
        num_frames: str = None,
        sample_fmt: str = None,
        sample_rate: str = None,
        start_time: str = None,
        timebase: str = None,
    ):
        # The bitrate.
        self.bitrate = bitrate
        # The output layout of the audio channels. Valid values:
        # 
        # *   **mono**
        # *   **stereo**
        self.channel_layout = channel_layout
        # The number of sound tracks.
        self.channels = channels
        # The full name of the encoding format.
        self.codec_long_name = codec_long_name
        # The short name of the encoding format.
        self.codec_name = codec_name
        # The tag of the encoding format.
        self.codec_tag = codec_tag
        # The tag string of the encoding format.
        self.codec_tag_string = codec_tag_string
        # The time base of the encoder.
        self.codec_time_base = codec_time_base
        # The duration.
        self.duration = duration
        # The sequence number of the audio stream. The value indicates the position of the audio stream in all audio streams.
        self.index = index
        # The language.
        self.lang = lang
        # The total number of frames.
        self.num_frames = num_frames
        # The sampling format.
        self.sample_fmt = sample_fmt
        # The sampling rate.
        self.sample_rate = sample_rate
        # The start time. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.start_time = start_time
        # The time base.
        self.timebase = timebase

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bitrate is not None:
            result['Bitrate'] = self.bitrate

        if self.channel_layout is not None:
            result['ChannelLayout'] = self.channel_layout

        if self.channels is not None:
            result['Channels'] = self.channels

        if self.codec_long_name is not None:
            result['CodecLongName'] = self.codec_long_name

        if self.codec_name is not None:
            result['CodecName'] = self.codec_name

        if self.codec_tag is not None:
            result['CodecTag'] = self.codec_tag

        if self.codec_tag_string is not None:
            result['CodecTagString'] = self.codec_tag_string

        if self.codec_time_base is not None:
            result['CodecTimeBase'] = self.codec_time_base

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.index is not None:
            result['Index'] = self.index

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.num_frames is not None:
            result['NumFrames'] = self.num_frames

        if self.sample_fmt is not None:
            result['SampleFmt'] = self.sample_fmt

        if self.sample_rate is not None:
            result['SampleRate'] = self.sample_rate

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.timebase is not None:
            result['Timebase'] = self.timebase

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bitrate') is not None:
            self.bitrate = m.get('Bitrate')

        if m.get('ChannelLayout') is not None:
            self.channel_layout = m.get('ChannelLayout')

        if m.get('Channels') is not None:
            self.channels = m.get('Channels')

        if m.get('CodecLongName') is not None:
            self.codec_long_name = m.get('CodecLongName')

        if m.get('CodecName') is not None:
            self.codec_name = m.get('CodecName')

        if m.get('CodecTag') is not None:
            self.codec_tag = m.get('CodecTag')

        if m.get('CodecTagString') is not None:
            self.codec_tag_string = m.get('CodecTagString')

        if m.get('CodecTimeBase') is not None:
            self.codec_time_base = m.get('CodecTimeBase')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('Index') is not None:
            self.index = m.get('Index')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('NumFrames') is not None:
            self.num_frames = m.get('NumFrames')

        if m.get('SampleFmt') is not None:
            self.sample_fmt = m.get('SampleFmt')

        if m.get('SampleRate') is not None:
            self.sample_rate = m.get('SampleRate')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Timebase') is not None:
            self.timebase = m.get('Timebase')

        return self

class BatchGetMediaInfosResponseBodyMediaInfosMediaInfo(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        cate_id: int = None,
        cate_name: str = None,
        cover_url: str = None,
        creation_time: str = None,
        description: str = None,
        download_switch: str = None,
        media_id: str = None,
        modification_time: str = None,
        reference_id: str = None,
        restore_expiration: str = None,
        restore_status: str = None,
        snapshots: List[str] = None,
        status: str = None,
        storage_class: str = None,
        storage_location: str = None,
        tags: str = None,
        template_group_id: str = None,
        title: str = None,
        user_data: str = None,
    ):
        # The ID of the application.
        self.app_id = app_id
        # The ID of the category.
        self.cate_id = cate_id
        # The name of the category.
        self.cate_name = cate_name
        # The thumbnail URL of the media asset.
        self.cover_url = cover_url
        # The time when the media asset was created. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.creation_time = creation_time
        # The description of the media asset.
        self.description = description
        # Indicates whether the offline download feature is enabled. If you enable the offline download feature, users can download and play videos by using the ApsaraVideo Player on a local PC. For more information, see [Configure download settings](https://help.aliyun.com/document_detail/86107.html). Valid values:
        # 
        # *   **on**
        # *   **off**
        self.download_switch = download_switch
        # The ID of the media asset.
        self.media_id = media_id
        # The time when the media asset was last updated. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.modification_time = modification_time
        self.reference_id = reference_id
        # The period of time in which the audio file remains in the restored state.
        self.restore_expiration = restore_expiration
        # The restoration status of the media asset. Valid values:
        # 
        # *   **Processing**
        # *   **Success**
        # *   **Failed**
        self.restore_status = restore_status
        # The array of video snapshot URLs.
        self.snapshots = snapshots
        # The status of the video. Valid values:
        # 
        # *   **Uploading**
        # *   **UploadFail**
        # *   **UploadSucc**
        # *   **Transcoding**
        # *   **TranscodeFail**
        # *   **Blocked**
        # *   **Normal**
        self.status = status
        # The storage type. Valid values:
        # 
        # *   **Standard**: All media assets are stored as Standard objects.
        # *   **IA**: All media assets are stored as IA objects.
        # *   **Archive**: All media assets are stored as Archive objects.
        # *   **ColdArchive**: All media assets are stored as Cold Archive objects.
        # *   **SourceIA**: Only the source files are IA objects.
        # *   **SourceArchive**: Only the source files are Archive objects.
        # *   **SourceColdArchive**: Only the source file is stored as a Cold Archive object.
        # *   **Changing**: The storage class of the media asset is being changed.
        # *   **SourceChanging**: The storage class of the media asset is being changed.
        self.storage_class = storage_class
        # The storage address of the media asset.
        self.storage_location = storage_location
        # The tags of the media asset. Separate tags with commas (,).
        self.tags = tags
        # The ID of the transcoding template group.
        self.template_group_id = template_group_id
        # The title of the media asset.
        self.title = title
        # The custom parameters.
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.cate_id is not None:
            result['CateId'] = self.cate_id

        if self.cate_name is not None:
            result['CateName'] = self.cate_name

        if self.cover_url is not None:
            result['CoverURL'] = self.cover_url

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.description is not None:
            result['Description'] = self.description

        if self.download_switch is not None:
            result['DownloadSwitch'] = self.download_switch

        if self.media_id is not None:
            result['MediaId'] = self.media_id

        if self.modification_time is not None:
            result['ModificationTime'] = self.modification_time

        if self.reference_id is not None:
            result['ReferenceId'] = self.reference_id

        if self.restore_expiration is not None:
            result['RestoreExpiration'] = self.restore_expiration

        if self.restore_status is not None:
            result['RestoreStatus'] = self.restore_status

        if self.snapshots is not None:
            result['Snapshots'] = self.snapshots

        if self.status is not None:
            result['Status'] = self.status

        if self.storage_class is not None:
            result['StorageClass'] = self.storage_class

        if self.storage_location is not None:
            result['StorageLocation'] = self.storage_location

        if self.tags is not None:
            result['Tags'] = self.tags

        if self.template_group_id is not None:
            result['TemplateGroupId'] = self.template_group_id

        if self.title is not None:
            result['Title'] = self.title

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('CateId') is not None:
            self.cate_id = m.get('CateId')

        if m.get('CateName') is not None:
            self.cate_name = m.get('CateName')

        if m.get('CoverURL') is not None:
            self.cover_url = m.get('CoverURL')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DownloadSwitch') is not None:
            self.download_switch = m.get('DownloadSwitch')

        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')

        if m.get('ModificationTime') is not None:
            self.modification_time = m.get('ModificationTime')

        if m.get('ReferenceId') is not None:
            self.reference_id = m.get('ReferenceId')

        if m.get('RestoreExpiration') is not None:
            self.restore_expiration = m.get('RestoreExpiration')

        if m.get('RestoreStatus') is not None:
            self.restore_status = m.get('RestoreStatus')

        if m.get('Snapshots') is not None:
            self.snapshots = m.get('Snapshots')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StorageClass') is not None:
            self.storage_class = m.get('StorageClass')

        if m.get('StorageLocation') is not None:
            self.storage_location = m.get('StorageLocation')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('TemplateGroupId') is not None:
            self.template_group_id = m.get('TemplateGroupId')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

