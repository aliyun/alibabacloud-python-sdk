# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_resourcedirectorymaster20220419 import models as main_models
from darabonba.model import DaraModel

class GetControlPolicyResponseBody(DaraModel):
    def __init__(
        self,
        control_policy: main_models.GetControlPolicyResponseBodyControlPolicy = None,
        request_id: str = None,
    ):
        # The details of the access control policy.
        self.control_policy = control_policy
        # The ID of the request.
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
            temp_model = main_models.GetControlPolicyResponseBodyControlPolicy()
            self.control_policy = temp_model.from_map(m.get('ControlPolicy'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetControlPolicyResponseBodyControlPolicy(DaraModel):
    def __init__(
        self,
        attachment_count: str = None,
        create_date: str = None,
        description: str = None,
        effect_scope: str = None,
        policy_document: str = None,
        policy_id: str = None,
        policy_name: str = None,
        policy_type: str = None,
        update_date: str = None,
    ):
        # The number of times that the access control policy is referenced.
        self.attachment_count = attachment_count
        # The time when the access control policy was created.
        self.create_date = create_date
        # The description of the access control policy.
        self.description = description
        # The effective scope of the access control policy. Valid values:
        # 
        # *   All: The access control policy is in effect for Alibaba Cloud accounts, RAM users, and RAM roles.
        # *   RAM: The access control policy is in effect only for RAM users and RAM roles.
        self.effect_scope = effect_scope
        # The document of the access control policy.
        self.policy_document = policy_document
        # The ID of the access control policy.
        self.policy_id = policy_id
        # The name of the access control policy.
        self.policy_name = policy_name
        # The type of the access control policy. Valid values:
        # 
        # *   System: system access control policy
        # *   Custom: custom access control policy
        self.policy_type = policy_type
        # The time when the access control policy was updated.
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

        if self.policy_document is not None:
            result['PolicyDocument'] = self.policy_document

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

        if m.get('PolicyDocument') is not None:
            self.policy_document = m.get('PolicyDocument')

        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')

        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')

        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')

        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')

        return self

