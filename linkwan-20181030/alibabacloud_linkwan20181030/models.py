# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict


class GetKpmEncryptedNodeTuplesByOrderIdRequest(TeaModel):
    def __init__(
        self,
        api_product: str = None,
        api_revision: str = None,
        order_id: int = None,
    ):
        self.api_product = api_product
        self.api_revision = api_revision
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.api_product is not None:
            result['ApiProduct'] = self.api_product
        if self.api_revision is not None:
            result['ApiRevision'] = self.api_revision
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiProduct') is not None:
            self.api_product = m.get('ApiProduct')
        if m.get('ApiRevision') is not None:
            self.api_revision = m.get('ApiRevision')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class GetKpmEncryptedNodeTuplesByOrderIdResponseBodyEncryptedNodeTuplesEncryptedNodeTuple(TeaModel):
    def __init__(
        self,
        app_key_kcv: str = None,
        dev_eui: str = None,
        encrypted_nwk_key: str = None,
        nwk_key_kcv: str = None,
        encrypted_gen_app_key: str = None,
        pin_code: str = None,
        gen_app_key_kcv: str = None,
        lora_version: str = None,
        encrypted_app_key: str = None,
    ):
        self.app_key_kcv = app_key_kcv
        self.dev_eui = dev_eui
        self.encrypted_nwk_key = encrypted_nwk_key
        self.nwk_key_kcv = nwk_key_kcv
        self.encrypted_gen_app_key = encrypted_gen_app_key
        self.pin_code = pin_code
        self.gen_app_key_kcv = gen_app_key_kcv
        self.lora_version = lora_version
        self.encrypted_app_key = encrypted_app_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_key_kcv is not None:
            result['AppKeyKcv'] = self.app_key_kcv
        if self.dev_eui is not None:
            result['DevEui'] = self.dev_eui
        if self.encrypted_nwk_key is not None:
            result['EncryptedNwkKey'] = self.encrypted_nwk_key
        if self.nwk_key_kcv is not None:
            result['NwkKeyKcv'] = self.nwk_key_kcv
        if self.encrypted_gen_app_key is not None:
            result['EncryptedGenAppKey'] = self.encrypted_gen_app_key
        if self.pin_code is not None:
            result['PinCode'] = self.pin_code
        if self.gen_app_key_kcv is not None:
            result['GenAppKeyKcv'] = self.gen_app_key_kcv
        if self.lora_version is not None:
            result['LoraVersion'] = self.lora_version
        if self.encrypted_app_key is not None:
            result['EncryptedAppKey'] = self.encrypted_app_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKeyKcv') is not None:
            self.app_key_kcv = m.get('AppKeyKcv')
        if m.get('DevEui') is not None:
            self.dev_eui = m.get('DevEui')
        if m.get('EncryptedNwkKey') is not None:
            self.encrypted_nwk_key = m.get('EncryptedNwkKey')
        if m.get('NwkKeyKcv') is not None:
            self.nwk_key_kcv = m.get('NwkKeyKcv')
        if m.get('EncryptedGenAppKey') is not None:
            self.encrypted_gen_app_key = m.get('EncryptedGenAppKey')
        if m.get('PinCode') is not None:
            self.pin_code = m.get('PinCode')
        if m.get('GenAppKeyKcv') is not None:
            self.gen_app_key_kcv = m.get('GenAppKeyKcv')
        if m.get('LoraVersion') is not None:
            self.lora_version = m.get('LoraVersion')
        if m.get('EncryptedAppKey') is not None:
            self.encrypted_app_key = m.get('EncryptedAppKey')
        return self


class GetKpmEncryptedNodeTuplesByOrderIdResponseBodyEncryptedNodeTuples(TeaModel):
    def __init__(
        self,
        encrypted_node_tuple: List[GetKpmEncryptedNodeTuplesByOrderIdResponseBodyEncryptedNodeTuplesEncryptedNodeTuple] = None,
    ):
        self.encrypted_node_tuple = encrypted_node_tuple

    def validate(self):
        if self.encrypted_node_tuple:
            for k in self.encrypted_node_tuple:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['EncryptedNodeTuple'] = []
        if self.encrypted_node_tuple is not None:
            for k in self.encrypted_node_tuple:
                result['EncryptedNodeTuple'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.encrypted_node_tuple = []
        if m.get('EncryptedNodeTuple') is not None:
            for k in m.get('EncryptedNodeTuple'):
                temp_model = GetKpmEncryptedNodeTuplesByOrderIdResponseBodyEncryptedNodeTuplesEncryptedNodeTuple()
                self.encrypted_node_tuple.append(temp_model.from_map(k))
        return self


class GetKpmEncryptedNodeTuplesByOrderIdResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        message: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        encrypted_node_tuples: GetKpmEncryptedNodeTuplesByOrderIdResponseBodyEncryptedNodeTuples = None,
        code: str = None,
        success: bool = None,
        encrypted_session_zmk: str = None,
    ):
        self.request_id = request_id
        self.message = message
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.encrypted_node_tuples = encrypted_node_tuples
        self.code = code
        self.success = success
        self.encrypted_session_zmk = encrypted_session_zmk

    def validate(self):
        if self.encrypted_node_tuples:
            self.encrypted_node_tuples.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.encrypted_node_tuples is not None:
            result['EncryptedNodeTuples'] = self.encrypted_node_tuples.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        if self.encrypted_session_zmk is not None:
            result['EncryptedSessionZmk'] = self.encrypted_session_zmk
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('EncryptedNodeTuples') is not None:
            temp_model = GetKpmEncryptedNodeTuplesByOrderIdResponseBodyEncryptedNodeTuples()
            self.encrypted_node_tuples = temp_model.from_map(m['EncryptedNodeTuples'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('EncryptedSessionZmk') is not None:
            self.encrypted_session_zmk = m.get('EncryptedSessionZmk')
        return self


class GetKpmEncryptedNodeTuplesByOrderIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetKpmEncryptedNodeTuplesByOrderIdResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = GetKpmEncryptedNodeTuplesByOrderIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitKpmEncryptedNodeTupleOrderRequest(TeaModel):
    def __init__(
        self,
        api_product: str = None,
        api_revision: str = None,
        lora_version: str = None,
        required_count: int = None,
    ):
        self.api_product = api_product
        self.api_revision = api_revision
        self.lora_version = lora_version
        self.required_count = required_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.api_product is not None:
            result['ApiProduct'] = self.api_product
        if self.api_revision is not None:
            result['ApiRevision'] = self.api_revision
        if self.lora_version is not None:
            result['LoraVersion'] = self.lora_version
        if self.required_count is not None:
            result['RequiredCount'] = self.required_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiProduct') is not None:
            self.api_product = m.get('ApiProduct')
        if m.get('ApiRevision') is not None:
            self.api_revision = m.get('ApiRevision')
        if m.get('LoraVersion') is not None:
            self.lora_version = m.get('LoraVersion')
        if m.get('RequiredCount') is not None:
            self.required_count = m.get('RequiredCount')
        return self


class SubmitKpmEncryptedNodeTupleOrderResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        message: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        order_id: int = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.message = message
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.order_id = order_id
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SubmitKpmEncryptedNodeTupleOrderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SubmitKpmEncryptedNodeTupleOrderResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = SubmitKpmEncryptedNodeTupleOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


