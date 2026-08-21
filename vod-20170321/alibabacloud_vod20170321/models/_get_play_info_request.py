# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetPlayInfoRequest(DaraModel):
    def __init__(
        self,
        addition_type: str = None,
        auth_timeout: int = None,
        codec_name: str = None,
        definition: str = None,
        digital_watermark_type: str = None,
        formats: str = None,
        output_type: str = None,
        play_config: str = None,
        re_auth_info: str = None,
        reference_id: str = None,
        result_type: str = None,
        stream_type: str = None,
        trace: str = None,
        video_id: str = None,
    ):
        # Obtains the URL of the China-accessible bullet screen mask data. Valid values: **danmu**.
        # 
        # > This parameter takes effect only when `outputType` is set to `cdn`.
        self.addition_type = addition_type
        # The validity period of the playback URL. Unit: seconds.
        # 
        # - If OutputType is set to **cdn**:
        # 
        #     - The playback URL expires periodically only when URL authentication is enabled. Otherwise, the URL is permanently valid. For information about how to enable and configure URL authentication, refer to [URL authentication](https://help.aliyun.com/document_detail/86090.html).
        #     - Minimum value: **1**.
        #     - Maximum value: unlimited.
        #     - Default value: If this parameter is not specified, the default validity period configured in URL authentication is used.
        # 
        # - If OutputType is set to **oss**:
        # 
        #     - The playback URL expires periodically only when the storage permission is private. Otherwise, the URL is permanently valid.
        #     - Minimum value: **1**.
        #     - Maximum value: To reduce security risks to the origin server, when audio or video files are stored in an ApsaraVideo VOD system bucket, the maximum value is **604800** (7 days). When audio or video files are stored in your own OSS bucket, the maximum value is **129600** (36 hours). If the maximum value does not meet your requirements, set OutputType to **cdn** and configure URL authentication to set a longer validity period.
        #     - Default value: If this parameter is not specified, the default value is **3600**.
        self.auth_timeout = auth_timeout
        self.codec_name = codec_name
        # The definition of the video stream. Separate multiple definitions with commas (,). Valid values:
        # 
        # - **FD**: low definition.
        # - **LD**: standard definition.
        # - **SD**: high definition.
        # - **HD**: ultra-high definition.
        # - **OD**: original definition.
        # - **2K**: 2K.
        # - **4K**: 4K.
        # - **SQ**: standard sound quality.
        # - **HQ**: high sound quality.
        # - **AUTO**: adaptive bitrate streaming.
        # 
        # > - By default, streams of all definitions are returned.
        # > - When generating tracing watermarks, this parameter is required and must be consistent with the definition configured during tracing watermark transcoding.
        # > - The AUTO definition is returned only when transcoding packaging is configured in the transcoding template. For more information, refer to [PackageSetting: transcoding packaging settings](~~52839#title-4fk-cg8-gzx~~).
        self.definition = definition
        # The digital watermarking type. Valid values:
        # 
        # - TraceMark: tracing watermark.
        # - CopyrightMark: copyright watermark.
        self.digital_watermark_type = digital_watermark_type
        # The media stream format. Separate multiple formats with commas (,). Valid values:
        # 
        # - **mp4**
        # - **m3u8**
        # - **mp3**
        # - **flv**
        # - **mpd**
        # 
        # 
        # > - By default, streams in all formats are returned.
        # > - The mpd format is returned only when the `dash` container format is configured in the transcoding template. For more information, refer to [Container: container format](~~52839#title-7rr-3hj-gy5~~).
        self.formats = formats
        # The type of the output URL. Valid values:
        # 
        # - **oss**: back-to-origin URL.
        # - **cdn** (default): accelerated URL.
        self.output_type = output_type
        # The custom playback settings. The value is a JSON string that supports specifying domain name playback settings. For details about parameter construction, refer to [PlayConfig](~~86952#section-9g7-s9b-v7z~~).
        # 
        # > - If PlayConfig is not set or `PlayDomain` within it is not set, the operation uses the default domain name configured in ApsaraVideo VOD. If no default domain name is configured, the most recently modified domain name is used as the playback domain name based on reverse chronological order of modification time. To prevent an unexpected domain name from being returned, set a default playback domain name. Log on to the [ApsaraVideo VOD console](https://vod.console.aliyun.com) and choose **Configuration Management** > **Media Management** > **Storage** > **Manage** > **Domain names that perform origin fetch from this storage address** to set the default playback domain name.
        # > - When the `EncryptType` parameter in PlayConfig is set to `AliyunVoDEncryption`, the playback URL of the privately encrypted stream is not returned by default to ensure video security. To return the playback URL of the privately encrypted stream, set the `ResultType` parameter to `Multiple`.
        self.play_config = play_config
        # The CDN reauthentication parameter. The value is a JSON string. When type A signing is enabled for URL authentication, you can use this parameter to set the `uid` and `rand` of the authentication URL. For more information, refer to [Type A signing](https://help.aliyun.com/document_detail/2249352.html).
        self.re_auth_info = re_auth_info
        # The custom ID. Only lowercase letters, uppercase letters, digits, hyphens, and underscores are supported. The length is 6 to 64 characters. The ID is unique per user.
        self.reference_id = reference_id
        # The type of the returned data. Valid values:
        # 
        # - **Single** (default): returns only the latest transcoded stream for each definition and format.
        # - **Multiple**: returns all transcoded streams for each definition and format.
        self.result_type = result_type
        # The media stream type. Separate multiple types with commas (,). Valid values:
        # 
        # - **video**: video.
        # - **audio**: audio.
        # 
        # By default, streams of all types are returned.
        self.stream_type = stream_type
        # The custom digital watermarking settings.
        # - When `DigitalWatermarkType` is set to `TraceMark`, pass in this parameter to set the tracing watermark information for the video and return the video stream that contains the watermark information. Only English letters, digits, and Chinese characters are supported. A maximum of 1024 characters are supported.
        # - When `DigitalWatermarkType` is set to `CopyrightMark`, `Trace` corresponds to the **watermark text** configured when the watermark template was created. Pass in this parameter to query and return the video stream with the specified watermark text.
        self.trace = trace
        # The audio or video ID. Only a single audio or video ID is supported. You can obtain the ID by using the following methods:
        # - For audio or video files uploaded through the console, log on to the [ApsaraVideo VOD console](https://vod.console.aliyun.com) and choose **Media Files** > **Audio/Video** to view the audio or video ID.
        # - When uploading audio or video files by calling the [CreateUploadVideo](https://help.aliyun.com/document_detail/55407.html) operation, the audio or video ID is the value of the VideoId response parameter.
        # - After the audio or video file is uploaded, call the [SearchMedia](https://help.aliyun.com/document_detail/86044.html) operation to query the audio or video ID, which is the value of the VideoId response parameter.
        self.video_id = video_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.addition_type is not None:
            result['AdditionType'] = self.addition_type

        if self.auth_timeout is not None:
            result['AuthTimeout'] = self.auth_timeout

        if self.codec_name is not None:
            result['CodecName'] = self.codec_name

        if self.definition is not None:
            result['Definition'] = self.definition

        if self.digital_watermark_type is not None:
            result['DigitalWatermarkType'] = self.digital_watermark_type

        if self.formats is not None:
            result['Formats'] = self.formats

        if self.output_type is not None:
            result['OutputType'] = self.output_type

        if self.play_config is not None:
            result['PlayConfig'] = self.play_config

        if self.re_auth_info is not None:
            result['ReAuthInfo'] = self.re_auth_info

        if self.reference_id is not None:
            result['ReferenceId'] = self.reference_id

        if self.result_type is not None:
            result['ResultType'] = self.result_type

        if self.stream_type is not None:
            result['StreamType'] = self.stream_type

        if self.trace is not None:
            result['Trace'] = self.trace

        if self.video_id is not None:
            result['VideoId'] = self.video_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdditionType') is not None:
            self.addition_type = m.get('AdditionType')

        if m.get('AuthTimeout') is not None:
            self.auth_timeout = m.get('AuthTimeout')

        if m.get('CodecName') is not None:
            self.codec_name = m.get('CodecName')

        if m.get('Definition') is not None:
            self.definition = m.get('Definition')

        if m.get('DigitalWatermarkType') is not None:
            self.digital_watermark_type = m.get('DigitalWatermarkType')

        if m.get('Formats') is not None:
            self.formats = m.get('Formats')

        if m.get('OutputType') is not None:
            self.output_type = m.get('OutputType')

        if m.get('PlayConfig') is not None:
            self.play_config = m.get('PlayConfig')

        if m.get('ReAuthInfo') is not None:
            self.re_auth_info = m.get('ReAuthInfo')

        if m.get('ReferenceId') is not None:
            self.reference_id = m.get('ReferenceId')

        if m.get('ResultType') is not None:
            self.result_type = m.get('ResultType')

        if m.get('StreamType') is not None:
            self.stream_type = m.get('StreamType')

        if m.get('Trace') is not None:
            self.trace = m.get('Trace')

        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')

        return self

