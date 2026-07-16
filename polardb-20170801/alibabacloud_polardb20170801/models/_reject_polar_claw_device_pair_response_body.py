# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RejectPolarClawDevicePairResponseBody(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        code: int = None,
        device_id: str = None,
        message: str = None,
        pair_request_id: str = None,
        request_id: str = None,
    ):
        # The application ID.
        self.application_id = application_id
        # The response status code.
        self.code = code
        # The unique device ID.
        self.device_id = device_id
        # The returned message.
        self.message = message
        # The pairing request ID.
        self.pair_request_id = pair_request_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.code is not None:
            result['Code'] = self.code

        if self.device_id is not None:
            result['DeviceId'] = self.device_id

        if self.message is not None:
            result['Message'] = self.message

        if self.pair_request_id is not None:
            result['PairRequestId'] = self.pair_request_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PairRequestId') is not None:
            self.pair_request_id = m.get('PairRequestId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

