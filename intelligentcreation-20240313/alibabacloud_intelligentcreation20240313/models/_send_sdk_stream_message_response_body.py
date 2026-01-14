# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SendSdkStreamMessageResponseBody(DaraModel):
    def __init__(
        self,
        common_stream_message: str = None,
    ):
        self.common_stream_message = common_stream_message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.common_stream_message is not None:
            result['commonStreamMessage'] = self.common_stream_message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonStreamMessage') is not None:
            self.common_stream_message = m.get('commonStreamMessage')

        return self

