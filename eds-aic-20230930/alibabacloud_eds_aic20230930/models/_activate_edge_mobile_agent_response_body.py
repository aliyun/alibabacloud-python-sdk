# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_eds_aic20230930 import models as main_models
from darabonba.model import DaraModel

class ActivateEdgeMobileAgentResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ActivateEdgeMobileAgentResponseBodyData = None,
        request_id: str = None,
    ):
        # The response data object.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.ActivateEdgeMobileAgentResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self



class ActivateEdgeMobileAgentResponseBodyData(DaraModel):
    def __init__(
        self,
        auth_token: str = None,
        device_id: str = None,
        idempotent: bool = None,
        instance_id: str = None,
    ):
        # The assigned API key. The plaintext value is returned only upon the first activation.
        self.auth_token = auth_token
        # The device ID.
        self.device_id = device_id
        # Indicates whether the request is an idempotent duplicate request.
        self.idempotent = idempotent
        # The EdgeMobile instance ID.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_token is not None:
            result['AuthToken'] = self.auth_token

        if self.device_id is not None:
            result['DeviceId'] = self.device_id

        if self.idempotent is not None:
            result['Idempotent'] = self.idempotent

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthToken') is not None:
            self.auth_token = m.get('AuthToken')

        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')

        if m.get('Idempotent') is not None:
            self.idempotent = m.get('Idempotent')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

