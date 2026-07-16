# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_imm20200930 import models as main_models
from darabonba.model import DaraModel

class TargetVideo(DaraModel):
    def __init__(
        self,
        disable_video: bool = None,
        filter_video: main_models.TargetVideoFilterVideo = None,
        stream: List[int] = None,
        transcode_video: main_models.TargetVideoTranscodeVideo = None,
    ):
        # Specifies whether to disable video stream generation. Valid values:
        # 
        # - true: Disables video stream generation. The output file will not contain a video stream.
        # 
        # - false (default): Enables video stream generation.
        self.disable_video = disable_video
        # The video processing parameters. This parameter is invalid if **TranscodeVideo** is empty or if **TranscodeVideo.Codec** is set to copy.
        # 
        # > You cannot set this parameter for the GenerateVideoPlaylist API.
        self.filter_video = filter_video
        # A list of index numbers for the source video streams to process. If you leave this parameter empty (default), the system processes the video stream with the smallest index number (the first video stream). If you set the index number to a value greater than 100, the system processes all video streams.
        # 
        # - Example: `[0,1]` processes video streams with index numbers 0 and 1. `[1]` processes the video stream with index number 1. `[101]` processes all video streams.
        # 
        # > The system only processes video streams with existing index numbers. If a video stream corresponding to an index number does not exist, the system ignores that index number.
        self.stream = stream
        # The video transcoding parameters. An empty value disables video processing. The output file will not contain a video stream.
        # 
        # > Do not disable video processing by leaving this parameter empty.
        self.transcode_video = transcode_video

    def validate(self):
        if self.filter_video:
            self.filter_video.validate()
        if self.transcode_video:
            self.transcode_video.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.disable_video is not None:
            result['DisableVideo'] = self.disable_video

        if self.filter_video is not None:
            result['FilterVideo'] = self.filter_video.to_map()

        if self.stream is not None:
            result['Stream'] = self.stream

        if self.transcode_video is not None:
            result['TranscodeVideo'] = self.transcode_video.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisableVideo') is not None:
            self.disable_video = m.get('DisableVideo')

        if m.get('FilterVideo') is not None:
            temp_model = main_models.TargetVideoFilterVideo()
            self.filter_video = temp_model.from_map(m.get('FilterVideo'))

        if m.get('Stream') is not None:
            self.stream = m.get('Stream')

        if m.get('TranscodeVideo') is not None:
            temp_model = main_models.TargetVideoTranscodeVideo()
            self.transcode_video = temp_model.from_map(m.get('TranscodeVideo'))

        return self

class TargetVideoTranscodeVideo(DaraModel):
    def __init__(
        self,
        adaptive_resolution_direction: bool = None,
        bframes: int = None,
        bitrate: int = None,
        bitrate_option: str = None,
        buffer_size: int = None,
        crf: float = None,
        codec: str = None,
        frame_rate: float = None,
        frame_rate_option: str = None,
        gopsize: int = None,
        max_bitrate: int = None,
        pixel_format: str = None,
        refs: int = None,
        resolution: str = None,
        resolution_option: str = None,
        rotation: int = None,
        scale_type: str = None,
        video_slim: int = None,
    ):
        # Specifies whether to enable adaptive resolution for long and short edges. Valid values:
        # 
        # - true: Yes. In this case, the format for the **Resolution** parameter is `long edge × short edge`.
        # 
        # - false (default): No. In this case, the format for the **Resolution** parameter is `width × height`.
        self.adaptive_resolution_direction = adaptive_resolution_direction
        # The number of consecutive B-frames. The default value is 3.
        self.bframes = bframes
        # The video stream bitrate in bits per second (bit/s).
        # 
        # > This parameter is mutually exclusive with **CRF**. If both this parameter and the **CRF** parameter are empty, the system encodes the video with a CRF value of 23.
        self.bitrate = bitrate
        # The video bitrate option. Valid values:
        # 
        # - fixed: Always uses the specified target video bitrate.
        # 
        # - adaptive: Uses the source video bitrate if it is lower than the specified target video bitrate.
        # 
        # - fall: The task fails if the source video bitrate is lower than the specified target video bitrate.
        # 
        # Default value:
        # 
        # - For the CreateMediaConvert API, the default value is fixed.
        # 
        # - For the GenerateVideoPlaylist API, the default value is adaptive.
        # 
        # > This parameter must be set together with the **Bitrate** parameter.
        self.bitrate_option = bitrate_option
        # The size of the decoding buffer for dynamic bitrate, in bits per second (bps).
        # 
        # > This parameter is effective only when used with the **CRF** parameter.
        self.buffer_size = buffer_size
        # Specifies the Constant Rate Factor (CRF) mode. This parameter is mutually exclusive with **Bitrate**. The value ranges from 0 to 51. A larger value indicates lower image quality. A value from 18 to 38 is recommended.
        self.crf = crf
        # The video encoding format. Valid values:
        # 
        # - For the CreateMediaConvert API: copy (default), h264, h265, and vp9.
        # 
        # 
        #   >Warning: 
        # 
        #   If you set this parameter to copy, the system directly copies the video stream to the output file. In this case, the other parameters under **TranscodeVideo** are invalid. The copy value cannot be used for video concatenation and is typically used for container format conversion.
        # 
        #   
        # 
        # - For the GenerateVideoPlaylist API: h264 (default) and h265.
        self.codec = codec
        # The video frame rate. By default, this is the same as the source video.
        self.frame_rate = frame_rate
        # The frame rate option. Valid values:
        # 
        # - fixed: Always uses the specified target video frame rate.
        # 
        # - adaptive: Uses the source video frame rate if it is lower than the specified target video frame rate.
        # 
        # - fall: The task fails if the source video frame rate is lower than the specified target video frame rate.
        # 
        # Default value:
        # 
        # - For the CreateMediaConvert API, the default value is fixed.
        # 
        # - For the GenerateVideoPlaylist API, the default value is adaptive.
        # 
        # > This parameter must be set together with the **FrameRate** parameter.
        self.frame_rate_option = frame_rate_option
        # The size of the Group of Pictures (GOP) in frames. The default value is 150.
        # 
        # > This parameter is not supported by the GenerateVideoPlaylist API.
        self.gopsize = gopsize
        # The maximum bitrate limit for dynamic bitrate. When you use this parameter, you must also specify the BufferSize parameter.
        # 
        # > This parameter is effective only when used with the **CRF** parameter.
        self.max_bitrate = max_bitrate
        # The pixel format. By default, this is the same as the source video. Valid values:
        # 
        # - yuv420p
        # 
        # - yuv422p
        # 
        # - yuv444p
        # 
        # - yuv420p10le
        # 
        # - yuv422p10le
        # 
        # - yuv444p10le
        # 
        # - yuva420p
        # 
        # > The yuva420p value is available only for the CreateMediaConvert API, and the **Codec** parameter must be set to vp9.
        self.pixel_format = pixel_format
        # The number of reference frames. The default value is 2.
        self.refs = refs
        # The resolution of the output video in the format of `width × height`. By default, this is the same as the playback resolution of the source video. You can configure both width and height, or only width or height. You can also use this parameter with the **AdaptiveResolutionDirection** parameter to configure both the long and short edges, or only the long or short edge. The value for a single edge ranges from (0, 4096].
        # 
        # - Example 1: If **AdaptiveResolutionDirection** is set to false, `1280x720` sets the width to 1280 and the height to 720. `1280x` sets the width to 1280 and keeps the height the same as the source video. `x720` sets the height to 720 and keeps the width the same as the source video.
        # 
        # - Example 2: If **AdaptiveResolutionDirection** is set to true, `1280x720` sets the long edge to 1280 and the short edge to 720. `1280x` sets the long edge to 1280 and keeps the short edge the same as the source video. `x720` sets the short edge to 720 and keeps the long edge the same as the source video.
        # 
        # > If the source video contains rotation information, the width, height, long edge, and short edge are determined based on the rotated video, which means the playback resolution is used.
        self.resolution = resolution
        # The resolution option. Valid values:
        # 
        # - fixed: Always uses the specified target video resolution.
        # 
        # - adaptive: Uses the source video resolution if its area is smaller than the area of the specified target video resolution.
        # 
        # - fall: The task fails if the area of the source video resolution is smaller than the area of the specified target video resolution.
        # 
        # Default value:
        # 
        # - For the CreateMediaConvert API, the default value is fixed.
        # 
        # - For the GenerateVideoPlaylist API, the default value is adaptive.
        # 
        # > This parameter must be set together with the **Resolution** parameter.
        self.resolution_option = resolution_option
        # The clockwise rotation angle of the video in degrees. Valid values:
        # 
        # - 0 (default)
        # 
        # - 90
        # 
        # - 180
        # 
        # - 270
        self.rotation = rotation
        # The scaling mode. Valid values:
        # 
        # - stretch (default): Fixes the width and height or the long and short edges, and forces scaling to stretch and fill any blank areas.
        # 
        # - crop: Scales the video proportionally to the minimum resolution that extends beyond the specified rectangle (defined by width/height or long/short edges), and then center-crops the excess parts.
        # 
        # - fill: Scales the video proportionally to the maximum resolution that fits within the specified rectangle (defined by width/height or long/short edges), and then center-fills any blank areas with black.
        # 
        # - fit: Scales the video proportionally to the maximum resolution that fits within the specified rectangle (defined by width/height or long/short edges).
        # 
        # > This parameter must be set together with the **Resolution** parameter.
        self.scale_type = scale_type
        # Enables the Narrowband HD mode. Set the value as follows:
        # 
        # 0: The default value. Disables the mode.
        # 
        # 1: Enables transcoding in Narrowband HD mode.
        # 
        # > For best results, use the officially recommended Bitrate or CRF parameters for video transcoding and encoding in Narrowband HD mode.
        # 
        # >Notice: 
        # 
        # Narrowband HD only supports the h.264/h.265 format, yuv420p, and an 8-bit depth. It does not support transcoding output for multiple target videos or video concatenation. For more information, see [Introduction to Narrowband HD](https://help.aliyun.com/document_detail/2984556.html).
        self.video_slim = video_slim

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.adaptive_resolution_direction is not None:
            result['AdaptiveResolutionDirection'] = self.adaptive_resolution_direction

        if self.bframes is not None:
            result['BFrames'] = self.bframes

        if self.bitrate is not None:
            result['Bitrate'] = self.bitrate

        if self.bitrate_option is not None:
            result['BitrateOption'] = self.bitrate_option

        if self.buffer_size is not None:
            result['BufferSize'] = self.buffer_size

        if self.crf is not None:
            result['CRF'] = self.crf

        if self.codec is not None:
            result['Codec'] = self.codec

        if self.frame_rate is not None:
            result['FrameRate'] = self.frame_rate

        if self.frame_rate_option is not None:
            result['FrameRateOption'] = self.frame_rate_option

        if self.gopsize is not None:
            result['GOPSize'] = self.gopsize

        if self.max_bitrate is not None:
            result['MaxBitrate'] = self.max_bitrate

        if self.pixel_format is not None:
            result['PixelFormat'] = self.pixel_format

        if self.refs is not None:
            result['Refs'] = self.refs

        if self.resolution is not None:
            result['Resolution'] = self.resolution

        if self.resolution_option is not None:
            result['ResolutionOption'] = self.resolution_option

        if self.rotation is not None:
            result['Rotation'] = self.rotation

        if self.scale_type is not None:
            result['ScaleType'] = self.scale_type

        if self.video_slim is not None:
            result['VideoSlim'] = self.video_slim

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdaptiveResolutionDirection') is not None:
            self.adaptive_resolution_direction = m.get('AdaptiveResolutionDirection')

        if m.get('BFrames') is not None:
            self.bframes = m.get('BFrames')

        if m.get('Bitrate') is not None:
            self.bitrate = m.get('Bitrate')

        if m.get('BitrateOption') is not None:
            self.bitrate_option = m.get('BitrateOption')

        if m.get('BufferSize') is not None:
            self.buffer_size = m.get('BufferSize')

        if m.get('CRF') is not None:
            self.crf = m.get('CRF')

        if m.get('Codec') is not None:
            self.codec = m.get('Codec')

        if m.get('FrameRate') is not None:
            self.frame_rate = m.get('FrameRate')

        if m.get('FrameRateOption') is not None:
            self.frame_rate_option = m.get('FrameRateOption')

        if m.get('GOPSize') is not None:
            self.gopsize = m.get('GOPSize')

        if m.get('MaxBitrate') is not None:
            self.max_bitrate = m.get('MaxBitrate')

        if m.get('PixelFormat') is not None:
            self.pixel_format = m.get('PixelFormat')

        if m.get('Refs') is not None:
            self.refs = m.get('Refs')

        if m.get('Resolution') is not None:
            self.resolution = m.get('Resolution')

        if m.get('ResolutionOption') is not None:
            self.resolution_option = m.get('ResolutionOption')

        if m.get('Rotation') is not None:
            self.rotation = m.get('Rotation')

        if m.get('ScaleType') is not None:
            self.scale_type = m.get('ScaleType')

        if m.get('VideoSlim') is not None:
            self.video_slim = m.get('VideoSlim')

        return self

class TargetVideoFilterVideo(DaraModel):
    def __init__(
        self,
        delogos: List[main_models.TargetVideoFilterVideoDelogos] = None,
        desensitization: main_models.TargetVideoFilterVideoDesensitization = None,
        speed: float = None,
        watermarks: List[main_models.TargetVideoFilterVideoWatermarks] = None,
    ):
        # Blurs a rectangular area of the video to remove logos, station icons, and other elements.
        self.delogos = delogos
        # The video desensitization configuration.
        # 
        # >Notice: 
        # 
        # - This parameter applies only to the CreateMediaConvertTask API.
        self.desensitization = desensitization
        # The video playback speed setting. The value ranges from 0.5 to 1.0. The default value is 1.0.
        # 
        # > - This is the ratio of the default playback speed of the transcoded media file to that of the source media file. This is not a high-speed transcoding feature.
        # 
        # >Notice: 
        # 
        # - This parameter applies only to the CreateMediaConvertTask API.
        self.speed = speed
        # A list of video watermarks.
        self.watermarks = watermarks

    def validate(self):
        if self.delogos:
            for v1 in self.delogos:
                 if v1:
                    v1.validate()
        if self.desensitization:
            self.desensitization.validate()
        if self.watermarks:
            for v1 in self.watermarks:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Delogos'] = []
        if self.delogos is not None:
            for k1 in self.delogos:
                result['Delogos'].append(k1.to_map() if k1 else None)

        if self.desensitization is not None:
            result['Desensitization'] = self.desensitization.to_map()

        if self.speed is not None:
            result['Speed'] = self.speed

        result['Watermarks'] = []
        if self.watermarks is not None:
            for k1 in self.watermarks:
                result['Watermarks'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.delogos = []
        if m.get('Delogos') is not None:
            for k1 in m.get('Delogos'):
                temp_model = main_models.TargetVideoFilterVideoDelogos()
                self.delogos.append(temp_model.from_map(k1))

        if m.get('Desensitization') is not None:
            temp_model = main_models.TargetVideoFilterVideoDesensitization()
            self.desensitization = temp_model.from_map(m.get('Desensitization'))

        if m.get('Speed') is not None:
            self.speed = m.get('Speed')

        self.watermarks = []
        if m.get('Watermarks') is not None:
            for k1 in m.get('Watermarks'):
                temp_model = main_models.TargetVideoFilterVideoWatermarks()
                self.watermarks.append(temp_model.from_map(k1))

        return self

class TargetVideoFilterVideoWatermarks(DaraModel):
    def __init__(
        self,
        border_color: str = None,
        border_width: int = None,
        content: str = None,
        duration: float = None,
        dx: float = None,
        dy: float = None,
        font_apha: float = None,
        font_color: str = None,
        font_name: str = None,
        font_size: int = None,
        height: float = None,
        refer_pos: str = None,
        start_time: float = None,
        type: str = None,
        uri: str = None,
        width: float = None,
    ):
        # The outline color of the watermark text. The format is #RRGGBB. The default value is #000000. You can also enter values such as "red" or "green".
        # 
        # >Notice: 
        # 
        # This parameter is effective only when the `Type` parameter is set to `text`.
        self.border_color = border_color
        # The outline width for the text watermark, in pixels (px). The value must be an integer from 0 to 4096. The default value is 0.
        # 
        # >Notice: 
        # 
        # This parameter is effective only when the `Type` parameter is set to `text`.
        self.border_width = border_width
        # The content of the text watermark. The default value is empty.
        # 
        # >Notice: 
        # 
        # This parameter is effective only when the `Type` parameter is set to `text`.
        self.content = content
        # The duration for which the watermark is displayed, in seconds (s). By default, the watermark is displayed until the end of the video.
        self.duration = duration
        # The meaning of this parameter varies depending on whether the value is an integer or a decimal:
        # 
        # - 0 (default): The pixel offset is 0. The ratio of the horizontal offset to the output video width is also 0.
        # 
        # - Integer: The offset in pixels (px). The value ranges from 1 to 4096.
        # 
        # - Decimal: The ratio of the horizontal offset to the output video width. The value ranges from (0, 1).
        self.dx = dx
        # The meaning of this parameter varies depending on whether the value is an integer or a decimal:
        # 
        # - 0 (default): The pixel offset is 0. The ratio of the vertical offset to the output video height is also 0.
        # 
        # - Integer: The offset in pixels (px). The value ranges from 1 to 4096.
        # 
        # - Decimal: The ratio of the vertical offset to the output video height. The value ranges from (0, 1).
        self.dy = dy
        # The font opacity of the text watermark. The value ranges from (0, 1]. The default value is 1, which means fully opaque.
        # 
        # >Notice: 
        # 
        # This parameter is effective only when the `Type` parameter is set to `text`.
        self.font_apha = font_apha
        # The font color of the watermark text. The format is #RRGGBB. The default value is #000000. You can also enter values such as "red" or "green".
        # 
        # >Notice: 
        # 
        # This parameter is effective only when the `Type` parameter is set to `text`.
        self.font_color = font_color
        # The font name for the text watermark. Valid values:
        # 
        # - SourceHanSans-Regular (default)
        # 
        # - SourceHanSans-Bold
        # 
        # - SourceHanSerif-Regular
        # 
        # - SourceHanSerif-Bold
        # 
        # >Notice: 
        # 
        # This parameter is effective only when the `Type` parameter is set to `text`.
        self.font_name = font_name
        # The font size for the text watermark. The default value is 16. The value must be an integer in the range (4, 120).
        # 
        # >Notice: 
        # 
        # This parameter is effective only when the `Type` parameter is set to `text`.
        self.font_size = font_size
        # The height of the watermark image. By default, this is the height of the original watermark image. The meaning of this parameter varies depending on whether the value is an integer or a decimal:
        # 
        # - Integer: The height of the watermark in pixels (px). The value ranges from 1 to 4096.
        # 
        # - Decimal: The ratio of the watermark height to the output video height. The value ranges from (0, 1).
        self.height = height
        # The reference position for adding the watermark. Valid values:
        # 
        # - topleft (default): The top-left corner.
        # 
        # - topright: The top-right corner.
        # 
        # - bottomright: The bottom-right corner.
        # 
        # - bottomleft: The bottom-left corner.
        self.refer_pos = refer_pos
        # The start time for adding the watermark, in seconds (s). By default, the watermark is added from the beginning of the video.
        self.start_time = start_time
        # The watermark type. Valid values:
        # 
        # - text (default): A text watermark.
        # 
        # - file: An image or animated image watermark.
        self.type = type
        # The OSS URL of the watermark file. Supported formats are PNG and MOV.
        # 
        # The OSS URL must follow the format `oss://<bucket>/<object>`, where `<bucket>` is the name of an OSS bucket in the same region as the current project, and `<object>` is the full path of the file, including the file name extension.
        # 
        # >Notice: 
        # 
        # This parameter is effective only when the `Type` parameter is set to `file`.
        self.uri = uri
        # The width of the watermark image. By default, this is the width of the original watermark image. The meaning of this parameter varies depending on whether the value is an integer or a decimal:
        # 
        # - Integer: The width of the watermark in pixels (px). The value ranges from 1 to 4096.
        # 
        # - Decimal: The ratio of the watermark width to the output video width. The value ranges from (0, 1).
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.border_color is not None:
            result['BorderColor'] = self.border_color

        if self.border_width is not None:
            result['BorderWidth'] = self.border_width

        if self.content is not None:
            result['Content'] = self.content

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.dx is not None:
            result['Dx'] = self.dx

        if self.dy is not None:
            result['Dy'] = self.dy

        if self.font_apha is not None:
            result['FontApha'] = self.font_apha

        if self.font_color is not None:
            result['FontColor'] = self.font_color

        if self.font_name is not None:
            result['FontName'] = self.font_name

        if self.font_size is not None:
            result['FontSize'] = self.font_size

        if self.height is not None:
            result['Height'] = self.height

        if self.refer_pos is not None:
            result['ReferPos'] = self.refer_pos

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.type is not None:
            result['Type'] = self.type

        if self.uri is not None:
            result['URI'] = self.uri

        if self.width is not None:
            result['Width'] = self.width

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BorderColor') is not None:
            self.border_color = m.get('BorderColor')

        if m.get('BorderWidth') is not None:
            self.border_width = m.get('BorderWidth')

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('Dx') is not None:
            self.dx = m.get('Dx')

        if m.get('Dy') is not None:
            self.dy = m.get('Dy')

        if m.get('FontApha') is not None:
            self.font_apha = m.get('FontApha')

        if m.get('FontColor') is not None:
            self.font_color = m.get('FontColor')

        if m.get('FontName') is not None:
            self.font_name = m.get('FontName')

        if m.get('FontSize') is not None:
            self.font_size = m.get('FontSize')

        if m.get('Height') is not None:
            self.height = m.get('Height')

        if m.get('ReferPos') is not None:
            self.refer_pos = m.get('ReferPos')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('URI') is not None:
            self.uri = m.get('URI')

        if m.get('Width') is not None:
            self.width = m.get('Width')

        return self

class TargetVideoFilterVideoDesensitization(DaraModel):
    def __init__(
        self,
        face: main_models.TargetVideoFilterVideoDesensitizationFace = None,
        license_plate: main_models.TargetVideoFilterVideoDesensitizationLicensePlate = None,
    ):
        # The facial desensitization configuration.
        # 
        # > This feature is in public preview. If you have any questions, join the DingTalk group for feedback. For the DingTalk group number, see [Contact us](https://help.aliyun.com/document_detail/84454.html).
        self.face = face
        # The license plate desensitization configuration.
        # 
        # > This feature is in public preview. If you have any questions, join the DingTalk group for feedback. For the DingTalk group number, see [Contact us](https://help.aliyun.com/document_detail/84454.html).
        self.license_plate = license_plate

    def validate(self):
        if self.face:
            self.face.validate()
        if self.license_plate:
            self.license_plate.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.face is not None:
            result['Face'] = self.face.to_map()

        if self.license_plate is not None:
            result['LicensePlate'] = self.license_plate.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Face') is not None:
            temp_model = main_models.TargetVideoFilterVideoDesensitizationFace()
            self.face = temp_model.from_map(m.get('Face'))

        if m.get('LicensePlate') is not None:
            temp_model = main_models.TargetVideoFilterVideoDesensitizationLicensePlate()
            self.license_plate = temp_model.from_map(m.get('LicensePlate'))

        return self

class TargetVideoFilterVideoDesensitizationLicensePlate(DaraModel):
    def __init__(
        self,
        confidence: float = None,
        min_size: int = None,
    ):
        # The confidence threshold for license plate recognition. This sets the lower limit for the confidence level. If the confidence level of a detected license plate is below this threshold, the license plate is not desensitized.
        # 
        # - Value range: 0.0 to 1.0.
        # 
        # - Default value: 0.0 (no confidence filtering).
        self.confidence = confidence
        # The minimum license plate size threshold. This sets the minimum size for a license plate to be desensitized. If the width or height of a detected license plate is smaller than this threshold, the license plate is not desensitized. The unit is pixels. The default value is 0, which means there is no restriction on license plate size.
        self.min_size = min_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.confidence is not None:
            result['Confidence'] = self.confidence

        if self.min_size is not None:
            result['MinSize'] = self.min_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')

        if m.get('MinSize') is not None:
            self.min_size = m.get('MinSize')

        return self

class TargetVideoFilterVideoDesensitizationFace(DaraModel):
    def __init__(
        self,
        confidence: float = None,
        min_size: int = None,
    ):
        # The confidence threshold for facial recognition. This sets the lower limit for the confidence level. If the confidence level of a detected face is below this threshold, the face is not desensitized.
        # 
        # - Value range: 0.0 to 1.0.
        # 
        # - Default value: 0.0 (no confidence filtering).
        self.confidence = confidence
        # The minimum face size threshold. This sets the minimum size for a face to be desensitized. If the width or height of a detected face is smaller than this threshold, the face is not desensitized. The unit is pixels. The default value is 0, which means there is no restriction on face size.
        self.min_size = min_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.confidence is not None:
            result['Confidence'] = self.confidence

        if self.min_size is not None:
            result['MinSize'] = self.min_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')

        if m.get('MinSize') is not None:
            self.min_size = m.get('MinSize')

        return self

class TargetVideoFilterVideoDelogos(DaraModel):
    def __init__(
        self,
        duration: float = None,
        dx: float = None,
        dy: float = None,
        height: float = None,
        refer_pos: str = None,
        start_time: float = None,
        width: float = None,
    ):
        # The duration for which the mosaic is displayed, in seconds (s). By default, the mosaic is displayed until the end of the video.
        self.duration = duration
        # The meaning of this parameter varies depending on whether the value is an integer or a decimal:
        # 
        # - 0 (default): The pixel offset is 0. The ratio of the horizontal offset to the output video width is also 0.
        # 
        # - Integer: The offset in pixels (px). The value ranges from 1 to 4096.
        # 
        # - Decimal: The ratio of the horizontal offset to the output video width. The value ranges from (0, 1).
        self.dx = dx
        # The default value is 0. The meaning of this parameter varies depending on whether the value is an integer or a decimal:
        # 
        # - 0 (default): The pixel offset is 0. The ratio of the vertical offset to the output video height is also 0.
        # 
        # - Integer: The offset in pixels (px). The value ranges from 1 to 4096.
        # 
        # - Decimal: The ratio of the vertical offset to the output video height. The value ranges from (0, 1).
        self.dy = dy
        # The height of the mosaic. The default value is the decimal 1.0, which means it fills the entire height of the output video. The meaning of this parameter varies depending on whether the value is an integer or a decimal:
        # 
        # - Integer: The height in pixels (px). The value ranges from 1 to 4096.
        # 
        # - Decimal: The ratio of the mosaic height to the output video height. The value ranges from (0, 1).
        self.height = height
        # The reference position for adding the mosaic. Valid values:
        # 
        # - topleft (default): The top-left corner.
        # 
        # - topright: The top-right corner.
        # 
        # - bottomright: The bottom-right corner.
        # 
        # - bottomleft: The bottom-left corner.
        self.refer_pos = refer_pos
        # The start time for adding the mosaic, in seconds (s). By default, the mosaic is added from the beginning of the video.
        self.start_time = start_time
        # The width of the mosaic. The default value is the decimal 1.0, which means it fills the entire width of the output video. The meaning of this parameter varies depending on whether the value is an integer or a decimal:
        # 
        # - Integer: The width in pixels (px). The value ranges from 1 to 4096.
        # 
        # - Decimal: The ratio of the mosaic width to the output video width. The value ranges from (0, 1).
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.duration is not None:
            result['Duration'] = self.duration

        if self.dx is not None:
            result['Dx'] = self.dx

        if self.dy is not None:
            result['Dy'] = self.dy

        if self.height is not None:
            result['Height'] = self.height

        if self.refer_pos is not None:
            result['ReferPos'] = self.refer_pos

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.width is not None:
            result['Width'] = self.width

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('Dx') is not None:
            self.dx = m.get('Dx')

        if m.get('Dy') is not None:
            self.dy = m.get('Dy')

        if m.get('Height') is not None:
            self.height = m.get('Height')

        if m.get('ReferPos') is not None:
            self.refer_pos = m.get('ReferPos')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Width') is not None:
            self.width = m.get('Width')

        return self

