# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class GetPolicyAttachmentResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetPolicyAttachmentResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # Response code.
        self.code = code
        # Response data.
        self.data = data
        # Response message.
        self.message = message
        # ID of the request
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
            temp_model = main_models.GetPolicyAttachmentResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class GetPolicyAttachmentResponseBodyData(DaraModel):
    def __init__(
        self,
        attach_resource_id: str = None,
        attach_resource_type: str = None,
        config: str = None,
        environment_id: str = None,
        gateway_id: str = None,
        policy_attachment_id: str = None,
        policy_id: str = None,
    ):
        # Attached Resource ID
        self.attach_resource_id = attach_resource_id
        # Attached resource type, HttpApi, GatewayRoute, Operation, GatewayService, GatewayServicePort, Gateway, Domain
        self.attach_resource_type = attach_resource_type
        # Policy attachment configuration
        self.config = config
        # Environment ID
        self.environment_id = environment_id
        # Gateway Instance ID
        self.gateway_id = gateway_id
        # Policy Attachment ID
        self.policy_attachment_id = policy_attachment_id
        # Policy ID
        self.policy_id = policy_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attach_resource_id is not None:
            result['attachResourceId'] = self.attach_resource_id

        if self.attach_resource_type is not None:
            result['attachResourceType'] = self.attach_resource_type

        if self.config is not None:
            result['config'] = self.config

        if self.environment_id is not None:
            result['environmentId'] = self.environment_id

        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id

        if self.policy_attachment_id is not None:
            result['policyAttachmentId'] = self.policy_attachment_id

        if self.policy_id is not None:
            result['policyId'] = self.policy_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('attachResourceId') is not None:
            self.attach_resource_id = m.get('attachResourceId')

        if m.get('attachResourceType') is not None:
            self.attach_resource_type = m.get('attachResourceType')

        if m.get('config') is not None:
            self.config = m.get('config')

        if m.get('environmentId') is not None:
            self.environment_id = m.get('environmentId')

        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')

        if m.get('policyAttachmentId') is not None:
            self.policy_attachment_id = m.get('policyAttachmentId')

        if m.get('policyId') is not None:
            self.policy_id = m.get('policyId')

        return self

