# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_mts20140618 import models as main_models
from darabonba.model import DaraModel

class UpdateTemplateResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        template: main_models.UpdateTemplateResponseBodyTemplate = None,
    ):
        # The type of the transcoding template.
        self.request_id = request_id
        # The type of the transcoding template.
        self.template = template

    def validate(self):
        if self.template:
            self.template.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.template is not None:
            result['Template'] = self.template.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Template') is not None:
            temp_model = main_models.UpdateTemplateResponseBodyTemplate()
            self.template = temp_model.from_map(m.get('Template'))

        return self

class UpdateTemplateResponseBodyTemplate(DaraModel):
    def __init__(
        self,
        audio: main_models.UpdateTemplateResponseBodyTemplateAudio = None,
        container: main_models.UpdateTemplateResponseBodyTemplateContainer = None,
        id: str = None,
        mux_config: main_models.UpdateTemplateResponseBodyTemplateMuxConfig = None,
        name: str = None,
        state: str = None,
        trans_config: main_models.UpdateTemplateResponseBodyTemplateTransConfig = None,
        video: main_models.UpdateTemplateResponseBodyTemplateVideo = None,
    ):
        # The audio codec settings.
        self.audio = audio
        # The container format.
        self.container = container
        # The container configurations.
        self.id = id
        # The transmuxing configurations for WebP.
        self.mux_config = mux_config
        # The audio codec configurations.
        self.name = name
        # The transmuxing configurations.
        self.state = state
        # Indicates whether the audio bitrate is checked. If the bitrate of the output audio is greater than the bitrate of the input audio, the bitrate of the input audio is retained after transcoding. In this case, the specified audio bitrate does not take effect. This parameter has a lower priority than the IsCheckAudioBitrateFail parameter. Valid values:
        # 
        # *   **true**: The audio bitrate is checked.
        # 
        # *   **false**: The audio bitrate is not checked.
        # 
        # *   Default value:
        # 
        #     *   If the parameter is left empty and the codec of the output audio is different from that of the input audio, the default value is false.
        #     *   If the parameter is left empty and the codec of the output audio is the same as that of the input audio, the default value is true.
        self.trans_config = trans_config
        # The video codec configurations.
        self.video = video

    def validate(self):
        if self.audio:
            self.audio.validate()
        if self.container:
            self.container.validate()
        if self.mux_config:
            self.mux_config.validate()
        if self.trans_config:
            self.trans_config.validate()
        if self.video:
            self.video.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audio is not None:
            result['Audio'] = self.audio.to_map()

        if self.container is not None:
            result['Container'] = self.container.to_map()

        if self.id is not None:
            result['Id'] = self.id

        if self.mux_config is not None:
            result['MuxConfig'] = self.mux_config.to_map()

        if self.name is not None:
            result['Name'] = self.name

        if self.state is not None:
            result['State'] = self.state

        if self.trans_config is not None:
            result['TransConfig'] = self.trans_config.to_map()

        if self.video is not None:
            result['Video'] = self.video.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Audio') is not None:
            temp_model = main_models.UpdateTemplateResponseBodyTemplateAudio()
            self.audio = temp_model.from_map(m.get('Audio'))

        if m.get('Container') is not None:
            temp_model = main_models.UpdateTemplateResponseBodyTemplateContainer()
            self.container = temp_model.from_map(m.get('Container'))

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('MuxConfig') is not None:
            temp_model = main_models.UpdateTemplateResponseBodyTemplateMuxConfig()
            self.mux_config = temp_model.from_map(m.get('MuxConfig'))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('TransConfig') is not None:
            temp_model = main_models.UpdateTemplateResponseBodyTemplateTransConfig()
            self.trans_config = temp_model.from_map(m.get('TransConfig'))

        if m.get('Video') is not None:
            temp_model = main_models.UpdateTemplateResponseBodyTemplateVideo()
            self.video = temp_model.from_map(m.get('Video'))

        return self

class UpdateTemplateResponseBodyTemplateVideo(DaraModel):
    def __init__(
        self,
        bitrate: str = None,
        bitrate_bnd: main_models.UpdateTemplateResponseBodyTemplateVideoBitrateBnd = None,
        bufsize: str = None,
        codec: str = None,
        crf: str = None,
        crop: str = None,
        degrain: str = None,
        fps: str = None,
        gop: str = None,
        hdr_2sdr: str = None,
        height: str = None,
        long_short_mode: str = None,
        max_fps: str = None,
        maxrate: str = None,
        narrow_band: main_models.UpdateTemplateResponseBodyTemplateVideoNarrowBand = None,
        pad: str = None,
        pix_fmt: str = None,
        preset: str = None,
        profile: str = None,
        qscale: str = None,
        remove: str = None,
        reso_priority: str = None,
        scan_mode: str = None,
        width: str = None,
    ):
        # The maximum bitrate of the video. Unit: Kbit/s.
        self.bitrate = bitrate
        # The upper limit of the total bitrate. Unit: Kbit/s.
        self.bitrate_bnd = bitrate_bnd
        # The level of quality control on the video.
        self.bufsize = bufsize
        # The height of the output video.
        # 
        # *   Unit: pixel.
        # *   Default value: the height of the input video.
        self.codec = codec
        # Indicates whether the video stream is deleted. Valid values:
        # 
        # *   **true**: The video stream is deleted.
        # *   **false**: The video stream is retained.
        # *   Default value: **false**.
        self.crf = crf
        # The average bitrate of the video. Unit: Kbit/s.
        self.crop = crop
        # The average bitrate range of the video.
        self.degrain = degrain
        # The preset video algorithm. Default value: **medium**. Valid values:
        # 
        # *   **veryfast**
        # *   **fast**
        # *   **medium**
        # *   **slow**
        # *   **slower**
        self.fps = fps
        # The width of the video.
        # 
        # *   Unit: pixel.
        # *   Default value: **the width of the input video**.
        self.gop = gop
        # Indicates whether the HDR2SDR conversion feature is enabled. If this feature is enabled, high dynamic range (HDR) videos are transcoded to standard dynamic range (SDR) videos.
        self.hdr_2sdr = hdr_2sdr
        # The level of the independent denoising algorithm.
        self.height = height
        # The size of the buffer.
        # 
        # *   Unit: KB.
        # *   Default value: **6000**.
        self.long_short_mode = long_short_mode
        # The encoding profile. Valid values:
        # 
        # *   **baseline**: applicable to mobile devices.
        # *   **main**: applicable to standard-definition devices.
        # *   **high**: applicable to high-definition devices.
        # *   Default value: **high**.
        self.max_fps = max_fps
        # The maximum frame rate.
        self.maxrate = maxrate
        # The Narrowband HD settings.
        self.narrow_band = narrow_band
        # The video codec. Default value: **H.264**.
        self.pad = pad
        # The black borders added to the video.
        # 
        # *   Format: width:height:left:top.
        # *   Example: 1280:800:0:140.
        self.pix_fmt = pix_fmt
        # The scan mode. Valid values:
        # 
        # *   **interlaced**: An interlaced scan is performed.
        # *   **progressive**: A progressive scan is performed.
        self.preset = preset
        # The bitrate quality control factor.
        # 
        # *   Default value if the Codec parameter is set to H.264: **23**. Default value if the Codec parameter is set to H.265: **26**.
        # *   If this parameter is returned, the setting of the Bitrate parameter is invalid.
        self.profile = profile
        # The method used to crop the video.
        # 
        # *   **border**: automatically detects and removes borders.
        # *   Value in the width:height:left:top format: crops the video based on custom settings.**** Example: 1280:800:0:140.
        self.qscale = qscale
        # The maximum number of frames between two keyframes. Default value: **250**.
        self.remove = remove
        # The general transcoding configurations.
        self.reso_priority = reso_priority
        # The policy of resolution adjustment.
        self.scan_mode = scan_mode
        # The frame rate.
        # 
        # *   A value of 60 is returned if the frame rate of the input video exceeds 60.
        # *   Default value: the frame rate of the input video.
        self.width = width

    def validate(self):
        if self.bitrate_bnd:
            self.bitrate_bnd.validate()
        if self.narrow_band:
            self.narrow_band.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bitrate is not None:
            result['Bitrate'] = self.bitrate

        if self.bitrate_bnd is not None:
            result['BitrateBnd'] = self.bitrate_bnd.to_map()

        if self.bufsize is not None:
            result['Bufsize'] = self.bufsize

        if self.codec is not None:
            result['Codec'] = self.codec

        if self.crf is not None:
            result['Crf'] = self.crf

        if self.crop is not None:
            result['Crop'] = self.crop

        if self.degrain is not None:
            result['Degrain'] = self.degrain

        if self.fps is not None:
            result['Fps'] = self.fps

        if self.gop is not None:
            result['Gop'] = self.gop

        if self.hdr_2sdr is not None:
            result['Hdr2sdr'] = self.hdr_2sdr

        if self.height is not None:
            result['Height'] = self.height

        if self.long_short_mode is not None:
            result['LongShortMode'] = self.long_short_mode

        if self.max_fps is not None:
            result['MaxFps'] = self.max_fps

        if self.maxrate is not None:
            result['Maxrate'] = self.maxrate

        if self.narrow_band is not None:
            result['NarrowBand'] = self.narrow_band.to_map()

        if self.pad is not None:
            result['Pad'] = self.pad

        if self.pix_fmt is not None:
            result['PixFmt'] = self.pix_fmt

        if self.preset is not None:
            result['Preset'] = self.preset

        if self.profile is not None:
            result['Profile'] = self.profile

        if self.qscale is not None:
            result['Qscale'] = self.qscale

        if self.remove is not None:
            result['Remove'] = self.remove

        if self.reso_priority is not None:
            result['ResoPriority'] = self.reso_priority

        if self.scan_mode is not None:
            result['ScanMode'] = self.scan_mode

        if self.width is not None:
            result['Width'] = self.width

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bitrate') is not None:
            self.bitrate = m.get('Bitrate')

        if m.get('BitrateBnd') is not None:
            temp_model = main_models.UpdateTemplateResponseBodyTemplateVideoBitrateBnd()
            self.bitrate_bnd = temp_model.from_map(m.get('BitrateBnd'))

        if m.get('Bufsize') is not None:
            self.bufsize = m.get('Bufsize')

        if m.get('Codec') is not None:
            self.codec = m.get('Codec')

        if m.get('Crf') is not None:
            self.crf = m.get('Crf')

        if m.get('Crop') is not None:
            self.crop = m.get('Crop')

        if m.get('Degrain') is not None:
            self.degrain = m.get('Degrain')

        if m.get('Fps') is not None:
            self.fps = m.get('Fps')

        if m.get('Gop') is not None:
            self.gop = m.get('Gop')

        if m.get('Hdr2sdr') is not None:
            self.hdr_2sdr = m.get('Hdr2sdr')

        if m.get('Height') is not None:
            self.height = m.get('Height')

        if m.get('LongShortMode') is not None:
            self.long_short_mode = m.get('LongShortMode')

        if m.get('MaxFps') is not None:
            self.max_fps = m.get('MaxFps')

        if m.get('Maxrate') is not None:
            self.maxrate = m.get('Maxrate')

        if m.get('NarrowBand') is not None:
            temp_model = main_models.UpdateTemplateResponseBodyTemplateVideoNarrowBand()
            self.narrow_band = temp_model.from_map(m.get('NarrowBand'))

        if m.get('Pad') is not None:
            self.pad = m.get('Pad')

        if m.get('PixFmt') is not None:
            self.pix_fmt = m.get('PixFmt')

        if m.get('Preset') is not None:
            self.preset = m.get('Preset')

        if m.get('Profile') is not None:
            self.profile = m.get('Profile')

        if m.get('Qscale') is not None:
            self.qscale = m.get('Qscale')

        if m.get('Remove') is not None:
            self.remove = m.get('Remove')

        if m.get('ResoPriority') is not None:
            self.reso_priority = m.get('ResoPriority')

        if m.get('ScanMode') is not None:
            self.scan_mode = m.get('ScanMode')

        if m.get('Width') is not None:
            self.width = m.get('Width')

        return self

class UpdateTemplateResponseBodyTemplateVideoNarrowBand(DaraModel):
    def __init__(
        self,
        abrmax: float = None,
        max_abr_ratio: float = None,
        version: str = None,
    ):
        # The upper limit of the dynamic bitrate. If this parameter is set, the average bitrate is in the range of (0, 1000000].
        self.abrmax = abrmax
        # The maximum ratio of the upper limit of dynamic bitrate. If this parameter is set, the value of Abrmax does not exceed x times of the source video bitrate. Valid values: (0,1.0].
        self.max_abr_ratio = max_abr_ratio
        # The Narrowband HD version. Only 1.0 may be returned.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.abrmax is not None:
            result['Abrmax'] = self.abrmax

        if self.max_abr_ratio is not None:
            result['MaxAbrRatio'] = self.max_abr_ratio

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Abrmax') is not None:
            self.abrmax = m.get('Abrmax')

        if m.get('MaxAbrRatio') is not None:
            self.max_abr_ratio = m.get('MaxAbrRatio')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

class UpdateTemplateResponseBodyTemplateVideoBitrateBnd(DaraModel):
    def __init__(
        self,
        max: str = None,
        min: str = None,
    ):
        # The lower limit of the total bitrate. Unit: Kbit/s.
        self.max = max
        # The pixel format. Valid values: standard pixel formats such as yuv420p and yuvj420p.
        self.min = min

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max is not None:
            result['Max'] = self.max

        if self.min is not None:
            result['Min'] = self.min

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Max') is not None:
            self.max = m.get('Max')

        if m.get('Min') is not None:
            self.min = m.get('Min')

        return self

class UpdateTemplateResponseBodyTemplateTransConfig(DaraModel):
    def __init__(
        self,
        adj_dar_method: str = None,
        is_check_audio_bitrate: str = None,
        is_check_audio_bitrate_fail: str = None,
        is_check_reso: str = None,
        is_check_reso_fail: str = None,
        is_check_video_bitrate: str = None,
        is_check_video_bitrate_fail: str = None,
        trans_mode: str = None,
    ):
        # Indicates whether the video bitrate is checked. If this parameter is set to true and the system detects that the video bitrate of the output file is greater than that of the input file, the video bitrate of the input file is retained after transcoding. Valid values:
        # 
        # *   **true**: The video bitrate is checked.
        # *   **false**: The video bitrate is not checked.
        # *   Default value: **false**.
        self.adj_dar_method = adj_dar_method
        # The transcoding mode. Default value: **onepass**. Valid values:
        # 
        # *   **onepass**
        # *   **twopass**
        # *   **CBR**
        self.is_check_audio_bitrate = is_check_audio_bitrate
        # The status of the template. Valid values:
        # 
        # *   **Normal**: The template is normal.
        # *   **Deleted**: The template is deleted.
        self.is_check_audio_bitrate_fail = is_check_audio_bitrate_fail
        # Indicates whether the video bitrate is checked. This parameter has a higher priority than the IsCheckVideoBitrate parameter. Valid values:
        # 
        # *   **true**: The video bitrate is checked
        # *   **false**: The video bitrate is not checked.
        # *   Default value: **false**.
        self.is_check_reso = is_check_reso
        # Indicates whether the audio bitrate is checked. This parameter has a higher priority than the IsCheckAudioBitrate parameter. Valid values:
        # 
        # *   **true**: The audio bitrate is checked.
        # *   **false**: The audio bitrate is not checked.
        # *   Default value: **false**.
        self.is_check_reso_fail = is_check_reso_fail
        # Indicates whether the resolution is checked. If this parameter is set to true and the system detects that the resolution of the output file is higher than that of the input file based on the width or height, an error that indicates a transcoding failure is returned. Valid values:
        # 
        # *   **true**: The resolution is checked.
        # *   **false**: The resolution is not checked.
        # *   Default value: **false**.
        self.is_check_video_bitrate = is_check_video_bitrate
        # The method of resolution adjustment. Default value: **none**. Valid values:
        # 
        # *   rescale: The input video is rescaled.
        # *   crop: The input video is cropped.
        # *   none: No change is made.
        self.is_check_video_bitrate_fail = is_check_video_bitrate_fail
        # Indicates whether the resolution is checked. If the output resolution is higher than the input resolution based on the width or height, the input resolution is retained after transcoding. Valid values:
        # 
        # *   **true**: The resolution is checked.
        # *   **false**: The resolution is not checked.
        # *   Default value: **false**.
        self.trans_mode = trans_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.adj_dar_method is not None:
            result['AdjDarMethod'] = self.adj_dar_method

        if self.is_check_audio_bitrate is not None:
            result['IsCheckAudioBitrate'] = self.is_check_audio_bitrate

        if self.is_check_audio_bitrate_fail is not None:
            result['IsCheckAudioBitrateFail'] = self.is_check_audio_bitrate_fail

        if self.is_check_reso is not None:
            result['IsCheckReso'] = self.is_check_reso

        if self.is_check_reso_fail is not None:
            result['IsCheckResoFail'] = self.is_check_reso_fail

        if self.is_check_video_bitrate is not None:
            result['IsCheckVideoBitrate'] = self.is_check_video_bitrate

        if self.is_check_video_bitrate_fail is not None:
            result['IsCheckVideoBitrateFail'] = self.is_check_video_bitrate_fail

        if self.trans_mode is not None:
            result['TransMode'] = self.trans_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdjDarMethod') is not None:
            self.adj_dar_method = m.get('AdjDarMethod')

        if m.get('IsCheckAudioBitrate') is not None:
            self.is_check_audio_bitrate = m.get('IsCheckAudioBitrate')

        if m.get('IsCheckAudioBitrateFail') is not None:
            self.is_check_audio_bitrate_fail = m.get('IsCheckAudioBitrateFail')

        if m.get('IsCheckReso') is not None:
            self.is_check_reso = m.get('IsCheckReso')

        if m.get('IsCheckResoFail') is not None:
            self.is_check_reso_fail = m.get('IsCheckResoFail')

        if m.get('IsCheckVideoBitrate') is not None:
            self.is_check_video_bitrate = m.get('IsCheckVideoBitrate')

        if m.get('IsCheckVideoBitrateFail') is not None:
            self.is_check_video_bitrate_fail = m.get('IsCheckVideoBitrateFail')

        if m.get('TransMode') is not None:
            self.trans_mode = m.get('TransMode')

        return self

class UpdateTemplateResponseBodyTemplateMuxConfig(DaraModel):
    def __init__(
        self,
        gif: main_models.UpdateTemplateResponseBodyTemplateMuxConfigGif = None,
        segment: main_models.UpdateTemplateResponseBodyTemplateMuxConfigSegment = None,
        webp: main_models.UpdateTemplateResponseBodyTemplateMuxConfigWebp = None,
    ):
        # The duration for which the final frame is paused. Unit: milliseconds.
        self.gif = gif
        # The length of the segment. Unit: seconds.
        self.segment = segment
        # The loop count.
        self.webp = webp

    def validate(self):
        if self.gif:
            self.gif.validate()
        if self.segment:
            self.segment.validate()
        if self.webp:
            self.webp.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gif is not None:
            result['Gif'] = self.gif.to_map()

        if self.segment is not None:
            result['Segment'] = self.segment.to_map()

        if self.webp is not None:
            result['Webp'] = self.webp.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Gif') is not None:
            temp_model = main_models.UpdateTemplateResponseBodyTemplateMuxConfigGif()
            self.gif = temp_model.from_map(m.get('Gif'))

        if m.get('Segment') is not None:
            temp_model = main_models.UpdateTemplateResponseBodyTemplateMuxConfigSegment()
            self.segment = temp_model.from_map(m.get('Segment'))

        if m.get('Webp') is not None:
            temp_model = main_models.UpdateTemplateResponseBodyTemplateMuxConfigWebp()
            self.webp = temp_model.from_map(m.get('Webp'))

        return self

class UpdateTemplateResponseBodyTemplateMuxConfigWebp(DaraModel):
    def __init__(
        self,
        loop: str = None,
    ):
        # The transmuxing configurations for GIF.
        self.loop = loop

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.loop is not None:
            result['Loop'] = self.loop

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Loop') is not None:
            self.loop = m.get('Loop')

        return self

class UpdateTemplateResponseBodyTemplateMuxConfigSegment(DaraModel):
    def __init__(
        self,
        duration: str = None,
    ):
        # The name of the template.
        self.duration = duration

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.duration is not None:
            result['Duration'] = self.duration

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        return self

class UpdateTemplateResponseBodyTemplateMuxConfigGif(DaraModel):
    def __init__(
        self,
        dither_mode: str = None,
        final_delay: str = None,
        is_custom_palette: str = None,
        loop: str = None,
    ):
        # The loop count.
        self.dither_mode = dither_mode
        # The color dithering algorithm of the palette. Valid values: sierra and bayer.
        self.final_delay = final_delay
        # The segment configurations.
        self.is_custom_palette = is_custom_palette
        # Indicates whether the custom palette is used.
        self.loop = loop

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dither_mode is not None:
            result['DitherMode'] = self.dither_mode

        if self.final_delay is not None:
            result['FinalDelay'] = self.final_delay

        if self.is_custom_palette is not None:
            result['IsCustomPalette'] = self.is_custom_palette

        if self.loop is not None:
            result['Loop'] = self.loop

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DitherMode') is not None:
            self.dither_mode = m.get('DitherMode')

        if m.get('FinalDelay') is not None:
            self.final_delay = m.get('FinalDelay')

        if m.get('IsCustomPalette') is not None:
            self.is_custom_palette = m.get('IsCustomPalette')

        if m.get('Loop') is not None:
            self.loop = m.get('Loop')

        return self

class UpdateTemplateResponseBodyTemplateContainer(DaraModel):
    def __init__(
        self,
        format: str = None,
    ):
        # The container format.
        self.format = format

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.format is not None:
            result['Format'] = self.format

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Format') is not None:
            self.format = m.get('Format')

        return self

class UpdateTemplateResponseBodyTemplateAudio(DaraModel):
    def __init__(
        self,
        bitrate: str = None,
        channels: str = None,
        codec: str = None,
        profile: str = None,
        qscale: str = None,
        remove: str = None,
        samplerate: str = None,
        volume: main_models.UpdateTemplateResponseBodyTemplateAudioVolume = None,
    ):
        # The ID of the transcoding template.
        self.bitrate = bitrate
        # The audio bitrate of the output file.
        # 
        # *   Valid values: 8 to 1000.****
        # *   Unit: Kbit/s.
        # *   Default value: **128**.
        self.channels = channels
        # The sampling rate.
        # 
        # *   Unit: Hz.
        # *   Default value: **44100**.
        self.codec = codec
        # Indicates whether the audio stream is deleted.
        # 
        # *   **true**: The audio stream is deleted.
        # *   **false**: The audio stream is retained.
        # *   Default value: **false**.
        self.profile = profile
        # The number of sound channels. Default value: **2**.
        self.qscale = qscale
        # The audio codec format. Default value: **aac**. Valid values:
        # 
        # *   **aac**
        # *   **mp3**
        # *   **vorbis**
        # *   **flac**
        self.remove = remove
        # The level of the independent denoising algorithm.
        self.samplerate = samplerate
        # The volume control configurations.
        self.volume = volume

    def validate(self):
        if self.volume:
            self.volume.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bitrate is not None:
            result['Bitrate'] = self.bitrate

        if self.channels is not None:
            result['Channels'] = self.channels

        if self.codec is not None:
            result['Codec'] = self.codec

        if self.profile is not None:
            result['Profile'] = self.profile

        if self.qscale is not None:
            result['Qscale'] = self.qscale

        if self.remove is not None:
            result['Remove'] = self.remove

        if self.samplerate is not None:
            result['Samplerate'] = self.samplerate

        if self.volume is not None:
            result['Volume'] = self.volume.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bitrate') is not None:
            self.bitrate = m.get('Bitrate')

        if m.get('Channels') is not None:
            self.channels = m.get('Channels')

        if m.get('Codec') is not None:
            self.codec = m.get('Codec')

        if m.get('Profile') is not None:
            self.profile = m.get('Profile')

        if m.get('Qscale') is not None:
            self.qscale = m.get('Qscale')

        if m.get('Remove') is not None:
            self.remove = m.get('Remove')

        if m.get('Samplerate') is not None:
            self.samplerate = m.get('Samplerate')

        if m.get('Volume') is not None:
            temp_model = main_models.UpdateTemplateResponseBodyTemplateAudioVolume()
            self.volume = temp_model.from_map(m.get('Volume'))

        return self

class UpdateTemplateResponseBodyTemplateAudioVolume(DaraModel):
    def __init__(
        self,
        integrated_loudness_target: str = None,
        level: str = None,
        loudness_range_target: str = None,
        method: str = None,
        peak_level: str = None,
        true_peak: str = None,
    ):
        # The expected volume.
        # 
        # *   This parameter takes effect only if the value of Method is dynamic.
        # *   Unit: decibel.
        # *   Valid values: [-70,-5].
        # *   Default value: -6.
        self.integrated_loudness_target = integrated_loudness_target
        # The increased volume relative to the volume of the input audio.
        # 
        # *   This parameter takes effect only if the value of Method is linear.
        # *   Unit: decibel.
        # *   Valid values: less than or equal to 20.
        # *   Default value: -20.
        self.level = level
        # The range of the volume relative to the expected volume.
        # 
        # *   This parameter takes effect only if the value of Method is dynamic.
        # *   Unit: decibel.
        # *   Valid values: [1,20].
        # *   Default value: 8.
        self.loudness_range_target = loudness_range_target
        # The volume adjustment method. Valid values:
        # 
        # *   **auto**
        # *   **dynamic**
        # *   **linear**
        self.method = method
        # The volume adjustment coefficient.
        # 
        # This parameter takes effect only if the value of Method is adaptive.
        # 
        # Valid values: [0,1].
        # 
        # Default value: 0.9.
        self.peak_level = peak_level
        # The peak volume.
        # 
        # *   This parameter takes effect only if the value of Method is dynamic.
        # *   Unit: decibel.
        # *   Valid values: [-9,0].
        # *   Default value: -1.
        self.true_peak = true_peak

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.integrated_loudness_target is not None:
            result['IntegratedLoudnessTarget'] = self.integrated_loudness_target

        if self.level is not None:
            result['Level'] = self.level

        if self.loudness_range_target is not None:
            result['LoudnessRangeTarget'] = self.loudness_range_target

        if self.method is not None:
            result['Method'] = self.method

        if self.peak_level is not None:
            result['PeakLevel'] = self.peak_level

        if self.true_peak is not None:
            result['TruePeak'] = self.true_peak

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IntegratedLoudnessTarget') is not None:
            self.integrated_loudness_target = m.get('IntegratedLoudnessTarget')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('LoudnessRangeTarget') is not None:
            self.loudness_range_target = m.get('LoudnessRangeTarget')

        if m.get('Method') is not None:
            self.method = m.get('Method')

        if m.get('PeakLevel') is not None:
            self.peak_level = m.get('PeakLevel')

        if m.get('TruePeak') is not None:
            self.true_peak = m.get('TruePeak')

        return self

