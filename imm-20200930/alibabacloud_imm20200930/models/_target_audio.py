# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_imm20200930 import models as main_models
from darabonba.model import DaraModel

class TargetAudio(DaraModel):
    def __init__(
        self,
        disable_audio: bool = None,
        filter_audio: main_models.TargetAudioFilterAudio = None,
        stream: List[int] = None,
        transcode_audio: main_models.TargetAudioTranscodeAudio = None,
    ):
        # Specifies whether to disable audio stream generation. Valid values:
        # 
        # *   true: disables audio stream generation. No audio stream is included in the output file.
        # *   false: does not disable audio stream generation. This is the default value.
        self.disable_audio = disable_audio
        # The audio processing settings. This parameter is invalid if **TranscodeAudio** is left empty or **TranscodeAudio.Codec** is set to copy.
        # 
        # >  This parameter is not available to the GenerateVideoPlaylist operation.
        self.filter_audio = filter_audio
        # The index numbers of audio streams. If you do not specify this parameter, the first audio stream (the one with the smallest index number) is processed. If the array contains an element greater than 100, all audio streams are processed.
        # 
        # *   For example, you can set the parameter to `[0,1]` to process audio streams with index numbers 0 and 1, `[1]` to process only the audio stream with the index number 1, or `[101]` to process all audio streams.
        # 
        # >  If you specify an index number but no audio stream with the index number is found, the index number is ignored.
        self.stream = stream
        # The audio transcoding settings. If you do not specify this parameter, no audio streams are included in the output file.
        # 
        # >  We recommend that you do not use this parameter to disable audio stream generation.
        self.transcode_audio = transcode_audio

    def validate(self):
        if self.filter_audio:
            self.filter_audio.validate()
        if self.transcode_audio:
            self.transcode_audio.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.disable_audio is not None:
            result['DisableAudio'] = self.disable_audio

        if self.filter_audio is not None:
            result['FilterAudio'] = self.filter_audio.to_map()

        if self.stream is not None:
            result['Stream'] = self.stream

        if self.transcode_audio is not None:
            result['TranscodeAudio'] = self.transcode_audio.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisableAudio') is not None:
            self.disable_audio = m.get('DisableAudio')

        if m.get('FilterAudio') is not None:
            temp_model = main_models.TargetAudioFilterAudio()
            self.filter_audio = temp_model.from_map(m.get('FilterAudio'))

        if m.get('Stream') is not None:
            self.stream = m.get('Stream')

        if m.get('TranscodeAudio') is not None:
            temp_model = main_models.TargetAudioTranscodeAudio()
            self.transcode_audio = temp_model.from_map(m.get('TranscodeAudio'))

        return self

class TargetAudioTranscodeAudio(DaraModel):
    def __init__(
        self,
        bitrate: int = None,
        bitrate_option: str = None,
        bits_per_sample: int = None,
        channel: int = None,
        codec: str = None,
        quality: int = None,
        sample_rate: int = None,
        sample_rate_option: str = None,
    ):
        # The bitrate of the audio stream. Unit: bit/s. This parameter and the **Quality** parameter are mutually exclusive. Valid values: 1000 to 10000000.
        self.bitrate = bitrate
        # The audio bitrate option. Valid values:
        # 
        # *   fixed: always uses the target bitrate.
        # *   adaptive: uses the source bitrate when the source bitrate is smaller than the target bitrate.
        # *   fall: returns a failure when the source bitrate is smaller than the target bitrate.
        # 
        # Default values:
        # 
        # *   fixed for the CreateMediaConvert operation.
        # *   adaptive for the GenerateVideoPlaylist operation.
        # 
        # >  This parameter must be used in conjunction with the **Bitrate** parameter.
        self.bitrate_option = bitrate_option
        # The audio bit depth. Valid values: 16 and 24.
        # 
        # >  This parameter takes effect only when Codec is set to flac.
        self.bits_per_sample = bits_per_sample
        # The number of sound channels. By default, the audio stream has the same number of sound channels as the source audio. Valid values: [1,8].
        # 
        # >  The number of sound channels varies with audio formats: one or two for MP3, up to six for AC3 5.1, and one for AMR.
        self.channel = channel
        # The codec. Valid values:
        # 
        # *   copy, mp3, vorbis, aac, flac, ac3, opus, and amr for the CreateMediaConvert operation. The default value is copy.
        # *   aac for the GenerateVideoPlaylist operation. The default value is aac.
        # 
        # >  When you set the parameter to copy, the audio stream is directly copied into the output file and all other parameters in **TranscodeAudio** do not take effect. The copy value is commonly used in container format conversion scenarios. You cannot use this value in audio merging scenarios.
        self.codec = codec
        # The audio quality. Valid values: 0 to 100. The greater the value, the higher the quality. This parameter and the **Bitrate** parameter are mutually exclusive.
        self.quality = quality
        # The sampling rate option. Unit: Hz. By default, the source sampling rate is used. Valid values: 8000, 12025, 12000, 16000, 22050, 24000, 32000, 44100, 48000, 64000, 88200, and 96000.
        # 
        # >  Supported sampling rates vary with formats: 48 kHz and lower for MP3, 8 kHz, 12 kHz, 16 kHz, 24 kHz, and 48 kHz for Opus, 32 kHz, 44.1 kHz, and 48 kHz for AC3, and 8 kHz and 16 kHz for AMR.
        self.sample_rate = sample_rate
        # The sampling rate option. Valid values:
        # 
        # *   fixed: always uses the target sampling rate.
        # *   adaptive: uses the source sampling rate when the source sampling rate is smaller than the target sampling rate.
        # *   fall: returns a failure when the source sampling rate is smaller than the target sampling rate.
        # 
        # Default values:
        # 
        # *   fixed for the CreateMediaConvert operation.
        # *   adaptive for the GenerateVideoPlaylist operation.
        # 
        # >  This parameter must be used in conjunction with the **SampleRate** parameter.
        self.sample_rate_option = sample_rate_option

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bitrate is not None:
            result['Bitrate'] = self.bitrate

        if self.bitrate_option is not None:
            result['BitrateOption'] = self.bitrate_option

        if self.bits_per_sample is not None:
            result['BitsPerSample'] = self.bits_per_sample

        if self.channel is not None:
            result['Channel'] = self.channel

        if self.codec is not None:
            result['Codec'] = self.codec

        if self.quality is not None:
            result['Quality'] = self.quality

        if self.sample_rate is not None:
            result['SampleRate'] = self.sample_rate

        if self.sample_rate_option is not None:
            result['SampleRateOption'] = self.sample_rate_option

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bitrate') is not None:
            self.bitrate = m.get('Bitrate')

        if m.get('BitrateOption') is not None:
            self.bitrate_option = m.get('BitrateOption')

        if m.get('BitsPerSample') is not None:
            self.bits_per_sample = m.get('BitsPerSample')

        if m.get('Channel') is not None:
            self.channel = m.get('Channel')

        if m.get('Codec') is not None:
            self.codec = m.get('Codec')

        if m.get('Quality') is not None:
            self.quality = m.get('Quality')

        if m.get('SampleRate') is not None:
            self.sample_rate = m.get('SampleRate')

        if m.get('SampleRateOption') is not None:
            self.sample_rate_option = m.get('SampleRateOption')

        return self

class TargetAudioFilterAudio(DaraModel):
    def __init__(
        self,
        mixing: bool = None,
    ):
        # Specifies whether to mix all sound tracks into a single track. Valid values:
        # 
        # *   false (default)
        # *   true
        self.mixing = mixing

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mixing is not None:
            result['Mixing'] = self.mixing

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Mixing') is not None:
            self.mixing = m.get('Mixing')

        return self

