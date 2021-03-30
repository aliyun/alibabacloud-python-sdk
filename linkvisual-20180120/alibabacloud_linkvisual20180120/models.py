# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, Any, List


class AddEventRecordPlanDeviceRequest(TeaModel):
    def __init__(
        self,
        iot_id: str = None,
        plan_id: str = None,
        stream_type: int = None,
    ):
        self.iot_id = iot_id
        self.plan_id = plan_id
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
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        if self.stream_type is not None:
            result['StreamType'] = self.stream_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        if m.get('StreamType') is not None:
            self.stream_type = m.get('StreamType')
        return self


class AddEventRecordPlanDeviceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddEventRecordPlanDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddEventRecordPlanDeviceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AddEventRecordPlanDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddFaceDeviceGroupRequest(TeaModel):
    def __init__(
        self,
        isolation_id: str = None,
        device_group_name: str = None,
    ):
        self.isolation_id = isolation_id
        self.device_group_name = device_group_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.isolation_id is not None:
            result['IsolationId'] = self.isolation_id
        if self.device_group_name is not None:
            result['DeviceGroupName'] = self.device_group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsolationId') is not None:
            self.isolation_id = m.get('IsolationId')
        if m.get('DeviceGroupName') is not None:
            self.device_group_name = m.get('DeviceGroupName')
        return self


class AddFaceDeviceGroupResponseBodyData(TeaModel):
    def __init__(
        self,
        device_group_id: str = None,
        modified_time: str = None,
        device_group_name: str = None,
    ):
        self.device_group_id = device_group_id
        self.modified_time = modified_time
        self.device_group_name = device_group_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_group_id is not None:
            result['DeviceGroupId'] = self.device_group_id
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.device_group_name is not None:
            result['DeviceGroupName'] = self.device_group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceGroupId') is not None:
            self.device_group_id = m.get('DeviceGroupId')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('DeviceGroupName') is not None:
            self.device_group_name = m.get('DeviceGroupName')
        return self


class AddFaceDeviceGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: AddFaceDeviceGroupResponseBodyData = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.data = data
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = AddFaceDeviceGroupResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddFaceDeviceGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddFaceDeviceGroupResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AddFaceDeviceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddFaceDeviceToDeviceGroupRequest(TeaModel):
    def __init__(
        self,
        isolation_id: str = None,
        iot_instance_id: str = None,
        product_key: str = None,
        device_name: str = None,
        device_group_id: str = None,
    ):
        self.isolation_id = isolation_id
        self.iot_instance_id = iot_instance_id
        self.product_key = product_key
        self.device_name = device_name
        self.device_group_id = device_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.isolation_id is not None:
            result['IsolationId'] = self.isolation_id
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.device_group_id is not None:
            result['DeviceGroupId'] = self.device_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsolationId') is not None:
            self.isolation_id = m.get('IsolationId')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('DeviceGroupId') is not None:
            self.device_group_id = m.get('DeviceGroupId')
        return self


class AddFaceDeviceToDeviceGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddFaceDeviceToDeviceGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddFaceDeviceToDeviceGroupResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AddFaceDeviceToDeviceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddFaceUserRequest(TeaModel):
    def __init__(
        self,
        isolation_id: str = None,
        face_pic_url: str = None,
        custom_user_id: str = None,
        name: str = None,
        params: str = None,
    ):
        self.isolation_id = isolation_id
        self.face_pic_url = face_pic_url
        self.custom_user_id = custom_user_id
        self.name = name
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
        if self.face_pic_url is not None:
            result['FacePicUrl'] = self.face_pic_url
        if self.custom_user_id is not None:
            result['CustomUserId'] = self.custom_user_id
        if self.name is not None:
            result['Name'] = self.name
        if self.params is not None:
            result['Params'] = self.params
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsolationId') is not None:
            self.isolation_id = m.get('IsolationId')
        if m.get('FacePicUrl') is not None:
            self.face_pic_url = m.get('FacePicUrl')
        if m.get('CustomUserId') is not None:
            self.custom_user_id = m.get('CustomUserId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Params') is not None:
            self.params = m.get('Params')
        return self


class AddFaceUserResponseBodyData(TeaModel):
    def __init__(
        self,
        params: str = None,
        custom_user_id: str = None,
        user_id: str = None,
        name: str = None,
    ):
        self.params = params
        self.custom_user_id = custom_user_id
        self.user_id = user_id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.params is not None:
            result['Params'] = self.params
        if self.custom_user_id is not None:
            result['CustomUserId'] = self.custom_user_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Params') is not None:
            self.params = m.get('Params')
        if m.get('CustomUserId') is not None:
            self.custom_user_id = m.get('CustomUserId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class AddFaceUserResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: AddFaceUserResponseBodyData = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.data = data
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = AddFaceUserResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddFaceUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddFaceUserResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
        request_id: str = None,
        data: AddFaceUserGroupResponseBodyData = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.data = data
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = AddFaceUserGroupResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddFaceUserGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddFaceUserGroupResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AddFaceUserGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddFaceUserGroupAndDeviceGroupRelationRequest(TeaModel):
    def __init__(
        self,
        isolation_id: str = None,
        iot_instance_id: str = None,
        user_group_id: str = None,
        device_group_id: str = None,
        relation: str = None,
    ):
        self.isolation_id = isolation_id
        self.iot_instance_id = iot_instance_id
        self.user_group_id = user_group_id
        self.device_group_id = device_group_id
        self.relation = relation

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.isolation_id is not None:
            result['IsolationId'] = self.isolation_id
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        if self.device_group_id is not None:
            result['DeviceGroupId'] = self.device_group_id
        if self.relation is not None:
            result['Relation'] = self.relation
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsolationId') is not None:
            self.isolation_id = m.get('IsolationId')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        if m.get('DeviceGroupId') is not None:
            self.device_group_id = m.get('DeviceGroupId')
        if m.get('Relation') is not None:
            self.relation = m.get('Relation')
        return self


class AddFaceUserGroupAndDeviceGroupRelationResponseBodyData(TeaModel):
    def __init__(
        self,
        modified_time: str = None,
        control_id: str = None,
    ):
        self.modified_time = modified_time
        self.control_id = control_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.control_id is not None:
            result['ControlId'] = self.control_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('ControlId') is not None:
            self.control_id = m.get('ControlId')
        return self


class AddFaceUserGroupAndDeviceGroupRelationResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: AddFaceUserGroupAndDeviceGroupRelationResponseBodyData = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.data = data
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = AddFaceUserGroupAndDeviceGroupRelationResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddFaceUserGroupAndDeviceGroupRelationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddFaceUserGroupAndDeviceGroupRelationResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AddFaceUserGroupAndDeviceGroupRelationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddFaceUserPictureRequest(TeaModel):
    def __init__(
        self,
        isolation_id: str = None,
        user_id: str = None,
        face_pic_url: str = None,
    ):
        self.isolation_id = isolation_id
        self.user_id = user_id
        self.face_pic_url = face_pic_url

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
        if self.face_pic_url is not None:
            result['FacePicUrl'] = self.face_pic_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsolationId') is not None:
            self.isolation_id = m.get('IsolationId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('FacePicUrl') is not None:
            self.face_pic_url = m.get('FacePicUrl')
        return self


class AddFaceUserPictureResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: Dict[str, Any] = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.data = data
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddFaceUserPictureResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddFaceUserPictureResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AddFaceUserPictureResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddFaceUserToUserGroupRequest(TeaModel):
    def __init__(
        self,
        isolation_id: str = None,
        user_id: str = None,
        user_group_id: str = None,
    ):
        self.isolation_id = isolation_id
        self.user_id = user_id
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
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsolationId') is not None:
            self.isolation_id = m.get('IsolationId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        return self


class AddFaceUserToUserGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddFaceUserToUserGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddFaceUserToUserGroupResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AddFaceUserToUserGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddRecordPlanDeviceRequest(TeaModel):
    def __init__(
        self,
        iot_id: str = None,
        plan_id: str = None,
        stream_type: int = None,
    ):
        self.iot_id = iot_id
        self.plan_id = plan_id
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
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        if self.stream_type is not None:
            result['StreamType'] = self.stream_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        if m.get('StreamType') is not None:
            self.stream_type = m.get('StreamType')
        return self


class AddRecordPlanDeviceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddRecordPlanDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddRecordPlanDeviceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AddRecordPlanDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BindAIPlanWithDevicesRequest(TeaModel):
    def __init__(
        self,
        plan_id: str = None,
        iot_id_list: List[str] = None,
    ):
        self.plan_id = plan_id
        self.iot_id_list = iot_id_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        if self.iot_id_list is not None:
            result['IotIdList'] = self.iot_id_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        if m.get('IotIdList') is not None:
            self.iot_id_list = m.get('IotIdList')
        return self


class BindAIPlanWithDevicesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class BindAIPlanWithDevicesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: BindAIPlanWithDevicesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = BindAIPlanWithDevicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BindPictureSearchAppWithDevicesRequest(TeaModel):
    def __init__(
        self,
        app_instance_id: str = None,
        iot_instance_id: str = None,
        device_iot_ids: List[str] = None,
    ):
        self.app_instance_id = app_instance_id
        self.iot_instance_id = iot_instance_id
        self.device_iot_ids = device_iot_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_id is not None:
            result['AppInstanceId'] = self.app_instance_id
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.device_iot_ids is not None:
            result['DeviceIotIds'] = self.device_iot_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceId') is not None:
            self.app_instance_id = m.get('AppInstanceId')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('DeviceIotIds') is not None:
            self.device_iot_ids = m.get('DeviceIotIds')
        return self


class BindPictureSearchAppWithDevicesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class BindPictureSearchAppWithDevicesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: BindPictureSearchAppWithDevicesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = BindPictureSearchAppWithDevicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckFaceUserDoExistOnDeviceRequest(TeaModel):
    def __init__(
        self,
        isolation_id: str = None,
        iot_instance_id: str = None,
        user_id: str = None,
        product_key: str = None,
        device_name: str = None,
    ):
        self.isolation_id = isolation_id
        self.iot_instance_id = iot_instance_id
        self.user_id = user_id
        self.product_key = product_key
        self.device_name = device_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.isolation_id is not None:
            result['IsolationId'] = self.isolation_id
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsolationId') is not None:
            self.isolation_id = m.get('IsolationId')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
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
        request_id: str = None,
        data: CheckFaceUserDoExistOnDeviceResponseBodyData = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.data = data
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = CheckFaceUserDoExistOnDeviceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CheckFaceUserDoExistOnDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CheckFaceUserDoExistOnDeviceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CheckFaceUserDoExistOnDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ClearFaceDeviceDBRequest(TeaModel):
    def __init__(
        self,
        isolation_id: str = None,
        iot_instance_id: str = None,
        product_key: str = None,
        device_name: str = None,
    ):
        self.isolation_id = isolation_id
        self.iot_instance_id = iot_instance_id
        self.product_key = product_key
        self.device_name = device_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.isolation_id is not None:
            result['IsolationId'] = self.isolation_id
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsolationId') is not None:
            self.isolation_id = m.get('IsolationId')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        return self


class ClearFaceDeviceDBResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: Dict[str, Any] = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.data = data
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ClearFaceDeviceDBResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ClearFaceDeviceDBResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ClearFaceDeviceDBResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConfigAIActionRequestDataTypeConfigList(TeaModel):
    def __init__(
        self,
        data_type: str = None,
        configs: str = None,
    ):
        self.data_type = data_type
        self.configs = configs

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.configs is not None:
            result['Configs'] = self.configs
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('Configs') is not None:
            self.configs = m.get('Configs')
        return self


class ConfigAIActionRequest(TeaModel):
    def __init__(
        self,
        action_id: str = None,
        algo_config: str = None,
        data_type_config_list: List[ConfigAIActionRequestDataTypeConfigList] = None,
    ):
        self.action_id = action_id
        self.algo_config = algo_config
        self.data_type_config_list = data_type_config_list

    def validate(self):
        if self.data_type_config_list:
            for k in self.data_type_config_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_id is not None:
            result['ActionId'] = self.action_id
        if self.algo_config is not None:
            result['AlgoConfig'] = self.algo_config
        result['DataTypeConfigList'] = []
        if self.data_type_config_list is not None:
            for k in self.data_type_config_list:
                result['DataTypeConfigList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionId') is not None:
            self.action_id = m.get('ActionId')
        if m.get('AlgoConfig') is not None:
            self.algo_config = m.get('AlgoConfig')
        self.data_type_config_list = []
        if m.get('DataTypeConfigList') is not None:
            for k in m.get('DataTypeConfigList'):
                temp_model = ConfigAIActionRequestDataTypeConfigList()
                self.data_type_config_list.append(temp_model.from_map(k))
        return self


class ConfigAIActionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ConfigAIActionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ConfigAIActionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ConfigAIActionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAIAppRequest(TeaModel):
    def __init__(
        self,
        app_template_id: str = None,
        app_template_version: str = None,
        level: int = None,
        name: str = None,
        description: str = None,
    ):
        self.app_template_id = app_template_id
        self.app_template_version = app_template_version
        self.level = level
        self.name = name
        self.description = description

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_template_id is not None:
            result['AppTemplateId'] = self.app_template_id
        if self.app_template_version is not None:
            result['AppTemplateVersion'] = self.app_template_version
        if self.level is not None:
            result['Level'] = self.level
        if self.name is not None:
            result['Name'] = self.name
        if self.description is not None:
            result['Description'] = self.description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppTemplateId') is not None:
            self.app_template_id = m.get('AppTemplateId')
        if m.get('AppTemplateVersion') is not None:
            self.app_template_version = m.get('AppTemplateVersion')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        return self


class CreateAIAppResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: str = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.data = data
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateAIAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateAIAppResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateAIAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAIPlanRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        plan_template_id: str = None,
        description: str = None,
    ):
        self.app_id = app_id
        self.plan_template_id = plan_template_id
        self.description = description

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.plan_template_id is not None:
            result['PlanTemplateId'] = self.plan_template_id
        if self.description is not None:
            result['Description'] = self.description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('PlanTemplateId') is not None:
            self.plan_template_id = m.get('PlanTemplateId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        return self


class CreateAIPlanResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: str = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.data = data
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateAIPlanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateAIPlanResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateAIPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAlgorithmRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        description: str = None,
    ):
        self.name = name
        self.description = description

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.description is not None:
            result['Description'] = self.description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        return self


class CreateAlgorithmResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: int = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.data = data
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateAlgorithmResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateAlgorithmResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateAlgorithmResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDevicePurifyJobRequest(TeaModel):
    def __init__(
        self,
        iot_id: str = None,
        start_time: int = None,
        end_time: int = None,
    ):
        self.iot_id = iot_id
        self.start_time = start_time
        self.end_time = end_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        return self


class CreateDevicePurifyJobResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: str = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.data = data
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateDevicePurifyJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateDevicePurifyJobResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateDevicePurifyJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDevicePurifyJobByPlanIdRequest(TeaModel):
    def __init__(
        self,
        plan_id: str = None,
        utc: int = None,
    ):
        self.plan_id = plan_id
        self.utc = utc

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        if self.utc is not None:
            result['Utc'] = self.utc
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        if m.get('Utc') is not None:
            self.utc = m.get('Utc')
        return self


class CreateDevicePurifyJobByPlanIdResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: str = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.data = data
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateDevicePurifyJobByPlanIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateDevicePurifyJobByPlanIdResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateDevicePurifyJobByPlanIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDevicePurifyPlanRequest(TeaModel):
    def __init__(
        self,
        iot_id: str = None,
        start_time: int = None,
        end_time: int = None,
    ):
        self.iot_id = iot_id
        self.start_time = start_time
        self.end_time = end_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        return self


class CreateDevicePurifyPlanResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: str = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.data = data
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateDevicePurifyPlanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateDevicePurifyPlanResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateDevicePurifyPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateEventRecordPlanRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        event_types: str = None,
        pre_record_duration: int = None,
        record_duration: int = None,
        template_id: str = None,
    ):
        self.name = name
        self.event_types = event_types
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
        if self.name is not None:
            result['Name'] = self.name
        if self.event_types is not None:
            result['EventTypes'] = self.event_types
        if self.pre_record_duration is not None:
            result['PreRecordDuration'] = self.pre_record_duration
        if self.record_duration is not None:
            result['RecordDuration'] = self.record_duration
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('EventTypes') is not None:
            self.event_types = m.get('EventTypes')
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
        request_id: str = None,
        data: str = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.data = data
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateEventRecordPlanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateEventRecordPlanResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateEventRecordPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateModelRequest(TeaModel):
    def __init__(
        self,
        algorithm_id: int = None,
        name: str = None,
        model_package_standard: str = None,
        hardware: str = None,
        upload_model_path: str = None,
        need_encrypt: bool = None,
        description: str = None,
    ):
        self.algorithm_id = algorithm_id
        self.name = name
        self.model_package_standard = model_package_standard
        self.hardware = hardware
        self.upload_model_path = upload_model_path
        self.need_encrypt = need_encrypt
        self.description = description

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm_id is not None:
            result['AlgorithmId'] = self.algorithm_id
        if self.name is not None:
            result['Name'] = self.name
        if self.model_package_standard is not None:
            result['ModelPackageStandard'] = self.model_package_standard
        if self.hardware is not None:
            result['Hardware'] = self.hardware
        if self.upload_model_path is not None:
            result['UploadModelPath'] = self.upload_model_path
        if self.need_encrypt is not None:
            result['NeedEncrypt'] = self.need_encrypt
        if self.description is not None:
            result['Description'] = self.description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlgorithmId') is not None:
            self.algorithm_id = m.get('AlgorithmId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ModelPackageStandard') is not None:
            self.model_package_standard = m.get('ModelPackageStandard')
        if m.get('Hardware') is not None:
            self.hardware = m.get('Hardware')
        if m.get('UploadModelPath') is not None:
            self.upload_model_path = m.get('UploadModelPath')
        if m.get('NeedEncrypt') is not None:
            self.need_encrypt = m.get('NeedEncrypt')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        return self


class CreateModelResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: Dict[str, Any] = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.data = data
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateModelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateModelResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateModelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePictureSearchAppRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        desc: str = None,
    ):
        self.name = name
        self.desc = desc

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.desc is not None:
            result['Desc'] = self.desc
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
        return self


class CreatePictureSearchAppResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: str = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.data = data
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreatePictureSearchAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreatePictureSearchAppResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreatePictureSearchAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePictureSearchJobRequest(TeaModel):
    def __init__(
        self,
        app_instance_id: str = None,
        search_pic_url: str = None,
        start_time: int = None,
        end_time: int = None,
        threshold: float = None,
        body_threshold: float = None,
        picture_search_type: int = None,
    ):
        self.app_instance_id = app_instance_id
        self.search_pic_url = search_pic_url
        self.start_time = start_time
        self.end_time = end_time
        self.threshold = threshold
        self.body_threshold = body_threshold
        self.picture_search_type = picture_search_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_id is not None:
            result['AppInstanceId'] = self.app_instance_id
        if self.search_pic_url is not None:
            result['SearchPicUrl'] = self.search_pic_url
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        if self.body_threshold is not None:
            result['BodyThreshold'] = self.body_threshold
        if self.picture_search_type is not None:
            result['PictureSearchType'] = self.picture_search_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceId') is not None:
            self.app_instance_id = m.get('AppInstanceId')
        if m.get('SearchPicUrl') is not None:
            self.search_pic_url = m.get('SearchPicUrl')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        if m.get('BodyThreshold') is not None:
            self.body_threshold = m.get('BodyThreshold')
        if m.get('PictureSearchType') is not None:
            self.picture_search_type = m.get('PictureSearchType')
        return self


class CreatePictureSearchJobResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: str = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.data = data
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreatePictureSearchJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreatePictureSearchJobResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreatePictureSearchJobResponseBody()
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
        request_id: str = None,
        data: str = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.data = data
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateRecordPlanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateRecordPlanResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateRecordPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTimeTemplateRequestTimeSections(TeaModel):
    def __init__(
        self,
        day_of_week: int = None,
        begin: int = None,
        end: int = None,
    ):
        self.day_of_week = day_of_week
        self.begin = begin
        self.end = end

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.day_of_week is not None:
            result['DayOfWeek'] = self.day_of_week
        if self.begin is not None:
            result['Begin'] = self.begin
        if self.end is not None:
            result['End'] = self.end
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DayOfWeek') is not None:
            self.day_of_week = m.get('DayOfWeek')
        if m.get('Begin') is not None:
            self.begin = m.get('Begin')
        if m.get('End') is not None:
            self.end = m.get('End')
        return self


class CreateTimeTemplateRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        all_day: int = None,
        time_sections: List[CreateTimeTemplateRequestTimeSections] = None,
    ):
        self.name = name
        self.all_day = all_day
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
        if self.name is not None:
            result['Name'] = self.name
        if self.all_day is not None:
            result['AllDay'] = self.all_day
        result['TimeSections'] = []
        if self.time_sections is not None:
            for k in self.time_sections:
                result['TimeSections'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('AllDay') is not None:
            self.all_day = m.get('AllDay')
        self.time_sections = []
        if m.get('TimeSections') is not None:
            for k in m.get('TimeSections'):
                temp_model = CreateTimeTemplateRequestTimeSections()
                self.time_sections.append(temp_model.from_map(k))
        return self


class CreateTimeTemplateResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: str = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.data = data
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateTimeTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateTimeTemplateResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateTimeTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAlgorithmRequest(TeaModel):
    def __init__(
        self,
        algorithm_id: int = None,
    ):
        self.algorithm_id = algorithm_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm_id is not None:
            result['AlgorithmId'] = self.algorithm_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlgorithmId') is not None:
            self.algorithm_id = m.get('AlgorithmId')
        return self


class DeleteAlgorithmResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteAlgorithmResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteAlgorithmResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteAlgorithmResponseBody()
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
        request_id: str = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteEventRecordPlanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteEventRecordPlanResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteEventRecordPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteEventRecordPlanDeviceRequest(TeaModel):
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


class DeleteEventRecordPlanDeviceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteEventRecordPlanDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteEventRecordPlanDeviceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteEventRecordPlanDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteFaceDeviceGroupRequest(TeaModel):
    def __init__(
        self,
        isolation_id: str = None,
        device_group_id: str = None,
    ):
        self.isolation_id = isolation_id
        self.device_group_id = device_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.isolation_id is not None:
            result['IsolationId'] = self.isolation_id
        if self.device_group_id is not None:
            result['DeviceGroupId'] = self.device_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsolationId') is not None:
            self.isolation_id = m.get('IsolationId')
        if m.get('DeviceGroupId') is not None:
            self.device_group_id = m.get('DeviceGroupId')
        return self


class DeleteFaceDeviceGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteFaceDeviceGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteFaceDeviceGroupResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
        request_id: str = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteFaceUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteFaceUserResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
        request_id: str = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteFaceUserGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteFaceUserGroupResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteFaceUserGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteFaceUserGroupAndDeviceGroupRelationRequest(TeaModel):
    def __init__(
        self,
        isolation_id: str = None,
        control_id: str = None,
    ):
        self.isolation_id = isolation_id
        self.control_id = control_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.isolation_id is not None:
            result['IsolationId'] = self.isolation_id
        if self.control_id is not None:
            result['ControlId'] = self.control_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsolationId') is not None:
            self.isolation_id = m.get('IsolationId')
        if m.get('ControlId') is not None:
            self.control_id = m.get('ControlId')
        return self


class DeleteFaceUserGroupAndDeviceGroupRelationResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteFaceUserGroupAndDeviceGroupRelationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteFaceUserGroupAndDeviceGroupRelationResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteFaceUserGroupAndDeviceGroupRelationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteFaceUserPictureRequest(TeaModel):
    def __init__(
        self,
        isolation_id: str = None,
        user_id: str = None,
        face_pic_md_5: str = None,
    ):
        self.isolation_id = isolation_id
        self.user_id = user_id
        self.face_pic_md_5 = face_pic_md_5

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
        if self.face_pic_md_5 is not None:
            result['FacePicMd5'] = self.face_pic_md_5
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsolationId') is not None:
            self.isolation_id = m.get('IsolationId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('FacePicMd5') is not None:
            self.face_pic_md_5 = m.get('FacePicMd5')
        return self


class DeleteFaceUserPictureResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteFaceUserPictureResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteFaceUserPictureResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteFaceUserPictureResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteModelRequest(TeaModel):
    def __init__(
        self,
        model_id: int = None,
    ):
        self.model_id = model_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.model_id is not None:
            result['ModelId'] = self.model_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')
        return self


class DeleteModelResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteModelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteModelResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteModelResponseBody()
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
        request_id: str = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteRecordPlanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteRecordPlanResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteRecordPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRecordPlanDeviceRequest(TeaModel):
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


class DeleteRecordPlanDeviceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteRecordPlanDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteRecordPlanDeviceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteRecordPlanDeviceResponseBody()
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
        request_id: str = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteTimeTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteTimeTemplateResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteTimeTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeployModelBatchRequestDeviceList(TeaModel):
    def __init__(
        self,
        product_key: str = None,
        device_name: str = None,
        iot_id: str = None,
    ):
        self.product_key = product_key
        self.device_name = device_name
        self.iot_id = iot_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        return self


class DeployModelBatchRequest(TeaModel):
    def __init__(
        self,
        model_id: int = None,
        device_list: List[DeployModelBatchRequestDeviceList] = None,
    ):
        self.model_id = model_id
        self.device_list = device_list

    def validate(self):
        if self.device_list:
            for k in self.device_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.model_id is not None:
            result['ModelId'] = self.model_id
        result['DeviceList'] = []
        if self.device_list is not None:
            for k in self.device_list:
                result['DeviceList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')
        self.device_list = []
        if m.get('DeviceList') is not None:
            for k in m.get('DeviceList'):
                temp_model = DeployModelBatchRequestDeviceList()
                self.device_list.append(temp_model.from_map(k))
        return self


class DeployModelBatchResponseBodyData(TeaModel):
    def __init__(
        self,
        deploy_task_result_volist: List[Dict[str, Any]] = None,
    ):
        self.deploy_task_result_volist = deploy_task_result_volist

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deploy_task_result_volist is not None:
            result['DeployTaskResultVOList'] = self.deploy_task_result_volist
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeployTaskResultVOList') is not None:
            self.deploy_task_result_volist = m.get('DeployTaskResultVOList')
        return self


class DeployModelBatchResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: DeployModelBatchResponseBodyData = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.data = data
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = DeployModelBatchResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeployModelBatchResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeployModelBatchResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeployModelBatchResponseBody()
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
        blur_score: float = None,
        gender: int = None,
        face_rects: DetectUserFaceByUrlResponseBodyDataDataFaceRects = None,
        occlusion_score: float = None,
        good_for_library: bool = None,
        good_for_recognition: bool = None,
        age: int = None,
        landmarks: DetectUserFaceByUrlResponseBodyDataDataLandmarks = None,
        face_probability: float = None,
        pose_score: float = None,
    ):
        self.blur_score = blur_score
        self.gender = gender
        self.face_rects = face_rects
        self.occlusion_score = occlusion_score
        self.good_for_library = good_for_library
        self.good_for_recognition = good_for_recognition
        self.age = age
        self.landmarks = landmarks
        self.face_probability = face_probability
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
        if self.blur_score is not None:
            result['BlurScore'] = self.blur_score
        if self.gender is not None:
            result['Gender'] = self.gender
        if self.face_rects is not None:
            result['FaceRects'] = self.face_rects.to_map()
        if self.occlusion_score is not None:
            result['OcclusionScore'] = self.occlusion_score
        if self.good_for_library is not None:
            result['GoodForLibrary'] = self.good_for_library
        if self.good_for_recognition is not None:
            result['GoodForRecognition'] = self.good_for_recognition
        if self.age is not None:
            result['Age'] = self.age
        if self.landmarks is not None:
            result['Landmarks'] = self.landmarks.to_map()
        if self.face_probability is not None:
            result['FaceProbability'] = self.face_probability
        if self.pose_score is not None:
            result['PoseScore'] = self.pose_score
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BlurScore') is not None:
            self.blur_score = m.get('BlurScore')
        if m.get('Gender') is not None:
            self.gender = m.get('Gender')
        if m.get('FaceRects') is not None:
            temp_model = DetectUserFaceByUrlResponseBodyDataDataFaceRects()
            self.face_rects = temp_model.from_map(m['FaceRects'])
        if m.get('OcclusionScore') is not None:
            self.occlusion_score = m.get('OcclusionScore')
        if m.get('GoodForLibrary') is not None:
            self.good_for_library = m.get('GoodForLibrary')
        if m.get('GoodForRecognition') is not None:
            self.good_for_recognition = m.get('GoodForRecognition')
        if m.get('Age') is not None:
            self.age = m.get('Age')
        if m.get('Landmarks') is not None:
            temp_model = DetectUserFaceByUrlResponseBodyDataDataLandmarks()
            self.landmarks = temp_model.from_map(m['Landmarks'])
        if m.get('FaceProbability') is not None:
            self.face_probability = m.get('FaceProbability')
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
        request_id: str = None,
        data: DetectUserFaceByUrlResponseBodyData = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.data = data
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = DetectUserFaceByUrlResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DetectUserFaceByUrlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DetectUserFaceByUrlResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DetectUserFaceByUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAIActionRequest(TeaModel):
    def __init__(
        self,
        action_id: str = None,
    ):
        self.action_id = action_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_id is not None:
            result['ActionId'] = self.action_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionId') is not None:
            self.action_id = m.get('ActionId')
        return self


class GetAIActionResponseBodyData(TeaModel):
    def __init__(
        self,
        algo_config: str = None,
        action: str = None,
        action_id: str = None,
        action_template_id: str = None,
        alog: str = None,
        action_index: int = None,
        action_config: str = None,
        plan_id: str = None,
    ):
        self.algo_config = algo_config
        self.action = action
        self.action_id = action_id
        self.action_template_id = action_template_id
        self.alog = alog
        self.action_index = action_index
        self.action_config = action_config
        self.plan_id = plan_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algo_config is not None:
            result['AlgoConfig'] = self.algo_config
        if self.action is not None:
            result['Action'] = self.action
        if self.action_id is not None:
            result['ActionId'] = self.action_id
        if self.action_template_id is not None:
            result['ActionTemplateId'] = self.action_template_id
        if self.alog is not None:
            result['Alog'] = self.alog
        if self.action_index is not None:
            result['ActionIndex'] = self.action_index
        if self.action_config is not None:
            result['ActionConfig'] = self.action_config
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlgoConfig') is not None:
            self.algo_config = m.get('AlgoConfig')
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('ActionId') is not None:
            self.action_id = m.get('ActionId')
        if m.get('ActionTemplateId') is not None:
            self.action_template_id = m.get('ActionTemplateId')
        if m.get('Alog') is not None:
            self.alog = m.get('Alog')
        if m.get('ActionIndex') is not None:
            self.action_index = m.get('ActionIndex')
        if m.get('ActionConfig') is not None:
            self.action_config = m.get('ActionConfig')
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        return self


class GetAIActionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: GetAIActionResponseBodyData = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.data = data
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = GetAIActionResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetAIActionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetAIActionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetAIActionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAIActionConfigRequest(TeaModel):
    def __init__(
        self,
        algo: str = None,
        algo_action: str = None,
    ):
        self.algo = algo
        self.algo_action = algo_action

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algo is not None:
            result['Algo'] = self.algo
        if self.algo_action is not None:
            result['AlgoAction'] = self.algo_action
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Algo') is not None:
            self.algo = m.get('Algo')
        if m.get('AlgoAction') is not None:
            self.algo_action = m.get('AlgoAction')
        return self


class GetAIActionConfigResponseBodyDataInParamList(TeaModel):
    def __init__(
        self,
        need_config: bool = None,
        data_type: str = None,
        config_items: List[str] = None,
    ):
        self.need_config = need_config
        self.data_type = data_type
        self.config_items = config_items

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.need_config is not None:
            result['NeedConfig'] = self.need_config
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.config_items is not None:
            result['ConfigItems'] = self.config_items
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NeedConfig') is not None:
            self.need_config = m.get('NeedConfig')
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('ConfigItems') is not None:
            self.config_items = m.get('ConfigItems')
        return self


class GetAIActionConfigResponseBodyDataOutParamList(TeaModel):
    def __init__(
        self,
        need_config: bool = None,
        data_type: str = None,
        config_items: List[str] = None,
    ):
        self.need_config = need_config
        self.data_type = data_type
        self.config_items = config_items

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.need_config is not None:
            result['NeedConfig'] = self.need_config
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.config_items is not None:
            result['ConfigItems'] = self.config_items
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NeedConfig') is not None:
            self.need_config = m.get('NeedConfig')
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('ConfigItems') is not None:
            self.config_items = m.get('ConfigItems')
        return self


class GetAIActionConfigResponseBodyData(TeaModel):
    def __init__(
        self,
        in_param_list: List[GetAIActionConfigResponseBodyDataInParamList] = None,
        algo_action: str = None,
        sync: str = None,
        need_device: bool = None,
        out_param_list: List[GetAIActionConfigResponseBodyDataOutParamList] = None,
        algo_config_items: str = None,
        des: str = None,
    ):
        self.in_param_list = in_param_list
        self.algo_action = algo_action
        self.sync = sync
        self.need_device = need_device
        self.out_param_list = out_param_list
        self.algo_config_items = algo_config_items
        self.des = des

    def validate(self):
        if self.in_param_list:
            for k in self.in_param_list:
                if k:
                    k.validate()
        if self.out_param_list:
            for k in self.out_param_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['InParamList'] = []
        if self.in_param_list is not None:
            for k in self.in_param_list:
                result['InParamList'].append(k.to_map() if k else None)
        if self.algo_action is not None:
            result['AlgoAction'] = self.algo_action
        if self.sync is not None:
            result['Sync'] = self.sync
        if self.need_device is not None:
            result['NeedDevice'] = self.need_device
        result['OutParamList'] = []
        if self.out_param_list is not None:
            for k in self.out_param_list:
                result['OutParamList'].append(k.to_map() if k else None)
        if self.algo_config_items is not None:
            result['AlgoConfigItems'] = self.algo_config_items
        if self.des is not None:
            result['Des'] = self.des
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.in_param_list = []
        if m.get('InParamList') is not None:
            for k in m.get('InParamList'):
                temp_model = GetAIActionConfigResponseBodyDataInParamList()
                self.in_param_list.append(temp_model.from_map(k))
        if m.get('AlgoAction') is not None:
            self.algo_action = m.get('AlgoAction')
        if m.get('Sync') is not None:
            self.sync = m.get('Sync')
        if m.get('NeedDevice') is not None:
            self.need_device = m.get('NeedDevice')
        self.out_param_list = []
        if m.get('OutParamList') is not None:
            for k in m.get('OutParamList'):
                temp_model = GetAIActionConfigResponseBodyDataOutParamList()
                self.out_param_list.append(temp_model.from_map(k))
        if m.get('AlgoConfigItems') is not None:
            self.algo_config_items = m.get('AlgoConfigItems')
        if m.get('Des') is not None:
            self.des = m.get('Des')
        return self


class GetAIActionConfigResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: GetAIActionConfigResponseBodyData = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.data = data
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = GetAIActionConfigResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetAIActionConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetAIActionConfigResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetAIActionConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAIAppRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
    ):
        self.app_id = app_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        return self


class GetAIAppResponseBodyData(TeaModel):
    def __init__(
        self,
        description: str = None,
        version: str = None,
        app_id: str = None,
        app_template_id: str = None,
        name: str = None,
        level: int = None,
    ):
        self.description = description
        self.version = version
        self.app_id = app_id
        self.app_template_id = app_template_id
        self.name = name
        self.level = level

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.version is not None:
            result['Version'] = self.version
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_template_id is not None:
            result['AppTemplateId'] = self.app_template_id
        if self.name is not None:
            result['Name'] = self.name
        if self.level is not None:
            result['Level'] = self.level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppTemplateId') is not None:
            self.app_template_id = m.get('AppTemplateId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        return self


class GetAIAppResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: GetAIAppResponseBodyData = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.data = data
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = GetAIAppResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetAIAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetAIAppResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetAIAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAIJobRequest(TeaModel):
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


class GetAIJobResponseBodyDataDataDTOList(TeaModel):
    def __init__(
        self,
        data_source: str = None,
        data_type: str = None,
        algo_data: str = None,
        job_id: str = None,
        data_id: str = None,
        iot_id: str = None,
    ):
        self.data_source = data_source
        self.data_type = data_type
        self.algo_data = algo_data
        self.job_id = job_id
        self.data_id = data_id
        self.iot_id = iot_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_source is not None:
            result['DataSource'] = self.data_source
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.algo_data is not None:
            result['AlgoData'] = self.algo_data
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSource') is not None:
            self.data_source = m.get('DataSource')
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('AlgoData') is not None:
            self.algo_data = m.get('AlgoData')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        return self


class GetAIJobResponseBodyDataActionJobDTO(TeaModel):
    def __init__(
        self,
        status: int = None,
        job_id: str = None,
        action_id: str = None,
        iot_id: str = None,
    ):
        self.status = status
        self.job_id = job_id
        self.action_id = action_id
        self.iot_id = iot_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.action_id is not None:
            result['ActionId'] = self.action_id
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('ActionId') is not None:
            self.action_id = m.get('ActionId')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        return self


class GetAIJobResponseBodyData(TeaModel):
    def __init__(
        self,
        data_dtolist: List[GetAIJobResponseBodyDataDataDTOList] = None,
        action_job_dto: GetAIJobResponseBodyDataActionJobDTO = None,
    ):
        self.data_dtolist = data_dtolist
        self.action_job_dto = action_job_dto

    def validate(self):
        if self.data_dtolist:
            for k in self.data_dtolist:
                if k:
                    k.validate()
        if self.action_job_dto:
            self.action_job_dto.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataDTOList'] = []
        if self.data_dtolist is not None:
            for k in self.data_dtolist:
                result['DataDTOList'].append(k.to_map() if k else None)
        if self.action_job_dto is not None:
            result['ActionJobDTO'] = self.action_job_dto.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_dtolist = []
        if m.get('DataDTOList') is not None:
            for k in m.get('DataDTOList'):
                temp_model = GetAIJobResponseBodyDataDataDTOList()
                self.data_dtolist.append(temp_model.from_map(k))
        if m.get('ActionJobDTO') is not None:
            temp_model = GetAIJobResponseBodyDataActionJobDTO()
            self.action_job_dto = temp_model.from_map(m['ActionJobDTO'])
        return self


class GetAIJobResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: GetAIJobResponseBodyData = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.data = data
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = GetAIJobResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetAIJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetAIJobResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetAIJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAIPlanRequest(TeaModel):
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


class GetAIPlanResponseBodyData(TeaModel):
    def __init__(
        self,
        plan_template_id: str = None,
        trigger_enum: int = None,
        description: str = None,
        pre_timing: int = None,
        app_id: str = None,
        interval_timing: int = None,
        plan_id: str = None,
    ):
        self.plan_template_id = plan_template_id
        self.trigger_enum = trigger_enum
        self.description = description
        self.pre_timing = pre_timing
        self.app_id = app_id
        self.interval_timing = interval_timing
        self.plan_id = plan_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.plan_template_id is not None:
            result['PlanTemplateId'] = self.plan_template_id
        if self.trigger_enum is not None:
            result['TriggerEnum'] = self.trigger_enum
        if self.description is not None:
            result['Description'] = self.description
        if self.pre_timing is not None:
            result['PreTiming'] = self.pre_timing
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.interval_timing is not None:
            result['IntervalTiming'] = self.interval_timing
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PlanTemplateId') is not None:
            self.plan_template_id = m.get('PlanTemplateId')
        if m.get('TriggerEnum') is not None:
            self.trigger_enum = m.get('TriggerEnum')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('PreTiming') is not None:
            self.pre_timing = m.get('PreTiming')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('IntervalTiming') is not None:
            self.interval_timing = m.get('IntervalTiming')
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        return self


class GetAIPlanResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: GetAIPlanResponseBodyData = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.data = data
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = GetAIPlanResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetAIPlanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetAIPlanResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetAIPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAlgorithmDetailByIdRequest(TeaModel):
    def __init__(
        self,
        algorithm_id: int = None,
    ):
        self.algorithm_id = algorithm_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm_id is not None:
            result['AlgorithmId'] = self.algorithm_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlgorithmId') is not None:
            self.algorithm_id = m.get('AlgorithmId')
        return self


class GetAlgorithmDetailByIdResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: Dict[str, Any] = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.data = data
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetAlgorithmDetailByIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetAlgorithmDetailByIdResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetAlgorithmDetailByIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAlgorithmDetailByNameRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
    ):
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class GetAlgorithmDetailByNameResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: Dict[str, Any] = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.data = data
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetAlgorithmDetailByNameResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetAlgorithmDetailByNameResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetAlgorithmDetailByNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDevicePurifyJobByJobIdRequest(TeaModel):
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


class GetDevicePurifyJobByJobIdResponseBodyData(TeaModel):
    def __init__(
        self,
        status: int = None,
        device_name: str = None,
        user_id: str = None,
        plan_id: str = None,
        end_time: int = None,
        start_time: int = None,
        purify_record_index_url: str = None,
        product_key: str = None,
        purify_record_name_url: str = None,
        job_id: str = None,
        iot_id: str = None,
        tenant_id: str = None,
    ):
        self.status = status
        self.device_name = device_name
        self.user_id = user_id
        self.plan_id = plan_id
        self.end_time = end_time
        self.start_time = start_time
        self.purify_record_index_url = purify_record_index_url
        self.product_key = product_key
        self.purify_record_name_url = purify_record_name_url
        self.job_id = job_id
        self.iot_id = iot_id
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.purify_record_index_url is not None:
            result['PurifyRecordIndexUrl'] = self.purify_record_index_url
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        if self.purify_record_name_url is not None:
            result['PurifyRecordNameUrl'] = self.purify_record_name_url
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('PurifyRecordIndexUrl') is not None:
            self.purify_record_index_url = m.get('PurifyRecordIndexUrl')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        if m.get('PurifyRecordNameUrl') is not None:
            self.purify_record_name_url = m.get('PurifyRecordNameUrl')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class GetDevicePurifyJobByJobIdResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: GetDevicePurifyJobByJobIdResponseBodyData = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.data = data
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = GetDevicePurifyJobByJobIdResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetDevicePurifyJobByJobIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetDevicePurifyJobByJobIdResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetDevicePurifyJobByJobIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetModelDetailRequest(TeaModel):
    def __init__(
        self,
        algorithm_id: int = None,
        version: str = None,
    ):
        self.algorithm_id = algorithm_id
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm_id is not None:
            result['AlgorithmId'] = self.algorithm_id
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlgorithmId') is not None:
            self.algorithm_id = m.get('AlgorithmId')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class GetModelDetailResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: Dict[str, Any] = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.data = data
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetModelDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetModelDetailResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetModelDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetModelDetailByIdRequest(TeaModel):
    def __init__(
        self,
        model_id: int = None,
    ):
        self.model_id = model_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.model_id is not None:
            result['ModelId'] = self.model_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')
        return self


class GetModelDetailByIdResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: Dict[str, Any] = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.data = data
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetModelDetailByIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetModelDetailByIdResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetModelDetailByIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetModelOssPolicyRequest(TeaModel):
    def __init__(
        self,
        algorithm_id: int = None,
        hardware: str = None,
        model_package_standard: str = None,
    ):
        self.algorithm_id = algorithm_id
        self.hardware = hardware
        self.model_package_standard = model_package_standard

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm_id is not None:
            result['AlgorithmId'] = self.algorithm_id
        if self.hardware is not None:
            result['Hardware'] = self.hardware
        if self.model_package_standard is not None:
            result['ModelPackageStandard'] = self.model_package_standard
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlgorithmId') is not None:
            self.algorithm_id = m.get('AlgorithmId')
        if m.get('Hardware') is not None:
            self.hardware = m.get('Hardware')
        if m.get('ModelPackageStandard') is not None:
            self.model_package_standard = m.get('ModelPackageStandard')
        return self


class GetModelOssPolicyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: Dict[str, Any] = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.data = data
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetModelOssPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetModelOssPolicyResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetModelOssPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPictureInfoWithVectorIdsRequest(TeaModel):
    def __init__(
        self,
        vector_id_list: List[str] = None,
    ):
        self.vector_id_list = vector_id_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.vector_id_list is not None:
            result['VectorIdList'] = self.vector_id_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VectorIdList') is not None:
            self.vector_id_list = m.get('VectorIdList')
        return self


class GetPictureInfoWithVectorIdsResponseBodyData(TeaModel):
    def __init__(
        self,
        pic_url: str = None,
        gateway_iot_id: str = None,
        iot_id: str = None,
    ):
        self.pic_url = pic_url
        self.gateway_iot_id = gateway_iot_id
        self.iot_id = iot_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pic_url is not None:
            result['PicUrl'] = self.pic_url
        if self.gateway_iot_id is not None:
            result['GatewayIotId'] = self.gateway_iot_id
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PicUrl') is not None:
            self.pic_url = m.get('PicUrl')
        if m.get('GatewayIotId') is not None:
            self.gateway_iot_id = m.get('GatewayIotId')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        return self


class GetPictureInfoWithVectorIdsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: List[GetPictureInfoWithVectorIdsResponseBodyData] = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.data = data
        self.error_message = error_message
        self.code = code
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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetPictureInfoWithVectorIdsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetPictureInfoWithVectorIdsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetPictureInfoWithVectorIdsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetPictureInfoWithVectorIdsResponseBody()
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
        end_time: int = None,
        start_time: int = None,
        job_status: int = None,
        search_pic_url: str = None,
        create_time: int = None,
        job_id: str = None,
        threshold: float = None,
    ):
        self.end_time = end_time
        self.start_time = start_time
        self.job_status = job_status
        self.search_pic_url = search_pic_url
        self.create_time = create_time
        self.job_id = job_id
        self.threshold = threshold

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.job_status is not None:
            result['JobStatus'] = self.job_status
        if self.search_pic_url is not None:
            result['SearchPicUrl'] = self.search_pic_url
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('JobStatus') is not None:
            self.job_status = m.get('JobStatus')
        if m.get('SearchPicUrl') is not None:
            self.search_pic_url = m.get('SearchPicUrl')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        return self


class GetPictureSearchJobStatusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: GetPictureSearchJobStatusResponseBodyData = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.data = data
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = GetPictureSearchJobStatusResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetPictureSearchJobStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetPictureSearchJobStatusResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetPictureSearchJobStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPictureWithVectorIdRequest(TeaModel):
    def __init__(
        self,
        vector_id: str = None,
    ):
        self.vector_id = vector_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.vector_id is not None:
            result['VectorId'] = self.vector_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VectorId') is not None:
            self.vector_id = m.get('VectorId')
        return self


class GetPictureWithVectorIdResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: str = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.data = data
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetPictureWithVectorIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetPictureWithVectorIdResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetPictureWithVectorIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAlgorithmsByPageRequest(TeaModel):
    def __init__(
        self,
        name_pattern: str = None,
        page_size: int = None,
        current_page: int = None,
    ):
        self.name_pattern = name_pattern
        self.page_size = page_size
        self.current_page = current_page

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name_pattern is not None:
            result['NamePattern'] = self.name_pattern
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NamePattern') is not None:
            self.name_pattern = m.get('NamePattern')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        return self


class ListAlgorithmsByPageResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: Dict[str, Any] = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.data = data
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListAlgorithmsByPageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListAlgorithmsByPageResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListAlgorithmsByPageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDeployTaskByModelIdAndDevicesRequestDeviceList(TeaModel):
    def __init__(
        self,
        product_key: str = None,
        device_name: str = None,
        iot_id: str = None,
    ):
        self.product_key = product_key
        self.device_name = device_name
        self.iot_id = iot_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        return self


class ListDeployTaskByModelIdAndDevicesRequest(TeaModel):
    def __init__(
        self,
        model_id: int = None,
        device_list: List[ListDeployTaskByModelIdAndDevicesRequestDeviceList] = None,
    ):
        self.model_id = model_id
        self.device_list = device_list

    def validate(self):
        if self.device_list:
            for k in self.device_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.model_id is not None:
            result['ModelId'] = self.model_id
        result['DeviceList'] = []
        if self.device_list is not None:
            for k in self.device_list:
                result['DeviceList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')
        self.device_list = []
        if m.get('DeviceList') is not None:
            for k in m.get('DeviceList'):
                temp_model = ListDeployTaskByModelIdAndDevicesRequestDeviceList()
                self.device_list.append(temp_model.from_map(k))
        return self


class ListDeployTaskByModelIdAndDevicesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: Dict[str, Any] = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.data = data
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListDeployTaskByModelIdAndDevicesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListDeployTaskByModelIdAndDevicesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListDeployTaskByModelIdAndDevicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDeployTaskByPageRequest(TeaModel):
    def __init__(
        self,
        page_size: int = None,
        current_page: int = None,
    ):
        self.page_size = page_size
        self.current_page = current_page

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        return self


class ListDeployTaskByPageResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: Dict[str, Any] = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.data = data
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListDeployTaskByPageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListDeployTaskByPageResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListDeployTaskByPageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListModelsByPageRequest(TeaModel):
    def __init__(
        self,
        algorithm_id: int = None,
        size_type: str = None,
        model_package_standard: str = None,
        hardware: str = None,
        name_pattern: str = None,
        page_size: int = None,
        current_page: int = None,
    ):
        self.algorithm_id = algorithm_id
        self.size_type = size_type
        self.model_package_standard = model_package_standard
        self.hardware = hardware
        self.name_pattern = name_pattern
        self.page_size = page_size
        self.current_page = current_page

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm_id is not None:
            result['AlgorithmId'] = self.algorithm_id
        if self.size_type is not None:
            result['SizeType'] = self.size_type
        if self.model_package_standard is not None:
            result['ModelPackageStandard'] = self.model_package_standard
        if self.hardware is not None:
            result['Hardware'] = self.hardware
        if self.name_pattern is not None:
            result['NamePattern'] = self.name_pattern
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlgorithmId') is not None:
            self.algorithm_id = m.get('AlgorithmId')
        if m.get('SizeType') is not None:
            self.size_type = m.get('SizeType')
        if m.get('ModelPackageStandard') is not None:
            self.model_package_standard = m.get('ModelPackageStandard')
        if m.get('Hardware') is not None:
            self.hardware = m.get('Hardware')
        if m.get('NamePattern') is not None:
            self.name_pattern = m.get('NamePattern')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        return self


class ListModelsByPageResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: Dict[str, Any] = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.data = data
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListModelsByPageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListModelsByPageResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListModelsByPageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListModelVersionsByPageRequest(TeaModel):
    def __init__(
        self,
        algorithm_name: str = None,
        size_type: str = None,
        model_package_standard: str = None,
        hardware: str = None,
        page_size: int = None,
        current_page: int = None,
    ):
        self.algorithm_name = algorithm_name
        self.size_type = size_type
        self.model_package_standard = model_package_standard
        self.hardware = hardware
        self.page_size = page_size
        self.current_page = current_page

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm_name is not None:
            result['AlgorithmName'] = self.algorithm_name
        if self.size_type is not None:
            result['SizeType'] = self.size_type
        if self.model_package_standard is not None:
            result['ModelPackageStandard'] = self.model_package_standard
        if self.hardware is not None:
            result['Hardware'] = self.hardware
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlgorithmName') is not None:
            self.algorithm_name = m.get('AlgorithmName')
        if m.get('SizeType') is not None:
            self.size_type = m.get('SizeType')
        if m.get('ModelPackageStandard') is not None:
            self.model_package_standard = m.get('ModelPackageStandard')
        if m.get('Hardware') is not None:
            self.hardware = m.get('Hardware')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        return self


class ListModelVersionsByPageResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: Dict[str, Any] = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.data = data
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListModelVersionsByPageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListModelVersionsByPageResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListModelVersionsByPageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PictureSearchPictureRequest(TeaModel):
    def __init__(
        self,
        app_instance_id: str = None,
        page_size: int = None,
        current_page: int = None,
        search_pic_url: str = None,
        start_time: int = None,
        end_time: int = None,
        threshold: float = None,
        contain_pic_url: bool = None,
        picture_search_type: int = None,
    ):
        self.app_instance_id = app_instance_id
        self.page_size = page_size
        self.current_page = current_page
        self.search_pic_url = search_pic_url
        self.start_time = start_time
        self.end_time = end_time
        self.threshold = threshold
        self.contain_pic_url = contain_pic_url
        self.picture_search_type = picture_search_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_id is not None:
            result['AppInstanceId'] = self.app_instance_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.search_pic_url is not None:
            result['SearchPicUrl'] = self.search_pic_url
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        if self.contain_pic_url is not None:
            result['ContainPicUrl'] = self.contain_pic_url
        if self.picture_search_type is not None:
            result['PictureSearchType'] = self.picture_search_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceId') is not None:
            self.app_instance_id = m.get('AppInstanceId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('SearchPicUrl') is not None:
            self.search_pic_url = m.get('SearchPicUrl')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        if m.get('ContainPicUrl') is not None:
            self.contain_pic_url = m.get('ContainPicUrl')
        if m.get('PictureSearchType') is not None:
            self.picture_search_type = m.get('PictureSearchType')
        return self


class PictureSearchPictureResponseBodyDataPageData(TeaModel):
    def __init__(
        self,
        pic_url: str = None,
        event_time: int = None,
        gateway_iot_id: str = None,
        vector_id: str = None,
        threshold: float = None,
        vector_type: int = None,
        iot_id: str = None,
    ):
        self.pic_url = pic_url
        self.event_time = event_time
        self.gateway_iot_id = gateway_iot_id
        self.vector_id = vector_id
        self.threshold = threshold
        self.vector_type = vector_type
        self.iot_id = iot_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pic_url is not None:
            result['PicUrl'] = self.pic_url
        if self.event_time is not None:
            result['EventTime'] = self.event_time
        if self.gateway_iot_id is not None:
            result['GatewayIotId'] = self.gateway_iot_id
        if self.vector_id is not None:
            result['VectorId'] = self.vector_id
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        if self.vector_type is not None:
            result['VectorType'] = self.vector_type
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PicUrl') is not None:
            self.pic_url = m.get('PicUrl')
        if m.get('EventTime') is not None:
            self.event_time = m.get('EventTime')
        if m.get('GatewayIotId') is not None:
            self.gateway_iot_id = m.get('GatewayIotId')
        if m.get('VectorId') is not None:
            self.vector_id = m.get('VectorId')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        if m.get('VectorType') is not None:
            self.vector_type = m.get('VectorType')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        return self


class PictureSearchPictureResponseBodyData(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        page_data: List[PictureSearchPictureResponseBodyDataPageData] = None,
        page_size: int = None,
        total: int = None,
        page_count: int = None,
    ):
        self.current_page = current_page
        self.page_data = page_data
        self.page_size = page_size
        self.total = total
        self.page_count = page_count

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
        result['PageData'] = []
        if self.page_data is not None:
            for k in self.page_data:
                result['PageData'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.page_data = []
        if m.get('PageData') is not None:
            for k in m.get('PageData'):
                temp_model = PictureSearchPictureResponseBodyDataPageData()
                self.page_data.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        return self


class PictureSearchPictureResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: PictureSearchPictureResponseBodyData = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.data = data
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = PictureSearchPictureResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class PictureSearchPictureResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: PictureSearchPictureResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = PictureSearchPictureResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryAIActionRequest(TeaModel):
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


class QueryAIActionResponseBodyData(TeaModel):
    def __init__(
        self,
        algo_config: str = None,
        action: str = None,
        algo: str = None,
        action_id: str = None,
        action_template_id: str = None,
        action_index: int = None,
        action_config: str = None,
        plan_id: str = None,
    ):
        self.algo_config = algo_config
        self.action = action
        self.algo = algo
        self.action_id = action_id
        self.action_template_id = action_template_id
        self.action_index = action_index
        self.action_config = action_config
        self.plan_id = plan_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algo_config is not None:
            result['AlgoConfig'] = self.algo_config
        if self.action is not None:
            result['Action'] = self.action
        if self.algo is not None:
            result['Algo'] = self.algo
        if self.action_id is not None:
            result['ActionId'] = self.action_id
        if self.action_template_id is not None:
            result['ActionTemplateId'] = self.action_template_id
        if self.action_index is not None:
            result['ActionIndex'] = self.action_index
        if self.action_config is not None:
            result['ActionConfig'] = self.action_config
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlgoConfig') is not None:
            self.algo_config = m.get('AlgoConfig')
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('Algo') is not None:
            self.algo = m.get('Algo')
        if m.get('ActionId') is not None:
            self.action_id = m.get('ActionId')
        if m.get('ActionTemplateId') is not None:
            self.action_template_id = m.get('ActionTemplateId')
        if m.get('ActionIndex') is not None:
            self.action_index = m.get('ActionIndex')
        if m.get('ActionConfig') is not None:
            self.action_config = m.get('ActionConfig')
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        return self


class QueryAIActionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: List[QueryAIActionResponseBodyData] = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.data = data
        self.error_message = error_message
        self.code = code
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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = QueryAIActionResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryAIActionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryAIActionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryAIActionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryAIAppRequest(TeaModel):
    def __init__(
        self,
        page_size: int = None,
        current_page: int = None,
    ):
        self.page_size = page_size
        self.current_page = current_page

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        return self


class QueryAIAppResponseBodyDataList(TeaModel):
    def __init__(
        self,
        description: str = None,
        version: str = None,
        app_id: str = None,
        app_template_id: str = None,
        name: str = None,
        level: int = None,
    ):
        self.description = description
        self.version = version
        self.app_id = app_id
        self.app_template_id = app_template_id
        self.name = name
        self.level = level

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.version is not None:
            result['Version'] = self.version
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_template_id is not None:
            result['AppTemplateId'] = self.app_template_id
        if self.name is not None:
            result['Name'] = self.name
        if self.level is not None:
            result['Level'] = self.level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppTemplateId') is not None:
            self.app_template_id = m.get('AppTemplateId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        return self


class QueryAIAppResponseBodyData(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        list: List[QueryAIAppResponseBodyDataList] = None,
        page_size: int = None,
        total: int = None,
        page_count: int = None,
    ):
        self.current_page = current_page
        self.list = list
        self.page_size = page_size
        self.total = total
        self.page_count = page_count

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
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = QueryAIAppResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        return self


class QueryAIAppResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: QueryAIAppResponseBodyData = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.data = data
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = QueryAIAppResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryAIAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryAIAppResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryAIAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryAIJobsRequest(TeaModel):
    def __init__(
        self,
        action_id: str = None,
        iot_id: str = None,
        page_size: int = None,
        current_page: int = None,
    ):
        self.action_id = action_id
        self.iot_id = iot_id
        self.page_size = page_size
        self.current_page = current_page

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_id is not None:
            result['ActionId'] = self.action_id
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionId') is not None:
            self.action_id = m.get('ActionId')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        return self


class QueryAIJobsResponseBodyDataList(TeaModel):
    def __init__(
        self,
        status: int = None,
        job_id: str = None,
        action_id: str = None,
        iot_id: str = None,
    ):
        self.status = status
        self.job_id = job_id
        self.action_id = action_id
        self.iot_id = iot_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.action_id is not None:
            result['ActionId'] = self.action_id
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('ActionId') is not None:
            self.action_id = m.get('ActionId')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        return self


class QueryAIJobsResponseBodyData(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        list: List[QueryAIJobsResponseBodyDataList] = None,
        page_size: int = None,
        total: int = None,
        page_count: int = None,
    ):
        self.current_page = current_page
        self.list = list
        self.page_size = page_size
        self.total = total
        self.page_count = page_count

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
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = QueryAIJobsResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        return self


class QueryAIJobsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: QueryAIJobsResponseBodyData = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.data = data
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = QueryAIJobsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryAIJobsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryAIJobsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryAIJobsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryAIPlanRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        page_size: int = None,
        current_page: int = None,
    ):
        self.app_id = app_id
        self.page_size = page_size
        self.current_page = current_page

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        return self


class QueryAIPlanResponseBodyDataList(TeaModel):
    def __init__(
        self,
        plan_template_id: str = None,
        trigger_enum: int = None,
        description: str = None,
        pre_timing: int = None,
        app_id: str = None,
        interval_timing: int = None,
        plan_id: str = None,
    ):
        self.plan_template_id = plan_template_id
        self.trigger_enum = trigger_enum
        self.description = description
        self.pre_timing = pre_timing
        self.app_id = app_id
        self.interval_timing = interval_timing
        self.plan_id = plan_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.plan_template_id is not None:
            result['PlanTemplateId'] = self.plan_template_id
        if self.trigger_enum is not None:
            result['TriggerEnum'] = self.trigger_enum
        if self.description is not None:
            result['Description'] = self.description
        if self.pre_timing is not None:
            result['PreTiming'] = self.pre_timing
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.interval_timing is not None:
            result['IntervalTiming'] = self.interval_timing
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PlanTemplateId') is not None:
            self.plan_template_id = m.get('PlanTemplateId')
        if m.get('TriggerEnum') is not None:
            self.trigger_enum = m.get('TriggerEnum')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('PreTiming') is not None:
            self.pre_timing = m.get('PreTiming')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('IntervalTiming') is not None:
            self.interval_timing = m.get('IntervalTiming')
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        return self


class QueryAIPlanResponseBodyData(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        list: List[QueryAIPlanResponseBodyDataList] = None,
        page_size: int = None,
        total: int = None,
        page_count: int = None,
    ):
        self.current_page = current_page
        self.list = list
        self.page_size = page_size
        self.total = total
        self.page_count = page_count

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
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = QueryAIPlanResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        return self


class QueryAIPlanResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: QueryAIPlanResponseBodyData = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.data = data
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = QueryAIPlanResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryAIPlanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryAIPlanResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryAIPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryAIPlanTemplatesRequest(TeaModel):
    def __init__(
        self,
        app_template_id: str = None,
        app_version: str = None,
    ):
        self.app_template_id = app_template_id
        self.app_version = app_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_template_id is not None:
            result['AppTemplateId'] = self.app_template_id
        if self.app_version is not None:
            result['AppVersion'] = self.app_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppTemplateId') is not None:
            self.app_template_id = m.get('AppTemplateId')
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')
        return self


class QueryAIPlanTemplatesResponseBodyData(TeaModel):
    def __init__(
        self,
        plan_template_id: str = None,
        trigger_enum: int = None,
        description: str = None,
        interval_timing: int = None,
        app_version: str = None,
        app_template_id: str = None,
    ):
        self.plan_template_id = plan_template_id
        self.trigger_enum = trigger_enum
        self.description = description
        self.interval_timing = interval_timing
        self.app_version = app_version
        self.app_template_id = app_template_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.plan_template_id is not None:
            result['PlanTemplateId'] = self.plan_template_id
        if self.trigger_enum is not None:
            result['TriggerEnum'] = self.trigger_enum
        if self.description is not None:
            result['Description'] = self.description
        if self.interval_timing is not None:
            result['IntervalTiming'] = self.interval_timing
        if self.app_version is not None:
            result['AppVersion'] = self.app_version
        if self.app_template_id is not None:
            result['AppTemplateId'] = self.app_template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PlanTemplateId') is not None:
            self.plan_template_id = m.get('PlanTemplateId')
        if m.get('TriggerEnum') is not None:
            self.trigger_enum = m.get('TriggerEnum')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('IntervalTiming') is not None:
            self.interval_timing = m.get('IntervalTiming')
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')
        if m.get('AppTemplateId') is not None:
            self.app_template_id = m.get('AppTemplateId')
        return self


class QueryAIPlanTemplatesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: List[QueryAIPlanTemplatesResponseBodyData] = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.data = data
        self.error_message = error_message
        self.code = code
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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = QueryAIPlanTemplatesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryAIPlanTemplatesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryAIPlanTemplatesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryAIPlanTemplatesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryDeviceEventRequest(TeaModel):
    def __init__(
        self,
        iot_id: str = None,
        event_type: int = None,
        begin_time: int = None,
        end_time: int = None,
        current_page: int = None,
        page_size: int = None,
        iot_instance_id: str = None,
    ):
        self.iot_id = iot_id
        self.event_type = event_type
        self.begin_time = begin_time
        self.end_time = end_time
        self.current_page = current_page
        self.page_size = page_size
        self.iot_instance_id = iot_instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.event_type is not None:
            result['EventType'] = self.event_type
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        return self


class QueryDeviceEventResponseBodyDataList(TeaModel):
    def __init__(
        self,
        event_id: str = None,
        event_time: str = None,
        event_type: int = None,
        event_pic_id: str = None,
        event_desc: str = None,
        event_data: str = None,
    ):
        self.event_id = event_id
        self.event_time = event_time
        self.event_type = event_type
        self.event_pic_id = event_pic_id
        self.event_desc = event_desc
        self.event_data = event_data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_id is not None:
            result['EventId'] = self.event_id
        if self.event_time is not None:
            result['EventTime'] = self.event_time
        if self.event_type is not None:
            result['EventType'] = self.event_type
        if self.event_pic_id is not None:
            result['EventPicId'] = self.event_pic_id
        if self.event_desc is not None:
            result['EventDesc'] = self.event_desc
        if self.event_data is not None:
            result['EventData'] = self.event_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        if m.get('EventTime') is not None:
            self.event_time = m.get('EventTime')
        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')
        if m.get('EventPicId') is not None:
            self.event_pic_id = m.get('EventPicId')
        if m.get('EventDesc') is not None:
            self.event_desc = m.get('EventDesc')
        if m.get('EventData') is not None:
            self.event_data = m.get('EventData')
        return self


class QueryDeviceEventResponseBodyData(TeaModel):
    def __init__(
        self,
        list: List[QueryDeviceEventResponseBodyDataList] = None,
        page_size: int = None,
        page_count: int = None,
        total: int = None,
        page: int = None,
    ):
        self.list = list
        self.page_size = page_size
        self.page_count = page_count
        self.total = total
        self.page = page

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
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        if self.total is not None:
            result['Total'] = self.total
        if self.page is not None:
            result['Page'] = self.page
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = QueryDeviceEventResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        return self


class QueryDeviceEventResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: QueryDeviceEventResponseBodyData = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.data = data
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = QueryDeviceEventResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryDeviceEventResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryDeviceEventResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryDeviceEventResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryDeviceEventPictureRequest(TeaModel):
    def __init__(
        self,
        iot_id: str = None,
        event_id: str = None,
        iot_instance_id: str = None,
    ):
        self.iot_id = iot_id
        self.event_id = event_id
        self.iot_instance_id = iot_instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.event_id is not None:
            result['EventId'] = self.event_id
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        return self


class QueryDeviceEventPictureResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: str = None,
        error_message: str = None,
        code: int = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.data = data
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryDeviceEventPictureResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryDeviceEventPictureResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryDeviceEventPictureResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryDeviceEventRecordRequest(TeaModel):
    def __init__(
        self,
        iot_id: str = None,
        event_id: str = None,
        iot_instance_id: str = None,
    ):
        self.iot_id = iot_id
        self.event_id = event_id
        self.iot_instance_id = iot_instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.event_id is not None:
            result['EventId'] = self.event_id
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        return self


class QueryDeviceEventRecordResponseBodyData(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        begin_time: str = None,
        file_name: str = None,
        vod_url: str = None,
    ):
        self.end_time = end_time
        self.begin_time = begin_time
        self.file_name = file_name
        self.vod_url = vod_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.vod_url is not None:
            result['VodUrl'] = self.vod_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('VodUrl') is not None:
            self.vod_url = m.get('VodUrl')
        return self


class QueryDeviceEventRecordResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: List[QueryDeviceEventRecordResponseBodyData] = None,
        error_message: str = None,
        code: int = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.data = data
        self.error_message = error_message
        self.code = code
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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = QueryDeviceEventRecordResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryDeviceEventRecordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryDeviceEventRecordResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryDeviceEventRecordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryDeviceFileVodRequest(TeaModel):
    def __init__(
        self,
        iot_id: str = None,
        file_name: str = None,
        should_encrypt: bool = None,
        encrypt_type: int = None,
    ):
        self.iot_id = iot_id
        self.file_name = file_name
        self.should_encrypt = should_encrypt
        self.encrypt_type = encrypt_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.should_encrypt is not None:
            result['ShouldEncrypt'] = self.should_encrypt
        if self.encrypt_type is not None:
            result['EncryptType'] = self.encrypt_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('ShouldEncrypt') is not None:
            self.should_encrypt = m.get('ShouldEncrypt')
        if m.get('EncryptType') is not None:
            self.encrypt_type = m.get('EncryptType')
        return self


class QueryDeviceFileVodResponseBodyData(TeaModel):
    def __init__(
        self,
        vod_url: str = None,
    ):
        self.vod_url = vod_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.vod_url is not None:
            result['VodUrl'] = self.vod_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VodUrl') is not None:
            self.vod_url = m.get('VodUrl')
        return self


class QueryDeviceFileVodResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        decrypt_key: str = None,
        data: QueryDeviceFileVodResponseBodyData = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.decrypt_key = decrypt_key
        self.data = data
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.decrypt_key is not None:
            result['DecryptKey'] = self.decrypt_key
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DecryptKey') is not None:
            self.decrypt_key = m.get('DecryptKey')
        if m.get('Data') is not None:
            temp_model = QueryDeviceFileVodResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryDeviceFileVodResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryDeviceFileVodResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryDeviceFileVodResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryDevicePictureFileRequest(TeaModel):
    def __init__(
        self,
        iot_id: str = None,
        capture_id: str = None,
        picture_type: int = None,
        iot_instance_id: str = None,
    ):
        self.iot_id = iot_id
        self.capture_id = capture_id
        self.picture_type = picture_type
        self.iot_instance_id = iot_instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.capture_id is not None:
            result['CaptureId'] = self.capture_id
        if self.picture_type is not None:
            result['PictureType'] = self.picture_type
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('CaptureId') is not None:
            self.capture_id = m.get('CaptureId')
        if m.get('PictureType') is not None:
            self.picture_type = m.get('PictureType')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        return self


class QueryDevicePictureFileResponseBodyData(TeaModel):
    def __init__(
        self,
        pic_url: str = None,
        pic_create_time: int = None,
        pic_id: str = None,
        thumb_url: str = None,
        iot_id: str = None,
    ):
        self.pic_url = pic_url
        self.pic_create_time = pic_create_time
        self.pic_id = pic_id
        self.thumb_url = thumb_url
        self.iot_id = iot_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pic_url is not None:
            result['PicUrl'] = self.pic_url
        if self.pic_create_time is not None:
            result['PicCreateTime'] = self.pic_create_time
        if self.pic_id is not None:
            result['PicId'] = self.pic_id
        if self.thumb_url is not None:
            result['ThumbUrl'] = self.thumb_url
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PicUrl') is not None:
            self.pic_url = m.get('PicUrl')
        if m.get('PicCreateTime') is not None:
            self.pic_create_time = m.get('PicCreateTime')
        if m.get('PicId') is not None:
            self.pic_id = m.get('PicId')
        if m.get('ThumbUrl') is not None:
            self.thumb_url = m.get('ThumbUrl')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        return self


class QueryDevicePictureFileResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: QueryDevicePictureFileResponseBodyData = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.data = data
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = QueryDevicePictureFileResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryDevicePictureFileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryDevicePictureFileResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
        request_id: str = None,
        data: QueryDevicePictureLifeCycleResponseBodyData = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.data = data
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = QueryDevicePictureLifeCycleResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryDevicePictureLifeCycleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryDevicePictureLifeCycleResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryDevicePictureLifeCycleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryDevicePurifyJobsRequest(TeaModel):
    def __init__(
        self,
        iot_id: str = None,
        page_size: int = None,
        current_page: int = None,
    ):
        self.iot_id = iot_id
        self.page_size = page_size
        self.current_page = current_page

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        return self


class QueryDevicePurifyJobsResponseBodyDataList(TeaModel):
    def __init__(
        self,
        status: int = None,
        device_name: str = None,
        user_id: str = None,
        plan_id: str = None,
        end_time: int = None,
        start_time: int = None,
        purify_record_index_url: str = None,
        product_key: str = None,
        purify_record_name_url: str = None,
        job_id: str = None,
        iot_id: str = None,
        tenant_id: str = None,
    ):
        self.status = status
        self.device_name = device_name
        self.user_id = user_id
        self.plan_id = plan_id
        self.end_time = end_time
        self.start_time = start_time
        self.purify_record_index_url = purify_record_index_url
        self.product_key = product_key
        self.purify_record_name_url = purify_record_name_url
        self.job_id = job_id
        self.iot_id = iot_id
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.purify_record_index_url is not None:
            result['PurifyRecordIndexUrl'] = self.purify_record_index_url
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        if self.purify_record_name_url is not None:
            result['PurifyRecordNameUrl'] = self.purify_record_name_url
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('PurifyRecordIndexUrl') is not None:
            self.purify_record_index_url = m.get('PurifyRecordIndexUrl')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        if m.get('PurifyRecordNameUrl') is not None:
            self.purify_record_name_url = m.get('PurifyRecordNameUrl')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class QueryDevicePurifyJobsResponseBodyData(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        list: List[QueryDevicePurifyJobsResponseBodyDataList] = None,
        page_size: int = None,
        total: int = None,
        page_count: int = None,
    ):
        self.current_page = current_page
        self.list = list
        self.page_size = page_size
        self.total = total
        self.page_count = page_count

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
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = QueryDevicePurifyJobsResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        return self


class QueryDevicePurifyJobsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: QueryDevicePurifyJobsResponseBodyData = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.data = data
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = QueryDevicePurifyJobsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryDevicePurifyJobsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryDevicePurifyJobsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryDevicePurifyJobsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryDevicePurifyPlanByPlanIdRequest(TeaModel):
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


class QueryDevicePurifyPlanByPlanIdResponseBodyData(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        start_time: int = None,
        product_key: str = None,
        device_name: str = None,
        user_id: str = None,
        plan_id: str = None,
        tenant_id: str = None,
        iot_id: str = None,
    ):
        self.end_time = end_time
        self.start_time = start_time
        self.product_key = product_key
        self.device_name = device_name
        self.user_id = user_id
        self.plan_id = plan_id
        self.tenant_id = tenant_id
        self.iot_id = iot_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        return self


class QueryDevicePurifyPlanByPlanIdResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: QueryDevicePurifyPlanByPlanIdResponseBodyData = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.data = data
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = QueryDevicePurifyPlanByPlanIdResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryDevicePurifyPlanByPlanIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryDevicePurifyPlanByPlanIdResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryDevicePurifyPlanByPlanIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryDevicePurifyPlansRequest(TeaModel):
    def __init__(
        self,
        iot_id: str = None,
        page_size: int = None,
        current_page: int = None,
    ):
        self.iot_id = iot_id
        self.page_size = page_size
        self.current_page = current_page

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        return self


class QueryDevicePurifyPlansResponseBodyDataList(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        start_time: int = None,
        product_key: str = None,
        device_name: str = None,
        user_id: str = None,
        plan_id: str = None,
        tenant_id: str = None,
        iot_id: str = None,
    ):
        self.end_time = end_time
        self.start_time = start_time
        self.product_key = product_key
        self.device_name = device_name
        self.user_id = user_id
        self.plan_id = plan_id
        self.tenant_id = tenant_id
        self.iot_id = iot_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        return self


class QueryDevicePurifyPlansResponseBodyData(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        list: List[QueryDevicePurifyPlansResponseBodyDataList] = None,
        page_size: int = None,
        total: int = None,
        page_count: int = None,
    ):
        self.current_page = current_page
        self.list = list
        self.page_size = page_size
        self.total = total
        self.page_count = page_count

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
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = QueryDevicePurifyPlansResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        return self


class QueryDevicePurifyPlansResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: QueryDevicePurifyPlansResponseBodyData = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.data = data
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = QueryDevicePurifyPlansResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryDevicePurifyPlansResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryDevicePurifyPlansResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryDevicePurifyPlansResponseBody()
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
        request_id: str = None,
        data: List[QueryDeviceRecordLifeCycleResponseBodyData] = None,
        error_message: str = None,
        code: int = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.data = data
        self.error_message = error_message
        self.code = code
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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = QueryDeviceRecordLifeCycleResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryDeviceRecordLifeCycleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryDeviceRecordLifeCycleResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryDeviceRecordLifeCycleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryDeviceVodUrlRequest(TeaModel):
    def __init__(
        self,
        file_name: str = None,
        scheme: str = None,
        seek_time: int = None,
        iot_instance_id: str = None,
        iot_id: str = None,
        play_un_limited: bool = None,
        encrypt_type: int = None,
        should_encrypt: bool = None,
    ):
        self.file_name = file_name
        self.scheme = scheme
        self.seek_time = seek_time
        self.iot_instance_id = iot_instance_id
        self.iot_id = iot_id
        self.play_un_limited = play_un_limited
        self.encrypt_type = encrypt_type
        self.should_encrypt = should_encrypt

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.scheme is not None:
            result['Scheme'] = self.scheme
        if self.seek_time is not None:
            result['SeekTime'] = self.seek_time
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.play_un_limited is not None:
            result['PlayUnLimited'] = self.play_un_limited
        if self.encrypt_type is not None:
            result['EncryptType'] = self.encrypt_type
        if self.should_encrypt is not None:
            result['ShouldEncrypt'] = self.should_encrypt
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('Scheme') is not None:
            self.scheme = m.get('Scheme')
        if m.get('SeekTime') is not None:
            self.seek_time = m.get('SeekTime')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('PlayUnLimited') is not None:
            self.play_un_limited = m.get('PlayUnLimited')
        if m.get('EncryptType') is not None:
            self.encrypt_type = m.get('EncryptType')
        if m.get('ShouldEncrypt') is not None:
            self.should_encrypt = m.get('ShouldEncrypt')
        return self


class QueryDeviceVodUrlResponseBodyData(TeaModel):
    def __init__(
        self,
        vod_url: str = None,
    ):
        self.vod_url = vod_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.vod_url is not None:
            result['VodUrl'] = self.vod_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VodUrl') is not None:
            self.vod_url = m.get('VodUrl')
        return self


class QueryDeviceVodUrlResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        decrypt_key: str = None,
        data: QueryDeviceVodUrlResponseBodyData = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.decrypt_key = decrypt_key
        self.data = data
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.decrypt_key is not None:
            result['DecryptKey'] = self.decrypt_key
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DecryptKey') is not None:
            self.decrypt_key = m.get('DecryptKey')
        if m.get('Data') is not None:
            temp_model = QueryDeviceVodUrlResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryDeviceVodUrlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryDeviceVodUrlResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryDeviceVodUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryDeviceVodUrlByTimeRequest(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        scheme: str = None,
        seek_time: int = None,
        iot_instance_id: str = None,
        begin_time: int = None,
        iot_id: str = None,
        play_un_limited: bool = None,
        encrypt_type: int = None,
        should_encrypt: bool = None,
    ):
        self.end_time = end_time
        self.scheme = scheme
        self.seek_time = seek_time
        self.iot_instance_id = iot_instance_id
        self.begin_time = begin_time
        self.iot_id = iot_id
        self.play_un_limited = play_un_limited
        self.encrypt_type = encrypt_type
        self.should_encrypt = should_encrypt

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.scheme is not None:
            result['Scheme'] = self.scheme
        if self.seek_time is not None:
            result['SeekTime'] = self.seek_time
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.play_un_limited is not None:
            result['PlayUnLimited'] = self.play_un_limited
        if self.encrypt_type is not None:
            result['EncryptType'] = self.encrypt_type
        if self.should_encrypt is not None:
            result['ShouldEncrypt'] = self.should_encrypt
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Scheme') is not None:
            self.scheme = m.get('Scheme')
        if m.get('SeekTime') is not None:
            self.seek_time = m.get('SeekTime')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('PlayUnLimited') is not None:
            self.play_un_limited = m.get('PlayUnLimited')
        if m.get('EncryptType') is not None:
            self.encrypt_type = m.get('EncryptType')
        if m.get('ShouldEncrypt') is not None:
            self.should_encrypt = m.get('ShouldEncrypt')
        return self


class QueryDeviceVodUrlByTimeResponseBodyData(TeaModel):
    def __init__(
        self,
        vod_url: str = None,
    ):
        self.vod_url = vod_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.vod_url is not None:
            result['VodUrl'] = self.vod_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VodUrl') is not None:
            self.vod_url = m.get('VodUrl')
        return self


class QueryDeviceVodUrlByTimeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        decrypt_key: str = None,
        data: QueryDeviceVodUrlByTimeResponseBodyData = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.decrypt_key = decrypt_key
        self.data = data
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.decrypt_key is not None:
            result['DecryptKey'] = self.decrypt_key
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DecryptKey') is not None:
            self.decrypt_key = m.get('DecryptKey')
        if m.get('Data') is not None:
            temp_model = QueryDeviceVodUrlByTimeResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryDeviceVodUrlByTimeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryDeviceVodUrlByTimeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
        day_of_week: int = None,
        begin: int = None,
        end: int = None,
    ):
        self.day_of_week = day_of_week
        self.begin = begin
        self.end = end

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.day_of_week is not None:
            result['DayOfWeek'] = self.day_of_week
        if self.begin is not None:
            result['Begin'] = self.begin
        if self.end is not None:
            result['End'] = self.end
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DayOfWeek') is not None:
            self.day_of_week = m.get('DayOfWeek')
        if m.get('Begin') is not None:
            self.begin = m.get('Begin')
        if m.get('End') is not None:
            self.end = m.get('End')
        return self


class QueryEventRecordPlanDetailResponseBodyDataTemplateInfo(TeaModel):
    def __init__(
        self,
        time_section_list: List[QueryEventRecordPlanDetailResponseBodyDataTemplateInfoTimeSectionList] = None,
        all_day: int = None,
        default: int = None,
        name: str = None,
        template_id: str = None,
    ):
        self.time_section_list = time_section_list
        self.all_day = all_day
        self.default = default
        self.name = name
        self.template_id = template_id

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
        result['TimeSectionList'] = []
        if self.time_section_list is not None:
            for k in self.time_section_list:
                result['TimeSectionList'].append(k.to_map() if k else None)
        if self.all_day is not None:
            result['AllDay'] = self.all_day
        if self.default is not None:
            result['Default'] = self.default
        if self.name is not None:
            result['Name'] = self.name
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.time_section_list = []
        if m.get('TimeSectionList') is not None:
            for k in m.get('TimeSectionList'):
                temp_model = QueryEventRecordPlanDetailResponseBodyDataTemplateInfoTimeSectionList()
                self.time_section_list.append(temp_model.from_map(k))
        if m.get('AllDay') is not None:
            self.all_day = m.get('AllDay')
        if m.get('Default') is not None:
            self.default = m.get('Default')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class QueryEventRecordPlanDetailResponseBodyData(TeaModel):
    def __init__(
        self,
        record_duration: int = None,
        pre_record_duration: int = None,
        name: str = None,
        plan_id: str = None,
        template_info: QueryEventRecordPlanDetailResponseBodyDataTemplateInfo = None,
        template_id: str = None,
    ):
        self.record_duration = record_duration
        self.pre_record_duration = pre_record_duration
        self.name = name
        self.plan_id = plan_id
        self.template_info = template_info
        self.template_id = template_id

    def validate(self):
        if self.template_info:
            self.template_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.record_duration is not None:
            result['RecordDuration'] = self.record_duration
        if self.pre_record_duration is not None:
            result['PreRecordDuration'] = self.pre_record_duration
        if self.name is not None:
            result['Name'] = self.name
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        if self.template_info is not None:
            result['TemplateInfo'] = self.template_info.to_map()
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RecordDuration') is not None:
            self.record_duration = m.get('RecordDuration')
        if m.get('PreRecordDuration') is not None:
            self.pre_record_duration = m.get('PreRecordDuration')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        if m.get('TemplateInfo') is not None:
            temp_model = QueryEventRecordPlanDetailResponseBodyDataTemplateInfo()
            self.template_info = temp_model.from_map(m['TemplateInfo'])
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class QueryEventRecordPlanDetailResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: QueryEventRecordPlanDetailResponseBodyData = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.data = data
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = QueryEventRecordPlanDetailResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryEventRecordPlanDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryEventRecordPlanDetailResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryEventRecordPlanDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryEventRecordPlanDeviceByDeviceRequest(TeaModel):
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


class QueryEventRecordPlanDeviceByDeviceResponseBodyDataTemplateInfoTimeSectionList(TeaModel):
    def __init__(
        self,
        day_of_week: int = None,
        begin: int = None,
        end: int = None,
    ):
        self.day_of_week = day_of_week
        self.begin = begin
        self.end = end

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.day_of_week is not None:
            result['DayOfWeek'] = self.day_of_week
        if self.begin is not None:
            result['Begin'] = self.begin
        if self.end is not None:
            result['End'] = self.end
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DayOfWeek') is not None:
            self.day_of_week = m.get('DayOfWeek')
        if m.get('Begin') is not None:
            self.begin = m.get('Begin')
        if m.get('End') is not None:
            self.end = m.get('End')
        return self


class QueryEventRecordPlanDeviceByDeviceResponseBodyDataTemplateInfo(TeaModel):
    def __init__(
        self,
        time_section_list: List[QueryEventRecordPlanDeviceByDeviceResponseBodyDataTemplateInfoTimeSectionList] = None,
        all_day: int = None,
        default: int = None,
        name: str = None,
        template_id: str = None,
    ):
        self.time_section_list = time_section_list
        self.all_day = all_day
        self.default = default
        self.name = name
        self.template_id = template_id

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
        result['TimeSectionList'] = []
        if self.time_section_list is not None:
            for k in self.time_section_list:
                result['TimeSectionList'].append(k.to_map() if k else None)
        if self.all_day is not None:
            result['AllDay'] = self.all_day
        if self.default is not None:
            result['Default'] = self.default
        if self.name is not None:
            result['Name'] = self.name
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.time_section_list = []
        if m.get('TimeSectionList') is not None:
            for k in m.get('TimeSectionList'):
                temp_model = QueryEventRecordPlanDeviceByDeviceResponseBodyDataTemplateInfoTimeSectionList()
                self.time_section_list.append(temp_model.from_map(k))
        if m.get('AllDay') is not None:
            self.all_day = m.get('AllDay')
        if m.get('Default') is not None:
            self.default = m.get('Default')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class QueryEventRecordPlanDeviceByDeviceResponseBodyData(TeaModel):
    def __init__(
        self,
        record_duration: int = None,
        pre_record_duration: int = None,
        name: str = None,
        plan_id: str = None,
        template_info: QueryEventRecordPlanDeviceByDeviceResponseBodyDataTemplateInfo = None,
        template_id: str = None,
    ):
        self.record_duration = record_duration
        self.pre_record_duration = pre_record_duration
        self.name = name
        self.plan_id = plan_id
        self.template_info = template_info
        self.template_id = template_id

    def validate(self):
        if self.template_info:
            self.template_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.record_duration is not None:
            result['RecordDuration'] = self.record_duration
        if self.pre_record_duration is not None:
            result['PreRecordDuration'] = self.pre_record_duration
        if self.name is not None:
            result['Name'] = self.name
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        if self.template_info is not None:
            result['TemplateInfo'] = self.template_info.to_map()
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RecordDuration') is not None:
            self.record_duration = m.get('RecordDuration')
        if m.get('PreRecordDuration') is not None:
            self.pre_record_duration = m.get('PreRecordDuration')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        if m.get('TemplateInfo') is not None:
            temp_model = QueryEventRecordPlanDeviceByDeviceResponseBodyDataTemplateInfo()
            self.template_info = temp_model.from_map(m['TemplateInfo'])
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class QueryEventRecordPlanDeviceByDeviceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: QueryEventRecordPlanDeviceByDeviceResponseBodyData = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.data = data
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = QueryEventRecordPlanDeviceByDeviceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryEventRecordPlanDeviceByDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryEventRecordPlanDeviceByDeviceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryEventRecordPlanDeviceByDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryEventRecordPlanDeviceByPlanRequest(TeaModel):
    def __init__(
        self,
        plan_id: str = None,
        current_page: int = None,
        page_size: int = None,
    ):
        self.plan_id = plan_id
        self.current_page = current_page
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class QueryEventRecordPlanDeviceByPlanResponseBodyDataList(TeaModel):
    def __init__(
        self,
        stream_type: int = None,
        iot_id: str = None,
    ):
        self.stream_type = stream_type
        self.iot_id = iot_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.stream_type is not None:
            result['StreamType'] = self.stream_type
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StreamType') is not None:
            self.stream_type = m.get('StreamType')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        return self


class QueryEventRecordPlanDeviceByPlanResponseBodyData(TeaModel):
    def __init__(
        self,
        list: List[QueryEventRecordPlanDeviceByPlanResponseBodyDataList] = None,
        page_size: int = None,
        total: int = None,
        page_count: int = None,
        page: int = None,
    ):
        self.list = list
        self.page_size = page_size
        self.total = total
        self.page_count = page_count
        self.page = page

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
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        if self.page is not None:
            result['Page'] = self.page
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = QueryEventRecordPlanDeviceByPlanResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        return self


class QueryEventRecordPlanDeviceByPlanResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: QueryEventRecordPlanDeviceByPlanResponseBodyData = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.data = data
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = QueryEventRecordPlanDeviceByPlanResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryEventRecordPlanDeviceByPlanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryEventRecordPlanDeviceByPlanResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
        record_duration: int = None,
        pre_record_duration: int = None,
        plan_id: str = None,
        name: str = None,
        template_id: str = None,
    ):
        self.event_type = event_type
        self.record_duration = record_duration
        self.pre_record_duration = pre_record_duration
        self.plan_id = plan_id
        self.name = name
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
        if self.record_duration is not None:
            result['RecordDuration'] = self.record_duration
        if self.pre_record_duration is not None:
            result['PreRecordDuration'] = self.pre_record_duration
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        if self.name is not None:
            result['Name'] = self.name
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')
        if m.get('RecordDuration') is not None:
            self.record_duration = m.get('RecordDuration')
        if m.get('PreRecordDuration') is not None:
            self.pre_record_duration = m.get('PreRecordDuration')
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class QueryEventRecordPlansResponseBodyData(TeaModel):
    def __init__(
        self,
        list: List[QueryEventRecordPlansResponseBodyDataList] = None,
        page_size: int = None,
        page_count: int = None,
        total: int = None,
        page: int = None,
    ):
        self.list = list
        self.page_size = page_size
        self.page_count = page_count
        self.total = total
        self.page = page

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
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        if self.total is not None:
            result['Total'] = self.total
        if self.page is not None:
            result['Page'] = self.page
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = QueryEventRecordPlansResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        return self


class QueryEventRecordPlansResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: QueryEventRecordPlansResponseBodyData = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.data = data
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = QueryEventRecordPlansResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryEventRecordPlansResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryEventRecordPlansResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryEventRecordPlansResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryFaceAllDeviceGroupRequest(TeaModel):
    def __init__(
        self,
        isolation_id: str = None,
        iot_instance_id: str = None,
        page_size: int = None,
        page_no: int = None,
    ):
        self.isolation_id = isolation_id
        self.iot_instance_id = iot_instance_id
        self.page_size = page_size
        self.page_no = page_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.isolation_id is not None:
            result['IsolationId'] = self.isolation_id
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsolationId') is not None:
            self.isolation_id = m.get('IsolationId')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        return self


class QueryFaceAllDeviceGroupResponseBodyDataDeviceGroupList(TeaModel):
    def __init__(
        self,
        device_group_id: str = None,
        modified_time: str = None,
        device_group_name: str = None,
    ):
        self.device_group_id = device_group_id
        self.modified_time = modified_time
        self.device_group_name = device_group_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_group_id is not None:
            result['DeviceGroupId'] = self.device_group_id
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.device_group_name is not None:
            result['DeviceGroupName'] = self.device_group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceGroupId') is not None:
            self.device_group_id = m.get('DeviceGroupId')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('DeviceGroupName') is not None:
            self.device_group_name = m.get('DeviceGroupName')
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
        request_id: str = None,
        data: QueryFaceAllDeviceGroupResponseBodyData = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.data = data
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = QueryFaceAllDeviceGroupResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryFaceAllDeviceGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryFaceAllDeviceGroupResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryFaceAllDeviceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryFaceAllUserGroupRequest(TeaModel):
    def __init__(
        self,
        isolation_id: str = None,
        page_size: int = None,
        page_no: int = None,
    ):
        self.isolation_id = isolation_id
        self.page_size = page_size
        self.page_no = page_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.isolation_id is not None:
            result['IsolationId'] = self.isolation_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsolationId') is not None:
            self.isolation_id = m.get('IsolationId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
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
        user_group_list: List[QueryFaceAllUserGroupResponseBodyDataUserGroupList] = None,
        page_size: int = None,
        total: int = None,
    ):
        self.page_no = page_no
        self.user_group_list = user_group_list
        self.page_size = page_size
        self.total = total

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
        result['UserGroupList'] = []
        if self.user_group_list is not None:
            for k in self.user_group_list:
                result['UserGroupList'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        self.user_group_list = []
        if m.get('UserGroupList') is not None:
            for k in m.get('UserGroupList'):
                temp_model = QueryFaceAllUserGroupResponseBodyDataUserGroupList()
                self.user_group_list.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class QueryFaceAllUserGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: QueryFaceAllUserGroupResponseBodyData = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.data = data
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = QueryFaceAllUserGroupResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryFaceAllUserGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryFaceAllUserGroupResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryFaceAllUserGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryFaceAllUserGroupAndDeviceGroupRelationRequest(TeaModel):
    def __init__(
        self,
        isolation_id: str = None,
        page_size: int = None,
        page_no: int = None,
    ):
        self.isolation_id = isolation_id
        self.page_size = page_size
        self.page_no = page_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.isolation_id is not None:
            result['IsolationId'] = self.isolation_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsolationId') is not None:
            self.isolation_id = m.get('IsolationId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        return self


class QueryFaceAllUserGroupAndDeviceGroupRelationResponseBodyDataList(TeaModel):
    def __init__(
        self,
        device_group_id: str = None,
        modified_time: str = None,
        control_type: str = None,
        user_group_id: str = None,
        control_id: str = None,
    ):
        self.device_group_id = device_group_id
        self.modified_time = modified_time
        self.control_type = control_type
        self.user_group_id = user_group_id
        self.control_id = control_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_group_id is not None:
            result['DeviceGroupId'] = self.device_group_id
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.control_type is not None:
            result['ControlType'] = self.control_type
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        if self.control_id is not None:
            result['ControlId'] = self.control_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceGroupId') is not None:
            self.device_group_id = m.get('DeviceGroupId')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('ControlType') is not None:
            self.control_type = m.get('ControlType')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        if m.get('ControlId') is not None:
            self.control_id = m.get('ControlId')
        return self


class QueryFaceAllUserGroupAndDeviceGroupRelationResponseBodyData(TeaModel):
    def __init__(
        self,
        list: List[QueryFaceAllUserGroupAndDeviceGroupRelationResponseBodyDataList] = None,
        page_size: int = None,
        total: int = None,
        page: int = None,
    ):
        self.list = list
        self.page_size = page_size
        self.total = total
        self.page = page

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
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        if self.page is not None:
            result['Page'] = self.page
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = QueryFaceAllUserGroupAndDeviceGroupRelationResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        return self


class QueryFaceAllUserGroupAndDeviceGroupRelationResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: QueryFaceAllUserGroupAndDeviceGroupRelationResponseBodyData = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.data = data
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = QueryFaceAllUserGroupAndDeviceGroupRelationResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryFaceAllUserGroupAndDeviceGroupRelationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryFaceAllUserGroupAndDeviceGroupRelationResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryFaceAllUserGroupAndDeviceGroupRelationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryFaceAllUserIdsByGroupIdRequest(TeaModel):
    def __init__(
        self,
        isolation_id: str = None,
        user_group_id: str = None,
        page_size: int = None,
        page_no: int = None,
    ):
        self.isolation_id = isolation_id
        self.user_group_id = user_group_id
        self.page_size = page_size
        self.page_no = page_no

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
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsolationId') is not None:
            self.isolation_id = m.get('IsolationId')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        return self


class QueryFaceAllUserIdsByGroupIdResponseBodyDataList(TeaModel):
    def __init__(
        self,
        params: str = None,
        custom_user_id: str = None,
        user_id: str = None,
        name: str = None,
    ):
        self.params = params
        self.custom_user_id = custom_user_id
        self.user_id = user_id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.params is not None:
            result['Params'] = self.params
        if self.custom_user_id is not None:
            result['CustomUserId'] = self.custom_user_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Params') is not None:
            self.params = m.get('Params')
        if m.get('CustomUserId') is not None:
            self.custom_user_id = m.get('CustomUserId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class QueryFaceAllUserIdsByGroupIdResponseBodyData(TeaModel):
    def __init__(
        self,
        list: List[QueryFaceAllUserIdsByGroupIdResponseBodyDataList] = None,
        page_size: int = None,
        total: int = None,
        page: int = None,
    ):
        self.list = list
        self.page_size = page_size
        self.total = total
        self.page = page

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
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        if self.page is not None:
            result['Page'] = self.page
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = QueryFaceAllUserIdsByGroupIdResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        return self


class QueryFaceAllUserIdsByGroupIdResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: QueryFaceAllUserIdsByGroupIdResponseBodyData = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.data = data
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = QueryFaceAllUserIdsByGroupIdResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryFaceAllUserIdsByGroupIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryFaceAllUserIdsByGroupIdResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
        request_id: str = None,
        data: str = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.data = data
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryFaceCustomUserIdByUserIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryFaceCustomUserIdByUserIdResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryFaceCustomUserIdByUserIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryFaceDeviceGroupsByDeviceRequest(TeaModel):
    def __init__(
        self,
        isolation_id: str = None,
        iot_instance_id: str = None,
        product_key: str = None,
        device_name: str = None,
        page_size: int = None,
        page_no: int = None,
    ):
        self.isolation_id = isolation_id
        self.iot_instance_id = iot_instance_id
        self.product_key = product_key
        self.device_name = device_name
        self.page_size = page_size
        self.page_no = page_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.isolation_id is not None:
            result['IsolationId'] = self.isolation_id
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsolationId') is not None:
            self.isolation_id = m.get('IsolationId')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        return self


class QueryFaceDeviceGroupsByDeviceResponseBodyDataDeviceGroupList(TeaModel):
    def __init__(
        self,
        device_group_id: str = None,
        modified_time: str = None,
        device_group_name: str = None,
    ):
        self.device_group_id = device_group_id
        self.modified_time = modified_time
        self.device_group_name = device_group_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_group_id is not None:
            result['DeviceGroupId'] = self.device_group_id
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.device_group_name is not None:
            result['DeviceGroupName'] = self.device_group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceGroupId') is not None:
            self.device_group_id = m.get('DeviceGroupId')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('DeviceGroupName') is not None:
            self.device_group_name = m.get('DeviceGroupName')
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
        request_id: str = None,
        data: QueryFaceDeviceGroupsByDeviceResponseBodyData = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.data = data
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = QueryFaceDeviceGroupsByDeviceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryFaceDeviceGroupsByDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryFaceDeviceGroupsByDeviceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
        algorithm_version: str = None,
        algorithm_provider: str = None,
        error_message: str = None,
        error_code: str = None,
        face_md_5: str = None,
    ):
        self.algorithm_name = algorithm_name
        self.algorithm_version = algorithm_version
        self.algorithm_provider = algorithm_provider
        self.error_message = error_message
        self.error_code = error_code
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
        if self.algorithm_version is not None:
            result['AlgorithmVersion'] = self.algorithm_version
        if self.algorithm_provider is not None:
            result['AlgorithmProvider'] = self.algorithm_provider
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.face_md_5 is not None:
            result['FaceMd5'] = self.face_md_5
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlgorithmName') is not None:
            self.algorithm_name = m.get('AlgorithmName')
        if m.get('AlgorithmVersion') is not None:
            self.algorithm_version = m.get('AlgorithmVersion')
        if m.get('AlgorithmProvider') is not None:
            self.algorithm_provider = m.get('AlgorithmProvider')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('FaceMd5') is not None:
            self.face_md_5 = m.get('FaceMd5')
        return self


class QueryFaceUserResponseBodyDataFacePicList(TeaModel):
    def __init__(
        self,
        face_url: str = None,
        feature_dtolist: List[QueryFaceUserResponseBodyDataFacePicListFeatureDTOList] = None,
        face_md_5: str = None,
    ):
        self.face_url = face_url
        self.feature_dtolist = feature_dtolist
        self.face_md_5 = face_md_5

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
        if self.face_url is not None:
            result['FaceUrl'] = self.face_url
        result['FeatureDTOList'] = []
        if self.feature_dtolist is not None:
            for k in self.feature_dtolist:
                result['FeatureDTOList'].append(k.to_map() if k else None)
        if self.face_md_5 is not None:
            result['FaceMd5'] = self.face_md_5
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FaceUrl') is not None:
            self.face_url = m.get('FaceUrl')
        self.feature_dtolist = []
        if m.get('FeatureDTOList') is not None:
            for k in m.get('FeatureDTOList'):
                temp_model = QueryFaceUserResponseBodyDataFacePicListFeatureDTOList()
                self.feature_dtolist.append(temp_model.from_map(k))
        if m.get('FaceMd5') is not None:
            self.face_md_5 = m.get('FaceMd5')
        return self


class QueryFaceUserResponseBodyData(TeaModel):
    def __init__(
        self,
        params: str = None,
        custom_user_id: str = None,
        user_id: str = None,
        face_pic_list: List[QueryFaceUserResponseBodyDataFacePicList] = None,
        name: str = None,
    ):
        self.params = params
        self.custom_user_id = custom_user_id
        self.user_id = user_id
        self.face_pic_list = face_pic_list
        self.name = name

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
        if self.params is not None:
            result['Params'] = self.params
        if self.custom_user_id is not None:
            result['CustomUserId'] = self.custom_user_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        result['FacePicList'] = []
        if self.face_pic_list is not None:
            for k in self.face_pic_list:
                result['FacePicList'].append(k.to_map() if k else None)
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Params') is not None:
            self.params = m.get('Params')
        if m.get('CustomUserId') is not None:
            self.custom_user_id = m.get('CustomUserId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        self.face_pic_list = []
        if m.get('FacePicList') is not None:
            for k in m.get('FacePicList'):
                temp_model = QueryFaceUserResponseBodyDataFacePicList()
                self.face_pic_list.append(temp_model.from_map(k))
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class QueryFaceUserResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: QueryFaceUserResponseBodyData = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.data = data
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = QueryFaceUserResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryFaceUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryFaceUserResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryFaceUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryFaceUserGroupRequest(TeaModel):
    def __init__(
        self,
        isolation_id: str = None,
        user_id: str = None,
        page_size: int = None,
        page_no: int = None,
    ):
        self.isolation_id = isolation_id
        self.user_id = user_id
        self.page_size = page_size
        self.page_no = page_no

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
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsolationId') is not None:
            self.isolation_id = m.get('IsolationId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
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
        user_group_list: List[QueryFaceUserGroupResponseBodyDataUserGroupList] = None,
        page_size: int = None,
        total: int = None,
    ):
        self.page_no = page_no
        self.user_group_list = user_group_list
        self.page_size = page_size
        self.total = total

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
        result['UserGroupList'] = []
        if self.user_group_list is not None:
            for k in self.user_group_list:
                result['UserGroupList'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        self.user_group_list = []
        if m.get('UserGroupList') is not None:
            for k in m.get('UserGroupList'):
                temp_model = QueryFaceUserGroupResponseBodyDataUserGroupList()
                self.user_group_list.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class QueryFaceUserGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: QueryFaceUserGroupResponseBodyData = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.data = data
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = QueryFaceUserGroupResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryFaceUserGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryFaceUserGroupResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryFaceUserGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryFaceUserGroupAndDeviceGroupRelationRequest(TeaModel):
    def __init__(
        self,
        isolation_id: str = None,
        control_id: str = None,
    ):
        self.isolation_id = isolation_id
        self.control_id = control_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.isolation_id is not None:
            result['IsolationId'] = self.isolation_id
        if self.control_id is not None:
            result['ControlId'] = self.control_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsolationId') is not None:
            self.isolation_id = m.get('IsolationId')
        if m.get('ControlId') is not None:
            self.control_id = m.get('ControlId')
        return self


class QueryFaceUserGroupAndDeviceGroupRelationResponseBodyData(TeaModel):
    def __init__(
        self,
        device_group_id: str = None,
        modified_time: str = None,
        control_type: str = None,
        user_group_id: str = None,
        control_id: str = None,
    ):
        self.device_group_id = device_group_id
        self.modified_time = modified_time
        self.control_type = control_type
        self.user_group_id = user_group_id
        self.control_id = control_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_group_id is not None:
            result['DeviceGroupId'] = self.device_group_id
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.control_type is not None:
            result['ControlType'] = self.control_type
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        if self.control_id is not None:
            result['ControlId'] = self.control_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceGroupId') is not None:
            self.device_group_id = m.get('DeviceGroupId')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('ControlType') is not None:
            self.control_type = m.get('ControlType')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        if m.get('ControlId') is not None:
            self.control_id = m.get('ControlId')
        return self


class QueryFaceUserGroupAndDeviceGroupRelationResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: QueryFaceUserGroupAndDeviceGroupRelationResponseBodyData = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.data = data
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = QueryFaceUserGroupAndDeviceGroupRelationResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryFaceUserGroupAndDeviceGroupRelationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryFaceUserGroupAndDeviceGroupRelationResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryFaceUserGroupAndDeviceGroupRelationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryFaceUserIdByCustomUserIdRequest(TeaModel):
    def __init__(
        self,
        isolation_id: str = None,
        custom_user_id: str = None,
    ):
        self.isolation_id = isolation_id
        self.custom_user_id = custom_user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.isolation_id is not None:
            result['IsolationId'] = self.isolation_id
        if self.custom_user_id is not None:
            result['CustomUserId'] = self.custom_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsolationId') is not None:
            self.isolation_id = m.get('IsolationId')
        if m.get('CustomUserId') is not None:
            self.custom_user_id = m.get('CustomUserId')
        return self


class QueryFaceUserIdByCustomUserIdResponseBodyData(TeaModel):
    def __init__(
        self,
        params: str = None,
        custom_user_id: str = None,
        user_id: str = None,
        name: str = None,
    ):
        self.params = params
        self.custom_user_id = custom_user_id
        self.user_id = user_id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.params is not None:
            result['Params'] = self.params
        if self.custom_user_id is not None:
            result['CustomUserId'] = self.custom_user_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Params') is not None:
            self.params = m.get('Params')
        if m.get('CustomUserId') is not None:
            self.custom_user_id = m.get('CustomUserId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class QueryFaceUserIdByCustomUserIdResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: QueryFaceUserIdByCustomUserIdResponseBodyData = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.data = data
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = QueryFaceUserIdByCustomUserIdResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryFaceUserIdByCustomUserIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryFaceUserIdByCustomUserIdResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryFaceUserIdByCustomUserIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryIotIdsByAIPlanRequest(TeaModel):
    def __init__(
        self,
        plan_id: str = None,
        page_size: int = None,
        current_page: int = None,
    ):
        self.plan_id = plan_id
        self.page_size = page_size
        self.current_page = current_page

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        return self


class QueryIotIdsByAIPlanResponseBodyData(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        list: List[str] = None,
        page_size: int = None,
        total: int = None,
        page_count: int = None,
    ):
        self.current_page = current_page
        self.list = list
        self.page_size = page_size
        self.total = total
        self.page_count = page_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.list is not None:
            result['List'] = self.list
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('List') is not None:
            self.list = m.get('List')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        return self


class QueryIotIdsByAIPlanResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: QueryIotIdsByAIPlanResponseBodyData = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.data = data
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = QueryIotIdsByAIPlanResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryIotIdsByAIPlanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryIotIdsByAIPlanResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryIotIdsByAIPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryLiveStreamingRequest(TeaModel):
    def __init__(
        self,
        scheme: str = None,
        iot_instance_id: str = None,
        stream_type: int = None,
        cache_duration: int = None,
        iot_id: str = None,
        should_encrypt: bool = None,
        play_un_limited: bool = None,
        encrypt_type: int = None,
        force_iframe: bool = None,
    ):
        self.scheme = scheme
        self.iot_instance_id = iot_instance_id
        self.stream_type = stream_type
        self.cache_duration = cache_duration
        self.iot_id = iot_id
        self.should_encrypt = should_encrypt
        self.play_un_limited = play_un_limited
        self.encrypt_type = encrypt_type
        self.force_iframe = force_iframe

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scheme is not None:
            result['Scheme'] = self.scheme
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.stream_type is not None:
            result['StreamType'] = self.stream_type
        if self.cache_duration is not None:
            result['CacheDuration'] = self.cache_duration
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.should_encrypt is not None:
            result['ShouldEncrypt'] = self.should_encrypt
        if self.play_un_limited is not None:
            result['PlayUnLimited'] = self.play_un_limited
        if self.encrypt_type is not None:
            result['EncryptType'] = self.encrypt_type
        if self.force_iframe is not None:
            result['ForceIFrame'] = self.force_iframe
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Scheme') is not None:
            self.scheme = m.get('Scheme')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('StreamType') is not None:
            self.stream_type = m.get('StreamType')
        if m.get('CacheDuration') is not None:
            self.cache_duration = m.get('CacheDuration')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('ShouldEncrypt') is not None:
            self.should_encrypt = m.get('ShouldEncrypt')
        if m.get('PlayUnLimited') is not None:
            self.play_un_limited = m.get('PlayUnLimited')
        if m.get('EncryptType') is not None:
            self.encrypt_type = m.get('EncryptType')
        if m.get('ForceIFrame') is not None:
            self.force_iframe = m.get('ForceIFrame')
        return self


class QueryLiveStreamingResponseBodyData(TeaModel):
    def __init__(
        self,
        path: str = None,
        decrypt_key: str = None,
    ):
        self.path = path
        self.decrypt_key = decrypt_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.path is not None:
            result['Path'] = self.path
        if self.decrypt_key is not None:
            result['DecryptKey'] = self.decrypt_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('DecryptKey') is not None:
            self.decrypt_key = m.get('DecryptKey')
        return self


class QueryLiveStreamingResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: QueryLiveStreamingResponseBodyData = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.data = data
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = QueryLiveStreamingResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryLiveStreamingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryLiveStreamingResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryLiveStreamingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryMonthRecordRequest(TeaModel):
    def __init__(
        self,
        iot_id: str = None,
        month: str = None,
        iot_instance_id: str = None,
    ):
        self.iot_id = iot_id
        self.month = month
        self.iot_instance_id = iot_instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.month is not None:
            result['Month'] = self.month
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('Month') is not None:
            self.month = m.get('Month')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        return self


class QueryMonthRecordResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: str = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.data = data
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryMonthRecordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryMonthRecordResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryMonthRecordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryPictureFilesRequest(TeaModel):
    def __init__(
        self,
        iot_id: str = None,
        begin_time: int = None,
        end_time: int = None,
        current_page: int = None,
        page_size: int = None,
        picture_type: int = None,
        picture_source: int = None,
        iot_instance_id: str = None,
    ):
        self.iot_id = iot_id
        self.begin_time = begin_time
        self.end_time = end_time
        self.current_page = current_page
        self.page_size = page_size
        self.picture_type = picture_type
        self.picture_source = picture_source
        self.iot_instance_id = iot_instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.picture_type is not None:
            result['PictureType'] = self.picture_type
        if self.picture_source is not None:
            result['PictureSource'] = self.picture_source
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PictureType') is not None:
            self.picture_type = m.get('PictureType')
        if m.get('PictureSource') is not None:
            self.picture_source = m.get('PictureSource')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        return self


class QueryPictureFilesResponseBodyDataList(TeaModel):
    def __init__(
        self,
        pic_url: str = None,
        pic_create_time: int = None,
        pic_id: str = None,
        thumb_url: str = None,
        iot_id: str = None,
    ):
        self.pic_url = pic_url
        self.pic_create_time = pic_create_time
        self.pic_id = pic_id
        self.thumb_url = thumb_url
        self.iot_id = iot_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pic_url is not None:
            result['PicUrl'] = self.pic_url
        if self.pic_create_time is not None:
            result['PicCreateTime'] = self.pic_create_time
        if self.pic_id is not None:
            result['PicId'] = self.pic_id
        if self.thumb_url is not None:
            result['ThumbUrl'] = self.thumb_url
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PicUrl') is not None:
            self.pic_url = m.get('PicUrl')
        if m.get('PicCreateTime') is not None:
            self.pic_create_time = m.get('PicCreateTime')
        if m.get('PicId') is not None:
            self.pic_id = m.get('PicId')
        if m.get('ThumbUrl') is not None:
            self.thumb_url = m.get('ThumbUrl')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        return self


class QueryPictureFilesResponseBodyData(TeaModel):
    def __init__(
        self,
        list: List[QueryPictureFilesResponseBodyDataList] = None,
        page_size: int = None,
        page: int = None,
    ):
        self.list = list
        self.page_size = page_size
        self.page = page

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
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page is not None:
            result['Page'] = self.page
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = QueryPictureFilesResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        return self


class QueryPictureFilesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: QueryPictureFilesResponseBodyData = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.data = data
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = QueryPictureFilesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryPictureFilesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryPictureFilesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryPictureFilesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryPictureSearchAiboxesRequest(TeaModel):
    def __init__(
        self,
        app_instance_id: str = None,
        page_size: int = None,
        current_page: int = None,
        iot_instance_id: str = None,
    ):
        self.app_instance_id = app_instance_id
        self.page_size = page_size
        self.current_page = current_page
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
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceId') is not None:
            self.app_instance_id = m.get('AppInstanceId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        return self


class QueryPictureSearchAiboxesResponseBodyDataPageData(TeaModel):
    def __init__(
        self,
        nick_name: str = None,
        iot_id: str = None,
    ):
        self.nick_name = nick_name
        self.iot_id = iot_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.nick_name is not None:
            result['NickName'] = self.nick_name
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NickName') is not None:
            self.nick_name = m.get('NickName')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        return self


class QueryPictureSearchAiboxesResponseBodyData(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        page_data: List[QueryPictureSearchAiboxesResponseBodyDataPageData] = None,
        page_size: int = None,
        total: int = None,
        page_count: int = None,
    ):
        self.current_page = current_page
        self.page_data = page_data
        self.page_size = page_size
        self.total = total
        self.page_count = page_count

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
        result['PageData'] = []
        if self.page_data is not None:
            for k in self.page_data:
                result['PageData'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.page_data = []
        if m.get('PageData') is not None:
            for k in m.get('PageData'):
                temp_model = QueryPictureSearchAiboxesResponseBodyDataPageData()
                self.page_data.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        return self


class QueryPictureSearchAiboxesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: QueryPictureSearchAiboxesResponseBodyData = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.data = data
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = QueryPictureSearchAiboxesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryPictureSearchAiboxesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryPictureSearchAiboxesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryPictureSearchAiboxesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryPictureSearchAppResponseBodyDataData(TeaModel):
    def __init__(
        self,
        app_instance_id: str = None,
        modified_time: int = None,
        version: str = None,
        create_time: int = None,
        app_template_id: str = None,
        name: str = None,
        level: str = None,
    ):
        self.app_instance_id = app_instance_id
        self.modified_time = modified_time
        self.version = version
        self.create_time = create_time
        self.app_template_id = app_template_id
        self.name = name
        self.level = level

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_id is not None:
            result['AppInstanceId'] = self.app_instance_id
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.version is not None:
            result['Version'] = self.version
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.app_template_id is not None:
            result['AppTemplateId'] = self.app_template_id
        if self.name is not None:
            result['Name'] = self.name
        if self.level is not None:
            result['Level'] = self.level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceId') is not None:
            self.app_instance_id = m.get('AppInstanceId')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('AppTemplateId') is not None:
            self.app_template_id = m.get('AppTemplateId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        return self


class QueryPictureSearchAppResponseBodyData(TeaModel):
    def __init__(
        self,
        data: List[QueryPictureSearchAppResponseBodyDataData] = None,
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
                temp_model = QueryPictureSearchAppResponseBodyDataData()
                self.data.append(temp_model.from_map(k))
        return self


class QueryPictureSearchAppResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: QueryPictureSearchAppResponseBodyData = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.data = data
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = QueryPictureSearchAppResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryPictureSearchAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryPictureSearchAppResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryPictureSearchAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryPictureSearchAppsRequest(TeaModel):
    def __init__(
        self,
        page_size: int = None,
        current_page: int = None,
    ):
        self.page_size = page_size
        self.current_page = current_page

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        return self


class QueryPictureSearchAppsResponseBodyDataPageData(TeaModel):
    def __init__(
        self,
        app_instance_id: str = None,
        modified_time: int = None,
        description: str = None,
        version: str = None,
        create_time: int = None,
        app_template_id: str = None,
        name: str = None,
    ):
        self.app_instance_id = app_instance_id
        self.modified_time = modified_time
        self.description = description
        self.version = version
        self.create_time = create_time
        self.app_template_id = app_template_id
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
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.description is not None:
            result['Description'] = self.description
        if self.version is not None:
            result['Version'] = self.version
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.app_template_id is not None:
            result['AppTemplateId'] = self.app_template_id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceId') is not None:
            self.app_instance_id = m.get('AppInstanceId')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('AppTemplateId') is not None:
            self.app_template_id = m.get('AppTemplateId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class QueryPictureSearchAppsResponseBodyData(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        page_data: List[QueryPictureSearchAppsResponseBodyDataPageData] = None,
        page_size: int = None,
        total: int = None,
        page_count: int = None,
    ):
        self.current_page = current_page
        self.page_data = page_data
        self.page_size = page_size
        self.total = total
        self.page_count = page_count

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
        result['PageData'] = []
        if self.page_data is not None:
            for k in self.page_data:
                result['PageData'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.page_data = []
        if m.get('PageData') is not None:
            for k in m.get('PageData'):
                temp_model = QueryPictureSearchAppsResponseBodyDataPageData()
                self.page_data.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        return self


class QueryPictureSearchAppsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: QueryPictureSearchAppsResponseBodyData = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.data = data
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = QueryPictureSearchAppsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryPictureSearchAppsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryPictureSearchAppsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryPictureSearchAppsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryPictureSearchDevicesRequest(TeaModel):
    def __init__(
        self,
        app_instance_id: str = None,
        page_size: int = None,
        current_page: int = None,
    ):
        self.app_instance_id = app_instance_id
        self.page_size = page_size
        self.current_page = current_page

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_id is not None:
            result['AppInstanceId'] = self.app_instance_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceId') is not None:
            self.app_instance_id = m.get('AppInstanceId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        return self


class QueryPictureSearchDevicesResponseBodyDataPageData(TeaModel):
    def __init__(
        self,
        nick_name: str = None,
        iot_id: str = None,
    ):
        self.nick_name = nick_name
        self.iot_id = iot_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.nick_name is not None:
            result['NickName'] = self.nick_name
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NickName') is not None:
            self.nick_name = m.get('NickName')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        return self


class QueryPictureSearchDevicesResponseBodyData(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        page_data: List[QueryPictureSearchDevicesResponseBodyDataPageData] = None,
        page_size: int = None,
        total: int = None,
        page_count: int = None,
    ):
        self.current_page = current_page
        self.page_data = page_data
        self.page_size = page_size
        self.total = total
        self.page_count = page_count

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
        result['PageData'] = []
        if self.page_data is not None:
            for k in self.page_data:
                result['PageData'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.page_data = []
        if m.get('PageData') is not None:
            for k in m.get('PageData'):
                temp_model = QueryPictureSearchDevicesResponseBodyDataPageData()
                self.page_data.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        return self


class QueryPictureSearchDevicesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: QueryPictureSearchDevicesResponseBodyData = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.data = data
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = QueryPictureSearchDevicesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryPictureSearchDevicesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryPictureSearchDevicesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryPictureSearchDevicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryPictureSearchJobRequest(TeaModel):
    def __init__(
        self,
        app_instance_id: str = None,
        job_status: int = None,
        page_size: int = None,
        current_page: int = None,
    ):
        self.app_instance_id = app_instance_id
        self.job_status = job_status
        self.page_size = page_size
        self.current_page = current_page

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_id is not None:
            result['AppInstanceId'] = self.app_instance_id
        if self.job_status is not None:
            result['JobStatus'] = self.job_status
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceId') is not None:
            self.app_instance_id = m.get('AppInstanceId')
        if m.get('JobStatus') is not None:
            self.job_status = m.get('JobStatus')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        return self


class QueryPictureSearchJobResponseBodyDataPageData(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        start_time: int = None,
        job_status: int = None,
        search_pic_url: str = None,
        create_time: int = None,
        job_id: str = None,
        threshold: float = None,
    ):
        self.end_time = end_time
        self.start_time = start_time
        self.job_status = job_status
        self.search_pic_url = search_pic_url
        self.create_time = create_time
        self.job_id = job_id
        self.threshold = threshold

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.job_status is not None:
            result['JobStatus'] = self.job_status
        if self.search_pic_url is not None:
            result['SearchPicUrl'] = self.search_pic_url
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('JobStatus') is not None:
            self.job_status = m.get('JobStatus')
        if m.get('SearchPicUrl') is not None:
            self.search_pic_url = m.get('SearchPicUrl')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        return self


class QueryPictureSearchJobResponseBodyData(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        page_data: List[QueryPictureSearchJobResponseBodyDataPageData] = None,
        page_size: int = None,
        total: int = None,
        page_count: int = None,
    ):
        self.current_page = current_page
        self.page_data = page_data
        self.page_size = page_size
        self.total = total
        self.page_count = page_count

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
        result['PageData'] = []
        if self.page_data is not None:
            for k in self.page_data:
                result['PageData'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.page_data = []
        if m.get('PageData') is not None:
            for k in m.get('PageData'):
                temp_model = QueryPictureSearchJobResponseBodyDataPageData()
                self.page_data.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        return self


class QueryPictureSearchJobResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: QueryPictureSearchJobResponseBodyData = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.data = data
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = QueryPictureSearchJobResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryPictureSearchJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryPictureSearchJobResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryPictureSearchJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryPictureSearchJobResultRequest(TeaModel):
    def __init__(
        self,
        app_instance_id: str = None,
        job_id: str = None,
        page_size: int = None,
        current_page: int = None,
    ):
        self.app_instance_id = app_instance_id
        self.job_id = job_id
        self.page_size = page_size
        self.current_page = current_page

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
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceId') is not None:
            self.app_instance_id = m.get('AppInstanceId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        return self


class QueryPictureSearchJobResultResponseBodyDataPageData(TeaModel):
    def __init__(
        self,
        pic_url: str = None,
        event_time: int = None,
        gateway_iot_id: str = None,
        vector_id: str = None,
        device_nick_name: str = None,
        threshold: float = None,
        iot_id: str = None,
    ):
        self.pic_url = pic_url
        self.event_time = event_time
        self.gateway_iot_id = gateway_iot_id
        self.vector_id = vector_id
        self.device_nick_name = device_nick_name
        self.threshold = threshold
        self.iot_id = iot_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pic_url is not None:
            result['PicUrl'] = self.pic_url
        if self.event_time is not None:
            result['EventTime'] = self.event_time
        if self.gateway_iot_id is not None:
            result['GatewayIotId'] = self.gateway_iot_id
        if self.vector_id is not None:
            result['VectorId'] = self.vector_id
        if self.device_nick_name is not None:
            result['DeviceNickName'] = self.device_nick_name
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PicUrl') is not None:
            self.pic_url = m.get('PicUrl')
        if m.get('EventTime') is not None:
            self.event_time = m.get('EventTime')
        if m.get('GatewayIotId') is not None:
            self.gateway_iot_id = m.get('GatewayIotId')
        if m.get('VectorId') is not None:
            self.vector_id = m.get('VectorId')
        if m.get('DeviceNickName') is not None:
            self.device_nick_name = m.get('DeviceNickName')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        return self


class QueryPictureSearchJobResultResponseBodyData(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        page_data: List[QueryPictureSearchJobResultResponseBodyDataPageData] = None,
        page_size: int = None,
        total: int = None,
        page_count: int = None,
    ):
        self.current_page = current_page
        self.page_data = page_data
        self.page_size = page_size
        self.total = total
        self.page_count = page_count

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
        result['PageData'] = []
        if self.page_data is not None:
            for k in self.page_data:
                result['PageData'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.page_data = []
        if m.get('PageData') is not None:
            for k in m.get('PageData'):
                temp_model = QueryPictureSearchJobResultResponseBodyDataPageData()
                self.page_data.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        return self


class QueryPictureSearchJobResultResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: QueryPictureSearchJobResultResponseBodyData = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.data = data
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = QueryPictureSearchJobResultResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryPictureSearchJobResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryPictureSearchJobResultResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryPictureSearchJobResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryRecordRequest(TeaModel):
    def __init__(
        self,
        iot_id: str = None,
        stream_type: int = None,
        begin_time: int = None,
        end_time: int = None,
        record_type: int = None,
        current_page: int = None,
        page_size: int = None,
        need_snapshot: bool = None,
        iot_instance_id: str = None,
    ):
        self.iot_id = iot_id
        self.stream_type = stream_type
        self.begin_time = begin_time
        self.end_time = end_time
        self.record_type = record_type
        self.current_page = current_page
        self.page_size = page_size
        self.need_snapshot = need_snapshot
        self.iot_instance_id = iot_instance_id

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
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.record_type is not None:
            result['RecordType'] = self.record_type
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.need_snapshot is not None:
            result['NeedSnapshot'] = self.need_snapshot
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('StreamType') is not None:
            self.stream_type = m.get('StreamType')
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RecordType') is not None:
            self.record_type = m.get('RecordType')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('NeedSnapshot') is not None:
            self.need_snapshot = m.get('NeedSnapshot')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        return self


class QueryRecordResponseBodyDataList(TeaModel):
    def __init__(
        self,
        snapshot_url: str = None,
        end_time: str = None,
        record_type: int = None,
        stream_type: int = None,
        begin_time: str = None,
        file_name: str = None,
        video_frame_number: int = None,
        file_size: int = None,
    ):
        self.snapshot_url = snapshot_url
        self.end_time = end_time
        self.record_type = record_type
        self.stream_type = stream_type
        self.begin_time = begin_time
        self.file_name = file_name
        self.video_frame_number = video_frame_number
        self.file_size = file_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.snapshot_url is not None:
            result['SnapshotUrl'] = self.snapshot_url
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.record_type is not None:
            result['RecordType'] = self.record_type
        if self.stream_type is not None:
            result['StreamType'] = self.stream_type
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.video_frame_number is not None:
            result['VideoFrameNumber'] = self.video_frame_number
        if self.file_size is not None:
            result['FileSize'] = self.file_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SnapshotUrl') is not None:
            self.snapshot_url = m.get('SnapshotUrl')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RecordType') is not None:
            self.record_type = m.get('RecordType')
        if m.get('StreamType') is not None:
            self.stream_type = m.get('StreamType')
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('VideoFrameNumber') is not None:
            self.video_frame_number = m.get('VideoFrameNumber')
        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')
        return self


class QueryRecordResponseBodyData(TeaModel):
    def __init__(
        self,
        list: List[QueryRecordResponseBodyDataList] = None,
        page_size: int = None,
        page: int = None,
    ):
        self.list = list
        self.page_size = page_size
        self.page = page

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
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page is not None:
            result['Page'] = self.page
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = QueryRecordResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        return self


class QueryRecordResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: QueryRecordResponseBodyData = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.data = data
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = QueryRecordResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryRecordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryRecordResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryRecordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryRecordByRecordIdRequest(TeaModel):
    def __init__(
        self,
        iot_id: str = None,
        record_id: str = None,
        iot_instance_id: str = None,
    ):
        self.iot_id = iot_id
        self.record_id = record_id
        self.iot_instance_id = iot_instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.record_id is not None:
            result['RecordId'] = self.record_id
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        return self


class QueryRecordByRecordIdResponseBodyData(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        begin_time: str = None,
        file_name: str = None,
        vod_url: str = None,
    ):
        self.end_time = end_time
        self.begin_time = begin_time
        self.file_name = file_name
        self.vod_url = vod_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.vod_url is not None:
            result['VodUrl'] = self.vod_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('VodUrl') is not None:
            self.vod_url = m.get('VodUrl')
        return self


class QueryRecordByRecordIdResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: List[QueryRecordByRecordIdResponseBodyData] = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.data = data
        self.error_message = error_message
        self.code = code
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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = QueryRecordByRecordIdResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryRecordByRecordIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryRecordByRecordIdResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryRecordByRecordIdResponseBody()
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
        day_of_week: int = None,
        begin: int = None,
        end: int = None,
    ):
        self.day_of_week = day_of_week
        self.begin = begin
        self.end = end

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.day_of_week is not None:
            result['DayOfWeek'] = self.day_of_week
        if self.begin is not None:
            result['Begin'] = self.begin
        if self.end is not None:
            result['End'] = self.end
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DayOfWeek') is not None:
            self.day_of_week = m.get('DayOfWeek')
        if m.get('Begin') is not None:
            self.begin = m.get('Begin')
        if m.get('End') is not None:
            self.end = m.get('End')
        return self


class QueryRecordPlanDetailResponseBodyDataTemplateInfo(TeaModel):
    def __init__(
        self,
        time_section_list: List[QueryRecordPlanDetailResponseBodyDataTemplateInfoTimeSectionList] = None,
        all_day: int = None,
        default: int = None,
        name: str = None,
        template_id: str = None,
    ):
        self.time_section_list = time_section_list
        self.all_day = all_day
        self.default = default
        self.name = name
        self.template_id = template_id

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
        result['TimeSectionList'] = []
        if self.time_section_list is not None:
            for k in self.time_section_list:
                result['TimeSectionList'].append(k.to_map() if k else None)
        if self.all_day is not None:
            result['AllDay'] = self.all_day
        if self.default is not None:
            result['Default'] = self.default
        if self.name is not None:
            result['Name'] = self.name
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.time_section_list = []
        if m.get('TimeSectionList') is not None:
            for k in m.get('TimeSectionList'):
                temp_model = QueryRecordPlanDetailResponseBodyDataTemplateInfoTimeSectionList()
                self.time_section_list.append(temp_model.from_map(k))
        if m.get('AllDay') is not None:
            self.all_day = m.get('AllDay')
        if m.get('Default') is not None:
            self.default = m.get('Default')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class QueryRecordPlanDetailResponseBodyData(TeaModel):
    def __init__(
        self,
        plan_id: str = None,
        name: str = None,
        template_info: QueryRecordPlanDetailResponseBodyDataTemplateInfo = None,
        template_id: str = None,
    ):
        self.plan_id = plan_id
        self.name = name
        self.template_info = template_info
        self.template_id = template_id

    def validate(self):
        if self.template_info:
            self.template_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        if self.name is not None:
            result['Name'] = self.name
        if self.template_info is not None:
            result['TemplateInfo'] = self.template_info.to_map()
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('TemplateInfo') is not None:
            temp_model = QueryRecordPlanDetailResponseBodyDataTemplateInfo()
            self.template_info = temp_model.from_map(m['TemplateInfo'])
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class QueryRecordPlanDetailResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: QueryRecordPlanDetailResponseBodyData = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.data = data
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = QueryRecordPlanDetailResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryRecordPlanDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryRecordPlanDetailResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryRecordPlanDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryRecordPlanDeviceByDeviceRequest(TeaModel):
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


class QueryRecordPlanDeviceByDeviceResponseBodyDataTemplateInfoTimeSectionList(TeaModel):
    def __init__(
        self,
        day_of_week: int = None,
        begin: int = None,
        end: int = None,
    ):
        self.day_of_week = day_of_week
        self.begin = begin
        self.end = end

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.day_of_week is not None:
            result['DayOfWeek'] = self.day_of_week
        if self.begin is not None:
            result['Begin'] = self.begin
        if self.end is not None:
            result['End'] = self.end
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DayOfWeek') is not None:
            self.day_of_week = m.get('DayOfWeek')
        if m.get('Begin') is not None:
            self.begin = m.get('Begin')
        if m.get('End') is not None:
            self.end = m.get('End')
        return self


class QueryRecordPlanDeviceByDeviceResponseBodyDataTemplateInfo(TeaModel):
    def __init__(
        self,
        time_section_list: List[QueryRecordPlanDeviceByDeviceResponseBodyDataTemplateInfoTimeSectionList] = None,
        all_day: int = None,
        default: int = None,
        name: str = None,
        template_id: str = None,
    ):
        self.time_section_list = time_section_list
        self.all_day = all_day
        self.default = default
        self.name = name
        self.template_id = template_id

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
        result['TimeSectionList'] = []
        if self.time_section_list is not None:
            for k in self.time_section_list:
                result['TimeSectionList'].append(k.to_map() if k else None)
        if self.all_day is not None:
            result['AllDay'] = self.all_day
        if self.default is not None:
            result['Default'] = self.default
        if self.name is not None:
            result['Name'] = self.name
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.time_section_list = []
        if m.get('TimeSectionList') is not None:
            for k in m.get('TimeSectionList'):
                temp_model = QueryRecordPlanDeviceByDeviceResponseBodyDataTemplateInfoTimeSectionList()
                self.time_section_list.append(temp_model.from_map(k))
        if m.get('AllDay') is not None:
            self.all_day = m.get('AllDay')
        if m.get('Default') is not None:
            self.default = m.get('Default')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class QueryRecordPlanDeviceByDeviceResponseBodyData(TeaModel):
    def __init__(
        self,
        plan_id: str = None,
        name: str = None,
        template_info: QueryRecordPlanDeviceByDeviceResponseBodyDataTemplateInfo = None,
        template_id: str = None,
    ):
        self.plan_id = plan_id
        self.name = name
        self.template_info = template_info
        self.template_id = template_id

    def validate(self):
        if self.template_info:
            self.template_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        if self.name is not None:
            result['Name'] = self.name
        if self.template_info is not None:
            result['TemplateInfo'] = self.template_info.to_map()
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('TemplateInfo') is not None:
            temp_model = QueryRecordPlanDeviceByDeviceResponseBodyDataTemplateInfo()
            self.template_info = temp_model.from_map(m['TemplateInfo'])
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class QueryRecordPlanDeviceByDeviceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: QueryRecordPlanDeviceByDeviceResponseBodyData = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.data = data
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = QueryRecordPlanDeviceByDeviceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryRecordPlanDeviceByDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryRecordPlanDeviceByDeviceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryRecordPlanDeviceByDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryRecordPlanDeviceByPlanRequest(TeaModel):
    def __init__(
        self,
        plan_id: str = None,
        current_page: int = None,
        page_size: int = None,
    ):
        self.plan_id = plan_id
        self.current_page = current_page
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class QueryRecordPlanDeviceByPlanResponseBodyDataList(TeaModel):
    def __init__(
        self,
        stream_type: int = None,
        iot_id: str = None,
    ):
        self.stream_type = stream_type
        self.iot_id = iot_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.stream_type is not None:
            result['StreamType'] = self.stream_type
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StreamType') is not None:
            self.stream_type = m.get('StreamType')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        return self


class QueryRecordPlanDeviceByPlanResponseBodyData(TeaModel):
    def __init__(
        self,
        list: List[QueryRecordPlanDeviceByPlanResponseBodyDataList] = None,
        page_size: int = None,
        total: int = None,
        page_count: int = None,
        page: int = None,
    ):
        self.list = list
        self.page_size = page_size
        self.total = total
        self.page_count = page_count
        self.page = page

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
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        if self.page is not None:
            result['Page'] = self.page
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = QueryRecordPlanDeviceByPlanResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        return self


class QueryRecordPlanDeviceByPlanResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: QueryRecordPlanDeviceByPlanResponseBodyData = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.data = data
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = QueryRecordPlanDeviceByPlanResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryRecordPlanDeviceByPlanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryRecordPlanDeviceByPlanResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
        plan_id: str = None,
        name: str = None,
        template_id: str = None,
    ):
        self.plan_id = plan_id
        self.name = name
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        if self.name is not None:
            result['Name'] = self.name
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class QueryRecordPlansResponseBodyData(TeaModel):
    def __init__(
        self,
        list: List[QueryRecordPlansResponseBodyDataList] = None,
        page_size: int = None,
        page_count: int = None,
        total: int = None,
        page: int = None,
    ):
        self.list = list
        self.page_size = page_size
        self.page_count = page_count
        self.total = total
        self.page = page

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
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        if self.total is not None:
            result['Total'] = self.total
        if self.page is not None:
            result['Page'] = self.page
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = QueryRecordPlansResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        return self


class QueryRecordPlansResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: QueryRecordPlansResponseBodyData = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.data = data
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = QueryRecordPlansResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryRecordPlansResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryRecordPlansResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryRecordPlansResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryRecordUrlRequest(TeaModel):
    def __init__(
        self,
        iot_id: str = None,
        file_name: str = None,
        iot_instance_id: str = None,
    ):
        self.iot_id = iot_id
        self.file_name = file_name
        self.iot_instance_id = iot_instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        return self


class QueryRecordUrlResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: str = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.data = data
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryRecordUrlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryRecordUrlResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryRecordUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryStandardAIAppTemplatesRequest(TeaModel):
    def __init__(
        self,
        page_size: int = None,
        current_page: int = None,
    ):
        self.page_size = page_size
        self.current_page = current_page

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        return self


class QueryStandardAIAppTemplatesResponseBodyDataList(TeaModel):
    def __init__(
        self,
        description: str = None,
        version: str = None,
        app_template_id: str = None,
        name: str = None,
    ):
        self.description = description
        self.version = version
        self.app_template_id = app_template_id
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
        if self.version is not None:
            result['Version'] = self.version
        if self.app_template_id is not None:
            result['AppTemplateId'] = self.app_template_id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('AppTemplateId') is not None:
            self.app_template_id = m.get('AppTemplateId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class QueryStandardAIAppTemplatesResponseBodyData(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        list: List[QueryStandardAIAppTemplatesResponseBodyDataList] = None,
        page_size: int = None,
        total: int = None,
        page_count: int = None,
    ):
        self.current_page = current_page
        self.list = list
        self.page_size = page_size
        self.total = total
        self.page_count = page_count

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
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = QueryStandardAIAppTemplatesResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        return self


class QueryStandardAIAppTemplatesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: QueryStandardAIAppTemplatesResponseBodyData = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.data = data
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = QueryStandardAIAppTemplatesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryStandardAIAppTemplatesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryStandardAIAppTemplatesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryStandardAIAppTemplatesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTimeTemplateRequest(TeaModel):
    def __init__(
        self,
        page_size: int = None,
        current_page: int = None,
    ):
        self.page_size = page_size
        self.current_page = current_page

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        return self


class QueryTimeTemplateResponseBodyDataListTimeSectionList(TeaModel):
    def __init__(
        self,
        day_of_week: int = None,
        begin: int = None,
        end: int = None,
    ):
        self.day_of_week = day_of_week
        self.begin = begin
        self.end = end

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.day_of_week is not None:
            result['DayOfWeek'] = self.day_of_week
        if self.begin is not None:
            result['Begin'] = self.begin
        if self.end is not None:
            result['End'] = self.end
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DayOfWeek') is not None:
            self.day_of_week = m.get('DayOfWeek')
        if m.get('Begin') is not None:
            self.begin = m.get('Begin')
        if m.get('End') is not None:
            self.end = m.get('End')
        return self


class QueryTimeTemplateResponseBodyDataList(TeaModel):
    def __init__(
        self,
        time_section_list: List[QueryTimeTemplateResponseBodyDataListTimeSectionList] = None,
        all_day: int = None,
        default: int = None,
        name: str = None,
        template_id: str = None,
    ):
        self.time_section_list = time_section_list
        self.all_day = all_day
        self.default = default
        self.name = name
        self.template_id = template_id

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
        result['TimeSectionList'] = []
        if self.time_section_list is not None:
            for k in self.time_section_list:
                result['TimeSectionList'].append(k.to_map() if k else None)
        if self.all_day is not None:
            result['AllDay'] = self.all_day
        if self.default is not None:
            result['Default'] = self.default
        if self.name is not None:
            result['Name'] = self.name
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.time_section_list = []
        if m.get('TimeSectionList') is not None:
            for k in m.get('TimeSectionList'):
                temp_model = QueryTimeTemplateResponseBodyDataListTimeSectionList()
                self.time_section_list.append(temp_model.from_map(k))
        if m.get('AllDay') is not None:
            self.all_day = m.get('AllDay')
        if m.get('Default') is not None:
            self.default = m.get('Default')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class QueryTimeTemplateResponseBodyData(TeaModel):
    def __init__(
        self,
        list: List[QueryTimeTemplateResponseBodyDataList] = None,
        page_size: int = None,
        total: int = None,
        page_count: int = None,
        page: int = None,
    ):
        self.list = list
        self.page_size = page_size
        self.total = total
        self.page_count = page_count
        self.page = page

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
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        if self.page is not None:
            result['Page'] = self.page
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = QueryTimeTemplateResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        return self


class QueryTimeTemplateResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: QueryTimeTemplateResponseBodyData = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.data = data
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = QueryTimeTemplateResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryTimeTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryTimeTemplateResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
        day_of_week: int = None,
        begin: int = None,
        end: int = None,
    ):
        self.day_of_week = day_of_week
        self.begin = begin
        self.end = end

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.day_of_week is not None:
            result['DayOfWeek'] = self.day_of_week
        if self.begin is not None:
            result['Begin'] = self.begin
        if self.end is not None:
            result['End'] = self.end
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DayOfWeek') is not None:
            self.day_of_week = m.get('DayOfWeek')
        if m.get('Begin') is not None:
            self.begin = m.get('Begin')
        if m.get('End') is not None:
            self.end = m.get('End')
        return self


class QueryTimeTemplateDetailResponseBodyData(TeaModel):
    def __init__(
        self,
        time_section_list: List[QueryTimeTemplateDetailResponseBodyDataTimeSectionList] = None,
        all_day: int = None,
        default: int = None,
        name: str = None,
        template_id: str = None,
    ):
        self.time_section_list = time_section_list
        self.all_day = all_day
        self.default = default
        self.name = name
        self.template_id = template_id

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
        result['TimeSectionList'] = []
        if self.time_section_list is not None:
            for k in self.time_section_list:
                result['TimeSectionList'].append(k.to_map() if k else None)
        if self.all_day is not None:
            result['AllDay'] = self.all_day
        if self.default is not None:
            result['Default'] = self.default
        if self.name is not None:
            result['Name'] = self.name
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.time_section_list = []
        if m.get('TimeSectionList') is not None:
            for k in m.get('TimeSectionList'):
                temp_model = QueryTimeTemplateDetailResponseBodyDataTimeSectionList()
                self.time_section_list.append(temp_model.from_map(k))
        if m.get('AllDay') is not None:
            self.all_day = m.get('AllDay')
        if m.get('Default') is not None:
            self.default = m.get('Default')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class QueryTimeTemplateDetailResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: QueryTimeTemplateDetailResponseBodyData = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.data = data
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = QueryTimeTemplateDetailResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryTimeTemplateDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryTimeTemplateDetailResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryTimeTemplateDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryVoiceIntercomRequest(TeaModel):
    def __init__(
        self,
        iot_id: str = None,
        iot_instance_id: str = None,
    ):
        self.iot_id = iot_id
        self.iot_instance_id = iot_instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        return self


class QueryVoiceIntercomResponseBodyDataCryptoKey(TeaModel):
    def __init__(
        self,
        key: str = None,
        iv: str = None,
    ):
        self.key = key
        self.iv = iv

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.iv is not None:
            result['Iv'] = self.iv
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Iv') is not None:
            self.iv = m.get('Iv')
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
        request_id: str = None,
        data: QueryVoiceIntercomResponseBodyData = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.data = data
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = QueryVoiceIntercomResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryVoiceIntercomResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryVoiceIntercomResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryVoiceIntercomResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveAIAppRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
    ):
        self.app_id = app_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        return self


class RemoveAIAppResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RemoveAIAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RemoveAIAppResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RemoveAIAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveAIPlanRequest(TeaModel):
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


class RemoveAIPlanResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RemoveAIPlanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RemoveAIPlanResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RemoveAIPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveDevicePurifyPlanRequest(TeaModel):
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


class RemoveDevicePurifyPlanResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RemoveDevicePurifyPlanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RemoveDevicePurifyPlanResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RemoveDevicePurifyPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveFaceDeviceFromDeviceGroupRequest(TeaModel):
    def __init__(
        self,
        isolation_id: str = None,
        iot_instance_id: str = None,
        product_key: str = None,
        device_name: str = None,
        device_group_id: str = None,
    ):
        self.isolation_id = isolation_id
        self.iot_instance_id = iot_instance_id
        self.product_key = product_key
        self.device_name = device_name
        self.device_group_id = device_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.isolation_id is not None:
            result['IsolationId'] = self.isolation_id
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.device_group_id is not None:
            result['DeviceGroupId'] = self.device_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsolationId') is not None:
            self.isolation_id = m.get('IsolationId')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('DeviceGroupId') is not None:
            self.device_group_id = m.get('DeviceGroupId')
        return self


class RemoveFaceDeviceFromDeviceGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RemoveFaceDeviceFromDeviceGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RemoveFaceDeviceFromDeviceGroupResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RemoveFaceDeviceFromDeviceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveFaceUserFromUserGroupRequest(TeaModel):
    def __init__(
        self,
        isolation_id: str = None,
        user_id: str = None,
        user_group_id: str = None,
    ):
        self.isolation_id = isolation_id
        self.user_id = user_id
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
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsolationId') is not None:
            self.isolation_id = m.get('IsolationId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        return self


class RemoveFaceUserFromUserGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RemoveFaceUserFromUserGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RemoveFaceUserFromUserGroupResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RemoveFaceUserFromUserGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetDevicePictureLifeCycleRequest(TeaModel):
    def __init__(
        self,
        iot_id: str = None,
        day: int = None,
    ):
        self.iot_id = iot_id
        self.day = day

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.day is not None:
            result['Day'] = self.day
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('Day') is not None:
            self.day = m.get('Day')
        return self


class SetDevicePictureLifeCycleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SetDevicePictureLifeCycleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SetDevicePictureLifeCycleResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SetDevicePictureLifeCycleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetDeviceRecordLifeCycleRequest(TeaModel):
    def __init__(
        self,
        iot_id: str = None,
        day: int = None,
    ):
        self.iot_id = iot_id
        self.day = day

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.day is not None:
            result['Day'] = self.day
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('Day') is not None:
            self.day = m.get('Day')
        return self


class SetDeviceRecordLifeCycleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SetDeviceRecordLifeCycleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SetDeviceRecordLifeCycleResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SetDeviceRecordLifeCycleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopLiveStreamingRequest(TeaModel):
    def __init__(
        self,
        iot_id: str = None,
        stream_type: int = None,
        iot_instance_id: str = None,
    ):
        self.iot_id = iot_id
        self.stream_type = stream_type
        self.iot_instance_id = iot_instance_id

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
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('StreamType') is not None:
            self.stream_type = m.get('StreamType')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        return self


class StopLiveStreamingResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class StopLiveStreamingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StopLiveStreamingResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = StopLiveStreamingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopTriggeredRecordRequest(TeaModel):
    def __init__(
        self,
        iot_id: str = None,
        record_id: str = None,
    ):
        self.iot_id = iot_id
        self.record_id = record_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.record_id is not None:
            result['RecordId'] = self.record_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')
        return self


class StopTriggeredRecordResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class StopTriggeredRecordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StopTriggeredRecordResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = StopTriggeredRecordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TriggerCapturePictureRequest(TeaModel):
    def __init__(
        self,
        iot_id: str = None,
        iot_instance_id: str = None,
    ):
        self.iot_id = iot_id
        self.iot_instance_id = iot_instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        return self


class TriggerCapturePictureResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: str = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.data = data
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class TriggerCapturePictureResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: TriggerCapturePictureResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = TriggerCapturePictureResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TriggerRecordRequest(TeaModel):
    def __init__(
        self,
        iot_id: str = None,
        stream_type: int = None,
        pre_record_duration: int = None,
        record_duration: int = None,
        iot_instance_id: str = None,
    ):
        self.iot_id = iot_id
        self.stream_type = stream_type
        self.pre_record_duration = pre_record_duration
        self.record_duration = record_duration
        self.iot_instance_id = iot_instance_id

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
        if self.pre_record_duration is not None:
            result['PreRecordDuration'] = self.pre_record_duration
        if self.record_duration is not None:
            result['RecordDuration'] = self.record_duration
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('StreamType') is not None:
            self.stream_type = m.get('StreamType')
        if m.get('PreRecordDuration') is not None:
            self.pre_record_duration = m.get('PreRecordDuration')
        if m.get('RecordDuration') is not None:
            self.record_duration = m.get('RecordDuration')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        return self


class TriggerRecordResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: str = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.data = data
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class TriggerRecordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: TriggerRecordResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = TriggerRecordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnbindAIPlanWithDevicesRequest(TeaModel):
    def __init__(
        self,
        plan_id: str = None,
        iot_id_list: List[str] = None,
    ):
        self.plan_id = plan_id
        self.iot_id_list = iot_id_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        if self.iot_id_list is not None:
            result['IotIdList'] = self.iot_id_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        if m.get('IotIdList') is not None:
            self.iot_id_list = m.get('IotIdList')
        return self


class UnbindAIPlanWithDevicesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UnbindAIPlanWithDevicesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UnbindAIPlanWithDevicesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UnbindAIPlanWithDevicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnbindPictureSearchAppWithDevicesRequest(TeaModel):
    def __init__(
        self,
        app_instance_id: str = None,
        iot_instance_id: str = None,
        device_iot_ids: List[str] = None,
    ):
        self.app_instance_id = app_instance_id
        self.iot_instance_id = iot_instance_id
        self.device_iot_ids = device_iot_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_id is not None:
            result['AppInstanceId'] = self.app_instance_id
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.device_iot_ids is not None:
            result['DeviceIotIds'] = self.device_iot_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceId') is not None:
            self.app_instance_id = m.get('AppInstanceId')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('DeviceIotIds') is not None:
            self.device_iot_ids = m.get('DeviceIotIds')
        return self


class UnbindPictureSearchAppWithDevicesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UnbindPictureSearchAppWithDevicesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UnbindPictureSearchAppWithDevicesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UnbindPictureSearchAppWithDevicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAIAppRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        level: int = None,
        name: str = None,
        description: str = None,
    ):
        self.app_id = app_id
        self.level = level
        self.name = name
        self.description = description

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.level is not None:
            result['Level'] = self.level
        if self.name is not None:
            result['Name'] = self.name
        if self.description is not None:
            result['Description'] = self.description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        return self


class UpdateAIAppResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateAIAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateAIAppResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateAIAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAIPlanRequest(TeaModel):
    def __init__(
        self,
        plan_id: str = None,
        description: str = None,
    ):
        self.plan_id = plan_id
        self.description = description

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        if self.description is not None:
            result['Description'] = self.description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        return self


class UpdateAIPlanResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateAIPlanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateAIPlanResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateAIPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDevicePurifyPlanRequest(TeaModel):
    def __init__(
        self,
        plan_id: str = None,
        start_time: int = None,
        end_time: int = None,
    ):
        self.plan_id = plan_id
        self.start_time = start_time
        self.end_time = end_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        return self


class UpdateDevicePurifyPlanResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateDevicePurifyPlanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateDevicePurifyPlanResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateDevicePurifyPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateEventRecordPlanRequest(TeaModel):
    def __init__(
        self,
        plan_id: str = None,
        name: str = None,
        event_types: str = None,
        pre_record_duration: int = None,
        record_duration: int = None,
        template_id: str = None,
    ):
        self.plan_id = plan_id
        self.name = name
        self.event_types = event_types
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
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        if self.name is not None:
            result['Name'] = self.name
        if self.event_types is not None:
            result['EventTypes'] = self.event_types
        if self.pre_record_duration is not None:
            result['PreRecordDuration'] = self.pre_record_duration
        if self.record_duration is not None:
            result['RecordDuration'] = self.record_duration
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('EventTypes') is not None:
            self.event_types = m.get('EventTypes')
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
        request_id: str = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateEventRecordPlanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateEventRecordPlanResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateEventRecordPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateFaceUserRequest(TeaModel):
    def __init__(
        self,
        isolation_id: str = None,
        user_id: str = None,
        name: str = None,
        params: str = None,
        face_pic_url: str = None,
        custom_user_id: str = None,
    ):
        self.isolation_id = isolation_id
        self.user_id = user_id
        self.name = name
        self.params = params
        self.face_pic_url = face_pic_url
        self.custom_user_id = custom_user_id

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
        if self.name is not None:
            result['Name'] = self.name
        if self.params is not None:
            result['Params'] = self.params
        if self.face_pic_url is not None:
            result['FacePicUrl'] = self.face_pic_url
        if self.custom_user_id is not None:
            result['CustomUserId'] = self.custom_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsolationId') is not None:
            self.isolation_id = m.get('IsolationId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Params') is not None:
            self.params = m.get('Params')
        if m.get('FacePicUrl') is not None:
            self.face_pic_url = m.get('FacePicUrl')
        if m.get('CustomUserId') is not None:
            self.custom_user_id = m.get('CustomUserId')
        return self


class UpdateFaceUserResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateFaceUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateFaceUserResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateFaceUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateFaceUserGroupAndDeviceGroupRelationRequest(TeaModel):
    def __init__(
        self,
        isolation_id: str = None,
        control_id: str = None,
        relation: str = None,
    ):
        self.isolation_id = isolation_id
        self.control_id = control_id
        self.relation = relation

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.isolation_id is not None:
            result['IsolationId'] = self.isolation_id
        if self.control_id is not None:
            result['ControlId'] = self.control_id
        if self.relation is not None:
            result['Relation'] = self.relation
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsolationId') is not None:
            self.isolation_id = m.get('IsolationId')
        if m.get('ControlId') is not None:
            self.control_id = m.get('ControlId')
        if m.get('Relation') is not None:
            self.relation = m.get('Relation')
        return self


class UpdateFaceUserGroupAndDeviceGroupRelationResponseBodyData(TeaModel):
    def __init__(
        self,
        modified_time: str = None,
        control_id: str = None,
    ):
        self.modified_time = modified_time
        self.control_id = control_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.control_id is not None:
            result['ControlId'] = self.control_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('ControlId') is not None:
            self.control_id = m.get('ControlId')
        return self


class UpdateFaceUserGroupAndDeviceGroupRelationResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: UpdateFaceUserGroupAndDeviceGroupRelationResponseBodyData = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.data = data
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = UpdateFaceUserGroupAndDeviceGroupRelationResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateFaceUserGroupAndDeviceGroupRelationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateFaceUserGroupAndDeviceGroupRelationResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateFaceUserGroupAndDeviceGroupRelationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateModelRequest(TeaModel):
    def __init__(
        self,
        model_id: int = None,
        name: str = None,
        hardware: str = None,
        description: str = None,
    ):
        self.model_id = model_id
        self.name = name
        self.hardware = hardware
        self.description = description

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.model_id is not None:
            result['ModelId'] = self.model_id
        if self.name is not None:
            result['Name'] = self.name
        if self.hardware is not None:
            result['Hardware'] = self.hardware
        if self.description is not None:
            result['Description'] = self.description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Hardware') is not None:
            self.hardware = m.get('Hardware')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        return self


class UpdateModelResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: Dict[str, Any] = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.data = data
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateModelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateModelResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateModelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdatePictureSearchAppRequest(TeaModel):
    def __init__(
        self,
        app_instance_id: str = None,
        name: str = None,
        description: str = None,
    ):
        self.app_instance_id = app_instance_id
        self.name = name
        self.description = description

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_id is not None:
            result['AppInstanceId'] = self.app_instance_id
        if self.name is not None:
            result['Name'] = self.name
        if self.description is not None:
            result['Description'] = self.description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceId') is not None:
            self.app_instance_id = m.get('AppInstanceId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        return self


class UpdatePictureSearchAppResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdatePictureSearchAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdatePictureSearchAppResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdatePictureSearchAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateRecordPlanRequest(TeaModel):
    def __init__(
        self,
        plan_id: str = None,
        name: str = None,
        template_id: str = None,
    ):
        self.plan_id = plan_id
        self.name = name
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        if self.name is not None:
            result['Name'] = self.name
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class UpdateRecordPlanResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateRecordPlanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateRecordPlanResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateRecordPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateTimeTemplateRequestTimeSections(TeaModel):
    def __init__(
        self,
        day_of_week: int = None,
        begin: int = None,
        end: int = None,
    ):
        self.day_of_week = day_of_week
        self.begin = begin
        self.end = end

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.day_of_week is not None:
            result['DayOfWeek'] = self.day_of_week
        if self.begin is not None:
            result['Begin'] = self.begin
        if self.end is not None:
            result['End'] = self.end
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DayOfWeek') is not None:
            self.day_of_week = m.get('DayOfWeek')
        if m.get('Begin') is not None:
            self.begin = m.get('Begin')
        if m.get('End') is not None:
            self.end = m.get('End')
        return self


class UpdateTimeTemplateRequest(TeaModel):
    def __init__(
        self,
        template_id: str = None,
        name: str = None,
        all_day: int = None,
        time_sections: List[UpdateTimeTemplateRequestTimeSections] = None,
    ):
        self.template_id = template_id
        self.name = name
        self.all_day = all_day
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
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.name is not None:
            result['Name'] = self.name
        if self.all_day is not None:
            result['AllDay'] = self.all_day
        result['TimeSections'] = []
        if self.time_sections is not None:
            for k in self.time_sections:
                result['TimeSections'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('AllDay') is not None:
            self.all_day = m.get('AllDay')
        self.time_sections = []
        if m.get('TimeSections') is not None:
            for k in m.get('TimeSections'):
                temp_model = UpdateTimeTemplateRequestTimeSections()
                self.time_sections.append(temp_model.from_map(k))
        return self


class UpdateTimeTemplateResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateTimeTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateTimeTemplateResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateTimeTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


