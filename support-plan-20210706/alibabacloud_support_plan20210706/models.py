# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class EnterpriseDingtalkGroupMember(TeaModel):
    def __init__(
        self,
        is_admin: bool = None,
        mobile: str = None,
        name: str = None,
    ):
        # 代表资源名称的资源属性字段
        self.is_admin = is_admin
        # 代表资源组的资源属性字段
        self.mobile = mobile
        # 代表创建时间的资源属性字段
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_admin is not None:
            result['IsAdmin'] = self.is_admin
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsAdmin') is not None:
            self.is_admin = m.get('IsAdmin')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class CloseTaskOrderRequest(TeaModel):
    def __init__(
        self,
        order_id: str = None,
        user_name: str = None,
    ):
        # This parameter is required.
        self.order_id = order_id
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class CloseTaskOrderResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # code
        self.code = code
        # data
        self.data = data
        # msg
        self.message = message
        # requestId
        self.request_id = request_id
        # success
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


class CloseTaskOrderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CloseTaskOrderResponseBody = None,
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
            temp_model = CloseTaskOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTaskOrderRequest(TeaModel):
    def __init__(
        self,
        customer_real_name: str = None,
        customer_user_id: str = None,
        important_description: str = None,
        is_important: str = None,
        open_group_id: str = None,
        product_type: str = None,
        product_type_name: str = None,
        task_title: str = None,
    ):
        self.customer_real_name = customer_real_name
        self.customer_user_id = customer_user_id
        self.important_description = important_description
        # This parameter is required.
        self.is_important = is_important
        # This parameter is required.
        self.open_group_id = open_group_id
        # productType
        # 
        # This parameter is required.
        self.product_type = product_type
        self.product_type_name = product_type_name
        # taskTitle
        # 
        # This parameter is required.
        self.task_title = task_title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.customer_real_name is not None:
            result['CustomerRealName'] = self.customer_real_name
        if self.customer_user_id is not None:
            result['CustomerUserId'] = self.customer_user_id
        if self.important_description is not None:
            result['ImportantDescription'] = self.important_description
        if self.is_important is not None:
            result['IsImportant'] = self.is_important
        if self.open_group_id is not None:
            result['OpenGroupId'] = self.open_group_id
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.product_type_name is not None:
            result['ProductTypeName'] = self.product_type_name
        if self.task_title is not None:
            result['TaskTitle'] = self.task_title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomerRealName') is not None:
            self.customer_real_name = m.get('CustomerRealName')
        if m.get('CustomerUserId') is not None:
            self.customer_user_id = m.get('CustomerUserId')
        if m.get('ImportantDescription') is not None:
            self.important_description = m.get('ImportantDescription')
        if m.get('IsImportant') is not None:
            self.is_important = m.get('IsImportant')
        if m.get('OpenGroupId') is not None:
            self.open_group_id = m.get('OpenGroupId')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('ProductTypeName') is not None:
            self.product_type_name = m.get('ProductTypeName')
        if m.get('TaskTitle') is not None:
            self.task_title = m.get('TaskTitle')
        return self


class CreateTaskOrderResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # code
        self.code = code
        self.data = data
        # msg
        self.message = message
        # requestId
        self.request_id = request_id
        # success
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


class CreateTaskOrderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateTaskOrderResponseBody = None,
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
            temp_model = CreateTaskOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTaskOrderByEventReportRequestEventBodyEventLocation(TeaModel):
    def __init__(
        self,
        domain: str = None,
    ):
        self.domain = domain

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        return self


class CreateTaskOrderByEventReportRequestEventBody(TeaModel):
    def __init__(
        self,
        event_desc: str = None,
        event_id: str = None,
        event_level: str = None,
        event_location: CreateTaskOrderByEventReportRequestEventBodyEventLocation = None,
        event_time: str = None,
    ):
        # This parameter is required.
        self.event_desc = event_desc
        self.event_id = event_id
        self.event_level = event_level
        self.event_location = event_location
        self.event_time = event_time

    def validate(self):
        if self.event_location:
            self.event_location.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_desc is not None:
            result['EventDesc'] = self.event_desc
        if self.event_id is not None:
            result['EventId'] = self.event_id
        if self.event_level is not None:
            result['EventLevel'] = self.event_level
        if self.event_location is not None:
            result['EventLocation'] = self.event_location.to_map()
        if self.event_time is not None:
            result['EventTime'] = self.event_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventDesc') is not None:
            self.event_desc = m.get('EventDesc')
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        if m.get('EventLevel') is not None:
            self.event_level = m.get('EventLevel')
        if m.get('EventLocation') is not None:
            temp_model = CreateTaskOrderByEventReportRequestEventBodyEventLocation()
            self.event_location = temp_model.from_map(m['EventLocation'])
        if m.get('EventTime') is not None:
            self.event_time = m.get('EventTime')
        return self


class CreateTaskOrderByEventReportRequestExtinfo(TeaModel):
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


class CreateTaskOrderByEventReportRequest(TeaModel):
    def __init__(
        self,
        business: str = None,
        create_real_name: str = None,
        create_user_id: str = None,
        event_body: CreateTaskOrderByEventReportRequestEventBody = None,
        extinfo: List[CreateTaskOrderByEventReportRequestExtinfo] = None,
        important_desc: str = None,
        join_child_group_user_ids: str = None,
        monitor_congregation: str = None,
        open_group_id: str = None,
        product_type: str = None,
    ):
        self.business = business
        # This parameter is required.
        self.create_real_name = create_real_name
        # This parameter is required.
        self.create_user_id = create_user_id
        self.event_body = event_body
        self.extinfo = extinfo
        self.important_desc = important_desc
        self.join_child_group_user_ids = join_child_group_user_ids
        self.monitor_congregation = monitor_congregation
        # This parameter is required.
        self.open_group_id = open_group_id
        # This parameter is required.
        self.product_type = product_type

    def validate(self):
        if self.event_body:
            self.event_body.validate()
        if self.extinfo:
            for k in self.extinfo:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business is not None:
            result['Business'] = self.business
        if self.create_real_name is not None:
            result['CreateRealName'] = self.create_real_name
        if self.create_user_id is not None:
            result['CreateUserId'] = self.create_user_id
        if self.event_body is not None:
            result['EventBody'] = self.event_body.to_map()
        result['Extinfo'] = []
        if self.extinfo is not None:
            for k in self.extinfo:
                result['Extinfo'].append(k.to_map() if k else None)
        if self.important_desc is not None:
            result['ImportantDesc'] = self.important_desc
        if self.join_child_group_user_ids is not None:
            result['JoinChildGroupUserIds'] = self.join_child_group_user_ids
        if self.monitor_congregation is not None:
            result['MonitorCongregation'] = self.monitor_congregation
        if self.open_group_id is not None:
            result['OpenGroupId'] = self.open_group_id
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Business') is not None:
            self.business = m.get('Business')
        if m.get('CreateRealName') is not None:
            self.create_real_name = m.get('CreateRealName')
        if m.get('CreateUserId') is not None:
            self.create_user_id = m.get('CreateUserId')
        if m.get('EventBody') is not None:
            temp_model = CreateTaskOrderByEventReportRequestEventBody()
            self.event_body = temp_model.from_map(m['EventBody'])
        self.extinfo = []
        if m.get('Extinfo') is not None:
            for k in m.get('Extinfo'):
                temp_model = CreateTaskOrderByEventReportRequestExtinfo()
                self.extinfo.append(temp_model.from_map(k))
        if m.get('ImportantDesc') is not None:
            self.important_desc = m.get('ImportantDesc')
        if m.get('JoinChildGroupUserIds') is not None:
            self.join_child_group_user_ids = m.get('JoinChildGroupUserIds')
        if m.get('MonitorCongregation') is not None:
            self.monitor_congregation = m.get('MonitorCongregation')
        if m.get('OpenGroupId') is not None:
            self.open_group_id = m.get('OpenGroupId')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        return self


class CreateTaskOrderByEventReportShrinkRequest(TeaModel):
    def __init__(
        self,
        business: str = None,
        create_real_name: str = None,
        create_user_id: str = None,
        event_body_shrink: str = None,
        extinfo_shrink: str = None,
        important_desc: str = None,
        join_child_group_user_ids: str = None,
        monitor_congregation: str = None,
        open_group_id: str = None,
        product_type: str = None,
    ):
        self.business = business
        # This parameter is required.
        self.create_real_name = create_real_name
        # This parameter is required.
        self.create_user_id = create_user_id
        self.event_body_shrink = event_body_shrink
        self.extinfo_shrink = extinfo_shrink
        self.important_desc = important_desc
        self.join_child_group_user_ids = join_child_group_user_ids
        self.monitor_congregation = monitor_congregation
        # This parameter is required.
        self.open_group_id = open_group_id
        # This parameter is required.
        self.product_type = product_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business is not None:
            result['Business'] = self.business
        if self.create_real_name is not None:
            result['CreateRealName'] = self.create_real_name
        if self.create_user_id is not None:
            result['CreateUserId'] = self.create_user_id
        if self.event_body_shrink is not None:
            result['EventBody'] = self.event_body_shrink
        if self.extinfo_shrink is not None:
            result['Extinfo'] = self.extinfo_shrink
        if self.important_desc is not None:
            result['ImportantDesc'] = self.important_desc
        if self.join_child_group_user_ids is not None:
            result['JoinChildGroupUserIds'] = self.join_child_group_user_ids
        if self.monitor_congregation is not None:
            result['MonitorCongregation'] = self.monitor_congregation
        if self.open_group_id is not None:
            result['OpenGroupId'] = self.open_group_id
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Business') is not None:
            self.business = m.get('Business')
        if m.get('CreateRealName') is not None:
            self.create_real_name = m.get('CreateRealName')
        if m.get('CreateUserId') is not None:
            self.create_user_id = m.get('CreateUserId')
        if m.get('EventBody') is not None:
            self.event_body_shrink = m.get('EventBody')
        if m.get('Extinfo') is not None:
            self.extinfo_shrink = m.get('Extinfo')
        if m.get('ImportantDesc') is not None:
            self.important_desc = m.get('ImportantDesc')
        if m.get('JoinChildGroupUserIds') is not None:
            self.join_child_group_user_ids = m.get('JoinChildGroupUserIds')
        if m.get('MonitorCongregation') is not None:
            self.monitor_congregation = m.get('MonitorCongregation')
        if m.get('OpenGroupId') is not None:
            self.open_group_id = m.get('OpenGroupId')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        return self


class CreateTaskOrderByEventReportResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # code
        self.code = code
        self.data = data
        # msg
        self.message = message
        # requestId
        self.request_id = request_id
        # success
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


class CreateTaskOrderByEventReportResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateTaskOrderByEventReportResponseBody = None,
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
            temp_model = CreateTaskOrderByEventReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteEnterpriseDingtalkGroupCustomerMemberRequest(TeaModel):
    def __init__(
        self,
        mobiles: List[str] = None,
        open_group_id: str = None,
    ):
        # This parameter is required.
        self.mobiles = mobiles
        # This parameter is required.
        self.open_group_id = open_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mobiles is not None:
            result['Mobiles'] = self.mobiles
        if self.open_group_id is not None:
            result['OpenGroupId'] = self.open_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Mobiles') is not None:
            self.mobiles = m.get('Mobiles')
        if m.get('OpenGroupId') is not None:
            self.open_group_id = m.get('OpenGroupId')
        return self


class DeleteEnterpriseDingtalkGroupCustomerMemberShrinkRequest(TeaModel):
    def __init__(
        self,
        mobiles_shrink: str = None,
        open_group_id: str = None,
    ):
        # This parameter is required.
        self.mobiles_shrink = mobiles_shrink
        # This parameter is required.
        self.open_group_id = open_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mobiles_shrink is not None:
            result['Mobiles'] = self.mobiles_shrink
        if self.open_group_id is not None:
            result['OpenGroupId'] = self.open_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Mobiles') is not None:
            self.mobiles_shrink = m.get('Mobiles')
        if m.get('OpenGroupId') is not None:
            self.open_group_id = m.get('OpenGroupId')
        return self


class DeleteEnterpriseDingtalkGroupCustomerMemberResponseBody(TeaModel):
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


class DeleteEnterpriseDingtalkGroupCustomerMemberResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteEnterpriseDingtalkGroupCustomerMemberResponseBody = None,
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
            temp_model = DeleteEnterpriseDingtalkGroupCustomerMemberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetEnterpriseDingtalkGroupRequest(TeaModel):
    def __init__(
        self,
        open_group_id: str = None,
    ):
        # This parameter is required.
        self.open_group_id = open_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.open_group_id is not None:
            result['OpenGroupId'] = self.open_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OpenGroupId') is not None:
            self.open_group_id = m.get('OpenGroupId')
        return self


class GetEnterpriseDingtalkGroupResponseBodyData(TeaModel):
    def __init__(
        self,
        group_name: str = None,
        open_group_id: str = None,
    ):
        self.group_name = group_name
        self.open_group_id = open_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.open_group_id is not None:
            result['OpenGroupId'] = self.open_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('OpenGroupId') is not None:
            self.open_group_id = m.get('OpenGroupId')
        return self


class GetEnterpriseDingtalkGroupResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetEnterpriseDingtalkGroupResponseBodyData = None,
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
            temp_model = GetEnterpriseDingtalkGroupResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetEnterpriseDingtalkGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetEnterpriseDingtalkGroupResponseBody = None,
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
            temp_model = GetEnterpriseDingtalkGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetEnterpriseDingtalkGroupCustomerMemberRequest(TeaModel):
    def __init__(
        self,
        mobile: str = None,
        open_group_id: str = None,
    ):
        # This parameter is required.
        self.mobile = mobile
        # This parameter is required.
        self.open_group_id = open_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.open_group_id is not None:
            result['OpenGroupId'] = self.open_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('OpenGroupId') is not None:
            self.open_group_id = m.get('OpenGroupId')
        return self


class GetEnterpriseDingtalkGroupCustomerMemberResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: EnterpriseDingtalkGroupMember = None,
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
            temp_model = EnterpriseDingtalkGroupMember()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetEnterpriseDingtalkGroupCustomerMemberResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetEnterpriseDingtalkGroupCustomerMemberResponseBody = None,
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
            temp_model = GetEnterpriseDingtalkGroupCustomerMemberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDdTaskOrderRequest(TeaModel):
    def __init__(
        self,
        caller_parent_id: int = None,
        caller_type: str = None,
        caller_uid: int = None,
        create_real_name: str = None,
        end_time: str = None,
        open_group_id: str = None,
        order_id: str = None,
        page_no: str = None,
        page_size: str = None,
        request_id: str = None,
        start_time: str = None,
        task_status: str = None,
    ):
        # callerParentId
        self.caller_parent_id = caller_parent_id
        # callerType
        self.caller_type = caller_type
        # callerUid
        self.caller_uid = caller_uid
        # createRealName
        self.create_real_name = create_real_name
        # endTime
        self.end_time = end_time
        # openGroupId
        self.open_group_id = open_group_id
        # orderId
        self.order_id = order_id
        # pageNo
        self.page_no = page_no
        # pageSize
        self.page_size = page_size
        # requestId
        self.request_id = request_id
        # startTime
        self.start_time = start_time
        # taskStatus
        self.task_status = task_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.caller_parent_id is not None:
            result['CallerParentId'] = self.caller_parent_id
        if self.caller_type is not None:
            result['CallerType'] = self.caller_type
        if self.caller_uid is not None:
            result['CallerUid'] = self.caller_uid
        if self.create_real_name is not None:
            result['CreateRealName'] = self.create_real_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.open_group_id is not None:
            result['OpenGroupId'] = self.open_group_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallerParentId') is not None:
            self.caller_parent_id = m.get('CallerParentId')
        if m.get('CallerType') is not None:
            self.caller_type = m.get('CallerType')
        if m.get('CallerUid') is not None:
            self.caller_uid = m.get('CallerUid')
        if m.get('CreateRealName') is not None:
            self.create_real_name = m.get('CreateRealName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('OpenGroupId') is not None:
            self.open_group_id = m.get('OpenGroupId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        return self


class ListDdTaskOrderResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # code
        self.code = code
        # data
        self.data = data
        # msg
        self.message = message
        # requestId
        self.request_id = request_id
        # success
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


class ListDdTaskOrderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDdTaskOrderResponseBody = None,
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
            temp_model = ListDdTaskOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEnterpriseDingtalkGroupCustomerMembersRequest(TeaModel):
    def __init__(
        self,
        open_group_id: str = None,
    ):
        # This parameter is required.
        self.open_group_id = open_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.open_group_id is not None:
            result['OpenGroupId'] = self.open_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OpenGroupId') is not None:
            self.open_group_id = m.get('OpenGroupId')
        return self


class ListEnterpriseDingtalkGroupCustomerMembersResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[EnterpriseDingtalkGroupMember] = None,
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
                temp_model = EnterpriseDingtalkGroupMember()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListEnterpriseDingtalkGroupCustomerMembersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListEnterpriseDingtalkGroupCustomerMembersResponseBody = None,
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
            temp_model = ListEnterpriseDingtalkGroupCustomerMembersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEnterpriseDingtalkGroupsResponseBodyData(TeaModel):
    def __init__(
        self,
        group_name: str = None,
        open_group_id: str = None,
    ):
        self.group_name = group_name
        self.open_group_id = open_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.open_group_id is not None:
            result['OpenGroupId'] = self.open_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('OpenGroupId') is not None:
            self.open_group_id = m.get('OpenGroupId')
        return self


class ListEnterpriseDingtalkGroupsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[ListEnterpriseDingtalkGroupsResponseBodyData] = None,
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
                temp_model = ListEnterpriseDingtalkGroupsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListEnterpriseDingtalkGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListEnterpriseDingtalkGroupsResponseBody = None,
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
            temp_model = ListEnterpriseDingtalkGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProductByGroupRequest(TeaModel):
    def __init__(
        self,
        open_group_id: str = None,
    ):
        # This parameter is required.
        self.open_group_id = open_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.open_group_id is not None:
            result['OpenGroupId'] = self.open_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OpenGroupId') is not None:
            self.open_group_id = m.get('OpenGroupId')
        return self


class ListProductByGroupResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # code
        self.code = code
        # data
        self.data = data
        # msg
        self.message = message
        # requestId
        self.request_id = request_id
        # success
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


class ListProductByGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListProductByGroupResponseBody = None,
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
            temp_model = ListProductByGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTaskInfoRequest(TeaModel):
    def __init__(
        self,
        order_id: str = None,
    ):
        # The ID of the order.
        # 
        # This parameter is required.
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class QueryTaskInfoResponseBodyData(TeaModel):
    def __init__(
        self,
        order_id: str = None,
        task_status: str = None,
    ):
        self.order_id = order_id
        self.task_status = task_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        return self


class QueryTaskInfoResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: QueryTaskInfoResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The status code or error code.
        self.code = code
        # The data returned.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request is successful.
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
            temp_model = QueryTaskInfoResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryTaskInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryTaskInfoResponseBody = None,
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
            temp_model = QueryTaskInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReplyMessageApiRequest(TeaModel):
    def __init__(
        self,
        msg_content: str = None,
        msg_type: str = None,
        open_group_id: str = None,
        order_id: str = None,
        user_id: str = None,
        user_name: str = None,
    ):
        # This parameter is required.
        self.msg_content = msg_content
        self.msg_type = msg_type
        self.open_group_id = open_group_id
        # This parameter is required.
        self.order_id = order_id
        self.user_id = user_id
        # This parameter is required.
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.msg_content is not None:
            result['MsgContent'] = self.msg_content
        if self.msg_type is not None:
            result['MsgType'] = self.msg_type
        if self.open_group_id is not None:
            result['OpenGroupId'] = self.open_group_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MsgContent') is not None:
            self.msg_content = m.get('MsgContent')
        if m.get('MsgType') is not None:
            self.msg_type = m.get('MsgType')
        if m.get('OpenGroupId') is not None:
            self.open_group_id = m.get('OpenGroupId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class ReplyMessageApiResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # code
        self.code = code
        # data
        self.data = data
        # msg
        self.message = message
        # requestId
        self.request_id = request_id
        # success
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


class ReplyMessageApiResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ReplyMessageApiResponseBody = None,
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
            temp_model = ReplyMessageApiResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RestOpenTaskOrderRequest(TeaModel):
    def __init__(
        self,
        open_group_id: str = None,
        order_id: str = None,
        reset_content: str = None,
        reset_type: str = None,
        user_name: str = None,
    ):
        self.open_group_id = open_group_id
        # This parameter is required.
        self.order_id = order_id
        self.reset_content = reset_content
        self.reset_type = reset_type
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.open_group_id is not None:
            result['OpenGroupId'] = self.open_group_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.reset_content is not None:
            result['ResetContent'] = self.reset_content
        if self.reset_type is not None:
            result['ResetType'] = self.reset_type
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OpenGroupId') is not None:
            self.open_group_id = m.get('OpenGroupId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('ResetContent') is not None:
            self.reset_content = m.get('ResetContent')
        if m.get('ResetType') is not None:
            self.reset_type = m.get('ResetType')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class RestOpenTaskOrderResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
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


class RestOpenTaskOrderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RestOpenTaskOrderResponseBody = None,
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
            temp_model = RestOpenTaskOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


