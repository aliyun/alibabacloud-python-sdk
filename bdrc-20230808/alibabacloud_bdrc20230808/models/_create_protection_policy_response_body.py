# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_bdrc20230808 import models as main_models
from darabonba.model import DaraModel

class CreateProtectionPolicyResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.CreateProtectionPolicyResponseBodyData = None,
        request_id: str = None,
    ):
        # The data returned.
        self.data = data
        # The unique ID of the request.
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
            temp_model = main_models.CreateProtectionPolicyResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CreateProtectionPolicyResponseBodyData(DaraModel):
    def __init__(
        self,
        protection_policy_id: str = None,
    ):
        # The ID of the protection policy.
        self.protection_policy_id = protection_policy_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.protection_policy_id is not None:
            result['ProtectionPolicyId'] = self.protection_policy_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProtectionPolicyId') is not None:
            self.protection_policy_id = m.get('ProtectionPolicyId')

        return self

