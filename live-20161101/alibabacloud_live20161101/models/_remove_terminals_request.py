# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class RemoveTerminalsRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        channel_id: str = None,
        terminal_ids: List[str] = None,
    ):
        # The ID of the application. You can specify only one application ID in each request.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The ID of the channel. You can specify only one channel ID in each request.
        # 
        # This parameter is required.
        self.channel_id = channel_id
        # The IDs of the users that you want to remove.
        # 
        # This parameter is required.
        self.terminal_ids = terminal_ids

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

        if self.terminal_ids is not None:
            result['TerminalIds'] = self.terminal_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')

        if m.get('TerminalIds') is not None:
            self.terminal_ids = m.get('TerminalIds')

        return self

