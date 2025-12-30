# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class GetPlayInfoResponseBody(DaraModel):
    def __init__(
        self,
        media_base: main_models.GetPlayInfoResponseBodyMediaBase = None,
        play_info_list: List[main_models.GetPlayInfoResponseBodyPlayInfoList] = None,
        request_id: str = None,
    ):
        # The information about the media asset.
        self.media_base = media_base
        # The information about the audio or video stream.
        self.play_info_list = play_info_list
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.media_base:
            self.media_base.validate()
        if self.play_info_list:
            for v1 in self.play_info_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.media_base is not None:
            result['MediaBase'] = self.media_base.to_map()

        result['PlayInfoList'] = []
        if self.play_info_list is not None:
            for k1 in self.play_info_list:
                result['PlayInfoList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MediaBase') is not None:
            temp_model = main_models.GetPlayInfoResponseBodyMediaBase()
            self.media_base = temp_model.from_map(m.get('MediaBase'))

        self.play_info_list = []
        if m.get('PlayInfoList') is not None:
            for k1 in m.get('PlayInfoList'):
                temp_model = main_models.GetPlayInfoResponseBodyPlayInfoList()
                self.play_info_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetPlayInfoResponseBodyPlayInfoList(DaraModel):
    def __init__(
        self,
        bit_depth: int = None,
        bitrate: str = None,
        creation_time: str = None,
        definition: str = None,
        duration: str = None,
        encrypt: int = None,
        encrypt_type: str = None,
        file_url: str = None,
        format: str = None,
        fps: str = None,
        hdrtype: str = None,
        height: int = None,
        job_id: str = None,
        modification_time: str = None,
        narrow_band_type: str = None,
        play_url: str = None,
        size: int = None,
        status: str = None,
        stream_tags: str = None,
        stream_type: str = None,
        trans_template_type: str = None,
        watermark_id: str = None,
        width: int = None,
    ):
        # The color depth.
        self.bit_depth = bit_depth
        # The bitrate of the media stream. Unit: Kbit/s.
        self.bitrate = bitrate
        # The time when the media stream was created. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.creation_time = creation_time
        # The quality of the media stream. Valid values:
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
        # Indicates whether the media stream is encrypted. Valid values:
        # 
        # *   **0**: The media stream is not encrypted.
        # *   **1**: The media stream is encrypted.
        self.encrypt = encrypt
        # The encryption type of the media stream. Valid values:
        # 
        # *   **AliyunVoDEncryption**: Alibaba Cloud proprietary cryptography
        # *   **HLSEncryption**: HTTP Live Streaming (HLS) encryption
        # 
        # >  If the encryption type is AliyunVoDEncryption, only ApsaraVideo Player SDK can be used to play videos.
        self.encrypt_type = encrypt_type
        # The OSS URL of the file.
        self.file_url = file_url
        # The format of the media stream.
        # 
        # *   If the media asset is a video file, the valid values are **mp4** and **m3u8**.
        # *   If the media asset is an audio-only file, the value is **mp3**.
        self.format = format
        # The frame rate of the media stream. Unit: frames per second (FPS).
        self.fps = fps
        # The high dynamic range (HDR) type of the media stream. Valid values:
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
        # The task ID.
        self.job_id = job_id
        # The time when the media stream was updated. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.modification_time = modification_time
        # The type of Narrowband HD™ transcoding. Valid values:
        # 
        # *   **0**: standard transcoding
        # *   **1.0**: Narrowband HD™ 1.0 transcoding
        # *   **2.0**: Narrowband HD™ 2.0 transcoding
        # 
        # This parameter is returned only when a definition that is available in the built-in Narrowband HD™ 1.0 transcoding template is specified. For more information, see the [Definition parameter in TranscodeTemplate](https://help.aliyun.com/document_detail/52839.html) table.
        self.narrow_band_type = narrow_band_type
        # The playback URL of the media stream.
        self.play_url = play_url
        # The size of the media stream. Unit: bytes.
        self.size = size
        # The status of the media stream. Valid values:
        # 
        # *   **Normal**
        # *   **Invisible**
        self.status = status
        # The tags of the media stream, which are used to identify the transcoding type.
        self.stream_tags = stream_tags
        # The type of the media stream. If the media stream is a video stream, the value is **video**. If the media stream is an audio-only stream, the value is **audio**.
        self.stream_type = stream_type
        # The type of the transcoding template. Valid values:
        # 
        # *   Normal: standard transcoding
        # *   AudioTranscode: audio transcoding
        # *   Remux: container format conversion
        # *   NarrowBandV1: Narrowband HD™ 1.0
        # *   NarrowBandV2: Narrowband HD™ 2.0
        # *   UHD: audio and video enhancement (ultra-high definition)
        self.trans_template_type = trans_template_type
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

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.definition is not None:
            result['Definition'] = self.definition

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.encrypt is not None:
            result['Encrypt'] = self.encrypt

        if self.encrypt_type is not None:
            result['EncryptType'] = self.encrypt_type

        if self.file_url is not None:
            result['FileURL'] = self.file_url

        if self.format is not None:
            result['Format'] = self.format

        if self.fps is not None:
            result['Fps'] = self.fps

        if self.hdrtype is not None:
            result['HDRType'] = self.hdrtype

        if self.height is not None:
            result['Height'] = self.height

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.modification_time is not None:
            result['ModificationTime'] = self.modification_time

        if self.narrow_band_type is not None:
            result['NarrowBandType'] = self.narrow_band_type

        if self.play_url is not None:
            result['PlayURL'] = self.play_url

        if self.size is not None:
            result['Size'] = self.size

        if self.status is not None:
            result['Status'] = self.status

        if self.stream_tags is not None:
            result['StreamTags'] = self.stream_tags

        if self.stream_type is not None:
            result['StreamType'] = self.stream_type

        if self.trans_template_type is not None:
            result['TransTemplateType'] = self.trans_template_type

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

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('Definition') is not None:
            self.definition = m.get('Definition')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('Encrypt') is not None:
            self.encrypt = m.get('Encrypt')

        if m.get('EncryptType') is not None:
            self.encrypt_type = m.get('EncryptType')

        if m.get('FileURL') is not None:
            self.file_url = m.get('FileURL')

        if m.get('Format') is not None:
            self.format = m.get('Format')

        if m.get('Fps') is not None:
            self.fps = m.get('Fps')

        if m.get('HDRType') is not None:
            self.hdrtype = m.get('HDRType')

        if m.get('Height') is not None:
            self.height = m.get('Height')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('ModificationTime') is not None:
            self.modification_time = m.get('ModificationTime')

        if m.get('NarrowBandType') is not None:
            self.narrow_band_type = m.get('NarrowBandType')

        if m.get('PlayURL') is not None:
            self.play_url = m.get('PlayURL')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StreamTags') is not None:
            self.stream_tags = m.get('StreamTags')

        if m.get('StreamType') is not None:
            self.stream_type = m.get('StreamType')

        if m.get('TransTemplateType') is not None:
            self.trans_template_type = m.get('TransTemplateType')

        if m.get('WatermarkId') is not None:
            self.watermark_id = m.get('WatermarkId')

        if m.get('Width') is not None:
            self.width = m.get('Width')

        return self

class GetPlayInfoResponseBodyMediaBase(DaraModel):
    def __init__(
        self,
        cate_id: int = None,
        cover_url: str = None,
        creation_time: str = None,
        description: str = None,
        media_id: str = None,
        media_tags: str = None,
        media_type: str = None,
        status: str = None,
        title: str = None,
    ):
        # The category ID. You can use one of the following methods to obtain the ID:
        # 
        # *   Log on to the [Intelligent Media Services (IMS) console](https://ims.console.aliyun.com) and choose **Media Asset Management** > **Category Management** to view the category ID.
        # *   View the value of the CateId parameter returned by the AddCategory operation that you called to create a category.
        # *   View the value of the CateId parameter returned by the GetCategories operation that you called to query a category.
        self.cate_id = cate_id
        # The URL of the thumbnail.
        self.cover_url = cover_url
        # The time when the media asset was created.
        self.creation_time = creation_time
        # The content description.
        self.description = description
        # The ID of the media asset.
        self.media_id = media_id
        # The tags.
        # 
        # *   Up to 16 tags are supported.
        # *   Multiple tags are separated by commas (,).
        # *   Each tag can be up to 32 bytes in length.
        # *   The value is encoded in UTF-8.
        self.media_tags = media_tags
        # The type of the media asset. Valid values:
        # 
        # video audio
        self.media_type = media_type
        # The resource status. Valid values:
        # 
        # Init: the initial state, which indicates that the source file is not ready.
        # 
        # Preparing: The source file is being prepared. For example, the file is being uploaded or edited.
        # 
        # PrepareFail: The source file failed to be prepared. For example, the information of the source file failed to be obtained.
        # 
        # Normal: The source file is ready.
        self.status = status
        # The title.
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cate_id is not None:
            result['CateId'] = self.cate_id

        if self.cover_url is not None:
            result['CoverURL'] = self.cover_url

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.description is not None:
            result['Description'] = self.description

        if self.media_id is not None:
            result['MediaId'] = self.media_id

        if self.media_tags is not None:
            result['MediaTags'] = self.media_tags

        if self.media_type is not None:
            result['MediaType'] = self.media_type

        if self.status is not None:
            result['Status'] = self.status

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CateId') is not None:
            self.cate_id = m.get('CateId')

        if m.get('CoverURL') is not None:
            self.cover_url = m.get('CoverURL')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')

        if m.get('MediaTags') is not None:
            self.media_tags = m.get('MediaTags')

        if m.get('MediaType') is not None:
            self.media_type = m.get('MediaType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

