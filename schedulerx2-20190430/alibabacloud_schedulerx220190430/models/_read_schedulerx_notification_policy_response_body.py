# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_schedulerx220190430 import models as main_models
from darabonba.model import DaraModel

class ReadSchedulerxNotificationPolicyResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: main_models.ReadSchedulerxNotificationPolicyResponseBodyAccessDeniedDetail = None,
        code: int = None,
        data: main_models.ReadSchedulerxNotificationPolicyResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The access denial details.
        self.access_denied_detail = access_denied_detail
        # The status code.
        self.code = code
        # *
        self.data = data
        # The error message.
        self.message = message
        # The unique request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.access_denied_detail:
            self.access_denied_detail.validate()
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail.to_map()

        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            temp_model = main_models.ReadSchedulerxNotificationPolicyResponseBodyAccessDeniedDetail()
            self.access_denied_detail = temp_model.from_map(m.get('AccessDeniedDetail'))

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.ReadSchedulerxNotificationPolicyResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ReadSchedulerxNotificationPolicyResponseBodyData(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        records: List[main_models.ReadSchedulerxNotificationPolicyResponseBodyDataRecords] = None,
        total: int = None,
    ):
        # The maximum number of entries returned.
        self.max_results = max_results
        # When data that matches the query conditions has not been fully retrieved, the server returns nextToken. You can then use nextToken to continue retrieving the remaining data.
        self.next_token = next_token
        # The data records.
        self.records = records
        # The total number of records.
        self.total = total

    def validate(self):
        if self.records:
            for v1 in self.records:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        result['Records'] = []
        if self.records is not None:
            for k1 in self.records:
                result['Records'].append(k1.to_map() if k1 else None)

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        self.records = []
        if m.get('Records') is not None:
            for k1 in m.get('Records'):
                temp_model = main_models.ReadSchedulerxNotificationPolicyResponseBodyDataRecords()
                self.records.append(temp_model.from_map(k1))

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class ReadSchedulerxNotificationPolicyResponseBodyDataRecords(DaraModel):
    def __init__(
        self,
        channel_time_range: str = None,
        create_time: str = None,
        creator: str = None,
        description: str = None,
        policy_name: str = None,
        reference_apps: List[main_models.ReadSchedulerxNotificationPolicyResponseBodyDataRecordsReferenceApps] = None,
        update_time: str = None,
        updater: str = None,
    ):
        # The configuration of the notification policy.
        self.channel_time_range = channel_time_range
        # The creation time.
        self.create_time = create_time
        # The creator.
        self.creator = creator
        # The description of the notification policy.
        self.description = description
        # The name of the notification policy.
        self.policy_name = policy_name
        # The list of applications associated with the notification policy.
        self.reference_apps = reference_apps
        # The update time.
        self.update_time = update_time
        # The updater.
        self.updater = updater

    def validate(self):
        if self.reference_apps:
            for v1 in self.reference_apps:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channel_time_range is not None:
            result['ChannelTimeRange'] = self.channel_time_range

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.creator is not None:
            result['Creator'] = self.creator

        if self.description is not None:
            result['Description'] = self.description

        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name

        result['ReferenceApps'] = []
        if self.reference_apps is not None:
            for k1 in self.reference_apps:
                result['ReferenceApps'].append(k1.to_map() if k1 else None)

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.updater is not None:
            result['Updater'] = self.updater

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelTimeRange') is not None:
            self.channel_time_range = m.get('ChannelTimeRange')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Creator') is not None:
            self.creator = m.get('Creator')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')

        self.reference_apps = []
        if m.get('ReferenceApps') is not None:
            for k1 in m.get('ReferenceApps'):
                temp_model = main_models.ReadSchedulerxNotificationPolicyResponseBodyDataRecordsReferenceApps()
                self.reference_apps.append(temp_model.from_map(k1))

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('Updater') is not None:
            self.updater = m.get('Updater')

        return self

class ReadSchedulerxNotificationPolicyResponseBodyDataRecordsReferenceApps(DaraModel):
    def __init__(
        self,
        app_group_id: int = None,
        group_id: str = None,
        namespace_name: str = None,
        namespace_uid: str = None,
    ):
        # The ID of the task group.
        self.app_group_id = app_group_id
        # The ID of the application.
        self.group_id = group_id
        # The name of the namespace.
        self.namespace_name = namespace_name
        # The unique identifier of the namespace.
        self.namespace_uid = namespace_uid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_group_id is not None:
            result['AppGroupId'] = self.app_group_id

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.namespace_name is not None:
            result['NamespaceName'] = self.namespace_name

        if self.namespace_uid is not None:
            result['NamespaceUid'] = self.namespace_uid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppGroupId') is not None:
            self.app_group_id = m.get('AppGroupId')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('NamespaceName') is not None:
            self.namespace_name = m.get('NamespaceName')

        if m.get('NamespaceUid') is not None:
            self.namespace_uid = m.get('NamespaceUid')

        return self

class ReadSchedulerxNotificationPolicyResponseBodyAccessDeniedDetail(DaraModel):
    def __init__(
        self,
        auth_action: str = None,
        auth_principal_display_name: str = None,
        auth_principal_owner_id: str = None,
        auth_principal_type: str = None,
        encoded_diagnostic_message: str = None,
        no_permission_type: str = None,
        policy_type: str = None,
    ):
        # The authentication operation.
        self.auth_action = auth_action
        # The principal name.
        self.auth_principal_display_name = auth_principal_display_name
        # The account of the principal.
        self.auth_principal_owner_id = auth_principal_owner_id
        # The principal type.
        self.auth_principal_type = auth_principal_type
        # The encoded diagnostic message.
        self.encoded_diagnostic_message = encoded_diagnostic_message
        # The permission denial type.
        self.no_permission_type = no_permission_type
        # The policy type.
        self.policy_type = policy_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_action is not None:
            result['AuthAction'] = self.auth_action

        if self.auth_principal_display_name is not None:
            result['AuthPrincipalDisplayName'] = self.auth_principal_display_name

        if self.auth_principal_owner_id is not None:
            result['AuthPrincipalOwnerId'] = self.auth_principal_owner_id

        if self.auth_principal_type is not None:
            result['AuthPrincipalType'] = self.auth_principal_type

        if self.encoded_diagnostic_message is not None:
            result['EncodedDiagnosticMessage'] = self.encoded_diagnostic_message

        if self.no_permission_type is not None:
            result['NoPermissionType'] = self.no_permission_type

        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthAction') is not None:
            self.auth_action = m.get('AuthAction')

        if m.get('AuthPrincipalDisplayName') is not None:
            self.auth_principal_display_name = m.get('AuthPrincipalDisplayName')

        if m.get('AuthPrincipalOwnerId') is not None:
            self.auth_principal_owner_id = m.get('AuthPrincipalOwnerId')

        if m.get('AuthPrincipalType') is not None:
            self.auth_principal_type = m.get('AuthPrincipalType')

        if m.get('EncodedDiagnosticMessage') is not None:
            self.encoded_diagnostic_message = m.get('EncodedDiagnosticMessage')

        if m.get('NoPermissionType') is not None:
            self.no_permission_type = m.get('NoPermissionType')

        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')

        return self

