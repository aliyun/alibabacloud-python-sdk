# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict


class ProductInstance(TeaModel):
    def __init__(
        self,
        app_code: str = None,
        buyer_name: str = None,
        buyer_uid: str = None,
        channel: str = None,
        config: str = None,
        end: int = None,
        instance_id: str = None,
        order_no: str = None,
        product_code: str = None,
        product_spec_code: str = None,
        start: int = None,
        tenant_name: str = None,
        tenant_uid: str = None,
    ):
        # 应用码
        self.app_code = app_code
        # 购买者名称
        self.buyer_name = buyer_name
        # 购买者账号uid
        self.buyer_uid = buyer_uid
        # 商业化渠道码
        self.channel = channel
        # 购买配置信息
        self.config = config
        # 生效结束时间
        self.end = end
        # 实例id
        self.instance_id = instance_id
        # 订单号，幂等使用
        self.order_no = order_no
        # 产品码
        self.product_code = product_code
        # 规格码
        self.product_spec_code = product_spec_code
        # 生效开始时间
        self.start = start
        # 租户名称
        self.tenant_name = tenant_name
        # 租户uid
        self.tenant_uid = tenant_uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_code is not None:
            result['appCode'] = self.app_code
        if self.buyer_name is not None:
            result['buyerName'] = self.buyer_name
        if self.buyer_uid is not None:
            result['buyerUid'] = self.buyer_uid
        if self.channel is not None:
            result['channel'] = self.channel
        if self.config is not None:
            result['config'] = self.config
        if self.end is not None:
            result['end'] = self.end
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.order_no is not None:
            result['orderNo'] = self.order_no
        if self.product_code is not None:
            result['productCode'] = self.product_code
        if self.product_spec_code is not None:
            result['productSpecCode'] = self.product_spec_code
        if self.start is not None:
            result['start'] = self.start
        if self.tenant_name is not None:
            result['tenantName'] = self.tenant_name
        if self.tenant_uid is not None:
            result['tenantUid'] = self.tenant_uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appCode') is not None:
            self.app_code = m.get('appCode')
        if m.get('buyerName') is not None:
            self.buyer_name = m.get('buyerName')
        if m.get('buyerUid') is not None:
            self.buyer_uid = m.get('buyerUid')
        if m.get('channel') is not None:
            self.channel = m.get('channel')
        if m.get('config') is not None:
            self.config = m.get('config')
        if m.get('end') is not None:
            self.end = m.get('end')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('orderNo') is not None:
            self.order_no = m.get('orderNo')
        if m.get('productCode') is not None:
            self.product_code = m.get('productCode')
        if m.get('productSpecCode') is not None:
            self.product_spec_code = m.get('productSpecCode')
        if m.get('start') is not None:
            self.start = m.get('start')
        if m.get('tenantName') is not None:
            self.tenant_name = m.get('tenantName')
        if m.get('tenantUid') is not None:
            self.tenant_uid = m.get('tenantUid')
        return self


class CloseProductRequest(TeaModel):
    def __init__(
        self,
        product_instance: ProductInstance = None,
    ):
        self.product_instance = product_instance

    def validate(self):
        if self.product_instance:
            self.product_instance.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product_instance is not None:
            result['productInstance'] = self.product_instance.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('productInstance') is not None:
            temp_model = ProductInstance()
            self.product_instance = temp_model.from_map(m['productInstance'])
        return self


class CloseProductResponseBody(TeaModel):
    def __init__(
        self,
        data: int = None,
        request_id: str = None,
    ):
        self.data = data
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CloseProductResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CloseProductResponseBody = None,
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
            temp_model = CloseProductResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConsoleProxyRequest(TeaModel):
    def __init__(
        self,
        app_code: str = None,
        interface_name: str = None,
        param_json: str = None,
    ):
        self.app_code = app_code
        self.interface_name = interface_name
        self.param_json = param_json

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_code is not None:
            result['appCode'] = self.app_code
        if self.interface_name is not None:
            result['interfaceName'] = self.interface_name
        if self.param_json is not None:
            result['paramJson'] = self.param_json
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appCode') is not None:
            self.app_code = m.get('appCode')
        if m.get('interfaceName') is not None:
            self.interface_name = m.get('interfaceName')
        if m.get('paramJson') is not None:
            self.param_json = m.get('paramJson')
        return self


class ConsoleProxyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result_json: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.result_json = result_json

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result_json is not None:
            result['resultJson'] = self.result_json
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('resultJson') is not None:
            self.result_json = m.get('resultJson')
        return self


class ConsoleProxyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ConsoleProxyResponseBody = None,
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
            temp_model = ConsoleProxyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OpenProductRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        product_instance: ProductInstance = None,
    ):
        # 幂等参数
        self.client_token = client_token
        self.product_instance = product_instance

    def validate(self):
        if self.product_instance:
            self.product_instance.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.product_instance is not None:
            result['productInstance'] = self.product_instance.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('productInstance') is not None:
            temp_model = ProductInstance()
            self.product_instance = temp_model.from_map(m['productInstance'])
        return self


class OpenProductResponseBody(TeaModel):
    def __init__(
        self,
        id: int = None,
        request_id: str = None,
    ):
        self.id = id
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class OpenProductResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: OpenProductResponseBody = None,
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
            temp_model = OpenProductResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


