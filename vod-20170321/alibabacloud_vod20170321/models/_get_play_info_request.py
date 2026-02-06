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
        # The URL of the masked live comment data. Value: **danmu**.
        # 
        # >  This parameter takes effect only when the `outputType` parameter is set to `cdn`.
        self.addition_type = addition_type
        # The validity period of the playback URL. Unit: seconds.
        # 
        # *   If you set OutputType to **cdn**:
        # 
        #     *   The playback URL has a validity period only if URL signing is enabled. Otherwise, the playback URL is permanently valid. For more information about how to enable and configure URL signing, see [URL signing](https://help.aliyun.com/document_detail/86090.html).
        #     *   Minimum value: **1**.
        #     *   Maximum value: unlimited.
        #     *   Default value: The default validity period that is specified in URL signing is used.
        # 
        # *   If you set OutputType to **oss**:
        # 
        #     *   This parameter takes effect only when the ACL of the Object Storage Service (OSS) bucket is private. Otherwise, the playback URL does not expire.
        #     *   Minimum value: **1**.
        #     *   Maximum value: If the media file is stored in the VOD bucket, the maximum validity period is **2592000** (30 days). If the media file is stored in an OSS bucket, the maximum validity period is **129600** (36 hours). This limit is imposed to reduce security risks of the origin server. If you require a longer validity period, set OutputType to **cdn** and configure URL signing to specify a longer validity period.
        #     *   Default value: **3600**.
        self.auth_timeout = auth_timeout
        self.codec_name = codec_name
        # The quality of the video stream. Separate multiple qualities with commas (,). Valid values:
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
        # 
        # > *   By default, ApsaraVideo VOD returns video streams in all the preceding qualities.
        # > *   However, video streams for adaptive bitrate streaming are returned only if the PackageSetting parameter is specified in the transcoding template. For more information, see the [PackageSetting parameter in the TranscodeTemplate table](~~52839#title-4fk-cg8-gzx~~).
        self.definition = definition
        # The type of the digital watermark. Valid values:
        # 
        # *   TraceMark: tracing watermark
        # *   CopyrightMark: copyright watermark
        self.digital_watermark_type = digital_watermark_type
        # The format of the media stream. Separate multiple formats with commas (,). Valid values:
        # 
        # *   **mp4**
        # *   **m3u8**
        # *   **mp3**
        # *   **flv**
        # *   **mpd**
        # 
        # > *   By default, ApsaraVideo VOD returns video streams in all the preceding formats.
        # >*   However, video streams in the MPD format are returned only if the `dash` container format is specified in the transcoding template. For more information, see the [Container parameter in the TranscodeTemplate table](~~52839#title-7rr-3hj-gy5~~).
        self.formats = formats
        # The type of the output URL. Default value: oss. Valid values:
        # 
        # *   **oss**
        # *   **cdn**
        self.output_type = output_type
        # The custom playback configuration. The value must be a JSON string. You can specify a domain name for playback. For more information, see [PlayConfig](~~86952#section-9g7-s9b-v7z~~).
        # 
        # > *   If you do not set the PlayConfig parameter or the `PlayDomain` parameter that is nested under the PlayConfig parameter, the default domain name specified in ApsaraVideo VOD is used in this operation. If no default domain name is specified, the domain names are queried in reverse chronological order based on the time when the domain names were last modified. To prevent domain name issues, we recommend that you perform the following steps to specify the default playback domain name: Log on to the [ApsaraVideo VOD console](https://vod.console.aliyun.com). In the left-side navigation pane, choose **Configuration Management** > **Media Management** > **Storage**. Find the domain name that you want to configure and click **Manage** in the Actions column. On the page that appears, set the default playback domain name in the **Origin Domain Name** section.
        # > *   If you set the `EncryptType` parameter nested under the PlayConfig parameter to `AliyunVoDEncryption`, the playback URLs of videos encrypted by using Alibaba Cloud proprietary cryptography are not automatically returned to ensure video security. To return playback URLs of videos encrypted by using Alibaba Cloud proprietary cryptography, you must set the `ResultType` parameter to `Multiple`.
        self.play_config = play_config
        # The CDN reauthentication configuration. The value must be a JSON string. If CDN reauthentication is enabled, you can use this parameter to specify the `UID` and `rand` fields for URL authentication. For more information, see [URL authentication](https://help.aliyun.com/document_detail/2249352.html).
        self.re_auth_info = re_auth_info
        self.reference_id = reference_id
        # The type of the data to return. Default value: Single. Valid values:
        # 
        # *   **Single**: Only one latest transcoded stream is returned for each quality and format.
        # *   **Multiple**: All transcoded streams are returned for each quality and format.
        self.result_type = result_type
        # The type of the media stream. Separate multiple types with commas (,). Valid values:
        # 
        # *   **video**
        # *   **audio**
        # 
        # By default, video and audio streams are returned.
        self.stream_type = stream_type
        # The custom digital watermark.
        # 
        # *   If you set `DigitalWatermarkType` to `TraceMark`, specify this parameter to configure the video tracing watermark and return the video stream that contains the watermark. The value can be up to 1,024 characters in length and can contain letters and digits.
        # *   If you set `DigitalWatermarkType` to `CopyrightMark`, specify the **watermark text** that you created for the watermark template for this parameter.`` You can specify this parameter to query and return the video stream that contains the specified watermark text.
        self.trace = trace
        # The ID of the media file. You can specify only one ID. You can use one of the following methods to obtain the ID:
        # 
        # *   Log on to the [ApsaraVideo VOD console](https://vod.console.aliyun.com). In the left-side navigation pane, choose **Media Files** > **Audio/Video**. On the page that appears, view the media ID.
        # *   Obtain the value of the VideoId parameter in the response to the [CreateUploadVideo](https://help.aliyun.com/document_detail/55407.html) operation that you called to upload the audio or video file.
        # *   Obtain the value of VideoId by calling the [SearchMedia](https://help.aliyun.com/document_detail/86044.html) operation. This method is applicable to files that have been uploaded.
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

