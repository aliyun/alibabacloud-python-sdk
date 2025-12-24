# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateRtcMPUEventSubRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        callback_url: str = None,
        channel_ids: str = None,
    ):
        # The ID of the application.
        # 
        # >  The ID can be up to 64 characters in length and can contain letters, digits, underscores (_), and hyphens (-).
        # 
        # This parameter is required.
        self.app_id = app_id
        # The callback URL.
        # 
        # >  You can use headers such as HTTP and HTTPS in callback URLs. The URL can be up to 2,083 characters and contain letters, digits, and the following special characters: - _ ? % = # . / +
        self.callback_url = callback_url
        # The ID of the channel to which you want to send mixed-stream relay event callbacks. Separate multiple channel IDs with commas (,).
        # 
        # > 
        # 
        # *   If you leave this parameter empty, you are subscribed to all mixed-stream relay events submitted in the application.
        # 
        # *   You cannot specify duplicate channel IDs. You can specify up to 20 channel IDs in each call.
        # *   The ID can be up to 64 characters in length and contain letters, digits, underscores (_), and hyphens (-).
        self.channel_ids = channel_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.callback_url is not None:
            result['CallbackUrl'] = self.callback_url

        if self.channel_ids is not None:
            result['ChannelIds'] = self.channel_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('CallbackUrl') is not None:
            self.callback_url = m.get('CallbackUrl')

        if m.get('ChannelIds') is not None:
            self.channel_ids = m.get('ChannelIds')

        return self

