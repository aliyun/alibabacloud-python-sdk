# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, Any, List


class AddVirtualNumberRelationRequest(TeaModel):
    def __init__(
        self,
        corp_name_list: str = None,
        number_list: str = None,
        owner_id: int = None,
        phone_num: str = None,
        prod_code: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        route_type: int = None,
    ):
        # The company names. Separate multiple company names with commas (,).
        self.corp_name_list = corp_name_list
        # The real numbers. Separate multiple real numbers with commas (,).
        # 
        # This parameter is required.
        self.number_list = number_list
        self.owner_id = owner_id
        # The virtual number.
        # 
        # This parameter is required.
        self.phone_num = phone_num
        # The service name. Default value: **dyvms**.
        self.prod_code = prod_code
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The route type. Valid values:
        # 
        # *   **0**: number location first.
        # *   **1**: random.
        # 
        # This parameter is required.
        self.route_type = route_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_name_list is not None:
            result['CorpNameList'] = self.corp_name_list
        if self.number_list is not None:
            result['NumberList'] = self.number_list
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.phone_num is not None:
            result['PhoneNum'] = self.phone_num
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.route_type is not None:
            result['RouteType'] = self.route_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpNameList') is not None:
            self.corp_name_list = m.get('CorpNameList')
        if m.get('NumberList') is not None:
            self.number_list = m.get('NumberList')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PhoneNum') is not None:
            self.phone_num = m.get('PhoneNum')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RouteType') is not None:
            self.route_type = m.get('RouteType')
        return self


class AddVirtualNumberRelationResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
    ):
        # The response code.
        # 
        # *   The value 200 indicates that the request was successful.
        # *   For more information about other response codes, see [API error codes](https://help.aliyun.com/document_detail/112502.html).
        self.code = code
        # The numbers that failed to be associated.
        # 
        # > If all numbers are associated, no value is returned for this parameter.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id

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
        return self


class AddVirtualNumberRelationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddVirtualNumberRelationResponseBody = None,
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
            temp_model = AddVirtualNumberRelationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchRobotSmartCallRequest(TeaModel):
    def __init__(
        self,
        called_number: str = None,
        called_show_number: str = None,
        corp_name: str = None,
        dialog_id: str = None,
        early_media_asr: bool = None,
        is_self_line: bool = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        schedule_call: bool = None,
        schedule_time: int = None,
        task_name: str = None,
        tts_param: str = None,
        tts_param_head: str = None,
    ):
        # The called number. Only mobile phone numbers in the Chinese mainland are supported.
        # 
        # You can set up to 1,000 called numbers and separate the numbers with commas (,).
        # 
        # This parameter is required.
        self.called_number = called_number
        # The number displayed to called parties, which must be a number you purchased. You can view the numbers you purchased in the [Voice Messaging Service console](https://dyvms.console.aliyun.com/dyvms.htm#/number/normal).
        # 
        # You can set up to 100 numbers and separate the numbers with commas (,).
        # 
        # This parameter is required.
        self.called_show_number = called_show_number
        # The company name, which must be the same as the **company name** specified on the [qualification management page](https://dyvms.console.aliyun.com/dyvms.htm#/corp/normal).
        # 
        # > This parameter is optional if **isSelfLine** is set to **true**.
        self.corp_name = corp_name
        # The ID of the robot or communication script that is used to initiate a call.
        # 
        # You can obtain the **communication script ID** from the [Communication script management](https://dyvms.console.aliyun.com/dyvms.htm#/smart-call/saas/robot/list) page.
        # 
        # This parameter is required.
        self.dialog_id = dialog_id
        # The speech recognition identifier of early media. The default value is **false**, which means that the speech recognition identifier of early media is not enabled.
        # 
        # Set the parameter to **true** if you want to enable the speech recognition identifier of early media.
        self.early_media_asr = early_media_asr
        # Specifies whether to call the self-managed line. Default value: **false**.
        self.is_self_line = is_self_line
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Specifies whether the call is scheduled. If you set this parameter to **true**, the **ScheduleTime** parameter is required.
        self.schedule_call = schedule_call
        # The preset call time. This value is a UNIX timestamp. Unit: milliseconds.
        # 
        # >  This parameter is required only when **ScheduleCall** is set to **true**.
        self.schedule_time = schedule_time
        # The task name. The task name can be up to 30 characters in length.
        # 
        # This parameter is required.
        self.task_name = task_name
        # The variable value of the TTS template, in the JSON format.
        # 
        # The variable value must correspond to a number. The TtsParam parameter must be used together with the TtsParamHead parameter.
        self.tts_param = tts_param
        # The call tasks with variables, in the JSON format.
        # 
        # The parameter value is a list of variable names. The TtsParamHead parameter must be used together with the TtsParam parameter.
        self.tts_param_head = tts_param_head

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.called_number is not None:
            result['CalledNumber'] = self.called_number
        if self.called_show_number is not None:
            result['CalledShowNumber'] = self.called_show_number
        if self.corp_name is not None:
            result['CorpName'] = self.corp_name
        if self.dialog_id is not None:
            result['DialogId'] = self.dialog_id
        if self.early_media_asr is not None:
            result['EarlyMediaAsr'] = self.early_media_asr
        if self.is_self_line is not None:
            result['IsSelfLine'] = self.is_self_line
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.schedule_call is not None:
            result['ScheduleCall'] = self.schedule_call
        if self.schedule_time is not None:
            result['ScheduleTime'] = self.schedule_time
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.tts_param is not None:
            result['TtsParam'] = self.tts_param
        if self.tts_param_head is not None:
            result['TtsParamHead'] = self.tts_param_head
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CalledNumber') is not None:
            self.called_number = m.get('CalledNumber')
        if m.get('CalledShowNumber') is not None:
            self.called_show_number = m.get('CalledShowNumber')
        if m.get('CorpName') is not None:
            self.corp_name = m.get('CorpName')
        if m.get('DialogId') is not None:
            self.dialog_id = m.get('DialogId')
        if m.get('EarlyMediaAsr') is not None:
            self.early_media_asr = m.get('EarlyMediaAsr')
        if m.get('IsSelfLine') is not None:
            self.is_self_line = m.get('IsSelfLine')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ScheduleCall') is not None:
            self.schedule_call = m.get('ScheduleCall')
        if m.get('ScheduleTime') is not None:
            self.schedule_time = m.get('ScheduleTime')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('TtsParam') is not None:
            self.tts_param = m.get('TtsParam')
        if m.get('TtsParamHead') is not None:
            self.tts_param_head = m.get('TtsParamHead')
        return self


class BatchRobotSmartCallResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        task_id: str = None,
    ):
        # The response code.
        # 
        # *   The value OK indicates that the request was successful.
        # *   For more information about other response codes, see [API error codes](https://help.aliyun.com/document_detail/112502.html).
        self.code = code
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The unique ID of the robocall task. You can call the [QueryCallDetailByTaskId](https://help.aliyun.com/document_detail/393537.html) operation to query the details of the task based on the task ID.
        self.task_id = task_id

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
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class BatchRobotSmartCallResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BatchRobotSmartCallResponseBody = None,
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
            temp_model = BatchRobotSmartCallResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelCallRequest(TeaModel):
    def __init__(
        self,
        call_id: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # This parameter is required.
        self.call_id = call_id
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.call_id is not None:
            result['CallId'] = self.call_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallId') is not None:
            self.call_id = m.get('CallId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class CancelCallResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        status: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.status = status

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
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class CancelCallResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CancelCallResponseBody = None,
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
            temp_model = CancelCallResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelOrderRobotTaskRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        task_id: int = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The unique ID of the robocall task. You can call the [CreateRobotTask](https://help.aliyun.com/document_detail/393531.html) operation to obtain the ID of the robocall task.
        # 
        # This parameter is required.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CancelOrderRobotTaskResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
    ):
        # The response code.
        # 
        # *   The value OK indicates that the request was successful.
        # *   For more information about other response codes, see [API error codes](https://help.aliyun.com/document_detail/112502.html).
        self.code = code
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**: The request was successful.
        # *   **false**: The request failed.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id

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
        return self


class CancelOrderRobotTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CancelOrderRobotTaskResponseBody = None,
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
            temp_model = CancelOrderRobotTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelRobotTaskRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        task_id: int = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The unique ID of the robocall task. You can call the [CreateRobotTask](https://help.aliyun.com/document_detail/393531.html) operation to obtain the task ID.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CancelRobotTaskResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
    ):
        # The response code.
        # 
        # *   The value OK indicates that the request was successful.
        # *   For more information about other response codes, see [API error codes](https://help.aliyun.com/document_detail/112502.html).
        self.code = code
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**: The request was successful.
        # *   **false**: The request failed.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id

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
        return self


class CancelRobotTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CancelRobotTaskResponseBody = None,
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
            temp_model = CancelRobotTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ChangeMediaTypeRequest(TeaModel):
    def __init__(
        self,
        call_id: str = None,
        called_num: str = None,
        media_type: str = None,
        out_id: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.call_id = call_id
        # This parameter is required.
        self.called_num = called_num
        self.media_type = media_type
        self.out_id = out_id
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.call_id is not None:
            result['CallId'] = self.call_id
        if self.called_num is not None:
            result['CalledNum'] = self.called_num
        if self.media_type is not None:
            result['MediaType'] = self.media_type
        if self.out_id is not None:
            result['OutId'] = self.out_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallId') is not None:
            self.call_id = m.get('CallId')
        if m.get('CalledNum') is not None:
            self.called_num = m.get('CalledNum')
        if m.get('MediaType') is not None:
            self.media_type = m.get('MediaType')
        if m.get('OutId') is not None:
            self.out_id = m.get('OutId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class ChangeMediaTypeResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        message: str = None,
        model: bool = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.message = message
        self.model = model
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.model is not None:
            result['Model'] = self.model
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ChangeMediaTypeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ChangeMediaTypeResponseBody = None,
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
            temp_model = ChangeMediaTypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCallTaskRequest(TeaModel):
    def __init__(
        self,
        biz_type: str = None,
        data: str = None,
        data_type: str = None,
        fire_time: str = None,
        owner_id: int = None,
        resource: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        resource_type: str = None,
        schedule_type: str = None,
        stop_time: str = None,
        task_name: str = None,
        template_code: str = None,
        template_name: str = None,
    ):
        # The type of the task template. Valid values:
        # 
        # *   **VMS_VOICE_TTS**: the text-to-speech (TTS) notification template.
        # *   **VMS_VOICE_CODE**: the voice notification template.
        # *   **VMS_TTS**: the voice verification code template.
        self.biz_type = biz_type
        # The called numbers.
        # 
        # *   If you set DataType to LIST, the value of Data is in the LIST format.
        # *   If you set DataType to JSON, the value of Data is in the JSON format.
        self.data = data
        # The type of called numbers. Valid values:
        # 
        # *   **LIST**: the called numbers that are separated by commas (,).
        # *   **JSON**: a JSON-formatted list of called numbers with template parameters.
        self.data_type = data_type
        # This parameter is unavailable.
        self.fire_time = fire_time
        self.owner_id = owner_id
        # The calling number. Only virtual numbers are supported.
        self.resource = resource
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The type of the calling number. Set the value to **LIST**.
        self.resource_type = resource_type
        # This parameter is unavailable.
        self.schedule_type = schedule_type
        # This parameter is unavailable.
        self.stop_time = stop_time
        # The task name.
        self.task_name = task_name
        # The template ID.
        self.template_code = template_code
        # The template name.
        self.template_name = template_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.data is not None:
            result['Data'] = self.data
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.fire_time is not None:
            result['FireTime'] = self.fire_time
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource is not None:
            result['Resource'] = self.resource
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.schedule_type is not None:
            result['ScheduleType'] = self.schedule_type
        if self.stop_time is not None:
            result['StopTime'] = self.stop_time
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('FireTime') is not None:
            self.fire_time = m.get('FireTime')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Resource') is not None:
            self.resource = m.get('Resource')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ScheduleType') is not None:
            self.schedule_type = m.get('ScheduleType')
        if m.get('StopTime') is not None:
            self.stop_time = m.get('StopTime')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        return self


class CreateCallTaskResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: int = None,
        request_id: str = None,
    ):
        # The response code.
        self.code = code
        # The task ID.
        self.data = data
        # The request ID.
        self.request_id = request_id

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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateCallTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateCallTaskResponseBody = None,
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
            temp_model = CreateCallTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRobotTaskRequest(TeaModel):
    def __init__(
        self,
        caller: str = None,
        corp_name: str = None,
        dialog_id: int = None,
        is_self_line: bool = None,
        number_status_ident: bool = None,
        owner_id: int = None,
        recall_interval: int = None,
        recall_state_codes: str = None,
        recall_times: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        retry_type: int = None,
        task_name: str = None,
    ):
        # The calling number.
        # 
        # You must use the phone numbers that you have purchased and separate multiple numbers with commas (,). You can log on to the [Voice Messaging Service console](https://dyvms.console.aliyun.com/overview/home) and choose **Real Number Service** > **Real Number Management** to view the numbers you purchased.
        # 
        # This parameter is required.
        self.caller = caller
        # The company name, which must be the same as the **enterprise name** on the qualification management page.
        self.corp_name = corp_name
        # The ID of the robot or communication script that is used to initiate the call.
        # 
        # You can log on to the [Voice Messaging Service console](https://dyvms.console.aliyun.com/overview/home) and choose **Intelligent Voice Robot** > **Communication Script Management** to view the communication script ID.
        # 
        # This parameter is required.
        self.dialog_id = dialog_id
        # Specifies whether to call the self-managed line. Valid values:
        # 
        # *   **false** (default)
        # *   **true**\
        # 
        # > If you set this parameter to **true**, calling numbers are not verified.
        self.is_self_line = is_self_line
        # Specifies whether to enable number status identification. Valid values:
        # 
        # *   **false** (default)
        # *   **true**\
        # 
        # > If you set this parameter to **true**, the reason why a call is not answered is recorded.
        # 
        # This parameter is required.
        self.number_status_ident = number_status_ident
        self.owner_id = owner_id
        # The redial interval. Unit: minutes. The value must be greater than 1.
        # 
        # > The maximum redial interval is 30 minutes.
        self.recall_interval = recall_interval
        # The call state in which redial is required. Separate multiple call states with commas (,). Valid values:
        # 
        # *   **200010**: The phone of the called party is powered off.
        # *   **200011**: The number of the called party is out of service.
        # *   **200002**: The line is busy.
        # *   **200012**: The call is lost.
        # *   **200005**: The called party cannot be connected.
        # *   **200003**: The called party does not respond to the call.
        self.recall_state_codes = recall_state_codes
        # The number of redial times.
        self.recall_times = recall_times
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Specifies whether to enable auto-redial. Valid values:
        # 
        # *   **1**: enables auto-redial.
        # *   **0**: disables auto-redial.
        # 
        # This parameter is required.
        self.retry_type = retry_type
        # The task name. The task name can be up to 30 characters in length.
        # 
        # This parameter is required.
        self.task_name = task_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.caller is not None:
            result['Caller'] = self.caller
        if self.corp_name is not None:
            result['CorpName'] = self.corp_name
        if self.dialog_id is not None:
            result['DialogId'] = self.dialog_id
        if self.is_self_line is not None:
            result['IsSelfLine'] = self.is_self_line
        if self.number_status_ident is not None:
            result['NumberStatusIdent'] = self.number_status_ident
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.recall_interval is not None:
            result['RecallInterval'] = self.recall_interval
        if self.recall_state_codes is not None:
            result['RecallStateCodes'] = self.recall_state_codes
        if self.recall_times is not None:
            result['RecallTimes'] = self.recall_times
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.retry_type is not None:
            result['RetryType'] = self.retry_type
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Caller') is not None:
            self.caller = m.get('Caller')
        if m.get('CorpName') is not None:
            self.corp_name = m.get('CorpName')
        if m.get('DialogId') is not None:
            self.dialog_id = m.get('DialogId')
        if m.get('IsSelfLine') is not None:
            self.is_self_line = m.get('IsSelfLine')
        if m.get('NumberStatusIdent') is not None:
            self.number_status_ident = m.get('NumberStatusIdent')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RecallInterval') is not None:
            self.recall_interval = m.get('RecallInterval')
        if m.get('RecallStateCodes') is not None:
            self.recall_state_codes = m.get('RecallStateCodes')
        if m.get('RecallTimes') is not None:
            self.recall_times = m.get('RecallTimes')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RetryType') is not None:
            self.retry_type = m.get('RetryType')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        return self


class CreateRobotTaskResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
    ):
        # The response code.
        # 
        # *   The value OK indicates that the request was successful.
        # *   For more information about other response codes, see [API error codes](https://help.aliyun.com/document_detail/112502.html).
        self.code = code
        # The unique ID of the robocall task.
        # 
        # You can call the [QueryRobotTaskDetail](https://help.aliyun.com/document_detail/393538.html) operation to query the details of the task based on the task ID.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id

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
        return self


class CreateRobotTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateRobotTaskResponseBody = None,
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
            temp_model = CreateRobotTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DegradeVideoFileRequest(TeaModel):
    def __init__(
        self,
        call_id: str = None,
        called_number: str = None,
        media_type: str = None,
        out_id: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.call_id = call_id
        # This parameter is required.
        self.called_number = called_number
        self.media_type = media_type
        self.out_id = out_id
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.call_id is not None:
            result['CallId'] = self.call_id
        if self.called_number is not None:
            result['CalledNumber'] = self.called_number
        if self.media_type is not None:
            result['MediaType'] = self.media_type
        if self.out_id is not None:
            result['OutId'] = self.out_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallId') is not None:
            self.call_id = m.get('CallId')
        if m.get('CalledNumber') is not None:
            self.called_number = m.get('CalledNumber')
        if m.get('MediaType') is not None:
            self.media_type = m.get('MediaType')
        if m.get('OutId') is not None:
            self.out_id = m.get('OutId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DegradeVideoFileResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: Dict[str, Any] = None,
        message: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.data = data
        self.message = message
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DegradeVideoFileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DegradeVideoFileResponseBody = None,
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
            temp_model = DegradeVideoFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRobotTaskRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        task_id: int = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The unique ID of the robocall task. You can call the [CreateRobotTask](~~CreateRobotTask~~) operation to obtain the task ID.
        # 
        # This parameter is required.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DeleteRobotTaskResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
    ):
        # The response code.
        # 
        # *   The value OK indicates that the request was successful.
        # *   For more information about other response codes, see [API error codes](https://help.aliyun.com/document_detail/112502.html).
        self.code = code
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**: The request was successful.
        # *   **false**: The request failed.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id

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
        return self


class DeleteRobotTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteRobotTaskResponseBody = None,
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
            temp_model = DeleteRobotTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExecuteCallTaskRequest(TeaModel):
    def __init__(
        self,
        fire_time: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        status: str = None,
        task_id: int = None,
    ):
        # The time when the call task is executed, in the yyyy-MM-dd HH:mm:ss format.
        # 
        # > You can leave this parameter empty.
        self.fire_time = fire_time
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The task state. Valid values:
        # 
        # *   **RUNNING**\
        # *   **STOP**\
        # *   **CANCEL**\
        # 
        # This parameter is required.
        self.status = status
        # The task ID. You can call the [CreateCallTask](~~CreateCallTask~~) operation to obtain the task ID.
        # 
        # This parameter is required.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fire_time is not None:
            result['FireTime'] = self.fire_time
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.status is not None:
            result['Status'] = self.status
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FireTime') is not None:
            self.fire_time = m.get('FireTime')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class ExecuteCallTaskResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
        request_id: str = None,
    ):
        # The response code.
        self.code = code
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**: The request was successful.
        # *   **false**: The request failed.
        self.data = data
        # The request ID.
        self.request_id = request_id

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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ExecuteCallTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ExecuteCallTaskResponseBody = None,
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
            temp_model = ExecuteCallTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCallMediaTypeRequest(TeaModel):
    def __init__(
        self,
        call_id: str = None,
        called_number: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.call_id = call_id
        # This parameter is required.
        self.called_number = called_number
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.call_id is not None:
            result['CallId'] = self.call_id
        if self.called_number is not None:
            result['CalledNumber'] = self.called_number
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallId') is not None:
            self.call_id = m.get('CallId')
        if m.get('CalledNumber') is not None:
            self.called_number = m.get('CalledNumber')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class GetCallMediaTypeResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: Dict[str, Any] = None,
        message: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.data = data
        self.message = message
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetCallMediaTypeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetCallMediaTypeResponseBody = None,
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
            temp_model = GetCallMediaTypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCallProgressRequest(TeaModel):
    def __init__(
        self,
        call_id: str = None,
        called_num: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.call_id = call_id
        # This parameter is required.
        self.called_num = called_num
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.call_id is not None:
            result['CallId'] = self.call_id
        if self.called_num is not None:
            result['CalledNum'] = self.called_num
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallId') is not None:
            self.call_id = m.get('CallId')
        if m.get('CalledNum') is not None:
            self.called_num = m.get('CalledNum')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class GetCallProgressResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        message: str = None,
        model: Dict[str, Any] = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.message = message
        self.model = model
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.model is not None:
            result['Model'] = self.model
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetCallProgressResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetCallProgressResponseBody = None,
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
            temp_model = GetCallProgressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetHotlineQualificationByOrderRequest(TeaModel):
    def __init__(
        self,
        order_id: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The ticket ID.
        # 
        # You can log on to the [Voice Messaging Service console](https://dyvms.console.aliyun.com/overview/home), choose **Qualification\\&Communication Script Management** > **Qualification Management**, and then click the **400 Qualifications** tab to view the ticket ID.
        # 
        # This parameter is required.
        self.order_id = order_id
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class GetHotlineQualificationByOrderResponseBodyData(TeaModel):
    def __init__(
        self,
        order_id: str = None,
        qualification_id: str = None,
        status: str = None,
    ):
        # The ID of the qualification application ticket.
        self.order_id = order_id
        # The qualification ID.
        self.qualification_id = qualification_id
        # The qualification state. Valid values:
        # 
        # *   **NORMAL**\
        # *   **OTHER**\
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.qualification_id is not None:
            result['QualificationId'] = self.qualification_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('QualificationId') is not None:
            self.qualification_id = m.get('QualificationId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetHotlineQualificationByOrderResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetHotlineQualificationByOrderResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The response code.
        # 
        # *   The value OK indicates that the request was successful.
        # *   For more information about other response codes, see [API error codes](https://help.aliyun.com/document_detail/112502.html).
        self.code = code
        # The response parameters.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetHotlineQualificationByOrderResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetHotlineQualificationByOrderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetHotlineQualificationByOrderResponseBody = None,
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
            temp_model = GetHotlineQualificationByOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTemporaryFileUrlRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        video_id: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # This parameter is required.
        self.video_id = video_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.video_id is not None:
            result['VideoId'] = self.video_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')
        return self


class GetTemporaryFileUrlResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: Dict[str, Any] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
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
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
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
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
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


class GetTemporaryFileUrlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetTemporaryFileUrlResponseBody = None,
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
            temp_model = GetTemporaryFileUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTokenRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        token_type: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The token type.
        self.token_type = token_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.token_type is not None:
            result['TokenType'] = self.token_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TokenType') is not None:
            self.token_type = m.get('TokenType')
        return self


class GetTokenResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        token: str = None,
    ):
        # The response code.
        # 
        # *   The value OK indicates that the request was successful.
        # *   For more information about other response codes, see [API error codes](https://help.aliyun.com/document_detail/112502.html).
        self.code = code
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success
        # The token.
        self.token = token

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
        if self.token is not None:
            result['Token'] = self.token
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
        if m.get('Token') is not None:
            self.token = m.get('Token')
        return self


class GetTokenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetTokenResponseBody = None,
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
            temp_model = GetTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetVideoFieldUrlRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        video_file: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.video_file = video_file

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.video_file is not None:
            result['VideoFile'] = self.video_file
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('VideoFile') is not None:
            self.video_file = m.get('VideoFile')
        return self


class GetVideoFieldUrlResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        message: str = None,
        model: Dict[str, Any] = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.message = message
        self.model = model
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.model is not None:
            result['Model'] = self.model
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetVideoFieldUrlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetVideoFieldUrlResponseBody = None,
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
            temp_model = GetVideoFieldUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class IvrCallRequestMenuKeyMap(TeaModel):
    def __init__(
        self,
        code: str = None,
        key: str = None,
        tts_params: str = None,
    ):
        # The voice that corresponds to the key specified by the **MenuKeyMap.N.Key** parameter.
        # 
        # *   If you use a voice notification file, this parameter specifies the voice ID. You can log on to the [Voice Messaging Service console](https://dyvms.console.aliyun.com/overview/home), choose **Voice Messages** > **Voice Notifications**, and then click the **Voice Notification Files** tab to view the voice ID.
        # *   If you use a TTS template, this parameter specifies the template ID. You can log on to the [Voice Messaging Service console](https://dyvms.console.aliyun.com/overview/home), choose **Voice Messages** > **Voice Notifications**, and then click the **TTS Template** tab to view the template ID.
        self.code = code
        # The key that can be pressed by the subscriber.
        self.key = key
        # The variables in the TTS template, in the JSON format.
        # 
        # > 
        # 
        # *   This parameter specifies the substitution relationship of the variables in the TTS template if the value of the **MenuKeyMap.N.Code** parameter is set to the ID of the TTS template.
        # 
        # *   This parameter is required if the value of the **MenuKeyMap.N.Code** parameter is set to the ID of a TTS template that contains variables.
        self.tts_params = tts_params

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.key is not None:
            result['Key'] = self.key
        if self.tts_params is not None:
            result['TtsParams'] = self.tts_params
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('TtsParams') is not None:
            self.tts_params = m.get('TtsParams')
        return self


class IvrCallRequest(TeaModel):
    def __init__(
        self,
        bye_code: str = None,
        bye_tts_params: str = None,
        called_number: str = None,
        called_show_number: str = None,
        menu_key_map: List[IvrCallRequestMenuKeyMap] = None,
        out_id: str = None,
        owner_id: int = None,
        play_times: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        start_code: str = None,
        start_tts_params: str = None,
        timeout: int = None,
    ):
        # The end voice.
        # 
        # *   If you use a voice notification file, this parameter specifies the voice ID. You can log on to the [Voice Messaging Service console](https://dyvms.console.aliyun.com/overview/home), choose **Voice Messages** > **Voice Notifications**, and then click the **Voice Notification Files** tab to view the voice ID.
        # *   If you use a TTS template, this parameter specifies the template ID. You can log on to the [Voice Messaging Service console](https://dyvms.console.aliyun.com/overview/home), choose **Voice Messages** > **Voice Notifications**, and then click the **TTS Template** tab to view the template ID.
        # 
        # > The value of the ByeCode parameter must be of the same type as the value of the StartCode parameter. This means that both parameters must specify voice IDs or TTS template IDs.
        self.bye_code = bye_code
        # The variables in the TTS template, in the JSON format.
        # 
        # > This parameter is required when the ByeCode parameter is set to the ID of a TTS template that contains variables.
        self.bye_tts_params = bye_tts_params
        # The called number.
        # 
        # Only phone numbers in the Chinese mainland are supported. Each request supports only one called number.
        # 
        # This parameter is required.
        self.called_number = called_number
        # The calling number.
        # 
        # The value must be a number you purchased. Each request supports only one calling number. In most cases, a calling number is configured with the maximum number of concurrent requests. New requests fail if the maximum number of concurrent requests is reached. You can log on to the [Voice Messaging Service console](https://dyvms.console.aliyun.com/overview/home) and choose **Real Number Service > Real Number Management** to view the number you purchased.
        # 
        # This parameter is required.
        self.called_show_number = called_show_number
        # The information about the key pressed by the subscriber.
        self.menu_key_map = menu_key_map
        # The ID that is reserved for the caller of the operation. This ID is returned to the caller in a receipt message.
        # 
        # The value is of the STRING type and must be 1 to 15 bytes in length.
        self.out_id = out_id
        self.owner_id = owner_id
        # The number of replay times. Valid values: 1 to 3.
        self.play_times = play_times
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The voice that is played when the call begins.
        # 
        # *   If you use a voice notification file, this parameter specifies the voice ID. You can log on to the [Voice Messaging Service console](https://dyvms.console.aliyun.com/overview/home), choose **Voice Messages** > Voice Notifications, and then click the **Voice Notification Files** tab to view the voice ID.
        # *   If you use a text-to-speech (TTS) template, this parameter specifies the template ID. You can log on to the [Voice Messaging Service console](https://dyvms.console.aliyun.com/overview/home), choose **Voice Messages** > **Voice Notifications**, and then click the **TTS Template** tab to view the template ID.
        # 
        # This parameter is required.
        self.start_code = start_code
        # The variables in the TTS template, in the JSON format.
        # 
        # > This parameter is required when the StartCode parameter is set to the ID of a TTS template that contains variables.
        self.start_tts_params = start_tts_params
        # The timeout period for the subscriber to press a key. Unit: milliseconds.
        self.timeout = timeout

    def validate(self):
        if self.menu_key_map:
            for k in self.menu_key_map:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bye_code is not None:
            result['ByeCode'] = self.bye_code
        if self.bye_tts_params is not None:
            result['ByeTtsParams'] = self.bye_tts_params
        if self.called_number is not None:
            result['CalledNumber'] = self.called_number
        if self.called_show_number is not None:
            result['CalledShowNumber'] = self.called_show_number
        result['MenuKeyMap'] = []
        if self.menu_key_map is not None:
            for k in self.menu_key_map:
                result['MenuKeyMap'].append(k.to_map() if k else None)
        if self.out_id is not None:
            result['OutId'] = self.out_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.play_times is not None:
            result['PlayTimes'] = self.play_times
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.start_code is not None:
            result['StartCode'] = self.start_code
        if self.start_tts_params is not None:
            result['StartTtsParams'] = self.start_tts_params
        if self.timeout is not None:
            result['Timeout'] = self.timeout
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ByeCode') is not None:
            self.bye_code = m.get('ByeCode')
        if m.get('ByeTtsParams') is not None:
            self.bye_tts_params = m.get('ByeTtsParams')
        if m.get('CalledNumber') is not None:
            self.called_number = m.get('CalledNumber')
        if m.get('CalledShowNumber') is not None:
            self.called_show_number = m.get('CalledShowNumber')
        self.menu_key_map = []
        if m.get('MenuKeyMap') is not None:
            for k in m.get('MenuKeyMap'):
                temp_model = IvrCallRequestMenuKeyMap()
                self.menu_key_map.append(temp_model.from_map(k))
        if m.get('OutId') is not None:
            self.out_id = m.get('OutId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PlayTimes') is not None:
            self.play_times = m.get('PlayTimes')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('StartCode') is not None:
            self.start_code = m.get('StartCode')
        if m.get('StartTtsParams') is not None:
            self.start_tts_params = m.get('StartTtsParams')
        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')
        return self


class IvrCallResponseBody(TeaModel):
    def __init__(
        self,
        call_id: str = None,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        # The unique receipt ID of the call.
        # 
        # You can call the [QueryCallDetailByCallId](https://help.aliyun.com/document_detail/393529.html) operation to query the details of the call based on the receipt ID.
        self.call_id = call_id
        # The response code.
        # 
        # *   The value OK indicates that the request was successful.
        # *   For more information about other response codes, see [API error codes](https://help.aliyun.com/document_detail/112502.html).
        self.code = code
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.call_id is not None:
            result['CallId'] = self.call_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallId') is not None:
            self.call_id = m.get('CallId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class IvrCallResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: IvrCallResponseBody = None,
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
            temp_model = IvrCallResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCallTaskRequest(TeaModel):
    def __init__(
        self,
        biz_type: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        status: str = None,
        task_id: str = None,
        task_name: str = None,
        template_name: str = None,
    ):
        # The type of the task template. Valid values:
        # 
        # *   **VMS_VOICE_TTS**: the text-to-speech (TTS) notification template.
        # *   **VMS_VOICE_CODE**: the voice notification template.
        # *   **VMS_TTS**: the voice verification code template.
        self.biz_type = biz_type
        self.owner_id = owner_id
        # The page number. Default value: **1**.
        self.page_number = page_number
        # The number of entries per page. Default value: **10**.
        self.page_size = page_size
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The task state. Valid values:
        # 
        # *   **INIT**: The task is in the initial state.
        # *   **RELEASE**: The task is being parsed.
        # *   **RUNNING**: The task is running.
        # *   **STOP**: The task is suspended.
        # *   **SYSTEM_STOP**: The task is suspended by the system.
        # *   **CANCEL**: The task is canceled.
        # *   **SYSTEM_CANCEL**: The task is canceled by the system.
        # *   **DONE**: The task is complete.
        self.status = status
        # The task ID.
        self.task_id = task_id
        # The task name.
        self.task_name = task_name
        # The template name.
        self.template_name = template_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.status is not None:
            result['Status'] = self.status
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        return self


class ListCallTaskResponseBodyData(TeaModel):
    def __init__(
        self,
        biz_type: str = None,
        complete_time: str = None,
        completed_count: int = None,
        completed_rate: int = None,
        data: str = None,
        data_type: str = None,
        fire_time: str = None,
        id: int = None,
        resource: str = None,
        status: str = None,
        stop_time: str = None,
        task_name: str = None,
        template_code: str = None,
        template_name: str = None,
        total_count: int = None,
    ):
        # The type of the task template. Valid values:
        # 
        # *   **VMS_VOICE_TTS**: the TTS notification template.
        # *   **VMS_VOICE_CODE**: the voice notification template.
        # *   **VMS_TTS**: the voice verification code template.
        self.biz_type = biz_type
        # The time when the task was completed. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.complete_time = complete_time
        # The number of tasks that were complete.
        self.completed_count = completed_count
        # The task progress.
        self.completed_rate = completed_rate
        # This parameter is unavailable.
        self.data = data
        # The type of the called number.
        self.data_type = data_type
        # The time when the scheduled task was started. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.fire_time = fire_time
        # The task ID.
        self.id = id
        # The calling number.
        self.resource = resource
        # The task state. Valid values:
        # 
        # *   **INIT**: The task was in the initial state.
        # *   **RELEASE**: The task was being parsed.
        # *   **RUNNING**: The task was running.
        # *   **STOP**: The task was manually suspended.
        # *   **SYSTEM_STOP**: The task was suspended by the system.
        # *   **CANCEL**: The task was manually canceled.
        # *   **SYSTEM_CANCEL**: The task was canceled by the system.
        # *   **DONE**: The task was complete.
        self.status = status
        # This parameter is unavailable.
        self.stop_time = stop_time
        # The task name.
        self.task_name = task_name
        # The ID of the voice template.
        self.template_code = template_code
        # The template name.
        self.template_name = template_name
        # The total number of called numbers.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.complete_time is not None:
            result['CompleteTime'] = self.complete_time
        if self.completed_count is not None:
            result['CompletedCount'] = self.completed_count
        if self.completed_rate is not None:
            result['CompletedRate'] = self.completed_rate
        if self.data is not None:
            result['Data'] = self.data
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.fire_time is not None:
            result['FireTime'] = self.fire_time
        if self.id is not None:
            result['Id'] = self.id
        if self.resource is not None:
            result['Resource'] = self.resource
        if self.status is not None:
            result['Status'] = self.status
        if self.stop_time is not None:
            result['StopTime'] = self.stop_time
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('CompleteTime') is not None:
            self.complete_time = m.get('CompleteTime')
        if m.get('CompletedCount') is not None:
            self.completed_count = m.get('CompletedCount')
        if m.get('CompletedRate') is not None:
            self.completed_rate = m.get('CompletedRate')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('FireTime') is not None:
            self.fire_time = m.get('FireTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Resource') is not None:
            self.resource = m.get('Resource')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StopTime') is not None:
            self.stop_time = m.get('StopTime')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListCallTaskResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[ListCallTaskResponseBodyData] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total: int = None,
    ):
        # The response code.
        self.code = code
        # The task information.
        self.data = data
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of tasks.
        self.total = total

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
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListCallTaskResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListCallTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListCallTaskResponseBody = None,
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
            temp_model = ListCallTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCallTaskDetailRequest(TeaModel):
    def __init__(
        self,
        called_num: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        status: str = None,
        task_id: int = None,
    ):
        # The called number.
        self.called_num = called_num
        self.owner_id = owner_id
        # The page number. Default value: **1**.
        self.page_number = page_number
        # The number of entries per page. Default value: **10**.
        self.page_size = page_size
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The task state. Valid values:
        # 
        # *   **SUCCESS**: The task is successful.
        # *   **FAIL**: The task fails.
        # *   **INIT**: The task is not started.
        self.status = status
        # The task ID.
        # 
        # This parameter is required.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.called_num is not None:
            result['CalledNum'] = self.called_num
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.status is not None:
            result['Status'] = self.status
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CalledNum') is not None:
            self.called_num = m.get('CalledNum')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class ListCallTaskDetailResponseBodyData(TeaModel):
    def __init__(
        self,
        called_num: str = None,
        caller: str = None,
        duration: int = None,
        id: int = None,
        status: str = None,
    ):
        # The called number.
        self.called_num = called_num
        # The calling number.
        self.caller = caller
        # The call duration. Unit: seconds.
        self.duration = duration
        # This parameter is unavailable.
        self.id = id
        # The task state. Valid values:
        # 
        # *   **SUCCESS**: The task was successful.
        # *   **FAIL**: The task failed.
        # *   **INIT**: The task was not started.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.called_num is not None:
            result['CalledNum'] = self.called_num
        if self.caller is not None:
            result['Caller'] = self.caller
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.id is not None:
            result['Id'] = self.id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CalledNum') is not None:
            self.called_num = m.get('CalledNum')
        if m.get('Caller') is not None:
            self.caller = m.get('Caller')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListCallTaskDetailResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[ListCallTaskDetailResponseBodyData] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total: int = None,
        total_page: int = None,
    ):
        # The response code.
        # 
        # *   The value OK indicates that the request was successful.
        # *   For more information about other response codes, see [API error codes](https://help.aliyun.com/document_detail/112502.html).
        self.code = code
        # The information about the task.
        self.data = data
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of called numbers.
        self.total = total
        # The total number of pages.
        self.total_page = total_page

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
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListCallTaskDetailResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        return self


class ListCallTaskDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListCallTaskDetailResponseBody = None,
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
            temp_model = ListCallTaskDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListHotlineTransferRegisterFileRequest(TeaModel):
    def __init__(
        self,
        hotline_number: str = None,
        owner_id: int = None,
        page_no: int = None,
        page_size: int = None,
        qualification_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The China 400 number.
        # 
        # This parameter is required.
        self.hotline_number = hotline_number
        self.owner_id = owner_id
        # The page number. Default value: **1**.
        self.page_no = page_no
        # The number of entries per page. Valid values: 1 to 10.
        self.page_size = page_size
        # The qualification ID. You can call the [GetHotlineQualificationByOrder](https://help.aliyun.com/document_detail/393548.html) operation to obtain the qualification ID.
        # 
        # This parameter is required.
        self.qualification_id = qualification_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotline_number is not None:
            result['HotlineNumber'] = self.hotline_number
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.qualification_id is not None:
            result['QualificationId'] = self.qualification_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HotlineNumber') is not None:
            self.hotline_number = m.get('HotlineNumber')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('QualificationId') is not None:
            self.qualification_id = m.get('QualificationId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class ListHotlineTransferRegisterFileResponseBodyDataValues(TeaModel):
    def __init__(
        self,
        agree: str = None,
        corp_name: str = None,
        hotline_number: str = None,
        mng_op_identity_card: str = None,
        mng_op_mail: str = None,
        mng_op_mobile: str = None,
        mng_op_name: str = None,
        qualification_id: str = None,
        res_unique_code: int = None,
    ):
        # The authenticity of the commitment.
        self.agree = agree
        # The enterprise name.
        self.corp_name = corp_name
        # The China 400 number.
        self.hotline_number = hotline_number
        # The ID card number of the handler.
        self.mng_op_identity_card = mng_op_identity_card
        # The email address of the handler.
        self.mng_op_mail = mng_op_mail
        # The mobile phone number of the handler.
        self.mng_op_mobile = mng_op_mobile
        # The name of the handler.
        self.mng_op_name = mng_op_name
        # The qualification ID.
        self.qualification_id = qualification_id
        # The unique code of the query operation.
        self.res_unique_code = res_unique_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agree is not None:
            result['Agree'] = self.agree
        if self.corp_name is not None:
            result['CorpName'] = self.corp_name
        if self.hotline_number is not None:
            result['HotlineNumber'] = self.hotline_number
        if self.mng_op_identity_card is not None:
            result['MngOpIdentityCard'] = self.mng_op_identity_card
        if self.mng_op_mail is not None:
            result['MngOpMail'] = self.mng_op_mail
        if self.mng_op_mobile is not None:
            result['MngOpMobile'] = self.mng_op_mobile
        if self.mng_op_name is not None:
            result['MngOpName'] = self.mng_op_name
        if self.qualification_id is not None:
            result['QualificationId'] = self.qualification_id
        if self.res_unique_code is not None:
            result['ResUniqueCode'] = self.res_unique_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Agree') is not None:
            self.agree = m.get('Agree')
        if m.get('CorpName') is not None:
            self.corp_name = m.get('CorpName')
        if m.get('HotlineNumber') is not None:
            self.hotline_number = m.get('HotlineNumber')
        if m.get('MngOpIdentityCard') is not None:
            self.mng_op_identity_card = m.get('MngOpIdentityCard')
        if m.get('MngOpMail') is not None:
            self.mng_op_mail = m.get('MngOpMail')
        if m.get('MngOpMobile') is not None:
            self.mng_op_mobile = m.get('MngOpMobile')
        if m.get('MngOpName') is not None:
            self.mng_op_name = m.get('MngOpName')
        if m.get('QualificationId') is not None:
            self.qualification_id = m.get('QualificationId')
        if m.get('ResUniqueCode') is not None:
            self.res_unique_code = m.get('ResUniqueCode')
        return self


class ListHotlineTransferRegisterFileResponseBodyData(TeaModel):
    def __init__(
        self,
        page_no: int = None,
        page_size: int = None,
        total: int = None,
        values: List[ListHotlineTransferRegisterFileResponseBodyDataValues] = None,
    ):
        # The page number.
        self.page_no = page_no
        # The number of entries per page.
        self.page_size = page_size
        # The total number of entries returned.
        self.total = total
        # The registration file.
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
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        result['Values'] = []
        if self.values is not None:
            for k in self.values:
                result['Values'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        self.values = []
        if m.get('Values') is not None:
            for k in m.get('Values'):
                temp_model = ListHotlineTransferRegisterFileResponseBodyDataValues()
                self.values.append(temp_model.from_map(k))
        return self


class ListHotlineTransferRegisterFileResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListHotlineTransferRegisterFileResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The response code.
        # 
        # *   The value OK indicates that the request was successful.
        # *   For more information about other response codes, see [API error codes](https://help.aliyun.com/document_detail/112502.html).
        self.code = code
        # The response parameters.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ListHotlineTransferRegisterFileResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListHotlineTransferRegisterFileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListHotlineTransferRegisterFileResponseBody = None,
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
            temp_model = ListHotlineTransferRegisterFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PauseVideoFileRequest(TeaModel):
    def __init__(
        self,
        call_id: str = None,
        called_number: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.call_id = call_id
        # This parameter is required.
        self.called_number = called_number
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.call_id is not None:
            result['CallId'] = self.call_id
        if self.called_number is not None:
            result['CalledNumber'] = self.called_number
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallId') is not None:
            self.call_id = m.get('CallId')
        if m.get('CalledNumber') is not None:
            self.called_number = m.get('CalledNumber')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class PauseVideoFileResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: Dict[str, Any] = None,
        message: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.data = data
        self.message = message
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class PauseVideoFileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PauseVideoFileResponseBody = None,
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
            temp_model = PauseVideoFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PlayVideoFileRequest(TeaModel):
    def __init__(
        self,
        call_id: str = None,
        called_number: str = None,
        only_phone: bool = None,
        out_id: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        video_id: str = None,
    ):
        self.call_id = call_id
        self.called_number = called_number
        self.only_phone = only_phone
        self.out_id = out_id
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # This parameter is required.
        self.video_id = video_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.call_id is not None:
            result['CallId'] = self.call_id
        if self.called_number is not None:
            result['CalledNumber'] = self.called_number
        if self.only_phone is not None:
            result['OnlyPhone'] = self.only_phone
        if self.out_id is not None:
            result['OutId'] = self.out_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.video_id is not None:
            result['VideoId'] = self.video_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallId') is not None:
            self.call_id = m.get('CallId')
        if m.get('CalledNumber') is not None:
            self.called_number = m.get('CalledNumber')
        if m.get('OnlyPhone') is not None:
            self.only_phone = m.get('OnlyPhone')
        if m.get('OutId') is not None:
            self.out_id = m.get('OutId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')
        return self


class PlayVideoFileResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        message: str = None,
        model: bool = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.message = message
        self.model = model
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.model is not None:
            result['Model'] = self.model
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class PlayVideoFileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PlayVideoFileResponseBody = None,
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
            temp_model = PlayVideoFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryCallDetailByCallIdRequest(TeaModel):
    def __init__(
        self,
        call_id: str = None,
        owner_id: int = None,
        prod_id: int = None,
        query_date: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The unique ID of the call.
        # 
        # > 
        # 
        # *   The CallId parameter is included in the response parameters of the outbound call operation that you call to initiate a call.
        # 
        # *   The date when the call specified by CallId is started must be the same as the date specified by QueryDate.
        # 
        # *   The value of CallId must match the value of ProdId.
        # 
        # This parameter is required.
        self.call_id = call_id
        self.owner_id = owner_id
        # The service ID. Valid values:
        # 
        # *   **11000000300006**: voice notification. You can call the [SingleCallByVoice](https://help.aliyun.com/document_detail/393517.html) operation to send a voice notification of the voice notification file type to the specified number.
        # *   **11010000138001**: voice verification code. You can call the [SingleCallByTts](https://help.aliyun.com/document_detail/393519.html) operation to send a voice verification code or a text-to-speech (TTS) voice notification to the specified number.
        # *   **11000000300005**: IVR. You can call the [IvrCall](https://help.aliyun.com/document_detail/393521.html) operation to initiate an interactive voice call to the specified number.
        # *   **11000000300009**: Session Initiation Protocol (SIP) call.
        # *   **11030000180001**: intelligent outbound call.
        # 
        # This parameter is required.
        self.prod_id = prod_id
        # The time at which call details are queried. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        # 
        # > The system queries the call records that are generated within 24 hours after the specified point in time. For example, if you specify the time 20:00:01 on November 21, 2022, the system queries the call records that are generated for the specified call ID from 20:00:01 on November 21, 2022, to 20:00:01 on November 22, 2022.
        # 
        # This parameter is required.
        self.query_date = query_date
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.call_id is not None:
            result['CallId'] = self.call_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.prod_id is not None:
            result['ProdId'] = self.prod_id
        if self.query_date is not None:
            result['QueryDate'] = self.query_date
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallId') is not None:
            self.call_id = m.get('CallId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProdId') is not None:
            self.prod_id = m.get('ProdId')
        if m.get('QueryDate') is not None:
            self.query_date = m.get('QueryDate')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class QueryCallDetailByCallIdResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
    ):
        # The response code.
        # 
        # *   The value OK indicates that the request was successful.
        # *   For more information about other response codes, see [API error codes](https://help.aliyun.com/document_detail/112502.html).
        self.code = code
        # The details of the call, in the JSON format.
        # 
        # *   **caller**: the calling number.
        # *   **startDate**: the time when the call was started.
        # *   **stateDesc**: the description of the call state.
        # *   **duration**: the call duration. Unit: seconds. The value **0** indicates that the user was not connected.
        # *   **callerShowNumber**: the calling number displayed to the called party.
        # *   **gmtCreate**: the time when the call request was received.
        # *   **state**: the call state. The call state is returned by the Internet service provider (ISP) in real time. For more information about call states, see [ISP-returned error codes](https://help.aliyun.com/document_detail/55085.html).
        # *   **endDate**: the time when the call was ended.
        # *   **calleeShowNumber**: the number displayed to the called party.
        # *   **callee**: the called number.
        # *   **aRingTime**: the time when Line A started to ring, in the yyyy-MM-dd HH:mm:ss format.
        # *   **aEndTime**: the time when ringing on Line A ended, in the yyyy-MM-dd HH:mm:ss format.
        # *   **bRingTime**: the time when Line B started to ring, in the yyyy-MM-dd HH:mm:ss format.
        # *   **bEndTime**: the time when ringing on Line B ended, in the yyyy-MM-dd HH:mm:ss format.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id

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
        return self


class QueryCallDetailByCallIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryCallDetailByCallIdResponseBody = None,
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
            temp_model = QueryCallDetailByCallIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryCallDetailByTaskIdRequest(TeaModel):
    def __init__(
        self,
        callee: str = None,
        owner_id: int = None,
        query_date: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        task_id: str = None,
    ):
        # The called number. You can view the outbound call records of only one called number.
        # 
        # This parameter is required.
        self.callee = callee
        self.owner_id = owner_id
        # The start time of the outbound robocall task. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        # 
        # This parameter is required.
        self.query_date = query_date
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The unique ID of the outbound robocall task. The task ID is returned after the outbound robocall task is successfully delivered. You can view the task ID on the [Task Management](https://dyvms.console.aliyun.com/job/list) page of the Voice Messaging Service console, or call the **BatchRobotSmartCall** operation to obtain the **task ID**.
        # 
        # This parameter is required.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.callee is not None:
            result['Callee'] = self.callee
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.query_date is not None:
            result['QueryDate'] = self.query_date
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Callee') is not None:
            self.callee = m.get('Callee')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('QueryDate') is not None:
            self.query_date = m.get('QueryDate')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class QueryCallDetailByTaskIdResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
    ):
        # The response code.
        # 
        # *   The value OK indicates that the request was successful.
        # *   For more information about other response codes, see [API error codes](https://help.aliyun.com/document_detail/112502.html).
        self.code = code
        # The call details of the outbound robocall task, in the JSON format.
        # 
        # *   **startDate**: the time when the call was answered.
        # 
        # *   **stateDesc**: the reason why the call was hung up. If the status code of early media was returned, this parameter indicates the reason why the status code of early media was used.
        # 
        # *   **statusCode**: the status code.
        # 
        # *   **EndDate**: the time when the call was ended.
        # 
        # *   **calleeShowNumber**: the calling number displayed to the called party.
        # 
        # *   **callee**: the called number.
        # 
        # *   **duration**: the billing duration.
        # 
        # *   **gmtCreate**: the time when the outbound robocall task was created.
        # 
        # *   **hangupDirection**: the party who hung up.
        # 
        # *   **tags**: the call tags.
        # 
        # *   **dialogCount**: the number of conversation rounds in the call.
        # 
        # *   **sureCount**: the number of times that the robocall task was acknowledged.
        # 
        # *   **denyCount**: the number of times that the robocall task was denied.
        # 
        # *   **rejectCount**: the number of times that the robocall task was rejected.
        # 
        # *   **customCount**: the number of times that the robocall task was customized.
        # 
        # *   **knowledgeCount**: the number of times that the knowledge base was queried.
        # 
        # *   **recordFile**: the download URL of the recording file. The URL is valid only for 48 hours. The recording file must be downloaded in time.
        # 
        # *   **callId**: the call ID.
        # 
        # *   **recordStatus**: indicates whether a recording file was available. Valid values:
        # 
        #     *   1: A recording file was available.
        #     *   2: No recording file was available.
        # 
        # *   **knowledgeCommonCount**: the number of call failures caused by the common issues in the knowledge base.
        # 
        # *   **knowledgeBusinessCount**: the number of call failures caused by the business issues in the knowledge base.
        # 
        # *   **callee**: the called number.
        # 
        # *   **dialogDetail**: the conversation details. The value is a JSON array that contains the following parameters:
        # 
        #     *   **role**: the role who spoke.
        #     *   **content**: the content of the speech.
        #     *   **time**: the start time of the speech.
        # 
        # > The preceding parameters are for reference only. The actually returned parameters prevail.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id

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
        return self


class QueryCallDetailByTaskIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryCallDetailByTaskIdResponseBody = None,
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
            temp_model = QueryCallDetailByTaskIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryCallInPoolTransferConfigRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        phone_number: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.owner_id = owner_id
        # The China 400 number used to transfer the call.
        # 
        # This parameter is required.
        self.phone_number = phone_number
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class QueryCallInPoolTransferConfigResponseBodyDataDetails(TeaModel):
    def __init__(
        self,
        called: str = None,
    ):
        # The number used to transfer the call.
        self.called = called

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.called is not None:
            result['Called'] = self.called
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Called') is not None:
            self.called = m.get('Called')
        return self


class QueryCallInPoolTransferConfigResponseBodyData(TeaModel):
    def __init__(
        self,
        called_route_mode: str = None,
        details: List[QueryCallInPoolTransferConfigResponseBodyDataDetails] = None,
        gmt_create: int = None,
        transfer_timeout: str = None,
    ):
        # The call mode. Valid values:
        # 
        # *   **roundRobin**\
        # *   **random**\
        self.called_route_mode = called_route_mode
        # The details of the response parameters.
        self.details = details
        # The time when the call transfer task was created.
        self.gmt_create = gmt_create
        # The timeout period for transferring the call.
        self.transfer_timeout = transfer_timeout

    def validate(self):
        if self.details:
            for k in self.details:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.called_route_mode is not None:
            result['CalledRouteMode'] = self.called_route_mode
        result['Details'] = []
        if self.details is not None:
            for k in self.details:
                result['Details'].append(k.to_map() if k else None)
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.transfer_timeout is not None:
            result['TransferTimeout'] = self.transfer_timeout
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CalledRouteMode') is not None:
            self.called_route_mode = m.get('CalledRouteMode')
        self.details = []
        if m.get('Details') is not None:
            for k in m.get('Details'):
                temp_model = QueryCallInPoolTransferConfigResponseBodyDataDetails()
                self.details.append(temp_model.from_map(k))
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('TransferTimeout') is not None:
            self.transfer_timeout = m.get('TransferTimeout')
        return self


class QueryCallInPoolTransferConfigResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: QueryCallInPoolTransferConfigResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The response code.
        # 
        # *   The value OK indicates that the request was successful.
        # *   For more information about other response codes, see [API error codes](https://help.aliyun.com/document_detail/112502.html).
        self.code = code
        # The response parameters.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = QueryCallInPoolTransferConfigResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryCallInPoolTransferConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryCallInPoolTransferConfigResponseBody = None,
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
            temp_model = QueryCallInPoolTransferConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryCallInTransferRecordRequest(TeaModel):
    def __init__(
        self,
        call_in_caller: str = None,
        owner_id: int = None,
        page_no: int = None,
        page_size: int = None,
        phone_number: str = None,
        query_date: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The calling number of the inbound call.
        self.call_in_caller = call_in_caller
        self.owner_id = owner_id
        # The page number. Default value: **1**.
        # 
        # This parameter is required.
        self.page_no = page_no
        # The number of entries per page. Valid values: 1 to 10.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The phone number to which a call is transferred.
        # 
        # This parameter is required.
        self.phone_number = phone_number
        # The time at which call transfer records are queried, in the YYYY-MM-DD hh:mm:ss format.
        # 
        # > The query result is all the call transfer records of the specified day.
        # 
        # This parameter is required.
        self.query_date = query_date
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.call_in_caller is not None:
            result['CallInCaller'] = self.call_in_caller
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.query_date is not None:
            result['QueryDate'] = self.query_date
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallInCaller') is not None:
            self.call_in_caller = m.get('CallInCaller')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('QueryDate') is not None:
            self.query_date = m.get('QueryDate')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class QueryCallInTransferRecordResponseBodyDataValues(TeaModel):
    def __init__(
        self,
        call_in_called: str = None,
        call_in_caller: str = None,
        gmt_create: int = None,
        record_url: str = None,
        transfer_called: str = None,
        transfer_caller: str = None,
    ):
        # The called number of the inbound call.
        self.call_in_called = call_in_called
        # The calling number of the inbound call.
        self.call_in_caller = call_in_caller
        # The time when the call was initiated.
        self.gmt_create = gmt_create
        # The recording URL.
        self.record_url = record_url
        # The phone number to which the call was transferred.
        self.transfer_called = transfer_called
        # The calling number that transferred the call.
        self.transfer_caller = transfer_caller

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.call_in_called is not None:
            result['CallInCalled'] = self.call_in_called
        if self.call_in_caller is not None:
            result['CallInCaller'] = self.call_in_caller
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.record_url is not None:
            result['RecordUrl'] = self.record_url
        if self.transfer_called is not None:
            result['TransferCalled'] = self.transfer_called
        if self.transfer_caller is not None:
            result['TransferCaller'] = self.transfer_caller
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallInCalled') is not None:
            self.call_in_called = m.get('CallInCalled')
        if m.get('CallInCaller') is not None:
            self.call_in_caller = m.get('CallInCaller')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('RecordUrl') is not None:
            self.record_url = m.get('RecordUrl')
        if m.get('TransferCalled') is not None:
            self.transfer_called = m.get('TransferCalled')
        if m.get('TransferCaller') is not None:
            self.transfer_caller = m.get('TransferCaller')
        return self


class QueryCallInTransferRecordResponseBodyData(TeaModel):
    def __init__(
        self,
        page_no: int = None,
        page_size: int = None,
        total: int = None,
        values: List[QueryCallInTransferRecordResponseBodyDataValues] = None,
    ):
        # The page number.
        self.page_no = page_no
        # The number of entries per page.
        self.page_size = page_size
        # The total number of entries returned.
        self.total = total
        # The call transfer records.
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
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        result['Values'] = []
        if self.values is not None:
            for k in self.values:
                result['Values'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        self.values = []
        if m.get('Values') is not None:
            for k in m.get('Values'):
                temp_model = QueryCallInTransferRecordResponseBodyDataValues()
                self.values.append(temp_model.from_map(k))
        return self


class QueryCallInTransferRecordResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: QueryCallInTransferRecordResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The response code.
        # 
        # *   The value OK indicates that the request was successful.
        # *   For more information about other response codes, see [API error codes](https://help.aliyun.com/document_detail/112502.html).
        self.code = code
        # The response parameters.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = QueryCallInTransferRecordResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryCallInTransferRecordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryCallInTransferRecordResponseBody = None,
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
            temp_model = QueryCallInTransferRecordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryRobotInfoListRequest(TeaModel):
    def __init__(
        self,
        audit_status: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The review state. Valid values:
        # 
        # *   **CONFIGURABLE**\
        # *   **AUDITING**\
        # *   **AUDITPASS**\
        # *   **AUDITFAIL**\
        self.audit_status = audit_status
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audit_status is not None:
            result['AuditStatus'] = self.audit_status
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuditStatus') is not None:
            self.audit_status = m.get('AuditStatus')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class QueryRobotInfoListResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
    ):
        # The response code.
        # 
        # *   The value OK indicates that the request was successful.
        # *   For more information about other response codes, see [API error codes](https://help.aliyun.com/document_detail/112502.html).
        self.code = code
        # The basic information about the robot, in the JSON format. The basic information contains the following parameters:
        # 
        # *   **id**: the robot ID.
        # *   **robotName**: the robot name.
        # *   **robotType**: the robot type.
        # *   **auditStatus**: the review state.
        # *   **gmtCreate**: the time when the task was created.
        # *   **gmtModified**: the time when the task was modified.
        # *   **partnerId**: the partner ID.
        # *   **asrId**: the ID of the automatic speech recognition (ASR) model.
        # *   **asrType**: the ASR type. Valid values: **Public** and **Private**.
        # *   **remark**: the additional information.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id

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
        return self


class QueryRobotInfoListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryRobotInfoListResponseBody = None,
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
            temp_model = QueryRobotInfoListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryRobotTaskCallDetailRequest(TeaModel):
    def __init__(
        self,
        callee: str = None,
        owner_id: int = None,
        query_date: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        task_id: int = None,
    ):
        # The called number.
        # 
        # This parameter is required.
        self.callee = callee
        self.owner_id = owner_id
        # The timestamp of the time at which the call details you want to query.
        # 
        # This parameter is required.
        self.query_date = query_date
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The unique ID of the robocall task. You can call the [CreateRobotTask](https://help.aliyun.com/document_detail/393531.html) operation to obtain the task ID.
        # 
        # This parameter is required.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.callee is not None:
            result['Callee'] = self.callee
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.query_date is not None:
            result['QueryDate'] = self.query_date
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Callee') is not None:
            self.callee = m.get('Callee')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('QueryDate') is not None:
            self.query_date = m.get('QueryDate')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class QueryRobotTaskCallDetailResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
    ):
        # The response code.
        # 
        # *   The value OK indicates that the request was successful.
        # *   For more information about other response codes, see [API error codes](https://help.aliyun.com/document_detail/112502.html).
        self.code = code
        # The call details of a robocall task, in the JSON format.
        # 
        # *   **taskId**: the unique ID of the robocall task.
        # *   **caller**: the calling number.
        # *   **called**: the called number.
        # *   **duration**: the call duration. Unit: seconds.
        # *   **label**: the label of the called party.
        # *   **dialogCount**: the number of conversation rounds in the call.
        # *   **callResult**: the call result.
        # *   **hangupDirection**: the party who hung up. Valid values: **0**: the robot. **1**: the called party.
        # *   **transferResult**: the result of transferring the call to an agent. Valid values: **1**, **0**, and **3**. The value 1 indicates that the call was transferred to the agent. The value 0 indicates that the call failed to be transferred to the agent. The value 3 indicates that the call was not transferred to the agent.
        # *   **transferNumber**: the phone number of the agent to whom the call was transferred.
        # *   **transferFailReason**: the reason why the call failed to be transferred to the agent.
        # *   **callId**: the unique receipt ID of the call, in the `taskId^bizId` format.
        # *   **recallCurTimes**: the number of recalls.
        # *   **callStartTime**: the start time of the call.
        # *   **callEndTime**: the end time of the call.
        # *   **sureCount**: the number of times that the robocall task was affirmed.
        # *   **denyCount**: the number of times that the robocall task was denied.
        # *   **rejectCount**: the number of times that the robocall task was rejected.
        # *   **customCount**: the number of times that the robocall task was customized.
        # *   **knowledgeCount**: the number of times that the knowledge base was queried.
        # *   **defaultCount**: the default number of calls.
        # *   **knowledgeBusinessCount**: the number of call failures caused by the business issues in the knowledge base.
        # *   **knowledgeCommonCount**: the number of call failures caused by the common issues in the knowledge base.
        # *   **recordStatus**: Indicates whether the call has a recording file. Valid values: **1**: The call has a recording file. **2**: The call does not have a recording file.
        # *   **recordFile**: the download URL of the recording file.
        # *   **dialogDetail**: the dialog details, in a JSON-formatted array. **role**: the object of the speech. **content**: the content of the speech. **speakTime**: the time of the speech.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id

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
        return self


class QueryRobotTaskCallDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryRobotTaskCallDetailResponseBody = None,
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
            temp_model = QueryRobotTaskCallDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryRobotTaskCallListRequest(TeaModel):
    def __init__(
        self,
        call_result: str = None,
        called: str = None,
        dialog_count_from: str = None,
        dialog_count_to: str = None,
        duration_from: str = None,
        duration_to: str = None,
        hangup_direction: str = None,
        owner_id: int = None,
        page_no: int = None,
        page_size: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        task_id: str = None,
    ):
        # The call result. Valid values:
        # 
        # *   **200002**: The line is busy.
        # *   **200005**: The called party cannot be connected.
        # *   **200010**: The phone of the called party is powered off.
        # *   **200011**: The called party is out of service.
        # *   **200012**: The call is lost.
        self.call_result = call_result
        # The called number.
        self.called = called
        # The minimum number of conversation rounds in the call.
        self.dialog_count_from = dialog_count_from
        # The maximum number of conversation rounds in the call.
        self.dialog_count_to = dialog_count_to
        # The minimum call duration.
        self.duration_from = duration_from
        # The maximum call duration.
        self.duration_to = duration_to
        # The party who hangs up. Valid values:
        # 
        # *   **0**: the called party.
        # *   **1**: the robot.
        self.hangup_direction = hangup_direction
        self.owner_id = owner_id
        # The page number.
        self.page_no = page_no
        # The number of entries per page.
        self.page_size = page_size
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The unique ID of the robocall task. You can call the [CreateRobotTask](https://help.aliyun.com/document_detail/393531.html) operation to obtain the task ID.
        # 
        # This parameter is required.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.call_result is not None:
            result['CallResult'] = self.call_result
        if self.called is not None:
            result['Called'] = self.called
        if self.dialog_count_from is not None:
            result['DialogCountFrom'] = self.dialog_count_from
        if self.dialog_count_to is not None:
            result['DialogCountTo'] = self.dialog_count_to
        if self.duration_from is not None:
            result['DurationFrom'] = self.duration_from
        if self.duration_to is not None:
            result['DurationTo'] = self.duration_to
        if self.hangup_direction is not None:
            result['HangupDirection'] = self.hangup_direction
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallResult') is not None:
            self.call_result = m.get('CallResult')
        if m.get('Called') is not None:
            self.called = m.get('Called')
        if m.get('DialogCountFrom') is not None:
            self.dialog_count_from = m.get('DialogCountFrom')
        if m.get('DialogCountTo') is not None:
            self.dialog_count_to = m.get('DialogCountTo')
        if m.get('DurationFrom') is not None:
            self.duration_from = m.get('DurationFrom')
        if m.get('DurationTo') is not None:
            self.duration_to = m.get('DurationTo')
        if m.get('HangupDirection') is not None:
            self.hangup_direction = m.get('HangupDirection')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class QueryRobotTaskCallListResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
    ):
        # The response code.
        # 
        # *   The value OK indicates that the request was successful.
        # *   For more information about other response codes, see [API error codes](https://help.aliyun.com/document_detail/112502.html).
        self.code = code
        # The information about the robocall task, which is a JSON-formatted array.
        # 
        # *   **taskId**: the unique ID of the robocall task.
        # *   **caller**: the calling number.
        # *   **called**: the called number.
        # *   **duration**: the call duration. Unit: seconds.
        # *   **label**: the label of the called party.
        # *   **dialogCount**: the number of conversation rounds in the call.
        # *   **callResult**: the call result.
        # *   **hangupDirection**: the party who hung up. Valid values: **1** and **0**. The value 1 indicates the called party, and the value 0 indicates the robot.
        # *   **transferResult**: the result of transferring the call to an agent. Valid values: **1**, **0**, and **3**. The value 1 indicates that the call was transferred to an agent. The value 0 indicates that the call failed to be transferred to an agent. The value 3 indicates that the call was not transferred to an agent.
        # *   **transferNumber**: the phone number of the agent to whom the call was transferred.
        # *   **transferFailReason**: the reason why the call failed to be transferred to an agent.
        # *   **callId**: the unique receipt ID of the call.
        # *   **recallCurTimes**: the number of recalls.
        # *   **callStartTime**: the start time of the call.
        # *   **callEndTime**: the end time of the call.
        # *   **sureCount**: the number of times that the robocall task was acknowledged.
        # *   **denyCount**: the number of times that the robocall task was denied.
        # *   **rejectCount**: the number of times that the robocall task was rejected.
        # *   **customCount**: the number of times that the robocall task was customized.
        # *   **knowledgeCount**: the number of times that the knowledge base was queried.
        # *   **defaultCount**: the default number of calls.
        # *   **knowledgeBusinessCount**: the number of call failures caused by the business issues in the knowledge base.
        # *   **knowledgeCommonCount**: the number of call failures caused by the common issues in the knowledge base.
        # *   ****\
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id

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
        return self


class QueryRobotTaskCallListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryRobotTaskCallListResponseBody = None,
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
            temp_model = QueryRobotTaskCallListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryRobotTaskDetailRequest(TeaModel):
    def __init__(
        self,
        id: int = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The unique ID of the robocall task. You can call the [CreateRobotTask](~~CreateRobotTask~~) operation to obtain the task ID.
        # 
        # This parameter is required.
        self.id = id
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class QueryRobotTaskDetailResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
    ):
        # The response code.
        # 
        # *   The value OK indicates that the request was successful.
        # *   For more information about other response codes, see [API error codes](https://help.aliyun.com/document_detail/112502.html).
        self.code = code
        # The details of the robocall task, in the JSON format.
        # 
        # *   **Id**: the unique ID of the robocall task.
        # *   **taskName**: the task name.
        # *   **robotId**: the robot ID.
        # *   **robotName**: the robot name.
        # *   **corpName**: the company name.
        # *   **caller**: the number displayed to the called party.
        # *   **numberStatusIdent**: indicates whether number status identification was enabled. Valid values: **true** and **false**. The value true indicates that number status identification was enabled. The value false indicates that number status identification was not enabled.
        # *   **status**: the task state. You can call the [QueryRobotTaskList](~~QueryRobotTaskList~~) operation to obtain the task state from the `status` parameter.
        # *   **scheduleType**: the scheduling type. Valid values: **SINGLE** and **ORDER**. The value SINGLE indicates that the task was started immediately after it was created. The value ORDER indicates that the task was started at a scheduled time.
        # *   **retryType**: indicates whether auto-redial was enabled. Valid values: **1** and **0**. The value 1 indicates that auto-redial was enabled. The value 0 indicates that auto-redial was not enabled.
        # *   **recallStateCodes**: the call state in which redial is required. Valid values: **200010**, **200011**, **200002**, **200012**, and **200005**. The value 200010 indicates that the phone of the called party was powered off. The value 200011 indicates that the number of the called party was out of service. The value 200002 indicates that the line was busy. The value 200012 indicates that the call was lost. The value 200005 indicates that the called party could not be connected.
        # *   **recallTimes**: the number of redial times.
        # *   **recallInterval**: the redial interval. Unit: minutes.
        # *   **createTime**: the time when the task was created, in the yyyy-MM-dd HH:mm:ss format.
        # *   **fireTime**: the time when the task was started, in the yyyy-MM-dd HH:mm:ss format.
        # *   **completeTime**: the time when the task was completed, in the yyyy-MM-dd HH:mm:ss format.
        # *   **filename**: the name of the called number file.
        # *   **ossFilePath**: the path of the called number file.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id

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
        return self


class QueryRobotTaskDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryRobotTaskDetailResponseBody = None,
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
            temp_model = QueryRobotTaskDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryRobotTaskListRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        page_no: int = None,
        page_size: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        status: str = None,
        task_name: str = None,
        time: str = None,
    ):
        self.owner_id = owner_id
        # The page number.
        self.page_no = page_no
        # The number of entries per page.
        self.page_size = page_size
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The task state. Valid values:
        # 
        # *   **INIT**: The task is not started.
        # *   **READY**: The task is ready to start.
        # *   **DISPATCH**: The task is being parsed.
        # *   **EXCUTING**: The task is being executed.
        # *   **MANUAL_STOP**: The task is manually suspended.
        # *   **SYSTEM_STOP**: The task is suspended by the system.
        # *   **ARREARS_STOP**: The task is suspended due to overdue payments.
        # *   **CANCEL**: The task is manually canceled.
        # *   **SYSTEM_CANCEL**: The task is canceled by the system.
        # *   **FINISH**: The task is complete.
        self.status = status
        # The task name.
        self.task_name = task_name
        # The date when the task is created, in the yyyy-MM-dd format.
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.status is not None:
            result['Status'] = self.status
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.time is not None:
            result['Time'] = self.time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        return self


class QueryRobotTaskListResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        message: str = None,
        page_no: str = None,
        page_size: str = None,
        request_id: str = None,
        total_count: str = None,
    ):
        # The response code.
        self.code = code
        # The robocall tasks, in the JSON format.
        # 
        # *   **id**: the unique ID of the robocall task.
        # *   **taskName**: the task name.
        # *   **robotId**: the robot ID.
        # *   **robotName**: the robot name.
        # *   **status**: the task state.
        # *   **scheduleType**: the scheduling type. Valid values: **SINGLE** and **ORDER**. The value SINGLE indicates that the task was started immediately after it was created. The value ORDER indicates that the task was started at a scheduled time.
        # *   **createTime**: the time when the task was created, in the yyyy.MM.dd HH:mm:ss format.
        # *   **completeTime**: the time when the task was completed, in the yyyy.MM.dd HH:mm:ss format.
        # *   **fireTime**: the time when the task was started, in the yyyy.MM.dd HH:mm:ss format.
        # *   **totalCount**: the total number of calls processed.
        # *   **finishCount**: the number of calls completed.
        self.data = data
        # The returned message.
        self.message = message
        # The page number.
        self.page_no = page_no
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of tasks.
        self.total_count = total_count

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
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class QueryRobotTaskListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryRobotTaskListResponseBody = None,
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
            temp_model = QueryRobotTaskListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryRobotv2AllListRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class QueryRobotv2AllListResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
    ):
        # The response code.
        # 
        # *   The value OK indicates that the request was successful.
        # *   For more information about other response codes, see [API error codes](https://help.aliyun.com/document_detail/112502.html).
        self.code = code
        # The information about the robot communication script, in the JSON format.
        # 
        # *   **id**: the ID of the robot communication script.
        # *   **robotName**: the name of the robot communication script.
        # *   **robotType**: the type of the robot communication script.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id

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
        return self


class QueryRobotv2AllListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryRobotv2AllListResponseBody = None,
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
            temp_model = QueryRobotv2AllListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryVideoPlayProgressRequest(TeaModel):
    def __init__(
        self,
        call_id: str = None,
        called_number: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.call_id = call_id
        # This parameter is required.
        self.called_number = called_number
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.call_id is not None:
            result['CallId'] = self.call_id
        if self.called_number is not None:
            result['CalledNumber'] = self.called_number
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallId') is not None:
            self.call_id = m.get('CallId')
        if m.get('CalledNumber') is not None:
            self.called_number = m.get('CalledNumber')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class QueryVideoPlayProgressResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: Dict[str, Any] = None,
        message: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.data = data
        self.message = message
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryVideoPlayProgressResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryVideoPlayProgressResponseBody = None,
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
            temp_model = QueryVideoPlayProgressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryVirtualNumberRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        page_no: int = None,
        page_size: int = None,
        prod_code: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        route_type: int = None,
    ):
        self.owner_id = owner_id
        # The page number.
        self.page_no = page_no
        # The number of entries per page.
        self.page_size = page_size
        # The service name. Default value: **dyvms**.
        self.prod_code = prod_code
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The route type. Valid values:
        # 
        # *   **0**: number location first.
        # *   **1**: random.
        self.route_type = route_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.route_type is not None:
            result['RouteType'] = self.route_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RouteType') is not None:
            self.route_type = m.get('RouteType')
        return self


class QueryVirtualNumberResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        request_id: str = None,
    ):
        # The response code. The value 200 indicates that the request was successful.
        self.code = code
        # The details of the numbers associated with the virtual numbers. The following fields are returned:
        # 
        # *   createTime: the time when the number was activated.
        # *   qualificationCount: the number of qualifications.
        # *   cityCount: the number of cities.
        # *   phoneNumCount: the number of virtual numbers.
        # *   remark: the additional information.
        # *   phoneNum: the virtual number.
        # *   routeType: the route type.
        # *   canCancel: indicates whether the number can be deactivated.
        # *   specCount: the number of Internet service providers (ISPs).
        # *   status: the number state. Valid values: **1**, **0**, and **-1**. The value 1 indicates that the number is valid. The value 0 indicates that the number is invalid. The value -1 indicates that the number was deactivated.
        # *   pageNo: the page number.
        # *   pageSize: the number of entries per page.
        # *   total: the total number of virtual numbers.
        self.data = data
        # The request ID.
        self.request_id = request_id

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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryVirtualNumberResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryVirtualNumberResponseBody = None,
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
            temp_model = QueryVirtualNumberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryVirtualNumberRelationRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        page_no: int = None,
        page_size: int = None,
        phone_num: str = None,
        prod_code: str = None,
        qualification_id: int = None,
        region_name_city: str = None,
        related_num: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        route_type: int = None,
        spec_id: int = None,
    ):
        self.owner_id = owner_id
        # The page number.
        self.page_no = page_no
        # The number of entries per page.
        self.page_size = page_size
        # The virtual number.
        self.phone_num = phone_num
        # The service name. Default value: **dyvms**.
        self.prod_code = prod_code
        # The qualification ID.
        # 
        # You can log on to the [Voice Messaging Service console](https://dyvms.console.aliyun.com/overview/home), choose **Qualifications\\&Communication Scripts > Qualification Management**, and then click **Details** in the Actions column to view the qualification ID.
        self.qualification_id = qualification_id
        # The city to which the virtual number belongs.
        self.region_name_city = region_name_city
        # The real number.
        self.related_num = related_num
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The route type. Valid values:
        # 
        # **0**: number location first. **1**: random.
        self.route_type = route_type
        # The number type. Valid values:
        # 
        # *   **1**: the number provided by a virtual network operator, in the 05710000\\*\\*\\*\\* format.
        # *   **2**: the number provided by an Internet service provider (ISP).
        # *   **3**: a 5-digit phone number that starts with 95.
        self.spec_id = spec_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.phone_num is not None:
            result['PhoneNum'] = self.phone_num
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.qualification_id is not None:
            result['QualificationId'] = self.qualification_id
        if self.region_name_city is not None:
            result['RegionNameCity'] = self.region_name_city
        if self.related_num is not None:
            result['RelatedNum'] = self.related_num
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.route_type is not None:
            result['RouteType'] = self.route_type
        if self.spec_id is not None:
            result['SpecId'] = self.spec_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PhoneNum') is not None:
            self.phone_num = m.get('PhoneNum')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('QualificationId') is not None:
            self.qualification_id = m.get('QualificationId')
        if m.get('RegionNameCity') is not None:
            self.region_name_city = m.get('RegionNameCity')
        if m.get('RelatedNum') is not None:
            self.related_num = m.get('RelatedNum')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RouteType') is not None:
            self.route_type = m.get('RouteType')
        if m.get('SpecId') is not None:
            self.spec_id = m.get('SpecId')
        return self


class QueryVirtualNumberRelationResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        request_id: str = None,
    ):
        # The response code.
        # 
        # *   The value 200 indicates that the request was successful.
        # *   For more information about other response codes, see [API error codes](https://help.aliyun.com/document_detail/112502.html).
        self.code = code
        # The list of associations between virtual numbers and real numbers. The following fields are returned:
        # 
        # *   **relatedNum**: the real number.
        # *   **createTime**: the time when the number was activated.
        # *   **pageNo**: the page number.
        # *   **pageSize**: the number of entries per page.
        # *   **total**: the total number of entries returned.
        self.data = data
        # The request ID.
        self.request_id = request_id

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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryVirtualNumberRelationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryVirtualNumberRelationResponseBody = None,
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
            temp_model = QueryVirtualNumberRelationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryVmsRealNumberCallConnectionRateInfoRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        real_number: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        time_period: str = None,
        virtual_number: str = None,
    ):
        self.owner_id = owner_id
        # 真实号码
        self.real_number = real_number
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # 时间段
        self.time_period = time_period
        # 虚拟号码
        self.virtual_number = virtual_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.real_number is not None:
            result['RealNumber'] = self.real_number
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.time_period is not None:
            result['TimePeriod'] = self.time_period
        if self.virtual_number is not None:
            result['VirtualNumber'] = self.virtual_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RealNumber') is not None:
            self.real_number = m.get('RealNumber')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TimePeriod') is not None:
            self.time_period = m.get('TimePeriod')
        if m.get('VirtualNumber') is not None:
            self.virtual_number = m.get('VirtualNumber')
        return self


class QueryVmsRealNumberCallConnectionRateInfoResponseBodyModel(TeaModel):
    def __init__(
        self,
        call_connection_rate: float = None,
        complete_count: int = None,
        region_id: str = None,
        request_count: int = None,
        resource_id: str = None,
        resource_type: str = None,
        ringing_count: int = None,
        ringing_rate: float = None,
    ):
        # 接通率
        self.call_connection_rate = call_connection_rate
        # 接通数
        self.complete_count = complete_count
        self.region_id = region_id
        # 请求通话数
        self.request_count = request_count
        self.resource_id = resource_id
        # EcsInstance, EcsDisk, EcsImage, EcsSnapshot, EcsSecurityGroup, EcsEip, EcsVpc, EcsVRouter, EcsVSwitch, EcsVRouteTable, EcsAuthImage, EcsAll, SlbLoadbalancer, SlbVm, RdsInstance, RdsAllInstance, KvsInstance, OcsInstance, OdpsInstance
        self.resource_type = resource_type
        # 响铃数
        self.ringing_count = ringing_count
        # 响铃率
        self.ringing_rate = ringing_rate

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.call_connection_rate is not None:
            result['CallConnectionRate'] = self.call_connection_rate
        if self.complete_count is not None:
            result['CompleteCount'] = self.complete_count
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_count is not None:
            result['RequestCount'] = self.request_count
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.ringing_count is not None:
            result['RingingCount'] = self.ringing_count
        if self.ringing_rate is not None:
            result['RingingRate'] = self.ringing_rate
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallConnectionRate') is not None:
            self.call_connection_rate = m.get('CallConnectionRate')
        if m.get('CompleteCount') is not None:
            self.complete_count = m.get('CompleteCount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestCount') is not None:
            self.request_count = m.get('RequestCount')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('RingingCount') is not None:
            self.ringing_count = m.get('RingingCount')
        if m.get('RingingRate') is not None:
            self.ringing_rate = m.get('RingingRate')
        return self


class QueryVmsRealNumberCallConnectionRateInfoResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        message: str = None,
        model: QueryVmsRealNumberCallConnectionRateInfoResponseBodyModel = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.message = message
        self.model = model
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.model:
            self.model.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.model is not None:
            result['Model'] = self.model.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Model') is not None:
            temp_model = QueryVmsRealNumberCallConnectionRateInfoResponseBodyModel()
            self.model = temp_model.from_map(m['Model'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryVmsRealNumberCallConnectionRateInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryVmsRealNumberCallConnectionRateInfoResponseBody = None,
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
            temp_model = QueryVmsRealNumberCallConnectionRateInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryVmsVirtualNumberRelationByPageRequest(TeaModel):
    def __init__(
        self,
        number_city: str = None,
        number_province: str = None,
        owner_id: int = None,
        page_no: int = None,
        page_size: int = None,
        real_number: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        state: int = None,
        virtual_number: str = None,
    ):
        # 号码归属地--城市
        self.number_city = number_city
        # 号码归属地--省
        self.number_province = number_province
        self.owner_id = owner_id
        self.page_no = page_no
        self.page_size = page_size
        # 真实号码
        self.real_number = real_number
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # 状态 1:有效；0:无效；-1:注销
        self.state = state
        # 虚拟号码
        self.virtual_number = virtual_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.number_city is not None:
            result['NumberCity'] = self.number_city
        if self.number_province is not None:
            result['NumberProvince'] = self.number_province
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.real_number is not None:
            result['RealNumber'] = self.real_number
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.state is not None:
            result['State'] = self.state
        if self.virtual_number is not None:
            result['VirtualNumber'] = self.virtual_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NumberCity') is not None:
            self.number_city = m.get('NumberCity')
        if m.get('NumberProvince') is not None:
            self.number_province = m.get('NumberProvince')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RealNumber') is not None:
            self.real_number = m.get('RealNumber')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('VirtualNumber') is not None:
            self.virtual_number = m.get('VirtualNumber')
        return self


class QueryVmsVirtualNumberRelationByPageResponseBodyModelData(TeaModel):
    def __init__(
        self,
        number_city: str = None,
        number_province: str = None,
        real_number: str = None,
        state: int = None,
        virtual_number: str = None,
    ):
        # 号码归属地--城市
        self.number_city = number_city
        # 号码归属地--省
        self.number_province = number_province
        # 真实号码
        self.real_number = real_number
        # 状态 1:有效；0:无效；-1:注销
        self.state = state
        # 虚拟号码
        self.virtual_number = virtual_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.number_city is not None:
            result['NumberCity'] = self.number_city
        if self.number_province is not None:
            result['NumberProvince'] = self.number_province
        if self.real_number is not None:
            result['RealNumber'] = self.real_number
        if self.state is not None:
            result['State'] = self.state
        if self.virtual_number is not None:
            result['VirtualNumber'] = self.virtual_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NumberCity') is not None:
            self.number_city = m.get('NumberCity')
        if m.get('NumberProvince') is not None:
            self.number_province = m.get('NumberProvince')
        if m.get('RealNumber') is not None:
            self.real_number = m.get('RealNumber')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('VirtualNumber') is not None:
            self.virtual_number = m.get('VirtualNumber')
        return self


class QueryVmsVirtualNumberRelationByPageResponseBodyModel(TeaModel):
    def __init__(
        self,
        data: List[QueryVmsVirtualNumberRelationByPageResponseBodyModelData] = None,
        page_no: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.data = data
        self.page_no = page_no
        self.page_size = page_size
        self.total = total

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
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = QueryVmsVirtualNumberRelationByPageResponseBodyModelData()
                self.data.append(temp_model.from_map(k))
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class QueryVmsVirtualNumberRelationByPageResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        message: str = None,
        model: QueryVmsVirtualNumberRelationByPageResponseBodyModel = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.message = message
        self.model = model
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.model:
            self.model.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.model is not None:
            result['Model'] = self.model.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Model') is not None:
            temp_model = QueryVmsVirtualNumberRelationByPageResponseBodyModel()
            self.model = temp_model.from_map(m['Model'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryVmsVirtualNumberRelationByPageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryVmsVirtualNumberRelationByPageResponseBody = None,
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
            temp_model = QueryVmsVirtualNumberRelationByPageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryVoiceFileAuditInfoRequest(TeaModel):
    def __init__(
        self,
        business_type: int = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        voice_codes: str = None,
    ):
        # The type of the voice file. Valid values:
        # 
        # *   **0** (default): the voice notification file.
        # *   **2**: the recording file.
        self.business_type = business_type
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The ID of the voice file. You can log on to the [Voice Messaging Service console](https://dyvms.console.aliyun.com/overview/home), choose **Voice Messages** > **Voice Notifications** or **Voice File Management**, and then click the **Voice Notification Files** tab to view the **voice ID**.
        # 
        # > You can query up to 10 voice files each time. Separate the voice file names with commas (,).
        # 
        # This parameter is required.
        self.voice_codes = voice_codes

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_type is not None:
            result['BusinessType'] = self.business_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.voice_codes is not None:
            result['VoiceCodes'] = self.voice_codes
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('VoiceCodes') is not None:
            self.voice_codes = m.get('VoiceCodes')
        return self


class QueryVoiceFileAuditInfoResponseBodyData(TeaModel):
    def __init__(
        self,
        audit_state: str = None,
        reject_info: str = None,
        voice_code: str = None,
    ):
        # The review state of the voice file. Valid values:
        # 
        # *   **AUDIT_STATE_INIT**: The voice file was under review.
        # *   **AUDIT_STATE_PASS**: The voice file was approved.
        # *   **AUDIT_STATE_NOT_PASS**: The voice file was rejected.
        # *   **AUDIT_STATE_UPLOADING**: The voice file was approved and is being uploaded.
        # *   **AUDIT_STATE_REDOING**: The voice file was being reprocessed.
        # *   **AUDIT_SATE_CANCEL**: The review of the voice file was canceled.
        # *   **AUDIT_PAUSE**: The review of the voice file was suspended.
        # *   **AUDIT_ORDER_FINISHED**: The voice file was approved by the ticket system and was waiting for the review of the Internet service provider (ISP).
        self.audit_state = audit_state
        # The reason why the voice file was rejected.
        self.reject_info = reject_info
        # The code of the voice file.
        self.voice_code = voice_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audit_state is not None:
            result['AuditState'] = self.audit_state
        if self.reject_info is not None:
            result['RejectInfo'] = self.reject_info
        if self.voice_code is not None:
            result['VoiceCode'] = self.voice_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuditState') is not None:
            self.audit_state = m.get('AuditState')
        if m.get('RejectInfo') is not None:
            self.reject_info = m.get('RejectInfo')
        if m.get('VoiceCode') is not None:
            self.voice_code = m.get('VoiceCode')
        return self


class QueryVoiceFileAuditInfoResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[QueryVoiceFileAuditInfoResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
    ):
        # The response code.
        # 
        # The value OK indicates that the request was successful. For more information about other response codes, see [API error codes](https://help.aliyun.com/document_detail/112502.html).
        self.code = code
        # The response parameters.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = QueryVoiceFileAuditInfoResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryVoiceFileAuditInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryVoiceFileAuditInfoResponseBody = None,
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
            temp_model = QueryVoiceFileAuditInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecoverCallInConfigRequest(TeaModel):
    def __init__(
        self,
        number: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The China 400 number that is used to transfer the inbound call.
        # 
        # This parameter is required.
        self.number = number
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.number is not None:
            result['Number'] = self.number
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Number') is not None:
            self.number = m.get('Number')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class RecoverCallInConfigResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
        message: str = None,
        request_id: str = None,
    ):
        # The response code.
        self.code = code
        # Indicates whether the inbound call was resumed. Valid values:
        # 
        # *   true: The inbound call was resumed.
        # *   false: The inbound call failed to be resumed.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id

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
        return self


class RecoverCallInConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RecoverCallInConfigResponseBody = None,
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
            temp_model = RecoverCallInConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResumeVideoFileRequest(TeaModel):
    def __init__(
        self,
        call_id: str = None,
        called_number: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.call_id = call_id
        # This parameter is required.
        self.called_number = called_number
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.call_id is not None:
            result['CallId'] = self.call_id
        if self.called_number is not None:
            result['CalledNumber'] = self.called_number
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallId') is not None:
            self.call_id = m.get('CallId')
        if m.get('CalledNumber') is not None:
            self.called_number = m.get('CalledNumber')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class ResumeVideoFileResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: Dict[str, Any] = None,
        message: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.data = data
        self.message = message
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ResumeVideoFileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ResumeVideoFileResponseBody = None,
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
            temp_model = ResumeVideoFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SeekVideoFileRequest(TeaModel):
    def __init__(
        self,
        call_id: str = None,
        called_number: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        seek_times: int = None,
    ):
        # 呼叫唯一ID
        self.call_id = call_id
        # 被叫号码
        self.called_number = called_number
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # 快进或快退值，负数为快退，单位秒
        self.seek_times = seek_times

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.call_id is not None:
            result['CallId'] = self.call_id
        if self.called_number is not None:
            result['CalledNumber'] = self.called_number
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.seek_times is not None:
            result['SeekTimes'] = self.seek_times
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallId') is not None:
            self.call_id = m.get('CallId')
        if m.get('CalledNumber') is not None:
            self.called_number = m.get('CalledNumber')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SeekTimes') is not None:
            self.seek_times = m.get('SeekTimes')
        return self


class SeekVideoFileResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: Dict[str, Any] = None,
        message: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.data = data
        self.message = message
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SeekVideoFileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SeekVideoFileResponseBody = None,
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
            temp_model = SeekVideoFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendVerificationRequest(TeaModel):
    def __init__(
        self,
        biz_type: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        target: str = None,
        verify_type: str = None,
    ):
        # The business type. Set the value to **CONTACT**.
        # 
        # This parameter is required.
        self.biz_type = biz_type
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The mobile phone number that receives the SMS verification code.
        # 
        # This parameter is required.
        self.target = target
        # The mode of sending the SMS verification code. Set the value to **SMS**.
        # 
        # This parameter is required.
        self.verify_type = verify_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.target is not None:
            result['Target'] = self.target
        if self.verify_type is not None:
            result['VerifyType'] = self.verify_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Target') is not None:
            self.target = m.get('Target')
        if m.get('VerifyType') is not None:
            self.verify_type = m.get('VerifyType')
        return self


class SendVerificationResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
        message: str = None,
        request_id: str = None,
    ):
        # The response code.
        # 
        # *   The value OK indicates that the request was successful.
        # *   For more information about other response codes, see [API error codes](https://help.aliyun.com/document_detail/112502.html).
        self.code = code
        # Indicates whether the verification code was sent successfully.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id

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
        return self


class SendVerificationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SendVerificationResponseBody = None,
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
            temp_model = SendVerificationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetTransferCalleePoolConfigRequestDetails(TeaModel):
    def __init__(
        self,
        called: str = None,
        caller: str = None,
    ):
        # The called number.
        # 
        # This parameter is required.
        self.called = called
        # The calling number.
        self.caller = caller

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.called is not None:
            result['Called'] = self.called
        if self.caller is not None:
            result['Caller'] = self.caller
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Called') is not None:
            self.called = m.get('Called')
        if m.get('Caller') is not None:
            self.caller = m.get('Caller')
        return self


class SetTransferCalleePoolConfigRequest(TeaModel):
    def __init__(
        self,
        called_route_mode: str = None,
        details: List[SetTransferCalleePoolConfigRequestDetails] = None,
        owner_id: int = None,
        phone_number: str = None,
        qualification_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The call mode. Valid values:
        # 
        # *   **roundRobin**\
        # *   **random**\
        # 
        # This parameter is required.
        self.called_route_mode = called_route_mode
        # The information about the phone numbers for transferring the call.
        # 
        # This parameter is required.
        self.details = details
        self.owner_id = owner_id
        # The phone number used for transferring the call.
        # 
        # This parameter is required.
        self.phone_number = phone_number
        # The qualification ID. You can call the [GetHotlineQualificationByOrder](https://help.aliyun.com/document_detail/393548.html) operation to obtain the qualification ID.
        # 
        # This parameter is required.
        self.qualification_id = qualification_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        if self.details:
            for k in self.details:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.called_route_mode is not None:
            result['CalledRouteMode'] = self.called_route_mode
        result['Details'] = []
        if self.details is not None:
            for k in self.details:
                result['Details'].append(k.to_map() if k else None)
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.qualification_id is not None:
            result['QualificationId'] = self.qualification_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CalledRouteMode') is not None:
            self.called_route_mode = m.get('CalledRouteMode')
        self.details = []
        if m.get('Details') is not None:
            for k in m.get('Details'):
                temp_model = SetTransferCalleePoolConfigRequestDetails()
                self.details.append(temp_model.from_map(k))
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('QualificationId') is not None:
            self.qualification_id = m.get('QualificationId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class SetTransferCalleePoolConfigResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
        message: str = None,
        request_id: str = None,
    ):
        # The response code.
        # 
        # *   The value OK indicates that the request was successful.
        # *   For more information about other response codes, see [API error codes](https://help.aliyun.com/document_detail/112502.html).
        self.code = code
        # Indicates whether the phone numbers for transferring the call were configured.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id

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
        return self


class SetTransferCalleePoolConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetTransferCalleePoolConfigResponseBody = None,
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
            temp_model = SetTransferCalleePoolConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SingleCallByTtsRequest(TeaModel):
    def __init__(
        self,
        called_number: str = None,
        called_show_number: str = None,
        out_id: str = None,
        owner_id: int = None,
        play_times: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        speed: int = None,
        tts_code: str = None,
        tts_param: str = None,
        volume: int = None,
    ):
        # The mobile phone number that receives voice notifications.
        # 
        # *   Number format in the Chinese mainland:
        # 
        #     *   Mobile phone number, for example, 159\\*\\*\\*\\*0000.
        #     *   Landline number, for example, 0571\\*\\*\\*\\*5678.
        # 
        # *   Number format outside the Chinese mainland: country code + phone number, for example, 85200\\*\\*\\*\\*00.
        # 
        # > 
        # 
        # *   Each request supports only one called number. For more information, see [How to use voice notifications in the Chinese mainland](https://help.aliyun.com/document_detail/150016.html) or [How to use voice verification codes in regions outside the Chinese mainland](https://help.aliyun.com/document_detail/270044.html).
        # 
        # *   Voice verification codes are sent to a called number at the following frequency: one time per minute, five times per hour, and 20 times per 24 hours.
        # 
        # This parameter is required.
        self.called_number = called_number
        # The number displayed to the called party.
        # 
        # *   You do not need to specify this parameter if you use the text-to-speech (TTS) notification template or voice verification code template for outbound calls in the common mode. For more information, see [FAQ about the common outbound call mode](https://help.aliyun.com/document_detail/172104.html).
        # *   If you use the TTS notification template or voice verification code template for outbound calls in the dedicated mode, you must specify a number you purchased and only one number can be specified. You can log on to the [Voice Messaging Service console](https://dyvms.console.aliyun.com/overview/home) and choose **Voice Numbers** > **Real Number Management** to view the number you purchased.
        self.called_show_number = called_show_number
        # The custom ID that is reserved for the caller of the operation when the request is initiated. This ID is returned to the caller in a receipt message.
        # 
        # The value is of the STRING type and must be 1 to 15 bytes in length.
        self.out_id = out_id
        self.owner_id = owner_id
        # The number of times a voice notification is played back in a call. Valid values: 1 to 3. Default value: 3.
        self.play_times = play_times
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The playback speed. Valid value: -500 to 500.
        self.speed = speed
        # The ID of the approved TTS notification template or voice verification code template.
        # 
        # You can log on to the [Voice Messaging Service console](https://dyvms.console.aliyun.com/overview/home), and choose **Voice Messages** > **Voice Verification Codes** or choose **Voice Messages** > **Voice Notifications** to view the **template ID**.
        # 
        # > The account to which the TTS template belongs must be the same as the account that is used to call the SingleCallByTts operation.
        # 
        # This parameter is required.
        self.tts_code = tts_code
        # The variables in the template, in the JSON format.
        # 
        # > The variables in the template must be less than 250 characters in length. The length of each single variable is not limited. These variables do not support URLs. The variables in the verification code template support only digits and letters.
        self.tts_param = tts_param
        # The playback volume of the voice notification. Valid values: 0 to 100. Default value: 100.
        self.volume = volume

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.called_number is not None:
            result['CalledNumber'] = self.called_number
        if self.called_show_number is not None:
            result['CalledShowNumber'] = self.called_show_number
        if self.out_id is not None:
            result['OutId'] = self.out_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.play_times is not None:
            result['PlayTimes'] = self.play_times
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.speed is not None:
            result['Speed'] = self.speed
        if self.tts_code is not None:
            result['TtsCode'] = self.tts_code
        if self.tts_param is not None:
            result['TtsParam'] = self.tts_param
        if self.volume is not None:
            result['Volume'] = self.volume
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CalledNumber') is not None:
            self.called_number = m.get('CalledNumber')
        if m.get('CalledShowNumber') is not None:
            self.called_show_number = m.get('CalledShowNumber')
        if m.get('OutId') is not None:
            self.out_id = m.get('OutId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PlayTimes') is not None:
            self.play_times = m.get('PlayTimes')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Speed') is not None:
            self.speed = m.get('Speed')
        if m.get('TtsCode') is not None:
            self.tts_code = m.get('TtsCode')
        if m.get('TtsParam') is not None:
            self.tts_param = m.get('TtsParam')
        if m.get('Volume') is not None:
            self.volume = m.get('Volume')
        return self


class SingleCallByTtsResponseBody(TeaModel):
    def __init__(
        self,
        call_id: str = None,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        # The unique receipt ID of the call.
        # 
        # You can call the [QueryCallDetailByCallId](https://help.aliyun.com/document_detail/393529.html) operation to query the details of the call based on the receipt ID.
        self.call_id = call_id
        # The response code.
        # 
        # *   The value OK indicates that the request was successful.
        # *   For more information about other response codes, see [API error codes](https://help.aliyun.com/document_detail/112502.html).
        self.code = code
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.call_id is not None:
            result['CallId'] = self.call_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallId') is not None:
            self.call_id = m.get('CallId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SingleCallByTtsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SingleCallByTtsResponseBody = None,
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
            temp_model = SingleCallByTtsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SingleCallByVideoRequest(TeaModel):
    def __init__(
        self,
        called_number: str = None,
        called_show_number: str = None,
        out_id: str = None,
        owner_id: int = None,
        play_times: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        speed: int = None,
        video_code: str = None,
        voice_code: str = None,
        volume: int = None,
    ):
        # This parameter is required.
        self.called_number = called_number
        self.called_show_number = called_show_number
        self.out_id = out_id
        self.owner_id = owner_id
        self.play_times = play_times
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.speed = speed
        # This parameter is required.
        self.video_code = video_code
        # This parameter is required.
        self.voice_code = voice_code
        self.volume = volume

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.called_number is not None:
            result['CalledNumber'] = self.called_number
        if self.called_show_number is not None:
            result['CalledShowNumber'] = self.called_show_number
        if self.out_id is not None:
            result['OutId'] = self.out_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.play_times is not None:
            result['PlayTimes'] = self.play_times
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.speed is not None:
            result['Speed'] = self.speed
        if self.video_code is not None:
            result['VideoCode'] = self.video_code
        if self.voice_code is not None:
            result['VoiceCode'] = self.voice_code
        if self.volume is not None:
            result['Volume'] = self.volume
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CalledNumber') is not None:
            self.called_number = m.get('CalledNumber')
        if m.get('CalledShowNumber') is not None:
            self.called_show_number = m.get('CalledShowNumber')
        if m.get('OutId') is not None:
            self.out_id = m.get('OutId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PlayTimes') is not None:
            self.play_times = m.get('PlayTimes')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Speed') is not None:
            self.speed = m.get('Speed')
        if m.get('VideoCode') is not None:
            self.video_code = m.get('VideoCode')
        if m.get('VoiceCode') is not None:
            self.voice_code = m.get('VoiceCode')
        if m.get('Volume') is not None:
            self.volume = m.get('Volume')
        return self


class SingleCallByVideoResponseBody(TeaModel):
    def __init__(
        self,
        call_id: str = None,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.call_id = call_id
        self.code = code
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.call_id is not None:
            result['CallId'] = self.call_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallId') is not None:
            self.call_id = m.get('CallId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SingleCallByVideoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SingleCallByVideoResponseBody = None,
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
            temp_model = SingleCallByVideoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SingleCallByVoiceRequest(TeaModel):
    def __init__(
        self,
        called_number: str = None,
        called_show_number: str = None,
        out_id: str = None,
        owner_id: int = None,
        play_times: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        speed: int = None,
        voice_code: str = None,
        volume: int = None,
    ):
        # The number for receiving voice notifications.
        # 
        # Number format:
        # 
        # *   In the Chinese mainland:
        # 
        #     *   Mobile phone number, for example, 159\\*\\*\\*\\*0000.
        #     *   Landline number, for example, 0571\\*\\*\\*\\*5678.
        # 
        # *   Outside the Chinese mainland: country code + phone number, for example, 85200\\*\\*\\*\\*00.
        # 
        # > 
        # 
        # *   You can specify only one called number for a request. For more information, see [How to use voice notifications in the Chinese mainland](https://help.aliyun.com/document_detail/150016.html) or [How to use voice notifications in regions outside the Chinese mainland](https://help.aliyun.com/document_detail/268810.html).
        # 
        # *   Voice notifications are sent to a called number at the following frequency: one time per minute, five times per hour, and 20 times per 24 hours.
        # 
        # This parameter is required.
        self.called_number = called_number
        # The number displayed to the called party.
        # 
        # *   You do not need to specify this parameter if you use a voice notification file that uses the common outbound call mode. For more information, see [FAQ about the common outbound call mode](https://help.aliyun.com/document_detail/172104.html).
        # *   If you use a voice notification file that uses the dedicated outbound call mode, you must specify a number that you purchased. You can specify only one number. You can log on to the [Voice Messaging Service console](https://dyvms.console.aliyun.com/overview/home) and choose **Real Number Service** > **Real Number Management** to view the number that you purchased.
        self.called_show_number = called_show_number
        # The ID reserved for the caller. This ID is returned to the caller in a receipt message.
        # 
        # The value must be of the STRING type and 1 to 15 bytes in length.
        self.out_id = out_id
        self.owner_id = owner_id
        # The number of times the voice notification file is played. Valid values: 1 to 3.
        self.play_times = play_times
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The playback speed of the voice notification file. Valid values: -500 to 500.
        self.speed = speed
        # The voice ID of the voice notification file.
        # 
        # You can log on to the [Voice Messaging Service console](https://dyvms.console.aliyun.com/overview/home), choose **Voice Messages** > **Voice Notifications** or **Voice File Management**, and then click the **Voice Notification Files** tab to view the **voice ID**.
        # 
        # This parameter is required.
        self.voice_code = voice_code
        # The playback volume of the voice notification file. Valid values: 0 to 100. Default value: 100.
        self.volume = volume

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.called_number is not None:
            result['CalledNumber'] = self.called_number
        if self.called_show_number is not None:
            result['CalledShowNumber'] = self.called_show_number
        if self.out_id is not None:
            result['OutId'] = self.out_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.play_times is not None:
            result['PlayTimes'] = self.play_times
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.speed is not None:
            result['Speed'] = self.speed
        if self.voice_code is not None:
            result['VoiceCode'] = self.voice_code
        if self.volume is not None:
            result['Volume'] = self.volume
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CalledNumber') is not None:
            self.called_number = m.get('CalledNumber')
        if m.get('CalledShowNumber') is not None:
            self.called_show_number = m.get('CalledShowNumber')
        if m.get('OutId') is not None:
            self.out_id = m.get('OutId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PlayTimes') is not None:
            self.play_times = m.get('PlayTimes')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Speed') is not None:
            self.speed = m.get('Speed')
        if m.get('VoiceCode') is not None:
            self.voice_code = m.get('VoiceCode')
        if m.get('Volume') is not None:
            self.volume = m.get('Volume')
        return self


class SingleCallByVoiceResponseBody(TeaModel):
    def __init__(
        self,
        call_id: str = None,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        # The unique receipt ID for the call.
        # 
        # You can call the [QueryCallDetailByCallId](https://help.aliyun.com/document_detail/393529.html) operation to query the details of the call.
        self.call_id = call_id
        # The response code.
        # 
        # *   The value OK indicates that the request was successful.****\
        # *   For more information about other response codes, see [API error codes](https://help.aliyun.com/document_detail/112502.html).
        self.code = code
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.call_id is not None:
            result['CallId'] = self.call_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallId') is not None:
            self.call_id = m.get('CallId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SingleCallByVoiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SingleCallByVoiceResponseBody = None,
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
            temp_model = SingleCallByVoiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SkipVideoFileRequest(TeaModel):
    def __init__(
        self,
        call_id: str = None,
        called_number: str = None,
        out_id: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        skip_times: int = None,
    ):
        self.call_id = call_id
        # This parameter is required.
        self.called_number = called_number
        self.out_id = out_id
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # This parameter is required.
        self.skip_times = skip_times

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.call_id is not None:
            result['CallId'] = self.call_id
        if self.called_number is not None:
            result['CalledNumber'] = self.called_number
        if self.out_id is not None:
            result['OutId'] = self.out_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.skip_times is not None:
            result['SkipTimes'] = self.skip_times
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallId') is not None:
            self.call_id = m.get('CallId')
        if m.get('CalledNumber') is not None:
            self.called_number = m.get('CalledNumber')
        if m.get('OutId') is not None:
            self.out_id = m.get('OutId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SkipTimes') is not None:
            self.skip_times = m.get('SkipTimes')
        return self


class SkipVideoFileResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: bool = None,
        message: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.data = data
        self.message = message
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SkipVideoFileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SkipVideoFileResponseBody = None,
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
            temp_model = SkipVideoFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SmartCallRequest(TeaModel):
    def __init__(
        self,
        action_code_break: bool = None,
        action_code_time_break: int = None,
        asr_base_id: str = None,
        asr_model_id: str = None,
        background_file_code: str = None,
        background_speed: int = None,
        background_volume: int = None,
        called_number: str = None,
        called_show_number: str = None,
        dynamic_id: str = None,
        early_media_asr: bool = None,
        enable_itn: bool = None,
        mute_time: int = None,
        noise_threshold: float = None,
        out_id: str = None,
        owner_id: int = None,
        pause_time: int = None,
        record_flag: bool = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        session_timeout: int = None,
        speed: int = None,
        stream_asr: int = None,
        tts_conf: bool = None,
        tts_speed: int = None,
        tts_style: str = None,
        tts_volume: int = None,
        voice_code: str = None,
        voice_code_param: str = None,
        volume: int = None,
    ):
        # Specifies whether the playback of the recording file can be interrupted. Default value: **true**. The default value indicates that the playback of the recording file can be interrupted.
        # 
        # If you set the value of this parameter to false, the playback of the recording file cannot be interrupted even if the value of action_break is set to true.
        # 
        # > The value of action_code_break takes precedence over the value of action_break.
        self.action_code_break = action_code_break
        # The duration that the user keeps speaking. The playback of the recording file is interrupted when this duration is reached. Unit: milliseconds.
        # 
        # If the value of ActionCodeBreak is set to **true** for the recording file and the duration that the user keeps speaking reaches the specified duration, the playback of the recording file is interrupted. If you do not specify ActionCodeTimeBreak or set the value of ActionCodeTimeBreak to 0, the setting of ActionCodeBreak does not take effect.
        self.action_code_time_break = action_code_time_break
        # The ASR base model. Valid values:
        # 
        # *   **customer_service_8k** (default): Chinese Mandarin.
        # *   **dialect_customer_service_8k**: a heavy accent.
        # 
        # > You must specify the ASR model when you call the SmartCall operation. We recommend that you specify either of the AsrModelId and AsrBaseId parameters.
        # 
        # *   If you specify only the AsrModelId parameter, the specified ASR model is used.
        # 
        # *   If you specify only the AsrBaseId parameter, the ASR base model is used.
        # 
        # *   If you specify neither of the two parameters, the default ASR base model is used, that is, the default value customer_service_8k is used for the AsrBaseId parameter.
        # 
        # *   If you specify both parameters, make sure that their values do not conflict with each other.
        self.asr_base_id = asr_base_id
        # The ID of the Automatic Speech Recognition (ASR) model.
        # 
        # You can log on to the [Voice Messaging Service console](https://dyvms.console.aliyun.com/overview/home) and view the ID of the ASR model on the **ASR Model Management** page.
        # 
        # > You must specify the ASR model when you call the SmartCall operation. We recommend that you specify either of the AsrModelId and AsrBaseId parameters.
        # 
        # *   If you specify only the AsrModelId parameter, the specified ASR model is used.
        # 
        # *   If you specify only the AsrBaseId parameter, the specified ASR base model is used.
        # 
        # *   If you specify neither of the two parameters, the default value customer_service_8k is used for the AsrBaseId parameter. This means that the default Mandarin ASR base model is used.
        # 
        # *   If you specify both parameters, make sure that their values do not conflict with each other.
        self.asr_model_id = asr_model_id
        # The ID of the background voice file that is played back when the user talks with the robot.
        # 
        # You can log on to the [Voice Messaging Service console](https://dyvms.console.aliyun.com/overview/home), choose **Voice File Management**, click the **Intelligent Speech Interaction Recording File** tab, and then click **Details** in the Actions column to view the voice ID.
        self.background_file_code = background_file_code
        # This parameter is unavailable.
        self.background_speed = background_speed
        # This parameter is unavailable.
        self.background_volume = background_volume
        # The called number. Only phone numbers in the Chinese mainland are supported.
        # 
        # This parameter is required.
        self.called_number = called_number
        # The number displayed to the called party. The value must be the number you purchased.
        # 
        # You can log on to the [Voice Messaging Service console](https://dyvms.console.aliyun.com/overview/home) and choose **Voice Numbers** > **Real Number Management** to view the number you purchased.
        # 
        # This parameter is required.
        self.called_show_number = called_show_number
        # The dynamic extension ID that is reserved for the caller of the operation. This ID is returned in the callback URL and is used as the development identifier of the customer.
        self.dynamic_id = dynamic_id
        # Specifies whether to enable speech recognition of early media. Valid values:
        # 
        # *   **false** (default): Speech recognition of early media is disabled.
        # *   **true**: Speech recognition of early media is enabled.
        # 
        # > If you set the value of this parameter to **true**, the reason why the call is not answered is recorded.
        self.early_media_asr = early_media_asr
        # Specifies whether to enable Inverse Text Normalization (ITN) during post-processing. Default value: **false**. If you set the value to false, ITN is not enabled during post-processing.
        # 
        # If you set the value to **true**, Chinese numerals are converted into Arabic numerals for output.
        self.enable_itn = enable_itn
        # The silence duration. The system determines the end of the conversation based on the silence duration of the user. Unit: milliseconds. Valid values: 1000 to 20000.****\
        # 
        # > 
        # 
        # *   If you specify a value out of the valid range, the default value **10000** is used.
        # 
        # *   The parameter value can be adjusted during the conversation. The last setting prevails.
        self.mute_time = mute_time
        self.noise_threshold = noise_threshold
        # The ID that is reserved for the caller of the operation. This ID is returned to the caller in a receipt message.
        # 
        # The value is of the STRING type and must be 1 to 15 bytes in length.
        self.out_id = out_id
        self.owner_id = owner_id
        # The pause duration. The system determines the end of a sentence based on the pause duration of the user in the conversation. Unit: milliseconds. Valid values: 300 to 1200.****\
        # 
        # > 
        # 
        # *   If you specify a value out of the valid range, the default value **800** is used.
        # 
        # *   You cannot change the parameter value after specifying it.
        self.pause_time = pause_time
        # Specifies whether to record the conversation. Valid values:
        # 
        # *   **true**: The conversation is recorded.
        # *   **false**: The conversation is not recorded.
        self.record_flag = record_flag
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The maximum call duration. The call is automatically hung up when the maximum call duration is reached. Unit: seconds.
        # 
        # > The maximum call duration is 3,600 seconds.
        self.session_timeout = session_timeout
        # This parameter is unavailable.
        self.speed = speed
        # Specifies whether to enable streaming ASR, which intelligently judges what the user wants to express based on the first few words spoken by the user. Valid values:
        # 
        # *   **0**: Streaming ASR is disabled.
        # *   **1**: Streaming ASR is enabled.
        self.stream_asr = stream_asr
        # Specifies whether to set TTS sound parameters. Valid values:
        # 
        # *   **true**: TTS sound parameters must be set. You must set the **TtsStyle**, **TtsColume**, and **TtsSpeed** parameters to specify a sound style.
        # *   **false**: TTS sound parameters do not need to be set. The values of TTS sound parameters do not take effect even if you set them.
        self.tts_conf = tts_conf
        # The speed of TTS variable playback. Valid values: -200 to 200. Default value: 0.
        self.tts_speed = tts_speed
        # The sound style for TTS variable playback. Default value: **xiaoyun**. For more information about the sound styles, see the **Sound styles** table below.
        self.tts_style = tts_style
        # The volume of TTS variable playback. Valid values: 0 to 100. Default value: 0.
        self.tts_volume = tts_volume
        # The recording file that is played back in the intelligent outbound call.
        # 
        # The file can be an online file, a voice file uploaded from the Voice Messaging Service console, or a text-to-speech (TTS) template that contains variables. You can specify multiple files and a TTS variable together. Separate them with commas (,). The values of the variables in the TTS template are specified by the **VoiceCodeParam** parameter.
        # 
        # *   If you use an online file as the recording file, set the value of **VoiceCode** to the URL of the file that can be accessed over the Internet.
        # *   If you use a voice file uploaded from the Voice Messaging Service console as the recording file, set the value of **VoiceCode** to the voice ID of the file. You can log on to the [Voice Messaging Service console](https://dyvms.console.aliyun.com/overview/home), choose **Voice File Management**, click the **Intelligent Speech Interaction Recording File** tab, and then click **Details** in the Actions column to view the voice ID.
        # *   If you use a TTS template that contains variables as the recording file, set the value of **VoiceCode** to a variable name such as $name$, and also set a value for the variable in the **VoiceCodeParam** parameter.
        # 
        # This parameter is required.
        self.voice_code = voice_code
        # The value of the TTS variable, in the JSON format. This value must match the TTS variable specified by the **VoiceCode** parameter.
        self.voice_code_param = voice_code_param
        # The volume at which the recording file is played. Valid values: -4 to 4. We recommend that you set the value of this parameter to **1**.
        self.volume = volume

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_code_break is not None:
            result['ActionCodeBreak'] = self.action_code_break
        if self.action_code_time_break is not None:
            result['ActionCodeTimeBreak'] = self.action_code_time_break
        if self.asr_base_id is not None:
            result['AsrBaseId'] = self.asr_base_id
        if self.asr_model_id is not None:
            result['AsrModelId'] = self.asr_model_id
        if self.background_file_code is not None:
            result['BackgroundFileCode'] = self.background_file_code
        if self.background_speed is not None:
            result['BackgroundSpeed'] = self.background_speed
        if self.background_volume is not None:
            result['BackgroundVolume'] = self.background_volume
        if self.called_number is not None:
            result['CalledNumber'] = self.called_number
        if self.called_show_number is not None:
            result['CalledShowNumber'] = self.called_show_number
        if self.dynamic_id is not None:
            result['DynamicId'] = self.dynamic_id
        if self.early_media_asr is not None:
            result['EarlyMediaAsr'] = self.early_media_asr
        if self.enable_itn is not None:
            result['EnableITN'] = self.enable_itn
        if self.mute_time is not None:
            result['MuteTime'] = self.mute_time
        if self.noise_threshold is not None:
            result['NoiseThreshold'] = self.noise_threshold
        if self.out_id is not None:
            result['OutId'] = self.out_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.pause_time is not None:
            result['PauseTime'] = self.pause_time
        if self.record_flag is not None:
            result['RecordFlag'] = self.record_flag
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.session_timeout is not None:
            result['SessionTimeout'] = self.session_timeout
        if self.speed is not None:
            result['Speed'] = self.speed
        if self.stream_asr is not None:
            result['StreamAsr'] = self.stream_asr
        if self.tts_conf is not None:
            result['TtsConf'] = self.tts_conf
        if self.tts_speed is not None:
            result['TtsSpeed'] = self.tts_speed
        if self.tts_style is not None:
            result['TtsStyle'] = self.tts_style
        if self.tts_volume is not None:
            result['TtsVolume'] = self.tts_volume
        if self.voice_code is not None:
            result['VoiceCode'] = self.voice_code
        if self.voice_code_param is not None:
            result['VoiceCodeParam'] = self.voice_code_param
        if self.volume is not None:
            result['Volume'] = self.volume
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionCodeBreak') is not None:
            self.action_code_break = m.get('ActionCodeBreak')
        if m.get('ActionCodeTimeBreak') is not None:
            self.action_code_time_break = m.get('ActionCodeTimeBreak')
        if m.get('AsrBaseId') is not None:
            self.asr_base_id = m.get('AsrBaseId')
        if m.get('AsrModelId') is not None:
            self.asr_model_id = m.get('AsrModelId')
        if m.get('BackgroundFileCode') is not None:
            self.background_file_code = m.get('BackgroundFileCode')
        if m.get('BackgroundSpeed') is not None:
            self.background_speed = m.get('BackgroundSpeed')
        if m.get('BackgroundVolume') is not None:
            self.background_volume = m.get('BackgroundVolume')
        if m.get('CalledNumber') is not None:
            self.called_number = m.get('CalledNumber')
        if m.get('CalledShowNumber') is not None:
            self.called_show_number = m.get('CalledShowNumber')
        if m.get('DynamicId') is not None:
            self.dynamic_id = m.get('DynamicId')
        if m.get('EarlyMediaAsr') is not None:
            self.early_media_asr = m.get('EarlyMediaAsr')
        if m.get('EnableITN') is not None:
            self.enable_itn = m.get('EnableITN')
        if m.get('MuteTime') is not None:
            self.mute_time = m.get('MuteTime')
        if m.get('NoiseThreshold') is not None:
            self.noise_threshold = m.get('NoiseThreshold')
        if m.get('OutId') is not None:
            self.out_id = m.get('OutId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PauseTime') is not None:
            self.pause_time = m.get('PauseTime')
        if m.get('RecordFlag') is not None:
            self.record_flag = m.get('RecordFlag')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SessionTimeout') is not None:
            self.session_timeout = m.get('SessionTimeout')
        if m.get('Speed') is not None:
            self.speed = m.get('Speed')
        if m.get('StreamAsr') is not None:
            self.stream_asr = m.get('StreamAsr')
        if m.get('TtsConf') is not None:
            self.tts_conf = m.get('TtsConf')
        if m.get('TtsSpeed') is not None:
            self.tts_speed = m.get('TtsSpeed')
        if m.get('TtsStyle') is not None:
            self.tts_style = m.get('TtsStyle')
        if m.get('TtsVolume') is not None:
            self.tts_volume = m.get('TtsVolume')
        if m.get('VoiceCode') is not None:
            self.voice_code = m.get('VoiceCode')
        if m.get('VoiceCodeParam') is not None:
            self.voice_code_param = m.get('VoiceCodeParam')
        if m.get('Volume') is not None:
            self.volume = m.get('Volume')
        return self


class SmartCallResponseBody(TeaModel):
    def __init__(
        self,
        call_id: str = None,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        # The unique receipt ID for this call.
        # 
        # You can call the [QueryCallDetailByCallId](~~QueryCallDetailByCallId~~) operation to query the details of the call based on the receipt ID.
        self.call_id = call_id
        # The response code.
        # 
        # *   The value OK indicates that the request was successful.
        # *   For more information about other response codes, see [API error codes](https://help.aliyun.com/document_detail/112502.html).
        self.code = code
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.call_id is not None:
            result['CallId'] = self.call_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallId') is not None:
            self.call_id = m.get('CallId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SmartCallResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SmartCallResponseBody = None,
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
            temp_model = SmartCallResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SmartCallOperateRequest(TeaModel):
    def __init__(
        self,
        call_id: str = None,
        command: str = None,
        owner_id: int = None,
        param: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The unique receipt ID of the call. You can call the [SmartCall](https://help.aliyun.com/document_detail/393526.html) operation to obtain the receipt ID.
        # 
        # This parameter is required.
        self.call_id = call_id
        # The action that is initiated to the called number of an outbound robocall.
        # 
        # > Only the value **parallelBridge** is supported. This value indicates that a bridge action is initiated between a called number and an agent of the call center.
        # 
        # This parameter is required.
        self.command = command
        self.owner_id = owner_id
        # The extended field.
        self.param = param
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.call_id is not None:
            result['CallId'] = self.call_id
        if self.command is not None:
            result['Command'] = self.command
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.param is not None:
            result['Param'] = self.param
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallId') is not None:
            self.call_id = m.get('CallId')
        if m.get('Command') is not None:
            self.command = m.get('Command')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Param') is not None:
            self.param = m.get('Param')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class SmartCallOperateResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        status: bool = None,
    ):
        # The response code.
        # 
        # *   The value OK indicates that the request was successful.
        # *   For more information about other response codes, see [API error codes](https://help.aliyun.com/document_detail/112502.html).
        self.code = code
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The action result. Valid values:
        # 
        # *   **true**: The action was successful.
        # *   **false**: The action failed.
        self.status = status

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
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class SmartCallOperateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SmartCallOperateResponseBody = None,
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
            temp_model = SmartCallOperateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartRobotTaskRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        schedule_time: str = None,
        task_id: int = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The time scheduled for starting the robocall task, in the yyyy-MM-dd HH:mm:ss format.
        self.schedule_time = schedule_time
        # The unique ID of the robocall task. You can call the [CreateRobotTask](~~CreateRobotTask~~) operation to obtain the task ID.
        # 
        # This parameter is required.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.schedule_time is not None:
            result['ScheduleTime'] = self.schedule_time
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ScheduleTime') is not None:
            self.schedule_time = m.get('ScheduleTime')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class StartRobotTaskResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
    ):
        # The response code.
        # 
        # *   The value OK indicates that the request was successful.
        # *   For more information about other response codes, see [API error codes](https://help.aliyun.com/document_detail/112502.html).
        self.code = code
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**: The request was successful.
        # *   **false**: The request failed.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id

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
        return self


class StartRobotTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StartRobotTaskResponseBody = None,
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
            temp_model = StartRobotTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopCallInConfigRequest(TeaModel):
    def __init__(
        self,
        number: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The China 400 number from which the inbound call to be stopped is transferred.
        # 
        # This parameter is required.
        self.number = number
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.number is not None:
            result['Number'] = self.number
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Number') is not None:
            self.number = m.get('Number')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class StopCallInConfigResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
        message: str = None,
        request_id: str = None,
    ):
        # The response code.
        self.code = code
        # Indicates whether the inbound call was stopped. Valid values:
        # 
        # *   true: The inbound call was stopped.
        # *   false: The inbound call failed to be stopped.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id

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
        return self


class StopCallInConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StopCallInConfigResponseBody = None,
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
            temp_model = StopCallInConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopRobotTaskRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        task_id: int = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The unique ID of the robocall task. You can call the [CreateRobotTask](~~CreateRobotTask~~) operation to obtain the task ID.
        # 
        # This parameter is required.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class StopRobotTaskResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
    ):
        # The response code.
        # 
        # *   The value OK indicates that the request was successful.
        # *   For more information about other response codes, see [API error codes](https://help.aliyun.com/document_detail/112502.html).
        self.code = code
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**: The request was successful.
        # *   **false**: The request failed.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id

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
        return self


class StopRobotTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StopRobotTaskResponseBody = None,
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
            temp_model = StopRobotTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitHotlineTransferRegisterRequestTransferPhoneNumberInfos(TeaModel):
    def __init__(
        self,
        identity_card: str = None,
        phone_number: str = None,
        phone_number_owner_name: str = None,
    ):
        # The ID card number of the number owner.
        # 
        # This parameter is required.
        self.identity_card = identity_card
        # The China 400 number that you want to submit for registration.
        # 
        # This parameter is required.
        self.phone_number = phone_number
        # The real name or company name of the number owner.
        # 
        # This parameter is required.
        self.phone_number_owner_name = phone_number_owner_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.identity_card is not None:
            result['IdentityCard'] = self.identity_card
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.phone_number_owner_name is not None:
            result['PhoneNumberOwnerName'] = self.phone_number_owner_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IdentityCard') is not None:
            self.identity_card = m.get('IdentityCard')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('PhoneNumberOwnerName') is not None:
            self.phone_number_owner_name = m.get('PhoneNumberOwnerName')
        return self


class SubmitHotlineTransferRegisterRequest(TeaModel):
    def __init__(
        self,
        agreement: str = None,
        hotline_number: str = None,
        operator_identity_card: str = None,
        operator_mail: str = None,
        operator_mail_verify_code: str = None,
        operator_mobile: str = None,
        operator_mobile_verify_code: str = None,
        operator_name: str = None,
        owner_id: int = None,
        qualification_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        transfer_phone_number_infos: List[SubmitHotlineTransferRegisterRequestTransferPhoneNumberInfos] = None,
    ):
        # The authenticity of the commitment. Valid values:
        # 
        # *   **true**: The commitment is authentic.
        # *   **false**: The commitment is not authentic.
        # 
        # This parameter is required.
        self.agreement = agreement
        # The China 400 number.
        # 
        # This parameter is required.
        self.hotline_number = hotline_number
        # The ID card number of the handler.
        # 
        # This parameter is required.
        self.operator_identity_card = operator_identity_card
        # The email address of the handler.
        # 
        # This parameter is required.
        self.operator_mail = operator_mail
        # The verification code that is received by the mailbox of the handler.
        self.operator_mail_verify_code = operator_mail_verify_code
        # The mobile phone number of the handler.
        # 
        # This parameter is required.
        self.operator_mobile = operator_mobile
        # The verification code that is received by the mobile phone of the handler.
        # 
        # This parameter is required.
        self.operator_mobile_verify_code = operator_mobile_verify_code
        # The name of the handler.
        # 
        # This parameter is required.
        self.operator_name = operator_name
        self.owner_id = owner_id
        # The qualification ID. You can call the [GetHotlineQualificationByOrder](https://help.aliyun.com/document_detail/393548.html) operation to obtain the qualification ID.
        # 
        # This parameter is required.
        self.qualification_id = qualification_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The registration information about the China 400 number.
        # 
        # This parameter is required.
        self.transfer_phone_number_infos = transfer_phone_number_infos

    def validate(self):
        if self.transfer_phone_number_infos:
            for k in self.transfer_phone_number_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agreement is not None:
            result['Agreement'] = self.agreement
        if self.hotline_number is not None:
            result['HotlineNumber'] = self.hotline_number
        if self.operator_identity_card is not None:
            result['OperatorIdentityCard'] = self.operator_identity_card
        if self.operator_mail is not None:
            result['OperatorMail'] = self.operator_mail
        if self.operator_mail_verify_code is not None:
            result['OperatorMailVerifyCode'] = self.operator_mail_verify_code
        if self.operator_mobile is not None:
            result['OperatorMobile'] = self.operator_mobile
        if self.operator_mobile_verify_code is not None:
            result['OperatorMobileVerifyCode'] = self.operator_mobile_verify_code
        if self.operator_name is not None:
            result['OperatorName'] = self.operator_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.qualification_id is not None:
            result['QualificationId'] = self.qualification_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        result['TransferPhoneNumberInfos'] = []
        if self.transfer_phone_number_infos is not None:
            for k in self.transfer_phone_number_infos:
                result['TransferPhoneNumberInfos'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Agreement') is not None:
            self.agreement = m.get('Agreement')
        if m.get('HotlineNumber') is not None:
            self.hotline_number = m.get('HotlineNumber')
        if m.get('OperatorIdentityCard') is not None:
            self.operator_identity_card = m.get('OperatorIdentityCard')
        if m.get('OperatorMail') is not None:
            self.operator_mail = m.get('OperatorMail')
        if m.get('OperatorMailVerifyCode') is not None:
            self.operator_mail_verify_code = m.get('OperatorMailVerifyCode')
        if m.get('OperatorMobile') is not None:
            self.operator_mobile = m.get('OperatorMobile')
        if m.get('OperatorMobileVerifyCode') is not None:
            self.operator_mobile_verify_code = m.get('OperatorMobileVerifyCode')
        if m.get('OperatorName') is not None:
            self.operator_name = m.get('OperatorName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('QualificationId') is not None:
            self.qualification_id = m.get('QualificationId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        self.transfer_phone_number_infos = []
        if m.get('TransferPhoneNumberInfos') is not None:
            for k in m.get('TransferPhoneNumberInfos'):
                temp_model = SubmitHotlineTransferRegisterRequestTransferPhoneNumberInfos()
                self.transfer_phone_number_infos.append(temp_model.from_map(k))
        return self


class SubmitHotlineTransferRegisterResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: int = None,
        message: str = None,
        request_id: str = None,
    ):
        # The response code.
        # 
        # *   The value OK indicates that the request was successful.
        # *   For more information about other response codes, see [API error codes](https://help.aliyun.com/document_detail/112502.html).
        self.code = code
        # The registration ID.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id

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
        return self


class SubmitHotlineTransferRegisterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SubmitHotlineTransferRegisterResponseBody = None,
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
            temp_model = SubmitHotlineTransferRegisterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpgradeVideoFileRequest(TeaModel):
    def __init__(
        self,
        call_id: str = None,
        called_number: str = None,
        media_type: str = None,
        out_id: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.call_id = call_id
        # This parameter is required.
        self.called_number = called_number
        self.media_type = media_type
        self.out_id = out_id
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.call_id is not None:
            result['CallId'] = self.call_id
        if self.called_number is not None:
            result['CalledNumber'] = self.called_number
        if self.media_type is not None:
            result['MediaType'] = self.media_type
        if self.out_id is not None:
            result['OutId'] = self.out_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallId') is not None:
            self.call_id = m.get('CallId')
        if m.get('CalledNumber') is not None:
            self.called_number = m.get('CalledNumber')
        if m.get('MediaType') is not None:
            self.media_type = m.get('MediaType')
        if m.get('OutId') is not None:
            self.out_id = m.get('OutId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class UpgradeVideoFileResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: Dict[str, Any] = None,
        message: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.data = data
        self.message = message
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpgradeVideoFileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpgradeVideoFileResponseBody = None,
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
            temp_model = UpgradeVideoFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UploadRobotTaskCalledFileRequest(TeaModel):
    def __init__(
        self,
        called_number: str = None,
        id: int = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        tts_param: str = None,
        tts_param_head: str = None,
    ):
        # The called numbers. Separate multiple called numbers with commas (,).
        # 
        # > After you create a robocall task, you must upload called numbers in batches. You can upload up to 300,000 called numbers for each task.
        # 
        # This parameter is required.
        self.called_number = called_number
        # The unique ID of the robocall task. You can call the [CreateRobotTask](~~CreateRobotTask~~) operation to obtain the ID of the robocall task.
        # 
        # This parameter is required.
        self.id = id
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The values of the variable in the text-to-speech (TTS) template, in the JSON format. The variable values specified by the TtsParam parameter must match the variable names specified by the TtsParamHead parameter.
        # 
        # *   If all the called numbers carry the same variable values, you can set the value of the number field to **all** and upload only one copy of the variable values.
        # *   If only some of the called numbers carry the same variable values, you can set the value of the number field to **all** for these called numbers and set the value of the number field and variable values for other called numbers based on your business requirements. The system preferentially selects the values that you set for the called numbers.
        self.tts_param = tts_param
        # The list of variable names carried in the robocall task, in the JSON format. The TtsParamHead parameter must be used together with the TtsParam parameter.
        self.tts_param_head = tts_param_head

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.called_number is not None:
            result['CalledNumber'] = self.called_number
        if self.id is not None:
            result['Id'] = self.id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.tts_param is not None:
            result['TtsParam'] = self.tts_param
        if self.tts_param_head is not None:
            result['TtsParamHead'] = self.tts_param_head
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CalledNumber') is not None:
            self.called_number = m.get('CalledNumber')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TtsParam') is not None:
            self.tts_param = m.get('TtsParam')
        if m.get('TtsParamHead') is not None:
            self.tts_param_head = m.get('TtsParamHead')
        return self


class UploadRobotTaskCalledFileResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
    ):
        # The response code.
        # 
        # *   The value OK indicates that the request was successful.
        # *   For more information about other response codes, see [API error codes](https://help.aliyun.com/document_detail/112502.html).
        self.code = code
        # The unique ID of the robocall task.
        # 
        # You can call the [QueryRobotTaskDetail](~~QueryRobotTaskDetail~~) operation to query the details of the robocall task based on the task ID.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id

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
        return self


class UploadRobotTaskCalledFileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UploadRobotTaskCalledFileResponseBody = None,
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
            temp_model = UploadRobotTaskCalledFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


