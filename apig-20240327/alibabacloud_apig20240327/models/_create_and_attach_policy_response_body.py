# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class CreateAndAttachPolicyResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.CreateAndAttachPolicyResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The status code returned.
        self.code = code
        # The returned data.
        self.data = data
        # The response message returned.
        self.message = message
        # The request ID, which is used to trace the call link.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.CreateAndAttachPolicyResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class CreateAndAttachPolicyResponseBodyData(DaraModel):
    def __init__(
        self,
        attachment: main_models.Attachment = None,
        policy_id: str = None,
    ):
        # The association information of the policy.
        self.attachment = attachment
        # The policy ID.
        self.policy_id = policy_id

    def validate(self):
        if self.attachment:
            self.attachment.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attachment is not None:
            result['attachment'] = self.attachment.to_map()

        if self.policy_id is not None:
            result['policyId'] = self.policy_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('attachment') is not None:
            temp_model = main_models.Attachment()
            self.attachment = temp_model.from_map(m.get('attachment'))

        if m.get('policyId') is not None:
            self.policy_id = m.get('policyId')

        return self

