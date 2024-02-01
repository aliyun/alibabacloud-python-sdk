# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, Any, List


class AddEventRecordPlanDeviceRequest(TeaModel):
    def __init__(
        self,
        device_name: str = None,
        iot_id: str = None,
        iot_instance_id: str = None,
        plan_id: str = None,
        product_key: str = None,
        stream_type: int = None,
    ):
        self.device_name = device_name
        self.iot_id = iot_id
        self.iot_instance_id = iot_instance_id
        self.plan_id = plan_id
        self.product_key = product_key
        self.stream_type = stream_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        if self.stream_type is not None:
            result['StreamType'] = self.stream_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        if m.get('StreamType') is not None:
            self.stream_type = m.get('StreamType')
        return self


class AddEventRecordPlanDeviceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.error_message = error_message
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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddEventRecordPlanDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddEventRecordPlanDeviceResponseBody = None,
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
            temp_model = AddEventRecordPlanDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddFaceDeviceGroupRequest(TeaModel):
    def __init__(
        self,
        device_group_name: str = None,
        isolation_id: str = None,
    ):
        self.device_group_name = device_group_name
        self.isolation_id = isolation_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_group_name is not None:
            result['DeviceGroupName'] = self.device_group_name
        if self.isolation_id is not None:
            result['IsolationId'] = self.isolation_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceGroupName') is not None:
            self.device_group_name = m.get('DeviceGroupName')
        if m.get('IsolationId') is not None:
            self.isolation_id = m.get('IsolationId')
        return self


class AddFaceDeviceGroupResponseBodyData(TeaModel):
    def __init__(
        self,
        device_group_id: str = None,
        device_group_name: str = None,
        modified_time: str = None,
    ):
        self.device_group_id = device_group_id
        self.device_group_name = device_group_name
        self.modified_time = modified_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_group_id is not None:
            result['DeviceGroupId'] = self.device_group_id
        if self.device_group_name is not None:
            result['DeviceGroupName'] = self.device_group_name
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceGroupId') is not None:
            self.device_group_id = m.get('DeviceGroupId')
        if m.get('DeviceGroupName') is not None:
            self.device_group_name = m.get('DeviceGroupName')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        return self


class AddFaceDeviceGroupResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: AddFaceDeviceGroupResponseBodyData = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_message = error_message
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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = AddFaceDeviceGroupResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddFaceDeviceGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddFaceDeviceGroupResponseBody = None,
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
            temp_model = AddFaceDeviceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddFaceDeviceToDeviceGroupRequest(TeaModel):
    def __init__(
        self,
        device_group_id: str = None,
        device_name: str = None,
        iot_instance_id: str = None,
        isolation_id: str = None,
        product_key: str = None,
    ):
        self.device_group_id = device_group_id
        self.device_name = device_name
        self.iot_instance_id = iot_instance_id
        self.isolation_id = isolation_id
        self.product_key = product_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_group_id is not None:
            result['DeviceGroupId'] = self.device_group_id
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.isolation_id is not None:
            result['IsolationId'] = self.isolation_id
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceGroupId') is not None:
            self.device_group_id = m.get('DeviceGroupId')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('IsolationId') is not None:
            self.isolation_id = m.get('IsolationId')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        return self


class AddFaceDeviceToDeviceGroupResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.error_message = error_message
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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddFaceDeviceToDeviceGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddFaceDeviceToDeviceGroupResponseBody = None,
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
            temp_model = AddFaceDeviceToDeviceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddFaceUserRequest(TeaModel):
    def __init__(
        self,
        custom_user_id: str = None,
        face_pic_url: str = None,
        isolation_id: str = None,
        name: str = None,
        params: str = None,
    ):
        self.custom_user_id = custom_user_id
        self.face_pic_url = face_pic_url
        self.isolation_id = isolation_id
        self.name = name
        self.params = params

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_user_id is not None:
            result['CustomUserId'] = self.custom_user_id
        if self.face_pic_url is not None:
            result['FacePicUrl'] = self.face_pic_url
        if self.isolation_id is not None:
            result['IsolationId'] = self.isolation_id
        if self.name is not None:
            result['Name'] = self.name
        if self.params is not None:
            result['Params'] = self.params
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomUserId') is not None:
            self.custom_user_id = m.get('CustomUserId')
        if m.get('FacePicUrl') is not None:
            self.face_pic_url = m.get('FacePicUrl')
        if m.get('IsolationId') is not None:
            self.isolation_id = m.get('IsolationId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Params') is not None:
            self.params = m.get('Params')
        return self


class AddFaceUserResponseBodyData(TeaModel):
    def __init__(
        self,
        custom_user_id: str = None,
        name: str = None,
        params: str = None,
        user_id: str = None,
    ):
        self.custom_user_id = custom_user_id
        self.name = name
        self.params = params
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_user_id is not None:
            result['CustomUserId'] = self.custom_user_id
        if self.name is not None:
            result['Name'] = self.name
        if self.params is not None:
            result['Params'] = self.params
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomUserId') is not None:
            self.custom_user_id = m.get('CustomUserId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Params') is not None:
            self.params = m.get('Params')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class AddFaceUserResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: AddFaceUserResponseBodyData = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_message = error_message
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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = AddFaceUserResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddFaceUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddFaceUserResponseBody = None,
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
            temp_model = AddFaceUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddFaceUserGroupRequest(TeaModel):
    def __init__(
        self,
        isolation_id: str = None,
        user_group_name: str = None,
    ):
        self.isolation_id = isolation_id
        self.user_group_name = user_group_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.isolation_id is not None:
            result['IsolationId'] = self.isolation_id
        if self.user_group_name is not None:
            result['UserGroupName'] = self.user_group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsolationId') is not None:
            self.isolation_id = m.get('IsolationId')
        if m.get('UserGroupName') is not None:
            self.user_group_name = m.get('UserGroupName')
        return self


class AddFaceUserGroupResponseBodyData(TeaModel):
    def __init__(
        self,
        modified_time: str = None,
        user_group_id: str = None,
        user_group_name: str = None,
    ):
        self.modified_time = modified_time
        self.user_group_id = user_group_id
        self.user_group_name = user_group_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        if self.user_group_name is not None:
            result['UserGroupName'] = self.user_group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        if m.get('UserGroupName') is not None:
            self.user_group_name = m.get('UserGroupName')
        return self


class AddFaceUserGroupResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: AddFaceUserGroupResponseBodyData = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_message = error_message
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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = AddFaceUserGroupResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddFaceUserGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddFaceUserGroupResponseBody = None,
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
            temp_model = AddFaceUserGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddFaceUserGroupAndDeviceGroupRelationRequest(TeaModel):
    def __init__(
        self,
        device_group_id: str = None,
        iot_instance_id: str = None,
        isolation_id: str = None,
        relation: str = None,
        user_group_id: str = None,
    ):
        self.device_group_id = device_group_id
        self.iot_instance_id = iot_instance_id
        self.isolation_id = isolation_id
        self.relation = relation
        self.user_group_id = user_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_group_id is not None:
            result['DeviceGroupId'] = self.device_group_id
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.isolation_id is not None:
            result['IsolationId'] = self.isolation_id
        if self.relation is not None:
            result['Relation'] = self.relation
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceGroupId') is not None:
            self.device_group_id = m.get('DeviceGroupId')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('IsolationId') is not None:
            self.isolation_id = m.get('IsolationId')
        if m.get('Relation') is not None:
            self.relation = m.get('Relation')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        return self


class AddFaceUserGroupAndDeviceGroupRelationResponseBodyData(TeaModel):
    def __init__(
        self,
        control_id: str = None,
        modified_time: str = None,
    ):
        self.control_id = control_id
        self.modified_time = modified_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.control_id is not None:
            result['ControlId'] = self.control_id
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ControlId') is not None:
            self.control_id = m.get('ControlId')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        return self


class AddFaceUserGroupAndDeviceGroupRelationResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: AddFaceUserGroupAndDeviceGroupRelationResponseBodyData = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_message = error_message
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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = AddFaceUserGroupAndDeviceGroupRelationResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddFaceUserGroupAndDeviceGroupRelationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddFaceUserGroupAndDeviceGroupRelationResponseBody = None,
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
            temp_model = AddFaceUserGroupAndDeviceGroupRelationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddFaceUserPictureRequest(TeaModel):
    def __init__(
        self,
        face_pic_url: str = None,
        isolation_id: str = None,
        user_id: str = None,
    ):
        self.face_pic_url = face_pic_url
        self.isolation_id = isolation_id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.face_pic_url is not None:
            result['FacePicUrl'] = self.face_pic_url
        if self.isolation_id is not None:
            result['IsolationId'] = self.isolation_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FacePicUrl') is not None:
            self.face_pic_url = m.get('FacePicUrl')
        if m.get('IsolationId') is not None:
            self.isolation_id = m.get('IsolationId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class AddFaceUserPictureResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: Dict[str, Any] = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_message = error_message
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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddFaceUserPictureResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddFaceUserPictureResponseBody = None,
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
            temp_model = AddFaceUserPictureResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddFaceUserToUserGroupRequest(TeaModel):
    def __init__(
        self,
        isolation_id: str = None,
        user_group_id: str = None,
        user_id: str = None,
    ):
        self.isolation_id = isolation_id
        self.user_group_id = user_group_id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.isolation_id is not None:
            result['IsolationId'] = self.isolation_id
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsolationId') is not None:
            self.isolation_id = m.get('IsolationId')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class AddFaceUserToUserGroupResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.error_message = error_message
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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddFaceUserToUserGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddFaceUserToUserGroupResponseBody = None,
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
            temp_model = AddFaceUserToUserGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddRecordPlanDeviceRequest(TeaModel):
    def __init__(
        self,
        device_name: str = None,
        iot_id: str = None,
        iot_instance_id: str = None,
        plan_id: str = None,
        product_key: str = None,
        stream_type: int = None,
    ):
        self.device_name = device_name
        self.iot_id = iot_id
        self.iot_instance_id = iot_instance_id
        self.plan_id = plan_id
        self.product_key = product_key
        self.stream_type = stream_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        if self.stream_type is not None:
            result['StreamType'] = self.stream_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        if m.get('StreamType') is not None:
            self.stream_type = m.get('StreamType')
        return self


class AddRecordPlanDeviceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.error_message = error_message
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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddRecordPlanDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddRecordPlanDeviceResponseBody = None,
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
            temp_model = AddRecordPlanDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchQueryVisionDeviceInfoRequest(TeaModel):
    def __init__(
        self,
        device_name_list: List[str] = None,
        iot_id_list: List[str] = None,
        iot_instance_id: str = None,
        product_key: str = None,
    ):
        self.device_name_list = device_name_list
        self.iot_id_list = iot_id_list
        self.iot_instance_id = iot_instance_id
        self.product_key = product_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name_list is not None:
            result['DeviceNameList'] = self.device_name_list
        if self.iot_id_list is not None:
            result['IotIdList'] = self.iot_id_list
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceNameList') is not None:
            self.device_name_list = m.get('DeviceNameList')
        if m.get('IotIdList') is not None:
            self.iot_id_list = m.get('IotIdList')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        return self


class BatchQueryVisionDeviceInfoResponseBodyDataDeviceInfoListGbDeviceInfo(TeaModel):
    def __init__(
        self,
        device_protocol: int = None,
        gb_id: str = None,
        net_protocol: int = None,
        nick_name: str = None,
        password: str = None,
        sub_product_key: str = None,
    ):
        self.device_protocol = device_protocol
        self.gb_id = gb_id
        self.net_protocol = net_protocol
        self.nick_name = nick_name
        self.password = password
        self.sub_product_key = sub_product_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_protocol is not None:
            result['DeviceProtocol'] = self.device_protocol
        if self.gb_id is not None:
            result['GbId'] = self.gb_id
        if self.net_protocol is not None:
            result['NetProtocol'] = self.net_protocol
        if self.nick_name is not None:
            result['NickName'] = self.nick_name
        if self.password is not None:
            result['Password'] = self.password
        if self.sub_product_key is not None:
            result['SubProductKey'] = self.sub_product_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceProtocol') is not None:
            self.device_protocol = m.get('DeviceProtocol')
        if m.get('GbId') is not None:
            self.gb_id = m.get('GbId')
        if m.get('NetProtocol') is not None:
            self.net_protocol = m.get('NetProtocol')
        if m.get('NickName') is not None:
            self.nick_name = m.get('NickName')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('SubProductKey') is not None:
            self.sub_product_key = m.get('SubProductKey')
        return self


class BatchQueryVisionDeviceInfoResponseBodyDataDeviceInfoListRtmpDeviceInfo(TeaModel):
    def __init__(
        self,
        pull_auth_key: str = None,
        pull_key_expire_time: int = None,
        push_auth_key: str = None,
        push_key_expire_time: int = None,
        push_url_sample: str = None,
        stream_name: str = None,
        stream_status: int = None,
    ):
        self.pull_auth_key = pull_auth_key
        self.pull_key_expire_time = pull_key_expire_time
        self.push_auth_key = push_auth_key
        self.push_key_expire_time = push_key_expire_time
        self.push_url_sample = push_url_sample
        self.stream_name = stream_name
        self.stream_status = stream_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pull_auth_key is not None:
            result['PullAuthKey'] = self.pull_auth_key
        if self.pull_key_expire_time is not None:
            result['PullKeyExpireTime'] = self.pull_key_expire_time
        if self.push_auth_key is not None:
            result['PushAuthKey'] = self.push_auth_key
        if self.push_key_expire_time is not None:
            result['PushKeyExpireTime'] = self.push_key_expire_time
        if self.push_url_sample is not None:
            result['PushUrlSample'] = self.push_url_sample
        if self.stream_name is not None:
            result['StreamName'] = self.stream_name
        if self.stream_status is not None:
            result['StreamStatus'] = self.stream_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PullAuthKey') is not None:
            self.pull_auth_key = m.get('PullAuthKey')
        if m.get('PullKeyExpireTime') is not None:
            self.pull_key_expire_time = m.get('PullKeyExpireTime')
        if m.get('PushAuthKey') is not None:
            self.push_auth_key = m.get('PushAuthKey')
        if m.get('PushKeyExpireTime') is not None:
            self.push_key_expire_time = m.get('PushKeyExpireTime')
        if m.get('PushUrlSample') is not None:
            self.push_url_sample = m.get('PushUrlSample')
        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')
        if m.get('StreamStatus') is not None:
            self.stream_status = m.get('StreamStatus')
        return self


class BatchQueryVisionDeviceInfoResponseBodyDataDeviceInfoList(TeaModel):
    def __init__(
        self,
        description: str = None,
        device_type: int = None,
        gb_device_info: BatchQueryVisionDeviceInfoResponseBodyDataDeviceInfoListGbDeviceInfo = None,
        iot_id: str = None,
        rtmp_device_info: BatchQueryVisionDeviceInfoResponseBodyDataDeviceInfoListRtmpDeviceInfo = None,
    ):
        self.description = description
        self.device_type = device_type
        self.gb_device_info = gb_device_info
        self.iot_id = iot_id
        self.rtmp_device_info = rtmp_device_info

    def validate(self):
        if self.gb_device_info:
            self.gb_device_info.validate()
        if self.rtmp_device_info:
            self.rtmp_device_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.device_type is not None:
            result['DeviceType'] = self.device_type
        if self.gb_device_info is not None:
            result['GbDeviceInfo'] = self.gb_device_info.to_map()
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.rtmp_device_info is not None:
            result['RtmpDeviceInfo'] = self.rtmp_device_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DeviceType') is not None:
            self.device_type = m.get('DeviceType')
        if m.get('GbDeviceInfo') is not None:
            temp_model = BatchQueryVisionDeviceInfoResponseBodyDataDeviceInfoListGbDeviceInfo()
            self.gb_device_info = temp_model.from_map(m['GbDeviceInfo'])
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('RtmpDeviceInfo') is not None:
            temp_model = BatchQueryVisionDeviceInfoResponseBodyDataDeviceInfoListRtmpDeviceInfo()
            self.rtmp_device_info = temp_model.from_map(m['RtmpDeviceInfo'])
        return self


class BatchQueryVisionDeviceInfoResponseBodyData(TeaModel):
    def __init__(
        self,
        device_info_list: List[BatchQueryVisionDeviceInfoResponseBodyDataDeviceInfoList] = None,
    ):
        self.device_info_list = device_info_list

    def validate(self):
        if self.device_info_list:
            for k in self.device_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DeviceInfoList'] = []
        if self.device_info_list is not None:
            for k in self.device_info_list:
                result['DeviceInfoList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.device_info_list = []
        if m.get('DeviceInfoList') is not None:
            for k in m.get('DeviceInfoList'):
                temp_model = BatchQueryVisionDeviceInfoResponseBodyDataDeviceInfoList()
                self.device_info_list.append(temp_model.from_map(k))
        return self


class BatchQueryVisionDeviceInfoResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: BatchQueryVisionDeviceInfoResponseBodyData = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_message = error_message
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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = BatchQueryVisionDeviceInfoResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class BatchQueryVisionDeviceInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BatchQueryVisionDeviceInfoResponseBody = None,
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
            temp_model = BatchQueryVisionDeviceInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BindPictureSearchAppWithDevicesRequest(TeaModel):
    def __init__(
        self,
        app_instance_id: str = None,
        device_iot_ids: List[str] = None,
        iot_instance_id: str = None,
    ):
        self.app_instance_id = app_instance_id
        self.device_iot_ids = device_iot_ids
        self.iot_instance_id = iot_instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_id is not None:
            result['AppInstanceId'] = self.app_instance_id
        if self.device_iot_ids is not None:
            result['DeviceIotIds'] = self.device_iot_ids
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceId') is not None:
            self.app_instance_id = m.get('AppInstanceId')
        if m.get('DeviceIotIds') is not None:
            self.device_iot_ids = m.get('DeviceIotIds')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        return self


class BindPictureSearchAppWithDevicesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.error_message = error_message
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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class BindPictureSearchAppWithDevicesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BindPictureSearchAppWithDevicesResponseBody = None,
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
            temp_model = BindPictureSearchAppWithDevicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckFaceUserDoExistOnDeviceRequest(TeaModel):
    def __init__(
        self,
        device_name: str = None,
        iot_instance_id: str = None,
        isolation_id: str = None,
        product_key: str = None,
        user_id: str = None,
    ):
        self.device_name = device_name
        self.iot_instance_id = iot_instance_id
        self.isolation_id = isolation_id
        self.product_key = product_key
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.isolation_id is not None:
            result['IsolationId'] = self.isolation_id
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('IsolationId') is not None:
            self.isolation_id = m.get('IsolationId')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class CheckFaceUserDoExistOnDeviceResponseBodyData(TeaModel):
    def __init__(
        self,
        do_exist: bool = None,
    ):
        self.do_exist = do_exist

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.do_exist is not None:
            result['DoExist'] = self.do_exist
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DoExist') is not None:
            self.do_exist = m.get('DoExist')
        return self


class CheckFaceUserDoExistOnDeviceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CheckFaceUserDoExistOnDeviceResponseBodyData = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_message = error_message
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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = CheckFaceUserDoExistOnDeviceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CheckFaceUserDoExistOnDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CheckFaceUserDoExistOnDeviceResponseBody = None,
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
            temp_model = CheckFaceUserDoExistOnDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ClearFaceDeviceDBRequest(TeaModel):
    def __init__(
        self,
        device_name: str = None,
        iot_instance_id: str = None,
        isolation_id: str = None,
        product_key: str = None,
    ):
        self.device_name = device_name
        self.iot_instance_id = iot_instance_id
        self.isolation_id = isolation_id
        self.product_key = product_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.isolation_id is not None:
            result['IsolationId'] = self.isolation_id
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('IsolationId') is not None:
            self.isolation_id = m.get('IsolationId')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        return self


class ClearFaceDeviceDBResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: Dict[str, Any] = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_message = error_message
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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ClearFaceDeviceDBResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ClearFaceDeviceDBResponseBody = None,
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
            temp_model = ClearFaceDeviceDBResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateEventRecordPlanRequest(TeaModel):
    def __init__(
        self,
        event_types: str = None,
        name: str = None,
        pre_record_duration: int = None,
        record_duration: int = None,
        template_id: str = None,
    ):
        self.event_types = event_types
        self.name = name
        self.pre_record_duration = pre_record_duration
        self.record_duration = record_duration
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_types is not None:
            result['EventTypes'] = self.event_types
        if self.name is not None:
            result['Name'] = self.name
        if self.pre_record_duration is not None:
            result['PreRecordDuration'] = self.pre_record_duration
        if self.record_duration is not None:
            result['RecordDuration'] = self.record_duration
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventTypes') is not None:
            self.event_types = m.get('EventTypes')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PreRecordDuration') is not None:
            self.pre_record_duration = m.get('PreRecordDuration')
        if m.get('RecordDuration') is not None:
            self.record_duration = m.get('RecordDuration')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class CreateEventRecordPlanResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_message = error_message
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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateEventRecordPlanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateEventRecordPlanResponseBody = None,
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
            temp_model = CreateEventRecordPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateGbDeviceRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        device_name: str = None,
        device_type: int = None,
        gb_id: str = None,
        iot_instance_id: str = None,
        media_net_protocol: str = None,
        password: str = None,
        product_key: str = None,
        sub_product_key: str = None,
    ):
        self.description = description
        self.device_name = device_name
        self.device_type = device_type
        self.gb_id = gb_id
        self.iot_instance_id = iot_instance_id
        self.media_net_protocol = media_net_protocol
        self.password = password
        self.product_key = product_key
        self.sub_product_key = sub_product_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.device_type is not None:
            result['DeviceType'] = self.device_type
        if self.gb_id is not None:
            result['GbId'] = self.gb_id
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.media_net_protocol is not None:
            result['MediaNetProtocol'] = self.media_net_protocol
        if self.password is not None:
            result['Password'] = self.password
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        if self.sub_product_key is not None:
            result['SubProductKey'] = self.sub_product_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('DeviceType') is not None:
            self.device_type = m.get('DeviceType')
        if m.get('GbId') is not None:
            self.gb_id = m.get('GbId')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('MediaNetProtocol') is not None:
            self.media_net_protocol = m.get('MediaNetProtocol')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        if m.get('SubProductKey') is not None:
            self.sub_product_key = m.get('SubProductKey')
        return self


class CreateGbDeviceResponseBodyData(TeaModel):
    def __init__(
        self,
        device_name: str = None,
        iot_id: str = None,
    ):
        self.device_name = device_name
        self.iot_id = iot_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        return self


class CreateGbDeviceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CreateGbDeviceResponseBodyData = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_message = error_message
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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = CreateGbDeviceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateGbDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateGbDeviceResponseBody = None,
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
            temp_model = CreateGbDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateLocalFileUploadJobRequestTimeSlot(TeaModel):
    def __init__(
        self,
        device_name: str = None,
        end_time: int = None,
        iot_id: str = None,
        product_key: str = None,
        start_time: int = None,
    ):
        self.device_name = device_name
        self.end_time = end_time
        self.iot_id = iot_id
        self.product_key = product_key
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class CreateLocalFileUploadJobRequest(TeaModel):
    def __init__(
        self,
        iot_instance_id: str = None,
        time_slot: List[CreateLocalFileUploadJobRequestTimeSlot] = None,
    ):
        self.iot_instance_id = iot_instance_id
        self.time_slot = time_slot

    def validate(self):
        if self.time_slot:
            for k in self.time_slot:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        result['TimeSlot'] = []
        if self.time_slot is not None:
            for k in self.time_slot:
                result['TimeSlot'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        self.time_slot = []
        if m.get('TimeSlot') is not None:
            for k in m.get('TimeSlot'):
                temp_model = CreateLocalFileUploadJobRequestTimeSlot()
                self.time_slot.append(temp_model.from_map(k))
        return self


class CreateLocalFileUploadJobResponseBodyData(TeaModel):
    def __init__(
        self,
        job_id: str = None,
    ):
        self.job_id = job_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class CreateLocalFileUploadJobResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CreateLocalFileUploadJobResponseBodyData = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_message = error_message
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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = CreateLocalFileUploadJobResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateLocalFileUploadJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateLocalFileUploadJobResponseBody = None,
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
            temp_model = CreateLocalFileUploadJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateLocalRecordDownloadByTimeJobRequest(TeaModel):
    def __init__(
        self,
        begin_time: int = None,
        device_name: str = None,
        end_time: int = None,
        iot_id: str = None,
        iot_instance_id: str = None,
        product_key: str = None,
        speed: float = None,
    ):
        self.begin_time = begin_time
        self.device_name = device_name
        self.end_time = end_time
        self.iot_id = iot_id
        self.iot_instance_id = iot_instance_id
        self.product_key = product_key
        self.speed = speed

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        if self.speed is not None:
            result['Speed'] = self.speed
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        if m.get('Speed') is not None:
            self.speed = m.get('Speed')
        return self


class CreateLocalRecordDownloadByTimeJobResponseBodyData(TeaModel):
    def __init__(
        self,
        job_id: str = None,
    ):
        self.job_id = job_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class CreateLocalRecordDownloadByTimeJobResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CreateLocalRecordDownloadByTimeJobResponseBodyData = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_message = error_message
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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = CreateLocalRecordDownloadByTimeJobResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateLocalRecordDownloadByTimeJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateLocalRecordDownloadByTimeJobResponseBody = None,
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
            temp_model = CreateLocalRecordDownloadByTimeJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePictureSearchAppRequest(TeaModel):
    def __init__(
        self,
        desc: str = None,
        iot_instance_id: str = None,
        name: str = None,
    ):
        self.desc = desc
        self.iot_instance_id = iot_instance_id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desc is not None:
            result['Desc'] = self.desc
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class CreatePictureSearchAppResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_message = error_message
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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreatePictureSearchAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreatePictureSearchAppResponseBody = None,
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
            temp_model = CreatePictureSearchAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePictureSearchJobRequest(TeaModel):
    def __init__(
        self,
        app_instance_id: str = None,
        body_threshold: float = None,
        end_time: int = None,
        picture_search_type: int = None,
        search_pic_url: str = None,
        start_time: int = None,
        threshold: float = None,
    ):
        self.app_instance_id = app_instance_id
        self.body_threshold = body_threshold
        self.end_time = end_time
        self.picture_search_type = picture_search_type
        self.search_pic_url = search_pic_url
        self.start_time = start_time
        self.threshold = threshold

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_id is not None:
            result['AppInstanceId'] = self.app_instance_id
        if self.body_threshold is not None:
            result['BodyThreshold'] = self.body_threshold
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.picture_search_type is not None:
            result['PictureSearchType'] = self.picture_search_type
        if self.search_pic_url is not None:
            result['SearchPicUrl'] = self.search_pic_url
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceId') is not None:
            self.app_instance_id = m.get('AppInstanceId')
        if m.get('BodyThreshold') is not None:
            self.body_threshold = m.get('BodyThreshold')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PictureSearchType') is not None:
            self.picture_search_type = m.get('PictureSearchType')
        if m.get('SearchPicUrl') is not None:
            self.search_pic_url = m.get('SearchPicUrl')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        return self


class CreatePictureSearchJobResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_message = error_message
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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreatePictureSearchJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreatePictureSearchJobResponseBody = None,
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
            temp_model = CreatePictureSearchJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRecordDownloadByTimeJobRequest(TeaModel):
    def __init__(
        self,
        begin_time: int = None,
        device_name: str = None,
        end_time: int = None,
        iot_id: str = None,
        iot_instance_id: str = None,
        product_key: str = None,
        record_type: int = None,
        stream_type: int = None,
    ):
        self.begin_time = begin_time
        self.device_name = device_name
        self.end_time = end_time
        self.iot_id = iot_id
        self.iot_instance_id = iot_instance_id
        self.product_key = product_key
        self.record_type = record_type
        self.stream_type = stream_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        if self.record_type is not None:
            result['RecordType'] = self.record_type
        if self.stream_type is not None:
            result['StreamType'] = self.stream_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        if m.get('RecordType') is not None:
            self.record_type = m.get('RecordType')
        if m.get('StreamType') is not None:
            self.stream_type = m.get('StreamType')
        return self


class CreateRecordDownloadByTimeJobResponseBodyData(TeaModel):
    def __init__(
        self,
        job_id: str = None,
    ):
        self.job_id = job_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class CreateRecordDownloadByTimeJobResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CreateRecordDownloadByTimeJobResponseBodyData = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_message = error_message
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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = CreateRecordDownloadByTimeJobResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateRecordDownloadByTimeJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateRecordDownloadByTimeJobResponseBody = None,
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
            temp_model = CreateRecordDownloadByTimeJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRecordPlanRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        template_id: str = None,
    ):
        self.name = name
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class CreateRecordPlanResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_message = error_message
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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateRecordPlanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateRecordPlanResponseBody = None,
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
            temp_model = CreateRecordPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRtmpDeviceRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        device_name: str = None,
        iot_instance_id: str = None,
        product_key: str = None,
        pull_auth_key: str = None,
        pull_key_expire_time: int = None,
        push_auth_key: str = None,
        push_key_expire_time: int = None,
        sub_stream_name: str = None,
    ):
        self.description = description
        self.device_name = device_name
        self.iot_instance_id = iot_instance_id
        self.product_key = product_key
        self.pull_auth_key = pull_auth_key
        self.pull_key_expire_time = pull_key_expire_time
        self.push_auth_key = push_auth_key
        self.push_key_expire_time = push_key_expire_time
        self.sub_stream_name = sub_stream_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        if self.pull_auth_key is not None:
            result['PullAuthKey'] = self.pull_auth_key
        if self.pull_key_expire_time is not None:
            result['PullKeyExpireTime'] = self.pull_key_expire_time
        if self.push_auth_key is not None:
            result['PushAuthKey'] = self.push_auth_key
        if self.push_key_expire_time is not None:
            result['PushKeyExpireTime'] = self.push_key_expire_time
        if self.sub_stream_name is not None:
            result['SubStreamName'] = self.sub_stream_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        if m.get('PullAuthKey') is not None:
            self.pull_auth_key = m.get('PullAuthKey')
        if m.get('PullKeyExpireTime') is not None:
            self.pull_key_expire_time = m.get('PullKeyExpireTime')
        if m.get('PushAuthKey') is not None:
            self.push_auth_key = m.get('PushAuthKey')
        if m.get('PushKeyExpireTime') is not None:
            self.push_key_expire_time = m.get('PushKeyExpireTime')
        if m.get('SubStreamName') is not None:
            self.sub_stream_name = m.get('SubStreamName')
        return self


class CreateRtmpDeviceResponseBodyData(TeaModel):
    def __init__(
        self,
        device_name: str = None,
        iot_id: str = None,
        stream_name: str = None,
    ):
        self.device_name = device_name
        self.iot_id = iot_id
        self.stream_name = stream_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.stream_name is not None:
            result['StreamName'] = self.stream_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')
        return self


class CreateRtmpDeviceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CreateRtmpDeviceResponseBodyData = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_message = error_message
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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = CreateRtmpDeviceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateRtmpDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateRtmpDeviceResponseBody = None,
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
            temp_model = CreateRtmpDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateStreamPushJobRequest(TeaModel):
    def __init__(
        self,
        device_name: str = None,
        iot_id: str = None,
        iot_instance_id: str = None,
        job_type: int = None,
        product_key: str = None,
        push_url: str = None,
        stream_type: int = None,
    ):
        self.device_name = device_name
        self.iot_id = iot_id
        self.iot_instance_id = iot_instance_id
        self.job_type = job_type
        self.product_key = product_key
        self.push_url = push_url
        self.stream_type = stream_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.job_type is not None:
            result['JobType'] = self.job_type
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        if self.push_url is not None:
            result['PushUrl'] = self.push_url
        if self.stream_type is not None:
            result['StreamType'] = self.stream_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        if m.get('PushUrl') is not None:
            self.push_url = m.get('PushUrl')
        if m.get('StreamType') is not None:
            self.stream_type = m.get('StreamType')
        return self


class CreateStreamPushJobResponseBodyData(TeaModel):
    def __init__(
        self,
        job_id: str = None,
    ):
        self.job_id = job_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class CreateStreamPushJobResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CreateStreamPushJobResponseBodyData = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_message = error_message
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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = CreateStreamPushJobResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateStreamPushJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateStreamPushJobResponseBody = None,
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
            temp_model = CreateStreamPushJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateStreamSnapshotJobRequest(TeaModel):
    def __init__(
        self,
        device_name: str = None,
        iot_id: str = None,
        iot_instance_id: str = None,
        product_key: str = None,
        snapshot_interval: int = None,
        stream_type: int = None,
    ):
        self.device_name = device_name
        self.iot_id = iot_id
        self.iot_instance_id = iot_instance_id
        self.product_key = product_key
        self.snapshot_interval = snapshot_interval
        self.stream_type = stream_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        if self.snapshot_interval is not None:
            result['SnapshotInterval'] = self.snapshot_interval
        if self.stream_type is not None:
            result['StreamType'] = self.stream_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        if m.get('SnapshotInterval') is not None:
            self.snapshot_interval = m.get('SnapshotInterval')
        if m.get('StreamType') is not None:
            self.stream_type = m.get('StreamType')
        return self


class CreateStreamSnapshotJobResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.error_message = error_message
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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateStreamSnapshotJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateStreamSnapshotJobResponseBody = None,
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
            temp_model = CreateStreamSnapshotJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTimeTemplateRequestTimeSections(TeaModel):
    def __init__(
        self,
        begin: int = None,
        day_of_week: int = None,
        end: int = None,
    ):
        self.begin = begin
        self.day_of_week = day_of_week
        self.end = end

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin is not None:
            result['Begin'] = self.begin
        if self.day_of_week is not None:
            result['DayOfWeek'] = self.day_of_week
        if self.end is not None:
            result['End'] = self.end
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Begin') is not None:
            self.begin = m.get('Begin')
        if m.get('DayOfWeek') is not None:
            self.day_of_week = m.get('DayOfWeek')
        if m.get('End') is not None:
            self.end = m.get('End')
        return self


class CreateTimeTemplateRequest(TeaModel):
    def __init__(
        self,
        all_day: int = None,
        name: str = None,
        time_sections: List[CreateTimeTemplateRequestTimeSections] = None,
    ):
        self.all_day = all_day
        self.name = name
        self.time_sections = time_sections

    def validate(self):
        if self.time_sections:
            for k in self.time_sections:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all_day is not None:
            result['AllDay'] = self.all_day
        if self.name is not None:
            result['Name'] = self.name
        result['TimeSections'] = []
        if self.time_sections is not None:
            for k in self.time_sections:
                result['TimeSections'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllDay') is not None:
            self.all_day = m.get('AllDay')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.time_sections = []
        if m.get('TimeSections') is not None:
            for k in m.get('TimeSections'):
                temp_model = CreateTimeTemplateRequestTimeSections()
                self.time_sections.append(temp_model.from_map(k))
        return self


class CreateTimeTemplateResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_message = error_message
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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateTimeTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateTimeTemplateResponseBody = None,
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
            temp_model = CreateTimeTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteEventRecordPlanRequest(TeaModel):
    def __init__(
        self,
        plan_id: str = None,
    ):
        self.plan_id = plan_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        return self


class DeleteEventRecordPlanResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.error_message = error_message
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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteEventRecordPlanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteEventRecordPlanResponseBody = None,
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
            temp_model = DeleteEventRecordPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteEventRecordPlanDeviceRequest(TeaModel):
    def __init__(
        self,
        device_name: str = None,
        iot_id: str = None,
        iot_instance_id: str = None,
        product_key: str = None,
        stream_type: int = None,
    ):
        self.device_name = device_name
        self.iot_id = iot_id
        self.iot_instance_id = iot_instance_id
        self.product_key = product_key
        self.stream_type = stream_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        if self.stream_type is not None:
            result['StreamType'] = self.stream_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        if m.get('StreamType') is not None:
            self.stream_type = m.get('StreamType')
        return self


class DeleteEventRecordPlanDeviceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.error_message = error_message
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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteEventRecordPlanDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteEventRecordPlanDeviceResponseBody = None,
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
            temp_model = DeleteEventRecordPlanDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteFaceDeviceGroupRequest(TeaModel):
    def __init__(
        self,
        device_group_id: str = None,
        isolation_id: str = None,
    ):
        self.device_group_id = device_group_id
        self.isolation_id = isolation_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_group_id is not None:
            result['DeviceGroupId'] = self.device_group_id
        if self.isolation_id is not None:
            result['IsolationId'] = self.isolation_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceGroupId') is not None:
            self.device_group_id = m.get('DeviceGroupId')
        if m.get('IsolationId') is not None:
            self.isolation_id = m.get('IsolationId')
        return self


class DeleteFaceDeviceGroupResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.error_message = error_message
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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteFaceDeviceGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteFaceDeviceGroupResponseBody = None,
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
            temp_model = DeleteFaceDeviceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteFaceUserRequest(TeaModel):
    def __init__(
        self,
        isolation_id: str = None,
        user_id: str = None,
    ):
        self.isolation_id = isolation_id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.isolation_id is not None:
            result['IsolationId'] = self.isolation_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsolationId') is not None:
            self.isolation_id = m.get('IsolationId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class DeleteFaceUserResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.error_message = error_message
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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteFaceUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteFaceUserResponseBody = None,
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
            temp_model = DeleteFaceUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteFaceUserGroupRequest(TeaModel):
    def __init__(
        self,
        isolation_id: str = None,
        user_group_id: str = None,
    ):
        self.isolation_id = isolation_id
        self.user_group_id = user_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.isolation_id is not None:
            result['IsolationId'] = self.isolation_id
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsolationId') is not None:
            self.isolation_id = m.get('IsolationId')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        return self


class DeleteFaceUserGroupResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.error_message = error_message
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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteFaceUserGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteFaceUserGroupResponseBody = None,
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
            temp_model = DeleteFaceUserGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteFaceUserGroupAndDeviceGroupRelationRequest(TeaModel):
    def __init__(
        self,
        control_id: str = None,
        isolation_id: str = None,
    ):
        self.control_id = control_id
        self.isolation_id = isolation_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.control_id is not None:
            result['ControlId'] = self.control_id
        if self.isolation_id is not None:
            result['IsolationId'] = self.isolation_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ControlId') is not None:
            self.control_id = m.get('ControlId')
        if m.get('IsolationId') is not None:
            self.isolation_id = m.get('IsolationId')
        return self


class DeleteFaceUserGroupAndDeviceGroupRelationResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.error_message = error_message
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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteFaceUserGroupAndDeviceGroupRelationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteFaceUserGroupAndDeviceGroupRelationResponseBody = None,
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
            temp_model = DeleteFaceUserGroupAndDeviceGroupRelationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteFaceUserPictureRequest(TeaModel):
    def __init__(
        self,
        face_pic_md_5: str = None,
        isolation_id: str = None,
        user_id: str = None,
    ):
        self.face_pic_md_5 = face_pic_md_5
        self.isolation_id = isolation_id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.face_pic_md_5 is not None:
            result['FacePicMd5'] = self.face_pic_md_5
        if self.isolation_id is not None:
            result['IsolationId'] = self.isolation_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FacePicMd5') is not None:
            self.face_pic_md_5 = m.get('FacePicMd5')
        if m.get('IsolationId') is not None:
            self.isolation_id = m.get('IsolationId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class DeleteFaceUserPictureResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.error_message = error_message
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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteFaceUserPictureResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteFaceUserPictureResponseBody = None,
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
            temp_model = DeleteFaceUserPictureResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteGbDeviceRequest(TeaModel):
    def __init__(
        self,
        device_name: str = None,
        iot_id: str = None,
        iot_instance_id: str = None,
        product_key: str = None,
    ):
        self.device_name = device_name
        self.iot_id = iot_id
        self.iot_instance_id = iot_instance_id
        self.product_key = product_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        return self


class DeleteGbDeviceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.error_message = error_message
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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteGbDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteGbDeviceResponseBody = None,
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
            temp_model = DeleteGbDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteLocalFileUploadJobRequest(TeaModel):
    def __init__(
        self,
        iot_instance_id: str = None,
        job_id: str = None,
    ):
        self.iot_instance_id = iot_instance_id
        self.job_id = job_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class DeleteLocalFileUploadJobResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: Dict[str, Any] = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_message = error_message
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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteLocalFileUploadJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteLocalFileUploadJobResponseBody = None,
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
            temp_model = DeleteLocalFileUploadJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeletePictureRequest(TeaModel):
    def __init__(
        self,
        device_name: str = None,
        iot_id: str = None,
        iot_instance_id: str = None,
        picture_id_list: List[str] = None,
        product_key: str = None,
    ):
        self.device_name = device_name
        self.iot_id = iot_id
        self.iot_instance_id = iot_instance_id
        self.picture_id_list = picture_id_list
        self.product_key = product_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.picture_id_list is not None:
            result['PictureIdList'] = self.picture_id_list
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('PictureIdList') is not None:
            self.picture_id_list = m.get('PictureIdList')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        return self


class DeletePictureResponseBodyData(TeaModel):
    def __init__(
        self,
        deleted_count: int = None,
    ):
        self.deleted_count = deleted_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deleted_count is not None:
            result['DeletedCount'] = self.deleted_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeletedCount') is not None:
            self.deleted_count = m.get('DeletedCount')
        return self


class DeletePictureResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: DeletePictureResponseBodyData = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_message = error_message
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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = DeletePictureResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeletePictureResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeletePictureResponseBody = None,
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
            temp_model = DeletePictureResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRecordRequest(TeaModel):
    def __init__(
        self,
        device_name: str = None,
        file_name_list: List[str] = None,
        iot_id: str = None,
        iot_instance_id: str = None,
        product_key: str = None,
    ):
        self.device_name = device_name
        self.file_name_list = file_name_list
        self.iot_id = iot_id
        self.iot_instance_id = iot_instance_id
        self.product_key = product_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.file_name_list is not None:
            result['FileNameList'] = self.file_name_list
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('FileNameList') is not None:
            self.file_name_list = m.get('FileNameList')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        return self


class DeleteRecordResponseBodyData(TeaModel):
    def __init__(
        self,
        deleted_count: int = None,
    ):
        self.deleted_count = deleted_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deleted_count is not None:
            result['DeletedCount'] = self.deleted_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeletedCount') is not None:
            self.deleted_count = m.get('DeletedCount')
        return self


class DeleteRecordResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: DeleteRecordResponseBodyData = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_message = error_message
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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = DeleteRecordResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteRecordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteRecordResponseBody = None,
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
            temp_model = DeleteRecordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRecordPlanRequest(TeaModel):
    def __init__(
        self,
        plan_id: str = None,
    ):
        self.plan_id = plan_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        return self


class DeleteRecordPlanResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.error_message = error_message
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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteRecordPlanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteRecordPlanResponseBody = None,
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
            temp_model = DeleteRecordPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRecordPlanDeviceRequest(TeaModel):
    def __init__(
        self,
        device_name: str = None,
        iot_id: str = None,
        iot_instance_id: str = None,
        product_key: str = None,
        stream_type: int = None,
    ):
        self.device_name = device_name
        self.iot_id = iot_id
        self.iot_instance_id = iot_instance_id
        self.product_key = product_key
        self.stream_type = stream_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        if self.stream_type is not None:
            result['StreamType'] = self.stream_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        if m.get('StreamType') is not None:
            self.stream_type = m.get('StreamType')
        return self


class DeleteRecordPlanDeviceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.error_message = error_message
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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteRecordPlanDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteRecordPlanDeviceResponseBody = None,
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
            temp_model = DeleteRecordPlanDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRtmpDeviceRequest(TeaModel):
    def __init__(
        self,
        device_name: str = None,
        iot_id: str = None,
        iot_instance_id: str = None,
        product_key: str = None,
    ):
        self.device_name = device_name
        self.iot_id = iot_id
        self.iot_instance_id = iot_instance_id
        self.product_key = product_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        return self


class DeleteRtmpDeviceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.error_message = error_message
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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteRtmpDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteRtmpDeviceResponseBody = None,
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
            temp_model = DeleteRtmpDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRtmpKeyRequest(TeaModel):
    def __init__(
        self,
        device_name: str = None,
        iot_id: str = None,
        iot_instance_id: str = None,
        product_key: str = None,
        type: int = None,
    ):
        self.device_name = device_name
        self.iot_id = iot_id
        self.iot_instance_id = iot_instance_id
        self.product_key = product_key
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DeleteRtmpKeyResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.error_message = error_message
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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteRtmpKeyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteRtmpKeyResponseBody = None,
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
            temp_model = DeleteRtmpKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteStreamPushJobRequest(TeaModel):
    def __init__(
        self,
        device_name: str = None,
        iot_id: str = None,
        iot_instance_id: str = None,
        job_id: str = None,
        product_key: str = None,
    ):
        self.device_name = device_name
        self.iot_id = iot_id
        self.iot_instance_id = iot_instance_id
        self.job_id = job_id
        self.product_key = product_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        return self


class DeleteStreamPushJobResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.error_message = error_message
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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteStreamPushJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteStreamPushJobResponseBody = None,
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
            temp_model = DeleteStreamPushJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteStreamSnapshotJobRequest(TeaModel):
    def __init__(
        self,
        device_name: str = None,
        iot_id: str = None,
        iot_instance_id: str = None,
        product_key: str = None,
        stream_type: int = None,
    ):
        self.device_name = device_name
        self.iot_id = iot_id
        self.iot_instance_id = iot_instance_id
        self.product_key = product_key
        self.stream_type = stream_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        if self.stream_type is not None:
            result['StreamType'] = self.stream_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        if m.get('StreamType') is not None:
            self.stream_type = m.get('StreamType')
        return self


class DeleteStreamSnapshotJobResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.error_message = error_message
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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteStreamSnapshotJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteStreamSnapshotJobResponseBody = None,
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
            temp_model = DeleteStreamSnapshotJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTimeTemplateRequest(TeaModel):
    def __init__(
        self,
        template_id: str = None,
    ):
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class DeleteTimeTemplateResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.error_message = error_message
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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteTimeTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteTimeTemplateResponseBody = None,
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
            temp_model = DeleteTimeTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetectUserFaceByUrlRequest(TeaModel):
    def __init__(
        self,
        face_pic_url: str = None,
    ):
        self.face_pic_url = face_pic_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.face_pic_url is not None:
            result['FacePicUrl'] = self.face_pic_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FacePicUrl') is not None:
            self.face_pic_url = m.get('FacePicUrl')
        return self


class DetectUserFaceByUrlResponseBodyDataDataFaceRects(TeaModel):
    def __init__(
        self,
        face_rects_data: List[str] = None,
    ):
        self.face_rects_data = face_rects_data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.face_rects_data is not None:
            result['FaceRectsData'] = self.face_rects_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FaceRectsData') is not None:
            self.face_rects_data = m.get('FaceRectsData')
        return self


class DetectUserFaceByUrlResponseBodyDataDataLandmarks(TeaModel):
    def __init__(
        self,
        landmarks_data: List[str] = None,
    ):
        self.landmarks_data = landmarks_data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.landmarks_data is not None:
            result['LandmarksData'] = self.landmarks_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LandmarksData') is not None:
            self.landmarks_data = m.get('LandmarksData')
        return self


class DetectUserFaceByUrlResponseBodyDataData(TeaModel):
    def __init__(
        self,
        age: int = None,
        blur_score: float = None,
        face_probability: float = None,
        face_rects: DetectUserFaceByUrlResponseBodyDataDataFaceRects = None,
        gender: int = None,
        good_for_library: bool = None,
        good_for_recognition: bool = None,
        landmarks: DetectUserFaceByUrlResponseBodyDataDataLandmarks = None,
        occlusion_score: float = None,
        pose_score: float = None,
    ):
        self.age = age
        self.blur_score = blur_score
        self.face_probability = face_probability
        self.face_rects = face_rects
        self.gender = gender
        self.good_for_library = good_for_library
        self.good_for_recognition = good_for_recognition
        self.landmarks = landmarks
        self.occlusion_score = occlusion_score
        self.pose_score = pose_score

    def validate(self):
        if self.face_rects:
            self.face_rects.validate()
        if self.landmarks:
            self.landmarks.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.age is not None:
            result['Age'] = self.age
        if self.blur_score is not None:
            result['BlurScore'] = self.blur_score
        if self.face_probability is not None:
            result['FaceProbability'] = self.face_probability
        if self.face_rects is not None:
            result['FaceRects'] = self.face_rects.to_map()
        if self.gender is not None:
            result['Gender'] = self.gender
        if self.good_for_library is not None:
            result['GoodForLibrary'] = self.good_for_library
        if self.good_for_recognition is not None:
            result['GoodForRecognition'] = self.good_for_recognition
        if self.landmarks is not None:
            result['Landmarks'] = self.landmarks.to_map()
        if self.occlusion_score is not None:
            result['OcclusionScore'] = self.occlusion_score
        if self.pose_score is not None:
            result['PoseScore'] = self.pose_score
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Age') is not None:
            self.age = m.get('Age')
        if m.get('BlurScore') is not None:
            self.blur_score = m.get('BlurScore')
        if m.get('FaceProbability') is not None:
            self.face_probability = m.get('FaceProbability')
        if m.get('FaceRects') is not None:
            temp_model = DetectUserFaceByUrlResponseBodyDataDataFaceRects()
            self.face_rects = temp_model.from_map(m['FaceRects'])
        if m.get('Gender') is not None:
            self.gender = m.get('Gender')
        if m.get('GoodForLibrary') is not None:
            self.good_for_library = m.get('GoodForLibrary')
        if m.get('GoodForRecognition') is not None:
            self.good_for_recognition = m.get('GoodForRecognition')
        if m.get('Landmarks') is not None:
            temp_model = DetectUserFaceByUrlResponseBodyDataDataLandmarks()
            self.landmarks = temp_model.from_map(m['Landmarks'])
        if m.get('OcclusionScore') is not None:
            self.occlusion_score = m.get('OcclusionScore')
        if m.get('PoseScore') is not None:
            self.pose_score = m.get('PoseScore')
        return self


class DetectUserFaceByUrlResponseBodyData(TeaModel):
    def __init__(
        self,
        data: List[DetectUserFaceByUrlResponseBodyDataData] = None,
    ):
        self.data = data

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
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = DetectUserFaceByUrlResponseBodyDataData()
                self.data.append(temp_model.from_map(k))
        return self


class DetectUserFaceByUrlResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: DetectUserFaceByUrlResponseBodyData = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_message = error_message
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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = DetectUserFaceByUrlResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DetectUserFaceByUrlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DetectUserFaceByUrlResponseBody = None,
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
            temp_model = DetectUserFaceByUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableGbSubDeviceRequest(TeaModel):
    def __init__(
        self,
        device_name: str = None,
        iot_id: str = None,
        iot_instance_id: str = None,
        product_key: str = None,
        sub_device_id: str = None,
    ):
        self.device_name = device_name
        self.iot_id = iot_id
        self.iot_instance_id = iot_instance_id
        self.product_key = product_key
        self.sub_device_id = sub_device_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        if self.sub_device_id is not None:
            result['SubDeviceId'] = self.sub_device_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        if m.get('SubDeviceId') is not None:
            self.sub_device_id = m.get('SubDeviceId')
        return self


class EnableGbSubDeviceResponseBodyData(TeaModel):
    def __init__(
        self,
        device_name: str = None,
        product_key: str = None,
    ):
        self.device_name = device_name
        self.product_key = product_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        return self


class EnableGbSubDeviceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: EnableGbSubDeviceResponseBodyData = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_message = error_message
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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = EnableGbSubDeviceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class EnableGbSubDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EnableGbSubDeviceResponseBody = None,
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
            temp_model = EnableGbSubDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPictureSearchJobStatusRequest(TeaModel):
    def __init__(
        self,
        app_instance_id: str = None,
        job_id: str = None,
    ):
        self.app_instance_id = app_instance_id
        self.job_id = job_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_id is not None:
            result['AppInstanceId'] = self.app_instance_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceId') is not None:
            self.app_instance_id = m.get('AppInstanceId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class GetPictureSearchJobStatusResponseBodyData(TeaModel):
    def __init__(
        self,
        create_time: int = None,
        end_time: int = None,
        job_id: str = None,
        job_status: int = None,
        search_pic_url: str = None,
        start_time: int = None,
        threshold: float = None,
    ):
        self.create_time = create_time
        self.end_time = end_time
        self.job_id = job_id
        self.job_status = job_status
        self.search_pic_url = search_pic_url
        self.start_time = start_time
        self.threshold = threshold

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.job_status is not None:
            result['JobStatus'] = self.job_status
        if self.search_pic_url is not None:
            result['SearchPicUrl'] = self.search_pic_url
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('JobStatus') is not None:
            self.job_status = m.get('JobStatus')
        if m.get('SearchPicUrl') is not None:
            self.search_pic_url = m.get('SearchPicUrl')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        return self


class GetPictureSearchJobStatusResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetPictureSearchJobStatusResponseBodyData = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_message = error_message
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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = GetPictureSearchJobStatusResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetPictureSearchJobStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetPictureSearchJobStatusResponseBody = None,
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
            temp_model = GetPictureSearchJobStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PictureSearchPictureRequest(TeaModel):
    def __init__(
        self,
        app_instance_id: str = None,
        contain_pic_url: bool = None,
        current_page: int = None,
        end_time: int = None,
        page_size: int = None,
        picture_search_type: int = None,
        search_pic_url: str = None,
        start_time: int = None,
        threshold: float = None,
    ):
        self.app_instance_id = app_instance_id
        self.contain_pic_url = contain_pic_url
        self.current_page = current_page
        self.end_time = end_time
        self.page_size = page_size
        self.picture_search_type = picture_search_type
        self.search_pic_url = search_pic_url
        self.start_time = start_time
        self.threshold = threshold

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_id is not None:
            result['AppInstanceId'] = self.app_instance_id
        if self.contain_pic_url is not None:
            result['ContainPicUrl'] = self.contain_pic_url
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.picture_search_type is not None:
            result['PictureSearchType'] = self.picture_search_type
        if self.search_pic_url is not None:
            result['SearchPicUrl'] = self.search_pic_url
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceId') is not None:
            self.app_instance_id = m.get('AppInstanceId')
        if m.get('ContainPicUrl') is not None:
            self.contain_pic_url = m.get('ContainPicUrl')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PictureSearchType') is not None:
            self.picture_search_type = m.get('PictureSearchType')
        if m.get('SearchPicUrl') is not None:
            self.search_pic_url = m.get('SearchPicUrl')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        return self


class PictureSearchPictureResponseBodyDataPageData(TeaModel):
    def __init__(
        self,
        event_time: int = None,
        gateway_iot_id: str = None,
        iot_id: str = None,
        pic_url: str = None,
        threshold: float = None,
        vector_id: str = None,
        vector_type: int = None,
    ):
        self.event_time = event_time
        self.gateway_iot_id = gateway_iot_id
        self.iot_id = iot_id
        self.pic_url = pic_url
        self.threshold = threshold
        self.vector_id = vector_id
        self.vector_type = vector_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_time is not None:
            result['EventTime'] = self.event_time
        if self.gateway_iot_id is not None:
            result['GatewayIotId'] = self.gateway_iot_id
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.pic_url is not None:
            result['PicUrl'] = self.pic_url
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        if self.vector_id is not None:
            result['VectorId'] = self.vector_id
        if self.vector_type is not None:
            result['VectorType'] = self.vector_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventTime') is not None:
            self.event_time = m.get('EventTime')
        if m.get('GatewayIotId') is not None:
            self.gateway_iot_id = m.get('GatewayIotId')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('PicUrl') is not None:
            self.pic_url = m.get('PicUrl')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        if m.get('VectorId') is not None:
            self.vector_id = m.get('VectorId')
        if m.get('VectorType') is not None:
            self.vector_type = m.get('VectorType')
        return self


class PictureSearchPictureResponseBodyData(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        page_count: int = None,
        page_data: List[PictureSearchPictureResponseBodyDataPageData] = None,
        page_size: int = None,
        total: int = None,
    ):
        self.current_page = current_page
        self.page_count = page_count
        self.page_data = page_data
        self.page_size = page_size
        self.total = total

    def validate(self):
        if self.page_data:
            for k in self.page_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        result['PageData'] = []
        if self.page_data is not None:
            for k in self.page_data:
                result['PageData'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        self.page_data = []
        if m.get('PageData') is not None:
            for k in m.get('PageData'):
                temp_model = PictureSearchPictureResponseBodyDataPageData()
                self.page_data.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class PictureSearchPictureResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: PictureSearchPictureResponseBodyData = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_message = error_message
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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = PictureSearchPictureResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class PictureSearchPictureResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PictureSearchPictureResponseBody = None,
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
            temp_model = PictureSearchPictureResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryCarProcessEventsRequest(TeaModel):
    def __init__(
        self,
        action_type: int = None,
        area_index: int = None,
        begin_time: int = None,
        current_page: int = None,
        end_time: int = None,
        iot_instance_id: str = None,
        page_size: int = None,
        plate_no: str = None,
        sub_device_name: str = None,
        sub_iot_id: str = None,
        sub_product_key: str = None,
    ):
        self.action_type = action_type
        self.area_index = area_index
        self.begin_time = begin_time
        self.current_page = current_page
        self.end_time = end_time
        self.iot_instance_id = iot_instance_id
        self.page_size = page_size
        self.plate_no = plate_no
        self.sub_device_name = sub_device_name
        self.sub_iot_id = sub_iot_id
        self.sub_product_key = sub_product_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_type is not None:
            result['ActionType'] = self.action_type
        if self.area_index is not None:
            result['AreaIndex'] = self.area_index
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.plate_no is not None:
            result['PlateNo'] = self.plate_no
        if self.sub_device_name is not None:
            result['SubDeviceName'] = self.sub_device_name
        if self.sub_iot_id is not None:
            result['SubIotId'] = self.sub_iot_id
        if self.sub_product_key is not None:
            result['SubProductKey'] = self.sub_product_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionType') is not None:
            self.action_type = m.get('ActionType')
        if m.get('AreaIndex') is not None:
            self.area_index = m.get('AreaIndex')
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PlateNo') is not None:
            self.plate_no = m.get('PlateNo')
        if m.get('SubDeviceName') is not None:
            self.sub_device_name = m.get('SubDeviceName')
        if m.get('SubIotId') is not None:
            self.sub_iot_id = m.get('SubIotId')
        if m.get('SubProductKey') is not None:
            self.sub_product_key = m.get('SubProductKey')
        return self


class QueryCarProcessEventsResponseBodyDataPageData(TeaModel):
    def __init__(
        self,
        action_type: int = None,
        area_index: int = None,
        confidence: int = None,
        event_id: str = None,
        event_pic_id: str = None,
        event_pic_url: str = None,
        event_time: int = None,
        event_type: int = None,
        iot_id: str = None,
        plate_no: str = None,
        sub_device_name: str = None,
        sub_device_nick_name: str = None,
        sub_iot_id: str = None,
        sub_product_key: str = None,
        task_id: str = None,
    ):
        self.action_type = action_type
        self.area_index = area_index
        self.confidence = confidence
        self.event_id = event_id
        self.event_pic_id = event_pic_id
        self.event_pic_url = event_pic_url
        self.event_time = event_time
        self.event_type = event_type
        self.iot_id = iot_id
        self.plate_no = plate_no
        self.sub_device_name = sub_device_name
        self.sub_device_nick_name = sub_device_nick_name
        self.sub_iot_id = sub_iot_id
        self.sub_product_key = sub_product_key
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_type is not None:
            result['ActionType'] = self.action_type
        if self.area_index is not None:
            result['AreaIndex'] = self.area_index
        if self.confidence is not None:
            result['Confidence'] = self.confidence
        if self.event_id is not None:
            result['EventId'] = self.event_id
        if self.event_pic_id is not None:
            result['EventPicId'] = self.event_pic_id
        if self.event_pic_url is not None:
            result['EventPicUrl'] = self.event_pic_url
        if self.event_time is not None:
            result['EventTime'] = self.event_time
        if self.event_type is not None:
            result['EventType'] = self.event_type
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.plate_no is not None:
            result['PlateNo'] = self.plate_no
        if self.sub_device_name is not None:
            result['SubDeviceName'] = self.sub_device_name
        if self.sub_device_nick_name is not None:
            result['SubDeviceNickName'] = self.sub_device_nick_name
        if self.sub_iot_id is not None:
            result['SubIotId'] = self.sub_iot_id
        if self.sub_product_key is not None:
            result['SubProductKey'] = self.sub_product_key
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionType') is not None:
            self.action_type = m.get('ActionType')
        if m.get('AreaIndex') is not None:
            self.area_index = m.get('AreaIndex')
        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        if m.get('EventPicId') is not None:
            self.event_pic_id = m.get('EventPicId')
        if m.get('EventPicUrl') is not None:
            self.event_pic_url = m.get('EventPicUrl')
        if m.get('EventTime') is not None:
            self.event_time = m.get('EventTime')
        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('PlateNo') is not None:
            self.plate_no = m.get('PlateNo')
        if m.get('SubDeviceName') is not None:
            self.sub_device_name = m.get('SubDeviceName')
        if m.get('SubDeviceNickName') is not None:
            self.sub_device_nick_name = m.get('SubDeviceNickName')
        if m.get('SubIotId') is not None:
            self.sub_iot_id = m.get('SubIotId')
        if m.get('SubProductKey') is not None:
            self.sub_product_key = m.get('SubProductKey')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class QueryCarProcessEventsResponseBodyData(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        page_count: int = None,
        page_data: List[QueryCarProcessEventsResponseBodyDataPageData] = None,
        page_size: int = None,
        total: int = None,
    ):
        self.current_page = current_page
        self.page_count = page_count
        self.page_data = page_data
        self.page_size = page_size
        self.total = total

    def validate(self):
        if self.page_data:
            for k in self.page_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        result['PageData'] = []
        if self.page_data is not None:
            for k in self.page_data:
                result['PageData'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        self.page_data = []
        if m.get('PageData') is not None:
            for k in m.get('PageData'):
                temp_model = QueryCarProcessEventsResponseBodyDataPageData()
                self.page_data.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class QueryCarProcessEventsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: QueryCarProcessEventsResponseBodyData = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_message = error_message
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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = QueryCarProcessEventsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryCarProcessEventsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryCarProcessEventsResponseBody = None,
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
            temp_model = QueryCarProcessEventsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryDeviceEventRequest(TeaModel):
    def __init__(
        self,
        begin_time: int = None,
        current_page: int = None,
        device_name: str = None,
        end_time: int = None,
        event_type: int = None,
        iot_id: str = None,
        iot_instance_id: str = None,
        page_size: int = None,
        product_key: str = None,
    ):
        self.begin_time = begin_time
        self.current_page = current_page
        self.device_name = device_name
        self.end_time = end_time
        self.event_type = event_type
        self.iot_id = iot_id
        self.iot_instance_id = iot_instance_id
        self.page_size = page_size
        self.product_key = product_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.event_type is not None:
            result['EventType'] = self.event_type
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        return self


class QueryDeviceEventResponseBodyDataList(TeaModel):
    def __init__(
        self,
        event_data: str = None,
        event_desc: str = None,
        event_id: str = None,
        event_pic_id: str = None,
        event_time: str = None,
        event_type: int = None,
    ):
        self.event_data = event_data
        self.event_desc = event_desc
        self.event_id = event_id
        self.event_pic_id = event_pic_id
        self.event_time = event_time
        self.event_type = event_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_data is not None:
            result['EventData'] = self.event_data
        if self.event_desc is not None:
            result['EventDesc'] = self.event_desc
        if self.event_id is not None:
            result['EventId'] = self.event_id
        if self.event_pic_id is not None:
            result['EventPicId'] = self.event_pic_id
        if self.event_time is not None:
            result['EventTime'] = self.event_time
        if self.event_type is not None:
            result['EventType'] = self.event_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventData') is not None:
            self.event_data = m.get('EventData')
        if m.get('EventDesc') is not None:
            self.event_desc = m.get('EventDesc')
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        if m.get('EventPicId') is not None:
            self.event_pic_id = m.get('EventPicId')
        if m.get('EventTime') is not None:
            self.event_time = m.get('EventTime')
        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')
        return self


class QueryDeviceEventResponseBodyData(TeaModel):
    def __init__(
        self,
        list: List[QueryDeviceEventResponseBodyDataList] = None,
        page: int = None,
        page_count: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.list = list
        self.page = page
        self.page_count = page_count
        self.page_size = page_size
        self.total = total

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.page is not None:
            result['Page'] = self.page
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = QueryDeviceEventResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class QueryDeviceEventResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: QueryDeviceEventResponseBodyData = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_message = error_message
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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = QueryDeviceEventResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryDeviceEventResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryDeviceEventResponseBody = None,
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
            temp_model = QueryDeviceEventResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryDeviceEventPictureRequest(TeaModel):
    def __init__(
        self,
        device_name: str = None,
        event_id: str = None,
        iot_id: str = None,
        iot_instance_id: str = None,
        product_key: str = None,
    ):
        self.device_name = device_name
        self.event_id = event_id
        self.iot_id = iot_id
        self.iot_instance_id = iot_instance_id
        self.product_key = product_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.event_id is not None:
            result['EventId'] = self.event_id
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        return self


class QueryDeviceEventPictureResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_message = error_message
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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryDeviceEventPictureResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryDeviceEventPictureResponseBody = None,
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
            temp_model = QueryDeviceEventPictureResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryDeviceEventRecordRequest(TeaModel):
    def __init__(
        self,
        device_name: str = None,
        event_id: str = None,
        iot_id: str = None,
        iot_instance_id: str = None,
        product_key: str = None,
    ):
        self.device_name = device_name
        self.event_id = event_id
        self.iot_id = iot_id
        self.iot_instance_id = iot_instance_id
        self.product_key = product_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.event_id is not None:
            result['EventId'] = self.event_id
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        return self


class QueryDeviceEventRecordResponseBodyData(TeaModel):
    def __init__(
        self,
        begin_time: str = None,
        end_time: str = None,
        file_name: str = None,
        vod_url: str = None,
    ):
        self.begin_time = begin_time
        self.end_time = end_time
        self.file_name = file_name
        self.vod_url = vod_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.vod_url is not None:
            result['VodUrl'] = self.vod_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('VodUrl') is not None:
            self.vod_url = m.get('VodUrl')
        return self


class QueryDeviceEventRecordResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: List[QueryDeviceEventRecordResponseBodyData] = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_message = error_message
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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
                temp_model = QueryDeviceEventRecordResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryDeviceEventRecordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryDeviceEventRecordResponseBody = None,
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
            temp_model = QueryDeviceEventRecordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryDevicePictureByListRequest(TeaModel):
    def __init__(
        self,
        device_name: str = None,
        expire_time: int = None,
        iot_id: str = None,
        iot_instance_id: str = None,
        picture_id_list: List[str] = None,
        picture_type: int = None,
        product_key: str = None,
        thumb_width: int = None,
    ):
        self.device_name = device_name
        self.expire_time = expire_time
        self.iot_id = iot_id
        self.iot_instance_id = iot_instance_id
        self.picture_id_list = picture_id_list
        self.picture_type = picture_type
        self.product_key = product_key
        self.thumb_width = thumb_width

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.picture_id_list is not None:
            result['PictureIdList'] = self.picture_id_list
        if self.picture_type is not None:
            result['PictureType'] = self.picture_type
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        if self.thumb_width is not None:
            result['ThumbWidth'] = self.thumb_width
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('PictureIdList') is not None:
            self.picture_id_list = m.get('PictureIdList')
        if m.get('PictureType') is not None:
            self.picture_type = m.get('PictureType')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        if m.get('ThumbWidth') is not None:
            self.thumb_width = m.get('ThumbWidth')
        return self


class QueryDevicePictureByListResponseBodyDataPicData(TeaModel):
    def __init__(
        self,
        iot_id: str = None,
        pic_create_time: int = None,
        pic_id: str = None,
        pic_url: str = None,
        thumb_url: str = None,
    ):
        self.iot_id = iot_id
        self.pic_create_time = pic_create_time
        self.pic_id = pic_id
        self.pic_url = pic_url
        self.thumb_url = thumb_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.pic_create_time is not None:
            result['PicCreateTime'] = self.pic_create_time
        if self.pic_id is not None:
            result['PicId'] = self.pic_id
        if self.pic_url is not None:
            result['PicUrl'] = self.pic_url
        if self.thumb_url is not None:
            result['ThumbUrl'] = self.thumb_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('PicCreateTime') is not None:
            self.pic_create_time = m.get('PicCreateTime')
        if m.get('PicId') is not None:
            self.pic_id = m.get('PicId')
        if m.get('PicUrl') is not None:
            self.pic_url = m.get('PicUrl')
        if m.get('ThumbUrl') is not None:
            self.thumb_url = m.get('ThumbUrl')
        return self


class QueryDevicePictureByListResponseBodyData(TeaModel):
    def __init__(
        self,
        pic_data: List[QueryDevicePictureByListResponseBodyDataPicData] = None,
    ):
        self.pic_data = pic_data

    def validate(self):
        if self.pic_data:
            for k in self.pic_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['picData'] = []
        if self.pic_data is not None:
            for k in self.pic_data:
                result['picData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.pic_data = []
        if m.get('picData') is not None:
            for k in m.get('picData'):
                temp_model = QueryDevicePictureByListResponseBodyDataPicData()
                self.pic_data.append(temp_model.from_map(k))
        return self


class QueryDevicePictureByListResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: QueryDevicePictureByListResponseBodyData = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_message = error_message
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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = QueryDevicePictureByListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryDevicePictureByListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryDevicePictureByListResponseBody = None,
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
            temp_model = QueryDevicePictureByListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryDevicePictureFileRequest(TeaModel):
    def __init__(
        self,
        capture_id: str = None,
        device_name: str = None,
        expire_time: int = None,
        iot_id: str = None,
        iot_instance_id: str = None,
        picture_type: int = None,
        product_key: str = None,
        thumb_width: int = None,
    ):
        self.capture_id = capture_id
        self.device_name = device_name
        self.expire_time = expire_time
        self.iot_id = iot_id
        self.iot_instance_id = iot_instance_id
        self.picture_type = picture_type
        self.product_key = product_key
        self.thumb_width = thumb_width

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.capture_id is not None:
            result['CaptureId'] = self.capture_id
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.picture_type is not None:
            result['PictureType'] = self.picture_type
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        if self.thumb_width is not None:
            result['ThumbWidth'] = self.thumb_width
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CaptureId') is not None:
            self.capture_id = m.get('CaptureId')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('PictureType') is not None:
            self.picture_type = m.get('PictureType')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        if m.get('ThumbWidth') is not None:
            self.thumb_width = m.get('ThumbWidth')
        return self


class QueryDevicePictureFileResponseBodyData(TeaModel):
    def __init__(
        self,
        iot_id: str = None,
        pic_create_time: int = None,
        pic_id: str = None,
        pic_url: str = None,
        thumb_url: str = None,
    ):
        self.iot_id = iot_id
        self.pic_create_time = pic_create_time
        self.pic_id = pic_id
        self.pic_url = pic_url
        self.thumb_url = thumb_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.pic_create_time is not None:
            result['PicCreateTime'] = self.pic_create_time
        if self.pic_id is not None:
            result['PicId'] = self.pic_id
        if self.pic_url is not None:
            result['PicUrl'] = self.pic_url
        if self.thumb_url is not None:
            result['ThumbUrl'] = self.thumb_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('PicCreateTime') is not None:
            self.pic_create_time = m.get('PicCreateTime')
        if m.get('PicId') is not None:
            self.pic_id = m.get('PicId')
        if m.get('PicUrl') is not None:
            self.pic_url = m.get('PicUrl')
        if m.get('ThumbUrl') is not None:
            self.thumb_url = m.get('ThumbUrl')
        return self


class QueryDevicePictureFileResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: QueryDevicePictureFileResponseBodyData = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_message = error_message
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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = QueryDevicePictureFileResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryDevicePictureFileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryDevicePictureFileResponseBody = None,
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
            temp_model = QueryDevicePictureFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryDevicePictureLifeCycleRequest(TeaModel):
    def __init__(
        self,
        iot_id: str = None,
    ):
        self.iot_id = iot_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        return self


class QueryDevicePictureLifeCycleResponseBodyData(TeaModel):
    def __init__(
        self,
        day: int = None,
        iot_id: str = None,
    ):
        self.day = day
        self.iot_id = iot_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.day is not None:
            result['Day'] = self.day
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Day') is not None:
            self.day = m.get('Day')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        return self


class QueryDevicePictureLifeCycleResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: QueryDevicePictureLifeCycleResponseBodyData = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_message = error_message
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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = QueryDevicePictureLifeCycleResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryDevicePictureLifeCycleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryDevicePictureLifeCycleResponseBody = None,
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
            temp_model = QueryDevicePictureLifeCycleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryDeviceRecordLifeCycleRequest(TeaModel):
    def __init__(
        self,
        device_list: List[str] = None,
    ):
        self.device_list = device_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_list is not None:
            result['DeviceList'] = self.device_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceList') is not None:
            self.device_list = m.get('DeviceList')
        return self


class QueryDeviceRecordLifeCycleResponseBodyData(TeaModel):
    def __init__(
        self,
        day: int = None,
        iot_id: str = None,
    ):
        self.day = day
        self.iot_id = iot_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.day is not None:
            result['Day'] = self.day
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Day') is not None:
            self.day = m.get('Day')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        return self


class QueryDeviceRecordLifeCycleResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: List[QueryDeviceRecordLifeCycleResponseBodyData] = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_message = error_message
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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
                temp_model = QueryDeviceRecordLifeCycleResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryDeviceRecordLifeCycleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryDeviceRecordLifeCycleResponseBody = None,
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
            temp_model = QueryDeviceRecordLifeCycleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryDeviceVodUrlRequest(TeaModel):
    def __init__(
        self,
        device_name: str = None,
        enable_stun: bool = None,
        encrypt_type: int = None,
        file_name: str = None,
        iot_id: str = None,
        iot_instance_id: str = None,
        play_un_limited: bool = None,
        product_key: str = None,
        scheme: str = None,
        seek_time: int = None,
        should_encrypt: bool = None,
        url_valid_duration: int = None,
    ):
        self.device_name = device_name
        self.enable_stun = enable_stun
        self.encrypt_type = encrypt_type
        self.file_name = file_name
        self.iot_id = iot_id
        self.iot_instance_id = iot_instance_id
        self.play_un_limited = play_un_limited
        self.product_key = product_key
        self.scheme = scheme
        self.seek_time = seek_time
        self.should_encrypt = should_encrypt
        self.url_valid_duration = url_valid_duration

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.enable_stun is not None:
            result['EnableStun'] = self.enable_stun
        if self.encrypt_type is not None:
            result['EncryptType'] = self.encrypt_type
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.play_un_limited is not None:
            result['PlayUnLimited'] = self.play_un_limited
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        if self.scheme is not None:
            result['Scheme'] = self.scheme
        if self.seek_time is not None:
            result['SeekTime'] = self.seek_time
        if self.should_encrypt is not None:
            result['ShouldEncrypt'] = self.should_encrypt
        if self.url_valid_duration is not None:
            result['UrlValidDuration'] = self.url_valid_duration
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('EnableStun') is not None:
            self.enable_stun = m.get('EnableStun')
        if m.get('EncryptType') is not None:
            self.encrypt_type = m.get('EncryptType')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('PlayUnLimited') is not None:
            self.play_un_limited = m.get('PlayUnLimited')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        if m.get('Scheme') is not None:
            self.scheme = m.get('Scheme')
        if m.get('SeekTime') is not None:
            self.seek_time = m.get('SeekTime')
        if m.get('ShouldEncrypt') is not None:
            self.should_encrypt = m.get('ShouldEncrypt')
        if m.get('UrlValidDuration') is not None:
            self.url_valid_duration = m.get('UrlValidDuration')
        return self


class QueryDeviceVodUrlResponseBodyData(TeaModel):
    def __init__(
        self,
        decrypt_key: str = None,
        stun_info: str = None,
        vod_url: str = None,
    ):
        self.decrypt_key = decrypt_key
        self.stun_info = stun_info
        self.vod_url = vod_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.decrypt_key is not None:
            result['DecryptKey'] = self.decrypt_key
        if self.stun_info is not None:
            result['StunInfo'] = self.stun_info
        if self.vod_url is not None:
            result['VodUrl'] = self.vod_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DecryptKey') is not None:
            self.decrypt_key = m.get('DecryptKey')
        if m.get('StunInfo') is not None:
            self.stun_info = m.get('StunInfo')
        if m.get('VodUrl') is not None:
            self.vod_url = m.get('VodUrl')
        return self


class QueryDeviceVodUrlResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: QueryDeviceVodUrlResponseBodyData = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_message = error_message
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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = QueryDeviceVodUrlResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryDeviceVodUrlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryDeviceVodUrlResponseBody = None,
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
            temp_model = QueryDeviceVodUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryDeviceVodUrlByTimeRequest(TeaModel):
    def __init__(
        self,
        begin_time: int = None,
        device_name: str = None,
        enable_stun: bool = None,
        encrypt_type: int = None,
        end_time: int = None,
        iot_id: str = None,
        iot_instance_id: str = None,
        play_un_limited: bool = None,
        product_key: str = None,
        scheme: str = None,
        seek_time: int = None,
        should_encrypt: bool = None,
        url_valid_duration: int = None,
    ):
        self.begin_time = begin_time
        self.device_name = device_name
        self.enable_stun = enable_stun
        self.encrypt_type = encrypt_type
        self.end_time = end_time
        self.iot_id = iot_id
        self.iot_instance_id = iot_instance_id
        self.play_un_limited = play_un_limited
        self.product_key = product_key
        self.scheme = scheme
        self.seek_time = seek_time
        self.should_encrypt = should_encrypt
        self.url_valid_duration = url_valid_duration

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.enable_stun is not None:
            result['EnableStun'] = self.enable_stun
        if self.encrypt_type is not None:
            result['EncryptType'] = self.encrypt_type
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.play_un_limited is not None:
            result['PlayUnLimited'] = self.play_un_limited
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        if self.scheme is not None:
            result['Scheme'] = self.scheme
        if self.seek_time is not None:
            result['SeekTime'] = self.seek_time
        if self.should_encrypt is not None:
            result['ShouldEncrypt'] = self.should_encrypt
        if self.url_valid_duration is not None:
            result['UrlValidDuration'] = self.url_valid_duration
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('EnableStun') is not None:
            self.enable_stun = m.get('EnableStun')
        if m.get('EncryptType') is not None:
            self.encrypt_type = m.get('EncryptType')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('PlayUnLimited') is not None:
            self.play_un_limited = m.get('PlayUnLimited')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        if m.get('Scheme') is not None:
            self.scheme = m.get('Scheme')
        if m.get('SeekTime') is not None:
            self.seek_time = m.get('SeekTime')
        if m.get('ShouldEncrypt') is not None:
            self.should_encrypt = m.get('ShouldEncrypt')
        if m.get('UrlValidDuration') is not None:
            self.url_valid_duration = m.get('UrlValidDuration')
        return self


class QueryDeviceVodUrlByTimeResponseBodyData(TeaModel):
    def __init__(
        self,
        decrypt_key: str = None,
        stun_info: str = None,
        vod_url: str = None,
    ):
        self.decrypt_key = decrypt_key
        self.stun_info = stun_info
        self.vod_url = vod_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.decrypt_key is not None:
            result['DecryptKey'] = self.decrypt_key
        if self.stun_info is not None:
            result['StunInfo'] = self.stun_info
        if self.vod_url is not None:
            result['VodUrl'] = self.vod_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DecryptKey') is not None:
            self.decrypt_key = m.get('DecryptKey')
        if m.get('StunInfo') is not None:
            self.stun_info = m.get('StunInfo')
        if m.get('VodUrl') is not None:
            self.vod_url = m.get('VodUrl')
        return self


class QueryDeviceVodUrlByTimeResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: QueryDeviceVodUrlByTimeResponseBodyData = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_message = error_message
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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = QueryDeviceVodUrlByTimeResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryDeviceVodUrlByTimeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryDeviceVodUrlByTimeResponseBody = None,
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
            temp_model = QueryDeviceVodUrlByTimeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryEventRecordPlanDetailRequest(TeaModel):
    def __init__(
        self,
        plan_id: str = None,
    ):
        self.plan_id = plan_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        return self


class QueryEventRecordPlanDetailResponseBodyDataTemplateInfoTimeSectionList(TeaModel):
    def __init__(
        self,
        begin: int = None,
        day_of_week: int = None,
        end: int = None,
    ):
        self.begin = begin
        self.day_of_week = day_of_week
        self.end = end

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin is not None:
            result['Begin'] = self.begin
        if self.day_of_week is not None:
            result['DayOfWeek'] = self.day_of_week
        if self.end is not None:
            result['End'] = self.end
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Begin') is not None:
            self.begin = m.get('Begin')
        if m.get('DayOfWeek') is not None:
            self.day_of_week = m.get('DayOfWeek')
        if m.get('End') is not None:
            self.end = m.get('End')
        return self


class QueryEventRecordPlanDetailResponseBodyDataTemplateInfo(TeaModel):
    def __init__(
        self,
        all_day: int = None,
        default: int = None,
        name: str = None,
        template_id: str = None,
        time_section_list: List[QueryEventRecordPlanDetailResponseBodyDataTemplateInfoTimeSectionList] = None,
    ):
        self.all_day = all_day
        self.default = default
        self.name = name
        self.template_id = template_id
        self.time_section_list = time_section_list

    def validate(self):
        if self.time_section_list:
            for k in self.time_section_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all_day is not None:
            result['AllDay'] = self.all_day
        if self.default is not None:
            result['Default'] = self.default
        if self.name is not None:
            result['Name'] = self.name
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        result['TimeSectionList'] = []
        if self.time_section_list is not None:
            for k in self.time_section_list:
                result['TimeSectionList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllDay') is not None:
            self.all_day = m.get('AllDay')
        if m.get('Default') is not None:
            self.default = m.get('Default')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        self.time_section_list = []
        if m.get('TimeSectionList') is not None:
            for k in m.get('TimeSectionList'):
                temp_model = QueryEventRecordPlanDetailResponseBodyDataTemplateInfoTimeSectionList()
                self.time_section_list.append(temp_model.from_map(k))
        return self


class QueryEventRecordPlanDetailResponseBodyData(TeaModel):
    def __init__(
        self,
        name: str = None,
        plan_id: str = None,
        pre_record_duration: int = None,
        record_duration: int = None,
        template_id: str = None,
        template_info: QueryEventRecordPlanDetailResponseBodyDataTemplateInfo = None,
    ):
        self.name = name
        self.plan_id = plan_id
        self.pre_record_duration = pre_record_duration
        self.record_duration = record_duration
        self.template_id = template_id
        self.template_info = template_info

    def validate(self):
        if self.template_info:
            self.template_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        if self.pre_record_duration is not None:
            result['PreRecordDuration'] = self.pre_record_duration
        if self.record_duration is not None:
            result['RecordDuration'] = self.record_duration
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_info is not None:
            result['TemplateInfo'] = self.template_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        if m.get('PreRecordDuration') is not None:
            self.pre_record_duration = m.get('PreRecordDuration')
        if m.get('RecordDuration') is not None:
            self.record_duration = m.get('RecordDuration')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateInfo') is not None:
            temp_model = QueryEventRecordPlanDetailResponseBodyDataTemplateInfo()
            self.template_info = temp_model.from_map(m['TemplateInfo'])
        return self


class QueryEventRecordPlanDetailResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: QueryEventRecordPlanDetailResponseBodyData = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_message = error_message
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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = QueryEventRecordPlanDetailResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryEventRecordPlanDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryEventRecordPlanDetailResponseBody = None,
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
            temp_model = QueryEventRecordPlanDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryEventRecordPlanDeviceByDeviceRequest(TeaModel):
    def __init__(
        self,
        device_name: str = None,
        iot_id: str = None,
        iot_instance_id: str = None,
        product_key: str = None,
        stream_type: int = None,
    ):
        self.device_name = device_name
        self.iot_id = iot_id
        self.iot_instance_id = iot_instance_id
        self.product_key = product_key
        self.stream_type = stream_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        if self.stream_type is not None:
            result['StreamType'] = self.stream_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        if m.get('StreamType') is not None:
            self.stream_type = m.get('StreamType')
        return self


class QueryEventRecordPlanDeviceByDeviceResponseBodyDataTemplateInfoTimeSectionList(TeaModel):
    def __init__(
        self,
        begin: int = None,
        day_of_week: int = None,
        end: int = None,
    ):
        self.begin = begin
        self.day_of_week = day_of_week
        self.end = end

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin is not None:
            result['Begin'] = self.begin
        if self.day_of_week is not None:
            result['DayOfWeek'] = self.day_of_week
        if self.end is not None:
            result['End'] = self.end
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Begin') is not None:
            self.begin = m.get('Begin')
        if m.get('DayOfWeek') is not None:
            self.day_of_week = m.get('DayOfWeek')
        if m.get('End') is not None:
            self.end = m.get('End')
        return self


class QueryEventRecordPlanDeviceByDeviceResponseBodyDataTemplateInfo(TeaModel):
    def __init__(
        self,
        all_day: int = None,
        default: int = None,
        name: str = None,
        template_id: str = None,
        time_section_list: List[QueryEventRecordPlanDeviceByDeviceResponseBodyDataTemplateInfoTimeSectionList] = None,
    ):
        self.all_day = all_day
        self.default = default
        self.name = name
        self.template_id = template_id
        self.time_section_list = time_section_list

    def validate(self):
        if self.time_section_list:
            for k in self.time_section_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all_day is not None:
            result['AllDay'] = self.all_day
        if self.default is not None:
            result['Default'] = self.default
        if self.name is not None:
            result['Name'] = self.name
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        result['TimeSectionList'] = []
        if self.time_section_list is not None:
            for k in self.time_section_list:
                result['TimeSectionList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllDay') is not None:
            self.all_day = m.get('AllDay')
        if m.get('Default') is not None:
            self.default = m.get('Default')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        self.time_section_list = []
        if m.get('TimeSectionList') is not None:
            for k in m.get('TimeSectionList'):
                temp_model = QueryEventRecordPlanDeviceByDeviceResponseBodyDataTemplateInfoTimeSectionList()
                self.time_section_list.append(temp_model.from_map(k))
        return self


class QueryEventRecordPlanDeviceByDeviceResponseBodyData(TeaModel):
    def __init__(
        self,
        name: str = None,
        plan_id: str = None,
        pre_record_duration: int = None,
        record_duration: int = None,
        template_id: str = None,
        template_info: QueryEventRecordPlanDeviceByDeviceResponseBodyDataTemplateInfo = None,
    ):
        self.name = name
        self.plan_id = plan_id
        self.pre_record_duration = pre_record_duration
        self.record_duration = record_duration
        self.template_id = template_id
        self.template_info = template_info

    def validate(self):
        if self.template_info:
            self.template_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        if self.pre_record_duration is not None:
            result['PreRecordDuration'] = self.pre_record_duration
        if self.record_duration is not None:
            result['RecordDuration'] = self.record_duration
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_info is not None:
            result['TemplateInfo'] = self.template_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        if m.get('PreRecordDuration') is not None:
            self.pre_record_duration = m.get('PreRecordDuration')
        if m.get('RecordDuration') is not None:
            self.record_duration = m.get('RecordDuration')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateInfo') is not None:
            temp_model = QueryEventRecordPlanDeviceByDeviceResponseBodyDataTemplateInfo()
            self.template_info = temp_model.from_map(m['TemplateInfo'])
        return self


class QueryEventRecordPlanDeviceByDeviceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: QueryEventRecordPlanDeviceByDeviceResponseBodyData = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_message = error_message
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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = QueryEventRecordPlanDeviceByDeviceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryEventRecordPlanDeviceByDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryEventRecordPlanDeviceByDeviceResponseBody = None,
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
            temp_model = QueryEventRecordPlanDeviceByDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryEventRecordPlanDeviceByPlanRequest(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        plan_id: str = None,
    ):
        self.current_page = current_page
        self.page_size = page_size
        self.plan_id = plan_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        return self


class QueryEventRecordPlanDeviceByPlanResponseBodyDataList(TeaModel):
    def __init__(
        self,
        iot_id: str = None,
        stream_type: int = None,
    ):
        self.iot_id = iot_id
        self.stream_type = stream_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.stream_type is not None:
            result['StreamType'] = self.stream_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('StreamType') is not None:
            self.stream_type = m.get('StreamType')
        return self


class QueryEventRecordPlanDeviceByPlanResponseBodyData(TeaModel):
    def __init__(
        self,
        list: List[QueryEventRecordPlanDeviceByPlanResponseBodyDataList] = None,
        page: int = None,
        page_count: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.list = list
        self.page = page
        self.page_count = page_count
        self.page_size = page_size
        self.total = total

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.page is not None:
            result['Page'] = self.page
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = QueryEventRecordPlanDeviceByPlanResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class QueryEventRecordPlanDeviceByPlanResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: QueryEventRecordPlanDeviceByPlanResponseBodyData = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_message = error_message
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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = QueryEventRecordPlanDeviceByPlanResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryEventRecordPlanDeviceByPlanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryEventRecordPlanDeviceByPlanResponseBody = None,
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
            temp_model = QueryEventRecordPlanDeviceByPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryEventRecordPlansRequest(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
    ):
        self.current_page = current_page
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class QueryEventRecordPlansResponseBodyDataList(TeaModel):
    def __init__(
        self,
        event_type: str = None,
        name: str = None,
        plan_id: str = None,
        pre_record_duration: int = None,
        record_duration: int = None,
        template_id: str = None,
    ):
        self.event_type = event_type
        self.name = name
        self.plan_id = plan_id
        self.pre_record_duration = pre_record_duration
        self.record_duration = record_duration
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_type is not None:
            result['EventType'] = self.event_type
        if self.name is not None:
            result['Name'] = self.name
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        if self.pre_record_duration is not None:
            result['PreRecordDuration'] = self.pre_record_duration
        if self.record_duration is not None:
            result['RecordDuration'] = self.record_duration
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        if m.get('PreRecordDuration') is not None:
            self.pre_record_duration = m.get('PreRecordDuration')
        if m.get('RecordDuration') is not None:
            self.record_duration = m.get('RecordDuration')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class QueryEventRecordPlansResponseBodyData(TeaModel):
    def __init__(
        self,
        list: List[QueryEventRecordPlansResponseBodyDataList] = None,
        page: int = None,
        page_count: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.list = list
        self.page = page
        self.page_count = page_count
        self.page_size = page_size
        self.total = total

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.page is not None:
            result['Page'] = self.page
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = QueryEventRecordPlansResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class QueryEventRecordPlansResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: QueryEventRecordPlansResponseBodyData = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_message = error_message
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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = QueryEventRecordPlansResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryEventRecordPlansResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryEventRecordPlansResponseBody = None,
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
            temp_model = QueryEventRecordPlansResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryFaceAllDeviceGroupRequest(TeaModel):
    def __init__(
        self,
        iot_instance_id: str = None,
        isolation_id: str = None,
        page_no: int = None,
        page_size: int = None,
    ):
        self.iot_instance_id = iot_instance_id
        self.isolation_id = isolation_id
        self.page_no = page_no
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.isolation_id is not None:
            result['IsolationId'] = self.isolation_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('IsolationId') is not None:
            self.isolation_id = m.get('IsolationId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class QueryFaceAllDeviceGroupResponseBodyDataDeviceGroupList(TeaModel):
    def __init__(
        self,
        device_group_id: str = None,
        device_group_name: str = None,
        modified_time: str = None,
    ):
        self.device_group_id = device_group_id
        self.device_group_name = device_group_name
        self.modified_time = modified_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_group_id is not None:
            result['DeviceGroupId'] = self.device_group_id
        if self.device_group_name is not None:
            result['DeviceGroupName'] = self.device_group_name
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceGroupId') is not None:
            self.device_group_id = m.get('DeviceGroupId')
        if m.get('DeviceGroupName') is not None:
            self.device_group_name = m.get('DeviceGroupName')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        return self


class QueryFaceAllDeviceGroupResponseBodyData(TeaModel):
    def __init__(
        self,
        device_group_list: List[QueryFaceAllDeviceGroupResponseBodyDataDeviceGroupList] = None,
        page_no: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.device_group_list = device_group_list
        self.page_no = page_no
        self.page_size = page_size
        self.total = total

    def validate(self):
        if self.device_group_list:
            for k in self.device_group_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DeviceGroupList'] = []
        if self.device_group_list is not None:
            for k in self.device_group_list:
                result['DeviceGroupList'].append(k.to_map() if k else None)
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.device_group_list = []
        if m.get('DeviceGroupList') is not None:
            for k in m.get('DeviceGroupList'):
                temp_model = QueryFaceAllDeviceGroupResponseBodyDataDeviceGroupList()
                self.device_group_list.append(temp_model.from_map(k))
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class QueryFaceAllDeviceGroupResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: QueryFaceAllDeviceGroupResponseBodyData = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_message = error_message
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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = QueryFaceAllDeviceGroupResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryFaceAllDeviceGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryFaceAllDeviceGroupResponseBody = None,
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
            temp_model = QueryFaceAllDeviceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryFaceAllUserGroupRequest(TeaModel):
    def __init__(
        self,
        isolation_id: str = None,
        page_no: int = None,
        page_size: int = None,
    ):
        self.isolation_id = isolation_id
        self.page_no = page_no
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.isolation_id is not None:
            result['IsolationId'] = self.isolation_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsolationId') is not None:
            self.isolation_id = m.get('IsolationId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class QueryFaceAllUserGroupResponseBodyDataUserGroupList(TeaModel):
    def __init__(
        self,
        modified_time: str = None,
        user_group_id: str = None,
        user_group_name: str = None,
    ):
        self.modified_time = modified_time
        self.user_group_id = user_group_id
        self.user_group_name = user_group_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        if self.user_group_name is not None:
            result['UserGroupName'] = self.user_group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        if m.get('UserGroupName') is not None:
            self.user_group_name = m.get('UserGroupName')
        return self


class QueryFaceAllUserGroupResponseBodyData(TeaModel):
    def __init__(
        self,
        page_no: int = None,
        page_size: int = None,
        total: int = None,
        user_group_list: List[QueryFaceAllUserGroupResponseBodyDataUserGroupList] = None,
    ):
        self.page_no = page_no
        self.page_size = page_size
        self.total = total
        self.user_group_list = user_group_list

    def validate(self):
        if self.user_group_list:
            for k in self.user_group_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        result['UserGroupList'] = []
        if self.user_group_list is not None:
            for k in self.user_group_list:
                result['UserGroupList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        self.user_group_list = []
        if m.get('UserGroupList') is not None:
            for k in m.get('UserGroupList'):
                temp_model = QueryFaceAllUserGroupResponseBodyDataUserGroupList()
                self.user_group_list.append(temp_model.from_map(k))
        return self


class QueryFaceAllUserGroupResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: QueryFaceAllUserGroupResponseBodyData = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_message = error_message
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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = QueryFaceAllUserGroupResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryFaceAllUserGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryFaceAllUserGroupResponseBody = None,
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
            temp_model = QueryFaceAllUserGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryFaceAllUserGroupAndDeviceGroupRelationRequest(TeaModel):
    def __init__(
        self,
        isolation_id: str = None,
        page_no: int = None,
        page_size: int = None,
    ):
        self.isolation_id = isolation_id
        self.page_no = page_no
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.isolation_id is not None:
            result['IsolationId'] = self.isolation_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsolationId') is not None:
            self.isolation_id = m.get('IsolationId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class QueryFaceAllUserGroupAndDeviceGroupRelationResponseBodyDataList(TeaModel):
    def __init__(
        self,
        control_id: str = None,
        control_type: str = None,
        device_group_id: str = None,
        modified_time: str = None,
        user_group_id: str = None,
    ):
        self.control_id = control_id
        self.control_type = control_type
        self.device_group_id = device_group_id
        self.modified_time = modified_time
        self.user_group_id = user_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.control_id is not None:
            result['ControlId'] = self.control_id
        if self.control_type is not None:
            result['ControlType'] = self.control_type
        if self.device_group_id is not None:
            result['DeviceGroupId'] = self.device_group_id
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ControlId') is not None:
            self.control_id = m.get('ControlId')
        if m.get('ControlType') is not None:
            self.control_type = m.get('ControlType')
        if m.get('DeviceGroupId') is not None:
            self.device_group_id = m.get('DeviceGroupId')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        return self


class QueryFaceAllUserGroupAndDeviceGroupRelationResponseBodyData(TeaModel):
    def __init__(
        self,
        list: List[QueryFaceAllUserGroupAndDeviceGroupRelationResponseBodyDataList] = None,
        page: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.list = list
        self.page = page
        self.page_size = page_size
        self.total = total

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = QueryFaceAllUserGroupAndDeviceGroupRelationResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class QueryFaceAllUserGroupAndDeviceGroupRelationResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: QueryFaceAllUserGroupAndDeviceGroupRelationResponseBodyData = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_message = error_message
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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = QueryFaceAllUserGroupAndDeviceGroupRelationResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryFaceAllUserGroupAndDeviceGroupRelationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryFaceAllUserGroupAndDeviceGroupRelationResponseBody = None,
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
            temp_model = QueryFaceAllUserGroupAndDeviceGroupRelationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryFaceAllUserIdsByGroupIdRequest(TeaModel):
    def __init__(
        self,
        isolation_id: str = None,
        page_no: int = None,
        page_size: int = None,
        user_group_id: str = None,
    ):
        self.isolation_id = isolation_id
        self.page_no = page_no
        self.page_size = page_size
        self.user_group_id = user_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.isolation_id is not None:
            result['IsolationId'] = self.isolation_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsolationId') is not None:
            self.isolation_id = m.get('IsolationId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        return self


class QueryFaceAllUserIdsByGroupIdResponseBodyDataList(TeaModel):
    def __init__(
        self,
        custom_user_id: str = None,
        name: str = None,
        params: str = None,
        user_id: str = None,
    ):
        self.custom_user_id = custom_user_id
        self.name = name
        self.params = params
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_user_id is not None:
            result['CustomUserId'] = self.custom_user_id
        if self.name is not None:
            result['Name'] = self.name
        if self.params is not None:
            result['Params'] = self.params
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomUserId') is not None:
            self.custom_user_id = m.get('CustomUserId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Params') is not None:
            self.params = m.get('Params')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class QueryFaceAllUserIdsByGroupIdResponseBodyData(TeaModel):
    def __init__(
        self,
        list: List[QueryFaceAllUserIdsByGroupIdResponseBodyDataList] = None,
        page: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.list = list
        self.page = page
        self.page_size = page_size
        self.total = total

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = QueryFaceAllUserIdsByGroupIdResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class QueryFaceAllUserIdsByGroupIdResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: QueryFaceAllUserIdsByGroupIdResponseBodyData = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_message = error_message
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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = QueryFaceAllUserIdsByGroupIdResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryFaceAllUserIdsByGroupIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryFaceAllUserIdsByGroupIdResponseBody = None,
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
            temp_model = QueryFaceAllUserIdsByGroupIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryFaceCustomUserIdByUserIdRequest(TeaModel):
    def __init__(
        self,
        isolation_id: str = None,
        user_id: str = None,
    ):
        self.isolation_id = isolation_id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.isolation_id is not None:
            result['IsolationId'] = self.isolation_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsolationId') is not None:
            self.isolation_id = m.get('IsolationId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class QueryFaceCustomUserIdByUserIdResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_message = error_message
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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryFaceCustomUserIdByUserIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryFaceCustomUserIdByUserIdResponseBody = None,
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
            temp_model = QueryFaceCustomUserIdByUserIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryFaceDeviceGroupsByDeviceRequest(TeaModel):
    def __init__(
        self,
        device_name: str = None,
        iot_instance_id: str = None,
        isolation_id: str = None,
        page_no: int = None,
        page_size: int = None,
        product_key: str = None,
    ):
        self.device_name = device_name
        self.iot_instance_id = iot_instance_id
        self.isolation_id = isolation_id
        self.page_no = page_no
        self.page_size = page_size
        self.product_key = product_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.isolation_id is not None:
            result['IsolationId'] = self.isolation_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('IsolationId') is not None:
            self.isolation_id = m.get('IsolationId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        return self


class QueryFaceDeviceGroupsByDeviceResponseBodyDataDeviceGroupList(TeaModel):
    def __init__(
        self,
        device_group_id: str = None,
        device_group_name: str = None,
        modified_time: str = None,
    ):
        self.device_group_id = device_group_id
        self.device_group_name = device_group_name
        self.modified_time = modified_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_group_id is not None:
            result['DeviceGroupId'] = self.device_group_id
        if self.device_group_name is not None:
            result['DeviceGroupName'] = self.device_group_name
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceGroupId') is not None:
            self.device_group_id = m.get('DeviceGroupId')
        if m.get('DeviceGroupName') is not None:
            self.device_group_name = m.get('DeviceGroupName')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        return self


class QueryFaceDeviceGroupsByDeviceResponseBodyData(TeaModel):
    def __init__(
        self,
        device_group_list: List[QueryFaceDeviceGroupsByDeviceResponseBodyDataDeviceGroupList] = None,
        page_no: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.device_group_list = device_group_list
        self.page_no = page_no
        self.page_size = page_size
        self.total = total

    def validate(self):
        if self.device_group_list:
            for k in self.device_group_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DeviceGroupList'] = []
        if self.device_group_list is not None:
            for k in self.device_group_list:
                result['DeviceGroupList'].append(k.to_map() if k else None)
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.device_group_list = []
        if m.get('DeviceGroupList') is not None:
            for k in m.get('DeviceGroupList'):
                temp_model = QueryFaceDeviceGroupsByDeviceResponseBodyDataDeviceGroupList()
                self.device_group_list.append(temp_model.from_map(k))
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class QueryFaceDeviceGroupsByDeviceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: QueryFaceDeviceGroupsByDeviceResponseBodyData = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_message = error_message
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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = QueryFaceDeviceGroupsByDeviceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryFaceDeviceGroupsByDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryFaceDeviceGroupsByDeviceResponseBody = None,
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
            temp_model = QueryFaceDeviceGroupsByDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryFaceUserRequest(TeaModel):
    def __init__(
        self,
        isolation_id: str = None,
        user_id: str = None,
    ):
        self.isolation_id = isolation_id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.isolation_id is not None:
            result['IsolationId'] = self.isolation_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsolationId') is not None:
            self.isolation_id = m.get('IsolationId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class QueryFaceUserResponseBodyDataFacePicListFeatureDTOList(TeaModel):
    def __init__(
        self,
        algorithm_name: str = None,
        algorithm_provider: str = None,
        algorithm_version: str = None,
        error_code: str = None,
        error_message: str = None,
        face_md_5: str = None,
    ):
        self.algorithm_name = algorithm_name
        self.algorithm_provider = algorithm_provider
        self.algorithm_version = algorithm_version
        self.error_code = error_code
        self.error_message = error_message
        self.face_md_5 = face_md_5

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm_name is not None:
            result['AlgorithmName'] = self.algorithm_name
        if self.algorithm_provider is not None:
            result['AlgorithmProvider'] = self.algorithm_provider
        if self.algorithm_version is not None:
            result['AlgorithmVersion'] = self.algorithm_version
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.face_md_5 is not None:
            result['FaceMd5'] = self.face_md_5
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlgorithmName') is not None:
            self.algorithm_name = m.get('AlgorithmName')
        if m.get('AlgorithmProvider') is not None:
            self.algorithm_provider = m.get('AlgorithmProvider')
        if m.get('AlgorithmVersion') is not None:
            self.algorithm_version = m.get('AlgorithmVersion')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('FaceMd5') is not None:
            self.face_md_5 = m.get('FaceMd5')
        return self


class QueryFaceUserResponseBodyDataFacePicList(TeaModel):
    def __init__(
        self,
        face_md_5: str = None,
        face_url: str = None,
        feature_dtolist: List[QueryFaceUserResponseBodyDataFacePicListFeatureDTOList] = None,
    ):
        self.face_md_5 = face_md_5
        self.face_url = face_url
        self.feature_dtolist = feature_dtolist

    def validate(self):
        if self.feature_dtolist:
            for k in self.feature_dtolist:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.face_md_5 is not None:
            result['FaceMd5'] = self.face_md_5
        if self.face_url is not None:
            result['FaceUrl'] = self.face_url
        result['FeatureDTOList'] = []
        if self.feature_dtolist is not None:
            for k in self.feature_dtolist:
                result['FeatureDTOList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FaceMd5') is not None:
            self.face_md_5 = m.get('FaceMd5')
        if m.get('FaceUrl') is not None:
            self.face_url = m.get('FaceUrl')
        self.feature_dtolist = []
        if m.get('FeatureDTOList') is not None:
            for k in m.get('FeatureDTOList'):
                temp_model = QueryFaceUserResponseBodyDataFacePicListFeatureDTOList()
                self.feature_dtolist.append(temp_model.from_map(k))
        return self


class QueryFaceUserResponseBodyData(TeaModel):
    def __init__(
        self,
        custom_user_id: str = None,
        face_pic_list: List[QueryFaceUserResponseBodyDataFacePicList] = None,
        name: str = None,
        params: str = None,
        user_id: str = None,
    ):
        self.custom_user_id = custom_user_id
        self.face_pic_list = face_pic_list
        self.name = name
        self.params = params
        self.user_id = user_id

    def validate(self):
        if self.face_pic_list:
            for k in self.face_pic_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_user_id is not None:
            result['CustomUserId'] = self.custom_user_id
        result['FacePicList'] = []
        if self.face_pic_list is not None:
            for k in self.face_pic_list:
                result['FacePicList'].append(k.to_map() if k else None)
        if self.name is not None:
            result['Name'] = self.name
        if self.params is not None:
            result['Params'] = self.params
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomUserId') is not None:
            self.custom_user_id = m.get('CustomUserId')
        self.face_pic_list = []
        if m.get('FacePicList') is not None:
            for k in m.get('FacePicList'):
                temp_model = QueryFaceUserResponseBodyDataFacePicList()
                self.face_pic_list.append(temp_model.from_map(k))
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Params') is not None:
            self.params = m.get('Params')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class QueryFaceUserResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: QueryFaceUserResponseBodyData = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_message = error_message
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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = QueryFaceUserResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryFaceUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryFaceUserResponseBody = None,
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
            temp_model = QueryFaceUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryFaceUserBatchRequest(TeaModel):
    def __init__(
        self,
        isolation_id: str = None,
        user_id_list: List[str] = None,
    ):
        self.isolation_id = isolation_id
        self.user_id_list = user_id_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.isolation_id is not None:
            result['IsolationId'] = self.isolation_id
        if self.user_id_list is not None:
            result['UserIdList'] = self.user_id_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsolationId') is not None:
            self.isolation_id = m.get('IsolationId')
        if m.get('UserIdList') is not None:
            self.user_id_list = m.get('UserIdList')
        return self


class QueryFaceUserBatchResponseBodyDataFacePicListFeatureDTOList(TeaModel):
    def __init__(
        self,
        algorithm_name: str = None,
        algorithm_provider: str = None,
        algorithm_version: str = None,
        error_code: str = None,
        error_message: str = None,
        face_md_5: str = None,
    ):
        self.algorithm_name = algorithm_name
        self.algorithm_provider = algorithm_provider
        self.algorithm_version = algorithm_version
        self.error_code = error_code
        self.error_message = error_message
        self.face_md_5 = face_md_5

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm_name is not None:
            result['AlgorithmName'] = self.algorithm_name
        if self.algorithm_provider is not None:
            result['AlgorithmProvider'] = self.algorithm_provider
        if self.algorithm_version is not None:
            result['AlgorithmVersion'] = self.algorithm_version
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.face_md_5 is not None:
            result['FaceMd5'] = self.face_md_5
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlgorithmName') is not None:
            self.algorithm_name = m.get('AlgorithmName')
        if m.get('AlgorithmProvider') is not None:
            self.algorithm_provider = m.get('AlgorithmProvider')
        if m.get('AlgorithmVersion') is not None:
            self.algorithm_version = m.get('AlgorithmVersion')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('FaceMd5') is not None:
            self.face_md_5 = m.get('FaceMd5')
        return self


class QueryFaceUserBatchResponseBodyDataFacePicList(TeaModel):
    def __init__(
        self,
        face_md_5: str = None,
        face_url: str = None,
        feature_dtolist: List[QueryFaceUserBatchResponseBodyDataFacePicListFeatureDTOList] = None,
    ):
        self.face_md_5 = face_md_5
        self.face_url = face_url
        self.feature_dtolist = feature_dtolist

    def validate(self):
        if self.feature_dtolist:
            for k in self.feature_dtolist:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.face_md_5 is not None:
            result['FaceMd5'] = self.face_md_5
        if self.face_url is not None:
            result['FaceUrl'] = self.face_url
        result['FeatureDTOList'] = []
        if self.feature_dtolist is not None:
            for k in self.feature_dtolist:
                result['FeatureDTOList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FaceMd5') is not None:
            self.face_md_5 = m.get('FaceMd5')
        if m.get('FaceUrl') is not None:
            self.face_url = m.get('FaceUrl')
        self.feature_dtolist = []
        if m.get('FeatureDTOList') is not None:
            for k in m.get('FeatureDTOList'):
                temp_model = QueryFaceUserBatchResponseBodyDataFacePicListFeatureDTOList()
                self.feature_dtolist.append(temp_model.from_map(k))
        return self


class QueryFaceUserBatchResponseBodyData(TeaModel):
    def __init__(
        self,
        create_time: int = None,
        custom_user_id: str = None,
        face_pic_list: List[QueryFaceUserBatchResponseBodyDataFacePicList] = None,
        modify_time: int = None,
        name: str = None,
        params: str = None,
        user_id: str = None,
    ):
        self.create_time = create_time
        self.custom_user_id = custom_user_id
        self.face_pic_list = face_pic_list
        self.modify_time = modify_time
        self.name = name
        self.params = params
        self.user_id = user_id

    def validate(self):
        if self.face_pic_list:
            for k in self.face_pic_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.custom_user_id is not None:
            result['CustomUserId'] = self.custom_user_id
        result['FacePicList'] = []
        if self.face_pic_list is not None:
            for k in self.face_pic_list:
                result['FacePicList'].append(k.to_map() if k else None)
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.name is not None:
            result['Name'] = self.name
        if self.params is not None:
            result['Params'] = self.params
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CustomUserId') is not None:
            self.custom_user_id = m.get('CustomUserId')
        self.face_pic_list = []
        if m.get('FacePicList') is not None:
            for k in m.get('FacePicList'):
                temp_model = QueryFaceUserBatchResponseBodyDataFacePicList()
                self.face_pic_list.append(temp_model.from_map(k))
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Params') is not None:
            self.params = m.get('Params')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class QueryFaceUserBatchResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[QueryFaceUserBatchResponseBodyData] = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_message = error_message
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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
                temp_model = QueryFaceUserBatchResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryFaceUserBatchResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryFaceUserBatchResponseBody = None,
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
            temp_model = QueryFaceUserBatchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryFaceUserByNameRequest(TeaModel):
    def __init__(
        self,
        isolation_id: str = None,
        name: str = None,
        page_no: int = None,
        page_size: int = None,
        params: str = None,
    ):
        self.isolation_id = isolation_id
        self.name = name
        self.page_no = page_no
        self.page_size = page_size
        self.params = params

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.isolation_id is not None:
            result['IsolationId'] = self.isolation_id
        if self.name is not None:
            result['Name'] = self.name
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.params is not None:
            result['Params'] = self.params
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsolationId') is not None:
            self.isolation_id = m.get('IsolationId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Params') is not None:
            self.params = m.get('Params')
        return self


class QueryFaceUserByNameResponseBodyDataListFacePicListFeatureDTOList(TeaModel):
    def __init__(
        self,
        algorithm_name: str = None,
        algorithm_provider: str = None,
        algorithm_version: str = None,
        error_code: str = None,
        error_message: str = None,
        face_md_5: str = None,
    ):
        self.algorithm_name = algorithm_name
        self.algorithm_provider = algorithm_provider
        self.algorithm_version = algorithm_version
        self.error_code = error_code
        self.error_message = error_message
        self.face_md_5 = face_md_5

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm_name is not None:
            result['AlgorithmName'] = self.algorithm_name
        if self.algorithm_provider is not None:
            result['AlgorithmProvider'] = self.algorithm_provider
        if self.algorithm_version is not None:
            result['AlgorithmVersion'] = self.algorithm_version
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.face_md_5 is not None:
            result['FaceMd5'] = self.face_md_5
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlgorithmName') is not None:
            self.algorithm_name = m.get('AlgorithmName')
        if m.get('AlgorithmProvider') is not None:
            self.algorithm_provider = m.get('AlgorithmProvider')
        if m.get('AlgorithmVersion') is not None:
            self.algorithm_version = m.get('AlgorithmVersion')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('FaceMd5') is not None:
            self.face_md_5 = m.get('FaceMd5')
        return self


class QueryFaceUserByNameResponseBodyDataListFacePicList(TeaModel):
    def __init__(
        self,
        face_md_5: str = None,
        face_url: str = None,
        feature_dtolist: List[QueryFaceUserByNameResponseBodyDataListFacePicListFeatureDTOList] = None,
    ):
        self.face_md_5 = face_md_5
        self.face_url = face_url
        self.feature_dtolist = feature_dtolist

    def validate(self):
        if self.feature_dtolist:
            for k in self.feature_dtolist:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.face_md_5 is not None:
            result['FaceMd5'] = self.face_md_5
        if self.face_url is not None:
            result['FaceUrl'] = self.face_url
        result['FeatureDTOList'] = []
        if self.feature_dtolist is not None:
            for k in self.feature_dtolist:
                result['FeatureDTOList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FaceMd5') is not None:
            self.face_md_5 = m.get('FaceMd5')
        if m.get('FaceUrl') is not None:
            self.face_url = m.get('FaceUrl')
        self.feature_dtolist = []
        if m.get('FeatureDTOList') is not None:
            for k in m.get('FeatureDTOList'):
                temp_model = QueryFaceUserByNameResponseBodyDataListFacePicListFeatureDTOList()
                self.feature_dtolist.append(temp_model.from_map(k))
        return self


class QueryFaceUserByNameResponseBodyDataList(TeaModel):
    def __init__(
        self,
        create_time: int = None,
        custom_user_id: str = None,
        face_pic_list: List[QueryFaceUserByNameResponseBodyDataListFacePicList] = None,
        modify_time: int = None,
        name: str = None,
        params: str = None,
        user_id: str = None,
    ):
        self.create_time = create_time
        self.custom_user_id = custom_user_id
        self.face_pic_list = face_pic_list
        self.modify_time = modify_time
        self.name = name
        self.params = params
        self.user_id = user_id

    def validate(self):
        if self.face_pic_list:
            for k in self.face_pic_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.custom_user_id is not None:
            result['CustomUserId'] = self.custom_user_id
        result['FacePicList'] = []
        if self.face_pic_list is not None:
            for k in self.face_pic_list:
                result['FacePicList'].append(k.to_map() if k else None)
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.name is not None:
            result['Name'] = self.name
        if self.params is not None:
            result['Params'] = self.params
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CustomUserId') is not None:
            self.custom_user_id = m.get('CustomUserId')
        self.face_pic_list = []
        if m.get('FacePicList') is not None:
            for k in m.get('FacePicList'):
                temp_model = QueryFaceUserByNameResponseBodyDataListFacePicList()
                self.face_pic_list.append(temp_model.from_map(k))
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Params') is not None:
            self.params = m.get('Params')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class QueryFaceUserByNameResponseBodyData(TeaModel):
    def __init__(
        self,
        list: List[QueryFaceUserByNameResponseBodyDataList] = None,
        page: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.list = list
        self.page = page
        self.page_size = page_size
        self.total = total

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = QueryFaceUserByNameResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class QueryFaceUserByNameResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: QueryFaceUserByNameResponseBodyData = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_message = error_message
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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = QueryFaceUserByNameResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryFaceUserByNameResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryFaceUserByNameResponseBody = None,
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
            temp_model = QueryFaceUserByNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryFaceUserGroupRequest(TeaModel):
    def __init__(
        self,
        isolation_id: str = None,
        page_no: int = None,
        page_size: int = None,
        user_id: str = None,
    ):
        self.isolation_id = isolation_id
        self.page_no = page_no
        self.page_size = page_size
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.isolation_id is not None:
            result['IsolationId'] = self.isolation_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsolationId') is not None:
            self.isolation_id = m.get('IsolationId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class QueryFaceUserGroupResponseBodyDataUserGroupList(TeaModel):
    def __init__(
        self,
        modified_time: str = None,
        user_group_id: str = None,
        user_group_name: str = None,
    ):
        self.modified_time = modified_time
        self.user_group_id = user_group_id
        self.user_group_name = user_group_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        if self.user_group_name is not None:
            result['UserGroupName'] = self.user_group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        if m.get('UserGroupName') is not None:
            self.user_group_name = m.get('UserGroupName')
        return self


class QueryFaceUserGroupResponseBodyData(TeaModel):
    def __init__(
        self,
        page_no: int = None,
        page_size: int = None,
        total: int = None,
        user_group_list: List[QueryFaceUserGroupResponseBodyDataUserGroupList] = None,
    ):
        self.page_no = page_no
        self.page_size = page_size
        self.total = total
        self.user_group_list = user_group_list

    def validate(self):
        if self.user_group_list:
            for k in self.user_group_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        result['UserGroupList'] = []
        if self.user_group_list is not None:
            for k in self.user_group_list:
                result['UserGroupList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        self.user_group_list = []
        if m.get('UserGroupList') is not None:
            for k in m.get('UserGroupList'):
                temp_model = QueryFaceUserGroupResponseBodyDataUserGroupList()
                self.user_group_list.append(temp_model.from_map(k))
        return self


class QueryFaceUserGroupResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: QueryFaceUserGroupResponseBodyData = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_message = error_message
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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = QueryFaceUserGroupResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryFaceUserGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryFaceUserGroupResponseBody = None,
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
            temp_model = QueryFaceUserGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryFaceUserGroupAndDeviceGroupRelationRequest(TeaModel):
    def __init__(
        self,
        control_id: str = None,
        isolation_id: str = None,
    ):
        self.control_id = control_id
        self.isolation_id = isolation_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.control_id is not None:
            result['ControlId'] = self.control_id
        if self.isolation_id is not None:
            result['IsolationId'] = self.isolation_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ControlId') is not None:
            self.control_id = m.get('ControlId')
        if m.get('IsolationId') is not None:
            self.isolation_id = m.get('IsolationId')
        return self


class QueryFaceUserGroupAndDeviceGroupRelationResponseBodyData(TeaModel):
    def __init__(
        self,
        control_id: str = None,
        control_type: str = None,
        device_group_id: str = None,
        modified_time: str = None,
        user_group_id: str = None,
    ):
        self.control_id = control_id
        self.control_type = control_type
        self.device_group_id = device_group_id
        self.modified_time = modified_time
        self.user_group_id = user_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.control_id is not None:
            result['ControlId'] = self.control_id
        if self.control_type is not None:
            result['ControlType'] = self.control_type
        if self.device_group_id is not None:
            result['DeviceGroupId'] = self.device_group_id
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ControlId') is not None:
            self.control_id = m.get('ControlId')
        if m.get('ControlType') is not None:
            self.control_type = m.get('ControlType')
        if m.get('DeviceGroupId') is not None:
            self.device_group_id = m.get('DeviceGroupId')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        return self


class QueryFaceUserGroupAndDeviceGroupRelationResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: QueryFaceUserGroupAndDeviceGroupRelationResponseBodyData = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_message = error_message
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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = QueryFaceUserGroupAndDeviceGroupRelationResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryFaceUserGroupAndDeviceGroupRelationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryFaceUserGroupAndDeviceGroupRelationResponseBody = None,
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
            temp_model = QueryFaceUserGroupAndDeviceGroupRelationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryFaceUserIdByCustomUserIdRequest(TeaModel):
    def __init__(
        self,
        custom_user_id: str = None,
        isolation_id: str = None,
    ):
        self.custom_user_id = custom_user_id
        self.isolation_id = isolation_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_user_id is not None:
            result['CustomUserId'] = self.custom_user_id
        if self.isolation_id is not None:
            result['IsolationId'] = self.isolation_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomUserId') is not None:
            self.custom_user_id = m.get('CustomUserId')
        if m.get('IsolationId') is not None:
            self.isolation_id = m.get('IsolationId')
        return self


class QueryFaceUserIdByCustomUserIdResponseBodyData(TeaModel):
    def __init__(
        self,
        custom_user_id: str = None,
        name: str = None,
        params: str = None,
        user_id: str = None,
    ):
        self.custom_user_id = custom_user_id
        self.name = name
        self.params = params
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_user_id is not None:
            result['CustomUserId'] = self.custom_user_id
        if self.name is not None:
            result['Name'] = self.name
        if self.params is not None:
            result['Params'] = self.params
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomUserId') is not None:
            self.custom_user_id = m.get('CustomUserId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Params') is not None:
            self.params = m.get('Params')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class QueryFaceUserIdByCustomUserIdResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: QueryFaceUserIdByCustomUserIdResponseBodyData = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_message = error_message
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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = QueryFaceUserIdByCustomUserIdResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryFaceUserIdByCustomUserIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryFaceUserIdByCustomUserIdResponseBody = None,
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
            temp_model = QueryFaceUserIdByCustomUserIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryGbSubDeviceListRequest(TeaModel):
    def __init__(
        self,
        device_name: str = None,
        iot_id: str = None,
        iot_instance_id: str = None,
        page_size: int = None,
        page_start: int = None,
        product_key: str = None,
    ):
        self.device_name = device_name
        self.iot_id = iot_id
        self.iot_instance_id = iot_instance_id
        self.page_size = page_size
        self.page_start = page_start
        self.product_key = product_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_start is not None:
            result['PageStart'] = self.page_start
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageStart') is not None:
            self.page_start = m.get('PageStart')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        return self


class QueryGbSubDeviceListResponseBodyDataGbSubDeviceList(TeaModel):
    def __init__(
        self,
        device_enable: int = None,
        device_id: str = None,
        device_name: str = None,
        iot_id: str = None,
        product_key: str = None,
    ):
        self.device_enable = device_enable
        self.device_id = device_id
        self.device_name = device_name
        self.iot_id = iot_id
        self.product_key = product_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_enable is not None:
            result['DeviceEnable'] = self.device_enable
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceEnable') is not None:
            self.device_enable = m.get('DeviceEnable')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        return self


class QueryGbSubDeviceListResponseBodyData(TeaModel):
    def __init__(
        self,
        gb_sub_device_list: List[QueryGbSubDeviceListResponseBodyDataGbSubDeviceList] = None,
        total: int = None,
    ):
        self.gb_sub_device_list = gb_sub_device_list
        self.total = total

    def validate(self):
        if self.gb_sub_device_list:
            for k in self.gb_sub_device_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['GbSubDeviceList'] = []
        if self.gb_sub_device_list is not None:
            for k in self.gb_sub_device_list:
                result['GbSubDeviceList'].append(k.to_map() if k else None)
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.gb_sub_device_list = []
        if m.get('GbSubDeviceList') is not None:
            for k in m.get('GbSubDeviceList'):
                temp_model = QueryGbSubDeviceListResponseBodyDataGbSubDeviceList()
                self.gb_sub_device_list.append(temp_model.from_map(k))
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class QueryGbSubDeviceListResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: QueryGbSubDeviceListResponseBodyData = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_message = error_message
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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = QueryGbSubDeviceListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryGbSubDeviceListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryGbSubDeviceListResponseBody = None,
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
            temp_model = QueryGbSubDeviceListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryLiveStreamingRequest(TeaModel):
    def __init__(
        self,
        cache_duration: int = None,
        device_name: str = None,
        enable_stun: bool = None,
        encrypt_type: int = None,
        force_iframe: bool = None,
        iot_id: str = None,
        iot_instance_id: str = None,
        play_un_limited: bool = None,
        product_key: str = None,
        scheme: str = None,
        should_encrypt: bool = None,
        stream_type: int = None,
        url_valid_duration: int = None,
    ):
        self.cache_duration = cache_duration
        self.device_name = device_name
        self.enable_stun = enable_stun
        self.encrypt_type = encrypt_type
        self.force_iframe = force_iframe
        self.iot_id = iot_id
        self.iot_instance_id = iot_instance_id
        self.play_un_limited = play_un_limited
        self.product_key = product_key
        self.scheme = scheme
        self.should_encrypt = should_encrypt
        self.stream_type = stream_type
        self.url_valid_duration = url_valid_duration

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cache_duration is not None:
            result['CacheDuration'] = self.cache_duration
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.enable_stun is not None:
            result['EnableStun'] = self.enable_stun
        if self.encrypt_type is not None:
            result['EncryptType'] = self.encrypt_type
        if self.force_iframe is not None:
            result['ForceIFrame'] = self.force_iframe
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.play_un_limited is not None:
            result['PlayUnLimited'] = self.play_un_limited
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        if self.scheme is not None:
            result['Scheme'] = self.scheme
        if self.should_encrypt is not None:
            result['ShouldEncrypt'] = self.should_encrypt
        if self.stream_type is not None:
            result['StreamType'] = self.stream_type
        if self.url_valid_duration is not None:
            result['UrlValidDuration'] = self.url_valid_duration
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CacheDuration') is not None:
            self.cache_duration = m.get('CacheDuration')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('EnableStun') is not None:
            self.enable_stun = m.get('EnableStun')
        if m.get('EncryptType') is not None:
            self.encrypt_type = m.get('EncryptType')
        if m.get('ForceIFrame') is not None:
            self.force_iframe = m.get('ForceIFrame')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('PlayUnLimited') is not None:
            self.play_un_limited = m.get('PlayUnLimited')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        if m.get('Scheme') is not None:
            self.scheme = m.get('Scheme')
        if m.get('ShouldEncrypt') is not None:
            self.should_encrypt = m.get('ShouldEncrypt')
        if m.get('StreamType') is not None:
            self.stream_type = m.get('StreamType')
        if m.get('UrlValidDuration') is not None:
            self.url_valid_duration = m.get('UrlValidDuration')
        return self


class QueryLiveStreamingResponseBodyData(TeaModel):
    def __init__(
        self,
        path: str = None,
        relay_decrypt_key: str = None,
        stun_info: str = None,
    ):
        self.path = path
        self.relay_decrypt_key = relay_decrypt_key
        self.stun_info = stun_info

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.path is not None:
            result['Path'] = self.path
        if self.relay_decrypt_key is not None:
            result['RelayDecryptKey'] = self.relay_decrypt_key
        if self.stun_info is not None:
            result['StunInfo'] = self.stun_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('RelayDecryptKey') is not None:
            self.relay_decrypt_key = m.get('RelayDecryptKey')
        if m.get('StunInfo') is not None:
            self.stun_info = m.get('StunInfo')
        return self


class QueryLiveStreamingResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: QueryLiveStreamingResponseBodyData = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_message = error_message
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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = QueryLiveStreamingResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryLiveStreamingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryLiveStreamingResponseBody = None,
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
            temp_model = QueryLiveStreamingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryLocalFileUploadJobRequest(TeaModel):
    def __init__(
        self,
        iot_instance_id: str = None,
        job_id: str = None,
    ):
        self.iot_instance_id = iot_instance_id
        self.job_id = job_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class QueryLocalFileUploadJobResponseBodyDataResultListFileList(TeaModel):
    def __init__(
        self,
        file_end_time: int = None,
        file_name: str = None,
        file_start_time: int = None,
    ):
        self.file_end_time = file_end_time
        self.file_name = file_name
        self.file_start_time = file_start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_end_time is not None:
            result['FileEndTime'] = self.file_end_time
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_start_time is not None:
            result['FileStartTime'] = self.file_start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileEndTime') is not None:
            self.file_end_time = m.get('FileEndTime')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileStartTime') is not None:
            self.file_start_time = m.get('FileStartTime')
        return self


class QueryLocalFileUploadJobResponseBodyDataResultList(TeaModel):
    def __init__(
        self,
        code: int = None,
        device_name: str = None,
        file_list: List[QueryLocalFileUploadJobResponseBodyDataResultListFileList] = None,
        iot_id: str = None,
        product_key: str = None,
        slot_end_time: int = None,
        slot_start_time: int = None,
        slot_status: int = None,
    ):
        self.code = code
        self.device_name = device_name
        self.file_list = file_list
        self.iot_id = iot_id
        self.product_key = product_key
        self.slot_end_time = slot_end_time
        self.slot_start_time = slot_start_time
        self.slot_status = slot_status

    def validate(self):
        if self.file_list:
            for k in self.file_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        result['FileList'] = []
        if self.file_list is not None:
            for k in self.file_list:
                result['FileList'].append(k.to_map() if k else None)
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        if self.slot_end_time is not None:
            result['SlotEndTime'] = self.slot_end_time
        if self.slot_start_time is not None:
            result['SlotStartTime'] = self.slot_start_time
        if self.slot_status is not None:
            result['SlotStatus'] = self.slot_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        self.file_list = []
        if m.get('FileList') is not None:
            for k in m.get('FileList'):
                temp_model = QueryLocalFileUploadJobResponseBodyDataResultListFileList()
                self.file_list.append(temp_model.from_map(k))
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        if m.get('SlotEndTime') is not None:
            self.slot_end_time = m.get('SlotEndTime')
        if m.get('SlotStartTime') is not None:
            self.slot_start_time = m.get('SlotStartTime')
        if m.get('SlotStatus') is not None:
            self.slot_status = m.get('SlotStatus')
        return self


class QueryLocalFileUploadJobResponseBodyData(TeaModel):
    def __init__(
        self,
        result_list: List[QueryLocalFileUploadJobResponseBodyDataResultList] = None,
        status: int = None,
    ):
        self.result_list = result_list
        self.status = status

    def validate(self):
        if self.result_list:
            for k in self.result_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ResultList'] = []
        if self.result_list is not None:
            for k in self.result_list:
                result['ResultList'].append(k.to_map() if k else None)
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.result_list = []
        if m.get('ResultList') is not None:
            for k in m.get('ResultList'):
                temp_model = QueryLocalFileUploadJobResponseBodyDataResultList()
                self.result_list.append(temp_model.from_map(k))
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class QueryLocalFileUploadJobResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: QueryLocalFileUploadJobResponseBodyData = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_message = error_message
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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = QueryLocalFileUploadJobResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryLocalFileUploadJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryLocalFileUploadJobResponseBody = None,
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
            temp_model = QueryLocalFileUploadJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryMonthRecordRequest(TeaModel):
    def __init__(
        self,
        device_name: str = None,
        iot_id: str = None,
        iot_instance_id: str = None,
        month: str = None,
        product_key: str = None,
    ):
        self.device_name = device_name
        self.iot_id = iot_id
        self.iot_instance_id = iot_instance_id
        self.month = month
        self.product_key = product_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.month is not None:
            result['Month'] = self.month
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('Month') is not None:
            self.month = m.get('Month')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        return self


class QueryMonthRecordResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_message = error_message
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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryMonthRecordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryMonthRecordResponseBody = None,
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
            temp_model = QueryMonthRecordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryPictureFilesRequest(TeaModel):
    def __init__(
        self,
        begin_time: int = None,
        current_page: int = None,
        device_name: str = None,
        end_time: int = None,
        iot_id: str = None,
        iot_instance_id: str = None,
        page_size: int = None,
        picture_source: int = None,
        picture_type: int = None,
        product_key: str = None,
    ):
        self.begin_time = begin_time
        self.current_page = current_page
        self.device_name = device_name
        self.end_time = end_time
        self.iot_id = iot_id
        self.iot_instance_id = iot_instance_id
        self.page_size = page_size
        self.picture_source = picture_source
        self.picture_type = picture_type
        self.product_key = product_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.picture_source is not None:
            result['PictureSource'] = self.picture_source
        if self.picture_type is not None:
            result['PictureType'] = self.picture_type
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PictureSource') is not None:
            self.picture_source = m.get('PictureSource')
        if m.get('PictureType') is not None:
            self.picture_type = m.get('PictureType')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        return self


class QueryPictureFilesResponseBodyDataList(TeaModel):
    def __init__(
        self,
        iot_id: str = None,
        pic_create_time: int = None,
        pic_id: str = None,
        pic_url: str = None,
        thumb_url: str = None,
    ):
        self.iot_id = iot_id
        self.pic_create_time = pic_create_time
        self.pic_id = pic_id
        self.pic_url = pic_url
        self.thumb_url = thumb_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.pic_create_time is not None:
            result['PicCreateTime'] = self.pic_create_time
        if self.pic_id is not None:
            result['PicId'] = self.pic_id
        if self.pic_url is not None:
            result['PicUrl'] = self.pic_url
        if self.thumb_url is not None:
            result['ThumbUrl'] = self.thumb_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('PicCreateTime') is not None:
            self.pic_create_time = m.get('PicCreateTime')
        if m.get('PicId') is not None:
            self.pic_id = m.get('PicId')
        if m.get('PicUrl') is not None:
            self.pic_url = m.get('PicUrl')
        if m.get('ThumbUrl') is not None:
            self.thumb_url = m.get('ThumbUrl')
        return self


class QueryPictureFilesResponseBodyData(TeaModel):
    def __init__(
        self,
        list: List[QueryPictureFilesResponseBodyDataList] = None,
        page: int = None,
        page_size: int = None,
    ):
        self.list = list
        self.page = page
        self.page_size = page_size

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = QueryPictureFilesResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class QueryPictureFilesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: QueryPictureFilesResponseBodyData = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_message = error_message
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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = QueryPictureFilesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryPictureFilesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryPictureFilesResponseBody = None,
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
            temp_model = QueryPictureFilesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryPictureSearchAiboxesRequest(TeaModel):
    def __init__(
        self,
        app_instance_id: str = None,
        current_page: int = None,
        iot_instance_id: str = None,
        page_size: int = None,
    ):
        self.app_instance_id = app_instance_id
        self.current_page = current_page
        self.iot_instance_id = iot_instance_id
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_id is not None:
            result['AppInstanceId'] = self.app_instance_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceId') is not None:
            self.app_instance_id = m.get('AppInstanceId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class QueryPictureSearchAiboxesResponseBodyDataPageData(TeaModel):
    def __init__(
        self,
        iot_id: str = None,
        nick_name: str = None,
    ):
        self.iot_id = iot_id
        self.nick_name = nick_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.nick_name is not None:
            result['NickName'] = self.nick_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('NickName') is not None:
            self.nick_name = m.get('NickName')
        return self


class QueryPictureSearchAiboxesResponseBodyData(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        page_count: int = None,
        page_data: List[QueryPictureSearchAiboxesResponseBodyDataPageData] = None,
        page_size: int = None,
        total: int = None,
    ):
        self.current_page = current_page
        self.page_count = page_count
        self.page_data = page_data
        self.page_size = page_size
        self.total = total

    def validate(self):
        if self.page_data:
            for k in self.page_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        result['PageData'] = []
        if self.page_data is not None:
            for k in self.page_data:
                result['PageData'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        self.page_data = []
        if m.get('PageData') is not None:
            for k in m.get('PageData'):
                temp_model = QueryPictureSearchAiboxesResponseBodyDataPageData()
                self.page_data.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class QueryPictureSearchAiboxesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: QueryPictureSearchAiboxesResponseBodyData = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_message = error_message
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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = QueryPictureSearchAiboxesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryPictureSearchAiboxesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryPictureSearchAiboxesResponseBody = None,
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
            temp_model = QueryPictureSearchAiboxesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryPictureSearchAppsRequest(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        iot_instance_id: str = None,
        page_size: int = None,
    ):
        self.current_page = current_page
        self.iot_instance_id = iot_instance_id
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class QueryPictureSearchAppsResponseBodyDataPageData(TeaModel):
    def __init__(
        self,
        app_instance_id: str = None,
        app_template_id: str = None,
        create_time: int = None,
        description: str = None,
        modified_time: int = None,
        name: str = None,
        version: str = None,
    ):
        self.app_instance_id = app_instance_id
        self.app_template_id = app_template_id
        self.create_time = create_time
        self.description = description
        self.modified_time = modified_time
        self.name = name
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_id is not None:
            result['AppInstanceId'] = self.app_instance_id
        if self.app_template_id is not None:
            result['AppTemplateId'] = self.app_template_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.name is not None:
            result['Name'] = self.name
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceId') is not None:
            self.app_instance_id = m.get('AppInstanceId')
        if m.get('AppTemplateId') is not None:
            self.app_template_id = m.get('AppTemplateId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class QueryPictureSearchAppsResponseBodyData(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        page_count: int = None,
        page_data: List[QueryPictureSearchAppsResponseBodyDataPageData] = None,
        page_size: int = None,
        total: int = None,
    ):
        self.current_page = current_page
        self.page_count = page_count
        self.page_data = page_data
        self.page_size = page_size
        self.total = total

    def validate(self):
        if self.page_data:
            for k in self.page_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        result['PageData'] = []
        if self.page_data is not None:
            for k in self.page_data:
                result['PageData'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        self.page_data = []
        if m.get('PageData') is not None:
            for k in m.get('PageData'):
                temp_model = QueryPictureSearchAppsResponseBodyDataPageData()
                self.page_data.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class QueryPictureSearchAppsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: QueryPictureSearchAppsResponseBodyData = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_message = error_message
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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = QueryPictureSearchAppsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryPictureSearchAppsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryPictureSearchAppsResponseBody = None,
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
            temp_model = QueryPictureSearchAppsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryPictureSearchDevicesRequest(TeaModel):
    def __init__(
        self,
        app_instance_id: str = None,
        current_page: int = None,
        page_size: int = None,
    ):
        self.app_instance_id = app_instance_id
        self.current_page = current_page
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_id is not None:
            result['AppInstanceId'] = self.app_instance_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceId') is not None:
            self.app_instance_id = m.get('AppInstanceId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class QueryPictureSearchDevicesResponseBodyDataPageData(TeaModel):
    def __init__(
        self,
        iot_id: str = None,
        nick_name: str = None,
    ):
        self.iot_id = iot_id
        self.nick_name = nick_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.nick_name is not None:
            result['NickName'] = self.nick_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('NickName') is not None:
            self.nick_name = m.get('NickName')
        return self


class QueryPictureSearchDevicesResponseBodyData(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        page_count: int = None,
        page_data: List[QueryPictureSearchDevicesResponseBodyDataPageData] = None,
        page_size: int = None,
        total: int = None,
    ):
        self.current_page = current_page
        self.page_count = page_count
        self.page_data = page_data
        self.page_size = page_size
        self.total = total

    def validate(self):
        if self.page_data:
            for k in self.page_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        result['PageData'] = []
        if self.page_data is not None:
            for k in self.page_data:
                result['PageData'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        self.page_data = []
        if m.get('PageData') is not None:
            for k in m.get('PageData'):
                temp_model = QueryPictureSearchDevicesResponseBodyDataPageData()
                self.page_data.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class QueryPictureSearchDevicesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: QueryPictureSearchDevicesResponseBodyData = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_message = error_message
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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = QueryPictureSearchDevicesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryPictureSearchDevicesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryPictureSearchDevicesResponseBody = None,
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
            temp_model = QueryPictureSearchDevicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryPictureSearchJobRequest(TeaModel):
    def __init__(
        self,
        app_instance_id: str = None,
        current_page: int = None,
        job_status: int = None,
        page_size: int = None,
    ):
        self.app_instance_id = app_instance_id
        self.current_page = current_page
        self.job_status = job_status
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_id is not None:
            result['AppInstanceId'] = self.app_instance_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.job_status is not None:
            result['JobStatus'] = self.job_status
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceId') is not None:
            self.app_instance_id = m.get('AppInstanceId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('JobStatus') is not None:
            self.job_status = m.get('JobStatus')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class QueryPictureSearchJobResponseBodyDataPageData(TeaModel):
    def __init__(
        self,
        create_time: int = None,
        end_time: int = None,
        job_id: str = None,
        job_status: int = None,
        search_pic_url: str = None,
        start_time: int = None,
        threshold: float = None,
    ):
        self.create_time = create_time
        self.end_time = end_time
        self.job_id = job_id
        self.job_status = job_status
        self.search_pic_url = search_pic_url
        self.start_time = start_time
        self.threshold = threshold

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.job_status is not None:
            result['JobStatus'] = self.job_status
        if self.search_pic_url is not None:
            result['SearchPicUrl'] = self.search_pic_url
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('JobStatus') is not None:
            self.job_status = m.get('JobStatus')
        if m.get('SearchPicUrl') is not None:
            self.search_pic_url = m.get('SearchPicUrl')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        return self


class QueryPictureSearchJobResponseBodyData(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        page_count: int = None,
        page_data: List[QueryPictureSearchJobResponseBodyDataPageData] = None,
        page_size: int = None,
        total: int = None,
    ):
        self.current_page = current_page
        self.page_count = page_count
        self.page_data = page_data
        self.page_size = page_size
        self.total = total

    def validate(self):
        if self.page_data:
            for k in self.page_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        result['PageData'] = []
        if self.page_data is not None:
            for k in self.page_data:
                result['PageData'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        self.page_data = []
        if m.get('PageData') is not None:
            for k in m.get('PageData'):
                temp_model = QueryPictureSearchJobResponseBodyDataPageData()
                self.page_data.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class QueryPictureSearchJobResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: QueryPictureSearchJobResponseBodyData = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_message = error_message
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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = QueryPictureSearchJobResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryPictureSearchJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryPictureSearchJobResponseBody = None,
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
            temp_model = QueryPictureSearchJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryPictureSearchJobResultRequest(TeaModel):
    def __init__(
        self,
        app_instance_id: str = None,
        current_page: int = None,
        job_id: str = None,
        page_size: int = None,
    ):
        self.app_instance_id = app_instance_id
        self.current_page = current_page
        self.job_id = job_id
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_id is not None:
            result['AppInstanceId'] = self.app_instance_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceId') is not None:
            self.app_instance_id = m.get('AppInstanceId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class QueryPictureSearchJobResultResponseBodyDataPageData(TeaModel):
    def __init__(
        self,
        device_nick_name: str = None,
        event_time: int = None,
        gateway_iot_id: str = None,
        iot_id: str = None,
        pic_url: str = None,
        threshold: float = None,
        vector_id: str = None,
    ):
        self.device_nick_name = device_nick_name
        self.event_time = event_time
        self.gateway_iot_id = gateway_iot_id
        self.iot_id = iot_id
        self.pic_url = pic_url
        self.threshold = threshold
        self.vector_id = vector_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_nick_name is not None:
            result['DeviceNickName'] = self.device_nick_name
        if self.event_time is not None:
            result['EventTime'] = self.event_time
        if self.gateway_iot_id is not None:
            result['GatewayIotId'] = self.gateway_iot_id
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.pic_url is not None:
            result['PicUrl'] = self.pic_url
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        if self.vector_id is not None:
            result['VectorId'] = self.vector_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceNickName') is not None:
            self.device_nick_name = m.get('DeviceNickName')
        if m.get('EventTime') is not None:
            self.event_time = m.get('EventTime')
        if m.get('GatewayIotId') is not None:
            self.gateway_iot_id = m.get('GatewayIotId')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('PicUrl') is not None:
            self.pic_url = m.get('PicUrl')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        if m.get('VectorId') is not None:
            self.vector_id = m.get('VectorId')
        return self


class QueryPictureSearchJobResultResponseBodyData(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        page_count: int = None,
        page_data: List[QueryPictureSearchJobResultResponseBodyDataPageData] = None,
        page_size: int = None,
        total: int = None,
    ):
        self.current_page = current_page
        self.page_count = page_count
        self.page_data = page_data
        self.page_size = page_size
        self.total = total

    def validate(self):
        if self.page_data:
            for k in self.page_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        result['PageData'] = []
        if self.page_data is not None:
            for k in self.page_data:
                result['PageData'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        self.page_data = []
        if m.get('PageData') is not None:
            for k in m.get('PageData'):
                temp_model = QueryPictureSearchJobResultResponseBodyDataPageData()
                self.page_data.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class QueryPictureSearchJobResultResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: QueryPictureSearchJobResultResponseBodyData = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_message = error_message
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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = QueryPictureSearchJobResultResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryPictureSearchJobResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryPictureSearchJobResultResponseBody = None,
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
            temp_model = QueryPictureSearchJobResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryRecordRequest(TeaModel):
    def __init__(
        self,
        begin_time: int = None,
        current_page: int = None,
        device_name: str = None,
        end_time: int = None,
        iot_id: str = None,
        iot_instance_id: str = None,
        need_snapshot: bool = None,
        page_size: int = None,
        product_key: str = None,
        record_type: int = None,
        stream_type: int = None,
    ):
        self.begin_time = begin_time
        self.current_page = current_page
        self.device_name = device_name
        self.end_time = end_time
        self.iot_id = iot_id
        self.iot_instance_id = iot_instance_id
        self.need_snapshot = need_snapshot
        self.page_size = page_size
        self.product_key = product_key
        self.record_type = record_type
        self.stream_type = stream_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.need_snapshot is not None:
            result['NeedSnapshot'] = self.need_snapshot
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        if self.record_type is not None:
            result['RecordType'] = self.record_type
        if self.stream_type is not None:
            result['StreamType'] = self.stream_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('NeedSnapshot') is not None:
            self.need_snapshot = m.get('NeedSnapshot')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        if m.get('RecordType') is not None:
            self.record_type = m.get('RecordType')
        if m.get('StreamType') is not None:
            self.stream_type = m.get('StreamType')
        return self


class QueryRecordResponseBodyDataList(TeaModel):
    def __init__(
        self,
        begin_time: str = None,
        end_time: str = None,
        event_type: int = None,
        file_name: str = None,
        file_size: int = None,
        record_type: int = None,
        snapshot_url: str = None,
        stream_type: int = None,
        video_frame_number: int = None,
    ):
        self.begin_time = begin_time
        self.end_time = end_time
        self.event_type = event_type
        self.file_name = file_name
        self.file_size = file_size
        self.record_type = record_type
        self.snapshot_url = snapshot_url
        self.stream_type = stream_type
        self.video_frame_number = video_frame_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.event_type is not None:
            result['EventType'] = self.event_type
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_size is not None:
            result['FileSize'] = self.file_size
        if self.record_type is not None:
            result['RecordType'] = self.record_type
        if self.snapshot_url is not None:
            result['SnapshotUrl'] = self.snapshot_url
        if self.stream_type is not None:
            result['StreamType'] = self.stream_type
        if self.video_frame_number is not None:
            result['VideoFrameNumber'] = self.video_frame_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')
        if m.get('RecordType') is not None:
            self.record_type = m.get('RecordType')
        if m.get('SnapshotUrl') is not None:
            self.snapshot_url = m.get('SnapshotUrl')
        if m.get('StreamType') is not None:
            self.stream_type = m.get('StreamType')
        if m.get('VideoFrameNumber') is not None:
            self.video_frame_number = m.get('VideoFrameNumber')
        return self


class QueryRecordResponseBodyData(TeaModel):
    def __init__(
        self,
        list: List[QueryRecordResponseBodyDataList] = None,
        page: int = None,
        page_size: int = None,
    ):
        self.list = list
        self.page = page
        self.page_size = page_size

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = QueryRecordResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class QueryRecordResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: QueryRecordResponseBodyData = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_message = error_message
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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = QueryRecordResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryRecordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryRecordResponseBody = None,
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
            temp_model = QueryRecordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryRecordByRecordIdRequest(TeaModel):
    def __init__(
        self,
        device_name: str = None,
        iot_id: str = None,
        iot_instance_id: str = None,
        product_key: str = None,
        record_id: str = None,
    ):
        self.device_name = device_name
        self.iot_id = iot_id
        self.iot_instance_id = iot_instance_id
        self.product_key = product_key
        self.record_id = record_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        if self.record_id is not None:
            result['RecordId'] = self.record_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')
        return self


class QueryRecordByRecordIdResponseBodyData(TeaModel):
    def __init__(
        self,
        begin_time: str = None,
        end_time: str = None,
        file_name: str = None,
        vod_url: str = None,
    ):
        self.begin_time = begin_time
        self.end_time = end_time
        self.file_name = file_name
        self.vod_url = vod_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.vod_url is not None:
            result['VodUrl'] = self.vod_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('VodUrl') is not None:
            self.vod_url = m.get('VodUrl')
        return self


class QueryRecordByRecordIdResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[QueryRecordByRecordIdResponseBodyData] = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_message = error_message
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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
                temp_model = QueryRecordByRecordIdResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryRecordByRecordIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryRecordByRecordIdResponseBody = None,
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
            temp_model = QueryRecordByRecordIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryRecordDownloadJobByIdRequest(TeaModel):
    def __init__(
        self,
        iot_instance_id: str = None,
        job_id: str = None,
    ):
        self.iot_instance_id = iot_instance_id
        self.job_id = job_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class QueryRecordDownloadJobByIdResponseBodyData(TeaModel):
    def __init__(
        self,
        begin_time: int = None,
        end_time: int = None,
        file_name: str = None,
        iot_id: str = None,
        job_error_code: int = None,
        progress: int = None,
        record_type: int = None,
        status: int = None,
        stream_type: int = None,
        type: int = None,
        url: str = None,
    ):
        self.begin_time = begin_time
        self.end_time = end_time
        self.file_name = file_name
        self.iot_id = iot_id
        self.job_error_code = job_error_code
        self.progress = progress
        self.record_type = record_type
        self.status = status
        self.stream_type = stream_type
        self.type = type
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.job_error_code is not None:
            result['JobErrorCode'] = self.job_error_code
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.record_type is not None:
            result['RecordType'] = self.record_type
        if self.status is not None:
            result['Status'] = self.status
        if self.stream_type is not None:
            result['StreamType'] = self.stream_type
        if self.type is not None:
            result['Type'] = self.type
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('JobErrorCode') is not None:
            self.job_error_code = m.get('JobErrorCode')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('RecordType') is not None:
            self.record_type = m.get('RecordType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StreamType') is not None:
            self.stream_type = m.get('StreamType')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class QueryRecordDownloadJobByIdResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: QueryRecordDownloadJobByIdResponseBodyData = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_message = error_message
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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = QueryRecordDownloadJobByIdResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryRecordDownloadJobByIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryRecordDownloadJobByIdResponseBody = None,
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
            temp_model = QueryRecordDownloadJobByIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryRecordDownloadJobListRequest(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        device_name: str = None,
        iot_id: str = None,
        iot_instance_id: str = None,
        page_size: int = None,
        product_key: str = None,
    ):
        self.current_page = current_page
        self.device_name = device_name
        self.iot_id = iot_id
        self.iot_instance_id = iot_instance_id
        self.page_size = page_size
        self.product_key = product_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        return self


class QueryRecordDownloadJobListResponseBodyDataJobList(TeaModel):
    def __init__(
        self,
        begin_time: int = None,
        end_time: int = None,
        file_name: str = None,
        iot_id: str = None,
        job_error_code: int = None,
        job_id: str = None,
        progress: int = None,
        record_type: int = None,
        status: int = None,
        stream_type: int = None,
        type: int = None,
        url: str = None,
    ):
        self.begin_time = begin_time
        self.end_time = end_time
        self.file_name = file_name
        self.iot_id = iot_id
        self.job_error_code = job_error_code
        self.job_id = job_id
        self.progress = progress
        self.record_type = record_type
        self.status = status
        self.stream_type = stream_type
        self.type = type
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.job_error_code is not None:
            result['JobErrorCode'] = self.job_error_code
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.record_type is not None:
            result['RecordType'] = self.record_type
        if self.status is not None:
            result['Status'] = self.status
        if self.stream_type is not None:
            result['StreamType'] = self.stream_type
        if self.type is not None:
            result['Type'] = self.type
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('JobErrorCode') is not None:
            self.job_error_code = m.get('JobErrorCode')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('RecordType') is not None:
            self.record_type = m.get('RecordType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StreamType') is not None:
            self.stream_type = m.get('StreamType')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class QueryRecordDownloadJobListResponseBodyData(TeaModel):
    def __init__(
        self,
        job_list: List[QueryRecordDownloadJobListResponseBodyDataJobList] = None,
        total: int = None,
    ):
        self.job_list = job_list
        self.total = total

    def validate(self):
        if self.job_list:
            for k in self.job_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['JobList'] = []
        if self.job_list is not None:
            for k in self.job_list:
                result['JobList'].append(k.to_map() if k else None)
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.job_list = []
        if m.get('JobList') is not None:
            for k in m.get('JobList'):
                temp_model = QueryRecordDownloadJobListResponseBodyDataJobList()
                self.job_list.append(temp_model.from_map(k))
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class QueryRecordDownloadJobListResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: QueryRecordDownloadJobListResponseBodyData = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_message = error_message
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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = QueryRecordDownloadJobListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryRecordDownloadJobListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryRecordDownloadJobListResponseBody = None,
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
            temp_model = QueryRecordDownloadJobListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryRecordDownloadUrlRequest(TeaModel):
    def __init__(
        self,
        device_name: str = None,
        file_name: str = None,
        iot_id: str = None,
        iot_instance_id: str = None,
        product_key: str = None,
    ):
        self.device_name = device_name
        self.file_name = file_name
        self.iot_id = iot_id
        self.iot_instance_id = iot_instance_id
        self.product_key = product_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        return self


class QueryRecordDownloadUrlResponseBodyData(TeaModel):
    def __init__(
        self,
        progress: int = None,
        status: int = None,
        url: str = None,
    ):
        self.progress = progress
        self.status = status
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.status is not None:
            result['Status'] = self.status
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class QueryRecordDownloadUrlResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: QueryRecordDownloadUrlResponseBodyData = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_message = error_message
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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = QueryRecordDownloadUrlResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryRecordDownloadUrlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryRecordDownloadUrlResponseBody = None,
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
            temp_model = QueryRecordDownloadUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryRecordPlanDetailRequest(TeaModel):
    def __init__(
        self,
        plan_id: str = None,
    ):
        self.plan_id = plan_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        return self


class QueryRecordPlanDetailResponseBodyDataTemplateInfoTimeSectionList(TeaModel):
    def __init__(
        self,
        begin: int = None,
        day_of_week: int = None,
        end: int = None,
    ):
        self.begin = begin
        self.day_of_week = day_of_week
        self.end = end

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin is not None:
            result['Begin'] = self.begin
        if self.day_of_week is not None:
            result['DayOfWeek'] = self.day_of_week
        if self.end is not None:
            result['End'] = self.end
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Begin') is not None:
            self.begin = m.get('Begin')
        if m.get('DayOfWeek') is not None:
            self.day_of_week = m.get('DayOfWeek')
        if m.get('End') is not None:
            self.end = m.get('End')
        return self


class QueryRecordPlanDetailResponseBodyDataTemplateInfo(TeaModel):
    def __init__(
        self,
        all_day: int = None,
        default: int = None,
        name: str = None,
        template_id: str = None,
        time_section_list: List[QueryRecordPlanDetailResponseBodyDataTemplateInfoTimeSectionList] = None,
    ):
        self.all_day = all_day
        self.default = default
        self.name = name
        self.template_id = template_id
        self.time_section_list = time_section_list

    def validate(self):
        if self.time_section_list:
            for k in self.time_section_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all_day is not None:
            result['AllDay'] = self.all_day
        if self.default is not None:
            result['Default'] = self.default
        if self.name is not None:
            result['Name'] = self.name
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        result['TimeSectionList'] = []
        if self.time_section_list is not None:
            for k in self.time_section_list:
                result['TimeSectionList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllDay') is not None:
            self.all_day = m.get('AllDay')
        if m.get('Default') is not None:
            self.default = m.get('Default')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        self.time_section_list = []
        if m.get('TimeSectionList') is not None:
            for k in m.get('TimeSectionList'):
                temp_model = QueryRecordPlanDetailResponseBodyDataTemplateInfoTimeSectionList()
                self.time_section_list.append(temp_model.from_map(k))
        return self


class QueryRecordPlanDetailResponseBodyData(TeaModel):
    def __init__(
        self,
        name: str = None,
        plan_id: str = None,
        template_id: str = None,
        template_info: QueryRecordPlanDetailResponseBodyDataTemplateInfo = None,
    ):
        self.name = name
        self.plan_id = plan_id
        self.template_id = template_id
        self.template_info = template_info

    def validate(self):
        if self.template_info:
            self.template_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_info is not None:
            result['TemplateInfo'] = self.template_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateInfo') is not None:
            temp_model = QueryRecordPlanDetailResponseBodyDataTemplateInfo()
            self.template_info = temp_model.from_map(m['TemplateInfo'])
        return self


class QueryRecordPlanDetailResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: QueryRecordPlanDetailResponseBodyData = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_message = error_message
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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = QueryRecordPlanDetailResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryRecordPlanDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryRecordPlanDetailResponseBody = None,
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
            temp_model = QueryRecordPlanDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryRecordPlanDeviceByDeviceRequest(TeaModel):
    def __init__(
        self,
        device_name: str = None,
        iot_id: str = None,
        iot_instance_id: str = None,
        product_key: str = None,
        stream_type: int = None,
    ):
        self.device_name = device_name
        self.iot_id = iot_id
        self.iot_instance_id = iot_instance_id
        self.product_key = product_key
        self.stream_type = stream_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        if self.stream_type is not None:
            result['StreamType'] = self.stream_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        if m.get('StreamType') is not None:
            self.stream_type = m.get('StreamType')
        return self


class QueryRecordPlanDeviceByDeviceResponseBodyDataTemplateInfoTimeSectionList(TeaModel):
    def __init__(
        self,
        begin: int = None,
        day_of_week: int = None,
        end: int = None,
    ):
        self.begin = begin
        self.day_of_week = day_of_week
        self.end = end

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin is not None:
            result['Begin'] = self.begin
        if self.day_of_week is not None:
            result['DayOfWeek'] = self.day_of_week
        if self.end is not None:
            result['End'] = self.end
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Begin') is not None:
            self.begin = m.get('Begin')
        if m.get('DayOfWeek') is not None:
            self.day_of_week = m.get('DayOfWeek')
        if m.get('End') is not None:
            self.end = m.get('End')
        return self


class QueryRecordPlanDeviceByDeviceResponseBodyDataTemplateInfo(TeaModel):
    def __init__(
        self,
        all_day: int = None,
        default: int = None,
        name: str = None,
        template_id: str = None,
        time_section_list: List[QueryRecordPlanDeviceByDeviceResponseBodyDataTemplateInfoTimeSectionList] = None,
    ):
        self.all_day = all_day
        self.default = default
        self.name = name
        self.template_id = template_id
        self.time_section_list = time_section_list

    def validate(self):
        if self.time_section_list:
            for k in self.time_section_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all_day is not None:
            result['AllDay'] = self.all_day
        if self.default is not None:
            result['Default'] = self.default
        if self.name is not None:
            result['Name'] = self.name
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        result['TimeSectionList'] = []
        if self.time_section_list is not None:
            for k in self.time_section_list:
                result['TimeSectionList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllDay') is not None:
            self.all_day = m.get('AllDay')
        if m.get('Default') is not None:
            self.default = m.get('Default')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        self.time_section_list = []
        if m.get('TimeSectionList') is not None:
            for k in m.get('TimeSectionList'):
                temp_model = QueryRecordPlanDeviceByDeviceResponseBodyDataTemplateInfoTimeSectionList()
                self.time_section_list.append(temp_model.from_map(k))
        return self


class QueryRecordPlanDeviceByDeviceResponseBodyData(TeaModel):
    def __init__(
        self,
        name: str = None,
        plan_id: str = None,
        template_id: str = None,
        template_info: QueryRecordPlanDeviceByDeviceResponseBodyDataTemplateInfo = None,
    ):
        self.name = name
        self.plan_id = plan_id
        self.template_id = template_id
        self.template_info = template_info

    def validate(self):
        if self.template_info:
            self.template_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_info is not None:
            result['TemplateInfo'] = self.template_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateInfo') is not None:
            temp_model = QueryRecordPlanDeviceByDeviceResponseBodyDataTemplateInfo()
            self.template_info = temp_model.from_map(m['TemplateInfo'])
        return self


class QueryRecordPlanDeviceByDeviceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: QueryRecordPlanDeviceByDeviceResponseBodyData = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_message = error_message
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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = QueryRecordPlanDeviceByDeviceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryRecordPlanDeviceByDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryRecordPlanDeviceByDeviceResponseBody = None,
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
            temp_model = QueryRecordPlanDeviceByDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryRecordPlanDeviceByPlanRequest(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        plan_id: str = None,
    ):
        self.current_page = current_page
        self.page_size = page_size
        self.plan_id = plan_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        return self


class QueryRecordPlanDeviceByPlanResponseBodyDataList(TeaModel):
    def __init__(
        self,
        iot_id: str = None,
        stream_type: int = None,
    ):
        self.iot_id = iot_id
        self.stream_type = stream_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.stream_type is not None:
            result['StreamType'] = self.stream_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('StreamType') is not None:
            self.stream_type = m.get('StreamType')
        return self


class QueryRecordPlanDeviceByPlanResponseBodyData(TeaModel):
    def __init__(
        self,
        list: List[QueryRecordPlanDeviceByPlanResponseBodyDataList] = None,
        page: int = None,
        page_count: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.list = list
        self.page = page
        self.page_count = page_count
        self.page_size = page_size
        self.total = total

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.page is not None:
            result['Page'] = self.page
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = QueryRecordPlanDeviceByPlanResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class QueryRecordPlanDeviceByPlanResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: QueryRecordPlanDeviceByPlanResponseBodyData = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_message = error_message
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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = QueryRecordPlanDeviceByPlanResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryRecordPlanDeviceByPlanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryRecordPlanDeviceByPlanResponseBody = None,
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
            temp_model = QueryRecordPlanDeviceByPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryRecordPlansRequest(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
    ):
        self.current_page = current_page
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class QueryRecordPlansResponseBodyDataList(TeaModel):
    def __init__(
        self,
        name: str = None,
        plan_id: str = None,
        template_id: str = None,
    ):
        self.name = name
        self.plan_id = plan_id
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class QueryRecordPlansResponseBodyData(TeaModel):
    def __init__(
        self,
        list: List[QueryRecordPlansResponseBodyDataList] = None,
        page: int = None,
        page_count: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.list = list
        self.page = page
        self.page_count = page_count
        self.page_size = page_size
        self.total = total

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.page is not None:
            result['Page'] = self.page
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = QueryRecordPlansResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class QueryRecordPlansResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: QueryRecordPlansResponseBodyData = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_message = error_message
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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = QueryRecordPlansResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryRecordPlansResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryRecordPlansResponseBody = None,
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
            temp_model = QueryRecordPlansResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryRecordUrlRequest(TeaModel):
    def __init__(
        self,
        device_name: str = None,
        file_name: str = None,
        iot_id: str = None,
        iot_instance_id: str = None,
        product_key: str = None,
        seek_time: int = None,
        url_valid_duration: int = None,
    ):
        self.device_name = device_name
        self.file_name = file_name
        self.iot_id = iot_id
        self.iot_instance_id = iot_instance_id
        self.product_key = product_key
        self.seek_time = seek_time
        self.url_valid_duration = url_valid_duration

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        if self.seek_time is not None:
            result['SeekTime'] = self.seek_time
        if self.url_valid_duration is not None:
            result['UrlValidDuration'] = self.url_valid_duration
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        if m.get('SeekTime') is not None:
            self.seek_time = m.get('SeekTime')
        if m.get('UrlValidDuration') is not None:
            self.url_valid_duration = m.get('UrlValidDuration')
        return self


class QueryRecordUrlResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_message = error_message
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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryRecordUrlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryRecordUrlResponseBody = None,
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
            temp_model = QueryRecordUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryRecordUrlByTimeRequest(TeaModel):
    def __init__(
        self,
        begin_time: int = None,
        device_name: str = None,
        end_time: int = None,
        iot_id: str = None,
        iot_instance_id: str = None,
        product_key: str = None,
        stream_type: int = None,
        url_valid_duration: int = None,
    ):
        self.begin_time = begin_time
        self.device_name = device_name
        self.end_time = end_time
        self.iot_id = iot_id
        self.iot_instance_id = iot_instance_id
        self.product_key = product_key
        self.stream_type = stream_type
        self.url_valid_duration = url_valid_duration

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        if self.stream_type is not None:
            result['StreamType'] = self.stream_type
        if self.url_valid_duration is not None:
            result['UrlValidDuration'] = self.url_valid_duration
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        if m.get('StreamType') is not None:
            self.stream_type = m.get('StreamType')
        if m.get('UrlValidDuration') is not None:
            self.url_valid_duration = m.get('UrlValidDuration')
        return self


class QueryRecordUrlByTimeResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_message = error_message
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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryRecordUrlByTimeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryRecordUrlByTimeResponseBody = None,
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
            temp_model = QueryRecordUrlByTimeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryRtmpKeyRequest(TeaModel):
    def __init__(
        self,
        device_name: str = None,
        iot_id: str = None,
        iot_instance_id: str = None,
        product_key: str = None,
    ):
        self.device_name = device_name
        self.iot_id = iot_id
        self.iot_instance_id = iot_instance_id
        self.product_key = product_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        return self


class QueryRtmpKeyResponseBodyData(TeaModel):
    def __init__(
        self,
        pull_auth_key: str = None,
        pull_key_expire_time: int = None,
        push_auth_key: str = None,
        push_key_expire_time: int = None,
        stream_name: str = None,
    ):
        self.pull_auth_key = pull_auth_key
        self.pull_key_expire_time = pull_key_expire_time
        self.push_auth_key = push_auth_key
        self.push_key_expire_time = push_key_expire_time
        self.stream_name = stream_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pull_auth_key is not None:
            result['PullAuthKey'] = self.pull_auth_key
        if self.pull_key_expire_time is not None:
            result['PullKeyExpireTime'] = self.pull_key_expire_time
        if self.push_auth_key is not None:
            result['PushAuthKey'] = self.push_auth_key
        if self.push_key_expire_time is not None:
            result['PushKeyExpireTime'] = self.push_key_expire_time
        if self.stream_name is not None:
            result['StreamName'] = self.stream_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PullAuthKey') is not None:
            self.pull_auth_key = m.get('PullAuthKey')
        if m.get('PullKeyExpireTime') is not None:
            self.pull_key_expire_time = m.get('PullKeyExpireTime')
        if m.get('PushAuthKey') is not None:
            self.push_auth_key = m.get('PushAuthKey')
        if m.get('PushKeyExpireTime') is not None:
            self.push_key_expire_time = m.get('PushKeyExpireTime')
        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')
        return self


class QueryRtmpKeyResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: QueryRtmpKeyResponseBodyData = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_message = error_message
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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = QueryRtmpKeyResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryRtmpKeyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryRtmpKeyResponseBody = None,
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
            temp_model = QueryRtmpKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryStreamPushJobRequest(TeaModel):
    def __init__(
        self,
        device_name: str = None,
        iot_id: str = None,
        iot_instance_id: str = None,
        job_id: str = None,
        product_key: str = None,
    ):
        self.device_name = device_name
        self.iot_id = iot_id
        self.iot_instance_id = iot_instance_id
        self.job_id = job_id
        self.product_key = product_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        return self


class QueryStreamPushJobResponseBodyData(TeaModel):
    def __init__(
        self,
        create_time: int = None,
        job_type: int = None,
        push_status: int = None,
        push_url: str = None,
        stream_type: int = None,
    ):
        self.create_time = create_time
        self.job_type = job_type
        self.push_status = push_status
        self.push_url = push_url
        self.stream_type = stream_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.job_type is not None:
            result['JobType'] = self.job_type
        if self.push_status is not None:
            result['PushStatus'] = self.push_status
        if self.push_url is not None:
            result['PushUrl'] = self.push_url
        if self.stream_type is not None:
            result['StreamType'] = self.stream_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')
        if m.get('PushStatus') is not None:
            self.push_status = m.get('PushStatus')
        if m.get('PushUrl') is not None:
            self.push_url = m.get('PushUrl')
        if m.get('StreamType') is not None:
            self.stream_type = m.get('StreamType')
        return self


class QueryStreamPushJobResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: QueryStreamPushJobResponseBodyData = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_message = error_message
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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = QueryStreamPushJobResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryStreamPushJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryStreamPushJobResponseBody = None,
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
            temp_model = QueryStreamPushJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryStreamPushJobListRequest(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        device_name: str = None,
        iot_id: str = None,
        iot_instance_id: str = None,
        job_type: int = None,
        page_size: int = None,
        product_key: str = None,
    ):
        self.current_page = current_page
        self.device_name = device_name
        self.iot_id = iot_id
        self.iot_instance_id = iot_instance_id
        self.job_type = job_type
        self.page_size = page_size
        self.product_key = product_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.job_type is not None:
            result['JobType'] = self.job_type
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        return self


class QueryStreamPushJobListResponseBodyDataJobList(TeaModel):
    def __init__(
        self,
        create_time: int = None,
        job_id: str = None,
        job_type: int = None,
        push_status: int = None,
        push_url: str = None,
        stream_type: int = None,
    ):
        self.create_time = create_time
        self.job_id = job_id
        self.job_type = job_type
        self.push_status = push_status
        self.push_url = push_url
        self.stream_type = stream_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.job_type is not None:
            result['JobType'] = self.job_type
        if self.push_status is not None:
            result['PushStatus'] = self.push_status
        if self.push_url is not None:
            result['PushUrl'] = self.push_url
        if self.stream_type is not None:
            result['StreamType'] = self.stream_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')
        if m.get('PushStatus') is not None:
            self.push_status = m.get('PushStatus')
        if m.get('PushUrl') is not None:
            self.push_url = m.get('PushUrl')
        if m.get('StreamType') is not None:
            self.stream_type = m.get('StreamType')
        return self


class QueryStreamPushJobListResponseBodyData(TeaModel):
    def __init__(
        self,
        job_list: List[QueryStreamPushJobListResponseBodyDataJobList] = None,
        total: int = None,
    ):
        self.job_list = job_list
        self.total = total

    def validate(self):
        if self.job_list:
            for k in self.job_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['JobList'] = []
        if self.job_list is not None:
            for k in self.job_list:
                result['JobList'].append(k.to_map() if k else None)
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.job_list = []
        if m.get('JobList') is not None:
            for k in m.get('JobList'):
                temp_model = QueryStreamPushJobListResponseBodyDataJobList()
                self.job_list.append(temp_model.from_map(k))
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class QueryStreamPushJobListResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: QueryStreamPushJobListResponseBodyData = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_message = error_message
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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = QueryStreamPushJobListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryStreamPushJobListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryStreamPushJobListResponseBody = None,
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
            temp_model = QueryStreamPushJobListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryStreamSnapshotJobRequest(TeaModel):
    def __init__(
        self,
        device_name: str = None,
        iot_id: str = None,
        iot_instance_id: str = None,
        product_key: str = None,
    ):
        self.device_name = device_name
        self.iot_id = iot_id
        self.iot_instance_id = iot_instance_id
        self.product_key = product_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        return self


class QueryStreamSnapshotJobResponseBodyDataJobList(TeaModel):
    def __init__(
        self,
        snapshot_interval: int = None,
        stream_type: int = None,
    ):
        self.snapshot_interval = snapshot_interval
        self.stream_type = stream_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.snapshot_interval is not None:
            result['SnapshotInterval'] = self.snapshot_interval
        if self.stream_type is not None:
            result['StreamType'] = self.stream_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SnapshotInterval') is not None:
            self.snapshot_interval = m.get('SnapshotInterval')
        if m.get('StreamType') is not None:
            self.stream_type = m.get('StreamType')
        return self


class QueryStreamSnapshotJobResponseBodyData(TeaModel):
    def __init__(
        self,
        job_list: List[QueryStreamSnapshotJobResponseBodyDataJobList] = None,
    ):
        self.job_list = job_list

    def validate(self):
        if self.job_list:
            for k in self.job_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['JobList'] = []
        if self.job_list is not None:
            for k in self.job_list:
                result['JobList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.job_list = []
        if m.get('JobList') is not None:
            for k in m.get('JobList'):
                temp_model = QueryStreamSnapshotJobResponseBodyDataJobList()
                self.job_list.append(temp_model.from_map(k))
        return self


class QueryStreamSnapshotJobResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: QueryStreamSnapshotJobResponseBodyData = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_message = error_message
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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = QueryStreamSnapshotJobResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryStreamSnapshotJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryStreamSnapshotJobResponseBody = None,
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
            temp_model = QueryStreamSnapshotJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTimeTemplateRequest(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
    ):
        self.current_page = current_page
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class QueryTimeTemplateResponseBodyDataListTimeSectionList(TeaModel):
    def __init__(
        self,
        begin: int = None,
        day_of_week: int = None,
        end: int = None,
    ):
        self.begin = begin
        self.day_of_week = day_of_week
        self.end = end

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin is not None:
            result['Begin'] = self.begin
        if self.day_of_week is not None:
            result['DayOfWeek'] = self.day_of_week
        if self.end is not None:
            result['End'] = self.end
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Begin') is not None:
            self.begin = m.get('Begin')
        if m.get('DayOfWeek') is not None:
            self.day_of_week = m.get('DayOfWeek')
        if m.get('End') is not None:
            self.end = m.get('End')
        return self


class QueryTimeTemplateResponseBodyDataList(TeaModel):
    def __init__(
        self,
        all_day: int = None,
        default: int = None,
        name: str = None,
        template_id: str = None,
        time_section_list: List[QueryTimeTemplateResponseBodyDataListTimeSectionList] = None,
    ):
        self.all_day = all_day
        self.default = default
        self.name = name
        self.template_id = template_id
        self.time_section_list = time_section_list

    def validate(self):
        if self.time_section_list:
            for k in self.time_section_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all_day is not None:
            result['AllDay'] = self.all_day
        if self.default is not None:
            result['Default'] = self.default
        if self.name is not None:
            result['Name'] = self.name
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        result['TimeSectionList'] = []
        if self.time_section_list is not None:
            for k in self.time_section_list:
                result['TimeSectionList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllDay') is not None:
            self.all_day = m.get('AllDay')
        if m.get('Default') is not None:
            self.default = m.get('Default')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        self.time_section_list = []
        if m.get('TimeSectionList') is not None:
            for k in m.get('TimeSectionList'):
                temp_model = QueryTimeTemplateResponseBodyDataListTimeSectionList()
                self.time_section_list.append(temp_model.from_map(k))
        return self


class QueryTimeTemplateResponseBodyData(TeaModel):
    def __init__(
        self,
        list: List[QueryTimeTemplateResponseBodyDataList] = None,
        page: int = None,
        page_count: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.list = list
        self.page = page
        self.page_count = page_count
        self.page_size = page_size
        self.total = total

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.page is not None:
            result['Page'] = self.page
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = QueryTimeTemplateResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class QueryTimeTemplateResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: QueryTimeTemplateResponseBodyData = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_message = error_message
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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = QueryTimeTemplateResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryTimeTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryTimeTemplateResponseBody = None,
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
            temp_model = QueryTimeTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTimeTemplateDetailRequest(TeaModel):
    def __init__(
        self,
        template_id: str = None,
    ):
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class QueryTimeTemplateDetailResponseBodyDataTimeSectionList(TeaModel):
    def __init__(
        self,
        begin: int = None,
        day_of_week: int = None,
        end: int = None,
    ):
        self.begin = begin
        self.day_of_week = day_of_week
        self.end = end

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin is not None:
            result['Begin'] = self.begin
        if self.day_of_week is not None:
            result['DayOfWeek'] = self.day_of_week
        if self.end is not None:
            result['End'] = self.end
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Begin') is not None:
            self.begin = m.get('Begin')
        if m.get('DayOfWeek') is not None:
            self.day_of_week = m.get('DayOfWeek')
        if m.get('End') is not None:
            self.end = m.get('End')
        return self


class QueryTimeTemplateDetailResponseBodyData(TeaModel):
    def __init__(
        self,
        all_day: int = None,
        default: int = None,
        name: str = None,
        template_id: str = None,
        time_section_list: List[QueryTimeTemplateDetailResponseBodyDataTimeSectionList] = None,
    ):
        self.all_day = all_day
        self.default = default
        self.name = name
        self.template_id = template_id
        self.time_section_list = time_section_list

    def validate(self):
        if self.time_section_list:
            for k in self.time_section_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all_day is not None:
            result['AllDay'] = self.all_day
        if self.default is not None:
            result['Default'] = self.default
        if self.name is not None:
            result['Name'] = self.name
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        result['TimeSectionList'] = []
        if self.time_section_list is not None:
            for k in self.time_section_list:
                result['TimeSectionList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllDay') is not None:
            self.all_day = m.get('AllDay')
        if m.get('Default') is not None:
            self.default = m.get('Default')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        self.time_section_list = []
        if m.get('TimeSectionList') is not None:
            for k in m.get('TimeSectionList'):
                temp_model = QueryTimeTemplateDetailResponseBodyDataTimeSectionList()
                self.time_section_list.append(temp_model.from_map(k))
        return self


class QueryTimeTemplateDetailResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: QueryTimeTemplateDetailResponseBodyData = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_message = error_message
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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = QueryTimeTemplateDetailResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryTimeTemplateDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryTimeTemplateDetailResponseBody = None,
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
            temp_model = QueryTimeTemplateDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryVisionDeviceInfoRequest(TeaModel):
    def __init__(
        self,
        device_name: str = None,
        iot_id: str = None,
        iot_instance_id: str = None,
        product_key: str = None,
    ):
        self.device_name = device_name
        self.iot_id = iot_id
        self.iot_instance_id = iot_instance_id
        self.product_key = product_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        return self


class QueryVisionDeviceInfoResponseBodyDataGbDeviceInfo(TeaModel):
    def __init__(
        self,
        device_protocol: int = None,
        gb_id: str = None,
        net_protocol: int = None,
        nick_name: str = None,
        password: str = None,
        sub_product_key: str = None,
    ):
        self.device_protocol = device_protocol
        self.gb_id = gb_id
        self.net_protocol = net_protocol
        self.nick_name = nick_name
        self.password = password
        self.sub_product_key = sub_product_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_protocol is not None:
            result['DeviceProtocol'] = self.device_protocol
        if self.gb_id is not None:
            result['GbId'] = self.gb_id
        if self.net_protocol is not None:
            result['NetProtocol'] = self.net_protocol
        if self.nick_name is not None:
            result['NickName'] = self.nick_name
        if self.password is not None:
            result['Password'] = self.password
        if self.sub_product_key is not None:
            result['SubProductKey'] = self.sub_product_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceProtocol') is not None:
            self.device_protocol = m.get('DeviceProtocol')
        if m.get('GbId') is not None:
            self.gb_id = m.get('GbId')
        if m.get('NetProtocol') is not None:
            self.net_protocol = m.get('NetProtocol')
        if m.get('NickName') is not None:
            self.nick_name = m.get('NickName')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('SubProductKey') is not None:
            self.sub_product_key = m.get('SubProductKey')
        return self


class QueryVisionDeviceInfoResponseBodyDataRtmpDeviceInfo(TeaModel):
    def __init__(
        self,
        pull_auth_key: str = None,
        pull_key_expire_time: int = None,
        push_auth_key: str = None,
        push_key_expire_time: int = None,
        push_url_sample: str = None,
        stream_name: str = None,
        stream_status: int = None,
    ):
        self.pull_auth_key = pull_auth_key
        self.pull_key_expire_time = pull_key_expire_time
        self.push_auth_key = push_auth_key
        self.push_key_expire_time = push_key_expire_time
        self.push_url_sample = push_url_sample
        self.stream_name = stream_name
        self.stream_status = stream_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pull_auth_key is not None:
            result['PullAuthKey'] = self.pull_auth_key
        if self.pull_key_expire_time is not None:
            result['PullKeyExpireTime'] = self.pull_key_expire_time
        if self.push_auth_key is not None:
            result['PushAuthKey'] = self.push_auth_key
        if self.push_key_expire_time is not None:
            result['PushKeyExpireTime'] = self.push_key_expire_time
        if self.push_url_sample is not None:
            result['PushUrlSample'] = self.push_url_sample
        if self.stream_name is not None:
            result['StreamName'] = self.stream_name
        if self.stream_status is not None:
            result['StreamStatus'] = self.stream_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PullAuthKey') is not None:
            self.pull_auth_key = m.get('PullAuthKey')
        if m.get('PullKeyExpireTime') is not None:
            self.pull_key_expire_time = m.get('PullKeyExpireTime')
        if m.get('PushAuthKey') is not None:
            self.push_auth_key = m.get('PushAuthKey')
        if m.get('PushKeyExpireTime') is not None:
            self.push_key_expire_time = m.get('PushKeyExpireTime')
        if m.get('PushUrlSample') is not None:
            self.push_url_sample = m.get('PushUrlSample')
        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')
        if m.get('StreamStatus') is not None:
            self.stream_status = m.get('StreamStatus')
        return self


class QueryVisionDeviceInfoResponseBodyData(TeaModel):
    def __init__(
        self,
        description: str = None,
        device_type: int = None,
        gb_device_info: QueryVisionDeviceInfoResponseBodyDataGbDeviceInfo = None,
        rtmp_device_info: QueryVisionDeviceInfoResponseBodyDataRtmpDeviceInfo = None,
    ):
        self.description = description
        self.device_type = device_type
        self.gb_device_info = gb_device_info
        self.rtmp_device_info = rtmp_device_info

    def validate(self):
        if self.gb_device_info:
            self.gb_device_info.validate()
        if self.rtmp_device_info:
            self.rtmp_device_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.device_type is not None:
            result['DeviceType'] = self.device_type
        if self.gb_device_info is not None:
            result['GbDeviceInfo'] = self.gb_device_info.to_map()
        if self.rtmp_device_info is not None:
            result['RtmpDeviceInfo'] = self.rtmp_device_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DeviceType') is not None:
            self.device_type = m.get('DeviceType')
        if m.get('GbDeviceInfo') is not None:
            temp_model = QueryVisionDeviceInfoResponseBodyDataGbDeviceInfo()
            self.gb_device_info = temp_model.from_map(m['GbDeviceInfo'])
        if m.get('RtmpDeviceInfo') is not None:
            temp_model = QueryVisionDeviceInfoResponseBodyDataRtmpDeviceInfo()
            self.rtmp_device_info = temp_model.from_map(m['RtmpDeviceInfo'])
        return self


class QueryVisionDeviceInfoResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: QueryVisionDeviceInfoResponseBodyData = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_message = error_message
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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = QueryVisionDeviceInfoResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryVisionDeviceInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryVisionDeviceInfoResponseBody = None,
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
            temp_model = QueryVisionDeviceInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryVoiceIntercomRequest(TeaModel):
    def __init__(
        self,
        device_name: str = None,
        iot_id: str = None,
        iot_instance_id: str = None,
        product_key: str = None,
        scheme: str = None,
    ):
        self.device_name = device_name
        self.iot_id = iot_id
        self.iot_instance_id = iot_instance_id
        self.product_key = product_key
        self.scheme = scheme

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        if self.scheme is not None:
            result['Scheme'] = self.scheme
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        if m.get('Scheme') is not None:
            self.scheme = m.get('Scheme')
        return self


class QueryVoiceIntercomResponseBodyDataCryptoKey(TeaModel):
    def __init__(
        self,
        iv: str = None,
        key: str = None,
    ):
        self.iv = iv
        self.key = key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.iv is not None:
            result['Iv'] = self.iv
        if self.key is not None:
            result['Key'] = self.key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Iv') is not None:
            self.iv = m.get('Iv')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        return self


class QueryVoiceIntercomResponseBodyData(TeaModel):
    def __init__(
        self,
        crypto_key: QueryVoiceIntercomResponseBodyDataCryptoKey = None,
        url: str = None,
    ):
        self.crypto_key = crypto_key
        self.url = url

    def validate(self):
        if self.crypto_key:
            self.crypto_key.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.crypto_key is not None:
            result['CryptoKey'] = self.crypto_key.to_map()
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CryptoKey') is not None:
            temp_model = QueryVoiceIntercomResponseBodyDataCryptoKey()
            self.crypto_key = temp_model.from_map(m['CryptoKey'])
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class QueryVoiceIntercomResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: QueryVoiceIntercomResponseBodyData = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_message = error_message
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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = QueryVoiceIntercomResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryVoiceIntercomResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryVoiceIntercomResponseBody = None,
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
            temp_model = QueryVoiceIntercomResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RefreshGbSubDeviceListRequest(TeaModel):
    def __init__(
        self,
        device_name: str = None,
        iot_id: str = None,
        iot_instance_id: str = None,
        product_key: str = None,
    ):
        self.device_name = device_name
        self.iot_id = iot_id
        self.iot_instance_id = iot_instance_id
        self.product_key = product_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        return self


class RefreshGbSubDeviceListResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.error_message = error_message
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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RefreshGbSubDeviceListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RefreshGbSubDeviceListResponseBody = None,
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
            temp_model = RefreshGbSubDeviceListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveFaceDeviceFromDeviceGroupRequest(TeaModel):
    def __init__(
        self,
        device_group_id: str = None,
        device_name: str = None,
        iot_instance_id: str = None,
        isolation_id: str = None,
        product_key: str = None,
    ):
        self.device_group_id = device_group_id
        self.device_name = device_name
        self.iot_instance_id = iot_instance_id
        self.isolation_id = isolation_id
        self.product_key = product_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_group_id is not None:
            result['DeviceGroupId'] = self.device_group_id
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.isolation_id is not None:
            result['IsolationId'] = self.isolation_id
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceGroupId') is not None:
            self.device_group_id = m.get('DeviceGroupId')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('IsolationId') is not None:
            self.isolation_id = m.get('IsolationId')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        return self


class RemoveFaceDeviceFromDeviceGroupResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.error_message = error_message
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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RemoveFaceDeviceFromDeviceGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RemoveFaceDeviceFromDeviceGroupResponseBody = None,
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
            temp_model = RemoveFaceDeviceFromDeviceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveFaceUserFromUserGroupRequest(TeaModel):
    def __init__(
        self,
        isolation_id: str = None,
        user_group_id: str = None,
        user_id: str = None,
    ):
        self.isolation_id = isolation_id
        self.user_group_id = user_group_id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.isolation_id is not None:
            result['IsolationId'] = self.isolation_id
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsolationId') is not None:
            self.isolation_id = m.get('IsolationId')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class RemoveFaceUserFromUserGroupResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.error_message = error_message
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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RemoveFaceUserFromUserGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RemoveFaceUserFromUserGroupResponseBody = None,
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
            temp_model = RemoveFaceUserFromUserGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetDevicePictureLifeCycleRequest(TeaModel):
    def __init__(
        self,
        day: int = None,
        device_name: str = None,
        iot_id: str = None,
        iot_instance_id: str = None,
        product_key: str = None,
    ):
        self.day = day
        self.device_name = device_name
        self.iot_id = iot_id
        self.iot_instance_id = iot_instance_id
        self.product_key = product_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.day is not None:
            result['Day'] = self.day
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Day') is not None:
            self.day = m.get('Day')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        return self


class SetDevicePictureLifeCycleResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.error_message = error_message
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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SetDevicePictureLifeCycleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetDevicePictureLifeCycleResponseBody = None,
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
            temp_model = SetDevicePictureLifeCycleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetDeviceRecordLifeCycleRequest(TeaModel):
    def __init__(
        self,
        day: int = None,
        device_name: str = None,
        iot_id: str = None,
        iot_instance_id: str = None,
        product_key: str = None,
    ):
        self.day = day
        self.device_name = device_name
        self.iot_id = iot_id
        self.iot_instance_id = iot_instance_id
        self.product_key = product_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.day is not None:
            result['Day'] = self.day
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Day') is not None:
            self.day = m.get('Day')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        return self


class SetDeviceRecordLifeCycleResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.error_message = error_message
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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SetDeviceRecordLifeCycleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetDeviceRecordLifeCycleResponseBody = None,
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
            temp_model = SetDeviceRecordLifeCycleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopLiveStreamingRequest(TeaModel):
    def __init__(
        self,
        device_name: str = None,
        iot_id: str = None,
        iot_instance_id: str = None,
        product_key: str = None,
        stream_type: int = None,
    ):
        self.device_name = device_name
        self.iot_id = iot_id
        self.iot_instance_id = iot_instance_id
        self.product_key = product_key
        self.stream_type = stream_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        if self.stream_type is not None:
            result['StreamType'] = self.stream_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        if m.get('StreamType') is not None:
            self.stream_type = m.get('StreamType')
        return self


class StopLiveStreamingResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.error_message = error_message
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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class StopLiveStreamingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StopLiveStreamingResponseBody = None,
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
            temp_model = StopLiveStreamingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopTriggeredRecordRequest(TeaModel):
    def __init__(
        self,
        device_name: str = None,
        iot_id: str = None,
        iot_instance_id: str = None,
        product_key: str = None,
        record_id: str = None,
    ):
        self.device_name = device_name
        self.iot_id = iot_id
        self.iot_instance_id = iot_instance_id
        self.product_key = product_key
        self.record_id = record_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        if self.record_id is not None:
            result['RecordId'] = self.record_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')
        return self


class StopTriggeredRecordResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.error_message = error_message
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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class StopTriggeredRecordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StopTriggeredRecordResponseBody = None,
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
            temp_model = StopTriggeredRecordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TransferDeviceInstanceRequest(TeaModel):
    def __init__(
        self,
        device_name_list: List[str] = None,
        product_key: str = None,
        source_instance_id: str = None,
        target_instance_id: str = None,
    ):
        self.device_name_list = device_name_list
        self.product_key = product_key
        self.source_instance_id = source_instance_id
        self.target_instance_id = target_instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name_list is not None:
            result['DeviceNameList'] = self.device_name_list
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        if self.source_instance_id is not None:
            result['SourceInstanceId'] = self.source_instance_id
        if self.target_instance_id is not None:
            result['TargetInstanceId'] = self.target_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceNameList') is not None:
            self.device_name_list = m.get('DeviceNameList')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        if m.get('SourceInstanceId') is not None:
            self.source_instance_id = m.get('SourceInstanceId')
        if m.get('TargetInstanceId') is not None:
            self.target_instance_id = m.get('TargetInstanceId')
        return self


class TransferDeviceInstanceResponseBodyDataFailedList(TeaModel):
    def __init__(
        self,
        device_name: str = None,
        message: str = None,
    ):
        self.device_name = device_name
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class TransferDeviceInstanceResponseBodyDataSuccessList(TeaModel):
    def __init__(
        self,
        device_name: str = None,
        message: str = None,
    ):
        self.device_name = device_name
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class TransferDeviceInstanceResponseBodyData(TeaModel):
    def __init__(
        self,
        failed_list: List[TransferDeviceInstanceResponseBodyDataFailedList] = None,
        success_list: List[TransferDeviceInstanceResponseBodyDataSuccessList] = None,
    ):
        self.failed_list = failed_list
        self.success_list = success_list

    def validate(self):
        if self.failed_list:
            for k in self.failed_list:
                if k:
                    k.validate()
        if self.success_list:
            for k in self.success_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FailedList'] = []
        if self.failed_list is not None:
            for k in self.failed_list:
                result['FailedList'].append(k.to_map() if k else None)
        result['SuccessList'] = []
        if self.success_list is not None:
            for k in self.success_list:
                result['SuccessList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.failed_list = []
        if m.get('FailedList') is not None:
            for k in m.get('FailedList'):
                temp_model = TransferDeviceInstanceResponseBodyDataFailedList()
                self.failed_list.append(temp_model.from_map(k))
        self.success_list = []
        if m.get('SuccessList') is not None:
            for k in m.get('SuccessList'):
                temp_model = TransferDeviceInstanceResponseBodyDataSuccessList()
                self.success_list.append(temp_model.from_map(k))
        return self


class TransferDeviceInstanceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: TransferDeviceInstanceResponseBodyData = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_message = error_message
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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = TransferDeviceInstanceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class TransferDeviceInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: TransferDeviceInstanceResponseBody = None,
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
            temp_model = TransferDeviceInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TriggerCapturePictureRequest(TeaModel):
    def __init__(
        self,
        device_name: str = None,
        iot_id: str = None,
        iot_instance_id: str = None,
        product_key: str = None,
    ):
        self.device_name = device_name
        self.iot_id = iot_id
        self.iot_instance_id = iot_instance_id
        self.product_key = product_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        return self


class TriggerCapturePictureResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_message = error_message
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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class TriggerCapturePictureResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: TriggerCapturePictureResponseBody = None,
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
            temp_model = TriggerCapturePictureResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TriggerRecordRequest(TeaModel):
    def __init__(
        self,
        device_name: str = None,
        iot_id: str = None,
        iot_instance_id: str = None,
        pre_record_duration: int = None,
        product_key: str = None,
        record_duration: int = None,
        stream_type: int = None,
    ):
        self.device_name = device_name
        self.iot_id = iot_id
        self.iot_instance_id = iot_instance_id
        self.pre_record_duration = pre_record_duration
        self.product_key = product_key
        self.record_duration = record_duration
        self.stream_type = stream_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.pre_record_duration is not None:
            result['PreRecordDuration'] = self.pre_record_duration
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        if self.record_duration is not None:
            result['RecordDuration'] = self.record_duration
        if self.stream_type is not None:
            result['StreamType'] = self.stream_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('PreRecordDuration') is not None:
            self.pre_record_duration = m.get('PreRecordDuration')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        if m.get('RecordDuration') is not None:
            self.record_duration = m.get('RecordDuration')
        if m.get('StreamType') is not None:
            self.stream_type = m.get('StreamType')
        return self


class TriggerRecordResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_message = error_message
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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class TriggerRecordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: TriggerRecordResponseBody = None,
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
            temp_model = TriggerRecordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnbindPictureSearchAppWithDevicesRequest(TeaModel):
    def __init__(
        self,
        app_instance_id: str = None,
        device_iot_ids: List[str] = None,
        iot_instance_id: str = None,
    ):
        self.app_instance_id = app_instance_id
        self.device_iot_ids = device_iot_ids
        self.iot_instance_id = iot_instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_id is not None:
            result['AppInstanceId'] = self.app_instance_id
        if self.device_iot_ids is not None:
            result['DeviceIotIds'] = self.device_iot_ids
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceId') is not None:
            self.app_instance_id = m.get('AppInstanceId')
        if m.get('DeviceIotIds') is not None:
            self.device_iot_ids = m.get('DeviceIotIds')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        return self


class UnbindPictureSearchAppWithDevicesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.error_message = error_message
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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UnbindPictureSearchAppWithDevicesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UnbindPictureSearchAppWithDevicesResponseBody = None,
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
            temp_model = UnbindPictureSearchAppWithDevicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateEventRecordPlanRequest(TeaModel):
    def __init__(
        self,
        event_types: str = None,
        name: str = None,
        plan_id: str = None,
        pre_record_duration: int = None,
        record_duration: int = None,
        template_id: str = None,
    ):
        self.event_types = event_types
        self.name = name
        self.plan_id = plan_id
        self.pre_record_duration = pre_record_duration
        self.record_duration = record_duration
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_types is not None:
            result['EventTypes'] = self.event_types
        if self.name is not None:
            result['Name'] = self.name
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        if self.pre_record_duration is not None:
            result['PreRecordDuration'] = self.pre_record_duration
        if self.record_duration is not None:
            result['RecordDuration'] = self.record_duration
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventTypes') is not None:
            self.event_types = m.get('EventTypes')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        if m.get('PreRecordDuration') is not None:
            self.pre_record_duration = m.get('PreRecordDuration')
        if m.get('RecordDuration') is not None:
            self.record_duration = m.get('RecordDuration')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class UpdateEventRecordPlanResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.error_message = error_message
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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateEventRecordPlanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateEventRecordPlanResponseBody = None,
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
            temp_model = UpdateEventRecordPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateFaceUserRequest(TeaModel):
    def __init__(
        self,
        custom_user_id: str = None,
        face_pic_url: str = None,
        isolation_id: str = None,
        name: str = None,
        params: str = None,
        user_id: str = None,
    ):
        self.custom_user_id = custom_user_id
        self.face_pic_url = face_pic_url
        self.isolation_id = isolation_id
        self.name = name
        self.params = params
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_user_id is not None:
            result['CustomUserId'] = self.custom_user_id
        if self.face_pic_url is not None:
            result['FacePicUrl'] = self.face_pic_url
        if self.isolation_id is not None:
            result['IsolationId'] = self.isolation_id
        if self.name is not None:
            result['Name'] = self.name
        if self.params is not None:
            result['Params'] = self.params
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomUserId') is not None:
            self.custom_user_id = m.get('CustomUserId')
        if m.get('FacePicUrl') is not None:
            self.face_pic_url = m.get('FacePicUrl')
        if m.get('IsolationId') is not None:
            self.isolation_id = m.get('IsolationId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Params') is not None:
            self.params = m.get('Params')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class UpdateFaceUserResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.error_message = error_message
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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateFaceUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateFaceUserResponseBody = None,
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
            temp_model = UpdateFaceUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateFaceUserGroupAndDeviceGroupRelationRequest(TeaModel):
    def __init__(
        self,
        control_id: str = None,
        isolation_id: str = None,
        relation: str = None,
    ):
        self.control_id = control_id
        self.isolation_id = isolation_id
        self.relation = relation

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.control_id is not None:
            result['ControlId'] = self.control_id
        if self.isolation_id is not None:
            result['IsolationId'] = self.isolation_id
        if self.relation is not None:
            result['Relation'] = self.relation
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ControlId') is not None:
            self.control_id = m.get('ControlId')
        if m.get('IsolationId') is not None:
            self.isolation_id = m.get('IsolationId')
        if m.get('Relation') is not None:
            self.relation = m.get('Relation')
        return self


class UpdateFaceUserGroupAndDeviceGroupRelationResponseBodyData(TeaModel):
    def __init__(
        self,
        control_id: str = None,
        modified_time: str = None,
    ):
        self.control_id = control_id
        self.modified_time = modified_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.control_id is not None:
            result['ControlId'] = self.control_id
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ControlId') is not None:
            self.control_id = m.get('ControlId')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        return self


class UpdateFaceUserGroupAndDeviceGroupRelationResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: UpdateFaceUserGroupAndDeviceGroupRelationResponseBodyData = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_message = error_message
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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = UpdateFaceUserGroupAndDeviceGroupRelationResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateFaceUserGroupAndDeviceGroupRelationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateFaceUserGroupAndDeviceGroupRelationResponseBody = None,
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
            temp_model = UpdateFaceUserGroupAndDeviceGroupRelationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateGbDeviceRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        device_name: str = None,
        gb_id: str = None,
        iot_id: str = None,
        iot_instance_id: str = None,
        password: str = None,
        product_key: str = None,
    ):
        self.description = description
        self.device_name = device_name
        self.gb_id = gb_id
        self.iot_id = iot_id
        self.iot_instance_id = iot_instance_id
        self.password = password
        self.product_key = product_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.gb_id is not None:
            result['GbId'] = self.gb_id
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.password is not None:
            result['Password'] = self.password
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('GbId') is not None:
            self.gb_id = m.get('GbId')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        return self


class UpdateGbDeviceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.error_message = error_message
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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateGbDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateGbDeviceResponseBody = None,
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
            temp_model = UpdateGbDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateInstanceInternetProtocolRequest(TeaModel):
    def __init__(
        self,
        iot_instance_id: str = None,
        ip_version: str = None,
    ):
        self.iot_instance_id = iot_instance_id
        self.ip_version = ip_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')
        return self


class UpdateInstanceInternetProtocolResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: Dict[str, Any] = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_message = error_message
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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateInstanceInternetProtocolResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateInstanceInternetProtocolResponseBody = None,
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
            temp_model = UpdateInstanceInternetProtocolResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdatePictureSearchAppRequest(TeaModel):
    def __init__(
        self,
        app_instance_id: str = None,
        description: str = None,
        name: str = None,
    ):
        self.app_instance_id = app_instance_id
        self.description = description
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_id is not None:
            result['AppInstanceId'] = self.app_instance_id
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceId') is not None:
            self.app_instance_id = m.get('AppInstanceId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class UpdatePictureSearchAppResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.error_message = error_message
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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdatePictureSearchAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdatePictureSearchAppResponseBody = None,
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
            temp_model = UpdatePictureSearchAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateRecordPlanRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        plan_id: str = None,
        template_id: str = None,
    ):
        self.name = name
        self.plan_id = plan_id
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class UpdateRecordPlanResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.error_message = error_message
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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateRecordPlanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateRecordPlanResponseBody = None,
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
            temp_model = UpdateRecordPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateRtmpKeyRequest(TeaModel):
    def __init__(
        self,
        device_name: str = None,
        iot_id: str = None,
        iot_instance_id: str = None,
        product_key: str = None,
        pull_auth_key: str = None,
        pull_key_expire_time: int = None,
        push_auth_key: str = None,
        push_key_expire_time: int = None,
    ):
        self.device_name = device_name
        self.iot_id = iot_id
        self.iot_instance_id = iot_instance_id
        self.product_key = product_key
        self.pull_auth_key = pull_auth_key
        self.pull_key_expire_time = pull_key_expire_time
        self.push_auth_key = push_auth_key
        self.push_key_expire_time = push_key_expire_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        if self.pull_auth_key is not None:
            result['PullAuthKey'] = self.pull_auth_key
        if self.pull_key_expire_time is not None:
            result['PullKeyExpireTime'] = self.pull_key_expire_time
        if self.push_auth_key is not None:
            result['PushAuthKey'] = self.push_auth_key
        if self.push_key_expire_time is not None:
            result['PushKeyExpireTime'] = self.push_key_expire_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        if m.get('PullAuthKey') is not None:
            self.pull_auth_key = m.get('PullAuthKey')
        if m.get('PullKeyExpireTime') is not None:
            self.pull_key_expire_time = m.get('PullKeyExpireTime')
        if m.get('PushAuthKey') is not None:
            self.push_auth_key = m.get('PushAuthKey')
        if m.get('PushKeyExpireTime') is not None:
            self.push_key_expire_time = m.get('PushKeyExpireTime')
        return self


class UpdateRtmpKeyResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.error_message = error_message
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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateRtmpKeyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateRtmpKeyResponseBody = None,
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
            temp_model = UpdateRtmpKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateTimeTemplateRequestTimeSections(TeaModel):
    def __init__(
        self,
        begin: int = None,
        day_of_week: int = None,
        end: int = None,
    ):
        self.begin = begin
        self.day_of_week = day_of_week
        self.end = end

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin is not None:
            result['Begin'] = self.begin
        if self.day_of_week is not None:
            result['DayOfWeek'] = self.day_of_week
        if self.end is not None:
            result['End'] = self.end
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Begin') is not None:
            self.begin = m.get('Begin')
        if m.get('DayOfWeek') is not None:
            self.day_of_week = m.get('DayOfWeek')
        if m.get('End') is not None:
            self.end = m.get('End')
        return self


class UpdateTimeTemplateRequest(TeaModel):
    def __init__(
        self,
        all_day: int = None,
        name: str = None,
        template_id: str = None,
        time_sections: List[UpdateTimeTemplateRequestTimeSections] = None,
    ):
        self.all_day = all_day
        self.name = name
        self.template_id = template_id
        self.time_sections = time_sections

    def validate(self):
        if self.time_sections:
            for k in self.time_sections:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all_day is not None:
            result['AllDay'] = self.all_day
        if self.name is not None:
            result['Name'] = self.name
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        result['TimeSections'] = []
        if self.time_sections is not None:
            for k in self.time_sections:
                result['TimeSections'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllDay') is not None:
            self.all_day = m.get('AllDay')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        self.time_sections = []
        if m.get('TimeSections') is not None:
            for k in m.get('TimeSections'):
                temp_model = UpdateTimeTemplateRequestTimeSections()
                self.time_sections.append(temp_model.from_map(k))
        return self


class UpdateTimeTemplateResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.error_message = error_message
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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateTimeTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateTimeTemplateResponseBody = None,
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
            temp_model = UpdateTimeTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


