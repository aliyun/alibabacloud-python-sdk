# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List, Any


class AttachEBEventBusRequest(TeaModel):
    def __init__(
        self,
        event_bus_name: bytes = None,
        event_source_full_name: bytes = None,
    ):
        # 事件源英文Code
        self.event_bus_name = event_bus_name
        # 事件源ID
        self.event_source_full_name = event_source_full_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name
        if self.event_source_full_name is not None:
            result['EventSourceFullName'] = self.event_source_full_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')
        if m.get('EventSourceFullName') is not None:
            self.event_source_full_name = m.get('EventSourceFullName')
        return self


class AttachEBEventBusResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AttachEBEventBusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AttachEBEventBusResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = AttachEBEventBusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckRoleForProductRequest(TeaModel):
    def __init__(
        self,
        product_name: str = None,
    ):
        self.product_name = product_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        return self


class CheckRoleForProductResponseBodyData(TeaModel):
    def __init__(
        self,
        check_pass: bool = None,
        sts_role_auth_url: str = None,
        sts_role_name: str = None,
    ):
        self.check_pass = check_pass
        self.sts_role_auth_url = sts_role_auth_url
        self.sts_role_name = sts_role_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_pass is not None:
            result['CheckPass'] = self.check_pass
        if self.sts_role_auth_url is not None:
            result['StsRoleAuthURL'] = self.sts_role_auth_url
        if self.sts_role_name is not None:
            result['StsRoleName'] = self.sts_role_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckPass') is not None:
            self.check_pass = m.get('CheckPass')
        if m.get('StsRoleAuthURL') is not None:
            self.sts_role_auth_url = m.get('StsRoleAuthURL')
        if m.get('StsRoleName') is not None:
            self.sts_role_name = m.get('StsRoleName')
        return self


class CheckRoleForProductResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CheckRoleForProductResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = CheckRoleForProductResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CheckRoleForProductResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CheckRoleForProductResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = CheckRoleForProductResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckRoleForTargetRequest(TeaModel):
    def __init__(
        self,
        target_type: str = None,
    ):
        self.target_type = target_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        return self


class CheckRoleForTargetResponseBodyData(TeaModel):
    def __init__(
        self,
        check_pass: bool = None,
        sts_role_auth_url: str = None,
        sts_role_name: str = None,
    ):
        self.check_pass = check_pass
        self.sts_role_auth_url = sts_role_auth_url
        self.sts_role_name = sts_role_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_pass is not None:
            result['CheckPass'] = self.check_pass
        if self.sts_role_auth_url is not None:
            result['StsRoleAuthURL'] = self.sts_role_auth_url
        if self.sts_role_name is not None:
            result['StsRoleName'] = self.sts_role_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckPass') is not None:
            self.check_pass = m.get('CheckPass')
        if m.get('StsRoleAuthURL') is not None:
            self.sts_role_auth_url = m.get('StsRoleAuthURL')
        if m.get('StsRoleName') is not None:
            self.sts_role_name = m.get('StsRoleName')
        return self


class CheckRoleForTargetResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CheckRoleForTargetResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = CheckRoleForTargetResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CheckRoleForTargetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CheckRoleForTargetResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = CheckRoleForTargetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckServiceLinkedRoleForDeleteRequest(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        deletion_task_id: str = None,
        service_name: str = None,
    ):
        self.account_id = account_id
        self.deletion_task_id = deletion_task_id
        self.service_name = service_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.deletion_task_id is not None:
            result['DeletionTaskId'] = self.deletion_task_id
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('DeletionTaskId') is not None:
            self.deletion_task_id = m.get('DeletionTaskId')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        return self


class CheckServiceLinkedRoleForDeleteResponseBodyRoleUsages(TeaModel):
    def __init__(
        self,
        region: str = None,
        resources: List[str] = None,
    ):
        self.region = region
        self.resources = resources

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region is not None:
            result['Region'] = self.region
        if self.resources is not None:
            result['Resources'] = self.resources
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Resources') is not None:
            self.resources = m.get('Resources')
        return self


class CheckServiceLinkedRoleForDeleteResponseBody(TeaModel):
    def __init__(
        self,
        deletable: bool = None,
        request_id: str = None,
        role_usages: List[CheckServiceLinkedRoleForDeleteResponseBodyRoleUsages] = None,
    ):
        self.deletable = deletable
        self.request_id = request_id
        self.role_usages = role_usages

    def validate(self):
        if self.role_usages:
            for k in self.role_usages:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deletable is not None:
            result['Deletable'] = self.deletable
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['RoleUsages'] = []
        if self.role_usages is not None:
            for k in self.role_usages:
                result['RoleUsages'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Deletable') is not None:
            self.deletable = m.get('Deletable')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.role_usages = []
        if m.get('RoleUsages') is not None:
            for k in m.get('RoleUsages'):
                temp_model = CheckServiceLinkedRoleForDeleteResponseBodyRoleUsages()
                self.role_usages.append(temp_model.from_map(k))
        return self


class CheckServiceLinkedRoleForDeleteResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CheckServiceLinkedRoleForDeleteResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = CheckServiceLinkedRoleForDeleteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CompleteCommodityRequest(TeaModel):
    def __init__(
        self,
        data: str = None,
    ):
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class CompleteCommodityResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        synchro: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success
        self.synchro = synchro

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.synchro is not None:
            result['Synchro'] = self.synchro
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Synchro') is not None:
            self.synchro = m.get('Synchro')
        return self


class CompleteCommodityResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CompleteCommodityResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = CompleteCommodityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CompleteOrderParamRequest(TeaModel):
    def __init__(
        self,
        data: str = None,
    ):
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class CompleteOrderParamResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        synchro: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success
        self.synchro = synchro

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.synchro is not None:
            result['Synchro'] = self.synchro
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Synchro') is not None:
            self.synchro = m.get('Synchro')
        return self


class CompleteOrderParamResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CompleteOrderParamResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = CompleteOrderParamResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateEventBusRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        description: str = None,
        event_bus_name: str = None,
    ):
        self.client_token = client_token
        self.description = description
        self.event_bus_name = event_bus_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')
        return self


class CreateEventBusResponseBodyData(TeaModel):
    def __init__(
        self,
        event_bus_arn: str = None,
    ):
        self.event_bus_arn = event_bus_arn

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_bus_arn is not None:
            result['EventBusARN'] = self.event_bus_arn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventBusARN') is not None:
            self.event_bus_arn = m.get('EventBusARN')
        return self


class CreateEventBusResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CreateEventBusResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = CreateEventBusResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateEventBusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateEventBusResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = CreateEventBusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateEventSourceRequest(TeaModel):
    def __init__(
        self,
        description: bytes = None,
        event_bus_name: bytes = None,
        event_source_name: bytes = None,
        external_source_config: Dict[str, Any] = None,
        external_source_type: bytes = None,
        linked_external_source: bool = None,
    ):
        # 事件源描述详情
        self.description = description
        self.event_bus_name = event_bus_name
        # 事件源英文Code
        self.event_source_name = event_source_name
        self.external_source_config = external_source_config
        self.external_source_type = external_source_type
        self.linked_external_source = linked_external_source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name
        if self.event_source_name is not None:
            result['EventSourceName'] = self.event_source_name
        if self.external_source_config is not None:
            result['ExternalSourceConfig'] = self.external_source_config
        if self.external_source_type is not None:
            result['ExternalSourceType'] = self.external_source_type
        if self.linked_external_source is not None:
            result['LinkedExternalSource'] = self.linked_external_source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')
        if m.get('EventSourceName') is not None:
            self.event_source_name = m.get('EventSourceName')
        if m.get('ExternalSourceConfig') is not None:
            self.external_source_config = m.get('ExternalSourceConfig')
        if m.get('ExternalSourceType') is not None:
            self.external_source_type = m.get('ExternalSourceType')
        if m.get('LinkedExternalSource') is not None:
            self.linked_external_source = m.get('LinkedExternalSource')
        return self


class CreateEventSourceShrinkRequest(TeaModel):
    def __init__(
        self,
        description: bytes = None,
        event_bus_name: bytes = None,
        event_source_name: bytes = None,
        external_source_config_shrink: str = None,
        external_source_type: bytes = None,
        linked_external_source: bool = None,
    ):
        # 事件源描述详情
        self.description = description
        self.event_bus_name = event_bus_name
        # 事件源英文Code
        self.event_source_name = event_source_name
        self.external_source_config_shrink = external_source_config_shrink
        self.external_source_type = external_source_type
        self.linked_external_source = linked_external_source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name
        if self.event_source_name is not None:
            result['EventSourceName'] = self.event_source_name
        if self.external_source_config_shrink is not None:
            result['ExternalSourceConfig'] = self.external_source_config_shrink
        if self.external_source_type is not None:
            result['ExternalSourceType'] = self.external_source_type
        if self.linked_external_source is not None:
            result['LinkedExternalSource'] = self.linked_external_source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')
        if m.get('EventSourceName') is not None:
            self.event_source_name = m.get('EventSourceName')
        if m.get('ExternalSourceConfig') is not None:
            self.external_source_config_shrink = m.get('ExternalSourceConfig')
        if m.get('ExternalSourceType') is not None:
            self.external_source_type = m.get('ExternalSourceType')
        if m.get('LinkedExternalSource') is not None:
            self.linked_external_source = m.get('LinkedExternalSource')
        return self


class CreateEventSourceResponseBodyData(TeaModel):
    def __init__(
        self,
        event_source_arn: str = None,
    ):
        self.event_source_arn = event_source_arn

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_source_arn is not None:
            result['EventSourceARN'] = self.event_source_arn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventSourceARN') is not None:
            self.event_source_arn = m.get('EventSourceARN')
        return self


class CreateEventSourceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CreateEventSourceResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = CreateEventSourceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateEventSourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateEventSourceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = CreateEventSourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateEventStreamingRequestRunOptionsBatchWindow(TeaModel):
    def __init__(
        self,
        count_based_window: int = None,
        time_based_window: int = None,
    ):
        self.count_based_window = count_based_window
        self.time_based_window = time_based_window

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count_based_window is not None:
            result['CountBasedWindow'] = self.count_based_window
        if self.time_based_window is not None:
            result['TimeBasedWindow'] = self.time_based_window
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CountBasedWindow') is not None:
            self.count_based_window = m.get('CountBasedWindow')
        if m.get('TimeBasedWindow') is not None:
            self.time_based_window = m.get('TimeBasedWindow')
        return self


class CreateEventStreamingRequestRunOptionsDeadLetterQueue(TeaModel):
    def __init__(
        self,
        arn: str = None,
    ):
        self.arn = arn

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arn is not None:
            result['Arn'] = self.arn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        return self


class CreateEventStreamingRequestRunOptionsRetryStrategy(TeaModel):
    def __init__(
        self,
        maximum_event_age_in_seconds: int = None,
        maximum_retry_attempts: int = None,
        push_retry_strategy: str = None,
    ):
        self.maximum_event_age_in_seconds = maximum_event_age_in_seconds
        self.maximum_retry_attempts = maximum_retry_attempts
        self.push_retry_strategy = push_retry_strategy

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.maximum_event_age_in_seconds is not None:
            result['MaximumEventAgeInSeconds'] = self.maximum_event_age_in_seconds
        if self.maximum_retry_attempts is not None:
            result['MaximumRetryAttempts'] = self.maximum_retry_attempts
        if self.push_retry_strategy is not None:
            result['PushRetryStrategy'] = self.push_retry_strategy
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaximumEventAgeInSeconds') is not None:
            self.maximum_event_age_in_seconds = m.get('MaximumEventAgeInSeconds')
        if m.get('MaximumRetryAttempts') is not None:
            self.maximum_retry_attempts = m.get('MaximumRetryAttempts')
        if m.get('PushRetryStrategy') is not None:
            self.push_retry_strategy = m.get('PushRetryStrategy')
        return self


class CreateEventStreamingRequestRunOptions(TeaModel):
    def __init__(
        self,
        batch_window: CreateEventStreamingRequestRunOptionsBatchWindow = None,
        dead_letter_queue: CreateEventStreamingRequestRunOptionsDeadLetterQueue = None,
        errors_tolerance: str = None,
        maximum_tasks: int = None,
        retry_strategy: CreateEventStreamingRequestRunOptionsRetryStrategy = None,
    ):
        self.batch_window = batch_window
        self.dead_letter_queue = dead_letter_queue
        self.errors_tolerance = errors_tolerance
        self.maximum_tasks = maximum_tasks
        self.retry_strategy = retry_strategy

    def validate(self):
        if self.batch_window:
            self.batch_window.validate()
        if self.dead_letter_queue:
            self.dead_letter_queue.validate()
        if self.retry_strategy:
            self.retry_strategy.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.batch_window is not None:
            result['BatchWindow'] = self.batch_window.to_map()
        if self.dead_letter_queue is not None:
            result['DeadLetterQueue'] = self.dead_letter_queue.to_map()
        if self.errors_tolerance is not None:
            result['ErrorsTolerance'] = self.errors_tolerance
        if self.maximum_tasks is not None:
            result['MaximumTasks'] = self.maximum_tasks
        if self.retry_strategy is not None:
            result['RetryStrategy'] = self.retry_strategy.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BatchWindow') is not None:
            temp_model = CreateEventStreamingRequestRunOptionsBatchWindow()
            self.batch_window = temp_model.from_map(m['BatchWindow'])
        if m.get('DeadLetterQueue') is not None:
            temp_model = CreateEventStreamingRequestRunOptionsDeadLetterQueue()
            self.dead_letter_queue = temp_model.from_map(m['DeadLetterQueue'])
        if m.get('ErrorsTolerance') is not None:
            self.errors_tolerance = m.get('ErrorsTolerance')
        if m.get('MaximumTasks') is not None:
            self.maximum_tasks = m.get('MaximumTasks')
        if m.get('RetryStrategy') is not None:
            temp_model = CreateEventStreamingRequestRunOptionsRetryStrategy()
            self.retry_strategy = temp_model.from_map(m['RetryStrategy'])
        return self


class CreateEventStreamingRequestSinkSinkFcParametersBody(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkFcParametersFunctionName(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkFcParametersInvocationType(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkFcParametersQualifier(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkFcParametersServiceName(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkFcParameters(TeaModel):
    def __init__(
        self,
        body: CreateEventStreamingRequestSinkSinkFcParametersBody = None,
        function_name: CreateEventStreamingRequestSinkSinkFcParametersFunctionName = None,
        invocation_type: CreateEventStreamingRequestSinkSinkFcParametersInvocationType = None,
        qualifier: CreateEventStreamingRequestSinkSinkFcParametersQualifier = None,
        service_name: CreateEventStreamingRequestSinkSinkFcParametersServiceName = None,
    ):
        self.body = body
        self.function_name = function_name
        self.invocation_type = invocation_type
        self.qualifier = qualifier
        self.service_name = service_name

    def validate(self):
        if self.body:
            self.body.validate()
        if self.function_name:
            self.function_name.validate()
        if self.invocation_type:
            self.invocation_type.validate()
        if self.qualifier:
            self.qualifier.validate()
        if self.service_name:
            self.service_name.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['Body'] = self.body.to_map()
        if self.function_name is not None:
            result['FunctionName'] = self.function_name.to_map()
        if self.invocation_type is not None:
            result['InvocationType'] = self.invocation_type.to_map()
        if self.qualifier is not None:
            result['Qualifier'] = self.qualifier.to_map()
        if self.service_name is not None:
            result['ServiceName'] = self.service_name.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Body') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkFcParametersBody()
            self.body = temp_model.from_map(m['Body'])
        if m.get('FunctionName') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkFcParametersFunctionName()
            self.function_name = temp_model.from_map(m['FunctionName'])
        if m.get('InvocationType') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkFcParametersInvocationType()
            self.invocation_type = temp_model.from_map(m['InvocationType'])
        if m.get('Qualifier') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkFcParametersQualifier()
            self.qualifier = temp_model.from_map(m['Qualifier'])
        if m.get('ServiceName') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkFcParametersServiceName()
            self.service_name = temp_model.from_map(m['ServiceName'])
        return self


class CreateEventStreamingRequestSinkSinkKafkaParametersAcks(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkKafkaParametersInstanceId(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkKafkaParametersKey(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkKafkaParametersSaslUser(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkKafkaParametersTopic(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkKafkaParametersValue(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkKafkaParameters(TeaModel):
    def __init__(
        self,
        acks: CreateEventStreamingRequestSinkSinkKafkaParametersAcks = None,
        instance_id: CreateEventStreamingRequestSinkSinkKafkaParametersInstanceId = None,
        key: CreateEventStreamingRequestSinkSinkKafkaParametersKey = None,
        sasl_user: CreateEventStreamingRequestSinkSinkKafkaParametersSaslUser = None,
        topic: CreateEventStreamingRequestSinkSinkKafkaParametersTopic = None,
        value: CreateEventStreamingRequestSinkSinkKafkaParametersValue = None,
    ):
        self.acks = acks
        self.instance_id = instance_id
        self.key = key
        self.sasl_user = sasl_user
        self.topic = topic
        self.value = value

    def validate(self):
        if self.acks:
            self.acks.validate()
        if self.instance_id:
            self.instance_id.validate()
        if self.key:
            self.key.validate()
        if self.sasl_user:
            self.sasl_user.validate()
        if self.topic:
            self.topic.validate()
        if self.value:
            self.value.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acks is not None:
            result['Acks'] = self.acks.to_map()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id.to_map()
        if self.key is not None:
            result['Key'] = self.key.to_map()
        if self.sasl_user is not None:
            result['SaslUser'] = self.sasl_user.to_map()
        if self.topic is not None:
            result['Topic'] = self.topic.to_map()
        if self.value is not None:
            result['Value'] = self.value.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Acks') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkKafkaParametersAcks()
            self.acks = temp_model.from_map(m['Acks'])
        if m.get('InstanceId') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkKafkaParametersInstanceId()
            self.instance_id = temp_model.from_map(m['InstanceId'])
        if m.get('Key') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkKafkaParametersKey()
            self.key = temp_model.from_map(m['Key'])
        if m.get('SaslUser') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkKafkaParametersSaslUser()
            self.sasl_user = temp_model.from_map(m['SaslUser'])
        if m.get('Topic') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkKafkaParametersTopic()
            self.topic = temp_model.from_map(m['Topic'])
        if m.get('Value') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkKafkaParametersValue()
            self.value = temp_model.from_map(m['Value'])
        return self


class CreateEventStreamingRequestSinkSinkMNSParametersBody(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkMNSParametersIsBase64Encode(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkMNSParametersQueueName(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkMNSParameters(TeaModel):
    def __init__(
        self,
        body: CreateEventStreamingRequestSinkSinkMNSParametersBody = None,
        is_base_64encode: CreateEventStreamingRequestSinkSinkMNSParametersIsBase64Encode = None,
        queue_name: CreateEventStreamingRequestSinkSinkMNSParametersQueueName = None,
    ):
        self.body = body
        self.is_base_64encode = is_base_64encode
        self.queue_name = queue_name

    def validate(self):
        if self.body:
            self.body.validate()
        if self.is_base_64encode:
            self.is_base_64encode.validate()
        if self.queue_name:
            self.queue_name.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['Body'] = self.body.to_map()
        if self.is_base_64encode is not None:
            result['IsBase64Encode'] = self.is_base_64encode.to_map()
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Body') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkMNSParametersBody()
            self.body = temp_model.from_map(m['Body'])
        if m.get('IsBase64Encode') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkMNSParametersIsBase64Encode()
            self.is_base_64encode = temp_model.from_map(m['IsBase64Encode'])
        if m.get('QueueName') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkMNSParametersQueueName()
            self.queue_name = temp_model.from_map(m['QueueName'])
        return self


class CreateEventStreamingRequestSinkSinkRabbitMQParametersBody(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkRabbitMQParametersExchange(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkRabbitMQParametersInstanceId(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkRabbitMQParametersMessageId(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkRabbitMQParametersProperties(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkRabbitMQParametersQueueName(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkRabbitMQParametersRoutingKey(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkRabbitMQParametersTargetType(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkRabbitMQParametersVirtualHostName(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkRabbitMQParameters(TeaModel):
    def __init__(
        self,
        body: CreateEventStreamingRequestSinkSinkRabbitMQParametersBody = None,
        exchange: CreateEventStreamingRequestSinkSinkRabbitMQParametersExchange = None,
        instance_id: CreateEventStreamingRequestSinkSinkRabbitMQParametersInstanceId = None,
        message_id: CreateEventStreamingRequestSinkSinkRabbitMQParametersMessageId = None,
        properties: CreateEventStreamingRequestSinkSinkRabbitMQParametersProperties = None,
        queue_name: CreateEventStreamingRequestSinkSinkRabbitMQParametersQueueName = None,
        routing_key: CreateEventStreamingRequestSinkSinkRabbitMQParametersRoutingKey = None,
        target_type: CreateEventStreamingRequestSinkSinkRabbitMQParametersTargetType = None,
        virtual_host_name: CreateEventStreamingRequestSinkSinkRabbitMQParametersVirtualHostName = None,
    ):
        self.body = body
        self.exchange = exchange
        self.instance_id = instance_id
        self.message_id = message_id
        self.properties = properties
        self.queue_name = queue_name
        self.routing_key = routing_key
        self.target_type = target_type
        self.virtual_host_name = virtual_host_name

    def validate(self):
        if self.body:
            self.body.validate()
        if self.exchange:
            self.exchange.validate()
        if self.instance_id:
            self.instance_id.validate()
        if self.message_id:
            self.message_id.validate()
        if self.properties:
            self.properties.validate()
        if self.queue_name:
            self.queue_name.validate()
        if self.routing_key:
            self.routing_key.validate()
        if self.target_type:
            self.target_type.validate()
        if self.virtual_host_name:
            self.virtual_host_name.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['Body'] = self.body.to_map()
        if self.exchange is not None:
            result['Exchange'] = self.exchange.to_map()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id.to_map()
        if self.message_id is not None:
            result['MessageId'] = self.message_id.to_map()
        if self.properties is not None:
            result['Properties'] = self.properties.to_map()
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name.to_map()
        if self.routing_key is not None:
            result['RoutingKey'] = self.routing_key.to_map()
        if self.target_type is not None:
            result['TargetType'] = self.target_type.to_map()
        if self.virtual_host_name is not None:
            result['VirtualHostName'] = self.virtual_host_name.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Body') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkRabbitMQParametersBody()
            self.body = temp_model.from_map(m['Body'])
        if m.get('Exchange') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkRabbitMQParametersExchange()
            self.exchange = temp_model.from_map(m['Exchange'])
        if m.get('InstanceId') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkRabbitMQParametersInstanceId()
            self.instance_id = temp_model.from_map(m['InstanceId'])
        if m.get('MessageId') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkRabbitMQParametersMessageId()
            self.message_id = temp_model.from_map(m['MessageId'])
        if m.get('Properties') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkRabbitMQParametersProperties()
            self.properties = temp_model.from_map(m['Properties'])
        if m.get('QueueName') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkRabbitMQParametersQueueName()
            self.queue_name = temp_model.from_map(m['QueueName'])
        if m.get('RoutingKey') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkRabbitMQParametersRoutingKey()
            self.routing_key = temp_model.from_map(m['RoutingKey'])
        if m.get('TargetType') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkRabbitMQParametersTargetType()
            self.target_type = temp_model.from_map(m['TargetType'])
        if m.get('VirtualHostName') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkRabbitMQParametersVirtualHostName()
            self.virtual_host_name = temp_model.from_map(m['VirtualHostName'])
        return self


class CreateEventStreamingRequestSinkSinkRocketMQParametersBody(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkRocketMQParametersInstanceId(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkRocketMQParametersKeys(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkRocketMQParametersProperties(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkRocketMQParametersTags(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkRocketMQParametersTopic(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkRocketMQParameters(TeaModel):
    def __init__(
        self,
        body: CreateEventStreamingRequestSinkSinkRocketMQParametersBody = None,
        instance_id: CreateEventStreamingRequestSinkSinkRocketMQParametersInstanceId = None,
        keys: CreateEventStreamingRequestSinkSinkRocketMQParametersKeys = None,
        properties: CreateEventStreamingRequestSinkSinkRocketMQParametersProperties = None,
        tags: CreateEventStreamingRequestSinkSinkRocketMQParametersTags = None,
        topic: CreateEventStreamingRequestSinkSinkRocketMQParametersTopic = None,
    ):
        self.body = body
        self.instance_id = instance_id
        self.keys = keys
        self.properties = properties
        self.tags = tags
        self.topic = topic

    def validate(self):
        if self.body:
            self.body.validate()
        if self.instance_id:
            self.instance_id.validate()
        if self.keys:
            self.keys.validate()
        if self.properties:
            self.properties.validate()
        if self.tags:
            self.tags.validate()
        if self.topic:
            self.topic.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['Body'] = self.body.to_map()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id.to_map()
        if self.keys is not None:
            result['Keys'] = self.keys.to_map()
        if self.properties is not None:
            result['Properties'] = self.properties.to_map()
        if self.tags is not None:
            result['Tags'] = self.tags.to_map()
        if self.topic is not None:
            result['Topic'] = self.topic.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Body') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkRocketMQParametersBody()
            self.body = temp_model.from_map(m['Body'])
        if m.get('InstanceId') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkRocketMQParametersInstanceId()
            self.instance_id = temp_model.from_map(m['InstanceId'])
        if m.get('Keys') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkRocketMQParametersKeys()
            self.keys = temp_model.from_map(m['Keys'])
        if m.get('Properties') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkRocketMQParametersProperties()
            self.properties = temp_model.from_map(m['Properties'])
        if m.get('Tags') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkRocketMQParametersTags()
            self.tags = temp_model.from_map(m['Tags'])
        if m.get('Topic') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkRocketMQParametersTopic()
            self.topic = temp_model.from_map(m['Topic'])
        return self


class CreateEventStreamingRequestSinkSinkSLSParametersBody(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkSLSParametersLogStore(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkSLSParametersProject(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkSLSParametersRoleName(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkSLSParametersTopic(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkSLSParameters(TeaModel):
    def __init__(
        self,
        body: CreateEventStreamingRequestSinkSinkSLSParametersBody = None,
        log_store: CreateEventStreamingRequestSinkSinkSLSParametersLogStore = None,
        project: CreateEventStreamingRequestSinkSinkSLSParametersProject = None,
        role_name: CreateEventStreamingRequestSinkSinkSLSParametersRoleName = None,
        topic: CreateEventStreamingRequestSinkSinkSLSParametersTopic = None,
    ):
        self.body = body
        self.log_store = log_store
        self.project = project
        self.role_name = role_name
        self.topic = topic

    def validate(self):
        if self.body:
            self.body.validate()
        if self.log_store:
            self.log_store.validate()
        if self.project:
            self.project.validate()
        if self.role_name:
            self.role_name.validate()
        if self.topic:
            self.topic.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['Body'] = self.body.to_map()
        if self.log_store is not None:
            result['LogStore'] = self.log_store.to_map()
        if self.project is not None:
            result['Project'] = self.project.to_map()
        if self.role_name is not None:
            result['RoleName'] = self.role_name.to_map()
        if self.topic is not None:
            result['Topic'] = self.topic.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Body') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkSLSParametersBody()
            self.body = temp_model.from_map(m['Body'])
        if m.get('LogStore') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkSLSParametersLogStore()
            self.log_store = temp_model.from_map(m['LogStore'])
        if m.get('Project') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkSLSParametersProject()
            self.project = temp_model.from_map(m['Project'])
        if m.get('RoleName') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkSLSParametersRoleName()
            self.role_name = temp_model.from_map(m['RoleName'])
        if m.get('Topic') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkSLSParametersTopic()
            self.topic = temp_model.from_map(m['Topic'])
        return self


class CreateEventStreamingRequestSink(TeaModel):
    def __init__(
        self,
        sink_fc_parameters: CreateEventStreamingRequestSinkSinkFcParameters = None,
        sink_kafka_parameters: CreateEventStreamingRequestSinkSinkKafkaParameters = None,
        sink_mnsparameters: CreateEventStreamingRequestSinkSinkMNSParameters = None,
        sink_rabbit_mqparameters: CreateEventStreamingRequestSinkSinkRabbitMQParameters = None,
        sink_rocket_mqparameters: CreateEventStreamingRequestSinkSinkRocketMQParameters = None,
        sink_slsparameters: CreateEventStreamingRequestSinkSinkSLSParameters = None,
    ):
        self.sink_fc_parameters = sink_fc_parameters
        self.sink_kafka_parameters = sink_kafka_parameters
        self.sink_mnsparameters = sink_mnsparameters
        self.sink_rabbit_mqparameters = sink_rabbit_mqparameters
        self.sink_rocket_mqparameters = sink_rocket_mqparameters
        self.sink_slsparameters = sink_slsparameters

    def validate(self):
        if self.sink_fc_parameters:
            self.sink_fc_parameters.validate()
        if self.sink_kafka_parameters:
            self.sink_kafka_parameters.validate()
        if self.sink_mnsparameters:
            self.sink_mnsparameters.validate()
        if self.sink_rabbit_mqparameters:
            self.sink_rabbit_mqparameters.validate()
        if self.sink_rocket_mqparameters:
            self.sink_rocket_mqparameters.validate()
        if self.sink_slsparameters:
            self.sink_slsparameters.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sink_fc_parameters is not None:
            result['SinkFcParameters'] = self.sink_fc_parameters.to_map()
        if self.sink_kafka_parameters is not None:
            result['SinkKafkaParameters'] = self.sink_kafka_parameters.to_map()
        if self.sink_mnsparameters is not None:
            result['SinkMNSParameters'] = self.sink_mnsparameters.to_map()
        if self.sink_rabbit_mqparameters is not None:
            result['SinkRabbitMQParameters'] = self.sink_rabbit_mqparameters.to_map()
        if self.sink_rocket_mqparameters is not None:
            result['SinkRocketMQParameters'] = self.sink_rocket_mqparameters.to_map()
        if self.sink_slsparameters is not None:
            result['SinkSLSParameters'] = self.sink_slsparameters.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SinkFcParameters') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkFcParameters()
            self.sink_fc_parameters = temp_model.from_map(m['SinkFcParameters'])
        if m.get('SinkKafkaParameters') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkKafkaParameters()
            self.sink_kafka_parameters = temp_model.from_map(m['SinkKafkaParameters'])
        if m.get('SinkMNSParameters') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkMNSParameters()
            self.sink_mnsparameters = temp_model.from_map(m['SinkMNSParameters'])
        if m.get('SinkRabbitMQParameters') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkRabbitMQParameters()
            self.sink_rabbit_mqparameters = temp_model.from_map(m['SinkRabbitMQParameters'])
        if m.get('SinkRocketMQParameters') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkRocketMQParameters()
            self.sink_rocket_mqparameters = temp_model.from_map(m['SinkRocketMQParameters'])
        if m.get('SinkSLSParameters') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkSLSParameters()
            self.sink_slsparameters = temp_model.from_map(m['SinkSLSParameters'])
        return self


class CreateEventStreamingRequestSourceSourceDTSParameters(TeaModel):
    def __init__(
        self,
        broker_url: str = None,
        init_check_point: int = None,
        password: str = None,
        sid: str = None,
        task_id: str = None,
        topic: str = None,
        username: str = None,
    ):
        self.broker_url = broker_url
        self.init_check_point = init_check_point
        self.password = password
        self.sid = sid
        self.task_id = task_id
        self.topic = topic
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.broker_url is not None:
            result['BrokerUrl'] = self.broker_url
        if self.init_check_point is not None:
            result['InitCheckPoint'] = self.init_check_point
        if self.password is not None:
            result['Password'] = self.password
        if self.sid is not None:
            result['Sid'] = self.sid
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.topic is not None:
            result['Topic'] = self.topic
        if self.username is not None:
            result['Username'] = self.username
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BrokerUrl') is not None:
            self.broker_url = m.get('BrokerUrl')
        if m.get('InitCheckPoint') is not None:
            self.init_check_point = m.get('InitCheckPoint')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('Sid') is not None:
            self.sid = m.get('Sid')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        return self


class CreateEventStreamingRequestSourceSourceKafkaParameters(TeaModel):
    def __init__(
        self,
        consumer_group: str = None,
        instance_id: str = None,
        network: str = None,
        offset_reset: str = None,
        region_id: str = None,
        security_group_id: str = None,
        topic: str = None,
        v_switch_ids: str = None,
        vpc_id: str = None,
    ):
        self.consumer_group = consumer_group
        self.instance_id = instance_id
        self.network = network
        self.offset_reset = offset_reset
        self.region_id = region_id
        self.security_group_id = security_group_id
        self.topic = topic
        self.v_switch_ids = v_switch_ids
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consumer_group is not None:
            result['ConsumerGroup'] = self.consumer_group
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.network is not None:
            result['Network'] = self.network
        if self.offset_reset is not None:
            result['OffsetReset'] = self.offset_reset
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.topic is not None:
            result['Topic'] = self.topic
        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsumerGroup') is not None:
            self.consumer_group = m.get('ConsumerGroup')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Network') is not None:
            self.network = m.get('Network')
        if m.get('OffsetReset') is not None:
            self.offset_reset = m.get('OffsetReset')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class CreateEventStreamingRequestSourceSourceMNSParameters(TeaModel):
    def __init__(
        self,
        is_base_64decode: bool = None,
        queue_name: str = None,
        region_id: str = None,
    ):
        self.is_base_64decode = is_base_64decode
        self.queue_name = queue_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_base_64decode is not None:
            result['IsBase64Decode'] = self.is_base_64decode
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsBase64Decode') is not None:
            self.is_base_64decode = m.get('IsBase64Decode')
        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CreateEventStreamingRequestSourceSourceMQTTParameters(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        region_id: str = None,
        topic: str = None,
    ):
        self.instance_id = instance_id
        self.region_id = region_id
        self.topic = topic

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.topic is not None:
            result['Topic'] = self.topic
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        return self


class CreateEventStreamingRequestSourceSourceRabbitMQParameters(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        queue_name: str = None,
        region_id: str = None,
        virtual_host_name: str = None,
    ):
        self.instance_id = instance_id
        self.queue_name = queue_name
        self.region_id = region_id
        self.virtual_host_name = virtual_host_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.virtual_host_name is not None:
            result['VirtualHostName'] = self.virtual_host_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VirtualHostName') is not None:
            self.virtual_host_name = m.get('VirtualHostName')
        return self


class CreateEventStreamingRequestSourceSourceRocketMQParameters(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        instance_id: str = None,
        offset: str = None,
        region_id: str = None,
        tag: str = None,
        timestamp: int = None,
        topic: str = None,
    ):
        self.group_id = group_id
        self.instance_id = instance_id
        self.offset = offset
        self.region_id = region_id
        self.tag = tag
        self.timestamp = timestamp
        self.topic = topic

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupID'] = self.group_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.offset is not None:
            result['Offset'] = self.offset
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.topic is not None:
            result['Topic'] = self.topic
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupID') is not None:
            self.group_id = m.get('GroupID')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Offset') is not None:
            self.offset = m.get('Offset')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        return self


class CreateEventStreamingRequestSourceSourceSLSParameters(TeaModel):
    def __init__(
        self,
        consume_position: str = None,
        log_store: str = None,
        project: str = None,
        role_name: str = None,
    ):
        self.consume_position = consume_position
        self.log_store = log_store
        self.project = project
        self.role_name = role_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consume_position is not None:
            result['ConsumePosition'] = self.consume_position
        if self.log_store is not None:
            result['LogStore'] = self.log_store
        if self.project is not None:
            result['Project'] = self.project
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsumePosition') is not None:
            self.consume_position = m.get('ConsumePosition')
        if m.get('LogStore') is not None:
            self.log_store = m.get('LogStore')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        return self


class CreateEventStreamingRequestSource(TeaModel):
    def __init__(
        self,
        source_dtsparameters: CreateEventStreamingRequestSourceSourceDTSParameters = None,
        source_kafka_parameters: CreateEventStreamingRequestSourceSourceKafkaParameters = None,
        source_mnsparameters: CreateEventStreamingRequestSourceSourceMNSParameters = None,
        source_mqttparameters: CreateEventStreamingRequestSourceSourceMQTTParameters = None,
        source_rabbit_mqparameters: CreateEventStreamingRequestSourceSourceRabbitMQParameters = None,
        source_rocket_mqparameters: CreateEventStreamingRequestSourceSourceRocketMQParameters = None,
        source_slsparameters: CreateEventStreamingRequestSourceSourceSLSParameters = None,
    ):
        self.source_dtsparameters = source_dtsparameters
        self.source_kafka_parameters = source_kafka_parameters
        self.source_mnsparameters = source_mnsparameters
        self.source_mqttparameters = source_mqttparameters
        self.source_rabbit_mqparameters = source_rabbit_mqparameters
        self.source_rocket_mqparameters = source_rocket_mqparameters
        self.source_slsparameters = source_slsparameters

    def validate(self):
        if self.source_dtsparameters:
            self.source_dtsparameters.validate()
        if self.source_kafka_parameters:
            self.source_kafka_parameters.validate()
        if self.source_mnsparameters:
            self.source_mnsparameters.validate()
        if self.source_mqttparameters:
            self.source_mqttparameters.validate()
        if self.source_rabbit_mqparameters:
            self.source_rabbit_mqparameters.validate()
        if self.source_rocket_mqparameters:
            self.source_rocket_mqparameters.validate()
        if self.source_slsparameters:
            self.source_slsparameters.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_dtsparameters is not None:
            result['SourceDTSParameters'] = self.source_dtsparameters.to_map()
        if self.source_kafka_parameters is not None:
            result['SourceKafkaParameters'] = self.source_kafka_parameters.to_map()
        if self.source_mnsparameters is not None:
            result['SourceMNSParameters'] = self.source_mnsparameters.to_map()
        if self.source_mqttparameters is not None:
            result['SourceMQTTParameters'] = self.source_mqttparameters.to_map()
        if self.source_rabbit_mqparameters is not None:
            result['SourceRabbitMQParameters'] = self.source_rabbit_mqparameters.to_map()
        if self.source_rocket_mqparameters is not None:
            result['SourceRocketMQParameters'] = self.source_rocket_mqparameters.to_map()
        if self.source_slsparameters is not None:
            result['SourceSLSParameters'] = self.source_slsparameters.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceDTSParameters') is not None:
            temp_model = CreateEventStreamingRequestSourceSourceDTSParameters()
            self.source_dtsparameters = temp_model.from_map(m['SourceDTSParameters'])
        if m.get('SourceKafkaParameters') is not None:
            temp_model = CreateEventStreamingRequestSourceSourceKafkaParameters()
            self.source_kafka_parameters = temp_model.from_map(m['SourceKafkaParameters'])
        if m.get('SourceMNSParameters') is not None:
            temp_model = CreateEventStreamingRequestSourceSourceMNSParameters()
            self.source_mnsparameters = temp_model.from_map(m['SourceMNSParameters'])
        if m.get('SourceMQTTParameters') is not None:
            temp_model = CreateEventStreamingRequestSourceSourceMQTTParameters()
            self.source_mqttparameters = temp_model.from_map(m['SourceMQTTParameters'])
        if m.get('SourceRabbitMQParameters') is not None:
            temp_model = CreateEventStreamingRequestSourceSourceRabbitMQParameters()
            self.source_rabbit_mqparameters = temp_model.from_map(m['SourceRabbitMQParameters'])
        if m.get('SourceRocketMQParameters') is not None:
            temp_model = CreateEventStreamingRequestSourceSourceRocketMQParameters()
            self.source_rocket_mqparameters = temp_model.from_map(m['SourceRocketMQParameters'])
        if m.get('SourceSLSParameters') is not None:
            temp_model = CreateEventStreamingRequestSourceSourceSLSParameters()
            self.source_slsparameters = temp_model.from_map(m['SourceSLSParameters'])
        return self


class CreateEventStreamingRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        event_streaming_name: str = None,
        filter_pattern: str = None,
        run_options: CreateEventStreamingRequestRunOptions = None,
        sink: CreateEventStreamingRequestSink = None,
        source: CreateEventStreamingRequestSource = None,
        tag: str = None,
    ):
        self.description = description
        self.event_streaming_name = event_streaming_name
        self.filter_pattern = filter_pattern
        self.run_options = run_options
        self.sink = sink
        self.source = source
        self.tag = tag

    def validate(self):
        if self.run_options:
            self.run_options.validate()
        if self.sink:
            self.sink.validate()
        if self.source:
            self.source.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.event_streaming_name is not None:
            result['EventStreamingName'] = self.event_streaming_name
        if self.filter_pattern is not None:
            result['FilterPattern'] = self.filter_pattern
        if self.run_options is not None:
            result['RunOptions'] = self.run_options.to_map()
        if self.sink is not None:
            result['Sink'] = self.sink.to_map()
        if self.source is not None:
            result['Source'] = self.source.to_map()
        if self.tag is not None:
            result['Tag'] = self.tag
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EventStreamingName') is not None:
            self.event_streaming_name = m.get('EventStreamingName')
        if m.get('FilterPattern') is not None:
            self.filter_pattern = m.get('FilterPattern')
        if m.get('RunOptions') is not None:
            temp_model = CreateEventStreamingRequestRunOptions()
            self.run_options = temp_model.from_map(m['RunOptions'])
        if m.get('Sink') is not None:
            temp_model = CreateEventStreamingRequestSink()
            self.sink = temp_model.from_map(m['Sink'])
        if m.get('Source') is not None:
            temp_model = CreateEventStreamingRequestSource()
            self.source = temp_model.from_map(m['Source'])
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        return self


class CreateEventStreamingShrinkRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        event_streaming_name: str = None,
        filter_pattern: str = None,
        run_options_shrink: str = None,
        sink_shrink: str = None,
        source_shrink: str = None,
        tag: str = None,
    ):
        self.description = description
        self.event_streaming_name = event_streaming_name
        self.filter_pattern = filter_pattern
        self.run_options_shrink = run_options_shrink
        self.sink_shrink = sink_shrink
        self.source_shrink = source_shrink
        self.tag = tag

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.event_streaming_name is not None:
            result['EventStreamingName'] = self.event_streaming_name
        if self.filter_pattern is not None:
            result['FilterPattern'] = self.filter_pattern
        if self.run_options_shrink is not None:
            result['RunOptions'] = self.run_options_shrink
        if self.sink_shrink is not None:
            result['Sink'] = self.sink_shrink
        if self.source_shrink is not None:
            result['Source'] = self.source_shrink
        if self.tag is not None:
            result['Tag'] = self.tag
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EventStreamingName') is not None:
            self.event_streaming_name = m.get('EventStreamingName')
        if m.get('FilterPattern') is not None:
            self.filter_pattern = m.get('FilterPattern')
        if m.get('RunOptions') is not None:
            self.run_options_shrink = m.get('RunOptions')
        if m.get('Sink') is not None:
            self.sink_shrink = m.get('Sink')
        if m.get('Source') is not None:
            self.source_shrink = m.get('Source')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        return self


class CreateEventStreamingResponseBodyData(TeaModel):
    def __init__(
        self,
        event_streaming_arn: str = None,
    ):
        self.event_streaming_arn = event_streaming_arn

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_streaming_arn is not None:
            result['EventStreamingARN'] = self.event_streaming_arn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventStreamingARN') is not None:
            self.event_streaming_arn = m.get('EventStreamingARN')
        return self


class CreateEventStreamingResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CreateEventStreamingResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = CreateEventStreamingResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateEventStreamingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateEventStreamingResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = CreateEventStreamingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRuleRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        description: str = None,
        event_bus_name: str = None,
        filter_pattern: str = None,
        rule_name: str = None,
        status: str = None,
        targets: Dict[str, Any] = None,
    ):
        self.client_token = client_token
        self.description = description
        self.event_bus_name = event_bus_name
        self.filter_pattern = filter_pattern
        self.rule_name = rule_name
        self.status = status
        self.targets = targets

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name
        if self.filter_pattern is not None:
            result['FilterPattern'] = self.filter_pattern
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.status is not None:
            result['Status'] = self.status
        if self.targets is not None:
            result['Targets'] = self.targets
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')
        if m.get('FilterPattern') is not None:
            self.filter_pattern = m.get('FilterPattern')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Targets') is not None:
            self.targets = m.get('Targets')
        return self


class CreateRuleShrinkRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        description: str = None,
        event_bus_name: str = None,
        filter_pattern: str = None,
        rule_name: str = None,
        status: str = None,
        targets_shrink: str = None,
    ):
        self.client_token = client_token
        self.description = description
        self.event_bus_name = event_bus_name
        self.filter_pattern = filter_pattern
        self.rule_name = rule_name
        self.status = status
        self.targets_shrink = targets_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name
        if self.filter_pattern is not None:
            result['FilterPattern'] = self.filter_pattern
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.status is not None:
            result['Status'] = self.status
        if self.targets_shrink is not None:
            result['Targets'] = self.targets_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')
        if m.get('FilterPattern') is not None:
            self.filter_pattern = m.get('FilterPattern')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Targets') is not None:
            self.targets_shrink = m.get('Targets')
        return self


class CreateRuleResponseBodyData(TeaModel):
    def __init__(
        self,
        rule_arn: str = None,
    ):
        self.rule_arn = rule_arn

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_arn is not None:
            result['RuleARN'] = self.rule_arn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RuleARN') is not None:
            self.rule_arn = m.get('RuleARN')
        return self


class CreateRuleResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CreateRuleResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = CreateRuleResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateRuleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = CreateRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSchemaRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        compatible_type: str = None,
        content: str = None,
        description: str = None,
        group_id: str = None,
        schema_id: str = None,
    ):
        self.client_token = client_token
        # Schema处理版本兼容性的策略
        self.compatible_type = compatible_type
        # Schema创建时间
        self.content = content
        # Schema描述信息
        self.description = description
        # Schema所属注册表
        self.group_id = group_id
        # Schema标识
        self.schema_id = schema_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.compatible_type is not None:
            result['CompatibleType'] = self.compatible_type
        if self.content is not None:
            result['Content'] = self.content
        if self.description is not None:
            result['Description'] = self.description
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.schema_id is not None:
            result['SchemaId'] = self.schema_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('CompatibleType') is not None:
            self.compatible_type = m.get('CompatibleType')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('SchemaId') is not None:
            self.schema_id = m.get('SchemaId')
        return self


class CreateSchemaResponseBodyData(TeaModel):
    def __init__(
        self,
        created_timestamp: int = None,
        schema_arn: str = None,
        version: int = None,
    ):
        self.created_timestamp = created_timestamp
        self.schema_arn = schema_arn
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_timestamp is not None:
            result['CreatedTimestamp'] = self.created_timestamp
        if self.schema_arn is not None:
            result['SchemaARN'] = self.schema_arn
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedTimestamp') is not None:
            self.created_timestamp = m.get('CreatedTimestamp')
        if m.get('SchemaARN') is not None:
            self.schema_arn = m.get('SchemaARN')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class CreateSchemaResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CreateSchemaResponseBodyData = None,
        http_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_code = http_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = CreateSchemaResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateSchemaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateSchemaResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = CreateSchemaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSchemaGroupRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        description: str = None,
        group_id: str = None,
        schema_format: str = None,
    ):
        self.client_token = client_token
        # 代表分组的类别
        self.description = description
        # 代表资源一级ID的资源属性字段
        self.group_id = group_id
        self.schema_format = schema_format

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.schema_format is not None:
            result['SchemaFormat'] = self.schema_format
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('SchemaFormat') is not None:
            self.schema_format = m.get('SchemaFormat')
        return self


class CreateSchemaGroupResponseBodyData(TeaModel):
    def __init__(
        self,
        created_timestamp: int = None,
        group_arn: str = None,
    ):
        self.created_timestamp = created_timestamp
        self.group_arn = group_arn

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_timestamp is not None:
            result['CreatedTimestamp'] = self.created_timestamp
        if self.group_arn is not None:
            result['GroupARN'] = self.group_arn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedTimestamp') is not None:
            self.created_timestamp = m.get('CreatedTimestamp')
        if m.get('GroupARN') is not None:
            self.group_arn = m.get('GroupARN')
        return self


class CreateSchemaGroupResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CreateSchemaGroupResponseBodyData = None,
        http_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_code = http_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = CreateSchemaGroupResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateSchemaGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateSchemaGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = CreateSchemaGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSchemaVersionRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        content: str = None,
        group_id: str = None,
        schema_id: str = None,
    ):
        self.client_token = client_token
        # 具体Schema内容
        self.content = content
        # 所属注册表
        self.group_id = group_id
        # 所属数据模型ID
        self.schema_id = schema_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.content is not None:
            result['Content'] = self.content
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.schema_id is not None:
            result['SchemaId'] = self.schema_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('SchemaId') is not None:
            self.schema_id = m.get('SchemaId')
        return self


class CreateSchemaVersionResponseBodyData(TeaModel):
    def __init__(
        self,
        created_timestamp: int = None,
        schema_version_arn: str = None,
        version: int = None,
    ):
        self.created_timestamp = created_timestamp
        self.schema_version_arn = schema_version_arn
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_timestamp is not None:
            result['CreatedTimestamp'] = self.created_timestamp
        if self.schema_version_arn is not None:
            result['SchemaVersionARN'] = self.schema_version_arn
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedTimestamp') is not None:
            self.created_timestamp = m.get('CreatedTimestamp')
        if m.get('SchemaVersionARN') is not None:
            self.schema_version_arn = m.get('SchemaVersionARN')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class CreateSchemaVersionResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CreateSchemaVersionResponseBodyData = None,
        http_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_code = http_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = CreateSchemaVersionResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateSchemaVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateSchemaVersionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = CreateSchemaVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateServiceLinkedRoleForProductRequest(TeaModel):
    def __init__(
        self,
        product_name: str = None,
    ):
        self.product_name = product_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        return self


class CreateServiceLinkedRoleForProductResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateServiceLinkedRoleForProductResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateServiceLinkedRoleForProductResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = CreateServiceLinkedRoleForProductResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateServiceLinkedRoleForTargetRequest(TeaModel):
    def __init__(
        self,
        target_type: str = None,
    ):
        self.target_type = target_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        return self


class CreateServiceLinkedRoleForTargetResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateServiceLinkedRoleForTargetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateServiceLinkedRoleForTargetResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = CreateServiceLinkedRoleForTargetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteEventBusRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        event_bus_name: str = None,
    ):
        self.client_token = client_token
        self.event_bus_name = event_bus_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')
        return self


class DeleteEventBusResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteEventBusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteEventBusResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DeleteEventBusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteEventSourceRequest(TeaModel):
    def __init__(
        self,
        event_source_name: str = None,
    ):
        # 事件源ID
        self.event_source_name = event_source_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_source_name is not None:
            result['EventSourceName'] = self.event_source_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventSourceName') is not None:
            self.event_source_name = m.get('EventSourceName')
        return self


class DeleteEventSourceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteEventSourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteEventSourceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DeleteEventSourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteEventStreamingRequest(TeaModel):
    def __init__(
        self,
        event_streaming_name: str = None,
    ):
        self.event_streaming_name = event_streaming_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_streaming_name is not None:
            result['EventStreamingName'] = self.event_streaming_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventStreamingName') is not None:
            self.event_streaming_name = m.get('EventStreamingName')
        return self


class DeleteEventStreamingResponseBody(TeaModel):
    def __init__(
        self,
        code: bool = None,
        data: bool = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteEventStreamingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteEventStreamingResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DeleteEventStreamingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRuleRequest(TeaModel):
    def __init__(
        self,
        event_bus_name: str = None,
        rule_name: str = None,
    ):
        self.event_bus_name = event_bus_name
        self.rule_name = rule_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        return self


class DeleteRuleResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteRuleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DeleteRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSchemaRequest(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        schema_id: str = None,
    ):
        self.group_id = group_id
        self.schema_id = schema_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.schema_id is not None:
            result['SchemaId'] = self.schema_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('SchemaId') is not None:
            self.schema_id = m.get('SchemaId')
        return self


class DeleteSchemaResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
        http_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_code = http_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteSchemaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteSchemaResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DeleteSchemaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSchemaGroupRequest(TeaModel):
    def __init__(
        self,
        group_id: str = None,
    ):
        self.group_id = group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        return self


class DeleteSchemaGroupResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
        http_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_code = http_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteSchemaGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteSchemaGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DeleteSchemaGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSchemaVersionRequest(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        schema_id: str = None,
        version_number: str = None,
    ):
        self.group_id = group_id
        self.schema_id = schema_id
        self.version_number = version_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.schema_id is not None:
            result['SchemaId'] = self.schema_id
        if self.version_number is not None:
            result['VersionNumber'] = self.version_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('SchemaId') is not None:
            self.schema_id = m.get('SchemaId')
        if m.get('VersionNumber') is not None:
            self.version_number = m.get('VersionNumber')
        return self


class DeleteSchemaVersionResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
        http_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_code = http_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteSchemaVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteSchemaVersionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DeleteSchemaVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSourceTaskRequest(TeaModel):
    def __init__(
        self,
        task_id: str = None,
    ):
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DeleteSourceTaskResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteSourceTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteSourceTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DeleteSourceTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTargetsRequest(TeaModel):
    def __init__(
        self,
        event_bus_name: str = None,
        rule_name: str = None,
        target_ids: Dict[str, Any] = None,
    ):
        self.event_bus_name = event_bus_name
        self.rule_name = rule_name
        self.target_ids = target_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.target_ids is not None:
            result['TargetIds'] = self.target_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('TargetIds') is not None:
            self.target_ids = m.get('TargetIds')
        return self


class DeleteTargetsShrinkRequest(TeaModel):
    def __init__(
        self,
        event_bus_name: str = None,
        rule_name: str = None,
        target_ids_shrink: str = None,
    ):
        self.event_bus_name = event_bus_name
        self.rule_name = rule_name
        self.target_ids_shrink = target_ids_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.target_ids_shrink is not None:
            result['TargetIds'] = self.target_ids_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('TargetIds') is not None:
            self.target_ids_shrink = m.get('TargetIds')
        return self


class DeleteTargetsResponseBodyDataErrorEntries(TeaModel):
    def __init__(
        self,
        entry_id: str = None,
        error_code: str = None,
        error_message: str = None,
    ):
        self.entry_id = entry_id
        self.error_code = error_code
        self.error_message = error_message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entry_id is not None:
            result['EntryId'] = self.entry_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EntryId') is not None:
            self.entry_id = m.get('EntryId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        return self


class DeleteTargetsResponseBodyData(TeaModel):
    def __init__(
        self,
        error_entries: List[DeleteTargetsResponseBodyDataErrorEntries] = None,
        error_entries_count: int = None,
    ):
        self.error_entries = error_entries
        self.error_entries_count = error_entries_count

    def validate(self):
        if self.error_entries:
            for k in self.error_entries:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ErrorEntries'] = []
        if self.error_entries is not None:
            for k in self.error_entries:
                result['ErrorEntries'].append(k.to_map() if k else None)
        if self.error_entries_count is not None:
            result['ErrorEntriesCount'] = self.error_entries_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.error_entries = []
        if m.get('ErrorEntries') is not None:
            for k in m.get('ErrorEntries'):
                temp_model = DeleteTargetsResponseBodyDataErrorEntries()
                self.error_entries.append(temp_model.from_map(k))
        if m.get('ErrorEntriesCount') is not None:
            self.error_entries_count = m.get('ErrorEntriesCount')
        return self


class DeleteTargetsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: DeleteTargetsResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = DeleteTargetsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteTargetsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteTargetsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DeleteTargetsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsResponseBodyData(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        region_name: str = None,
    ):
        self.region_id = region_id
        self.region_name = region_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.region_name is not None:
            result['RegionName'] = self.region_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RegionName') is not None:
            self.region_name = m.get('RegionName')
        return self


class DescribeRegionsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[DescribeRegionsResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeRegionsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeRegionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeRegionsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DescribeRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableRuleRequest(TeaModel):
    def __init__(
        self,
        event_bus_name: str = None,
        rule_name: str = None,
    ):
        self.event_bus_name = event_bus_name
        self.rule_name = rule_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        return self


class DisableRuleResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DisableRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DisableRuleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DisableRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableRuleRequest(TeaModel):
    def __init__(
        self,
        event_bus_name: str = None,
        rule_name: str = None,
    ):
        self.event_bus_name = event_bus_name
        self.rule_name = rule_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        return self


class EnableRuleResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class EnableRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EnableRuleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = EnableRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FetchProductResourceValuesRequest(TeaModel):
    def __init__(
        self,
        extra_params: str = None,
        product_name: str = None,
        resource_key: str = None,
    ):
        self.extra_params = extra_params
        self.product_name = product_name
        self.resource_key = resource_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extra_params is not None:
            result['ExtraParams'] = self.extra_params
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        if self.resource_key is not None:
            result['ResourceKey'] = self.resource_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExtraParams') is not None:
            self.extra_params = m.get('ExtraParams')
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        if m.get('ResourceKey') is not None:
            self.resource_key = m.get('ResourceKey')
        return self


class FetchProductResourceValuesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[str] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class FetchProductResourceValuesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: FetchProductResourceValuesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = FetchProductResourceValuesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FetchTargetResourceValuesRequest(TeaModel):
    def __init__(
        self,
        extra_params: str = None,
        resource_key: str = None,
        target_type: str = None,
    ):
        self.extra_params = extra_params
        self.resource_key = resource_key
        self.target_type = target_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extra_params is not None:
            result['ExtraParams'] = self.extra_params
        if self.resource_key is not None:
            result['ResourceKey'] = self.resource_key
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExtraParams') is not None:
            self.extra_params = m.get('ExtraParams')
        if m.get('ResourceKey') is not None:
            self.resource_key = m.get('ResourceKey')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        return self


class FetchTargetResourceValuesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[str] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class FetchTargetResourceValuesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: FetchTargetResourceValuesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = FetchTargetResourceValuesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetACSEventsSchemaRequest(TeaModel):
    def __init__(
        self,
        schema_id: str = None,
    ):
        self.schema_id = schema_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.schema_id is not None:
            result['SchemaId'] = self.schema_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SchemaId') is not None:
            self.schema_id = m.get('SchemaId')
        return self


class GetACSEventsSchemaResponseBodyData(TeaModel):
    def __init__(
        self,
        content: str = None,
        data_sample: str = None,
        description: str = None,
        format: str = None,
        group_id: str = None,
        latest_version: int = None,
        schema_id: str = None,
    ):
        self.content = content
        self.data_sample = data_sample
        self.description = description
        self.format = format
        self.group_id = group_id
        self.latest_version = latest_version
        self.schema_id = schema_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.data_sample is not None:
            result['DataSample'] = self.data_sample
        if self.description is not None:
            result['Description'] = self.description
        if self.format is not None:
            result['Format'] = self.format
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.latest_version is not None:
            result['LatestVersion'] = self.latest_version
        if self.schema_id is not None:
            result['SchemaId'] = self.schema_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('DataSample') is not None:
            self.data_sample = m.get('DataSample')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Format') is not None:
            self.format = m.get('Format')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('LatestVersion') is not None:
            self.latest_version = m.get('LatestVersion')
        if m.get('SchemaId') is not None:
            self.schema_id = m.get('SchemaId')
        return self


class GetACSEventsSchemaResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetACSEventsSchemaResponseBodyData = None,
        http_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_code = http_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetACSEventsSchemaResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetACSEventsSchemaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetACSEventsSchemaResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetACSEventsSchemaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetACSEventsSchemaGroupResponseBodyData(TeaModel):
    def __init__(
        self,
        description: str = None,
        format: str = None,
        group_id: str = None,
    ):
        self.description = description
        self.format = format
        self.group_id = group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.format is not None:
            result['Format'] = self.format
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Format') is not None:
            self.format = m.get('Format')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        return self


class GetACSEventsSchemaGroupResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetACSEventsSchemaGroupResponseBodyData = None,
        http_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_code = http_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetACSEventsSchemaGroupResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetACSEventsSchemaGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetACSEventsSchemaGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetACSEventsSchemaGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetACSEventsSchemaVersionRequest(TeaModel):
    def __init__(
        self,
        schema_id: str = None,
        version_number: int = None,
    ):
        self.schema_id = schema_id
        self.version_number = version_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.schema_id is not None:
            result['SchemaId'] = self.schema_id
        if self.version_number is not None:
            result['VersionNumber'] = self.version_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SchemaId') is not None:
            self.schema_id = m.get('SchemaId')
        if m.get('VersionNumber') is not None:
            self.version_number = m.get('VersionNumber')
        return self


class GetACSEventsSchemaVersionResponseBodyData(TeaModel):
    def __init__(
        self,
        content: str = None,
        data_sample: str = None,
        description: str = None,
        format: str = None,
        group_id: str = None,
        schema_id: str = None,
        version: int = None,
    ):
        self.content = content
        self.data_sample = data_sample
        self.description = description
        self.format = format
        self.group_id = group_id
        self.schema_id = schema_id
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.data_sample is not None:
            result['DataSample'] = self.data_sample
        if self.description is not None:
            result['Description'] = self.description
        if self.format is not None:
            result['Format'] = self.format
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.schema_id is not None:
            result['SchemaId'] = self.schema_id
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('DataSample') is not None:
            self.data_sample = m.get('DataSample')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Format') is not None:
            self.format = m.get('Format')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('SchemaId') is not None:
            self.schema_id = m.get('SchemaId')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class GetACSEventsSchemaVersionResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetACSEventsSchemaVersionResponseBodyData = None,
        http_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_code = http_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetACSEventsSchemaVersionResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetACSEventsSchemaVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetACSEventsSchemaVersionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetACSEventsSchemaVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDefaultSchemaGroupResponseBodyData(TeaModel):
    def __init__(
        self,
        created_timestamp: int = None,
        description: str = None,
        format: str = None,
        group_arn: str = None,
        group_id: str = None,
        updated_timestamp: int = None,
    ):
        self.created_timestamp = created_timestamp
        self.description = description
        self.format = format
        self.group_arn = group_arn
        self.group_id = group_id
        self.updated_timestamp = updated_timestamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_timestamp is not None:
            result['CreatedTimestamp'] = self.created_timestamp
        if self.description is not None:
            result['Description'] = self.description
        if self.format is not None:
            result['Format'] = self.format
        if self.group_arn is not None:
            result['GroupARN'] = self.group_arn
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.updated_timestamp is not None:
            result['UpdatedTimestamp'] = self.updated_timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedTimestamp') is not None:
            self.created_timestamp = m.get('CreatedTimestamp')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Format') is not None:
            self.format = m.get('Format')
        if m.get('GroupARN') is not None:
            self.group_arn = m.get('GroupARN')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('UpdatedTimestamp') is not None:
            self.updated_timestamp = m.get('UpdatedTimestamp')
        return self


class GetDefaultSchemaGroupResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetDefaultSchemaGroupResponseBodyData = None,
        http_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_code = http_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetDefaultSchemaGroupResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetDefaultSchemaGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDefaultSchemaGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetDefaultSchemaGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetEndpointsResponseBodyData(TeaModel):
    def __init__(
        self,
        public_endpoint: str = None,
        vpc_endpoint: str = None,
    ):
        self.public_endpoint = public_endpoint
        self.vpc_endpoint = vpc_endpoint

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.public_endpoint is not None:
            result['PublicEndpoint'] = self.public_endpoint
        if self.vpc_endpoint is not None:
            result['VpcEndpoint'] = self.vpc_endpoint
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PublicEndpoint') is not None:
            self.public_endpoint = m.get('PublicEndpoint')
        if m.get('VpcEndpoint') is not None:
            self.vpc_endpoint = m.get('VpcEndpoint')
        return self


class GetEndpointsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[GetEndpointsResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetEndpointsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetEndpointsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetEndpointsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetEndpointsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetEventBusRequest(TeaModel):
    def __init__(
        self,
        event_bus_name: str = None,
    ):
        self.event_bus_name = event_bus_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')
        return self


class GetEventBusResponseBodyData(TeaModel):
    def __init__(
        self,
        create_timestamp: int = None,
        description: str = None,
        event_bus_arn: str = None,
        event_bus_name: str = None,
    ):
        self.create_timestamp = create_timestamp
        self.description = description
        self.event_bus_arn = event_bus_arn
        self.event_bus_name = event_bus_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_timestamp is not None:
            result['CreateTimestamp'] = self.create_timestamp
        if self.description is not None:
            result['Description'] = self.description
        if self.event_bus_arn is not None:
            result['EventBusARN'] = self.event_bus_arn
        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTimestamp') is not None:
            self.create_timestamp = m.get('CreateTimestamp')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EventBusARN') is not None:
            self.event_bus_arn = m.get('EventBusARN')
        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')
        return self


class GetEventBusResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetEventBusResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetEventBusResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetEventBusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetEventBusResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetEventBusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetEventStreamingRequest(TeaModel):
    def __init__(
        self,
        event_streaming_name: str = None,
    ):
        self.event_streaming_name = event_streaming_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_streaming_name is not None:
            result['EventStreamingName'] = self.event_streaming_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventStreamingName') is not None:
            self.event_streaming_name = m.get('EventStreamingName')
        return self


class GetEventStreamingResponseBodyDataRunOptionsBatchWindow(TeaModel):
    def __init__(
        self,
        count_based_window: int = None,
        time_based_window: int = None,
    ):
        self.count_based_window = count_based_window
        self.time_based_window = time_based_window

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count_based_window is not None:
            result['CountBasedWindow'] = self.count_based_window
        if self.time_based_window is not None:
            result['TimeBasedWindow'] = self.time_based_window
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CountBasedWindow') is not None:
            self.count_based_window = m.get('CountBasedWindow')
        if m.get('TimeBasedWindow') is not None:
            self.time_based_window = m.get('TimeBasedWindow')
        return self


class GetEventStreamingResponseBodyDataRunOptionsDeadLetterQueue(TeaModel):
    def __init__(
        self,
        arn: str = None,
    ):
        self.arn = arn

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arn is not None:
            result['Arn'] = self.arn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        return self


class GetEventStreamingResponseBodyDataRunOptionsRetryStrategy(TeaModel):
    def __init__(
        self,
        maximum_event_age_in_seconds: float = None,
        maximum_retry_attempts: float = None,
        push_retry_strategy: str = None,
    ):
        self.maximum_event_age_in_seconds = maximum_event_age_in_seconds
        self.maximum_retry_attempts = maximum_retry_attempts
        self.push_retry_strategy = push_retry_strategy

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.maximum_event_age_in_seconds is not None:
            result['MaximumEventAgeInSeconds'] = self.maximum_event_age_in_seconds
        if self.maximum_retry_attempts is not None:
            result['MaximumRetryAttempts'] = self.maximum_retry_attempts
        if self.push_retry_strategy is not None:
            result['PushRetryStrategy'] = self.push_retry_strategy
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaximumEventAgeInSeconds') is not None:
            self.maximum_event_age_in_seconds = m.get('MaximumEventAgeInSeconds')
        if m.get('MaximumRetryAttempts') is not None:
            self.maximum_retry_attempts = m.get('MaximumRetryAttempts')
        if m.get('PushRetryStrategy') is not None:
            self.push_retry_strategy = m.get('PushRetryStrategy')
        return self


class GetEventStreamingResponseBodyDataRunOptions(TeaModel):
    def __init__(
        self,
        batch_window: GetEventStreamingResponseBodyDataRunOptionsBatchWindow = None,
        dead_letter_queue: GetEventStreamingResponseBodyDataRunOptionsDeadLetterQueue = None,
        errors_tolerance: str = None,
        maximum_tasks: int = None,
        retry_strategy: GetEventStreamingResponseBodyDataRunOptionsRetryStrategy = None,
    ):
        self.batch_window = batch_window
        self.dead_letter_queue = dead_letter_queue
        self.errors_tolerance = errors_tolerance
        self.maximum_tasks = maximum_tasks
        self.retry_strategy = retry_strategy

    def validate(self):
        if self.batch_window:
            self.batch_window.validate()
        if self.dead_letter_queue:
            self.dead_letter_queue.validate()
        if self.retry_strategy:
            self.retry_strategy.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.batch_window is not None:
            result['BatchWindow'] = self.batch_window.to_map()
        if self.dead_letter_queue is not None:
            result['DeadLetterQueue'] = self.dead_letter_queue.to_map()
        if self.errors_tolerance is not None:
            result['ErrorsTolerance'] = self.errors_tolerance
        if self.maximum_tasks is not None:
            result['MaximumTasks'] = self.maximum_tasks
        if self.retry_strategy is not None:
            result['RetryStrategy'] = self.retry_strategy.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BatchWindow') is not None:
            temp_model = GetEventStreamingResponseBodyDataRunOptionsBatchWindow()
            self.batch_window = temp_model.from_map(m['BatchWindow'])
        if m.get('DeadLetterQueue') is not None:
            temp_model = GetEventStreamingResponseBodyDataRunOptionsDeadLetterQueue()
            self.dead_letter_queue = temp_model.from_map(m['DeadLetterQueue'])
        if m.get('ErrorsTolerance') is not None:
            self.errors_tolerance = m.get('ErrorsTolerance')
        if m.get('MaximumTasks') is not None:
            self.maximum_tasks = m.get('MaximumTasks')
        if m.get('RetryStrategy') is not None:
            temp_model = GetEventStreamingResponseBodyDataRunOptionsRetryStrategy()
            self.retry_strategy = temp_model.from_map(m['RetryStrategy'])
        return self


class GetEventStreamingResponseBodyDataSinkSinkFcParametersBody(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetEventStreamingResponseBodyDataSinkSinkFcParametersFunctionName(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetEventStreamingResponseBodyDataSinkSinkFcParametersInvocationType(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetEventStreamingResponseBodyDataSinkSinkFcParametersQualifier(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetEventStreamingResponseBodyDataSinkSinkFcParametersServiceName(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetEventStreamingResponseBodyDataSinkSinkFcParameters(TeaModel):
    def __init__(
        self,
        body: GetEventStreamingResponseBodyDataSinkSinkFcParametersBody = None,
        function_name: GetEventStreamingResponseBodyDataSinkSinkFcParametersFunctionName = None,
        invocation_type: GetEventStreamingResponseBodyDataSinkSinkFcParametersInvocationType = None,
        qualifier: GetEventStreamingResponseBodyDataSinkSinkFcParametersQualifier = None,
        service_name: GetEventStreamingResponseBodyDataSinkSinkFcParametersServiceName = None,
    ):
        self.body = body
        self.function_name = function_name
        self.invocation_type = invocation_type
        self.qualifier = qualifier
        self.service_name = service_name

    def validate(self):
        if self.body:
            self.body.validate()
        if self.function_name:
            self.function_name.validate()
        if self.invocation_type:
            self.invocation_type.validate()
        if self.qualifier:
            self.qualifier.validate()
        if self.service_name:
            self.service_name.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['Body'] = self.body.to_map()
        if self.function_name is not None:
            result['FunctionName'] = self.function_name.to_map()
        if self.invocation_type is not None:
            result['InvocationType'] = self.invocation_type.to_map()
        if self.qualifier is not None:
            result['Qualifier'] = self.qualifier.to_map()
        if self.service_name is not None:
            result['ServiceName'] = self.service_name.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Body') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkFcParametersBody()
            self.body = temp_model.from_map(m['Body'])
        if m.get('FunctionName') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkFcParametersFunctionName()
            self.function_name = temp_model.from_map(m['FunctionName'])
        if m.get('InvocationType') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkFcParametersInvocationType()
            self.invocation_type = temp_model.from_map(m['InvocationType'])
        if m.get('Qualifier') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkFcParametersQualifier()
            self.qualifier = temp_model.from_map(m['Qualifier'])
        if m.get('ServiceName') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkFcParametersServiceName()
            self.service_name = temp_model.from_map(m['ServiceName'])
        return self


class GetEventStreamingResponseBodyDataSinkSinkKafkaParametersAcks(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetEventStreamingResponseBodyDataSinkSinkKafkaParametersInstanceId(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetEventStreamingResponseBodyDataSinkSinkKafkaParametersKey(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetEventStreamingResponseBodyDataSinkSinkKafkaParametersSaslUser(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetEventStreamingResponseBodyDataSinkSinkKafkaParametersTopic(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetEventStreamingResponseBodyDataSinkSinkKafkaParametersValue(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetEventStreamingResponseBodyDataSinkSinkKafkaParameters(TeaModel):
    def __init__(
        self,
        acks: GetEventStreamingResponseBodyDataSinkSinkKafkaParametersAcks = None,
        instance_id: GetEventStreamingResponseBodyDataSinkSinkKafkaParametersInstanceId = None,
        key: GetEventStreamingResponseBodyDataSinkSinkKafkaParametersKey = None,
        sasl_user: GetEventStreamingResponseBodyDataSinkSinkKafkaParametersSaslUser = None,
        topic: GetEventStreamingResponseBodyDataSinkSinkKafkaParametersTopic = None,
        value: GetEventStreamingResponseBodyDataSinkSinkKafkaParametersValue = None,
    ):
        self.acks = acks
        self.instance_id = instance_id
        self.key = key
        self.sasl_user = sasl_user
        self.topic = topic
        self.value = value

    def validate(self):
        if self.acks:
            self.acks.validate()
        if self.instance_id:
            self.instance_id.validate()
        if self.key:
            self.key.validate()
        if self.sasl_user:
            self.sasl_user.validate()
        if self.topic:
            self.topic.validate()
        if self.value:
            self.value.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acks is not None:
            result['Acks'] = self.acks.to_map()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id.to_map()
        if self.key is not None:
            result['Key'] = self.key.to_map()
        if self.sasl_user is not None:
            result['SaslUser'] = self.sasl_user.to_map()
        if self.topic is not None:
            result['Topic'] = self.topic.to_map()
        if self.value is not None:
            result['Value'] = self.value.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Acks') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkKafkaParametersAcks()
            self.acks = temp_model.from_map(m['Acks'])
        if m.get('InstanceId') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkKafkaParametersInstanceId()
            self.instance_id = temp_model.from_map(m['InstanceId'])
        if m.get('Key') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkKafkaParametersKey()
            self.key = temp_model.from_map(m['Key'])
        if m.get('SaslUser') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkKafkaParametersSaslUser()
            self.sasl_user = temp_model.from_map(m['SaslUser'])
        if m.get('Topic') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkKafkaParametersTopic()
            self.topic = temp_model.from_map(m['Topic'])
        if m.get('Value') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkKafkaParametersValue()
            self.value = temp_model.from_map(m['Value'])
        return self


class GetEventStreamingResponseBodyDataSinkSinkMNSParametersBody(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetEventStreamingResponseBodyDataSinkSinkMNSParametersIsBase64Encode(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetEventStreamingResponseBodyDataSinkSinkMNSParametersQueueName(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetEventStreamingResponseBodyDataSinkSinkMNSParameters(TeaModel):
    def __init__(
        self,
        body: GetEventStreamingResponseBodyDataSinkSinkMNSParametersBody = None,
        is_base_64encode: GetEventStreamingResponseBodyDataSinkSinkMNSParametersIsBase64Encode = None,
        queue_name: GetEventStreamingResponseBodyDataSinkSinkMNSParametersQueueName = None,
    ):
        self.body = body
        self.is_base_64encode = is_base_64encode
        self.queue_name = queue_name

    def validate(self):
        if self.body:
            self.body.validate()
        if self.is_base_64encode:
            self.is_base_64encode.validate()
        if self.queue_name:
            self.queue_name.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['Body'] = self.body.to_map()
        if self.is_base_64encode is not None:
            result['IsBase64Encode'] = self.is_base_64encode.to_map()
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Body') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkMNSParametersBody()
            self.body = temp_model.from_map(m['Body'])
        if m.get('IsBase64Encode') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkMNSParametersIsBase64Encode()
            self.is_base_64encode = temp_model.from_map(m['IsBase64Encode'])
        if m.get('QueueName') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkMNSParametersQueueName()
            self.queue_name = temp_model.from_map(m['QueueName'])
        return self


class GetEventStreamingResponseBodyDataSinkSinkRabbitMQParametersBody(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetEventStreamingResponseBodyDataSinkSinkRabbitMQParametersExchange(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetEventStreamingResponseBodyDataSinkSinkRabbitMQParametersInstanceId(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetEventStreamingResponseBodyDataSinkSinkRabbitMQParametersMessageId(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetEventStreamingResponseBodyDataSinkSinkRabbitMQParametersProperties(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetEventStreamingResponseBodyDataSinkSinkRabbitMQParametersQueueName(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetEventStreamingResponseBodyDataSinkSinkRabbitMQParametersRoutingKey(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetEventStreamingResponseBodyDataSinkSinkRabbitMQParametersTargetType(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetEventStreamingResponseBodyDataSinkSinkRabbitMQParametersVirtualHostName(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetEventStreamingResponseBodyDataSinkSinkRabbitMQParameters(TeaModel):
    def __init__(
        self,
        body: GetEventStreamingResponseBodyDataSinkSinkRabbitMQParametersBody = None,
        exchange: GetEventStreamingResponseBodyDataSinkSinkRabbitMQParametersExchange = None,
        instance_id: GetEventStreamingResponseBodyDataSinkSinkRabbitMQParametersInstanceId = None,
        message_id: GetEventStreamingResponseBodyDataSinkSinkRabbitMQParametersMessageId = None,
        properties: GetEventStreamingResponseBodyDataSinkSinkRabbitMQParametersProperties = None,
        queue_name: GetEventStreamingResponseBodyDataSinkSinkRabbitMQParametersQueueName = None,
        routing_key: GetEventStreamingResponseBodyDataSinkSinkRabbitMQParametersRoutingKey = None,
        target_type: GetEventStreamingResponseBodyDataSinkSinkRabbitMQParametersTargetType = None,
        virtual_host_name: GetEventStreamingResponseBodyDataSinkSinkRabbitMQParametersVirtualHostName = None,
    ):
        self.body = body
        self.exchange = exchange
        self.instance_id = instance_id
        self.message_id = message_id
        self.properties = properties
        self.queue_name = queue_name
        self.routing_key = routing_key
        self.target_type = target_type
        self.virtual_host_name = virtual_host_name

    def validate(self):
        if self.body:
            self.body.validate()
        if self.exchange:
            self.exchange.validate()
        if self.instance_id:
            self.instance_id.validate()
        if self.message_id:
            self.message_id.validate()
        if self.properties:
            self.properties.validate()
        if self.queue_name:
            self.queue_name.validate()
        if self.routing_key:
            self.routing_key.validate()
        if self.target_type:
            self.target_type.validate()
        if self.virtual_host_name:
            self.virtual_host_name.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['Body'] = self.body.to_map()
        if self.exchange is not None:
            result['Exchange'] = self.exchange.to_map()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id.to_map()
        if self.message_id is not None:
            result['MessageId'] = self.message_id.to_map()
        if self.properties is not None:
            result['Properties'] = self.properties.to_map()
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name.to_map()
        if self.routing_key is not None:
            result['RoutingKey'] = self.routing_key.to_map()
        if self.target_type is not None:
            result['TargetType'] = self.target_type.to_map()
        if self.virtual_host_name is not None:
            result['VirtualHostName'] = self.virtual_host_name.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Body') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkRabbitMQParametersBody()
            self.body = temp_model.from_map(m['Body'])
        if m.get('Exchange') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkRabbitMQParametersExchange()
            self.exchange = temp_model.from_map(m['Exchange'])
        if m.get('InstanceId') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkRabbitMQParametersInstanceId()
            self.instance_id = temp_model.from_map(m['InstanceId'])
        if m.get('MessageId') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkRabbitMQParametersMessageId()
            self.message_id = temp_model.from_map(m['MessageId'])
        if m.get('Properties') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkRabbitMQParametersProperties()
            self.properties = temp_model.from_map(m['Properties'])
        if m.get('QueueName') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkRabbitMQParametersQueueName()
            self.queue_name = temp_model.from_map(m['QueueName'])
        if m.get('RoutingKey') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkRabbitMQParametersRoutingKey()
            self.routing_key = temp_model.from_map(m['RoutingKey'])
        if m.get('TargetType') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkRabbitMQParametersTargetType()
            self.target_type = temp_model.from_map(m['TargetType'])
        if m.get('VirtualHostName') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkRabbitMQParametersVirtualHostName()
            self.virtual_host_name = temp_model.from_map(m['VirtualHostName'])
        return self


class GetEventStreamingResponseBodyDataSinkSinkRocketMQParametersBody(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetEventStreamingResponseBodyDataSinkSinkRocketMQParametersInstanceId(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetEventStreamingResponseBodyDataSinkSinkRocketMQParametersKeys(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetEventStreamingResponseBodyDataSinkSinkRocketMQParametersProperties(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetEventStreamingResponseBodyDataSinkSinkRocketMQParametersTags(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetEventStreamingResponseBodyDataSinkSinkRocketMQParametersTopic(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetEventStreamingResponseBodyDataSinkSinkRocketMQParameters(TeaModel):
    def __init__(
        self,
        body: GetEventStreamingResponseBodyDataSinkSinkRocketMQParametersBody = None,
        instance_id: GetEventStreamingResponseBodyDataSinkSinkRocketMQParametersInstanceId = None,
        keys: GetEventStreamingResponseBodyDataSinkSinkRocketMQParametersKeys = None,
        properties: GetEventStreamingResponseBodyDataSinkSinkRocketMQParametersProperties = None,
        tags: GetEventStreamingResponseBodyDataSinkSinkRocketMQParametersTags = None,
        topic: GetEventStreamingResponseBodyDataSinkSinkRocketMQParametersTopic = None,
    ):
        self.body = body
        self.instance_id = instance_id
        self.keys = keys
        self.properties = properties
        self.tags = tags
        self.topic = topic

    def validate(self):
        if self.body:
            self.body.validate()
        if self.instance_id:
            self.instance_id.validate()
        if self.keys:
            self.keys.validate()
        if self.properties:
            self.properties.validate()
        if self.tags:
            self.tags.validate()
        if self.topic:
            self.topic.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['Body'] = self.body.to_map()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id.to_map()
        if self.keys is not None:
            result['Keys'] = self.keys.to_map()
        if self.properties is not None:
            result['Properties'] = self.properties.to_map()
        if self.tags is not None:
            result['Tags'] = self.tags.to_map()
        if self.topic is not None:
            result['Topic'] = self.topic.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Body') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkRocketMQParametersBody()
            self.body = temp_model.from_map(m['Body'])
        if m.get('InstanceId') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkRocketMQParametersInstanceId()
            self.instance_id = temp_model.from_map(m['InstanceId'])
        if m.get('Keys') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkRocketMQParametersKeys()
            self.keys = temp_model.from_map(m['Keys'])
        if m.get('Properties') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkRocketMQParametersProperties()
            self.properties = temp_model.from_map(m['Properties'])
        if m.get('Tags') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkRocketMQParametersTags()
            self.tags = temp_model.from_map(m['Tags'])
        if m.get('Topic') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkRocketMQParametersTopic()
            self.topic = temp_model.from_map(m['Topic'])
        return self


class GetEventStreamingResponseBodyDataSinkSinkSLSParametersBody(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetEventStreamingResponseBodyDataSinkSinkSLSParametersLogStore(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetEventStreamingResponseBodyDataSinkSinkSLSParametersProject(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetEventStreamingResponseBodyDataSinkSinkSLSParametersRoleName(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetEventStreamingResponseBodyDataSinkSinkSLSParametersTopic(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetEventStreamingResponseBodyDataSinkSinkSLSParameters(TeaModel):
    def __init__(
        self,
        body: GetEventStreamingResponseBodyDataSinkSinkSLSParametersBody = None,
        log_store: GetEventStreamingResponseBodyDataSinkSinkSLSParametersLogStore = None,
        project: GetEventStreamingResponseBodyDataSinkSinkSLSParametersProject = None,
        role_name: GetEventStreamingResponseBodyDataSinkSinkSLSParametersRoleName = None,
        topic: GetEventStreamingResponseBodyDataSinkSinkSLSParametersTopic = None,
    ):
        self.body = body
        self.log_store = log_store
        self.project = project
        self.role_name = role_name
        self.topic = topic

    def validate(self):
        if self.body:
            self.body.validate()
        if self.log_store:
            self.log_store.validate()
        if self.project:
            self.project.validate()
        if self.role_name:
            self.role_name.validate()
        if self.topic:
            self.topic.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['Body'] = self.body.to_map()
        if self.log_store is not None:
            result['LogStore'] = self.log_store.to_map()
        if self.project is not None:
            result['Project'] = self.project.to_map()
        if self.role_name is not None:
            result['RoleName'] = self.role_name.to_map()
        if self.topic is not None:
            result['Topic'] = self.topic.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Body') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkSLSParametersBody()
            self.body = temp_model.from_map(m['Body'])
        if m.get('LogStore') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkSLSParametersLogStore()
            self.log_store = temp_model.from_map(m['LogStore'])
        if m.get('Project') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkSLSParametersProject()
            self.project = temp_model.from_map(m['Project'])
        if m.get('RoleName') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkSLSParametersRoleName()
            self.role_name = temp_model.from_map(m['RoleName'])
        if m.get('Topic') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkSLSParametersTopic()
            self.topic = temp_model.from_map(m['Topic'])
        return self


class GetEventStreamingResponseBodyDataSink(TeaModel):
    def __init__(
        self,
        sink_fc_parameters: GetEventStreamingResponseBodyDataSinkSinkFcParameters = None,
        sink_kafka_parameters: GetEventStreamingResponseBodyDataSinkSinkKafkaParameters = None,
        sink_mnsparameters: GetEventStreamingResponseBodyDataSinkSinkMNSParameters = None,
        sink_rabbit_mqparameters: GetEventStreamingResponseBodyDataSinkSinkRabbitMQParameters = None,
        sink_rocket_mqparameters: GetEventStreamingResponseBodyDataSinkSinkRocketMQParameters = None,
        sink_slsparameters: GetEventStreamingResponseBodyDataSinkSinkSLSParameters = None,
    ):
        self.sink_fc_parameters = sink_fc_parameters
        self.sink_kafka_parameters = sink_kafka_parameters
        self.sink_mnsparameters = sink_mnsparameters
        self.sink_rabbit_mqparameters = sink_rabbit_mqparameters
        self.sink_rocket_mqparameters = sink_rocket_mqparameters
        self.sink_slsparameters = sink_slsparameters

    def validate(self):
        if self.sink_fc_parameters:
            self.sink_fc_parameters.validate()
        if self.sink_kafka_parameters:
            self.sink_kafka_parameters.validate()
        if self.sink_mnsparameters:
            self.sink_mnsparameters.validate()
        if self.sink_rabbit_mqparameters:
            self.sink_rabbit_mqparameters.validate()
        if self.sink_rocket_mqparameters:
            self.sink_rocket_mqparameters.validate()
        if self.sink_slsparameters:
            self.sink_slsparameters.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sink_fc_parameters is not None:
            result['SinkFcParameters'] = self.sink_fc_parameters.to_map()
        if self.sink_kafka_parameters is not None:
            result['SinkKafkaParameters'] = self.sink_kafka_parameters.to_map()
        if self.sink_mnsparameters is not None:
            result['SinkMNSParameters'] = self.sink_mnsparameters.to_map()
        if self.sink_rabbit_mqparameters is not None:
            result['SinkRabbitMQParameters'] = self.sink_rabbit_mqparameters.to_map()
        if self.sink_rocket_mqparameters is not None:
            result['SinkRocketMQParameters'] = self.sink_rocket_mqparameters.to_map()
        if self.sink_slsparameters is not None:
            result['SinkSLSParameters'] = self.sink_slsparameters.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SinkFcParameters') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkFcParameters()
            self.sink_fc_parameters = temp_model.from_map(m['SinkFcParameters'])
        if m.get('SinkKafkaParameters') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkKafkaParameters()
            self.sink_kafka_parameters = temp_model.from_map(m['SinkKafkaParameters'])
        if m.get('SinkMNSParameters') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkMNSParameters()
            self.sink_mnsparameters = temp_model.from_map(m['SinkMNSParameters'])
        if m.get('SinkRabbitMQParameters') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkRabbitMQParameters()
            self.sink_rabbit_mqparameters = temp_model.from_map(m['SinkRabbitMQParameters'])
        if m.get('SinkRocketMQParameters') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkRocketMQParameters()
            self.sink_rocket_mqparameters = temp_model.from_map(m['SinkRocketMQParameters'])
        if m.get('SinkSLSParameters') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkSLSParameters()
            self.sink_slsparameters = temp_model.from_map(m['SinkSLSParameters'])
        return self


class GetEventStreamingResponseBodyDataSourceSourceDTSParameters(TeaModel):
    def __init__(
        self,
        broker_url: str = None,
        init_check_point: str = None,
        password: str = None,
        sid: str = None,
        task_id: str = None,
        topic: str = None,
        username: str = None,
    ):
        self.broker_url = broker_url
        self.init_check_point = init_check_point
        self.password = password
        self.sid = sid
        self.task_id = task_id
        self.topic = topic
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.broker_url is not None:
            result['BrokerUrl'] = self.broker_url
        if self.init_check_point is not None:
            result['InitCheckPoint'] = self.init_check_point
        if self.password is not None:
            result['Password'] = self.password
        if self.sid is not None:
            result['Sid'] = self.sid
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.topic is not None:
            result['Topic'] = self.topic
        if self.username is not None:
            result['Username'] = self.username
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BrokerUrl') is not None:
            self.broker_url = m.get('BrokerUrl')
        if m.get('InitCheckPoint') is not None:
            self.init_check_point = m.get('InitCheckPoint')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('Sid') is not None:
            self.sid = m.get('Sid')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        return self


class GetEventStreamingResponseBodyDataSourceSourceKafkaParameters(TeaModel):
    def __init__(
        self,
        consumer_group: str = None,
        instance_id: str = None,
        network: str = None,
        offset_reset: str = None,
        region_id: str = None,
        security_group_id: str = None,
        topic: str = None,
        v_switch_ids: str = None,
        vpc_id: str = None,
    ):
        self.consumer_group = consumer_group
        self.instance_id = instance_id
        self.network = network
        self.offset_reset = offset_reset
        self.region_id = region_id
        self.security_group_id = security_group_id
        self.topic = topic
        self.v_switch_ids = v_switch_ids
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consumer_group is not None:
            result['ConsumerGroup'] = self.consumer_group
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.network is not None:
            result['Network'] = self.network
        if self.offset_reset is not None:
            result['OffsetReset'] = self.offset_reset
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.topic is not None:
            result['Topic'] = self.topic
        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsumerGroup') is not None:
            self.consumer_group = m.get('ConsumerGroup')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Network') is not None:
            self.network = m.get('Network')
        if m.get('OffsetReset') is not None:
            self.offset_reset = m.get('OffsetReset')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class GetEventStreamingResponseBodyDataSourceSourceMNSParameters(TeaModel):
    def __init__(
        self,
        is_base_64decode: bool = None,
        queue_name: str = None,
        region_id: str = None,
    ):
        self.is_base_64decode = is_base_64decode
        self.queue_name = queue_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_base_64decode is not None:
            result['IsBase64Decode'] = self.is_base_64decode
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsBase64Decode') is not None:
            self.is_base_64decode = m.get('IsBase64Decode')
        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetEventStreamingResponseBodyDataSourceSourceMQTTParameters(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        region_id: str = None,
        topic: str = None,
    ):
        self.instance_id = instance_id
        self.region_id = region_id
        self.topic = topic

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.topic is not None:
            result['Topic'] = self.topic
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        return self


class GetEventStreamingResponseBodyDataSourceSourceRabbitMQParameters(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        queue_name: str = None,
        region_id: str = None,
        virtual_host_name: str = None,
    ):
        self.instance_id = instance_id
        self.queue_name = queue_name
        self.region_id = region_id
        self.virtual_host_name = virtual_host_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.virtual_host_name is not None:
            result['VirtualHostName'] = self.virtual_host_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VirtualHostName') is not None:
            self.virtual_host_name = m.get('VirtualHostName')
        return self


class GetEventStreamingResponseBodyDataSourceSourceRocketMQParameters(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        instance_id: str = None,
        offset: str = None,
        region_id: str = None,
        tag: str = None,
        timestamp: int = None,
        topic: str = None,
    ):
        self.group_id = group_id
        self.instance_id = instance_id
        self.offset = offset
        self.region_id = region_id
        self.tag = tag
        self.timestamp = timestamp
        self.topic = topic

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupID'] = self.group_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.offset is not None:
            result['Offset'] = self.offset
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.topic is not None:
            result['Topic'] = self.topic
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupID') is not None:
            self.group_id = m.get('GroupID')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Offset') is not None:
            self.offset = m.get('Offset')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        return self


class GetEventStreamingResponseBodyDataSourceSourceSLSParameters(TeaModel):
    def __init__(
        self,
        consume_position: str = None,
        consumer_group: str = None,
        log_store: str = None,
        project: str = None,
        role_name: str = None,
    ):
        self.consume_position = consume_position
        self.consumer_group = consumer_group
        self.log_store = log_store
        self.project = project
        self.role_name = role_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consume_position is not None:
            result['ConsumePosition'] = self.consume_position
        if self.consumer_group is not None:
            result['ConsumerGroup'] = self.consumer_group
        if self.log_store is not None:
            result['LogStore'] = self.log_store
        if self.project is not None:
            result['Project'] = self.project
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsumePosition') is not None:
            self.consume_position = m.get('ConsumePosition')
        if m.get('ConsumerGroup') is not None:
            self.consumer_group = m.get('ConsumerGroup')
        if m.get('LogStore') is not None:
            self.log_store = m.get('LogStore')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        return self


class GetEventStreamingResponseBodyDataSource(TeaModel):
    def __init__(
        self,
        source_dtsparameters: GetEventStreamingResponseBodyDataSourceSourceDTSParameters = None,
        source_kafka_parameters: GetEventStreamingResponseBodyDataSourceSourceKafkaParameters = None,
        source_mnsparameters: GetEventStreamingResponseBodyDataSourceSourceMNSParameters = None,
        source_mqttparameters: GetEventStreamingResponseBodyDataSourceSourceMQTTParameters = None,
        source_rabbit_mqparameters: GetEventStreamingResponseBodyDataSourceSourceRabbitMQParameters = None,
        source_rocket_mqparameters: GetEventStreamingResponseBodyDataSourceSourceRocketMQParameters = None,
        source_slsparameters: GetEventStreamingResponseBodyDataSourceSourceSLSParameters = None,
    ):
        self.source_dtsparameters = source_dtsparameters
        self.source_kafka_parameters = source_kafka_parameters
        self.source_mnsparameters = source_mnsparameters
        self.source_mqttparameters = source_mqttparameters
        self.source_rabbit_mqparameters = source_rabbit_mqparameters
        self.source_rocket_mqparameters = source_rocket_mqparameters
        self.source_slsparameters = source_slsparameters

    def validate(self):
        if self.source_dtsparameters:
            self.source_dtsparameters.validate()
        if self.source_kafka_parameters:
            self.source_kafka_parameters.validate()
        if self.source_mnsparameters:
            self.source_mnsparameters.validate()
        if self.source_mqttparameters:
            self.source_mqttparameters.validate()
        if self.source_rabbit_mqparameters:
            self.source_rabbit_mqparameters.validate()
        if self.source_rocket_mqparameters:
            self.source_rocket_mqparameters.validate()
        if self.source_slsparameters:
            self.source_slsparameters.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_dtsparameters is not None:
            result['SourceDTSParameters'] = self.source_dtsparameters.to_map()
        if self.source_kafka_parameters is not None:
            result['SourceKafkaParameters'] = self.source_kafka_parameters.to_map()
        if self.source_mnsparameters is not None:
            result['SourceMNSParameters'] = self.source_mnsparameters.to_map()
        if self.source_mqttparameters is not None:
            result['SourceMQTTParameters'] = self.source_mqttparameters.to_map()
        if self.source_rabbit_mqparameters is not None:
            result['SourceRabbitMQParameters'] = self.source_rabbit_mqparameters.to_map()
        if self.source_rocket_mqparameters is not None:
            result['SourceRocketMQParameters'] = self.source_rocket_mqparameters.to_map()
        if self.source_slsparameters is not None:
            result['SourceSLSParameters'] = self.source_slsparameters.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceDTSParameters') is not None:
            temp_model = GetEventStreamingResponseBodyDataSourceSourceDTSParameters()
            self.source_dtsparameters = temp_model.from_map(m['SourceDTSParameters'])
        if m.get('SourceKafkaParameters') is not None:
            temp_model = GetEventStreamingResponseBodyDataSourceSourceKafkaParameters()
            self.source_kafka_parameters = temp_model.from_map(m['SourceKafkaParameters'])
        if m.get('SourceMNSParameters') is not None:
            temp_model = GetEventStreamingResponseBodyDataSourceSourceMNSParameters()
            self.source_mnsparameters = temp_model.from_map(m['SourceMNSParameters'])
        if m.get('SourceMQTTParameters') is not None:
            temp_model = GetEventStreamingResponseBodyDataSourceSourceMQTTParameters()
            self.source_mqttparameters = temp_model.from_map(m['SourceMQTTParameters'])
        if m.get('SourceRabbitMQParameters') is not None:
            temp_model = GetEventStreamingResponseBodyDataSourceSourceRabbitMQParameters()
            self.source_rabbit_mqparameters = temp_model.from_map(m['SourceRabbitMQParameters'])
        if m.get('SourceRocketMQParameters') is not None:
            temp_model = GetEventStreamingResponseBodyDataSourceSourceRocketMQParameters()
            self.source_rocket_mqparameters = temp_model.from_map(m['SourceRocketMQParameters'])
        if m.get('SourceSLSParameters') is not None:
            temp_model = GetEventStreamingResponseBodyDataSourceSourceSLSParameters()
            self.source_slsparameters = temp_model.from_map(m['SourceSLSParameters'])
        return self


class GetEventStreamingResponseBodyData(TeaModel):
    def __init__(
        self,
        description: str = None,
        event_streaming_name: str = None,
        filter_pattern: str = None,
        run_options: GetEventStreamingResponseBodyDataRunOptions = None,
        sink: GetEventStreamingResponseBodyDataSink = None,
        source: GetEventStreamingResponseBodyDataSource = None,
        status: str = None,
        tag: str = None,
    ):
        self.description = description
        self.event_streaming_name = event_streaming_name
        self.filter_pattern = filter_pattern
        self.run_options = run_options
        self.sink = sink
        self.source = source
        self.status = status
        self.tag = tag

    def validate(self):
        if self.run_options:
            self.run_options.validate()
        if self.sink:
            self.sink.validate()
        if self.source:
            self.source.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.event_streaming_name is not None:
            result['EventStreamingName'] = self.event_streaming_name
        if self.filter_pattern is not None:
            result['FilterPattern'] = self.filter_pattern
        if self.run_options is not None:
            result['RunOptions'] = self.run_options.to_map()
        if self.sink is not None:
            result['Sink'] = self.sink.to_map()
        if self.source is not None:
            result['Source'] = self.source.to_map()
        if self.status is not None:
            result['Status'] = self.status
        if self.tag is not None:
            result['Tag'] = self.tag
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EventStreamingName') is not None:
            self.event_streaming_name = m.get('EventStreamingName')
        if m.get('FilterPattern') is not None:
            self.filter_pattern = m.get('FilterPattern')
        if m.get('RunOptions') is not None:
            temp_model = GetEventStreamingResponseBodyDataRunOptions()
            self.run_options = temp_model.from_map(m['RunOptions'])
        if m.get('Sink') is not None:
            temp_model = GetEventStreamingResponseBodyDataSink()
            self.sink = temp_model.from_map(m['Sink'])
        if m.get('Source') is not None:
            temp_model = GetEventStreamingResponseBodyDataSource()
            self.source = temp_model.from_map(m['Source'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        return self


class GetEventStreamingResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetEventStreamingResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetEventStreamingResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetEventStreamingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetEventStreamingResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetEventStreamingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRuleRequest(TeaModel):
    def __init__(
        self,
        event_bus_name: str = None,
        rule_name: str = None,
    ):
        self.event_bus_name = event_bus_name
        self.rule_name = rule_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        return self


class GetRuleResponseBodyDataTargetsDeadLetterQueue(TeaModel):
    def __init__(
        self,
        arn: str = None,
    ):
        self.arn = arn

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arn is not None:
            result['Arn'] = self.arn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        return self


class GetRuleResponseBodyDataTargetsParamList(TeaModel):
    def __init__(
        self,
        form: str = None,
        resource_key: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.resource_key = resource_key
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.resource_key is not None:
            result['ResourceKey'] = self.resource_key
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('ResourceKey') is not None:
            self.resource_key = m.get('ResourceKey')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetRuleResponseBodyDataTargets(TeaModel):
    def __init__(
        self,
        dead_letter_queue: GetRuleResponseBodyDataTargetsDeadLetterQueue = None,
        detail_map: Dict[str, Any] = None,
        endpoint: str = None,
        id: str = None,
        param_list: List[GetRuleResponseBodyDataTargetsParamList] = None,
        push_retry_strategy: str = None,
        push_selector: str = None,
        type: str = None,
    ):
        self.dead_letter_queue = dead_letter_queue
        self.detail_map = detail_map
        self.endpoint = endpoint
        self.id = id
        self.param_list = param_list
        self.push_retry_strategy = push_retry_strategy
        self.push_selector = push_selector
        self.type = type

    def validate(self):
        if self.dead_letter_queue:
            self.dead_letter_queue.validate()
        if self.param_list:
            for k in self.param_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dead_letter_queue is not None:
            result['DeadLetterQueue'] = self.dead_letter_queue.to_map()
        if self.detail_map is not None:
            result['DetailMap'] = self.detail_map
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.id is not None:
            result['Id'] = self.id
        result['ParamList'] = []
        if self.param_list is not None:
            for k in self.param_list:
                result['ParamList'].append(k.to_map() if k else None)
        if self.push_retry_strategy is not None:
            result['PushRetryStrategy'] = self.push_retry_strategy
        if self.push_selector is not None:
            result['PushSelector'] = self.push_selector
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeadLetterQueue') is not None:
            temp_model = GetRuleResponseBodyDataTargetsDeadLetterQueue()
            self.dead_letter_queue = temp_model.from_map(m['DeadLetterQueue'])
        if m.get('DetailMap') is not None:
            self.detail_map = m.get('DetailMap')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        self.param_list = []
        if m.get('ParamList') is not None:
            for k in m.get('ParamList'):
                temp_model = GetRuleResponseBodyDataTargetsParamList()
                self.param_list.append(temp_model.from_map(k))
        if m.get('PushRetryStrategy') is not None:
            self.push_retry_strategy = m.get('PushRetryStrategy')
        if m.get('PushSelector') is not None:
            self.push_selector = m.get('PushSelector')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetRuleResponseBodyData(TeaModel):
    def __init__(
        self,
        created_timestamp: int = None,
        description: str = None,
        event_bus_name: str = None,
        filter_pattern: str = None,
        rule_arn: str = None,
        rule_name: str = None,
        status: str = None,
        targets: List[GetRuleResponseBodyDataTargets] = None,
    ):
        self.created_timestamp = created_timestamp
        self.description = description
        self.event_bus_name = event_bus_name
        self.filter_pattern = filter_pattern
        self.rule_arn = rule_arn
        self.rule_name = rule_name
        self.status = status
        self.targets = targets

    def validate(self):
        if self.targets:
            for k in self.targets:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_timestamp is not None:
            result['CreatedTimestamp'] = self.created_timestamp
        if self.description is not None:
            result['Description'] = self.description
        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name
        if self.filter_pattern is not None:
            result['FilterPattern'] = self.filter_pattern
        if self.rule_arn is not None:
            result['RuleARN'] = self.rule_arn
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.status is not None:
            result['Status'] = self.status
        result['Targets'] = []
        if self.targets is not None:
            for k in self.targets:
                result['Targets'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedTimestamp') is not None:
            self.created_timestamp = m.get('CreatedTimestamp')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')
        if m.get('FilterPattern') is not None:
            self.filter_pattern = m.get('FilterPattern')
        if m.get('RuleARN') is not None:
            self.rule_arn = m.get('RuleARN')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.targets = []
        if m.get('Targets') is not None:
            for k in m.get('Targets'):
                temp_model = GetRuleResponseBodyDataTargets()
                self.targets.append(temp_model.from_map(k))
        return self


class GetRuleResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetRuleResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetRuleResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetRuleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSchemaRequest(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        schema_id: str = None,
    ):
        self.group_id = group_id
        self.schema_id = schema_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.schema_id is not None:
            result['SchemaId'] = self.schema_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('SchemaId') is not None:
            self.schema_id = m.get('SchemaId')
        return self


class GetSchemaResponseBodyData(TeaModel):
    def __init__(
        self,
        compatible_type: str = None,
        content: str = None,
        created_timestamp: int = None,
        description: str = None,
        format: str = None,
        group_id: str = None,
        latest_version: int = None,
        schema_id: str = None,
        updated_timestamp: int = None,
    ):
        self.compatible_type = compatible_type
        self.content = content
        self.created_timestamp = created_timestamp
        self.description = description
        self.format = format
        self.group_id = group_id
        self.latest_version = latest_version
        self.schema_id = schema_id
        self.updated_timestamp = updated_timestamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compatible_type is not None:
            result['CompatibleType'] = self.compatible_type
        if self.content is not None:
            result['Content'] = self.content
        if self.created_timestamp is not None:
            result['CreatedTimestamp'] = self.created_timestamp
        if self.description is not None:
            result['Description'] = self.description
        if self.format is not None:
            result['Format'] = self.format
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.latest_version is not None:
            result['LatestVersion'] = self.latest_version
        if self.schema_id is not None:
            result['SchemaId'] = self.schema_id
        if self.updated_timestamp is not None:
            result['UpdatedTimestamp'] = self.updated_timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompatibleType') is not None:
            self.compatible_type = m.get('CompatibleType')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('CreatedTimestamp') is not None:
            self.created_timestamp = m.get('CreatedTimestamp')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Format') is not None:
            self.format = m.get('Format')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('LatestVersion') is not None:
            self.latest_version = m.get('LatestVersion')
        if m.get('SchemaId') is not None:
            self.schema_id = m.get('SchemaId')
        if m.get('UpdatedTimestamp') is not None:
            self.updated_timestamp = m.get('UpdatedTimestamp')
        return self


class GetSchemaResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetSchemaResponseBodyData = None,
        http_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_code = http_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetSchemaResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetSchemaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetSchemaResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetSchemaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSchemaGroupRequest(TeaModel):
    def __init__(
        self,
        group_id: str = None,
    ):
        self.group_id = group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        return self


class GetSchemaGroupResponseBodyData(TeaModel):
    def __init__(
        self,
        created_timestamp: int = None,
        description: str = None,
        format: str = None,
        group_arn: str = None,
        group_id: str = None,
        updated_timestamp: int = None,
    ):
        self.created_timestamp = created_timestamp
        self.description = description
        self.format = format
        self.group_arn = group_arn
        self.group_id = group_id
        self.updated_timestamp = updated_timestamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_timestamp is not None:
            result['CreatedTimestamp'] = self.created_timestamp
        if self.description is not None:
            result['Description'] = self.description
        if self.format is not None:
            result['Format'] = self.format
        if self.group_arn is not None:
            result['GroupARN'] = self.group_arn
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.updated_timestamp is not None:
            result['UpdatedTimestamp'] = self.updated_timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedTimestamp') is not None:
            self.created_timestamp = m.get('CreatedTimestamp')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Format') is not None:
            self.format = m.get('Format')
        if m.get('GroupARN') is not None:
            self.group_arn = m.get('GroupARN')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('UpdatedTimestamp') is not None:
            self.updated_timestamp = m.get('UpdatedTimestamp')
        return self


class GetSchemaGroupResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetSchemaGroupResponseBodyData = None,
        http_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_code = http_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetSchemaGroupResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetSchemaGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetSchemaGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetSchemaGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSchemaVersionRequest(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        schema_id: str = None,
        version_number: int = None,
    ):
        self.group_id = group_id
        self.schema_id = schema_id
        self.version_number = version_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.schema_id is not None:
            result['SchemaId'] = self.schema_id
        if self.version_number is not None:
            result['VersionNumber'] = self.version_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('SchemaId') is not None:
            self.schema_id = m.get('SchemaId')
        if m.get('VersionNumber') is not None:
            self.version_number = m.get('VersionNumber')
        return self


class GetSchemaVersionResponseBodyData(TeaModel):
    def __init__(
        self,
        content: str = None,
        created_timestamp: int = None,
        format: str = None,
        group_id: str = None,
        schema_id: str = None,
        schema_version_arn: str = None,
        updated_timestamp: int = None,
        version: int = None,
    ):
        self.content = content
        self.created_timestamp = created_timestamp
        self.format = format
        self.group_id = group_id
        self.schema_id = schema_id
        self.schema_version_arn = schema_version_arn
        self.updated_timestamp = updated_timestamp
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.created_timestamp is not None:
            result['CreatedTimestamp'] = self.created_timestamp
        if self.format is not None:
            result['Format'] = self.format
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.schema_id is not None:
            result['SchemaId'] = self.schema_id
        if self.schema_version_arn is not None:
            result['SchemaVersionARN'] = self.schema_version_arn
        if self.updated_timestamp is not None:
            result['UpdatedTimestamp'] = self.updated_timestamp
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('CreatedTimestamp') is not None:
            self.created_timestamp = m.get('CreatedTimestamp')
        if m.get('Format') is not None:
            self.format = m.get('Format')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('SchemaId') is not None:
            self.schema_id = m.get('SchemaId')
        if m.get('SchemaVersionARN') is not None:
            self.schema_version_arn = m.get('SchemaVersionARN')
        if m.get('UpdatedTimestamp') is not None:
            self.updated_timestamp = m.get('UpdatedTimestamp')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class GetSchemaVersionResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetSchemaVersionResponseBodyData = None,
        http_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_code = http_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetSchemaVersionResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetSchemaVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetSchemaVersionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetSchemaVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSourceTaskRequest(TeaModel):
    def __init__(
        self,
        task_id: str = None,
    ):
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class GetSourceTaskResponseBodyData(TeaModel):
    def __init__(
        self,
        bus_name: str = None,
        id: str = None,
        last_date_sync_time: str = None,
        name: str = None,
        sended_records: int = None,
        source_config: Dict[str, Any] = None,
        source_type: str = None,
        status: str = None,
    ):
        self.bus_name = bus_name
        self.id = id
        self.last_date_sync_time = last_date_sync_time
        self.name = name
        self.sended_records = sended_records
        self.source_config = source_config
        self.source_type = source_type
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bus_name is not None:
            result['BusName'] = self.bus_name
        if self.id is not None:
            result['Id'] = self.id
        if self.last_date_sync_time is not None:
            result['LastDateSyncTime'] = self.last_date_sync_time
        if self.name is not None:
            result['Name'] = self.name
        if self.sended_records is not None:
            result['SendedRecords'] = self.sended_records
        if self.source_config is not None:
            result['SourceConfig'] = self.source_config
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusName') is not None:
            self.bus_name = m.get('BusName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LastDateSyncTime') is not None:
            self.last_date_sync_time = m.get('LastDateSyncTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SendedRecords') is not None:
            self.sended_records = m.get('SendedRecords')
        if m.get('SourceConfig') is not None:
            self.source_config = m.get('SourceConfig')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetSourceTaskResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetSourceTaskResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetSourceTaskResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetSourceTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetSourceTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetSourceTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListACSEventsSchemaVersionsRequest(TeaModel):
    def __init__(
        self,
        limit: int = None,
        next_token: str = None,
        schema_id: str = None,
    ):
        self.limit = limit
        self.next_token = next_token
        self.schema_id = schema_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.schema_id is not None:
            result['SchemaId'] = self.schema_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('SchemaId') is not None:
            self.schema_id = m.get('SchemaId')
        return self


class ListACSEventsSchemaVersionsResponseBodyDataVersions(TeaModel):
    def __init__(
        self,
        content: str = None,
        data_sample: str = None,
        format: str = None,
        group_id: str = None,
        schema_id: str = None,
        version: int = None,
    ):
        self.content = content
        self.data_sample = data_sample
        self.format = format
        self.group_id = group_id
        self.schema_id = schema_id
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.data_sample is not None:
            result['DataSample'] = self.data_sample
        if self.format is not None:
            result['Format'] = self.format
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.schema_id is not None:
            result['SchemaId'] = self.schema_id
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('DataSample') is not None:
            self.data_sample = m.get('DataSample')
        if m.get('Format') is not None:
            self.format = m.get('Format')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('SchemaId') is not None:
            self.schema_id = m.get('SchemaId')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class ListACSEventsSchemaVersionsResponseBodyData(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        total: int = None,
        versions: List[ListACSEventsSchemaVersionsResponseBodyDataVersions] = None,
    ):
        self.next_token = next_token
        self.total = total
        self.versions = versions

    def validate(self):
        if self.versions:
            for k in self.versions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.total is not None:
            result['Total'] = self.total
        result['Versions'] = []
        if self.versions is not None:
            for k in self.versions:
                result['Versions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        self.versions = []
        if m.get('Versions') is not None:
            for k in m.get('Versions'):
                temp_model = ListACSEventsSchemaVersionsResponseBodyDataVersions()
                self.versions.append(temp_model.from_map(k))
        return self


class ListACSEventsSchemaVersionsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListACSEventsSchemaVersionsResponseBodyData = None,
        http_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_code = http_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ListACSEventsSchemaVersionsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListACSEventsSchemaVersionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListACSEventsSchemaVersionsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ListACSEventsSchemaVersionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListACSEventsSchemasRequest(TeaModel):
    def __init__(
        self,
        limit: int = None,
        next_token: str = None,
        prefix: str = None,
    ):
        self.limit = limit
        self.next_token = next_token
        self.prefix = prefix

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.prefix is not None:
            result['Prefix'] = self.prefix
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Prefix') is not None:
            self.prefix = m.get('Prefix')
        return self


class ListACSEventsSchemasResponseBodyDataSchemas(TeaModel):
    def __init__(
        self,
        description: str = None,
        format: str = None,
        group_id: str = None,
        latest_version: int = None,
        schema_id: str = None,
    ):
        self.description = description
        self.format = format
        self.group_id = group_id
        self.latest_version = latest_version
        self.schema_id = schema_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.format is not None:
            result['Format'] = self.format
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.latest_version is not None:
            result['LatestVersion'] = self.latest_version
        if self.schema_id is not None:
            result['SchemaId'] = self.schema_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Format') is not None:
            self.format = m.get('Format')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('LatestVersion') is not None:
            self.latest_version = m.get('LatestVersion')
        if m.get('SchemaId') is not None:
            self.schema_id = m.get('SchemaId')
        return self


class ListACSEventsSchemasResponseBodyData(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        schemas: List[ListACSEventsSchemasResponseBodyDataSchemas] = None,
        total: int = None,
    ):
        self.next_token = next_token
        self.schemas = schemas
        self.total = total

    def validate(self):
        if self.schemas:
            for k in self.schemas:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['Schemas'] = []
        if self.schemas is not None:
            for k in self.schemas:
                result['Schemas'].append(k.to_map() if k else None)
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.schemas = []
        if m.get('Schemas') is not None:
            for k in m.get('Schemas'):
                temp_model = ListACSEventsSchemasResponseBodyDataSchemas()
                self.schemas.append(temp_model.from_map(k))
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListACSEventsSchemasResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListACSEventsSchemasResponseBodyData = None,
        http_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_code = http_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ListACSEventsSchemasResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListACSEventsSchemasResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListACSEventsSchemasResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ListACSEventsSchemasResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAliyunOfficialEventSourcesRequest(TeaModel):
    def __init__(
        self,
        limit: int = None,
        name_prefix: str = None,
        next_token: str = None,
        type: bytes = None,
    ):
        self.limit = limit
        self.name_prefix = name_prefix
        self.next_token = next_token
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.name_prefix is not None:
            result['NamePrefix'] = self.name_prefix
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('NamePrefix') is not None:
            self.name_prefix = m.get('NamePrefix')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListAliyunOfficialEventSourcesResponseBodyDataEventSourceListEventTypes(TeaModel):
    def __init__(
        self,
        description: str = None,
        group_name: str = None,
        name: str = None,
        short_name: str = None,
    ):
        self.description = description
        self.group_name = group_name
        self.name = name
        self.short_name = short_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.name is not None:
            result['Name'] = self.name
        if self.short_name is not None:
            result['ShortName'] = self.short_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ShortName') is not None:
            self.short_name = m.get('ShortName')
        return self


class ListAliyunOfficialEventSourcesResponseBodyDataEventSourceList(TeaModel):
    def __init__(
        self,
        arn: str = None,
        ctime: float = None,
        description: str = None,
        event_bus_name: str = None,
        event_types: List[ListAliyunOfficialEventSourcesResponseBodyDataEventSourceListEventTypes] = None,
        name: str = None,
        status: str = None,
        type: str = None,
    ):
        self.arn = arn
        self.ctime = ctime
        self.description = description
        self.event_bus_name = event_bus_name
        self.event_types = event_types
        self.name = name
        self.status = status
        self.type = type

    def validate(self):
        if self.event_types:
            for k in self.event_types:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arn is not None:
            result['Arn'] = self.arn
        if self.ctime is not None:
            result['Ctime'] = self.ctime
        if self.description is not None:
            result['Description'] = self.description
        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name
        result['EventTypes'] = []
        if self.event_types is not None:
            for k in self.event_types:
                result['EventTypes'].append(k.to_map() if k else None)
        if self.name is not None:
            result['Name'] = self.name
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        if m.get('Ctime') is not None:
            self.ctime = m.get('Ctime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')
        self.event_types = []
        if m.get('EventTypes') is not None:
            for k in m.get('EventTypes'):
                temp_model = ListAliyunOfficialEventSourcesResponseBodyDataEventSourceListEventTypes()
                self.event_types.append(temp_model.from_map(k))
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListAliyunOfficialEventSourcesResponseBodyData(TeaModel):
    def __init__(
        self,
        event_source_list: List[ListAliyunOfficialEventSourcesResponseBodyDataEventSourceList] = None,
        next_token: str = None,
        total: float = None,
    ):
        self.event_source_list = event_source_list
        self.next_token = next_token
        self.total = total

    def validate(self):
        if self.event_source_list:
            for k in self.event_source_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['EventSourceList'] = []
        if self.event_source_list is not None:
            for k in self.event_source_list:
                result['EventSourceList'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.event_source_list = []
        if m.get('EventSourceList') is not None:
            for k in m.get('EventSourceList'):
                temp_model = ListAliyunOfficialEventSourcesResponseBodyDataEventSourceList()
                self.event_source_list.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListAliyunOfficialEventSourcesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListAliyunOfficialEventSourcesResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ListAliyunOfficialEventSourcesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListAliyunOfficialEventSourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAliyunOfficialEventSourcesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ListAliyunOfficialEventSourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEventBusesRequest(TeaModel):
    def __init__(
        self,
        event_bus_type: str = None,
        limit: int = None,
        name_prefix: str = None,
        next_token: str = None,
    ):
        self.event_bus_type = event_bus_type
        self.limit = limit
        self.name_prefix = name_prefix
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_bus_type is not None:
            result['EventBusType'] = self.event_bus_type
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.name_prefix is not None:
            result['NamePrefix'] = self.name_prefix
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventBusType') is not None:
            self.event_bus_type = m.get('EventBusType')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('NamePrefix') is not None:
            self.name_prefix = m.get('NamePrefix')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class ListEventBusesResponseBodyDataEventBuses(TeaModel):
    def __init__(
        self,
        create_timestamp: int = None,
        description: str = None,
        event_bus_arn: str = None,
        event_bus_name: str = None,
    ):
        self.create_timestamp = create_timestamp
        self.description = description
        self.event_bus_arn = event_bus_arn
        self.event_bus_name = event_bus_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_timestamp is not None:
            result['CreateTimestamp'] = self.create_timestamp
        if self.description is not None:
            result['Description'] = self.description
        if self.event_bus_arn is not None:
            result['EventBusARN'] = self.event_bus_arn
        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTimestamp') is not None:
            self.create_timestamp = m.get('CreateTimestamp')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EventBusARN') is not None:
            self.event_bus_arn = m.get('EventBusARN')
        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')
        return self


class ListEventBusesResponseBodyData(TeaModel):
    def __init__(
        self,
        event_buses: List[ListEventBusesResponseBodyDataEventBuses] = None,
        next_token: str = None,
        total: int = None,
    ):
        self.event_buses = event_buses
        self.next_token = next_token
        self.total = total

    def validate(self):
        if self.event_buses:
            for k in self.event_buses:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['EventBuses'] = []
        if self.event_buses is not None:
            for k in self.event_buses:
                result['EventBuses'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.event_buses = []
        if m.get('EventBuses') is not None:
            for k in m.get('EventBuses'):
                temp_model = ListEventBusesResponseBodyDataEventBuses()
                self.event_buses.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListEventBusesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListEventBusesResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ListEventBusesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListEventBusesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListEventBusesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ListEventBusesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEventSourcesRequest(TeaModel):
    def __init__(
        self,
        limit: int = None,
        name_prefix: str = None,
        next_token: str = None,
        type: bytes = None,
    ):
        self.limit = limit
        self.name_prefix = name_prefix
        self.next_token = next_token
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.name_prefix is not None:
            result['NamePrefix'] = self.name_prefix
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('NamePrefix') is not None:
            self.name_prefix = m.get('NamePrefix')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListEventSourcesResponseBodyDataEventTypes(TeaModel):
    def __init__(
        self,
        description: str = None,
        event_source_name: str = None,
        group_name: str = None,
        name: str = None,
        short_name: str = None,
    ):
        self.description = description
        self.event_source_name = event_source_name
        self.group_name = group_name
        self.name = name
        self.short_name = short_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.event_source_name is not None:
            result['EventSourceName'] = self.event_source_name
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.name is not None:
            result['Name'] = self.name
        if self.short_name is not None:
            result['ShortName'] = self.short_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EventSourceName') is not None:
            self.event_source_name = m.get('EventSourceName')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ShortName') is not None:
            self.short_name = m.get('ShortName')
        return self


class ListEventSourcesResponseBodyData(TeaModel):
    def __init__(
        self,
        arn: str = None,
        attached_buses: List[str] = None,
        ctime: float = None,
        description: str = None,
        event_types: List[ListEventSourcesResponseBodyDataEventTypes] = None,
        external_source_config: Dict[str, Any] = None,
        external_source_type: str = None,
        full_name: str = None,
        linked_external_source: bool = None,
        name: str = None,
        status: str = None,
        type: str = None,
    ):
        self.arn = arn
        self.attached_buses = attached_buses
        self.ctime = ctime
        self.description = description
        self.event_types = event_types
        self.external_source_config = external_source_config
        self.external_source_type = external_source_type
        self.full_name = full_name
        self.linked_external_source = linked_external_source
        self.name = name
        self.status = status
        self.type = type

    def validate(self):
        if self.event_types:
            for k in self.event_types:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arn is not None:
            result['ARN'] = self.arn
        if self.attached_buses is not None:
            result['AttachedBuses'] = self.attached_buses
        if self.ctime is not None:
            result['Ctime'] = self.ctime
        if self.description is not None:
            result['Description'] = self.description
        result['EventTypes'] = []
        if self.event_types is not None:
            for k in self.event_types:
                result['EventTypes'].append(k.to_map() if k else None)
        if self.external_source_config is not None:
            result['ExternalSourceConfig'] = self.external_source_config
        if self.external_source_type is not None:
            result['ExternalSourceType'] = self.external_source_type
        if self.full_name is not None:
            result['FullName'] = self.full_name
        if self.linked_external_source is not None:
            result['LinkedExternalSource'] = self.linked_external_source
        if self.name is not None:
            result['Name'] = self.name
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ARN') is not None:
            self.arn = m.get('ARN')
        if m.get('AttachedBuses') is not None:
            self.attached_buses = m.get('AttachedBuses')
        if m.get('Ctime') is not None:
            self.ctime = m.get('Ctime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        self.event_types = []
        if m.get('EventTypes') is not None:
            for k in m.get('EventTypes'):
                temp_model = ListEventSourcesResponseBodyDataEventTypes()
                self.event_types.append(temp_model.from_map(k))
        if m.get('ExternalSourceConfig') is not None:
            self.external_source_config = m.get('ExternalSourceConfig')
        if m.get('ExternalSourceType') is not None:
            self.external_source_type = m.get('ExternalSourceType')
        if m.get('FullName') is not None:
            self.full_name = m.get('FullName')
        if m.get('LinkedExternalSource') is not None:
            self.linked_external_source = m.get('LinkedExternalSource')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListEventSourcesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[ListEventSourcesResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListEventSourcesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListEventSourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListEventSourcesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ListEventSourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEventStreamingRequest(TeaModel):
    def __init__(
        self,
        limit: int = None,
        name_prefix: str = None,
        next_token: str = None,
        sink_type: str = None,
        source_type: str = None,
        tag: str = None,
    ):
        self.limit = limit
        self.name_prefix = name_prefix
        self.next_token = next_token
        self.sink_type = sink_type
        self.source_type = source_type
        self.tag = tag

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.name_prefix is not None:
            result['NamePrefix'] = self.name_prefix
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.sink_type is not None:
            result['SinkType'] = self.sink_type
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.tag is not None:
            result['Tag'] = self.tag
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('NamePrefix') is not None:
            self.name_prefix = m.get('NamePrefix')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('SinkType') is not None:
            self.sink_type = m.get('SinkType')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        return self


class ListEventStreamingResponseBodyDataEventStreamingsRunOptionsBatchWindow(TeaModel):
    def __init__(
        self,
        count_based_window: int = None,
        time_based_window: int = None,
    ):
        self.count_based_window = count_based_window
        self.time_based_window = time_based_window

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count_based_window is not None:
            result['CountBasedWindow'] = self.count_based_window
        if self.time_based_window is not None:
            result['TimeBasedWindow'] = self.time_based_window
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CountBasedWindow') is not None:
            self.count_based_window = m.get('CountBasedWindow')
        if m.get('TimeBasedWindow') is not None:
            self.time_based_window = m.get('TimeBasedWindow')
        return self


class ListEventStreamingResponseBodyDataEventStreamingsRunOptionsDeadLetterQueue(TeaModel):
    def __init__(
        self,
        arn: str = None,
    ):
        self.arn = arn

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arn is not None:
            result['Arn'] = self.arn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        return self


class ListEventStreamingResponseBodyDataEventStreamingsRunOptionsRetryStrategy(TeaModel):
    def __init__(
        self,
        maximum_event_age_in_seconds: float = None,
        maximum_retry_attempts: float = None,
        push_retry_strategy: str = None,
    ):
        self.maximum_event_age_in_seconds = maximum_event_age_in_seconds
        self.maximum_retry_attempts = maximum_retry_attempts
        self.push_retry_strategy = push_retry_strategy

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.maximum_event_age_in_seconds is not None:
            result['MaximumEventAgeInSeconds'] = self.maximum_event_age_in_seconds
        if self.maximum_retry_attempts is not None:
            result['MaximumRetryAttempts'] = self.maximum_retry_attempts
        if self.push_retry_strategy is not None:
            result['PushRetryStrategy'] = self.push_retry_strategy
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaximumEventAgeInSeconds') is not None:
            self.maximum_event_age_in_seconds = m.get('MaximumEventAgeInSeconds')
        if m.get('MaximumRetryAttempts') is not None:
            self.maximum_retry_attempts = m.get('MaximumRetryAttempts')
        if m.get('PushRetryStrategy') is not None:
            self.push_retry_strategy = m.get('PushRetryStrategy')
        return self


class ListEventStreamingResponseBodyDataEventStreamingsRunOptions(TeaModel):
    def __init__(
        self,
        batch_window: ListEventStreamingResponseBodyDataEventStreamingsRunOptionsBatchWindow = None,
        dead_letter_queue: ListEventStreamingResponseBodyDataEventStreamingsRunOptionsDeadLetterQueue = None,
        errors_tolerance: str = None,
        maximum_tasks: int = None,
        retry_strategy: ListEventStreamingResponseBodyDataEventStreamingsRunOptionsRetryStrategy = None,
    ):
        self.batch_window = batch_window
        self.dead_letter_queue = dead_letter_queue
        self.errors_tolerance = errors_tolerance
        self.maximum_tasks = maximum_tasks
        self.retry_strategy = retry_strategy

    def validate(self):
        if self.batch_window:
            self.batch_window.validate()
        if self.dead_letter_queue:
            self.dead_letter_queue.validate()
        if self.retry_strategy:
            self.retry_strategy.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.batch_window is not None:
            result['BatchWindow'] = self.batch_window.to_map()
        if self.dead_letter_queue is not None:
            result['DeadLetterQueue'] = self.dead_letter_queue.to_map()
        if self.errors_tolerance is not None:
            result['ErrorsTolerance'] = self.errors_tolerance
        if self.maximum_tasks is not None:
            result['MaximumTasks'] = self.maximum_tasks
        if self.retry_strategy is not None:
            result['RetryStrategy'] = self.retry_strategy.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BatchWindow') is not None:
            temp_model = ListEventStreamingResponseBodyDataEventStreamingsRunOptionsBatchWindow()
            self.batch_window = temp_model.from_map(m['BatchWindow'])
        if m.get('DeadLetterQueue') is not None:
            temp_model = ListEventStreamingResponseBodyDataEventStreamingsRunOptionsDeadLetterQueue()
            self.dead_letter_queue = temp_model.from_map(m['DeadLetterQueue'])
        if m.get('ErrorsTolerance') is not None:
            self.errors_tolerance = m.get('ErrorsTolerance')
        if m.get('MaximumTasks') is not None:
            self.maximum_tasks = m.get('MaximumTasks')
        if m.get('RetryStrategy') is not None:
            temp_model = ListEventStreamingResponseBodyDataEventStreamingsRunOptionsRetryStrategy()
            self.retry_strategy = temp_model.from_map(m['RetryStrategy'])
        return self


class ListEventStreamingResponseBodyDataEventStreamingsSinkSinkFcParametersBody(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListEventStreamingResponseBodyDataEventStreamingsSinkSinkFcParametersFunctionName(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListEventStreamingResponseBodyDataEventStreamingsSinkSinkFcParametersInvocationType(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListEventStreamingResponseBodyDataEventStreamingsSinkSinkFcParametersQualifier(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListEventStreamingResponseBodyDataEventStreamingsSinkSinkFcParametersServiceName(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListEventStreamingResponseBodyDataEventStreamingsSinkSinkFcParameters(TeaModel):
    def __init__(
        self,
        body: ListEventStreamingResponseBodyDataEventStreamingsSinkSinkFcParametersBody = None,
        function_name: ListEventStreamingResponseBodyDataEventStreamingsSinkSinkFcParametersFunctionName = None,
        invocation_type: ListEventStreamingResponseBodyDataEventStreamingsSinkSinkFcParametersInvocationType = None,
        qualifier: ListEventStreamingResponseBodyDataEventStreamingsSinkSinkFcParametersQualifier = None,
        service_name: ListEventStreamingResponseBodyDataEventStreamingsSinkSinkFcParametersServiceName = None,
    ):
        self.body = body
        self.function_name = function_name
        self.invocation_type = invocation_type
        self.qualifier = qualifier
        self.service_name = service_name

    def validate(self):
        if self.body:
            self.body.validate()
        if self.function_name:
            self.function_name.validate()
        if self.invocation_type:
            self.invocation_type.validate()
        if self.qualifier:
            self.qualifier.validate()
        if self.service_name:
            self.service_name.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['Body'] = self.body.to_map()
        if self.function_name is not None:
            result['FunctionName'] = self.function_name.to_map()
        if self.invocation_type is not None:
            result['InvocationType'] = self.invocation_type.to_map()
        if self.qualifier is not None:
            result['Qualifier'] = self.qualifier.to_map()
        if self.service_name is not None:
            result['ServiceName'] = self.service_name.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Body') is not None:
            temp_model = ListEventStreamingResponseBodyDataEventStreamingsSinkSinkFcParametersBody()
            self.body = temp_model.from_map(m['Body'])
        if m.get('FunctionName') is not None:
            temp_model = ListEventStreamingResponseBodyDataEventStreamingsSinkSinkFcParametersFunctionName()
            self.function_name = temp_model.from_map(m['FunctionName'])
        if m.get('InvocationType') is not None:
            temp_model = ListEventStreamingResponseBodyDataEventStreamingsSinkSinkFcParametersInvocationType()
            self.invocation_type = temp_model.from_map(m['InvocationType'])
        if m.get('Qualifier') is not None:
            temp_model = ListEventStreamingResponseBodyDataEventStreamingsSinkSinkFcParametersQualifier()
            self.qualifier = temp_model.from_map(m['Qualifier'])
        if m.get('ServiceName') is not None:
            temp_model = ListEventStreamingResponseBodyDataEventStreamingsSinkSinkFcParametersServiceName()
            self.service_name = temp_model.from_map(m['ServiceName'])
        return self


class ListEventStreamingResponseBodyDataEventStreamingsSinkSinkKafkaParametersAcks(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListEventStreamingResponseBodyDataEventStreamingsSinkSinkKafkaParametersInstanceId(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListEventStreamingResponseBodyDataEventStreamingsSinkSinkKafkaParametersKey(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListEventStreamingResponseBodyDataEventStreamingsSinkSinkKafkaParametersSaslUser(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListEventStreamingResponseBodyDataEventStreamingsSinkSinkKafkaParametersTopic(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListEventStreamingResponseBodyDataEventStreamingsSinkSinkKafkaParametersValue(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListEventStreamingResponseBodyDataEventStreamingsSinkSinkKafkaParameters(TeaModel):
    def __init__(
        self,
        acks: ListEventStreamingResponseBodyDataEventStreamingsSinkSinkKafkaParametersAcks = None,
        instance_id: ListEventStreamingResponseBodyDataEventStreamingsSinkSinkKafkaParametersInstanceId = None,
        key: ListEventStreamingResponseBodyDataEventStreamingsSinkSinkKafkaParametersKey = None,
        sasl_user: ListEventStreamingResponseBodyDataEventStreamingsSinkSinkKafkaParametersSaslUser = None,
        topic: ListEventStreamingResponseBodyDataEventStreamingsSinkSinkKafkaParametersTopic = None,
        value: ListEventStreamingResponseBodyDataEventStreamingsSinkSinkKafkaParametersValue = None,
    ):
        self.acks = acks
        self.instance_id = instance_id
        self.key = key
        self.sasl_user = sasl_user
        self.topic = topic
        self.value = value

    def validate(self):
        if self.acks:
            self.acks.validate()
        if self.instance_id:
            self.instance_id.validate()
        if self.key:
            self.key.validate()
        if self.sasl_user:
            self.sasl_user.validate()
        if self.topic:
            self.topic.validate()
        if self.value:
            self.value.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acks is not None:
            result['Acks'] = self.acks.to_map()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id.to_map()
        if self.key is not None:
            result['Key'] = self.key.to_map()
        if self.sasl_user is not None:
            result['SaslUser'] = self.sasl_user.to_map()
        if self.topic is not None:
            result['Topic'] = self.topic.to_map()
        if self.value is not None:
            result['Value'] = self.value.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Acks') is not None:
            temp_model = ListEventStreamingResponseBodyDataEventStreamingsSinkSinkKafkaParametersAcks()
            self.acks = temp_model.from_map(m['Acks'])
        if m.get('InstanceId') is not None:
            temp_model = ListEventStreamingResponseBodyDataEventStreamingsSinkSinkKafkaParametersInstanceId()
            self.instance_id = temp_model.from_map(m['InstanceId'])
        if m.get('Key') is not None:
            temp_model = ListEventStreamingResponseBodyDataEventStreamingsSinkSinkKafkaParametersKey()
            self.key = temp_model.from_map(m['Key'])
        if m.get('SaslUser') is not None:
            temp_model = ListEventStreamingResponseBodyDataEventStreamingsSinkSinkKafkaParametersSaslUser()
            self.sasl_user = temp_model.from_map(m['SaslUser'])
        if m.get('Topic') is not None:
            temp_model = ListEventStreamingResponseBodyDataEventStreamingsSinkSinkKafkaParametersTopic()
            self.topic = temp_model.from_map(m['Topic'])
        if m.get('Value') is not None:
            temp_model = ListEventStreamingResponseBodyDataEventStreamingsSinkSinkKafkaParametersValue()
            self.value = temp_model.from_map(m['Value'])
        return self


class ListEventStreamingResponseBodyDataEventStreamingsSinkSinkMNSParametersBody(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListEventStreamingResponseBodyDataEventStreamingsSinkSinkMNSParametersIsBase64Encode(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListEventStreamingResponseBodyDataEventStreamingsSinkSinkMNSParametersQueueName(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListEventStreamingResponseBodyDataEventStreamingsSinkSinkMNSParameters(TeaModel):
    def __init__(
        self,
        body: ListEventStreamingResponseBodyDataEventStreamingsSinkSinkMNSParametersBody = None,
        is_base_64encode: ListEventStreamingResponseBodyDataEventStreamingsSinkSinkMNSParametersIsBase64Encode = None,
        queue_name: ListEventStreamingResponseBodyDataEventStreamingsSinkSinkMNSParametersQueueName = None,
    ):
        self.body = body
        self.is_base_64encode = is_base_64encode
        self.queue_name = queue_name

    def validate(self):
        if self.body:
            self.body.validate()
        if self.is_base_64encode:
            self.is_base_64encode.validate()
        if self.queue_name:
            self.queue_name.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['Body'] = self.body.to_map()
        if self.is_base_64encode is not None:
            result['IsBase64Encode'] = self.is_base_64encode.to_map()
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Body') is not None:
            temp_model = ListEventStreamingResponseBodyDataEventStreamingsSinkSinkMNSParametersBody()
            self.body = temp_model.from_map(m['Body'])
        if m.get('IsBase64Encode') is not None:
            temp_model = ListEventStreamingResponseBodyDataEventStreamingsSinkSinkMNSParametersIsBase64Encode()
            self.is_base_64encode = temp_model.from_map(m['IsBase64Encode'])
        if m.get('QueueName') is not None:
            temp_model = ListEventStreamingResponseBodyDataEventStreamingsSinkSinkMNSParametersQueueName()
            self.queue_name = temp_model.from_map(m['QueueName'])
        return self


class ListEventStreamingResponseBodyDataEventStreamingsSinkSinkRabbitMQParametersBody(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListEventStreamingResponseBodyDataEventStreamingsSinkSinkRabbitMQParametersExchange(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListEventStreamingResponseBodyDataEventStreamingsSinkSinkRabbitMQParametersInstanceId(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListEventStreamingResponseBodyDataEventStreamingsSinkSinkRabbitMQParametersMessageId(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListEventStreamingResponseBodyDataEventStreamingsSinkSinkRabbitMQParametersProperties(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListEventStreamingResponseBodyDataEventStreamingsSinkSinkRabbitMQParametersQueueName(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListEventStreamingResponseBodyDataEventStreamingsSinkSinkRabbitMQParametersRoutingKey(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListEventStreamingResponseBodyDataEventStreamingsSinkSinkRabbitMQParametersTargetType(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListEventStreamingResponseBodyDataEventStreamingsSinkSinkRabbitMQParametersVirtualHostName(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListEventStreamingResponseBodyDataEventStreamingsSinkSinkRabbitMQParameters(TeaModel):
    def __init__(
        self,
        body: ListEventStreamingResponseBodyDataEventStreamingsSinkSinkRabbitMQParametersBody = None,
        exchange: ListEventStreamingResponseBodyDataEventStreamingsSinkSinkRabbitMQParametersExchange = None,
        instance_id: ListEventStreamingResponseBodyDataEventStreamingsSinkSinkRabbitMQParametersInstanceId = None,
        message_id: ListEventStreamingResponseBodyDataEventStreamingsSinkSinkRabbitMQParametersMessageId = None,
        properties: ListEventStreamingResponseBodyDataEventStreamingsSinkSinkRabbitMQParametersProperties = None,
        queue_name: ListEventStreamingResponseBodyDataEventStreamingsSinkSinkRabbitMQParametersQueueName = None,
        routing_key: ListEventStreamingResponseBodyDataEventStreamingsSinkSinkRabbitMQParametersRoutingKey = None,
        target_type: ListEventStreamingResponseBodyDataEventStreamingsSinkSinkRabbitMQParametersTargetType = None,
        virtual_host_name: ListEventStreamingResponseBodyDataEventStreamingsSinkSinkRabbitMQParametersVirtualHostName = None,
    ):
        self.body = body
        self.exchange = exchange
        self.instance_id = instance_id
        self.message_id = message_id
        self.properties = properties
        self.queue_name = queue_name
        self.routing_key = routing_key
        self.target_type = target_type
        self.virtual_host_name = virtual_host_name

    def validate(self):
        if self.body:
            self.body.validate()
        if self.exchange:
            self.exchange.validate()
        if self.instance_id:
            self.instance_id.validate()
        if self.message_id:
            self.message_id.validate()
        if self.properties:
            self.properties.validate()
        if self.queue_name:
            self.queue_name.validate()
        if self.routing_key:
            self.routing_key.validate()
        if self.target_type:
            self.target_type.validate()
        if self.virtual_host_name:
            self.virtual_host_name.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['Body'] = self.body.to_map()
        if self.exchange is not None:
            result['Exchange'] = self.exchange.to_map()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id.to_map()
        if self.message_id is not None:
            result['MessageId'] = self.message_id.to_map()
        if self.properties is not None:
            result['Properties'] = self.properties.to_map()
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name.to_map()
        if self.routing_key is not None:
            result['RoutingKey'] = self.routing_key.to_map()
        if self.target_type is not None:
            result['TargetType'] = self.target_type.to_map()
        if self.virtual_host_name is not None:
            result['VirtualHostName'] = self.virtual_host_name.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Body') is not None:
            temp_model = ListEventStreamingResponseBodyDataEventStreamingsSinkSinkRabbitMQParametersBody()
            self.body = temp_model.from_map(m['Body'])
        if m.get('Exchange') is not None:
            temp_model = ListEventStreamingResponseBodyDataEventStreamingsSinkSinkRabbitMQParametersExchange()
            self.exchange = temp_model.from_map(m['Exchange'])
        if m.get('InstanceId') is not None:
            temp_model = ListEventStreamingResponseBodyDataEventStreamingsSinkSinkRabbitMQParametersInstanceId()
            self.instance_id = temp_model.from_map(m['InstanceId'])
        if m.get('MessageId') is not None:
            temp_model = ListEventStreamingResponseBodyDataEventStreamingsSinkSinkRabbitMQParametersMessageId()
            self.message_id = temp_model.from_map(m['MessageId'])
        if m.get('Properties') is not None:
            temp_model = ListEventStreamingResponseBodyDataEventStreamingsSinkSinkRabbitMQParametersProperties()
            self.properties = temp_model.from_map(m['Properties'])
        if m.get('QueueName') is not None:
            temp_model = ListEventStreamingResponseBodyDataEventStreamingsSinkSinkRabbitMQParametersQueueName()
            self.queue_name = temp_model.from_map(m['QueueName'])
        if m.get('RoutingKey') is not None:
            temp_model = ListEventStreamingResponseBodyDataEventStreamingsSinkSinkRabbitMQParametersRoutingKey()
            self.routing_key = temp_model.from_map(m['RoutingKey'])
        if m.get('TargetType') is not None:
            temp_model = ListEventStreamingResponseBodyDataEventStreamingsSinkSinkRabbitMQParametersTargetType()
            self.target_type = temp_model.from_map(m['TargetType'])
        if m.get('VirtualHostName') is not None:
            temp_model = ListEventStreamingResponseBodyDataEventStreamingsSinkSinkRabbitMQParametersVirtualHostName()
            self.virtual_host_name = temp_model.from_map(m['VirtualHostName'])
        return self


class ListEventStreamingResponseBodyDataEventStreamingsSinkSinkRocketMQParametersBody(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListEventStreamingResponseBodyDataEventStreamingsSinkSinkRocketMQParametersInstanceId(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListEventStreamingResponseBodyDataEventStreamingsSinkSinkRocketMQParametersKeys(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListEventStreamingResponseBodyDataEventStreamingsSinkSinkRocketMQParametersProperties(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListEventStreamingResponseBodyDataEventStreamingsSinkSinkRocketMQParametersTags(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListEventStreamingResponseBodyDataEventStreamingsSinkSinkRocketMQParametersTopic(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListEventStreamingResponseBodyDataEventStreamingsSinkSinkRocketMQParameters(TeaModel):
    def __init__(
        self,
        body: ListEventStreamingResponseBodyDataEventStreamingsSinkSinkRocketMQParametersBody = None,
        instance_id: ListEventStreamingResponseBodyDataEventStreamingsSinkSinkRocketMQParametersInstanceId = None,
        keys: ListEventStreamingResponseBodyDataEventStreamingsSinkSinkRocketMQParametersKeys = None,
        properties: ListEventStreamingResponseBodyDataEventStreamingsSinkSinkRocketMQParametersProperties = None,
        tags: ListEventStreamingResponseBodyDataEventStreamingsSinkSinkRocketMQParametersTags = None,
        topic: ListEventStreamingResponseBodyDataEventStreamingsSinkSinkRocketMQParametersTopic = None,
    ):
        self.body = body
        self.instance_id = instance_id
        self.keys = keys
        self.properties = properties
        self.tags = tags
        self.topic = topic

    def validate(self):
        if self.body:
            self.body.validate()
        if self.instance_id:
            self.instance_id.validate()
        if self.keys:
            self.keys.validate()
        if self.properties:
            self.properties.validate()
        if self.tags:
            self.tags.validate()
        if self.topic:
            self.topic.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['Body'] = self.body.to_map()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id.to_map()
        if self.keys is not None:
            result['Keys'] = self.keys.to_map()
        if self.properties is not None:
            result['Properties'] = self.properties.to_map()
        if self.tags is not None:
            result['Tags'] = self.tags.to_map()
        if self.topic is not None:
            result['Topic'] = self.topic.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Body') is not None:
            temp_model = ListEventStreamingResponseBodyDataEventStreamingsSinkSinkRocketMQParametersBody()
            self.body = temp_model.from_map(m['Body'])
        if m.get('InstanceId') is not None:
            temp_model = ListEventStreamingResponseBodyDataEventStreamingsSinkSinkRocketMQParametersInstanceId()
            self.instance_id = temp_model.from_map(m['InstanceId'])
        if m.get('Keys') is not None:
            temp_model = ListEventStreamingResponseBodyDataEventStreamingsSinkSinkRocketMQParametersKeys()
            self.keys = temp_model.from_map(m['Keys'])
        if m.get('Properties') is not None:
            temp_model = ListEventStreamingResponseBodyDataEventStreamingsSinkSinkRocketMQParametersProperties()
            self.properties = temp_model.from_map(m['Properties'])
        if m.get('Tags') is not None:
            temp_model = ListEventStreamingResponseBodyDataEventStreamingsSinkSinkRocketMQParametersTags()
            self.tags = temp_model.from_map(m['Tags'])
        if m.get('Topic') is not None:
            temp_model = ListEventStreamingResponseBodyDataEventStreamingsSinkSinkRocketMQParametersTopic()
            self.topic = temp_model.from_map(m['Topic'])
        return self


class ListEventStreamingResponseBodyDataEventStreamingsSinkSinkSLSParametersBody(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListEventStreamingResponseBodyDataEventStreamingsSinkSinkSLSParametersLogStore(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListEventStreamingResponseBodyDataEventStreamingsSinkSinkSLSParametersProject(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListEventStreamingResponseBodyDataEventStreamingsSinkSinkSLSParametersRoleName(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListEventStreamingResponseBodyDataEventStreamingsSinkSinkSLSParametersTopic(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListEventStreamingResponseBodyDataEventStreamingsSinkSinkSLSParameters(TeaModel):
    def __init__(
        self,
        body: ListEventStreamingResponseBodyDataEventStreamingsSinkSinkSLSParametersBody = None,
        log_store: ListEventStreamingResponseBodyDataEventStreamingsSinkSinkSLSParametersLogStore = None,
        project: ListEventStreamingResponseBodyDataEventStreamingsSinkSinkSLSParametersProject = None,
        role_name: ListEventStreamingResponseBodyDataEventStreamingsSinkSinkSLSParametersRoleName = None,
        topic: ListEventStreamingResponseBodyDataEventStreamingsSinkSinkSLSParametersTopic = None,
    ):
        self.body = body
        self.log_store = log_store
        self.project = project
        self.role_name = role_name
        self.topic = topic

    def validate(self):
        if self.body:
            self.body.validate()
        if self.log_store:
            self.log_store.validate()
        if self.project:
            self.project.validate()
        if self.role_name:
            self.role_name.validate()
        if self.topic:
            self.topic.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['Body'] = self.body.to_map()
        if self.log_store is not None:
            result['LogStore'] = self.log_store.to_map()
        if self.project is not None:
            result['Project'] = self.project.to_map()
        if self.role_name is not None:
            result['RoleName'] = self.role_name.to_map()
        if self.topic is not None:
            result['Topic'] = self.topic.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Body') is not None:
            temp_model = ListEventStreamingResponseBodyDataEventStreamingsSinkSinkSLSParametersBody()
            self.body = temp_model.from_map(m['Body'])
        if m.get('LogStore') is not None:
            temp_model = ListEventStreamingResponseBodyDataEventStreamingsSinkSinkSLSParametersLogStore()
            self.log_store = temp_model.from_map(m['LogStore'])
        if m.get('Project') is not None:
            temp_model = ListEventStreamingResponseBodyDataEventStreamingsSinkSinkSLSParametersProject()
            self.project = temp_model.from_map(m['Project'])
        if m.get('RoleName') is not None:
            temp_model = ListEventStreamingResponseBodyDataEventStreamingsSinkSinkSLSParametersRoleName()
            self.role_name = temp_model.from_map(m['RoleName'])
        if m.get('Topic') is not None:
            temp_model = ListEventStreamingResponseBodyDataEventStreamingsSinkSinkSLSParametersTopic()
            self.topic = temp_model.from_map(m['Topic'])
        return self


class ListEventStreamingResponseBodyDataEventStreamingsSink(TeaModel):
    def __init__(
        self,
        sink_fc_parameters: ListEventStreamingResponseBodyDataEventStreamingsSinkSinkFcParameters = None,
        sink_kafka_parameters: ListEventStreamingResponseBodyDataEventStreamingsSinkSinkKafkaParameters = None,
        sink_mnsparameters: ListEventStreamingResponseBodyDataEventStreamingsSinkSinkMNSParameters = None,
        sink_rabbit_mqparameters: ListEventStreamingResponseBodyDataEventStreamingsSinkSinkRabbitMQParameters = None,
        sink_rocket_mqparameters: ListEventStreamingResponseBodyDataEventStreamingsSinkSinkRocketMQParameters = None,
        sink_slsparameters: ListEventStreamingResponseBodyDataEventStreamingsSinkSinkSLSParameters = None,
    ):
        self.sink_fc_parameters = sink_fc_parameters
        self.sink_kafka_parameters = sink_kafka_parameters
        self.sink_mnsparameters = sink_mnsparameters
        self.sink_rabbit_mqparameters = sink_rabbit_mqparameters
        self.sink_rocket_mqparameters = sink_rocket_mqparameters
        self.sink_slsparameters = sink_slsparameters

    def validate(self):
        if self.sink_fc_parameters:
            self.sink_fc_parameters.validate()
        if self.sink_kafka_parameters:
            self.sink_kafka_parameters.validate()
        if self.sink_mnsparameters:
            self.sink_mnsparameters.validate()
        if self.sink_rabbit_mqparameters:
            self.sink_rabbit_mqparameters.validate()
        if self.sink_rocket_mqparameters:
            self.sink_rocket_mqparameters.validate()
        if self.sink_slsparameters:
            self.sink_slsparameters.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sink_fc_parameters is not None:
            result['SinkFcParameters'] = self.sink_fc_parameters.to_map()
        if self.sink_kafka_parameters is not None:
            result['SinkKafkaParameters'] = self.sink_kafka_parameters.to_map()
        if self.sink_mnsparameters is not None:
            result['SinkMNSParameters'] = self.sink_mnsparameters.to_map()
        if self.sink_rabbit_mqparameters is not None:
            result['SinkRabbitMQParameters'] = self.sink_rabbit_mqparameters.to_map()
        if self.sink_rocket_mqparameters is not None:
            result['SinkRocketMQParameters'] = self.sink_rocket_mqparameters.to_map()
        if self.sink_slsparameters is not None:
            result['SinkSLSParameters'] = self.sink_slsparameters.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SinkFcParameters') is not None:
            temp_model = ListEventStreamingResponseBodyDataEventStreamingsSinkSinkFcParameters()
            self.sink_fc_parameters = temp_model.from_map(m['SinkFcParameters'])
        if m.get('SinkKafkaParameters') is not None:
            temp_model = ListEventStreamingResponseBodyDataEventStreamingsSinkSinkKafkaParameters()
            self.sink_kafka_parameters = temp_model.from_map(m['SinkKafkaParameters'])
        if m.get('SinkMNSParameters') is not None:
            temp_model = ListEventStreamingResponseBodyDataEventStreamingsSinkSinkMNSParameters()
            self.sink_mnsparameters = temp_model.from_map(m['SinkMNSParameters'])
        if m.get('SinkRabbitMQParameters') is not None:
            temp_model = ListEventStreamingResponseBodyDataEventStreamingsSinkSinkRabbitMQParameters()
            self.sink_rabbit_mqparameters = temp_model.from_map(m['SinkRabbitMQParameters'])
        if m.get('SinkRocketMQParameters') is not None:
            temp_model = ListEventStreamingResponseBodyDataEventStreamingsSinkSinkRocketMQParameters()
            self.sink_rocket_mqparameters = temp_model.from_map(m['SinkRocketMQParameters'])
        if m.get('SinkSLSParameters') is not None:
            temp_model = ListEventStreamingResponseBodyDataEventStreamingsSinkSinkSLSParameters()
            self.sink_slsparameters = temp_model.from_map(m['SinkSLSParameters'])
        return self


class ListEventStreamingResponseBodyDataEventStreamingsSourceSourceDTSParameters(TeaModel):
    def __init__(
        self,
        broker_url: str = None,
        init_check_point: str = None,
        password: str = None,
        sid: str = None,
        task_id: str = None,
        topic: str = None,
        username: str = None,
    ):
        self.broker_url = broker_url
        self.init_check_point = init_check_point
        self.password = password
        self.sid = sid
        self.task_id = task_id
        self.topic = topic
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.broker_url is not None:
            result['BrokerUrl'] = self.broker_url
        if self.init_check_point is not None:
            result['InitCheckPoint'] = self.init_check_point
        if self.password is not None:
            result['Password'] = self.password
        if self.sid is not None:
            result['Sid'] = self.sid
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.topic is not None:
            result['Topic'] = self.topic
        if self.username is not None:
            result['Username'] = self.username
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BrokerUrl') is not None:
            self.broker_url = m.get('BrokerUrl')
        if m.get('InitCheckPoint') is not None:
            self.init_check_point = m.get('InitCheckPoint')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('Sid') is not None:
            self.sid = m.get('Sid')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        return self


class ListEventStreamingResponseBodyDataEventStreamingsSourceSourceKafkaParameters(TeaModel):
    def __init__(
        self,
        consumer_group: str = None,
        instance_id: str = None,
        network: str = None,
        offset_reset: str = None,
        region_id: str = None,
        security_group_id: str = None,
        topic: str = None,
        v_switch_ids: str = None,
        vpc_id: str = None,
    ):
        self.consumer_group = consumer_group
        self.instance_id = instance_id
        self.network = network
        self.offset_reset = offset_reset
        self.region_id = region_id
        self.security_group_id = security_group_id
        self.topic = topic
        self.v_switch_ids = v_switch_ids
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consumer_group is not None:
            result['ConsumerGroup'] = self.consumer_group
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.network is not None:
            result['Network'] = self.network
        if self.offset_reset is not None:
            result['OffsetReset'] = self.offset_reset
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.topic is not None:
            result['Topic'] = self.topic
        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsumerGroup') is not None:
            self.consumer_group = m.get('ConsumerGroup')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Network') is not None:
            self.network = m.get('Network')
        if m.get('OffsetReset') is not None:
            self.offset_reset = m.get('OffsetReset')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class ListEventStreamingResponseBodyDataEventStreamingsSourceSourceMNSParameters(TeaModel):
    def __init__(
        self,
        is_base_64decode: bool = None,
        queue_name: str = None,
        region_id: str = None,
    ):
        self.is_base_64decode = is_base_64decode
        self.queue_name = queue_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_base_64decode is not None:
            result['IsBase64Decode'] = self.is_base_64decode
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsBase64Decode') is not None:
            self.is_base_64decode = m.get('IsBase64Decode')
        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListEventStreamingResponseBodyDataEventStreamingsSourceSourceMQTTParameters(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        region_id: str = None,
        topic: str = None,
    ):
        self.instance_id = instance_id
        self.region_id = region_id
        self.topic = topic

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.topic is not None:
            result['Topic'] = self.topic
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        return self


class ListEventStreamingResponseBodyDataEventStreamingsSourceSourceRabbitMQParameters(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        queue_name: str = None,
        region_id: str = None,
        virtual_host_name: str = None,
    ):
        self.instance_id = instance_id
        self.queue_name = queue_name
        self.region_id = region_id
        self.virtual_host_name = virtual_host_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.virtual_host_name is not None:
            result['VirtualHostName'] = self.virtual_host_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VirtualHostName') is not None:
            self.virtual_host_name = m.get('VirtualHostName')
        return self


class ListEventStreamingResponseBodyDataEventStreamingsSourceSourceRocketMQParameters(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        instance_id: str = None,
        offset: str = None,
        region_id: str = None,
        tag: str = None,
        timestamp: int = None,
        topic: str = None,
    ):
        self.group_id = group_id
        self.instance_id = instance_id
        self.offset = offset
        self.region_id = region_id
        self.tag = tag
        self.timestamp = timestamp
        self.topic = topic

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupID'] = self.group_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.offset is not None:
            result['Offset'] = self.offset
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.topic is not None:
            result['Topic'] = self.topic
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupID') is not None:
            self.group_id = m.get('GroupID')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Offset') is not None:
            self.offset = m.get('Offset')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        return self


class ListEventStreamingResponseBodyDataEventStreamingsSourceSourceSLSParameters(TeaModel):
    def __init__(
        self,
        consume_position: str = None,
        consumer_group: str = None,
        log_store: str = None,
        project: str = None,
        role_name: str = None,
    ):
        self.consume_position = consume_position
        self.consumer_group = consumer_group
        self.log_store = log_store
        self.project = project
        self.role_name = role_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consume_position is not None:
            result['ConsumePosition'] = self.consume_position
        if self.consumer_group is not None:
            result['ConsumerGroup'] = self.consumer_group
        if self.log_store is not None:
            result['LogStore'] = self.log_store
        if self.project is not None:
            result['Project'] = self.project
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsumePosition') is not None:
            self.consume_position = m.get('ConsumePosition')
        if m.get('ConsumerGroup') is not None:
            self.consumer_group = m.get('ConsumerGroup')
        if m.get('LogStore') is not None:
            self.log_store = m.get('LogStore')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        return self


class ListEventStreamingResponseBodyDataEventStreamingsSource(TeaModel):
    def __init__(
        self,
        source_dtsparameters: ListEventStreamingResponseBodyDataEventStreamingsSourceSourceDTSParameters = None,
        source_kafka_parameters: ListEventStreamingResponseBodyDataEventStreamingsSourceSourceKafkaParameters = None,
        source_mnsparameters: ListEventStreamingResponseBodyDataEventStreamingsSourceSourceMNSParameters = None,
        source_mqttparameters: ListEventStreamingResponseBodyDataEventStreamingsSourceSourceMQTTParameters = None,
        source_rabbit_mqparameters: ListEventStreamingResponseBodyDataEventStreamingsSourceSourceRabbitMQParameters = None,
        source_rocket_mqparameters: ListEventStreamingResponseBodyDataEventStreamingsSourceSourceRocketMQParameters = None,
        source_slsparameters: ListEventStreamingResponseBodyDataEventStreamingsSourceSourceSLSParameters = None,
    ):
        self.source_dtsparameters = source_dtsparameters
        self.source_kafka_parameters = source_kafka_parameters
        self.source_mnsparameters = source_mnsparameters
        self.source_mqttparameters = source_mqttparameters
        self.source_rabbit_mqparameters = source_rabbit_mqparameters
        self.source_rocket_mqparameters = source_rocket_mqparameters
        self.source_slsparameters = source_slsparameters

    def validate(self):
        if self.source_dtsparameters:
            self.source_dtsparameters.validate()
        if self.source_kafka_parameters:
            self.source_kafka_parameters.validate()
        if self.source_mnsparameters:
            self.source_mnsparameters.validate()
        if self.source_mqttparameters:
            self.source_mqttparameters.validate()
        if self.source_rabbit_mqparameters:
            self.source_rabbit_mqparameters.validate()
        if self.source_rocket_mqparameters:
            self.source_rocket_mqparameters.validate()
        if self.source_slsparameters:
            self.source_slsparameters.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_dtsparameters is not None:
            result['SourceDTSParameters'] = self.source_dtsparameters.to_map()
        if self.source_kafka_parameters is not None:
            result['SourceKafkaParameters'] = self.source_kafka_parameters.to_map()
        if self.source_mnsparameters is not None:
            result['SourceMNSParameters'] = self.source_mnsparameters.to_map()
        if self.source_mqttparameters is not None:
            result['SourceMQTTParameters'] = self.source_mqttparameters.to_map()
        if self.source_rabbit_mqparameters is not None:
            result['SourceRabbitMQParameters'] = self.source_rabbit_mqparameters.to_map()
        if self.source_rocket_mqparameters is not None:
            result['SourceRocketMQParameters'] = self.source_rocket_mqparameters.to_map()
        if self.source_slsparameters is not None:
            result['SourceSLSParameters'] = self.source_slsparameters.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceDTSParameters') is not None:
            temp_model = ListEventStreamingResponseBodyDataEventStreamingsSourceSourceDTSParameters()
            self.source_dtsparameters = temp_model.from_map(m['SourceDTSParameters'])
        if m.get('SourceKafkaParameters') is not None:
            temp_model = ListEventStreamingResponseBodyDataEventStreamingsSourceSourceKafkaParameters()
            self.source_kafka_parameters = temp_model.from_map(m['SourceKafkaParameters'])
        if m.get('SourceMNSParameters') is not None:
            temp_model = ListEventStreamingResponseBodyDataEventStreamingsSourceSourceMNSParameters()
            self.source_mnsparameters = temp_model.from_map(m['SourceMNSParameters'])
        if m.get('SourceMQTTParameters') is not None:
            temp_model = ListEventStreamingResponseBodyDataEventStreamingsSourceSourceMQTTParameters()
            self.source_mqttparameters = temp_model.from_map(m['SourceMQTTParameters'])
        if m.get('SourceRabbitMQParameters') is not None:
            temp_model = ListEventStreamingResponseBodyDataEventStreamingsSourceSourceRabbitMQParameters()
            self.source_rabbit_mqparameters = temp_model.from_map(m['SourceRabbitMQParameters'])
        if m.get('SourceRocketMQParameters') is not None:
            temp_model = ListEventStreamingResponseBodyDataEventStreamingsSourceSourceRocketMQParameters()
            self.source_rocket_mqparameters = temp_model.from_map(m['SourceRocketMQParameters'])
        if m.get('SourceSLSParameters') is not None:
            temp_model = ListEventStreamingResponseBodyDataEventStreamingsSourceSourceSLSParameters()
            self.source_slsparameters = temp_model.from_map(m['SourceSLSParameters'])
        return self


class ListEventStreamingResponseBodyDataEventStreamings(TeaModel):
    def __init__(
        self,
        description: str = None,
        event_streaming_name: str = None,
        filter_pattern: str = None,
        run_options: ListEventStreamingResponseBodyDataEventStreamingsRunOptions = None,
        sink: ListEventStreamingResponseBodyDataEventStreamingsSink = None,
        source: ListEventStreamingResponseBodyDataEventStreamingsSource = None,
        status: str = None,
        tag: str = None,
    ):
        self.description = description
        self.event_streaming_name = event_streaming_name
        self.filter_pattern = filter_pattern
        self.run_options = run_options
        self.sink = sink
        self.source = source
        self.status = status
        self.tag = tag

    def validate(self):
        if self.run_options:
            self.run_options.validate()
        if self.sink:
            self.sink.validate()
        if self.source:
            self.source.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.event_streaming_name is not None:
            result['EventStreamingName'] = self.event_streaming_name
        if self.filter_pattern is not None:
            result['FilterPattern'] = self.filter_pattern
        if self.run_options is not None:
            result['RunOptions'] = self.run_options.to_map()
        if self.sink is not None:
            result['Sink'] = self.sink.to_map()
        if self.source is not None:
            result['Source'] = self.source.to_map()
        if self.status is not None:
            result['Status'] = self.status
        if self.tag is not None:
            result['Tag'] = self.tag
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EventStreamingName') is not None:
            self.event_streaming_name = m.get('EventStreamingName')
        if m.get('FilterPattern') is not None:
            self.filter_pattern = m.get('FilterPattern')
        if m.get('RunOptions') is not None:
            temp_model = ListEventStreamingResponseBodyDataEventStreamingsRunOptions()
            self.run_options = temp_model.from_map(m['RunOptions'])
        if m.get('Sink') is not None:
            temp_model = ListEventStreamingResponseBodyDataEventStreamingsSink()
            self.sink = temp_model.from_map(m['Sink'])
        if m.get('Source') is not None:
            temp_model = ListEventStreamingResponseBodyDataEventStreamingsSource()
            self.source = temp_model.from_map(m['Source'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        return self


class ListEventStreamingResponseBodyData(TeaModel):
    def __init__(
        self,
        event_streamings: List[ListEventStreamingResponseBodyDataEventStreamings] = None,
        next_token: str = None,
        total: int = None,
    ):
        self.event_streamings = event_streamings
        self.next_token = next_token
        self.total = total

    def validate(self):
        if self.event_streamings:
            for k in self.event_streamings:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['EventStreamings'] = []
        if self.event_streamings is not None:
            for k in self.event_streamings:
                result['EventStreamings'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.event_streamings = []
        if m.get('EventStreamings') is not None:
            for k in m.get('EventStreamings'):
                temp_model = ListEventStreamingResponseBodyDataEventStreamings()
                self.event_streamings.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListEventStreamingResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListEventStreamingResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ListEventStreamingResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListEventStreamingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListEventStreamingResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ListEventStreamingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEventStreamingMetricsRequest(TeaModel):
    def __init__(
        self,
        names: List[str] = None,
    ):
        self.names = names

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.names is not None:
            result['Names'] = self.names
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Names') is not None:
            self.names = m.get('Names')
        return self


class ListEventStreamingMetricsResponseBodyData(TeaModel):
    def __init__(
        self,
        delay_time: float = None,
        diff_offset: float = None,
        last_sync_time: float = None,
        name: str = None,
        status: str = None,
        tps: float = None,
    ):
        self.delay_time = delay_time
        self.diff_offset = diff_offset
        self.last_sync_time = last_sync_time
        self.name = name
        self.status = status
        self.tps = tps

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delay_time is not None:
            result['DelayTime'] = self.delay_time
        if self.diff_offset is not None:
            result['DiffOffset'] = self.diff_offset
        if self.last_sync_time is not None:
            result['LastSyncTime'] = self.last_sync_time
        if self.name is not None:
            result['Name'] = self.name
        if self.status is not None:
            result['Status'] = self.status
        if self.tps is not None:
            result['TPS'] = self.tps
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DelayTime') is not None:
            self.delay_time = m.get('DelayTime')
        if m.get('DiffOffset') is not None:
            self.diff_offset = m.get('DiffOffset')
        if m.get('LastSyncTime') is not None:
            self.last_sync_time = m.get('LastSyncTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TPS') is not None:
            self.tps = m.get('TPS')
        return self


class ListEventStreamingMetricsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[ListEventStreamingMetricsResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListEventStreamingMetricsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListEventStreamingMetricsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListEventStreamingMetricsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ListEventStreamingMetricsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRulesRequest(TeaModel):
    def __init__(
        self,
        event_bus_name: str = None,
        limit: int = None,
        next_token: str = None,
        rule_name_prefix: str = None,
    ):
        self.event_bus_name = event_bus_name
        self.limit = limit
        self.next_token = next_token
        self.rule_name_prefix = rule_name_prefix

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.rule_name_prefix is not None:
            result['RuleNamePrefix'] = self.rule_name_prefix
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RuleNamePrefix') is not None:
            self.rule_name_prefix = m.get('RuleNamePrefix')
        return self


class ListRulesResponseBodyDataRulesTargets(TeaModel):
    def __init__(
        self,
        endpoint: str = None,
        id: str = None,
        push_selector: str = None,
        type: str = None,
    ):
        self.endpoint = endpoint
        self.id = id
        self.push_selector = push_selector
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.id is not None:
            result['Id'] = self.id
        if self.push_selector is not None:
            result['PushSelector'] = self.push_selector
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('PushSelector') is not None:
            self.push_selector = m.get('PushSelector')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListRulesResponseBodyDataRules(TeaModel):
    def __init__(
        self,
        created_timestamp: int = None,
        description: str = None,
        detail_map: Dict[str, Any] = None,
        event_bus_name: str = None,
        filter_pattern: str = None,
        rule_arn: str = None,
        rule_name: str = None,
        status: str = None,
        targets: List[ListRulesResponseBodyDataRulesTargets] = None,
    ):
        self.created_timestamp = created_timestamp
        self.description = description
        self.detail_map = detail_map
        self.event_bus_name = event_bus_name
        self.filter_pattern = filter_pattern
        self.rule_arn = rule_arn
        self.rule_name = rule_name
        self.status = status
        self.targets = targets

    def validate(self):
        if self.targets:
            for k in self.targets:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_timestamp is not None:
            result['CreatedTimestamp'] = self.created_timestamp
        if self.description is not None:
            result['Description'] = self.description
        if self.detail_map is not None:
            result['DetailMap'] = self.detail_map
        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name
        if self.filter_pattern is not None:
            result['FilterPattern'] = self.filter_pattern
        if self.rule_arn is not None:
            result['RuleARN'] = self.rule_arn
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.status is not None:
            result['Status'] = self.status
        result['Targets'] = []
        if self.targets is not None:
            for k in self.targets:
                result['Targets'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedTimestamp') is not None:
            self.created_timestamp = m.get('CreatedTimestamp')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DetailMap') is not None:
            self.detail_map = m.get('DetailMap')
        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')
        if m.get('FilterPattern') is not None:
            self.filter_pattern = m.get('FilterPattern')
        if m.get('RuleARN') is not None:
            self.rule_arn = m.get('RuleARN')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.targets = []
        if m.get('Targets') is not None:
            for k in m.get('Targets'):
                temp_model = ListRulesResponseBodyDataRulesTargets()
                self.targets.append(temp_model.from_map(k))
        return self


class ListRulesResponseBodyData(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        rules: List[ListRulesResponseBodyDataRules] = None,
        total: int = None,
    ):
        self.next_token = next_token
        self.rules = rules
        self.total = total

    def validate(self):
        if self.rules:
            for k in self.rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['Rules'] = []
        if self.rules is not None:
            for k in self.rules:
                result['Rules'].append(k.to_map() if k else None)
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.rules = []
        if m.get('Rules') is not None:
            for k in m.get('Rules'):
                temp_model = ListRulesResponseBodyDataRules()
                self.rules.append(temp_model.from_map(k))
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListRulesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListRulesResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ListRulesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListRulesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ListRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSchemaGroupsRequest(TeaModel):
    def __init__(
        self,
        limit: int = None,
        next_token: str = None,
        prefix: str = None,
    ):
        self.limit = limit
        self.next_token = next_token
        self.prefix = prefix

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.prefix is not None:
            result['Prefix'] = self.prefix
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Prefix') is not None:
            self.prefix = m.get('Prefix')
        return self


class ListSchemaGroupsResponseBodyDataGroups(TeaModel):
    def __init__(
        self,
        created_timestamp: int = None,
        description: str = None,
        format: str = None,
        group_arn: str = None,
        group_id: str = None,
        updated_timestamp: int = None,
    ):
        self.created_timestamp = created_timestamp
        self.description = description
        self.format = format
        self.group_arn = group_arn
        self.group_id = group_id
        self.updated_timestamp = updated_timestamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_timestamp is not None:
            result['CreatedTimestamp'] = self.created_timestamp
        if self.description is not None:
            result['Description'] = self.description
        if self.format is not None:
            result['Format'] = self.format
        if self.group_arn is not None:
            result['GroupARN'] = self.group_arn
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.updated_timestamp is not None:
            result['UpdatedTimestamp'] = self.updated_timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedTimestamp') is not None:
            self.created_timestamp = m.get('CreatedTimestamp')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Format') is not None:
            self.format = m.get('Format')
        if m.get('GroupARN') is not None:
            self.group_arn = m.get('GroupARN')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('UpdatedTimestamp') is not None:
            self.updated_timestamp = m.get('UpdatedTimestamp')
        return self


class ListSchemaGroupsResponseBodyData(TeaModel):
    def __init__(
        self,
        groups: List[ListSchemaGroupsResponseBodyDataGroups] = None,
        next_token: str = None,
        total: int = None,
    ):
        self.groups = groups
        self.next_token = next_token
        self.total = total

    def validate(self):
        if self.groups:
            for k in self.groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Groups'] = []
        if self.groups is not None:
            for k in self.groups:
                result['Groups'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.groups = []
        if m.get('Groups') is not None:
            for k in m.get('Groups'):
                temp_model = ListSchemaGroupsResponseBodyDataGroups()
                self.groups.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListSchemaGroupsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListSchemaGroupsResponseBodyData = None,
        http_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_code = http_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ListSchemaGroupsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListSchemaGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListSchemaGroupsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ListSchemaGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSchemaVersionsRequest(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        limit: int = None,
        next_token: str = None,
        schema_id: str = None,
    ):
        self.group_id = group_id
        self.limit = limit
        self.next_token = next_token
        self.schema_id = schema_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.schema_id is not None:
            result['SchemaId'] = self.schema_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('SchemaId') is not None:
            self.schema_id = m.get('SchemaId')
        return self


class ListSchemaVersionsResponseBodyDataVersions(TeaModel):
    def __init__(
        self,
        content: str = None,
        created_timestamp: int = None,
        format: str = None,
        group_id: str = None,
        schema_id: str = None,
        schema_version_arn: str = None,
        updated_timestamp: int = None,
        version: int = None,
    ):
        self.content = content
        self.created_timestamp = created_timestamp
        self.format = format
        self.group_id = group_id
        self.schema_id = schema_id
        self.schema_version_arn = schema_version_arn
        self.updated_timestamp = updated_timestamp
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.created_timestamp is not None:
            result['CreatedTimestamp'] = self.created_timestamp
        if self.format is not None:
            result['Format'] = self.format
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.schema_id is not None:
            result['SchemaId'] = self.schema_id
        if self.schema_version_arn is not None:
            result['SchemaVersionARN'] = self.schema_version_arn
        if self.updated_timestamp is not None:
            result['UpdatedTimestamp'] = self.updated_timestamp
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('CreatedTimestamp') is not None:
            self.created_timestamp = m.get('CreatedTimestamp')
        if m.get('Format') is not None:
            self.format = m.get('Format')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('SchemaId') is not None:
            self.schema_id = m.get('SchemaId')
        if m.get('SchemaVersionARN') is not None:
            self.schema_version_arn = m.get('SchemaVersionARN')
        if m.get('UpdatedTimestamp') is not None:
            self.updated_timestamp = m.get('UpdatedTimestamp')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class ListSchemaVersionsResponseBodyData(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        total: int = None,
        versions: List[ListSchemaVersionsResponseBodyDataVersions] = None,
    ):
        self.next_token = next_token
        self.total = total
        self.versions = versions

    def validate(self):
        if self.versions:
            for k in self.versions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.total is not None:
            result['Total'] = self.total
        result['Versions'] = []
        if self.versions is not None:
            for k in self.versions:
                result['Versions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        self.versions = []
        if m.get('Versions') is not None:
            for k in m.get('Versions'):
                temp_model = ListSchemaVersionsResponseBodyDataVersions()
                self.versions.append(temp_model.from_map(k))
        return self


class ListSchemaVersionsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListSchemaVersionsResponseBodyData = None,
        http_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_code = http_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ListSchemaVersionsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListSchemaVersionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListSchemaVersionsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ListSchemaVersionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSchemasRequest(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        limit: int = None,
        next_token: str = None,
        prefix: str = None,
    ):
        self.group_id = group_id
        self.limit = limit
        self.next_token = next_token
        self.prefix = prefix

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.prefix is not None:
            result['Prefix'] = self.prefix
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Prefix') is not None:
            self.prefix = m.get('Prefix')
        return self


class ListSchemasResponseBodyDataSchemas(TeaModel):
    def __init__(
        self,
        compatible_type: str = None,
        created_timestamp: int = None,
        description: str = None,
        format: str = None,
        group_id: str = None,
        latest_version: int = None,
        schema_id: str = None,
        updated_timestamp: int = None,
    ):
        self.compatible_type = compatible_type
        self.created_timestamp = created_timestamp
        self.description = description
        self.format = format
        self.group_id = group_id
        self.latest_version = latest_version
        self.schema_id = schema_id
        self.updated_timestamp = updated_timestamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compatible_type is not None:
            result['CompatibleType'] = self.compatible_type
        if self.created_timestamp is not None:
            result['CreatedTimestamp'] = self.created_timestamp
        if self.description is not None:
            result['Description'] = self.description
        if self.format is not None:
            result['Format'] = self.format
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.latest_version is not None:
            result['LatestVersion'] = self.latest_version
        if self.schema_id is not None:
            result['SchemaId'] = self.schema_id
        if self.updated_timestamp is not None:
            result['UpdatedTimestamp'] = self.updated_timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompatibleType') is not None:
            self.compatible_type = m.get('CompatibleType')
        if m.get('CreatedTimestamp') is not None:
            self.created_timestamp = m.get('CreatedTimestamp')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Format') is not None:
            self.format = m.get('Format')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('LatestVersion') is not None:
            self.latest_version = m.get('LatestVersion')
        if m.get('SchemaId') is not None:
            self.schema_id = m.get('SchemaId')
        if m.get('UpdatedTimestamp') is not None:
            self.updated_timestamp = m.get('UpdatedTimestamp')
        return self


class ListSchemasResponseBodyData(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        schemas: List[ListSchemasResponseBodyDataSchemas] = None,
        total: int = None,
    ):
        self.next_token = next_token
        self.schemas = schemas
        self.total = total

    def validate(self):
        if self.schemas:
            for k in self.schemas:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['Schemas'] = []
        if self.schemas is not None:
            for k in self.schemas:
                result['Schemas'].append(k.to_map() if k else None)
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.schemas = []
        if m.get('Schemas') is not None:
            for k in m.get('Schemas'):
                temp_model = ListSchemasResponseBodyDataSchemas()
                self.schemas.append(temp_model.from_map(k))
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListSchemasResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListSchemasResponseBodyData = None,
        http_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_code = http_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ListSchemasResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListSchemasResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListSchemasResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ListSchemasResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSourceTaskResponseBodyData(TeaModel):
    def __init__(
        self,
        bus_name: str = None,
        id: str = None,
        last_date_sync_time: str = None,
        name: str = None,
        sended_records: int = None,
        source: str = None,
        status: str = None,
    ):
        self.bus_name = bus_name
        self.id = id
        self.last_date_sync_time = last_date_sync_time
        self.name = name
        self.sended_records = sended_records
        self.source = source
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bus_name is not None:
            result['BusName'] = self.bus_name
        if self.id is not None:
            result['Id'] = self.id
        if self.last_date_sync_time is not None:
            result['LastDateSyncTime'] = self.last_date_sync_time
        if self.name is not None:
            result['Name'] = self.name
        if self.sended_records is not None:
            result['SendedRecords'] = self.sended_records
        if self.source is not None:
            result['Source'] = self.source
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusName') is not None:
            self.bus_name = m.get('BusName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LastDateSyncTime') is not None:
            self.last_date_sync_time = m.get('LastDateSyncTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SendedRecords') is not None:
            self.sended_records = m.get('SendedRecords')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListSourceTaskResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[ListSourceTaskResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListSourceTaskResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListSourceTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListSourceTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ListSourceTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTargetTypesRequest(TeaModel):
    def __init__(
        self,
        limit: int = None,
        name_prefix: str = None,
        next_token: str = None,
    ):
        self.limit = limit
        self.name_prefix = name_prefix
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.name_prefix is not None:
            result['NamePrefix'] = self.name_prefix
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('NamePrefix') is not None:
            self.name_prefix = m.get('NamePrefix')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class ListTargetTypesResponseBodyDataResourceKeysDefaultValues(TeaModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        self.name = name
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListTargetTypesResponseBodyDataResourceKeysResourceGroupDefaultValues(TeaModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        self.name = name
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListTargetTypesResponseBodyDataResourceKeysResourceGroup(TeaModel):
    def __init__(
        self,
        default_values: List[ListTargetTypesResponseBodyDataResourceKeysResourceGroupDefaultValues] = None,
        dependent_resource_keys: List[str] = None,
        forms: List[str] = None,
        input_type: str = None,
        placeholder: str = None,
        resource_key: str = None,
        resource_name: str = None,
        show_if: str = None,
        tips: str = None,
    ):
        self.default_values = default_values
        self.dependent_resource_keys = dependent_resource_keys
        self.forms = forms
        self.input_type = input_type
        self.placeholder = placeholder
        self.resource_key = resource_key
        self.resource_name = resource_name
        self.show_if = show_if
        self.tips = tips

    def validate(self):
        if self.default_values:
            for k in self.default_values:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DefaultValues'] = []
        if self.default_values is not None:
            for k in self.default_values:
                result['DefaultValues'].append(k.to_map() if k else None)
        if self.dependent_resource_keys is not None:
            result['DependentResourceKeys'] = self.dependent_resource_keys
        if self.forms is not None:
            result['Forms'] = self.forms
        if self.input_type is not None:
            result['InputType'] = self.input_type
        if self.placeholder is not None:
            result['Placeholder'] = self.placeholder
        if self.resource_key is not None:
            result['ResourceKey'] = self.resource_key
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.show_if is not None:
            result['ShowIf'] = self.show_if
        if self.tips is not None:
            result['Tips'] = self.tips
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.default_values = []
        if m.get('DefaultValues') is not None:
            for k in m.get('DefaultValues'):
                temp_model = ListTargetTypesResponseBodyDataResourceKeysResourceGroupDefaultValues()
                self.default_values.append(temp_model.from_map(k))
        if m.get('DependentResourceKeys') is not None:
            self.dependent_resource_keys = m.get('DependentResourceKeys')
        if m.get('Forms') is not None:
            self.forms = m.get('Forms')
        if m.get('InputType') is not None:
            self.input_type = m.get('InputType')
        if m.get('Placeholder') is not None:
            self.placeholder = m.get('Placeholder')
        if m.get('ResourceKey') is not None:
            self.resource_key = m.get('ResourceKey')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('ShowIf') is not None:
            self.show_if = m.get('ShowIf')
        if m.get('Tips') is not None:
            self.tips = m.get('Tips')
        return self


class ListTargetTypesResponseBodyDataResourceKeys(TeaModel):
    def __init__(
        self,
        advanced_option: bool = None,
        default_values: List[ListTargetTypesResponseBodyDataResourceKeysDefaultValues] = None,
        dependent_resource_keys: List[str] = None,
        forms: List[str] = None,
        input_type: str = None,
        placeholder: str = None,
        resource_group: List[ListTargetTypesResponseBodyDataResourceKeysResourceGroup] = None,
        resource_key: str = None,
        resource_name: str = None,
        show_if: str = None,
        tips: str = None,
    ):
        self.advanced_option = advanced_option
        self.default_values = default_values
        self.dependent_resource_keys = dependent_resource_keys
        self.forms = forms
        self.input_type = input_type
        self.placeholder = placeholder
        self.resource_group = resource_group
        self.resource_key = resource_key
        self.resource_name = resource_name
        self.show_if = show_if
        self.tips = tips

    def validate(self):
        if self.default_values:
            for k in self.default_values:
                if k:
                    k.validate()
        if self.resource_group:
            for k in self.resource_group:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.advanced_option is not None:
            result['AdvancedOption'] = self.advanced_option
        result['DefaultValues'] = []
        if self.default_values is not None:
            for k in self.default_values:
                result['DefaultValues'].append(k.to_map() if k else None)
        if self.dependent_resource_keys is not None:
            result['DependentResourceKeys'] = self.dependent_resource_keys
        if self.forms is not None:
            result['Forms'] = self.forms
        if self.input_type is not None:
            result['InputType'] = self.input_type
        if self.placeholder is not None:
            result['Placeholder'] = self.placeholder
        result['ResourceGroup'] = []
        if self.resource_group is not None:
            for k in self.resource_group:
                result['ResourceGroup'].append(k.to_map() if k else None)
        if self.resource_key is not None:
            result['ResourceKey'] = self.resource_key
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.show_if is not None:
            result['ShowIf'] = self.show_if
        if self.tips is not None:
            result['Tips'] = self.tips
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdvancedOption') is not None:
            self.advanced_option = m.get('AdvancedOption')
        self.default_values = []
        if m.get('DefaultValues') is not None:
            for k in m.get('DefaultValues'):
                temp_model = ListTargetTypesResponseBodyDataResourceKeysDefaultValues()
                self.default_values.append(temp_model.from_map(k))
        if m.get('DependentResourceKeys') is not None:
            self.dependent_resource_keys = m.get('DependentResourceKeys')
        if m.get('Forms') is not None:
            self.forms = m.get('Forms')
        if m.get('InputType') is not None:
            self.input_type = m.get('InputType')
        if m.get('Placeholder') is not None:
            self.placeholder = m.get('Placeholder')
        self.resource_group = []
        if m.get('ResourceGroup') is not None:
            for k in m.get('ResourceGroup'):
                temp_model = ListTargetTypesResponseBodyDataResourceKeysResourceGroup()
                self.resource_group.append(temp_model.from_map(k))
        if m.get('ResourceKey') is not None:
            self.resource_key = m.get('ResourceKey')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('ShowIf') is not None:
            self.show_if = m.get('ShowIf')
        if m.get('Tips') is not None:
            self.tips = m.get('Tips')
        return self


class ListTargetTypesResponseBodyData(TeaModel):
    def __init__(
        self,
        acsname: str = None,
        arn: str = None,
        full_name: str = None,
        name: str = None,
        resource_keys: List[ListTargetTypesResponseBodyDataResourceKeys] = None,
    ):
        self.acsname = acsname
        self.arn = arn
        self.full_name = full_name
        self.name = name
        self.resource_keys = resource_keys

    def validate(self):
        if self.resource_keys:
            for k in self.resource_keys:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acsname is not None:
            result['ACSName'] = self.acsname
        if self.arn is not None:
            result['Arn'] = self.arn
        if self.full_name is not None:
            result['FullName'] = self.full_name
        if self.name is not None:
            result['Name'] = self.name
        result['ResourceKeys'] = []
        if self.resource_keys is not None:
            for k in self.resource_keys:
                result['ResourceKeys'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ACSName') is not None:
            self.acsname = m.get('ACSName')
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        if m.get('FullName') is not None:
            self.full_name = m.get('FullName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.resource_keys = []
        if m.get('ResourceKeys') is not None:
            for k in m.get('ResourceKeys'):
                temp_model = ListTargetTypesResponseBodyDataResourceKeys()
                self.resource_keys.append(temp_model.from_map(k))
        return self


class ListTargetTypesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[ListTargetTypesResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListTargetTypesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListTargetTypesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTargetTypesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ListTargetTypesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTargetsRequest(TeaModel):
    def __init__(
        self,
        event_bus_name: str = None,
        limit: int = None,
        rule_name: str = None,
    ):
        self.event_bus_name = event_bus_name
        self.limit = limit
        self.rule_name = rule_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        return self


class ListTargetsResponseBodyDataTargetsParamList(TeaModel):
    def __init__(
        self,
        form: str = None,
        resource_key: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.resource_key = resource_key
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.resource_key is not None:
            result['ResourceKey'] = self.resource_key
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('ResourceKey') is not None:
            self.resource_key = m.get('ResourceKey')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListTargetsResponseBodyDataTargets(TeaModel):
    def __init__(
        self,
        detail_map: Dict[str, Any] = None,
        endpoint: str = None,
        id: str = None,
        param_list: List[ListTargetsResponseBodyDataTargetsParamList] = None,
        push_selector: str = None,
        type: str = None,
    ):
        self.detail_map = detail_map
        self.endpoint = endpoint
        self.id = id
        self.param_list = param_list
        self.push_selector = push_selector
        self.type = type

    def validate(self):
        if self.param_list:
            for k in self.param_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.detail_map is not None:
            result['DetailMap'] = self.detail_map
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.id is not None:
            result['Id'] = self.id
        result['ParamList'] = []
        if self.param_list is not None:
            for k in self.param_list:
                result['ParamList'].append(k.to_map() if k else None)
        if self.push_selector is not None:
            result['PushSelector'] = self.push_selector
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DetailMap') is not None:
            self.detail_map = m.get('DetailMap')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        self.param_list = []
        if m.get('ParamList') is not None:
            for k in m.get('ParamList'):
                temp_model = ListTargetsResponseBodyDataTargetsParamList()
                self.param_list.append(temp_model.from_map(k))
        if m.get('PushSelector') is not None:
            self.push_selector = m.get('PushSelector')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListTargetsResponseBodyData(TeaModel):
    def __init__(
        self,
        targets: List[ListTargetsResponseBodyDataTargets] = None,
    ):
        self.targets = targets

    def validate(self):
        if self.targets:
            for k in self.targets:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Targets'] = []
        if self.targets is not None:
            for k in self.targets:
                result['Targets'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.targets = []
        if m.get('Targets') is not None:
            for k in m.get('Targets'):
                temp_model = ListTargetsResponseBodyDataTargets()
                self.targets.append(temp_model.from_map(k))
        return self


class ListTargetsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListTargetsResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ListTargetsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListTargetsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTargetsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ListTargetsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUserDefinedEventSourcesRequest(TeaModel):
    def __init__(
        self,
        limit: int = None,
        name_prefix: str = None,
        next_token: str = None,
        type: bytes = None,
    ):
        self.limit = limit
        self.name_prefix = name_prefix
        self.next_token = next_token
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.name_prefix is not None:
            result['NamePrefix'] = self.name_prefix
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('NamePrefix') is not None:
            self.name_prefix = m.get('NamePrefix')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListUserDefinedEventSourcesResponseBodyDataEventSourceList(TeaModel):
    def __init__(
        self,
        arn: str = None,
        ctime: float = None,
        description: str = None,
        event_bus_name: str = None,
        external_source_config: Dict[str, Any] = None,
        external_source_type: str = None,
        linked_external_source: bool = None,
        name: str = None,
        status: str = None,
        type: str = None,
    ):
        self.arn = arn
        self.ctime = ctime
        self.description = description
        self.event_bus_name = event_bus_name
        self.external_source_config = external_source_config
        self.external_source_type = external_source_type
        self.linked_external_source = linked_external_source
        self.name = name
        self.status = status
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arn is not None:
            result['Arn'] = self.arn
        if self.ctime is not None:
            result['Ctime'] = self.ctime
        if self.description is not None:
            result['Description'] = self.description
        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name
        if self.external_source_config is not None:
            result['ExternalSourceConfig'] = self.external_source_config
        if self.external_source_type is not None:
            result['ExternalSourceType'] = self.external_source_type
        if self.linked_external_source is not None:
            result['LinkedExternalSource'] = self.linked_external_source
        if self.name is not None:
            result['Name'] = self.name
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        if m.get('Ctime') is not None:
            self.ctime = m.get('Ctime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')
        if m.get('ExternalSourceConfig') is not None:
            self.external_source_config = m.get('ExternalSourceConfig')
        if m.get('ExternalSourceType') is not None:
            self.external_source_type = m.get('ExternalSourceType')
        if m.get('LinkedExternalSource') is not None:
            self.linked_external_source = m.get('LinkedExternalSource')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListUserDefinedEventSourcesResponseBodyData(TeaModel):
    def __init__(
        self,
        event_source_list: List[ListUserDefinedEventSourcesResponseBodyDataEventSourceList] = None,
        next_token: str = None,
        total: float = None,
    ):
        self.event_source_list = event_source_list
        self.next_token = next_token
        self.total = total

    def validate(self):
        if self.event_source_list:
            for k in self.event_source_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['EventSourceList'] = []
        if self.event_source_list is not None:
            for k in self.event_source_list:
                result['EventSourceList'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.event_source_list = []
        if m.get('EventSourceList') is not None:
            for k in m.get('EventSourceList'):
                temp_model = ListUserDefinedEventSourcesResponseBodyDataEventSourceList()
                self.event_source_list.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListUserDefinedEventSourcesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListUserDefinedEventSourcesResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ListUserDefinedEventSourcesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListUserDefinedEventSourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListUserDefinedEventSourcesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ListUserDefinedEventSourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PauseEventStreamingRequest(TeaModel):
    def __init__(
        self,
        event_streaming_name: str = None,
    ):
        self.event_streaming_name = event_streaming_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_streaming_name is not None:
            result['EventStreamingName'] = self.event_streaming_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventStreamingName') is not None:
            self.event_streaming_name = m.get('EventStreamingName')
        return self


class PauseEventStreamingResponseBody(TeaModel):
    def __init__(
        self,
        code: bool = None,
        data: bool = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class PauseEventStreamingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PauseEventStreamingResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = PauseEventStreamingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PayOrderCallbackRequest(TeaModel):
    def __init__(
        self,
        data: str = None,
    ):
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class PayOrderCallbackResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        synchro: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success
        self.synchro = synchro

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.synchro is not None:
            result['Synchro'] = self.synchro
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Synchro') is not None:
            self.synchro = m.get('Synchro')
        return self


class PayOrderCallbackResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PayOrderCallbackResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = PayOrderCallbackResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PutEventsRequest(TeaModel):
    def __init__(
        self,
        event_string: str = None,
    ):
        self.event_string = event_string

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_string is not None:
            result['EventString'] = self.event_string
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventString') is not None:
            self.event_string = m.get('EventString')
        return self


class PutEventsResponseBodyData(TeaModel):
    def __init__(
        self,
        event_id: str = None,
        trace_id: str = None,
    ):
        self.event_id = event_id
        self.trace_id = trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_id is not None:
            result['EventId'] = self.event_id
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class PutEventsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: PutEventsResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = PutEventsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class PutEventsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PutEventsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = PutEventsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryEventRequest(TeaModel):
    def __init__(
        self,
        event_bus_name: str = None,
        event_id: str = None,
        event_source: str = None,
    ):
        self.event_bus_name = event_bus_name
        self.event_id = event_id
        self.event_source = event_source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name
        if self.event_id is not None:
            result['EventId'] = self.event_id
        if self.event_source is not None:
            result['EventSource'] = self.event_source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        if m.get('EventSource') is not None:
            self.event_source = m.get('EventSource')
        return self


class QueryEventResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: Dict[str, Any] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryEventResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryEventResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = QueryEventResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryEventTracesRequest(TeaModel):
    def __init__(
        self,
        event_bus_name: str = None,
        event_id: str = None,
    ):
        self.event_bus_name = event_bus_name
        self.event_id = event_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name
        if self.event_id is not None:
            result['EventId'] = self.event_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        return self


class QueryEventTracesResponseBodyData(TeaModel):
    def __init__(
        self,
        action: str = None,
        action_time: int = None,
        endpoint: str = None,
        event_bus_name: str = None,
        event_id: str = None,
        event_source: str = None,
        notify_latency: str = None,
        notify_status: str = None,
        notify_time: int = None,
        received_time: int = None,
        rule_matching_time: str = None,
        rule_name: str = None,
    ):
        self.action = action
        self.action_time = action_time
        self.endpoint = endpoint
        self.event_bus_name = event_bus_name
        self.event_id = event_id
        self.event_source = event_source
        self.notify_latency = notify_latency
        self.notify_status = notify_status
        self.notify_time = notify_time
        self.received_time = received_time
        self.rule_matching_time = rule_matching_time
        self.rule_name = rule_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.action_time is not None:
            result['ActionTime'] = self.action_time
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name
        if self.event_id is not None:
            result['EventId'] = self.event_id
        if self.event_source is not None:
            result['EventSource'] = self.event_source
        if self.notify_latency is not None:
            result['NotifyLatency'] = self.notify_latency
        if self.notify_status is not None:
            result['NotifyStatus'] = self.notify_status
        if self.notify_time is not None:
            result['NotifyTime'] = self.notify_time
        if self.received_time is not None:
            result['ReceivedTime'] = self.received_time
        if self.rule_matching_time is not None:
            result['RuleMatchingTime'] = self.rule_matching_time
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('ActionTime') is not None:
            self.action_time = m.get('ActionTime')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        if m.get('EventSource') is not None:
            self.event_source = m.get('EventSource')
        if m.get('NotifyLatency') is not None:
            self.notify_latency = m.get('NotifyLatency')
        if m.get('NotifyStatus') is not None:
            self.notify_status = m.get('NotifyStatus')
        if m.get('NotifyTime') is not None:
            self.notify_time = m.get('NotifyTime')
        if m.get('ReceivedTime') is not None:
            self.received_time = m.get('ReceivedTime')
        if m.get('RuleMatchingTime') is not None:
            self.rule_matching_time = m.get('RuleMatchingTime')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        return self


class QueryEventTracesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[QueryEventTracesResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = QueryEventTracesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryEventTracesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryEventTracesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = QueryEventTracesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTracedEventByEventIdRequest(TeaModel):
    def __init__(
        self,
        event_bus_name: str = None,
        event_id: str = None,
        event_source: str = None,
    ):
        self.event_bus_name = event_bus_name
        self.event_id = event_id
        self.event_source = event_source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name
        if self.event_id is not None:
            result['EventId'] = self.event_id
        if self.event_source is not None:
            result['EventSource'] = self.event_source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        if m.get('EventSource') is not None:
            self.event_source = m.get('EventSource')
        return self


class QueryTracedEventByEventIdResponseBodyDataEvents(TeaModel):
    def __init__(
        self,
        event_bus_name: str = None,
        event_id: str = None,
        event_received_time: int = None,
        event_source: str = None,
        event_type: str = None,
    ):
        self.event_bus_name = event_bus_name
        self.event_id = event_id
        self.event_received_time = event_received_time
        self.event_source = event_source
        self.event_type = event_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name
        if self.event_id is not None:
            result['EventId'] = self.event_id
        if self.event_received_time is not None:
            result['EventReceivedTime'] = self.event_received_time
        if self.event_source is not None:
            result['EventSource'] = self.event_source
        if self.event_type is not None:
            result['EventType'] = self.event_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        if m.get('EventReceivedTime') is not None:
            self.event_received_time = m.get('EventReceivedTime')
        if m.get('EventSource') is not None:
            self.event_source = m.get('EventSource')
        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')
        return self


class QueryTracedEventByEventIdResponseBodyData(TeaModel):
    def __init__(
        self,
        events: List[QueryTracedEventByEventIdResponseBodyDataEvents] = None,
        next_token: str = None,
        total: int = None,
    ):
        self.events = events
        self.next_token = next_token
        self.total = total

    def validate(self):
        if self.events:
            for k in self.events:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Events'] = []
        if self.events is not None:
            for k in self.events:
                result['Events'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.events = []
        if m.get('Events') is not None:
            for k in m.get('Events'):
                temp_model = QueryTracedEventByEventIdResponseBodyDataEvents()
                self.events.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class QueryTracedEventByEventIdResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[QueryTracedEventByEventIdResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = QueryTracedEventByEventIdResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryTracedEventByEventIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryTracedEventByEventIdResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = QueryTracedEventByEventIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTracedEventsRequest(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        event_bus_name: str = None,
        event_source: str = None,
        event_type: str = None,
        limit: int = None,
        matched_rule: str = None,
        next_token: str = None,
        start_time: int = None,
    ):
        self.end_time = end_time
        self.event_bus_name = event_bus_name
        self.event_source = event_source
        self.event_type = event_type
        self.limit = limit
        self.matched_rule = matched_rule
        self.next_token = next_token
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name
        if self.event_source is not None:
            result['EventSource'] = self.event_source
        if self.event_type is not None:
            result['EventType'] = self.event_type
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.matched_rule is not None:
            result['MatchedRule'] = self.matched_rule
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')
        if m.get('EventSource') is not None:
            self.event_source = m.get('EventSource')
        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('MatchedRule') is not None:
            self.matched_rule = m.get('MatchedRule')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class QueryTracedEventsResponseBodyDataEvents(TeaModel):
    def __init__(
        self,
        event_bus_name: str = None,
        event_id: str = None,
        event_received_time: int = None,
        event_source: str = None,
        event_type: str = None,
    ):
        self.event_bus_name = event_bus_name
        self.event_id = event_id
        self.event_received_time = event_received_time
        self.event_source = event_source
        self.event_type = event_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name
        if self.event_id is not None:
            result['EventId'] = self.event_id
        if self.event_received_time is not None:
            result['EventReceivedTime'] = self.event_received_time
        if self.event_source is not None:
            result['EventSource'] = self.event_source
        if self.event_type is not None:
            result['EventType'] = self.event_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        if m.get('EventReceivedTime') is not None:
            self.event_received_time = m.get('EventReceivedTime')
        if m.get('EventSource') is not None:
            self.event_source = m.get('EventSource')
        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')
        return self


class QueryTracedEventsResponseBodyData(TeaModel):
    def __init__(
        self,
        events: List[QueryTracedEventsResponseBodyDataEvents] = None,
        next_token: str = None,
        total: int = None,
    ):
        self.events = events
        self.next_token = next_token
        self.total = total

    def validate(self):
        if self.events:
            for k in self.events:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Events'] = []
        if self.events is not None:
            for k in self.events:
                result['Events'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.events = []
        if m.get('Events') is not None:
            for k in m.get('Events'):
                temp_model = QueryTracedEventsResponseBodyDataEvents()
                self.events.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class QueryTracedEventsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: QueryTracedEventsResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = QueryTracedEventsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryTracedEventsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryTracedEventsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = QueryTracedEventsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RefundRequest(TeaModel):
    def __init__(
        self,
        data: str = None,
    ):
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class RefundResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        synchro: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success
        self.synchro = synchro

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.synchro is not None:
            result['Synchro'] = self.synchro
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Synchro') is not None:
            self.synchro = m.get('Synchro')
        return self


class RefundResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RefundResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = RefundResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveAndPublishSourceTaskRequest(TeaModel):
    def __init__(
        self,
        bus_name: str = None,
        id: str = None,
        name: str = None,
        source_config: Dict[str, Any] = None,
        source_type: str = None,
    ):
        self.bus_name = bus_name
        self.id = id
        self.name = name
        self.source_config = source_config
        self.source_type = source_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bus_name is not None:
            result['BusName'] = self.bus_name
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.source_config is not None:
            result['SourceConfig'] = self.source_config
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusName') is not None:
            self.bus_name = m.get('BusName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SourceConfig') is not None:
            self.source_config = m.get('SourceConfig')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        return self


class SaveAndPublishSourceTaskShrinkRequest(TeaModel):
    def __init__(
        self,
        bus_name: str = None,
        id: str = None,
        name: str = None,
        source_config_shrink: str = None,
        source_type: str = None,
    ):
        self.bus_name = bus_name
        self.id = id
        self.name = name
        self.source_config_shrink = source_config_shrink
        self.source_type = source_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bus_name is not None:
            result['BusName'] = self.bus_name
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.source_config_shrink is not None:
            result['SourceConfig'] = self.source_config_shrink
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusName') is not None:
            self.bus_name = m.get('BusName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SourceConfig') is not None:
            self.source_config_shrink = m.get('SourceConfig')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        return self


class SaveAndPublishSourceTaskResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SaveAndPublishSourceTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SaveAndPublishSourceTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = SaveAndPublishSourceTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveAndStartEventStreamingRequestEBEventSourceEntry(TeaModel):
    def __init__(
        self,
        description: str = None,
        external_source_config: Dict[str, Any] = None,
        external_source_type: str = None,
        is_new: bool = None,
        name: str = None,
    ):
        self.description = description
        self.external_source_config = external_source_config
        self.external_source_type = external_source_type
        self.is_new = is_new
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.external_source_config is not None:
            result['ExternalSourceConfig'] = self.external_source_config
        if self.external_source_type is not None:
            result['ExternalSourceType'] = self.external_source_type
        if self.is_new is not None:
            result['IsNew'] = self.is_new
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ExternalSourceConfig') is not None:
            self.external_source_config = m.get('ExternalSourceConfig')
        if m.get('ExternalSourceType') is not None:
            self.external_source_type = m.get('ExternalSourceType')
        if m.get('IsNew') is not None:
            self.is_new = m.get('IsNew')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class SaveAndStartEventStreamingRequestTargetsParamList(TeaModel):
    def __init__(
        self,
        form: str = None,
        resource_key: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.resource_key = resource_key
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.resource_key is not None:
            result['ResourceKey'] = self.resource_key
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('ResourceKey') is not None:
            self.resource_key = m.get('ResourceKey')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class SaveAndStartEventStreamingRequestTargets(TeaModel):
    def __init__(
        self,
        endpoint: str = None,
        id: str = None,
        param_list: List[SaveAndStartEventStreamingRequestTargetsParamList] = None,
        push_retry_strategy: str = None,
        type: str = None,
    ):
        self.endpoint = endpoint
        self.id = id
        self.param_list = param_list
        self.push_retry_strategy = push_retry_strategy
        self.type = type

    def validate(self):
        if self.param_list:
            for k in self.param_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.id is not None:
            result['Id'] = self.id
        result['ParamList'] = []
        if self.param_list is not None:
            for k in self.param_list:
                result['ParamList'].append(k.to_map() if k else None)
        if self.push_retry_strategy is not None:
            result['PushRetryStrategy'] = self.push_retry_strategy
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        self.param_list = []
        if m.get('ParamList') is not None:
            for k in m.get('ParamList'):
                temp_model = SaveAndStartEventStreamingRequestTargetsParamList()
                self.param_list.append(temp_model.from_map(k))
        if m.get('PushRetryStrategy') is not None:
            self.push_retry_strategy = m.get('PushRetryStrategy')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class SaveAndStartEventStreamingRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        ebevent_source_entry: SaveAndStartEventStreamingRequestEBEventSourceEntry = None,
        filter_pattern: str = None,
        name: str = None,
        targets: SaveAndStartEventStreamingRequestTargets = None,
    ):
        self.description = description
        self.ebevent_source_entry = ebevent_source_entry
        self.filter_pattern = filter_pattern
        self.name = name
        self.targets = targets

    def validate(self):
        if self.ebevent_source_entry:
            self.ebevent_source_entry.validate()
        if self.targets:
            self.targets.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.ebevent_source_entry is not None:
            result['EBEventSourceEntry'] = self.ebevent_source_entry.to_map()
        if self.filter_pattern is not None:
            result['FilterPattern'] = self.filter_pattern
        if self.name is not None:
            result['Name'] = self.name
        if self.targets is not None:
            result['Targets'] = self.targets.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EBEventSourceEntry') is not None:
            temp_model = SaveAndStartEventStreamingRequestEBEventSourceEntry()
            self.ebevent_source_entry = temp_model.from_map(m['EBEventSourceEntry'])
        if m.get('FilterPattern') is not None:
            self.filter_pattern = m.get('FilterPattern')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Targets') is not None:
            temp_model = SaveAndStartEventStreamingRequestTargets()
            self.targets = temp_model.from_map(m['Targets'])
        return self


class SaveAndStartEventStreamingShrinkRequestTargetsParamList(TeaModel):
    def __init__(
        self,
        form: str = None,
        resource_key: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.resource_key = resource_key
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.resource_key is not None:
            result['ResourceKey'] = self.resource_key
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('ResourceKey') is not None:
            self.resource_key = m.get('ResourceKey')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class SaveAndStartEventStreamingShrinkRequestTargets(TeaModel):
    def __init__(
        self,
        endpoint: str = None,
        id: str = None,
        param_list: List[SaveAndStartEventStreamingShrinkRequestTargetsParamList] = None,
        push_retry_strategy: str = None,
        type: str = None,
    ):
        self.endpoint = endpoint
        self.id = id
        self.param_list = param_list
        self.push_retry_strategy = push_retry_strategy
        self.type = type

    def validate(self):
        if self.param_list:
            for k in self.param_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.id is not None:
            result['Id'] = self.id
        result['ParamList'] = []
        if self.param_list is not None:
            for k in self.param_list:
                result['ParamList'].append(k.to_map() if k else None)
        if self.push_retry_strategy is not None:
            result['PushRetryStrategy'] = self.push_retry_strategy
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        self.param_list = []
        if m.get('ParamList') is not None:
            for k in m.get('ParamList'):
                temp_model = SaveAndStartEventStreamingShrinkRequestTargetsParamList()
                self.param_list.append(temp_model.from_map(k))
        if m.get('PushRetryStrategy') is not None:
            self.push_retry_strategy = m.get('PushRetryStrategy')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class SaveAndStartEventStreamingShrinkRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        ebevent_source_entry_shrink: str = None,
        filter_pattern: str = None,
        name: str = None,
        targets: SaveAndStartEventStreamingShrinkRequestTargets = None,
    ):
        self.description = description
        self.ebevent_source_entry_shrink = ebevent_source_entry_shrink
        self.filter_pattern = filter_pattern
        self.name = name
        self.targets = targets

    def validate(self):
        if self.targets:
            self.targets.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.ebevent_source_entry_shrink is not None:
            result['EBEventSourceEntry'] = self.ebevent_source_entry_shrink
        if self.filter_pattern is not None:
            result['FilterPattern'] = self.filter_pattern
        if self.name is not None:
            result['Name'] = self.name
        if self.targets is not None:
            result['Targets'] = self.targets.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EBEventSourceEntry') is not None:
            self.ebevent_source_entry_shrink = m.get('EBEventSourceEntry')
        if m.get('FilterPattern') is not None:
            self.filter_pattern = m.get('FilterPattern')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Targets') is not None:
            temp_model = SaveAndStartEventStreamingShrinkRequestTargets()
            self.targets = temp_model.from_map(m['Targets'])
        return self


class SaveAndStartEventStreamingResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SaveAndStartEventStreamingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SaveAndStartEventStreamingResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = SaveAndStartEventStreamingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveAndStartSourceTaskRequest(TeaModel):
    def __init__(
        self,
        bus_name: str = None,
        id: str = None,
        name: str = None,
        source_config: Dict[str, Any] = None,
        source_type: str = None,
    ):
        self.bus_name = bus_name
        self.id = id
        self.name = name
        self.source_config = source_config
        self.source_type = source_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bus_name is not None:
            result['BusName'] = self.bus_name
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.source_config is not None:
            result['SourceConfig'] = self.source_config
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusName') is not None:
            self.bus_name = m.get('BusName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SourceConfig') is not None:
            self.source_config = m.get('SourceConfig')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        return self


class SaveAndStartSourceTaskShrinkRequest(TeaModel):
    def __init__(
        self,
        bus_name: str = None,
        id: str = None,
        name: str = None,
        source_config_shrink: str = None,
        source_type: str = None,
    ):
        self.bus_name = bus_name
        self.id = id
        self.name = name
        self.source_config_shrink = source_config_shrink
        self.source_type = source_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bus_name is not None:
            result['BusName'] = self.bus_name
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.source_config_shrink is not None:
            result['SourceConfig'] = self.source_config_shrink
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusName') is not None:
            self.bus_name = m.get('BusName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SourceConfig') is not None:
            self.source_config_shrink = m.get('SourceConfig')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        return self


class SaveAndStartSourceTaskResponseBodyData(TeaModel):
    def __init__(
        self,
        task_id: str = None,
    ):
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class SaveAndStartSourceTaskResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: SaveAndStartSourceTaskResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = SaveAndStartSourceTaskResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SaveAndStartSourceTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SaveAndStartSourceTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = SaveAndStartSourceTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartEventStreamingRequest(TeaModel):
    def __init__(
        self,
        event_streaming_name: str = None,
    ):
        self.event_streaming_name = event_streaming_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_streaming_name is not None:
            result['EventStreamingName'] = self.event_streaming_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventStreamingName') is not None:
            self.event_streaming_name = m.get('EventStreamingName')
        return self


class StartEventStreamingResponseBody(TeaModel):
    def __init__(
        self,
        code: bool = None,
        data: bool = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class StartEventStreamingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StartEventStreamingResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = StartEventStreamingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartSourceTaskRequest(TeaModel):
    def __init__(
        self,
        task_id: str = None,
    ):
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class StartSourceTaskResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class StartSourceTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StartSourceTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = StartSourceTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateEventBusRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        event_bus_name: str = None,
    ):
        self.description = description
        self.event_bus_name = event_bus_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')
        return self


class UpdateEventBusResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateEventBusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateEventBusResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = UpdateEventBusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateEventSourceRequest(TeaModel):
    def __init__(
        self,
        description: bytes = None,
        event_bus_name: bytes = None,
        event_source_name: bytes = None,
        external_source_config: Dict[str, Any] = None,
        external_source_type: bytes = None,
        linked_external_source: bool = None,
    ):
        # 事件源描述详情
        self.description = description
        self.event_bus_name = event_bus_name
        # 事件源英文Code
        self.event_source_name = event_source_name
        self.external_source_config = external_source_config
        self.external_source_type = external_source_type
        self.linked_external_source = linked_external_source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name
        if self.event_source_name is not None:
            result['EventSourceName'] = self.event_source_name
        if self.external_source_config is not None:
            result['ExternalSourceConfig'] = self.external_source_config
        if self.external_source_type is not None:
            result['ExternalSourceType'] = self.external_source_type
        if self.linked_external_source is not None:
            result['LinkedExternalSource'] = self.linked_external_source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')
        if m.get('EventSourceName') is not None:
            self.event_source_name = m.get('EventSourceName')
        if m.get('ExternalSourceConfig') is not None:
            self.external_source_config = m.get('ExternalSourceConfig')
        if m.get('ExternalSourceType') is not None:
            self.external_source_type = m.get('ExternalSourceType')
        if m.get('LinkedExternalSource') is not None:
            self.linked_external_source = m.get('LinkedExternalSource')
        return self


class UpdateEventSourceShrinkRequest(TeaModel):
    def __init__(
        self,
        description: bytes = None,
        event_bus_name: bytes = None,
        event_source_name: bytes = None,
        external_source_config_shrink: str = None,
        external_source_type: bytes = None,
        linked_external_source: bool = None,
    ):
        # 事件源描述详情
        self.description = description
        self.event_bus_name = event_bus_name
        # 事件源英文Code
        self.event_source_name = event_source_name
        self.external_source_config_shrink = external_source_config_shrink
        self.external_source_type = external_source_type
        self.linked_external_source = linked_external_source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name
        if self.event_source_name is not None:
            result['EventSourceName'] = self.event_source_name
        if self.external_source_config_shrink is not None:
            result['ExternalSourceConfig'] = self.external_source_config_shrink
        if self.external_source_type is not None:
            result['ExternalSourceType'] = self.external_source_type
        if self.linked_external_source is not None:
            result['LinkedExternalSource'] = self.linked_external_source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')
        if m.get('EventSourceName') is not None:
            self.event_source_name = m.get('EventSourceName')
        if m.get('ExternalSourceConfig') is not None:
            self.external_source_config_shrink = m.get('ExternalSourceConfig')
        if m.get('ExternalSourceType') is not None:
            self.external_source_type = m.get('ExternalSourceType')
        if m.get('LinkedExternalSource') is not None:
            self.linked_external_source = m.get('LinkedExternalSource')
        return self


class UpdateEventSourceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateEventSourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateEventSourceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = UpdateEventSourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateEventStreamingRequestRunOptionsBatchWindow(TeaModel):
    def __init__(
        self,
        count_based_window: int = None,
        time_based_window: int = None,
    ):
        self.count_based_window = count_based_window
        self.time_based_window = time_based_window

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count_based_window is not None:
            result['CountBasedWindow'] = self.count_based_window
        if self.time_based_window is not None:
            result['TimeBasedWindow'] = self.time_based_window
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CountBasedWindow') is not None:
            self.count_based_window = m.get('CountBasedWindow')
        if m.get('TimeBasedWindow') is not None:
            self.time_based_window = m.get('TimeBasedWindow')
        return self


class UpdateEventStreamingRequestRunOptionsDeadLetterQueue(TeaModel):
    def __init__(
        self,
        arn: str = None,
    ):
        self.arn = arn

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arn is not None:
            result['Arn'] = self.arn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        return self


class UpdateEventStreamingRequestRunOptionsRetryStrategy(TeaModel):
    def __init__(
        self,
        maximum_event_age_in_seconds: int = None,
        maximum_retry_attempts: int = None,
        push_retry_strategy: str = None,
    ):
        self.maximum_event_age_in_seconds = maximum_event_age_in_seconds
        self.maximum_retry_attempts = maximum_retry_attempts
        self.push_retry_strategy = push_retry_strategy

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.maximum_event_age_in_seconds is not None:
            result['MaximumEventAgeInSeconds'] = self.maximum_event_age_in_seconds
        if self.maximum_retry_attempts is not None:
            result['MaximumRetryAttempts'] = self.maximum_retry_attempts
        if self.push_retry_strategy is not None:
            result['PushRetryStrategy'] = self.push_retry_strategy
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaximumEventAgeInSeconds') is not None:
            self.maximum_event_age_in_seconds = m.get('MaximumEventAgeInSeconds')
        if m.get('MaximumRetryAttempts') is not None:
            self.maximum_retry_attempts = m.get('MaximumRetryAttempts')
        if m.get('PushRetryStrategy') is not None:
            self.push_retry_strategy = m.get('PushRetryStrategy')
        return self


class UpdateEventStreamingRequestRunOptions(TeaModel):
    def __init__(
        self,
        batch_window: UpdateEventStreamingRequestRunOptionsBatchWindow = None,
        dead_letter_queue: UpdateEventStreamingRequestRunOptionsDeadLetterQueue = None,
        errors_tolerance: str = None,
        maximum_tasks: int = None,
        retry_strategy: UpdateEventStreamingRequestRunOptionsRetryStrategy = None,
    ):
        self.batch_window = batch_window
        self.dead_letter_queue = dead_letter_queue
        self.errors_tolerance = errors_tolerance
        self.maximum_tasks = maximum_tasks
        self.retry_strategy = retry_strategy

    def validate(self):
        if self.batch_window:
            self.batch_window.validate()
        if self.dead_letter_queue:
            self.dead_letter_queue.validate()
        if self.retry_strategy:
            self.retry_strategy.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.batch_window is not None:
            result['BatchWindow'] = self.batch_window.to_map()
        if self.dead_letter_queue is not None:
            result['DeadLetterQueue'] = self.dead_letter_queue.to_map()
        if self.errors_tolerance is not None:
            result['ErrorsTolerance'] = self.errors_tolerance
        if self.maximum_tasks is not None:
            result['MaximumTasks'] = self.maximum_tasks
        if self.retry_strategy is not None:
            result['RetryStrategy'] = self.retry_strategy.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BatchWindow') is not None:
            temp_model = UpdateEventStreamingRequestRunOptionsBatchWindow()
            self.batch_window = temp_model.from_map(m['BatchWindow'])
        if m.get('DeadLetterQueue') is not None:
            temp_model = UpdateEventStreamingRequestRunOptionsDeadLetterQueue()
            self.dead_letter_queue = temp_model.from_map(m['DeadLetterQueue'])
        if m.get('ErrorsTolerance') is not None:
            self.errors_tolerance = m.get('ErrorsTolerance')
        if m.get('MaximumTasks') is not None:
            self.maximum_tasks = m.get('MaximumTasks')
        if m.get('RetryStrategy') is not None:
            temp_model = UpdateEventStreamingRequestRunOptionsRetryStrategy()
            self.retry_strategy = temp_model.from_map(m['RetryStrategy'])
        return self


class UpdateEventStreamingRequestSinkSinkFcParametersBody(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateEventStreamingRequestSinkSinkFcParametersFunctionName(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateEventStreamingRequestSinkSinkFcParametersInvocationType(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateEventStreamingRequestSinkSinkFcParametersQualifier(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateEventStreamingRequestSinkSinkFcParametersServiceName(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateEventStreamingRequestSinkSinkFcParameters(TeaModel):
    def __init__(
        self,
        body: UpdateEventStreamingRequestSinkSinkFcParametersBody = None,
        function_name: UpdateEventStreamingRequestSinkSinkFcParametersFunctionName = None,
        invocation_type: UpdateEventStreamingRequestSinkSinkFcParametersInvocationType = None,
        qualifier: UpdateEventStreamingRequestSinkSinkFcParametersQualifier = None,
        service_name: UpdateEventStreamingRequestSinkSinkFcParametersServiceName = None,
    ):
        self.body = body
        self.function_name = function_name
        self.invocation_type = invocation_type
        self.qualifier = qualifier
        self.service_name = service_name

    def validate(self):
        if self.body:
            self.body.validate()
        if self.function_name:
            self.function_name.validate()
        if self.invocation_type:
            self.invocation_type.validate()
        if self.qualifier:
            self.qualifier.validate()
        if self.service_name:
            self.service_name.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['Body'] = self.body.to_map()
        if self.function_name is not None:
            result['FunctionName'] = self.function_name.to_map()
        if self.invocation_type is not None:
            result['InvocationType'] = self.invocation_type.to_map()
        if self.qualifier is not None:
            result['Qualifier'] = self.qualifier.to_map()
        if self.service_name is not None:
            result['ServiceName'] = self.service_name.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Body') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkFcParametersBody()
            self.body = temp_model.from_map(m['Body'])
        if m.get('FunctionName') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkFcParametersFunctionName()
            self.function_name = temp_model.from_map(m['FunctionName'])
        if m.get('InvocationType') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkFcParametersInvocationType()
            self.invocation_type = temp_model.from_map(m['InvocationType'])
        if m.get('Qualifier') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkFcParametersQualifier()
            self.qualifier = temp_model.from_map(m['Qualifier'])
        if m.get('ServiceName') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkFcParametersServiceName()
            self.service_name = temp_model.from_map(m['ServiceName'])
        return self


class UpdateEventStreamingRequestSinkSinkKafkaParametersAcks(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateEventStreamingRequestSinkSinkKafkaParametersInstanceId(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateEventStreamingRequestSinkSinkKafkaParametersKey(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateEventStreamingRequestSinkSinkKafkaParametersSaslUser(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateEventStreamingRequestSinkSinkKafkaParametersTopic(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateEventStreamingRequestSinkSinkKafkaParametersValue(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateEventStreamingRequestSinkSinkKafkaParameters(TeaModel):
    def __init__(
        self,
        acks: UpdateEventStreamingRequestSinkSinkKafkaParametersAcks = None,
        instance_id: UpdateEventStreamingRequestSinkSinkKafkaParametersInstanceId = None,
        key: UpdateEventStreamingRequestSinkSinkKafkaParametersKey = None,
        sasl_user: UpdateEventStreamingRequestSinkSinkKafkaParametersSaslUser = None,
        topic: UpdateEventStreamingRequestSinkSinkKafkaParametersTopic = None,
        value: UpdateEventStreamingRequestSinkSinkKafkaParametersValue = None,
    ):
        self.acks = acks
        self.instance_id = instance_id
        self.key = key
        self.sasl_user = sasl_user
        self.topic = topic
        self.value = value

    def validate(self):
        if self.acks:
            self.acks.validate()
        if self.instance_id:
            self.instance_id.validate()
        if self.key:
            self.key.validate()
        if self.sasl_user:
            self.sasl_user.validate()
        if self.topic:
            self.topic.validate()
        if self.value:
            self.value.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acks is not None:
            result['Acks'] = self.acks.to_map()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id.to_map()
        if self.key is not None:
            result['Key'] = self.key.to_map()
        if self.sasl_user is not None:
            result['SaslUser'] = self.sasl_user.to_map()
        if self.topic is not None:
            result['Topic'] = self.topic.to_map()
        if self.value is not None:
            result['Value'] = self.value.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Acks') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkKafkaParametersAcks()
            self.acks = temp_model.from_map(m['Acks'])
        if m.get('InstanceId') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkKafkaParametersInstanceId()
            self.instance_id = temp_model.from_map(m['InstanceId'])
        if m.get('Key') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkKafkaParametersKey()
            self.key = temp_model.from_map(m['Key'])
        if m.get('SaslUser') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkKafkaParametersSaslUser()
            self.sasl_user = temp_model.from_map(m['SaslUser'])
        if m.get('Topic') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkKafkaParametersTopic()
            self.topic = temp_model.from_map(m['Topic'])
        if m.get('Value') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkKafkaParametersValue()
            self.value = temp_model.from_map(m['Value'])
        return self


class UpdateEventStreamingRequestSinkSinkMNSParametersBody(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateEventStreamingRequestSinkSinkMNSParametersIsBase64Encode(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateEventStreamingRequestSinkSinkMNSParametersQueueName(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateEventStreamingRequestSinkSinkMNSParameters(TeaModel):
    def __init__(
        self,
        body: UpdateEventStreamingRequestSinkSinkMNSParametersBody = None,
        is_base_64encode: UpdateEventStreamingRequestSinkSinkMNSParametersIsBase64Encode = None,
        queue_name: UpdateEventStreamingRequestSinkSinkMNSParametersQueueName = None,
    ):
        self.body = body
        self.is_base_64encode = is_base_64encode
        self.queue_name = queue_name

    def validate(self):
        if self.body:
            self.body.validate()
        if self.is_base_64encode:
            self.is_base_64encode.validate()
        if self.queue_name:
            self.queue_name.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['Body'] = self.body.to_map()
        if self.is_base_64encode is not None:
            result['IsBase64Encode'] = self.is_base_64encode.to_map()
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Body') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkMNSParametersBody()
            self.body = temp_model.from_map(m['Body'])
        if m.get('IsBase64Encode') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkMNSParametersIsBase64Encode()
            self.is_base_64encode = temp_model.from_map(m['IsBase64Encode'])
        if m.get('QueueName') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkMNSParametersQueueName()
            self.queue_name = temp_model.from_map(m['QueueName'])
        return self


class UpdateEventStreamingRequestSinkSinkRabbitMQParametersBody(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateEventStreamingRequestSinkSinkRabbitMQParametersExchange(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateEventStreamingRequestSinkSinkRabbitMQParametersInstanceId(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateEventStreamingRequestSinkSinkRabbitMQParametersMessageId(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateEventStreamingRequestSinkSinkRabbitMQParametersProperties(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateEventStreamingRequestSinkSinkRabbitMQParametersQueueName(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateEventStreamingRequestSinkSinkRabbitMQParametersRoutingKey(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateEventStreamingRequestSinkSinkRabbitMQParametersTargetType(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateEventStreamingRequestSinkSinkRabbitMQParametersVirtualHostName(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateEventStreamingRequestSinkSinkRabbitMQParameters(TeaModel):
    def __init__(
        self,
        body: UpdateEventStreamingRequestSinkSinkRabbitMQParametersBody = None,
        exchange: UpdateEventStreamingRequestSinkSinkRabbitMQParametersExchange = None,
        instance_id: UpdateEventStreamingRequestSinkSinkRabbitMQParametersInstanceId = None,
        message_id: UpdateEventStreamingRequestSinkSinkRabbitMQParametersMessageId = None,
        properties: UpdateEventStreamingRequestSinkSinkRabbitMQParametersProperties = None,
        queue_name: UpdateEventStreamingRequestSinkSinkRabbitMQParametersQueueName = None,
        routing_key: UpdateEventStreamingRequestSinkSinkRabbitMQParametersRoutingKey = None,
        target_type: UpdateEventStreamingRequestSinkSinkRabbitMQParametersTargetType = None,
        virtual_host_name: UpdateEventStreamingRequestSinkSinkRabbitMQParametersVirtualHostName = None,
    ):
        self.body = body
        self.exchange = exchange
        self.instance_id = instance_id
        self.message_id = message_id
        self.properties = properties
        self.queue_name = queue_name
        self.routing_key = routing_key
        self.target_type = target_type
        self.virtual_host_name = virtual_host_name

    def validate(self):
        if self.body:
            self.body.validate()
        if self.exchange:
            self.exchange.validate()
        if self.instance_id:
            self.instance_id.validate()
        if self.message_id:
            self.message_id.validate()
        if self.properties:
            self.properties.validate()
        if self.queue_name:
            self.queue_name.validate()
        if self.routing_key:
            self.routing_key.validate()
        if self.target_type:
            self.target_type.validate()
        if self.virtual_host_name:
            self.virtual_host_name.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['Body'] = self.body.to_map()
        if self.exchange is not None:
            result['Exchange'] = self.exchange.to_map()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id.to_map()
        if self.message_id is not None:
            result['MessageId'] = self.message_id.to_map()
        if self.properties is not None:
            result['Properties'] = self.properties.to_map()
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name.to_map()
        if self.routing_key is not None:
            result['RoutingKey'] = self.routing_key.to_map()
        if self.target_type is not None:
            result['TargetType'] = self.target_type.to_map()
        if self.virtual_host_name is not None:
            result['VirtualHostName'] = self.virtual_host_name.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Body') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkRabbitMQParametersBody()
            self.body = temp_model.from_map(m['Body'])
        if m.get('Exchange') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkRabbitMQParametersExchange()
            self.exchange = temp_model.from_map(m['Exchange'])
        if m.get('InstanceId') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkRabbitMQParametersInstanceId()
            self.instance_id = temp_model.from_map(m['InstanceId'])
        if m.get('MessageId') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkRabbitMQParametersMessageId()
            self.message_id = temp_model.from_map(m['MessageId'])
        if m.get('Properties') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkRabbitMQParametersProperties()
            self.properties = temp_model.from_map(m['Properties'])
        if m.get('QueueName') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkRabbitMQParametersQueueName()
            self.queue_name = temp_model.from_map(m['QueueName'])
        if m.get('RoutingKey') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkRabbitMQParametersRoutingKey()
            self.routing_key = temp_model.from_map(m['RoutingKey'])
        if m.get('TargetType') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkRabbitMQParametersTargetType()
            self.target_type = temp_model.from_map(m['TargetType'])
        if m.get('VirtualHostName') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkRabbitMQParametersVirtualHostName()
            self.virtual_host_name = temp_model.from_map(m['VirtualHostName'])
        return self


class UpdateEventStreamingRequestSinkSinkRocketMQParametersBody(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateEventStreamingRequestSinkSinkRocketMQParametersInstanceId(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateEventStreamingRequestSinkSinkRocketMQParametersKeys(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateEventStreamingRequestSinkSinkRocketMQParametersProperties(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateEventStreamingRequestSinkSinkRocketMQParametersTags(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateEventStreamingRequestSinkSinkRocketMQParametersTopic(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateEventStreamingRequestSinkSinkRocketMQParameters(TeaModel):
    def __init__(
        self,
        body: UpdateEventStreamingRequestSinkSinkRocketMQParametersBody = None,
        instance_id: UpdateEventStreamingRequestSinkSinkRocketMQParametersInstanceId = None,
        keys: UpdateEventStreamingRequestSinkSinkRocketMQParametersKeys = None,
        properties: UpdateEventStreamingRequestSinkSinkRocketMQParametersProperties = None,
        tags: UpdateEventStreamingRequestSinkSinkRocketMQParametersTags = None,
        topic: UpdateEventStreamingRequestSinkSinkRocketMQParametersTopic = None,
    ):
        self.body = body
        self.instance_id = instance_id
        self.keys = keys
        self.properties = properties
        self.tags = tags
        self.topic = topic

    def validate(self):
        if self.body:
            self.body.validate()
        if self.instance_id:
            self.instance_id.validate()
        if self.keys:
            self.keys.validate()
        if self.properties:
            self.properties.validate()
        if self.tags:
            self.tags.validate()
        if self.topic:
            self.topic.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['Body'] = self.body.to_map()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id.to_map()
        if self.keys is not None:
            result['Keys'] = self.keys.to_map()
        if self.properties is not None:
            result['Properties'] = self.properties.to_map()
        if self.tags is not None:
            result['Tags'] = self.tags.to_map()
        if self.topic is not None:
            result['Topic'] = self.topic.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Body') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkRocketMQParametersBody()
            self.body = temp_model.from_map(m['Body'])
        if m.get('InstanceId') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkRocketMQParametersInstanceId()
            self.instance_id = temp_model.from_map(m['InstanceId'])
        if m.get('Keys') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkRocketMQParametersKeys()
            self.keys = temp_model.from_map(m['Keys'])
        if m.get('Properties') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkRocketMQParametersProperties()
            self.properties = temp_model.from_map(m['Properties'])
        if m.get('Tags') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkRocketMQParametersTags()
            self.tags = temp_model.from_map(m['Tags'])
        if m.get('Topic') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkRocketMQParametersTopic()
            self.topic = temp_model.from_map(m['Topic'])
        return self


class UpdateEventStreamingRequestSinkSinkSLSParametersBody(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateEventStreamingRequestSinkSinkSLSParametersLogStore(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateEventStreamingRequestSinkSinkSLSParametersProject(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateEventStreamingRequestSinkSinkSLSParametersRoleName(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateEventStreamingRequestSinkSinkSLSParametersTopic(TeaModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateEventStreamingRequestSinkSinkSLSParameters(TeaModel):
    def __init__(
        self,
        body: UpdateEventStreamingRequestSinkSinkSLSParametersBody = None,
        log_store: UpdateEventStreamingRequestSinkSinkSLSParametersLogStore = None,
        project: UpdateEventStreamingRequestSinkSinkSLSParametersProject = None,
        role_name: UpdateEventStreamingRequestSinkSinkSLSParametersRoleName = None,
        topic: UpdateEventStreamingRequestSinkSinkSLSParametersTopic = None,
    ):
        self.body = body
        self.log_store = log_store
        self.project = project
        self.role_name = role_name
        self.topic = topic

    def validate(self):
        if self.body:
            self.body.validate()
        if self.log_store:
            self.log_store.validate()
        if self.project:
            self.project.validate()
        if self.role_name:
            self.role_name.validate()
        if self.topic:
            self.topic.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['Body'] = self.body.to_map()
        if self.log_store is not None:
            result['LogStore'] = self.log_store.to_map()
        if self.project is not None:
            result['Project'] = self.project.to_map()
        if self.role_name is not None:
            result['RoleName'] = self.role_name.to_map()
        if self.topic is not None:
            result['Topic'] = self.topic.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Body') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkSLSParametersBody()
            self.body = temp_model.from_map(m['Body'])
        if m.get('LogStore') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkSLSParametersLogStore()
            self.log_store = temp_model.from_map(m['LogStore'])
        if m.get('Project') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkSLSParametersProject()
            self.project = temp_model.from_map(m['Project'])
        if m.get('RoleName') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkSLSParametersRoleName()
            self.role_name = temp_model.from_map(m['RoleName'])
        if m.get('Topic') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkSLSParametersTopic()
            self.topic = temp_model.from_map(m['Topic'])
        return self


class UpdateEventStreamingRequestSink(TeaModel):
    def __init__(
        self,
        sink_fc_parameters: UpdateEventStreamingRequestSinkSinkFcParameters = None,
        sink_kafka_parameters: UpdateEventStreamingRequestSinkSinkKafkaParameters = None,
        sink_mnsparameters: UpdateEventStreamingRequestSinkSinkMNSParameters = None,
        sink_rabbit_mqparameters: UpdateEventStreamingRequestSinkSinkRabbitMQParameters = None,
        sink_rocket_mqparameters: UpdateEventStreamingRequestSinkSinkRocketMQParameters = None,
        sink_slsparameters: UpdateEventStreamingRequestSinkSinkSLSParameters = None,
    ):
        self.sink_fc_parameters = sink_fc_parameters
        self.sink_kafka_parameters = sink_kafka_parameters
        self.sink_mnsparameters = sink_mnsparameters
        self.sink_rabbit_mqparameters = sink_rabbit_mqparameters
        self.sink_rocket_mqparameters = sink_rocket_mqparameters
        self.sink_slsparameters = sink_slsparameters

    def validate(self):
        if self.sink_fc_parameters:
            self.sink_fc_parameters.validate()
        if self.sink_kafka_parameters:
            self.sink_kafka_parameters.validate()
        if self.sink_mnsparameters:
            self.sink_mnsparameters.validate()
        if self.sink_rabbit_mqparameters:
            self.sink_rabbit_mqparameters.validate()
        if self.sink_rocket_mqparameters:
            self.sink_rocket_mqparameters.validate()
        if self.sink_slsparameters:
            self.sink_slsparameters.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sink_fc_parameters is not None:
            result['SinkFcParameters'] = self.sink_fc_parameters.to_map()
        if self.sink_kafka_parameters is not None:
            result['SinkKafkaParameters'] = self.sink_kafka_parameters.to_map()
        if self.sink_mnsparameters is not None:
            result['SinkMNSParameters'] = self.sink_mnsparameters.to_map()
        if self.sink_rabbit_mqparameters is not None:
            result['SinkRabbitMQParameters'] = self.sink_rabbit_mqparameters.to_map()
        if self.sink_rocket_mqparameters is not None:
            result['SinkRocketMQParameters'] = self.sink_rocket_mqparameters.to_map()
        if self.sink_slsparameters is not None:
            result['SinkSLSParameters'] = self.sink_slsparameters.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SinkFcParameters') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkFcParameters()
            self.sink_fc_parameters = temp_model.from_map(m['SinkFcParameters'])
        if m.get('SinkKafkaParameters') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkKafkaParameters()
            self.sink_kafka_parameters = temp_model.from_map(m['SinkKafkaParameters'])
        if m.get('SinkMNSParameters') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkMNSParameters()
            self.sink_mnsparameters = temp_model.from_map(m['SinkMNSParameters'])
        if m.get('SinkRabbitMQParameters') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkRabbitMQParameters()
            self.sink_rabbit_mqparameters = temp_model.from_map(m['SinkRabbitMQParameters'])
        if m.get('SinkRocketMQParameters') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkRocketMQParameters()
            self.sink_rocket_mqparameters = temp_model.from_map(m['SinkRocketMQParameters'])
        if m.get('SinkSLSParameters') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkSLSParameters()
            self.sink_slsparameters = temp_model.from_map(m['SinkSLSParameters'])
        return self


class UpdateEventStreamingRequestSourceSourceDTSParameters(TeaModel):
    def __init__(
        self,
        broker_url: str = None,
        init_check_point: int = None,
        password: str = None,
        sid: str = None,
        task_id: str = None,
        topic: str = None,
        username: str = None,
    ):
        self.broker_url = broker_url
        self.init_check_point = init_check_point
        self.password = password
        self.sid = sid
        self.task_id = task_id
        self.topic = topic
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.broker_url is not None:
            result['BrokerUrl'] = self.broker_url
        if self.init_check_point is not None:
            result['InitCheckPoint'] = self.init_check_point
        if self.password is not None:
            result['Password'] = self.password
        if self.sid is not None:
            result['Sid'] = self.sid
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.topic is not None:
            result['Topic'] = self.topic
        if self.username is not None:
            result['Username'] = self.username
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BrokerUrl') is not None:
            self.broker_url = m.get('BrokerUrl')
        if m.get('InitCheckPoint') is not None:
            self.init_check_point = m.get('InitCheckPoint')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('Sid') is not None:
            self.sid = m.get('Sid')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        return self


class UpdateEventStreamingRequestSourceSourceKafkaParameters(TeaModel):
    def __init__(
        self,
        consumer_group: str = None,
        instance_id: str = None,
        network: str = None,
        offset_reset: str = None,
        region_id: str = None,
        security_group_id: str = None,
        topic: str = None,
        v_switch_ids: str = None,
        vpc_id: str = None,
    ):
        self.consumer_group = consumer_group
        self.instance_id = instance_id
        self.network = network
        self.offset_reset = offset_reset
        self.region_id = region_id
        self.security_group_id = security_group_id
        self.topic = topic
        self.v_switch_ids = v_switch_ids
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consumer_group is not None:
            result['ConsumerGroup'] = self.consumer_group
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.network is not None:
            result['Network'] = self.network
        if self.offset_reset is not None:
            result['OffsetReset'] = self.offset_reset
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.topic is not None:
            result['Topic'] = self.topic
        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsumerGroup') is not None:
            self.consumer_group = m.get('ConsumerGroup')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Network') is not None:
            self.network = m.get('Network')
        if m.get('OffsetReset') is not None:
            self.offset_reset = m.get('OffsetReset')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class UpdateEventStreamingRequestSourceSourceMNSParameters(TeaModel):
    def __init__(
        self,
        is_base_64decode: bool = None,
        queue_name: str = None,
        region_id: str = None,
    ):
        self.is_base_64decode = is_base_64decode
        self.queue_name = queue_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_base_64decode is not None:
            result['IsBase64Decode'] = self.is_base_64decode
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsBase64Decode') is not None:
            self.is_base_64decode = m.get('IsBase64Decode')
        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class UpdateEventStreamingRequestSourceSourceMQTTParameters(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        region_id: str = None,
        topic: str = None,
    ):
        self.instance_id = instance_id
        self.region_id = region_id
        self.topic = topic

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.topic is not None:
            result['Topic'] = self.topic
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        return self


class UpdateEventStreamingRequestSourceSourceRabbitMQParameters(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        queue_name: str = None,
        region_id: str = None,
        virtual_host_name: str = None,
    ):
        self.instance_id = instance_id
        self.queue_name = queue_name
        self.region_id = region_id
        self.virtual_host_name = virtual_host_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.virtual_host_name is not None:
            result['VirtualHostName'] = self.virtual_host_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VirtualHostName') is not None:
            self.virtual_host_name = m.get('VirtualHostName')
        return self


class UpdateEventStreamingRequestSourceSourceRocketMQParameters(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        instance_id: str = None,
        offset: str = None,
        region_id: str = None,
        tag: str = None,
        timestamp: int = None,
        topic: str = None,
    ):
        self.group_id = group_id
        self.instance_id = instance_id
        self.offset = offset
        self.region_id = region_id
        self.tag = tag
        self.timestamp = timestamp
        self.topic = topic

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupID'] = self.group_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.offset is not None:
            result['Offset'] = self.offset
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.topic is not None:
            result['Topic'] = self.topic
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupID') is not None:
            self.group_id = m.get('GroupID')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Offset') is not None:
            self.offset = m.get('Offset')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        return self


class UpdateEventStreamingRequestSourceSourceSLSParameters(TeaModel):
    def __init__(
        self,
        role_name: str = None,
    ):
        self.role_name = role_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        return self


class UpdateEventStreamingRequestSource(TeaModel):
    def __init__(
        self,
        source_dtsparameters: UpdateEventStreamingRequestSourceSourceDTSParameters = None,
        source_kafka_parameters: UpdateEventStreamingRequestSourceSourceKafkaParameters = None,
        source_mnsparameters: UpdateEventStreamingRequestSourceSourceMNSParameters = None,
        source_mqttparameters: UpdateEventStreamingRequestSourceSourceMQTTParameters = None,
        source_rabbit_mqparameters: UpdateEventStreamingRequestSourceSourceRabbitMQParameters = None,
        source_rocket_mqparameters: UpdateEventStreamingRequestSourceSourceRocketMQParameters = None,
        source_slsparameters: UpdateEventStreamingRequestSourceSourceSLSParameters = None,
    ):
        self.source_dtsparameters = source_dtsparameters
        self.source_kafka_parameters = source_kafka_parameters
        self.source_mnsparameters = source_mnsparameters
        self.source_mqttparameters = source_mqttparameters
        self.source_rabbit_mqparameters = source_rabbit_mqparameters
        self.source_rocket_mqparameters = source_rocket_mqparameters
        self.source_slsparameters = source_slsparameters

    def validate(self):
        if self.source_dtsparameters:
            self.source_dtsparameters.validate()
        if self.source_kafka_parameters:
            self.source_kafka_parameters.validate()
        if self.source_mnsparameters:
            self.source_mnsparameters.validate()
        if self.source_mqttparameters:
            self.source_mqttparameters.validate()
        if self.source_rabbit_mqparameters:
            self.source_rabbit_mqparameters.validate()
        if self.source_rocket_mqparameters:
            self.source_rocket_mqparameters.validate()
        if self.source_slsparameters:
            self.source_slsparameters.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_dtsparameters is not None:
            result['SourceDTSParameters'] = self.source_dtsparameters.to_map()
        if self.source_kafka_parameters is not None:
            result['SourceKafkaParameters'] = self.source_kafka_parameters.to_map()
        if self.source_mnsparameters is not None:
            result['SourceMNSParameters'] = self.source_mnsparameters.to_map()
        if self.source_mqttparameters is not None:
            result['SourceMQTTParameters'] = self.source_mqttparameters.to_map()
        if self.source_rabbit_mqparameters is not None:
            result['SourceRabbitMQParameters'] = self.source_rabbit_mqparameters.to_map()
        if self.source_rocket_mqparameters is not None:
            result['SourceRocketMQParameters'] = self.source_rocket_mqparameters.to_map()
        if self.source_slsparameters is not None:
            result['SourceSLSParameters'] = self.source_slsparameters.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceDTSParameters') is not None:
            temp_model = UpdateEventStreamingRequestSourceSourceDTSParameters()
            self.source_dtsparameters = temp_model.from_map(m['SourceDTSParameters'])
        if m.get('SourceKafkaParameters') is not None:
            temp_model = UpdateEventStreamingRequestSourceSourceKafkaParameters()
            self.source_kafka_parameters = temp_model.from_map(m['SourceKafkaParameters'])
        if m.get('SourceMNSParameters') is not None:
            temp_model = UpdateEventStreamingRequestSourceSourceMNSParameters()
            self.source_mnsparameters = temp_model.from_map(m['SourceMNSParameters'])
        if m.get('SourceMQTTParameters') is not None:
            temp_model = UpdateEventStreamingRequestSourceSourceMQTTParameters()
            self.source_mqttparameters = temp_model.from_map(m['SourceMQTTParameters'])
        if m.get('SourceRabbitMQParameters') is not None:
            temp_model = UpdateEventStreamingRequestSourceSourceRabbitMQParameters()
            self.source_rabbit_mqparameters = temp_model.from_map(m['SourceRabbitMQParameters'])
        if m.get('SourceRocketMQParameters') is not None:
            temp_model = UpdateEventStreamingRequestSourceSourceRocketMQParameters()
            self.source_rocket_mqparameters = temp_model.from_map(m['SourceRocketMQParameters'])
        if m.get('SourceSLSParameters') is not None:
            temp_model = UpdateEventStreamingRequestSourceSourceSLSParameters()
            self.source_slsparameters = temp_model.from_map(m['SourceSLSParameters'])
        return self


class UpdateEventStreamingRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        event_streaming_name: str = None,
        filter_pattern: str = None,
        run_options: UpdateEventStreamingRequestRunOptions = None,
        sink: UpdateEventStreamingRequestSink = None,
        source: UpdateEventStreamingRequestSource = None,
        tag: str = None,
    ):
        self.description = description
        self.event_streaming_name = event_streaming_name
        self.filter_pattern = filter_pattern
        self.run_options = run_options
        self.sink = sink
        self.source = source
        self.tag = tag

    def validate(self):
        if self.run_options:
            self.run_options.validate()
        if self.sink:
            self.sink.validate()
        if self.source:
            self.source.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.event_streaming_name is not None:
            result['EventStreamingName'] = self.event_streaming_name
        if self.filter_pattern is not None:
            result['FilterPattern'] = self.filter_pattern
        if self.run_options is not None:
            result['RunOptions'] = self.run_options.to_map()
        if self.sink is not None:
            result['Sink'] = self.sink.to_map()
        if self.source is not None:
            result['Source'] = self.source.to_map()
        if self.tag is not None:
            result['Tag'] = self.tag
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EventStreamingName') is not None:
            self.event_streaming_name = m.get('EventStreamingName')
        if m.get('FilterPattern') is not None:
            self.filter_pattern = m.get('FilterPattern')
        if m.get('RunOptions') is not None:
            temp_model = UpdateEventStreamingRequestRunOptions()
            self.run_options = temp_model.from_map(m['RunOptions'])
        if m.get('Sink') is not None:
            temp_model = UpdateEventStreamingRequestSink()
            self.sink = temp_model.from_map(m['Sink'])
        if m.get('Source') is not None:
            temp_model = UpdateEventStreamingRequestSource()
            self.source = temp_model.from_map(m['Source'])
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        return self


class UpdateEventStreamingShrinkRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        event_streaming_name: str = None,
        filter_pattern: str = None,
        run_options_shrink: str = None,
        sink_shrink: str = None,
        source_shrink: str = None,
        tag: str = None,
    ):
        self.description = description
        self.event_streaming_name = event_streaming_name
        self.filter_pattern = filter_pattern
        self.run_options_shrink = run_options_shrink
        self.sink_shrink = sink_shrink
        self.source_shrink = source_shrink
        self.tag = tag

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.event_streaming_name is not None:
            result['EventStreamingName'] = self.event_streaming_name
        if self.filter_pattern is not None:
            result['FilterPattern'] = self.filter_pattern
        if self.run_options_shrink is not None:
            result['RunOptions'] = self.run_options_shrink
        if self.sink_shrink is not None:
            result['Sink'] = self.sink_shrink
        if self.source_shrink is not None:
            result['Source'] = self.source_shrink
        if self.tag is not None:
            result['Tag'] = self.tag
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EventStreamingName') is not None:
            self.event_streaming_name = m.get('EventStreamingName')
        if m.get('FilterPattern') is not None:
            self.filter_pattern = m.get('FilterPattern')
        if m.get('RunOptions') is not None:
            self.run_options_shrink = m.get('RunOptions')
        if m.get('Sink') is not None:
            self.sink_shrink = m.get('Sink')
        if m.get('Source') is not None:
            self.source_shrink = m.get('Source')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        return self


class UpdateEventStreamingResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateEventStreamingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateEventStreamingResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = UpdateEventStreamingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateRuleRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        description: str = None,
        event_bus_name: str = None,
        filter_pattern: str = None,
        rule_name: str = None,
        status: str = None,
    ):
        self.client_token = client_token
        self.description = description
        self.event_bus_name = event_bus_name
        self.filter_pattern = filter_pattern
        self.rule_name = rule_name
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name
        if self.filter_pattern is not None:
            result['FilterPattern'] = self.filter_pattern
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')
        if m.get('FilterPattern') is not None:
            self.filter_pattern = m.get('FilterPattern')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class UpdateRuleResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateRuleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = UpdateRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateSchemaRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        compatible_type: str = None,
        description: str = None,
        group_id: str = None,
        schema_id: str = None,
    ):
        self.client_token = client_token
        # Schema处理版本兼容性的策略
        self.compatible_type = compatible_type
        # Schema描述信息
        self.description = description
        # Schema所属注册表
        self.group_id = group_id
        # Schema标识
        self.schema_id = schema_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.compatible_type is not None:
            result['CompatibleType'] = self.compatible_type
        if self.description is not None:
            result['Description'] = self.description
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.schema_id is not None:
            result['SchemaId'] = self.schema_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('CompatibleType') is not None:
            self.compatible_type = m.get('CompatibleType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('SchemaId') is not None:
            self.schema_id = m.get('SchemaId')
        return self


class UpdateSchemaResponseBodyData(TeaModel):
    def __init__(
        self,
        created_timestamp: int = None,
        group_arn: str = None,
    ):
        self.created_timestamp = created_timestamp
        self.group_arn = group_arn

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_timestamp is not None:
            result['CreatedTimestamp'] = self.created_timestamp
        if self.group_arn is not None:
            result['GroupARN'] = self.group_arn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedTimestamp') is not None:
            self.created_timestamp = m.get('CreatedTimestamp')
        if m.get('GroupARN') is not None:
            self.group_arn = m.get('GroupARN')
        return self


class UpdateSchemaResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: UpdateSchemaResponseBodyData = None,
        http_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_code = http_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = UpdateSchemaResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateSchemaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateSchemaResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = UpdateSchemaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateSchemaGroupRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        description: str = None,
        group_id: str = None,
    ):
        self.client_token = client_token
        # 代表分组内Schema的格式类型
        self.description = description
        # 代表资源一级ID的资源属性字段
        self.group_id = group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        return self


class UpdateSchemaGroupResponseBodyData(TeaModel):
    def __init__(
        self,
        updated_timestamp: int = None,
    ):
        self.updated_timestamp = updated_timestamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.updated_timestamp is not None:
            result['UpdatedTimestamp'] = self.updated_timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UpdatedTimestamp') is not None:
            self.updated_timestamp = m.get('UpdatedTimestamp')
        return self


class UpdateSchemaGroupResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: UpdateSchemaGroupResponseBodyData = None,
        http_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_code = http_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = UpdateSchemaGroupResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateSchemaGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateSchemaGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = UpdateSchemaGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateSchemaVersionRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        group_id: str = None,
        schema_id: str = None,
        version_number: str = None,
    ):
        self.client_token = client_token
        self.group_id = group_id
        self.schema_id = schema_id
        self.version_number = version_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.schema_id is not None:
            result['SchemaId'] = self.schema_id
        if self.version_number is not None:
            result['VersionNumber'] = self.version_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('SchemaId') is not None:
            self.schema_id = m.get('SchemaId')
        if m.get('VersionNumber') is not None:
            self.version_number = m.get('VersionNumber')
        return self


class UpdateSchemaVersionResponseBodyData(TeaModel):
    def __init__(
        self,
        schema_version_arn: str = None,
        updated_timestamp: int = None,
    ):
        self.schema_version_arn = schema_version_arn
        self.updated_timestamp = updated_timestamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.schema_version_arn is not None:
            result['SchemaVersionARN'] = self.schema_version_arn
        if self.updated_timestamp is not None:
            result['UpdatedTimestamp'] = self.updated_timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SchemaVersionARN') is not None:
            self.schema_version_arn = m.get('SchemaVersionARN')
        if m.get('UpdatedTimestamp') is not None:
            self.updated_timestamp = m.get('UpdatedTimestamp')
        return self


class UpdateSchemaVersionResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: UpdateSchemaVersionResponseBodyData = None,
        http_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_code = http_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = UpdateSchemaVersionResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateSchemaVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateSchemaVersionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = UpdateSchemaVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateTargetsRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        event_bus_name: str = None,
        rule_name: str = None,
        targets: Dict[str, Any] = None,
    ):
        self.client_token = client_token
        self.event_bus_name = event_bus_name
        self.rule_name = rule_name
        self.targets = targets

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.targets is not None:
            result['Targets'] = self.targets
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('Targets') is not None:
            self.targets = m.get('Targets')
        return self


class UpdateTargetsShrinkRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        event_bus_name: str = None,
        rule_name: str = None,
        targets_shrink: str = None,
    ):
        self.client_token = client_token
        self.event_bus_name = event_bus_name
        self.rule_name = rule_name
        self.targets_shrink = targets_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.targets_shrink is not None:
            result['Targets'] = self.targets_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('Targets') is not None:
            self.targets_shrink = m.get('Targets')
        return self


class UpdateTargetsResponseBodyDataErrorEntries(TeaModel):
    def __init__(
        self,
        entry_id: str = None,
        error_code: str = None,
        error_message: str = None,
    ):
        self.entry_id = entry_id
        self.error_code = error_code
        self.error_message = error_message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entry_id is not None:
            result['EntryId'] = self.entry_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EntryId') is not None:
            self.entry_id = m.get('EntryId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        return self


class UpdateTargetsResponseBodyData(TeaModel):
    def __init__(
        self,
        error_entries: List[UpdateTargetsResponseBodyDataErrorEntries] = None,
        error_entries_count: int = None,
    ):
        self.error_entries = error_entries
        self.error_entries_count = error_entries_count

    def validate(self):
        if self.error_entries:
            for k in self.error_entries:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ErrorEntries'] = []
        if self.error_entries is not None:
            for k in self.error_entries:
                result['ErrorEntries'].append(k.to_map() if k else None)
        if self.error_entries_count is not None:
            result['ErrorEntriesCount'] = self.error_entries_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.error_entries = []
        if m.get('ErrorEntries') is not None:
            for k in m.get('ErrorEntries'):
                temp_model = UpdateTargetsResponseBodyDataErrorEntries()
                self.error_entries.append(temp_model.from_map(k))
        if m.get('ErrorEntriesCount') is not None:
            self.error_entries_count = m.get('ErrorEntriesCount')
        return self


class UpdateTargetsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: UpdateTargetsResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = UpdateTargetsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateTargetsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateTargetsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = UpdateTargetsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class VerifyRequest(TeaModel):
    def __init__(
        self,
        data: str = None,
    ):
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class VerifyResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        synchro: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success
        self.synchro = synchro

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.synchro is not None:
            result['Synchro'] = self.synchro
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Synchro') is not None:
            self.synchro = m.get('Synchro')
        return self


class VerifyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: VerifyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = VerifyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


