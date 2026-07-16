# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alidns20150109 import models as main_models
from darabonba.model import DaraModel

class ListAtiChangeLogsResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: main_models.ListAtiChangeLogsResponseBodyAccessDeniedDetail = None,
        logs: main_models.ListAtiChangeLogsResponseBodyLogs = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_items: int = None,
        total_pages: int = None,
    ):
        # The details of the access denial. This field is returned only when RAM authentication fails.
        self.access_denied_detail = access_denied_detail
        self.logs = logs
        # The current page number. Minimum value: 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries in the address list.
        self.total_items = total_items
        # The total number of pages.
        self.total_pages = total_pages

    def validate(self):
        if self.access_denied_detail:
            self.access_denied_detail.validate()
        if self.logs:
            self.logs.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail.to_map()

        if self.logs is not None:
            result['Logs'] = self.logs.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_items is not None:
            result['TotalItems'] = self.total_items

        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            temp_model = main_models.ListAtiChangeLogsResponseBodyAccessDeniedDetail()
            self.access_denied_detail = temp_model.from_map(m.get('AccessDeniedDetail'))

        if m.get('Logs') is not None:
            temp_model = main_models.ListAtiChangeLogsResponseBodyLogs()
            self.logs = temp_model.from_map(m.get('Logs'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalItems') is not None:
            self.total_items = m.get('TotalItems')

        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')

        return self

class ListAtiChangeLogsResponseBodyLogs(DaraModel):
    def __init__(
        self,
        log: List[main_models.ListAtiChangeLogsResponseBodyLogsLog] = None,
    ):
        self.log = log

    def validate(self):
        if self.log:
            for v1 in self.log:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Log'] = []
        if self.log is not None:
            for k1 in self.log:
                result['Log'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.log = []
        if m.get('Log') is not None:
            for k1 in m.get('Log'):
                temp_model = main_models.ListAtiChangeLogsResponseBodyLogsLog()
                self.log.append(temp_model.from_map(k1))

        return self

class ListAtiChangeLogsResponseBodyLogsLog(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        agent_status: str = None,
        create_timestamp: int = None,
        creator_sub_type: str = None,
        creator_type: str = None,
        error_message: str = None,
        log_id: str = None,
        operation_name: str = None,
        operation_type: str = None,
        operator_account: str = None,
        result: str = None,
        source_ip: str = None,
        timestamp: int = None,
        update_timestamp: int = None,
        version: str = None,
    ):
        self.agent_id = agent_id
        self.agent_status = agent_status
        self.create_timestamp = create_timestamp
        self.creator_sub_type = creator_sub_type
        self.creator_type = creator_type
        self.error_message = error_message
        self.log_id = log_id
        self.operation_name = operation_name
        self.operation_type = operation_type
        self.operator_account = operator_account
        self.result = result
        self.source_ip = source_ip
        self.timestamp = timestamp
        self.update_timestamp = update_timestamp
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_id is not None:
            result['AgentId'] = self.agent_id

        if self.agent_status is not None:
            result['AgentStatus'] = self.agent_status

        if self.create_timestamp is not None:
            result['CreateTimestamp'] = self.create_timestamp

        if self.creator_sub_type is not None:
            result['CreatorSubType'] = self.creator_sub_type

        if self.creator_type is not None:
            result['CreatorType'] = self.creator_type

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.log_id is not None:
            result['LogId'] = self.log_id

        if self.operation_name is not None:
            result['OperationName'] = self.operation_name

        if self.operation_type is not None:
            result['OperationType'] = self.operation_type

        if self.operator_account is not None:
            result['OperatorAccount'] = self.operator_account

        if self.result is not None:
            result['Result'] = self.result

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        if self.update_timestamp is not None:
            result['UpdateTimestamp'] = self.update_timestamp

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')

        if m.get('AgentStatus') is not None:
            self.agent_status = m.get('AgentStatus')

        if m.get('CreateTimestamp') is not None:
            self.create_timestamp = m.get('CreateTimestamp')

        if m.get('CreatorSubType') is not None:
            self.creator_sub_type = m.get('CreatorSubType')

        if m.get('CreatorType') is not None:
            self.creator_type = m.get('CreatorType')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('LogId') is not None:
            self.log_id = m.get('LogId')

        if m.get('OperationName') is not None:
            self.operation_name = m.get('OperationName')

        if m.get('OperationType') is not None:
            self.operation_type = m.get('OperationType')

        if m.get('OperatorAccount') is not None:
            self.operator_account = m.get('OperatorAccount')

        if m.get('Result') is not None:
            self.result = m.get('Result')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        if m.get('UpdateTimestamp') is not None:
            self.update_timestamp = m.get('UpdateTimestamp')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

class ListAtiChangeLogsResponseBodyAccessDeniedDetail(DaraModel):
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
        # The unauthorized operation that was attempted.
        self.auth_action = auth_action
        # The display name of the authorization principal.
        self.auth_principal_display_name = auth_principal_display_name
        # The owner ID of the authorization principal.
        self.auth_principal_owner_id = auth_principal_owner_id
        # The identity type.
        self.auth_principal_type = auth_principal_type
        # The encrypted diagnostic message.
        self.encoded_diagnostic_message = encoded_diagnostic_message
        # The reason for the authentication failure. Valid values:
        # - ExplicitDeny: explicit deny.
        # - ImplicitDeny: implicit deny.
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

