# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_resourcemanager20200331 import models as main_models
from darabonba.model import DaraModel

class CreatePolicyVersionResponseBody(DaraModel):
    def __init__(
        self,
        policy_version: main_models.CreatePolicyVersionResponseBodyPolicyVersion = None,
        request_id: str = None,
    ):
        # The information about the policy version.
        self.policy_version = policy_version
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.policy_version:
            self.policy_version.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.policy_version is not None:
            result['PolicyVersion'] = self.policy_version.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyVersion') is not None:
            temp_model = main_models.CreatePolicyVersionResponseBodyPolicyVersion()
            self.policy_version = temp_model.from_map(m.get('PolicyVersion'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CreatePolicyVersionResponseBodyPolicyVersion(DaraModel):
    def __init__(
        self,
        create_date: str = None,
        is_default_version: bool = None,
        version_id: str = None,
    ):
        # The time when the policy version was created.
        self.create_date = create_date
        # Indicates whether the policy version is the default version.
        self.is_default_version = is_default_version
        # The ID of the policy version.
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

        if self.version_id is not None:
            result['VersionId'] = self.version_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')

        if m.get('IsDefaultVersion') is not None:
            self.is_default_version = m.get('IsDefaultVersion')

        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')

        return self

