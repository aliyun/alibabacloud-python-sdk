# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sddp20190103 import models as main_models
from darabonba.model import DaraModel

class DescribeUserStatusResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        user_status: main_models.DescribeUserStatusResponseBodyUserStatus = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The details of the current logon account.
        self.user_status = user_status

    def validate(self):
        if self.user_status:
            self.user_status.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.user_status is not None:
            result['UserStatus'] = self.user_status.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('UserStatus') is not None:
            temp_model = main_models.DescribeUserStatusResponseBodyUserStatus()
            self.user_status = temp_model.from_map(m.get('UserStatus'))

        return self

class DescribeUserStatusResponseBodyUserStatus(DaraModel):
    def __init__(
        self,
        access_key_id: str = None,
        asset_role_authed: bool = None,
        audit_closable: bool = None,
        audit_releasable: bool = None,
        authed: bool = None,
        charge_type: str = None,
        data_manager_role: int = None,
        instance_id: str = None,
        instance_num: int = None,
        instance_total_count: int = None,
        lab_status: int = None,
        oss_total_size: int = None,
        protection_days: int = None,
        purchased: bool = None,
        release_days: int = None,
        release_time: int = None,
        remain_days: int = None,
        trail: bool = None,
        use_agent_audit: bool = None,
        use_instance_num: int = None,
        use_oss_size: int = None,
    ):
        # The AccessKey ID authorized by the user.
        self.access_key_id = access_key_id
        # Indicates whether the current logon account has authorized the service-linked role for DSC asset synchronization. Valid values:
        # - **true**: authorized.
        # - **false**: not authorized.
        self.asset_role_authed = asset_role_authed
        # Indicates whether SQL Explorer can be disabled. Valid values:
        # - **true**: can be disabled.
        # - **false**: cannot be disabled.
        self.audit_closable = audit_closable
        # Indicates whether SQL Explorer can be released. Valid values:
        # - **true**: can be released.
        # - **false**: cannot be released.
        self.audit_releasable = audit_releasable
        # Indicates whether the current logon account has authorized DSC to access RAM. Valid values:
        # - **true**: authorized.
        # - **false**: not authorized.
        self.authed = authed
        # The billing method of the DSC service purchased by the current logon account. Valid values:
        # - **PREPAY**: subscription.
        # - **POSTPAY**: pay-as-you-go.
        self.charge_type = charge_type
        # The permissions of the current account. Valid values:
        # - **0**: has management or read-only permissions for Data Security Center.
        # - **1**: has data domain management permissions.
        self.data_manager_role = data_manager_role
        # The instance ID of the Data Security Center product purchased by the Alibaba Cloud account.
        self.instance_id = instance_id
        # The number of instances in the current logon account.
        self.instance_num = instance_num
        # The total number of instances.
        self.instance_total_count = instance_total_count
        # Indicates whether the asset lab feature is enabled. Valid values:
        # - **1**: enabled.
        # - **0**: not enabled.
        self.lab_status = lab_status
        # The total OSS storage capacity. Unit: bytes.
        self.oss_total_size = oss_total_size
        # The total number of days that user assets have been protected.
        self.protection_days = protection_days
        # Indicates whether the DSC service is purchased. Valid values:
        # 
        # - **true**: purchased.
        # - **false**: not purchased.
        self.purchased = purchased
        # The number of days from expiration to release. Unit: days.
        self.release_days = release_days
        # The release time. Unit: milliseconds.
        self.release_time = release_time
        # The remaining days of the protection period for assets in the current logon account.
        self.remain_days = remain_days
        # Indicates whether the current logon account is using a trial version of DSC. Valid values:
        # - **true**: trial.
        # - **false**: non-trial.
        self.trail = trail
        # Indicates whether the Agent audit feature has been used. Valid values:
        # - **1**: has been used.
        # - **0**: has not been used.
        self.use_agent_audit = use_agent_audit
        # The number of instances that are used.
        self.use_instance_num = use_instance_num
        # The used OSS storage capacity. Unit: bytes.
        self.use_oss_size = use_oss_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_key_id is not None:
            result['AccessKeyId'] = self.access_key_id

        if self.asset_role_authed is not None:
            result['AssetRoleAuthed'] = self.asset_role_authed

        if self.audit_closable is not None:
            result['AuditClosable'] = self.audit_closable

        if self.audit_releasable is not None:
            result['AuditReleasable'] = self.audit_releasable

        if self.authed is not None:
            result['Authed'] = self.authed

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.data_manager_role is not None:
            result['DataManagerRole'] = self.data_manager_role

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_num is not None:
            result['InstanceNum'] = self.instance_num

        if self.instance_total_count is not None:
            result['InstanceTotalCount'] = self.instance_total_count

        if self.lab_status is not None:
            result['LabStatus'] = self.lab_status

        if self.oss_total_size is not None:
            result['OssTotalSize'] = self.oss_total_size

        if self.protection_days is not None:
            result['ProtectionDays'] = self.protection_days

        if self.purchased is not None:
            result['Purchased'] = self.purchased

        if self.release_days is not None:
            result['ReleaseDays'] = self.release_days

        if self.release_time is not None:
            result['ReleaseTime'] = self.release_time

        if self.remain_days is not None:
            result['RemainDays'] = self.remain_days

        if self.trail is not None:
            result['Trail'] = self.trail

        if self.use_agent_audit is not None:
            result['UseAgentAudit'] = self.use_agent_audit

        if self.use_instance_num is not None:
            result['UseInstanceNum'] = self.use_instance_num

        if self.use_oss_size is not None:
            result['UseOssSize'] = self.use_oss_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessKeyId') is not None:
            self.access_key_id = m.get('AccessKeyId')

        if m.get('AssetRoleAuthed') is not None:
            self.asset_role_authed = m.get('AssetRoleAuthed')

        if m.get('AuditClosable') is not None:
            self.audit_closable = m.get('AuditClosable')

        if m.get('AuditReleasable') is not None:
            self.audit_releasable = m.get('AuditReleasable')

        if m.get('Authed') is not None:
            self.authed = m.get('Authed')

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('DataManagerRole') is not None:
            self.data_manager_role = m.get('DataManagerRole')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceNum') is not None:
            self.instance_num = m.get('InstanceNum')

        if m.get('InstanceTotalCount') is not None:
            self.instance_total_count = m.get('InstanceTotalCount')

        if m.get('LabStatus') is not None:
            self.lab_status = m.get('LabStatus')

        if m.get('OssTotalSize') is not None:
            self.oss_total_size = m.get('OssTotalSize')

        if m.get('ProtectionDays') is not None:
            self.protection_days = m.get('ProtectionDays')

        if m.get('Purchased') is not None:
            self.purchased = m.get('Purchased')

        if m.get('ReleaseDays') is not None:
            self.release_days = m.get('ReleaseDays')

        if m.get('ReleaseTime') is not None:
            self.release_time = m.get('ReleaseTime')

        if m.get('RemainDays') is not None:
            self.remain_days = m.get('RemainDays')

        if m.get('Trail') is not None:
            self.trail = m.get('Trail')

        if m.get('UseAgentAudit') is not None:
            self.use_agent_audit = m.get('UseAgentAudit')

        if m.get('UseInstanceNum') is not None:
            self.use_instance_num = m.get('UseInstanceNum')

        if m.get('UseOssSize') is not None:
            self.use_oss_size = m.get('UseOssSize')

        return self

