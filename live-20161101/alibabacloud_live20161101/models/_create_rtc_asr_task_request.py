# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateRtcAsrTaskRequest(DaraModel):
    def __init__(
        self,
        auth_key: str = None,
        auto_terminate_delay: int = None,
        auto_terminate_enabled: bool = None,
        callback_url: str = None,
        channel_id: str = None,
        language: str = None,
        mode: str = None,
        owner_id: int = None,
        region_id: str = None,
        report_interval: int = None,
        rtc_user_id: str = None,
        sdkapp_id: str = None,
        stream_url: str = None,
        target_languages: str = None,
        translate_enabled: bool = None,
    ):
        # The AuthKey that is used to generate the MD5 signature in callbacks.
        self.auth_key = auth_key
        # The maximum latency at which the task is automatically stopped. Unit: seconds. Valid values: 1 to 10.
        self.auto_terminate_delay = auto_terminate_delay
        # Specifies whether to automatically stop the task when the latency exceeds the specified limit. Default value: false.
        self.auto_terminate_enabled = auto_terminate_enabled
        # The callback URL.
        # 
        # This parameter is required.
        self.callback_url = callback_url
        # The ID of the channel.
        # 
        # >  This parameter is required and takes effect only if you set the Mode parameter to rtc.
        self.channel_id = channel_id
        # The source language of the audio. Valid values:
        # 
        # *   ja: Japanese
        # *   yue: Cantonese
        # *   fspk: mixed Mandarin and English
        # *   en: English
        # *   cn: Mandarin
        # 
        # This parameter is required.
        self.language = language
        # The type of the stream. Valid values: live and rtc. The value live specifies a regular live stream, such as a Real-Time Messaging Protocol (RTMP) stream.
        # 
        # This parameter is required.
        self.mode = mode
        self.owner_id = owner_id
        self.region_id = region_id
        # The interval at which callbacks are returned. Unit: milliseconds. Valid values: -1 and 0 to 500.
        # 
        # *   \\-1: accepts callbacks only for whole sentences, but not for incomplete sentences.
        # *   0 or an empty value: returns callbacks in real time.
        # *   A value that is greater than 0 and less than or equal to 500: returns callbacks at the specified interval.
        self.report_interval = report_interval
        # The ID of the user who ingests the stream.
        # 
        # >  This parameter is required and takes effect only if you set the Mode parameter to rtc. You can specify only one user ID.
        self.rtc_user_id = rtc_user_id
        # The ID of the ApsaraVideo Real-time Communication (ARTC) application.
        # 
        # >  This parameter is required and takes effect only if you set the Mode parameter to rtc.
        self.sdkapp_id = sdkapp_id
        # The URL of the live stream.
        # 
        # >  This parameter is required and takes effect only if you set the Mode parameter to live.
        self.stream_url = stream_url
        # The language into which the subtitles are translated. Valid values:
        # 
        # *   cn: Chinese
        # *   en: English
        # *   ja: Japanese
        self.target_languages = target_languages
        # Specifies whether to enable the translation feature.
        self.translate_enabled = translate_enabled

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_key is not None:
            result['AuthKey'] = self.auth_key

        if self.auto_terminate_delay is not None:
            result['AutoTerminateDelay'] = self.auto_terminate_delay

        if self.auto_terminate_enabled is not None:
            result['AutoTerminateEnabled'] = self.auto_terminate_enabled

        if self.callback_url is not None:
            result['CallbackURL'] = self.callback_url

        if self.channel_id is not None:
            result['ChannelID'] = self.channel_id

        if self.language is not None:
            result['Language'] = self.language

        if self.mode is not None:
            result['Mode'] = self.mode

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.report_interval is not None:
            result['ReportInterval'] = self.report_interval

        if self.rtc_user_id is not None:
            result['RtcUserId'] = self.rtc_user_id

        if self.sdkapp_id is not None:
            result['SDKAppID'] = self.sdkapp_id

        if self.stream_url is not None:
            result['StreamURL'] = self.stream_url

        if self.target_languages is not None:
            result['TargetLanguages'] = self.target_languages

        if self.translate_enabled is not None:
            result['TranslateEnabled'] = self.translate_enabled

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthKey') is not None:
            self.auth_key = m.get('AuthKey')

        if m.get('AutoTerminateDelay') is not None:
            self.auto_terminate_delay = m.get('AutoTerminateDelay')

        if m.get('AutoTerminateEnabled') is not None:
            self.auto_terminate_enabled = m.get('AutoTerminateEnabled')

        if m.get('CallbackURL') is not None:
            self.callback_url = m.get('CallbackURL')

        if m.get('ChannelID') is not None:
            self.channel_id = m.get('ChannelID')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ReportInterval') is not None:
            self.report_interval = m.get('ReportInterval')

        if m.get('RtcUserId') is not None:
            self.rtc_user_id = m.get('RtcUserId')

        if m.get('SDKAppID') is not None:
            self.sdkapp_id = m.get('SDKAppID')

        if m.get('StreamURL') is not None:
            self.stream_url = m.get('StreamURL')

        if m.get('TargetLanguages') is not None:
            self.target_languages = m.get('TargetLanguages')

        if m.get('TranslateEnabled') is not None:
            self.translate_enabled = m.get('TranslateEnabled')

        return self

