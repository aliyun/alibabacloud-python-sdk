# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteDeviceCertificateResponseBody(DaraModel):
    def __init__(
        self,
        device_sn: str = None,
        request_id: str = None,
    ):
        # The SN of the deleted device certificate. The SN uniquely identifies a device certificate.
        self.device_sn = device_sn
        # The common parameter. Each request has a unique ID that can be used for troubleshooting.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.device_sn is not None:
            result['DeviceSn'] = self.device_sn

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceSn') is not None:
            self.device_sn = m.get('DeviceSn')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

