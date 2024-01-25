# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


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
        ext_risk_info: str = None,
        passed: str = None,
        sub_code: str = None,
    ):
        self.ekyc_result = ekyc_result
        self.ext_basic_info = ext_basic_info
        self.ext_face_info = ext_face_info
        self.ext_id_info = ext_id_info
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


class DeletePictureRequest(TeaModel):
    def __init__(
        self,
        delete_pic_after_query: str = None,
        transaction_id: str = None,
    ):
        self.delete_pic_after_query = delete_pic_after_query
        self.transaction_id = transaction_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delete_pic_after_query is not None:
            result['DeletePicAfterQuery'] = self.delete_pic_after_query
        if self.transaction_id is not None:
            result['TransactionId'] = self.transaction_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeletePicAfterQuery') is not None:
            self.delete_pic_after_query = m.get('DeletePicAfterQuery')
        if m.get('TransactionId') is not None:
            self.transaction_id = m.get('TransactionId')
        return self


class DeletePictureResponseBodyResult(TeaModel):
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


class DeletePictureResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: DeletePictureResponseBodyResult = None,
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
            temp_model = DeletePictureResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class DeletePictureResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeletePictureResponseBody = None,
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
            temp_model = DeletePictureResponseBody()
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


class DescribeAddressLabelsRequest(TeaModel):
    def __init__(
        self,
        address: str = None,
        coin: str = None,
        merchant_biz_id: str = None,
    ):
        self.address = address
        self.coin = coin
        self.merchant_biz_id = merchant_biz_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.coin is not None:
            result['Coin'] = self.coin
        if self.merchant_biz_id is not None:
            result['MerchantBizId'] = self.merchant_biz_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('Coin') is not None:
            self.coin = m.get('Coin')
        if m.get('MerchantBizId') is not None:
            self.merchant_biz_id = m.get('MerchantBizId')
        return self


class DescribeAddressLabelsResponseBodyData(TeaModel):
    def __init__(
        self,
        label_list: List[str] = None,
    ):
        self.label_list = label_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label_list is not None:
            result['LabelList'] = self.label_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LabelList') is not None:
            self.label_list = m.get('LabelList')
        return self


class DescribeAddressLabelsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: DescribeAddressLabelsResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        # Id of the request
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
            temp_model = DescribeAddressLabelsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeAddressLabelsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAddressLabelsResponseBody = None,
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
            temp_model = DescribeAddressLabelsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAddressOverviewRequest(TeaModel):
    def __init__(
        self,
        address: str = None,
        coin: str = None,
        merchant_biz_id: str = None,
    ):
        self.address = address
        self.coin = coin
        self.merchant_biz_id = merchant_biz_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.coin is not None:
            result['Coin'] = self.coin
        if self.merchant_biz_id is not None:
            result['MerchantBizId'] = self.merchant_biz_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('Coin') is not None:
            self.coin = m.get('Coin')
        if m.get('MerchantBizId') is not None:
            self.merchant_biz_id = m.get('MerchantBizId')
        return self


class DescribeAddressOverviewResponseBodyData(TeaModel):
    def __init__(
        self,
        balance: float = None,
        first_seen: int = None,
        last_seen: int = None,
        received_txs_count: int = None,
        spent_txs_count: int = None,
        total_received: float = None,
        total_spent: float = None,
        txs_count: int = None,
    ):
        self.balance = balance
        self.first_seen = first_seen
        self.last_seen = last_seen
        self.received_txs_count = received_txs_count
        self.spent_txs_count = spent_txs_count
        self.total_received = total_received
        self.total_spent = total_spent
        self.txs_count = txs_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.balance is not None:
            result['Balance'] = self.balance
        if self.first_seen is not None:
            result['FirstSeen'] = self.first_seen
        if self.last_seen is not None:
            result['LastSeen'] = self.last_seen
        if self.received_txs_count is not None:
            result['ReceivedTxsCount'] = self.received_txs_count
        if self.spent_txs_count is not None:
            result['SpentTxsCount'] = self.spent_txs_count
        if self.total_received is not None:
            result['TotalReceived'] = self.total_received
        if self.total_spent is not None:
            result['TotalSpent'] = self.total_spent
        if self.txs_count is not None:
            result['TxsCount'] = self.txs_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Balance') is not None:
            self.balance = m.get('Balance')
        if m.get('FirstSeen') is not None:
            self.first_seen = m.get('FirstSeen')
        if m.get('LastSeen') is not None:
            self.last_seen = m.get('LastSeen')
        if m.get('ReceivedTxsCount') is not None:
            self.received_txs_count = m.get('ReceivedTxsCount')
        if m.get('SpentTxsCount') is not None:
            self.spent_txs_count = m.get('SpentTxsCount')
        if m.get('TotalReceived') is not None:
            self.total_received = m.get('TotalReceived')
        if m.get('TotalSpent') is not None:
            self.total_spent = m.get('TotalSpent')
        if m.get('TxsCount') is not None:
            self.txs_count = m.get('TxsCount')
        return self


class DescribeAddressOverviewResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: DescribeAddressOverviewResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        # Id of the request
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
            temp_model = DescribeAddressOverviewResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeAddressOverviewResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAddressOverviewResponseBody = None,
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
            temp_model = DescribeAddressOverviewResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeMaliciousAddressRequest(TeaModel):
    def __init__(
        self,
        coin: str = None,
        end: str = None,
        merchant_biz_id: str = None,
        start: str = None,
    ):
        self.coin = coin
        self.end = end
        self.merchant_biz_id = merchant_biz_id
        self.start = start

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.coin is not None:
            result['Coin'] = self.coin
        if self.end is not None:
            result['End'] = self.end
        if self.merchant_biz_id is not None:
            result['MerchantBizId'] = self.merchant_biz_id
        if self.start is not None:
            result['Start'] = self.start
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Coin') is not None:
            self.coin = m.get('Coin')
        if m.get('End') is not None:
            self.end = m.get('End')
        if m.get('MerchantBizId') is not None:
            self.merchant_biz_id = m.get('MerchantBizId')
        if m.get('Start') is not None:
            self.start = m.get('Start')
        return self


class DescribeMaliciousAddressResponseBodyData(TeaModel):
    def __init__(
        self,
        add_time: str = None,
        address: str = None,
        coin: str = None,
        detail: str = None,
        tag: str = None,
    ):
        self.add_time = add_time
        self.address = address
        self.coin = coin
        self.detail = detail
        self.tag = tag

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.add_time is not None:
            result['AddTime'] = self.add_time
        if self.address is not None:
            result['Address'] = self.address
        if self.coin is not None:
            result['Coin'] = self.coin
        if self.detail is not None:
            result['Detail'] = self.detail
        if self.tag is not None:
            result['Tag'] = self.tag
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddTime') is not None:
            self.add_time = m.get('AddTime')
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('Coin') is not None:
            self.coin = m.get('Coin')
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        return self


class DescribeMaliciousAddressResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[DescribeMaliciousAddressResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        # Id of the request
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
                temp_model = DescribeMaliciousAddressResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeMaliciousAddressResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeMaliciousAddressResponseBody = None,
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
            temp_model = DescribeMaliciousAddressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRiskScoreRequest(TeaModel):
    def __init__(
        self,
        address: str = None,
        coin: str = None,
        merchant_biz_id: str = None,
    ):
        self.address = address
        self.coin = coin
        self.merchant_biz_id = merchant_biz_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.coin is not None:
            result['Coin'] = self.coin
        if self.merchant_biz_id is not None:
            result['MerchantBizId'] = self.merchant_biz_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('Coin') is not None:
            self.coin = m.get('Coin')
        if m.get('MerchantBizId') is not None:
            self.merchant_biz_id = m.get('MerchantBizId')
        return self


class DescribeRiskScoreResponseBodyData(TeaModel):
    def __init__(
        self,
        detail_list: List[str] = None,
        hacking_event: str = None,
        risk_level: str = None,
        score: int = None,
    ):
        self.detail_list = detail_list
        self.hacking_event = hacking_event
        self.risk_level = risk_level
        self.score = score

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.detail_list is not None:
            result['DetailList'] = self.detail_list
        if self.hacking_event is not None:
            result['HackingEvent'] = self.hacking_event
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        if self.score is not None:
            result['Score'] = self.score
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DetailList') is not None:
            self.detail_list = m.get('DetailList')
        if m.get('HackingEvent') is not None:
            self.hacking_event = m.get('HackingEvent')
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        return self


class DescribeRiskScoreResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: DescribeRiskScoreResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        # Id of the request
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
            temp_model = DescribeRiskScoreResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeRiskScoreResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeRiskScoreResponseBody = None,
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
            temp_model = DescribeRiskScoreResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTransactionsListRequest(TeaModel):
    def __init__(
        self,
        address: str = None,
        coin: str = None,
        end_timestamp: int = None,
        merchant_biz_id: str = None,
        page: int = None,
        start_timestamp: int = None,
        type: str = None,
    ):
        self.address = address
        self.coin = coin
        self.end_timestamp = end_timestamp
        self.merchant_biz_id = merchant_biz_id
        self.page = page
        self.start_timestamp = start_timestamp
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.coin is not None:
            result['Coin'] = self.coin
        if self.end_timestamp is not None:
            result['EndTimestamp'] = self.end_timestamp
        if self.merchant_biz_id is not None:
            result['MerchantBizId'] = self.merchant_biz_id
        if self.page is not None:
            result['Page'] = self.page
        if self.start_timestamp is not None:
            result['StartTimestamp'] = self.start_timestamp
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('Coin') is not None:
            self.coin = m.get('Coin')
        if m.get('EndTimestamp') is not None:
            self.end_timestamp = m.get('EndTimestamp')
        if m.get('MerchantBizId') is not None:
            self.merchant_biz_id = m.get('MerchantBizId')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('StartTimestamp') is not None:
            self.start_timestamp = m.get('StartTimestamp')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeTransactionsListResponseBodyDataIn(TeaModel):
    def __init__(
        self,
        address: str = None,
        amount: float = None,
        label: str = None,
        tx_hash_list: List[str] = None,
        type: int = None,
    ):
        self.address = address
        self.amount = amount
        self.label = label
        self.tx_hash_list = tx_hash_list
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.label is not None:
            result['Label'] = self.label
        if self.tx_hash_list is not None:
            result['TxHashList'] = self.tx_hash_list
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('TxHashList') is not None:
            self.tx_hash_list = m.get('TxHashList')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeTransactionsListResponseBodyDataOut(TeaModel):
    def __init__(
        self,
        address: str = None,
        amount: float = None,
        label: str = None,
        tx_hash_list: List[str] = None,
        type: int = None,
    ):
        self.address = address
        self.amount = amount
        self.label = label
        self.tx_hash_list = tx_hash_list
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.label is not None:
            result['Label'] = self.label
        if self.tx_hash_list is not None:
            result['TxHashList'] = self.tx_hash_list
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('TxHashList') is not None:
            self.tx_hash_list = m.get('TxHashList')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeTransactionsListResponseBodyData(TeaModel):
    def __init__(
        self,
        in_: List[DescribeTransactionsListResponseBodyDataIn] = None,
        out: List[DescribeTransactionsListResponseBodyDataOut] = None,
        page: int = None,
        total_pages: int = None,
        transactions_on_page: int = None,
    ):
        self.in_ = in_
        self.out = out
        self.page = page
        self.total_pages = total_pages
        self.transactions_on_page = transactions_on_page

    def validate(self):
        if self.in_:
            for k in self.in_:
                if k:
                    k.validate()
        if self.out:
            for k in self.out:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['In'] = []
        if self.in_ is not None:
            for k in self.in_:
                result['In'].append(k.to_map() if k else None)
        result['Out'] = []
        if self.out is not None:
            for k in self.out:
                result['Out'].append(k.to_map() if k else None)
        if self.page is not None:
            result['Page'] = self.page
        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages
        if self.transactions_on_page is not None:
            result['TransactionsOnPage'] = self.transactions_on_page
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.in_ = []
        if m.get('In') is not None:
            for k in m.get('In'):
                temp_model = DescribeTransactionsListResponseBodyDataIn()
                self.in_.append(temp_model.from_map(k))
        self.out = []
        if m.get('Out') is not None:
            for k in m.get('Out'):
                temp_model = DescribeTransactionsListResponseBodyDataOut()
                self.out.append(temp_model.from_map(k))
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')
        if m.get('TransactionsOnPage') is not None:
            self.transactions_on_page = m.get('TransactionsOnPage')
        return self


class DescribeTransactionsListResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: DescribeTransactionsListResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        # Id of the request
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
            temp_model = DescribeTransactionsListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeTransactionsListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeTransactionsListResponseBody = None,
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
            temp_model = DescribeTransactionsListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeWeb3AddressLabelsRequest(TeaModel):
    def __init__(
        self,
        address: str = None,
        chain_short_name: str = None,
        merchant_biz_id: str = None,
    ):
        # The address hash.
        self.address = address
        # This is the short name of blockchain。
        # [ ETH, MATIC, BNB ]
        self.chain_short_name = chain_short_name
        # A unique business ID for tracing purpose. For example，the sequence ID from the merchant\"s business-related database.
        self.merchant_biz_id = merchant_biz_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.chain_short_name is not None:
            result['ChainShortName'] = self.chain_short_name
        if self.merchant_biz_id is not None:
            result['MerchantBizId'] = self.merchant_biz_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('ChainShortName') is not None:
            self.chain_short_name = m.get('ChainShortName')
        if m.get('MerchantBizId') is not None:
            self.merchant_biz_id = m.get('MerchantBizId')
        return self


class DescribeWeb3AddressLabelsResponseBodyData(TeaModel):
    def __init__(
        self,
        address: str = None,
        balance: str = None,
        balance_symbol: str = None,
        chain_name: str = None,
        chain_short_name: str = None,
        contract_address: str = None,
        create_contract_address: str = None,
        create_contract_transaction_hash: str = None,
        custom_risk_assessment: str = None,
        first_transaction_time: str = None,
        is_producer_address: str = None,
        last_transaction_time: str = None,
        receive_amount: str = None,
        send_amount: str = None,
        tag: str = None,
        token: str = None,
        token_amount: int = None,
        token_list: str = None,
        transaction_count: int = None,
    ):
        # address
        self.address = address
        # amount of native currency
        self.balance = balance
        # native currency of the chain
        self.balance_symbol = balance_symbol
        # ChainNameEnumstring name of blockchain
        self.chain_name = chain_name
        # ChainShortName
        self.chain_short_name = chain_short_name
        # 0: EOA; 1: Contract
        self.contract_address = contract_address
        # the address of deployer if the current address is a contract, null if the current address is an EOA
        self.create_contract_address = create_contract_address
        # contract creation hash if the current address is a contract, null if the current address is an EOA
        self.create_contract_transaction_hash = create_contract_transaction_hash
        # customized assessment detail
        self.custom_risk_assessment = custom_risk_assessment
        # the first transaction hash sent by the address
        self.first_transaction_time = first_transaction_time
        # 0: Not validator; 1: validator
        self.is_producer_address = is_producer_address
        # the latest transaction hash sent by the address
        self.last_transaction_time = last_transaction_time
        # the amount of native currency received in 180 days
        self.receive_amount = receive_amount
        # the amount of native currency sent in 180 days
        self.send_amount = send_amount
        # tag
        self.tag = tag
        # if the address is an erc20 token, returns the token name
        self.token = token
        # the number of erc20 tokens involved with current address in 180 days
        self.token_amount = token_amount
        # address of erc20 tokens involved with current address in 180 days
        self.token_list = token_list
        # the number of transactions
        self.transaction_count = transaction_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.balance is not None:
            result['Balance'] = self.balance
        if self.balance_symbol is not None:
            result['BalanceSymbol'] = self.balance_symbol
        if self.chain_name is not None:
            result['ChainName'] = self.chain_name
        if self.chain_short_name is not None:
            result['ChainShortName'] = self.chain_short_name
        if self.contract_address is not None:
            result['ContractAddress'] = self.contract_address
        if self.create_contract_address is not None:
            result['CreateContractAddress'] = self.create_contract_address
        if self.create_contract_transaction_hash is not None:
            result['CreateContractTransactionHash'] = self.create_contract_transaction_hash
        if self.custom_risk_assessment is not None:
            result['CustomRiskAssessment'] = self.custom_risk_assessment
        if self.first_transaction_time is not None:
            result['FirstTransactionTime'] = self.first_transaction_time
        if self.is_producer_address is not None:
            result['IsProducerAddress'] = self.is_producer_address
        if self.last_transaction_time is not None:
            result['LastTransactionTime'] = self.last_transaction_time
        if self.receive_amount is not None:
            result['ReceiveAmount'] = self.receive_amount
        if self.send_amount is not None:
            result['SendAmount'] = self.send_amount
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.token is not None:
            result['Token'] = self.token
        if self.token_amount is not None:
            result['TokenAmount'] = self.token_amount
        if self.token_list is not None:
            result['TokenList'] = self.token_list
        if self.transaction_count is not None:
            result['TransactionCount'] = self.transaction_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('Balance') is not None:
            self.balance = m.get('Balance')
        if m.get('BalanceSymbol') is not None:
            self.balance_symbol = m.get('BalanceSymbol')
        if m.get('ChainName') is not None:
            self.chain_name = m.get('ChainName')
        if m.get('ChainShortName') is not None:
            self.chain_short_name = m.get('ChainShortName')
        if m.get('ContractAddress') is not None:
            self.contract_address = m.get('ContractAddress')
        if m.get('CreateContractAddress') is not None:
            self.create_contract_address = m.get('CreateContractAddress')
        if m.get('CreateContractTransactionHash') is not None:
            self.create_contract_transaction_hash = m.get('CreateContractTransactionHash')
        if m.get('CustomRiskAssessment') is not None:
            self.custom_risk_assessment = m.get('CustomRiskAssessment')
        if m.get('FirstTransactionTime') is not None:
            self.first_transaction_time = m.get('FirstTransactionTime')
        if m.get('IsProducerAddress') is not None:
            self.is_producer_address = m.get('IsProducerAddress')
        if m.get('LastTransactionTime') is not None:
            self.last_transaction_time = m.get('LastTransactionTime')
        if m.get('ReceiveAmount') is not None:
            self.receive_amount = m.get('ReceiveAmount')
        if m.get('SendAmount') is not None:
            self.send_amount = m.get('SendAmount')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        if m.get('TokenAmount') is not None:
            self.token_amount = m.get('TokenAmount')
        if m.get('TokenList') is not None:
            self.token_list = m.get('TokenList')
        if m.get('TransactionCount') is not None:
            self.transaction_count = m.get('TransactionCount')
        return self


class DescribeWeb3AddressLabelsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: DescribeWeb3AddressLabelsResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
    ):
        # Return code. For the full list of codes, see Codes and Messages.
        self.code = code
        # data
        self.data = data
        # The HTTP status code
        self.http_status_code = http_status_code
        # Response detailed message.
        self.message = message
        # The unique ID of the request, which can be used to locate issues.
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
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
            temp_model = DescribeWeb3AddressLabelsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeWeb3AddressLabelsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeWeb3AddressLabelsResponseBody = None,
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
            temp_model = DescribeWeb3AddressLabelsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeWeb3RiskScoreRequest(TeaModel):
    def __init__(
        self,
        chain_short_name: str = None,
        depth: int = None,
        merchant_biz_id: str = None,
        object_id: str = None,
        object_type: str = None,
    ):
        # This is the short name of blockchain。
        # [ ETH, MATIC, BNB ]
        self.chain_short_name = chain_short_name
        # minimum: 1
        # maximum: 100
        # the maximum depth for risk analysis. For UTXO-based blockchains, default and maximum is enforced at 100.
        # For account-based blockchains, default and maximum is enforced at 6
        self.depth = depth
        # A unique business ID for tracing purpose. For example，the sequence ID from the merchant\"s business-related database.
        self.merchant_biz_id = merchant_biz_id
        # For TRANSACTION objects, you need to provide the transaction hash。
        # For ADDRESS objects, you need to provide the address or reference address hash。
        self.object_id = object_id
        # The object of the analysis.
        # [ TRANSACTION, ADDRESS ]
        self.object_type = object_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.chain_short_name is not None:
            result['ChainShortName'] = self.chain_short_name
        if self.depth is not None:
            result['Depth'] = self.depth
        if self.merchant_biz_id is not None:
            result['MerchantBizId'] = self.merchant_biz_id
        if self.object_id is not None:
            result['ObjectId'] = self.object_id
        if self.object_type is not None:
            result['ObjectType'] = self.object_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChainShortName') is not None:
            self.chain_short_name = m.get('ChainShortName')
        if m.get('Depth') is not None:
            self.depth = m.get('Depth')
        if m.get('MerchantBizId') is not None:
            self.merchant_biz_id = m.get('MerchantBizId')
        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')
        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')
        return self


class DescribeWeb3RiskScoreResponseBodyDataRiskResults(TeaModel):
    def __init__(
        self,
        description: str = None,
        severity: str = None,
        type: str = None,
    ):
        # description
        self.description = description
        # [ CRITICAL, HIGH, MEDIUM, LOW, NO ]
        # 100: Critical
        # 67-99: High risk
        # 34-66: Medium risk
        # 1-33: Low risk
        # 0: No risk
        self.severity = severity
        # Address
        # Transaction
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.severity is not None:
            result['Severity'] = self.severity
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Severity') is not None:
            self.severity = m.get('Severity')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeWeb3RiskScoreResponseBodyData(TeaModel):
    def __init__(
        self,
        risk_results: List[DescribeWeb3RiskScoreResponseBodyDataRiskResults] = None,
        score: str = None,
    ):
        # risk results
        self.risk_results = risk_results
        # Risk score
        self.score = score

    def validate(self):
        if self.risk_results:
            for k in self.risk_results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RiskResults'] = []
        if self.risk_results is not None:
            for k in self.risk_results:
                result['RiskResults'].append(k.to_map() if k else None)
        if self.score is not None:
            result['Score'] = self.score
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.risk_results = []
        if m.get('RiskResults') is not None:
            for k in m.get('RiskResults'):
                temp_model = DescribeWeb3RiskScoreResponseBodyDataRiskResults()
                self.risk_results.append(temp_model.from_map(k))
        if m.get('Score') is not None:
            self.score = m.get('Score')
        return self


class DescribeWeb3RiskScoreResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: DescribeWeb3RiskScoreResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
    ):
        # Return code. For the full list of codes, see Codes and Messages.
        self.code = code
        # data
        self.data = data
        # The HTTP status code.
        self.http_status_code = http_status_code
        # Response detailed message.
        self.message = message
        # The unique ID of the request, which can be used to locate issues.
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
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
            temp_model = DescribeWeb3RiskScoreResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeWeb3RiskScoreResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeWeb3RiskScoreResponseBody = None,
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
            temp_model = DescribeWeb3RiskScoreResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeWeb3TransactionLabelsRequest(TeaModel):
    def __init__(
        self,
        chain_short_name: str = None,
        merchant_biz_id: str = None,
        transaction: str = None,
    ):
        # This is the short name of blockchain。
        # [ ETH, MATIC, BNB ]
        self.chain_short_name = chain_short_name
        # A unique business ID for tracing purpose. For example，the sequence ID from the merchant\"s business-related database.
        self.merchant_biz_id = merchant_biz_id
        # The Transaction hash.
        self.transaction = transaction

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.chain_short_name is not None:
            result['ChainShortName'] = self.chain_short_name
        if self.merchant_biz_id is not None:
            result['MerchantBizId'] = self.merchant_biz_id
        if self.transaction is not None:
            result['Transaction'] = self.transaction
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChainShortName') is not None:
            self.chain_short_name = m.get('ChainShortName')
        if m.get('MerchantBizId') is not None:
            self.merchant_biz_id = m.get('MerchantBizId')
        if m.get('Transaction') is not None:
            self.transaction = m.get('Transaction')
        return self


class DescribeWeb3TransactionLabelsResponseBodyDataContractDetails(TeaModel):
    def __init__(
        self,
        amount: str = None,
        from_: str = None,
        gas_limit: int = None,
        index: int = None,
        to: str = None,
    ):
        # the value of internal transaction
        self.amount = amount
        # the sender of internal transaction
        self.from_ = from_
        # the gaslimit of internal transaction
        self.gas_limit = gas_limit
        # the call layer of internal transaction
        self.index = index
        # the receiver of internal transaction
        self.to = to

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.from_ is not None:
            result['From'] = self.from_
        if self.gas_limit is not None:
            result['GasLimit'] = self.gas_limit
        if self.index is not None:
            result['Index'] = self.index
        if self.to is not None:
            result['To'] = self.to
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('From') is not None:
            self.from_ = m.get('From')
        if m.get('GasLimit') is not None:
            self.gas_limit = m.get('GasLimit')
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('To') is not None:
            self.to = m.get('To')
        return self


class DescribeWeb3TransactionLabelsResponseBodyDataInputDetails(TeaModel):
    def __init__(
        self,
        amount: int = None,
        input_hash: str = None,
        is_contract: str = None,
        tag: str = None,
    ):
        # example: 15. the amount of transation sent by the address
        self.amount = amount
        # the address hash
        self.input_hash = input_hash
        # example: true. is it a contract
        self.is_contract = is_contract
        # example: Dex . the tag of the address
        self.tag = tag

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.input_hash is not None:
            result['InputHash'] = self.input_hash
        if self.is_contract is not None:
            result['IsContract'] = self.is_contract
        if self.tag is not None:
            result['Tag'] = self.tag
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('InputHash') is not None:
            self.input_hash = m.get('InputHash')
        if m.get('IsContract') is not None:
            self.is_contract = m.get('IsContract')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        return self


class DescribeWeb3TransactionLabelsResponseBodyDataOutputDetails(TeaModel):
    def __init__(
        self,
        amount: int = None,
        input_hash: str = None,
        is_contract: str = None,
        tag: str = None,
    ):
        # example: 15. the amount of transation sent by the address
        self.amount = amount
        # the address hash
        self.input_hash = input_hash
        # example: true. is it a contract
        self.is_contract = is_contract
        # example: Dex. the tag of the address
        self.tag = tag

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.input_hash is not None:
            result['InputHash'] = self.input_hash
        if self.is_contract is not None:
            result['IsContract'] = self.is_contract
        if self.tag is not None:
            result['Tag'] = self.tag
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('InputHash') is not None:
            self.input_hash = m.get('InputHash')
        if m.get('IsContract') is not None:
            self.is_contract = m.get('IsContract')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        return self


class DescribeWeb3TransactionLabelsResponseBodyDataTokenTransferDetails(TeaModel):
    def __init__(
        self,
        amount: str = None,
        from_: str = None,
        index: int = None,
        symbol: str = None,
        to: str = None,
        token: str = None,
        token_contract_address: str = None,
        token_id: str = None,
    ):
        # the token amount
        self.amount = amount
        # the sender of the token
        self.from_ = from_
        # the call layer of to token transfer
        self.index = index
        # the token symbol
        self.symbol = symbol
        # the receiver of the token
        self.to = to
        # the token name
        self.token = token
        # the token address
        self.token_contract_address = token_contract_address
        # NFT ID, if the token is erc721
        self.token_id = token_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.from_ is not None:
            result['From'] = self.from_
        if self.index is not None:
            result['Index'] = self.index
        if self.symbol is not None:
            result['Symbol'] = self.symbol
        if self.to is not None:
            result['To'] = self.to
        if self.token is not None:
            result['Token'] = self.token
        if self.token_contract_address is not None:
            result['TokenContractAddress'] = self.token_contract_address
        if self.token_id is not None:
            result['TokenId'] = self.token_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('From') is not None:
            self.from_ = m.get('From')
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('Symbol') is not None:
            self.symbol = m.get('Symbol')
        if m.get('To') is not None:
            self.to = m.get('To')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        if m.get('TokenContractAddress') is not None:
            self.token_contract_address = m.get('TokenContractAddress')
        if m.get('TokenId') is not None:
            self.token_id = m.get('TokenId')
        return self


class DescribeWeb3TransactionLabelsResponseBodyData(TeaModel):
    def __init__(
        self,
        amount: str = None,
        chain_name: str = None,
        chain_short_name: str = None,
        contract_details: List[DescribeWeb3TransactionLabelsResponseBodyDataContractDetails] = None,
        error_log: str = None,
        gas_limit: int = None,
        gas_price: str = None,
        gas_used: int = None,
        height: int = None,
        index: int = None,
        input_data: str = None,
        input_details: List[DescribeWeb3TransactionLabelsResponseBodyDataInputDetails] = None,
        method_id: str = None,
        nonce: str = None,
        output_details: List[DescribeWeb3TransactionLabelsResponseBodyDataOutputDetails] = None,
        state: int = None,
        token_transfer_details: List[DescribeWeb3TransactionLabelsResponseBodyDataTokenTransferDetails] = None,
        transaction_symbol: str = None,
        transaction_time: str = None,
        transaction_type: str = None,
        txfee: str = None,
        txid: str = None,
    ):
        # the amount of native currency
        self.amount = amount
        # chainName
        self.chain_name = chain_name
        # short name of blockchain
        self.chain_short_name = chain_short_name
        # contract details
        self.contract_details = contract_details
        # error log
        self.error_log = error_log
        # gasLimit
        self.gas_limit = gas_limit
        # gasPrice
        self.gas_price = gas_price
        # gasUsed
        self.gas_used = gas_used
        # height
        self.height = height
        # the position of the transaction in the block
        self.index = index
        # input data
        self.input_data = input_data
        # input details
        self.input_details = input_details
        # the method name of contract call. For external transaction method: [\"CALL\",\"CALLCODE\",\"DELEGATECALL\",\"STATICCALL\"]; for internal transaction method: the first 4 bytes of the hash of the method name
        self.method_id = method_id
        # nonce
        self.nonce = nonce
        # output details
        self.output_details = output_details
        # the transaction state. 1: success 0: fail
        self.state = state
        # token transfer details
        self.token_transfer_details = token_transfer_details
        # the symbol of native currency
        self.transaction_symbol = transaction_symbol
        # the block timestamp
        self.transaction_time = transaction_time
        # Integer	0: legacy; 1: eip 2930; 2: eip 1559
        self.transaction_type = transaction_type
        # the transaction fee in eth
        self.txfee = txfee
        # Txid
        self.txid = txid

    def validate(self):
        if self.contract_details:
            for k in self.contract_details:
                if k:
                    k.validate()
        if self.input_details:
            for k in self.input_details:
                if k:
                    k.validate()
        if self.output_details:
            for k in self.output_details:
                if k:
                    k.validate()
        if self.token_transfer_details:
            for k in self.token_transfer_details:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.chain_name is not None:
            result['ChainName'] = self.chain_name
        if self.chain_short_name is not None:
            result['ChainShortName'] = self.chain_short_name
        result['ContractDetails'] = []
        if self.contract_details is not None:
            for k in self.contract_details:
                result['ContractDetails'].append(k.to_map() if k else None)
        if self.error_log is not None:
            result['ErrorLog'] = self.error_log
        if self.gas_limit is not None:
            result['GasLimit'] = self.gas_limit
        if self.gas_price is not None:
            result['GasPrice'] = self.gas_price
        if self.gas_used is not None:
            result['GasUsed'] = self.gas_used
        if self.height is not None:
            result['Height'] = self.height
        if self.index is not None:
            result['Index'] = self.index
        if self.input_data is not None:
            result['InputData'] = self.input_data
        result['InputDetails'] = []
        if self.input_details is not None:
            for k in self.input_details:
                result['InputDetails'].append(k.to_map() if k else None)
        if self.method_id is not None:
            result['MethodId'] = self.method_id
        if self.nonce is not None:
            result['Nonce'] = self.nonce
        result['OutputDetails'] = []
        if self.output_details is not None:
            for k in self.output_details:
                result['OutputDetails'].append(k.to_map() if k else None)
        if self.state is not None:
            result['State'] = self.state
        result['TokenTransferDetails'] = []
        if self.token_transfer_details is not None:
            for k in self.token_transfer_details:
                result['TokenTransferDetails'].append(k.to_map() if k else None)
        if self.transaction_symbol is not None:
            result['TransactionSymbol'] = self.transaction_symbol
        if self.transaction_time is not None:
            result['TransactionTime'] = self.transaction_time
        if self.transaction_type is not None:
            result['TransactionType'] = self.transaction_type
        if self.txfee is not None:
            result['Txfee'] = self.txfee
        if self.txid is not None:
            result['Txid'] = self.txid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('ChainName') is not None:
            self.chain_name = m.get('ChainName')
        if m.get('ChainShortName') is not None:
            self.chain_short_name = m.get('ChainShortName')
        self.contract_details = []
        if m.get('ContractDetails') is not None:
            for k in m.get('ContractDetails'):
                temp_model = DescribeWeb3TransactionLabelsResponseBodyDataContractDetails()
                self.contract_details.append(temp_model.from_map(k))
        if m.get('ErrorLog') is not None:
            self.error_log = m.get('ErrorLog')
        if m.get('GasLimit') is not None:
            self.gas_limit = m.get('GasLimit')
        if m.get('GasPrice') is not None:
            self.gas_price = m.get('GasPrice')
        if m.get('GasUsed') is not None:
            self.gas_used = m.get('GasUsed')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('InputData') is not None:
            self.input_data = m.get('InputData')
        self.input_details = []
        if m.get('InputDetails') is not None:
            for k in m.get('InputDetails'):
                temp_model = DescribeWeb3TransactionLabelsResponseBodyDataInputDetails()
                self.input_details.append(temp_model.from_map(k))
        if m.get('MethodId') is not None:
            self.method_id = m.get('MethodId')
        if m.get('Nonce') is not None:
            self.nonce = m.get('Nonce')
        self.output_details = []
        if m.get('OutputDetails') is not None:
            for k in m.get('OutputDetails'):
                temp_model = DescribeWeb3TransactionLabelsResponseBodyDataOutputDetails()
                self.output_details.append(temp_model.from_map(k))
        if m.get('State') is not None:
            self.state = m.get('State')
        self.token_transfer_details = []
        if m.get('TokenTransferDetails') is not None:
            for k in m.get('TokenTransferDetails'):
                temp_model = DescribeWeb3TransactionLabelsResponseBodyDataTokenTransferDetails()
                self.token_transfer_details.append(temp_model.from_map(k))
        if m.get('TransactionSymbol') is not None:
            self.transaction_symbol = m.get('TransactionSymbol')
        if m.get('TransactionTime') is not None:
            self.transaction_time = m.get('TransactionTime')
        if m.get('TransactionType') is not None:
            self.transaction_type = m.get('TransactionType')
        if m.get('Txfee') is not None:
            self.txfee = m.get('Txfee')
        if m.get('Txid') is not None:
            self.txid = m.get('Txid')
        return self


class DescribeWeb3TransactionLabelsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: DescribeWeb3TransactionLabelsResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
    ):
        # Return code. For the full list of codes, see Codes and Messages.
        self.code = code
        # data
        self.data = data
        # The HTTP status code.
        self.http_status_code = http_status_code
        # Response detailed message.
        self.message = message
        # The unique ID of the request, which can be used to locate issues.
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
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
            temp_model = DescribeWeb3TransactionLabelsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeWeb3TransactionLabelsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeWeb3TransactionLabelsResponseBody = None,
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
            temp_model = DescribeWeb3TransactionLabelsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DocOcrRequest(TeaModel):
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
        face_attack: str = None,
        face_quality_score: float = None,
        occlusion_result: str = None,
    ):
        self.face_attack = face_attack
        self.face_quality_score = face_quality_score
        self.occlusion_result = occlusion_result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.face_attack is not None:
            result['FaceAttack'] = self.face_attack
        if self.face_quality_score is not None:
            result['FaceQualityScore'] = self.face_quality_score
        if self.occlusion_result is not None:
            result['OcclusionResult'] = self.occlusion_result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FaceAttack') is not None:
            self.face_attack = m.get('FaceAttack')
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
        face_picture_base_64: str = None,
        face_picture_url: str = None,
        flow_type: str = None,
        id_face_quality: str = None,
        id_spoof: str = None,
        language_config: str = None,
        merchant_biz_id: str = None,
        merchant_user_id: str = None,
        meta_info: str = None,
        ocr: str = None,
        operation_mode: str = None,
        pages: str = None,
        product_code: str = None,
        product_config: str = None,
        product_flow: str = None,
        return_url: str = None,
        scene_code: str = None,
        service_level: str = None,
    ):
        self.authorize = authorize
        self.callback_token = callback_token
        self.callback_url = callback_url
        self.crop = crop
        self.doc_scan_mode = doc_scan_mode
        self.doc_type = doc_type
        self.face_picture_base_64 = face_picture_base_64
        self.face_picture_url = face_picture_url
        self.flow_type = flow_type
        self.id_face_quality = id_face_quality
        self.id_spoof = id_spoof
        self.language_config = language_config
        self.merchant_biz_id = merchant_biz_id
        self.merchant_user_id = merchant_user_id
        self.meta_info = meta_info
        # OCR。
        self.ocr = ocr
        self.operation_mode = operation_mode
        self.pages = pages
        self.product_code = product_code
        self.product_config = product_config
        self.product_flow = product_flow
        self.return_url = return_url
        self.scene_code = scene_code
        self.service_level = service_level

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
        if self.face_picture_base_64 is not None:
            result['FacePictureBase64'] = self.face_picture_base_64
        if self.face_picture_url is not None:
            result['FacePictureUrl'] = self.face_picture_url
        if self.flow_type is not None:
            result['FlowType'] = self.flow_type
        if self.id_face_quality is not None:
            result['IdFaceQuality'] = self.id_face_quality
        if self.id_spoof is not None:
            result['IdSpoof'] = self.id_spoof
        if self.language_config is not None:
            result['LanguageConfig'] = self.language_config
        if self.merchant_biz_id is not None:
            result['MerchantBizId'] = self.merchant_biz_id
        if self.merchant_user_id is not None:
            result['MerchantUserId'] = self.merchant_user_id
        if self.meta_info is not None:
            result['MetaInfo'] = self.meta_info
        if self.ocr is not None:
            result['Ocr'] = self.ocr
        if self.operation_mode is not None:
            result['OperationMode'] = self.operation_mode
        if self.pages is not None:
            result['Pages'] = self.pages
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.product_config is not None:
            result['ProductConfig'] = self.product_config
        if self.product_flow is not None:
            result['ProductFlow'] = self.product_flow
        if self.return_url is not None:
            result['ReturnUrl'] = self.return_url
        if self.scene_code is not None:
            result['SceneCode'] = self.scene_code
        if self.service_level is not None:
            result['ServiceLevel'] = self.service_level
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
        if m.get('FacePictureBase64') is not None:
            self.face_picture_base_64 = m.get('FacePictureBase64')
        if m.get('FacePictureUrl') is not None:
            self.face_picture_url = m.get('FacePictureUrl')
        if m.get('FlowType') is not None:
            self.flow_type = m.get('FlowType')
        if m.get('IdFaceQuality') is not None:
            self.id_face_quality = m.get('IdFaceQuality')
        if m.get('IdSpoof') is not None:
            self.id_spoof = m.get('IdSpoof')
        if m.get('LanguageConfig') is not None:
            self.language_config = m.get('LanguageConfig')
        if m.get('MerchantBizId') is not None:
            self.merchant_biz_id = m.get('MerchantBizId')
        if m.get('MerchantUserId') is not None:
            self.merchant_user_id = m.get('MerchantUserId')
        if m.get('MetaInfo') is not None:
            self.meta_info = m.get('MetaInfo')
        if m.get('Ocr') is not None:
            self.ocr = m.get('Ocr')
        if m.get('OperationMode') is not None:
            self.operation_mode = m.get('OperationMode')
        if m.get('Pages') is not None:
            self.pages = m.get('Pages')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProductConfig') is not None:
            self.product_config = m.get('ProductConfig')
        if m.get('ProductFlow') is not None:
            self.product_flow = m.get('ProductFlow')
        if m.get('ReturnUrl') is not None:
            self.return_url = m.get('ReturnUrl')
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


