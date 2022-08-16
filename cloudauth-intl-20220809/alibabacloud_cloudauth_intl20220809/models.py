# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict


class CheckResultRequest(TeaModel):
    def __init__(
        self,
        extra_image_control_list: str = None,
        is_return_image: str = None,
        merchant_biz_id: str = None,
        return_five_category_spoof_result: str = None,
        transaction_id: str = None,
    ):
        self.extra_image_control_list = extra_image_control_list
        self.is_return_image = is_return_image
        self.merchant_biz_id = merchant_biz_id
        self.return_five_category_spoof_result = return_five_category_spoof_result
        self.transaction_id = transaction_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extra_image_control_list is not None:
            result['ExtraImageControlList'] = self.extra_image_control_list
        if self.is_return_image is not None:
            result['IsReturnImage'] = self.is_return_image
        if self.merchant_biz_id is not None:
            result['MerchantBizId'] = self.merchant_biz_id
        if self.return_five_category_spoof_result is not None:
            result['ReturnFiveCategorySpoofResult'] = self.return_five_category_spoof_result
        if self.transaction_id is not None:
            result['TransactionId'] = self.transaction_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExtraImageControlList') is not None:
            self.extra_image_control_list = m.get('ExtraImageControlList')
        if m.get('IsReturnImage') is not None:
            self.is_return_image = m.get('IsReturnImage')
        if m.get('MerchantBizId') is not None:
            self.merchant_biz_id = m.get('MerchantBizId')
        if m.get('ReturnFiveCategorySpoofResult') is not None:
            self.return_five_category_spoof_result = m.get('ReturnFiveCategorySpoofResult')
        if m.get('TransactionId') is not None:
            self.transaction_id = m.get('TransactionId')
        return self


class CheckResultResponseBodyResult(TeaModel):
    def __init__(
        self,
        ekyc_result: str = None,
        ext_basic_info: str = None,
        ext_face_info: str = None,
        ext_id_info: str = None,
        ext_risk_info: str = None,
    ):
        self.ekyc_result = ekyc_result
        self.ext_basic_info = ext_basic_info
        self.ext_face_info = ext_face_info
        self.ext_id_info = ext_id_info
        self.ext_risk_info = ext_risk_info

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ekyc_result is not None:
            result['EkycResult'] = self.ekyc_result
        if self.ext_basic_info is not None:
            result['ExtBasicInfo'] = self.ext_basic_info
        if self.ext_face_info is not None:
            result['ExtFaceInfo'] = self.ext_face_info
        if self.ext_id_info is not None:
            result['ExtIdInfo'] = self.ext_id_info
        if self.ext_risk_info is not None:
            result['ExtRiskInfo'] = self.ext_risk_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EkycResult') is not None:
            self.ekyc_result = m.get('EkycResult')
        if m.get('ExtBasicInfo') is not None:
            self.ext_basic_info = m.get('ExtBasicInfo')
        if m.get('ExtFaceInfo') is not None:
            self.ext_face_info = m.get('ExtFaceInfo')
        if m.get('ExtIdInfo') is not None:
            self.ext_id_info = m.get('ExtIdInfo')
        if m.get('ExtRiskInfo') is not None:
            self.ext_risk_info = m.get('ExtRiskInfo')
        return self


class CheckResultResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: CheckResultResponseBodyResult = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result

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
            temp_model = CheckResultResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class CheckResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CheckResultResponseBody = None,
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
            temp_model = CheckResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InitializeRequest(TeaModel):
    def __init__(
        self,
        doc_type: str = None,
        flow_type: str = None,
        merchant_biz_id: str = None,
        merchant_user_id: str = None,
        meta_info: str = None,
        operation_mode: str = None,
        pages: str = None,
        product_code: str = None,
        product_config: str = None,
        scene_code: str = None,
        service_level: str = None,
    ):
        self.doc_type = doc_type
        self.flow_type = flow_type
        self.merchant_biz_id = merchant_biz_id
        self.merchant_user_id = merchant_user_id
        self.meta_info = meta_info
        self.operation_mode = operation_mode
        self.pages = pages
        self.product_code = product_code
        self.product_config = product_config
        self.scene_code = scene_code
        self.service_level = service_level

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.doc_type is not None:
            result['DocType'] = self.doc_type
        if self.flow_type is not None:
            result['FlowType'] = self.flow_type
        if self.merchant_biz_id is not None:
            result['MerchantBizId'] = self.merchant_biz_id
        if self.merchant_user_id is not None:
            result['MerchantUserId'] = self.merchant_user_id
        if self.meta_info is not None:
            result['MetaInfo'] = self.meta_info
        if self.operation_mode is not None:
            result['OperationMode'] = self.operation_mode
        if self.pages is not None:
            result['Pages'] = self.pages
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.product_config is not None:
            result['ProductConfig'] = self.product_config
        if self.scene_code is not None:
            result['SceneCode'] = self.scene_code
        if self.service_level is not None:
            result['ServiceLevel'] = self.service_level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DocType') is not None:
            self.doc_type = m.get('DocType')
        if m.get('FlowType') is not None:
            self.flow_type = m.get('FlowType')
        if m.get('MerchantBizId') is not None:
            self.merchant_biz_id = m.get('MerchantBizId')
        if m.get('MerchantUserId') is not None:
            self.merchant_user_id = m.get('MerchantUserId')
        if m.get('MetaInfo') is not None:
            self.meta_info = m.get('MetaInfo')
        if m.get('OperationMode') is not None:
            self.operation_mode = m.get('OperationMode')
        if m.get('Pages') is not None:
            self.pages = m.get('Pages')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProductConfig') is not None:
            self.product_config = m.get('ProductConfig')
        if m.get('SceneCode') is not None:
            self.scene_code = m.get('SceneCode')
        if m.get('ServiceLevel') is not None:
            self.service_level = m.get('ServiceLevel')
        return self


class InitializeResponseBodyResult(TeaModel):
    def __init__(
        self,
        client_cfg: str = None,
        transaction_id: str = None,
    ):
        self.client_cfg = client_cfg
        self.transaction_id = transaction_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_cfg is not None:
            result['ClientCfg'] = self.client_cfg
        if self.transaction_id is not None:
            result['TransactionId'] = self.transaction_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientCfg') is not None:
            self.client_cfg = m.get('ClientCfg')
        if m.get('TransactionId') is not None:
            self.transaction_id = m.get('TransactionId')
        return self


class InitializeResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: InitializeResponseBodyResult = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result

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
            temp_model = InitializeResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class InitializeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: InitializeResponseBody = None,
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
            temp_model = InitializeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


