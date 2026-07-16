# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class EnablePolarClawChannelRequest(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        channel_id: str = None,
        restart: bool = None,
    ):
        # The ID of the application.
        # 
        # This parameter is required.
        self.application_id = application_id
        # The ID of the channel.
        # 
        # This parameter is required.
        self.channel_id = channel_id
        # Specifies whether to restart the gateway after the channel is enabled. The default value is `true`.
        self.restart = restart

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id

        if self.restart is not None:
            result['Restart'] = self.restart

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')

        if m.get('Restart') is not None:
            self.restart = m.get('Restart')

        return self

