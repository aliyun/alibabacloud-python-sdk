# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List, Any


class ActivateLicenseRequest(TeaModel):
    def __init__(
        self,
        identification: str = None,
        license_code: str = None,
    ):
        self.identification = identification
        # This parameter is required.
        self.license_code = license_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.identification is not None:
            result['Identification'] = self.identification
        if self.license_code is not None:
            result['LicenseCode'] = self.license_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Identification') is not None:
            self.identification = m.get('Identification')
        if m.get('LicenseCode') is not None:
            self.license_code = m.get('LicenseCode')
        return self


class ActivateLicenseResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
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
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ActivateLicenseResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ActivateLicenseResponseBody = None,
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
            temp_model = ActivateLicenseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AutoRenewInstanceRequest(TeaModel):
    def __init__(
        self,
        auto_renew_cycle: str = None,
        auto_renew_duration: int = None,
        order_biz_id: int = None,
        owner_id: int = None,
        type: str = None,
    ):
        self.auto_renew_cycle = auto_renew_cycle
        self.auto_renew_duration = auto_renew_duration
        # This parameter is required.
        self.order_biz_id = order_biz_id
        self.owner_id = owner_id
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_renew_cycle is not None:
            result['AutoRenewCycle'] = self.auto_renew_cycle
        if self.auto_renew_duration is not None:
            result['AutoRenewDuration'] = self.auto_renew_duration
        if self.order_biz_id is not None:
            result['OrderBizId'] = self.order_biz_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoRenewCycle') is not None:
            self.auto_renew_cycle = m.get('AutoRenewCycle')
        if m.get('AutoRenewDuration') is not None:
            self.auto_renew_duration = m.get('AutoRenewDuration')
        if m.get('OrderBizId') is not None:
            self.order_biz_id = m.get('OrderBizId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class AutoRenewInstanceResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AutoRenewInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AutoRenewInstanceResponseBody = None,
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
            temp_model = AutoRenewInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateOrderRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        commodity: str = None,
        order_souce: str = None,
        order_type: str = None,
        owner_id: str = None,
        payment_type: str = None,
    ):
        # This parameter is required.
        self.client_token = client_token
        # This parameter is required.
        self.commodity = commodity
        self.order_souce = order_souce
        # This parameter is required.
        self.order_type = order_type
        self.owner_id = owner_id
        # This parameter is required.
        self.payment_type = payment_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.commodity is not None:
            result['Commodity'] = self.commodity
        if self.order_souce is not None:
            result['OrderSouce'] = self.order_souce
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.payment_type is not None:
            result['PaymentType'] = self.payment_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Commodity') is not None:
            self.commodity = m.get('Commodity')
        if m.get('OrderSouce') is not None:
            self.order_souce = m.get('OrderSouce')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PaymentType') is not None:
            self.payment_type = m.get('PaymentType')
        return self


class CreateOrderResponseBodyInstanceIds(TeaModel):
    def __init__(
        self,
        instance_id: List[str] = None,
    ):
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class CreateOrderResponseBody(TeaModel):
    def __init__(
        self,
        instance_ids: CreateOrderResponseBodyInstanceIds = None,
        order_id: str = None,
        request_id: str = None,
    ):
        self.instance_ids = instance_ids
        self.order_id = order_id
        self.request_id = request_id

    def validate(self):
        if self.instance_ids:
            self.instance_ids.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids.to_map()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceIds') is not None:
            temp_model = CreateOrderResponseBodyInstanceIds()
            self.instance_ids = temp_model.from_map(m['InstanceIds'])
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateOrderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateOrderResponseBody = None,
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
            temp_model = CreateOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CrossAccountVerifyTokenRequest(TeaModel):
    def __init__(
        self,
        token: str = None,
    ):
        self.token = token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.token is not None:
            result['Token'] = self.token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Token') is not None:
            self.token = m.get('Token')
        return self


class CrossAccountVerifyTokenResponseBodyResult(TeaModel):
    def __init__(
        self,
        auth_roles: List[str] = None,
        auth_time: int = None,
        name: str = None,
        uid: str = None,
    ):
        self.auth_roles = auth_roles
        self.auth_time = auth_time
        self.name = name
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_roles is not None:
            result['AuthRoles'] = self.auth_roles
        if self.auth_time is not None:
            result['AuthTime'] = self.auth_time
        if self.name is not None:
            result['Name'] = self.name
        if self.uid is not None:
            result['Uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthRoles') is not None:
            self.auth_roles = m.get('AuthRoles')
        if m.get('AuthTime') is not None:
            self.auth_time = m.get('AuthTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        return self


class CrossAccountVerifyTokenResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: CrossAccountVerifyTokenResponseBodyResult = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        # RequestId
        self.request_id = request_id
        self.result = result
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

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
        if self.result is not None:
            result['Result'] = self.result.to_map()
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
        if m.get('Result') is not None:
            temp_model = CrossAccountVerifyTokenResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CrossAccountVerifyTokenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CrossAccountVerifyTokenResponseBody = None,
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
            temp_model = CrossAccountVerifyTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeApiMeteringRequest(TeaModel):
    def __init__(
        self,
        page_num: int = None,
        product_code: str = None,
        type: int = None,
    ):
        # This parameter is required.
        self.page_num = page_num
        self.product_code = product_code
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.product_code is not None:
            result['productCode'] = self.product_code
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('productCode') is not None:
            self.product_code = m.get('productCode')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class DescribeApiMeteringResponseBodyResult(TeaModel):
    def __init__(
        self,
        aliyun_pk: int = None,
        product_code: str = None,
        product_name: str = None,
        total_capacity: int = None,
        total_quota: int = None,
        total_usage: int = None,
        unit: str = None,
    ):
        self.aliyun_pk = aliyun_pk
        self.product_code = product_code
        self.product_name = product_name
        self.total_capacity = total_capacity
        self.total_quota = total_quota
        self.total_usage = total_usage
        self.unit = unit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aliyun_pk is not None:
            result['AliyunPk'] = self.aliyun_pk
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        if self.total_capacity is not None:
            result['TotalCapacity'] = self.total_capacity
        if self.total_quota is not None:
            result['TotalQuota'] = self.total_quota
        if self.total_usage is not None:
            result['TotalUsage'] = self.total_usage
        if self.unit is not None:
            result['Unit'] = self.unit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunPk') is not None:
            self.aliyun_pk = m.get('AliyunPk')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        if m.get('TotalCapacity') is not None:
            self.total_capacity = m.get('TotalCapacity')
        if m.get('TotalQuota') is not None:
            self.total_quota = m.get('TotalQuota')
        if m.get('TotalUsage') is not None:
            self.total_usage = m.get('TotalUsage')
        if m.get('Unit') is not None:
            self.unit = m.get('Unit')
        return self


class DescribeApiMeteringResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        count: int = None,
        fatal: bool = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        result: List[DescribeApiMeteringResponseBodyResult] = None,
        success: bool = None,
        version: str = None,
    ):
        self.code = code
        self.count = count
        # fatal
        self.fatal = fatal
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.result = result
        self.success = success
        self.version = version

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.count is not None:
            result['Count'] = self.count
        if self.fatal is not None:
            result['Fatal'] = self.fatal
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Fatal') is not None:
            self.fatal = m.get('Fatal')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = DescribeApiMeteringResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class DescribeApiMeteringResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeApiMeteringResponseBody = None,
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
            temp_model = DescribeApiMeteringResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCurrentNodeInfoRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DescribeCurrentNodeInfoResponseBodyResult(TeaModel):
    def __init__(
        self,
        allow_rollback_node: bool = None,
        auto_finish_node: bool = None,
        final_step_no: int = None,
        gmt_expired: int = None,
        gmt_finished: int = None,
        gmt_start: int = None,
        need_attachment: bool = None,
        next_node_id: int = None,
        node_id: int = None,
        node_name: str = None,
        node_status: str = None,
        operator_role: str = None,
        parent_node_id: int = None,
        previous_node_id: int = None,
        step_no: int = None,
        template_form: str = None,
    ):
        self.allow_rollback_node = allow_rollback_node
        self.auto_finish_node = auto_finish_node
        self.final_step_no = final_step_no
        self.gmt_expired = gmt_expired
        self.gmt_finished = gmt_finished
        self.gmt_start = gmt_start
        self.need_attachment = need_attachment
        self.next_node_id = next_node_id
        self.node_id = node_id
        self.node_name = node_name
        self.node_status = node_status
        self.operator_role = operator_role
        self.parent_node_id = parent_node_id
        self.previous_node_id = previous_node_id
        self.step_no = step_no
        self.template_form = template_form

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_rollback_node is not None:
            result['AllowRollbackNode'] = self.allow_rollback_node
        if self.auto_finish_node is not None:
            result['AutoFinishNode'] = self.auto_finish_node
        if self.final_step_no is not None:
            result['FinalStepNo'] = self.final_step_no
        if self.gmt_expired is not None:
            result['GmtExpired'] = self.gmt_expired
        if self.gmt_finished is not None:
            result['GmtFinished'] = self.gmt_finished
        if self.gmt_start is not None:
            result['GmtStart'] = self.gmt_start
        if self.need_attachment is not None:
            result['NeedAttachment'] = self.need_attachment
        if self.next_node_id is not None:
            result['NextNodeId'] = self.next_node_id
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.node_name is not None:
            result['NodeName'] = self.node_name
        if self.node_status is not None:
            result['NodeStatus'] = self.node_status
        if self.operator_role is not None:
            result['OperatorRole'] = self.operator_role
        if self.parent_node_id is not None:
            result['ParentNodeId'] = self.parent_node_id
        if self.previous_node_id is not None:
            result['PreviousNodeId'] = self.previous_node_id
        if self.step_no is not None:
            result['StepNo'] = self.step_no
        if self.template_form is not None:
            result['TemplateForm'] = self.template_form
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowRollbackNode') is not None:
            self.allow_rollback_node = m.get('AllowRollbackNode')
        if m.get('AutoFinishNode') is not None:
            self.auto_finish_node = m.get('AutoFinishNode')
        if m.get('FinalStepNo') is not None:
            self.final_step_no = m.get('FinalStepNo')
        if m.get('GmtExpired') is not None:
            self.gmt_expired = m.get('GmtExpired')
        if m.get('GmtFinished') is not None:
            self.gmt_finished = m.get('GmtFinished')
        if m.get('GmtStart') is not None:
            self.gmt_start = m.get('GmtStart')
        if m.get('NeedAttachment') is not None:
            self.need_attachment = m.get('NeedAttachment')
        if m.get('NextNodeId') is not None:
            self.next_node_id = m.get('NextNodeId')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')
        if m.get('NodeStatus') is not None:
            self.node_status = m.get('NodeStatus')
        if m.get('OperatorRole') is not None:
            self.operator_role = m.get('OperatorRole')
        if m.get('ParentNodeId') is not None:
            self.parent_node_id = m.get('ParentNodeId')
        if m.get('PreviousNodeId') is not None:
            self.previous_node_id = m.get('PreviousNodeId')
        if m.get('StepNo') is not None:
            self.step_no = m.get('StepNo')
        if m.get('TemplateForm') is not None:
            self.template_form = m.get('TemplateForm')
        return self


class DescribeCurrentNodeInfoResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: DescribeCurrentNodeInfoResponseBodyResult = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.result = result
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = DescribeCurrentNodeInfoResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeCurrentNodeInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeCurrentNodeInfoResponseBody = None,
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
            temp_model = DescribeCurrentNodeInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDistributionProductsRequestFilter(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # This parameter is required.
        self.key = key
        # This parameter is required.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeDistributionProductsRequest(TeaModel):
    def __init__(
        self,
        filter: List[DescribeDistributionProductsRequestFilter] = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.filter = filter
        # This parameter is required.
        self.page_number = page_number
        # This parameter is required.
        self.page_size = page_size

    def validate(self):
        if self.filter:
            for k in self.filter:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Filter'] = []
        if self.filter is not None:
            for k in self.filter:
                result['Filter'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.filter = []
        if m.get('Filter') is not None:
            for k in m.get('Filter'):
                temp_model = DescribeDistributionProductsRequestFilter()
                self.filter.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeDistributionProductsResponseBodyResults(TeaModel):
    def __init__(
        self,
        code: str = None,
        first_category_name: str = None,
        image_url: str = None,
        name: str = None,
        price: str = None,
        score: str = None,
        second_category_name: str = None,
        short_description: str = None,
        submission_radio: str = None,
        supplier_name: str = None,
        supplier_uid: str = None,
        trade_count: str = None,
        type: str = None,
        user_comment_count: str = None,
    ):
        self.code = code
        self.first_category_name = first_category_name
        self.image_url = image_url
        self.name = name
        self.price = price
        self.score = score
        self.second_category_name = second_category_name
        self.short_description = short_description
        self.submission_radio = submission_radio
        self.supplier_name = supplier_name
        self.supplier_uid = supplier_uid
        self.trade_count = trade_count
        self.type = type
        self.user_comment_count = user_comment_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.first_category_name is not None:
            result['FirstCategoryName'] = self.first_category_name
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.name is not None:
            result['Name'] = self.name
        if self.price is not None:
            result['Price'] = self.price
        if self.score is not None:
            result['Score'] = self.score
        if self.second_category_name is not None:
            result['SecondCategoryName'] = self.second_category_name
        if self.short_description is not None:
            result['ShortDescription'] = self.short_description
        if self.submission_radio is not None:
            result['SubmissionRadio'] = self.submission_radio
        if self.supplier_name is not None:
            result['SupplierName'] = self.supplier_name
        if self.supplier_uid is not None:
            result['SupplierUId'] = self.supplier_uid
        if self.trade_count is not None:
            result['TradeCount'] = self.trade_count
        if self.type is not None:
            result['Type'] = self.type
        if self.user_comment_count is not None:
            result['UserCommentCount'] = self.user_comment_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('FirstCategoryName') is not None:
            self.first_category_name = m.get('FirstCategoryName')
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Price') is not None:
            self.price = m.get('Price')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('SecondCategoryName') is not None:
            self.second_category_name = m.get('SecondCategoryName')
        if m.get('ShortDescription') is not None:
            self.short_description = m.get('ShortDescription')
        if m.get('SubmissionRadio') is not None:
            self.submission_radio = m.get('SubmissionRadio')
        if m.get('SupplierName') is not None:
            self.supplier_name = m.get('SupplierName')
        if m.get('SupplierUId') is not None:
            self.supplier_uid = m.get('SupplierUId')
        if m.get('TradeCount') is not None:
            self.trade_count = m.get('TradeCount')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UserCommentCount') is not None:
            self.user_comment_count = m.get('UserCommentCount')
        return self


class DescribeDistributionProductsResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        results: List[DescribeDistributionProductsResponseBodyResults] = None,
        total_count: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.results = results
        self.total_count = total_count

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.results = []
        if m.get('Results') is not None:
            for k in m.get('Results'):
                temp_model = DescribeDistributionProductsResponseBodyResults()
                self.results.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeDistributionProductsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDistributionProductsResponseBody = None,
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
            temp_model = DescribeDistributionProductsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDistributionProductsLinkRequest(TeaModel):
    def __init__(
        self,
        codes: List[str] = None,
    ):
        # This parameter is required.
        self.codes = codes

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.codes is not None:
            result['Codes'] = self.codes
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Codes') is not None:
            self.codes = m.get('Codes')
        return self


class DescribeDistributionProductsLinkShrinkRequest(TeaModel):
    def __init__(
        self,
        codes_shrink: str = None,
    ):
        # This parameter is required.
        self.codes_shrink = codes_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.codes_shrink is not None:
            result['Codes'] = self.codes_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Codes') is not None:
            self.codes_shrink = m.get('Codes')
        return self


class DescribeDistributionProductsLinkResponseBodyResult(TeaModel):
    def __init__(
        self,
        code: str = None,
        name: str = None,
        url: str = None,
    ):
        self.code = code
        self.name = name
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.name is not None:
            result['Name'] = self.name
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class DescribeDistributionProductsLinkResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[DescribeDistributionProductsLinkResponseBodyResult] = None,
        success: bool = None,
        total_count: int = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.result = result
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = DescribeDistributionProductsLinkResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeDistributionProductsLinkResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDistributionProductsLinkResponseBody = None,
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
            temp_model = DescribeDistributionProductsLinkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        order_type: str = None,
        owner_id: int = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        self.order_type = order_type
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DescribeInstanceResponseBodyModulesModulePropertiesPropertyPropertyValuesPropertyValue(TeaModel):
    def __init__(
        self,
        display_name: str = None,
        max: str = None,
        min: str = None,
        remark: str = None,
        step: str = None,
        type: str = None,
        value: str = None,
    ):
        self.display_name = display_name
        self.max = max
        self.min = min
        self.remark = remark
        self.step = step
        self.type = type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.max is not None:
            result['Max'] = self.max
        if self.min is not None:
            result['Min'] = self.min
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.step is not None:
            result['Step'] = self.step
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Max') is not None:
            self.max = m.get('Max')
        if m.get('Min') is not None:
            self.min = m.get('Min')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('Step') is not None:
            self.step = m.get('Step')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeInstanceResponseBodyModulesModulePropertiesPropertyPropertyValues(TeaModel):
    def __init__(
        self,
        property_value: List[DescribeInstanceResponseBodyModulesModulePropertiesPropertyPropertyValuesPropertyValue] = None,
    ):
        self.property_value = property_value

    def validate(self):
        if self.property_value:
            for k in self.property_value:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PropertyValue'] = []
        if self.property_value is not None:
            for k in self.property_value:
                result['PropertyValue'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.property_value = []
        if m.get('PropertyValue') is not None:
            for k in m.get('PropertyValue'):
                temp_model = DescribeInstanceResponseBodyModulesModulePropertiesPropertyPropertyValuesPropertyValue()
                self.property_value.append(temp_model.from_map(k))
        return self


class DescribeInstanceResponseBodyModulesModulePropertiesProperty(TeaModel):
    def __init__(
        self,
        display_unit: str = None,
        key: str = None,
        name: str = None,
        property_values: DescribeInstanceResponseBodyModulesModulePropertiesPropertyPropertyValues = None,
        show_type: str = None,
    ):
        self.display_unit = display_unit
        self.key = key
        self.name = name
        self.property_values = property_values
        self.show_type = show_type

    def validate(self):
        if self.property_values:
            self.property_values.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display_unit is not None:
            result['DisplayUnit'] = self.display_unit
        if self.key is not None:
            result['Key'] = self.key
        if self.name is not None:
            result['Name'] = self.name
        if self.property_values is not None:
            result['PropertyValues'] = self.property_values.to_map()
        if self.show_type is not None:
            result['ShowType'] = self.show_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayUnit') is not None:
            self.display_unit = m.get('DisplayUnit')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PropertyValues') is not None:
            temp_model = DescribeInstanceResponseBodyModulesModulePropertiesPropertyPropertyValues()
            self.property_values = temp_model.from_map(m['PropertyValues'])
        if m.get('ShowType') is not None:
            self.show_type = m.get('ShowType')
        return self


class DescribeInstanceResponseBodyModulesModuleProperties(TeaModel):
    def __init__(
        self,
        property: List[DescribeInstanceResponseBodyModulesModulePropertiesProperty] = None,
    ):
        self.property = property

    def validate(self):
        if self.property:
            for k in self.property:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Property'] = []
        if self.property is not None:
            for k in self.property:
                result['Property'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.property = []
        if m.get('Property') is not None:
            for k in m.get('Property'):
                temp_model = DescribeInstanceResponseBodyModulesModulePropertiesProperty()
                self.property.append(temp_model.from_map(k))
        return self


class DescribeInstanceResponseBodyModulesModule(TeaModel):
    def __init__(
        self,
        code: str = None,
        id: str = None,
        name: str = None,
        properties: DescribeInstanceResponseBodyModulesModuleProperties = None,
    ):
        self.code = code
        self.id = id
        self.name = name
        self.properties = properties

    def validate(self):
        if self.properties:
            self.properties.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.properties is not None:
            result['Properties'] = self.properties.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Properties') is not None:
            temp_model = DescribeInstanceResponseBodyModulesModuleProperties()
            self.properties = temp_model.from_map(m['Properties'])
        return self


class DescribeInstanceResponseBodyModules(TeaModel):
    def __init__(
        self,
        module: List[DescribeInstanceResponseBodyModulesModule] = None,
    ):
        self.module = module

    def validate(self):
        if self.module:
            for k in self.module:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Module'] = []
        if self.module is not None:
            for k in self.module:
                result['Module'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.module = []
        if m.get('Module') is not None:
            for k in m.get('Module'):
                temp_model = DescribeInstanceResponseBodyModulesModule()
                self.module.append(temp_model.from_map(k))
        return self


class DescribeInstanceResponseBodyRelationalData(TeaModel):
    def __init__(
        self,
        service_status: str = None,
    ):
        self.service_status = service_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_status is not None:
            result['ServiceStatus'] = self.service_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceStatus') is not None:
            self.service_status = m.get('ServiceStatus')
        return self


class DescribeInstanceResponseBody(TeaModel):
    def __init__(
        self,
        active_address: str = None,
        app_json: str = None,
        auto_renewal: str = None,
        began_on: int = None,
        component_json: str = None,
        constraints: str = None,
        created_on: int = None,
        end_on: int = None,
        extend_json: str = None,
        host_json: str = None,
        instance_id: int = None,
        is_trial: bool = None,
        license_code: str = None,
        modules: DescribeInstanceResponseBodyModules = None,
        order_id: int = None,
        product_code: str = None,
        product_name: str = None,
        product_sku_code: str = None,
        product_type: str = None,
        relational_data: DescribeInstanceResponseBodyRelationalData = None,
        status: str = None,
        supplier_name: str = None,
    ):
        self.active_address = active_address
        self.app_json = app_json
        self.auto_renewal = auto_renewal
        self.began_on = began_on
        self.component_json = component_json
        self.constraints = constraints
        self.created_on = created_on
        self.end_on = end_on
        self.extend_json = extend_json
        self.host_json = host_json
        self.instance_id = instance_id
        self.is_trial = is_trial
        self.license_code = license_code
        self.modules = modules
        self.order_id = order_id
        self.product_code = product_code
        self.product_name = product_name
        self.product_sku_code = product_sku_code
        self.product_type = product_type
        self.relational_data = relational_data
        self.status = status
        self.supplier_name = supplier_name

    def validate(self):
        if self.modules:
            self.modules.validate()
        if self.relational_data:
            self.relational_data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active_address is not None:
            result['ActiveAddress'] = self.active_address
        if self.app_json is not None:
            result['AppJson'] = self.app_json
        if self.auto_renewal is not None:
            result['AutoRenewal'] = self.auto_renewal
        if self.began_on is not None:
            result['BeganOn'] = self.began_on
        if self.component_json is not None:
            result['ComponentJson'] = self.component_json
        if self.constraints is not None:
            result['Constraints'] = self.constraints
        if self.created_on is not None:
            result['CreatedOn'] = self.created_on
        if self.end_on is not None:
            result['EndOn'] = self.end_on
        if self.extend_json is not None:
            result['ExtendJson'] = self.extend_json
        if self.host_json is not None:
            result['HostJson'] = self.host_json
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.is_trial is not None:
            result['IsTrial'] = self.is_trial
        if self.license_code is not None:
            result['LicenseCode'] = self.license_code
        if self.modules is not None:
            result['Modules'] = self.modules.to_map()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        if self.product_sku_code is not None:
            result['ProductSkuCode'] = self.product_sku_code
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.relational_data is not None:
            result['RelationalData'] = self.relational_data.to_map()
        if self.status is not None:
            result['Status'] = self.status
        if self.supplier_name is not None:
            result['SupplierName'] = self.supplier_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActiveAddress') is not None:
            self.active_address = m.get('ActiveAddress')
        if m.get('AppJson') is not None:
            self.app_json = m.get('AppJson')
        if m.get('AutoRenewal') is not None:
            self.auto_renewal = m.get('AutoRenewal')
        if m.get('BeganOn') is not None:
            self.began_on = m.get('BeganOn')
        if m.get('ComponentJson') is not None:
            self.component_json = m.get('ComponentJson')
        if m.get('Constraints') is not None:
            self.constraints = m.get('Constraints')
        if m.get('CreatedOn') is not None:
            self.created_on = m.get('CreatedOn')
        if m.get('EndOn') is not None:
            self.end_on = m.get('EndOn')
        if m.get('ExtendJson') is not None:
            self.extend_json = m.get('ExtendJson')
        if m.get('HostJson') is not None:
            self.host_json = m.get('HostJson')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IsTrial') is not None:
            self.is_trial = m.get('IsTrial')
        if m.get('LicenseCode') is not None:
            self.license_code = m.get('LicenseCode')
        if m.get('Modules') is not None:
            temp_model = DescribeInstanceResponseBodyModules()
            self.modules = temp_model.from_map(m['Modules'])
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        if m.get('ProductSkuCode') is not None:
            self.product_sku_code = m.get('ProductSkuCode')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('RelationalData') is not None:
            temp_model = DescribeInstanceResponseBodyRelationalData()
            self.relational_data = temp_model.from_map(m['RelationalData'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SupplierName') is not None:
            self.supplier_name = m.get('SupplierName')
        return self


class DescribeInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeInstanceResponseBody = None,
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
            temp_model = DescribeInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstancesRequest(TeaModel):
    def __init__(
        self,
        codes: str = None,
        except_codes: str = None,
        page_number: int = None,
        page_size: int = None,
        product_type: str = None,
    ):
        self.codes = codes
        self.except_codes = except_codes
        # This parameter is required.
        self.page_number = page_number
        # This parameter is required.
        self.page_size = page_size
        self.product_type = product_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.codes is not None:
            result['Codes'] = self.codes
        if self.except_codes is not None:
            result['ExceptCodes'] = self.except_codes
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Codes') is not None:
            self.codes = m.get('Codes')
        if m.get('ExceptCodes') is not None:
            self.except_codes = m.get('ExceptCodes')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        return self


class DescribeInstancesResponseBodyInstanceItemsInstanceItem(TeaModel):
    def __init__(
        self,
        api_json: str = None,
        app_json: str = None,
        began_on: int = None,
        created_on: int = None,
        end_on: int = None,
        extend_json: str = None,
        host_json: str = None,
        idaas_json: str = None,
        image_json: str = None,
        instance_id: int = None,
        order_id: int = None,
        product_code: str = None,
        product_name: str = None,
        product_sku_code: str = None,
        product_type: str = None,
        status: str = None,
        supplier_name: str = None,
    ):
        self.api_json = api_json
        self.app_json = app_json
        self.began_on = began_on
        self.created_on = created_on
        self.end_on = end_on
        self.extend_json = extend_json
        self.host_json = host_json
        self.idaas_json = idaas_json
        self.image_json = image_json
        self.instance_id = instance_id
        self.order_id = order_id
        self.product_code = product_code
        self.product_name = product_name
        self.product_sku_code = product_sku_code
        self.product_type = product_type
        self.status = status
        self.supplier_name = supplier_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_json is not None:
            result['ApiJson'] = self.api_json
        if self.app_json is not None:
            result['AppJson'] = self.app_json
        if self.began_on is not None:
            result['BeganOn'] = self.began_on
        if self.created_on is not None:
            result['CreatedOn'] = self.created_on
        if self.end_on is not None:
            result['EndOn'] = self.end_on
        if self.extend_json is not None:
            result['ExtendJson'] = self.extend_json
        if self.host_json is not None:
            result['HostJson'] = self.host_json
        if self.idaas_json is not None:
            result['IdaasJson'] = self.idaas_json
        if self.image_json is not None:
            result['ImageJson'] = self.image_json
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        if self.product_sku_code is not None:
            result['ProductSkuCode'] = self.product_sku_code
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.status is not None:
            result['Status'] = self.status
        if self.supplier_name is not None:
            result['SupplierName'] = self.supplier_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiJson') is not None:
            self.api_json = m.get('ApiJson')
        if m.get('AppJson') is not None:
            self.app_json = m.get('AppJson')
        if m.get('BeganOn') is not None:
            self.began_on = m.get('BeganOn')
        if m.get('CreatedOn') is not None:
            self.created_on = m.get('CreatedOn')
        if m.get('EndOn') is not None:
            self.end_on = m.get('EndOn')
        if m.get('ExtendJson') is not None:
            self.extend_json = m.get('ExtendJson')
        if m.get('HostJson') is not None:
            self.host_json = m.get('HostJson')
        if m.get('IdaasJson') is not None:
            self.idaas_json = m.get('IdaasJson')
        if m.get('ImageJson') is not None:
            self.image_json = m.get('ImageJson')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        if m.get('ProductSkuCode') is not None:
            self.product_sku_code = m.get('ProductSkuCode')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SupplierName') is not None:
            self.supplier_name = m.get('SupplierName')
        return self


class DescribeInstancesResponseBodyInstanceItems(TeaModel):
    def __init__(
        self,
        instance_item: List[DescribeInstancesResponseBodyInstanceItemsInstanceItem] = None,
    ):
        self.instance_item = instance_item

    def validate(self):
        if self.instance_item:
            for k in self.instance_item:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['InstanceItem'] = []
        if self.instance_item is not None:
            for k in self.instance_item:
                result['InstanceItem'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_item = []
        if m.get('InstanceItem') is not None:
            for k in m.get('InstanceItem'):
                temp_model = DescribeInstancesResponseBodyInstanceItemsInstanceItem()
                self.instance_item.append(temp_model.from_map(k))
        return self


class DescribeInstancesResponseBody(TeaModel):
    def __init__(
        self,
        instance_items: DescribeInstancesResponseBodyInstanceItems = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.instance_items = instance_items
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.instance_items:
            self.instance_items.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_items is not None:
            result['InstanceItems'] = self.instance_items.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceItems') is not None:
            temp_model = DescribeInstancesResponseBodyInstanceItems()
            self.instance_items = temp_model.from_map(m['InstanceItems'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeInstancesResponseBody = None,
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
            temp_model = DescribeInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeLicenseRequest(TeaModel):
    def __init__(
        self,
        license_code: str = None,
    ):
        # This parameter is required.
        self.license_code = license_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.license_code is not None:
            result['LicenseCode'] = self.license_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LicenseCode') is not None:
            self.license_code = m.get('LicenseCode')
        return self


class DescribeLicenseResponseBodyLicenseExtendArrayLicenseAttribute(TeaModel):
    def __init__(
        self,
        code: str = None,
        value: str = None,
    ):
        self.code = code
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeLicenseResponseBodyLicenseExtendArray(TeaModel):
    def __init__(
        self,
        license_attribute: List[DescribeLicenseResponseBodyLicenseExtendArrayLicenseAttribute] = None,
    ):
        self.license_attribute = license_attribute

    def validate(self):
        if self.license_attribute:
            for k in self.license_attribute:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['LicenseAttribute'] = []
        if self.license_attribute is not None:
            for k in self.license_attribute:
                result['LicenseAttribute'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.license_attribute = []
        if m.get('LicenseAttribute') is not None:
            for k in m.get('LicenseAttribute'):
                temp_model = DescribeLicenseResponseBodyLicenseExtendArrayLicenseAttribute()
                self.license_attribute.append(temp_model.from_map(k))
        return self


class DescribeLicenseResponseBodyLicenseExtendInfo(TeaModel):
    def __init__(
        self,
        account_quantity: int = None,
        ali_uid: int = None,
        email: str = None,
        mobile: str = None,
    ):
        self.account_quantity = account_quantity
        self.ali_uid = ali_uid
        self.email = email
        self.mobile = mobile

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_quantity is not None:
            result['AccountQuantity'] = self.account_quantity
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.email is not None:
            result['Email'] = self.email
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountQuantity') is not None:
            self.account_quantity = m.get('AccountQuantity')
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        return self


class DescribeLicenseResponseBodyLicense(TeaModel):
    def __init__(
        self,
        activate_time: str = None,
        create_time: str = None,
        expired_time: str = None,
        extend_array: DescribeLicenseResponseBodyLicenseExtendArray = None,
        extend_info: DescribeLicenseResponseBodyLicenseExtendInfo = None,
        instance_id: str = None,
        license_code: str = None,
        license_status: str = None,
        product_code: str = None,
        product_name: str = None,
        product_sku_id: str = None,
        supplier_name: str = None,
    ):
        self.activate_time = activate_time
        self.create_time = create_time
        self.expired_time = expired_time
        self.extend_array = extend_array
        self.extend_info = extend_info
        self.instance_id = instance_id
        self.license_code = license_code
        self.license_status = license_status
        self.product_code = product_code
        self.product_name = product_name
        self.product_sku_id = product_sku_id
        self.supplier_name = supplier_name

    def validate(self):
        if self.extend_array:
            self.extend_array.validate()
        if self.extend_info:
            self.extend_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.activate_time is not None:
            result['ActivateTime'] = self.activate_time
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.extend_array is not None:
            result['ExtendArray'] = self.extend_array.to_map()
        if self.extend_info is not None:
            result['ExtendInfo'] = self.extend_info.to_map()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.license_code is not None:
            result['LicenseCode'] = self.license_code
        if self.license_status is not None:
            result['LicenseStatus'] = self.license_status
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        if self.product_sku_id is not None:
            result['ProductSkuId'] = self.product_sku_id
        if self.supplier_name is not None:
            result['SupplierName'] = self.supplier_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActivateTime') is not None:
            self.activate_time = m.get('ActivateTime')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('ExtendArray') is not None:
            temp_model = DescribeLicenseResponseBodyLicenseExtendArray()
            self.extend_array = temp_model.from_map(m['ExtendArray'])
        if m.get('ExtendInfo') is not None:
            temp_model = DescribeLicenseResponseBodyLicenseExtendInfo()
            self.extend_info = temp_model.from_map(m['ExtendInfo'])
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('LicenseCode') is not None:
            self.license_code = m.get('LicenseCode')
        if m.get('LicenseStatus') is not None:
            self.license_status = m.get('LicenseStatus')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        if m.get('ProductSkuId') is not None:
            self.product_sku_id = m.get('ProductSkuId')
        if m.get('SupplierName') is not None:
            self.supplier_name = m.get('SupplierName')
        return self


class DescribeLicenseResponseBody(TeaModel):
    def __init__(
        self,
        license: DescribeLicenseResponseBodyLicense = None,
        request_id: str = None,
    ):
        self.license = license
        self.request_id = request_id

    def validate(self):
        if self.license:
            self.license.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.license is not None:
            result['License'] = self.license.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('License') is not None:
            temp_model = DescribeLicenseResponseBodyLicense()
            self.license = temp_model.from_map(m['License'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeLicenseResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeLicenseResponseBody = None,
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
            temp_model = DescribeLicenseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeOrderRequest(TeaModel):
    def __init__(
        self,
        order_id: str = None,
    ):
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


class DescribeOrderResponseBodyInstanceIds(TeaModel):
    def __init__(
        self,
        instance_id: List[str] = None,
    ):
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DescribeOrderResponseBodySupplierTelephones(TeaModel):
    def __init__(
        self,
        telephone: List[str] = None,
    ):
        self.telephone = telephone

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.telephone is not None:
            result['Telephone'] = self.telephone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Telephone') is not None:
            self.telephone = m.get('Telephone')
        return self


class DescribeOrderResponseBody(TeaModel):
    def __init__(
        self,
        account_quantity: int = None,
        ali_uid: int = None,
        components: Dict[str, Any] = None,
        coupon_price: float = None,
        created_on: int = None,
        instance_ids: DescribeOrderResponseBodyInstanceIds = None,
        order_id: int = None,
        order_status: str = None,
        order_type: str = None,
        original_price: float = None,
        paid_on: int = None,
        pay_status: str = None,
        payment_price: float = None,
        period_type: str = None,
        product_code: str = None,
        product_name: str = None,
        product_sku_code: str = None,
        quantity: int = None,
        request_id: str = None,
        supplier_company_name: str = None,
        supplier_telephones: DescribeOrderResponseBodySupplierTelephones = None,
        total_price: float = None,
    ):
        self.account_quantity = account_quantity
        self.ali_uid = ali_uid
        self.components = components
        self.coupon_price = coupon_price
        self.created_on = created_on
        self.instance_ids = instance_ids
        self.order_id = order_id
        self.order_status = order_status
        self.order_type = order_type
        self.original_price = original_price
        self.paid_on = paid_on
        self.pay_status = pay_status
        self.payment_price = payment_price
        self.period_type = period_type
        self.product_code = product_code
        self.product_name = product_name
        self.product_sku_code = product_sku_code
        self.quantity = quantity
        self.request_id = request_id
        self.supplier_company_name = supplier_company_name
        self.supplier_telephones = supplier_telephones
        self.total_price = total_price

    def validate(self):
        if self.instance_ids:
            self.instance_ids.validate()
        if self.supplier_telephones:
            self.supplier_telephones.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_quantity is not None:
            result['AccountQuantity'] = self.account_quantity
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.components is not None:
            result['Components'] = self.components
        if self.coupon_price is not None:
            result['CouponPrice'] = self.coupon_price
        if self.created_on is not None:
            result['CreatedOn'] = self.created_on
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids.to_map()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.order_status is not None:
            result['OrderStatus'] = self.order_status
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price
        if self.paid_on is not None:
            result['PaidOn'] = self.paid_on
        if self.pay_status is not None:
            result['PayStatus'] = self.pay_status
        if self.payment_price is not None:
            result['PaymentPrice'] = self.payment_price
        if self.period_type is not None:
            result['PeriodType'] = self.period_type
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        if self.product_sku_code is not None:
            result['ProductSkuCode'] = self.product_sku_code
        if self.quantity is not None:
            result['Quantity'] = self.quantity
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.supplier_company_name is not None:
            result['SupplierCompanyName'] = self.supplier_company_name
        if self.supplier_telephones is not None:
            result['SupplierTelephones'] = self.supplier_telephones.to_map()
        if self.total_price is not None:
            result['TotalPrice'] = self.total_price
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountQuantity') is not None:
            self.account_quantity = m.get('AccountQuantity')
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('Components') is not None:
            self.components = m.get('Components')
        if m.get('CouponPrice') is not None:
            self.coupon_price = m.get('CouponPrice')
        if m.get('CreatedOn') is not None:
            self.created_on = m.get('CreatedOn')
        if m.get('InstanceIds') is not None:
            temp_model = DescribeOrderResponseBodyInstanceIds()
            self.instance_ids = temp_model.from_map(m['InstanceIds'])
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('OrderStatus') is not None:
            self.order_status = m.get('OrderStatus')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        if m.get('OriginalPrice') is not None:
            self.original_price = m.get('OriginalPrice')
        if m.get('PaidOn') is not None:
            self.paid_on = m.get('PaidOn')
        if m.get('PayStatus') is not None:
            self.pay_status = m.get('PayStatus')
        if m.get('PaymentPrice') is not None:
            self.payment_price = m.get('PaymentPrice')
        if m.get('PeriodType') is not None:
            self.period_type = m.get('PeriodType')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        if m.get('ProductSkuCode') is not None:
            self.product_sku_code = m.get('ProductSkuCode')
        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SupplierCompanyName') is not None:
            self.supplier_company_name = m.get('SupplierCompanyName')
        if m.get('SupplierTelephones') is not None:
            temp_model = DescribeOrderResponseBodySupplierTelephones()
            self.supplier_telephones = temp_model.from_map(m['SupplierTelephones'])
        if m.get('TotalPrice') is not None:
            self.total_price = m.get('TotalPrice')
        return self


class DescribeOrderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeOrderResponseBody = None,
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
            temp_model = DescribeOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePriceRequest(TeaModel):
    def __init__(
        self,
        commodity: str = None,
        order_type: str = None,
    ):
        # This parameter is required.
        self.commodity = commodity
        # This parameter is required.
        self.order_type = order_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.commodity is not None:
            result['Commodity'] = self.commodity
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Commodity') is not None:
            self.commodity = m.get('Commodity')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        return self


class DescribePriceResponseBodyCouponsCoupon(TeaModel):
    def __init__(
        self,
        can_prom_fee: float = None,
        coupon_desc: str = None,
        coupon_name: str = None,
        coupon_option_code: str = None,
        coupon_option_no: str = None,
        is_selected: bool = None,
    ):
        self.can_prom_fee = can_prom_fee
        self.coupon_desc = coupon_desc
        self.coupon_name = coupon_name
        self.coupon_option_code = coupon_option_code
        self.coupon_option_no = coupon_option_no
        self.is_selected = is_selected

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.can_prom_fee is not None:
            result['CanPromFee'] = self.can_prom_fee
        if self.coupon_desc is not None:
            result['CouponDesc'] = self.coupon_desc
        if self.coupon_name is not None:
            result['CouponName'] = self.coupon_name
        if self.coupon_option_code is not None:
            result['CouponOptionCode'] = self.coupon_option_code
        if self.coupon_option_no is not None:
            result['CouponOptionNo'] = self.coupon_option_no
        if self.is_selected is not None:
            result['IsSelected'] = self.is_selected
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CanPromFee') is not None:
            self.can_prom_fee = m.get('CanPromFee')
        if m.get('CouponDesc') is not None:
            self.coupon_desc = m.get('CouponDesc')
        if m.get('CouponName') is not None:
            self.coupon_name = m.get('CouponName')
        if m.get('CouponOptionCode') is not None:
            self.coupon_option_code = m.get('CouponOptionCode')
        if m.get('CouponOptionNo') is not None:
            self.coupon_option_no = m.get('CouponOptionNo')
        if m.get('IsSelected') is not None:
            self.is_selected = m.get('IsSelected')
        return self


class DescribePriceResponseBodyCoupons(TeaModel):
    def __init__(
        self,
        coupon: List[DescribePriceResponseBodyCouponsCoupon] = None,
    ):
        self.coupon = coupon

    def validate(self):
        if self.coupon:
            for k in self.coupon:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Coupon'] = []
        if self.coupon is not None:
            for k in self.coupon:
                result['Coupon'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.coupon = []
        if m.get('Coupon') is not None:
            for k in m.get('Coupon'):
                temp_model = DescribePriceResponseBodyCouponsCoupon()
                self.coupon.append(temp_model.from_map(k))
        return self


class DescribePriceResponseBodyPromotionRulesPromotionRule(TeaModel):
    def __init__(
        self,
        name: str = None,
        rule_id: str = None,
        title: str = None,
    ):
        self.name = name
        self.rule_id = rule_id
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class DescribePriceResponseBodyPromotionRules(TeaModel):
    def __init__(
        self,
        promotion_rule: List[DescribePriceResponseBodyPromotionRulesPromotionRule] = None,
    ):
        self.promotion_rule = promotion_rule

    def validate(self):
        if self.promotion_rule:
            for k in self.promotion_rule:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PromotionRule'] = []
        if self.promotion_rule is not None:
            for k in self.promotion_rule:
                result['PromotionRule'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.promotion_rule = []
        if m.get('PromotionRule') is not None:
            for k in m.get('PromotionRule'):
                temp_model = DescribePriceResponseBodyPromotionRulesPromotionRule()
                self.promotion_rule.append(temp_model.from_map(k))
        return self


class DescribePriceResponseBody(TeaModel):
    def __init__(
        self,
        coupons: DescribePriceResponseBodyCoupons = None,
        currency: str = None,
        cuxiao: bool = None,
        cycle: str = None,
        discount_price: float = None,
        duration: int = None,
        expression_code: str = None,
        expression_message: str = None,
        info_title: str = None,
        original_price: float = None,
        product_code: str = None,
        promotion_rules: DescribePriceResponseBodyPromotionRules = None,
        trade_price: float = None,
    ):
        self.coupons = coupons
        self.currency = currency
        self.cuxiao = cuxiao
        self.cycle = cycle
        self.discount_price = discount_price
        self.duration = duration
        self.expression_code = expression_code
        self.expression_message = expression_message
        self.info_title = info_title
        self.original_price = original_price
        self.product_code = product_code
        self.promotion_rules = promotion_rules
        self.trade_price = trade_price

    def validate(self):
        if self.coupons:
            self.coupons.validate()
        if self.promotion_rules:
            self.promotion_rules.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.coupons is not None:
            result['Coupons'] = self.coupons.to_map()
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.cuxiao is not None:
            result['Cuxiao'] = self.cuxiao
        if self.cycle is not None:
            result['Cycle'] = self.cycle
        if self.discount_price is not None:
            result['DiscountPrice'] = self.discount_price
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.expression_code is not None:
            result['ExpressionCode'] = self.expression_code
        if self.expression_message is not None:
            result['ExpressionMessage'] = self.expression_message
        if self.info_title is not None:
            result['InfoTitle'] = self.info_title
        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.promotion_rules is not None:
            result['PromotionRules'] = self.promotion_rules.to_map()
        if self.trade_price is not None:
            result['TradePrice'] = self.trade_price
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Coupons') is not None:
            temp_model = DescribePriceResponseBodyCoupons()
            self.coupons = temp_model.from_map(m['Coupons'])
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('Cuxiao') is not None:
            self.cuxiao = m.get('Cuxiao')
        if m.get('Cycle') is not None:
            self.cycle = m.get('Cycle')
        if m.get('DiscountPrice') is not None:
            self.discount_price = m.get('DiscountPrice')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('ExpressionCode') is not None:
            self.expression_code = m.get('ExpressionCode')
        if m.get('ExpressionMessage') is not None:
            self.expression_message = m.get('ExpressionMessage')
        if m.get('InfoTitle') is not None:
            self.info_title = m.get('InfoTitle')
        if m.get('OriginalPrice') is not None:
            self.original_price = m.get('OriginalPrice')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('PromotionRules') is not None:
            temp_model = DescribePriceResponseBodyPromotionRules()
            self.promotion_rules = temp_model.from_map(m['PromotionRules'])
        if m.get('TradePrice') is not None:
            self.trade_price = m.get('TradePrice')
        return self


class DescribePriceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribePriceResponseBody = None,
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
            temp_model = DescribePriceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeProductRequest(TeaModel):
    def __init__(
        self,
        ali_uid: str = None,
        code: str = None,
        query_draft: bool = None,
    ):
        # AliUid
        self.ali_uid = ali_uid
        # This parameter is required.
        self.code = code
        self.query_draft = query_draft

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.code is not None:
            result['Code'] = self.code
        if self.query_draft is not None:
            result['QueryDraft'] = self.query_draft
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('QueryDraft') is not None:
            self.query_draft = m.get('QueryDraft')
        return self


class DescribeProductResponseBodyProductExtrasProductExtra(TeaModel):
    def __init__(
        self,
        key: str = None,
        label: str = None,
        order: int = None,
        type: str = None,
        values: str = None,
    ):
        self.key = key
        self.label = label
        self.order = order
        self.type = type
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.label is not None:
            result['Label'] = self.label
        if self.order is not None:
            result['Order'] = self.order
        if self.type is not None:
            result['Type'] = self.type
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class DescribeProductResponseBodyProductExtras(TeaModel):
    def __init__(
        self,
        product_extra: List[DescribeProductResponseBodyProductExtrasProductExtra] = None,
    ):
        self.product_extra = product_extra

    def validate(self):
        if self.product_extra:
            for k in self.product_extra:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ProductExtra'] = []
        if self.product_extra is not None:
            for k in self.product_extra:
                result['ProductExtra'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.product_extra = []
        if m.get('ProductExtra') is not None:
            for k in m.get('ProductExtra'):
                temp_model = DescribeProductResponseBodyProductExtrasProductExtra()
                self.product_extra.append(temp_model.from_map(k))
        return self


class DescribeProductResponseBodyProductSkusProductSkuModulesModulePropertiesPropertyPropertyValuesPropertyValue(TeaModel):
    def __init__(
        self,
        display_name: str = None,
        max: str = None,
        min: str = None,
        remark: str = None,
        step: str = None,
        type: str = None,
        value: str = None,
    ):
        self.display_name = display_name
        self.max = max
        self.min = min
        self.remark = remark
        self.step = step
        self.type = type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.max is not None:
            result['Max'] = self.max
        if self.min is not None:
            result['Min'] = self.min
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.step is not None:
            result['Step'] = self.step
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Max') is not None:
            self.max = m.get('Max')
        if m.get('Min') is not None:
            self.min = m.get('Min')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('Step') is not None:
            self.step = m.get('Step')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeProductResponseBodyProductSkusProductSkuModulesModulePropertiesPropertyPropertyValues(TeaModel):
    def __init__(
        self,
        property_value: List[DescribeProductResponseBodyProductSkusProductSkuModulesModulePropertiesPropertyPropertyValuesPropertyValue] = None,
    ):
        self.property_value = property_value

    def validate(self):
        if self.property_value:
            for k in self.property_value:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PropertyValue'] = []
        if self.property_value is not None:
            for k in self.property_value:
                result['PropertyValue'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.property_value = []
        if m.get('PropertyValue') is not None:
            for k in m.get('PropertyValue'):
                temp_model = DescribeProductResponseBodyProductSkusProductSkuModulesModulePropertiesPropertyPropertyValuesPropertyValue()
                self.property_value.append(temp_model.from_map(k))
        return self


class DescribeProductResponseBodyProductSkusProductSkuModulesModulePropertiesProperty(TeaModel):
    def __init__(
        self,
        display_unit: str = None,
        key: str = None,
        name: str = None,
        property_values: DescribeProductResponseBodyProductSkusProductSkuModulesModulePropertiesPropertyPropertyValues = None,
        show_type: str = None,
    ):
        self.display_unit = display_unit
        self.key = key
        self.name = name
        self.property_values = property_values
        self.show_type = show_type

    def validate(self):
        if self.property_values:
            self.property_values.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display_unit is not None:
            result['DisplayUnit'] = self.display_unit
        if self.key is not None:
            result['Key'] = self.key
        if self.name is not None:
            result['Name'] = self.name
        if self.property_values is not None:
            result['PropertyValues'] = self.property_values.to_map()
        if self.show_type is not None:
            result['ShowType'] = self.show_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayUnit') is not None:
            self.display_unit = m.get('DisplayUnit')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PropertyValues') is not None:
            temp_model = DescribeProductResponseBodyProductSkusProductSkuModulesModulePropertiesPropertyPropertyValues()
            self.property_values = temp_model.from_map(m['PropertyValues'])
        if m.get('ShowType') is not None:
            self.show_type = m.get('ShowType')
        return self


class DescribeProductResponseBodyProductSkusProductSkuModulesModuleProperties(TeaModel):
    def __init__(
        self,
        property: List[DescribeProductResponseBodyProductSkusProductSkuModulesModulePropertiesProperty] = None,
    ):
        self.property = property

    def validate(self):
        if self.property:
            for k in self.property:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Property'] = []
        if self.property is not None:
            for k in self.property:
                result['Property'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.property = []
        if m.get('Property') is not None:
            for k in m.get('Property'):
                temp_model = DescribeProductResponseBodyProductSkusProductSkuModulesModulePropertiesProperty()
                self.property.append(temp_model.from_map(k))
        return self


class DescribeProductResponseBodyProductSkusProductSkuModulesModule(TeaModel):
    def __init__(
        self,
        code: str = None,
        id: str = None,
        name: str = None,
        properties: DescribeProductResponseBodyProductSkusProductSkuModulesModuleProperties = None,
    ):
        self.code = code
        self.id = id
        self.name = name
        self.properties = properties

    def validate(self):
        if self.properties:
            self.properties.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.properties is not None:
            result['Properties'] = self.properties.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Properties') is not None:
            temp_model = DescribeProductResponseBodyProductSkusProductSkuModulesModuleProperties()
            self.properties = temp_model.from_map(m['Properties'])
        return self


class DescribeProductResponseBodyProductSkusProductSkuModules(TeaModel):
    def __init__(
        self,
        module: List[DescribeProductResponseBodyProductSkusProductSkuModulesModule] = None,
    ):
        self.module = module

    def validate(self):
        if self.module:
            for k in self.module:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Module'] = []
        if self.module is not None:
            for k in self.module:
                result['Module'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.module = []
        if m.get('Module') is not None:
            for k in m.get('Module'):
                temp_model = DescribeProductResponseBodyProductSkusProductSkuModulesModule()
                self.module.append(temp_model.from_map(k))
        return self


class DescribeProductResponseBodyProductSkusProductSkuOrderPeriodsOrderPeriod(TeaModel):
    def __init__(
        self,
        name: str = None,
        period_type: str = None,
    ):
        self.name = name
        self.period_type = period_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.period_type is not None:
            result['PeriodType'] = self.period_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PeriodType') is not None:
            self.period_type = m.get('PeriodType')
        return self


class DescribeProductResponseBodyProductSkusProductSkuOrderPeriods(TeaModel):
    def __init__(
        self,
        order_period: List[DescribeProductResponseBodyProductSkusProductSkuOrderPeriodsOrderPeriod] = None,
    ):
        self.order_period = order_period

    def validate(self):
        if self.order_period:
            for k in self.order_period:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['OrderPeriod'] = []
        if self.order_period is not None:
            for k in self.order_period:
                result['OrderPeriod'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.order_period = []
        if m.get('OrderPeriod') is not None:
            for k in m.get('OrderPeriod'):
                temp_model = DescribeProductResponseBodyProductSkusProductSkuOrderPeriodsOrderPeriod()
                self.order_period.append(temp_model.from_map(k))
        return self


class DescribeProductResponseBodyProductSkusProductSku(TeaModel):
    def __init__(
        self,
        charge_type: str = None,
        code: str = None,
        constraints: str = None,
        hidden: bool = None,
        modules: DescribeProductResponseBodyProductSkusProductSkuModules = None,
        name: str = None,
        order_periods: DescribeProductResponseBodyProductSkusProductSkuOrderPeriods = None,
    ):
        self.charge_type = charge_type
        self.code = code
        self.constraints = constraints
        self.hidden = hidden
        self.modules = modules
        self.name = name
        self.order_periods = order_periods

    def validate(self):
        if self.modules:
            self.modules.validate()
        if self.order_periods:
            self.order_periods.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.code is not None:
            result['Code'] = self.code
        if self.constraints is not None:
            result['Constraints'] = self.constraints
        if self.hidden is not None:
            result['Hidden'] = self.hidden
        if self.modules is not None:
            result['Modules'] = self.modules.to_map()
        if self.name is not None:
            result['Name'] = self.name
        if self.order_periods is not None:
            result['OrderPeriods'] = self.order_periods.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Constraints') is not None:
            self.constraints = m.get('Constraints')
        if m.get('Hidden') is not None:
            self.hidden = m.get('Hidden')
        if m.get('Modules') is not None:
            temp_model = DescribeProductResponseBodyProductSkusProductSkuModules()
            self.modules = temp_model.from_map(m['Modules'])
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OrderPeriods') is not None:
            temp_model = DescribeProductResponseBodyProductSkusProductSkuOrderPeriods()
            self.order_periods = temp_model.from_map(m['OrderPeriods'])
        return self


class DescribeProductResponseBodyProductSkus(TeaModel):
    def __init__(
        self,
        product_sku: List[DescribeProductResponseBodyProductSkusProductSku] = None,
    ):
        self.product_sku = product_sku

    def validate(self):
        if self.product_sku:
            for k in self.product_sku:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ProductSku'] = []
        if self.product_sku is not None:
            for k in self.product_sku:
                result['ProductSku'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.product_sku = []
        if m.get('ProductSku') is not None:
            for k in m.get('ProductSku'):
                temp_model = DescribeProductResponseBodyProductSkusProductSku()
                self.product_sku.append(temp_model.from_map(k))
        return self


class DescribeProductResponseBodyShopInfoTelephones(TeaModel):
    def __init__(
        self,
        telephone: List[str] = None,
    ):
        self.telephone = telephone

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.telephone is not None:
            result['Telephone'] = self.telephone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Telephone') is not None:
            self.telephone = m.get('Telephone')
        return self


class DescribeProductResponseBodyShopInfoWangWangsWangWang(TeaModel):
    def __init__(
        self,
        remark: str = None,
        user_name: str = None,
    ):
        self.remark = remark
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class DescribeProductResponseBodyShopInfoWangWangs(TeaModel):
    def __init__(
        self,
        wang_wang: List[DescribeProductResponseBodyShopInfoWangWangsWangWang] = None,
    ):
        self.wang_wang = wang_wang

    def validate(self):
        if self.wang_wang:
            for k in self.wang_wang:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['WangWang'] = []
        if self.wang_wang is not None:
            for k in self.wang_wang:
                result['WangWang'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.wang_wang = []
        if m.get('WangWang') is not None:
            for k in m.get('WangWang'):
                temp_model = DescribeProductResponseBodyShopInfoWangWangsWangWang()
                self.wang_wang.append(temp_model.from_map(k))
        return self


class DescribeProductResponseBodyShopInfo(TeaModel):
    def __init__(
        self,
        emails: str = None,
        id: int = None,
        name: str = None,
        telephones: DescribeProductResponseBodyShopInfoTelephones = None,
        wang_wangs: DescribeProductResponseBodyShopInfoWangWangs = None,
    ):
        self.emails = emails
        self.id = id
        self.name = name
        self.telephones = telephones
        self.wang_wangs = wang_wangs

    def validate(self):
        if self.telephones:
            self.telephones.validate()
        if self.wang_wangs:
            self.wang_wangs.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.emails is not None:
            result['Emails'] = self.emails
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.telephones is not None:
            result['Telephones'] = self.telephones.to_map()
        if self.wang_wangs is not None:
            result['WangWangs'] = self.wang_wangs.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Emails') is not None:
            self.emails = m.get('Emails')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Telephones') is not None:
            temp_model = DescribeProductResponseBodyShopInfoTelephones()
            self.telephones = temp_model.from_map(m['Telephones'])
        if m.get('WangWangs') is not None:
            temp_model = DescribeProductResponseBodyShopInfoWangWangs()
            self.wang_wangs = temp_model.from_map(m['WangWangs'])
        return self


class DescribeProductResponseBody(TeaModel):
    def __init__(
        self,
        audit_fail_msg: str = None,
        audit_status: str = None,
        audit_time: int = None,
        code: str = None,
        description: str = None,
        front_category_id: int = None,
        gmt_created: int = None,
        gmt_modified: int = None,
        name: str = None,
        pic_url: str = None,
        product_extras: DescribeProductResponseBodyProductExtras = None,
        product_skus: DescribeProductResponseBodyProductSkus = None,
        request_id: str = None,
        score: float = None,
        shop_info: DescribeProductResponseBodyShopInfo = None,
        short_description: str = None,
        status: str = None,
        supplier_pk: int = None,
        type: str = None,
        use_count: int = None,
    ):
        self.audit_fail_msg = audit_fail_msg
        self.audit_status = audit_status
        self.audit_time = audit_time
        self.code = code
        self.description = description
        self.front_category_id = front_category_id
        self.gmt_created = gmt_created
        self.gmt_modified = gmt_modified
        self.name = name
        self.pic_url = pic_url
        self.product_extras = product_extras
        self.product_skus = product_skus
        self.request_id = request_id
        self.score = score
        self.shop_info = shop_info
        self.short_description = short_description
        self.status = status
        self.supplier_pk = supplier_pk
        self.type = type
        self.use_count = use_count

    def validate(self):
        if self.product_extras:
            self.product_extras.validate()
        if self.product_skus:
            self.product_skus.validate()
        if self.shop_info:
            self.shop_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audit_fail_msg is not None:
            result['AuditFailMsg'] = self.audit_fail_msg
        if self.audit_status is not None:
            result['AuditStatus'] = self.audit_status
        if self.audit_time is not None:
            result['AuditTime'] = self.audit_time
        if self.code is not None:
            result['Code'] = self.code
        if self.description is not None:
            result['Description'] = self.description
        if self.front_category_id is not None:
            result['FrontCategoryId'] = self.front_category_id
        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.name is not None:
            result['Name'] = self.name
        if self.pic_url is not None:
            result['PicUrl'] = self.pic_url
        if self.product_extras is not None:
            result['ProductExtras'] = self.product_extras.to_map()
        if self.product_skus is not None:
            result['ProductSkus'] = self.product_skus.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.score is not None:
            result['Score'] = self.score
        if self.shop_info is not None:
            result['ShopInfo'] = self.shop_info.to_map()
        if self.short_description is not None:
            result['ShortDescription'] = self.short_description
        if self.status is not None:
            result['Status'] = self.status
        if self.supplier_pk is not None:
            result['SupplierPk'] = self.supplier_pk
        if self.type is not None:
            result['Type'] = self.type
        if self.use_count is not None:
            result['UseCount'] = self.use_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuditFailMsg') is not None:
            self.audit_fail_msg = m.get('AuditFailMsg')
        if m.get('AuditStatus') is not None:
            self.audit_status = m.get('AuditStatus')
        if m.get('AuditTime') is not None:
            self.audit_time = m.get('AuditTime')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FrontCategoryId') is not None:
            self.front_category_id = m.get('FrontCategoryId')
        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PicUrl') is not None:
            self.pic_url = m.get('PicUrl')
        if m.get('ProductExtras') is not None:
            temp_model = DescribeProductResponseBodyProductExtras()
            self.product_extras = temp_model.from_map(m['ProductExtras'])
        if m.get('ProductSkus') is not None:
            temp_model = DescribeProductResponseBodyProductSkus()
            self.product_skus = temp_model.from_map(m['ProductSkus'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('ShopInfo') is not None:
            temp_model = DescribeProductResponseBodyShopInfo()
            self.shop_info = temp_model.from_map(m['ShopInfo'])
        if m.get('ShortDescription') is not None:
            self.short_description = m.get('ShortDescription')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SupplierPk') is not None:
            self.supplier_pk = m.get('SupplierPk')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UseCount') is not None:
            self.use_count = m.get('UseCount')
        return self


class DescribeProductResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeProductResponseBody = None,
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
            temp_model = DescribeProductResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeProductsRequestFilter(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeProductsRequest(TeaModel):
    def __init__(
        self,
        filter: List[DescribeProductsRequestFilter] = None,
        page_number: int = None,
        page_size: int = None,
        search_term: str = None,
    ):
        self.filter = filter
        self.page_number = page_number
        self.page_size = page_size
        self.search_term = search_term

    def validate(self):
        if self.filter:
            for k in self.filter:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Filter'] = []
        if self.filter is not None:
            for k in self.filter:
                result['Filter'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.search_term is not None:
            result['SearchTerm'] = self.search_term
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.filter = []
        if m.get('Filter') is not None:
            for k in m.get('Filter'):
                temp_model = DescribeProductsRequestFilter()
                self.filter.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SearchTerm') is not None:
            self.search_term = m.get('SearchTerm')
        return self


class DescribeProductsResponseBodyProductItemsProductItem(TeaModel):
    def __init__(
        self,
        category_id: int = None,
        code: str = None,
        delivery_date: str = None,
        delivery_way: str = None,
        image_url: str = None,
        name: str = None,
        operation_system: str = None,
        price_info: str = None,
        score: str = None,
        short_description: str = None,
        suggested_price: str = None,
        supplier_id: int = None,
        supplier_name: str = None,
        tags: str = None,
        target_url: str = None,
        warranty_date: str = None,
    ):
        self.category_id = category_id
        self.code = code
        self.delivery_date = delivery_date
        self.delivery_way = delivery_way
        self.image_url = image_url
        self.name = name
        self.operation_system = operation_system
        self.price_info = price_info
        self.score = score
        self.short_description = short_description
        self.suggested_price = suggested_price
        self.supplier_id = supplier_id
        self.supplier_name = supplier_name
        self.tags = tags
        self.target_url = target_url
        self.warranty_date = warranty_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.code is not None:
            result['Code'] = self.code
        if self.delivery_date is not None:
            result['DeliveryDate'] = self.delivery_date
        if self.delivery_way is not None:
            result['DeliveryWay'] = self.delivery_way
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.name is not None:
            result['Name'] = self.name
        if self.operation_system is not None:
            result['OperationSystem'] = self.operation_system
        if self.price_info is not None:
            result['PriceInfo'] = self.price_info
        if self.score is not None:
            result['Score'] = self.score
        if self.short_description is not None:
            result['ShortDescription'] = self.short_description
        if self.suggested_price is not None:
            result['SuggestedPrice'] = self.suggested_price
        if self.supplier_id is not None:
            result['SupplierId'] = self.supplier_id
        if self.supplier_name is not None:
            result['SupplierName'] = self.supplier_name
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.target_url is not None:
            result['TargetUrl'] = self.target_url
        if self.warranty_date is not None:
            result['WarrantyDate'] = self.warranty_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DeliveryDate') is not None:
            self.delivery_date = m.get('DeliveryDate')
        if m.get('DeliveryWay') is not None:
            self.delivery_way = m.get('DeliveryWay')
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OperationSystem') is not None:
            self.operation_system = m.get('OperationSystem')
        if m.get('PriceInfo') is not None:
            self.price_info = m.get('PriceInfo')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('ShortDescription') is not None:
            self.short_description = m.get('ShortDescription')
        if m.get('SuggestedPrice') is not None:
            self.suggested_price = m.get('SuggestedPrice')
        if m.get('SupplierId') is not None:
            self.supplier_id = m.get('SupplierId')
        if m.get('SupplierName') is not None:
            self.supplier_name = m.get('SupplierName')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('TargetUrl') is not None:
            self.target_url = m.get('TargetUrl')
        if m.get('WarrantyDate') is not None:
            self.warranty_date = m.get('WarrantyDate')
        return self


class DescribeProductsResponseBodyProductItems(TeaModel):
    def __init__(
        self,
        product_item: List[DescribeProductsResponseBodyProductItemsProductItem] = None,
    ):
        self.product_item = product_item

    def validate(self):
        if self.product_item:
            for k in self.product_item:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ProductItem'] = []
        if self.product_item is not None:
            for k in self.product_item:
                result['ProductItem'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.product_item = []
        if m.get('ProductItem') is not None:
            for k in m.get('ProductItem'):
                temp_model = DescribeProductsResponseBodyProductItemsProductItem()
                self.product_item.append(temp_model.from_map(k))
        return self


class DescribeProductsResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        product_items: DescribeProductsResponseBodyProductItems = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.product_items = product_items
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.product_items:
            self.product_items.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.product_items is not None:
            result['ProductItems'] = self.product_items.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProductItems') is not None:
            temp_model = DescribeProductsResponseBodyProductItems()
            self.product_items = temp_model.from_map(m['ProductItems'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeProductsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeProductsResponseBody = None,
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
            temp_model = DescribeProductsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeProjectAttachmentsRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DescribeProjectAttachmentsResponseBodyResult(TeaModel):
    def __init__(
        self,
        attachment_token: str = None,
        attachment_type: str = None,
        content: str = None,
        file_link: str = None,
        file_link_gmt_expired: int = None,
        file_name: str = None,
        file_size: int = None,
        file_suffix: str = None,
        gmt_create: int = None,
        node_id: int = None,
        node_name: str = None,
        operator: int = None,
        operator_name: str = None,
        operator_role: str = None,
        step_no: int = None,
    ):
        self.attachment_token = attachment_token
        self.attachment_type = attachment_type
        self.content = content
        self.file_link = file_link
        self.file_link_gmt_expired = file_link_gmt_expired
        self.file_name = file_name
        self.file_size = file_size
        self.file_suffix = file_suffix
        self.gmt_create = gmt_create
        self.node_id = node_id
        self.node_name = node_name
        self.operator = operator
        self.operator_name = operator_name
        self.operator_role = operator_role
        self.step_no = step_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attachment_token is not None:
            result['AttachmentToken'] = self.attachment_token
        if self.attachment_type is not None:
            result['AttachmentType'] = self.attachment_type
        if self.content is not None:
            result['Content'] = self.content
        if self.file_link is not None:
            result['FileLink'] = self.file_link
        if self.file_link_gmt_expired is not None:
            result['FileLinkGmtExpired'] = self.file_link_gmt_expired
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_size is not None:
            result['FileSize'] = self.file_size
        if self.file_suffix is not None:
            result['FileSuffix'] = self.file_suffix
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.node_name is not None:
            result['NodeName'] = self.node_name
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.operator_name is not None:
            result['OperatorName'] = self.operator_name
        if self.operator_role is not None:
            result['OperatorRole'] = self.operator_role
        if self.step_no is not None:
            result['StepNo'] = self.step_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttachmentToken') is not None:
            self.attachment_token = m.get('AttachmentToken')
        if m.get('AttachmentType') is not None:
            self.attachment_type = m.get('AttachmentType')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('FileLink') is not None:
            self.file_link = m.get('FileLink')
        if m.get('FileLinkGmtExpired') is not None:
            self.file_link_gmt_expired = m.get('FileLinkGmtExpired')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')
        if m.get('FileSuffix') is not None:
            self.file_suffix = m.get('FileSuffix')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('OperatorName') is not None:
            self.operator_name = m.get('OperatorName')
        if m.get('OperatorRole') is not None:
            self.operator_role = m.get('OperatorRole')
        if m.get('StepNo') is not None:
            self.step_no = m.get('StepNo')
        return self


class DescribeProjectAttachmentsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[DescribeProjectAttachmentsResponseBodyResult] = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.result = result
        self.success = success

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = DescribeProjectAttachmentsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeProjectAttachmentsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeProjectAttachmentsResponseBody = None,
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
            temp_model = DescribeProjectAttachmentsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeProjectInfoRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DescribeProjectInfoResponseBodyResult(TeaModel):
    def __init__(
        self,
        current_step_no: int = None,
        customer_ali_uid: int = None,
        final_step_no: int = None,
        finish_type: str = None,
        gmt_create: int = None,
        gmt_expired: int = None,
        gmt_finished: int = None,
        instance_id: str = None,
        order_id: int = None,
        product_code: str = None,
        product_name: str = None,
        product_sku_code: str = None,
        product_sku_name: str = None,
        project_status: str = None,
        supplier_ali_uid: int = None,
        template_id: int = None,
        template_type: str = None,
    ):
        self.current_step_no = current_step_no
        self.customer_ali_uid = customer_ali_uid
        self.final_step_no = final_step_no
        self.finish_type = finish_type
        self.gmt_create = gmt_create
        self.gmt_expired = gmt_expired
        self.gmt_finished = gmt_finished
        self.instance_id = instance_id
        self.order_id = order_id
        self.product_code = product_code
        self.product_name = product_name
        self.product_sku_code = product_sku_code
        self.product_sku_name = product_sku_name
        self.project_status = project_status
        self.supplier_ali_uid = supplier_ali_uid
        self.template_id = template_id
        self.template_type = template_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_step_no is not None:
            result['CurrentStepNo'] = self.current_step_no
        if self.customer_ali_uid is not None:
            result['CustomerAliUid'] = self.customer_ali_uid
        if self.final_step_no is not None:
            result['FinalStepNo'] = self.final_step_no
        if self.finish_type is not None:
            result['FinishType'] = self.finish_type
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_expired is not None:
            result['GmtExpired'] = self.gmt_expired
        if self.gmt_finished is not None:
            result['GmtFinished'] = self.gmt_finished
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        if self.product_sku_code is not None:
            result['ProductSkuCode'] = self.product_sku_code
        if self.product_sku_name is not None:
            result['ProductSkuName'] = self.product_sku_name
        if self.project_status is not None:
            result['ProjectStatus'] = self.project_status
        if self.supplier_ali_uid is not None:
            result['SupplierAliUid'] = self.supplier_ali_uid
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentStepNo') is not None:
            self.current_step_no = m.get('CurrentStepNo')
        if m.get('CustomerAliUid') is not None:
            self.customer_ali_uid = m.get('CustomerAliUid')
        if m.get('FinalStepNo') is not None:
            self.final_step_no = m.get('FinalStepNo')
        if m.get('FinishType') is not None:
            self.finish_type = m.get('FinishType')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtExpired') is not None:
            self.gmt_expired = m.get('GmtExpired')
        if m.get('GmtFinished') is not None:
            self.gmt_finished = m.get('GmtFinished')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        if m.get('ProductSkuCode') is not None:
            self.product_sku_code = m.get('ProductSkuCode')
        if m.get('ProductSkuName') is not None:
            self.product_sku_name = m.get('ProductSkuName')
        if m.get('ProjectStatus') is not None:
            self.project_status = m.get('ProjectStatus')
        if m.get('SupplierAliUid') is not None:
            self.supplier_ali_uid = m.get('SupplierAliUid')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        return self


class DescribeProjectInfoResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: DescribeProjectInfoResponseBodyResult = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.result = result
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = DescribeProjectInfoResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeProjectInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeProjectInfoResponseBody = None,
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
            temp_model = DescribeProjectInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeProjectMessagesRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        page_index: int = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        self.page_index = page_index

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        return self


class DescribeProjectMessagesResponseBodyResult(TeaModel):
    def __init__(
        self,
        content: str = None,
        gmt_create: int = None,
        operator: int = None,
        operator_name: str = None,
        operator_role: str = None,
    ):
        self.content = content
        self.gmt_create = gmt_create
        self.operator = operator
        self.operator_name = operator_name
        self.operator_role = operator_role

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.operator_name is not None:
            result['OperatorName'] = self.operator_name
        if self.operator_role is not None:
            result['OperatorRole'] = self.operator_role
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('OperatorName') is not None:
            self.operator_name = m.get('OperatorName')
        if m.get('OperatorRole') is not None:
            self.operator_role = m.get('OperatorRole')
        return self


class DescribeProjectMessagesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[DescribeProjectMessagesResponseBodyResult] = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.request_id = request_id
        self.result = result
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = DescribeProjectMessagesResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeProjectMessagesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeProjectMessagesResponseBody = None,
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
            temp_model = DescribeProjectMessagesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeProjectNodesRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DescribeProjectNodesResponseBodyResult(TeaModel):
    def __init__(
        self,
        allow_rollback_node: bool = None,
        auto_finish_node: bool = None,
        final_step_no: int = None,
        gmt_expired: int = None,
        gmt_finished: int = None,
        gmt_start: int = None,
        need_attachment: bool = None,
        next_node_id: int = None,
        node_id: int = None,
        node_name: str = None,
        node_status: str = None,
        operator_role: str = None,
        parent_node_id: int = None,
        previous_node_id: int = None,
        step_no: int = None,
        template_form: str = None,
    ):
        self.allow_rollback_node = allow_rollback_node
        self.auto_finish_node = auto_finish_node
        self.final_step_no = final_step_no
        self.gmt_expired = gmt_expired
        self.gmt_finished = gmt_finished
        self.gmt_start = gmt_start
        self.need_attachment = need_attachment
        self.next_node_id = next_node_id
        self.node_id = node_id
        self.node_name = node_name
        self.node_status = node_status
        self.operator_role = operator_role
        self.parent_node_id = parent_node_id
        self.previous_node_id = previous_node_id
        self.step_no = step_no
        self.template_form = template_form

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_rollback_node is not None:
            result['AllowRollbackNode'] = self.allow_rollback_node
        if self.auto_finish_node is not None:
            result['AutoFinishNode'] = self.auto_finish_node
        if self.final_step_no is not None:
            result['FinalStepNo'] = self.final_step_no
        if self.gmt_expired is not None:
            result['GmtExpired'] = self.gmt_expired
        if self.gmt_finished is not None:
            result['GmtFinished'] = self.gmt_finished
        if self.gmt_start is not None:
            result['GmtStart'] = self.gmt_start
        if self.need_attachment is not None:
            result['NeedAttachment'] = self.need_attachment
        if self.next_node_id is not None:
            result['NextNodeId'] = self.next_node_id
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.node_name is not None:
            result['NodeName'] = self.node_name
        if self.node_status is not None:
            result['NodeStatus'] = self.node_status
        if self.operator_role is not None:
            result['OperatorRole'] = self.operator_role
        if self.parent_node_id is not None:
            result['ParentNodeId'] = self.parent_node_id
        if self.previous_node_id is not None:
            result['PreviousNodeId'] = self.previous_node_id
        if self.step_no is not None:
            result['StepNo'] = self.step_no
        if self.template_form is not None:
            result['TemplateForm'] = self.template_form
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowRollbackNode') is not None:
            self.allow_rollback_node = m.get('AllowRollbackNode')
        if m.get('AutoFinishNode') is not None:
            self.auto_finish_node = m.get('AutoFinishNode')
        if m.get('FinalStepNo') is not None:
            self.final_step_no = m.get('FinalStepNo')
        if m.get('GmtExpired') is not None:
            self.gmt_expired = m.get('GmtExpired')
        if m.get('GmtFinished') is not None:
            self.gmt_finished = m.get('GmtFinished')
        if m.get('GmtStart') is not None:
            self.gmt_start = m.get('GmtStart')
        if m.get('NeedAttachment') is not None:
            self.need_attachment = m.get('NeedAttachment')
        if m.get('NextNodeId') is not None:
            self.next_node_id = m.get('NextNodeId')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')
        if m.get('NodeStatus') is not None:
            self.node_status = m.get('NodeStatus')
        if m.get('OperatorRole') is not None:
            self.operator_role = m.get('OperatorRole')
        if m.get('ParentNodeId') is not None:
            self.parent_node_id = m.get('ParentNodeId')
        if m.get('PreviousNodeId') is not None:
            self.previous_node_id = m.get('PreviousNodeId')
        if m.get('StepNo') is not None:
            self.step_no = m.get('StepNo')
        if m.get('TemplateForm') is not None:
            self.template_form = m.get('TemplateForm')
        return self


class DescribeProjectNodesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[DescribeProjectNodesResponseBodyResult] = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.result = result
        self.success = success

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = DescribeProjectNodesResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeProjectNodesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeProjectNodesResponseBody = None,
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
            temp_model = DescribeProjectNodesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeProjectOperateLogsRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DescribeProjectOperateLogsResponseBodyResult(TeaModel):
    def __init__(
        self,
        description: str = None,
        gmt_create: int = None,
        operator: int = None,
        operator_name: str = None,
        operator_role: str = None,
    ):
        self.description = description
        self.gmt_create = gmt_create
        self.operator = operator
        self.operator_name = operator_name
        self.operator_role = operator_role

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.operator_name is not None:
            result['OperatorName'] = self.operator_name
        if self.operator_role is not None:
            result['OperatorRole'] = self.operator_role
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('OperatorName') is not None:
            self.operator_name = m.get('OperatorName')
        if m.get('OperatorRole') is not None:
            self.operator_role = m.get('OperatorRole')
        return self


class DescribeProjectOperateLogsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[DescribeProjectOperateLogsResponseBodyResult] = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.result = result
        self.success = success

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = DescribeProjectOperateLogsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeProjectOperateLogsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeProjectOperateLogsResponseBody = None,
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
            temp_model = DescribeProjectOperateLogsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FinishCurrentProjectNodeRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        node_id: int = None,
        remark: str = None,
        template_form: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.node_id = node_id
        self.remark = remark
        self.template_form = template_form

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.template_form is not None:
            result['TemplateForm'] = self.template_form
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('TemplateForm') is not None:
            self.template_form = m.get('TemplateForm')
        return self


class FinishCurrentProjectNodeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.result = result
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
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class FinishCurrentProjectNodeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: FinishCurrentProjectNodeResponseBody = None,
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
            temp_model = FinishCurrentProjectNodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PauseProjectRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        node_id: int = None,
        remark: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.node_id = node_id
        self.remark = remark

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.remark is not None:
            result['Remark'] = self.remark
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        return self


class PauseProjectResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.result = result
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
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class PauseProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PauseProjectResponseBody = None,
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
            temp_model = PauseProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PushMeteringDataRequest(TeaModel):
    def __init__(
        self,
        metering: str = None,
    ):
        self.metering = metering

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.metering is not None:
            result['Metering'] = self.metering
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Metering') is not None:
            self.metering = m.get('Metering')
        return self


class PushMeteringDataResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
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
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class PushMeteringDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PushMeteringDataResponseBody = None,
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
            temp_model = PushMeteringDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResumeProjectRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        node_id: int = None,
        remark: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.node_id = node_id
        self.remark = remark

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.remark is not None:
            result['Remark'] = self.remark
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        return self


class ResumeProjectResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.result = result
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
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ResumeProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ResumeProjectResponseBody = None,
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
            temp_model = ResumeProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RollbackCurrentProjectNodeRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        node_id: int = None,
        remark: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.node_id = node_id
        self.remark = remark

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.remark is not None:
            result['Remark'] = self.remark
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        return self


class RollbackCurrentProjectNodeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.result = result
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
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RollbackCurrentProjectNodeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RollbackCurrentProjectNodeResponseBody = None,
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
            temp_model = RollbackCurrentProjectNodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


