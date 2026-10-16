# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_resourcemanager20200331 import models as main_models
from darabonba.model import DaraModel

class CreateControlPolicyResponseBody(DaraModel):
    def __init__(
        self,
        control_policy: main_models.CreateControlPolicyResponseBodyControlPolicy = None,
        request_id: str = None,
    ):
        # The details of the control policy.
        self.control_policy = control_policy
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.control_policy:
            self.control_policy.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.control_policy is not None:
            result['ControlPolicy'] = self.control_policy.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ControlPolicy') is not None:
            temp_model = main_models.CreateControlPolicyResponseBodyControlPolicy()
            self.control_policy = temp_model.from_map(m.get('ControlPolicy'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CreateControlPolicyResponseBodyControlPolicy(DaraModel):
    def __init__(
        self,
        attachment_count: str = None,
        create_date: str = None,
        description: str = None,
        effect_scope: str = None,
        policy_id: str = None,
        policy_name: str = None,
        policy_type: str = None,
        update_date: str = None,
    ):
        # The number of times the control policy is referenced.
        self.attachment_count = attachment_count
        # The time when the control policy was created. The time is displayed in UTC in RFC 3339 format, with Z indicating UTC.
        self.create_date = create_date
        # The description of the control policy.
        self.description = description
        # The effective scope of the control policy.
        # 
        # Valid values: RAM, which indicates that the control policy takes effect only for Resource Access Management (RAM) users or RAM roles.
        self.effect_scope = effect_scope
        # The ID of the control policy.
        self.policy_id = policy_id
        # The Policy Name of the control policy.
        self.policy_name = policy_name
        # The type of the control policy. Valid values:
        # 
        # - System: system control policy.
        # - Custom: custom control policy.
        self.policy_type = policy_type
        # The time when the control policy was last updated. The time is displayed in UTC in RFC 3339 format, with Z indicating UTC.
        self.update_date = update_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attachment_count is not None:
            result['AttachmentCount'] = self.attachment_count

        if self.create_date is not None:
            result['CreateDate'] = self.create_date

        if self.description is not None:
            result['Description'] = self.description

        if self.effect_scope is not None:
            result['EffectScope'] = self.effect_scope

        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id

        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name

        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type

        if self.update_date is not None:
            result['UpdateDate'] = self.update_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttachmentCount') is not None:
            self.attachment_count = m.get('AttachmentCount')

        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EffectScope') is not None:
            self.effect_scope = m.get('EffectScope')

        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')

        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')

        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')

        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')

        return self

