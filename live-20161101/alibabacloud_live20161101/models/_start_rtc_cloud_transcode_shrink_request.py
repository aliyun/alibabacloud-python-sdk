# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class StartRtcCloudTranscodeShrinkRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        channel_id: str = None,
        input_param_shrink: str = None,
        max_idle_time: int = None,
        output_params_shrink: str = None,
    ):
        # The ID of the application to which the channel belongs. The ID can contain uppercase letters, lowercase letters, digits, underscores (_), and hyphens (-). The maximum length is 64 characters.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The ID of the channel to which the user to be transcoded belongs. The ID can contain uppercase letters, lowercase letters, digits, underscores (_), and hyphens (-). The maximum length is 64 characters.
        # 
        # This parameter is required.
        self.channel_id = channel_id
        # The parameters for the input stream subscription.
        # 
        # This parameter is required.
        self.input_param_shrink = input_param_shrink
        # The idle timeout period in seconds. If a task cannot subscribe to the specified streamer\\"s stream and remains idle for longer than this period, the task automatically stops. The value must be an integer from 10 to 14,400. The default value is 300.
        self.max_idle_time = max_idle_time
        # The parameters for the transcoded output.
        # 
        # This parameter is required.
        self.output_params_shrink = output_params_shrink

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

        if self.input_param_shrink is not None:
            result['InputParam'] = self.input_param_shrink

        if self.max_idle_time is not None:
            result['MaxIdleTime'] = self.max_idle_time

        if self.output_params_shrink is not None:
            result['OutputParams'] = self.output_params_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')

        if m.get('InputParam') is not None:
            self.input_param_shrink = m.get('InputParam')

        if m.get('MaxIdleTime') is not None:
            self.max_idle_time = m.get('MaxIdleTime')

        if m.get('OutputParams') is not None:
            self.output_params_shrink = m.get('OutputParams')

        return self

