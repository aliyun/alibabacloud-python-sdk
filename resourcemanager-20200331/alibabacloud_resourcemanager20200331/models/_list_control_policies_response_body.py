# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_resourcemanager20200331 import models as main_models
from darabonba.model import DaraModel

class ListControlPoliciesResponseBody(DaraModel):
    def __init__(
        self,
        control_policies: main_models.ListControlPoliciesResponseBodyControlPolicies = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.control_policies = control_policies
        # The number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The number of access control policies.
        self.total_count = total_count

    def validate(self):
        if self.control_policies:
            self.control_policies.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.control_policies is not None:
            result['ControlPolicies'] = self.control_policies.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ControlPolicies') is not None:
            temp_model = main_models.ListControlPoliciesResponseBodyControlPolicies()
            self.control_policies = temp_model.from_map(m.get('ControlPolicies'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListControlPoliciesResponseBodyControlPolicies(DaraModel):
    def __init__(
        self,
        control_policy: List[main_models.ListControlPoliciesResponseBodyControlPoliciesControlPolicy] = None,
    ):
        self.control_policy = control_policy

    def validate(self):
        if self.control_policy:
            for v1 in self.control_policy:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ControlPolicy'] = []
        if self.control_policy is not None:
            for k1 in self.control_policy:
                result['ControlPolicy'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.control_policy = []
        if m.get('ControlPolicy') is not None:
            for k1 in m.get('ControlPolicy'):
                temp_model = main_models.ListControlPoliciesResponseBodyControlPoliciesControlPolicy()
                self.control_policy.append(temp_model.from_map(k1))

        return self

class ListControlPoliciesResponseBodyControlPoliciesControlPolicy(DaraModel):
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
        self.attachment_count = attachment_count
        self.create_date = create_date
        self.description = description
        self.effect_scope = effect_scope
        self.policy_id = policy_id
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

