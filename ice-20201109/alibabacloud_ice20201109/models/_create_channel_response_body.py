# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class CreateChannelResponseBody(DaraModel):
    def __init__(
        self,
        channel: main_models.ChannelAssemblyChannel = None,
        request_id: str = None,
    ):
        # The channel information.
        self.channel = channel
        # **Request ID**
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
            temp_model = main_models.ChannelAssemblyChannel()
            self.channel = temp_model.from_map(m.get('Channel'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

