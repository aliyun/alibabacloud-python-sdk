# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DeleteCheckPolicyResponseBody(DaraModel):
    def __init__(
        self,
        policys: List[main_models.DeleteCheckPolicyResponseBodyPolicys] = None,
        request_id: str = None,
    ):
        # List of deleted policy details.
        self.policys = policys
        # The unique ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.policys:
            for v1 in self.policys:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Policys'] = []
        if self.policys is not None:
            for k1 in self.policys:
                result['Policys'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.policys = []
        if m.get('Policys') is not None:
            for k1 in m.get('Policys'):
                temp_model = main_models.DeleteCheckPolicyResponseBodyPolicys()
                self.policys.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DeleteCheckPolicyResponseBodyPolicys(DaraModel):
    def __init__(
        self,
        policy_id: int = None,
        policy_show_name: str = None,
        policy_type: str = None,
    ):
        # Deleted policy ID.
        self.policy_id = policy_id
        # The name of the custom policy.
        self.policy_show_name = policy_show_name
        # Policy type for custom check rule:
        # 
        # *   **STANDARD**: Standard-level policy
        # *   **REQUIREMENT**: Requirement-level policy
        # *   **SECTION**: Section-level policy
        self.policy_type = policy_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id

        if self.policy_show_name is not None:
            result['PolicyShowName'] = self.policy_show_name

        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')

        if m.get('PolicyShowName') is not None:
            self.policy_show_name = m.get('PolicyShowName')

        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')

        return self

