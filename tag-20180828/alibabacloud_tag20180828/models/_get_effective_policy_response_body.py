# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_tag20180828 import models as main_models
from darabonba.model import DaraModel

class GetEffectivePolicyResponseBody(DaraModel):
    def __init__(
        self,
        effective_policy: str = None,
        policy_attachments: List[main_models.GetEffectivePolicyResponseBodyPolicyAttachments] = None,
        request_id: str = None,
    ):
        # The effective policy.
        self.effective_policy = effective_policy
        self.policy_attachments = policy_attachments
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.policy_attachments:
            for v1 in self.policy_attachments:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.effective_policy is not None:
            result['EffectivePolicy'] = self.effective_policy

        result['PolicyAttachments'] = []
        if self.policy_attachments is not None:
            for k1 in self.policy_attachments:
                result['PolicyAttachments'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EffectivePolicy') is not None:
            self.effective_policy = m.get('EffectivePolicy')

        self.policy_attachments = []
        if m.get('PolicyAttachments') is not None:
            for k1 in m.get('PolicyAttachments'):
                temp_model = main_models.GetEffectivePolicyResponseBodyPolicyAttachments()
                self.policy_attachments.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetEffectivePolicyResponseBodyPolicyAttachments(DaraModel):
    def __init__(
        self,
        policy_list: List[main_models.GetEffectivePolicyResponseBodyPolicyAttachmentsPolicyList] = None,
        policy_type: str = None,
        tag_key: str = None,
    ):
        self.policy_list = policy_list
        self.policy_type = policy_type
        self.tag_key = tag_key

    def validate(self):
        if self.policy_list:
            for v1 in self.policy_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['PolicyList'] = []
        if self.policy_list is not None:
            for k1 in self.policy_list:
                result['PolicyList'].append(k1.to_map() if k1 else None)

        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type

        if self.tag_key is not None:
            result['TagKey'] = self.tag_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.policy_list = []
        if m.get('PolicyList') is not None:
            for k1 in m.get('PolicyList'):
                temp_model = main_models.GetEffectivePolicyResponseBodyPolicyAttachmentsPolicyList()
                self.policy_list.append(temp_model.from_map(k1))

        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')

        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        return self

class GetEffectivePolicyResponseBodyPolicyAttachmentsPolicyList(DaraModel):
    def __init__(
        self,
        attach_seq: int = None,
        attach_time: str = None,
        policy_id: str = None,
        policy_name: str = None,
        target_id: str = None,
        target_type: str = None,
    ):
        self.attach_seq = attach_seq
        self.attach_time = attach_time
        self.policy_id = policy_id
        self.policy_name = policy_name
        self.target_id = target_id
        self.target_type = target_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attach_seq is not None:
            result['AttachSeq'] = self.attach_seq

        if self.attach_time is not None:
            result['AttachTime'] = self.attach_time

        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id

        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name

        if self.target_id is not None:
            result['TargetId'] = self.target_id

        if self.target_type is not None:
            result['TargetType'] = self.target_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttachSeq') is not None:
            self.attach_seq = m.get('AttachSeq')

        if m.get('AttachTime') is not None:
            self.attach_time = m.get('AttachTime')

        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')

        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')

        if m.get('TargetId') is not None:
            self.target_id = m.get('TargetId')

        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')

        return self

