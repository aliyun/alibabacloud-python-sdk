# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class ListAbacPoliciesResponseBody(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        policy_list: List[main_models.ListAbacPoliciesResponseBodyPolicyList] = None,
        request_id: str = None,
        success: bool = None,
        tid: int = None,
        total_count: int = None,
    ):
        # The error code that is returned if the request failed.
        self.error_code = error_code
        # The error message that is returned if the request failed.
        self.error_message = error_message
        # The details of the permission policies.
        self.policy_list = policy_list
        # The request ID. You can use the request ID to locate logs and troubleshoot issues.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**: The request was successful.
        # *   **false**: The request failed.
        self.success = success
        # The ID of the tenant.
        self.tid = tid
        # The total number of policies.
        self.total_count = total_count

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
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        result['PolicyList'] = []
        if self.policy_list is not None:
            for k1 in self.policy_list:
                result['PolicyList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.tid is not None:
            result['Tid'] = self.tid

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        self.policy_list = []
        if m.get('PolicyList') is not None:
            for k1 in m.get('PolicyList'):
                temp_model = main_models.ListAbacPoliciesResponseBodyPolicyList()
                self.policy_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListAbacPoliciesResponseBodyPolicyList(DaraModel):
    def __init__(
        self,
        abac_policy_content: str = None,
        abac_policy_desc: str = None,
        abac_policy_id: int = None,
        abac_policy_name: str = None,
        abac_policy_source: str = None,
        creator_id: int = None,
    ):
        # The content of the policy.
        self.abac_policy_content = abac_policy_content
        # The description of the policy.
        self.abac_policy_desc = abac_policy_desc
        # The ID of the policy.
        self.abac_policy_id = abac_policy_id
        # The name of the policy.
        self.abac_policy_name = abac_policy_name
        # The source of the policy.
        self.abac_policy_source = abac_policy_source
        # The ID of the user who created the policy.
        self.creator_id = creator_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.abac_policy_content is not None:
            result['AbacPolicyContent'] = self.abac_policy_content

        if self.abac_policy_desc is not None:
            result['AbacPolicyDesc'] = self.abac_policy_desc

        if self.abac_policy_id is not None:
            result['AbacPolicyId'] = self.abac_policy_id

        if self.abac_policy_name is not None:
            result['AbacPolicyName'] = self.abac_policy_name

        if self.abac_policy_source is not None:
            result['AbacPolicySource'] = self.abac_policy_source

        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AbacPolicyContent') is not None:
            self.abac_policy_content = m.get('AbacPolicyContent')

        if m.get('AbacPolicyDesc') is not None:
            self.abac_policy_desc = m.get('AbacPolicyDesc')

        if m.get('AbacPolicyId') is not None:
            self.abac_policy_id = m.get('AbacPolicyId')

        if m.get('AbacPolicyName') is not None:
            self.abac_policy_name = m.get('AbacPolicyName')

        if m.get('AbacPolicySource') is not None:
            self.abac_policy_source = m.get('AbacPolicySource')

        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')

        return self

