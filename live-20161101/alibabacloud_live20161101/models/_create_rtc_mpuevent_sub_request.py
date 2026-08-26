# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateRtcMPUEventSubRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        callback_url: str = None,
        channel_ids: str = None,
    ):
        # The ID of the application to subscribe to. You can view your application IDs by navigating to **ApsaraVideo Live > Live+ > ApsaraVideo Real-time Communication > Application Management**. If no application exists, create one by clicking **Create Application**.
        # > The application ID consists of uppercase and lowercase letters, digits, underscores, and hyphens (-), with a maximum of 64 characters.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The callback URL. For the URL format, refer to the callback content specifications below.
        # > The callback URL protocol must be HTTP or HTTPS. The URL can contain only the following characters: a-z, A-Z, 0-9, -, _, ?, %, =, #, ., /, and +. The URL cannot exceed 2083 characters.
        # 
        # This parameter is required.
        self.callback_url = callback_url
        # The channel IDs of the stream mixing tasks for which you want to receive callbacks. You can specify multiple channel IDs separated by commas (,).
        # >- If you leave this parameter empty, callbacks for all stream mixing and relaying tasks under the specified AppId are received by default.
        # - When specifying multiple channel IDs, do not include duplicates. You can specify up to 20 channel IDs at a time.
        # - Each channel ID consists of uppercase and lowercase letters, digits, underscores, and hyphens (-), with a maximum of 64 characters.
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

