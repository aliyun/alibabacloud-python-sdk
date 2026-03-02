# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ims20190815 import models as main_models
from darabonba.model import DaraModel

class GetAccountSummaryResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        summary_map: main_models.GetAccountSummaryResponseBodySummaryMap = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The summary information of the Alibaba Cloud account.
        self.summary_map = summary_map

    def validate(self):
        if self.summary_map:
            self.summary_map.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.summary_map is not None:
            result['SummaryMap'] = self.summary_map.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SummaryMap') is not None:
            temp_model = main_models.GetAccountSummaryResponseBodySummaryMap()
            self.summary_map = temp_model.from_map(m.get('SummaryMap'))

        return self

class GetAccountSummaryResponseBodySummaryMap(DaraModel):
    def __init__(
        self,
        access_keys_per_user_quota: int = None,
        account_access_keys_per_account_quota: int = None,
        attached_policies_per_group_quota: int = None,
        attached_policies_per_role_quota: int = None,
        attached_policies_per_user_quota: int = None,
        attached_system_policies_per_group_quota: int = None,
        attached_system_policies_per_role_quota: int = None,
        attached_system_policies_per_user_quota: int = None,
        conditions_per_akpolicy_quota: int = None,
        groups: int = None,
        groups_per_user_quota: int = None,
        groups_quota: int = None,
        ipitems_per_akpolicy_quota: int = None,
        mfadevices: int = None,
        mfadevices_in_use: int = None,
        policies: int = None,
        policies_quota: int = None,
        policy_size_quota: int = None,
        roles: int = None,
        roles_quota: int = None,
        users: int = None,
        users_quota: int = None,
        versions_per_policy_quota: int = None,
        virtual_mfadevices_quota: int = None,
    ):
        # The maximum number of AccessKey pairs that a RAM user can have.
        self.access_keys_per_user_quota = access_keys_per_user_quota
        # The maximum number of AccessKeys for an Alibaba Cloud account.
        self.account_access_keys_per_account_quota = account_access_keys_per_account_quota
        # The maximum number of custom policies that can be attached to a user group.
        self.attached_policies_per_group_quota = attached_policies_per_group_quota
        # The maximum number of custom policies that can be attached to a RAM role.
        self.attached_policies_per_role_quota = attached_policies_per_role_quota
        # The maximum number of custom policies that can be attached to a RAM user.
        self.attached_policies_per_user_quota = attached_policies_per_user_quota
        # The maximum number of system policies that can be attached to a user group.
        self.attached_system_policies_per_group_quota = attached_system_policies_per_group_quota
        # The maximum number of system policies that can be attached to a RAM role.
        self.attached_system_policies_per_role_quota = attached_system_policies_per_role_quota
        # The maximum number of system policies that can be attached to a RAM user.
        self.attached_system_policies_per_user_quota = attached_system_policies_per_user_quota
        # The maximum number of conditions that can be set in an account-level or AccessKey-level network access control policy.
        self.conditions_per_akpolicy_quota = conditions_per_akpolicy_quota
        # The number of user groups.
        self.groups = groups
        # The maximum number of user groups that a RAM user can join.
        self.groups_per_user_quota = groups_per_user_quota
        # The maximum number of user groups that can be created.
        self.groups_quota = groups_quota
        # The maximum number of IP addresses that can be set in an account-level or AccessKey-level network access control policy.
        self.ipitems_per_akpolicy_quota = ipitems_per_akpolicy_quota
        # The number of virtual multi-factor authentication (MFA) devices.
        self.mfadevices = mfadevices
        # The number of virtual MFA devices that are in use.
        self.mfadevices_in_use = mfadevices_in_use
        # The number of custom policies.
        self.policies = policies
        # The maximum number of custom policies that can be created.
        self.policies_quota = policies_quota
        # The maximum length of a policy document.
        self.policy_size_quota = policy_size_quota
        # The number of RAM roles.
        self.roles = roles
        # The maximum number of RAM roles that can be created.
        self.roles_quota = roles_quota
        # The number of RAM users.
        self.users = users
        # The maximum number of RAM users that can be created.
        self.users_quota = users_quota
        # The maximum number of policy versions.
        self.versions_per_policy_quota = versions_per_policy_quota
        # The maximum number of virtual MFA devices that can be created.
        self.virtual_mfadevices_quota = virtual_mfadevices_quota

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_keys_per_user_quota is not None:
            result['AccessKeysPerUserQuota'] = self.access_keys_per_user_quota

        if self.account_access_keys_per_account_quota is not None:
            result['AccountAccessKeysPerAccountQuota'] = self.account_access_keys_per_account_quota

        if self.attached_policies_per_group_quota is not None:
            result['AttachedPoliciesPerGroupQuota'] = self.attached_policies_per_group_quota

        if self.attached_policies_per_role_quota is not None:
            result['AttachedPoliciesPerRoleQuota'] = self.attached_policies_per_role_quota

        if self.attached_policies_per_user_quota is not None:
            result['AttachedPoliciesPerUserQuota'] = self.attached_policies_per_user_quota

        if self.attached_system_policies_per_group_quota is not None:
            result['AttachedSystemPoliciesPerGroupQuota'] = self.attached_system_policies_per_group_quota

        if self.attached_system_policies_per_role_quota is not None:
            result['AttachedSystemPoliciesPerRoleQuota'] = self.attached_system_policies_per_role_quota

        if self.attached_system_policies_per_user_quota is not None:
            result['AttachedSystemPoliciesPerUserQuota'] = self.attached_system_policies_per_user_quota

        if self.conditions_per_akpolicy_quota is not None:
            result['ConditionsPerAKPolicyQuota'] = self.conditions_per_akpolicy_quota

        if self.groups is not None:
            result['Groups'] = self.groups

        if self.groups_per_user_quota is not None:
            result['GroupsPerUserQuota'] = self.groups_per_user_quota

        if self.groups_quota is not None:
            result['GroupsQuota'] = self.groups_quota

        if self.ipitems_per_akpolicy_quota is not None:
            result['IPItemsPerAKPolicyQuota'] = self.ipitems_per_akpolicy_quota

        if self.mfadevices is not None:
            result['MFADevices'] = self.mfadevices

        if self.mfadevices_in_use is not None:
            result['MFADevicesInUse'] = self.mfadevices_in_use

        if self.policies is not None:
            result['Policies'] = self.policies

        if self.policies_quota is not None:
            result['PoliciesQuota'] = self.policies_quota

        if self.policy_size_quota is not None:
            result['PolicySizeQuota'] = self.policy_size_quota

        if self.roles is not None:
            result['Roles'] = self.roles

        if self.roles_quota is not None:
            result['RolesQuota'] = self.roles_quota

        if self.users is not None:
            result['Users'] = self.users

        if self.users_quota is not None:
            result['UsersQuota'] = self.users_quota

        if self.versions_per_policy_quota is not None:
            result['VersionsPerPolicyQuota'] = self.versions_per_policy_quota

        if self.virtual_mfadevices_quota is not None:
            result['VirtualMFADevicesQuota'] = self.virtual_mfadevices_quota

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessKeysPerUserQuota') is not None:
            self.access_keys_per_user_quota = m.get('AccessKeysPerUserQuota')

        if m.get('AccountAccessKeysPerAccountQuota') is not None:
            self.account_access_keys_per_account_quota = m.get('AccountAccessKeysPerAccountQuota')

        if m.get('AttachedPoliciesPerGroupQuota') is not None:
            self.attached_policies_per_group_quota = m.get('AttachedPoliciesPerGroupQuota')

        if m.get('AttachedPoliciesPerRoleQuota') is not None:
            self.attached_policies_per_role_quota = m.get('AttachedPoliciesPerRoleQuota')

        if m.get('AttachedPoliciesPerUserQuota') is not None:
            self.attached_policies_per_user_quota = m.get('AttachedPoliciesPerUserQuota')

        if m.get('AttachedSystemPoliciesPerGroupQuota') is not None:
            self.attached_system_policies_per_group_quota = m.get('AttachedSystemPoliciesPerGroupQuota')

        if m.get('AttachedSystemPoliciesPerRoleQuota') is not None:
            self.attached_system_policies_per_role_quota = m.get('AttachedSystemPoliciesPerRoleQuota')

        if m.get('AttachedSystemPoliciesPerUserQuota') is not None:
            self.attached_system_policies_per_user_quota = m.get('AttachedSystemPoliciesPerUserQuota')

        if m.get('ConditionsPerAKPolicyQuota') is not None:
            self.conditions_per_akpolicy_quota = m.get('ConditionsPerAKPolicyQuota')

        if m.get('Groups') is not None:
            self.groups = m.get('Groups')

        if m.get('GroupsPerUserQuota') is not None:
            self.groups_per_user_quota = m.get('GroupsPerUserQuota')

        if m.get('GroupsQuota') is not None:
            self.groups_quota = m.get('GroupsQuota')

        if m.get('IPItemsPerAKPolicyQuota') is not None:
            self.ipitems_per_akpolicy_quota = m.get('IPItemsPerAKPolicyQuota')

        if m.get('MFADevices') is not None:
            self.mfadevices = m.get('MFADevices')

        if m.get('MFADevicesInUse') is not None:
            self.mfadevices_in_use = m.get('MFADevicesInUse')

        if m.get('Policies') is not None:
            self.policies = m.get('Policies')

        if m.get('PoliciesQuota') is not None:
            self.policies_quota = m.get('PoliciesQuota')

        if m.get('PolicySizeQuota') is not None:
            self.policy_size_quota = m.get('PolicySizeQuota')

        if m.get('Roles') is not None:
            self.roles = m.get('Roles')

        if m.get('RolesQuota') is not None:
            self.roles_quota = m.get('RolesQuota')

        if m.get('Users') is not None:
            self.users = m.get('Users')

        if m.get('UsersQuota') is not None:
            self.users_quota = m.get('UsersQuota')

        if m.get('VersionsPerPolicyQuota') is not None:
            self.versions_per_policy_quota = m.get('VersionsPerPolicyQuota')

        if m.get('VirtualMFADevicesQuota') is not None:
            self.virtual_mfadevices_quota = m.get('VirtualMFADevicesQuota')

        return self

