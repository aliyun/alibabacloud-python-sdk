# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List, Any


class BindApplicantRequest(TeaModel):
    def __init__(
        self,
        applicant_id: str = None,
        authorization_oss_key: str = None,
        biz_id: str = None,
    ):
        self.applicant_id = applicant_id
        self.authorization_oss_key = authorization_oss_key
        self.biz_id = biz_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.applicant_id is not None:
            result['ApplicantId'] = self.applicant_id
        if self.authorization_oss_key is not None:
            result['AuthorizationOssKey'] = self.authorization_oss_key
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicantId') is not None:
            self.applicant_id = m.get('ApplicantId')
        if m.get('AuthorizationOssKey') is not None:
            self.authorization_oss_key = m.get('AuthorizationOssKey')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        return self


class BindApplicantResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class BindApplicantResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BindApplicantResponseBody = None,
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
            temp_model = BindApplicantResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelOrderRequest(TeaModel):
    def __init__(
        self,
        order_id: int = None,
    ):
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


class CancelOrderResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CancelOrderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CancelOrderResponseBody = None,
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
            temp_model = CancelOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckAuthorizationLetterRequest(TeaModel):
    def __init__(
        self,
        applicant_type: str = None,
        color: str = None,
        contact_name: str = None,
        contact_number: str = None,
        contact_zipcode: str = None,
        oss_key: str = None,
        personal_type: str = None,
        type: str = None,
    ):
        self.applicant_type = applicant_type
        self.color = color
        self.contact_name = contact_name
        self.contact_number = contact_number
        self.contact_zipcode = contact_zipcode
        self.oss_key = oss_key
        self.personal_type = personal_type
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.applicant_type is not None:
            result['ApplicantType'] = self.applicant_type
        if self.color is not None:
            result['Color'] = self.color
        if self.contact_name is not None:
            result['ContactName'] = self.contact_name
        if self.contact_number is not None:
            result['ContactNumber'] = self.contact_number
        if self.contact_zipcode is not None:
            result['ContactZipcode'] = self.contact_zipcode
        if self.oss_key is not None:
            result['OssKey'] = self.oss_key
        if self.personal_type is not None:
            result['PersonalType'] = self.personal_type
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicantType') is not None:
            self.applicant_type = m.get('ApplicantType')
        if m.get('Color') is not None:
            self.color = m.get('Color')
        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')
        if m.get('ContactNumber') is not None:
            self.contact_number = m.get('ContactNumber')
        if m.get('ContactZipcode') is not None:
            self.contact_zipcode = m.get('ContactZipcode')
        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')
        if m.get('PersonalType') is not None:
            self.personal_type = m.get('PersonalType')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CheckAuthorizationLetterResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        template_url: str = None,
        tips: str = None,
    ):
        self.request_id = request_id
        self.template_url = template_url
        self.tips = tips

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.template_url is not None:
            result['TemplateUrl'] = self.template_url
        if self.tips is not None:
            result['Tips'] = self.tips
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TemplateUrl') is not None:
            self.template_url = m.get('TemplateUrl')
        if m.get('Tips') is not None:
            self.tips = m.get('Tips')
        return self


class CheckAuthorizationLetterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CheckAuthorizationLetterResponseBody = None,
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
            temp_model = CheckAuthorizationLetterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckBizAvailableRequest(TeaModel):
    def __init__(
        self,
        biz: str = None,
        scene: str = None,
    ):
        self.biz = biz
        self.scene = scene

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz is not None:
            result['Biz'] = self.biz
        if self.scene is not None:
            result['Scene'] = self.scene
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Biz') is not None:
            self.biz = m.get('Biz')
        if m.get('Scene') is not None:
            self.scene = m.get('Scene')
        return self


class CheckBizAvailableResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CheckBizAvailableResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CheckBizAvailableResponseBody = None,
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
            temp_model = CheckBizAvailableResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckDuplicateApplicantRiskRequest(TeaModel):
    def __init__(
        self,
        applicant_name: str = None,
        event_scene_type: int = None,
    ):
        self.applicant_name = applicant_name
        self.event_scene_type = event_scene_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.applicant_name is not None:
            result['ApplicantName'] = self.applicant_name
        if self.event_scene_type is not None:
            result['EventSceneType'] = self.event_scene_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicantName') is not None:
            self.applicant_name = m.get('ApplicantName')
        if m.get('EventSceneType') is not None:
            self.event_scene_type = m.get('EventSceneType')
        return self


class CheckDuplicateApplicantRiskResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: str = None,
    ):
        self.request_id = request_id
        self.result = result

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class CheckDuplicateApplicantRiskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CheckDuplicateApplicantRiskResponseBody = None,
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
            temp_model = CheckDuplicateApplicantRiskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckDuplicateClassificationRequest(TeaModel):
    def __init__(
        self,
        classification: str = None,
        event_scene_type: int = None,
        trademark_name: str = None,
    ):
        self.classification = classification
        self.event_scene_type = event_scene_type
        self.trademark_name = trademark_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.classification is not None:
            result['Classification'] = self.classification
        if self.event_scene_type is not None:
            result['EventSceneType'] = self.event_scene_type
        if self.trademark_name is not None:
            result['TrademarkName'] = self.trademark_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Classification') is not None:
            self.classification = m.get('Classification')
        if m.get('EventSceneType') is not None:
            self.event_scene_type = m.get('EventSceneType')
        if m.get('TrademarkName') is not None:
            self.trademark_name = m.get('TrademarkName')
        return self


class CheckDuplicateClassificationResponseBodyDataDuplicateSecondaryClassification(TeaModel):
    def __init__(
        self,
        secondary_classification: List[str] = None,
    ):
        self.secondary_classification = secondary_classification

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.secondary_classification is not None:
            result['SecondaryClassification'] = self.secondary_classification
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecondaryClassification') is not None:
            self.secondary_classification = m.get('SecondaryClassification')
        return self


class CheckDuplicateClassificationResponseBodyData(TeaModel):
    def __init__(
        self,
        duplicate_secondary_classification: CheckDuplicateClassificationResponseBodyDataDuplicateSecondaryClassification = None,
        trademark_name: str = None,
    ):
        self.duplicate_secondary_classification = duplicate_secondary_classification
        self.trademark_name = trademark_name

    def validate(self):
        if self.duplicate_secondary_classification:
            self.duplicate_secondary_classification.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.duplicate_secondary_classification is not None:
            result['DuplicateSecondaryClassification'] = self.duplicate_secondary_classification.to_map()
        if self.trademark_name is not None:
            result['TrademarkName'] = self.trademark_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DuplicateSecondaryClassification') is not None:
            temp_model = CheckDuplicateClassificationResponseBodyDataDuplicateSecondaryClassification()
            self.duplicate_secondary_classification = temp_model.from_map(m['DuplicateSecondaryClassification'])
        if m.get('TrademarkName') is not None:
            self.trademark_name = m.get('TrademarkName')
        return self


class CheckDuplicateClassificationResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CheckDuplicateClassificationResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
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
            temp_model = CheckDuplicateClassificationResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CheckDuplicateClassificationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CheckDuplicateClassificationResponseBody = None,
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
            temp_model = CheckDuplicateClassificationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckDuplicateTrademarkRequest(TeaModel):
    def __init__(
        self,
        classification: str = None,
        event_scene_type: int = None,
        material_name: str = None,
        trademark_name: str = None,
    ):
        self.classification = classification
        self.event_scene_type = event_scene_type
        self.material_name = material_name
        self.trademark_name = trademark_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.classification is not None:
            result['Classification'] = self.classification
        if self.event_scene_type is not None:
            result['EventSceneType'] = self.event_scene_type
        if self.material_name is not None:
            result['MaterialName'] = self.material_name
        if self.trademark_name is not None:
            result['TrademarkName'] = self.trademark_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Classification') is not None:
            self.classification = m.get('Classification')
        if m.get('EventSceneType') is not None:
            self.event_scene_type = m.get('EventSceneType')
        if m.get('MaterialName') is not None:
            self.material_name = m.get('MaterialName')
        if m.get('TrademarkName') is not None:
            self.trademark_name = m.get('TrademarkName')
        return self


class CheckDuplicateTrademarkResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        duplicate_trademark: str = None,
        message: str = None,
        request_id: str = None,
        type: str = None,
    ):
        self.code = code
        self.duplicate_trademark = duplicate_trademark
        self.message = message
        self.request_id = request_id
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.duplicate_trademark is not None:
            result['DuplicateTrademark'] = self.duplicate_trademark
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DuplicateTrademark') is not None:
            self.duplicate_trademark = m.get('DuplicateTrademark')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CheckDuplicateTrademarkResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CheckDuplicateTrademarkResponseBody = None,
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
            temp_model = CheckDuplicateTrademarkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckMaterialValidityRequest(TeaModel):
    def __init__(
        self,
        business_license_oss_key: str = None,
        card_number: str = None,
        id_card_name: str = None,
        id_card_number: str = None,
        id_card_oss_key: str = None,
        material_id: int = None,
        material_region: int = None,
        material_type: int = None,
        name: str = None,
        personal_type: int = None,
    ):
        self.business_license_oss_key = business_license_oss_key
        self.card_number = card_number
        self.id_card_name = id_card_name
        self.id_card_number = id_card_number
        self.id_card_oss_key = id_card_oss_key
        self.material_id = material_id
        self.material_region = material_region
        self.material_type = material_type
        self.name = name
        self.personal_type = personal_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_license_oss_key is not None:
            result['BusinessLicenseOssKey'] = self.business_license_oss_key
        if self.card_number is not None:
            result['CardNumber'] = self.card_number
        if self.id_card_name is not None:
            result['IdCardName'] = self.id_card_name
        if self.id_card_number is not None:
            result['IdCardNumber'] = self.id_card_number
        if self.id_card_oss_key is not None:
            result['IdCardOssKey'] = self.id_card_oss_key
        if self.material_id is not None:
            result['MaterialId'] = self.material_id
        if self.material_region is not None:
            result['MaterialRegion'] = self.material_region
        if self.material_type is not None:
            result['MaterialType'] = self.material_type
        if self.name is not None:
            result['Name'] = self.name
        if self.personal_type is not None:
            result['PersonalType'] = self.personal_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessLicenseOssKey') is not None:
            self.business_license_oss_key = m.get('BusinessLicenseOssKey')
        if m.get('CardNumber') is not None:
            self.card_number = m.get('CardNumber')
        if m.get('IdCardName') is not None:
            self.id_card_name = m.get('IdCardName')
        if m.get('IdCardNumber') is not None:
            self.id_card_number = m.get('IdCardNumber')
        if m.get('IdCardOssKey') is not None:
            self.id_card_oss_key = m.get('IdCardOssKey')
        if m.get('MaterialId') is not None:
            self.material_id = m.get('MaterialId')
        if m.get('MaterialRegion') is not None:
            self.material_region = m.get('MaterialRegion')
        if m.get('MaterialType') is not None:
            self.material_type = m.get('MaterialType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PersonalType') is not None:
            self.personal_type = m.get('PersonalType')
        return self


class CheckMaterialValidityResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CheckMaterialValidityResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CheckMaterialValidityResponseBody = None,
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
            temp_model = CheckMaterialValidityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckTrademarkNameRequest(TeaModel):
    def __init__(
        self,
        event_scene_type: int = None,
        trademark_name: str = None,
    ):
        self.event_scene_type = event_scene_type
        self.trademark_name = trademark_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_scene_type is not None:
            result['EventSceneType'] = self.event_scene_type
        if self.trademark_name is not None:
            result['TrademarkName'] = self.trademark_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventSceneType') is not None:
            self.event_scene_type = m.get('EventSceneType')
        if m.get('TrademarkName') is not None:
            self.trademark_name = m.get('TrademarkName')
        return self


class CheckTrademarkNameResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        result: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class CheckTrademarkNameResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CheckTrademarkNameResponseBody = None,
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
            temp_model = CheckTrademarkNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CloseTrademarkApplicationRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
    ):
        self.biz_id = biz_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        return self


class CloseTrademarkApplicationResponseBody(TeaModel):
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


class CloseTrademarkApplicationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CloseTrademarkApplicationResponseBody = None,
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
            temp_model = CloseTrademarkApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CombineAuthorizationLetterRequest(TeaModel):
    def __init__(
        self,
        address: str = None,
        applicant_type: str = None,
        contact_name: str = None,
        contact_phone: str = None,
        contact_postcode: str = None,
        material_id: str = None,
        material_name: str = None,
        nationality: str = None,
        personal_type: str = None,
        principal_name: int = None,
        tm_produce_type: str = None,
        trademark_name: str = None,
    ):
        self.address = address
        self.applicant_type = applicant_type
        self.contact_name = contact_name
        self.contact_phone = contact_phone
        self.contact_postcode = contact_postcode
        self.material_id = material_id
        self.material_name = material_name
        self.nationality = nationality
        self.personal_type = personal_type
        self.principal_name = principal_name
        self.tm_produce_type = tm_produce_type
        self.trademark_name = trademark_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.applicant_type is not None:
            result['ApplicantType'] = self.applicant_type
        if self.contact_name is not None:
            result['ContactName'] = self.contact_name
        if self.contact_phone is not None:
            result['ContactPhone'] = self.contact_phone
        if self.contact_postcode is not None:
            result['ContactPostcode'] = self.contact_postcode
        if self.material_id is not None:
            result['MaterialId'] = self.material_id
        if self.material_name is not None:
            result['MaterialName'] = self.material_name
        if self.nationality is not None:
            result['Nationality'] = self.nationality
        if self.personal_type is not None:
            result['PersonalType'] = self.personal_type
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name
        if self.tm_produce_type is not None:
            result['TmProduceType'] = self.tm_produce_type
        if self.trademark_name is not None:
            result['TrademarkName'] = self.trademark_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('ApplicantType') is not None:
            self.applicant_type = m.get('ApplicantType')
        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')
        if m.get('ContactPhone') is not None:
            self.contact_phone = m.get('ContactPhone')
        if m.get('ContactPostcode') is not None:
            self.contact_postcode = m.get('ContactPostcode')
        if m.get('MaterialId') is not None:
            self.material_id = m.get('MaterialId')
        if m.get('MaterialName') is not None:
            self.material_name = m.get('MaterialName')
        if m.get('Nationality') is not None:
            self.nationality = m.get('Nationality')
        if m.get('PersonalType') is not None:
            self.personal_type = m.get('PersonalType')
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')
        if m.get('TmProduceType') is not None:
            self.tm_produce_type = m.get('TmProduceType')
        if m.get('TrademarkName') is not None:
            self.trademark_name = m.get('TrademarkName')
        return self


class CombineAuthorizationLetterResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        template_combine_url: str = None,
    ):
        self.request_id = request_id
        self.template_combine_url = template_combine_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.template_combine_url is not None:
            result['TemplateCombineUrl'] = self.template_combine_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TemplateCombineUrl') is not None:
            self.template_combine_url = m.get('TemplateCombineUrl')
        return self


class CombineAuthorizationLetterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CombineAuthorizationLetterResponseBody = None,
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
            temp_model = CombineAuthorizationLetterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ComplementTrademarkApplicationRequest(TeaModel):
    def __init__(
        self,
        agreement_id: str = None,
        authorization_oss_key: str = None,
        biz_id: str = None,
        is_black_icon: bool = None,
        material_id: str = None,
        order_data: str = None,
        source: str = None,
        trademark_comment: str = None,
        trademark_icon_oss_key: str = None,
        trademark_name: str = None,
        trademark_name_type: str = None,
        trademark_type: int = None,
    ):
        self.agreement_id = agreement_id
        self.authorization_oss_key = authorization_oss_key
        self.biz_id = biz_id
        self.is_black_icon = is_black_icon
        self.material_id = material_id
        self.order_data = order_data
        self.source = source
        self.trademark_comment = trademark_comment
        self.trademark_icon_oss_key = trademark_icon_oss_key
        self.trademark_name = trademark_name
        self.trademark_name_type = trademark_name_type
        self.trademark_type = trademark_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agreement_id is not None:
            result['AgreementId'] = self.agreement_id
        if self.authorization_oss_key is not None:
            result['AuthorizationOssKey'] = self.authorization_oss_key
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.is_black_icon is not None:
            result['IsBlackIcon'] = self.is_black_icon
        if self.material_id is not None:
            result['MaterialId'] = self.material_id
        if self.order_data is not None:
            result['OrderData'] = self.order_data
        if self.source is not None:
            result['Source'] = self.source
        if self.trademark_comment is not None:
            result['TrademarkComment'] = self.trademark_comment
        if self.trademark_icon_oss_key is not None:
            result['TrademarkIconOssKey'] = self.trademark_icon_oss_key
        if self.trademark_name is not None:
            result['TrademarkName'] = self.trademark_name
        if self.trademark_name_type is not None:
            result['TrademarkNameType'] = self.trademark_name_type
        if self.trademark_type is not None:
            result['TrademarkType'] = self.trademark_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgreementId') is not None:
            self.agreement_id = m.get('AgreementId')
        if m.get('AuthorizationOssKey') is not None:
            self.authorization_oss_key = m.get('AuthorizationOssKey')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('IsBlackIcon') is not None:
            self.is_black_icon = m.get('IsBlackIcon')
        if m.get('MaterialId') is not None:
            self.material_id = m.get('MaterialId')
        if m.get('OrderData') is not None:
            self.order_data = m.get('OrderData')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('TrademarkComment') is not None:
            self.trademark_comment = m.get('TrademarkComment')
        if m.get('TrademarkIconOssKey') is not None:
            self.trademark_icon_oss_key = m.get('TrademarkIconOssKey')
        if m.get('TrademarkName') is not None:
            self.trademark_name = m.get('TrademarkName')
        if m.get('TrademarkNameType') is not None:
            self.trademark_name_type = m.get('TrademarkNameType')
        if m.get('TrademarkType') is not None:
            self.trademark_type = m.get('TrademarkType')
        return self


class ComplementTrademarkApplicationResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ComplementTrademarkApplicationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ComplementTrademarkApplicationResponseBody = None,
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
            temp_model = ComplementTrademarkApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConfirmExpertSolutionRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        note: str = None,
    ):
        self.biz_id = biz_id
        self.note = note

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.note is not None:
            result['Note'] = self.note
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        return self


class ConfirmExpertSolutionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ConfirmExpertSolutionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ConfirmExpertSolutionResponseBody = None,
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
            temp_model = ConfirmExpertSolutionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateApplicantRequest(TeaModel):
    def __init__(
        self,
        address: str = None,
        applicant_name: str = None,
        applicant_region: int = None,
        applicant_type: int = None,
        authorization_oss_key: str = None,
        business_licence_oss_key: str = None,
        card_number: str = None,
        contact_address: str = None,
        contact_city: str = None,
        contact_county: str = None,
        contact_district: str = None,
        contact_email: str = None,
        contact_name: str = None,
        contact_number: str = None,
        contact_province: str = None,
        contact_zipcode: str = None,
        country: str = None,
        eaddress: str = None,
        ename: str = None,
        id_card_name: str = None,
        id_card_number: str = None,
        id_card_oss_key: str = None,
        legal_notice_oss_key: str = None,
        passport_oss_key: str = None,
        personal_type: int = None,
        principal_name: int = None,
        province: str = None,
    ):
        self.address = address
        self.applicant_name = applicant_name
        self.applicant_region = applicant_region
        self.applicant_type = applicant_type
        self.authorization_oss_key = authorization_oss_key
        self.business_licence_oss_key = business_licence_oss_key
        self.card_number = card_number
        self.contact_address = contact_address
        self.contact_city = contact_city
        self.contact_county = contact_county
        self.contact_district = contact_district
        self.contact_email = contact_email
        self.contact_name = contact_name
        self.contact_number = contact_number
        self.contact_province = contact_province
        self.contact_zipcode = contact_zipcode
        self.country = country
        self.eaddress = eaddress
        self.ename = ename
        self.id_card_name = id_card_name
        self.id_card_number = id_card_number
        self.id_card_oss_key = id_card_oss_key
        self.legal_notice_oss_key = legal_notice_oss_key
        self.passport_oss_key = passport_oss_key
        self.personal_type = personal_type
        self.principal_name = principal_name
        self.province = province

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.applicant_name is not None:
            result['ApplicantName'] = self.applicant_name
        if self.applicant_region is not None:
            result['ApplicantRegion'] = self.applicant_region
        if self.applicant_type is not None:
            result['ApplicantType'] = self.applicant_type
        if self.authorization_oss_key is not None:
            result['AuthorizationOssKey'] = self.authorization_oss_key
        if self.business_licence_oss_key is not None:
            result['BusinessLicenceOssKey'] = self.business_licence_oss_key
        if self.card_number is not None:
            result['CardNumber'] = self.card_number
        if self.contact_address is not None:
            result['ContactAddress'] = self.contact_address
        if self.contact_city is not None:
            result['ContactCity'] = self.contact_city
        if self.contact_county is not None:
            result['ContactCounty'] = self.contact_county
        if self.contact_district is not None:
            result['ContactDistrict'] = self.contact_district
        if self.contact_email is not None:
            result['ContactEmail'] = self.contact_email
        if self.contact_name is not None:
            result['ContactName'] = self.contact_name
        if self.contact_number is not None:
            result['ContactNumber'] = self.contact_number
        if self.contact_province is not None:
            result['ContactProvince'] = self.contact_province
        if self.contact_zipcode is not None:
            result['ContactZipcode'] = self.contact_zipcode
        if self.country is not None:
            result['Country'] = self.country
        if self.eaddress is not None:
            result['EAddress'] = self.eaddress
        if self.ename is not None:
            result['EName'] = self.ename
        if self.id_card_name is not None:
            result['IdCardName'] = self.id_card_name
        if self.id_card_number is not None:
            result['IdCardNumber'] = self.id_card_number
        if self.id_card_oss_key is not None:
            result['IdCardOssKey'] = self.id_card_oss_key
        if self.legal_notice_oss_key is not None:
            result['LegalNoticeOssKey'] = self.legal_notice_oss_key
        if self.passport_oss_key is not None:
            result['PassportOssKey'] = self.passport_oss_key
        if self.personal_type is not None:
            result['PersonalType'] = self.personal_type
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name
        if self.province is not None:
            result['Province'] = self.province
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('ApplicantName') is not None:
            self.applicant_name = m.get('ApplicantName')
        if m.get('ApplicantRegion') is not None:
            self.applicant_region = m.get('ApplicantRegion')
        if m.get('ApplicantType') is not None:
            self.applicant_type = m.get('ApplicantType')
        if m.get('AuthorizationOssKey') is not None:
            self.authorization_oss_key = m.get('AuthorizationOssKey')
        if m.get('BusinessLicenceOssKey') is not None:
            self.business_licence_oss_key = m.get('BusinessLicenceOssKey')
        if m.get('CardNumber') is not None:
            self.card_number = m.get('CardNumber')
        if m.get('ContactAddress') is not None:
            self.contact_address = m.get('ContactAddress')
        if m.get('ContactCity') is not None:
            self.contact_city = m.get('ContactCity')
        if m.get('ContactCounty') is not None:
            self.contact_county = m.get('ContactCounty')
        if m.get('ContactDistrict') is not None:
            self.contact_district = m.get('ContactDistrict')
        if m.get('ContactEmail') is not None:
            self.contact_email = m.get('ContactEmail')
        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')
        if m.get('ContactNumber') is not None:
            self.contact_number = m.get('ContactNumber')
        if m.get('ContactProvince') is not None:
            self.contact_province = m.get('ContactProvince')
        if m.get('ContactZipcode') is not None:
            self.contact_zipcode = m.get('ContactZipcode')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('EAddress') is not None:
            self.eaddress = m.get('EAddress')
        if m.get('EName') is not None:
            self.ename = m.get('EName')
        if m.get('IdCardName') is not None:
            self.id_card_name = m.get('IdCardName')
        if m.get('IdCardNumber') is not None:
            self.id_card_number = m.get('IdCardNumber')
        if m.get('IdCardOssKey') is not None:
            self.id_card_oss_key = m.get('IdCardOssKey')
        if m.get('LegalNoticeOssKey') is not None:
            self.legal_notice_oss_key = m.get('LegalNoticeOssKey')
        if m.get('PassportOssKey') is not None:
            self.passport_oss_key = m.get('PassportOssKey')
        if m.get('PersonalType') is not None:
            self.personal_type = m.get('PersonalType')
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        return self


class CreateApplicantResponseBody(TeaModel):
    def __init__(
        self,
        applicant_id: str = None,
        request_id: str = None,
    ):
        self.applicant_id = applicant_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.applicant_id is not None:
            result['ApplicantId'] = self.applicant_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicantId') is not None:
            self.applicant_id = m.get('ApplicantId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateApplicantResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateApplicantResponseBody = None,
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
            temp_model = CreateApplicantResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCommodityOrderRequest(TeaModel):
    def __init__(
        self,
        auto_pay: bool = None,
        biz_type: str = None,
        charge_type: str = None,
        client_token: str = None,
        commodity_code: str = None,
        components: Dict[str, Any] = None,
        duration: int = None,
        instance_id: str = None,
        order_params: Dict[str, Any] = None,
        order_type: str = None,
        pricing_cycle: str = None,
        quantity: int = None,
        spec_code: str = None,
        user_id: str = None,
    ):
        self.auto_pay = auto_pay
        self.biz_type = biz_type
        self.charge_type = charge_type
        self.client_token = client_token
        self.commodity_code = commodity_code
        self.components = components
        self.duration = duration
        self.instance_id = instance_id
        self.order_params = order_params
        self.order_type = order_type
        self.pricing_cycle = pricing_cycle
        self.quantity = quantity
        self.spec_code = spec_code
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        if self.components is not None:
            result['Components'] = self.components
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.order_params is not None:
            result['OrderParams'] = self.order_params
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle
        if self.quantity is not None:
            result['Quantity'] = self.quantity
        if self.spec_code is not None:
            result['SpecCode'] = self.spec_code
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        if m.get('Components') is not None:
            self.components = m.get('Components')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OrderParams') is not None:
            self.order_params = m.get('OrderParams')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')
        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')
        if m.get('SpecCode') is not None:
            self.spec_code = m.get('SpecCode')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class CreateCommodityOrderShrinkRequest(TeaModel):
    def __init__(
        self,
        auto_pay: bool = None,
        biz_type: str = None,
        charge_type: str = None,
        client_token: str = None,
        commodity_code: str = None,
        components_shrink: str = None,
        duration: int = None,
        instance_id: str = None,
        order_params_shrink: str = None,
        order_type: str = None,
        pricing_cycle: str = None,
        quantity: int = None,
        spec_code: str = None,
        user_id: str = None,
    ):
        self.auto_pay = auto_pay
        self.biz_type = biz_type
        self.charge_type = charge_type
        self.client_token = client_token
        self.commodity_code = commodity_code
        self.components_shrink = components_shrink
        self.duration = duration
        self.instance_id = instance_id
        self.order_params_shrink = order_params_shrink
        self.order_type = order_type
        self.pricing_cycle = pricing_cycle
        self.quantity = quantity
        self.spec_code = spec_code
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        if self.components_shrink is not None:
            result['Components'] = self.components_shrink
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.order_params_shrink is not None:
            result['OrderParams'] = self.order_params_shrink
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle
        if self.quantity is not None:
            result['Quantity'] = self.quantity
        if self.spec_code is not None:
            result['SpecCode'] = self.spec_code
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        if m.get('Components') is not None:
            self.components_shrink = m.get('Components')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OrderParams') is not None:
            self.order_params_shrink = m.get('OrderParams')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')
        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')
        if m.get('SpecCode') is not None:
            self.spec_code = m.get('SpecCode')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class CreateCommodityOrderResponseBody(TeaModel):
    def __init__(
        self,
        data: List[int] = None,
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


class CreateCommodityOrderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateCommodityOrderResponseBody = None,
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
            temp_model = CreateCommodityOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateOrderRequest(TeaModel):
    def __init__(
        self,
        agreement_id: str = None,
        applicant_id: str = None,
        application_type: int = None,
        authorization_oss_key: str = None,
        auto_pay: bool = None,
        black_and_white_icon: str = None,
        channel: str = None,
        classifications: str = None,
        idempotent_id: str = None,
        legal_notice_key: str = None,
        pay_type: str = None,
        payment_callback: str = None,
        principal_name: int = None,
        source: str = None,
        trademark_comment: str = None,
        trademark_icon: str = None,
        trademark_name: str = None,
        trademark_name_type: str = None,
    ):
        self.agreement_id = agreement_id
        self.applicant_id = applicant_id
        self.application_type = application_type
        self.authorization_oss_key = authorization_oss_key
        self.auto_pay = auto_pay
        self.black_and_white_icon = black_and_white_icon
        self.channel = channel
        self.classifications = classifications
        self.idempotent_id = idempotent_id
        self.legal_notice_key = legal_notice_key
        self.pay_type = pay_type
        self.payment_callback = payment_callback
        self.principal_name = principal_name
        self.source = source
        self.trademark_comment = trademark_comment
        self.trademark_icon = trademark_icon
        self.trademark_name = trademark_name
        self.trademark_name_type = trademark_name_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agreement_id is not None:
            result['AgreementId'] = self.agreement_id
        if self.applicant_id is not None:
            result['ApplicantId'] = self.applicant_id
        if self.application_type is not None:
            result['ApplicationType'] = self.application_type
        if self.authorization_oss_key is not None:
            result['AuthorizationOssKey'] = self.authorization_oss_key
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay
        if self.black_and_white_icon is not None:
            result['BlackAndWhiteIcon'] = self.black_and_white_icon
        if self.channel is not None:
            result['Channel'] = self.channel
        if self.classifications is not None:
            result['Classifications'] = self.classifications
        if self.idempotent_id is not None:
            result['IdempotentId'] = self.idempotent_id
        if self.legal_notice_key is not None:
            result['LegalNoticeKey'] = self.legal_notice_key
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.payment_callback is not None:
            result['PaymentCallback'] = self.payment_callback
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name
        if self.source is not None:
            result['Source'] = self.source
        if self.trademark_comment is not None:
            result['TrademarkComment'] = self.trademark_comment
        if self.trademark_icon is not None:
            result['TrademarkIcon'] = self.trademark_icon
        if self.trademark_name is not None:
            result['TrademarkName'] = self.trademark_name
        if self.trademark_name_type is not None:
            result['TrademarkNameType'] = self.trademark_name_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgreementId') is not None:
            self.agreement_id = m.get('AgreementId')
        if m.get('ApplicantId') is not None:
            self.applicant_id = m.get('ApplicantId')
        if m.get('ApplicationType') is not None:
            self.application_type = m.get('ApplicationType')
        if m.get('AuthorizationOssKey') is not None:
            self.authorization_oss_key = m.get('AuthorizationOssKey')
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')
        if m.get('BlackAndWhiteIcon') is not None:
            self.black_and_white_icon = m.get('BlackAndWhiteIcon')
        if m.get('Channel') is not None:
            self.channel = m.get('Channel')
        if m.get('Classifications') is not None:
            self.classifications = m.get('Classifications')
        if m.get('IdempotentId') is not None:
            self.idempotent_id = m.get('IdempotentId')
        if m.get('LegalNoticeKey') is not None:
            self.legal_notice_key = m.get('LegalNoticeKey')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('PaymentCallback') is not None:
            self.payment_callback = m.get('PaymentCallback')
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('TrademarkComment') is not None:
            self.trademark_comment = m.get('TrademarkComment')
        if m.get('TrademarkIcon') is not None:
            self.trademark_icon = m.get('TrademarkIcon')
        if m.get('TrademarkName') is not None:
            self.trademark_name = m.get('TrademarkName')
        if m.get('TrademarkNameType') is not None:
            self.trademark_name_type = m.get('TrademarkNameType')
        return self


class CreateOrderResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        order_ids: Dict[str, Any] = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.message = message
        self.order_ids = order_ids
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.order_ids is not None:
            result['OrderIds'] = self.order_ids
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('OrderIds') is not None:
            self.order_ids = m.get('OrderIds')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
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


class CreateTrademarkApplicationRequest(TeaModel):
    def __init__(
        self,
        agreement_id: str = None,
        applicant_id: str = None,
        application_type: int = None,
        authorization_oss_key: str = None,
        auto_pay: bool = None,
        black_and_white_icon: str = None,
        channel: str = None,
        classifications: str = None,
        idempotent_id: str = None,
        legal_notice_key: str = None,
        principal_name: int = None,
        source: str = None,
        trademark_comment: str = None,
        trademark_icon: str = None,
        trademark_name: str = None,
        trademark_name_type: str = None,
    ):
        self.agreement_id = agreement_id
        self.applicant_id = applicant_id
        self.application_type = application_type
        self.authorization_oss_key = authorization_oss_key
        self.auto_pay = auto_pay
        self.black_and_white_icon = black_and_white_icon
        self.channel = channel
        self.classifications = classifications
        self.idempotent_id = idempotent_id
        self.legal_notice_key = legal_notice_key
        self.principal_name = principal_name
        self.source = source
        self.trademark_comment = trademark_comment
        self.trademark_icon = trademark_icon
        self.trademark_name = trademark_name
        self.trademark_name_type = trademark_name_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agreement_id is not None:
            result['AgreementId'] = self.agreement_id
        if self.applicant_id is not None:
            result['ApplicantId'] = self.applicant_id
        if self.application_type is not None:
            result['ApplicationType'] = self.application_type
        if self.authorization_oss_key is not None:
            result['AuthorizationOssKey'] = self.authorization_oss_key
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay
        if self.black_and_white_icon is not None:
            result['BlackAndWhiteIcon'] = self.black_and_white_icon
        if self.channel is not None:
            result['Channel'] = self.channel
        if self.classifications is not None:
            result['Classifications'] = self.classifications
        if self.idempotent_id is not None:
            result['IdempotentId'] = self.idempotent_id
        if self.legal_notice_key is not None:
            result['LegalNoticeKey'] = self.legal_notice_key
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name
        if self.source is not None:
            result['Source'] = self.source
        if self.trademark_comment is not None:
            result['TrademarkComment'] = self.trademark_comment
        if self.trademark_icon is not None:
            result['TrademarkIcon'] = self.trademark_icon
        if self.trademark_name is not None:
            result['TrademarkName'] = self.trademark_name
        if self.trademark_name_type is not None:
            result['TrademarkNameType'] = self.trademark_name_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgreementId') is not None:
            self.agreement_id = m.get('AgreementId')
        if m.get('ApplicantId') is not None:
            self.applicant_id = m.get('ApplicantId')
        if m.get('ApplicationType') is not None:
            self.application_type = m.get('ApplicationType')
        if m.get('AuthorizationOssKey') is not None:
            self.authorization_oss_key = m.get('AuthorizationOssKey')
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')
        if m.get('BlackAndWhiteIcon') is not None:
            self.black_and_white_icon = m.get('BlackAndWhiteIcon')
        if m.get('Channel') is not None:
            self.channel = m.get('Channel')
        if m.get('Classifications') is not None:
            self.classifications = m.get('Classifications')
        if m.get('IdempotentId') is not None:
            self.idempotent_id = m.get('IdempotentId')
        if m.get('LegalNoticeKey') is not None:
            self.legal_notice_key = m.get('LegalNoticeKey')
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('TrademarkComment') is not None:
            self.trademark_comment = m.get('TrademarkComment')
        if m.get('TrademarkIcon') is not None:
            self.trademark_icon = m.get('TrademarkIcon')
        if m.get('TrademarkName') is not None:
            self.trademark_name = m.get('TrademarkName')
        if m.get('TrademarkNameType') is not None:
            self.trademark_name_type = m.get('TrademarkNameType')
        return self


class CreateTrademarkApplicationResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        order_id: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.message = message
        self.order_id = order_id
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateTrademarkApplicationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateTrademarkApplicationResponseBody = None,
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
            temp_model = CreateTrademarkApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSearchConditionRequest(TeaModel):
    def __init__(
        self,
        condition_id: int = None,
        session_id: str = None,
        umid: str = None,
    ):
        self.condition_id = condition_id
        self.session_id = session_id
        self.umid = umid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.condition_id is not None:
            result['ConditionId'] = self.condition_id
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.umid is not None:
            result['Umid'] = self.umid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConditionId') is not None:
            self.condition_id = m.get('ConditionId')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('Umid') is not None:
            self.umid = m.get('Umid')
        return self


class DeleteSearchConditionResponseBody(TeaModel):
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


class DeleteSearchConditionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteSearchConditionResponseBody = None,
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
            temp_model = DeleteSearchConditionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAdminTrademarkApplicationRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
    ):
        self.biz_id = biz_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        return self


class DescribeAdminTrademarkApplicationResponseBodyApplicant(TeaModel):
    def __init__(
        self,
        address: str = None,
        applicant_name: str = None,
        applicant_region: int = None,
        applicant_type: int = None,
        audit_status: int = None,
        authorization_url: str = None,
        business_licence_url: str = None,
        card_number: str = None,
        contact_address: str = None,
        contact_email: str = None,
        contact_name: str = None,
        contact_number: str = None,
        contact_zipcode: str = None,
        country: str = None,
        eaddress: str = None,
        ename: str = None,
        id_card_url: str = None,
        legal_notice_url: str = None,
        passport_url: str = None,
        principal_name: int = None,
        province: str = None,
    ):
        self.address = address
        self.applicant_name = applicant_name
        self.applicant_region = applicant_region
        self.applicant_type = applicant_type
        self.audit_status = audit_status
        self.authorization_url = authorization_url
        self.business_licence_url = business_licence_url
        self.card_number = card_number
        self.contact_address = contact_address
        self.contact_email = contact_email
        self.contact_name = contact_name
        self.contact_number = contact_number
        self.contact_zipcode = contact_zipcode
        self.country = country
        self.eaddress = eaddress
        self.ename = ename
        self.id_card_url = id_card_url
        self.legal_notice_url = legal_notice_url
        self.passport_url = passport_url
        self.principal_name = principal_name
        self.province = province

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.applicant_name is not None:
            result['ApplicantName'] = self.applicant_name
        if self.applicant_region is not None:
            result['ApplicantRegion'] = self.applicant_region
        if self.applicant_type is not None:
            result['ApplicantType'] = self.applicant_type
        if self.audit_status is not None:
            result['AuditStatus'] = self.audit_status
        if self.authorization_url is not None:
            result['AuthorizationUrl'] = self.authorization_url
        if self.business_licence_url is not None:
            result['BusinessLicenceUrl'] = self.business_licence_url
        if self.card_number is not None:
            result['CardNumber'] = self.card_number
        if self.contact_address is not None:
            result['ContactAddress'] = self.contact_address
        if self.contact_email is not None:
            result['ContactEmail'] = self.contact_email
        if self.contact_name is not None:
            result['ContactName'] = self.contact_name
        if self.contact_number is not None:
            result['ContactNumber'] = self.contact_number
        if self.contact_zipcode is not None:
            result['ContactZipcode'] = self.contact_zipcode
        if self.country is not None:
            result['Country'] = self.country
        if self.eaddress is not None:
            result['EAddress'] = self.eaddress
        if self.ename is not None:
            result['EName'] = self.ename
        if self.id_card_url is not None:
            result['IdCardUrl'] = self.id_card_url
        if self.legal_notice_url is not None:
            result['LegalNoticeUrl'] = self.legal_notice_url
        if self.passport_url is not None:
            result['PassportUrl'] = self.passport_url
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name
        if self.province is not None:
            result['Province'] = self.province
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('ApplicantName') is not None:
            self.applicant_name = m.get('ApplicantName')
        if m.get('ApplicantRegion') is not None:
            self.applicant_region = m.get('ApplicantRegion')
        if m.get('ApplicantType') is not None:
            self.applicant_type = m.get('ApplicantType')
        if m.get('AuditStatus') is not None:
            self.audit_status = m.get('AuditStatus')
        if m.get('AuthorizationUrl') is not None:
            self.authorization_url = m.get('AuthorizationUrl')
        if m.get('BusinessLicenceUrl') is not None:
            self.business_licence_url = m.get('BusinessLicenceUrl')
        if m.get('CardNumber') is not None:
            self.card_number = m.get('CardNumber')
        if m.get('ContactAddress') is not None:
            self.contact_address = m.get('ContactAddress')
        if m.get('ContactEmail') is not None:
            self.contact_email = m.get('ContactEmail')
        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')
        if m.get('ContactNumber') is not None:
            self.contact_number = m.get('ContactNumber')
        if m.get('ContactZipcode') is not None:
            self.contact_zipcode = m.get('ContactZipcode')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('EAddress') is not None:
            self.eaddress = m.get('EAddress')
        if m.get('EName') is not None:
            self.ename = m.get('EName')
        if m.get('IdCardUrl') is not None:
            self.id_card_url = m.get('IdCardUrl')
        if m.get('LegalNoticeUrl') is not None:
            self.legal_notice_url = m.get('LegalNoticeUrl')
        if m.get('PassportUrl') is not None:
            self.passport_url = m.get('PassportUrl')
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        return self


class DescribeAdminTrademarkApplicationResponseBodyFirstClassification(TeaModel):
    def __init__(
        self,
        classification_code: str = None,
        classification_name: str = None,
    ):
        self.classification_code = classification_code
        self.classification_name = classification_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.classification_code is not None:
            result['ClassificationCode'] = self.classification_code
        if self.classification_name is not None:
            result['ClassificationName'] = self.classification_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClassificationCode') is not None:
            self.classification_code = m.get('ClassificationCode')
        if m.get('ClassificationName') is not None:
            self.classification_name = m.get('ClassificationName')
        return self


class DescribeAdminTrademarkApplicationResponseBodySupplements(TeaModel):
    def __init__(
        self,
        accept_expiration_date: int = None,
        accept_time: int = None,
        application_type: int = None,
        content: str = None,
        official_file: str = None,
        operate_time: int = None,
        order_id: str = None,
        sbj_expiration_date: int = None,
        send_time: int = None,
        serial_number: str = None,
        supplement_id: int = None,
        supplement_status: int = None,
        trademark_number: str = None,
        user_files: List[str] = None,
    ):
        self.accept_expiration_date = accept_expiration_date
        self.accept_time = accept_time
        self.application_type = application_type
        self.content = content
        self.official_file = official_file
        self.operate_time = operate_time
        self.order_id = order_id
        self.sbj_expiration_date = sbj_expiration_date
        self.send_time = send_time
        self.serial_number = serial_number
        self.supplement_id = supplement_id
        self.supplement_status = supplement_status
        self.trademark_number = trademark_number
        self.user_files = user_files

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_expiration_date is not None:
            result['AcceptExpirationDate'] = self.accept_expiration_date
        if self.accept_time is not None:
            result['AcceptTime'] = self.accept_time
        if self.application_type is not None:
            result['ApplicationType'] = self.application_type
        if self.content is not None:
            result['Content'] = self.content
        if self.official_file is not None:
            result['OfficialFile'] = self.official_file
        if self.operate_time is not None:
            result['OperateTime'] = self.operate_time
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.sbj_expiration_date is not None:
            result['SbjExpirationDate'] = self.sbj_expiration_date
        if self.send_time is not None:
            result['SendTime'] = self.send_time
        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number
        if self.supplement_id is not None:
            result['SupplementId'] = self.supplement_id
        if self.supplement_status is not None:
            result['SupplementStatus'] = self.supplement_status
        if self.trademark_number is not None:
            result['TrademarkNumber'] = self.trademark_number
        if self.user_files is not None:
            result['UserFiles'] = self.user_files
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptExpirationDate') is not None:
            self.accept_expiration_date = m.get('AcceptExpirationDate')
        if m.get('AcceptTime') is not None:
            self.accept_time = m.get('AcceptTime')
        if m.get('ApplicationType') is not None:
            self.application_type = m.get('ApplicationType')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('OfficialFile') is not None:
            self.official_file = m.get('OfficialFile')
        if m.get('OperateTime') is not None:
            self.operate_time = m.get('OperateTime')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('SbjExpirationDate') is not None:
            self.sbj_expiration_date = m.get('SbjExpirationDate')
        if m.get('SendTime') is not None:
            self.send_time = m.get('SendTime')
        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')
        if m.get('SupplementId') is not None:
            self.supplement_id = m.get('SupplementId')
        if m.get('SupplementStatus') is not None:
            self.supplement_status = m.get('SupplementStatus')
        if m.get('TrademarkNumber') is not None:
            self.trademark_number = m.get('TrademarkNumber')
        if m.get('UserFiles') is not None:
            self.user_files = m.get('UserFiles')
        return self


class DescribeAdminTrademarkApplicationResponseBodyThirdClassifications(TeaModel):
    def __init__(
        self,
        classification_code: str = None,
        classification_name: str = None,
    ):
        self.classification_code = classification_code
        self.classification_name = classification_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.classification_code is not None:
            result['ClassificationCode'] = self.classification_code
        if self.classification_name is not None:
            result['ClassificationName'] = self.classification_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClassificationCode') is not None:
            self.classification_code = m.get('ClassificationCode')
        if m.get('ClassificationName') is not None:
            self.classification_name = m.get('ClassificationName')
        return self


class DescribeAdminTrademarkApplicationResponseBody(TeaModel):
    def __init__(
        self,
        accept_url: str = None,
        applicant: DescribeAdminTrademarkApplicationResponseBodyApplicant = None,
        applicant_id: int = None,
        application_status: int = None,
        application_type: int = None,
        authorization_url: str = None,
        biz_id: str = None,
        black_and_white_icon_url: str = None,
        create_time: int = None,
        extend_info: Dict[str, Any] = None,
        first_classification: DescribeAdminTrademarkApplicationResponseBodyFirstClassification = None,
        judge_result_urls: List[str] = None,
        note: str = None,
        order_id: str = None,
        order_price: float = None,
        principal_name: int = None,
        receipt_urls: List[str] = None,
        recv_user_logistics: str = None,
        request_id: str = None,
        send_sbj_logistics: str = None,
        send_user_logistics: str = None,
        service_price: float = None,
        supplements: List[DescribeAdminTrademarkApplicationResponseBodySupplements] = None,
        third_classifications: List[DescribeAdminTrademarkApplicationResponseBodyThirdClassifications] = None,
        total_price: float = None,
        trademark_icon: str = None,
        trademark_name: str = None,
        trademark_name_type: int = None,
        trademark_number: str = None,
        update_time: int = None,
        user_id: str = None,
    ):
        self.accept_url = accept_url
        self.applicant = applicant
        self.applicant_id = applicant_id
        self.application_status = application_status
        self.application_type = application_type
        self.authorization_url = authorization_url
        self.biz_id = biz_id
        self.black_and_white_icon_url = black_and_white_icon_url
        self.create_time = create_time
        self.extend_info = extend_info
        self.first_classification = first_classification
        self.judge_result_urls = judge_result_urls
        self.note = note
        self.order_id = order_id
        self.order_price = order_price
        self.principal_name = principal_name
        self.receipt_urls = receipt_urls
        self.recv_user_logistics = recv_user_logistics
        self.request_id = request_id
        self.send_sbj_logistics = send_sbj_logistics
        self.send_user_logistics = send_user_logistics
        self.service_price = service_price
        self.supplements = supplements
        self.third_classifications = third_classifications
        self.total_price = total_price
        self.trademark_icon = trademark_icon
        self.trademark_name = trademark_name
        self.trademark_name_type = trademark_name_type
        self.trademark_number = trademark_number
        self.update_time = update_time
        self.user_id = user_id

    def validate(self):
        if self.applicant:
            self.applicant.validate()
        if self.first_classification:
            self.first_classification.validate()
        if self.supplements:
            for k in self.supplements:
                if k:
                    k.validate()
        if self.third_classifications:
            for k in self.third_classifications:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_url is not None:
            result['AcceptUrl'] = self.accept_url
        if self.applicant is not None:
            result['Applicant'] = self.applicant.to_map()
        if self.applicant_id is not None:
            result['ApplicantId'] = self.applicant_id
        if self.application_status is not None:
            result['ApplicationStatus'] = self.application_status
        if self.application_type is not None:
            result['ApplicationType'] = self.application_type
        if self.authorization_url is not None:
            result['AuthorizationUrl'] = self.authorization_url
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.black_and_white_icon_url is not None:
            result['BlackAndWhiteIconUrl'] = self.black_and_white_icon_url
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.extend_info is not None:
            result['ExtendInfo'] = self.extend_info
        if self.first_classification is not None:
            result['FirstClassification'] = self.first_classification.to_map()
        if self.judge_result_urls is not None:
            result['JudgeResultUrls'] = self.judge_result_urls
        if self.note is not None:
            result['Note'] = self.note
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.order_price is not None:
            result['OrderPrice'] = self.order_price
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name
        if self.receipt_urls is not None:
            result['ReceiptUrls'] = self.receipt_urls
        if self.recv_user_logistics is not None:
            result['RecvUserLogistics'] = self.recv_user_logistics
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.send_sbj_logistics is not None:
            result['SendSbjLogistics'] = self.send_sbj_logistics
        if self.send_user_logistics is not None:
            result['SendUserLogistics'] = self.send_user_logistics
        if self.service_price is not None:
            result['ServicePrice'] = self.service_price
        result['Supplements'] = []
        if self.supplements is not None:
            for k in self.supplements:
                result['Supplements'].append(k.to_map() if k else None)
        result['ThirdClassifications'] = []
        if self.third_classifications is not None:
            for k in self.third_classifications:
                result['ThirdClassifications'].append(k.to_map() if k else None)
        if self.total_price is not None:
            result['TotalPrice'] = self.total_price
        if self.trademark_icon is not None:
            result['TrademarkIcon'] = self.trademark_icon
        if self.trademark_name is not None:
            result['TrademarkName'] = self.trademark_name
        if self.trademark_name_type is not None:
            result['TrademarkNameType'] = self.trademark_name_type
        if self.trademark_number is not None:
            result['TrademarkNumber'] = self.trademark_number
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptUrl') is not None:
            self.accept_url = m.get('AcceptUrl')
        if m.get('Applicant') is not None:
            temp_model = DescribeAdminTrademarkApplicationResponseBodyApplicant()
            self.applicant = temp_model.from_map(m['Applicant'])
        if m.get('ApplicantId') is not None:
            self.applicant_id = m.get('ApplicantId')
        if m.get('ApplicationStatus') is not None:
            self.application_status = m.get('ApplicationStatus')
        if m.get('ApplicationType') is not None:
            self.application_type = m.get('ApplicationType')
        if m.get('AuthorizationUrl') is not None:
            self.authorization_url = m.get('AuthorizationUrl')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BlackAndWhiteIconUrl') is not None:
            self.black_and_white_icon_url = m.get('BlackAndWhiteIconUrl')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ExtendInfo') is not None:
            self.extend_info = m.get('ExtendInfo')
        if m.get('FirstClassification') is not None:
            temp_model = DescribeAdminTrademarkApplicationResponseBodyFirstClassification()
            self.first_classification = temp_model.from_map(m['FirstClassification'])
        if m.get('JudgeResultUrls') is not None:
            self.judge_result_urls = m.get('JudgeResultUrls')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('OrderPrice') is not None:
            self.order_price = m.get('OrderPrice')
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')
        if m.get('ReceiptUrls') is not None:
            self.receipt_urls = m.get('ReceiptUrls')
        if m.get('RecvUserLogistics') is not None:
            self.recv_user_logistics = m.get('RecvUserLogistics')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SendSbjLogistics') is not None:
            self.send_sbj_logistics = m.get('SendSbjLogistics')
        if m.get('SendUserLogistics') is not None:
            self.send_user_logistics = m.get('SendUserLogistics')
        if m.get('ServicePrice') is not None:
            self.service_price = m.get('ServicePrice')
        self.supplements = []
        if m.get('Supplements') is not None:
            for k in m.get('Supplements'):
                temp_model = DescribeAdminTrademarkApplicationResponseBodySupplements()
                self.supplements.append(temp_model.from_map(k))
        self.third_classifications = []
        if m.get('ThirdClassifications') is not None:
            for k in m.get('ThirdClassifications'):
                temp_model = DescribeAdminTrademarkApplicationResponseBodyThirdClassifications()
                self.third_classifications.append(temp_model.from_map(k))
        if m.get('TotalPrice') is not None:
            self.total_price = m.get('TotalPrice')
        if m.get('TrademarkIcon') is not None:
            self.trademark_icon = m.get('TrademarkIcon')
        if m.get('TrademarkName') is not None:
            self.trademark_name = m.get('TrademarkName')
        if m.get('TrademarkNameType') is not None:
            self.trademark_name_type = m.get('TrademarkNameType')
        if m.get('TrademarkNumber') is not None:
            self.trademark_number = m.get('TrademarkNumber')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class DescribeAdminTrademarkApplicationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAdminTrademarkApplicationResponseBody = None,
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
            temp_model = DescribeAdminTrademarkApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeApplicantRequest(TeaModel):
    def __init__(
        self,
        applicant_id: int = None,
    ):
        self.applicant_id = applicant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.applicant_id is not None:
            result['ApplicantId'] = self.applicant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicantId') is not None:
            self.applicant_id = m.get('ApplicantId')
        return self


class DescribeApplicantResponseBody(TeaModel):
    def __init__(
        self,
        address: str = None,
        applicant_id: int = None,
        applicant_name: str = None,
        applicant_region: int = None,
        applicant_type: int = None,
        applicant_version: str = None,
        audit_status: int = None,
        authorization_audit_status: int = None,
        authorization_url: str = None,
        business_licence_url: str = None,
        card_number: str = None,
        contact_address: str = None,
        contact_city: str = None,
        contact_county: str = None,
        contact_district: str = None,
        contact_email: str = None,
        contact_name: str = None,
        contact_number: str = None,
        contact_province: str = None,
        contact_zipcode: str = None,
        country: str = None,
        eaddress: str = None,
        ename: str = None,
        id_card_name: str = None,
        id_card_number: str = None,
        id_card_url: str = None,
        legal_notice_url: str = None,
        note: str = None,
        passport_url: str = None,
        personal_type: int = None,
        principal_name: int = None,
        province: str = None,
        request_id: str = None,
        valid_date: int = None,
    ):
        self.address = address
        self.applicant_id = applicant_id
        self.applicant_name = applicant_name
        self.applicant_region = applicant_region
        self.applicant_type = applicant_type
        self.applicant_version = applicant_version
        self.audit_status = audit_status
        self.authorization_audit_status = authorization_audit_status
        self.authorization_url = authorization_url
        self.business_licence_url = business_licence_url
        self.card_number = card_number
        self.contact_address = contact_address
        self.contact_city = contact_city
        self.contact_county = contact_county
        self.contact_district = contact_district
        self.contact_email = contact_email
        self.contact_name = contact_name
        self.contact_number = contact_number
        self.contact_province = contact_province
        self.contact_zipcode = contact_zipcode
        self.country = country
        self.eaddress = eaddress
        self.ename = ename
        self.id_card_name = id_card_name
        self.id_card_number = id_card_number
        self.id_card_url = id_card_url
        self.legal_notice_url = legal_notice_url
        self.note = note
        self.passport_url = passport_url
        self.personal_type = personal_type
        self.principal_name = principal_name
        self.province = province
        self.request_id = request_id
        self.valid_date = valid_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.applicant_id is not None:
            result['ApplicantId'] = self.applicant_id
        if self.applicant_name is not None:
            result['ApplicantName'] = self.applicant_name
        if self.applicant_region is not None:
            result['ApplicantRegion'] = self.applicant_region
        if self.applicant_type is not None:
            result['ApplicantType'] = self.applicant_type
        if self.applicant_version is not None:
            result['ApplicantVersion'] = self.applicant_version
        if self.audit_status is not None:
            result['AuditStatus'] = self.audit_status
        if self.authorization_audit_status is not None:
            result['AuthorizationAuditStatus'] = self.authorization_audit_status
        if self.authorization_url is not None:
            result['AuthorizationUrl'] = self.authorization_url
        if self.business_licence_url is not None:
            result['BusinessLicenceUrl'] = self.business_licence_url
        if self.card_number is not None:
            result['CardNumber'] = self.card_number
        if self.contact_address is not None:
            result['ContactAddress'] = self.contact_address
        if self.contact_city is not None:
            result['ContactCity'] = self.contact_city
        if self.contact_county is not None:
            result['ContactCounty'] = self.contact_county
        if self.contact_district is not None:
            result['ContactDistrict'] = self.contact_district
        if self.contact_email is not None:
            result['ContactEmail'] = self.contact_email
        if self.contact_name is not None:
            result['ContactName'] = self.contact_name
        if self.contact_number is not None:
            result['ContactNumber'] = self.contact_number
        if self.contact_province is not None:
            result['ContactProvince'] = self.contact_province
        if self.contact_zipcode is not None:
            result['ContactZipcode'] = self.contact_zipcode
        if self.country is not None:
            result['Country'] = self.country
        if self.eaddress is not None:
            result['EAddress'] = self.eaddress
        if self.ename is not None:
            result['EName'] = self.ename
        if self.id_card_name is not None:
            result['IdCardName'] = self.id_card_name
        if self.id_card_number is not None:
            result['IdCardNumber'] = self.id_card_number
        if self.id_card_url is not None:
            result['IdCardUrl'] = self.id_card_url
        if self.legal_notice_url is not None:
            result['LegalNoticeUrl'] = self.legal_notice_url
        if self.note is not None:
            result['Note'] = self.note
        if self.passport_url is not None:
            result['PassportUrl'] = self.passport_url
        if self.personal_type is not None:
            result['PersonalType'] = self.personal_type
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name
        if self.province is not None:
            result['Province'] = self.province
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.valid_date is not None:
            result['ValidDate'] = self.valid_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('ApplicantId') is not None:
            self.applicant_id = m.get('ApplicantId')
        if m.get('ApplicantName') is not None:
            self.applicant_name = m.get('ApplicantName')
        if m.get('ApplicantRegion') is not None:
            self.applicant_region = m.get('ApplicantRegion')
        if m.get('ApplicantType') is not None:
            self.applicant_type = m.get('ApplicantType')
        if m.get('ApplicantVersion') is not None:
            self.applicant_version = m.get('ApplicantVersion')
        if m.get('AuditStatus') is not None:
            self.audit_status = m.get('AuditStatus')
        if m.get('AuthorizationAuditStatus') is not None:
            self.authorization_audit_status = m.get('AuthorizationAuditStatus')
        if m.get('AuthorizationUrl') is not None:
            self.authorization_url = m.get('AuthorizationUrl')
        if m.get('BusinessLicenceUrl') is not None:
            self.business_licence_url = m.get('BusinessLicenceUrl')
        if m.get('CardNumber') is not None:
            self.card_number = m.get('CardNumber')
        if m.get('ContactAddress') is not None:
            self.contact_address = m.get('ContactAddress')
        if m.get('ContactCity') is not None:
            self.contact_city = m.get('ContactCity')
        if m.get('ContactCounty') is not None:
            self.contact_county = m.get('ContactCounty')
        if m.get('ContactDistrict') is not None:
            self.contact_district = m.get('ContactDistrict')
        if m.get('ContactEmail') is not None:
            self.contact_email = m.get('ContactEmail')
        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')
        if m.get('ContactNumber') is not None:
            self.contact_number = m.get('ContactNumber')
        if m.get('ContactProvince') is not None:
            self.contact_province = m.get('ContactProvince')
        if m.get('ContactZipcode') is not None:
            self.contact_zipcode = m.get('ContactZipcode')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('EAddress') is not None:
            self.eaddress = m.get('EAddress')
        if m.get('EName') is not None:
            self.ename = m.get('EName')
        if m.get('IdCardName') is not None:
            self.id_card_name = m.get('IdCardName')
        if m.get('IdCardNumber') is not None:
            self.id_card_number = m.get('IdCardNumber')
        if m.get('IdCardUrl') is not None:
            self.id_card_url = m.get('IdCardUrl')
        if m.get('LegalNoticeUrl') is not None:
            self.legal_notice_url = m.get('LegalNoticeUrl')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        if m.get('PassportUrl') is not None:
            self.passport_url = m.get('PassportUrl')
        if m.get('PersonalType') is not None:
            self.personal_type = m.get('PersonalType')
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ValidDate') is not None:
            self.valid_date = m.get('ValidDate')
        return self


class DescribeApplicantResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeApplicantResponseBody = None,
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
            temp_model = DescribeApplicantResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePartnerTrademarkApplicationRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
    ):
        self.biz_id = biz_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        return self


class DescribePartnerTrademarkApplicationResponseBodyApplicant(TeaModel):
    def __init__(
        self,
        address: str = None,
        applicant_name: str = None,
        applicant_region: int = None,
        applicant_type: int = None,
        audit_status: int = None,
        authorization_url: str = None,
        business_licence_url: str = None,
        card_number: str = None,
        contact_address: str = None,
        contact_email: str = None,
        contact_name: str = None,
        contact_number: str = None,
        contact_zipcode: str = None,
        country: str = None,
        eaddress: str = None,
        ename: str = None,
        id_card_url: str = None,
        legal_notice_url: str = None,
        passport_url: str = None,
        principal_name: int = None,
        province: str = None,
    ):
        self.address = address
        self.applicant_name = applicant_name
        self.applicant_region = applicant_region
        self.applicant_type = applicant_type
        self.audit_status = audit_status
        self.authorization_url = authorization_url
        self.business_licence_url = business_licence_url
        self.card_number = card_number
        self.contact_address = contact_address
        self.contact_email = contact_email
        self.contact_name = contact_name
        self.contact_number = contact_number
        self.contact_zipcode = contact_zipcode
        self.country = country
        self.eaddress = eaddress
        self.ename = ename
        self.id_card_url = id_card_url
        self.legal_notice_url = legal_notice_url
        self.passport_url = passport_url
        self.principal_name = principal_name
        self.province = province

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.applicant_name is not None:
            result['ApplicantName'] = self.applicant_name
        if self.applicant_region is not None:
            result['ApplicantRegion'] = self.applicant_region
        if self.applicant_type is not None:
            result['ApplicantType'] = self.applicant_type
        if self.audit_status is not None:
            result['AuditStatus'] = self.audit_status
        if self.authorization_url is not None:
            result['AuthorizationUrl'] = self.authorization_url
        if self.business_licence_url is not None:
            result['BusinessLicenceUrl'] = self.business_licence_url
        if self.card_number is not None:
            result['CardNumber'] = self.card_number
        if self.contact_address is not None:
            result['ContactAddress'] = self.contact_address
        if self.contact_email is not None:
            result['ContactEmail'] = self.contact_email
        if self.contact_name is not None:
            result['ContactName'] = self.contact_name
        if self.contact_number is not None:
            result['ContactNumber'] = self.contact_number
        if self.contact_zipcode is not None:
            result['ContactZipcode'] = self.contact_zipcode
        if self.country is not None:
            result['Country'] = self.country
        if self.eaddress is not None:
            result['EAddress'] = self.eaddress
        if self.ename is not None:
            result['EName'] = self.ename
        if self.id_card_url is not None:
            result['IdCardUrl'] = self.id_card_url
        if self.legal_notice_url is not None:
            result['LegalNoticeUrl'] = self.legal_notice_url
        if self.passport_url is not None:
            result['PassportUrl'] = self.passport_url
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name
        if self.province is not None:
            result['Province'] = self.province
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('ApplicantName') is not None:
            self.applicant_name = m.get('ApplicantName')
        if m.get('ApplicantRegion') is not None:
            self.applicant_region = m.get('ApplicantRegion')
        if m.get('ApplicantType') is not None:
            self.applicant_type = m.get('ApplicantType')
        if m.get('AuditStatus') is not None:
            self.audit_status = m.get('AuditStatus')
        if m.get('AuthorizationUrl') is not None:
            self.authorization_url = m.get('AuthorizationUrl')
        if m.get('BusinessLicenceUrl') is not None:
            self.business_licence_url = m.get('BusinessLicenceUrl')
        if m.get('CardNumber') is not None:
            self.card_number = m.get('CardNumber')
        if m.get('ContactAddress') is not None:
            self.contact_address = m.get('ContactAddress')
        if m.get('ContactEmail') is not None:
            self.contact_email = m.get('ContactEmail')
        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')
        if m.get('ContactNumber') is not None:
            self.contact_number = m.get('ContactNumber')
        if m.get('ContactZipcode') is not None:
            self.contact_zipcode = m.get('ContactZipcode')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('EAddress') is not None:
            self.eaddress = m.get('EAddress')
        if m.get('EName') is not None:
            self.ename = m.get('EName')
        if m.get('IdCardUrl') is not None:
            self.id_card_url = m.get('IdCardUrl')
        if m.get('LegalNoticeUrl') is not None:
            self.legal_notice_url = m.get('LegalNoticeUrl')
        if m.get('PassportUrl') is not None:
            self.passport_url = m.get('PassportUrl')
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        return self


class DescribePartnerTrademarkApplicationResponseBodyFirstClassification(TeaModel):
    def __init__(
        self,
        classification_code: str = None,
        classification_name: str = None,
    ):
        self.classification_code = classification_code
        self.classification_name = classification_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.classification_code is not None:
            result['ClassificationCode'] = self.classification_code
        if self.classification_name is not None:
            result['ClassificationName'] = self.classification_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClassificationCode') is not None:
            self.classification_code = m.get('ClassificationCode')
        if m.get('ClassificationName') is not None:
            self.classification_name = m.get('ClassificationName')
        return self


class DescribePartnerTrademarkApplicationResponseBodySupplements(TeaModel):
    def __init__(
        self,
        accept_expiration_date: int = None,
        accept_time: int = None,
        application_type: int = None,
        content: str = None,
        official_file: str = None,
        operate_time: int = None,
        order_id: str = None,
        sbj_expiration_date: int = None,
        send_time: int = None,
        serial_number: str = None,
        supplement_id: int = None,
        supplement_status: int = None,
        trademark_number: str = None,
        user_files: List[str] = None,
    ):
        self.accept_expiration_date = accept_expiration_date
        self.accept_time = accept_time
        self.application_type = application_type
        self.content = content
        self.official_file = official_file
        self.operate_time = operate_time
        self.order_id = order_id
        self.sbj_expiration_date = sbj_expiration_date
        self.send_time = send_time
        self.serial_number = serial_number
        self.supplement_id = supplement_id
        self.supplement_status = supplement_status
        self.trademark_number = trademark_number
        self.user_files = user_files

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_expiration_date is not None:
            result['AcceptExpirationDate'] = self.accept_expiration_date
        if self.accept_time is not None:
            result['AcceptTime'] = self.accept_time
        if self.application_type is not None:
            result['ApplicationType'] = self.application_type
        if self.content is not None:
            result['Content'] = self.content
        if self.official_file is not None:
            result['OfficialFile'] = self.official_file
        if self.operate_time is not None:
            result['OperateTime'] = self.operate_time
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.sbj_expiration_date is not None:
            result['SbjExpirationDate'] = self.sbj_expiration_date
        if self.send_time is not None:
            result['SendTime'] = self.send_time
        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number
        if self.supplement_id is not None:
            result['SupplementId'] = self.supplement_id
        if self.supplement_status is not None:
            result['SupplementStatus'] = self.supplement_status
        if self.trademark_number is not None:
            result['TrademarkNumber'] = self.trademark_number
        if self.user_files is not None:
            result['UserFiles'] = self.user_files
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptExpirationDate') is not None:
            self.accept_expiration_date = m.get('AcceptExpirationDate')
        if m.get('AcceptTime') is not None:
            self.accept_time = m.get('AcceptTime')
        if m.get('ApplicationType') is not None:
            self.application_type = m.get('ApplicationType')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('OfficialFile') is not None:
            self.official_file = m.get('OfficialFile')
        if m.get('OperateTime') is not None:
            self.operate_time = m.get('OperateTime')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('SbjExpirationDate') is not None:
            self.sbj_expiration_date = m.get('SbjExpirationDate')
        if m.get('SendTime') is not None:
            self.send_time = m.get('SendTime')
        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')
        if m.get('SupplementId') is not None:
            self.supplement_id = m.get('SupplementId')
        if m.get('SupplementStatus') is not None:
            self.supplement_status = m.get('SupplementStatus')
        if m.get('TrademarkNumber') is not None:
            self.trademark_number = m.get('TrademarkNumber')
        if m.get('UserFiles') is not None:
            self.user_files = m.get('UserFiles')
        return self


class DescribePartnerTrademarkApplicationResponseBodyThirdClassifications(TeaModel):
    def __init__(
        self,
        classification_code: str = None,
        classification_name: str = None,
    ):
        self.classification_code = classification_code
        self.classification_name = classification_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.classification_code is not None:
            result['ClassificationCode'] = self.classification_code
        if self.classification_name is not None:
            result['ClassificationName'] = self.classification_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClassificationCode') is not None:
            self.classification_code = m.get('ClassificationCode')
        if m.get('ClassificationName') is not None:
            self.classification_name = m.get('ClassificationName')
        return self


class DescribePartnerTrademarkApplicationResponseBody(TeaModel):
    def __init__(
        self,
        accept_url: str = None,
        applicant: DescribePartnerTrademarkApplicationResponseBodyApplicant = None,
        applicant_id: int = None,
        application_status: int = None,
        application_type: int = None,
        authorization_url: str = None,
        biz_id: str = None,
        black_and_white_icon_url: str = None,
        create_time: int = None,
        extend_info: Dict[str, Any] = None,
        first_classification: DescribePartnerTrademarkApplicationResponseBodyFirstClassification = None,
        judge_result_urls: List[str] = None,
        note: str = None,
        order_id: str = None,
        order_price: float = None,
        principal_name: int = None,
        receipt_urls: List[str] = None,
        recv_user_logistics: str = None,
        request_id: str = None,
        send_sbj_logistics: str = None,
        send_user_logistics: str = None,
        service_price: float = None,
        supplements: List[DescribePartnerTrademarkApplicationResponseBodySupplements] = None,
        third_classifications: List[DescribePartnerTrademarkApplicationResponseBodyThirdClassifications] = None,
        total_price: float = None,
        trademark_icon: str = None,
        trademark_name: str = None,
        trademark_name_type: int = None,
        trademark_number: str = None,
        update_time: int = None,
    ):
        self.accept_url = accept_url
        self.applicant = applicant
        self.applicant_id = applicant_id
        self.application_status = application_status
        self.application_type = application_type
        self.authorization_url = authorization_url
        self.biz_id = biz_id
        self.black_and_white_icon_url = black_and_white_icon_url
        self.create_time = create_time
        self.extend_info = extend_info
        self.first_classification = first_classification
        self.judge_result_urls = judge_result_urls
        self.note = note
        self.order_id = order_id
        self.order_price = order_price
        self.principal_name = principal_name
        self.receipt_urls = receipt_urls
        self.recv_user_logistics = recv_user_logistics
        self.request_id = request_id
        self.send_sbj_logistics = send_sbj_logistics
        self.send_user_logistics = send_user_logistics
        self.service_price = service_price
        self.supplements = supplements
        self.third_classifications = third_classifications
        self.total_price = total_price
        self.trademark_icon = trademark_icon
        self.trademark_name = trademark_name
        self.trademark_name_type = trademark_name_type
        self.trademark_number = trademark_number
        self.update_time = update_time

    def validate(self):
        if self.applicant:
            self.applicant.validate()
        if self.first_classification:
            self.first_classification.validate()
        if self.supplements:
            for k in self.supplements:
                if k:
                    k.validate()
        if self.third_classifications:
            for k in self.third_classifications:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_url is not None:
            result['AcceptUrl'] = self.accept_url
        if self.applicant is not None:
            result['Applicant'] = self.applicant.to_map()
        if self.applicant_id is not None:
            result['ApplicantId'] = self.applicant_id
        if self.application_status is not None:
            result['ApplicationStatus'] = self.application_status
        if self.application_type is not None:
            result['ApplicationType'] = self.application_type
        if self.authorization_url is not None:
            result['AuthorizationUrl'] = self.authorization_url
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.black_and_white_icon_url is not None:
            result['BlackAndWhiteIconUrl'] = self.black_and_white_icon_url
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.extend_info is not None:
            result['ExtendInfo'] = self.extend_info
        if self.first_classification is not None:
            result['FirstClassification'] = self.first_classification.to_map()
        if self.judge_result_urls is not None:
            result['JudgeResultUrls'] = self.judge_result_urls
        if self.note is not None:
            result['Note'] = self.note
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.order_price is not None:
            result['OrderPrice'] = self.order_price
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name
        if self.receipt_urls is not None:
            result['ReceiptUrls'] = self.receipt_urls
        if self.recv_user_logistics is not None:
            result['RecvUserLogistics'] = self.recv_user_logistics
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.send_sbj_logistics is not None:
            result['SendSbjLogistics'] = self.send_sbj_logistics
        if self.send_user_logistics is not None:
            result['SendUserLogistics'] = self.send_user_logistics
        if self.service_price is not None:
            result['ServicePrice'] = self.service_price
        result['Supplements'] = []
        if self.supplements is not None:
            for k in self.supplements:
                result['Supplements'].append(k.to_map() if k else None)
        result['ThirdClassifications'] = []
        if self.third_classifications is not None:
            for k in self.third_classifications:
                result['ThirdClassifications'].append(k.to_map() if k else None)
        if self.total_price is not None:
            result['TotalPrice'] = self.total_price
        if self.trademark_icon is not None:
            result['TrademarkIcon'] = self.trademark_icon
        if self.trademark_name is not None:
            result['TrademarkName'] = self.trademark_name
        if self.trademark_name_type is not None:
            result['TrademarkNameType'] = self.trademark_name_type
        if self.trademark_number is not None:
            result['TrademarkNumber'] = self.trademark_number
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptUrl') is not None:
            self.accept_url = m.get('AcceptUrl')
        if m.get('Applicant') is not None:
            temp_model = DescribePartnerTrademarkApplicationResponseBodyApplicant()
            self.applicant = temp_model.from_map(m['Applicant'])
        if m.get('ApplicantId') is not None:
            self.applicant_id = m.get('ApplicantId')
        if m.get('ApplicationStatus') is not None:
            self.application_status = m.get('ApplicationStatus')
        if m.get('ApplicationType') is not None:
            self.application_type = m.get('ApplicationType')
        if m.get('AuthorizationUrl') is not None:
            self.authorization_url = m.get('AuthorizationUrl')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BlackAndWhiteIconUrl') is not None:
            self.black_and_white_icon_url = m.get('BlackAndWhiteIconUrl')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ExtendInfo') is not None:
            self.extend_info = m.get('ExtendInfo')
        if m.get('FirstClassification') is not None:
            temp_model = DescribePartnerTrademarkApplicationResponseBodyFirstClassification()
            self.first_classification = temp_model.from_map(m['FirstClassification'])
        if m.get('JudgeResultUrls') is not None:
            self.judge_result_urls = m.get('JudgeResultUrls')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('OrderPrice') is not None:
            self.order_price = m.get('OrderPrice')
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')
        if m.get('ReceiptUrls') is not None:
            self.receipt_urls = m.get('ReceiptUrls')
        if m.get('RecvUserLogistics') is not None:
            self.recv_user_logistics = m.get('RecvUserLogistics')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SendSbjLogistics') is not None:
            self.send_sbj_logistics = m.get('SendSbjLogistics')
        if m.get('SendUserLogistics') is not None:
            self.send_user_logistics = m.get('SendUserLogistics')
        if m.get('ServicePrice') is not None:
            self.service_price = m.get('ServicePrice')
        self.supplements = []
        if m.get('Supplements') is not None:
            for k in m.get('Supplements'):
                temp_model = DescribePartnerTrademarkApplicationResponseBodySupplements()
                self.supplements.append(temp_model.from_map(k))
        self.third_classifications = []
        if m.get('ThirdClassifications') is not None:
            for k in m.get('ThirdClassifications'):
                temp_model = DescribePartnerTrademarkApplicationResponseBodyThirdClassifications()
                self.third_classifications.append(temp_model.from_map(k))
        if m.get('TotalPrice') is not None:
            self.total_price = m.get('TotalPrice')
        if m.get('TrademarkIcon') is not None:
            self.trademark_icon = m.get('TrademarkIcon')
        if m.get('TrademarkName') is not None:
            self.trademark_name = m.get('TrademarkName')
        if m.get('TrademarkNameType') is not None:
            self.trademark_name_type = m.get('TrademarkNameType')
        if m.get('TrademarkNumber') is not None:
            self.trademark_number = m.get('TrademarkNumber')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class DescribePartnerTrademarkApplicationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribePartnerTrademarkApplicationResponseBody = None,
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
            temp_model = DescribePartnerTrademarkApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeQualificationStatusRequest(TeaModel):
    def __init__(
        self,
        tb_uid: str = None,
    ):
        self.tb_uid = tb_uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tb_uid is not None:
            result['TbUid'] = self.tb_uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TbUid') is not None:
            self.tb_uid = m.get('TbUid')
        return self


class DescribeQualificationStatusResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.status = status
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
        if self.status is not None:
            result['Status'] = self.status
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
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeQualificationStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeQualificationStatusResponseBody = None,
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
            temp_model = DescribeQualificationStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSupplementRequest(TeaModel):
    def __init__(
        self,
        supplement_id: int = None,
    ):
        self.supplement_id = supplement_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.supplement_id is not None:
            result['SupplementId'] = self.supplement_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SupplementId') is not None:
            self.supplement_id = m.get('SupplementId')
        return self


class DescribeSupplementResponseBodyUserFiles(TeaModel):
    def __init__(
        self,
        user_file: List[str] = None,
    ):
        self.user_file = user_file

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_file is not None:
            result['UserFile'] = self.user_file
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserFile') is not None:
            self.user_file = m.get('UserFile')
        return self


class DescribeSupplementResponseBody(TeaModel):
    def __init__(
        self,
        accept_expiration_date: int = None,
        accept_time: int = None,
        application_type: int = None,
        content: str = None,
        official_file: str = None,
        operate_time: int = None,
        request_id: str = None,
        sbj_expiration_date: int = None,
        send_time: int = None,
        serial_number: str = None,
        supplement_id: int = None,
        supplement_status: int = None,
        trademark_number: str = None,
        user_files: DescribeSupplementResponseBodyUserFiles = None,
    ):
        self.accept_expiration_date = accept_expiration_date
        self.accept_time = accept_time
        self.application_type = application_type
        self.content = content
        self.official_file = official_file
        self.operate_time = operate_time
        self.request_id = request_id
        self.sbj_expiration_date = sbj_expiration_date
        self.send_time = send_time
        self.serial_number = serial_number
        self.supplement_id = supplement_id
        self.supplement_status = supplement_status
        self.trademark_number = trademark_number
        self.user_files = user_files

    def validate(self):
        if self.user_files:
            self.user_files.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_expiration_date is not None:
            result['AcceptExpirationDate'] = self.accept_expiration_date
        if self.accept_time is not None:
            result['AcceptTime'] = self.accept_time
        if self.application_type is not None:
            result['ApplicationType'] = self.application_type
        if self.content is not None:
            result['Content'] = self.content
        if self.official_file is not None:
            result['OfficialFile'] = self.official_file
        if self.operate_time is not None:
            result['OperateTime'] = self.operate_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sbj_expiration_date is not None:
            result['SbjExpirationDate'] = self.sbj_expiration_date
        if self.send_time is not None:
            result['SendTime'] = self.send_time
        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number
        if self.supplement_id is not None:
            result['SupplementId'] = self.supplement_id
        if self.supplement_status is not None:
            result['SupplementStatus'] = self.supplement_status
        if self.trademark_number is not None:
            result['TrademarkNumber'] = self.trademark_number
        if self.user_files is not None:
            result['UserFiles'] = self.user_files.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptExpirationDate') is not None:
            self.accept_expiration_date = m.get('AcceptExpirationDate')
        if m.get('AcceptTime') is not None:
            self.accept_time = m.get('AcceptTime')
        if m.get('ApplicationType') is not None:
            self.application_type = m.get('ApplicationType')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('OfficialFile') is not None:
            self.official_file = m.get('OfficialFile')
        if m.get('OperateTime') is not None:
            self.operate_time = m.get('OperateTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SbjExpirationDate') is not None:
            self.sbj_expiration_date = m.get('SbjExpirationDate')
        if m.get('SendTime') is not None:
            self.send_time = m.get('SendTime')
        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')
        if m.get('SupplementId') is not None:
            self.supplement_id = m.get('SupplementId')
        if m.get('SupplementStatus') is not None:
            self.supplement_status = m.get('SupplementStatus')
        if m.get('TrademarkNumber') is not None:
            self.trademark_number = m.get('TrademarkNumber')
        if m.get('UserFiles') is not None:
            temp_model = DescribeSupplementResponseBodyUserFiles()
            self.user_files = temp_model.from_map(m['UserFiles'])
        return self


class DescribeSupplementResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeSupplementResponseBody = None,
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
            temp_model = DescribeSupplementResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTrademarkApplicationRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
    ):
        self.biz_id = biz_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        return self


class DescribeTrademarkApplicationResponseBodyApplicant(TeaModel):
    def __init__(
        self,
        address: str = None,
        applicant_name: str = None,
        applicant_region: int = None,
        applicant_type: int = None,
        audit_status: int = None,
        authorization_url: str = None,
        business_licence_url: str = None,
        card_number: str = None,
        contact_address: str = None,
        contact_email: str = None,
        contact_name: str = None,
        contact_number: str = None,
        contact_zipcode: str = None,
        country: str = None,
        eaddress: str = None,
        ename: str = None,
        id_card_name: str = None,
        id_card_number: str = None,
        id_card_url: str = None,
        legal_notice_url: str = None,
        passport_url: str = None,
        personal_type: int = None,
        principal_name: int = None,
        province: str = None,
    ):
        self.address = address
        self.applicant_name = applicant_name
        self.applicant_region = applicant_region
        self.applicant_type = applicant_type
        self.audit_status = audit_status
        self.authorization_url = authorization_url
        self.business_licence_url = business_licence_url
        self.card_number = card_number
        self.contact_address = contact_address
        self.contact_email = contact_email
        self.contact_name = contact_name
        self.contact_number = contact_number
        self.contact_zipcode = contact_zipcode
        self.country = country
        self.eaddress = eaddress
        self.ename = ename
        self.id_card_name = id_card_name
        self.id_card_number = id_card_number
        self.id_card_url = id_card_url
        self.legal_notice_url = legal_notice_url
        self.passport_url = passport_url
        self.personal_type = personal_type
        self.principal_name = principal_name
        self.province = province

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.applicant_name is not None:
            result['ApplicantName'] = self.applicant_name
        if self.applicant_region is not None:
            result['ApplicantRegion'] = self.applicant_region
        if self.applicant_type is not None:
            result['ApplicantType'] = self.applicant_type
        if self.audit_status is not None:
            result['AuditStatus'] = self.audit_status
        if self.authorization_url is not None:
            result['AuthorizationUrl'] = self.authorization_url
        if self.business_licence_url is not None:
            result['BusinessLicenceUrl'] = self.business_licence_url
        if self.card_number is not None:
            result['CardNumber'] = self.card_number
        if self.contact_address is not None:
            result['ContactAddress'] = self.contact_address
        if self.contact_email is not None:
            result['ContactEmail'] = self.contact_email
        if self.contact_name is not None:
            result['ContactName'] = self.contact_name
        if self.contact_number is not None:
            result['ContactNumber'] = self.contact_number
        if self.contact_zipcode is not None:
            result['ContactZipcode'] = self.contact_zipcode
        if self.country is not None:
            result['Country'] = self.country
        if self.eaddress is not None:
            result['EAddress'] = self.eaddress
        if self.ename is not None:
            result['EName'] = self.ename
        if self.id_card_name is not None:
            result['IdCardName'] = self.id_card_name
        if self.id_card_number is not None:
            result['IdCardNumber'] = self.id_card_number
        if self.id_card_url is not None:
            result['IdCardUrl'] = self.id_card_url
        if self.legal_notice_url is not None:
            result['LegalNoticeUrl'] = self.legal_notice_url
        if self.passport_url is not None:
            result['PassportUrl'] = self.passport_url
        if self.personal_type is not None:
            result['PersonalType'] = self.personal_type
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name
        if self.province is not None:
            result['Province'] = self.province
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('ApplicantName') is not None:
            self.applicant_name = m.get('ApplicantName')
        if m.get('ApplicantRegion') is not None:
            self.applicant_region = m.get('ApplicantRegion')
        if m.get('ApplicantType') is not None:
            self.applicant_type = m.get('ApplicantType')
        if m.get('AuditStatus') is not None:
            self.audit_status = m.get('AuditStatus')
        if m.get('AuthorizationUrl') is not None:
            self.authorization_url = m.get('AuthorizationUrl')
        if m.get('BusinessLicenceUrl') is not None:
            self.business_licence_url = m.get('BusinessLicenceUrl')
        if m.get('CardNumber') is not None:
            self.card_number = m.get('CardNumber')
        if m.get('ContactAddress') is not None:
            self.contact_address = m.get('ContactAddress')
        if m.get('ContactEmail') is not None:
            self.contact_email = m.get('ContactEmail')
        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')
        if m.get('ContactNumber') is not None:
            self.contact_number = m.get('ContactNumber')
        if m.get('ContactZipcode') is not None:
            self.contact_zipcode = m.get('ContactZipcode')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('EAddress') is not None:
            self.eaddress = m.get('EAddress')
        if m.get('EName') is not None:
            self.ename = m.get('EName')
        if m.get('IdCardName') is not None:
            self.id_card_name = m.get('IdCardName')
        if m.get('IdCardNumber') is not None:
            self.id_card_number = m.get('IdCardNumber')
        if m.get('IdCardUrl') is not None:
            self.id_card_url = m.get('IdCardUrl')
        if m.get('LegalNoticeUrl') is not None:
            self.legal_notice_url = m.get('LegalNoticeUrl')
        if m.get('PassportUrl') is not None:
            self.passport_url = m.get('PassportUrl')
        if m.get('PersonalType') is not None:
            self.personal_type = m.get('PersonalType')
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        return self


class DescribeTrademarkApplicationResponseBodyFirstClassification(TeaModel):
    def __init__(
        self,
        classification_code: str = None,
        classification_name: str = None,
    ):
        self.classification_code = classification_code
        self.classification_name = classification_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.classification_code is not None:
            result['ClassificationCode'] = self.classification_code
        if self.classification_name is not None:
            result['ClassificationName'] = self.classification_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClassificationCode') is not None:
            self.classification_code = m.get('ClassificationCode')
        if m.get('ClassificationName') is not None:
            self.classification_name = m.get('ClassificationName')
        return self


class DescribeTrademarkApplicationResponseBodyFlags(TeaModel):
    def __init__(
        self,
        flag: List[int] = None,
    ):
        self.flag = flag

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flag is not None:
            result['Flag'] = self.flag
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Flag') is not None:
            self.flag = m.get('Flag')
        return self


class DescribeTrademarkApplicationResponseBodyJudgeResultUrls(TeaModel):
    def __init__(
        self,
        judge_result_url: List[str] = None,
    ):
        self.judge_result_url = judge_result_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.judge_result_url is not None:
            result['JudgeResultUrl'] = self.judge_result_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JudgeResultUrl') is not None:
            self.judge_result_url = m.get('JudgeResultUrl')
        return self


class DescribeTrademarkApplicationResponseBodyReceiptUrls(TeaModel):
    def __init__(
        self,
        receipt_url: List[str] = None,
    ):
        self.receipt_url = receipt_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.receipt_url is not None:
            result['ReceiptUrl'] = self.receipt_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReceiptUrl') is not None:
            self.receipt_url = m.get('ReceiptUrl')
        return self


class DescribeTrademarkApplicationResponseBodySupplementsSupplementUserFiles(TeaModel):
    def __init__(
        self,
        user_file: List[str] = None,
    ):
        self.user_file = user_file

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_file is not None:
            result['UserFile'] = self.user_file
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserFile') is not None:
            self.user_file = m.get('UserFile')
        return self


class DescribeTrademarkApplicationResponseBodySupplementsSupplement(TeaModel):
    def __init__(
        self,
        accept_expiration_date: int = None,
        accept_time: int = None,
        application_type: int = None,
        content: str = None,
        official_file: str = None,
        operate_time: int = None,
        order_id: str = None,
        sbj_expiration_date: int = None,
        send_time: int = None,
        serial_number: str = None,
        supplement_id: int = None,
        supplement_status: int = None,
        trademark_number: str = None,
        user_files: DescribeTrademarkApplicationResponseBodySupplementsSupplementUserFiles = None,
    ):
        self.accept_expiration_date = accept_expiration_date
        self.accept_time = accept_time
        self.application_type = application_type
        self.content = content
        self.official_file = official_file
        self.operate_time = operate_time
        self.order_id = order_id
        self.sbj_expiration_date = sbj_expiration_date
        self.send_time = send_time
        self.serial_number = serial_number
        self.supplement_id = supplement_id
        self.supplement_status = supplement_status
        self.trademark_number = trademark_number
        self.user_files = user_files

    def validate(self):
        if self.user_files:
            self.user_files.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_expiration_date is not None:
            result['AcceptExpirationDate'] = self.accept_expiration_date
        if self.accept_time is not None:
            result['AcceptTime'] = self.accept_time
        if self.application_type is not None:
            result['ApplicationType'] = self.application_type
        if self.content is not None:
            result['Content'] = self.content
        if self.official_file is not None:
            result['OfficialFile'] = self.official_file
        if self.operate_time is not None:
            result['OperateTime'] = self.operate_time
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.sbj_expiration_date is not None:
            result['SbjExpirationDate'] = self.sbj_expiration_date
        if self.send_time is not None:
            result['SendTime'] = self.send_time
        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number
        if self.supplement_id is not None:
            result['SupplementId'] = self.supplement_id
        if self.supplement_status is not None:
            result['SupplementStatus'] = self.supplement_status
        if self.trademark_number is not None:
            result['TrademarkNumber'] = self.trademark_number
        if self.user_files is not None:
            result['UserFiles'] = self.user_files.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptExpirationDate') is not None:
            self.accept_expiration_date = m.get('AcceptExpirationDate')
        if m.get('AcceptTime') is not None:
            self.accept_time = m.get('AcceptTime')
        if m.get('ApplicationType') is not None:
            self.application_type = m.get('ApplicationType')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('OfficialFile') is not None:
            self.official_file = m.get('OfficialFile')
        if m.get('OperateTime') is not None:
            self.operate_time = m.get('OperateTime')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('SbjExpirationDate') is not None:
            self.sbj_expiration_date = m.get('SbjExpirationDate')
        if m.get('SendTime') is not None:
            self.send_time = m.get('SendTime')
        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')
        if m.get('SupplementId') is not None:
            self.supplement_id = m.get('SupplementId')
        if m.get('SupplementStatus') is not None:
            self.supplement_status = m.get('SupplementStatus')
        if m.get('TrademarkNumber') is not None:
            self.trademark_number = m.get('TrademarkNumber')
        if m.get('UserFiles') is not None:
            temp_model = DescribeTrademarkApplicationResponseBodySupplementsSupplementUserFiles()
            self.user_files = temp_model.from_map(m['UserFiles'])
        return self


class DescribeTrademarkApplicationResponseBodySupplements(TeaModel):
    def __init__(
        self,
        supplement: List[DescribeTrademarkApplicationResponseBodySupplementsSupplement] = None,
    ):
        self.supplement = supplement

    def validate(self):
        if self.supplement:
            for k in self.supplement:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Supplement'] = []
        if self.supplement is not None:
            for k in self.supplement:
                result['Supplement'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.supplement = []
        if m.get('Supplement') is not None:
            for k in m.get('Supplement'):
                temp_model = DescribeTrademarkApplicationResponseBodySupplementsSupplement()
                self.supplement.append(temp_model.from_map(k))
        return self


class DescribeTrademarkApplicationResponseBodyThirdClassificationsThirdClassification(TeaModel):
    def __init__(
        self,
        classification_code: str = None,
        classification_name: str = None,
    ):
        self.classification_code = classification_code
        self.classification_name = classification_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.classification_code is not None:
            result['ClassificationCode'] = self.classification_code
        if self.classification_name is not None:
            result['ClassificationName'] = self.classification_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClassificationCode') is not None:
            self.classification_code = m.get('ClassificationCode')
        if m.get('ClassificationName') is not None:
            self.classification_name = m.get('ClassificationName')
        return self


class DescribeTrademarkApplicationResponseBodyThirdClassifications(TeaModel):
    def __init__(
        self,
        third_classification: List[DescribeTrademarkApplicationResponseBodyThirdClassificationsThirdClassification] = None,
    ):
        self.third_classification = third_classification

    def validate(self):
        if self.third_classification:
            for k in self.third_classification:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ThirdClassification'] = []
        if self.third_classification is not None:
            for k in self.third_classification:
                result['ThirdClassification'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.third_classification = []
        if m.get('ThirdClassification') is not None:
            for k in m.get('ThirdClassification'):
                temp_model = DescribeTrademarkApplicationResponseBodyThirdClassificationsThirdClassification()
                self.third_classification.append(temp_model.from_map(k))
        return self


class DescribeTrademarkApplicationResponseBody(TeaModel):
    def __init__(
        self,
        accept_url: str = None,
        agreement_id: str = None,
        applicant: DescribeTrademarkApplicationResponseBodyApplicant = None,
        applicant_id: int = None,
        application_status: int = None,
        application_type: int = None,
        authorization_url: str = None,
        biz_id: str = None,
        black_and_white_icon_url: str = None,
        create_time: int = None,
        extend_info: Dict[str, Any] = None,
        first_classification: DescribeTrademarkApplicationResponseBodyFirstClassification = None,
        flags: DescribeTrademarkApplicationResponseBodyFlags = None,
        judge_result_urls: DescribeTrademarkApplicationResponseBodyJudgeResultUrls = None,
        note: str = None,
        order_id: str = None,
        order_price: float = None,
        principal_name: int = None,
        receipt_urls: DescribeTrademarkApplicationResponseBodyReceiptUrls = None,
        recv_user_logistics: str = None,
        request_id: str = None,
        send_sbj_logistics: str = None,
        send_user_logistics: str = None,
        service_price: float = None,
        supplements: DescribeTrademarkApplicationResponseBodySupplements = None,
        third_classifications: DescribeTrademarkApplicationResponseBodyThirdClassifications = None,
        total_price: float = None,
        trademark_icon: str = None,
        trademark_name: str = None,
        trademark_name_type: int = None,
        trademark_number: str = None,
        update_time: int = None,
    ):
        self.accept_url = accept_url
        self.agreement_id = agreement_id
        self.applicant = applicant
        self.applicant_id = applicant_id
        self.application_status = application_status
        self.application_type = application_type
        self.authorization_url = authorization_url
        self.biz_id = biz_id
        self.black_and_white_icon_url = black_and_white_icon_url
        self.create_time = create_time
        self.extend_info = extend_info
        self.first_classification = first_classification
        self.flags = flags
        self.judge_result_urls = judge_result_urls
        self.note = note
        self.order_id = order_id
        self.order_price = order_price
        self.principal_name = principal_name
        self.receipt_urls = receipt_urls
        self.recv_user_logistics = recv_user_logistics
        self.request_id = request_id
        self.send_sbj_logistics = send_sbj_logistics
        self.send_user_logistics = send_user_logistics
        self.service_price = service_price
        self.supplements = supplements
        self.third_classifications = third_classifications
        self.total_price = total_price
        self.trademark_icon = trademark_icon
        self.trademark_name = trademark_name
        self.trademark_name_type = trademark_name_type
        self.trademark_number = trademark_number
        self.update_time = update_time

    def validate(self):
        if self.applicant:
            self.applicant.validate()
        if self.first_classification:
            self.first_classification.validate()
        if self.flags:
            self.flags.validate()
        if self.judge_result_urls:
            self.judge_result_urls.validate()
        if self.receipt_urls:
            self.receipt_urls.validate()
        if self.supplements:
            self.supplements.validate()
        if self.third_classifications:
            self.third_classifications.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_url is not None:
            result['AcceptUrl'] = self.accept_url
        if self.agreement_id is not None:
            result['AgreementId'] = self.agreement_id
        if self.applicant is not None:
            result['Applicant'] = self.applicant.to_map()
        if self.applicant_id is not None:
            result['ApplicantId'] = self.applicant_id
        if self.application_status is not None:
            result['ApplicationStatus'] = self.application_status
        if self.application_type is not None:
            result['ApplicationType'] = self.application_type
        if self.authorization_url is not None:
            result['AuthorizationUrl'] = self.authorization_url
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.black_and_white_icon_url is not None:
            result['BlackAndWhiteIconUrl'] = self.black_and_white_icon_url
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.extend_info is not None:
            result['ExtendInfo'] = self.extend_info
        if self.first_classification is not None:
            result['FirstClassification'] = self.first_classification.to_map()
        if self.flags is not None:
            result['Flags'] = self.flags.to_map()
        if self.judge_result_urls is not None:
            result['JudgeResultUrls'] = self.judge_result_urls.to_map()
        if self.note is not None:
            result['Note'] = self.note
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.order_price is not None:
            result['OrderPrice'] = self.order_price
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name
        if self.receipt_urls is not None:
            result['ReceiptUrls'] = self.receipt_urls.to_map()
        if self.recv_user_logistics is not None:
            result['RecvUserLogistics'] = self.recv_user_logistics
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.send_sbj_logistics is not None:
            result['SendSbjLogistics'] = self.send_sbj_logistics
        if self.send_user_logistics is not None:
            result['SendUserLogistics'] = self.send_user_logistics
        if self.service_price is not None:
            result['ServicePrice'] = self.service_price
        if self.supplements is not None:
            result['Supplements'] = self.supplements.to_map()
        if self.third_classifications is not None:
            result['ThirdClassifications'] = self.third_classifications.to_map()
        if self.total_price is not None:
            result['TotalPrice'] = self.total_price
        if self.trademark_icon is not None:
            result['TrademarkIcon'] = self.trademark_icon
        if self.trademark_name is not None:
            result['TrademarkName'] = self.trademark_name
        if self.trademark_name_type is not None:
            result['TrademarkNameType'] = self.trademark_name_type
        if self.trademark_number is not None:
            result['TrademarkNumber'] = self.trademark_number
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptUrl') is not None:
            self.accept_url = m.get('AcceptUrl')
        if m.get('AgreementId') is not None:
            self.agreement_id = m.get('AgreementId')
        if m.get('Applicant') is not None:
            temp_model = DescribeTrademarkApplicationResponseBodyApplicant()
            self.applicant = temp_model.from_map(m['Applicant'])
        if m.get('ApplicantId') is not None:
            self.applicant_id = m.get('ApplicantId')
        if m.get('ApplicationStatus') is not None:
            self.application_status = m.get('ApplicationStatus')
        if m.get('ApplicationType') is not None:
            self.application_type = m.get('ApplicationType')
        if m.get('AuthorizationUrl') is not None:
            self.authorization_url = m.get('AuthorizationUrl')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BlackAndWhiteIconUrl') is not None:
            self.black_and_white_icon_url = m.get('BlackAndWhiteIconUrl')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ExtendInfo') is not None:
            self.extend_info = m.get('ExtendInfo')
        if m.get('FirstClassification') is not None:
            temp_model = DescribeTrademarkApplicationResponseBodyFirstClassification()
            self.first_classification = temp_model.from_map(m['FirstClassification'])
        if m.get('Flags') is not None:
            temp_model = DescribeTrademarkApplicationResponseBodyFlags()
            self.flags = temp_model.from_map(m['Flags'])
        if m.get('JudgeResultUrls') is not None:
            temp_model = DescribeTrademarkApplicationResponseBodyJudgeResultUrls()
            self.judge_result_urls = temp_model.from_map(m['JudgeResultUrls'])
        if m.get('Note') is not None:
            self.note = m.get('Note')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('OrderPrice') is not None:
            self.order_price = m.get('OrderPrice')
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')
        if m.get('ReceiptUrls') is not None:
            temp_model = DescribeTrademarkApplicationResponseBodyReceiptUrls()
            self.receipt_urls = temp_model.from_map(m['ReceiptUrls'])
        if m.get('RecvUserLogistics') is not None:
            self.recv_user_logistics = m.get('RecvUserLogistics')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SendSbjLogistics') is not None:
            self.send_sbj_logistics = m.get('SendSbjLogistics')
        if m.get('SendUserLogistics') is not None:
            self.send_user_logistics = m.get('SendUserLogistics')
        if m.get('ServicePrice') is not None:
            self.service_price = m.get('ServicePrice')
        if m.get('Supplements') is not None:
            temp_model = DescribeTrademarkApplicationResponseBodySupplements()
            self.supplements = temp_model.from_map(m['Supplements'])
        if m.get('ThirdClassifications') is not None:
            temp_model = DescribeTrademarkApplicationResponseBodyThirdClassifications()
            self.third_classifications = temp_model.from_map(m['ThirdClassifications'])
        if m.get('TotalPrice') is not None:
            self.total_price = m.get('TotalPrice')
        if m.get('TrademarkIcon') is not None:
            self.trademark_icon = m.get('TrademarkIcon')
        if m.get('TrademarkName') is not None:
            self.trademark_name = m.get('TrademarkName')
        if m.get('TrademarkNameType') is not None:
            self.trademark_name_type = m.get('TrademarkNameType')
        if m.get('TrademarkNumber') is not None:
            self.trademark_number = m.get('TrademarkNumber')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class DescribeTrademarkApplicationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeTrademarkApplicationResponseBody = None,
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
            temp_model = DescribeTrademarkApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTrademarkDetailForInnerRequest(TeaModel):
    def __init__(
        self,
        uid: str = None,
        umid: str = None,
    ):
        self.uid = uid
        self.umid = umid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.uid is not None:
            result['Uid'] = self.uid
        if self.umid is not None:
            result['Umid'] = self.umid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        if m.get('Umid') is not None:
            self.umid = m.get('Umid')
        return self


class DescribeTrademarkDetailForInnerResponseBodyFlowList(TeaModel):
    def __init__(
        self,
        date: str = None,
        procedure_code: str = None,
        procedure_date: str = None,
        procedure_name: str = None,
        procedure_result: str = None,
        procedure_step: str = None,
        registration_number: str = None,
    ):
        self.date = date
        self.procedure_code = procedure_code
        self.procedure_date = procedure_date
        self.procedure_name = procedure_name
        self.procedure_result = procedure_result
        self.procedure_step = procedure_step
        self.registration_number = registration_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.date is not None:
            result['Date'] = self.date
        if self.procedure_code is not None:
            result['ProcedureCode'] = self.procedure_code
        if self.procedure_date is not None:
            result['ProcedureDate'] = self.procedure_date
        if self.procedure_name is not None:
            result['ProcedureName'] = self.procedure_name
        if self.procedure_result is not None:
            result['ProcedureResult'] = self.procedure_result
        if self.procedure_step is not None:
            result['ProcedureStep'] = self.procedure_step
        if self.registration_number is not None:
            result['RegistrationNumber'] = self.registration_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Date') is not None:
            self.date = m.get('Date')
        if m.get('ProcedureCode') is not None:
            self.procedure_code = m.get('ProcedureCode')
        if m.get('ProcedureDate') is not None:
            self.procedure_date = m.get('ProcedureDate')
        if m.get('ProcedureName') is not None:
            self.procedure_name = m.get('ProcedureName')
        if m.get('ProcedureResult') is not None:
            self.procedure_result = m.get('ProcedureResult')
        if m.get('ProcedureStep') is not None:
            self.procedure_step = m.get('ProcedureStep')
        if m.get('RegistrationNumber') is not None:
            self.registration_number = m.get('RegistrationNumber')
        return self


class DescribeTrademarkDetailForInnerResponseBodyNoticeList(TeaModel):
    def __init__(
        self,
        ann_date: str = None,
        ann_id: str = None,
        ann_num: str = None,
        ann_type_code: str = None,
        ann_type_name: str = None,
        applicant: str = None,
        date: str = None,
        image_url: str = None,
        original_image_url: str = None,
        page_no: str = None,
        react_num: str = None,
        registration_number: str = None,
        trademark_name: str = None,
    ):
        self.ann_date = ann_date
        self.ann_id = ann_id
        self.ann_num = ann_num
        self.ann_type_code = ann_type_code
        self.ann_type_name = ann_type_name
        self.applicant = applicant
        self.date = date
        self.image_url = image_url
        self.original_image_url = original_image_url
        self.page_no = page_no
        self.react_num = react_num
        self.registration_number = registration_number
        self.trademark_name = trademark_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ann_date is not None:
            result['AnnDate'] = self.ann_date
        if self.ann_id is not None:
            result['AnnId'] = self.ann_id
        if self.ann_num is not None:
            result['AnnNum'] = self.ann_num
        if self.ann_type_code is not None:
            result['AnnTypeCode'] = self.ann_type_code
        if self.ann_type_name is not None:
            result['AnnTypeName'] = self.ann_type_name
        if self.applicant is not None:
            result['Applicant'] = self.applicant
        if self.date is not None:
            result['Date'] = self.date
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.original_image_url is not None:
            result['OriginalImageUrl'] = self.original_image_url
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.react_num is not None:
            result['ReactNum'] = self.react_num
        if self.registration_number is not None:
            result['RegistrationNumber'] = self.registration_number
        if self.trademark_name is not None:
            result['TrademarkName'] = self.trademark_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AnnDate') is not None:
            self.ann_date = m.get('AnnDate')
        if m.get('AnnId') is not None:
            self.ann_id = m.get('AnnId')
        if m.get('AnnNum') is not None:
            self.ann_num = m.get('AnnNum')
        if m.get('AnnTypeCode') is not None:
            self.ann_type_code = m.get('AnnTypeCode')
        if m.get('AnnTypeName') is not None:
            self.ann_type_name = m.get('AnnTypeName')
        if m.get('Applicant') is not None:
            self.applicant = m.get('Applicant')
        if m.get('Date') is not None:
            self.date = m.get('Date')
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('OriginalImageUrl') is not None:
            self.original_image_url = m.get('OriginalImageUrl')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('ReactNum') is not None:
            self.react_num = m.get('ReactNum')
        if m.get('RegistrationNumber') is not None:
            self.registration_number = m.get('RegistrationNumber')
        if m.get('TrademarkName') is not None:
            self.trademark_name = m.get('TrademarkName')
        return self


class DescribeTrademarkDetailForInnerResponseBody(TeaModel):
    def __init__(
        self,
        agency: str = None,
        apply_date: str = None,
        classification: str = None,
        exclusive_date_limit: str = None,
        flow_list: List[DescribeTrademarkDetailForInnerResponseBodyFlowList] = None,
        image: str = None,
        image_element: str = None,
        intl_reg_date: str = None,
        last_procedure_status: str = None,
        name: str = None,
        notice_list: List[DescribeTrademarkDetailForInnerResponseBodyNoticeList] = None,
        owner_address: str = None,
        owner_en_address: str = None,
        owner_en_name: str = None,
        owner_name: str = None,
        pre_ann_date: str = None,
        pre_ann_num: str = None,
        priority_date: str = None,
        product: str = None,
        product_description: str = None,
        reg_ann_date: str = None,
        reg_ann_num: int = None,
        registration_number: str = None,
        registration_type: str = None,
        request_id: str = None,
        share: str = None,
        similar_group: str = None,
        status: str = None,
        subsequent_designation_date: str = None,
        uid: str = None,
    ):
        self.agency = agency
        self.apply_date = apply_date
        self.classification = classification
        self.exclusive_date_limit = exclusive_date_limit
        self.flow_list = flow_list
        self.image = image
        self.image_element = image_element
        self.intl_reg_date = intl_reg_date
        self.last_procedure_status = last_procedure_status
        self.name = name
        self.notice_list = notice_list
        self.owner_address = owner_address
        self.owner_en_address = owner_en_address
        self.owner_en_name = owner_en_name
        self.owner_name = owner_name
        self.pre_ann_date = pre_ann_date
        self.pre_ann_num = pre_ann_num
        self.priority_date = priority_date
        self.product = product
        self.product_description = product_description
        self.reg_ann_date = reg_ann_date
        self.reg_ann_num = reg_ann_num
        self.registration_number = registration_number
        self.registration_type = registration_type
        self.request_id = request_id
        self.share = share
        self.similar_group = similar_group
        self.status = status
        self.subsequent_designation_date = subsequent_designation_date
        self.uid = uid

    def validate(self):
        if self.flow_list:
            for k in self.flow_list:
                if k:
                    k.validate()
        if self.notice_list:
            for k in self.notice_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agency is not None:
            result['Agency'] = self.agency
        if self.apply_date is not None:
            result['ApplyDate'] = self.apply_date
        if self.classification is not None:
            result['Classification'] = self.classification
        if self.exclusive_date_limit is not None:
            result['ExclusiveDateLimit'] = self.exclusive_date_limit
        result['FlowList'] = []
        if self.flow_list is not None:
            for k in self.flow_list:
                result['FlowList'].append(k.to_map() if k else None)
        if self.image is not None:
            result['Image'] = self.image
        if self.image_element is not None:
            result['ImageElement'] = self.image_element
        if self.intl_reg_date is not None:
            result['IntlRegDate'] = self.intl_reg_date
        if self.last_procedure_status is not None:
            result['LastProcedureStatus'] = self.last_procedure_status
        if self.name is not None:
            result['Name'] = self.name
        result['NoticeList'] = []
        if self.notice_list is not None:
            for k in self.notice_list:
                result['NoticeList'].append(k.to_map() if k else None)
        if self.owner_address is not None:
            result['OwnerAddress'] = self.owner_address
        if self.owner_en_address is not None:
            result['OwnerEnAddress'] = self.owner_en_address
        if self.owner_en_name is not None:
            result['OwnerEnName'] = self.owner_en_name
        if self.owner_name is not None:
            result['OwnerName'] = self.owner_name
        if self.pre_ann_date is not None:
            result['PreAnnDate'] = self.pre_ann_date
        if self.pre_ann_num is not None:
            result['PreAnnNum'] = self.pre_ann_num
        if self.priority_date is not None:
            result['PriorityDate'] = self.priority_date
        if self.product is not None:
            result['Product'] = self.product
        if self.product_description is not None:
            result['ProductDescription'] = self.product_description
        if self.reg_ann_date is not None:
            result['RegAnnDate'] = self.reg_ann_date
        if self.reg_ann_num is not None:
            result['RegAnnNum'] = self.reg_ann_num
        if self.registration_number is not None:
            result['RegistrationNumber'] = self.registration_number
        if self.registration_type is not None:
            result['RegistrationType'] = self.registration_type
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.share is not None:
            result['Share'] = self.share
        if self.similar_group is not None:
            result['SimilarGroup'] = self.similar_group
        if self.status is not None:
            result['Status'] = self.status
        if self.subsequent_designation_date is not None:
            result['SubsequentDesignationDate'] = self.subsequent_designation_date
        if self.uid is not None:
            result['Uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Agency') is not None:
            self.agency = m.get('Agency')
        if m.get('ApplyDate') is not None:
            self.apply_date = m.get('ApplyDate')
        if m.get('Classification') is not None:
            self.classification = m.get('Classification')
        if m.get('ExclusiveDateLimit') is not None:
            self.exclusive_date_limit = m.get('ExclusiveDateLimit')
        self.flow_list = []
        if m.get('FlowList') is not None:
            for k in m.get('FlowList'):
                temp_model = DescribeTrademarkDetailForInnerResponseBodyFlowList()
                self.flow_list.append(temp_model.from_map(k))
        if m.get('Image') is not None:
            self.image = m.get('Image')
        if m.get('ImageElement') is not None:
            self.image_element = m.get('ImageElement')
        if m.get('IntlRegDate') is not None:
            self.intl_reg_date = m.get('IntlRegDate')
        if m.get('LastProcedureStatus') is not None:
            self.last_procedure_status = m.get('LastProcedureStatus')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.notice_list = []
        if m.get('NoticeList') is not None:
            for k in m.get('NoticeList'):
                temp_model = DescribeTrademarkDetailForInnerResponseBodyNoticeList()
                self.notice_list.append(temp_model.from_map(k))
        if m.get('OwnerAddress') is not None:
            self.owner_address = m.get('OwnerAddress')
        if m.get('OwnerEnAddress') is not None:
            self.owner_en_address = m.get('OwnerEnAddress')
        if m.get('OwnerEnName') is not None:
            self.owner_en_name = m.get('OwnerEnName')
        if m.get('OwnerName') is not None:
            self.owner_name = m.get('OwnerName')
        if m.get('PreAnnDate') is not None:
            self.pre_ann_date = m.get('PreAnnDate')
        if m.get('PreAnnNum') is not None:
            self.pre_ann_num = m.get('PreAnnNum')
        if m.get('PriorityDate') is not None:
            self.priority_date = m.get('PriorityDate')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('ProductDescription') is not None:
            self.product_description = m.get('ProductDescription')
        if m.get('RegAnnDate') is not None:
            self.reg_ann_date = m.get('RegAnnDate')
        if m.get('RegAnnNum') is not None:
            self.reg_ann_num = m.get('RegAnnNum')
        if m.get('RegistrationNumber') is not None:
            self.registration_number = m.get('RegistrationNumber')
        if m.get('RegistrationType') is not None:
            self.registration_type = m.get('RegistrationType')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Share') is not None:
            self.share = m.get('Share')
        if m.get('SimilarGroup') is not None:
            self.similar_group = m.get('SimilarGroup')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubsequentDesignationDate') is not None:
            self.subsequent_designation_date = m.get('SubsequentDesignationDate')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        return self


class DescribeTrademarkDetailForInnerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeTrademarkDetailForInnerResponseBody = None,
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
            temp_model = DescribeTrademarkDetailForInnerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateUploadFilePolicyRequest(TeaModel):
    def __init__(
        self,
        file_type: str = None,
    ):
        self.file_type = file_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_type is not None:
            result['FileType'] = self.file_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')
        return self


class GenerateUploadFilePolicyResponseBody(TeaModel):
    def __init__(
        self,
        access_id: str = None,
        encoded_policy: str = None,
        expire_time: int = None,
        file_dir: str = None,
        host: str = None,
        request_id: str = None,
        signature: str = None,
    ):
        # OSSAccessKeyId
        self.access_id = access_id
        self.encoded_policy = encoded_policy
        self.expire_time = expire_time
        self.file_dir = file_dir
        # host
        self.host = host
        self.request_id = request_id
        self.signature = signature

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_id is not None:
            result['AccessId'] = self.access_id
        if self.encoded_policy is not None:
            result['EncodedPolicy'] = self.encoded_policy
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.file_dir is not None:
            result['FileDir'] = self.file_dir
        if self.host is not None:
            result['Host'] = self.host
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.signature is not None:
            result['Signature'] = self.signature
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessId') is not None:
            self.access_id = m.get('AccessId')
        if m.get('EncodedPolicy') is not None:
            self.encoded_policy = m.get('EncodedPolicy')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('FileDir') is not None:
            self.file_dir = m.get('FileDir')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Signature') is not None:
            self.signature = m.get('Signature')
        return self


class GenerateUploadFilePolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GenerateUploadFilePolicyResponseBody = None,
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
            temp_model = GenerateUploadFilePolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAlipayUrlRequest(TeaModel):
    def __init__(
        self,
        biz_type: str = None,
        order_id: int = None,
        return_url: str = None,
        type: str = None,
    ):
        self.biz_type = biz_type
        self.order_id = order_id
        self.return_url = return_url
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.return_url is not None:
            result['ReturnUrl'] = self.return_url
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('ReturnUrl') is not None:
            self.return_url = m.get('ReturnUrl')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetAlipayUrlResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetAlipayUrlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAlipayUrlResponseBody = None,
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
            temp_model = GetAlipayUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOrderConfirmUrlRequestItems(TeaModel):
    def __init__(
        self,
        item_code: str = None,
        quantity: int = None,
    ):
        self.item_code = item_code
        self.quantity = quantity

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.item_code is not None:
            result['ItemCode'] = self.item_code
        if self.quantity is not None:
            result['Quantity'] = self.quantity
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ItemCode') is not None:
            self.item_code = m.get('ItemCode')
        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')
        return self


class GetOrderConfirmUrlRequest(TeaModel):
    def __init__(
        self,
        items: List[GetOrderConfirmUrlRequestItems] = None,
        out_trace_code: str = None,
        out_trace_type: str = None,
    ):
        self.items = items
        self.out_trace_code = out_trace_code
        self.out_trace_type = out_trace_type

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.out_trace_code is not None:
            result['OutTraceCode'] = self.out_trace_code
        if self.out_trace_type is not None:
            result['OutTraceType'] = self.out_trace_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = GetOrderConfirmUrlRequestItems()
                self.items.append(temp_model.from_map(k))
        if m.get('OutTraceCode') is not None:
            self.out_trace_code = m.get('OutTraceCode')
        if m.get('OutTraceType') is not None:
            self.out_trace_type = m.get('OutTraceType')
        return self


class GetOrderConfirmUrlResponseBody(TeaModel):
    def __init__(
        self,
        confirm_url: str = None,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.confirm_url = confirm_url
        self.error_code = error_code
        self.error_message = error_message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.confirm_url is not None:
            result['ConfirmUrl'] = self.confirm_url
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfirmUrl') is not None:
            self.confirm_url = m.get('ConfirmUrl')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetOrderConfirmUrlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetOrderConfirmUrlResponseBody = None,
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
            temp_model = GetOrderConfirmUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetStsByTaobaoUidRequest(TeaModel):
    def __init__(
        self,
        aliyun_uid: str = None,
        tb_uid: str = None,
    ):
        self.aliyun_uid = aliyun_uid
        self.tb_uid = tb_uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aliyun_uid is not None:
            result['AliyunUid'] = self.aliyun_uid
        if self.tb_uid is not None:
            result['TbUid'] = self.tb_uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunUid') is not None:
            self.aliyun_uid = m.get('AliyunUid')
        if m.get('TbUid') is not None:
            self.tb_uid = m.get('TbUid')
        return self


class GetStsByTaobaoUidResponseBody(TeaModel):
    def __init__(
        self,
        access_key_id: str = None,
        access_key_secret: str = None,
        error_code: str = None,
        error_message: str = None,
        expiration: str = None,
        request_id: str = None,
        security_token: str = None,
        success: bool = None,
    ):
        self.access_key_id = access_key_id
        self.access_key_secret = access_key_secret
        self.error_code = error_code
        self.error_message = error_message
        self.expiration = expiration
        self.request_id = request_id
        self.security_token = security_token
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key_id is not None:
            result['AccessKeyId'] = self.access_key_id
        if self.access_key_secret is not None:
            result['AccessKeySecret'] = self.access_key_secret
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.expiration is not None:
            result['Expiration'] = self.expiration
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessKeyId') is not None:
            self.access_key_id = m.get('AccessKeyId')
        if m.get('AccessKeySecret') is not None:
            self.access_key_secret = m.get('AccessKeySecret')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Expiration') is not None:
            self.expiration = m.get('Expiration')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetStsByTaobaoUidResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetStsByTaobaoUidResponseBody = None,
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
            temp_model = GetStsByTaobaoUidResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAdminTrademarkApplicationLogsRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
    ):
        self.biz_id = biz_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        return self


class ListAdminTrademarkApplicationLogsResponseBodyTrademarkApplicationLogs(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        biz_status: int = None,
        note: str = None,
        operate_time: int = None,
        operate_type: int = None,
    ):
        self.biz_id = biz_id
        self.biz_status = biz_status
        self.note = note
        self.operate_time = operate_time
        self.operate_type = operate_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.biz_status is not None:
            result['BizStatus'] = self.biz_status
        if self.note is not None:
            result['Note'] = self.note
        if self.operate_time is not None:
            result['OperateTime'] = self.operate_time
        if self.operate_type is not None:
            result['OperateType'] = self.operate_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BizStatus') is not None:
            self.biz_status = m.get('BizStatus')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        if m.get('OperateTime') is not None:
            self.operate_time = m.get('OperateTime')
        if m.get('OperateType') is not None:
            self.operate_type = m.get('OperateType')
        return self


class ListAdminTrademarkApplicationLogsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        trademark_application_logs: List[ListAdminTrademarkApplicationLogsResponseBodyTrademarkApplicationLogs] = None,
    ):
        self.request_id = request_id
        self.trademark_application_logs = trademark_application_logs

    def validate(self):
        if self.trademark_application_logs:
            for k in self.trademark_application_logs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TrademarkApplicationLogs'] = []
        if self.trademark_application_logs is not None:
            for k in self.trademark_application_logs:
                result['TrademarkApplicationLogs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.trademark_application_logs = []
        if m.get('TrademarkApplicationLogs') is not None:
            for k in m.get('TrademarkApplicationLogs'):
                temp_model = ListAdminTrademarkApplicationLogsResponseBodyTrademarkApplicationLogs()
                self.trademark_application_logs.append(temp_model.from_map(k))
        return self


class ListAdminTrademarkApplicationLogsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAdminTrademarkApplicationLogsResponseBody = None,
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
            temp_model = ListAdminTrademarkApplicationLogsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAdminTrademarkApplicationsRequest(TeaModel):
    def __init__(
        self,
        applicant_name: str = None,
        application_status: int = None,
        application_type: str = None,
        biz_id: str = None,
        order_id: str = None,
        page_number: int = None,
        page_size: int = None,
        sort_order: str = None,
        supplement_status: int = None,
        trademark_name: str = None,
        trademark_number: str = None,
        user_id: str = None,
    ):
        self.applicant_name = applicant_name
        self.application_status = application_status
        self.application_type = application_type
        self.biz_id = biz_id
        self.order_id = order_id
        self.page_number = page_number
        self.page_size = page_size
        self.sort_order = sort_order
        self.supplement_status = supplement_status
        self.trademark_name = trademark_name
        self.trademark_number = trademark_number
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.applicant_name is not None:
            result['ApplicantName'] = self.applicant_name
        if self.application_status is not None:
            result['ApplicationStatus'] = self.application_status
        if self.application_type is not None:
            result['ApplicationType'] = self.application_type
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order
        if self.supplement_status is not None:
            result['SupplementStatus'] = self.supplement_status
        if self.trademark_name is not None:
            result['TrademarkName'] = self.trademark_name
        if self.trademark_number is not None:
            result['TrademarkNumber'] = self.trademark_number
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicantName') is not None:
            self.applicant_name = m.get('ApplicantName')
        if m.get('ApplicationStatus') is not None:
            self.application_status = m.get('ApplicationStatus')
        if m.get('ApplicationType') is not None:
            self.application_type = m.get('ApplicationType')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')
        if m.get('SupplementStatus') is not None:
            self.supplement_status = m.get('SupplementStatus')
        if m.get('TrademarkName') is not None:
            self.trademark_name = m.get('TrademarkName')
        if m.get('TrademarkNumber') is not None:
            self.trademark_number = m.get('TrademarkNumber')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ListAdminTrademarkApplicationsResponseBodyTrademarkApplicationsFirstClassification(TeaModel):
    def __init__(
        self,
        classification_code: str = None,
        classification_name: str = None,
    ):
        self.classification_code = classification_code
        self.classification_name = classification_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.classification_code is not None:
            result['ClassificationCode'] = self.classification_code
        if self.classification_name is not None:
            result['ClassificationName'] = self.classification_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClassificationCode') is not None:
            self.classification_code = m.get('ClassificationCode')
        if m.get('ClassificationName') is not None:
            self.classification_name = m.get('ClassificationName')
        return self


class ListAdminTrademarkApplicationsResponseBodyTrademarkApplicationsThirdClassification(TeaModel):
    def __init__(
        self,
        classification_code: str = None,
        classification_name: str = None,
    ):
        self.classification_code = classification_code
        self.classification_name = classification_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.classification_code is not None:
            result['ClassificationCode'] = self.classification_code
        if self.classification_name is not None:
            result['ClassificationName'] = self.classification_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClassificationCode') is not None:
            self.classification_code = m.get('ClassificationCode')
        if m.get('ClassificationName') is not None:
            self.classification_name = m.get('ClassificationName')
        return self


class ListAdminTrademarkApplicationsResponseBodyTrademarkApplications(TeaModel):
    def __init__(
        self,
        applicant_id: int = None,
        applicant_name: str = None,
        application_status: int = None,
        application_type: int = None,
        authorization_url: str = None,
        biz_id: str = None,
        create_time: int = None,
        first_classification: ListAdminTrademarkApplicationsResponseBodyTrademarkApplicationsFirstClassification = None,
        flags: List[str] = None,
        note: str = None,
        order_id: str = None,
        order_price: float = None,
        principal_name: int = None,
        service_price: float = None,
        supplement_id: int = None,
        supplement_status: int = None,
        system_version: str = None,
        third_classification: List[ListAdminTrademarkApplicationsResponseBodyTrademarkApplicationsThirdClassification] = None,
        total_price: float = None,
        trademark_icon: str = None,
        trademark_name: str = None,
        trademark_number: str = None,
        update_time: int = None,
        user_id: str = None,
    ):
        self.applicant_id = applicant_id
        self.applicant_name = applicant_name
        self.application_status = application_status
        self.application_type = application_type
        self.authorization_url = authorization_url
        self.biz_id = biz_id
        self.create_time = create_time
        self.first_classification = first_classification
        self.flags = flags
        self.note = note
        self.order_id = order_id
        self.order_price = order_price
        self.principal_name = principal_name
        self.service_price = service_price
        self.supplement_id = supplement_id
        self.supplement_status = supplement_status
        self.system_version = system_version
        self.third_classification = third_classification
        self.total_price = total_price
        self.trademark_icon = trademark_icon
        self.trademark_name = trademark_name
        self.trademark_number = trademark_number
        self.update_time = update_time
        self.user_id = user_id

    def validate(self):
        if self.first_classification:
            self.first_classification.validate()
        if self.third_classification:
            for k in self.third_classification:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.applicant_id is not None:
            result['ApplicantId'] = self.applicant_id
        if self.applicant_name is not None:
            result['ApplicantName'] = self.applicant_name
        if self.application_status is not None:
            result['ApplicationStatus'] = self.application_status
        if self.application_type is not None:
            result['ApplicationType'] = self.application_type
        if self.authorization_url is not None:
            result['AuthorizationUrl'] = self.authorization_url
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.first_classification is not None:
            result['FirstClassification'] = self.first_classification.to_map()
        if self.flags is not None:
            result['Flags'] = self.flags
        if self.note is not None:
            result['Note'] = self.note
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.order_price is not None:
            result['OrderPrice'] = self.order_price
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name
        if self.service_price is not None:
            result['ServicePrice'] = self.service_price
        if self.supplement_id is not None:
            result['SupplementId'] = self.supplement_id
        if self.supplement_status is not None:
            result['SupplementStatus'] = self.supplement_status
        if self.system_version is not None:
            result['SystemVersion'] = self.system_version
        result['ThirdClassification'] = []
        if self.third_classification is not None:
            for k in self.third_classification:
                result['ThirdClassification'].append(k.to_map() if k else None)
        if self.total_price is not None:
            result['TotalPrice'] = self.total_price
        if self.trademark_icon is not None:
            result['TrademarkIcon'] = self.trademark_icon
        if self.trademark_name is not None:
            result['TrademarkName'] = self.trademark_name
        if self.trademark_number is not None:
            result['TrademarkNumber'] = self.trademark_number
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicantId') is not None:
            self.applicant_id = m.get('ApplicantId')
        if m.get('ApplicantName') is not None:
            self.applicant_name = m.get('ApplicantName')
        if m.get('ApplicationStatus') is not None:
            self.application_status = m.get('ApplicationStatus')
        if m.get('ApplicationType') is not None:
            self.application_type = m.get('ApplicationType')
        if m.get('AuthorizationUrl') is not None:
            self.authorization_url = m.get('AuthorizationUrl')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('FirstClassification') is not None:
            temp_model = ListAdminTrademarkApplicationsResponseBodyTrademarkApplicationsFirstClassification()
            self.first_classification = temp_model.from_map(m['FirstClassification'])
        if m.get('Flags') is not None:
            self.flags = m.get('Flags')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('OrderPrice') is not None:
            self.order_price = m.get('OrderPrice')
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')
        if m.get('ServicePrice') is not None:
            self.service_price = m.get('ServicePrice')
        if m.get('SupplementId') is not None:
            self.supplement_id = m.get('SupplementId')
        if m.get('SupplementStatus') is not None:
            self.supplement_status = m.get('SupplementStatus')
        if m.get('SystemVersion') is not None:
            self.system_version = m.get('SystemVersion')
        self.third_classification = []
        if m.get('ThirdClassification') is not None:
            for k in m.get('ThirdClassification'):
                temp_model = ListAdminTrademarkApplicationsResponseBodyTrademarkApplicationsThirdClassification()
                self.third_classification.append(temp_model.from_map(k))
        if m.get('TotalPrice') is not None:
            self.total_price = m.get('TotalPrice')
        if m.get('TrademarkIcon') is not None:
            self.trademark_icon = m.get('TrademarkIcon')
        if m.get('TrademarkName') is not None:
            self.trademark_name = m.get('TrademarkName')
        if m.get('TrademarkNumber') is not None:
            self.trademark_number = m.get('TrademarkNumber')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ListAdminTrademarkApplicationsResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        trademark_applications: List[ListAdminTrademarkApplicationsResponseBodyTrademarkApplications] = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count
        self.trademark_applications = trademark_applications

    def validate(self):
        if self.trademark_applications:
            for k in self.trademark_applications:
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
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['TrademarkApplications'] = []
        if self.trademark_applications is not None:
            for k in self.trademark_applications:
                result['TrademarkApplications'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.trademark_applications = []
        if m.get('TrademarkApplications') is not None:
            for k in m.get('TrademarkApplications'):
                temp_model = ListAdminTrademarkApplicationsResponseBodyTrademarkApplications()
                self.trademark_applications.append(temp_model.from_map(k))
        return self


class ListAdminTrademarkApplicationsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAdminTrademarkApplicationsResponseBody = None,
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
            temp_model = ListAdminTrademarkApplicationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListApplicantsRequest(TeaModel):
    def __init__(
        self,
        applicant_name: str = None,
        applicant_region: int = None,
        applicant_type: int = None,
        applicant_version: str = None,
        audit_status: int = None,
        card_number: str = None,
        page_number: int = None,
        page_size: int = None,
        principal_name: int = None,
        system_version: str = None,
    ):
        self.applicant_name = applicant_name
        self.applicant_region = applicant_region
        self.applicant_type = applicant_type
        self.applicant_version = applicant_version
        self.audit_status = audit_status
        self.card_number = card_number
        self.page_number = page_number
        self.page_size = page_size
        self.principal_name = principal_name
        self.system_version = system_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.applicant_name is not None:
            result['ApplicantName'] = self.applicant_name
        if self.applicant_region is not None:
            result['ApplicantRegion'] = self.applicant_region
        if self.applicant_type is not None:
            result['ApplicantType'] = self.applicant_type
        if self.applicant_version is not None:
            result['ApplicantVersion'] = self.applicant_version
        if self.audit_status is not None:
            result['AuditStatus'] = self.audit_status
        if self.card_number is not None:
            result['CardNumber'] = self.card_number
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name
        if self.system_version is not None:
            result['SystemVersion'] = self.system_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicantName') is not None:
            self.applicant_name = m.get('ApplicantName')
        if m.get('ApplicantRegion') is not None:
            self.applicant_region = m.get('ApplicantRegion')
        if m.get('ApplicantType') is not None:
            self.applicant_type = m.get('ApplicantType')
        if m.get('ApplicantVersion') is not None:
            self.applicant_version = m.get('ApplicantVersion')
        if m.get('AuditStatus') is not None:
            self.audit_status = m.get('AuditStatus')
        if m.get('CardNumber') is not None:
            self.card_number = m.get('CardNumber')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')
        if m.get('SystemVersion') is not None:
            self.system_version = m.get('SystemVersion')
        return self


class ListApplicantsResponseBodyApplicantsApplicant(TeaModel):
    def __init__(
        self,
        applicant_id: int = None,
        applicant_name: str = None,
        applicant_region: int = None,
        applicant_type: int = None,
        applicant_version: str = None,
        audit_status: int = None,
        authorization_audit_status: int = None,
        authorization_url: str = None,
        card_number: str = None,
        contact_name: str = None,
        principal_name: int = None,
        system_version: str = None,
        valid_date: int = None,
    ):
        self.applicant_id = applicant_id
        self.applicant_name = applicant_name
        self.applicant_region = applicant_region
        self.applicant_type = applicant_type
        self.applicant_version = applicant_version
        self.audit_status = audit_status
        self.authorization_audit_status = authorization_audit_status
        self.authorization_url = authorization_url
        self.card_number = card_number
        self.contact_name = contact_name
        self.principal_name = principal_name
        self.system_version = system_version
        self.valid_date = valid_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.applicant_id is not None:
            result['ApplicantId'] = self.applicant_id
        if self.applicant_name is not None:
            result['ApplicantName'] = self.applicant_name
        if self.applicant_region is not None:
            result['ApplicantRegion'] = self.applicant_region
        if self.applicant_type is not None:
            result['ApplicantType'] = self.applicant_type
        if self.applicant_version is not None:
            result['ApplicantVersion'] = self.applicant_version
        if self.audit_status is not None:
            result['AuditStatus'] = self.audit_status
        if self.authorization_audit_status is not None:
            result['AuthorizationAuditStatus'] = self.authorization_audit_status
        if self.authorization_url is not None:
            result['AuthorizationUrl'] = self.authorization_url
        if self.card_number is not None:
            result['CardNumber'] = self.card_number
        if self.contact_name is not None:
            result['ContactName'] = self.contact_name
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name
        if self.system_version is not None:
            result['SystemVersion'] = self.system_version
        if self.valid_date is not None:
            result['ValidDate'] = self.valid_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicantId') is not None:
            self.applicant_id = m.get('ApplicantId')
        if m.get('ApplicantName') is not None:
            self.applicant_name = m.get('ApplicantName')
        if m.get('ApplicantRegion') is not None:
            self.applicant_region = m.get('ApplicantRegion')
        if m.get('ApplicantType') is not None:
            self.applicant_type = m.get('ApplicantType')
        if m.get('ApplicantVersion') is not None:
            self.applicant_version = m.get('ApplicantVersion')
        if m.get('AuditStatus') is not None:
            self.audit_status = m.get('AuditStatus')
        if m.get('AuthorizationAuditStatus') is not None:
            self.authorization_audit_status = m.get('AuthorizationAuditStatus')
        if m.get('AuthorizationUrl') is not None:
            self.authorization_url = m.get('AuthorizationUrl')
        if m.get('CardNumber') is not None:
            self.card_number = m.get('CardNumber')
        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')
        if m.get('SystemVersion') is not None:
            self.system_version = m.get('SystemVersion')
        if m.get('ValidDate') is not None:
            self.valid_date = m.get('ValidDate')
        return self


class ListApplicantsResponseBodyApplicants(TeaModel):
    def __init__(
        self,
        applicant: List[ListApplicantsResponseBodyApplicantsApplicant] = None,
    ):
        self.applicant = applicant

    def validate(self):
        if self.applicant:
            for k in self.applicant:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Applicant'] = []
        if self.applicant is not None:
            for k in self.applicant:
                result['Applicant'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.applicant = []
        if m.get('Applicant') is not None:
            for k in m.get('Applicant'):
                temp_model = ListApplicantsResponseBodyApplicantsApplicant()
                self.applicant.append(temp_model.from_map(k))
        return self


class ListApplicantsResponseBody(TeaModel):
    def __init__(
        self,
        applicants: ListApplicantsResponseBodyApplicants = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.applicants = applicants
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.applicants:
            self.applicants.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.applicants is not None:
            result['Applicants'] = self.applicants.to_map()
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
        if m.get('Applicants') is not None:
            temp_model = ListApplicantsResponseBodyApplicants()
            self.applicants = temp_model.from_map(m['Applicants'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListApplicantsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListApplicantsResponseBody = None,
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
            temp_model = ListApplicantsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAreasRequest(TeaModel):
    def __init__(
        self,
        biz_type: str = None,
        parent_code: str = None,
    ):
        self.biz_type = biz_type
        self.parent_code = parent_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.parent_code is not None:
            result['ParentCode'] = self.parent_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('ParentCode') is not None:
            self.parent_code = m.get('ParentCode')
        return self


class ListAreasResponseBodyDatasSubArea(TeaModel):
    def __init__(
        self,
        code: str = None,
        name: str = None,
        parent_code: str = None,
        sort_num: int = None,
    ):
        self.code = code
        self.name = name
        self.parent_code = parent_code
        self.sort_num = sort_num

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
        if self.parent_code is not None:
            result['ParentCode'] = self.parent_code
        if self.sort_num is not None:
            result['SortNum'] = self.sort_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ParentCode') is not None:
            self.parent_code = m.get('ParentCode')
        if m.get('SortNum') is not None:
            self.sort_num = m.get('SortNum')
        return self


class ListAreasResponseBodyDatas(TeaModel):
    def __init__(
        self,
        code: str = None,
        name: str = None,
        parent_code: str = None,
        sort_num: int = None,
        sub_area: List[ListAreasResponseBodyDatasSubArea] = None,
    ):
        self.code = code
        self.name = name
        self.parent_code = parent_code
        self.sort_num = sort_num
        self.sub_area = sub_area

    def validate(self):
        if self.sub_area:
            for k in self.sub_area:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.name is not None:
            result['Name'] = self.name
        if self.parent_code is not None:
            result['ParentCode'] = self.parent_code
        if self.sort_num is not None:
            result['SortNum'] = self.sort_num
        result['SubArea'] = []
        if self.sub_area is not None:
            for k in self.sub_area:
                result['SubArea'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ParentCode') is not None:
            self.parent_code = m.get('ParentCode')
        if m.get('SortNum') is not None:
            self.sort_num = m.get('SortNum')
        self.sub_area = []
        if m.get('SubArea') is not None:
            for k in m.get('SubArea'):
                temp_model = ListAreasResponseBodyDatasSubArea()
                self.sub_area.append(temp_model.from_map(k))
        return self


class ListAreasResponseBody(TeaModel):
    def __init__(
        self,
        datas: List[ListAreasResponseBodyDatas] = None,
        request_id: str = None,
    ):
        self.datas = datas
        self.request_id = request_id

    def validate(self):
        if self.datas:
            for k in self.datas:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Datas'] = []
        if self.datas is not None:
            for k in self.datas:
                result['Datas'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.datas = []
        if m.get('Datas') is not None:
            for k in m.get('Datas'):
                temp_model = ListAreasResponseBodyDatas()
                self.datas.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListAreasResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAreasResponseBody = None,
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
            temp_model = ListAreasResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListClassificationConditionsRequest(TeaModel):
    def __init__(
        self,
        tag_name: str = None,
        type: int = None,
    ):
        self.tag_name = tag_name
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_name is not None:
            result['TagName'] = self.tag_name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListClassificationConditionsResponseBodyData(TeaModel):
    def __init__(
        self,
        condition_content: str = None,
        create_time: int = None,
        id: int = None,
        session_id: str = None,
        tag_name: str = None,
        type: int = None,
        umid: str = None,
        update_time: int = None,
        user_id: int = None,
    ):
        self.condition_content = condition_content
        self.create_time = create_time
        self.id = id
        self.session_id = session_id
        self.tag_name = tag_name
        self.type = type
        self.umid = umid
        self.update_time = update_time
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.condition_content is not None:
            result['ConditionContent'] = self.condition_content
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.id is not None:
            result['Id'] = self.id
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.tag_name is not None:
            result['TagName'] = self.tag_name
        if self.type is not None:
            result['Type'] = self.type
        if self.umid is not None:
            result['Umid'] = self.umid
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConditionContent') is not None:
            self.condition_content = m.get('ConditionContent')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Umid') is not None:
            self.umid = m.get('Umid')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ListClassificationConditionsResponseBody(TeaModel):
    def __init__(
        self,
        data: List[ListClassificationConditionsResponseBodyData] = None,
        request_id: str = None,
    ):
        self.data = data
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
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListClassificationConditionsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListClassificationConditionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListClassificationConditionsResponseBody = None,
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
            temp_model = ListClassificationConditionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListClassificationsRequest(TeaModel):
    def __init__(
        self,
        parent_code: str = None,
    ):
        self.parent_code = parent_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.parent_code is not None:
            result['ParentCode'] = self.parent_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParentCode') is not None:
            self.parent_code = m.get('ParentCode')
        return self


class ListClassificationsResponseBodyClassificationsClassification(TeaModel):
    def __init__(
        self,
        classification_code: str = None,
        classification_name: str = None,
        id: int = None,
        level: int = None,
        official_code: str = None,
        parent_code: str = None,
    ):
        self.classification_code = classification_code
        self.classification_name = classification_name
        self.id = id
        self.level = level
        self.official_code = official_code
        self.parent_code = parent_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.classification_code is not None:
            result['ClassificationCode'] = self.classification_code
        if self.classification_name is not None:
            result['ClassificationName'] = self.classification_name
        if self.id is not None:
            result['Id'] = self.id
        if self.level is not None:
            result['Level'] = self.level
        if self.official_code is not None:
            result['OfficialCode'] = self.official_code
        if self.parent_code is not None:
            result['ParentCode'] = self.parent_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClassificationCode') is not None:
            self.classification_code = m.get('ClassificationCode')
        if m.get('ClassificationName') is not None:
            self.classification_name = m.get('ClassificationName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('OfficialCode') is not None:
            self.official_code = m.get('OfficialCode')
        if m.get('ParentCode') is not None:
            self.parent_code = m.get('ParentCode')
        return self


class ListClassificationsResponseBodyClassifications(TeaModel):
    def __init__(
        self,
        classification: List[ListClassificationsResponseBodyClassificationsClassification] = None,
    ):
        self.classification = classification

    def validate(self):
        if self.classification:
            for k in self.classification:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Classification'] = []
        if self.classification is not None:
            for k in self.classification:
                result['Classification'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.classification = []
        if m.get('Classification') is not None:
            for k in m.get('Classification'):
                temp_model = ListClassificationsResponseBodyClassificationsClassification()
                self.classification.append(temp_model.from_map(k))
        return self


class ListClassificationsResponseBody(TeaModel):
    def __init__(
        self,
        classifications: ListClassificationsResponseBodyClassifications = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.classifications = classifications
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.classifications:
            self.classifications.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.classifications is not None:
            result['Classifications'] = self.classifications.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Classifications') is not None:
            temp_model = ListClassificationsResponseBodyClassifications()
            self.classifications = temp_model.from_map(m['Classifications'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListClassificationsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListClassificationsResponseBody = None,
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
            temp_model = ListClassificationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTrademarkApplicationLogsRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
    ):
        self.biz_id = biz_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        return self


class ListTrademarkApplicationLogsResponseBodyTrademarkApplicationLogsTrademarkApplicationLog(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        biz_status: int = None,
        note: str = None,
        operate_time: int = None,
        operate_type: int = None,
    ):
        self.biz_id = biz_id
        self.biz_status = biz_status
        self.note = note
        self.operate_time = operate_time
        self.operate_type = operate_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.biz_status is not None:
            result['BizStatus'] = self.biz_status
        if self.note is not None:
            result['Note'] = self.note
        if self.operate_time is not None:
            result['OperateTime'] = self.operate_time
        if self.operate_type is not None:
            result['OperateType'] = self.operate_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BizStatus') is not None:
            self.biz_status = m.get('BizStatus')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        if m.get('OperateTime') is not None:
            self.operate_time = m.get('OperateTime')
        if m.get('OperateType') is not None:
            self.operate_type = m.get('OperateType')
        return self


class ListTrademarkApplicationLogsResponseBodyTrademarkApplicationLogs(TeaModel):
    def __init__(
        self,
        trademark_application_log: List[ListTrademarkApplicationLogsResponseBodyTrademarkApplicationLogsTrademarkApplicationLog] = None,
    ):
        self.trademark_application_log = trademark_application_log

    def validate(self):
        if self.trademark_application_log:
            for k in self.trademark_application_log:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TrademarkApplicationLog'] = []
        if self.trademark_application_log is not None:
            for k in self.trademark_application_log:
                result['TrademarkApplicationLog'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.trademark_application_log = []
        if m.get('TrademarkApplicationLog') is not None:
            for k in m.get('TrademarkApplicationLog'):
                temp_model = ListTrademarkApplicationLogsResponseBodyTrademarkApplicationLogsTrademarkApplicationLog()
                self.trademark_application_log.append(temp_model.from_map(k))
        return self


class ListTrademarkApplicationLogsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        trademark_application_logs: ListTrademarkApplicationLogsResponseBodyTrademarkApplicationLogs = None,
    ):
        self.request_id = request_id
        self.trademark_application_logs = trademark_application_logs

    def validate(self):
        if self.trademark_application_logs:
            self.trademark_application_logs.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.trademark_application_logs is not None:
            result['TrademarkApplicationLogs'] = self.trademark_application_logs.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TrademarkApplicationLogs') is not None:
            temp_model = ListTrademarkApplicationLogsResponseBodyTrademarkApplicationLogs()
            self.trademark_application_logs = temp_model.from_map(m['TrademarkApplicationLogs'])
        return self


class ListTrademarkApplicationLogsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTrademarkApplicationLogsResponseBody = None,
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
            temp_model = ListTrademarkApplicationLogsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTrademarkApplicationsRequest(TeaModel):
    def __init__(
        self,
        applicant_name: str = None,
        application_status: int = None,
        application_type: str = None,
        biz_id: str = None,
        create_time_left: int = None,
        create_time_right: int = None,
        flag: int = None,
        order_id: str = None,
        page_number: int = None,
        page_size: int = None,
        product_type: int = None,
        query_voucher_order_done_flag: bool = None,
        query_voucher_order_flag: bool = None,
        sort_filed: str = None,
        sort_order: str = None,
        supplement_status: int = None,
        trademark_name: str = None,
        trademark_number: str = None,
    ):
        self.applicant_name = applicant_name
        self.application_status = application_status
        self.application_type = application_type
        self.biz_id = biz_id
        self.create_time_left = create_time_left
        self.create_time_right = create_time_right
        self.flag = flag
        self.order_id = order_id
        self.page_number = page_number
        self.page_size = page_size
        self.product_type = product_type
        self.query_voucher_order_done_flag = query_voucher_order_done_flag
        self.query_voucher_order_flag = query_voucher_order_flag
        self.sort_filed = sort_filed
        self.sort_order = sort_order
        self.supplement_status = supplement_status
        self.trademark_name = trademark_name
        self.trademark_number = trademark_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.applicant_name is not None:
            result['ApplicantName'] = self.applicant_name
        if self.application_status is not None:
            result['ApplicationStatus'] = self.application_status
        if self.application_type is not None:
            result['ApplicationType'] = self.application_type
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.create_time_left is not None:
            result['CreateTimeLeft'] = self.create_time_left
        if self.create_time_right is not None:
            result['CreateTimeRight'] = self.create_time_right
        if self.flag is not None:
            result['Flag'] = self.flag
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.query_voucher_order_done_flag is not None:
            result['QueryVoucherOrderDoneFlag'] = self.query_voucher_order_done_flag
        if self.query_voucher_order_flag is not None:
            result['QueryVoucherOrderFlag'] = self.query_voucher_order_flag
        if self.sort_filed is not None:
            result['SortFiled'] = self.sort_filed
        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order
        if self.supplement_status is not None:
            result['SupplementStatus'] = self.supplement_status
        if self.trademark_name is not None:
            result['TrademarkName'] = self.trademark_name
        if self.trademark_number is not None:
            result['TrademarkNumber'] = self.trademark_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicantName') is not None:
            self.applicant_name = m.get('ApplicantName')
        if m.get('ApplicationStatus') is not None:
            self.application_status = m.get('ApplicationStatus')
        if m.get('ApplicationType') is not None:
            self.application_type = m.get('ApplicationType')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('CreateTimeLeft') is not None:
            self.create_time_left = m.get('CreateTimeLeft')
        if m.get('CreateTimeRight') is not None:
            self.create_time_right = m.get('CreateTimeRight')
        if m.get('Flag') is not None:
            self.flag = m.get('Flag')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('QueryVoucherOrderDoneFlag') is not None:
            self.query_voucher_order_done_flag = m.get('QueryVoucherOrderDoneFlag')
        if m.get('QueryVoucherOrderFlag') is not None:
            self.query_voucher_order_flag = m.get('QueryVoucherOrderFlag')
        if m.get('SortFiled') is not None:
            self.sort_filed = m.get('SortFiled')
        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')
        if m.get('SupplementStatus') is not None:
            self.supplement_status = m.get('SupplementStatus')
        if m.get('TrademarkName') is not None:
            self.trademark_name = m.get('TrademarkName')
        if m.get('TrademarkNumber') is not None:
            self.trademark_number = m.get('TrademarkNumber')
        return self


class ListTrademarkApplicationsResponseBodyTrademarkApplicationsTrademarkApplicationFirstClassification(TeaModel):
    def __init__(
        self,
        classification_code: str = None,
        classification_name: str = None,
    ):
        self.classification_code = classification_code
        self.classification_name = classification_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.classification_code is not None:
            result['ClassificationCode'] = self.classification_code
        if self.classification_name is not None:
            result['ClassificationName'] = self.classification_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClassificationCode') is not None:
            self.classification_code = m.get('ClassificationCode')
        if m.get('ClassificationName') is not None:
            self.classification_name = m.get('ClassificationName')
        return self


class ListTrademarkApplicationsResponseBodyTrademarkApplicationsTrademarkApplicationFlags(TeaModel):
    def __init__(
        self,
        flags: List[str] = None,
    ):
        self.flags = flags

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flags is not None:
            result['Flags'] = self.flags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Flags') is not None:
            self.flags = m.get('Flags')
        return self


class ListTrademarkApplicationsResponseBodyTrademarkApplicationsTrademarkApplicationThirdClassificationThirdClassification(TeaModel):
    def __init__(
        self,
        classification_code: str = None,
        classification_name: str = None,
    ):
        self.classification_code = classification_code
        self.classification_name = classification_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.classification_code is not None:
            result['ClassificationCode'] = self.classification_code
        if self.classification_name is not None:
            result['ClassificationName'] = self.classification_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClassificationCode') is not None:
            self.classification_code = m.get('ClassificationCode')
        if m.get('ClassificationName') is not None:
            self.classification_name = m.get('ClassificationName')
        return self


class ListTrademarkApplicationsResponseBodyTrademarkApplicationsTrademarkApplicationThirdClassification(TeaModel):
    def __init__(
        self,
        third_classification: List[ListTrademarkApplicationsResponseBodyTrademarkApplicationsTrademarkApplicationThirdClassificationThirdClassification] = None,
    ):
        self.third_classification = third_classification

    def validate(self):
        if self.third_classification:
            for k in self.third_classification:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ThirdClassification'] = []
        if self.third_classification is not None:
            for k in self.third_classification:
                result['ThirdClassification'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.third_classification = []
        if m.get('ThirdClassification') is not None:
            for k in m.get('ThirdClassification'):
                temp_model = ListTrademarkApplicationsResponseBodyTrademarkApplicationsTrademarkApplicationThirdClassificationThirdClassification()
                self.third_classification.append(temp_model.from_map(k))
        return self


class ListTrademarkApplicationsResponseBodyTrademarkApplicationsTrademarkApplication(TeaModel):
    def __init__(
        self,
        agreement_id: str = None,
        applicant_id: int = None,
        applicant_name: str = None,
        application_status: int = None,
        application_type: int = None,
        authorization_url: str = None,
        biz_id: str = None,
        create_time: int = None,
        first_classification: ListTrademarkApplicationsResponseBodyTrademarkApplicationsTrademarkApplicationFirstClassification = None,
        flags: ListTrademarkApplicationsResponseBodyTrademarkApplicationsTrademarkApplicationFlags = None,
        note: str = None,
        order_id: str = None,
        order_price: float = None,
        principal_name: int = None,
        service_price: float = None,
        supplement_id: int = None,
        supplement_status: int = None,
        system_version: str = None,
        third_classification: ListTrademarkApplicationsResponseBodyTrademarkApplicationsTrademarkApplicationThirdClassification = None,
        total_price: float = None,
        trademark_icon: str = None,
        trademark_name: str = None,
        trademark_number: str = None,
        update_time: int = None,
        user_id: str = None,
    ):
        self.agreement_id = agreement_id
        self.applicant_id = applicant_id
        self.applicant_name = applicant_name
        self.application_status = application_status
        self.application_type = application_type
        self.authorization_url = authorization_url
        self.biz_id = biz_id
        self.create_time = create_time
        self.first_classification = first_classification
        self.flags = flags
        self.note = note
        self.order_id = order_id
        self.order_price = order_price
        self.principal_name = principal_name
        self.service_price = service_price
        self.supplement_id = supplement_id
        self.supplement_status = supplement_status
        self.system_version = system_version
        self.third_classification = third_classification
        self.total_price = total_price
        self.trademark_icon = trademark_icon
        self.trademark_name = trademark_name
        self.trademark_number = trademark_number
        self.update_time = update_time
        self.user_id = user_id

    def validate(self):
        if self.first_classification:
            self.first_classification.validate()
        if self.flags:
            self.flags.validate()
        if self.third_classification:
            self.third_classification.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agreement_id is not None:
            result['AgreementId'] = self.agreement_id
        if self.applicant_id is not None:
            result['ApplicantId'] = self.applicant_id
        if self.applicant_name is not None:
            result['ApplicantName'] = self.applicant_name
        if self.application_status is not None:
            result['ApplicationStatus'] = self.application_status
        if self.application_type is not None:
            result['ApplicationType'] = self.application_type
        if self.authorization_url is not None:
            result['AuthorizationUrl'] = self.authorization_url
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.first_classification is not None:
            result['FirstClassification'] = self.first_classification.to_map()
        if self.flags is not None:
            result['Flags'] = self.flags.to_map()
        if self.note is not None:
            result['Note'] = self.note
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.order_price is not None:
            result['OrderPrice'] = self.order_price
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name
        if self.service_price is not None:
            result['ServicePrice'] = self.service_price
        if self.supplement_id is not None:
            result['SupplementId'] = self.supplement_id
        if self.supplement_status is not None:
            result['SupplementStatus'] = self.supplement_status
        if self.system_version is not None:
            result['SystemVersion'] = self.system_version
        if self.third_classification is not None:
            result['ThirdClassification'] = self.third_classification.to_map()
        if self.total_price is not None:
            result['TotalPrice'] = self.total_price
        if self.trademark_icon is not None:
            result['TrademarkIcon'] = self.trademark_icon
        if self.trademark_name is not None:
            result['TrademarkName'] = self.trademark_name
        if self.trademark_number is not None:
            result['TrademarkNumber'] = self.trademark_number
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgreementId') is not None:
            self.agreement_id = m.get('AgreementId')
        if m.get('ApplicantId') is not None:
            self.applicant_id = m.get('ApplicantId')
        if m.get('ApplicantName') is not None:
            self.applicant_name = m.get('ApplicantName')
        if m.get('ApplicationStatus') is not None:
            self.application_status = m.get('ApplicationStatus')
        if m.get('ApplicationType') is not None:
            self.application_type = m.get('ApplicationType')
        if m.get('AuthorizationUrl') is not None:
            self.authorization_url = m.get('AuthorizationUrl')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('FirstClassification') is not None:
            temp_model = ListTrademarkApplicationsResponseBodyTrademarkApplicationsTrademarkApplicationFirstClassification()
            self.first_classification = temp_model.from_map(m['FirstClassification'])
        if m.get('Flags') is not None:
            temp_model = ListTrademarkApplicationsResponseBodyTrademarkApplicationsTrademarkApplicationFlags()
            self.flags = temp_model.from_map(m['Flags'])
        if m.get('Note') is not None:
            self.note = m.get('Note')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('OrderPrice') is not None:
            self.order_price = m.get('OrderPrice')
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')
        if m.get('ServicePrice') is not None:
            self.service_price = m.get('ServicePrice')
        if m.get('SupplementId') is not None:
            self.supplement_id = m.get('SupplementId')
        if m.get('SupplementStatus') is not None:
            self.supplement_status = m.get('SupplementStatus')
        if m.get('SystemVersion') is not None:
            self.system_version = m.get('SystemVersion')
        if m.get('ThirdClassification') is not None:
            temp_model = ListTrademarkApplicationsResponseBodyTrademarkApplicationsTrademarkApplicationThirdClassification()
            self.third_classification = temp_model.from_map(m['ThirdClassification'])
        if m.get('TotalPrice') is not None:
            self.total_price = m.get('TotalPrice')
        if m.get('TrademarkIcon') is not None:
            self.trademark_icon = m.get('TrademarkIcon')
        if m.get('TrademarkName') is not None:
            self.trademark_name = m.get('TrademarkName')
        if m.get('TrademarkNumber') is not None:
            self.trademark_number = m.get('TrademarkNumber')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ListTrademarkApplicationsResponseBodyTrademarkApplications(TeaModel):
    def __init__(
        self,
        trademark_application: List[ListTrademarkApplicationsResponseBodyTrademarkApplicationsTrademarkApplication] = None,
    ):
        self.trademark_application = trademark_application

    def validate(self):
        if self.trademark_application:
            for k in self.trademark_application:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TrademarkApplication'] = []
        if self.trademark_application is not None:
            for k in self.trademark_application:
                result['TrademarkApplication'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.trademark_application = []
        if m.get('TrademarkApplication') is not None:
            for k in m.get('TrademarkApplication'):
                temp_model = ListTrademarkApplicationsResponseBodyTrademarkApplicationsTrademarkApplication()
                self.trademark_application.append(temp_model.from_map(k))
        return self


class ListTrademarkApplicationsResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        trademark_applications: ListTrademarkApplicationsResponseBodyTrademarkApplications = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count
        self.trademark_applications = trademark_applications

    def validate(self):
        if self.trademark_applications:
            self.trademark_applications.validate()

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
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.trademark_applications is not None:
            result['TrademarkApplications'] = self.trademark_applications.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('TrademarkApplications') is not None:
            temp_model = ListTrademarkApplicationsResponseBodyTrademarkApplications()
            self.trademark_applications = temp_model.from_map(m['TrademarkApplications'])
        return self


class ListTrademarkApplicationsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTrademarkApplicationsResponseBody = None,
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
            temp_model = ListTrademarkApplicationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTrademarkSearchForInnerRequest(TeaModel):
    def __init__(
        self,
        apply_begin_time: str = None,
        apply_end_time: str = None,
        classification: str = None,
        if_precision: bool = None,
        keyword: str = None,
        page_number: int = None,
        page_size: int = None,
        product: str = None,
        search_preference: str = None,
        search_type: str = None,
        status: str = None,
        umid: str = None,
        user_id: str = None,
    ):
        self.apply_begin_time = apply_begin_time
        self.apply_end_time = apply_end_time
        self.classification = classification
        self.if_precision = if_precision
        self.keyword = keyword
        self.page_number = page_number
        self.page_size = page_size
        self.product = product
        self.search_preference = search_preference
        self.search_type = search_type
        self.status = status
        self.umid = umid
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apply_begin_time is not None:
            result['ApplyBeginTime'] = self.apply_begin_time
        if self.apply_end_time is not None:
            result['ApplyEndTime'] = self.apply_end_time
        if self.classification is not None:
            result['Classification'] = self.classification
        if self.if_precision is not None:
            result['IfPrecision'] = self.if_precision
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.product is not None:
            result['Product'] = self.product
        if self.search_preference is not None:
            result['SearchPreference'] = self.search_preference
        if self.search_type is not None:
            result['SearchType'] = self.search_type
        if self.status is not None:
            result['Status'] = self.status
        if self.umid is not None:
            result['Umid'] = self.umid
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplyBeginTime') is not None:
            self.apply_begin_time = m.get('ApplyBeginTime')
        if m.get('ApplyEndTime') is not None:
            self.apply_end_time = m.get('ApplyEndTime')
        if m.get('Classification') is not None:
            self.classification = m.get('Classification')
        if m.get('IfPrecision') is not None:
            self.if_precision = m.get('IfPrecision')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('SearchPreference') is not None:
            self.search_preference = m.get('SearchPreference')
        if m.get('SearchType') is not None:
            self.search_type = m.get('SearchType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Umid') is not None:
            self.umid = m.get('Umid')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ListTrademarkSearchForInnerResponseBodyTrademarkSearchContents(TeaModel):
    def __init__(
        self,
        apply_date: str = None,
        classification: str = None,
        exclusive_date_limit: str = None,
        id: int = None,
        image: str = None,
        last_procedure_status: str = None,
        name: str = None,
        name_char_section: str = None,
        name_origin: str = None,
        name_simplified_chinese: str = None,
        name_sort: str = None,
        on_sale: str = None,
        owner_address: str = None,
        owner_en_address: str = None,
        owner_en_name: str = None,
        owner_name: str = None,
        pre_ann_date: str = None,
        pre_ann_num: str = None,
        product: str = None,
        product_del: List[str] = None,
        product_description: str = None,
        reg_ann_num: str = None,
        registration_number: str = None,
        share: str = None,
        similar_group_del: List[str] = None,
        uid: str = None,
        well_know: str = None,
    ):
        self.apply_date = apply_date
        self.classification = classification
        self.exclusive_date_limit = exclusive_date_limit
        self.id = id
        self.image = image
        self.last_procedure_status = last_procedure_status
        self.name = name
        self.name_char_section = name_char_section
        self.name_origin = name_origin
        self.name_simplified_chinese = name_simplified_chinese
        self.name_sort = name_sort
        self.on_sale = on_sale
        self.owner_address = owner_address
        self.owner_en_address = owner_en_address
        self.owner_en_name = owner_en_name
        self.owner_name = owner_name
        self.pre_ann_date = pre_ann_date
        self.pre_ann_num = pre_ann_num
        self.product = product
        self.product_del = product_del
        self.product_description = product_description
        self.reg_ann_num = reg_ann_num
        self.registration_number = registration_number
        self.share = share
        self.similar_group_del = similar_group_del
        self.uid = uid
        self.well_know = well_know

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apply_date is not None:
            result['ApplyDate'] = self.apply_date
        if self.classification is not None:
            result['Classification'] = self.classification
        if self.exclusive_date_limit is not None:
            result['ExclusiveDateLimit'] = self.exclusive_date_limit
        if self.id is not None:
            result['Id'] = self.id
        if self.image is not None:
            result['Image'] = self.image
        if self.last_procedure_status is not None:
            result['LastProcedureStatus'] = self.last_procedure_status
        if self.name is not None:
            result['Name'] = self.name
        if self.name_char_section is not None:
            result['NameCharSection'] = self.name_char_section
        if self.name_origin is not None:
            result['NameOrigin'] = self.name_origin
        if self.name_simplified_chinese is not None:
            result['NameSimplifiedChinese'] = self.name_simplified_chinese
        if self.name_sort is not None:
            result['NameSort'] = self.name_sort
        if self.on_sale is not None:
            result['OnSale'] = self.on_sale
        if self.owner_address is not None:
            result['OwnerAddress'] = self.owner_address
        if self.owner_en_address is not None:
            result['OwnerEnAddress'] = self.owner_en_address
        if self.owner_en_name is not None:
            result['OwnerEnName'] = self.owner_en_name
        if self.owner_name is not None:
            result['OwnerName'] = self.owner_name
        if self.pre_ann_date is not None:
            result['PreAnnDate'] = self.pre_ann_date
        if self.pre_ann_num is not None:
            result['PreAnnNum'] = self.pre_ann_num
        if self.product is not None:
            result['Product'] = self.product
        if self.product_del is not None:
            result['ProductDel'] = self.product_del
        if self.product_description is not None:
            result['ProductDescription'] = self.product_description
        if self.reg_ann_num is not None:
            result['RegAnnNum'] = self.reg_ann_num
        if self.registration_number is not None:
            result['RegistrationNumber'] = self.registration_number
        if self.share is not None:
            result['Share'] = self.share
        if self.similar_group_del is not None:
            result['SimilarGroupDel'] = self.similar_group_del
        if self.uid is not None:
            result['Uid'] = self.uid
        if self.well_know is not None:
            result['WellKnow'] = self.well_know
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplyDate') is not None:
            self.apply_date = m.get('ApplyDate')
        if m.get('Classification') is not None:
            self.classification = m.get('Classification')
        if m.get('ExclusiveDateLimit') is not None:
            self.exclusive_date_limit = m.get('ExclusiveDateLimit')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Image') is not None:
            self.image = m.get('Image')
        if m.get('LastProcedureStatus') is not None:
            self.last_procedure_status = m.get('LastProcedureStatus')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NameCharSection') is not None:
            self.name_char_section = m.get('NameCharSection')
        if m.get('NameOrigin') is not None:
            self.name_origin = m.get('NameOrigin')
        if m.get('NameSimplifiedChinese') is not None:
            self.name_simplified_chinese = m.get('NameSimplifiedChinese')
        if m.get('NameSort') is not None:
            self.name_sort = m.get('NameSort')
        if m.get('OnSale') is not None:
            self.on_sale = m.get('OnSale')
        if m.get('OwnerAddress') is not None:
            self.owner_address = m.get('OwnerAddress')
        if m.get('OwnerEnAddress') is not None:
            self.owner_en_address = m.get('OwnerEnAddress')
        if m.get('OwnerEnName') is not None:
            self.owner_en_name = m.get('OwnerEnName')
        if m.get('OwnerName') is not None:
            self.owner_name = m.get('OwnerName')
        if m.get('PreAnnDate') is not None:
            self.pre_ann_date = m.get('PreAnnDate')
        if m.get('PreAnnNum') is not None:
            self.pre_ann_num = m.get('PreAnnNum')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('ProductDel') is not None:
            self.product_del = m.get('ProductDel')
        if m.get('ProductDescription') is not None:
            self.product_description = m.get('ProductDescription')
        if m.get('RegAnnNum') is not None:
            self.reg_ann_num = m.get('RegAnnNum')
        if m.get('RegistrationNumber') is not None:
            self.registration_number = m.get('RegistrationNumber')
        if m.get('Share') is not None:
            self.share = m.get('Share')
        if m.get('SimilarGroupDel') is not None:
            self.similar_group_del = m.get('SimilarGroupDel')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        if m.get('WellKnow') is not None:
            self.well_know = m.get('WellKnow')
        return self


class ListTrademarkSearchForInnerResponseBody(TeaModel):
    def __init__(
        self,
        page_number: str = None,
        page_size: str = None,
        products: List[str] = None,
        request_id: str = None,
        total_count: str = None,
        trademark_search_contents: List[ListTrademarkSearchForInnerResponseBodyTrademarkSearchContents] = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.products = products
        self.request_id = request_id
        self.total_count = total_count
        self.trademark_search_contents = trademark_search_contents

    def validate(self):
        if self.trademark_search_contents:
            for k in self.trademark_search_contents:
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
        if self.products is not None:
            result['Products'] = self.products
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['TrademarkSearchContents'] = []
        if self.trademark_search_contents is not None:
            for k in self.trademark_search_contents:
                result['TrademarkSearchContents'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Products') is not None:
            self.products = m.get('Products')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.trademark_search_contents = []
        if m.get('TrademarkSearchContents') is not None:
            for k in m.get('TrademarkSearchContents'):
                temp_model = ListTrademarkSearchForInnerResponseBodyTrademarkSearchContents()
                self.trademark_search_contents.append(temp_model.from_map(k))
        return self


class ListTrademarkSearchForInnerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTrademarkSearchForInnerResponseBody = None,
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
            temp_model = ListTrademarkSearchForInnerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PutMeasureDataRequest(TeaModel):
    def __init__(
        self,
        biz_type: str = None,
        data: str = None,
        data_type: str = None,
        end_time: str = None,
        start_time: str = None,
    ):
        self.biz_type = biz_type
        self.data = data
        self.data_type = data_type
        self.end_time = end_time
        self.start_time = start_time

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
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class PutMeasureDataResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class PutMeasureDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PutMeasureDataResponseBody = None,
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
            temp_model = PutMeasureDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PutMeasureReadyFlagRequest(TeaModel):
    def __init__(
        self,
        biz_type: str = None,
        data_type: str = None,
        end_time: str = None,
        ready_flag: str = None,
        start_time: str = None,
    ):
        self.biz_type = biz_type
        self.data_type = data_type
        self.end_time = end_time
        self.ready_flag = ready_flag
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.ready_flag is not None:
            result['ReadyFlag'] = self.ready_flag
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ReadyFlag') is not None:
            self.ready_flag = m.get('ReadyFlag')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class PutMeasureReadyFlagResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class PutMeasureReadyFlagResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PutMeasureReadyFlagResponseBody = None,
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
            temp_model = PutMeasureReadyFlagResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryActivityItemsRequest(TeaModel):
    def __init__(
        self,
        activity_id: int = None,
        extend_info: str = None,
        floor_index: int = None,
        mock: bool = None,
        page_index: int = None,
        page_size: int = None,
        refresh: bool = None,
        um_id: str = None,
    ):
        self.activity_id = activity_id
        self.extend_info = extend_info
        self.floor_index = floor_index
        self.mock = mock
        self.page_index = page_index
        self.page_size = page_size
        self.refresh = refresh
        self.um_id = um_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.activity_id is not None:
            result['ActivityId'] = self.activity_id
        if self.extend_info is not None:
            result['ExtendInfo'] = self.extend_info
        if self.floor_index is not None:
            result['FloorIndex'] = self.floor_index
        if self.mock is not None:
            result['Mock'] = self.mock
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.refresh is not None:
            result['Refresh'] = self.refresh
        if self.um_id is not None:
            result['UmId'] = self.um_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActivityId') is not None:
            self.activity_id = m.get('ActivityId')
        if m.get('ExtendInfo') is not None:
            self.extend_info = m.get('ExtendInfo')
        if m.get('FloorIndex') is not None:
            self.floor_index = m.get('FloorIndex')
        if m.get('Mock') is not None:
            self.mock = m.get('Mock')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Refresh') is not None:
            self.refresh = m.get('Refresh')
        if m.get('UmId') is not None:
            self.um_id = m.get('UmId')
        return self


class QueryActivityItemsResponseBodyModuleFloorDisplayInfosFloorSubTitlesSubFloor(TeaModel):
    def __init__(
        self,
        icon: str = None,
        name: str = None,
        title: str = None,
        value: str = None,
    ):
        self.icon = icon
        self.name = name
        self.title = title
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.icon is not None:
            result['Icon'] = self.icon
        if self.name is not None:
            result['Name'] = self.name
        if self.title is not None:
            result['Title'] = self.title
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class QueryActivityItemsResponseBodyModuleFloorDisplayInfosFloorSubTitles(TeaModel):
    def __init__(
        self,
        sub_floor: List[QueryActivityItemsResponseBodyModuleFloorDisplayInfosFloorSubTitlesSubFloor] = None,
    ):
        self.sub_floor = sub_floor

    def validate(self):
        if self.sub_floor:
            for k in self.sub_floor:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['subFloor'] = []
        if self.sub_floor is not None:
            for k in self.sub_floor:
                result['subFloor'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.sub_floor = []
        if m.get('subFloor') is not None:
            for k in m.get('subFloor'):
                temp_model = QueryActivityItemsResponseBodyModuleFloorDisplayInfosFloorSubTitlesSubFloor()
                self.sub_floor.append(temp_model.from_map(k))
        return self


class QueryActivityItemsResponseBodyModuleFloorDisplayInfosFloor(TeaModel):
    def __init__(
        self,
        icon: str = None,
        index: int = None,
        name: str = None,
        sub_titles: QueryActivityItemsResponseBodyModuleFloorDisplayInfosFloorSubTitles = None,
        title: str = None,
    ):
        self.icon = icon
        self.index = index
        self.name = name
        self.sub_titles = sub_titles
        self.title = title

    def validate(self):
        if self.sub_titles:
            self.sub_titles.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.icon is not None:
            result['Icon'] = self.icon
        if self.index is not None:
            result['Index'] = self.index
        if self.name is not None:
            result['Name'] = self.name
        if self.sub_titles is not None:
            result['SubTitles'] = self.sub_titles.to_map()
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SubTitles') is not None:
            temp_model = QueryActivityItemsResponseBodyModuleFloorDisplayInfosFloorSubTitles()
            self.sub_titles = temp_model.from_map(m['SubTitles'])
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class QueryActivityItemsResponseBodyModuleFloorDisplayInfos(TeaModel):
    def __init__(
        self,
        floor: List[QueryActivityItemsResponseBodyModuleFloorDisplayInfosFloor] = None,
    ):
        self.floor = floor

    def validate(self):
        if self.floor:
            for k in self.floor:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['floor'] = []
        if self.floor is not None:
            for k in self.floor:
                result['floor'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.floor = []
        if m.get('floor') is not None:
            for k in m.get('floor'):
                temp_model = QueryActivityItemsResponseBodyModuleFloorDisplayInfosFloor()
                self.floor.append(temp_model.from_map(k))
        return self


class QueryActivityItemsResponseBodyModule(TeaModel):
    def __init__(
        self,
        data: str = None,
        floor_display_infos: QueryActivityItemsResponseBodyModuleFloorDisplayInfos = None,
        floor_items: str = None,
    ):
        self.data = data
        self.floor_display_infos = floor_display_infos
        self.floor_items = floor_items

    def validate(self):
        if self.floor_display_infos:
            self.floor_display_infos.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.floor_display_infos is not None:
            result['FloorDisplayInfos'] = self.floor_display_infos.to_map()
        if self.floor_items is not None:
            result['FloorItems'] = self.floor_items
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('FloorDisplayInfos') is not None:
            temp_model = QueryActivityItemsResponseBodyModuleFloorDisplayInfos()
            self.floor_display_infos = temp_model.from_map(m['FloorDisplayInfos'])
        if m.get('FloorItems') is not None:
            self.floor_items = m.get('FloorItems')
        return self


class QueryActivityItemsResponseBody(TeaModel):
    def __init__(
        self,
        module: QueryActivityItemsResponseBodyModule = None,
    ):
        self.module = module

    def validate(self):
        if self.module:
            self.module.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.module is not None:
            result['Module'] = self.module.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Module') is not None:
            temp_model = QueryActivityItemsResponseBodyModule()
            self.module = temp_model.from_map(m['Module'])
        return self


class QueryActivityItemsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryActivityItemsResponseBody = None,
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
            temp_model = QueryActivityItemsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryAliyunUidRequest(TeaModel):
    def __init__(
        self,
        tb_uid: str = None,
    ):
        self.tb_uid = tb_uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tb_uid is not None:
            result['TbUid'] = self.tb_uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TbUid') is not None:
            self.tb_uid = m.get('TbUid')
        return self


class QueryAliyunUidResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        uid: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.uid = uid

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
        if self.uid is not None:
            result['Uid'] = self.uid
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
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        return self


class QueryAliyunUidResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryAliyunUidResponseBody = None,
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
            temp_model = QueryAliyunUidResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryDetailItemRequest(TeaModel):
    def __init__(
        self,
        detail_convert_type: str = None,
        detail_id: str = None,
        detail_type: str = None,
        mock: bool = None,
    ):
        self.detail_convert_type = detail_convert_type
        self.detail_id = detail_id
        self.detail_type = detail_type
        self.mock = mock

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.detail_convert_type is not None:
            result['DetailConvertType'] = self.detail_convert_type
        if self.detail_id is not None:
            result['DetailId'] = self.detail_id
        if self.detail_type is not None:
            result['DetailType'] = self.detail_type
        if self.mock is not None:
            result['Mock'] = self.mock
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DetailConvertType') is not None:
            self.detail_convert_type = m.get('DetailConvertType')
        if m.get('DetailId') is not None:
            self.detail_id = m.get('DetailId')
        if m.get('DetailType') is not None:
            self.detail_type = m.get('DetailType')
        if m.get('Mock') is not None:
            self.mock = m.get('Mock')
        return self


class QueryDetailItemResponseBodyModuleAttributesAttribute(TeaModel):
    def __init__(
        self,
        name: str = None,
        title: str = None,
        value: str = None,
    ):
        self.name = name
        self.title = title
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
        if self.title is not None:
            result['Title'] = self.title
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class QueryDetailItemResponseBodyModuleAttributes(TeaModel):
    def __init__(
        self,
        attribute: List[QueryDetailItemResponseBodyModuleAttributesAttribute] = None,
    ):
        self.attribute = attribute

    def validate(self):
        if self.attribute:
            for k in self.attribute:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['attribute'] = []
        if self.attribute is not None:
            for k in self.attribute:
                result['attribute'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.attribute = []
        if m.get('attribute') is not None:
            for k in m.get('attribute'):
                temp_model = QueryDetailItemResponseBodyModuleAttributesAttribute()
                self.attribute.append(temp_model.from_map(k))
        return self


class QueryDetailItemResponseBodyModuleDetailPicUrl(TeaModel):
    def __init__(
        self,
        pic_ulr: List[str] = None,
    ):
        self.pic_ulr = pic_ulr

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pic_ulr is not None:
            result['picUlr'] = self.pic_ulr
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('picUlr') is not None:
            self.pic_ulr = m.get('picUlr')
        return self


class QueryDetailItemResponseBodyModule(TeaModel):
    def __init__(
        self,
        attributes: QueryDetailItemResponseBodyModuleAttributes = None,
        detail_description: str = None,
        detail_object_json: str = None,
        detail_page_pic_url: str = None,
        detail_pic_url: QueryDetailItemResponseBodyModuleDetailPicUrl = None,
        label: str = None,
        main_pic_url: str = None,
        title: str = None,
        type: str = None,
    ):
        self.attributes = attributes
        self.detail_description = detail_description
        self.detail_object_json = detail_object_json
        self.detail_page_pic_url = detail_page_pic_url
        self.detail_pic_url = detail_pic_url
        self.label = label
        self.main_pic_url = main_pic_url
        self.title = title
        self.type = type

    def validate(self):
        if self.attributes:
            self.attributes.validate()
        if self.detail_pic_url:
            self.detail_pic_url.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attributes is not None:
            result['Attributes'] = self.attributes.to_map()
        if self.detail_description is not None:
            result['DetailDescription'] = self.detail_description
        if self.detail_object_json is not None:
            result['DetailObjectJson'] = self.detail_object_json
        if self.detail_page_pic_url is not None:
            result['DetailPagePicUrl'] = self.detail_page_pic_url
        if self.detail_pic_url is not None:
            result['DetailPicUrl'] = self.detail_pic_url.to_map()
        if self.label is not None:
            result['Label'] = self.label
        if self.main_pic_url is not None:
            result['MainPicUrl'] = self.main_pic_url
        if self.title is not None:
            result['Title'] = self.title
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Attributes') is not None:
            temp_model = QueryDetailItemResponseBodyModuleAttributes()
            self.attributes = temp_model.from_map(m['Attributes'])
        if m.get('DetailDescription') is not None:
            self.detail_description = m.get('DetailDescription')
        if m.get('DetailObjectJson') is not None:
            self.detail_object_json = m.get('DetailObjectJson')
        if m.get('DetailPagePicUrl') is not None:
            self.detail_page_pic_url = m.get('DetailPagePicUrl')
        if m.get('DetailPicUrl') is not None:
            temp_model = QueryDetailItemResponseBodyModuleDetailPicUrl()
            self.detail_pic_url = temp_model.from_map(m['DetailPicUrl'])
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('MainPicUrl') is not None:
            self.main_pic_url = m.get('MainPicUrl')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class QueryDetailItemResponseBody(TeaModel):
    def __init__(
        self,
        module: QueryDetailItemResponseBodyModule = None,
    ):
        self.module = module

    def validate(self):
        if self.module:
            self.module.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.module is not None:
            result['Module'] = self.module.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Module') is not None:
            temp_model = QueryDetailItemResponseBodyModule()
            self.module = temp_model.from_map(m['Module'])
        return self


class QueryDetailItemResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryDetailItemResponseBody = None,
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
            temp_model = QueryDetailItemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryRemainResourcesRequest(TeaModel):
    def __init__(
        self,
        biz_type: str = None,
    ):
        self.biz_type = biz_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        return self


class QueryRemainResourcesResponseBody(TeaModel):
    def __init__(
        self,
        data: int = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryRemainResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryRemainResourcesResponseBody = None,
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
            temp_model = QueryRemainResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RefuseSupplementRequest(TeaModel):
    def __init__(
        self,
        supplement_id: int = None,
    ):
        self.supplement_id = supplement_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.supplement_id is not None:
            result['SupplementId'] = self.supplement_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SupplementId') is not None:
            self.supplement_id = m.get('SupplementId')
        return self


class RefuseSupplementResponseBody(TeaModel):
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


class RefuseSupplementResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RefuseSupplementResponseBody = None,
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
            temp_model = RefuseSupplementResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RejectExpertSolutionRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        note: str = None,
    ):
        self.biz_id = biz_id
        self.note = note

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.note is not None:
            result['Note'] = self.note
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        return self


class RejectExpertSolutionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RejectExpertSolutionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RejectExpertSolutionResponseBody = None,
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
            temp_model = RejectExpertSolutionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveApplicantRequest(TeaModel):
    def __init__(
        self,
        applicant_id: int = None,
    ):
        self.applicant_id = applicant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.applicant_id is not None:
            result['ApplicantId'] = self.applicant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicantId') is not None:
            self.applicant_id = m.get('ApplicantId')
        return self


class RemoveApplicantResponseBody(TeaModel):
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


class RemoveApplicantResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RemoveApplicantResponseBody = None,
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
            temp_model = RemoveApplicantResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveSearchConditionRequest(TeaModel):
    def __init__(
        self,
        condition_content: str = None,
        session_id: str = None,
        tag_name: str = None,
        type: int = None,
        umid: str = None,
    ):
        self.condition_content = condition_content
        self.session_id = session_id
        self.tag_name = tag_name
        self.type = type
        self.umid = umid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.condition_content is not None:
            result['ConditionContent'] = self.condition_content
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.tag_name is not None:
            result['TagName'] = self.tag_name
        if self.type is not None:
            result['Type'] = self.type
        if self.umid is not None:
            result['Umid'] = self.umid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConditionContent') is not None:
            self.condition_content = m.get('ConditionContent')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Umid') is not None:
            self.umid = m.get('Umid')
        return self


class SaveSearchConditionResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        condition_content: str = None,
        condition_id: int = None,
        message: str = None,
        request_id: str = None,
        session_id: str = None,
        success: bool = None,
        tag_name: str = None,
        type: int = None,
        umid: str = None,
        user_id: int = None,
    ):
        self.code = code
        self.condition_content = condition_content
        self.condition_id = condition_id
        self.message = message
        self.request_id = request_id
        self.session_id = session_id
        self.success = success
        self.tag_name = tag_name
        self.type = type
        self.umid = umid
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.condition_content is not None:
            result['ConditionContent'] = self.condition_content
        if self.condition_id is not None:
            result['ConditionId'] = self.condition_id
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.success is not None:
            result['Success'] = self.success
        if self.tag_name is not None:
            result['TagName'] = self.tag_name
        if self.type is not None:
            result['Type'] = self.type
        if self.umid is not None:
            result['Umid'] = self.umid
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ConditionContent') is not None:
            self.condition_content = m.get('ConditionContent')
        if m.get('ConditionId') is not None:
            self.condition_id = m.get('ConditionId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Umid') is not None:
            self.umid = m.get('Umid')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class SaveSearchConditionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SaveSearchConditionResponseBody = None,
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
            temp_model = SaveSearchConditionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveTemporaryApplicantRequest(TeaModel):
    def __init__(
        self,
        address: str = None,
        applicant_id: int = None,
        business_licence_oss_key: str = None,
        card_number: str = None,
        city: str = None,
        complete_applicant: bool = None,
        contact_address: str = None,
        contact_city: str = None,
        contact_county: str = None,
        contact_district: str = None,
        contact_email: str = None,
        contact_name: str = None,
        contact_number: str = None,
        contact_province: str = None,
        contact_zip_code: str = None,
        country: str = None,
        eaddress: str = None,
        ename: str = None,
        id_card_oss_key: str = None,
        legal_notice_oss_key: str = None,
        loa_oss_key: str = None,
        name: str = None,
        passport_oss_key: str = None,
        principal_name: int = None,
        province: str = None,
        region: str = None,
        town: str = None,
        type: str = None,
    ):
        self.address = address
        self.applicant_id = applicant_id
        self.business_licence_oss_key = business_licence_oss_key
        self.card_number = card_number
        self.city = city
        self.complete_applicant = complete_applicant
        self.contact_address = contact_address
        self.contact_city = contact_city
        self.contact_county = contact_county
        self.contact_district = contact_district
        self.contact_email = contact_email
        self.contact_name = contact_name
        self.contact_number = contact_number
        self.contact_province = contact_province
        self.contact_zip_code = contact_zip_code
        self.country = country
        self.eaddress = eaddress
        self.ename = ename
        self.id_card_oss_key = id_card_oss_key
        self.legal_notice_oss_key = legal_notice_oss_key
        self.loa_oss_key = loa_oss_key
        self.name = name
        self.passport_oss_key = passport_oss_key
        self.principal_name = principal_name
        self.province = province
        self.region = region
        self.town = town
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
        if self.applicant_id is not None:
            result['ApplicantId'] = self.applicant_id
        if self.business_licence_oss_key is not None:
            result['BusinessLicenceOssKey'] = self.business_licence_oss_key
        if self.card_number is not None:
            result['CardNumber'] = self.card_number
        if self.city is not None:
            result['City'] = self.city
        if self.complete_applicant is not None:
            result['CompleteApplicant'] = self.complete_applicant
        if self.contact_address is not None:
            result['ContactAddress'] = self.contact_address
        if self.contact_city is not None:
            result['ContactCity'] = self.contact_city
        if self.contact_county is not None:
            result['ContactCounty'] = self.contact_county
        if self.contact_district is not None:
            result['ContactDistrict'] = self.contact_district
        if self.contact_email is not None:
            result['ContactEmail'] = self.contact_email
        if self.contact_name is not None:
            result['ContactName'] = self.contact_name
        if self.contact_number is not None:
            result['ContactNumber'] = self.contact_number
        if self.contact_province is not None:
            result['ContactProvince'] = self.contact_province
        if self.contact_zip_code is not None:
            result['ContactZipCode'] = self.contact_zip_code
        if self.country is not None:
            result['Country'] = self.country
        if self.eaddress is not None:
            result['EAddress'] = self.eaddress
        if self.ename is not None:
            result['EName'] = self.ename
        if self.id_card_oss_key is not None:
            result['IdCardOssKey'] = self.id_card_oss_key
        if self.legal_notice_oss_key is not None:
            result['LegalNoticeOssKey'] = self.legal_notice_oss_key
        if self.loa_oss_key is not None:
            result['LoaOssKey'] = self.loa_oss_key
        if self.name is not None:
            result['Name'] = self.name
        if self.passport_oss_key is not None:
            result['PassportOssKey'] = self.passport_oss_key
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name
        if self.province is not None:
            result['Province'] = self.province
        if self.region is not None:
            result['Region'] = self.region
        if self.town is not None:
            result['Town'] = self.town
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('ApplicantId') is not None:
            self.applicant_id = m.get('ApplicantId')
        if m.get('BusinessLicenceOssKey') is not None:
            self.business_licence_oss_key = m.get('BusinessLicenceOssKey')
        if m.get('CardNumber') is not None:
            self.card_number = m.get('CardNumber')
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('CompleteApplicant') is not None:
            self.complete_applicant = m.get('CompleteApplicant')
        if m.get('ContactAddress') is not None:
            self.contact_address = m.get('ContactAddress')
        if m.get('ContactCity') is not None:
            self.contact_city = m.get('ContactCity')
        if m.get('ContactCounty') is not None:
            self.contact_county = m.get('ContactCounty')
        if m.get('ContactDistrict') is not None:
            self.contact_district = m.get('ContactDistrict')
        if m.get('ContactEmail') is not None:
            self.contact_email = m.get('ContactEmail')
        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')
        if m.get('ContactNumber') is not None:
            self.contact_number = m.get('ContactNumber')
        if m.get('ContactProvince') is not None:
            self.contact_province = m.get('ContactProvince')
        if m.get('ContactZipCode') is not None:
            self.contact_zip_code = m.get('ContactZipCode')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('EAddress') is not None:
            self.eaddress = m.get('EAddress')
        if m.get('EName') is not None:
            self.ename = m.get('EName')
        if m.get('IdCardOssKey') is not None:
            self.id_card_oss_key = m.get('IdCardOssKey')
        if m.get('LegalNoticeOssKey') is not None:
            self.legal_notice_oss_key = m.get('LegalNoticeOssKey')
        if m.get('LoaOssKey') is not None:
            self.loa_oss_key = m.get('LoaOssKey')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PassportOssKey') is not None:
            self.passport_oss_key = m.get('PassportOssKey')
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Town') is not None:
            self.town = m.get('Town')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class SaveTemporaryApplicantResponseBody(TeaModel):
    def __init__(
        self,
        applicant_id: int = None,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.applicant_id = applicant_id
        self.error_code = error_code
        self.error_message = error_message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.applicant_id is not None:
            result['ApplicantId'] = self.applicant_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicantId') is not None:
            self.applicant_id = m.get('ApplicantId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SaveTemporaryApplicantResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SaveTemporaryApplicantResponseBody = None,
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
            temp_model = SaveTemporaryApplicantResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchItemsRequest(TeaModel):
    def __init__(
        self,
        excluded_tags: str = None,
        excluded_uids: str = None,
        feeds_type: bool = None,
        int_cls: str = None,
        keywords: str = None,
        mock: bool = None,
        page_index: int = None,
        page_size: int = None,
        price_left: str = None,
        price_right: str = None,
        products: str = None,
        register_number: str = None,
        sort: str = None,
        sort_type: int = None,
        tags: str = None,
        trademark_name_length: int = None,
        trademark_name_type: str = None,
        um_id: str = None,
    ):
        self.excluded_tags = excluded_tags
        self.excluded_uids = excluded_uids
        self.feeds_type = feeds_type
        self.int_cls = int_cls
        self.keywords = keywords
        self.mock = mock
        self.page_index = page_index
        self.page_size = page_size
        self.price_left = price_left
        self.price_right = price_right
        self.products = products
        self.register_number = register_number
        self.sort = sort
        self.sort_type = sort_type
        self.tags = tags
        self.trademark_name_length = trademark_name_length
        self.trademark_name_type = trademark_name_type
        self.um_id = um_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.excluded_tags is not None:
            result['ExcludedTags'] = self.excluded_tags
        if self.excluded_uids is not None:
            result['ExcludedUids'] = self.excluded_uids
        if self.feeds_type is not None:
            result['FeedsType'] = self.feeds_type
        if self.int_cls is not None:
            result['IntCls'] = self.int_cls
        if self.keywords is not None:
            result['Keywords'] = self.keywords
        if self.mock is not None:
            result['Mock'] = self.mock
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.price_left is not None:
            result['PriceLeft'] = self.price_left
        if self.price_right is not None:
            result['PriceRight'] = self.price_right
        if self.products is not None:
            result['Products'] = self.products
        if self.register_number is not None:
            result['RegisterNumber'] = self.register_number
        if self.sort is not None:
            result['Sort'] = self.sort
        if self.sort_type is not None:
            result['SortType'] = self.sort_type
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.trademark_name_length is not None:
            result['TrademarkNameLength'] = self.trademark_name_length
        if self.trademark_name_type is not None:
            result['TrademarkNameType'] = self.trademark_name_type
        if self.um_id is not None:
            result['UmId'] = self.um_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExcludedTags') is not None:
            self.excluded_tags = m.get('ExcludedTags')
        if m.get('ExcludedUids') is not None:
            self.excluded_uids = m.get('ExcludedUids')
        if m.get('FeedsType') is not None:
            self.feeds_type = m.get('FeedsType')
        if m.get('IntCls') is not None:
            self.int_cls = m.get('IntCls')
        if m.get('Keywords') is not None:
            self.keywords = m.get('Keywords')
        if m.get('Mock') is not None:
            self.mock = m.get('Mock')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PriceLeft') is not None:
            self.price_left = m.get('PriceLeft')
        if m.get('PriceRight') is not None:
            self.price_right = m.get('PriceRight')
        if m.get('Products') is not None:
            self.products = m.get('Products')
        if m.get('RegisterNumber') is not None:
            self.register_number = m.get('RegisterNumber')
        if m.get('Sort') is not None:
            self.sort = m.get('Sort')
        if m.get('SortType') is not None:
            self.sort_type = m.get('SortType')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('TrademarkNameLength') is not None:
            self.trademark_name_length = m.get('TrademarkNameLength')
        if m.get('TrademarkNameType') is not None:
            self.trademark_name_type = m.get('TrademarkNameType')
        if m.get('UmId') is not None:
            self.um_id = m.get('UmId')
        return self


class SearchItemsResponseBodyModuleDateItem(TeaModel):
    def __init__(
        self,
        detail_view_object_source_datum: str = None,
        detail_view_object_source_type: str = None,
    ):
        self.detail_view_object_source_datum = detail_view_object_source_datum
        self.detail_view_object_source_type = detail_view_object_source_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.detail_view_object_source_datum is not None:
            result['DetailViewObjectSourceDatum'] = self.detail_view_object_source_datum
        if self.detail_view_object_source_type is not None:
            result['DetailViewObjectSourceType'] = self.detail_view_object_source_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DetailViewObjectSourceDatum') is not None:
            self.detail_view_object_source_datum = m.get('DetailViewObjectSourceDatum')
        if m.get('DetailViewObjectSourceType') is not None:
            self.detail_view_object_source_type = m.get('DetailViewObjectSourceType')
        return self


class SearchItemsResponseBodyModuleDate(TeaModel):
    def __init__(
        self,
        item: List[SearchItemsResponseBodyModuleDateItem] = None,
    ):
        self.item = item

    def validate(self):
        if self.item:
            for k in self.item:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['item'] = []
        if self.item is not None:
            for k in self.item:
                result['item'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.item = []
        if m.get('item') is not None:
            for k in m.get('item'):
                temp_model = SearchItemsResponseBodyModuleDateItem()
                self.item.append(temp_model.from_map(k))
        return self


class SearchItemsResponseBodyModule(TeaModel):
    def __init__(
        self,
        current_page_num: int = None,
        date: SearchItemsResponseBodyModuleDate = None,
        page_size: int = None,
        total_item_num: int = None,
        total_page_num: int = None,
    ):
        self.current_page_num = current_page_num
        self.date = date
        self.page_size = page_size
        self.total_item_num = total_item_num
        self.total_page_num = total_page_num

    def validate(self):
        if self.date:
            self.date.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page_num is not None:
            result['CurrentPageNum'] = self.current_page_num
        if self.date is not None:
            result['Date'] = self.date.to_map()
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_item_num is not None:
            result['TotalItemNum'] = self.total_item_num
        if self.total_page_num is not None:
            result['TotalPageNum'] = self.total_page_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPageNum') is not None:
            self.current_page_num = m.get('CurrentPageNum')
        if m.get('Date') is not None:
            temp_model = SearchItemsResponseBodyModuleDate()
            self.date = temp_model.from_map(m['Date'])
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalItemNum') is not None:
            self.total_item_num = m.get('TotalItemNum')
        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')
        return self


class SearchItemsResponseBody(TeaModel):
    def __init__(
        self,
        module: SearchItemsResponseBodyModule = None,
    ):
        self.module = module

    def validate(self):
        if self.module:
            self.module.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.module is not None:
            result['Module'] = self.module.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Module') is not None:
            temp_model = SearchItemsResponseBodyModule()
            self.module = temp_model.from_map(m['Module'])
        return self


class SearchItemsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SearchItemsResponseBody = None,
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
            temp_model = SearchItemsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchSimilarityRequestNameUriList(TeaModel):
    def __init__(
        self,
        name: str = None,
        uri: str = None,
    ):
        self.name = name
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.uri is not None:
            result['Uri'] = self.uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Uri') is not None:
            self.uri = m.get('Uri')
        return self


class SearchSimilarityRequest(TeaModel):
    def __init__(
        self,
        classifications: Dict[str, Any] = None,
        limit: int = None,
        name_uri_list: List[SearchSimilarityRequestNameUriList] = None,
        search_type: str = None,
        show_detail: bool = None,
        similar_groups: Dict[str, Any] = None,
        sorter: str = None,
        umid: str = None,
    ):
        self.classifications = classifications
        self.limit = limit
        self.name_uri_list = name_uri_list
        self.search_type = search_type
        self.show_detail = show_detail
        self.similar_groups = similar_groups
        self.sorter = sorter
        self.umid = umid

    def validate(self):
        if self.name_uri_list:
            for k in self.name_uri_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.classifications is not None:
            result['Classifications'] = self.classifications
        if self.limit is not None:
            result['Limit'] = self.limit
        result['NameUriList'] = []
        if self.name_uri_list is not None:
            for k in self.name_uri_list:
                result['NameUriList'].append(k.to_map() if k else None)
        if self.search_type is not None:
            result['SearchType'] = self.search_type
        if self.show_detail is not None:
            result['ShowDetail'] = self.show_detail
        if self.similar_groups is not None:
            result['SimilarGroups'] = self.similar_groups
        if self.sorter is not None:
            result['Sorter'] = self.sorter
        if self.umid is not None:
            result['Umid'] = self.umid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Classifications') is not None:
            self.classifications = m.get('Classifications')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        self.name_uri_list = []
        if m.get('NameUriList') is not None:
            for k in m.get('NameUriList'):
                temp_model = SearchSimilarityRequestNameUriList()
                self.name_uri_list.append(temp_model.from_map(k))
        if m.get('SearchType') is not None:
            self.search_type = m.get('SearchType')
        if m.get('ShowDetail') is not None:
            self.show_detail = m.get('ShowDetail')
        if m.get('SimilarGroups') is not None:
            self.similar_groups = m.get('SimilarGroups')
        if m.get('Sorter') is not None:
            self.sorter = m.get('Sorter')
        if m.get('Umid') is not None:
            self.umid = m.get('Umid')
        return self


class SearchSimilarityShrinkRequestNameUriList(TeaModel):
    def __init__(
        self,
        name: str = None,
        uri: str = None,
    ):
        self.name = name
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.uri is not None:
            result['Uri'] = self.uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Uri') is not None:
            self.uri = m.get('Uri')
        return self


class SearchSimilarityShrinkRequest(TeaModel):
    def __init__(
        self,
        classifications_shrink: str = None,
        limit: int = None,
        name_uri_list: List[SearchSimilarityShrinkRequestNameUriList] = None,
        search_type: str = None,
        show_detail: bool = None,
        similar_groups_shrink: str = None,
        sorter: str = None,
        umid: str = None,
    ):
        self.classifications_shrink = classifications_shrink
        self.limit = limit
        self.name_uri_list = name_uri_list
        self.search_type = search_type
        self.show_detail = show_detail
        self.similar_groups_shrink = similar_groups_shrink
        self.sorter = sorter
        self.umid = umid

    def validate(self):
        if self.name_uri_list:
            for k in self.name_uri_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.classifications_shrink is not None:
            result['Classifications'] = self.classifications_shrink
        if self.limit is not None:
            result['Limit'] = self.limit
        result['NameUriList'] = []
        if self.name_uri_list is not None:
            for k in self.name_uri_list:
                result['NameUriList'].append(k.to_map() if k else None)
        if self.search_type is not None:
            result['SearchType'] = self.search_type
        if self.show_detail is not None:
            result['ShowDetail'] = self.show_detail
        if self.similar_groups_shrink is not None:
            result['SimilarGroups'] = self.similar_groups_shrink
        if self.sorter is not None:
            result['Sorter'] = self.sorter
        if self.umid is not None:
            result['Umid'] = self.umid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Classifications') is not None:
            self.classifications_shrink = m.get('Classifications')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        self.name_uri_list = []
        if m.get('NameUriList') is not None:
            for k in m.get('NameUriList'):
                temp_model = SearchSimilarityShrinkRequestNameUriList()
                self.name_uri_list.append(temp_model.from_map(k))
        if m.get('SearchType') is not None:
            self.search_type = m.get('SearchType')
        if m.get('ShowDetail') is not None:
            self.show_detail = m.get('ShowDetail')
        if m.get('SimilarGroups') is not None:
            self.similar_groups_shrink = m.get('SimilarGroups')
        if m.get('Sorter') is not None:
            self.sorter = m.get('Sorter')
        if m.get('Umid') is not None:
            self.umid = m.get('Umid')
        return self


class SearchSimilarityResponseBodyDataListClassificationSimilarityListSimilarGroupListDetailList(TeaModel):
    def __init__(
        self,
        code: str = None,
        name: str = None,
        rate: int = None,
        tm_number: str = None,
        uid: str = None,
        uri: str = None,
    ):
        self.code = code
        self.name = name
        self.rate = rate
        self.tm_number = tm_number
        self.uid = uid
        self.uri = uri

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
        if self.rate is not None:
            result['Rate'] = self.rate
        if self.tm_number is not None:
            result['TmNumber'] = self.tm_number
        if self.uid is not None:
            result['Uid'] = self.uid
        if self.uri is not None:
            result['Uri'] = self.uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Rate') is not None:
            self.rate = m.get('Rate')
        if m.get('TmNumber') is not None:
            self.tm_number = m.get('TmNumber')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        if m.get('Uri') is not None:
            self.uri = m.get('Uri')
        return self


class SearchSimilarityResponseBodyDataListClassificationSimilarityListSimilarGroupList(TeaModel):
    def __init__(
        self,
        detail_list: List[SearchSimilarityResponseBodyDataListClassificationSimilarityListSimilarGroupListDetailList] = None,
        rate: int = None,
        similar_group: str = None,
        similar_group_name: str = None,
    ):
        self.detail_list = detail_list
        self.rate = rate
        self.similar_group = similar_group
        self.similar_group_name = similar_group_name

    def validate(self):
        if self.detail_list:
            for k in self.detail_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DetailList'] = []
        if self.detail_list is not None:
            for k in self.detail_list:
                result['DetailList'].append(k.to_map() if k else None)
        if self.rate is not None:
            result['Rate'] = self.rate
        if self.similar_group is not None:
            result['SimilarGroup'] = self.similar_group
        if self.similar_group_name is not None:
            result['SimilarGroupName'] = self.similar_group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.detail_list = []
        if m.get('DetailList') is not None:
            for k in m.get('DetailList'):
                temp_model = SearchSimilarityResponseBodyDataListClassificationSimilarityListSimilarGroupListDetailList()
                self.detail_list.append(temp_model.from_map(k))
        if m.get('Rate') is not None:
            self.rate = m.get('Rate')
        if m.get('SimilarGroup') is not None:
            self.similar_group = m.get('SimilarGroup')
        if m.get('SimilarGroupName') is not None:
            self.similar_group_name = m.get('SimilarGroupName')
        return self


class SearchSimilarityResponseBodyDataListClassificationSimilarityList(TeaModel):
    def __init__(
        self,
        classification: int = None,
        classification_name: str = None,
        rate: int = None,
        similar_group_list: List[SearchSimilarityResponseBodyDataListClassificationSimilarityListSimilarGroupList] = None,
    ):
        self.classification = classification
        self.classification_name = classification_name
        self.rate = rate
        self.similar_group_list = similar_group_list

    def validate(self):
        if self.similar_group_list:
            for k in self.similar_group_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.classification is not None:
            result['Classification'] = self.classification
        if self.classification_name is not None:
            result['ClassificationName'] = self.classification_name
        if self.rate is not None:
            result['Rate'] = self.rate
        result['SimilarGroupList'] = []
        if self.similar_group_list is not None:
            for k in self.similar_group_list:
                result['SimilarGroupList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Classification') is not None:
            self.classification = m.get('Classification')
        if m.get('ClassificationName') is not None:
            self.classification_name = m.get('ClassificationName')
        if m.get('Rate') is not None:
            self.rate = m.get('Rate')
        self.similar_group_list = []
        if m.get('SimilarGroupList') is not None:
            for k in m.get('SimilarGroupList'):
                temp_model = SearchSimilarityResponseBodyDataListClassificationSimilarityListSimilarGroupList()
                self.similar_group_list.append(temp_model.from_map(k))
        return self


class SearchSimilarityResponseBodyDataList(TeaModel):
    def __init__(
        self,
        classification_similarity_list: List[SearchSimilarityResponseBodyDataListClassificationSimilarityList] = None,
        name: str = None,
        uri: str = None,
    ):
        self.classification_similarity_list = classification_similarity_list
        self.name = name
        self.uri = uri

    def validate(self):
        if self.classification_similarity_list:
            for k in self.classification_similarity_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ClassificationSimilarityList'] = []
        if self.classification_similarity_list is not None:
            for k in self.classification_similarity_list:
                result['ClassificationSimilarityList'].append(k.to_map() if k else None)
        if self.name is not None:
            result['Name'] = self.name
        if self.uri is not None:
            result['Uri'] = self.uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.classification_similarity_list = []
        if m.get('ClassificationSimilarityList') is not None:
            for k in m.get('ClassificationSimilarityList'):
                temp_model = SearchSimilarityResponseBodyDataListClassificationSimilarityList()
                self.classification_similarity_list.append(temp_model.from_map(k))
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Uri') is not None:
            self.uri = m.get('Uri')
        return self


class SearchSimilarityResponseBody(TeaModel):
    def __init__(
        self,
        data_list: List[SearchSimilarityResponseBodyDataList] = None,
        request_id: str = None,
    ):
        self.data_list = data_list
        self.request_id = request_id

    def validate(self):
        if self.data_list:
            for k in self.data_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataList'] = []
        if self.data_list is not None:
            for k in self.data_list:
                result['DataList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_list = []
        if m.get('DataList') is not None:
            for k in m.get('DataList'):
                temp_model = SearchSimilarityResponseBodyDataList()
                self.data_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SearchSimilarityResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SearchSimilarityResponseBody = None,
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
            temp_model = SearchSimilarityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchSimilarityListRequest(TeaModel):
    def __init__(
        self,
        classifications: Dict[str, Any] = None,
        name: str = None,
        order_id: str = None,
        page_number: int = None,
        page_size: int = None,
        similar_groups: Dict[str, Any] = None,
        status: int = None,
        success_search_type: str = None,
        umid: str = None,
        uri: str = None,
    ):
        self.classifications = classifications
        self.name = name
        self.order_id = order_id
        self.page_number = page_number
        self.page_size = page_size
        self.similar_groups = similar_groups
        self.status = status
        self.success_search_type = success_search_type
        self.umid = umid
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.classifications is not None:
            result['Classifications'] = self.classifications
        if self.name is not None:
            result['Name'] = self.name
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.similar_groups is not None:
            result['SimilarGroups'] = self.similar_groups
        if self.status is not None:
            result['Status'] = self.status
        if self.success_search_type is not None:
            result['SuccessSearchType'] = self.success_search_type
        if self.umid is not None:
            result['Umid'] = self.umid
        if self.uri is not None:
            result['Uri'] = self.uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Classifications') is not None:
            self.classifications = m.get('Classifications')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SimilarGroups') is not None:
            self.similar_groups = m.get('SimilarGroups')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SuccessSearchType') is not None:
            self.success_search_type = m.get('SuccessSearchType')
        if m.get('Umid') is not None:
            self.umid = m.get('Umid')
        if m.get('Uri') is not None:
            self.uri = m.get('Uri')
        return self


class SearchSimilarityListShrinkRequest(TeaModel):
    def __init__(
        self,
        classifications_shrink: str = None,
        name: str = None,
        order_id: str = None,
        page_number: int = None,
        page_size: int = None,
        similar_groups_shrink: str = None,
        status: int = None,
        success_search_type: str = None,
        umid: str = None,
        uri: str = None,
    ):
        self.classifications_shrink = classifications_shrink
        self.name = name
        self.order_id = order_id
        self.page_number = page_number
        self.page_size = page_size
        self.similar_groups_shrink = similar_groups_shrink
        self.status = status
        self.success_search_type = success_search_type
        self.umid = umid
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.classifications_shrink is not None:
            result['Classifications'] = self.classifications_shrink
        if self.name is not None:
            result['Name'] = self.name
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.similar_groups_shrink is not None:
            result['SimilarGroups'] = self.similar_groups_shrink
        if self.status is not None:
            result['Status'] = self.status
        if self.success_search_type is not None:
            result['SuccessSearchType'] = self.success_search_type
        if self.umid is not None:
            result['Umid'] = self.umid
        if self.uri is not None:
            result['Uri'] = self.uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Classifications') is not None:
            self.classifications_shrink = m.get('Classifications')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SimilarGroups') is not None:
            self.similar_groups_shrink = m.get('SimilarGroups')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SuccessSearchType') is not None:
            self.success_search_type = m.get('SuccessSearchType')
        if m.get('Umid') is not None:
            self.umid = m.get('Umid')
        if m.get('Uri') is not None:
            self.uri = m.get('Uri')
        return self


class SearchSimilarityListResponseBodyData(TeaModel):
    def __init__(
        self,
        apply_date: str = None,
        classification: str = None,
        exclusive_date_limit: str = None,
        id: int = None,
        image: str = None,
        last_procedure_status: str = None,
        name: str = None,
        on_sale: int = None,
        owner_address: str = None,
        owner_en_address: str = None,
        owner_en_name: str = None,
        owner_name: str = None,
        pre_ann_date: str = None,
        pre_ann_num: str = None,
        product: str = None,
        product_desc: str = None,
        reg_ann_date: str = None,
        reg_ann_num: str = None,
        registration_number: str = None,
        share: str = None,
        status: str = None,
        uid: str = None,
    ):
        self.apply_date = apply_date
        self.classification = classification
        self.exclusive_date_limit = exclusive_date_limit
        self.id = id
        self.image = image
        self.last_procedure_status = last_procedure_status
        self.name = name
        self.on_sale = on_sale
        self.owner_address = owner_address
        self.owner_en_address = owner_en_address
        self.owner_en_name = owner_en_name
        self.owner_name = owner_name
        self.pre_ann_date = pre_ann_date
        self.pre_ann_num = pre_ann_num
        self.product = product
        self.product_desc = product_desc
        self.reg_ann_date = reg_ann_date
        self.reg_ann_num = reg_ann_num
        self.registration_number = registration_number
        self.share = share
        self.status = status
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apply_date is not None:
            result['ApplyDate'] = self.apply_date
        if self.classification is not None:
            result['Classification'] = self.classification
        if self.exclusive_date_limit is not None:
            result['ExclusiveDateLimit'] = self.exclusive_date_limit
        if self.id is not None:
            result['Id'] = self.id
        if self.image is not None:
            result['Image'] = self.image
        if self.last_procedure_status is not None:
            result['LastProcedureStatus'] = self.last_procedure_status
        if self.name is not None:
            result['Name'] = self.name
        if self.on_sale is not None:
            result['OnSale'] = self.on_sale
        if self.owner_address is not None:
            result['OwnerAddress'] = self.owner_address
        if self.owner_en_address is not None:
            result['OwnerEnAddress'] = self.owner_en_address
        if self.owner_en_name is not None:
            result['OwnerEnName'] = self.owner_en_name
        if self.owner_name is not None:
            result['OwnerName'] = self.owner_name
        if self.pre_ann_date is not None:
            result['PreAnnDate'] = self.pre_ann_date
        if self.pre_ann_num is not None:
            result['PreAnnNum'] = self.pre_ann_num
        if self.product is not None:
            result['Product'] = self.product
        if self.product_desc is not None:
            result['ProductDesc'] = self.product_desc
        if self.reg_ann_date is not None:
            result['RegAnnDate'] = self.reg_ann_date
        if self.reg_ann_num is not None:
            result['RegAnnNum'] = self.reg_ann_num
        if self.registration_number is not None:
            result['RegistrationNumber'] = self.registration_number
        if self.share is not None:
            result['Share'] = self.share
        if self.status is not None:
            result['Status'] = self.status
        if self.uid is not None:
            result['Uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplyDate') is not None:
            self.apply_date = m.get('ApplyDate')
        if m.get('Classification') is not None:
            self.classification = m.get('Classification')
        if m.get('ExclusiveDateLimit') is not None:
            self.exclusive_date_limit = m.get('ExclusiveDateLimit')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Image') is not None:
            self.image = m.get('Image')
        if m.get('LastProcedureStatus') is not None:
            self.last_procedure_status = m.get('LastProcedureStatus')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OnSale') is not None:
            self.on_sale = m.get('OnSale')
        if m.get('OwnerAddress') is not None:
            self.owner_address = m.get('OwnerAddress')
        if m.get('OwnerEnAddress') is not None:
            self.owner_en_address = m.get('OwnerEnAddress')
        if m.get('OwnerEnName') is not None:
            self.owner_en_name = m.get('OwnerEnName')
        if m.get('OwnerName') is not None:
            self.owner_name = m.get('OwnerName')
        if m.get('PreAnnDate') is not None:
            self.pre_ann_date = m.get('PreAnnDate')
        if m.get('PreAnnNum') is not None:
            self.pre_ann_num = m.get('PreAnnNum')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('ProductDesc') is not None:
            self.product_desc = m.get('ProductDesc')
        if m.get('RegAnnDate') is not None:
            self.reg_ann_date = m.get('RegAnnDate')
        if m.get('RegAnnNum') is not None:
            self.reg_ann_num = m.get('RegAnnNum')
        if m.get('RegistrationNumber') is not None:
            self.registration_number = m.get('RegistrationNumber')
        if m.get('Share') is not None:
            self.share = m.get('Share')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        return self


class SearchSimilarityListResponseBody(TeaModel):
    def __init__(
        self,
        data: List[SearchSimilarityListResponseBodyData] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.data = data
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

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
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = SearchSimilarityListResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class SearchSimilarityListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SearchSimilarityListResponseBody = None,
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
            temp_model = SearchSimilarityListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendMessageToUserRequest(TeaModel):
    def __init__(
        self,
        receiver_nick_name: str = None,
        sender_nick_name: str = None,
        template_data: Dict[str, Any] = None,
        template_id: str = None,
    ):
        self.receiver_nick_name = receiver_nick_name
        self.sender_nick_name = sender_nick_name
        self.template_data = template_data
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.receiver_nick_name is not None:
            result['ReceiverNickName'] = self.receiver_nick_name
        if self.sender_nick_name is not None:
            result['SenderNickName'] = self.sender_nick_name
        if self.template_data is not None:
            result['TemplateData'] = self.template_data
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReceiverNickName') is not None:
            self.receiver_nick_name = m.get('ReceiverNickName')
        if m.get('SenderNickName') is not None:
            self.sender_nick_name = m.get('SenderNickName')
        if m.get('TemplateData') is not None:
            self.template_data = m.get('TemplateData')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class SendMessageToUserShrinkRequest(TeaModel):
    def __init__(
        self,
        receiver_nick_name: str = None,
        sender_nick_name: str = None,
        template_data_shrink: str = None,
        template_id: str = None,
    ):
        self.receiver_nick_name = receiver_nick_name
        self.sender_nick_name = sender_nick_name
        self.template_data_shrink = template_data_shrink
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.receiver_nick_name is not None:
            result['ReceiverNickName'] = self.receiver_nick_name
        if self.sender_nick_name is not None:
            result['SenderNickName'] = self.sender_nick_name
        if self.template_data_shrink is not None:
            result['TemplateData'] = self.template_data_shrink
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReceiverNickName') is not None:
            self.receiver_nick_name = m.get('ReceiverNickName')
        if m.get('SenderNickName') is not None:
            self.sender_nick_name = m.get('SenderNickName')
        if m.get('TemplateData') is not None:
            self.template_data_shrink = m.get('TemplateData')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class SendMessageToUserResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SendMessageToUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SendMessageToUserResponseBody = None,
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
            temp_model = SendMessageToUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitSupplementRequest(TeaModel):
    def __init__(
        self,
        content: str = None,
        supplement_id: int = None,
        user_files: Dict[str, Any] = None,
    ):
        self.content = content
        self.supplement_id = supplement_id
        self.user_files = user_files

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.supplement_id is not None:
            result['SupplementId'] = self.supplement_id
        if self.user_files is not None:
            result['UserFiles'] = self.user_files
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('SupplementId') is not None:
            self.supplement_id = m.get('SupplementId')
        if m.get('UserFiles') is not None:
            self.user_files = m.get('UserFiles')
        return self


class SubmitSupplementShrinkRequest(TeaModel):
    def __init__(
        self,
        content: str = None,
        supplement_id: int = None,
        user_files_shrink: str = None,
    ):
        self.content = content
        self.supplement_id = supplement_id
        self.user_files_shrink = user_files_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.supplement_id is not None:
            result['SupplementId'] = self.supplement_id
        if self.user_files_shrink is not None:
            result['UserFiles'] = self.user_files_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('SupplementId') is not None:
            self.supplement_id = m.get('SupplementId')
        if m.get('UserFiles') is not None:
            self.user_files_shrink = m.get('UserFiles')
        return self


class SubmitSupplementResponseBody(TeaModel):
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


class SubmitSupplementResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SubmitSupplementResponseBody = None,
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
            temp_model = SubmitSupplementResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateApplicantRequest(TeaModel):
    def __init__(
        self,
        address: str = None,
        applicant_id: int = None,
        applicant_name: str = None,
        authorization_oss_key: str = None,
        business_licence_oss_key: str = None,
        card_number: str = None,
        contact_address: str = None,
        contact_city: str = None,
        contact_county: str = None,
        contact_district: str = None,
        contact_email: str = None,
        contact_name: str = None,
        contact_number: str = None,
        contact_province: str = None,
        contact_zipcode: str = None,
        eaddress: str = None,
        ename: str = None,
        id_card_name: str = None,
        id_card_number: str = None,
        id_card_oss_key: str = None,
        legal_notice_oss_key: str = None,
        passport_oss_key: str = None,
        personal_type: int = None,
        province: str = None,
    ):
        self.address = address
        self.applicant_id = applicant_id
        self.applicant_name = applicant_name
        self.authorization_oss_key = authorization_oss_key
        self.business_licence_oss_key = business_licence_oss_key
        self.card_number = card_number
        self.contact_address = contact_address
        self.contact_city = contact_city
        self.contact_county = contact_county
        self.contact_district = contact_district
        self.contact_email = contact_email
        self.contact_name = contact_name
        self.contact_number = contact_number
        self.contact_province = contact_province
        self.contact_zipcode = contact_zipcode
        self.eaddress = eaddress
        self.ename = ename
        self.id_card_name = id_card_name
        self.id_card_number = id_card_number
        self.id_card_oss_key = id_card_oss_key
        self.legal_notice_oss_key = legal_notice_oss_key
        self.passport_oss_key = passport_oss_key
        self.personal_type = personal_type
        self.province = province

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.applicant_id is not None:
            result['ApplicantId'] = self.applicant_id
        if self.applicant_name is not None:
            result['ApplicantName'] = self.applicant_name
        if self.authorization_oss_key is not None:
            result['AuthorizationOssKey'] = self.authorization_oss_key
        if self.business_licence_oss_key is not None:
            result['BusinessLicenceOssKey'] = self.business_licence_oss_key
        if self.card_number is not None:
            result['CardNumber'] = self.card_number
        if self.contact_address is not None:
            result['ContactAddress'] = self.contact_address
        if self.contact_city is not None:
            result['ContactCity'] = self.contact_city
        if self.contact_county is not None:
            result['ContactCounty'] = self.contact_county
        if self.contact_district is not None:
            result['ContactDistrict'] = self.contact_district
        if self.contact_email is not None:
            result['ContactEmail'] = self.contact_email
        if self.contact_name is not None:
            result['ContactName'] = self.contact_name
        if self.contact_number is not None:
            result['ContactNumber'] = self.contact_number
        if self.contact_province is not None:
            result['ContactProvince'] = self.contact_province
        if self.contact_zipcode is not None:
            result['ContactZipcode'] = self.contact_zipcode
        if self.eaddress is not None:
            result['EAddress'] = self.eaddress
        if self.ename is not None:
            result['EName'] = self.ename
        if self.id_card_name is not None:
            result['IdCardName'] = self.id_card_name
        if self.id_card_number is not None:
            result['IdCardNumber'] = self.id_card_number
        if self.id_card_oss_key is not None:
            result['IdCardOssKey'] = self.id_card_oss_key
        if self.legal_notice_oss_key is not None:
            result['LegalNoticeOssKey'] = self.legal_notice_oss_key
        if self.passport_oss_key is not None:
            result['PassportOssKey'] = self.passport_oss_key
        if self.personal_type is not None:
            result['PersonalType'] = self.personal_type
        if self.province is not None:
            result['Province'] = self.province
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('ApplicantId') is not None:
            self.applicant_id = m.get('ApplicantId')
        if m.get('ApplicantName') is not None:
            self.applicant_name = m.get('ApplicantName')
        if m.get('AuthorizationOssKey') is not None:
            self.authorization_oss_key = m.get('AuthorizationOssKey')
        if m.get('BusinessLicenceOssKey') is not None:
            self.business_licence_oss_key = m.get('BusinessLicenceOssKey')
        if m.get('CardNumber') is not None:
            self.card_number = m.get('CardNumber')
        if m.get('ContactAddress') is not None:
            self.contact_address = m.get('ContactAddress')
        if m.get('ContactCity') is not None:
            self.contact_city = m.get('ContactCity')
        if m.get('ContactCounty') is not None:
            self.contact_county = m.get('ContactCounty')
        if m.get('ContactDistrict') is not None:
            self.contact_district = m.get('ContactDistrict')
        if m.get('ContactEmail') is not None:
            self.contact_email = m.get('ContactEmail')
        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')
        if m.get('ContactNumber') is not None:
            self.contact_number = m.get('ContactNumber')
        if m.get('ContactProvince') is not None:
            self.contact_province = m.get('ContactProvince')
        if m.get('ContactZipcode') is not None:
            self.contact_zipcode = m.get('ContactZipcode')
        if m.get('EAddress') is not None:
            self.eaddress = m.get('EAddress')
        if m.get('EName') is not None:
            self.ename = m.get('EName')
        if m.get('IdCardName') is not None:
            self.id_card_name = m.get('IdCardName')
        if m.get('IdCardNumber') is not None:
            self.id_card_number = m.get('IdCardNumber')
        if m.get('IdCardOssKey') is not None:
            self.id_card_oss_key = m.get('IdCardOssKey')
        if m.get('LegalNoticeOssKey') is not None:
            self.legal_notice_oss_key = m.get('LegalNoticeOssKey')
        if m.get('PassportOssKey') is not None:
            self.passport_oss_key = m.get('PassportOssKey')
        if m.get('PersonalType') is not None:
            self.personal_type = m.get('PersonalType')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        return self


class UpdateApplicantResponseBody(TeaModel):
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


class UpdateApplicantResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateApplicantResponseBody = None,
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
            temp_model = UpdateApplicantResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


