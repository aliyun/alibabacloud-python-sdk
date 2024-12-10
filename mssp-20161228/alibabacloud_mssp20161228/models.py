# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List, Any


class CreateServiceWorkOrderRequest(TeaModel):
    def __init__(
        self,
        creator: str = None,
        customer_id: str = None,
        duration_day: str = None,
        is_attachment: str = None,
        is_work_order_notify: str = None,
        notify_day: str = None,
        notify_id: int = None,
        operate_remark: str = None,
        operate_type: str = None,
        operator: str = None,
        owner_id: str = None,
        start_time: int = None,
        work_order_detail: str = None,
        work_order_name: str = None,
        work_order_source: str = None,
        work_order_status: str = None,
        work_order_type: str = None,
    ):
        # Creator.
        # 
        # This parameter is required.
        self.creator = creator
        # Customer ID.
        # 
        # This parameter is required.
        self.customer_id = customer_id
        # Duration in days.
        # 
        # This parameter is required.
        self.duration_day = duration_day
        # Attachment requirement.
        # 
        # This parameter is required.
        self.is_attachment = is_attachment
        # Whether a reminder is needed.
        # 
        # This parameter is required.
        self.is_work_order_notify = is_work_order_notify
        # Number of days for advance notification.
        self.notify_day = notify_day
        # Notification ID.
        self.notify_id = notify_id
        # Operation remarks.
        # 
        # This parameter is required.
        self.operate_remark = operate_remark
        # Operation type.
        # 
        # This parameter is required.
        self.operate_type = operate_type
        # Operator.
        # 
        # This parameter is required.
        self.operator = operator
        # This parameter is required.
        self.owner_id = owner_id
        # Start time.
        # 
        # This parameter is required.
        self.start_time = start_time
        # Work order details.
        # 
        # This parameter is required.
        self.work_order_detail = work_order_detail
        # Work order name.
        # 
        # This parameter is required.
        self.work_order_name = work_order_name
        # Work order source.
        # 
        # This parameter is required.
        self.work_order_source = work_order_source
        # Work order status.
        # 
        # This parameter is required.
        self.work_order_status = work_order_status
        # Work order type.
        # 
        # This parameter is required.
        self.work_order_type = work_order_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creator is not None:
            result['Creator'] = self.creator
        if self.customer_id is not None:
            result['CustomerId'] = self.customer_id
        if self.duration_day is not None:
            result['DurationDay'] = self.duration_day
        if self.is_attachment is not None:
            result['IsAttachment'] = self.is_attachment
        if self.is_work_order_notify is not None:
            result['IsWorkOrderNotify'] = self.is_work_order_notify
        if self.notify_day is not None:
            result['NotifyDay'] = self.notify_day
        if self.notify_id is not None:
            result['NotifyId'] = self.notify_id
        if self.operate_remark is not None:
            result['OperateRemark'] = self.operate_remark
        if self.operate_type is not None:
            result['OperateType'] = self.operate_type
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.work_order_detail is not None:
            result['WorkOrderDetail'] = self.work_order_detail
        if self.work_order_name is not None:
            result['WorkOrderName'] = self.work_order_name
        if self.work_order_source is not None:
            result['WorkOrderSource'] = self.work_order_source
        if self.work_order_status is not None:
            result['WorkOrderStatus'] = self.work_order_status
        if self.work_order_type is not None:
            result['WorkOrderType'] = self.work_order_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')
        if m.get('CustomerId') is not None:
            self.customer_id = m.get('CustomerId')
        if m.get('DurationDay') is not None:
            self.duration_day = m.get('DurationDay')
        if m.get('IsAttachment') is not None:
            self.is_attachment = m.get('IsAttachment')
        if m.get('IsWorkOrderNotify') is not None:
            self.is_work_order_notify = m.get('IsWorkOrderNotify')
        if m.get('NotifyDay') is not None:
            self.notify_day = m.get('NotifyDay')
        if m.get('NotifyId') is not None:
            self.notify_id = m.get('NotifyId')
        if m.get('OperateRemark') is not None:
            self.operate_remark = m.get('OperateRemark')
        if m.get('OperateType') is not None:
            self.operate_type = m.get('OperateType')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('WorkOrderDetail') is not None:
            self.work_order_detail = m.get('WorkOrderDetail')
        if m.get('WorkOrderName') is not None:
            self.work_order_name = m.get('WorkOrderName')
        if m.get('WorkOrderSource') is not None:
            self.work_order_source = m.get('WorkOrderSource')
        if m.get('WorkOrderStatus') is not None:
            self.work_order_status = m.get('WorkOrderStatus')
        if m.get('WorkOrderType') is not None:
            self.work_order_type = m.get('WorkOrderType')
        return self


class CreateServiceWorkOrderResponseBodyData(TeaModel):
    def __init__(
        self,
        complete_time: int = None,
        create_time: int = None,
        creator: str = None,
        customer_id: str = None,
        end_time: int = None,
        id: int = None,
        owner_id: str = None,
        start_time: int = None,
        work_order_detail: str = None,
        work_order_name: str = None,
        work_order_source: str = None,
        work_order_status: str = None,
        work_order_type: str = None,
    ):
        # Completion time.
        self.complete_time = complete_time
        # Creation time.
        self.create_time = create_time
        # Creator.
        self.creator = creator
        # Customer ID.
        self.customer_id = customer_id
        # End time.
        self.end_time = end_time
        # Primary key.
        self.id = id
        # Owner.
        self.owner_id = owner_id
        # Start time.
        self.start_time = start_time
        # Work order details.
        self.work_order_detail = work_order_detail
        # Work order name.
        self.work_order_name = work_order_name
        # Work order source.
        self.work_order_source = work_order_source
        # Work order status.
        self.work_order_status = work_order_status
        # Work order type.
        self.work_order_type = work_order_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.complete_time is not None:
            result['CompleteTime'] = self.complete_time
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.creator is not None:
            result['Creator'] = self.creator
        if self.customer_id is not None:
            result['CustomerId'] = self.customer_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.id is not None:
            result['Id'] = self.id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.work_order_detail is not None:
            result['WorkOrderDetail'] = self.work_order_detail
        if self.work_order_name is not None:
            result['WorkOrderName'] = self.work_order_name
        if self.work_order_source is not None:
            result['WorkOrderSource'] = self.work_order_source
        if self.work_order_status is not None:
            result['WorkOrderStatus'] = self.work_order_status
        if self.work_order_type is not None:
            result['WorkOrderType'] = self.work_order_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompleteTime') is not None:
            self.complete_time = m.get('CompleteTime')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')
        if m.get('CustomerId') is not None:
            self.customer_id = m.get('CustomerId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('WorkOrderDetail') is not None:
            self.work_order_detail = m.get('WorkOrderDetail')
        if m.get('WorkOrderName') is not None:
            self.work_order_name = m.get('WorkOrderName')
        if m.get('WorkOrderSource') is not None:
            self.work_order_source = m.get('WorkOrderSource')
        if m.get('WorkOrderStatus') is not None:
            self.work_order_status = m.get('WorkOrderStatus')
        if m.get('WorkOrderType') is not None:
            self.work_order_type = m.get('WorkOrderType')
        return self


class CreateServiceWorkOrderResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CreateServiceWorkOrderResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Interface status code.
        self.code = code
        # Data returned by the interface.
        self.data = data
        # HTTP status code.
        self.http_status_code = http_status_code
        # The prompt message of the returned result.
        self.message = message
        # Request ID.
        # 
        # This parameter is required.
        self.request_id = request_id
        # Whether the call was successful.
        # - **true**: The call was successful. - **false**: The call failed.
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
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = CreateServiceWorkOrderResponseBodyData()
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


class CreateServiceWorkOrderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateServiceWorkOrderResponseBody = None,
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
            temp_model = CreateServiceWorkOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisposeServiceWorkOrderRequest(TeaModel):
    def __init__(
        self,
        attachment_name: str = None,
        end_time: int = None,
        forward_owner_id: str = None,
        id: int = None,
        is_attachment: str = None,
        is_work_order_notify: str = None,
        notify_id: int = None,
        operate_remark: str = None,
        operate_type: str = None,
        operator: str = None,
        start_time: int = None,
        upgrade_owner_id: str = None,
        work_order_detail: str = None,
        work_order_name: str = None,
        work_order_status: str = None,
    ):
        # Attachment name.
        self.attachment_name = attachment_name
        # End time.
        self.end_time = end_time
        # Forward to owner.
        self.forward_owner_id = forward_owner_id
        # Work order ID.
        # 
        # This parameter is required.
        self.id = id
        # Attachment requirement.
        self.is_attachment = is_attachment
        # Work order notification.
        self.is_work_order_notify = is_work_order_notify
        # Notification ID.
        self.notify_id = notify_id
        # Operation remarks.
        # 
        # This parameter is required.
        self.operate_remark = operate_remark
        # Processing type.
        # 
        # This parameter is required.
        self.operate_type = operate_type
        # Operator.
        # 
        # This parameter is required.
        self.operator = operator
        # Start time.
        self.start_time = start_time
        # Upgrade owner.
        self.upgrade_owner_id = upgrade_owner_id
        # Work order details.
        self.work_order_detail = work_order_detail
        # Work order name.
        # 
        # This parameter is required.
        self.work_order_name = work_order_name
        # Work order status.
        self.work_order_status = work_order_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attachment_name is not None:
            result['AttachmentName'] = self.attachment_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.forward_owner_id is not None:
            result['ForwardOwnerId'] = self.forward_owner_id
        if self.id is not None:
            result['Id'] = self.id
        if self.is_attachment is not None:
            result['IsAttachment'] = self.is_attachment
        if self.is_work_order_notify is not None:
            result['IsWorkOrderNotify'] = self.is_work_order_notify
        if self.notify_id is not None:
            result['NotifyId'] = self.notify_id
        if self.operate_remark is not None:
            result['OperateRemark'] = self.operate_remark
        if self.operate_type is not None:
            result['OperateType'] = self.operate_type
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.upgrade_owner_id is not None:
            result['UpgradeOwnerId'] = self.upgrade_owner_id
        if self.work_order_detail is not None:
            result['WorkOrderDetail'] = self.work_order_detail
        if self.work_order_name is not None:
            result['WorkOrderName'] = self.work_order_name
        if self.work_order_status is not None:
            result['WorkOrderStatus'] = self.work_order_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttachmentName') is not None:
            self.attachment_name = m.get('AttachmentName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ForwardOwnerId') is not None:
            self.forward_owner_id = m.get('ForwardOwnerId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IsAttachment') is not None:
            self.is_attachment = m.get('IsAttachment')
        if m.get('IsWorkOrderNotify') is not None:
            self.is_work_order_notify = m.get('IsWorkOrderNotify')
        if m.get('NotifyId') is not None:
            self.notify_id = m.get('NotifyId')
        if m.get('OperateRemark') is not None:
            self.operate_remark = m.get('OperateRemark')
        if m.get('OperateType') is not None:
            self.operate_type = m.get('OperateType')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('UpgradeOwnerId') is not None:
            self.upgrade_owner_id = m.get('UpgradeOwnerId')
        if m.get('WorkOrderDetail') is not None:
            self.work_order_detail = m.get('WorkOrderDetail')
        if m.get('WorkOrderName') is not None:
            self.work_order_name = m.get('WorkOrderName')
        if m.get('WorkOrderStatus') is not None:
            self.work_order_status = m.get('WorkOrderStatus')
        return self


class DisposeServiceWorkOrderResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # API response code.
        self.code = code
        # HTTP status code.
        self.http_status_code = http_status_code
        # Prompt message of the returned result.
        self.message = message
        # Request ID.
        # 
        # This parameter is required.
        self.request_id = request_id
        # Whether the call was successful. - **true**: The call was successful. - **false**: The call failed.
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
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DisposeServiceWorkOrderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DisposeServiceWorkOrderResponseBody = None,
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
            temp_model = DisposeServiceWorkOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisposeWorkTaskRequest(TeaModel):
    def __init__(
        self,
        operator: str = None,
        opt_remark: str = None,
        status: int = None,
        task_ids: str = None,
    ):
        # Operator.
        # 
        # This parameter is required.
        self.operator = operator
        # Operation remarks.
        # 
        # This parameter is required.
        self.opt_remark = opt_remark
        # Work order status.
        # 
        # This parameter is required.
        self.status = status
        # Work order ID, multiple IDs separated by commas.
        # 
        # This parameter is required.
        self.task_ids = task_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.opt_remark is not None:
            result['OptRemark'] = self.opt_remark
        if self.status is not None:
            result['Status'] = self.status
        if self.task_ids is not None:
            result['TaskIds'] = self.task_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('OptRemark') is not None:
            self.opt_remark = m.get('OptRemark')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskIds') is not None:
            self.task_ids = m.get('TaskIds')
        return self


class DisposeWorkTaskResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Interface response code.
        self.code = code
        # HTTP status code.
        self.http_status_code = http_status_code
        # Prompt message of the returned result.
        self.message = message
        # Request ID.
        # 
        # This parameter is required.
        self.request_id = request_id
        # Whether the call was successful. - **true**: The call was successful. - **false**: The call failed.
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
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DisposeWorkTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DisposeWorkTaskResponseBody = None,
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
            temp_model = DisposeWorkTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAlarmDetailByIdRequest(TeaModel):
    def __init__(
        self,
        id: int = None,
    ):
        # Primary key ID.
        # 
        # This parameter is required.
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetAlarmDetailByIdResponseBodyDataEventDetails(TeaModel):
    def __init__(
        self,
        name_display: str = None,
        type: str = None,
        value: str = None,
        value_display: str = None,
    ):
        # Alarm event display name.
        self.name_display = name_display
        # Alarm event type.
        self.type = type
        # Path where the alarm event occurred.
        self.value = value
        # Path where the alarm event occurred.
        self.value_display = value_display

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name_display is not None:
            result['NameDisplay'] = self.name_display
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        if self.value_display is not None:
            result['ValueDisplay'] = self.value_display
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NameDisplay') is not None:
            self.name_display = m.get('NameDisplay')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('ValueDisplay') is not None:
            self.value_display = m.get('ValueDisplay')
        return self


class GetAlarmDetailByIdResponseBodyData(TeaModel):
    def __init__(
        self,
        alarm_event_type: str = None,
        alarm_event_type_display: str = None,
        alarm_id: int = None,
        alarm_name: str = None,
        alarm_source: str = None,
        alarm_time: str = None,
        analysis_result: str = None,
        contain_hw_mode: bool = None,
        deal_time: str = None,
        desc: str = None,
        event_details: List[GetAlarmDetailByIdResponseBodyDataEventDetails] = None,
        event_level: str = None,
        id: int = None,
        instance_name: str = None,
        internet_ip: str = None,
        intranet_ip: str = None,
        occurrence_time: str = None,
        owner_id: str = None,
        remark: str = None,
        status: str = None,
        tactic_display_name: str = None,
    ):
        # Alarm event type.
        self.alarm_event_type = alarm_event_type
        # Alarm event type.
        self.alarm_event_type_display = alarm_event_type_display
        # Alarm ID.
        self.alarm_id = alarm_id
        # Alarm name.
        self.alarm_name = alarm_name
        # Alarm source.
        self.alarm_source = alarm_source
        # Latest alarm time.
        self.alarm_time = alarm_time
        # Analysis process.
        self.analysis_result = analysis_result
        # Whether high-protection mode is enabled. true means enabled, false means not enabled.
        self.contain_hw_mode = contain_hw_mode
        # Alarm handling time.
        self.deal_time = deal_time
        # Description.
        self.desc = desc
        # Event details information.
        self.event_details = event_details
        # Alarm level.
        self.event_level = event_level
        # Primary key ID of the work order.
        self.id = id
        # Affected asset.
        self.instance_name = instance_name
        # Public IP.
        self.internet_ip = internet_ip
        # Private IP.
        self.intranet_ip = intranet_ip
        # First occurrence time
        self.occurrence_time = occurrence_time
        # Owner.
        self.owner_id = owner_id
        # Disposal method.
        self.remark = remark
        # Handling status.
        self.status = status
        # ATT&CK tactic name.
        self.tactic_display_name = tactic_display_name

    def validate(self):
        if self.event_details:
            for k in self.event_details:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm_event_type is not None:
            result['AlarmEventType'] = self.alarm_event_type
        if self.alarm_event_type_display is not None:
            result['AlarmEventTypeDisplay'] = self.alarm_event_type_display
        if self.alarm_id is not None:
            result['AlarmId'] = self.alarm_id
        if self.alarm_name is not None:
            result['AlarmName'] = self.alarm_name
        if self.alarm_source is not None:
            result['AlarmSource'] = self.alarm_source
        if self.alarm_time is not None:
            result['AlarmTime'] = self.alarm_time
        if self.analysis_result is not None:
            result['AnalysisResult'] = self.analysis_result
        if self.contain_hw_mode is not None:
            result['ContainHwMode'] = self.contain_hw_mode
        if self.deal_time is not None:
            result['DealTime'] = self.deal_time
        if self.desc is not None:
            result['Desc'] = self.desc
        result['EventDetails'] = []
        if self.event_details is not None:
            for k in self.event_details:
                result['EventDetails'].append(k.to_map() if k else None)
        if self.event_level is not None:
            result['EventLevel'] = self.event_level
        if self.id is not None:
            result['Id'] = self.id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip
        if self.intranet_ip is not None:
            result['IntranetIp'] = self.intranet_ip
        if self.occurrence_time is not None:
            result['OccurrenceTime'] = self.occurrence_time
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.status is not None:
            result['Status'] = self.status
        if self.tactic_display_name is not None:
            result['TacticDisplayName'] = self.tactic_display_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmEventType') is not None:
            self.alarm_event_type = m.get('AlarmEventType')
        if m.get('AlarmEventTypeDisplay') is not None:
            self.alarm_event_type_display = m.get('AlarmEventTypeDisplay')
        if m.get('AlarmId') is not None:
            self.alarm_id = m.get('AlarmId')
        if m.get('AlarmName') is not None:
            self.alarm_name = m.get('AlarmName')
        if m.get('AlarmSource') is not None:
            self.alarm_source = m.get('AlarmSource')
        if m.get('AlarmTime') is not None:
            self.alarm_time = m.get('AlarmTime')
        if m.get('AnalysisResult') is not None:
            self.analysis_result = m.get('AnalysisResult')
        if m.get('ContainHwMode') is not None:
            self.contain_hw_mode = m.get('ContainHwMode')
        if m.get('DealTime') is not None:
            self.deal_time = m.get('DealTime')
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
        self.event_details = []
        if m.get('EventDetails') is not None:
            for k in m.get('EventDetails'):
                temp_model = GetAlarmDetailByIdResponseBodyDataEventDetails()
                self.event_details.append(temp_model.from_map(k))
        if m.get('EventLevel') is not None:
            self.event_level = m.get('EventLevel')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')
        if m.get('IntranetIp') is not None:
            self.intranet_ip = m.get('IntranetIp')
        if m.get('OccurrenceTime') is not None:
            self.occurrence_time = m.get('OccurrenceTime')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TacticDisplayName') is not None:
            self.tactic_display_name = m.get('TacticDisplayName')
        return self


class GetAlarmDetailByIdResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetAlarmDetailByIdResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # API response code.
        self.code = code
        # Data returned by the interface.
        self.data = data
        # HTTP status code.
        self.http_status_code = http_status_code
        # Return message.
        self.message = message
        # Request ID.
        # 
        # This parameter is required.
        self.request_id = request_id
        # Whether the operation was successful: - true: Success. - false: Failure.
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
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetAlarmDetailByIdResponseBodyData()
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


class GetAlarmDetailByIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAlarmDetailByIdResponseBody = None,
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
            temp_model = GetAlarmDetailByIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAttackedAssetDealRequest(TeaModel):
    def __init__(
        self,
        date_type: str = None,
        end_date: int = None,
        start_date: int = None,
        susp_event_source: str = None,
    ):
        # Time filter type, supporting filtering by the last 7 days, the last 30 days, the last half year, or custom time periods.
        # 
        # This parameter is required.
        self.date_type = date_type
        # End time.
        # 
        # This parameter is required.
        self.end_date = end_date
        # Start time.
        # 
        # This parameter is required.
        self.start_date = start_date
        # Source of the alert event.
        self.susp_event_source = susp_event_source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.date_type is not None:
            result['DateType'] = self.date_type
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.susp_event_source is not None:
            result['SuspEventSource'] = self.susp_event_source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DateType') is not None:
            self.date_type = m.get('DateType')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('SuspEventSource') is not None:
            self.susp_event_source = m.get('SuspEventSource')
        return self


class GetAttackedAssetDealResponseBodyDataEcsTrendList(TeaModel):
    def __init__(
        self,
        date: str = None,
        deal_count: int = None,
        find_count: int = None,
    ):
        # Date point.
        self.date = date
        # Number of processed items.
        self.deal_count = deal_count
        # Number of discovered items.
        self.find_count = find_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.date is not None:
            result['Date'] = self.date
        if self.deal_count is not None:
            result['DealCount'] = self.deal_count
        if self.find_count is not None:
            result['FindCount'] = self.find_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Date') is not None:
            self.date = m.get('Date')
        if m.get('DealCount') is not None:
            self.deal_count = m.get('DealCount')
        if m.get('FindCount') is not None:
            self.find_count = m.get('FindCount')
        return self


class GetAttackedAssetDealResponseBodyData(TeaModel):
    def __init__(
        self,
        ecs_trend_list: List[GetAttackedAssetDealResponseBodyDataEcsTrendList] = None,
    ):
        # Collection of attacked asset convergence trends.
        self.ecs_trend_list = ecs_trend_list

    def validate(self):
        if self.ecs_trend_list:
            for k in self.ecs_trend_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['EcsTrendList'] = []
        if self.ecs_trend_list is not None:
            for k in self.ecs_trend_list:
                result['EcsTrendList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ecs_trend_list = []
        if m.get('EcsTrendList') is not None:
            for k in m.get('EcsTrendList'):
                temp_model = GetAttackedAssetDealResponseBodyDataEcsTrendList()
                self.ecs_trend_list.append(temp_model.from_map(k))
        return self


class GetAttackedAssetDealResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetAttackedAssetDealResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Interface return code.
        self.code = code
        # Data query result.
        self.data = data
        # HTTP status code.
        self.http_status_code = http_status_code
        # Return message.
        self.message = message
        # Request ID.
        # 
        # This parameter is required.
        self.request_id = request_id
        # Whether the query was successful.<br />
        # **Enum values:**\
        # * true: Success.
        # * false: Failure.
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
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetAttackedAssetDealResponseBodyData()
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


class GetAttackedAssetDealResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAttackedAssetDealResponseBody = None,
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
            temp_model = GetAttackedAssetDealResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetBaselineSummaryRequest(TeaModel):
    def __init__(
        self,
        date_type: str = None,
        end_date: int = None,
        start_date: int = None,
        susp_event_source: str = None,
    ):
        # Time filter type, supports filtering by the last 7 days, the last 30 days, the last half year, or custom time periods.
        # 
        # This parameter is required.
        self.date_type = date_type
        # End time.
        # 
        # This parameter is required.
        self.end_date = end_date
        # Start time.
        # 
        # This parameter is required.
        self.start_date = start_date
        # Alert event source.
        self.susp_event_source = susp_event_source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.date_type is not None:
            result['DateType'] = self.date_type
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.susp_event_source is not None:
            result['SuspEventSource'] = self.susp_event_source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DateType') is not None:
            self.date_type = m.get('DateType')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('SuspEventSource') is not None:
            self.susp_event_source = m.get('SuspEventSource')
        return self


class GetBaselineSummaryResponseBodyDataTrendDTOList(TeaModel):
    def __init__(
        self,
        date: str = None,
        deal_count: int = None,
        find_count: int = None,
    ):
        # Date point.
        self.date = date
        # Number of processed items.
        self.deal_count = deal_count
        # Number of discovered items.
        self.find_count = find_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.date is not None:
            result['Date'] = self.date
        if self.deal_count is not None:
            result['DealCount'] = self.deal_count
        if self.find_count is not None:
            result['FindCount'] = self.find_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Date') is not None:
            self.date = m.get('Date')
        if m.get('DealCount') is not None:
            self.deal_count = m.get('DealCount')
        if m.get('FindCount') is not None:
            self.find_count = m.get('FindCount')
        return self


class GetBaselineSummaryResponseBodyData(TeaModel):
    def __init__(
        self,
        trend_dtolist: List[GetBaselineSummaryResponseBodyDataTrendDTOList] = None,
    ):
        # Collection of baseline statistical data.
        self.trend_dtolist = trend_dtolist

    def validate(self):
        if self.trend_dtolist:
            for k in self.trend_dtolist:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TrendDTOList'] = []
        if self.trend_dtolist is not None:
            for k in self.trend_dtolist:
                result['TrendDTOList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.trend_dtolist = []
        if m.get('TrendDTOList') is not None:
            for k in m.get('TrendDTOList'):
                temp_model = GetBaselineSummaryResponseBodyDataTrendDTOList()
                self.trend_dtolist.append(temp_model.from_map(k))
        return self


class GetBaselineSummaryResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetBaselineSummaryResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Interface response code.
        self.code = code
        # Data returned by the interface.
        self.data = data
        # HTTP status code.
        self.http_status_code = http_status_code
        # Prompt message for the returned result.
        self.message = message
        # Request ID.
        # 
        # This parameter is required.
        self.request_id = request_id
        # Indicates whether the operation was successful. Values: true: success; false: failure.
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
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetBaselineSummaryResponseBodyData()
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


class GetBaselineSummaryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetBaselineSummaryResponseBody = None,
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
            temp_model = GetBaselineSummaryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetConsoleScoreRequest(TeaModel):
    def __init__(
        self,
        date_type: str = None,
        end_date: int = None,
        start_date: int = None,
        susp_event_source: str = None,
    ):
        # Filter time type, supports filtering by the last 7 days, last 30 days, last half year, or custom. If empty, it represents the last 7 days.
        # 
        # This parameter is required.
        self.date_type = date_type
        # End date.
        # 
        # This parameter is required.
        self.end_date = end_date
        # Start date.
        # 
        # This parameter is required.
        self.start_date = start_date
        # Source of alert events.
        self.susp_event_source = susp_event_source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.date_type is not None:
            result['DateType'] = self.date_type
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.susp_event_source is not None:
            result['SuspEventSource'] = self.susp_event_source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DateType') is not None:
            self.date_type = m.get('DateType')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('SuspEventSource') is not None:
            self.susp_event_source = m.get('SuspEventSource')
        return self


class GetConsoleScoreResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: Any = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Interface response code.
        self.code = code
        # Data returned by the interface.
        self.data = data
        # HTTP status code.
        self.http_status_code = http_status_code
        # Prompt message for the result returned.
        self.message = message
        # Request ID.
        # 
        # This parameter is required.
        self.request_id = request_id
        # Indicates whether the operation was successful. true means success, false means failure.
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
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetConsoleScoreResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetConsoleScoreResponseBody = None,
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
            temp_model = GetConsoleScoreResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDetailByIdRequest(TeaModel):
    def __init__(
        self,
        id: int = None,
    ):
        # Primary key ID.
        # 
        # This parameter is required.
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetDetailByIdResponseBodyDataVulDetails(TeaModel):
    def __init__(
        self,
        cve_id: str = None,
        cvss_score: str = None,
        fix_suggestion: str = None,
        title: str = None,
    ):
        # CVE ID.
        self.cve_id = cve_id
        # The CVSS score of the vulnerability in the Alibaba Cloud vulnerability database.
        self.cvss_score = cvss_score
        # Fix suggestion.
        self.fix_suggestion = fix_suggestion
        # Title of the vulnerability announcement.
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cve_id is not None:
            result['CveId'] = self.cve_id
        if self.cvss_score is not None:
            result['CvssScore'] = self.cvss_score
        if self.fix_suggestion is not None:
            result['FixSuggestion'] = self.fix_suggestion
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CveId') is not None:
            self.cve_id = m.get('CveId')
        if m.get('CvssScore') is not None:
            self.cvss_score = m.get('CvssScore')
        if m.get('FixSuggestion') is not None:
            self.fix_suggestion = m.get('FixSuggestion')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class GetDetailByIdResponseBodyData(TeaModel):
    def __init__(
        self,
        vul_details: List[GetDetailByIdResponseBodyDataVulDetails] = None,
    ):
        # Vulnerability details.
        self.vul_details = vul_details

    def validate(self):
        if self.vul_details:
            for k in self.vul_details:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['VulDetails'] = []
        if self.vul_details is not None:
            for k in self.vul_details:
                result['VulDetails'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.vul_details = []
        if m.get('VulDetails') is not None:
            for k in m.get('VulDetails'):
                temp_model = GetDetailByIdResponseBodyDataVulDetails()
                self.vul_details.append(temp_model.from_map(k))
        return self


class GetDetailByIdResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetDetailByIdResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Interface return code.
        self.code = code
        # Data query result.
        self.data = data
        # HTTP status code.
        self.http_status_code = http_status_code
        # Return message.
        self.message = message
        # Request ID.
        # 
        # This parameter is required.
        self.request_id = request_id
        # Indicates whether the call was successful. Values: - **true**: indicates a successful call. - **false**: indicates a failed call.
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
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetDetailByIdResponseBodyData()
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


class GetDetailByIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDetailByIdResponseBody = None,
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
            temp_model = GetDetailByIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDocumentDownloadUrlRequest(TeaModel):
    def __init__(
        self,
        id: int = None,
    ):
        # Document management ID.
        # 
        # This parameter is required.
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetDocumentDownloadUrlResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # API status code.
        self.code = code
        # OSS file access URL.
        self.data = data
        # HTTP status code.
        self.http_status_code = http_status_code
        # Message of the returned result.
        self.message = message
        # Request ID.
        # 
        # This parameter is required.
        self.request_id = request_id
        # Whether the call was successful: - **true**: The call was successful. - **false**: The call failed.
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
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetDocumentDownloadUrlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDocumentDownloadUrlResponseBody = None,
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
            temp_model = GetDocumentDownloadUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDocumentPageRequest(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        delivered_by: str = None,
        document_name: str = None,
        document_type: str = None,
        page_size: int = None,
        report_type: str = None,
    ):
        # Current page.
        # 
        # This parameter is required.
        self.current_page = current_page
        # Delivered by.
        self.delivered_by = delivered_by
        # Document name.
        self.document_name = document_name
        # Document type.
        self.document_type = document_type
        # Page size.
        # 
        # This parameter is required.
        self.page_size = page_size
        # Report type.
        # 
        # This parameter is required.
        self.report_type = report_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.delivered_by is not None:
            result['DeliveredBy'] = self.delivered_by
        if self.document_name is not None:
            result['DocumentName'] = self.document_name
        if self.document_type is not None:
            result['DocumentType'] = self.document_type
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.report_type is not None:
            result['ReportType'] = self.report_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('DeliveredBy') is not None:
            self.delivered_by = m.get('DeliveredBy')
        if m.get('DocumentName') is not None:
            self.document_name = m.get('DocumentName')
        if m.get('DocumentType') is not None:
            self.document_type = m.get('DocumentType')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ReportType') is not None:
            self.report_type = m.get('ReportType')
        return self


class GetDocumentPageResponseBodyData(TeaModel):
    def __init__(
        self,
        delivered_by: str = None,
        document_name: str = None,
        document_type: str = None,
        id: int = None,
        upload_time: str = None,
    ):
        # Delivered by.
        self.delivered_by = delivered_by
        # Report name.
        self.document_name = document_name
        # Service report type.
        self.document_type = document_type
        # Document primary key ID.
        self.id = id
        # Report generation time.
        self.upload_time = upload_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delivered_by is not None:
            result['DeliveredBy'] = self.delivered_by
        if self.document_name is not None:
            result['DocumentName'] = self.document_name
        if self.document_type is not None:
            result['DocumentType'] = self.document_type
        if self.id is not None:
            result['Id'] = self.id
        if self.upload_time is not None:
            result['UploadTime'] = self.upload_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeliveredBy') is not None:
            self.delivered_by = m.get('DeliveredBy')
        if m.get('DocumentName') is not None:
            self.document_name = m.get('DocumentName')
        if m.get('DocumentType') is not None:
            self.document_type = m.get('DocumentType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('UploadTime') is not None:
            self.upload_time = m.get('UploadTime')
        return self


class GetDocumentPageResponseBodyPageInfo(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The current page number in pagination queries.
        self.current_page = current_page
        # The number of data items displayed per page.
        self.page_size = page_size
        # The total number of data items found.
        self.total_count = total_count

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
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class GetDocumentPageResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[GetDocumentPageResponseBodyData] = None,
        http_status_code: int = None,
        message: str = None,
        page_info: GetDocumentPageResponseBodyPageInfo = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Interface response code.
        self.code = code
        # Response data.
        self.data = data
        # HTTP status code.
        self.http_status_code = http_status_code
        # Prompt message for the response result.
        self.message = message
        # Pagination information.
        self.page_info = page_info
        # Request ID.
        # 
        # This parameter is required.
        self.request_id = request_id
        # Indicates whether the call was successful. - **true**: The call was successful. - **false**: The call failed.
        self.success = success

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()
        if self.page_info:
            self.page_info.validate()

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
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()
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
                temp_model = GetDocumentPageResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageInfo') is not None:
            temp_model = GetDocumentPageResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m['PageInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetDocumentPageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDocumentPageResponseBody = None,
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
            temp_model = GetDocumentPageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDocumentSummaryRequest(TeaModel):
    def __init__(
        self,
        report_type: str = None,
    ):
        # Type of service report.
        self.report_type = report_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.report_type is not None:
            result['ReportType'] = self.report_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReportType') is not None:
            self.report_type = m.get('ReportType')
        return self


class GetDocumentSummaryResponseBodyData(TeaModel):
    def __init__(
        self,
        document_count: int = None,
        frequency: int = None,
    ):
        # Number of documents.
        self.document_count = document_count
        # Number of services or days.
        self.frequency = frequency

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.document_count is not None:
            result['DocumentCount'] = self.document_count
        if self.frequency is not None:
            result['Frequency'] = self.frequency
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DocumentCount') is not None:
            self.document_count = m.get('DocumentCount')
        if m.get('Frequency') is not None:
            self.frequency = m.get('Frequency')
        return self


class GetDocumentSummaryResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetDocumentSummaryResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Interface return code.
        self.code = code
        # Data query result.
        self.data = data
        # HTTP status code.
        self.http_status_code = http_status_code
        # Prompt message for the returned result.
        self.message = message
        # Request ID.
        # 
        # This parameter is required.
        self.request_id = request_id
        # Whether the call was successful. Values:
        # - **true**: Yes.
        # - **false**: No.
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
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetDocumentSummaryResponseBodyData()
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


class GetDocumentSummaryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDocumentSummaryResponseBody = None,
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
            temp_model = GetDocumentSummaryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRecentDocumentRequest(TeaModel):
    def __init__(
        self,
        date_type: str = None,
        end_date: int = None,
        start_date: int = None,
        susp_event_source: str = None,
    ):
        # Filter time type, supports filtering by the last 7 days, the last 30 days, the last half year, or custom time ranges.
        # 
        # This parameter is required.
        self.date_type = date_type
        # End time.
        # 
        # This parameter is required.
        self.end_date = end_date
        # Start time.
        # 
        # This parameter is required.
        self.start_date = start_date
        # Alert event source.
        self.susp_event_source = susp_event_source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.date_type is not None:
            result['DateType'] = self.date_type
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.susp_event_source is not None:
            result['SuspEventSource'] = self.susp_event_source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DateType') is not None:
            self.date_type = m.get('DateType')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('SuspEventSource') is not None:
            self.susp_event_source = m.get('SuspEventSource')
        return self


class GetRecentDocumentResponseBodyData(TeaModel):
    def __init__(
        self,
        id: int = None,
        name: str = None,
        upload_time: str = None,
    ):
        # Primary key ID.
        self.id = id
        # Document name
        self.name = name
        # Upload time.
        self.upload_time = upload_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.upload_time is not None:
            result['UploadTime'] = self.upload_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('UploadTime') is not None:
            self.upload_time = m.get('UploadTime')
        return self


class GetRecentDocumentResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[GetRecentDocumentResponseBodyData] = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Interface response code.
        self.code = code
        # Data returned by the interface.
        self.data = data
        # HTTP status code.
        self.http_status_code = http_status_code
        # Response message.
        self.message = message
        # Request ID.
        # 
        # This parameter is required.
        self.request_id = request_id
        # Whether the call was successful. - **true**: The call was successful. - **false**: The call failed.
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
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetRecentDocumentResponseBodyData()
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


class GetRecentDocumentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetRecentDocumentResponseBody = None,
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
            temp_model = GetRecentDocumentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSafetyCoverRequest(TeaModel):
    def __init__(
        self,
        date_type: str = None,
        end_date: int = None,
        start_date: int = None,
        susp_event_source: str = None,
    ):
        # Filter time type, supports filtering by the last 7 days, the last 30 days, the last half year, or custom time periods.
        # 
        # This parameter is required.
        self.date_type = date_type
        # End time.
        # 
        # This parameter is required.
        self.end_date = end_date
        # Start time.
        # 
        # This parameter is required.
        self.start_date = start_date
        # Alert event source.
        self.susp_event_source = susp_event_source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.date_type is not None:
            result['DateType'] = self.date_type
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.susp_event_source is not None:
            result['SuspEventSource'] = self.susp_event_source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DateType') is not None:
            self.date_type = m.get('DateType')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('SuspEventSource') is not None:
            self.susp_event_source = m.get('SuspEventSource')
        return self


class GetSafetyCoverResponseBodyDataCfwProtection(TeaModel):
    def __init__(
        self,
        no_protection_count: int = None,
        protection_count: int = None,
        protection_growth_rate: str = None,
        protection_rate: str = None,
        total_count: int = None,
    ):
        # Number of unprotected items.
        self.no_protection_count = no_protection_count
        # Number of protected items.
        self.protection_count = protection_count
        # Year-over-year protection rate.
        self.protection_growth_rate = protection_growth_rate
        # Protection rate.
        self.protection_rate = protection_rate
        # Total quantity.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.no_protection_count is not None:
            result['NoProtectionCount'] = self.no_protection_count
        if self.protection_count is not None:
            result['ProtectionCount'] = self.protection_count
        if self.protection_growth_rate is not None:
            result['ProtectionGrowthRate'] = self.protection_growth_rate
        if self.protection_rate is not None:
            result['ProtectionRate'] = self.protection_rate
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NoProtectionCount') is not None:
            self.no_protection_count = m.get('NoProtectionCount')
        if m.get('ProtectionCount') is not None:
            self.protection_count = m.get('ProtectionCount')
        if m.get('ProtectionGrowthRate') is not None:
            self.protection_growth_rate = m.get('ProtectionGrowthRate')
        if m.get('ProtectionRate') is not None:
            self.protection_rate = m.get('ProtectionRate')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class GetSafetyCoverResponseBodyDataEcsProtection(TeaModel):
    def __init__(
        self,
        no_protection_count: int = None,
        protection_count: int = None,
        protection_growth_rate: str = None,
        protection_rate: str = None,
        total_count: int = None,
    ):
        # Number of unprotected items.
        self.no_protection_count = no_protection_count
        # Number of protected items.
        self.protection_count = protection_count
        # Year-over-year growth in protection rate.
        self.protection_growth_rate = protection_growth_rate
        # Protection rate.
        self.protection_rate = protection_rate
        # Total number of items.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.no_protection_count is not None:
            result['NoProtectionCount'] = self.no_protection_count
        if self.protection_count is not None:
            result['ProtectionCount'] = self.protection_count
        if self.protection_growth_rate is not None:
            result['ProtectionGrowthRate'] = self.protection_growth_rate
        if self.protection_rate is not None:
            result['ProtectionRate'] = self.protection_rate
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NoProtectionCount') is not None:
            self.no_protection_count = m.get('NoProtectionCount')
        if m.get('ProtectionCount') is not None:
            self.protection_count = m.get('ProtectionCount')
        if m.get('ProtectionGrowthRate') is not None:
            self.protection_growth_rate = m.get('ProtectionGrowthRate')
        if m.get('ProtectionRate') is not None:
            self.protection_rate = m.get('ProtectionRate')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class GetSafetyCoverResponseBodyDataWafProtection(TeaModel):
    def __init__(
        self,
        no_protection_count: int = None,
        protection_count: int = None,
        protection_growth_rate: str = None,
        protection_rate: str = None,
        total_count: int = None,
    ):
        # Number of unprotected items.
        self.no_protection_count = no_protection_count
        # Number of protected items.
        self.protection_count = protection_count
        # Year-over-year growth in protection rate.
        self.protection_growth_rate = protection_growth_rate
        # Protection rate.
        self.protection_rate = protection_rate
        # Total number of items.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.no_protection_count is not None:
            result['NoProtectionCount'] = self.no_protection_count
        if self.protection_count is not None:
            result['ProtectionCount'] = self.protection_count
        if self.protection_growth_rate is not None:
            result['ProtectionGrowthRate'] = self.protection_growth_rate
        if self.protection_rate is not None:
            result['ProtectionRate'] = self.protection_rate
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NoProtectionCount') is not None:
            self.no_protection_count = m.get('NoProtectionCount')
        if m.get('ProtectionCount') is not None:
            self.protection_count = m.get('ProtectionCount')
        if m.get('ProtectionGrowthRate') is not None:
            self.protection_growth_rate = m.get('ProtectionGrowthRate')
        if m.get('ProtectionRate') is not None:
            self.protection_rate = m.get('ProtectionRate')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class GetSafetyCoverResponseBodyData(TeaModel):
    def __init__(
        self,
        cfw_protection: GetSafetyCoverResponseBodyDataCfwProtection = None,
        ecs_protection: GetSafetyCoverResponseBodyDataEcsProtection = None,
        waf_protection: GetSafetyCoverResponseBodyDataWafProtection = None,
    ):
        # CFW protection coverage.
        self.cfw_protection = cfw_protection
        # ECS protection coverage.
        self.ecs_protection = ecs_protection
        # WAF protection coverage.
        self.waf_protection = waf_protection

    def validate(self):
        if self.cfw_protection:
            self.cfw_protection.validate()
        if self.ecs_protection:
            self.ecs_protection.validate()
        if self.waf_protection:
            self.waf_protection.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cfw_protection is not None:
            result['CfwProtection'] = self.cfw_protection.to_map()
        if self.ecs_protection is not None:
            result['EcsProtection'] = self.ecs_protection.to_map()
        if self.waf_protection is not None:
            result['WafProtection'] = self.waf_protection.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CfwProtection') is not None:
            temp_model = GetSafetyCoverResponseBodyDataCfwProtection()
            self.cfw_protection = temp_model.from_map(m['CfwProtection'])
        if m.get('EcsProtection') is not None:
            temp_model = GetSafetyCoverResponseBodyDataEcsProtection()
            self.ecs_protection = temp_model.from_map(m['EcsProtection'])
        if m.get('WafProtection') is not None:
            temp_model = GetSafetyCoverResponseBodyDataWafProtection()
            self.waf_protection = temp_model.from_map(m['WafProtection'])
        return self


class GetSafetyCoverResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetSafetyCoverResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # API return code.
        self.code = code
        # Data query result.
        self.data = data
        # HTTP status code.
        self.http_status_code = http_status_code
        # Message of the response result.
        self.message = message
        # Request ID.
        # 
        # This parameter is required.
        self.request_id = request_id
        # Whether the call was successful:
        # - **true**: Call succeeded.
        # - **false**: Call failed.
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
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetSafetyCoverResponseBodyData()
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


class GetSafetyCoverResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetSafetyCoverResponseBody = None,
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
            temp_model = GetSafetyCoverResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSowListRequest(TeaModel):
    def __init__(
        self,
        date_type: str = None,
        end_date: int = None,
        start_date: int = None,
        susp_event_source: str = None,
    ):
        # Filter time type, supports filtering by the last 7 days, the last 30 days, the last half year, or custom time ranges.
        # 
        # This parameter is required.
        self.date_type = date_type
        # End time.
        # 
        # This parameter is required.
        self.end_date = end_date
        # Start time.
        # 
        # This parameter is required.
        self.start_date = start_date
        # Alert event source.
        self.susp_event_source = susp_event_source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.date_type is not None:
            result['DateType'] = self.date_type
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.susp_event_source is not None:
            result['SuspEventSource'] = self.susp_event_source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DateType') is not None:
            self.date_type = m.get('DateType')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('SuspEventSource') is not None:
            self.susp_event_source = m.get('SuspEventSource')
        return self


class GetSowListResponseBodyData(TeaModel):
    def __init__(
        self,
        complete_time: str = None,
        operate_remark: str = None,
        progress: str = None,
        record_count: int = None,
        start_time: str = None,
        task_type_name: str = None,
        work_order_name: str = None,
    ):
        # Completion time.
        self.complete_time = complete_time
        # Operation remarks.
        self.operate_remark = operate_remark
        # Progress.
        self.progress = progress
        # Record count.
        self.record_count = record_count
        # Start time.
        self.start_time = start_time
        # Task type.
        self.task_type_name = task_type_name
        # Work order name.
        self.work_order_name = work_order_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.complete_time is not None:
            result['CompleteTime'] = self.complete_time
        if self.operate_remark is not None:
            result['OperateRemark'] = self.operate_remark
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.record_count is not None:
            result['RecordCount'] = self.record_count
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.task_type_name is not None:
            result['TaskTypeName'] = self.task_type_name
        if self.work_order_name is not None:
            result['WorkOrderName'] = self.work_order_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompleteTime') is not None:
            self.complete_time = m.get('CompleteTime')
        if m.get('OperateRemark') is not None:
            self.operate_remark = m.get('OperateRemark')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('RecordCount') is not None:
            self.record_count = m.get('RecordCount')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TaskTypeName') is not None:
            self.task_type_name = m.get('TaskTypeName')
        if m.get('WorkOrderName') is not None:
            self.work_order_name = m.get('WorkOrderName')
        return self


class GetSowListResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[GetSowListResponseBodyData] = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Interface response code.
        self.code = code
        # Data returned by the interface.
        self.data = data
        # HTTP status code.
        self.http_status_code = http_status_code
        # Prompt information for the returned result.
        self.message = message
        # Request ID.
        # 
        # This parameter is required.
        self.request_id = request_id
        # Whether the call was successful. - **true**: The call was successful. - **false**: The call failed.
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
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetSowListResponseBodyData()
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


class GetSowListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetSowListResponseBody = None,
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
            temp_model = GetSowListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSuspEventPageRequest(TeaModel):
    def __init__(
        self,
        alarm_end_time: int = None,
        alarm_start_time: int = None,
        current_page: int = None,
        page_size: int = None,
        source: str = None,
        status: int = None,
    ):
        # Alarm end time.
        self.alarm_end_time = alarm_end_time
        # Alarm start time.
        self.alarm_start_time = alarm_start_time
        # Current page number.
        # 
        # This parameter is required.
        self.current_page = current_page
        # Number of items per page.
        # 
        # This parameter is required.
        self.page_size = page_size
        # Alarm source.
        self.source = source
        # Disposal status.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm_end_time is not None:
            result['AlarmEndTime'] = self.alarm_end_time
        if self.alarm_start_time is not None:
            result['AlarmStartTime'] = self.alarm_start_time
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.source is not None:
            result['Source'] = self.source
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmEndTime') is not None:
            self.alarm_end_time = m.get('AlarmEndTime')
        if m.get('AlarmStartTime') is not None:
            self.alarm_start_time = m.get('AlarmStartTime')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetSuspEventPageResponseBodyData(TeaModel):
    def __init__(
        self,
        alarm_event_type: str = None,
        alarm_id: int = None,
        alarm_name: str = None,
        alarm_source: str = None,
        alarm_time: str = None,
        analysis_result: str = None,
        deal_time: str = None,
        event_level: str = None,
        id: int = None,
        instance_name: str = None,
        internet_ip: str = None,
        intranet_ip: str = None,
        occurrence_time: str = None,
        owner_id: str = None,
        remark: str = None,
        status: str = None,
    ):
        # Alarm event type.
        self.alarm_event_type = alarm_event_type
        # Alarm ID.
        self.alarm_id = alarm_id
        # Alarm name.
        self.alarm_name = alarm_name
        # Alarm source.
        self.alarm_source = alarm_source
        # Latest alarm time.
        self.alarm_time = alarm_time
        # Analysis process.
        self.analysis_result = analysis_result
        # Alarm handling time.
        self.deal_time = deal_time
        # Alarm level.
        self.event_level = event_level
        # Ticket primary key id.
        self.id = id
        # Affected asset.
        self.instance_name = instance_name
        # Public IP address.
        self.internet_ip = internet_ip
        # Private IP address.
        self.intranet_ip = intranet_ip
        # First occurrence time.
        self.occurrence_time = occurrence_time
        # Owner ID.
        self.owner_id = owner_id
        # Disposal method.
        self.remark = remark
        # Handling status.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm_event_type is not None:
            result['AlarmEventType'] = self.alarm_event_type
        if self.alarm_id is not None:
            result['AlarmId'] = self.alarm_id
        if self.alarm_name is not None:
            result['AlarmName'] = self.alarm_name
        if self.alarm_source is not None:
            result['AlarmSource'] = self.alarm_source
        if self.alarm_time is not None:
            result['AlarmTime'] = self.alarm_time
        if self.analysis_result is not None:
            result['AnalysisResult'] = self.analysis_result
        if self.deal_time is not None:
            result['DealTime'] = self.deal_time
        if self.event_level is not None:
            result['EventLevel'] = self.event_level
        if self.id is not None:
            result['Id'] = self.id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip
        if self.intranet_ip is not None:
            result['IntranetIp'] = self.intranet_ip
        if self.occurrence_time is not None:
            result['OccurrenceTime'] = self.occurrence_time
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmEventType') is not None:
            self.alarm_event_type = m.get('AlarmEventType')
        if m.get('AlarmId') is not None:
            self.alarm_id = m.get('AlarmId')
        if m.get('AlarmName') is not None:
            self.alarm_name = m.get('AlarmName')
        if m.get('AlarmSource') is not None:
            self.alarm_source = m.get('AlarmSource')
        if m.get('AlarmTime') is not None:
            self.alarm_time = m.get('AlarmTime')
        if m.get('AnalysisResult') is not None:
            self.analysis_result = m.get('AnalysisResult')
        if m.get('DealTime') is not None:
            self.deal_time = m.get('DealTime')
        if m.get('EventLevel') is not None:
            self.event_level = m.get('EventLevel')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')
        if m.get('IntranetIp') is not None:
            self.intranet_ip = m.get('IntranetIp')
        if m.get('OccurrenceTime') is not None:
            self.occurrence_time = m.get('OccurrenceTime')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetSuspEventPageResponseBodyPageInfo(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The current page number in pagination queries.
        self.current_page = current_page
        # The number of items displayed per page in the returned data.
        self.page_size = page_size
        # Total number of query results.
        self.total_count = total_count

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
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class GetSuspEventPageResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[GetSuspEventPageResponseBodyData] = None,
        http_status_code: int = None,
        message: str = None,
        page_info: GetSuspEventPageResponseBodyPageInfo = None,
        request_id: str = None,
        success: bool = None,
    ):
        # API response code.
        self.code = code
        # Data returned by the interface.
        self.data = data
        # HTTP status code.
        self.http_status_code = http_status_code
        # Prompt message of the returned result.
        self.message = message
        # Pagination information.
        self.page_info = page_info
        # Request ID.
        # 
        # This parameter is required.
        self.request_id = request_id
        # Whether the call was successful.
        # - **true**: The call was successful. - **false**: The call failed.
        self.success = success

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()
        if self.page_info:
            self.page_info.validate()

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
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()
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
                temp_model = GetSuspEventPageResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageInfo') is not None:
            temp_model = GetSuspEventPageResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m['PageInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetSuspEventPageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetSuspEventPageResponseBody = None,
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
            temp_model = GetSuspEventPageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSuspEventSummaryRequest(TeaModel):
    def __init__(
        self,
        date_type: str = None,
        end_date: int = None,
        start_date: int = None,
        susp_event_source: str = None,
    ):
        # Filter time type. Supports filtering by the last 7 days, the last 30 days, the last half year, or custom time ranges.
        # 
        # This parameter is required.
        self.date_type = date_type
        # End time.
        # 
        # This parameter is required.
        self.end_date = end_date
        # Start time.
        # 
        # This parameter is required.
        self.start_date = start_date
        # Alert event source.
        self.susp_event_source = susp_event_source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.date_type is not None:
            result['DateType'] = self.date_type
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.susp_event_source is not None:
            result['SuspEventSource'] = self.susp_event_source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DateType') is not None:
            self.date_type = m.get('DateType')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('SuspEventSource') is not None:
            self.susp_event_source = m.get('SuspEventSource')
        return self


class GetSuspEventSummaryResponseBodyDataNetworkAttackTrendDTOTrendList(TeaModel):
    def __init__(
        self,
        date: str = None,
        ddos_count: int = None,
        eip_count: int = None,
        waf_count: int = None,
    ):
        # Date.
        self.date = date
        # DDoS count.
        self.ddos_count = ddos_count
        # EIP count.
        self.eip_count = eip_count
        # WAF count.
        self.waf_count = waf_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.date is not None:
            result['Date'] = self.date
        if self.ddos_count is not None:
            result['DdosCount'] = self.ddos_count
        if self.eip_count is not None:
            result['EipCount'] = self.eip_count
        if self.waf_count is not None:
            result['WafCount'] = self.waf_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Date') is not None:
            self.date = m.get('Date')
        if m.get('DdosCount') is not None:
            self.ddos_count = m.get('DdosCount')
        if m.get('EipCount') is not None:
            self.eip_count = m.get('EipCount')
        if m.get('WafCount') is not None:
            self.waf_count = m.get('WafCount')
        return self


class GetSuspEventSummaryResponseBodyDataNetworkAttackTrendDTO(TeaModel):
    def __init__(
        self,
        trend_list: List[GetSuspEventSummaryResponseBodyDataNetworkAttackTrendDTOTrendList] = None,
    ):
        # Collection of trend nodes for each attack item.
        self.trend_list = trend_list

    def validate(self):
        if self.trend_list:
            for k in self.trend_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TrendList'] = []
        if self.trend_list is not None:
            for k in self.trend_list:
                result['TrendList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.trend_list = []
        if m.get('TrendList') is not None:
            for k in m.get('TrendList'):
                temp_model = GetSuspEventSummaryResponseBodyDataNetworkAttackTrendDTOTrendList()
                self.trend_list.append(temp_model.from_map(k))
        return self


class GetSuspEventSummaryResponseBodyDataSuspEventDealSummaryDTO(TeaModel):
    def __init__(
        self,
        completed_count: int = None,
        handing_count: int = None,
        handing_rate: str = None,
        total_count: int = None,
        total_growth_rate: str = None,
        wait_handle_count: int = None,
    ):
        # Completed.
        self.completed_count = completed_count
        # In progress.
        self.handing_count = handing_count
        # Alert handling rate.
        self.handing_rate = handing_rate
        # Total number of alerts.
        self.total_count = total_count
        # Year-over-year comparison of alerts.
        self.total_growth_rate = total_growth_rate
        # Number of unhandled alerts.
        self.wait_handle_count = wait_handle_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.completed_count is not None:
            result['CompletedCount'] = self.completed_count
        if self.handing_count is not None:
            result['HandingCount'] = self.handing_count
        if self.handing_rate is not None:
            result['HandingRate'] = self.handing_rate
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.total_growth_rate is not None:
            result['TotalGrowthRate'] = self.total_growth_rate
        if self.wait_handle_count is not None:
            result['WaitHandleCount'] = self.wait_handle_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompletedCount') is not None:
            self.completed_count = m.get('CompletedCount')
        if m.get('HandingCount') is not None:
            self.handing_count = m.get('HandingCount')
        if m.get('HandingRate') is not None:
            self.handing_rate = m.get('HandingRate')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('TotalGrowthRate') is not None:
            self.total_growth_rate = m.get('TotalGrowthRate')
        if m.get('WaitHandleCount') is not None:
            self.wait_handle_count = m.get('WaitHandleCount')
        return self


class GetSuspEventSummaryResponseBodyDataSuspEventTopDTOSuspEventList(TeaModel):
    def __init__(
        self,
        event_name: str = None,
        task_count: int = None,
    ):
        # Alert name.
        self.event_name = event_name
        # Count.
        self.task_count = task_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_name is not None:
            result['EventName'] = self.event_name
        if self.task_count is not None:
            result['TaskCount'] = self.task_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventName') is not None:
            self.event_name = m.get('EventName')
        if m.get('TaskCount') is not None:
            self.task_count = m.get('TaskCount')
        return self


class GetSuspEventSummaryResponseBodyDataSuspEventTopDTO(TeaModel):
    def __init__(
        self,
        susp_event_list: List[GetSuspEventSummaryResponseBodyDataSuspEventTopDTOSuspEventList] = None,
    ):
        # Top 10 before handling alarms
        self.susp_event_list = susp_event_list

    def validate(self):
        if self.susp_event_list:
            for k in self.susp_event_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SuspEventList'] = []
        if self.susp_event_list is not None:
            for k in self.susp_event_list:
                result['SuspEventList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.susp_event_list = []
        if m.get('SuspEventList') is not None:
            for k in m.get('SuspEventList'):
                temp_model = GetSuspEventSummaryResponseBodyDataSuspEventTopDTOSuspEventList()
                self.susp_event_list.append(temp_model.from_map(k))
        return self


class GetSuspEventSummaryResponseBodyDataSuspEventTrendDTOTrendList(TeaModel):
    def __init__(
        self,
        date: str = None,
        deal_count: int = None,
        find_count: int = None,
    ):
        # Time point.
        self.date = date
        # Number of handled alerts.
        self.deal_count = deal_count
        # Number of discovered alerts.
        self.find_count = find_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.date is not None:
            result['Date'] = self.date
        if self.deal_count is not None:
            result['DealCount'] = self.deal_count
        if self.find_count is not None:
            result['FindCount'] = self.find_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Date') is not None:
            self.date = m.get('Date')
        if m.get('DealCount') is not None:
            self.deal_count = m.get('DealCount')
        if m.get('FindCount') is not None:
            self.find_count = m.get('FindCount')
        return self


class GetSuspEventSummaryResponseBodyDataSuspEventTrendDTO(TeaModel):
    def __init__(
        self,
        trend_list: List[GetSuspEventSummaryResponseBodyDataSuspEventTrendDTOTrendList] = None,
    ):
        # Trend of alerts.
        self.trend_list = trend_list

    def validate(self):
        if self.trend_list:
            for k in self.trend_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TrendList'] = []
        if self.trend_list is not None:
            for k in self.trend_list:
                result['TrendList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.trend_list = []
        if m.get('TrendList') is not None:
            for k in m.get('TrendList'):
                temp_model = GetSuspEventSummaryResponseBodyDataSuspEventTrendDTOTrendList()
                self.trend_list.append(temp_model.from_map(k))
        return self


class GetSuspEventSummaryResponseBodyData(TeaModel):
    def __init__(
        self,
        network_attack_trend_dto: GetSuspEventSummaryResponseBodyDataNetworkAttackTrendDTO = None,
        susp_event_deal_summary_dto: GetSuspEventSummaryResponseBodyDataSuspEventDealSummaryDTO = None,
        susp_event_top_dto: GetSuspEventSummaryResponseBodyDataSuspEventTopDTO = None,
        susp_event_trend_dto: GetSuspEventSummaryResponseBodyDataSuspEventTrendDTO = None,
    ):
        # Network attack trend.
        self.network_attack_trend_dto = network_attack_trend_dto
        # Overview of alert handling.
        self.susp_event_deal_summary_dto = susp_event_deal_summary_dto
        # Top 10 alerts before handling.
        self.susp_event_top_dto = susp_event_top_dto
        # Trend of alert responses.
        self.susp_event_trend_dto = susp_event_trend_dto

    def validate(self):
        if self.network_attack_trend_dto:
            self.network_attack_trend_dto.validate()
        if self.susp_event_deal_summary_dto:
            self.susp_event_deal_summary_dto.validate()
        if self.susp_event_top_dto:
            self.susp_event_top_dto.validate()
        if self.susp_event_trend_dto:
            self.susp_event_trend_dto.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.network_attack_trend_dto is not None:
            result['NetworkAttackTrendDTO'] = self.network_attack_trend_dto.to_map()
        if self.susp_event_deal_summary_dto is not None:
            result['SuspEventDealSummaryDTO'] = self.susp_event_deal_summary_dto.to_map()
        if self.susp_event_top_dto is not None:
            result['SuspEventTopDTO'] = self.susp_event_top_dto.to_map()
        if self.susp_event_trend_dto is not None:
            result['SuspEventTrendDTO'] = self.susp_event_trend_dto.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NetworkAttackTrendDTO') is not None:
            temp_model = GetSuspEventSummaryResponseBodyDataNetworkAttackTrendDTO()
            self.network_attack_trend_dto = temp_model.from_map(m['NetworkAttackTrendDTO'])
        if m.get('SuspEventDealSummaryDTO') is not None:
            temp_model = GetSuspEventSummaryResponseBodyDataSuspEventDealSummaryDTO()
            self.susp_event_deal_summary_dto = temp_model.from_map(m['SuspEventDealSummaryDTO'])
        if m.get('SuspEventTopDTO') is not None:
            temp_model = GetSuspEventSummaryResponseBodyDataSuspEventTopDTO()
            self.susp_event_top_dto = temp_model.from_map(m['SuspEventTopDTO'])
        if m.get('SuspEventTrendDTO') is not None:
            temp_model = GetSuspEventSummaryResponseBodyDataSuspEventTrendDTO()
            self.susp_event_trend_dto = temp_model.from_map(m['SuspEventTrendDTO'])
        return self


class GetSuspEventSummaryResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetSuspEventSummaryResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # API response code.
        self.code = code
        # Data returned by the interface.
        self.data = data
        # HTTP status code.
        self.http_status_code = http_status_code
        # Prompt message for the returned result.
        self.message = message
        # Request ID.
        # 
        # This parameter is required.
        self.request_id = request_id
        # Whether the call was successful.
        # - true: Call succeeded.
        # - false: Call failed.
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
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetSuspEventSummaryResponseBodyData()
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


class GetSuspEventSummaryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetSuspEventSummaryResponseBody = None,
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
            temp_model = GetSuspEventSummaryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSuspPageSummaryResponseBodyData(TeaModel):
    def __init__(
        self,
        completed_count: int = None,
        handing_count: int = None,
        high_count: int = None,
        low_count: int = None,
        medium_count: int = None,
        total_count: int = None,
        wait_handle_count: int = None,
    ):
        # Number of completed items.
        self.completed_count = completed_count
        # Number of items being processed.
        self.handing_count = handing_count
        # Number of high-risk items.
        self.high_count = high_count
        # Number of low-risk items.
        self.low_count = low_count
        # Number of medium-risk items.
        self.medium_count = medium_count
        # Total number of items.
        self.total_count = total_count
        # Number of unhandled items.
        self.wait_handle_count = wait_handle_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.completed_count is not None:
            result['CompletedCount'] = self.completed_count
        if self.handing_count is not None:
            result['HandingCount'] = self.handing_count
        if self.high_count is not None:
            result['HighCount'] = self.high_count
        if self.low_count is not None:
            result['LowCount'] = self.low_count
        if self.medium_count is not None:
            result['MediumCount'] = self.medium_count
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.wait_handle_count is not None:
            result['WaitHandleCount'] = self.wait_handle_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompletedCount') is not None:
            self.completed_count = m.get('CompletedCount')
        if m.get('HandingCount') is not None:
            self.handing_count = m.get('HandingCount')
        if m.get('HighCount') is not None:
            self.high_count = m.get('HighCount')
        if m.get('LowCount') is not None:
            self.low_count = m.get('LowCount')
        if m.get('MediumCount') is not None:
            self.medium_count = m.get('MediumCount')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('WaitHandleCount') is not None:
            self.wait_handle_count = m.get('WaitHandleCount')
        return self


class GetSuspPageSummaryResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetSuspPageSummaryResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Interface response code.
        self.code = code
        # Data returned by the interface.
        self.data = data
        # HTTP status code.
        self.http_status_code = http_status_code
        # Prompt message for the result returned.
        self.message = message
        # Request ID.
        # 
        # This parameter is required.
        self.request_id = request_id
        # Indicates whether the call was successful.
        # - **true**: Call succeeded.
        # - **false**: Call failed.
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
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetSuspPageSummaryResponseBodyData()
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


class GetSuspPageSummaryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetSuspPageSummaryResponseBody = None,
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
            temp_model = GetSuspPageSummaryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserStatusResponseBodyData(TeaModel):
    def __init__(
        self,
        customer_type: str = None,
        end_date: str = None,
        instance_id: str = None,
        start_date: str = None,
        status: str = None,
        version: str = None,
    ):
        # Customer type.
        self.customer_type = customer_type
        # End date.
        self.end_date = end_date
        # Instance ID.
        self.instance_id = instance_id
        # Start date.
        self.start_date = start_date
        # Status.
        self.status = status
        # Version.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.customer_type is not None:
            result['CustomerType'] = self.customer_type
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.status is not None:
            result['Status'] = self.status
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomerType') is not None:
            self.customer_type = m.get('CustomerType')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class GetUserStatusResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetUserStatusResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Interface response code.
        self.code = code
        # Data returned by the interface.
        self.data = data
        # HTTP status code.
        self.http_status_code = http_status_code
        # Prompt message of the returned result.
        self.message = message
        # Request ID.
        # 
        # This parameter is required.
        self.request_id = request_id
        # Indicates whether the call was successful. - **true**: The call was successful. - **false**: The call failed.
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
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetUserStatusResponseBodyData()
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


class GetUserStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetUserStatusResponseBody = None,
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
            temp_model = GetUserStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetVulItemPageRequest(TeaModel):
    def __init__(
        self,
        alias_name: str = None,
        current_page: int = None,
        dealed: str = None,
        level: str = None,
        name: str = None,
        page_size: int = None,
        scan_type: str = None,
    ):
        # Vulnerability alias.
        self.alias_name = alias_name
        # Current page number.
        # 
        # This parameter is required.
        self.current_page = current_page
        # Processing status. y: processed; n: unprocessed; h: processing.
        self.dealed = dealed
        # Risk level.
        self.level = level
        # Vulnerability name.
        self.name = name
        # Number of items to display per page in the returned data.
        # 
        # This parameter is required.
        self.page_size = page_size
        # Vulnerability type.
        self.scan_type = scan_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias_name is not None:
            result['AliasName'] = self.alias_name
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.dealed is not None:
            result['Dealed'] = self.dealed
        if self.level is not None:
            result['Level'] = self.level
        if self.name is not None:
            result['Name'] = self.name
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.scan_type is not None:
            result['ScanType'] = self.scan_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliasName') is not None:
            self.alias_name = m.get('AliasName')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('Dealed') is not None:
            self.dealed = m.get('Dealed')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ScanType') is not None:
            self.scan_type = m.get('ScanType')
        return self


class GetVulItemPageResponseBodyData(TeaModel):
    def __init__(
        self,
        alias_name: str = None,
        asap_count: int = None,
        customer_id: str = None,
        cve_url_prefix: str = None,
        dealed: str = None,
        find_time: str = None,
        handled_count: int = None,
        id: int = None,
        later_count: int = None,
        level: str = None,
        name: str = None,
        nntf_count: int = None,
        related: str = None,
        related_cve_count: int = None,
        scan_type: str = None,
        tags: str = None,
        total_fix_count: int = None,
    ):
        # Vulnerability alias.
        self.alias_name = alias_name
        # Number of high-priority vulnerabilities to be fixed.
        self.asap_count = asap_count
        # User ID.
        self.customer_id = customer_id
        # Prefix for the CVE remediation advice URL.
        self.cve_url_prefix = cve_url_prefix
        # Processing status.
        self.dealed = dealed
        # Timestamp of the last discovery of the vulnerability.
        self.find_time = find_time
        # Number of processed vulnerabilities.
        self.handled_count = handled_count
        # Primary key ID.
        self.id = id
        # Number of medium-priority vulnerabilities to be fixed.
        self.later_count = later_count
        # Risk level
        self.level = level
        # Vulnerability name.
        self.name = name
        # Number of low-priority vulnerabilities to be fixed.
        self.nntf_count = nntf_count
        # CVE number.
        self.related = related
        # Number of related CVE numbers.
        self.related_cve_count = related_cve_count
        # Vulnerability type.
        self.scan_type = scan_type
        # Tags.
        self.tags = tags
        # Total number of fixed vulnerabilities.
        self.total_fix_count = total_fix_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias_name is not None:
            result['AliasName'] = self.alias_name
        if self.asap_count is not None:
            result['AsapCount'] = self.asap_count
        if self.customer_id is not None:
            result['CustomerId'] = self.customer_id
        if self.cve_url_prefix is not None:
            result['CveUrlPrefix'] = self.cve_url_prefix
        if self.dealed is not None:
            result['Dealed'] = self.dealed
        if self.find_time is not None:
            result['FindTime'] = self.find_time
        if self.handled_count is not None:
            result['HandledCount'] = self.handled_count
        if self.id is not None:
            result['Id'] = self.id
        if self.later_count is not None:
            result['LaterCount'] = self.later_count
        if self.level is not None:
            result['Level'] = self.level
        if self.name is not None:
            result['Name'] = self.name
        if self.nntf_count is not None:
            result['NntfCount'] = self.nntf_count
        if self.related is not None:
            result['Related'] = self.related
        if self.related_cve_count is not None:
            result['RelatedCveCount'] = self.related_cve_count
        if self.scan_type is not None:
            result['ScanType'] = self.scan_type
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.total_fix_count is not None:
            result['TotalFixCount'] = self.total_fix_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliasName') is not None:
            self.alias_name = m.get('AliasName')
        if m.get('AsapCount') is not None:
            self.asap_count = m.get('AsapCount')
        if m.get('CustomerId') is not None:
            self.customer_id = m.get('CustomerId')
        if m.get('CveUrlPrefix') is not None:
            self.cve_url_prefix = m.get('CveUrlPrefix')
        if m.get('Dealed') is not None:
            self.dealed = m.get('Dealed')
        if m.get('FindTime') is not None:
            self.find_time = m.get('FindTime')
        if m.get('HandledCount') is not None:
            self.handled_count = m.get('HandledCount')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LaterCount') is not None:
            self.later_count = m.get('LaterCount')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NntfCount') is not None:
            self.nntf_count = m.get('NntfCount')
        if m.get('Related') is not None:
            self.related = m.get('Related')
        if m.get('RelatedCveCount') is not None:
            self.related_cve_count = m.get('RelatedCveCount')
        if m.get('ScanType') is not None:
            self.scan_type = m.get('ScanType')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('TotalFixCount') is not None:
            self.total_fix_count = m.get('TotalFixCount')
        return self


class GetVulItemPageResponseBodyPageInfo(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The current page number for pagination queries.
        self.current_page = current_page
        # Number of items to display per page in the returned data.
        self.page_size = page_size
        # Total number of records in the query result.
        self.total_count = total_count

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
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class GetVulItemPageResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[GetVulItemPageResponseBodyData] = None,
        http_status_code: int = None,
        message: str = None,
        page_info: GetVulItemPageResponseBodyPageInfo = None,
        request_id: str = None,
        success: bool = None,
    ):
        # API response code.
        self.code = code
        # Data returned by the interface.
        self.data = data
        # HTTP status code.
        self.http_status_code = http_status_code
        # Prompt message for the returned result.
        self.message = message
        # Pagination information.
        self.page_info = page_info
        # Request response.
        # 
        # This parameter is required.
        self.request_id = request_id
        # Whether the call was successful.
        # true: Call succeeded. false: Call failed.
        self.success = success

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()
        if self.page_info:
            self.page_info.validate()

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
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()
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
                temp_model = GetVulItemPageResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageInfo') is not None:
            temp_model = GetVulItemPageResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m['PageInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetVulItemPageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetVulItemPageResponseBody = None,
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
            temp_model = GetVulItemPageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetVulListByIdRequest(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        dealed: str = None,
        id: int = None,
        necessity: str = None,
        page_size: int = None,
        remark: str = None,
        uuids: str = None,
    ):
        # Current page
        self.current_page = current_page
        # Whether it has been processed; y: processed; n: not processed
        self.dealed = dealed
        # Primary key ID
        # 
        # This parameter is required.
        self.id = id
        # Risk level
        self.necessity = necessity
        # Page size
        self.page_size = page_size
        # Asset information of the vulnerability to be queried, which can be set as asset name, public IP, or private IP.
        self.remark = remark
        # UUID of the server with the vulnerability to be queried. Multiple UUIDs should be separated by a comma (,).
        self.uuids = uuids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.dealed is not None:
            result['Dealed'] = self.dealed
        if self.id is not None:
            result['Id'] = self.id
        if self.necessity is not None:
            result['Necessity'] = self.necessity
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.uuids is not None:
            result['Uuids'] = self.uuids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('Dealed') is not None:
            self.dealed = m.get('Dealed')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Necessity') is not None:
            self.necessity = m.get('Necessity')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('Uuids') is not None:
            self.uuids = m.get('Uuids')
        return self


class GetVulListByIdResponseBodyDataEffectMsgDTOS(TeaModel):
    def __init__(
        self,
        match_list: str = None,
        path: str = None,
        soft_name: str = None,
    ):
        # Hit
        self.match_list = match_list
        # Path
        self.path = path
        # Software name
        self.soft_name = soft_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match_list is not None:
            result['MatchList'] = self.match_list
        if self.path is not None:
            result['Path'] = self.path
        if self.soft_name is not None:
            result['SoftName'] = self.soft_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MatchList') is not None:
            self.match_list = m.get('MatchList')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('SoftName') is not None:
            self.soft_name = m.get('SoftName')
        return self


class GetVulListByIdResponseBodyData(TeaModel):
    def __init__(
        self,
        alias_name: str = None,
        effect_msg_dtos: List[GetVulListByIdResponseBodyDataEffectMsgDTOS] = None,
        first_ts: str = None,
        instance_name: str = None,
        internet_ip: str = None,
        intranet_ip: str = None,
        last_ts: str = None,
        name: str = None,
        necessity: str = None,
        related: str = None,
        repair_cmd: str = None,
        repair_ts: str = None,
        status: str = None,
        tag: str = None,
        uuid: str = None,
    ):
        # Vulnerability Alias
        self.alias_name = alias_name
        # Impact description
        self.effect_msg_dtos = effect_msg_dtos
        # Timestamp of the first time the vulnerability was detected
        self.first_ts = first_ts
        # Instance name of the asset
        self.instance_name = instance_name
        # Public IP of the asset
        self.internet_ip = internet_ip
        # Private IP of the asset
        self.intranet_ip = intranet_ip
        # Timestamp of the last time the vulnerability was detected
        self.last_ts = last_ts
        # Vulnerability name
        self.name = name
        # Necessity level of vulnerability repair
        self.necessity = necessity
        # List of associated CVEs for the vulnerability, separated by commas (,) if there are multiple values.
        self.related = related
        # Repair command
        self.repair_cmd = repair_cmd
        # Timestamp of vulnerability repair
        self.repair_ts = repair_ts
        # Vulnerability status:
        # 1: Not fixed
        # 2: Fix failed
        # 3: Rollback failed
        # 4: Fixing
        # 5: Rolling back
        # 6: Verifying
        # 7: Fixed successfully
        # 8: Fixed successfully, pending reboot
        # 9: Rolled back successfully
        # 10: Ignored
        # 11: Rolled back successfully, pending reboot
        # 12: Vulnerability does not exist
        # 20: Expired
        self.status = status
        # Vulnerability tag
        self.tag = tag
        # UUID of the asset instance.
        self.uuid = uuid

    def validate(self):
        if self.effect_msg_dtos:
            for k in self.effect_msg_dtos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias_name is not None:
            result['AliasName'] = self.alias_name
        result['EffectMsgDTOS'] = []
        if self.effect_msg_dtos is not None:
            for k in self.effect_msg_dtos:
                result['EffectMsgDTOS'].append(k.to_map() if k else None)
        if self.first_ts is not None:
            result['FirstTs'] = self.first_ts
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip
        if self.intranet_ip is not None:
            result['IntranetIp'] = self.intranet_ip
        if self.last_ts is not None:
            result['LastTs'] = self.last_ts
        if self.name is not None:
            result['Name'] = self.name
        if self.necessity is not None:
            result['Necessity'] = self.necessity
        if self.related is not None:
            result['Related'] = self.related
        if self.repair_cmd is not None:
            result['RepairCmd'] = self.repair_cmd
        if self.repair_ts is not None:
            result['RepairTs'] = self.repair_ts
        if self.status is not None:
            result['Status'] = self.status
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliasName') is not None:
            self.alias_name = m.get('AliasName')
        self.effect_msg_dtos = []
        if m.get('EffectMsgDTOS') is not None:
            for k in m.get('EffectMsgDTOS'):
                temp_model = GetVulListByIdResponseBodyDataEffectMsgDTOS()
                self.effect_msg_dtos.append(temp_model.from_map(k))
        if m.get('FirstTs') is not None:
            self.first_ts = m.get('FirstTs')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')
        if m.get('IntranetIp') is not None:
            self.intranet_ip = m.get('IntranetIp')
        if m.get('LastTs') is not None:
            self.last_ts = m.get('LastTs')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Necessity') is not None:
            self.necessity = m.get('Necessity')
        if m.get('Related') is not None:
            self.related = m.get('Related')
        if m.get('RepairCmd') is not None:
            self.repair_cmd = m.get('RepairCmd')
        if m.get('RepairTs') is not None:
            self.repair_ts = m.get('RepairTs')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class GetVulListByIdResponseBodyPageInfo(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # Current page number.
        self.current_page = current_page
        # Number of items per page in the returned data.
        self.page_size = page_size
        # Total number of records in the query result.
        self.total_count = total_count

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
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class GetVulListByIdResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[GetVulListByIdResponseBodyData] = None,
        http_status_code: int = None,
        message: str = None,
        page_info: GetVulListByIdResponseBodyPageInfo = None,
        request_id: str = None,
        success: bool = None,
    ):
        # API response code.
        self.code = code
        # Data returned by the interface.
        self.data = data
        # HTTP status code.
        self.http_status_code = http_status_code
        # Prompt message for the returned result.
        self.message = message
        # Pagination information.
        self.page_info = page_info
        # Request ID.
        # 
        # This parameter is required.
        self.request_id = request_id
        # Indicates whether the call was successful. Values: - **true**: Yes. - **false**: No.
        self.success = success

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()
        if self.page_info:
            self.page_info.validate()

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
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()
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
                temp_model = GetVulListByIdResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageInfo') is not None:
            temp_model = GetVulListByIdResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m['PageInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetVulListByIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetVulListByIdResponseBody = None,
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
            temp_model = GetVulListByIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetVulPageSummaryResponseBodyData(TeaModel):
    def __init__(
        self,
        completed_count: int = None,
        handing_count: int = None,
        high_count: int = None,
        low_count: int = None,
        medium_count: int = None,
        total_count: int = None,
        wait_handle_count: int = None,
    ):
        # Number of completed items.
        self.completed_count = completed_count
        # Number of items being handled.
        self.handing_count = handing_count
        # Number of high-risk items.
        self.high_count = high_count
        # Number of low-risk items.
        self.low_count = low_count
        # Number of medium-risk items.
        self.medium_count = medium_count
        # Total number of items.
        self.total_count = total_count
        # Number of unhandled items.
        self.wait_handle_count = wait_handle_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.completed_count is not None:
            result['CompletedCount'] = self.completed_count
        if self.handing_count is not None:
            result['HandingCount'] = self.handing_count
        if self.high_count is not None:
            result['HighCount'] = self.high_count
        if self.low_count is not None:
            result['LowCount'] = self.low_count
        if self.medium_count is not None:
            result['MediumCount'] = self.medium_count
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.wait_handle_count is not None:
            result['WaitHandleCount'] = self.wait_handle_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompletedCount') is not None:
            self.completed_count = m.get('CompletedCount')
        if m.get('HandingCount') is not None:
            self.handing_count = m.get('HandingCount')
        if m.get('HighCount') is not None:
            self.high_count = m.get('HighCount')
        if m.get('LowCount') is not None:
            self.low_count = m.get('LowCount')
        if m.get('MediumCount') is not None:
            self.medium_count = m.get('MediumCount')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('WaitHandleCount') is not None:
            self.wait_handle_count = m.get('WaitHandleCount')
        return self


class GetVulPageSummaryResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetVulPageSummaryResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Interface return code.
        self.code = code
        # Data query result.
        self.data = data
        # HTTP status code.
        self.http_status_code = http_status_code
        # Return message.
        self.message = message
        # Request ID.
        # 
        # This parameter is required.
        self.request_id = request_id
        # Whether the call was successful. - **true**: The call was successful. - **false**: The call failed.
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
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetVulPageSummaryResponseBodyData()
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


class GetVulPageSummaryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetVulPageSummaryResponseBody = None,
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
            temp_model = GetVulPageSummaryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetVulSummaryRequest(TeaModel):
    def __init__(
        self,
        date_type: str = None,
        end_date: int = None,
        start_date: int = None,
        susp_event_source: str = None,
    ):
        # Filter time type. Supports filtering by the last 7 days, the last 30 days, the last half year, or a custom time range.
        # 
        # This parameter is required.
        self.date_type = date_type
        # End time.
        # 
        # This parameter is required.
        self.end_date = end_date
        # Start time.
        # 
        # This parameter is required.
        self.start_date = start_date
        # Alert event source.
        self.susp_event_source = susp_event_source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.date_type is not None:
            result['DateType'] = self.date_type
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.susp_event_source is not None:
            result['SuspEventSource'] = self.susp_event_source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DateType') is not None:
            self.date_type = m.get('DateType')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('SuspEventSource') is not None:
            self.susp_event_source = m.get('SuspEventSource')
        return self


class GetVulSummaryResponseBodyDataTrendList(TeaModel):
    def __init__(
        self,
        date: str = None,
        deal_count: int = None,
        find_count: int = None,
    ):
        # Time point.
        self.date = date
        # Number of handled items.
        self.deal_count = deal_count
        # Number of discovered items.
        self.find_count = find_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.date is not None:
            result['Date'] = self.date
        if self.deal_count is not None:
            result['DealCount'] = self.deal_count
        if self.find_count is not None:
            result['FindCount'] = self.find_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Date') is not None:
            self.date = m.get('Date')
        if m.get('DealCount') is not None:
            self.deal_count = m.get('DealCount')
        if m.get('FindCount') is not None:
            self.find_count = m.get('FindCount')
        return self


class GetVulSummaryResponseBodyData(TeaModel):
    def __init__(
        self,
        completed_count: int = None,
        deal_rate: str = None,
        trend_list: List[GetVulSummaryResponseBodyDataTrendList] = None,
        wait_handle_count: int = None,
    ):
        # Number of completed items.
        self.completed_count = completed_count
        # Risk convergence rate.
        self.deal_rate = deal_rate
        # Collection of vulnerability trend nodes.
        self.trend_list = trend_list
        # Number of unhandled items.
        self.wait_handle_count = wait_handle_count

    def validate(self):
        if self.trend_list:
            for k in self.trend_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.completed_count is not None:
            result['CompletedCount'] = self.completed_count
        if self.deal_rate is not None:
            result['DealRate'] = self.deal_rate
        result['TrendList'] = []
        if self.trend_list is not None:
            for k in self.trend_list:
                result['TrendList'].append(k.to_map() if k else None)
        if self.wait_handle_count is not None:
            result['WaitHandleCount'] = self.wait_handle_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompletedCount') is not None:
            self.completed_count = m.get('CompletedCount')
        if m.get('DealRate') is not None:
            self.deal_rate = m.get('DealRate')
        self.trend_list = []
        if m.get('TrendList') is not None:
            for k in m.get('TrendList'):
                temp_model = GetVulSummaryResponseBodyDataTrendList()
                self.trend_list.append(temp_model.from_map(k))
        if m.get('WaitHandleCount') is not None:
            self.wait_handle_count = m.get('WaitHandleCount')
        return self


class GetVulSummaryResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetVulSummaryResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Interface response code.
        self.code = code
        # Data returned by the interface.
        self.data = data
        # HTTP status code.
        self.http_status_code = http_status_code
        # Prompt message for the response result.
        self.message = message
        # Request ID.
        # 
        # This parameter is required.
        self.request_id = request_id
        # Whether the call was successful. - **true**: The call was successful. - **false**: The call failed.
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
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetVulSummaryResponseBodyData()
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


class GetVulSummaryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetVulSummaryResponseBody = None,
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
            temp_model = GetVulSummaryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetWorkTaskSummaryRequest(TeaModel):
    def __init__(
        self,
        date_type: str = None,
        end_date: int = None,
        start_date: int = None,
        susp_event_source: str = None,
    ):
        # Filter time type, supports filtering by the last 7 days, the last 30 days, the last half year, or custom time periods.
        # 
        # This parameter is required.
        self.date_type = date_type
        # End time.
        # 
        # This parameter is required.
        self.end_date = end_date
        # Start time.
        # 
        # This parameter is required.
        self.start_date = start_date
        # Alert event source.
        self.susp_event_source = susp_event_source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.date_type is not None:
            result['DateType'] = self.date_type
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.susp_event_source is not None:
            result['SuspEventSource'] = self.susp_event_source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DateType') is not None:
            self.date_type = m.get('DateType')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('SuspEventSource') is not None:
            self.susp_event_source = m.get('SuspEventSource')
        return self


class GetWorkTaskSummaryResponseBodyData(TeaModel):
    def __init__(
        self,
        deal_average_duration: int = None,
        deal_average_duration_growth_rate: str = None,
        deal_work_task_count: int = None,
        deal_work_task_count_rate: str = None,
        work_task_count: int = None,
        work_task_deal_rate: str = None,
        work_task_deal_rate_growth_rate: str = None,
        work_task_growth_rate: str = None,
    ):
        # Average response time (in minutes).
        self.deal_average_duration = deal_average_duration
        # Year-over-year growth rate of average response time.
        self.deal_average_duration_growth_rate = deal_average_duration_growth_rate
        # Number of work orders responded to.
        self.deal_work_task_count = deal_work_task_count
        # Year-over-year growth rate of the number of work orders responded to.
        self.deal_work_task_count_rate = deal_work_task_count_rate
        # Number of service responses.
        self.work_task_count = work_task_count
        # Problem closure rate.
        self.work_task_deal_rate = work_task_deal_rate
        # Year-over-year growth rate of problem closure rate.
        self.work_task_deal_rate_growth_rate = work_task_deal_rate_growth_rate
        # Year-over-year growth rate of service responses.
        self.work_task_growth_rate = work_task_growth_rate

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deal_average_duration is not None:
            result['DealAverageDuration'] = self.deal_average_duration
        if self.deal_average_duration_growth_rate is not None:
            result['DealAverageDurationGrowthRate'] = self.deal_average_duration_growth_rate
        if self.deal_work_task_count is not None:
            result['DealWorkTaskCount'] = self.deal_work_task_count
        if self.deal_work_task_count_rate is not None:
            result['DealWorkTaskCountRate'] = self.deal_work_task_count_rate
        if self.work_task_count is not None:
            result['WorkTaskCount'] = self.work_task_count
        if self.work_task_deal_rate is not None:
            result['WorkTaskDealRate'] = self.work_task_deal_rate
        if self.work_task_deal_rate_growth_rate is not None:
            result['WorkTaskDealRateGrowthRate'] = self.work_task_deal_rate_growth_rate
        if self.work_task_growth_rate is not None:
            result['WorkTaskGrowthRate'] = self.work_task_growth_rate
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DealAverageDuration') is not None:
            self.deal_average_duration = m.get('DealAverageDuration')
        if m.get('DealAverageDurationGrowthRate') is not None:
            self.deal_average_duration_growth_rate = m.get('DealAverageDurationGrowthRate')
        if m.get('DealWorkTaskCount') is not None:
            self.deal_work_task_count = m.get('DealWorkTaskCount')
        if m.get('DealWorkTaskCountRate') is not None:
            self.deal_work_task_count_rate = m.get('DealWorkTaskCountRate')
        if m.get('WorkTaskCount') is not None:
            self.work_task_count = m.get('WorkTaskCount')
        if m.get('WorkTaskDealRate') is not None:
            self.work_task_deal_rate = m.get('WorkTaskDealRate')
        if m.get('WorkTaskDealRateGrowthRate') is not None:
            self.work_task_deal_rate_growth_rate = m.get('WorkTaskDealRateGrowthRate')
        if m.get('WorkTaskGrowthRate') is not None:
            self.work_task_growth_rate = m.get('WorkTaskGrowthRate')
        return self


class GetWorkTaskSummaryResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetWorkTaskSummaryResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Response code.
        self.code = code
        # Data returned by the interface.
        self.data = data
        # HTTP status code.
        self.http_status_code = http_status_code
        # Prompt message for the response result.
        self.message = message
        # Request ID.
        # 
        # This parameter is required.
        self.request_id = request_id
        # Whether the call was successful. - **true**: The call was successful. - **false**: The call failed.
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
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetWorkTaskSummaryResponseBodyData()
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


class GetWorkTaskSummaryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetWorkTaskSummaryResponseBody = None,
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
            temp_model = GetWorkTaskSummaryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PageServiceCustomerRequest(TeaModel):
    def __init__(
        self,
        auth_status: int = None,
        cm_auth_status: int = None,
        current_page: int = None,
        end_time: int = None,
        monitor_auth_status: int = None,
        page_size: int = None,
        start_time: int = None,
    ):
        # Authorization status.
        self.auth_status = auth_status
        # Cloud Monitoring - Alert authorization status.
        self.cm_auth_status = cm_auth_status
        # The page number of the query result, default is 1.
        # 
        # This parameter is required.
        self.current_page = current_page
        # End time. The format is a Unix timestamp, which is the number of milliseconds since January 1, 1970.
        self.end_time = end_time
        # Cloud Security - Alert authorization status.
        self.monitor_auth_status = monitor_auth_status
        # Number of records per page.
        # 
        # This parameter is required.
        self.page_size = page_size
        # Start time. The format is a Unix timestamp, which is the number of milliseconds since January 1, 1970.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_status is not None:
            result['AuthStatus'] = self.auth_status
        if self.cm_auth_status is not None:
            result['CmAuthStatus'] = self.cm_auth_status
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.monitor_auth_status is not None:
            result['MonitorAuthStatus'] = self.monitor_auth_status
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthStatus') is not None:
            self.auth_status = m.get('AuthStatus')
        if m.get('CmAuthStatus') is not None:
            self.cm_auth_status = m.get('CmAuthStatus')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('MonitorAuthStatus') is not None:
            self.monitor_auth_status = m.get('MonitorAuthStatus')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class PageServiceCustomerResponseBodyData(TeaModel):
    def __init__(
        self,
        aliuid: str = None,
        auth_status: int = None,
        cm_auth_status: int = None,
        end_time: int = None,
        level: str = None,
        monitor_auth_status: int = None,
        name: str = None,
        own_id: str = None,
        start_time: int = None,
        user_id: str = None,
        version: str = None,
    ):
        # Customer UID.
        self.aliuid = aliuid
        # Authorization status.
        self.auth_status = auth_status
        # Cloud Monitoring - Alert authorization status.
        self.cm_auth_status = cm_auth_status
        # End time. The format is a Unix timestamp, which is the number of milliseconds since January 1, 1970.
        self.end_time = end_time
        # Customer level.
        self.level = level
        # Cloud Security - Alert authorization status.
        self.monitor_auth_status = monitor_auth_status
        # Customer name.
        self.name = name
        # Owner name.
        self.own_id = own_id
        # Start time. The format is a Unix timestamp, which is the number of milliseconds since January 1, 1970.
        self.start_time = start_time
        # Customer ID.
        self.user_id = user_id
        # Version information.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aliuid is not None:
            result['Aliuid'] = self.aliuid
        if self.auth_status is not None:
            result['AuthStatus'] = self.auth_status
        if self.cm_auth_status is not None:
            result['CmAuthStatus'] = self.cm_auth_status
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.level is not None:
            result['Level'] = self.level
        if self.monitor_auth_status is not None:
            result['MonitorAuthStatus'] = self.monitor_auth_status
        if self.name is not None:
            result['Name'] = self.name
        if self.own_id is not None:
            result['OwnId'] = self.own_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Aliuid') is not None:
            self.aliuid = m.get('Aliuid')
        if m.get('AuthStatus') is not None:
            self.auth_status = m.get('AuthStatus')
        if m.get('CmAuthStatus') is not None:
            self.cm_auth_status = m.get('CmAuthStatus')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('MonitorAuthStatus') is not None:
            self.monitor_auth_status = m.get('MonitorAuthStatus')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnId') is not None:
            self.own_id = m.get('OwnId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class PageServiceCustomerResponseBodyPageInfo(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The current page number in pagination queries.
        self.current_page = current_page
        # Number of items per page.
        self.page_size = page_size
        # Total number of query results.
        self.total_count = total_count

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
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class PageServiceCustomerResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[PageServiceCustomerResponseBodyData] = None,
        http_status_code: int = None,
        message: str = None,
        page_info: PageServiceCustomerResponseBodyPageInfo = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Interface return code.
        self.code = code
        # Data query results.
        self.data = data
        # HTTP status code.
        self.http_status_code = http_status_code
        # Return message. When the request is successful, it returns a success message; when the request fails, it returns the reason for the failure.
        self.message = message
        # Pagination information.
        self.page_info = page_info
        # Request ID.
        # 
        # This parameter is required.
        self.request_id = request_id
        # Request return status.
        # - true: Success.
        # - false: Failure.
        self.success = success

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()
        if self.page_info:
            self.page_info.validate()

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
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()
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
                temp_model = PageServiceCustomerResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageInfo') is not None:
            temp_model = PageServiceCustomerResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m['PageInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class PageServiceCustomerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PageServiceCustomerResponseBody = None,
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
            temp_model = PageServiceCustomerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendCustomEventRequest(TeaModel):
    def __init__(
        self,
        customer_id: str = None,
        data_source: str = None,
        event_description: str = None,
        event_details: str = None,
        event_name: str = None,
        event_type: str = None,
        find_time: int = None,
        instance_id: str = None,
        instance_name: str = None,
        is_send: str = None,
        level: str = None,
        occurrence_time: int = None,
        owner_id: str = None,
        product: str = None,
        unique_id: str = None,
        uuid: str = None,
    ):
        # User ID.
        # 
        # This parameter is required.
        self.customer_id = customer_id
        # Data source.
        self.data_source = data_source
        # Event details.
        self.event_description = event_description
        # Alert event details.
        self.event_details = event_details
        # Event name.
        # 
        # This parameter is required.
        self.event_name = event_name
        # Event type.
        # 
        # This parameter is required.
        self.event_type = event_type
        # Alert discovery time.
        # 
        # This parameter is required.
        self.find_time = find_time
        # Instance ID.
        self.instance_id = instance_id
        # Instance name.
        self.instance_name = instance_name
        # Whether to send.
        # 
        # This parameter is required.
        self.is_send = is_send
        # Event level.
        # 
        # This parameter is required.
        self.level = level
        # The first occurrence time of the alert event.
        self.occurrence_time = occurrence_time
        self.owner_id = owner_id
        # Product name.
        self.product = product
        # Unique ID.
        # 
        # This parameter is required.
        self.unique_id = unique_id
        # UUID.
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.customer_id is not None:
            result['CustomerId'] = self.customer_id
        if self.data_source is not None:
            result['DataSource'] = self.data_source
        if self.event_description is not None:
            result['EventDescription'] = self.event_description
        if self.event_details is not None:
            result['EventDetails'] = self.event_details
        if self.event_name is not None:
            result['EventName'] = self.event_name
        if self.event_type is not None:
            result['EventType'] = self.event_type
        if self.find_time is not None:
            result['FindTime'] = self.find_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.is_send is not None:
            result['IsSend'] = self.is_send
        if self.level is not None:
            result['Level'] = self.level
        if self.occurrence_time is not None:
            result['OccurrenceTime'] = self.occurrence_time
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.product is not None:
            result['Product'] = self.product
        if self.unique_id is not None:
            result['UniqueId'] = self.unique_id
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomerId') is not None:
            self.customer_id = m.get('CustomerId')
        if m.get('DataSource') is not None:
            self.data_source = m.get('DataSource')
        if m.get('EventDescription') is not None:
            self.event_description = m.get('EventDescription')
        if m.get('EventDetails') is not None:
            self.event_details = m.get('EventDetails')
        if m.get('EventName') is not None:
            self.event_name = m.get('EventName')
        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')
        if m.get('FindTime') is not None:
            self.find_time = m.get('FindTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('IsSend') is not None:
            self.is_send = m.get('IsSend')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('OccurrenceTime') is not None:
            self.occurrence_time = m.get('OccurrenceTime')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('UniqueId') is not None:
            self.unique_id = m.get('UniqueId')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class SendCustomEventResponseBodyData(TeaModel):
    def __init__(
        self,
        customer_id: str = None,
        customer_name: str = None,
        event_id: str = None,
        event_type: str = None,
        id: int = None,
        owner_id: str = None,
        owner_name: str = None,
        work_task_name: str = None,
    ):
        # Service UID.
        self.customer_id = customer_id
        # Customer name.
        self.customer_name = customer_name
        # Alert ID.
        self.event_id = event_id
        # Alert type.
        self.event_type = event_type
        # Work order ID.
        self.id = id
        # Owner ID.
        self.owner_id = owner_id
        # Owner name.
        self.owner_name = owner_name
        # Work order name.
        self.work_task_name = work_task_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.customer_id is not None:
            result['CustomerId'] = self.customer_id
        if self.customer_name is not None:
            result['CustomerName'] = self.customer_name
        if self.event_id is not None:
            result['EventId'] = self.event_id
        if self.event_type is not None:
            result['EventType'] = self.event_type
        if self.id is not None:
            result['Id'] = self.id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.owner_name is not None:
            result['OwnerName'] = self.owner_name
        if self.work_task_name is not None:
            result['WorkTaskName'] = self.work_task_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomerId') is not None:
            self.customer_id = m.get('CustomerId')
        if m.get('CustomerName') is not None:
            self.customer_name = m.get('CustomerName')
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('OwnerName') is not None:
            self.owner_name = m.get('OwnerName')
        if m.get('WorkTaskName') is not None:
            self.work_task_name = m.get('WorkTaskName')
        return self


class SendCustomEventResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: SendCustomEventResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Interface response code.
        self.code = code
        # Interface return data.
        self.data = data
        # HTTP status code.
        self.http_status_code = http_status_code
        # Return message. When the request is successful, it returns a success message; when the request fails, it returns the reason for the failure.
        self.message = message
        # Request ID.
        # 
        # This parameter is required.
        self.request_id = request_id
        # Whether the call was successful.
        # 
        # - true: Call succeeded.
        # 
        # - false: Call failed.
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
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = SendCustomEventResponseBodyData()
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


class SendCustomEventResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SendCustomEventResponseBody = None,
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
            temp_model = SendCustomEventResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


