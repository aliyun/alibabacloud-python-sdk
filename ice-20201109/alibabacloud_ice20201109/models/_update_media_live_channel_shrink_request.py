# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateMediaLiveChannelShrinkRequest(DaraModel):
    def __init__(
        self,
        audio_settings_shrink: str = None,
        channel_id: str = None,
        input_attachments_shrink: str = None,
        name: str = None,
        output_groups_shrink: str = None,
        video_settings_shrink: str = None,
    ):
        # The audio settings.
        self.audio_settings_shrink = audio_settings_shrink
        # The ID of the channel.
        # 
        # This parameter is required.
        self.channel_id = channel_id
        # The inputs associated with the channel.
        # 
        # This parameter is required.
        self.input_attachments_shrink = input_attachments_shrink
        # The name of the channel. Letters, digits, hyphens (-), and underscores (_) are supported. It can be up to 64 characters in length.
        # 
        # This parameter is required.
        self.name = name
        # The output groups.
        # 
        # This parameter is required.
        self.output_groups_shrink = output_groups_shrink
        # The video settings.
        self.video_settings_shrink = video_settings_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audio_settings_shrink is not None:
            result['AudioSettings'] = self.audio_settings_shrink

        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id

        if self.input_attachments_shrink is not None:
            result['InputAttachments'] = self.input_attachments_shrink

        if self.name is not None:
            result['Name'] = self.name

        if self.output_groups_shrink is not None:
            result['OutputGroups'] = self.output_groups_shrink

        if self.video_settings_shrink is not None:
            result['VideoSettings'] = self.video_settings_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AudioSettings') is not None:
            self.audio_settings_shrink = m.get('AudioSettings')

        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')

        if m.get('InputAttachments') is not None:
            self.input_attachments_shrink = m.get('InputAttachments')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OutputGroups') is not None:
            self.output_groups_shrink = m.get('OutputGroups')

        if m.get('VideoSettings') is not None:
            self.video_settings_shrink = m.get('VideoSettings')

        return self

