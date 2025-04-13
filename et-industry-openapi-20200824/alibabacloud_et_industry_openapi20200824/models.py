# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, Any, List


class GetMqttConnectRequest(TeaModel):
    def __init__(
        self,
        request: Dict[str, Any] = None,
    ):
        self.request = request

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request is not None:
            result['Request'] = self.request
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Request') is not None:
            self.request = m.get('Request')
        return self


class GetMqttConnectResponseBodyAccessDeniedDetail(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class GetMqttConnectResponseBodyData(TeaModel):
    def __init__(
        self,
        access_key: str = None,
        client_id: str = None,
        expire_time: int = None,
        instance_id: str = None,
        qos_level: int = None,
        server_uri: str = None,
        token: str = None,
    ):
        self.access_key = access_key
        self.client_id = client_id
        self.expire_time = expire_time
        self.instance_id = instance_id
        self.qos_level = qos_level
        self.server_uri = server_uri
        self.token = token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key is not None:
            result['AccessKey'] = self.access_key
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.qos_level is not None:
            result['QosLevel'] = self.qos_level
        if self.server_uri is not None:
            result['ServerUri'] = self.server_uri
        if self.token is not None:
            result['Token'] = self.token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessKey') is not None:
            self.access_key = m.get('AccessKey')
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('QosLevel') is not None:
            self.qos_level = m.get('QosLevel')
        if m.get('ServerUri') is not None:
            self.server_uri = m.get('ServerUri')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        return self


class GetMqttConnectResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: GetMqttConnectResponseBodyAccessDeniedDetail = None,
        code: str = None,
        data: GetMqttConnectResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.access_denied_detail:
            self.access_denied_detail.validate()
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
            temp_model = GetMqttConnectResponseBodyAccessDeniedDetail()
            self.access_denied_detail = temp_model.from_map(m['AccessDeniedDetail'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetMqttConnectResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetMqttConnectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetMqttConnectResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetMqttConnectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetNonceRequest(TeaModel):
    def __init__(
        self,
        request: Dict[str, Any] = None,
    ):
        self.request = request

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request is not None:
            result['Request'] = self.request
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Request') is not None:
            self.request = m.get('Request')
        return self


class GetNonceResponseBodyAccessDeniedDetail(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class GetNonceResponseBodyData(TeaModel):
    def __init__(
        self,
        expires_in: int = None,
        nonce: str = None,
    ):
        self.expires_in = expires_in
        self.nonce = nonce

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expires_in is not None:
            result['ExpiresIn'] = self.expires_in
        if self.nonce is not None:
            result['Nonce'] = self.nonce
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpiresIn') is not None:
            self.expires_in = m.get('ExpiresIn')
        if m.get('Nonce') is not None:
            self.nonce = m.get('Nonce')
        return self


class GetNonceResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: GetNonceResponseBodyAccessDeniedDetail = None,
        code: str = None,
        data: GetNonceResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.access_denied_detail:
            self.access_denied_detail.validate()
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
            temp_model = GetNonceResponseBodyAccessDeniedDetail()
            self.access_denied_detail = temp_model.from_map(m['AccessDeniedDetail'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetNonceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetNonceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetNonceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetNonceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListMeasurePointListByNodeCodePageRequest(TeaModel):
    def __init__(
        self,
        request: Dict[str, Any] = None,
    ):
        self.request = request

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request is not None:
            result['Request'] = self.request
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Request') is not None:
            self.request = m.get('Request')
        return self


class ListMeasurePointListByNodeCodePageResponseBodyAccessDeniedDetail(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ListMeasurePointListByNodeCodePageResponseBodyDataDataList(TeaModel):
    def __init__(
        self,
        acq_freq: str = None,
        alarm_attribute: str = None,
        alarm_level: str = None,
        calc_attribute: str = None,
        calc_formula: str = None,
        calc_type: str = None,
        code: str = None,
        create_user: str = None,
        data_source_id: str = None,
        data_type: str = None,
        description: str = None,
        err_msg_detail: str = None,
        full_name: str = None,
        gmt_create: int = None,
        gmt_modify: int = None,
        id: int = None,
        init_value: str = None,
        is_enable: str = None,
        last_upload_time: str = None,
        latest_value: str = None,
        lower_limit: str = None,
        measure_point_state: str = None,
        modify_user: str = None,
        name: str = None,
        node_code: str = None,
        node_id: int = None,
        node_name: str = None,
        parent_full_name: str = None,
        pay_load: str = None,
        protocol_config: str = None,
        source_point: str = None,
        tenant_code: str = None,
        time: str = None,
        type: str = None,
        unit: str = None,
        upper_limit: str = None,
    ):
        self.acq_freq = acq_freq
        self.alarm_attribute = alarm_attribute
        self.alarm_level = alarm_level
        self.calc_attribute = calc_attribute
        self.calc_formula = calc_formula
        self.calc_type = calc_type
        self.code = code
        self.create_user = create_user
        self.data_source_id = data_source_id
        self.data_type = data_type
        self.description = description
        self.err_msg_detail = err_msg_detail
        self.full_name = full_name
        self.gmt_create = gmt_create
        self.gmt_modify = gmt_modify
        self.id = id
        self.init_value = init_value
        self.is_enable = is_enable
        self.last_upload_time = last_upload_time
        self.latest_value = latest_value
        self.lower_limit = lower_limit
        self.measure_point_state = measure_point_state
        self.modify_user = modify_user
        self.name = name
        self.node_code = node_code
        self.node_id = node_id
        self.node_name = node_name
        self.parent_full_name = parent_full_name
        self.pay_load = pay_load
        self.protocol_config = protocol_config
        self.source_point = source_point
        self.tenant_code = tenant_code
        self.time = time
        self.type = type
        self.unit = unit
        self.upper_limit = upper_limit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acq_freq is not None:
            result['AcqFreq'] = self.acq_freq
        if self.alarm_attribute is not None:
            result['AlarmAttribute'] = self.alarm_attribute
        if self.alarm_level is not None:
            result['AlarmLevel'] = self.alarm_level
        if self.calc_attribute is not None:
            result['CalcAttribute'] = self.calc_attribute
        if self.calc_formula is not None:
            result['CalcFormula'] = self.calc_formula
        if self.calc_type is not None:
            result['CalcType'] = self.calc_type
        if self.code is not None:
            result['Code'] = self.code
        if self.create_user is not None:
            result['CreateUser'] = self.create_user
        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.description is not None:
            result['Description'] = self.description
        if self.err_msg_detail is not None:
            result['ErrMsgDetail'] = self.err_msg_detail
        if self.full_name is not None:
            result['FullName'] = self.full_name
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modify is not None:
            result['GmtModify'] = self.gmt_modify
        if self.id is not None:
            result['Id'] = self.id
        if self.init_value is not None:
            result['InitValue'] = self.init_value
        if self.is_enable is not None:
            result['IsEnable'] = self.is_enable
        if self.last_upload_time is not None:
            result['LastUploadTime'] = self.last_upload_time
        if self.latest_value is not None:
            result['LatestValue'] = self.latest_value
        if self.lower_limit is not None:
            result['LowerLimit'] = self.lower_limit
        if self.measure_point_state is not None:
            result['MeasurePointState'] = self.measure_point_state
        if self.modify_user is not None:
            result['ModifyUser'] = self.modify_user
        if self.name is not None:
            result['Name'] = self.name
        if self.node_code is not None:
            result['NodeCode'] = self.node_code
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.node_name is not None:
            result['NodeName'] = self.node_name
        if self.parent_full_name is not None:
            result['ParentFullName'] = self.parent_full_name
        if self.pay_load is not None:
            result['PayLoad'] = self.pay_load
        if self.protocol_config is not None:
            result['ProtocolConfig'] = self.protocol_config
        if self.source_point is not None:
            result['SourcePoint'] = self.source_point
        if self.tenant_code is not None:
            result['TenantCode'] = self.tenant_code
        if self.time is not None:
            result['Time'] = self.time
        if self.type is not None:
            result['Type'] = self.type
        if self.unit is not None:
            result['Unit'] = self.unit
        if self.upper_limit is not None:
            result['UpperLimit'] = self.upper_limit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcqFreq') is not None:
            self.acq_freq = m.get('AcqFreq')
        if m.get('AlarmAttribute') is not None:
            self.alarm_attribute = m.get('AlarmAttribute')
        if m.get('AlarmLevel') is not None:
            self.alarm_level = m.get('AlarmLevel')
        if m.get('CalcAttribute') is not None:
            self.calc_attribute = m.get('CalcAttribute')
        if m.get('CalcFormula') is not None:
            self.calc_formula = m.get('CalcFormula')
        if m.get('CalcType') is not None:
            self.calc_type = m.get('CalcType')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('CreateUser') is not None:
            self.create_user = m.get('CreateUser')
        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ErrMsgDetail') is not None:
            self.err_msg_detail = m.get('ErrMsgDetail')
        if m.get('FullName') is not None:
            self.full_name = m.get('FullName')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModify') is not None:
            self.gmt_modify = m.get('GmtModify')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InitValue') is not None:
            self.init_value = m.get('InitValue')
        if m.get('IsEnable') is not None:
            self.is_enable = m.get('IsEnable')
        if m.get('LastUploadTime') is not None:
            self.last_upload_time = m.get('LastUploadTime')
        if m.get('LatestValue') is not None:
            self.latest_value = m.get('LatestValue')
        if m.get('LowerLimit') is not None:
            self.lower_limit = m.get('LowerLimit')
        if m.get('MeasurePointState') is not None:
            self.measure_point_state = m.get('MeasurePointState')
        if m.get('ModifyUser') is not None:
            self.modify_user = m.get('ModifyUser')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NodeCode') is not None:
            self.node_code = m.get('NodeCode')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')
        if m.get('ParentFullName') is not None:
            self.parent_full_name = m.get('ParentFullName')
        if m.get('PayLoad') is not None:
            self.pay_load = m.get('PayLoad')
        if m.get('ProtocolConfig') is not None:
            self.protocol_config = m.get('ProtocolConfig')
        if m.get('SourcePoint') is not None:
            self.source_point = m.get('SourcePoint')
        if m.get('TenantCode') is not None:
            self.tenant_code = m.get('TenantCode')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Unit') is not None:
            self.unit = m.get('Unit')
        if m.get('UpperLimit') is not None:
            self.upper_limit = m.get('UpperLimit')
        return self


class ListMeasurePointListByNodeCodePageResponseBodyData(TeaModel):
    def __init__(
        self,
        count: int = None,
        current_page: int = None,
        data_list: List[ListMeasurePointListByNodeCodePageResponseBodyDataDataList] = None,
        total_page: int = None,
    ):
        self.count = count
        self.current_page = current_page
        self.data_list = data_list
        self.total_page = total_page

    def validate(self):
        if self.data_list:
            for k in self.data_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['DataList'] = []
        if self.data_list is not None:
            for k in self.data_list:
                result['DataList'].append(k.to_map() if k else None)
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.data_list = []
        if m.get('DataList') is not None:
            for k in m.get('DataList'):
                temp_model = ListMeasurePointListByNodeCodePageResponseBodyDataDataList()
                self.data_list.append(temp_model.from_map(k))
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        return self


class ListMeasurePointListByNodeCodePageResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: ListMeasurePointListByNodeCodePageResponseBodyAccessDeniedDetail = None,
        code: str = None,
        data: ListMeasurePointListByNodeCodePageResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.access_denied_detail:
            self.access_denied_detail.validate()
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
            temp_model = ListMeasurePointListByNodeCodePageResponseBodyAccessDeniedDetail()
            self.access_denied_detail = temp_model.from_map(m['AccessDeniedDetail'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ListMeasurePointListByNodeCodePageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListMeasurePointListByNodeCodePageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListMeasurePointListByNodeCodePageResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListMeasurePointListByNodeCodePageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MultiFieldBatchUploadRequest(TeaModel):
    def __init__(
        self,
        body: Dict[str, Any] = None,
    ):
        self.body = body

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class MultiFieldBatchUploadResponseBodyAccessDeniedDetail(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class MultiFieldBatchUploadResponseBodyDataMessage(TeaModel):
    def __init__(
        self,
        error_msg: str = None,
        measure_point: str = None,
        node: str = None,
    ):
        self.error_msg = error_msg
        self.measure_point = measure_point
        self.node = node

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.measure_point is not None:
            result['MeasurePoint'] = self.measure_point
        if self.node is not None:
            result['Node'] = self.node
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('MeasurePoint') is not None:
            self.measure_point = m.get('MeasurePoint')
        if m.get('Node') is not None:
            self.node = m.get('Node')
        return self


class MultiFieldBatchUploadResponseBodyData(TeaModel):
    def __init__(
        self,
        count: int = None,
        message: List[MultiFieldBatchUploadResponseBodyDataMessage] = None,
    ):
        self.count = count
        self.message = message

    def validate(self):
        if self.message:
            for k in self.message:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        result['Message'] = []
        if self.message is not None:
            for k in self.message:
                result['Message'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        self.message = []
        if m.get('Message') is not None:
            for k in m.get('Message'):
                temp_model = MultiFieldBatchUploadResponseBodyDataMessage()
                self.message.append(temp_model.from_map(k))
        return self


class MultiFieldBatchUploadResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: MultiFieldBatchUploadResponseBodyAccessDeniedDetail = None,
        code: str = None,
        data: MultiFieldBatchUploadResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.access_denied_detail:
            self.access_denied_detail.validate()
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
            temp_model = MultiFieldBatchUploadResponseBodyAccessDeniedDetail()
            self.access_denied_detail = temp_model.from_map(m['AccessDeniedDetail'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = MultiFieldBatchUploadResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class MultiFieldBatchUploadResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: MultiFieldBatchUploadResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = MultiFieldBatchUploadResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MultiSourcePointBatchUploadRequest(TeaModel):
    def __init__(
        self,
        body: Dict[str, Any] = None,
    ):
        self.body = body

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class MultiSourcePointBatchUploadResponseBodyAccessDeniedDetail(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class MultiSourcePointBatchUploadResponseBodyDataMessage(TeaModel):
    def __init__(
        self,
        error_msg: str = None,
        node: str = None,
        source_point: str = None,
    ):
        self.error_msg = error_msg
        self.node = node
        self.source_point = source_point

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.node is not None:
            result['Node'] = self.node
        if self.source_point is not None:
            result['SourcePoint'] = self.source_point
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('Node') is not None:
            self.node = m.get('Node')
        if m.get('SourcePoint') is not None:
            self.source_point = m.get('SourcePoint')
        return self


class MultiSourcePointBatchUploadResponseBodyData(TeaModel):
    def __init__(
        self,
        count: int = None,
        message: List[MultiSourcePointBatchUploadResponseBodyDataMessage] = None,
    ):
        self.count = count
        self.message = message

    def validate(self):
        if self.message:
            for k in self.message:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        result['Message'] = []
        if self.message is not None:
            for k in self.message:
                result['Message'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        self.message = []
        if m.get('Message') is not None:
            for k in m.get('Message'):
                temp_model = MultiSourcePointBatchUploadResponseBodyDataMessage()
                self.message.append(temp_model.from_map(k))
        return self


class MultiSourcePointBatchUploadResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: MultiSourcePointBatchUploadResponseBodyAccessDeniedDetail = None,
        code: str = None,
        data: MultiSourcePointBatchUploadResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.access_denied_detail:
            self.access_denied_detail.validate()
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
            temp_model = MultiSourcePointBatchUploadResponseBodyAccessDeniedDetail()
            self.access_denied_detail = temp_model.from_map(m['AccessDeniedDetail'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = MultiSourcePointBatchUploadResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class MultiSourcePointBatchUploadResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: MultiSourcePointBatchUploadResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = MultiSourcePointBatchUploadResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryFieldLatestBySourcePointRequest(TeaModel):
    def __init__(
        self,
        request: Dict[str, Any] = None,
    ):
        self.request = request

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request is not None:
            result['Request'] = self.request
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Request') is not None:
            self.request = m.get('Request')
        return self


class QueryFieldLatestBySourcePointResponseBodyAccessDeniedDetail(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class QueryFieldLatestBySourcePointResponseBodyDataValues(TeaModel):
    def __init__(
        self,
        event_time: str = None,
        process_time: str = None,
        quality: int = None,
        sample_type: str = None,
        time: int = None,
        timestamp: int = None,
        value: str = None,
    ):
        self.event_time = event_time
        self.process_time = process_time
        self.quality = quality
        self.sample_type = sample_type
        self.time = time
        self.timestamp = timestamp
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_time is not None:
            result['EventTime'] = self.event_time
        if self.process_time is not None:
            result['ProcessTime'] = self.process_time
        if self.quality is not None:
            result['Quality'] = self.quality
        if self.sample_type is not None:
            result['SampleType'] = self.sample_type
        if self.time is not None:
            result['Time'] = self.time
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventTime') is not None:
            self.event_time = m.get('EventTime')
        if m.get('ProcessTime') is not None:
            self.process_time = m.get('ProcessTime')
        if m.get('Quality') is not None:
            self.quality = m.get('Quality')
        if m.get('SampleType') is not None:
            self.sample_type = m.get('SampleType')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class QueryFieldLatestBySourcePointResponseBodyData(TeaModel):
    def __init__(
        self,
        measure_point: str = None,
        node: str = None,
        source_point: str = None,
        value_type: str = None,
        values: List[QueryFieldLatestBySourcePointResponseBodyDataValues] = None,
    ):
        self.measure_point = measure_point
        self.node = node
        self.source_point = source_point
        self.value_type = value_type
        self.values = values

    def validate(self):
        if self.values:
            for k in self.values:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.measure_point is not None:
            result['MeasurePoint'] = self.measure_point
        if self.node is not None:
            result['Node'] = self.node
        if self.source_point is not None:
            result['SourcePoint'] = self.source_point
        if self.value_type is not None:
            result['ValueType'] = self.value_type
        result['Values'] = []
        if self.values is not None:
            for k in self.values:
                result['Values'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MeasurePoint') is not None:
            self.measure_point = m.get('MeasurePoint')
        if m.get('Node') is not None:
            self.node = m.get('Node')
        if m.get('SourcePoint') is not None:
            self.source_point = m.get('SourcePoint')
        if m.get('ValueType') is not None:
            self.value_type = m.get('ValueType')
        self.values = []
        if m.get('Values') is not None:
            for k in m.get('Values'):
                temp_model = QueryFieldLatestBySourcePointResponseBodyDataValues()
                self.values.append(temp_model.from_map(k))
        return self


class QueryFieldLatestBySourcePointResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: QueryFieldLatestBySourcePointResponseBodyAccessDeniedDetail = None,
        code: str = None,
        data: List[QueryFieldLatestBySourcePointResponseBodyData] = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.access_denied_detail:
            self.access_denied_detail.validate()
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail.to_map()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
            temp_model = QueryFieldLatestBySourcePointResponseBodyAccessDeniedDetail()
            self.access_denied_detail = temp_model.from_map(m['AccessDeniedDetail'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = QueryFieldLatestBySourcePointResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryFieldLatestBySourcePointResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryFieldLatestBySourcePointResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryFieldLatestBySourcePointResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryIndustryDeviceDataRequest(TeaModel):
    def __init__(
        self,
        request: Dict[str, Any] = None,
    ):
        self.request = request

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request is not None:
            result['Request'] = self.request
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Request') is not None:
            self.request = m.get('Request')
        return self


class QueryIndustryDeviceDataResponseBodyAccessDeniedDetail(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class QueryIndustryDeviceDataResponseBodyDataValues(TeaModel):
    def __init__(
        self,
        event_time: str = None,
        process_time: str = None,
        quality: int = None,
        time: int = None,
        time_stamp: int = None,
        value: str = None,
    ):
        self.event_time = event_time
        self.process_time = process_time
        self.quality = quality
        self.time = time
        self.time_stamp = time_stamp
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_time is not None:
            result['EventTime'] = self.event_time
        if self.process_time is not None:
            result['ProcessTime'] = self.process_time
        if self.quality is not None:
            result['Quality'] = self.quality
        if self.time is not None:
            result['Time'] = self.time
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventTime') is not None:
            self.event_time = m.get('EventTime')
        if m.get('ProcessTime') is not None:
            self.process_time = m.get('ProcessTime')
        if m.get('Quality') is not None:
            self.quality = m.get('Quality')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class QueryIndustryDeviceDataResponseBodyData(TeaModel):
    def __init__(
        self,
        measure_point: str = None,
        node: str = None,
        value_type: str = None,
        values: List[QueryIndustryDeviceDataResponseBodyDataValues] = None,
    ):
        self.measure_point = measure_point
        self.node = node
        self.value_type = value_type
        self.values = values

    def validate(self):
        if self.values:
            for k in self.values:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.measure_point is not None:
            result['MeasurePoint'] = self.measure_point
        if self.node is not None:
            result['Node'] = self.node
        if self.value_type is not None:
            result['ValueType'] = self.value_type
        result['Values'] = []
        if self.values is not None:
            for k in self.values:
                result['Values'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MeasurePoint') is not None:
            self.measure_point = m.get('MeasurePoint')
        if m.get('Node') is not None:
            self.node = m.get('Node')
        if m.get('ValueType') is not None:
            self.value_type = m.get('ValueType')
        self.values = []
        if m.get('Values') is not None:
            for k in m.get('Values'):
                temp_model = QueryIndustryDeviceDataResponseBodyDataValues()
                self.values.append(temp_model.from_map(k))
        return self


class QueryIndustryDeviceDataResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: QueryIndustryDeviceDataResponseBodyAccessDeniedDetail = None,
        code: str = None,
        data: List[QueryIndustryDeviceDataResponseBodyData] = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.access_denied_detail:
            self.access_denied_detail.validate()
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail.to_map()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
            temp_model = QueryIndustryDeviceDataResponseBodyAccessDeniedDetail()
            self.access_denied_detail = temp_model.from_map(m['AccessDeniedDetail'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = QueryIndustryDeviceDataResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryIndustryDeviceDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryIndustryDeviceDataResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryIndustryDeviceDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryIndustryDeviceLimitsDataRequest(TeaModel):
    def __init__(
        self,
        request: Dict[str, Any] = None,
    ):
        self.request = request

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request is not None:
            result['Request'] = self.request
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Request') is not None:
            self.request = m.get('Request')
        return self


class QueryIndustryDeviceLimitsDataResponseBodyAccessDeniedDetail(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class QueryIndustryDeviceLimitsDataResponseBodyDataValues(TeaModel):
    def __init__(
        self,
        event_time: str = None,
        process_time: str = None,
        quality: int = None,
        time: int = None,
        time_stamp: int = None,
        value: str = None,
    ):
        self.event_time = event_time
        self.process_time = process_time
        self.quality = quality
        self.time = time
        self.time_stamp = time_stamp
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_time is not None:
            result['EventTime'] = self.event_time
        if self.process_time is not None:
            result['ProcessTime'] = self.process_time
        if self.quality is not None:
            result['Quality'] = self.quality
        if self.time is not None:
            result['Time'] = self.time
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventTime') is not None:
            self.event_time = m.get('EventTime')
        if m.get('ProcessTime') is not None:
            self.process_time = m.get('ProcessTime')
        if m.get('Quality') is not None:
            self.quality = m.get('Quality')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class QueryIndustryDeviceLimitsDataResponseBodyData(TeaModel):
    def __init__(
        self,
        measure_point: str = None,
        node: str = None,
        value_type: str = None,
        values: List[QueryIndustryDeviceLimitsDataResponseBodyDataValues] = None,
    ):
        self.measure_point = measure_point
        self.node = node
        self.value_type = value_type
        self.values = values

    def validate(self):
        if self.values:
            for k in self.values:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.measure_point is not None:
            result['MeasurePoint'] = self.measure_point
        if self.node is not None:
            result['Node'] = self.node
        if self.value_type is not None:
            result['ValueType'] = self.value_type
        result['Values'] = []
        if self.values is not None:
            for k in self.values:
                result['Values'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MeasurePoint') is not None:
            self.measure_point = m.get('MeasurePoint')
        if m.get('Node') is not None:
            self.node = m.get('Node')
        if m.get('ValueType') is not None:
            self.value_type = m.get('ValueType')
        self.values = []
        if m.get('Values') is not None:
            for k in m.get('Values'):
                temp_model = QueryIndustryDeviceLimitsDataResponseBodyDataValues()
                self.values.append(temp_model.from_map(k))
        return self


class QueryIndustryDeviceLimitsDataResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: QueryIndustryDeviceLimitsDataResponseBodyAccessDeniedDetail = None,
        code: str = None,
        data: List[QueryIndustryDeviceLimitsDataResponseBodyData] = None,
        http_status_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.access_denied_detail:
            self.access_denied_detail.validate()
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail.to_map()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
            temp_model = QueryIndustryDeviceLimitsDataResponseBodyAccessDeniedDetail()
            self.access_denied_detail = temp_model.from_map(m['AccessDeniedDetail'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = QueryIndustryDeviceLimitsDataResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryIndustryDeviceLimitsDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryIndustryDeviceLimitsDataResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryIndustryDeviceLimitsDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryIndustryDeviceStatusDataRequest(TeaModel):
    def __init__(
        self,
        request: Dict[str, Any] = None,
    ):
        self.request = request

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request is not None:
            result['Request'] = self.request
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Request') is not None:
            self.request = m.get('Request')
        return self


class QueryIndustryDeviceStatusDataResponseBodyAccessDeniedDetail(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class QueryIndustryDeviceStatusDataResponseBodyData(TeaModel):
    def __init__(
        self,
        measure_point: str = None,
        node: str = None,
        value_type: str = None,
        values: List[Dict[str, Any]] = None,
    ):
        self.measure_point = measure_point
        self.node = node
        self.value_type = value_type
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.measure_point is not None:
            result['MeasurePoint'] = self.measure_point
        if self.node is not None:
            result['Node'] = self.node
        if self.value_type is not None:
            result['ValueType'] = self.value_type
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MeasurePoint') is not None:
            self.measure_point = m.get('MeasurePoint')
        if m.get('Node') is not None:
            self.node = m.get('Node')
        if m.get('ValueType') is not None:
            self.value_type = m.get('ValueType')
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class QueryIndustryDeviceStatusDataResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: QueryIndustryDeviceStatusDataResponseBodyAccessDeniedDetail = None,
        code: str = None,
        data: List[QueryIndustryDeviceStatusDataResponseBodyData] = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.access_denied_detail:
            self.access_denied_detail.validate()
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail.to_map()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
            temp_model = QueryIndustryDeviceStatusDataResponseBodyAccessDeniedDetail()
            self.access_denied_detail = temp_model.from_map(m['AccessDeniedDetail'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = QueryIndustryDeviceStatusDataResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryIndustryDeviceStatusDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryIndustryDeviceStatusDataResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryIndustryDeviceStatusDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SourcePointBatchRequest(TeaModel):
    def __init__(
        self,
        request: Dict[str, Any] = None,
    ):
        self.request = request

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request is not None:
            result['Request'] = self.request
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Request') is not None:
            self.request = m.get('Request')
        return self


class SourcePointBatchResponseBodyAccessDeniedDetail(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class SourcePointBatchResponseBodyData(TeaModel):
    def __init__(
        self,
        count: int = None,
    ):
        self.count = count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class SourcePointBatchResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: SourcePointBatchResponseBodyAccessDeniedDetail = None,
        code: str = None,
        data: SourcePointBatchResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.access_denied_detail:
            self.access_denied_detail.validate()
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
            temp_model = SourcePointBatchResponseBodyAccessDeniedDetail()
            self.access_denied_detail = temp_model.from_map(m['AccessDeniedDetail'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = SourcePointBatchResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SourcePointBatchResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SourcePointBatchResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SourcePointBatchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UploadIndustryDeviceDataRequest(TeaModel):
    def __init__(
        self,
        request: Dict[str, Any] = None,
    ):
        self.request = request

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request is not None:
            result['Request'] = self.request
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Request') is not None:
            self.request = m.get('Request')
        return self


class UploadIndustryDeviceDataResponseBodyAccessDeniedDetail(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class UploadIndustryDeviceDataResponseBodyDataMessage(TeaModel):
    def __init__(
        self,
        error_msg: str = None,
        measure_point: str = None,
        node: str = None,
    ):
        self.error_msg = error_msg
        self.measure_point = measure_point
        self.node = node

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.measure_point is not None:
            result['MeasurePoint'] = self.measure_point
        if self.node is not None:
            result['Node'] = self.node
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('MeasurePoint') is not None:
            self.measure_point = m.get('MeasurePoint')
        if m.get('Node') is not None:
            self.node = m.get('Node')
        return self


class UploadIndustryDeviceDataResponseBodyData(TeaModel):
    def __init__(
        self,
        count: int = None,
        message: List[UploadIndustryDeviceDataResponseBodyDataMessage] = None,
    ):
        self.count = count
        self.message = message

    def validate(self):
        if self.message:
            for k in self.message:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        result['Message'] = []
        if self.message is not None:
            for k in self.message:
                result['Message'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        self.message = []
        if m.get('Message') is not None:
            for k in m.get('Message'):
                temp_model = UploadIndustryDeviceDataResponseBodyDataMessage()
                self.message.append(temp_model.from_map(k))
        return self


class UploadIndustryDeviceDataResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: UploadIndustryDeviceDataResponseBodyAccessDeniedDetail = None,
        code: str = None,
        data: UploadIndustryDeviceDataResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.access_denied_detail:
            self.access_denied_detail.validate()
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
            temp_model = UploadIndustryDeviceDataResponseBodyAccessDeniedDetail()
            self.access_denied_detail = temp_model.from_map(m['AccessDeniedDetail'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = UploadIndustryDeviceDataResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UploadIndustryDeviceDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UploadIndustryDeviceDataResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UploadIndustryDeviceDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


