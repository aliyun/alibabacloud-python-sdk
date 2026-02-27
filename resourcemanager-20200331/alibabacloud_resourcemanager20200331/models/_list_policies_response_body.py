# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_resourcemanager20200331 import models as main_models
from darabonba.model import DaraModel

class ListPoliciesResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        policies: main_models.ListPoliciesResponseBodyPolicies = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        self.policies = policies
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.policies:
            self.policies.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.policies is not None:
            result['Policies'] = self.policies.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Policies') is not None:
            temp_model = main_models.ListPoliciesResponseBodyPolicies()
            self.policies = temp_model.from_map(m.get('Policies'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

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
        update_date: str = None,
    ):
        self.attachment_count = attachment_count
        self.create_date = create_date
        self.default_version = default_version
        self.description = description
        self.policy_name = policy_name
        self.policy_type = policy_type
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

        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')

        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')

        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')

        return self

