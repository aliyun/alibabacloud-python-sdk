# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cloudsso20210515 import models as main_models
from darabonba.model import DaraModel

class GetDirectoryStatisticsResponseBody(DaraModel):
    def __init__(
        self,
        directory_statistics: main_models.GetDirectoryStatisticsResponseBodyDirectoryStatistics = None,
        request_id: str = None,
    ):
        # The statistics of the directory.
        self.directory_statistics = directory_statistics
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.directory_statistics:
            self.directory_statistics.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.directory_statistics is not None:
            result['DirectoryStatistics'] = self.directory_statistics.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DirectoryStatistics') is not None:
            temp_model = main_models.GetDirectoryStatisticsResponseBodyDirectoryStatistics()
            self.directory_statistics = temp_model.from_map(m.get('DirectoryStatistics'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetDirectoryStatisticsResponseBodyDirectoryStatistics(DaraModel):
    def __init__(
        self,
        access_assignment_count: int = None,
        access_configuration_count: int = None,
        access_configuration_quota: int = None,
        directory_id: str = None,
        directory_name: str = None,
        group_count: int = None,
        group_quota: int = None,
        in_progress_task_count: int = None,
        inline_policy_per_access_configuration_quota: int = None,
        region: str = None,
        scimserver_credential_count: int = None,
        scimsync_enabled: bool = None,
        ssoenabled: bool = None,
        system_policy_per_access_configuration_quota: int = None,
        user_count: int = None,
        user_quota: int = None,
    ):
        # The number of access permissions that are assigned.
        self.access_assignment_count = access_assignment_count
        # The number of access configurations.
        self.access_configuration_count = access_configuration_count
        # The quota for access configurations.
        self.access_configuration_quota = access_configuration_quota
        # The ID of the directory.
        self.directory_id = directory_id
        # The name of the directory.
        self.directory_name = directory_name
        # The number of user groups.
        self.group_count = group_count
        # The quota for user groups.
        self.group_quota = group_quota
        # The number of tasks that are being performed.
        self.in_progress_task_count = in_progress_task_count
        # The number of inline policies that can be configured for an access configuration.
        self.inline_policy_per_access_configuration_quota = inline_policy_per_access_configuration_quota
        # The region ID of the directory.
        self.region = region
        # The number of SCIM credentials.
        self.scimserver_credential_count = scimserver_credential_count
        # Indicates whether SCIM synchronization is enabled. Valid values:
        # 
        # *   true
        # *   false
        self.scimsync_enabled = scimsync_enabled
        # Indicates whether SSO is enabled. Valid values:
        # 
        # *   true
        # *   false
        self.ssoenabled = ssoenabled
        # The quota for system policies that can be configured for an access configuration.
        self.system_policy_per_access_configuration_quota = system_policy_per_access_configuration_quota
        # The number of users.
        self.user_count = user_count
        # The quota for users.
        self.user_quota = user_quota

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_assignment_count is not None:
            result['AccessAssignmentCount'] = self.access_assignment_count

        if self.access_configuration_count is not None:
            result['AccessConfigurationCount'] = self.access_configuration_count

        if self.access_configuration_quota is not None:
            result['AccessConfigurationQuota'] = self.access_configuration_quota

        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id

        if self.directory_name is not None:
            result['DirectoryName'] = self.directory_name

        if self.group_count is not None:
            result['GroupCount'] = self.group_count

        if self.group_quota is not None:
            result['GroupQuota'] = self.group_quota

        if self.in_progress_task_count is not None:
            result['InProgressTaskCount'] = self.in_progress_task_count

        if self.inline_policy_per_access_configuration_quota is not None:
            result['InlinePolicyPerAccessConfigurationQuota'] = self.inline_policy_per_access_configuration_quota

        if self.region is not None:
            result['Region'] = self.region

        if self.scimserver_credential_count is not None:
            result['SCIMServerCredentialCount'] = self.scimserver_credential_count

        if self.scimsync_enabled is not None:
            result['SCIMSyncEnabled'] = self.scimsync_enabled

        if self.ssoenabled is not None:
            result['SSOEnabled'] = self.ssoenabled

        if self.system_policy_per_access_configuration_quota is not None:
            result['SystemPolicyPerAccessConfigurationQuota'] = self.system_policy_per_access_configuration_quota

        if self.user_count is not None:
            result['UserCount'] = self.user_count

        if self.user_quota is not None:
            result['UserQuota'] = self.user_quota

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessAssignmentCount') is not None:
            self.access_assignment_count = m.get('AccessAssignmentCount')

        if m.get('AccessConfigurationCount') is not None:
            self.access_configuration_count = m.get('AccessConfigurationCount')

        if m.get('AccessConfigurationQuota') is not None:
            self.access_configuration_quota = m.get('AccessConfigurationQuota')

        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')

        if m.get('DirectoryName') is not None:
            self.directory_name = m.get('DirectoryName')

        if m.get('GroupCount') is not None:
            self.group_count = m.get('GroupCount')

        if m.get('GroupQuota') is not None:
            self.group_quota = m.get('GroupQuota')

        if m.get('InProgressTaskCount') is not None:
            self.in_progress_task_count = m.get('InProgressTaskCount')

        if m.get('InlinePolicyPerAccessConfigurationQuota') is not None:
            self.inline_policy_per_access_configuration_quota = m.get('InlinePolicyPerAccessConfigurationQuota')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('SCIMServerCredentialCount') is not None:
            self.scimserver_credential_count = m.get('SCIMServerCredentialCount')

        if m.get('SCIMSyncEnabled') is not None:
            self.scimsync_enabled = m.get('SCIMSyncEnabled')

        if m.get('SSOEnabled') is not None:
            self.ssoenabled = m.get('SSOEnabled')

        if m.get('SystemPolicyPerAccessConfigurationQuota') is not None:
            self.system_policy_per_access_configuration_quota = m.get('SystemPolicyPerAccessConfigurationQuota')

        if m.get('UserCount') is not None:
            self.user_count = m.get('UserCount')

        if m.get('UserQuota') is not None:
            self.user_quota = m.get('UserQuota')

        return self

