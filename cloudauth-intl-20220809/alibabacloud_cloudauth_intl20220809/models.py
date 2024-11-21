# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict


class CardOcrRequest(TeaModel):
    def __init__(
        self,
        doc_type: str = None,
        id_face_quality: str = None,
        id_ocr_picture_base_64: str = None,
        id_ocr_picture_url: str = None,
        merchant_biz_id: str = None,
        merchant_user_id: str = None,
        ocr: str = None,
        product_code: str = None,
        spoof: str = None,
    ):
        self.doc_type = doc_type
        self.id_face_quality = id_face_quality
        self.id_ocr_picture_base_64 = id_ocr_picture_base_64
        self.id_ocr_picture_url = id_ocr_picture_url
        self.merchant_biz_id = merchant_biz_id
        self.merchant_user_id = merchant_user_id
        self.ocr = ocr
        self.product_code = product_code
        self.spoof = spoof

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.doc_type is not None:
            result['DocType'] = self.doc_type
        if self.id_face_quality is not None:
            result['IdFaceQuality'] = self.id_face_quality
        if self.id_ocr_picture_base_64 is not None:
            result['IdOcrPictureBase64'] = self.id_ocr_picture_base_64
        if self.id_ocr_picture_url is not None:
            result['IdOcrPictureUrl'] = self.id_ocr_picture_url
        if self.merchant_biz_id is not None:
            result['MerchantBizId'] = self.merchant_biz_id
        if self.merchant_user_id is not None:
            result['MerchantUserId'] = self.merchant_user_id
        if self.ocr is not None:
            result['Ocr'] = self.ocr
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.spoof is not None:
            result['Spoof'] = self.spoof
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DocType') is not None:
            self.doc_type = m.get('DocType')
        if m.get('IdFaceQuality') is not None:
            self.id_face_quality = m.get('IdFaceQuality')
        if m.get('IdOcrPictureBase64') is not None:
            self.id_ocr_picture_base_64 = m.get('IdOcrPictureBase64')
        if m.get('IdOcrPictureUrl') is not None:
            self.id_ocr_picture_url = m.get('IdOcrPictureUrl')
        if m.get('MerchantBizId') is not None:
            self.merchant_biz_id = m.get('MerchantBizId')
        if m.get('MerchantUserId') is not None:
            self.merchant_user_id = m.get('MerchantUserId')
        if m.get('Ocr') is not None:
            self.ocr = m.get('Ocr')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('Spoof') is not None:
            self.spoof = m.get('Spoof')
        return self


class CardOcrResponseBodyResult(TeaModel):
    def __init__(
        self,
        ext_card_info: str = None,
        ext_id_info: str = None,
        passed: str = None,
        sub_code: str = None,
        transaction_id: str = None,
    ):
        self.ext_card_info = ext_card_info
        self.ext_id_info = ext_id_info
        self.passed = passed
        self.sub_code = sub_code
        self.transaction_id = transaction_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ext_card_info is not None:
            result['ExtCardInfo'] = self.ext_card_info
        if self.ext_id_info is not None:
            result['ExtIdInfo'] = self.ext_id_info
        if self.passed is not None:
            result['Passed'] = self.passed
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        if self.transaction_id is not None:
            result['TransactionId'] = self.transaction_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExtCardInfo') is not None:
            self.ext_card_info = m.get('ExtCardInfo')
        if m.get('ExtIdInfo') is not None:
            self.ext_id_info = m.get('ExtIdInfo')
        if m.get('Passed') is not None:
            self.passed = m.get('Passed')
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        if m.get('TransactionId') is not None:
            self.transaction_id = m.get('TransactionId')
        return self


class CardOcrResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: CardOcrResponseBodyResult = None,
    ):
        self.code = code
        self.message = message
        # Id of the request
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
            temp_model = CardOcrResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class CardOcrResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CardOcrResponseBody = None,
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
            temp_model = CardOcrResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


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
        ext_info: str = None,
        ext_risk_info: str = None,
        passed: str = None,
        sub_code: str = None,
    ):
        self.ekyc_result = ekyc_result
        self.ext_basic_info = ext_basic_info
        self.ext_face_info = ext_face_info
        self.ext_id_info = ext_id_info
        self.ext_info = ext_info
        self.ext_risk_info = ext_risk_info
        self.passed = passed
        self.sub_code = sub_code

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
        if self.ext_info is not None:
            result['ExtInfo'] = self.ext_info
        if self.ext_risk_info is not None:
            result['ExtRiskInfo'] = self.ext_risk_info
        if self.passed is not None:
            result['Passed'] = self.passed
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
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
        if m.get('ExtInfo') is not None:
            self.ext_info = m.get('ExtInfo')
        if m.get('ExtRiskInfo') is not None:
            self.ext_risk_info = m.get('ExtRiskInfo')
        if m.get('Passed') is not None:
            self.passed = m.get('Passed')
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
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
        # Id of the request
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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


class DeleteVerifyResultRequest(TeaModel):
    def __init__(
        self,
        delete_after_query: str = None,
        delete_type: str = None,
        transaction_id: str = None,
    ):
        self.delete_after_query = delete_after_query
        self.delete_type = delete_type
        self.transaction_id = transaction_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delete_after_query is not None:
            result['DeleteAfterQuery'] = self.delete_after_query
        if self.delete_type is not None:
            result['DeleteType'] = self.delete_type
        if self.transaction_id is not None:
            result['TransactionId'] = self.transaction_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeleteAfterQuery') is not None:
            self.delete_after_query = m.get('DeleteAfterQuery')
        if m.get('DeleteType') is not None:
            self.delete_type = m.get('DeleteType')
        if m.get('TransactionId') is not None:
            self.transaction_id = m.get('TransactionId')
        return self


class DeleteVerifyResultResponseBodyResult(TeaModel):
    def __init__(
        self,
        delete_result: str = None,
        transaction_id: str = None,
    ):
        self.delete_result = delete_result
        self.transaction_id = transaction_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delete_result is not None:
            result['DeleteResult'] = self.delete_result
        if self.transaction_id is not None:
            result['TransactionId'] = self.transaction_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeleteResult') is not None:
            self.delete_result = m.get('DeleteResult')
        if m.get('TransactionId') is not None:
            self.transaction_id = m.get('TransactionId')
        return self


class DeleteVerifyResultResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: DeleteVerifyResultResponseBodyResult = None,
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
            temp_model = DeleteVerifyResultResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class DeleteVerifyResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteVerifyResultResponseBody = None,
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
            temp_model = DeleteVerifyResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DocOcrRequest(TeaModel):
    def __init__(
        self,
        doc_type: str = None,
        id_face_quality: str = None,
        id_ocr_picture_base_64: str = None,
        id_ocr_picture_url: str = None,
        id_threshold: str = None,
        merchant_biz_id: str = None,
        merchant_user_id: str = None,
        ocr: str = None,
        product_code: str = None,
        spoof: str = None,
    ):
        self.doc_type = doc_type
        self.id_face_quality = id_face_quality
        self.id_ocr_picture_base_64 = id_ocr_picture_base_64
        self.id_ocr_picture_url = id_ocr_picture_url
        self.id_threshold = id_threshold
        self.merchant_biz_id = merchant_biz_id
        self.merchant_user_id = merchant_user_id
        self.ocr = ocr
        self.product_code = product_code
        self.spoof = spoof

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.doc_type is not None:
            result['DocType'] = self.doc_type
        if self.id_face_quality is not None:
            result['IdFaceQuality'] = self.id_face_quality
        if self.id_ocr_picture_base_64 is not None:
            result['IdOcrPictureBase64'] = self.id_ocr_picture_base_64
        if self.id_ocr_picture_url is not None:
            result['IdOcrPictureUrl'] = self.id_ocr_picture_url
        if self.id_threshold is not None:
            result['IdThreshold'] = self.id_threshold
        if self.merchant_biz_id is not None:
            result['MerchantBizId'] = self.merchant_biz_id
        if self.merchant_user_id is not None:
            result['MerchantUserId'] = self.merchant_user_id
        if self.ocr is not None:
            result['Ocr'] = self.ocr
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.spoof is not None:
            result['Spoof'] = self.spoof
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DocType') is not None:
            self.doc_type = m.get('DocType')
        if m.get('IdFaceQuality') is not None:
            self.id_face_quality = m.get('IdFaceQuality')
        if m.get('IdOcrPictureBase64') is not None:
            self.id_ocr_picture_base_64 = m.get('IdOcrPictureBase64')
        if m.get('IdOcrPictureUrl') is not None:
            self.id_ocr_picture_url = m.get('IdOcrPictureUrl')
        if m.get('IdThreshold') is not None:
            self.id_threshold = m.get('IdThreshold')
        if m.get('MerchantBizId') is not None:
            self.merchant_biz_id = m.get('MerchantBizId')
        if m.get('MerchantUserId') is not None:
            self.merchant_user_id = m.get('MerchantUserId')
        if m.get('Ocr') is not None:
            self.ocr = m.get('Ocr')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('Spoof') is not None:
            self.spoof = m.get('Spoof')
        return self


class DocOcrResponseBodyResult(TeaModel):
    def __init__(
        self,
        ext_id_info: str = None,
        passed: str = None,
        sub_code: str = None,
        transaction_id: str = None,
    ):
        self.ext_id_info = ext_id_info
        self.passed = passed
        self.sub_code = sub_code
        self.transaction_id = transaction_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ext_id_info is not None:
            result['ExtIdInfo'] = self.ext_id_info
        if self.passed is not None:
            result['Passed'] = self.passed
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        if self.transaction_id is not None:
            result['TransactionId'] = self.transaction_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExtIdInfo') is not None:
            self.ext_id_info = m.get('ExtIdInfo')
        if m.get('Passed') is not None:
            self.passed = m.get('Passed')
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        if m.get('TransactionId') is not None:
            self.transaction_id = m.get('TransactionId')
        return self


class DocOcrResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: DocOcrResponseBodyResult = None,
    ):
        self.code = code
        self.message = message
        # Id of the request
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
            temp_model = DocOcrResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class DocOcrResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DocOcrResponseBody = None,
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
            temp_model = DocOcrResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EkycVerifyRequest(TeaModel):
    def __init__(
        self,
        authorize: str = None,
        crop: str = None,
        doc_name: str = None,
        doc_no: str = None,
        doc_type: str = None,
        face_picture_base_64: str = None,
        face_picture_url: str = None,
        id_ocr_picture_base_64: str = None,
        id_ocr_picture_url: str = None,
        id_threshold: str = None,
        merchant_biz_id: str = None,
        merchant_user_id: str = None,
        product_code: str = None,
    ):
        self.authorize = authorize
        self.crop = crop
        self.doc_name = doc_name
        self.doc_no = doc_no
        self.doc_type = doc_type
        self.face_picture_base_64 = face_picture_base_64
        self.face_picture_url = face_picture_url
        self.id_ocr_picture_base_64 = id_ocr_picture_base_64
        self.id_ocr_picture_url = id_ocr_picture_url
        self.id_threshold = id_threshold
        self.merchant_biz_id = merchant_biz_id
        self.merchant_user_id = merchant_user_id
        self.product_code = product_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorize is not None:
            result['Authorize'] = self.authorize
        if self.crop is not None:
            result['Crop'] = self.crop
        if self.doc_name is not None:
            result['DocName'] = self.doc_name
        if self.doc_no is not None:
            result['DocNo'] = self.doc_no
        if self.doc_type is not None:
            result['DocType'] = self.doc_type
        if self.face_picture_base_64 is not None:
            result['FacePictureBase64'] = self.face_picture_base_64
        if self.face_picture_url is not None:
            result['FacePictureUrl'] = self.face_picture_url
        if self.id_ocr_picture_base_64 is not None:
            result['IdOcrPictureBase64'] = self.id_ocr_picture_base_64
        if self.id_ocr_picture_url is not None:
            result['IdOcrPictureUrl'] = self.id_ocr_picture_url
        if self.id_threshold is not None:
            result['IdThreshold'] = self.id_threshold
        if self.merchant_biz_id is not None:
            result['MerchantBizId'] = self.merchant_biz_id
        if self.merchant_user_id is not None:
            result['MerchantUserId'] = self.merchant_user_id
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Authorize') is not None:
            self.authorize = m.get('Authorize')
        if m.get('Crop') is not None:
            self.crop = m.get('Crop')
        if m.get('DocName') is not None:
            self.doc_name = m.get('DocName')
        if m.get('DocNo') is not None:
            self.doc_no = m.get('DocNo')
        if m.get('DocType') is not None:
            self.doc_type = m.get('DocType')
        if m.get('FacePictureBase64') is not None:
            self.face_picture_base_64 = m.get('FacePictureBase64')
        if m.get('FacePictureUrl') is not None:
            self.face_picture_url = m.get('FacePictureUrl')
        if m.get('IdOcrPictureBase64') is not None:
            self.id_ocr_picture_base_64 = m.get('IdOcrPictureBase64')
        if m.get('IdOcrPictureUrl') is not None:
            self.id_ocr_picture_url = m.get('IdOcrPictureUrl')
        if m.get('IdThreshold') is not None:
            self.id_threshold = m.get('IdThreshold')
        if m.get('MerchantBizId') is not None:
            self.merchant_biz_id = m.get('MerchantBizId')
        if m.get('MerchantUserId') is not None:
            self.merchant_user_id = m.get('MerchantUserId')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        return self


class EkycVerifyResponseBodyResult(TeaModel):
    def __init__(
        self,
        ext_face_info: str = None,
        ext_id_info: str = None,
        passed: str = None,
        sub_code: str = None,
        transaction_id: str = None,
    ):
        self.ext_face_info = ext_face_info
        self.ext_id_info = ext_id_info
        self.passed = passed
        self.sub_code = sub_code
        self.transaction_id = transaction_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ext_face_info is not None:
            result['ExtFaceInfo'] = self.ext_face_info
        if self.ext_id_info is not None:
            result['ExtIdInfo'] = self.ext_id_info
        if self.passed is not None:
            result['Passed'] = self.passed
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        if self.transaction_id is not None:
            result['TransactionId'] = self.transaction_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExtFaceInfo') is not None:
            self.ext_face_info = m.get('ExtFaceInfo')
        if m.get('ExtIdInfo') is not None:
            self.ext_id_info = m.get('ExtIdInfo')
        if m.get('Passed') is not None:
            self.passed = m.get('Passed')
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        if m.get('TransactionId') is not None:
            self.transaction_id = m.get('TransactionId')
        return self


class EkycVerifyResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: EkycVerifyResponseBodyResult = None,
    ):
        self.code = code
        self.message = message
        # Id of the request
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
            temp_model = EkycVerifyResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class EkycVerifyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EkycVerifyResponseBody = None,
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
            temp_model = EkycVerifyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FaceCompareRequest(TeaModel):
    def __init__(
        self,
        merchant_biz_id: str = None,
        source_face_picture: str = None,
        source_face_picture_url: str = None,
        target_face_picture: str = None,
        target_face_picture_url: str = None,
    ):
        self.merchant_biz_id = merchant_biz_id
        self.source_face_picture = source_face_picture
        self.source_face_picture_url = source_face_picture_url
        self.target_face_picture = target_face_picture
        self.target_face_picture_url = target_face_picture_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.merchant_biz_id is not None:
            result['MerchantBizId'] = self.merchant_biz_id
        if self.source_face_picture is not None:
            result['SourceFacePicture'] = self.source_face_picture
        if self.source_face_picture_url is not None:
            result['SourceFacePictureUrl'] = self.source_face_picture_url
        if self.target_face_picture is not None:
            result['TargetFacePicture'] = self.target_face_picture
        if self.target_face_picture_url is not None:
            result['TargetFacePictureUrl'] = self.target_face_picture_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MerchantBizId') is not None:
            self.merchant_biz_id = m.get('MerchantBizId')
        if m.get('SourceFacePicture') is not None:
            self.source_face_picture = m.get('SourceFacePicture')
        if m.get('SourceFacePictureUrl') is not None:
            self.source_face_picture_url = m.get('SourceFacePictureUrl')
        if m.get('TargetFacePicture') is not None:
            self.target_face_picture = m.get('TargetFacePicture')
        if m.get('TargetFacePictureUrl') is not None:
            self.target_face_picture_url = m.get('TargetFacePictureUrl')
        return self


class FaceCompareResponseBodyResult(TeaModel):
    def __init__(
        self,
        face_comparison_score: float = None,
        passed: str = None,
        transaction_id: str = None,
    ):
        self.face_comparison_score = face_comparison_score
        self.passed = passed
        self.transaction_id = transaction_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.face_comparison_score is not None:
            result['FaceComparisonScore'] = self.face_comparison_score
        if self.passed is not None:
            result['Passed'] = self.passed
        if self.transaction_id is not None:
            result['TransactionId'] = self.transaction_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FaceComparisonScore') is not None:
            self.face_comparison_score = m.get('FaceComparisonScore')
        if m.get('Passed') is not None:
            self.passed = m.get('Passed')
        if m.get('TransactionId') is not None:
            self.transaction_id = m.get('TransactionId')
        return self


class FaceCompareResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: FaceCompareResponseBodyResult = None,
    ):
        self.code = code
        self.message = message
        # Id of the request
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
            temp_model = FaceCompareResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class FaceCompareResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: FaceCompareResponseBody = None,
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
            temp_model = FaceCompareResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FaceGuardRiskRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        device_token: str = None,
        merchant_biz_id: str = None,
        product_code: str = None,
    ):
        self.biz_id = biz_id
        self.device_token = device_token
        self.merchant_biz_id = merchant_biz_id
        self.product_code = product_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.device_token is not None:
            result['DeviceToken'] = self.device_token
        if self.merchant_biz_id is not None:
            result['MerchantBizId'] = self.merchant_biz_id
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('DeviceToken') is not None:
            self.device_token = m.get('DeviceToken')
        if m.get('MerchantBizId') is not None:
            self.merchant_biz_id = m.get('MerchantBizId')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        return self


class FaceGuardRiskResponseBodyResult(TeaModel):
    def __init__(
        self,
        risk_extends: str = None,
        risk_tags: str = None,
        transaction_id: str = None,
    ):
        self.risk_extends = risk_extends
        self.risk_tags = risk_tags
        self.transaction_id = transaction_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.risk_extends is not None:
            result['RiskExtends'] = self.risk_extends
        if self.risk_tags is not None:
            result['RiskTags'] = self.risk_tags
        if self.transaction_id is not None:
            result['TransactionId'] = self.transaction_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RiskExtends') is not None:
            self.risk_extends = m.get('RiskExtends')
        if m.get('RiskTags') is not None:
            self.risk_tags = m.get('RiskTags')
        if m.get('TransactionId') is not None:
            self.transaction_id = m.get('TransactionId')
        return self


class FaceGuardRiskResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: FaceGuardRiskResponseBodyResult = None,
    ):
        self.code = code
        self.message = message
        # Id of the request
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
            temp_model = FaceGuardRiskResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class FaceGuardRiskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: FaceGuardRiskResponseBody = None,
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
            temp_model = FaceGuardRiskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FaceLivenessRequest(TeaModel):
    def __init__(
        self,
        crop: str = None,
        face_picture_base_64: str = None,
        face_picture_url: str = None,
        face_quality: str = None,
        merchant_biz_id: str = None,
        merchant_user_id: str = None,
        occlusion: str = None,
        product_code: str = None,
    ):
        self.crop = crop
        self.face_picture_base_64 = face_picture_base_64
        self.face_picture_url = face_picture_url
        self.face_quality = face_quality
        self.merchant_biz_id = merchant_biz_id
        self.merchant_user_id = merchant_user_id
        self.occlusion = occlusion
        self.product_code = product_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.crop is not None:
            result['Crop'] = self.crop
        if self.face_picture_base_64 is not None:
            result['FacePictureBase64'] = self.face_picture_base_64
        if self.face_picture_url is not None:
            result['FacePictureUrl'] = self.face_picture_url
        if self.face_quality is not None:
            result['FaceQuality'] = self.face_quality
        if self.merchant_biz_id is not None:
            result['MerchantBizId'] = self.merchant_biz_id
        if self.merchant_user_id is not None:
            result['MerchantUserId'] = self.merchant_user_id
        if self.occlusion is not None:
            result['Occlusion'] = self.occlusion
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Crop') is not None:
            self.crop = m.get('Crop')
        if m.get('FacePictureBase64') is not None:
            self.face_picture_base_64 = m.get('FacePictureBase64')
        if m.get('FacePictureUrl') is not None:
            self.face_picture_url = m.get('FacePictureUrl')
        if m.get('FaceQuality') is not None:
            self.face_quality = m.get('FaceQuality')
        if m.get('MerchantBizId') is not None:
            self.merchant_biz_id = m.get('MerchantBizId')
        if m.get('MerchantUserId') is not None:
            self.merchant_user_id = m.get('MerchantUserId')
        if m.get('Occlusion') is not None:
            self.occlusion = m.get('Occlusion')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        return self


class FaceLivenessResponseBodyResultExtFaceInfo(TeaModel):
    def __init__(
        self,
        face_age: int = None,
        face_attack: str = None,
        face_gender: str = None,
        face_quality_score: float = None,
        occlusion_result: str = None,
    ):
        self.face_age = face_age
        self.face_attack = face_attack
        self.face_gender = face_gender
        self.face_quality_score = face_quality_score
        self.occlusion_result = occlusion_result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.face_age is not None:
            result['FaceAge'] = self.face_age
        if self.face_attack is not None:
            result['FaceAttack'] = self.face_attack
        if self.face_gender is not None:
            result['FaceGender'] = self.face_gender
        if self.face_quality_score is not None:
            result['FaceQualityScore'] = self.face_quality_score
        if self.occlusion_result is not None:
            result['OcclusionResult'] = self.occlusion_result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FaceAge') is not None:
            self.face_age = m.get('FaceAge')
        if m.get('FaceAttack') is not None:
            self.face_attack = m.get('FaceAttack')
        if m.get('FaceGender') is not None:
            self.face_gender = m.get('FaceGender')
        if m.get('FaceQualityScore') is not None:
            self.face_quality_score = m.get('FaceQualityScore')
        if m.get('OcclusionResult') is not None:
            self.occlusion_result = m.get('OcclusionResult')
        return self


class FaceLivenessResponseBodyResult(TeaModel):
    def __init__(
        self,
        ext_face_info: FaceLivenessResponseBodyResultExtFaceInfo = None,
        passed: str = None,
        sub_code: str = None,
        transaction_id: str = None,
    ):
        self.ext_face_info = ext_face_info
        self.passed = passed
        self.sub_code = sub_code
        self.transaction_id = transaction_id

    def validate(self):
        if self.ext_face_info:
            self.ext_face_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ext_face_info is not None:
            result['ExtFaceInfo'] = self.ext_face_info.to_map()
        if self.passed is not None:
            result['Passed'] = self.passed
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        if self.transaction_id is not None:
            result['TransactionId'] = self.transaction_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExtFaceInfo') is not None:
            temp_model = FaceLivenessResponseBodyResultExtFaceInfo()
            self.ext_face_info = temp_model.from_map(m['ExtFaceInfo'])
        if m.get('Passed') is not None:
            self.passed = m.get('Passed')
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        if m.get('TransactionId') is not None:
            self.transaction_id = m.get('TransactionId')
        return self


class FaceLivenessResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: FaceLivenessResponseBodyResult = None,
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
            temp_model = FaceLivenessResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class FaceLivenessResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: FaceLivenessResponseBody = None,
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
            temp_model = FaceLivenessResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FraudResultCallBackRequest(TeaModel):
    def __init__(
        self,
        certify_id: str = None,
        ext_params: str = None,
        result_code: str = None,
        verify_deploy_env: str = None,
    ):
        self.certify_id = certify_id
        self.ext_params = ext_params
        self.result_code = result_code
        self.verify_deploy_env = verify_deploy_env

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certify_id is not None:
            result['CertifyId'] = self.certify_id
        if self.ext_params is not None:
            result['ExtParams'] = self.ext_params
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.verify_deploy_env is not None:
            result['VerifyDeployEnv'] = self.verify_deploy_env
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertifyId') is not None:
            self.certify_id = m.get('CertifyId')
        if m.get('ExtParams') is not None:
            self.ext_params = m.get('ExtParams')
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('VerifyDeployEnv') is not None:
            self.verify_deploy_env = m.get('VerifyDeployEnv')
        return self


class FraudResultCallBackResponseBody(TeaModel):
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


class FraudResultCallBackResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: FraudResultCallBackResponseBody = None,
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
            temp_model = FraudResultCallBackResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class Id2MetaVerifyIntlRequest(TeaModel):
    def __init__(
        self,
        identify_num: str = None,
        param_type: str = None,
        product_code: str = None,
        user_name: str = None,
    ):
        self.identify_num = identify_num
        self.param_type = param_type
        self.product_code = product_code
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.identify_num is not None:
            result['IdentifyNum'] = self.identify_num
        if self.param_type is not None:
            result['ParamType'] = self.param_type
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IdentifyNum') is not None:
            self.identify_num = m.get('IdentifyNum')
        if m.get('ParamType') is not None:
            self.param_type = m.get('ParamType')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class Id2MetaVerifyIntlResponseBodyResult(TeaModel):
    def __init__(
        self,
        biz_code: str = None,
    ):
        self.biz_code = biz_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_code is not None:
            result['BizCode'] = self.biz_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')
        return self


class Id2MetaVerifyIntlResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: Id2MetaVerifyIntlResponseBodyResult = None,
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
            temp_model = Id2MetaVerifyIntlResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class Id2MetaVerifyIntlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: Id2MetaVerifyIntlResponseBody = None,
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
            temp_model = Id2MetaVerifyIntlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InitializeRequest(TeaModel):
    def __init__(
        self,
        authorize: str = None,
        callback_token: str = None,
        callback_url: str = None,
        crop: str = None,
        doc_scan_mode: str = None,
        doc_type: str = None,
        doc_video: str = None,
        experience_code: str = None,
        face_picture_base_64: str = None,
        face_picture_url: str = None,
        id_face_quality: str = None,
        id_spoof: str = None,
        id_threshold: str = None,
        language_config: str = None,
        merchant_biz_id: str = None,
        merchant_user_id: str = None,
        meta_info: str = None,
        model: str = None,
        ocr: str = None,
        procedure_priority: str = None,
        product_code: str = None,
        product_flow: str = None,
        return_url: str = None,
        scene_code: str = None,
        security_level: str = None,
        show_album_icon: str = None,
        show_guide_page: str = None,
        show_ocr_result: str = None,
        style_config: str = None,
    ):
        self.authorize = authorize
        self.callback_token = callback_token
        self.callback_url = callback_url
        self.crop = crop
        self.doc_scan_mode = doc_scan_mode
        self.doc_type = doc_type
        self.doc_video = doc_video
        self.experience_code = experience_code
        self.face_picture_base_64 = face_picture_base_64
        self.face_picture_url = face_picture_url
        self.id_face_quality = id_face_quality
        self.id_spoof = id_spoof
        self.id_threshold = id_threshold
        self.language_config = language_config
        self.merchant_biz_id = merchant_biz_id
        self.merchant_user_id = merchant_user_id
        self.meta_info = meta_info
        self.model = model
        # OCR。
        self.ocr = ocr
        self.procedure_priority = procedure_priority
        self.product_code = product_code
        self.product_flow = product_flow
        self.return_url = return_url
        self.scene_code = scene_code
        self.security_level = security_level
        self.show_album_icon = show_album_icon
        self.show_guide_page = show_guide_page
        self.show_ocr_result = show_ocr_result
        self.style_config = style_config

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorize is not None:
            result['Authorize'] = self.authorize
        if self.callback_token is not None:
            result['CallbackToken'] = self.callback_token
        if self.callback_url is not None:
            result['CallbackUrl'] = self.callback_url
        if self.crop is not None:
            result['Crop'] = self.crop
        if self.doc_scan_mode is not None:
            result['DocScanMode'] = self.doc_scan_mode
        if self.doc_type is not None:
            result['DocType'] = self.doc_type
        if self.doc_video is not None:
            result['DocVideo'] = self.doc_video
        if self.experience_code is not None:
            result['ExperienceCode'] = self.experience_code
        if self.face_picture_base_64 is not None:
            result['FacePictureBase64'] = self.face_picture_base_64
        if self.face_picture_url is not None:
            result['FacePictureUrl'] = self.face_picture_url
        if self.id_face_quality is not None:
            result['IdFaceQuality'] = self.id_face_quality
        if self.id_spoof is not None:
            result['IdSpoof'] = self.id_spoof
        if self.id_threshold is not None:
            result['IdThreshold'] = self.id_threshold
        if self.language_config is not None:
            result['LanguageConfig'] = self.language_config
        if self.merchant_biz_id is not None:
            result['MerchantBizId'] = self.merchant_biz_id
        if self.merchant_user_id is not None:
            result['MerchantUserId'] = self.merchant_user_id
        if self.meta_info is not None:
            result['MetaInfo'] = self.meta_info
        if self.model is not None:
            result['Model'] = self.model
        if self.ocr is not None:
            result['Ocr'] = self.ocr
        if self.procedure_priority is not None:
            result['ProcedurePriority'] = self.procedure_priority
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.product_flow is not None:
            result['ProductFlow'] = self.product_flow
        if self.return_url is not None:
            result['ReturnUrl'] = self.return_url
        if self.scene_code is not None:
            result['SceneCode'] = self.scene_code
        if self.security_level is not None:
            result['SecurityLevel'] = self.security_level
        if self.show_album_icon is not None:
            result['ShowAlbumIcon'] = self.show_album_icon
        if self.show_guide_page is not None:
            result['ShowGuidePage'] = self.show_guide_page
        if self.show_ocr_result is not None:
            result['ShowOcrResult'] = self.show_ocr_result
        if self.style_config is not None:
            result['StyleConfig'] = self.style_config
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Authorize') is not None:
            self.authorize = m.get('Authorize')
        if m.get('CallbackToken') is not None:
            self.callback_token = m.get('CallbackToken')
        if m.get('CallbackUrl') is not None:
            self.callback_url = m.get('CallbackUrl')
        if m.get('Crop') is not None:
            self.crop = m.get('Crop')
        if m.get('DocScanMode') is not None:
            self.doc_scan_mode = m.get('DocScanMode')
        if m.get('DocType') is not None:
            self.doc_type = m.get('DocType')
        if m.get('DocVideo') is not None:
            self.doc_video = m.get('DocVideo')
        if m.get('ExperienceCode') is not None:
            self.experience_code = m.get('ExperienceCode')
        if m.get('FacePictureBase64') is not None:
            self.face_picture_base_64 = m.get('FacePictureBase64')
        if m.get('FacePictureUrl') is not None:
            self.face_picture_url = m.get('FacePictureUrl')
        if m.get('IdFaceQuality') is not None:
            self.id_face_quality = m.get('IdFaceQuality')
        if m.get('IdSpoof') is not None:
            self.id_spoof = m.get('IdSpoof')
        if m.get('IdThreshold') is not None:
            self.id_threshold = m.get('IdThreshold')
        if m.get('LanguageConfig') is not None:
            self.language_config = m.get('LanguageConfig')
        if m.get('MerchantBizId') is not None:
            self.merchant_biz_id = m.get('MerchantBizId')
        if m.get('MerchantUserId') is not None:
            self.merchant_user_id = m.get('MerchantUserId')
        if m.get('MetaInfo') is not None:
            self.meta_info = m.get('MetaInfo')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('Ocr') is not None:
            self.ocr = m.get('Ocr')
        if m.get('ProcedurePriority') is not None:
            self.procedure_priority = m.get('ProcedurePriority')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProductFlow') is not None:
            self.product_flow = m.get('ProductFlow')
        if m.get('ReturnUrl') is not None:
            self.return_url = m.get('ReturnUrl')
        if m.get('SceneCode') is not None:
            self.scene_code = m.get('SceneCode')
        if m.get('SecurityLevel') is not None:
            self.security_level = m.get('SecurityLevel')
        if m.get('ShowAlbumIcon') is not None:
            self.show_album_icon = m.get('ShowAlbumIcon')
        if m.get('ShowGuidePage') is not None:
            self.show_guide_page = m.get('ShowGuidePage')
        if m.get('ShowOcrResult') is not None:
            self.show_ocr_result = m.get('ShowOcrResult')
        if m.get('StyleConfig') is not None:
            self.style_config = m.get('StyleConfig')
        return self


class InitializeResponseBodyResult(TeaModel):
    def __init__(
        self,
        client_cfg: str = None,
        transaction_id: str = None,
        transaction_url: str = None,
    ):
        self.client_cfg = client_cfg
        self.transaction_id = transaction_id
        self.transaction_url = transaction_url

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
        if self.transaction_url is not None:
            result['TransactionUrl'] = self.transaction_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientCfg') is not None:
            self.client_cfg = m.get('ClientCfg')
        if m.get('TransactionId') is not None:
            self.transaction_id = m.get('TransactionId')
        if m.get('TransactionUrl') is not None:
            self.transaction_url = m.get('TransactionUrl')
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
        # Id of the request
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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


class Mobile3MetaVerifyIntlRequest(TeaModel):
    def __init__(
        self,
        identify_num: str = None,
        mobile: str = None,
        param_type: str = None,
        product_code: str = None,
        user_name: str = None,
    ):
        self.identify_num = identify_num
        self.mobile = mobile
        self.param_type = param_type
        self.product_code = product_code
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.identify_num is not None:
            result['IdentifyNum'] = self.identify_num
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.param_type is not None:
            result['ParamType'] = self.param_type
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IdentifyNum') is not None:
            self.identify_num = m.get('IdentifyNum')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('ParamType') is not None:
            self.param_type = m.get('ParamType')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class Mobile3MetaVerifyIntlResponseBodyResult(TeaModel):
    def __init__(
        self,
        biz_code: str = None,
        isp_name: str = None,
        sub_code: str = None,
    ):
        self.biz_code = biz_code
        self.isp_name = isp_name
        self.sub_code = sub_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_code is not None:
            result['BizCode'] = self.biz_code
        if self.isp_name is not None:
            result['IspName'] = self.isp_name
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')
        if m.get('IspName') is not None:
            self.isp_name = m.get('IspName')
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        return self


class Mobile3MetaVerifyIntlResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: Mobile3MetaVerifyIntlResponseBodyResult = None,
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
            temp_model = Mobile3MetaVerifyIntlResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class Mobile3MetaVerifyIntlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: Mobile3MetaVerifyIntlResponseBody = None,
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
            temp_model = Mobile3MetaVerifyIntlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


