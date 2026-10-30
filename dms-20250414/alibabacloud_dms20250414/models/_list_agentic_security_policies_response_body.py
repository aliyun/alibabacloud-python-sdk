# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms20250414 import models as main_models
from darabonba.model import DaraModel

class ListAgenticSecurityPoliciesResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListAgenticSecurityPoliciesResponseBodyData] = None,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        # The list of security policies returned by this query. Enabled system default policies are placed at the beginning, followed by the user policies on the current page. You can use Readonly to distinguish between the two types of policies.
        self.data = data
        # The error code returned when the request fails. This parameter is empty when the request is successful.
        self.error_code = error_code
        # The error message returned when the request fails. This parameter is empty when the request is successful.
        self.error_message = error_message
        # The request ID, which is used to locate and trace this call.
        self.request_id = request_id
        # Indicates whether the request is successful. Valid values:
        # - true: The request is successful.
        # - false: The request fails.
        self.success = success
        # The total number of policies that meet the query conditions. The value is the sum of the number of all enabled system default policies and the number of user policies of the current account that meet the filter conditions.
        self.total_count = total_count

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

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
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListAgenticSecurityPoliciesResponseBodyData()
                self.data.append(temp_model.from_map(k1))

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

class ListAgenticSecurityPoliciesResponseBodyData(DaraModel):
    def __init__(
        self,
        aliyun_account_uid: str = None,
        base_policy_id: str = None,
        description: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        policy_id: str = None,
        policy_name: str = None,
        policy_status: str = None,
        readonly: bool = None,
        tags: str = None,
        updated_by: str = None,
    ):
        # The UID of the Alibaba Cloud account to which the user policy belongs. This value is not returned for system default policies.
        self.aliyun_account_uid = aliyun_account_uid
        # The ID of the system default policy inherited by the user policy. This value is empty if no inheritance relationship is configured. This value is not returned for system default policies.
        self.base_policy_id = base_policy_id
        # The description of the security policy. The description of a system default policy is returned in the language of the request context.
        self.description = description
        # The time when the security policy was created. The time is in the yyyy-MM-dd HH:mm:ss format and does not contain a time zone offset.
        self.gmt_create = gmt_create
        # The time when the security policy was last modified. The time is in the yyyy-MM-dd HH:mm:ss format and does not contain a time zone offset.
        self.gmt_modified = gmt_modified
        # The business ID of the security policy. A system default policy ID starts with sp-sys-, and a user policy ID starts with sp-usr-.
        self.policy_id = policy_id
        # The Policy Name of the security policy. The Policy Name of a system default policy is returned in the language of the request context.
        self.policy_name = policy_name
        # The current state of the security policy. Valid values:
        # - ON: Enabled.
        # - OFF: Disabled.
        # - ARCHIVED: Archived.
        # All system default policies returned by this operation are in the ON state.
        self.policy_status = policy_status
        # Specifies whether the policy is read-only. Valid values:
        # - true: The policy is a system default policy.
        # - false: The policy is a user policy of the current account.
        self.readonly = readonly
        # The tags of the system default policy. Multiple tags are separated by commas (,). This value is not returned for user policies.
        self.tags = tags
        # The identifier of the operator that last modified the policy. For a user policy, the operator ID is recorded first. If no operator ID is available, the UID of the current Alibaba Cloud account is recorded.
        self.updated_by = updated_by

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aliyun_account_uid is not None:
            result['AliyunAccountUid'] = self.aliyun_account_uid

        if self.base_policy_id is not None:
            result['BasePolicyId'] = self.base_policy_id

        if self.description is not None:
            result['Description'] = self.description

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id

        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name

        if self.policy_status is not None:
            result['PolicyStatus'] = self.policy_status

        if self.readonly is not None:
            result['Readonly'] = self.readonly

        if self.tags is not None:
            result['Tags'] = self.tags

        if self.updated_by is not None:
            result['UpdatedBy'] = self.updated_by

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunAccountUid') is not None:
            self.aliyun_account_uid = m.get('AliyunAccountUid')

        if m.get('BasePolicyId') is not None:
            self.base_policy_id = m.get('BasePolicyId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')

        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')

        if m.get('PolicyStatus') is not None:
            self.policy_status = m.get('PolicyStatus')

        if m.get('Readonly') is not None:
            self.readonly = m.get('Readonly')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('UpdatedBy') is not None:
            self.updated_by = m.get('UpdatedBy')

        return self

