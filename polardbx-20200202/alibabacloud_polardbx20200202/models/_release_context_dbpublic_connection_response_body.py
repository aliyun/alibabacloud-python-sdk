# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_polardbx20200202 import models as main_models
from darabonba.model import DaraModel

class ReleaseContextDBPublicConnectionResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: main_models.ReleaseContextDBPublicConnectionResponseBodyAccessDeniedDetail = None,
        data: main_models.ReleaseContextDBPublicConnectionResponseBodyData = None,
        request_id: str = None,
    ):
        # The details of the access denial.
        self.access_denied_detail = access_denied_detail
        # The operation result.
        self.data = data
        # Id of the request
        self.request_id = request_id

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

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            temp_model = main_models.ReleaseContextDBPublicConnectionResponseBodyAccessDeniedDetail()
            self.access_denied_detail = temp_model.from_map(m.get('AccessDeniedDetail'))

        if m.get('Data') is not None:
            temp_model = main_models.ReleaseContextDBPublicConnectionResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ReleaseContextDBPublicConnectionResponseBodyData(DaraModel):
    def __init__(
        self,
        context_dbinstance_name: str = None,
        dbinstance_id: int = None,
        dbinstance_name: str = None,
        net_type: int = None,
        node_type: str = None,
        old_connection_string: str = None,
        old_port: str = None,
        task_id: int = None,
    ):
        # The context service instance name.
        self.context_dbinstance_name = context_dbinstance_name
        # The instance ID.
        self.dbinstance_id = dbinstance_id
        # The instance ID.
        self.dbinstance_name = dbinstance_name
        # The network type.
        self.net_type = net_type
        # The query node type. Valid values:
        # - service
        # - dashboard
        self.node_type = node_type
        # The database endpoint before the switchover.
        self.old_connection_string = old_connection_string
        # The previous port value.
        self.old_port = old_port
        # The task ID.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.context_dbinstance_name is not None:
            result['ContextDBInstanceName'] = self.context_dbinstance_name

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name

        if self.net_type is not None:
            result['NetType'] = self.net_type

        if self.node_type is not None:
            result['NodeType'] = self.node_type

        if self.old_connection_string is not None:
            result['OldConnectionString'] = self.old_connection_string

        if self.old_port is not None:
            result['OldPort'] = self.old_port

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContextDBInstanceName') is not None:
            self.context_dbinstance_name = m.get('ContextDBInstanceName')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')

        if m.get('NetType') is not None:
            self.net_type = m.get('NetType')

        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')

        if m.get('OldConnectionString') is not None:
            self.old_connection_string = m.get('OldConnectionString')

        if m.get('OldPort') is not None:
            self.old_port = m.get('OldPort')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

class ReleaseContextDBPublicConnectionResponseBodyAccessDeniedDetail(DaraModel):
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
        # The authentication action.
        self.auth_action = auth_action
        # The identity used for authentication in the request.
        self.auth_principal_display_name = auth_principal_display_name
        # The type of the authentication principal.
        self.auth_principal_owner_id = auth_principal_owner_id
        # The type of the authentication principal.
        self.auth_principal_type = auth_principal_type
        # The encoded diagnostic message.
        self.encoded_diagnostic_message = encoded_diagnostic_message
        # The type of the permission denial.
        self.no_permission_type = no_permission_type
        # PolicyType
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

