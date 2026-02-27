# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_resourcemanager20200331 import models as main_models
from darabonba.model import DaraModel

class ListControlPolicyAttachmentsForTargetResponseBody(DaraModel):
    def __init__(
        self,
        control_policy_attachments: main_models.ListControlPolicyAttachmentsForTargetResponseBodyControlPolicyAttachments = None,
        request_id: str = None,
    ):
        self.control_policy_attachments = control_policy_attachments
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.control_policy_attachments:
            self.control_policy_attachments.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.control_policy_attachments is not None:
            result['ControlPolicyAttachments'] = self.control_policy_attachments.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ControlPolicyAttachments') is not None:
            temp_model = main_models.ListControlPolicyAttachmentsForTargetResponseBodyControlPolicyAttachments()
            self.control_policy_attachments = temp_model.from_map(m.get('ControlPolicyAttachments'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListControlPolicyAttachmentsForTargetResponseBodyControlPolicyAttachments(DaraModel):
    def __init__(
        self,
        control_policy_attachment: List[main_models.ListControlPolicyAttachmentsForTargetResponseBodyControlPolicyAttachmentsControlPolicyAttachment] = None,
    ):
        self.control_policy_attachment = control_policy_attachment

    def validate(self):
        if self.control_policy_attachment:
            for v1 in self.control_policy_attachment:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ControlPolicyAttachment'] = []
        if self.control_policy_attachment is not None:
            for k1 in self.control_policy_attachment:
                result['ControlPolicyAttachment'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.control_policy_attachment = []
        if m.get('ControlPolicyAttachment') is not None:
            for k1 in m.get('ControlPolicyAttachment'):
                temp_model = main_models.ListControlPolicyAttachmentsForTargetResponseBodyControlPolicyAttachmentsControlPolicyAttachment()
                self.control_policy_attachment.append(temp_model.from_map(k1))

        return self

class ListControlPolicyAttachmentsForTargetResponseBodyControlPolicyAttachmentsControlPolicyAttachment(DaraModel):
    def __init__(
        self,
        attach_date: str = None,
        description: str = None,
        effect_scope: str = None,
        policy_id: str = None,
        policy_name: str = None,
        policy_type: str = None,
    ):
        self.attach_date = attach_date
        self.description = description
        self.effect_scope = effect_scope
        self.policy_id = policy_id
        self.policy_name = policy_name
        self.policy_type = policy_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attach_date is not None:
            result['AttachDate'] = self.attach_date

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttachDate') is not None:
            self.attach_date = m.get('AttachDate')

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

        return self

