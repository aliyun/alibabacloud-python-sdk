# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Any

from darabonba.model import DaraModel

class MediaConvertVideo(DaraModel):
    def __init__(
        self,
        bitrate: int = None,
        bufsize: int = None,
        codec: str = None,
        crf: Any = None,
        crop: str = None,
        fps: Any = None,
        gop: Any = None,
        height: int = None,
        long_short_mode: bool = None,
        max_fps: Any = None,
        maxrate: int = None,
        pad: str = None,
        profile: str = None,
        qscale: int = None,
        remove: bool = None,
        scan_mode: str = None,
        width: int = None,
    ):
        # The average bitrate of the output. If you use the CRB, ABR, or VBR bitrate control mode, you must specify Bitrate, and you must set TransMode to a valid value.
        # 
        # *   Unit: Kbps.
        # *   Valid values: -1 and [10,50000]. A value of -1 indicates that the original bitrate of the input is used.
        # 
        # Best practices:
        # 
        # *   CBR: Set TransMode to CBR and Bitrate, Maxrate, and Bufsize to the same value.
        # *   ABR: Set TransMode to onepass and specify Bitrate. You can also specify Maxrate and Bufsize to control the bitrate range.
        # *   VBR: Set TransMode to twopass and specify Maxrate/BitrateBnd and Bufsize.
        self.bitrate = bitrate
        # The buffer size. It controls bitrate fluctuations. A larger value allows for more bitrate variation and potentially higher video quality.
        # 
        # *   Unit: Kbps.
        # *   Valid values: [1000,128000].
        # *   Default value: 6000.
        self.bufsize = bufsize
        # The video codec.
        # 
        # *   Valid values: H.264, H.265, AV1, GIF, and WEBP.
        # *   Default value: H.264.
        self.codec = codec
        # The quality control factor. To use the CRF mode, you must specify Crf and set TransMode to fixCRF. A larger value means lower quality and a higher compression ratio.
        # 
        # *   Valid values: [20,51].
        # *   If Codec is set to H.264, the default value is 23. If Codec is set to H.265, the default value is 26. If Codec is set to AV1, the default value is 32.
        # 
        # Best Practice:
        # 
        # *   A value of 0 specifies lossless quality. A value of 51 specifies the worst quality. A recommended range is [23, 29]. You can adjust the value based on the complexity of the image. If you increase the value by six, the bitrate is reduced by half. Under the same definition, you can set the value for an animated cartoon higher than that for a shot video.
        # *   CRF targets perceptual quality, not a fixed bitrate. Use it with Maxrate and Bufsize to control bitrate fluctuations.
        self.crf = crf
        # Crops the video frame. You can set automatic black border removal or custom cropping.
        # 
        # *   Specify this parameter if the input resolution is greater than the output resolution. Do not specify AdjDarMethod if this parameter is specified.
        # 
        # *   To automatically remove black borders, set this parameter to border.
        # 
        # *   To use custom cropping, set the parameter in the format of {width}:{height}:{left}:{top}.
        # 
        #     *   width: the width of the output video.
        #     *   height: the height of the output video.
        #     *   left: the distance between the left border of the output and that of the original frame.
        #     *   top: the distance between the top border of the output and that of the original frame.
        # 
        # Example: 1920:800:0:140.
        self.crop = crop
        # The frame rate of the video stream.
        # 
        # *   Unit: frames per second (FPS).
        # *   Valid values: (0,60].
        # *   Default value: the frame rate of the input file. If the original frame rate exceeds 60 FPS, 60 is used.
        # *   Recommended values: 24, 25, and 30.
        self.fps = fps
        # The keyframe interval.
        # 
        # *   Set by time: The time interval, in seconds. Valid values: [1,100000].
        # *   Set by frame count: The number of frames. Valid values: [1,100000].
        # *   Default value: 10s.
        # 
        # Best practice: Set this parameter to 2-7s to improve the Time-to-First-Frame and seeking performance.
        self.gop = gop
        # The height or short edge of the output. If LongShortMode is set to false or left empty, this parameter specifies the height of the output. If LongShortMode is set to true, this parameter specifies the short edge of the output.
        # 
        # *   Unit: pixel.
        # 
        # *   Valid values: [128,4096]. The value must be an even number.
        # 
        # *   Default value:
        # 
        #     *   If neither Width nor Height is specified, the dimension of the input is used.
        #     *   If only Width is specified, Height is auto-scaled.
        self.height = height
        # Specifies whether to enable orientation-adaptive scaling. This parameter takes effect if at least one of the Width and Height parameters is specified. Valid values:
        # 
        # *   true
        # *   false
        # *   Default value: false.
        # 
        # Best practice: Enable this feature when your inputs include both horizontal and vertical videos. This prevents videos from stretching.
        self.long_short_mode = long_short_mode
        # The maximum frame rate.
        self.max_fps = max_fps
        # The maximum bitrate of the output.
        # 
        # *   Unit: Kbps.
        # *   Valid values: [10,50000].
        self.maxrate = maxrate
        # The black borders added to the video.
        # 
        # *   Specify this parameter if the input resolution is smaller than the output resolution. If you specify this parameter, do not specify IsCheckReso, IsCheckResoFail, or AdjDarMethod.
        # 
        # *   Format: {width}:{height}:{left}:{top}.
        # 
        #     *   width: the width of the output video.
        #     *   height: the height of the output video.
        #     *   left: the distance between the left border of the output and that of the original frame.
        #     *   top: the distance between the top border of the output and that of the original frame.
        # 
        # Example: 1920:1080:0:140.
        self.pad = pad
        # The codec profile.
        # 
        # *   This parameter takes effect only if Codec is set to H.264.
        # *   Valid values: baseline, main, and high.
        # *   Default value: high.
        # 
        # Best practice: For multi-bitrate streaming, use baseline for the lowest quality rendition to ensure maximum compatibility with older devices. Use main or high for other renditions.
        self.profile = profile
        # The video quality scale. This parameter applies to VBR mode. A higher value means lower video quality and a higher compression ratio.
        # 
        # *   This parameter takes effect only if Codec is set to H.264.
        # *   Valid values: [0,51].
        self.qscale = qscale
        # Specifies whether to delete the video stream. Valid values:
        # 
        # *   true: deletes the video stream. All video-related parameters are invalid.
        # *   false: retains the video stream.
        # *   Default value: false.
        self.remove = remove
        # The scan mode. Valid values:
        # 
        # *   If you leave this parameter empty, the output follows the source\\"s original scan mode.
        # *   auto: automatic deinterlacing
        # *   progressive
        # *   interlaced
        # *   By default, this parameter is left empty.
        # 
        # Best practice: The interlaced scan mode saves data traffic than the progressive scan mode but provides poor image quality. Therefore, the latter is commonly used in mainstream video production.
        # 
        # *   If you set ScanMode to progressive or interlaced, but this scan mode does not match that of the input, the video fails to be transcoded.
        # *   To improve compatibility, leave this parameter empty or set it to auto.
        self.scan_mode = scan_mode
        # The width or long edge of the output. If LongShortMode is set to false or left empty, this parameter specifies the width of the output. If LongShortMode is set to true, this parameter specifies the long edge of the output.
        # 
        # *   Unit: pixel.
        # 
        # *   Valid values: [128,4096]. The value must be an even number.
        # 
        # *   Default value:
        # 
        #     *   If neither Width nor Height is specified, the dimension of the input is used.
        #     *   If only Height is specified, Width is auto-scaled.
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bitrate is not None:
            result['Bitrate'] = self.bitrate

        if self.bufsize is not None:
            result['Bufsize'] = self.bufsize

        if self.codec is not None:
            result['Codec'] = self.codec

        if self.crf is not None:
            result['Crf'] = self.crf

        if self.crop is not None:
            result['Crop'] = self.crop

        if self.fps is not None:
            result['Fps'] = self.fps

        if self.gop is not None:
            result['Gop'] = self.gop

        if self.height is not None:
            result['Height'] = self.height

        if self.long_short_mode is not None:
            result['LongShortMode'] = self.long_short_mode

        if self.max_fps is not None:
            result['MaxFps'] = self.max_fps

        if self.maxrate is not None:
            result['Maxrate'] = self.maxrate

        if self.pad is not None:
            result['Pad'] = self.pad

        if self.profile is not None:
            result['Profile'] = self.profile

        if self.qscale is not None:
            result['Qscale'] = self.qscale

        if self.remove is not None:
            result['Remove'] = self.remove

        if self.scan_mode is not None:
            result['ScanMode'] = self.scan_mode

        if self.width is not None:
            result['Width'] = self.width

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bitrate') is not None:
            self.bitrate = m.get('Bitrate')

        if m.get('Bufsize') is not None:
            self.bufsize = m.get('Bufsize')

        if m.get('Codec') is not None:
            self.codec = m.get('Codec')

        if m.get('Crf') is not None:
            self.crf = m.get('Crf')

        if m.get('Crop') is not None:
            self.crop = m.get('Crop')

        if m.get('Fps') is not None:
            self.fps = m.get('Fps')

        if m.get('Gop') is not None:
            self.gop = m.get('Gop')

        if m.get('Height') is not None:
            self.height = m.get('Height')

        if m.get('LongShortMode') is not None:
            self.long_short_mode = m.get('LongShortMode')

        if m.get('MaxFps') is not None:
            self.max_fps = m.get('MaxFps')

        if m.get('Maxrate') is not None:
            self.maxrate = m.get('Maxrate')

        if m.get('Pad') is not None:
            self.pad = m.get('Pad')

        if m.get('Profile') is not None:
            self.profile = m.get('Profile')

        if m.get('Qscale') is not None:
            self.qscale = m.get('Qscale')

        if m.get('Remove') is not None:
            self.remove = m.get('Remove')

        if m.get('ScanMode') is not None:
            self.scan_mode = m.get('ScanMode')

        if m.get('Width') is not None:
            self.width = m.get('Width')

        return self

