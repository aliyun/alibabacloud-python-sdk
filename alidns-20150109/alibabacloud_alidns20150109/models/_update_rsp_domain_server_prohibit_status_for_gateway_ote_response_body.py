# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alidns20150109 import models as main_models
from darabonba.model import DaraModel

class UpdateRspDomainServerProhibitStatusForGatewayOteResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: main_models.UpdateRspDomainServerProhibitStatusForGatewayOteResponseBodyAccessDeniedDetail = None,
        data: main_models.UpdateRspDomainServerProhibitStatusForGatewayOteResponseBodyData = None,
        recoverable_error: bool = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.data = data
        self.recoverable_error = recoverable_error
        self.request_id = request_id
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

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.recoverable_error is not None:
            result['RecoverableError'] = self.recoverable_error

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            temp_model = main_models.UpdateRspDomainServerProhibitStatusForGatewayOteResponseBodyAccessDeniedDetail()
            self.access_denied_detail = temp_model.from_map(m.get('AccessDeniedDetail'))

        if m.get('Data') is not None:
            temp_model = main_models.UpdateRspDomainServerProhibitStatusForGatewayOteResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RecoverableError') is not None:
            self.recoverable_error = m.get('RecoverableError')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class UpdateRspDomainServerProhibitStatusForGatewayOteResponseBodyData(DaraModel):
    def __init__(
        self,
        domain_name: str = None,
        status_list: List[main_models.UpdateRspDomainServerProhibitStatusForGatewayOteResponseBodyDataStatusList] = None,
    ):
        self.domain_name = domain_name
        self.status_list = status_list

    def validate(self):
        if self.status_list:
            for v1 in self.status_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        result['StatusList'] = []
        if self.status_list is not None:
            for k1 in self.status_list:
                result['StatusList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        self.status_list = []
        if m.get('StatusList') is not None:
            for k1 in m.get('StatusList'):
                temp_model = main_models.UpdateRspDomainServerProhibitStatusForGatewayOteResponseBodyDataStatusList()
                self.status_list.append(temp_model.from_map(k1))

        return self

class UpdateRspDomainServerProhibitStatusForGatewayOteResponseBodyDataStatusList(DaraModel):
    def __init__(
        self,
        domain_name: str = None,
        status: str = None,
        status_msg: str = None,
    ):
        self.domain_name = domain_name
        self.status = status
        self.status_msg = status_msg

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.status is not None:
            result['Status'] = self.status

        if self.status_msg is not None:
            result['StatusMsg'] = self.status_msg

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StatusMsg') is not None:
            self.status_msg = m.get('StatusMsg')

        return self

class UpdateRspDomainServerProhibitStatusForGatewayOteResponseBodyAccessDeniedDetail(DaraModel):
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
        self.auth_action = auth_action
        self.auth_principal_display_name = auth_principal_display_name
        self.auth_principal_owner_id = auth_principal_owner_id
        self.auth_principal_type = auth_principal_type
        self.encoded_diagnostic_message = encoded_diagnostic_message
        self.no_permission_type = no_permission_type
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

