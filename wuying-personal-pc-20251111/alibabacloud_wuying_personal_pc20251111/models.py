# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict, Any


class CreateDesktopImageRequest(TeaModel):
    def __init__(
        self,
        api_key: str = None,
        auto_clean_user_data: bool = None,
        description: str = None,
        desktop_id: str = None,
        disk_type: str = None,
        enable_start_up_config: bool = None,
        image_name: str = None,
        session_id: str = None,
        start_up_file_path_list: List[str] = None,
    ):
        # This parameter is required.
        self.api_key = api_key
        self.auto_clean_user_data = auto_clean_user_data
        self.description = description
        # This parameter is required.
        self.desktop_id = desktop_id
        # This parameter is required.
        self.disk_type = disk_type
        self.enable_start_up_config = enable_start_up_config
        # This parameter is required.
        self.image_name = image_name
        self.session_id = session_id
        self.start_up_file_path_list = start_up_file_path_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_key is not None:
            result['ApiKey'] = self.api_key
        if self.auto_clean_user_data is not None:
            result['AutoCleanUserData'] = self.auto_clean_user_data
        if self.description is not None:
            result['Description'] = self.description
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.disk_type is not None:
            result['DiskType'] = self.disk_type
        if self.enable_start_up_config is not None:
            result['EnableStartUpConfig'] = self.enable_start_up_config
        if self.image_name is not None:
            result['ImageName'] = self.image_name
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.start_up_file_path_list is not None:
            result['StartUpFilePathList'] = self.start_up_file_path_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiKey') is not None:
            self.api_key = m.get('ApiKey')
        if m.get('AutoCleanUserData') is not None:
            self.auto_clean_user_data = m.get('AutoCleanUserData')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')
        if m.get('EnableStartUpConfig') is not None:
            self.enable_start_up_config = m.get('EnableStartUpConfig')
        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('StartUpFilePathList') is not None:
            self.start_up_file_path_list = m.get('StartUpFilePathList')
        return self


class CreateDesktopImageShrinkRequest(TeaModel):
    def __init__(
        self,
        api_key: str = None,
        auto_clean_user_data: bool = None,
        description: str = None,
        desktop_id: str = None,
        disk_type: str = None,
        enable_start_up_config: bool = None,
        image_name: str = None,
        session_id: str = None,
        start_up_file_path_list_shrink: str = None,
    ):
        # This parameter is required.
        self.api_key = api_key
        self.auto_clean_user_data = auto_clean_user_data
        self.description = description
        # This parameter is required.
        self.desktop_id = desktop_id
        # This parameter is required.
        self.disk_type = disk_type
        self.enable_start_up_config = enable_start_up_config
        # This parameter is required.
        self.image_name = image_name
        self.session_id = session_id
        self.start_up_file_path_list_shrink = start_up_file_path_list_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_key is not None:
            result['ApiKey'] = self.api_key
        if self.auto_clean_user_data is not None:
            result['AutoCleanUserData'] = self.auto_clean_user_data
        if self.description is not None:
            result['Description'] = self.description
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.disk_type is not None:
            result['DiskType'] = self.disk_type
        if self.enable_start_up_config is not None:
            result['EnableStartUpConfig'] = self.enable_start_up_config
        if self.image_name is not None:
            result['ImageName'] = self.image_name
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.start_up_file_path_list_shrink is not None:
            result['StartUpFilePathList'] = self.start_up_file_path_list_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiKey') is not None:
            self.api_key = m.get('ApiKey')
        if m.get('AutoCleanUserData') is not None:
            self.auto_clean_user_data = m.get('AutoCleanUserData')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')
        if m.get('EnableStartUpConfig') is not None:
            self.enable_start_up_config = m.get('EnableStartUpConfig')
        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('StartUpFilePathList') is not None:
            self.start_up_file_path_list_shrink = m.get('StartUpFilePathList')
        return self


class CreateDesktopImageResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        http_status_code: int = None,
        request_id: str = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.trace_id = trace_id

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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class CreateDesktopImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateDesktopImageResponseBody = None,
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
            temp_model = CreateDesktopImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateOrderRequestDynamicProductParamsInputActivateConfig(TeaModel):
    def __init__(
        self,
        city_name: str = None,
        desktop_name: str = None,
        image_id: str = None,
    ):
        self.city_name = city_name
        self.desktop_name = desktop_name
        self.image_id = image_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.city_name is not None:
            result['CityName'] = self.city_name
        if self.desktop_name is not None:
            result['DesktopName'] = self.desktop_name
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CityName') is not None:
            self.city_name = m.get('CityName')
        if m.get('DesktopName') is not None:
            self.desktop_name = m.get('DesktopName')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        return self


class CreateOrderRequestDynamicProductParams(TeaModel):
    def __init__(
        self,
        amount: int = None,
        delivery_address: str = None,
        dynamic_attributes: Dict[str, str] = None,
        input_activate_config: CreateOrderRequestDynamicProductParamsInputActivateConfig = None,
        instance_id_list: List[str] = None,
        linked_resource_id: str = None,
        package_code: str = None,
        product_code: str = None,
        product_sku_code: str = None,
        resource_id: str = None,
    ):
        self.amount = amount
        self.delivery_address = delivery_address
        self.dynamic_attributes = dynamic_attributes
        self.input_activate_config = input_activate_config
        self.instance_id_list = instance_id_list
        self.linked_resource_id = linked_resource_id
        self.package_code = package_code
        self.product_code = product_code
        self.product_sku_code = product_sku_code
        self.resource_id = resource_id

    def validate(self):
        if self.input_activate_config:
            self.input_activate_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.delivery_address is not None:
            result['DeliveryAddress'] = self.delivery_address
        if self.dynamic_attributes is not None:
            result['DynamicAttributes'] = self.dynamic_attributes
        if self.input_activate_config is not None:
            result['InputActivateConfig'] = self.input_activate_config.to_map()
        if self.instance_id_list is not None:
            result['InstanceIdList'] = self.instance_id_list
        if self.linked_resource_id is not None:
            result['LinkedResourceId'] = self.linked_resource_id
        if self.package_code is not None:
            result['PackageCode'] = self.package_code
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.product_sku_code is not None:
            result['ProductSkuCode'] = self.product_sku_code
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('DeliveryAddress') is not None:
            self.delivery_address = m.get('DeliveryAddress')
        if m.get('DynamicAttributes') is not None:
            self.dynamic_attributes = m.get('DynamicAttributes')
        if m.get('InputActivateConfig') is not None:
            temp_model = CreateOrderRequestDynamicProductParamsInputActivateConfig()
            self.input_activate_config = temp_model.from_map(m['InputActivateConfig'])
        if m.get('InstanceIdList') is not None:
            self.instance_id_list = m.get('InstanceIdList')
        if m.get('LinkedResourceId') is not None:
            self.linked_resource_id = m.get('LinkedResourceId')
        if m.get('PackageCode') is not None:
            self.package_code = m.get('PackageCode')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProductSkuCode') is not None:
            self.product_sku_code = m.get('ProductSkuCode')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        return self


class CreateOrderRequest(TeaModel):
    def __init__(
        self,
        api_key: str = None,
        auto_pay: bool = None,
        dynamic_product_params: List[CreateOrderRequestDynamicProductParams] = None,
        operation_type: str = None,
        order_from: str = None,
        session_id: str = None,
    ):
        # This parameter is required.
        self.api_key = api_key
        self.auto_pay = auto_pay
        # This parameter is required.
        self.dynamic_product_params = dynamic_product_params
        # This parameter is required.
        self.operation_type = operation_type
        self.order_from = order_from
        self.session_id = session_id

    def validate(self):
        if self.dynamic_product_params:
            for k in self.dynamic_product_params:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_key is not None:
            result['ApiKey'] = self.api_key
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay
        result['DynamicProductParams'] = []
        if self.dynamic_product_params is not None:
            for k in self.dynamic_product_params:
                result['DynamicProductParams'].append(k.to_map() if k else None)
        if self.operation_type is not None:
            result['OperationType'] = self.operation_type
        if self.order_from is not None:
            result['OrderFrom'] = self.order_from
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiKey') is not None:
            self.api_key = m.get('ApiKey')
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')
        self.dynamic_product_params = []
        if m.get('DynamicProductParams') is not None:
            for k in m.get('DynamicProductParams'):
                temp_model = CreateOrderRequestDynamicProductParams()
                self.dynamic_product_params.append(temp_model.from_map(k))
        if m.get('OperationType') is not None:
            self.operation_type = m.get('OperationType')
        if m.get('OrderFrom') is not None:
            self.order_from = m.get('OrderFrom')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        return self


class CreateOrderShrinkRequest(TeaModel):
    def __init__(
        self,
        api_key: str = None,
        auto_pay: bool = None,
        dynamic_product_params_shrink: str = None,
        operation_type: str = None,
        order_from: str = None,
        session_id: str = None,
    ):
        # This parameter is required.
        self.api_key = api_key
        self.auto_pay = auto_pay
        # This parameter is required.
        self.dynamic_product_params_shrink = dynamic_product_params_shrink
        # This parameter is required.
        self.operation_type = operation_type
        self.order_from = order_from
        self.session_id = session_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_key is not None:
            result['ApiKey'] = self.api_key
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay
        if self.dynamic_product_params_shrink is not None:
            result['DynamicProductParams'] = self.dynamic_product_params_shrink
        if self.operation_type is not None:
            result['OperationType'] = self.operation_type
        if self.order_from is not None:
            result['OrderFrom'] = self.order_from
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiKey') is not None:
            self.api_key = m.get('ApiKey')
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')
        if m.get('DynamicProductParams') is not None:
            self.dynamic_product_params_shrink = m.get('DynamicProductParams')
        if m.get('OperationType') is not None:
            self.operation_type = m.get('OperationType')
        if m.get('OrderFrom') is not None:
            self.order_from = m.get('OrderFrom')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        return self


class CreateOrderResponseBodyDataOrderDetailList(TeaModel):
    def __init__(
        self,
        instance_ids: List[str] = None,
        order_id: int = None,
    ):
        self.instance_ids = instance_ids
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class CreateOrderResponseBodyData(TeaModel):
    def __init__(
        self,
        order_detail_list: List[CreateOrderResponseBodyDataOrderDetailList] = None,
        order_id: str = None,
        pay_link: str = None,
        resource_id: str = None,
    ):
        self.order_detail_list = order_detail_list
        self.order_id = order_id
        self.pay_link = pay_link
        self.resource_id = resource_id

    def validate(self):
        if self.order_detail_list:
            for k in self.order_detail_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['OrderDetailList'] = []
        if self.order_detail_list is not None:
            for k in self.order_detail_list:
                result['OrderDetailList'].append(k.to_map() if k else None)
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.pay_link is not None:
            result['PayLink'] = self.pay_link
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.order_detail_list = []
        if m.get('OrderDetailList') is not None:
            for k in m.get('OrderDetailList'):
                temp_model = CreateOrderResponseBodyDataOrderDetailList()
                self.order_detail_list.append(temp_model.from_map(k))
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('PayLink') is not None:
            self.pay_link = m.get('PayLink')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        return self


class CreateOrderResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CreateOrderResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.trace_id = trace_id

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
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = CreateOrderResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
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


class DeleteDesktopRequest(TeaModel):
    def __init__(
        self,
        api_key: str = None,
        desktop_id: str = None,
        session_id: str = None,
    ):
        # This parameter is required.
        self.api_key = api_key
        # This parameter is required.
        self.desktop_id = desktop_id
        self.session_id = session_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_key is not None:
            result['ApiKey'] = self.api_key
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiKey') is not None:
            self.api_key = m.get('ApiKey')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        return self


class DeleteDesktopResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        request_id: str = None,
        trace_id: str = None,
    ):
        self.code = code
        self.request_id = request_id
        self.trace_id = trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class DeleteDesktopResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteDesktopResponseBody = None,
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
            temp_model = DeleteDesktopResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDesktopImageRequest(TeaModel):
    def __init__(
        self,
        api_key: str = None,
        image_id: str = None,
        is_clean_image_code: bool = None,
        session_id: str = None,
    ):
        # This parameter is required.
        self.api_key = api_key
        # This parameter is required.
        self.image_id = image_id
        self.is_clean_image_code = is_clean_image_code
        self.session_id = session_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_key is not None:
            result['ApiKey'] = self.api_key
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.is_clean_image_code is not None:
            result['IsCleanImageCode'] = self.is_clean_image_code
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiKey') is not None:
            self.api_key = m.get('ApiKey')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('IsCleanImageCode') is not None:
            self.is_clean_image_code = m.get('IsCleanImageCode')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        return self


class DeleteDesktopImageResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        request_id: str = None,
        trace_id: str = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.trace_id = trace_id

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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class DeleteDesktopImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteDesktopImageResponseBody = None,
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
            temp_model = DeleteDesktopImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAccessibleImagesRequest(TeaModel):
    def __init__(
        self,
        api_key: str = None,
        biz_source: str = None,
        desktop_id: str = None,
        desktop_type: str = None,
        image_type: str = None,
        resource_id: str = None,
        scene: str = None,
        search_key: str = None,
        session_id: str = None,
    ):
        # This parameter is required.
        self.api_key = api_key
        self.biz_source = biz_source
        self.desktop_id = desktop_id
        self.desktop_type = desktop_type
        self.image_type = image_type
        self.resource_id = resource_id
        self.scene = scene
        self.search_key = search_key
        self.session_id = session_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_key is not None:
            result['ApiKey'] = self.api_key
        if self.biz_source is not None:
            result['BizSource'] = self.biz_source
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.desktop_type is not None:
            result['DesktopType'] = self.desktop_type
        if self.image_type is not None:
            result['ImageType'] = self.image_type
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.scene is not None:
            result['Scene'] = self.scene
        if self.search_key is not None:
            result['SearchKey'] = self.search_key
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiKey') is not None:
            self.api_key = m.get('ApiKey')
        if m.get('BizSource') is not None:
            self.biz_source = m.get('BizSource')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('DesktopType') is not None:
            self.desktop_type = m.get('DesktopType')
        if m.get('ImageType') is not None:
            self.image_type = m.get('ImageType')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('Scene') is not None:
            self.scene = m.get('Scene')
        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        return self


class DescribeAccessibleImagesResponseBodyDataCurrentImageCodeInfo(TeaModel):
    def __init__(
        self,
        current_password: str = None,
        expire_time: str = None,
        gmt_created: str = None,
        gmt_modified: str = None,
        image_code: str = None,
        image_id: str = None,
        is_copy_password: bool = None,
        is_encrypted: bool = None,
        is_free: bool = None,
        period_days: int = None,
        redeem_count: int = None,
        redeem_quota: int = None,
    ):
        self.current_password = current_password
        self.expire_time = expire_time
        self.gmt_created = gmt_created
        self.gmt_modified = gmt_modified
        self.image_code = image_code
        self.image_id = image_id
        self.is_copy_password = is_copy_password
        self.is_encrypted = is_encrypted
        self.is_free = is_free
        self.period_days = period_days
        self.redeem_count = redeem_count
        self.redeem_quota = redeem_quota

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_password is not None:
            result['CurrentPassword'] = self.current_password
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.image_code is not None:
            result['ImageCode'] = self.image_code
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.is_copy_password is not None:
            result['IsCopyPassword'] = self.is_copy_password
        if self.is_encrypted is not None:
            result['IsEncrypted'] = self.is_encrypted
        if self.is_free is not None:
            result['IsFree'] = self.is_free
        if self.period_days is not None:
            result['PeriodDays'] = self.period_days
        if self.redeem_count is not None:
            result['RedeemCount'] = self.redeem_count
        if self.redeem_quota is not None:
            result['RedeemQuota'] = self.redeem_quota
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPassword') is not None:
            self.current_password = m.get('CurrentPassword')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('ImageCode') is not None:
            self.image_code = m.get('ImageCode')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('IsCopyPassword') is not None:
            self.is_copy_password = m.get('IsCopyPassword')
        if m.get('IsEncrypted') is not None:
            self.is_encrypted = m.get('IsEncrypted')
        if m.get('IsFree') is not None:
            self.is_free = m.get('IsFree')
        if m.get('PeriodDays') is not None:
            self.period_days = m.get('PeriodDays')
        if m.get('RedeemCount') is not None:
            self.redeem_count = m.get('RedeemCount')
        if m.get('RedeemQuota') is not None:
            self.redeem_quota = m.get('RedeemQuota')
        return self


class DescribeAccessibleImagesResponseBodyData(TeaModel):
    def __init__(
        self,
        activity_type: str = None,
        auth_time: str = None,
        can_update: bool = None,
        current_image_code_info: DescribeAccessibleImagesResponseBodyDataCurrentImageCodeInfo = None,
        data_disk_size: int = None,
        deploy_mode: str = None,
        description: str = None,
        docker_image_size: int = None,
        enable_start_up_config: bool = None,
        gmt_created: str = None,
        image_id: str = None,
        image_scope: str = None,
        image_source: str = None,
        image_type: str = None,
        is_gpu: bool = None,
        is_linggou: str = None,
        is_workstation: bool = None,
        name: str = None,
        operation_system: str = None,
        os_type: str = None,
        permission: str = None,
        platform: str = None,
        progress: str = None,
        receiver_type: str = None,
        share_codes: List[str] = None,
        share_codes_include_disable: List[str] = None,
        shared: bool = None,
        shared_by: str = None,
        source_desktop_id: str = None,
        source_desktop_type: str = None,
        source_image_id: str = None,
        source_image_name: str = None,
        start_up_file_list: List[str] = None,
        status: str = None,
        support_publish: bool = None,
        system_disk_size: int = None,
        validation_code: str = None,
    ):
        self.activity_type = activity_type
        self.auth_time = auth_time
        self.can_update = can_update
        self.current_image_code_info = current_image_code_info
        self.data_disk_size = data_disk_size
        self.deploy_mode = deploy_mode
        self.description = description
        self.docker_image_size = docker_image_size
        self.enable_start_up_config = enable_start_up_config
        self.gmt_created = gmt_created
        self.image_id = image_id
        self.image_scope = image_scope
        self.image_source = image_source
        self.image_type = image_type
        self.is_gpu = is_gpu
        self.is_linggou = is_linggou
        self.is_workstation = is_workstation
        self.name = name
        self.operation_system = operation_system
        self.os_type = os_type
        self.permission = permission
        self.platform = platform
        self.progress = progress
        self.receiver_type = receiver_type
        self.share_codes = share_codes
        self.share_codes_include_disable = share_codes_include_disable
        self.shared = shared
        self.shared_by = shared_by
        self.source_desktop_id = source_desktop_id
        self.source_desktop_type = source_desktop_type
        self.source_image_id = source_image_id
        self.source_image_name = source_image_name
        self.start_up_file_list = start_up_file_list
        self.status = status
        self.support_publish = support_publish
        self.system_disk_size = system_disk_size
        self.validation_code = validation_code

    def validate(self):
        if self.current_image_code_info:
            self.current_image_code_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.activity_type is not None:
            result['ActivityType'] = self.activity_type
        if self.auth_time is not None:
            result['AuthTime'] = self.auth_time
        if self.can_update is not None:
            result['CanUpdate'] = self.can_update
        if self.current_image_code_info is not None:
            result['CurrentImageCodeInfo'] = self.current_image_code_info.to_map()
        if self.data_disk_size is not None:
            result['DataDiskSize'] = self.data_disk_size
        if self.deploy_mode is not None:
            result['DeployMode'] = self.deploy_mode
        if self.description is not None:
            result['Description'] = self.description
        if self.docker_image_size is not None:
            result['DockerImageSize'] = self.docker_image_size
        if self.enable_start_up_config is not None:
            result['EnableStartUpConfig'] = self.enable_start_up_config
        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.image_scope is not None:
            result['ImageScope'] = self.image_scope
        if self.image_source is not None:
            result['ImageSource'] = self.image_source
        if self.image_type is not None:
            result['ImageType'] = self.image_type
        if self.is_gpu is not None:
            result['IsGpu'] = self.is_gpu
        if self.is_linggou is not None:
            result['IsLinggou'] = self.is_linggou
        if self.is_workstation is not None:
            result['IsWorkstation'] = self.is_workstation
        if self.name is not None:
            result['Name'] = self.name
        if self.operation_system is not None:
            result['OperationSystem'] = self.operation_system
        if self.os_type is not None:
            result['OsType'] = self.os_type
        if self.permission is not None:
            result['Permission'] = self.permission
        if self.platform is not None:
            result['Platform'] = self.platform
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.receiver_type is not None:
            result['ReceiverType'] = self.receiver_type
        if self.share_codes is not None:
            result['ShareCodes'] = self.share_codes
        if self.share_codes_include_disable is not None:
            result['ShareCodesIncludeDisable'] = self.share_codes_include_disable
        if self.shared is not None:
            result['Shared'] = self.shared
        if self.shared_by is not None:
            result['SharedBy'] = self.shared_by
        if self.source_desktop_id is not None:
            result['SourceDesktopId'] = self.source_desktop_id
        if self.source_desktop_type is not None:
            result['SourceDesktopType'] = self.source_desktop_type
        if self.source_image_id is not None:
            result['SourceImageId'] = self.source_image_id
        if self.source_image_name is not None:
            result['SourceImageName'] = self.source_image_name
        if self.start_up_file_list is not None:
            result['StartUpFileList'] = self.start_up_file_list
        if self.status is not None:
            result['Status'] = self.status
        if self.support_publish is not None:
            result['SupportPublish'] = self.support_publish
        if self.system_disk_size is not None:
            result['SystemDiskSize'] = self.system_disk_size
        if self.validation_code is not None:
            result['ValidationCode'] = self.validation_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActivityType') is not None:
            self.activity_type = m.get('ActivityType')
        if m.get('AuthTime') is not None:
            self.auth_time = m.get('AuthTime')
        if m.get('CanUpdate') is not None:
            self.can_update = m.get('CanUpdate')
        if m.get('CurrentImageCodeInfo') is not None:
            temp_model = DescribeAccessibleImagesResponseBodyDataCurrentImageCodeInfo()
            self.current_image_code_info = temp_model.from_map(m['CurrentImageCodeInfo'])
        if m.get('DataDiskSize') is not None:
            self.data_disk_size = m.get('DataDiskSize')
        if m.get('DeployMode') is not None:
            self.deploy_mode = m.get('DeployMode')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DockerImageSize') is not None:
            self.docker_image_size = m.get('DockerImageSize')
        if m.get('EnableStartUpConfig') is not None:
            self.enable_start_up_config = m.get('EnableStartUpConfig')
        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ImageScope') is not None:
            self.image_scope = m.get('ImageScope')
        if m.get('ImageSource') is not None:
            self.image_source = m.get('ImageSource')
        if m.get('ImageType') is not None:
            self.image_type = m.get('ImageType')
        if m.get('IsGpu') is not None:
            self.is_gpu = m.get('IsGpu')
        if m.get('IsLinggou') is not None:
            self.is_linggou = m.get('IsLinggou')
        if m.get('IsWorkstation') is not None:
            self.is_workstation = m.get('IsWorkstation')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OperationSystem') is not None:
            self.operation_system = m.get('OperationSystem')
        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')
        if m.get('Permission') is not None:
            self.permission = m.get('Permission')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('ReceiverType') is not None:
            self.receiver_type = m.get('ReceiverType')
        if m.get('ShareCodes') is not None:
            self.share_codes = m.get('ShareCodes')
        if m.get('ShareCodesIncludeDisable') is not None:
            self.share_codes_include_disable = m.get('ShareCodesIncludeDisable')
        if m.get('Shared') is not None:
            self.shared = m.get('Shared')
        if m.get('SharedBy') is not None:
            self.shared_by = m.get('SharedBy')
        if m.get('SourceDesktopId') is not None:
            self.source_desktop_id = m.get('SourceDesktopId')
        if m.get('SourceDesktopType') is not None:
            self.source_desktop_type = m.get('SourceDesktopType')
        if m.get('SourceImageId') is not None:
            self.source_image_id = m.get('SourceImageId')
        if m.get('SourceImageName') is not None:
            self.source_image_name = m.get('SourceImageName')
        if m.get('StartUpFileList') is not None:
            self.start_up_file_list = m.get('StartUpFileList')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SupportPublish') is not None:
            self.support_publish = m.get('SupportPublish')
        if m.get('SystemDiskSize') is not None:
            self.system_disk_size = m.get('SystemDiskSize')
        if m.get('ValidationCode') is not None:
            self.validation_code = m.get('ValidationCode')
        return self


class DescribeAccessibleImagesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[DescribeAccessibleImagesResponseBodyData] = None,
        http_status_code: int = None,
        request_id: str = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.trace_id = trace_id

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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeAccessibleImagesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class DescribeAccessibleImagesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAccessibleImagesResponseBody = None,
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
            temp_model = DescribeAccessibleImagesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCorePackageListRequest(TeaModel):
    def __init__(
        self,
        api_key: str = None,
        query_deduction_instances: bool = None,
        query_scenario: str = None,
    ):
        # This parameter is required.
        self.api_key = api_key
        self.query_deduction_instances = query_deduction_instances
        self.query_scenario = query_scenario

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_key is not None:
            result['ApiKey'] = self.api_key
        if self.query_deduction_instances is not None:
            result['QueryDeductionInstances'] = self.query_deduction_instances
        if self.query_scenario is not None:
            result['QueryScenario'] = self.query_scenario
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiKey') is not None:
            self.api_key = m.get('ApiKey')
        if m.get('QueryDeductionInstances') is not None:
            self.query_deduction_instances = m.get('QueryDeductionInstances')
        if m.get('QueryScenario') is not None:
            self.query_scenario = m.get('QueryScenario')
        return self


class DescribeCorePackageListResponseBodyCorePackageInfoCorePackageListRemainingPeriods(TeaModel):
    def __init__(
        self,
        period_end_time: str = None,
        period_start_time: str = None,
        remaining_core_hours: float = None,
        status: str = None,
        total_core_hours: float = None,
        used_core_hours: float = None,
    ):
        self.period_end_time = period_end_time
        self.period_start_time = period_start_time
        self.remaining_core_hours = remaining_core_hours
        self.status = status
        self.total_core_hours = total_core_hours
        self.used_core_hours = used_core_hours

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.period_end_time is not None:
            result['PeriodEndTime'] = self.period_end_time
        if self.period_start_time is not None:
            result['PeriodStartTime'] = self.period_start_time
        if self.remaining_core_hours is not None:
            result['RemainingCoreHours'] = self.remaining_core_hours
        if self.status is not None:
            result['Status'] = self.status
        if self.total_core_hours is not None:
            result['TotalCoreHours'] = self.total_core_hours
        if self.used_core_hours is not None:
            result['UsedCoreHours'] = self.used_core_hours
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PeriodEndTime') is not None:
            self.period_end_time = m.get('PeriodEndTime')
        if m.get('PeriodStartTime') is not None:
            self.period_start_time = m.get('PeriodStartTime')
        if m.get('RemainingCoreHours') is not None:
            self.remaining_core_hours = m.get('RemainingCoreHours')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TotalCoreHours') is not None:
            self.total_core_hours = m.get('TotalCoreHours')
        if m.get('UsedCoreHours') is not None:
            self.used_core_hours = m.get('UsedCoreHours')
        return self


class DescribeCorePackageListResponseBodyCorePackageInfoCorePackageList(TeaModel):
    def __init__(
        self,
        assigned_core_hours: float = None,
        deduction_instance_list: List[Any] = None,
        expire_time: str = None,
        instance_id: str = None,
        period_end_time: str = None,
        period_start_time: str = None,
        product_type: str = None,
        remaining_core_hours: float = None,
        remaining_periods: List[DescribeCorePackageListResponseBodyCorePackageInfoCorePackageListRemainingPeriods] = None,
        start_time: str = None,
        status: str = None,
        total_core_hours: float = None,
        unassigned_core_hours: float = None,
        used_core_hours: float = None,
    ):
        self.assigned_core_hours = assigned_core_hours
        self.deduction_instance_list = deduction_instance_list
        self.expire_time = expire_time
        self.instance_id = instance_id
        self.period_end_time = period_end_time
        self.period_start_time = period_start_time
        self.product_type = product_type
        self.remaining_core_hours = remaining_core_hours
        self.remaining_periods = remaining_periods
        self.start_time = start_time
        self.status = status
        self.total_core_hours = total_core_hours
        self.unassigned_core_hours = unassigned_core_hours
        self.used_core_hours = used_core_hours

    def validate(self):
        if self.remaining_periods:
            for k in self.remaining_periods:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.assigned_core_hours is not None:
            result['AssignedCoreHours'] = self.assigned_core_hours
        if self.deduction_instance_list is not None:
            result['DeductionInstanceList'] = self.deduction_instance_list
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.period_end_time is not None:
            result['PeriodEndTime'] = self.period_end_time
        if self.period_start_time is not None:
            result['PeriodStartTime'] = self.period_start_time
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.remaining_core_hours is not None:
            result['RemainingCoreHours'] = self.remaining_core_hours
        result['RemainingPeriods'] = []
        if self.remaining_periods is not None:
            for k in self.remaining_periods:
                result['RemainingPeriods'].append(k.to_map() if k else None)
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.total_core_hours is not None:
            result['TotalCoreHours'] = self.total_core_hours
        if self.unassigned_core_hours is not None:
            result['UnassignedCoreHours'] = self.unassigned_core_hours
        if self.used_core_hours is not None:
            result['UsedCoreHours'] = self.used_core_hours
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssignedCoreHours') is not None:
            self.assigned_core_hours = m.get('AssignedCoreHours')
        if m.get('DeductionInstanceList') is not None:
            self.deduction_instance_list = m.get('DeductionInstanceList')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PeriodEndTime') is not None:
            self.period_end_time = m.get('PeriodEndTime')
        if m.get('PeriodStartTime') is not None:
            self.period_start_time = m.get('PeriodStartTime')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('RemainingCoreHours') is not None:
            self.remaining_core_hours = m.get('RemainingCoreHours')
        self.remaining_periods = []
        if m.get('RemainingPeriods') is not None:
            for k in m.get('RemainingPeriods'):
                temp_model = DescribeCorePackageListResponseBodyCorePackageInfoCorePackageListRemainingPeriods()
                self.remaining_periods.append(temp_model.from_map(k))
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TotalCoreHours') is not None:
            self.total_core_hours = m.get('TotalCoreHours')
        if m.get('UnassignedCoreHours') is not None:
            self.unassigned_core_hours = m.get('UnassignedCoreHours')
        if m.get('UsedCoreHours') is not None:
            self.used_core_hours = m.get('UsedCoreHours')
        return self


class DescribeCorePackageListResponseBodyCorePackageInfo(TeaModel):
    def __init__(
        self,
        core_package_list: List[DescribeCorePackageListResponseBodyCorePackageInfoCorePackageList] = None,
        summary_remaining_core_hours: float = None,
    ):
        self.core_package_list = core_package_list
        self.summary_remaining_core_hours = summary_remaining_core_hours

    def validate(self):
        if self.core_package_list:
            for k in self.core_package_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CorePackageList'] = []
        if self.core_package_list is not None:
            for k in self.core_package_list:
                result['CorePackageList'].append(k.to_map() if k else None)
        if self.summary_remaining_core_hours is not None:
            result['SummaryRemainingCoreHours'] = self.summary_remaining_core_hours
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.core_package_list = []
        if m.get('CorePackageList') is not None:
            for k in m.get('CorePackageList'):
                temp_model = DescribeCorePackageListResponseBodyCorePackageInfoCorePackageList()
                self.core_package_list.append(temp_model.from_map(k))
        if m.get('SummaryRemainingCoreHours') is not None:
            self.summary_remaining_core_hours = m.get('SummaryRemainingCoreHours')
        return self


class DescribeCorePackageListResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        core_package_info: DescribeCorePackageListResponseBodyCorePackageInfo = None,
        message: str = None,
        request_id: str = None,
        trace_id: str = None,
    ):
        self.code = code
        self.core_package_info = core_package_info
        self.message = message
        self.request_id = request_id
        self.trace_id = trace_id

    def validate(self):
        if self.core_package_info:
            self.core_package_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.core_package_info is not None:
            result['CorePackageInfo'] = self.core_package_info.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('CorePackageInfo') is not None:
            temp_model = DescribeCorePackageListResponseBodyCorePackageInfo()
            self.core_package_info = temp_model.from_map(m['CorePackageInfo'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class DescribeCorePackageListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeCorePackageListResponseBody = None,
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
            temp_model = DescribeCorePackageListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDesktopsRequest(TeaModel):
    def __init__(
        self,
        api_key: str = None,
        display_type: str = None,
        max_results: int = None,
        next_token: str = None,
    ):
        # This parameter is required.
        self.api_key = api_key
        self.display_type = display_type
        self.max_results = max_results
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_key is not None:
            result['ApiKey'] = self.api_key
        if self.display_type is not None:
            result['DisplayType'] = self.display_type
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiKey') is not None:
            self.api_key = m.get('ApiKey')
        if m.get('DisplayType') is not None:
            self.display_type = m.get('DisplayType')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class DescribeDesktopsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        result: Any = None,
        trace_id: str = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id
        self.result = result
        self.trace_id = trace_id

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
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class DescribeDesktopsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDesktopsResponseBody = None,
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
            temp_model = DescribeDesktopsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeImageDetailRequest(TeaModel):
    def __init__(
        self,
        api_key: str = None,
        image_id: str = None,
        session_id: str = None,
        share_code: str = None,
    ):
        # This parameter is required.
        self.api_key = api_key
        self.image_id = image_id
        self.session_id = session_id
        self.share_code = share_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_key is not None:
            result['ApiKey'] = self.api_key
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.share_code is not None:
            result['ShareCode'] = self.share_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiKey') is not None:
            self.api_key = m.get('ApiKey')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('ShareCode') is not None:
            self.share_code = m.get('ShareCode')
        return self


class DescribeImageDetailResponseBodyDataCurrentImageCodeInfo(TeaModel):
    def __init__(
        self,
        current_password: str = None,
        expire_time: str = None,
        gmt_created: str = None,
        gmt_modified: str = None,
        image_code: str = None,
        is_copy_password: bool = None,
        is_encrypted: bool = None,
        is_free: bool = None,
        period_days: int = None,
        redeem_count: int = None,
        redeem_quota: int = None,
    ):
        self.current_password = current_password
        self.expire_time = expire_time
        self.gmt_created = gmt_created
        self.gmt_modified = gmt_modified
        self.image_code = image_code
        self.is_copy_password = is_copy_password
        self.is_encrypted = is_encrypted
        self.is_free = is_free
        self.period_days = period_days
        self.redeem_count = redeem_count
        self.redeem_quota = redeem_quota

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_password is not None:
            result['CurrentPassword'] = self.current_password
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.image_code is not None:
            result['ImageCode'] = self.image_code
        if self.is_copy_password is not None:
            result['IsCopyPassword'] = self.is_copy_password
        if self.is_encrypted is not None:
            result['IsEncrypted'] = self.is_encrypted
        if self.is_free is not None:
            result['IsFree'] = self.is_free
        if self.period_days is not None:
            result['PeriodDays'] = self.period_days
        if self.redeem_count is not None:
            result['RedeemCount'] = self.redeem_count
        if self.redeem_quota is not None:
            result['RedeemQuota'] = self.redeem_quota
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPassword') is not None:
            self.current_password = m.get('CurrentPassword')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('ImageCode') is not None:
            self.image_code = m.get('ImageCode')
        if m.get('IsCopyPassword') is not None:
            self.is_copy_password = m.get('IsCopyPassword')
        if m.get('IsEncrypted') is not None:
            self.is_encrypted = m.get('IsEncrypted')
        if m.get('IsFree') is not None:
            self.is_free = m.get('IsFree')
        if m.get('PeriodDays') is not None:
            self.period_days = m.get('PeriodDays')
        if m.get('RedeemCount') is not None:
            self.redeem_count = m.get('RedeemCount')
        if m.get('RedeemQuota') is not None:
            self.redeem_quota = m.get('RedeemQuota')
        return self


class DescribeImageDetailResponseBodyData(TeaModel):
    def __init__(
        self,
        current_image_code_info: DescribeImageDetailResponseBodyDataCurrentImageCodeInfo = None,
        data_disk_size: int = None,
        description: str = None,
        enable_start_up_config: bool = None,
        gmt_created: str = None,
        image_id: str = None,
        image_scope: str = None,
        is_gpu: bool = None,
        name: str = None,
        os_type: str = None,
        permission: str = None,
        platform: str = None,
        progress: str = None,
        share_codes: List[str] = None,
        share_codes_include_disable: List[str] = None,
        shared: bool = None,
        source_desktop_type: str = None,
        start_up_file_list: List[str] = None,
        status: str = None,
        system_disk_size: int = None,
    ):
        self.current_image_code_info = current_image_code_info
        self.data_disk_size = data_disk_size
        self.description = description
        self.enable_start_up_config = enable_start_up_config
        self.gmt_created = gmt_created
        self.image_id = image_id
        self.image_scope = image_scope
        self.is_gpu = is_gpu
        self.name = name
        self.os_type = os_type
        self.permission = permission
        self.platform = platform
        self.progress = progress
        self.share_codes = share_codes
        self.share_codes_include_disable = share_codes_include_disable
        self.shared = shared
        self.source_desktop_type = source_desktop_type
        self.start_up_file_list = start_up_file_list
        self.status = status
        self.system_disk_size = system_disk_size

    def validate(self):
        if self.current_image_code_info:
            self.current_image_code_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_image_code_info is not None:
            result['CurrentImageCodeInfo'] = self.current_image_code_info.to_map()
        if self.data_disk_size is not None:
            result['DataDiskSize'] = self.data_disk_size
        if self.description is not None:
            result['Description'] = self.description
        if self.enable_start_up_config is not None:
            result['EnableStartUpConfig'] = self.enable_start_up_config
        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.image_scope is not None:
            result['ImageScope'] = self.image_scope
        if self.is_gpu is not None:
            result['IsGpu'] = self.is_gpu
        if self.name is not None:
            result['Name'] = self.name
        if self.os_type is not None:
            result['OsType'] = self.os_type
        if self.permission is not None:
            result['Permission'] = self.permission
        if self.platform is not None:
            result['Platform'] = self.platform
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.share_codes is not None:
            result['ShareCodes'] = self.share_codes
        if self.share_codes_include_disable is not None:
            result['ShareCodesIncludeDisable'] = self.share_codes_include_disable
        if self.shared is not None:
            result['Shared'] = self.shared
        if self.source_desktop_type is not None:
            result['SourceDesktopType'] = self.source_desktop_type
        if self.start_up_file_list is not None:
            result['StartUpFileList'] = self.start_up_file_list
        if self.status is not None:
            result['Status'] = self.status
        if self.system_disk_size is not None:
            result['SystemDiskSize'] = self.system_disk_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentImageCodeInfo') is not None:
            temp_model = DescribeImageDetailResponseBodyDataCurrentImageCodeInfo()
            self.current_image_code_info = temp_model.from_map(m['CurrentImageCodeInfo'])
        if m.get('DataDiskSize') is not None:
            self.data_disk_size = m.get('DataDiskSize')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EnableStartUpConfig') is not None:
            self.enable_start_up_config = m.get('EnableStartUpConfig')
        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ImageScope') is not None:
            self.image_scope = m.get('ImageScope')
        if m.get('IsGpu') is not None:
            self.is_gpu = m.get('IsGpu')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')
        if m.get('Permission') is not None:
            self.permission = m.get('Permission')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('ShareCodes') is not None:
            self.share_codes = m.get('ShareCodes')
        if m.get('ShareCodesIncludeDisable') is not None:
            self.share_codes_include_disable = m.get('ShareCodesIncludeDisable')
        if m.get('Shared') is not None:
            self.shared = m.get('Shared')
        if m.get('SourceDesktopType') is not None:
            self.source_desktop_type = m.get('SourceDesktopType')
        if m.get('StartUpFileList') is not None:
            self.start_up_file_list = m.get('StartUpFileList')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SystemDiskSize') is not None:
            self.system_disk_size = m.get('SystemDiskSize')
        return self


class DescribeImageDetailResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: DescribeImageDetailResponseBodyData = None,
        http_status_code: int = None,
        request_id: str = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.trace_id = trace_id

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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = DescribeImageDetailResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class DescribeImageDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeImageDetailResponseBody = None,
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
            temp_model = DescribeImageDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePackageOrdersRequest(TeaModel):
    def __init__(
        self,
        api_key: str = None,
        current_page: int = None,
        desktop_id_list: List[str] = None,
        order_id_list: List[str] = None,
        order_status_list: List[str] = None,
        page_size: int = None,
        product_type_list: List[str] = None,
        resource_id_list: List[str] = None,
        session_id: str = None,
    ):
        # This parameter is required.
        self.api_key = api_key
        self.current_page = current_page
        self.desktop_id_list = desktop_id_list
        self.order_id_list = order_id_list
        self.order_status_list = order_status_list
        self.page_size = page_size
        self.product_type_list = product_type_list
        self.resource_id_list = resource_id_list
        self.session_id = session_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_key is not None:
            result['ApiKey'] = self.api_key
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.desktop_id_list is not None:
            result['DesktopIdList'] = self.desktop_id_list
        if self.order_id_list is not None:
            result['OrderIdList'] = self.order_id_list
        if self.order_status_list is not None:
            result['OrderStatusList'] = self.order_status_list
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.product_type_list is not None:
            result['ProductTypeList'] = self.product_type_list
        if self.resource_id_list is not None:
            result['ResourceIdList'] = self.resource_id_list
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiKey') is not None:
            self.api_key = m.get('ApiKey')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('DesktopIdList') is not None:
            self.desktop_id_list = m.get('DesktopIdList')
        if m.get('OrderIdList') is not None:
            self.order_id_list = m.get('OrderIdList')
        if m.get('OrderStatusList') is not None:
            self.order_status_list = m.get('OrderStatusList')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProductTypeList') is not None:
            self.product_type_list = m.get('ProductTypeList')
        if m.get('ResourceIdList') is not None:
            self.resource_id_list = m.get('ResourceIdList')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        return self


class DescribePackageOrdersShrinkRequest(TeaModel):
    def __init__(
        self,
        api_key: str = None,
        current_page: int = None,
        desktop_id_list_shrink: str = None,
        order_id_list_shrink: str = None,
        order_status_list_shrink: str = None,
        page_size: int = None,
        product_type_list_shrink: str = None,
        resource_id_list_shrink: str = None,
        session_id: str = None,
    ):
        # This parameter is required.
        self.api_key = api_key
        self.current_page = current_page
        self.desktop_id_list_shrink = desktop_id_list_shrink
        self.order_id_list_shrink = order_id_list_shrink
        self.order_status_list_shrink = order_status_list_shrink
        self.page_size = page_size
        self.product_type_list_shrink = product_type_list_shrink
        self.resource_id_list_shrink = resource_id_list_shrink
        self.session_id = session_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_key is not None:
            result['ApiKey'] = self.api_key
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.desktop_id_list_shrink is not None:
            result['DesktopIdList'] = self.desktop_id_list_shrink
        if self.order_id_list_shrink is not None:
            result['OrderIdList'] = self.order_id_list_shrink
        if self.order_status_list_shrink is not None:
            result['OrderStatusList'] = self.order_status_list_shrink
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.product_type_list_shrink is not None:
            result['ProductTypeList'] = self.product_type_list_shrink
        if self.resource_id_list_shrink is not None:
            result['ResourceIdList'] = self.resource_id_list_shrink
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiKey') is not None:
            self.api_key = m.get('ApiKey')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('DesktopIdList') is not None:
            self.desktop_id_list_shrink = m.get('DesktopIdList')
        if m.get('OrderIdList') is not None:
            self.order_id_list_shrink = m.get('OrderIdList')
        if m.get('OrderStatusList') is not None:
            self.order_status_list_shrink = m.get('OrderStatusList')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProductTypeList') is not None:
            self.product_type_list_shrink = m.get('ProductTypeList')
        if m.get('ResourceIdList') is not None:
            self.resource_id_list_shrink = m.get('ResourceIdList')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        return self


class DescribePackageOrdersResponseBodyPageOrderList(TeaModel):
    def __init__(
        self,
        amount: int = None,
        creator_ali_uid: int = None,
        delivery_address: str = None,
        desktop_id: str = None,
        gmt_canceled_time: str = None,
        gmt_create_time: str = None,
        gmt_paid_time: str = None,
        instance_id: str = None,
        order_id: str = None,
        order_status: str = None,
        order_type: str = None,
        product_code: str = None,
        product_sku_code: str = None,
        product_type: str = None,
        trade_price: str = None,
    ):
        self.amount = amount
        self.creator_ali_uid = creator_ali_uid
        self.delivery_address = delivery_address
        self.desktop_id = desktop_id
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ssZ
        self.gmt_canceled_time = gmt_canceled_time
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ssZ
        self.gmt_create_time = gmt_create_time
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ssZ
        self.gmt_paid_time = gmt_paid_time
        self.instance_id = instance_id
        self.order_id = order_id
        self.order_status = order_status
        self.order_type = order_type
        self.product_code = product_code
        self.product_sku_code = product_sku_code
        self.product_type = product_type
        self.trade_price = trade_price

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.creator_ali_uid is not None:
            result['CreatorAliUid'] = self.creator_ali_uid
        if self.delivery_address is not None:
            result['DeliveryAddress'] = self.delivery_address
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.gmt_canceled_time is not None:
            result['GmtCanceledTime'] = self.gmt_canceled_time
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_paid_time is not None:
            result['GmtPaidTime'] = self.gmt_paid_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.order_status is not None:
            result['OrderStatus'] = self.order_status
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.product_sku_code is not None:
            result['ProductSkuCode'] = self.product_sku_code
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.trade_price is not None:
            result['TradePrice'] = self.trade_price
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('CreatorAliUid') is not None:
            self.creator_ali_uid = m.get('CreatorAliUid')
        if m.get('DeliveryAddress') is not None:
            self.delivery_address = m.get('DeliveryAddress')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('GmtCanceledTime') is not None:
            self.gmt_canceled_time = m.get('GmtCanceledTime')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtPaidTime') is not None:
            self.gmt_paid_time = m.get('GmtPaidTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('OrderStatus') is not None:
            self.order_status = m.get('OrderStatus')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProductSkuCode') is not None:
            self.product_sku_code = m.get('ProductSkuCode')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('TradePrice') is not None:
            self.trade_price = m.get('TradePrice')
        return self


class DescribePackageOrdersResponseBodyPage(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        order_list: List[DescribePackageOrdersResponseBodyPageOrderList] = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.current_page = current_page
        self.order_list = order_list
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.order_list:
            for k in self.order_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['OrderList'] = []
        if self.order_list is not None:
            for k in self.order_list:
                result['OrderList'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.order_list = []
        if m.get('OrderList') is not None:
            for k in m.get('OrderList'):
                temp_model = DescribePackageOrdersResponseBodyPageOrderList()
                self.order_list.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribePackageOrdersResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        page: DescribePackageOrdersResponseBodyPage = None,
        request_id: str = None,
        trace_id: str = None,
    ):
        self.code = code
        self.message = message
        self.page = page
        self.request_id = request_id
        self.trace_id = trace_id

    def validate(self):
        if self.page:
            self.page.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.page is not None:
            result['Page'] = self.page.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Page') is not None:
            temp_model = DescribePackageOrdersResponseBodyPage()
            self.page = temp_model.from_map(m['Page'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class DescribePackageOrdersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribePackageOrdersResponseBody = None,
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
            temp_model = DescribePackageOrdersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateWuyingServerSceneUrlRequest(TeaModel):
    def __init__(
        self,
        client_id: str = None,
        client_ip: str = None,
        client_os: str = None,
        client_type: str = None,
        client_version: str = None,
        end_user_id: str = None,
        login_region_id: str = None,
        login_token: str = None,
        product_type: str = None,
        scene: str = None,
        session_id: str = None,
        uuid: str = None,
        wuying_server_id: str = None,
    ):
        self.client_id = client_id
        self.client_ip = client_ip
        self.client_os = client_os
        self.client_type = client_type
        self.client_version = client_version
        self.end_user_id = end_user_id
        self.login_region_id = login_region_id
        # This parameter is required.
        self.login_token = login_token
        # This parameter is required.
        self.product_type = product_type
        # This parameter is required.
        self.scene = scene
        # This parameter is required.
        self.session_id = session_id
        self.uuid = uuid
        # This parameter is required.
        self.wuying_server_id = wuying_server_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.client_ip is not None:
            result['ClientIp'] = self.client_ip
        if self.client_os is not None:
            result['ClientOS'] = self.client_os
        if self.client_type is not None:
            result['ClientType'] = self.client_type
        if self.client_version is not None:
            result['ClientVersion'] = self.client_version
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        if self.login_region_id is not None:
            result['LoginRegionId'] = self.login_region_id
        if self.login_token is not None:
            result['LoginToken'] = self.login_token
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.scene is not None:
            result['Scene'] = self.scene
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        if self.wuying_server_id is not None:
            result['WuyingServerId'] = self.wuying_server_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('ClientIp') is not None:
            self.client_ip = m.get('ClientIp')
        if m.get('ClientOS') is not None:
            self.client_os = m.get('ClientOS')
        if m.get('ClientType') is not None:
            self.client_type = m.get('ClientType')
        if m.get('ClientVersion') is not None:
            self.client_version = m.get('ClientVersion')
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        if m.get('LoginRegionId') is not None:
            self.login_region_id = m.get('LoginRegionId')
        if m.get('LoginToken') is not None:
            self.login_token = m.get('LoginToken')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('Scene') is not None:
            self.scene = m.get('Scene')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        if m.get('WuyingServerId') is not None:
            self.wuying_server_id = m.get('WuyingServerId')
        return self


class GenerateWuyingServerSceneUrlResponseBody(TeaModel):
    def __init__(
        self,
        expire_duration_hours: int = None,
        expire_time: str = None,
        request_id: str = None,
        url: str = None,
    ):
        self.expire_duration_hours = expire_duration_hours
        self.expire_time = expire_time
        self.request_id = request_id
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expire_duration_hours is not None:
            result['ExpireDurationHours'] = self.expire_duration_hours
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpireDurationHours') is not None:
            self.expire_duration_hours = m.get('ExpireDurationHours')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class GenerateWuyingServerSceneUrlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GenerateWuyingServerSceneUrlResponseBody = None,
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
            temp_model = GenerateWuyingServerSceneUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetProductListRequest(TeaModel):
    def __init__(
        self,
        api_key: str = None,
        config_version: str = None,
        max_results: int = None,
        next_token: str = None,
        session_id: str = None,
        type: str = None,
    ):
        # This parameter is required.
        self.api_key = api_key
        self.config_version = config_version
        self.max_results = max_results
        self.next_token = next_token
        self.session_id = session_id
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_key is not None:
            result['ApiKey'] = self.api_key
        if self.config_version is not None:
            result['ConfigVersion'] = self.config_version
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiKey') is not None:
            self.api_key = m.get('ApiKey')
        if m.get('ConfigVersion') is not None:
            self.config_version = m.get('ConfigVersion')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetProductListResponseBodyDisplayInfoProductListSkuList(TeaModel):
    def __init__(
        self,
        apple_sku_code: str = None,
        attribute: str = None,
        purchase_mode: str = None,
        sku_code: str = None,
        sku_desc: str = None,
        sku_name: str = None,
    ):
        self.apple_sku_code = apple_sku_code
        self.attribute = attribute
        self.purchase_mode = purchase_mode
        self.sku_code = sku_code
        self.sku_desc = sku_desc
        self.sku_name = sku_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apple_sku_code is not None:
            result['AppleSkuCode'] = self.apple_sku_code
        if self.attribute is not None:
            result['Attribute'] = self.attribute
        if self.purchase_mode is not None:
            result['PurchaseMode'] = self.purchase_mode
        if self.sku_code is not None:
            result['SkuCode'] = self.sku_code
        if self.sku_desc is not None:
            result['SkuDesc'] = self.sku_desc
        if self.sku_name is not None:
            result['SkuName'] = self.sku_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppleSkuCode') is not None:
            self.apple_sku_code = m.get('AppleSkuCode')
        if m.get('Attribute') is not None:
            self.attribute = m.get('Attribute')
        if m.get('PurchaseMode') is not None:
            self.purchase_mode = m.get('PurchaseMode')
        if m.get('SkuCode') is not None:
            self.sku_code = m.get('SkuCode')
        if m.get('SkuDesc') is not None:
            self.sku_desc = m.get('SkuDesc')
        if m.get('SkuName') is not None:
            self.sku_name = m.get('SkuName')
        return self


class GetProductListResponseBodyDisplayInfoProductList(TeaModel):
    def __init__(
        self,
        display_attribute: str = None,
        display_config: str = None,
        dynamic_attribute: str = None,
        is_enable: bool = None,
        modification_level: int = None,
        product_code: str = None,
        product_desc: str = None,
        product_group: str = None,
        product_name: str = None,
        product_type: str = None,
        sku_list: List[GetProductListResponseBodyDisplayInfoProductListSkuList] = None,
    ):
        self.display_attribute = display_attribute
        self.display_config = display_config
        self.dynamic_attribute = dynamic_attribute
        self.is_enable = is_enable
        self.modification_level = modification_level
        self.product_code = product_code
        self.product_desc = product_desc
        self.product_group = product_group
        self.product_name = product_name
        self.product_type = product_type
        self.sku_list = sku_list

    def validate(self):
        if self.sku_list:
            for k in self.sku_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display_attribute is not None:
            result['DisplayAttribute'] = self.display_attribute
        if self.display_config is not None:
            result['DisplayConfig'] = self.display_config
        if self.dynamic_attribute is not None:
            result['DynamicAttribute'] = self.dynamic_attribute
        if self.is_enable is not None:
            result['IsEnable'] = self.is_enable
        if self.modification_level is not None:
            result['ModificationLevel'] = self.modification_level
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.product_desc is not None:
            result['ProductDesc'] = self.product_desc
        if self.product_group is not None:
            result['ProductGroup'] = self.product_group
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        result['SkuList'] = []
        if self.sku_list is not None:
            for k in self.sku_list:
                result['SkuList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayAttribute') is not None:
            self.display_attribute = m.get('DisplayAttribute')
        if m.get('DisplayConfig') is not None:
            self.display_config = m.get('DisplayConfig')
        if m.get('DynamicAttribute') is not None:
            self.dynamic_attribute = m.get('DynamicAttribute')
        if m.get('IsEnable') is not None:
            self.is_enable = m.get('IsEnable')
        if m.get('ModificationLevel') is not None:
            self.modification_level = m.get('ModificationLevel')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProductDesc') is not None:
            self.product_desc = m.get('ProductDesc')
        if m.get('ProductGroup') is not None:
            self.product_group = m.get('ProductGroup')
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        self.sku_list = []
        if m.get('SkuList') is not None:
            for k in m.get('SkuList'):
                temp_model = GetProductListResponseBodyDisplayInfoProductListSkuList()
                self.sku_list.append(temp_model.from_map(k))
        return self


class GetProductListResponseBodyDisplayInfo(TeaModel):
    def __init__(
        self,
        product_list: List[GetProductListResponseBodyDisplayInfoProductList] = None,
    ):
        self.product_list = product_list

    def validate(self):
        if self.product_list:
            for k in self.product_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ProductList'] = []
        if self.product_list is not None:
            for k in self.product_list:
                result['ProductList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.product_list = []
        if m.get('ProductList') is not None:
            for k in m.get('ProductList'):
                temp_model = GetProductListResponseBodyDisplayInfoProductList()
                self.product_list.append(temp_model.from_map(k))
        return self


class GetProductListResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        display_info: GetProductListResponseBodyDisplayInfo = None,
        max_results: int = None,
        message: str = None,
        next_token: str = None,
        request_id: str = None,
        trace_id: str = None,
    ):
        self.code = code
        self.display_info = display_info
        self.max_results = max_results
        self.message = message
        self.next_token = next_token
        self.request_id = request_id
        self.trace_id = trace_id

    def validate(self):
        if self.display_info:
            self.display_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.display_info is not None:
            result['DisplayInfo'] = self.display_info.to_map()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.message is not None:
            result['Message'] = self.message
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DisplayInfo') is not None:
            temp_model = GetProductListResponseBodyDisplayInfo()
            self.display_info = temp_model.from_map(m['DisplayInfo'])
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class GetProductListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetProductListResponseBody = None,
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
            temp_model = GetProductListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserInfoRequest(TeaModel):
    def __init__(
        self,
        api_key: str = None,
    ):
        # This parameter is required.
        self.api_key = api_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_key is not None:
            result['ApiKey'] = self.api_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiKey') is not None:
            self.api_key = m.get('ApiKey')
        return self


class GetUserInfoResponseBody(TeaModel):
    def __init__(
        self,
        aliyun_id: str = None,
        nick_name: str = None,
        phone: str = None,
        request_id: str = None,
        union_id: str = None,
    ):
        self.aliyun_id = aliyun_id
        self.nick_name = nick_name
        self.phone = phone
        self.request_id = request_id
        self.union_id = union_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aliyun_id is not None:
            result['AliyunId'] = self.aliyun_id
        if self.nick_name is not None:
            result['NickName'] = self.nick_name
        if self.phone is not None:
            result['Phone'] = self.phone
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.union_id is not None:
            result['UnionId'] = self.union_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunId') is not None:
            self.aliyun_id = m.get('AliyunId')
        if m.get('NickName') is not None:
            self.nick_name = m.get('NickName')
        if m.get('Phone') is not None:
            self.phone = m.get('Phone')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UnionId') is not None:
            self.union_id = m.get('UnionId')
        return self


class GetUserInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetUserInfoResponseBody = None,
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
            temp_model = GetUserInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartDesktopRequest(TeaModel):
    def __init__(
        self,
        api_key: str = None,
        desktop_id: str = None,
        session_id: str = None,
    ):
        # This parameter is required.
        self.api_key = api_key
        # This parameter is required.
        self.desktop_id = desktop_id
        self.session_id = session_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_key is not None:
            result['ApiKey'] = self.api_key
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiKey') is not None:
            self.api_key = m.get('ApiKey')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        return self


class StartDesktopResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        request_id: str = None,
        trace_id: str = None,
    ):
        self.code = code
        self.request_id = request_id
        self.trace_id = trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class StartDesktopResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StartDesktopResponseBody = None,
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
            temp_model = StartDesktopResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopDesktopRequest(TeaModel):
    def __init__(
        self,
        api_key: str = None,
        desktop_id: str = None,
        session_id: str = None,
    ):
        # This parameter is required.
        self.api_key = api_key
        # This parameter is required.
        self.desktop_id = desktop_id
        self.session_id = session_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_key is not None:
            result['ApiKey'] = self.api_key
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiKey') is not None:
            self.api_key = m.get('ApiKey')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        return self


class StopDesktopResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        request_id: str = None,
        trace_id: str = None,
    ):
        self.code = code
        self.request_id = request_id
        self.trace_id = trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class StopDesktopResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StopDesktopResponseBody = None,
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
            temp_model = StopDesktopResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


