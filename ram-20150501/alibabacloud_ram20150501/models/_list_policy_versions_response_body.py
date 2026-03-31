# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ram20150501 import models as main_models
from darabonba.model import DaraModel

class ListPolicyVersionsResponseBody(DaraModel):
    def __init__(
        self,
        policy_versions: main_models.ListPolicyVersionsResponseBodyPolicyVersions = None,
        request_id: str = None,
    ):
        self.policy_versions = policy_versions
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.policy_versions:
            self.policy_versions.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.policy_versions is not None:
            result['PolicyVersions'] = self.policy_versions.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyVersions') is not None:
            temp_model = main_models.ListPolicyVersionsResponseBodyPolicyVersions()
            self.policy_versions = temp_model.from_map(m.get('PolicyVersions'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListPolicyVersionsResponseBodyPolicyVersions(DaraModel):
    def __init__(
        self,
        policy_version: List[main_models.ListPolicyVersionsResponseBodyPolicyVersionsPolicyVersion] = None,
    ):
        self.policy_version = policy_version

    def validate(self):
        if self.policy_version:
            for v1 in self.policy_version:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['PolicyVersion'] = []
        if self.policy_version is not None:
            for k1 in self.policy_version:
                result['PolicyVersion'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.policy_version = []
        if m.get('PolicyVersion') is not None:
            for k1 in m.get('PolicyVersion'):
                temp_model = main_models.ListPolicyVersionsResponseBodyPolicyVersionsPolicyVersion()
                self.policy_version.append(temp_model.from_map(k1))

        return self

class ListPolicyVersionsResponseBodyPolicyVersionsPolicyVersion(DaraModel):
    def __init__(
        self,
        create_date: str = None,
        is_default_version: bool = None,
        policy_document: str = None,
        version_id: str = None,
    ):
        self.create_date = create_date
        self.is_default_version = is_default_version
        self.policy_document = policy_document
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

