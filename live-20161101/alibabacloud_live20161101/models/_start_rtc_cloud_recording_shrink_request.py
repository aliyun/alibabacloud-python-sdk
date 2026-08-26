# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class StartRtcCloudRecordingShrinkRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        channel_id: str = None,
        max_idle_time: int = None,
        mix_layout_params_shrink: str = None,
        mix_transcode_params_shrink: str = None,
        notify_auth_key: str = None,
        notify_file_uploaded_format: List[str] = None,
        notify_url: str = None,
        record_params_shrink: str = None,
        storage_params_shrink: str = None,
        subscribe_params_shrink: str = None,
    ):
        # The ID of the app to which the channel to be recorded belongs. The app must belong to the primary account associated with the current API caller\\"s account.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The ID of the channel to be recorded. Make sure that the channel has active users when you call this operation. Otherwise, the recording task fails to be created.
        # 
        # This parameter is required.
        self.channel_id = channel_id
        # The idle timeout period. When the task remains idle for longer than MaxIdleTime, the task is automatically stopped. Unit: seconds. The value must be within [10,14400], which is a maximum of 4 hours. Default value: 300.
        self.max_idle_time = max_idle_time
        # The layout parameters. This parameter is not required in single-stream recording mode and is required in stream mixing recording mode when the output is not audio-only.
        self.mix_layout_params_shrink = mix_layout_params_shrink
        # The transcoding parameters. This parameter is not required in single-stream recording mode and is required in stream mixing recording mode.
        self.mix_transcode_params_shrink = mix_transcode_params_shrink
        # The authentication key for callback messages. Leave this parameter empty to skip authentication. If specified, the key must be 16 to 64 characters in length and consist of only uppercase and lowercase letters and digits.
        self.notify_auth_key = notify_auth_key
        # The specified formats for which a callback message is sent when the recording file upload event (RecordFileUploaded) is triggered.
        self.notify_file_uploaded_format = notify_file_uploaded_format
        # The URL for receiving callback messages. Task status messages are pushed to this URL in JSON format by using the POST method. The maximum length is 2048 characters.
        self.notify_url = notify_url
        # The recording parameters.
        # 
        # This parameter is required.
        self.record_params_shrink = record_params_shrink
        # The storage parameters.
        # 
        # This parameter is required.
        self.storage_params_shrink = storage_params_shrink
        # The subscription parameters.
        # 
        # This parameter is required.
        self.subscribe_params_shrink = subscribe_params_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id

        if self.max_idle_time is not None:
            result['MaxIdleTime'] = self.max_idle_time

        if self.mix_layout_params_shrink is not None:
            result['MixLayoutParams'] = self.mix_layout_params_shrink

        if self.mix_transcode_params_shrink is not None:
            result['MixTranscodeParams'] = self.mix_transcode_params_shrink

        if self.notify_auth_key is not None:
            result['NotifyAuthKey'] = self.notify_auth_key

        if self.notify_file_uploaded_format is not None:
            result['NotifyFileUploadedFormat'] = self.notify_file_uploaded_format

        if self.notify_url is not None:
            result['NotifyUrl'] = self.notify_url

        if self.record_params_shrink is not None:
            result['RecordParams'] = self.record_params_shrink

        if self.storage_params_shrink is not None:
            result['StorageParams'] = self.storage_params_shrink

        if self.subscribe_params_shrink is not None:
            result['SubscribeParams'] = self.subscribe_params_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')

        if m.get('MaxIdleTime') is not None:
            self.max_idle_time = m.get('MaxIdleTime')

        if m.get('MixLayoutParams') is not None:
            self.mix_layout_params_shrink = m.get('MixLayoutParams')

        if m.get('MixTranscodeParams') is not None:
            self.mix_transcode_params_shrink = m.get('MixTranscodeParams')

        if m.get('NotifyAuthKey') is not None:
            self.notify_auth_key = m.get('NotifyAuthKey')

        if m.get('NotifyFileUploadedFormat') is not None:
            self.notify_file_uploaded_format = m.get('NotifyFileUploadedFormat')

        if m.get('NotifyUrl') is not None:
            self.notify_url = m.get('NotifyUrl')

        if m.get('RecordParams') is not None:
            self.record_params_shrink = m.get('RecordParams')

        if m.get('StorageParams') is not None:
            self.storage_params_shrink = m.get('StorageParams')

        if m.get('SubscribeParams') is not None:
            self.subscribe_params_shrink = m.get('SubscribeParams')

        return self

