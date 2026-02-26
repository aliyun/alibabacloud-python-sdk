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
        # *   true: disables video stream generation. No video stream is included in the output file.
        # *   false: does not disable video stream generation. This is the default value.
        self.disable_video = disable_video
        # The video processing parameters. This parameter is invalid if **TranscodeVideo** is left empty or **TranscodeVideo.Codec** is set to copy.
        # 
        # > This parameter is not available to the GenerateVideoPlaylist operation.
        self.filter_video = filter_video
        # The index numbers of video streams. If you do not specify this parameter, the first video stream (the one with the smallest index number) is processed. If the array contains an element greater than 100, all video streams are processed.
        # 
        # *   For example, you can set the parameter to `[0,1]` to process video streams with index numbers 0 and 1, `[1]` to process only the video stream with the index number 1, and `[101]` to process all video streams.
        # 
        # > If you specify an index number but no video stream with the index number is found, the index number is ignored.
        self.stream = stream
        # The video transcoding parameters. If you do not specify this parameter, no video streams are included in the output file.
        # 
        # > We recommend that you do not use this parameter to disable video stream generation.
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
        # Specifies whether to enable adaptation to resolution based on long and short sides. Valid values:
        # 
        # *   true: The format of the **Resolution** parameter is `LongSide×ShortSide`. This is the default value.
        # *   false: The format of the **Resolution** parameter is `Width×Height`.
        self.adaptive_resolution_direction = adaptive_resolution_direction
        # The number of consecutive B frames. Default value: 3.
        self.bframes = bframes
        # The bitrate of the video stream. Unit: bit/s.
        # 
        # > This parameter and the **CRF** parameter are mutually exclusive. If you leave both the parameters empty, the **CRF** parameter with a value of 23 applies.
        self.bitrate = bitrate
        # The video bitrate option. Valid values:
        # 
        # *   fixed: always uses the target bitrate.
        # *   adaptive: uses the source bitrate when the source bitrate is less than the target bitrate.
        # *   fall: returns a failure when the source bitrate is less than the target bitrate.
        # 
        # Default value:
        # 
        # *   fixed for the CreateMediaConvert operation.
        # *   adaptive for the GenerateVideoPlaylist operation.
        # 
        # > This parameter must be used together with the **Bitrate** parameter.
        self.bitrate_option = bitrate_option
        # The size of the buffer for decoding when the dynamic bitrate is used. Unit: bit/s.
        # 
        # > This parameter must be used together with the **CRF** parameter.
        self.buffer_size = buffer_size
        # The constant rate factor (CRF) of the video. The value of this parameter falls within the [0,51] range. A greater indicates lower quality. We recommend that you specify a value within the [18,38] range. This parameter and the **Bitrate** parameter are mutually exclusive.
        self.crf = crf
        # The video coding format. Valid values:
        # 
        # *   copy, h264, h265, and vp9 for the CreateMediaConvert operation. The default value is copy.
        # 
        #     **
        # 
        #     **Warning **When you set the parameter to copy, the video stream is directly copied into the output file and all other parameters in TranscodeVideo do not take effect. The copy value is commonly used in container format conversion scenarios. You cannot use this value in video merging scenarios.
        # 
        # *   h264 and h265 for the GenerateVideoPlaylist operation. The default value is h264.
        self.codec = codec
        # The target frame rate. By default, the target frame rate is the same as the source frame rate.
        self.frame_rate = frame_rate
        # The frame rate option. Valid values:
        # 
        # *   fixed: always uses the target frame rate.
        # *   adaptive: uses the source frame rate when the source frame rate is less than the target frame rate.
        # *   fall: returns a failure if the source frame rate is less than the target frame rate.
        # 
        # Default value:
        # 
        # *   fixed for the CreateMediaConvert operation.
        # *   adaptive for the GenerateVideoPlaylist operation.
        # 
        # > This parameter must be used together with the **FrameRate** parameter.
        self.frame_rate_option = frame_rate_option
        # The keyframe interval. Default value: 150.
        # 
        # > This parameter is not available to the GenerateVideoPlaylist operation.
        self.gopsize = gopsize
        # The maximum bitrate when the dynamic bitrate is used. If you specify this parameter, you must also specify the BufferSize parameter.
        # 
        # > This parameter must be used together with the **CRF** parameter.
        self.max_bitrate = max_bitrate
        # The pixel format. By default, the pixel format matches that of the source video. Valid values:
        # 
        # *   yuv420p
        # *   yuv422p
        # *   yuv444p
        # *   yuv420p10le
        # *   yuv422p10le
        # *   yuv444p10le
        # *   yuva420p
        # 
        # > You can set the parameter to yuva420p only when you call the CreateMediaConvert operation and set the **Codec** parameter to vp9.
        self.pixel_format = pixel_format
        # The number of reference frames. Default value: 2.
        self.refs = refs
        # The target resolution in the `WidthxHeight` format. By default, the target resolution is the same as the source resolution. You can specify both width and height, or only one of them. You can use this parameter together with the **AdaptiveResolutionDirection** parameter to set both the long side and short side or one of them. The value of each side falls within the range of (0,4096].
        # 
        # *   Example 1: If **AdaptiveResolutionDirection** is set to false, `1280x720` specifies a width of 1280 pixels and a height of 720 pixels, `1280x` specifies a width of 1280 pixels and the same height as the source video, and `x720` specifies a height of 720 pixels and the same width as the source video.
        # *   Example 2: If **AdaptiveResolutionDirection** is set to true, `1280x720` specifies a long side of 1280 pixels and a short side of 720 pixels, `1280x` specifies a long side of 1280 pixels and the same short side as the source video, and `x720` specifies a short side of 720 pixels and the same long side as the source video.
        # 
        # > If the source video contains rotation information, the width, height, long side, and short side depend on the frame after rotation (the playback resolution).
        self.resolution = resolution
        # The resolution option. Valid values:
        # 
        # *   fixed: always uses the target video resolution.
        # *   adaptive: uses the source video resolution when the source video resolution is less than the target video resolution.
        # *   fall: returns a failure when the source video resolution is less than the target video resolution.
        # 
        # Default value:
        # 
        # *   fixed for the CreateMediaConvert operation.
        # *   adaptive for the GenerateVideoPlaylist operation.
        # 
        # > This parameter must be used together with the **Resolution** parameter.
        self.resolution_option = resolution_option
        # The degrees to rotate the video clockwise. Valid values:
        # 
        # *   0 (default)
        # *   90
        # *   180
        # *   270
        self.rotation = rotation
        # The resizing mode. Valid values:
        # 
        # *   stretch: forcibly stretches the video based on the specified width and height or long side and short side to fill any remaining space. This is the default value.
        # *   crop: proportionally resizes the video to the minimum resolution outside the rectangular shape based on the specified width and height or long side and short side, and crops the parts beyond the rectangular shape from the center.
        # *   fill: proportionally resizes the video to the maximum resolution within the rectangular shape based on the specified width and height or long side and short side, and fills empty space with black from the center.
        # *   fit: proportionally resizes the video to the maximum resolution that fits within the specified width and height or long side and short side.
        # 
        # > This parameter must be used together with the **Resolution** parameter.
        self.scale_type = scale_type
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
        # The configurations for blurring a rectangular area of the video. This parameter is used to remove logos from videos, such as TV channel logos.
        self.delogos = delogos
        # The video anonymization settings.
        # 
        # > 
        # 
        # *   This parameter only applies to the CreateMediaConvertTask operation.
        self.desensitization = desensitization
        # The video playback speed. Valid values: [0.5,1.0]. Default value: 1.0.
        # 
        # > 
        # 
        # *   This parameter specifies the ratio of the playback speed of the output media file to the default playback speed of the source media file. It does not indicate transcoding acceleration.
        # 
        # > 
        # 
        # *   This parameter only applies to the CreateMediaConvertTask operation.
        self.speed = speed
        # The video watermarks.
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
        # The color of the text watermark border. You can specify a color name, such as "red" or "green", or an RGB color code. The default color is #000000.
        # 
        # > This parameter takes effect only when the Type parameter is set to text.
        self.border_color = border_color
        # The width of the text watermark border. Unit: pixels. The value must be an integer within the [0,4096] range. Default value: 0.
        # 
        # > This parameter takes effect only when the Type parameter is set to text.
        self.border_width = border_width
        # The content of the text watermark. By default, this parameter is left empty.
        # 
        # > This parameter takes effect only when the Type parameter is set to text.
        self.content = content
        # The duration of watermarking (in seconds). By default, the watermark lasts until the video ends.
        self.duration = duration
        # The value of the parameter can be an integer or a decimal.
        # 
        # *   0: indicates that both the offset in pixels and the ratio of the horizontal offset relative to the height of the target resolution are 0. This is the default value.
        # *   An integer: the offset in pixels. Valid values: [1,4096].
        # *   A decimal: the ratio of the horizontal offset relative to the height of the target resolution. Valid values: (0,1).
        self.dx = dx
        # The value of the parameter can be an integer or a decimal.
        # 
        # *   0: indicates that both the offset in pixels and the ratio of the vertical offset relative to the height of the target resolution are 0. This is the default value.
        # *   An integer: the offset in pixels. Valid values: [1,4096].
        # *   A decimal: the ratio of the vertical offset relative to the height of the target resolution. Valid values: (0,1).
        self.dy = dy
        # The font transparency of the text watermark. Valid values: (0,1]. Default value: 1, which specifies that the text watermark is fully opaque.
        # 
        # > This parameter takes effect only when the Type parameter is set to text.
        self.font_apha = font_apha
        # The color of the text watermark. You can specify a color name, such as "red" or "green", or an RGB color code. The default color is #000000.
        # 
        # > This parameter takes effect only when the Type parameter is set to text.
        self.font_color = font_color
        # The font of the text watermark. Valid values:
        # 
        # *   SourceHanSans-Regular (default)
        # *   SourceHanSans-Bold
        # *   SourceHanSerif-Regular
        # *   SourceHanSerif-Bold
        # 
        # > This parameter takes effect only when the Type parameter is set to text.
        self.font_name = font_name
        # The size of the text watermark. Default value: 16. The value must be an integer within the (4,120) range.
        # 
        # > This parameter takes effect only when the Type parameter is set to text.
        self.font_size = font_size
        # The height of the image watermark. By default, the height is the same as the height of the original watermark file. The value of the parameter can be an integer or a decimal.
        # 
        # *   An integer: the number of pixels excluding the height of the logo. Valid values: [1,4096].
        # *   A decimal: the ratio relative to the height of the target resolution. Valid values: (0,1).
        self.height = height
        # The reference position for adding the watermark. Valid values:
        # 
        # *   topleft: the upper-left corner. This is the default value.
        # *   topright: the upper-right corner.
        # *   bottomright: the lower-right corner.
        # *   bottomleft: the lower-left corner.
        self.refer_pos = refer_pos
        # The start time of watermarking (in seconds). By default, the watermark begins at the start time of the video.
        self.start_time = start_time
        # The watermark type. Valid values:
        # 
        # *   text: a text watermark. This is the default value.
        # *   file: a still or animated image watermark.
        self.type = type
        # The Object Storage Service (OSS) URI of the watermark file. The watermark file can be a PNG or MOV file.
        # 
        # The URI is in the `oss://<bucket>/<object>` format, where `<bucket>` is the name of the bucket in the same region as the current project and `<object>` is the path of the object with the extension included.
        # 
        # > This parameter takes effect only when the Type parameter is set to file.
        self.uri = uri
        # The width of the image watermark. By default, the width is the same as the width of the original watermark file. The value of the parameter can be an integer or a decimal.
        # 
        # *   An integer: the number of pixels excluding the width of the logo. Valid values: [1,4096].
        # *   A decimal: the ratio relative to the width of the target resolution. Valid values: (0,1).
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
        # The settings for face anonymization.
        self.face = face
        # The settings for license plate anonymization.
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
        # The minimum confidence threshold. Valid values: 0 to 1. Default value: 0.
        self.confidence = confidence
        # The minimum threshold for license plate size. This parameter does not take effect if the width or height of the bounding box of a license plate falls below the specified minimum threshold. Default value: 0.
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
        # The minimum confidence threshold. Valid values: 0 to 1. Default value: 0.
        self.confidence = confidence
        # This parameter does not take effect if the width or height of the bounding box of a face falls below the specified minimum threshold. Default value: 0.
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
        # The duration of the blur in seconds. By default, the blur lasts until the end of the video.
        self.duration = duration
        # The value of the parameter can be an integer or a decimal.
        # 
        # *   0: indicates that both the offset in pixels and the ratio of the horizontal offset relative to the height of the target resolution are 0. This is the default value.
        # *   An integer: the offset in pixels. Valid values: [1,4096].
        # *   A decimal: the ratio of the horizontal offset relative to the height of the target resolution. Valid values: (0,1).
        self.dx = dx
        # Default value: 0. The value of the parameter can be an integer or a decimal.
        # 
        # *   0: indicates that both the offset in pixels and the ratio of the vertical offset relative to the height of the target resolution are 0. This is the default value.
        # *   An integer: the offset in pixels. Valid values: [1,4096].
        # *   A decimal: the ratio of the vertical offset relative to the height of the target resolution. Valid values: (0,1).
        self.dy = dy
        # The height of the blur. The default value is 1.0, which specifies that the blur is as high as the video. The value can be a decimal or an integer.
        # 
        # *   An integer: the number of pixels. Valid values: [1,4096].
        # *   A decimal: the ratio relative to the height of the target resolution. Valid values: (0,1).
        self.height = height
        # The reference position of the blur. Valid values:
        # 
        # *   topleft: the upper-left corner. This is the default value.
        # *   topright: the upper-right corner.
        # *   bottomright: the lower-right corner.
        # *   bottomleft: the lower-left corner.
        self.refer_pos = refer_pos
        # The start time of blurring (in seconds). By default, the blur begins at the start time of the video.
        self.start_time = start_time
        # The width of the blur. The default value is 1.0, which specifies that the blur is as wide as the video. The value can be a decimal or an integer.
        # 
        # *   An integer: the number of pixels. Valid values: [1,4096].
        # *   A decimal: the ratio relative to the width of the target resolution. Valid values: (0,1).
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

