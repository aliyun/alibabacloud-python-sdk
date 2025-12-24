# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetInstanceScreenshotResponseBody(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        request_id: str = None,
        screenshot: str = None,
    ):
        # The instance ID.
        self.instance_id = instance_id
        # The request ID.
        self.request_id = request_id
        # The Base64-encoded instance screenshot in the JPG format.
        self.screenshot = screenshot

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.screenshot is not None:
            result['Screenshot'] = self.screenshot

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Screenshot') is not None:
            self.screenshot = m.get('Screenshot')

        return self

