# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class MediaConvertAudio(DaraModel):
    def __init__(
        self,
        bitrate: int = None,
        channels: int = None,
        codec: str = None,
        profile: str = None,
        remove: bool = None,
        samplerate: str = None,
    ):
        # The audio bitrate of the output file.
        # 
        # *   Unit: Kbps.
        # *   Valid values: [8,1000].
        # *   Default value: 128.
        # *   Common values: 64, 128, and 256.
        self.bitrate = bitrate
        # The number of audio channels.
        # 
        # *   Valid values: 0, 1, 2, 4, 5, 6, and 8.
        # 
        #     *   If the Codec parameter is set to MP3 or OPUS, you can set this parameter to 0, 1, or 2.
        #     *   If the Codec parameter is set to AAC or FLAC, you can set this parameter to 0, 1, 2, 4, 5, 6, or 8.
        #     *   If the Codec parameter is set to VORBIS, you can set this parameter to 2.
        #     *   If the Format parameter is set to MPD, you cannot set this parameter to 8.
        # 
        # *   Default value: 2.
        # 
        # *   Set the value to 0 to preserve the original number of channels from the source file.
        self.channels = channels
        # The audio codec.
        # 
        # *   Valid values: AAC, AC3, EAC3, MP2, MP3, FLAC, OPUS, VORBIS, WMA-V1, WMA-V2, and pcm_s16le.
        # *   Default value: AAC.
        self.codec = codec
        # The audio codec profile.
        # 
        # *   This parameter takes effect only if the Codec parameter is set to AAC.
        # *   Valid values: aac_low, aac_he, aac_he_v2, aac_ld, and aac_eld.
        # *   Default value: aac_low.
        self.profile = profile
        # Specifies whether to remove the audio stream from the output.
        # 
        # *   true: deletes the audio stream. All other parameters in the Audio object are ignored.
        # *   false: retains the audio stream.
        # *   Default value: false.
        self.remove = remove
        # The sample rate.
        # 
        # *   Unit: Hz
        # *   Valid values: 22050, 32000, 44100, 48000, and 96000.
        # *   Default value: 44100.
        # 
        # The supported sample rates vary depending on the container and codec format. For example, when the audio codec is MP3, a sample rate of 96000 is not supported. If the container format is FLV, only sample rates of 22050 and 44100 are supported.
        self.samplerate = samplerate

    def validate(self):
        pass

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

        if self.remove is not None:
            result['Remove'] = self.remove

        if self.samplerate is not None:
            result['Samplerate'] = self.samplerate

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

        if m.get('Remove') is not None:
            self.remove = m.get('Remove')

        if m.get('Samplerate') is not None:
            self.samplerate = m.get('Samplerate')

        return self

