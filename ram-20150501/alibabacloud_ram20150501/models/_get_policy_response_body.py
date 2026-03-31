# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ram20150501 import models as main_models
from darabonba.model import DaraModel

class GetPolicyResponseBody(DaraModel):
    def __init__(
        self,
        default_policy_version: main_models.GetPolicyResponseBodyDefaultPolicyVersion = None,
        policy: main_models.GetPolicyResponseBodyPolicy = None,
        request_id: str = None,
    ):
        # The information about the default policy version.
        self.default_policy_version = default_policy_version
        # The basic information about the policy.
        self.policy = policy
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.default_policy_version:
            self.default_policy_version.validate()
        if self.policy:
            self.policy.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.default_policy_version is not None:
            result['DefaultPolicyVersion'] = self.default_policy_version.to_map()

        if self.policy is not None:
            result['Policy'] = self.policy.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultPolicyVersion') is not None:
            temp_model = main_models.GetPolicyResponseBodyDefaultPolicyVersion()
            self.default_policy_version = temp_model.from_map(m.get('DefaultPolicyVersion'))

        if m.get('Policy') is not None:
            temp_model = main_models.GetPolicyResponseBodyPolicy()
            self.policy = temp_model.from_map(m.get('Policy'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetPolicyResponseBodyPolicy(DaraModel):
    def __init__(
        self,
        attachment_count: int = None,
        create_date: str = None,
        default_version: str = None,
        description: str = None,
        policy_document: str = None,
        policy_name: str = None,
        policy_type: str = None,
        update_date: str = None,
    ):
        # The number of references to the policy.
        self.attachment_count = attachment_count
        # The time when the policy was created.
        self.create_date = create_date
        # The default version of the policy.
        self.default_version = default_version
        # The description of the policy.
        self.description = description
        # This parameter is deprecated.
        self.policy_document = policy_document
        # The name of the policy.
        self.policy_name = policy_name
        # The type of the policy.
        self.policy_type = policy_type
        # The time when the policy was modified.
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

        if self.default_version is not None:
            result['DefaultVersion'] = self.default_version

        if self.description is not None:
            result['Description'] = self.description

        if self.policy_document is not None:
            result['PolicyDocument'] = self.policy_document

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

        if m.get('DefaultVersion') is not None:
            self.default_version = m.get('DefaultVersion')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('PolicyDocument') is not None:
            self.policy_document = m.get('PolicyDocument')

        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')

        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')

        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')

        return self

class GetPolicyResponseBodyDefaultPolicyVersion(DaraModel):
    def __init__(
        self,
        create_date: str = None,
        is_default_version: bool = None,
        policy_document: str = None,
        version_id: str = None,
    ):
        # The time when the default policy version was created.
        self.create_date = create_date
        # An attribute in the `DefaultPolicyVersion` parameter. The value of the `IsDefaultVersion` parameter is `true`.
        self.is_default_version = is_default_version
        # The document of the policy.
        self.policy_document = policy_document
        # The ID of the default policy version.
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_date is not None:
            result['CreateDate'] = self.create_date

        if self.is_default_version is not None:
            result['IsDefaultVersion'] = self.is_default_version

        if self.policy_document is not None:
            result['PolicyDocument'] = self.policy_document

        if self.version_id is not None:
            result['VersionId'] = self.version_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')

        if m.get('IsDefaultVersion') is not None:
            self.is_default_version = m.get('IsDefaultVersion')

        if m.get('PolicyDocument') is not None:
            self.policy_document = m.get('PolicyDocument')

        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')

        return self

