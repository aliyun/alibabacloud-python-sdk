# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class VideoDRMLicenseResponseBody(DaraModel):
    def __init__(
        self,
        data: str = None,
        device_info: str = None,
        states: str = None,
    ):
        # The returned DRM license.
        self.data = data
        # The information about the device from which the DRM request was initiated.
        self.device_info = device_info
        # The request state returned by the DRM server.
        self.states = states

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['data'] = self.data

        if self.device_info is not None:
            result['device_info'] = self.device_info

        if self.states is not None:
            result['states'] = self.states

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')

        if m.get('device_info') is not None:
            self.device_info = m.get('device_info')

        if m.get('states') is not None:
            self.states = m.get('states')

        return self

