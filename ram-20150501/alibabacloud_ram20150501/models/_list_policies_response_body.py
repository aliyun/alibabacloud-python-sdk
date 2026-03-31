# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ram20150501 import models as main_models
from darabonba.model import DaraModel

class ListPoliciesResponseBody(DaraModel):
    def __init__(
        self,
        is_truncated: bool = None,
        marker: str = None,
        policies: main_models.ListPoliciesResponseBodyPolicies = None,
        request_id: str = None,
    ):
        # Indicates whether the response is truncated.
        self.is_truncated = is_truncated
        # The marker. This parameter is returned only if the value of `IsTruncated` is `true`. If the parameter is returned, you can call this operation again and set `Marker` to obtain the truncated part.``
        self.marker = marker
        self.policies = policies
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.policies:
            self.policies.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.is_truncated is not None:
            result['IsTruncated'] = self.is_truncated

        if self.marker is not None:
            result['Marker'] = self.marker

        if self.policies is not None:
            result['Policies'] = self.policies.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsTruncated') is not None:
            self.is_truncated = m.get('IsTruncated')

        if m.get('Marker') is not None:
            self.marker = m.get('Marker')

        if m.get('Policies') is not None:
            temp_model = main_models.ListPoliciesResponseBodyPolicies()
            self.policies = temp_model.from_map(m.get('Policies'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListPoliciesResponseBodyPolicies(DaraModel):
    def __init__(
        self,
        policy: List[main_models.ListPoliciesResponseBodyPoliciesPolicy] = None,
    ):
        self.policy = policy

    def validate(self):
        if self.policy:
            for v1 in self.policy:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Policy'] = []
        if self.policy is not None:
            for k1 in self.policy:
                result['Policy'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.policy = []
        if m.get('Policy') is not None:
            for k1 in m.get('Policy'):
                temp_model = main_models.ListPoliciesResponseBodyPoliciesPolicy()
                self.policy.append(temp_model.from_map(k1))

        return self

class ListPoliciesResponseBodyPoliciesPolicy(DaraModel):
    def __init__(
        self,
        attachment_count: int = None,
        create_date: str = None,
        default_version: str = None,
        description: str = None,
        policy_name: str = None,
        policy_type: str = None,
        tags: main_models.ListPoliciesResponseBodyPoliciesPolicyTags = None,
        update_date: str = None,
    ):
        self.attachment_count = attachment_count
        self.create_date = create_date
        self.default_version = default_version
        self.description = description
        self.policy_name = policy_name
        self.policy_type = policy_type
        self.tags = tags
        self.update_date = update_date

    def validate(self):
        if self.tags:
            self.tags.validate()

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

        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name

        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type

        if self.tags is not None:
            result['Tags'] = self.tags.to_map()

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

        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')

        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')

        if m.get('Tags') is not None:
            temp_model = main_models.ListPoliciesResponseBodyPoliciesPolicyTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')

        return self

class ListPoliciesResponseBodyPoliciesPolicyTags(DaraModel):
    def __init__(
        self,
        tag: List[main_models.ListPoliciesResponseBodyPoliciesPolicyTagsTag] = None,
    ):
        self.tag = tag

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.ListPoliciesResponseBodyPoliciesPolicyTagsTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class ListPoliciesResponseBodyPoliciesPolicyTagsTag(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        self.tag_key = tag_key
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key

        if self.tag_value is not None:
            result['TagValue'] = self.tag_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')

        return self

