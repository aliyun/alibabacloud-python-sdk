# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mts20140618 import models as main_models
from darabonba.model import DaraModel

class QueryTemplateListResponseBody(DaraModel):
    def __init__(
        self,
        non_exist_tids: main_models.QueryTemplateListResponseBodyNonExistTids = None,
        request_id: str = None,
        template_list: main_models.QueryTemplateListResponseBodyTemplateList = None,
    ):
        self.non_exist_tids = non_exist_tids
        # The ID of the request.
        self.request_id = request_id
        self.template_list = template_list

    def validate(self):
        if self.non_exist_tids:
            self.non_exist_tids.validate()
        if self.template_list:
            self.template_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.non_exist_tids is not None:
            result['NonExistTids'] = self.non_exist_tids.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.template_list is not None:
            result['TemplateList'] = self.template_list.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NonExistTids') is not None:
            temp_model = main_models.QueryTemplateListResponseBodyNonExistTids()
            self.non_exist_tids = temp_model.from_map(m.get('NonExistTids'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TemplateList') is not None:
            temp_model = main_models.QueryTemplateListResponseBodyTemplateList()
            self.template_list = temp_model.from_map(m.get('TemplateList'))

        return self

class QueryTemplateListResponseBodyTemplateList(DaraModel):
    def __init__(
        self,
        template: List[main_models.QueryTemplateListResponseBodyTemplateListTemplate] = None,
    ):
        self.template = template

    def validate(self):
        if self.template:
            for v1 in self.template:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Template'] = []
        if self.template is not None:
            for k1 in self.template:
                result['Template'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.template = []
        if m.get('Template') is not None:
            for k1 in m.get('Template'):
                temp_model = main_models.QueryTemplateListResponseBodyTemplateListTemplate()
                self.template.append(temp_model.from_map(k1))

        return self

class QueryTemplateListResponseBodyTemplateListTemplate(DaraModel):
    def __init__(
        self,
        audio: main_models.QueryTemplateListResponseBodyTemplateListTemplateAudio = None,
        container: main_models.QueryTemplateListResponseBodyTemplateListTemplateContainer = None,
        creation_time: str = None,
        id: str = None,
        mux_config: main_models.QueryTemplateListResponseBodyTemplateListTemplateMuxConfig = None,
        name: str = None,
        state: str = None,
        trans_config: main_models.QueryTemplateListResponseBodyTemplateListTemplateTransConfig = None,
        video: main_models.QueryTemplateListResponseBodyTemplateListTemplateVideo = None,
    ):
        self.audio = audio
        self.container = container
        self.creation_time = creation_time
        self.id = id
        self.mux_config = mux_config
        self.name = name
        self.state = state
        self.trans_config = trans_config
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

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

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
            temp_model = main_models.QueryTemplateListResponseBodyTemplateListTemplateAudio()
            self.audio = temp_model.from_map(m.get('Audio'))

        if m.get('Container') is not None:
            temp_model = main_models.QueryTemplateListResponseBodyTemplateListTemplateContainer()
            self.container = temp_model.from_map(m.get('Container'))

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('MuxConfig') is not None:
            temp_model = main_models.QueryTemplateListResponseBodyTemplateListTemplateMuxConfig()
            self.mux_config = temp_model.from_map(m.get('MuxConfig'))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('TransConfig') is not None:
            temp_model = main_models.QueryTemplateListResponseBodyTemplateListTemplateTransConfig()
            self.trans_config = temp_model.from_map(m.get('TransConfig'))

        if m.get('Video') is not None:
            temp_model = main_models.QueryTemplateListResponseBodyTemplateListTemplateVideo()
            self.video = temp_model.from_map(m.get('Video'))

        return self

class QueryTemplateListResponseBodyTemplateListTemplateVideo(DaraModel):
    def __init__(
        self,
        bitrate: str = None,
        bitrate_bnd: main_models.QueryTemplateListResponseBodyTemplateListTemplateVideoBitrateBnd = None,
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
        narrow_band: main_models.QueryTemplateListResponseBodyTemplateListTemplateVideoNarrowBand = None,
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
        self.bitrate = bitrate
        self.bitrate_bnd = bitrate_bnd
        self.bufsize = bufsize
        self.codec = codec
        self.crf = crf
        self.crop = crop
        self.degrain = degrain
        self.fps = fps
        self.gop = gop
        self.hdr_2sdr = hdr_2sdr
        self.height = height
        self.long_short_mode = long_short_mode
        self.max_fps = max_fps
        self.maxrate = maxrate
        self.narrow_band = narrow_band
        self.pad = pad
        self.pix_fmt = pix_fmt
        self.preset = preset
        self.profile = profile
        self.qscale = qscale
        self.remove = remove
        self.reso_priority = reso_priority
        self.scan_mode = scan_mode
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
            temp_model = main_models.QueryTemplateListResponseBodyTemplateListTemplateVideoBitrateBnd()
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
            temp_model = main_models.QueryTemplateListResponseBodyTemplateListTemplateVideoNarrowBand()
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

class QueryTemplateListResponseBodyTemplateListTemplateVideoNarrowBand(DaraModel):
    def __init__(
        self,
        abrmax: float = None,
        max_abr_ratio: float = None,
        version: str = None,
    ):
        self.abrmax = abrmax
        self.max_abr_ratio = max_abr_ratio
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

class QueryTemplateListResponseBodyTemplateListTemplateVideoBitrateBnd(DaraModel):
    def __init__(
        self,
        max: str = None,
        min: str = None,
    ):
        self.max = max
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

class QueryTemplateListResponseBodyTemplateListTemplateTransConfig(DaraModel):
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
        self.adj_dar_method = adj_dar_method
        self.is_check_audio_bitrate = is_check_audio_bitrate
        self.is_check_audio_bitrate_fail = is_check_audio_bitrate_fail
        self.is_check_reso = is_check_reso
        self.is_check_reso_fail = is_check_reso_fail
        self.is_check_video_bitrate = is_check_video_bitrate
        self.is_check_video_bitrate_fail = is_check_video_bitrate_fail
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

class QueryTemplateListResponseBodyTemplateListTemplateMuxConfig(DaraModel):
    def __init__(
        self,
        gif: main_models.QueryTemplateListResponseBodyTemplateListTemplateMuxConfigGif = None,
        segment: main_models.QueryTemplateListResponseBodyTemplateListTemplateMuxConfigSegment = None,
        webp: main_models.QueryTemplateListResponseBodyTemplateListTemplateMuxConfigWebp = None,
    ):
        self.gif = gif
        self.segment = segment
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
            temp_model = main_models.QueryTemplateListResponseBodyTemplateListTemplateMuxConfigGif()
            self.gif = temp_model.from_map(m.get('Gif'))

        if m.get('Segment') is not None:
            temp_model = main_models.QueryTemplateListResponseBodyTemplateListTemplateMuxConfigSegment()
            self.segment = temp_model.from_map(m.get('Segment'))

        if m.get('Webp') is not None:
            temp_model = main_models.QueryTemplateListResponseBodyTemplateListTemplateMuxConfigWebp()
            self.webp = temp_model.from_map(m.get('Webp'))

        return self

class QueryTemplateListResponseBodyTemplateListTemplateMuxConfigWebp(DaraModel):
    def __init__(
        self,
        loop: str = None,
    ):
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

class QueryTemplateListResponseBodyTemplateListTemplateMuxConfigSegment(DaraModel):
    def __init__(
        self,
        duration: str = None,
    ):
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

class QueryTemplateListResponseBodyTemplateListTemplateMuxConfigGif(DaraModel):
    def __init__(
        self,
        dither_mode: str = None,
        final_delay: str = None,
        is_custom_palette: str = None,
        loop: str = None,
    ):
        self.dither_mode = dither_mode
        self.final_delay = final_delay
        self.is_custom_palette = is_custom_palette
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

class QueryTemplateListResponseBodyTemplateListTemplateContainer(DaraModel):
    def __init__(
        self,
        format: str = None,
    ):
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

class QueryTemplateListResponseBodyTemplateListTemplateAudio(DaraModel):
    def __init__(
        self,
        bitrate: str = None,
        channels: str = None,
        codec: str = None,
        profile: str = None,
        qscale: str = None,
        remove: str = None,
        samplerate: str = None,
        volume: main_models.QueryTemplateListResponseBodyTemplateListTemplateAudioVolume = None,
    ):
        self.bitrate = bitrate
        self.channels = channels
        self.codec = codec
        self.profile = profile
        self.qscale = qscale
        self.remove = remove
        self.samplerate = samplerate
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
            temp_model = main_models.QueryTemplateListResponseBodyTemplateListTemplateAudioVolume()
            self.volume = temp_model.from_map(m.get('Volume'))

        return self

class QueryTemplateListResponseBodyTemplateListTemplateAudioVolume(DaraModel):
    def __init__(
        self,
        integrated_loudness_target: str = None,
        level: str = None,
        loudness_range_target: str = None,
        method: str = None,
        peak_level: str = None,
        true_peak: str = None,
    ):
        self.integrated_loudness_target = integrated_loudness_target
        self.level = level
        self.loudness_range_target = loudness_range_target
        self.method = method
        self.peak_level = peak_level
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

class QueryTemplateListResponseBodyNonExistTids(DaraModel):
    def __init__(
        self,
        string: List[str] = None,
    ):
        self.string = string

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.string is not None:
            result['String'] = self.string

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('String') is not None:
            self.string = m.get('String')

        return self

