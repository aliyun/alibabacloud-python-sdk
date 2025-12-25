# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class ListAbacAuthorizationsResponseBody(DaraModel):
    def __init__(
        self,
        authorization_list: List[main_models.ListAbacAuthorizationsResponseBodyAuthorizationList] = None,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        # The list of users to which the specified policy is attached.
        self.authorization_list = authorization_list
        # The error code that is returned when the request failed.
        self.error_code = error_code
        # The error message that is returned when the request failed.
        self.error_message = error_message
        # The request ID. You can use the ID to query logs and troubleshoot issues.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**: The request was successful.
        # *   **false**: The request failed.
        self.success = success
        # The number of objects to which the policy is attached.
        self.total_count = total_count

    def validate(self):
        if self.authorization_list:
            for v1 in self.authorization_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AuthorizationList'] = []
        if self.authorization_list is not None:
            for k1 in self.authorization_list:
                result['AuthorizationList'].append(k1.to_map() if k1 else None)

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.authorization_list = []
        if m.get('AuthorizationList') is not None:
            for k1 in m.get('AuthorizationList'):
                temp_model = main_models.ListAbacAuthorizationsResponseBodyAuthorizationList()
                self.authorization_list.append(temp_model.from_map(k1))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListAbacAuthorizationsResponseBodyAuthorizationList(DaraModel):
    def __init__(
        self,
        authorization_id: int = None,
        identity_id: int = None,
        identity_name: str = None,
        identity_type: str = None,
        policy_id: int = None,
        policy_name: str = None,
        policy_source: str = None,
    ):
        # The authorization ID.
        self.authorization_id = authorization_id
        # The ID of the object to which the policy is attached.
        self.identity_id = identity_id
        # The name of the object to which the policy is attached.
        self.identity_name = identity_name
        # The type of the object to which the policy is attached.
        self.identity_type = identity_type
        # The ID of the policy.
        self.policy_id = policy_id
        # The name of the policy.
        self.policy_name = policy_name
        # The source of the policy.
        self.policy_source = policy_source

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.authorization_id is not None:
            result['AuthorizationId'] = self.authorization_id

        if self.identity_id is not None:
            result['IdentityId'] = self.identity_id

        if self.identity_name is not None:
            result['IdentityName'] = self.identity_name

        if self.identity_type is not None:
            result['IdentityType'] = self.identity_type

        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id

        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name

        if self.policy_source is not None:
            result['PolicySource'] = self.policy_source

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorizationId') is not None:
            self.authorization_id = m.get('AuthorizationId')

        if m.get('IdentityId') is not None:
            self.identity_id = m.get('IdentityId')

        if m.get('IdentityName') is not None:
            self.identity_name = m.get('IdentityName')

        if m.get('IdentityType') is not None:
            self.identity_type = m.get('IdentityType')

        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')

        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')

        if m.get('PolicySource') is not None:
            self.policy_source = m.get('PolicySource')

        return self

