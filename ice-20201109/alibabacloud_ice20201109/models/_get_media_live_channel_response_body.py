# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class GetMediaLiveChannelResponseBody(DaraModel):
    def __init__(
        self,
        channel: main_models.GetMediaLiveChannelResponseBodyChannel = None,
        request_id: str = None,
    ):
        # The channel information.
        self.channel = channel
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.channel:
            self.channel.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channel is not None:
            result['Channel'] = self.channel.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Channel') is not None:
            temp_model = main_models.GetMediaLiveChannelResponseBodyChannel()
            self.channel = temp_model.from_map(m.get('Channel'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetMediaLiveChannelResponseBodyChannel(DaraModel):
    def __init__(
        self,
        audio_settings: List[main_models.GetMediaLiveChannelResponseBodyChannelAudioSettings] = None,
        channel_id: str = None,
        create_time: str = None,
        input_attachments: List[main_models.GetMediaLiveChannelResponseBodyChannelInputAttachments] = None,
        last_start_time: str = None,
        last_stop_time: str = None,
        name: str = None,
        output_groups: List[main_models.GetMediaLiveChannelResponseBodyChannelOutputGroups] = None,
        state: str = None,
        video_settings: List[main_models.GetMediaLiveChannelResponseBodyChannelVideoSettings] = None,
    ):
        # The audio settings.
        self.audio_settings = audio_settings
        # The ID of the channel.
        self.channel_id = channel_id
        # The time when the channel was created. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.create_time = create_time
        # The inputs associated with the channel.
        self.input_attachments = input_attachments
        # The time when the channel was last started. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC. If the channel has never been started since it was created, an empty string is returned.
        self.last_start_time = last_start_time
        # The time when the channel was last stopped. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC. If the channel has never stopped since it was created, an empty string is returned.
        self.last_stop_time = last_stop_time
        # The channel name.
        self.name = name
        # The output groups.
        self.output_groups = output_groups
        # The state of the channel. Valid values: IDLE, STARTING, RUNNING, RECOVERING, and STOPPING.
        self.state = state
        # The video settings.
        self.video_settings = video_settings

    def validate(self):
        if self.audio_settings:
            for v1 in self.audio_settings:
                 if v1:
                    v1.validate()
        if self.input_attachments:
            for v1 in self.input_attachments:
                 if v1:
                    v1.validate()
        if self.output_groups:
            for v1 in self.output_groups:
                 if v1:
                    v1.validate()
        if self.video_settings:
            for v1 in self.video_settings:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AudioSettings'] = []
        if self.audio_settings is not None:
            for k1 in self.audio_settings:
                result['AudioSettings'].append(k1.to_map() if k1 else None)

        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        result['InputAttachments'] = []
        if self.input_attachments is not None:
            for k1 in self.input_attachments:
                result['InputAttachments'].append(k1.to_map() if k1 else None)

        if self.last_start_time is not None:
            result['LastStartTime'] = self.last_start_time

        if self.last_stop_time is not None:
            result['LastStopTime'] = self.last_stop_time

        if self.name is not None:
            result['Name'] = self.name

        result['OutputGroups'] = []
        if self.output_groups is not None:
            for k1 in self.output_groups:
                result['OutputGroups'].append(k1.to_map() if k1 else None)

        if self.state is not None:
            result['State'] = self.state

        result['VideoSettings'] = []
        if self.video_settings is not None:
            for k1 in self.video_settings:
                result['VideoSettings'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.audio_settings = []
        if m.get('AudioSettings') is not None:
            for k1 in m.get('AudioSettings'):
                temp_model = main_models.GetMediaLiveChannelResponseBodyChannelAudioSettings()
                self.audio_settings.append(temp_model.from_map(k1))

        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        self.input_attachments = []
        if m.get('InputAttachments') is not None:
            for k1 in m.get('InputAttachments'):
                temp_model = main_models.GetMediaLiveChannelResponseBodyChannelInputAttachments()
                self.input_attachments.append(temp_model.from_map(k1))

        if m.get('LastStartTime') is not None:
            self.last_start_time = m.get('LastStartTime')

        if m.get('LastStopTime') is not None:
            self.last_stop_time = m.get('LastStopTime')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        self.output_groups = []
        if m.get('OutputGroups') is not None:
            for k1 in m.get('OutputGroups'):
                temp_model = main_models.GetMediaLiveChannelResponseBodyChannelOutputGroups()
                self.output_groups.append(temp_model.from_map(k1))

        if m.get('State') is not None:
            self.state = m.get('State')

        self.video_settings = []
        if m.get('VideoSettings') is not None:
            for k1 in m.get('VideoSettings'):
                temp_model = main_models.GetMediaLiveChannelResponseBodyChannelVideoSettings()
                self.video_settings.append(temp_model.from_map(k1))

        return self

class GetMediaLiveChannelResponseBodyChannelVideoSettings(DaraModel):
    def __init__(
        self,
        height: int = None,
        name: str = None,
        video_codec: str = None,
        video_codec_setting: main_models.GetMediaLiveChannelResponseBodyChannelVideoSettingsVideoCodecSetting = None,
        video_codec_type: str = None,
        width: int = None,
    ):
        # The height of the video in pixels.
        self.height = height
        # The name of the video settings.
        self.name = name
        # The video codec.
        self.video_codec = video_codec
        # The video encoding settings.
        self.video_codec_setting = video_codec_setting
        # The video transcoding method. Valid values: NORMAL (regular transcoding) and NBHD (Narrowband HD™ transcoding).
        self.video_codec_type = video_codec_type
        # The width of the video in pixels.
        self.width = width

    def validate(self):
        if self.video_codec_setting:
            self.video_codec_setting.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.height is not None:
            result['Height'] = self.height

        if self.name is not None:
            result['Name'] = self.name

        if self.video_codec is not None:
            result['VideoCodec'] = self.video_codec

        if self.video_codec_setting is not None:
            result['VideoCodecSetting'] = self.video_codec_setting.to_map()

        if self.video_codec_type is not None:
            result['VideoCodecType'] = self.video_codec_type

        if self.width is not None:
            result['Width'] = self.width

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Height') is not None:
            self.height = m.get('Height')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('VideoCodec') is not None:
            self.video_codec = m.get('VideoCodec')

        if m.get('VideoCodecSetting') is not None:
            temp_model = main_models.GetMediaLiveChannelResponseBodyChannelVideoSettingsVideoCodecSetting()
            self.video_codec_setting = temp_model.from_map(m.get('VideoCodecSetting'))

        if m.get('VideoCodecType') is not None:
            self.video_codec_type = m.get('VideoCodecType')

        if m.get('Width') is not None:
            self.width = m.get('Width')

        return self

class GetMediaLiveChannelResponseBodyChannelVideoSettingsVideoCodecSetting(DaraModel):
    def __init__(
        self,
        codec_detail: main_models.GetMediaLiveChannelResponseBodyChannelVideoSettingsVideoCodecSettingCodecDetail = None,
        framerate: main_models.GetMediaLiveChannelResponseBodyChannelVideoSettingsVideoCodecSettingFramerate = None,
        gop: main_models.GetMediaLiveChannelResponseBodyChannelVideoSettingsVideoCodecSettingGop = None,
        rate: main_models.GetMediaLiveChannelResponseBodyChannelVideoSettingsVideoCodecSettingRate = None,
    ):
        # The video encoding settings.
        self.codec_detail = codec_detail
        # The frame rate.
        self.framerate = framerate
        # The GOP setting.
        self.gop = gop
        # The video encoding rate.
        self.rate = rate

    def validate(self):
        if self.codec_detail:
            self.codec_detail.validate()
        if self.framerate:
            self.framerate.validate()
        if self.gop:
            self.gop.validate()
        if self.rate:
            self.rate.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.codec_detail is not None:
            result['CodecDetail'] = self.codec_detail.to_map()

        if self.framerate is not None:
            result['Framerate'] = self.framerate.to_map()

        if self.gop is not None:
            result['Gop'] = self.gop.to_map()

        if self.rate is not None:
            result['Rate'] = self.rate.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CodecDetail') is not None:
            temp_model = main_models.GetMediaLiveChannelResponseBodyChannelVideoSettingsVideoCodecSettingCodecDetail()
            self.codec_detail = temp_model.from_map(m.get('CodecDetail'))

        if m.get('Framerate') is not None:
            temp_model = main_models.GetMediaLiveChannelResponseBodyChannelVideoSettingsVideoCodecSettingFramerate()
            self.framerate = temp_model.from_map(m.get('Framerate'))

        if m.get('Gop') is not None:
            temp_model = main_models.GetMediaLiveChannelResponseBodyChannelVideoSettingsVideoCodecSettingGop()
            self.gop = temp_model.from_map(m.get('Gop'))

        if m.get('Rate') is not None:
            temp_model = main_models.GetMediaLiveChannelResponseBodyChannelVideoSettingsVideoCodecSettingRate()
            self.rate = temp_model.from_map(m.get('Rate'))

        return self

class GetMediaLiveChannelResponseBodyChannelVideoSettingsVideoCodecSettingRate(DaraModel):
    def __init__(
        self,
        bitrate: int = None,
        buffer_size: int = None,
        max_bitrate: int = None,
        rate_control_mode: str = None,
    ):
        # The video bitrate. Unit: bit/s.
        self.bitrate = bitrate
        # The video buffer size. Unit: bit/s.
        self.buffer_size = buffer_size
        # The maximum bitrate. Unit: bit/s.
        self.max_bitrate = max_bitrate
        # The bitrate control mode.
        self.rate_control_mode = rate_control_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bitrate is not None:
            result['Bitrate'] = self.bitrate

        if self.buffer_size is not None:
            result['BufferSize'] = self.buffer_size

        if self.max_bitrate is not None:
            result['MaxBitrate'] = self.max_bitrate

        if self.rate_control_mode is not None:
            result['RateControlMode'] = self.rate_control_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bitrate') is not None:
            self.bitrate = m.get('Bitrate')

        if m.get('BufferSize') is not None:
            self.buffer_size = m.get('BufferSize')

        if m.get('MaxBitrate') is not None:
            self.max_bitrate = m.get('MaxBitrate')

        if m.get('RateControlMode') is not None:
            self.rate_control_mode = m.get('RateControlMode')

        return self

class GetMediaLiveChannelResponseBodyChannelVideoSettingsVideoCodecSettingGop(DaraModel):
    def __init__(
        self,
        bframes_num: int = None,
        gop_size: int = None,
        gop_size_units: str = None,
    ):
        # The number of B frames.
        self.bframes_num = bframes_num
        # The GOP size.
        self.gop_size = gop_size
        # The GOP size unit.
        self.gop_size_units = gop_size_units

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bframes_num is not None:
            result['BframesNum'] = self.bframes_num

        if self.gop_size is not None:
            result['GopSize'] = self.gop_size

        if self.gop_size_units is not None:
            result['GopSizeUnits'] = self.gop_size_units

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BframesNum') is not None:
            self.bframes_num = m.get('BframesNum')

        if m.get('GopSize') is not None:
            self.gop_size = m.get('GopSize')

        if m.get('GopSizeUnits') is not None:
            self.gop_size_units = m.get('GopSizeUnits')

        return self

class GetMediaLiveChannelResponseBodyChannelVideoSettingsVideoCodecSettingFramerate(DaraModel):
    def __init__(
        self,
        framerate_control: str = None,
        framerate_denominator: int = None,
        framerate_numerator: int = None,
    ):
        # The frame rate mode.
        self.framerate_control = framerate_control
        # The denominator of the fixed frame rate.
        self.framerate_denominator = framerate_denominator
        # The numerator of the fixed frame rate.
        self.framerate_numerator = framerate_numerator

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.framerate_control is not None:
            result['FramerateControl'] = self.framerate_control

        if self.framerate_denominator is not None:
            result['FramerateDenominator'] = self.framerate_denominator

        if self.framerate_numerator is not None:
            result['FramerateNumerator'] = self.framerate_numerator

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FramerateControl') is not None:
            self.framerate_control = m.get('FramerateControl')

        if m.get('FramerateDenominator') is not None:
            self.framerate_denominator = m.get('FramerateDenominator')

        if m.get('FramerateNumerator') is not None:
            self.framerate_numerator = m.get('FramerateNumerator')

        return self

class GetMediaLiveChannelResponseBodyChannelVideoSettingsVideoCodecSettingCodecDetail(DaraModel):
    def __init__(
        self,
        level: str = None,
        profile: str = None,
    ):
        # The video encoding level. It is not supported yet.
        self.level = level
        # The H.264 profile.
        self.profile = profile

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.level is not None:
            result['Level'] = self.level

        if self.profile is not None:
            result['Profile'] = self.profile

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('Profile') is not None:
            self.profile = m.get('Profile')

        return self

class GetMediaLiveChannelResponseBodyChannelOutputGroups(DaraModel):
    def __init__(
        self,
        media_package_group_setting: main_models.GetMediaLiveChannelResponseBodyChannelOutputGroupsMediaPackageGroupSetting = None,
        monitor_url: str = None,
        name: str = None,
        outputs: List[main_models.GetMediaLiveChannelResponseBodyChannelOutputGroupsOutputs] = None,
        type: str = None,
    ):
        # The MediaPackage destination.
        self.media_package_group_setting = media_package_group_setting
        # The URL for monitoring the output group. The parameter is returned only when the output gourp type is MediaPackage.
        self.monitor_url = monitor_url
        # The name of the output group.
        self.name = name
        # The outputs in the output group.
        self.outputs = outputs
        # The output group type.
        self.type = type

    def validate(self):
        if self.media_package_group_setting:
            self.media_package_group_setting.validate()
        if self.outputs:
            for v1 in self.outputs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.media_package_group_setting is not None:
            result['MediaPackageGroupSetting'] = self.media_package_group_setting.to_map()

        if self.monitor_url is not None:
            result['MonitorUrl'] = self.monitor_url

        if self.name is not None:
            result['Name'] = self.name

        result['Outputs'] = []
        if self.outputs is not None:
            for k1 in self.outputs:
                result['Outputs'].append(k1.to_map() if k1 else None)

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MediaPackageGroupSetting') is not None:
            temp_model = main_models.GetMediaLiveChannelResponseBodyChannelOutputGroupsMediaPackageGroupSetting()
            self.media_package_group_setting = temp_model.from_map(m.get('MediaPackageGroupSetting'))

        if m.get('MonitorUrl') is not None:
            self.monitor_url = m.get('MonitorUrl')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        self.outputs = []
        if m.get('Outputs') is not None:
            for k1 in m.get('Outputs'):
                temp_model = main_models.GetMediaLiveChannelResponseBodyChannelOutputGroupsOutputs()
                self.outputs.append(temp_model.from_map(k1))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class GetMediaLiveChannelResponseBodyChannelOutputGroupsOutputs(DaraModel):
    def __init__(
        self,
        audio_setting_names: List[str] = None,
        media_package_output_setting: main_models.GetMediaLiveChannelResponseBodyChannelOutputGroupsOutputsMediaPackageOutputSetting = None,
        media_type: int = None,
        name: str = None,
        video_setting_name: str = None,
    ):
        # The referenced AudioSettings.
        self.audio_setting_names = audio_setting_names
        # The settings of the output delivered to MediaPackage.
        self.media_package_output_setting = media_package_output_setting
        # The media type of the output.
        self.media_type = media_type
        # The name of the output.
        self.name = name
        # The name of the referenced VideoSettings.
        self.video_setting_name = video_setting_name

    def validate(self):
        if self.media_package_output_setting:
            self.media_package_output_setting.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audio_setting_names is not None:
            result['AudioSettingNames'] = self.audio_setting_names

        if self.media_package_output_setting is not None:
            result['MediaPackageOutputSetting'] = self.media_package_output_setting.to_map()

        if self.media_type is not None:
            result['MediaType'] = self.media_type

        if self.name is not None:
            result['Name'] = self.name

        if self.video_setting_name is not None:
            result['VideoSettingName'] = self.video_setting_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AudioSettingNames') is not None:
            self.audio_setting_names = m.get('AudioSettingNames')

        if m.get('MediaPackageOutputSetting') is not None:
            temp_model = main_models.GetMediaLiveChannelResponseBodyChannelOutputGroupsOutputsMediaPackageOutputSetting()
            self.media_package_output_setting = temp_model.from_map(m.get('MediaPackageOutputSetting'))

        if m.get('MediaType') is not None:
            self.media_type = m.get('MediaType')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('VideoSettingName') is not None:
            self.video_setting_name = m.get('VideoSettingName')

        return self

class GetMediaLiveChannelResponseBodyChannelOutputGroupsOutputsMediaPackageOutputSetting(DaraModel):
    def __init__(
        self,
        audio_group_id: str = None,
        name_modifier: str = None,
    ):
        # The manifest audio group ID.
        self.audio_group_id = audio_group_id
        # The manifest name modifier. The child manifests include this modifier in their M3U8 file names.
        self.name_modifier = name_modifier

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audio_group_id is not None:
            result['AudioGroupId'] = self.audio_group_id

        if self.name_modifier is not None:
            result['NameModifier'] = self.name_modifier

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AudioGroupId') is not None:
            self.audio_group_id = m.get('AudioGroupId')

        if m.get('NameModifier') is not None:
            self.name_modifier = m.get('NameModifier')

        return self

class GetMediaLiveChannelResponseBodyChannelOutputGroupsMediaPackageGroupSetting(DaraModel):
    def __init__(
        self,
        channel_name: str = None,
        group_name: str = None,
    ):
        # ChannelName in MediaPackage.
        self.channel_name = channel_name
        # GroupName in MediaPackage.
        self.group_name = group_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channel_name is not None:
            result['ChannelName'] = self.channel_name

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelName') is not None:
            self.channel_name = m.get('ChannelName')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        return self

class GetMediaLiveChannelResponseBodyChannelInputAttachments(DaraModel):
    def __init__(
        self,
        audio_selectors: List[main_models.GetMediaLiveChannelResponseBodyChannelInputAttachmentsAudioSelectors] = None,
        input_id: str = None,
        input_name: str = None,
        language_name: str = None,
    ):
        # The audio selectors.
        self.audio_selectors = audio_selectors
        # The ID of the associated input.
        # 
        # This parameter is required.
        self.input_id = input_id
        # The name of the input.
        self.input_name = input_name
        # The language name.
        self.language_name = language_name

    def validate(self):
        if self.audio_selectors:
            for v1 in self.audio_selectors:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AudioSelectors'] = []
        if self.audio_selectors is not None:
            for k1 in self.audio_selectors:
                result['AudioSelectors'].append(k1.to_map() if k1 else None)

        if self.input_id is not None:
            result['InputId'] = self.input_id

        if self.input_name is not None:
            result['InputName'] = self.input_name

        if self.language_name is not None:
            result['LanguageName'] = self.language_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.audio_selectors = []
        if m.get('AudioSelectors') is not None:
            for k1 in m.get('AudioSelectors'):
                temp_model = main_models.GetMediaLiveChannelResponseBodyChannelInputAttachmentsAudioSelectors()
                self.audio_selectors.append(temp_model.from_map(k1))

        if m.get('InputId') is not None:
            self.input_id = m.get('InputId')

        if m.get('InputName') is not None:
            self.input_name = m.get('InputName')

        if m.get('LanguageName') is not None:
            self.language_name = m.get('LanguageName')

        return self

class GetMediaLiveChannelResponseBodyChannelInputAttachmentsAudioSelectors(DaraModel):
    def __init__(
        self,
        audio_language_selection: main_models.GetMediaLiveChannelResponseBodyChannelInputAttachmentsAudioSelectorsAudioLanguageSelection = None,
        audio_pid_selection: main_models.GetMediaLiveChannelResponseBodyChannelInputAttachmentsAudioSelectorsAudioPidSelection = None,
        audio_track_selection: List[main_models.GetMediaLiveChannelResponseBodyChannelInputAttachmentsAudioSelectorsAudioTrackSelection] = None,
        name: str = None,
    ):
        # The audio language selection.
        self.audio_language_selection = audio_language_selection
        # The audio PID selection.
        self.audio_pid_selection = audio_pid_selection
        # The audio track selection.
        self.audio_track_selection = audio_track_selection
        # The name of the audio selector.
        # 
        # This parameter is required.
        self.name = name

    def validate(self):
        if self.audio_language_selection:
            self.audio_language_selection.validate()
        if self.audio_pid_selection:
            self.audio_pid_selection.validate()
        if self.audio_track_selection:
            for v1 in self.audio_track_selection:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audio_language_selection is not None:
            result['AudioLanguageSelection'] = self.audio_language_selection.to_map()

        if self.audio_pid_selection is not None:
            result['AudioPidSelection'] = self.audio_pid_selection.to_map()

        result['AudioTrackSelection'] = []
        if self.audio_track_selection is not None:
            for k1 in self.audio_track_selection:
                result['AudioTrackSelection'].append(k1.to_map() if k1 else None)

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AudioLanguageSelection') is not None:
            temp_model = main_models.GetMediaLiveChannelResponseBodyChannelInputAttachmentsAudioSelectorsAudioLanguageSelection()
            self.audio_language_selection = temp_model.from_map(m.get('AudioLanguageSelection'))

        if m.get('AudioPidSelection') is not None:
            temp_model = main_models.GetMediaLiveChannelResponseBodyChannelInputAttachmentsAudioSelectorsAudioPidSelection()
            self.audio_pid_selection = temp_model.from_map(m.get('AudioPidSelection'))

        self.audio_track_selection = []
        if m.get('AudioTrackSelection') is not None:
            for k1 in m.get('AudioTrackSelection'):
                temp_model = main_models.GetMediaLiveChannelResponseBodyChannelInputAttachmentsAudioSelectorsAudioTrackSelection()
                self.audio_track_selection.append(temp_model.from_map(k1))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class GetMediaLiveChannelResponseBodyChannelInputAttachmentsAudioSelectorsAudioTrackSelection(DaraModel):
    def __init__(
        self,
        track_id: int = None,
    ):
        # The track ID from within a source.
        # 
        # This parameter is required.
        self.track_id = track_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.track_id is not None:
            result['TrackId'] = self.track_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TrackId') is not None:
            self.track_id = m.get('TrackId')

        return self

class GetMediaLiveChannelResponseBodyChannelInputAttachmentsAudioSelectorsAudioPidSelection(DaraModel):
    def __init__(
        self,
        pid: int = None,
    ):
        # A PID from within a source.
        # 
        # This parameter is required.
        self.pid = pid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.pid is not None:
            result['Pid'] = self.pid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')

        return self

class GetMediaLiveChannelResponseBodyChannelInputAttachmentsAudioSelectorsAudioLanguageSelection(DaraModel):
    def __init__(
        self,
        language_code: str = None,
    ):
        # A three-letter ISO 639-2 language code from within an audio source.
        # 
        # This parameter is required.
        self.language_code = language_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.language_code is not None:
            result['LanguageCode'] = self.language_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LanguageCode') is not None:
            self.language_code = m.get('LanguageCode')

        return self

class GetMediaLiveChannelResponseBodyChannelAudioSettings(DaraModel):
    def __init__(
        self,
        audio_codec: str = None,
        audio_codec_setting: main_models.GetMediaLiveChannelResponseBodyChannelAudioSettingsAudioCodecSetting = None,
        audio_selector_name: str = None,
        language_code: str = None,
        language_name: str = None,
        name: str = None,
    ):
        # The audio codec.
        self.audio_codec = audio_codec
        # The audio encoding settings.
        self.audio_codec_setting = audio_codec_setting
        # The name of the audio selector.
        self.audio_selector_name = audio_selector_name
        # A three-letter ISO 639-2 language code.
        self.language_code = language_code
        # The name of the language.
        self.language_name = language_name
        # The name of the audio settings.
        self.name = name

    def validate(self):
        if self.audio_codec_setting:
            self.audio_codec_setting.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audio_codec is not None:
            result['AudioCodec'] = self.audio_codec

        if self.audio_codec_setting is not None:
            result['AudioCodecSetting'] = self.audio_codec_setting.to_map()

        if self.audio_selector_name is not None:
            result['AudioSelectorName'] = self.audio_selector_name

        if self.language_code is not None:
            result['LanguageCode'] = self.language_code

        if self.language_name is not None:
            result['LanguageName'] = self.language_name

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AudioCodec') is not None:
            self.audio_codec = m.get('AudioCodec')

        if m.get('AudioCodecSetting') is not None:
            temp_model = main_models.GetMediaLiveChannelResponseBodyChannelAudioSettingsAudioCodecSetting()
            self.audio_codec_setting = temp_model.from_map(m.get('AudioCodecSetting'))

        if m.get('AudioSelectorName') is not None:
            self.audio_selector_name = m.get('AudioSelectorName')

        if m.get('LanguageCode') is not None:
            self.language_code = m.get('LanguageCode')

        if m.get('LanguageName') is not None:
            self.language_name = m.get('LanguageName')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class GetMediaLiveChannelResponseBodyChannelAudioSettingsAudioCodecSetting(DaraModel):
    def __init__(
        self,
        bitrate: int = None,
        profile: str = None,
        sample_rate: int = None,
    ):
        # The audio bitrate. Unit: bit/s.
        self.bitrate = bitrate
        # The audio codec profile.
        self.profile = profile
        # The audio sample rate. Unit: Hz.
        self.sample_rate = sample_rate

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bitrate is not None:
            result['Bitrate'] = self.bitrate

        if self.profile is not None:
            result['Profile'] = self.profile

        if self.sample_rate is not None:
            result['SampleRate'] = self.sample_rate

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bitrate') is not None:
            self.bitrate = m.get('Bitrate')

        if m.get('Profile') is not None:
            self.profile = m.get('Profile')

        if m.get('SampleRate') is not None:
            self.sample_rate = m.get('SampleRate')

        return self

