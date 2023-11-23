# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List, Any


class AcceptPartnerNotificationRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        material: str = None,
        operation: str = None,
        remark: str = None,
    ):
        self.biz_id = biz_id
        self.material = material
        self.operation = operation
        self.remark = remark

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.material is not None:
            result['Material'] = self.material
        if self.operation is not None:
            result['Operation'] = self.operation
        if self.remark is not None:
            result['Remark'] = self.remark
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Material') is not None:
            self.material = m.get('Material')
        if m.get('Operation') is not None:
            self.operation = m.get('Operation')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        return self


class AcceptPartnerNotificationResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_msg = error_msg
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
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AcceptPartnerNotificationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AcceptPartnerNotificationResponseBody = None,
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
            temp_model = AcceptPartnerNotificationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ApplyNotaryPostRequest(TeaModel):
    def __init__(
        self,
        notary_order_id: int = None,
        receiver_address: str = None,
        receiver_name: str = None,
        receiver_phone: str = None,
    ):
        self.notary_order_id = notary_order_id
        self.receiver_address = receiver_address
        self.receiver_name = receiver_name
        self.receiver_phone = receiver_phone

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.notary_order_id is not None:
            result['NotaryOrderId'] = self.notary_order_id
        if self.receiver_address is not None:
            result['ReceiverAddress'] = self.receiver_address
        if self.receiver_name is not None:
            result['ReceiverName'] = self.receiver_name
        if self.receiver_phone is not None:
            result['ReceiverPhone'] = self.receiver_phone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NotaryOrderId') is not None:
            self.notary_order_id = m.get('NotaryOrderId')
        if m.get('ReceiverAddress') is not None:
            self.receiver_address = m.get('ReceiverAddress')
        if m.get('ReceiverName') is not None:
            self.receiver_name = m.get('ReceiverName')
        if m.get('ReceiverPhone') is not None:
            self.receiver_phone = m.get('ReceiverPhone')
        return self


class ApplyNotaryPostResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_msg = error_msg
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
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ApplyNotaryPostResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ApplyNotaryPostResponseBody = None,
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
            temp_model = ApplyNotaryPostResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AskAdjudicationFileRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        contact_address: str = None,
        contact_city: str = None,
        contact_county: str = None,
        contact_district: str = None,
        contact_name: str = None,
        contact_number: str = None,
        contact_province: str = None,
    ):
        self.biz_id = biz_id
        self.contact_address = contact_address
        self.contact_city = contact_city
        self.contact_county = contact_county
        self.contact_district = contact_district
        self.contact_name = contact_name
        self.contact_number = contact_number
        self.contact_province = contact_province

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.contact_address is not None:
            result['ContactAddress'] = self.contact_address
        if self.contact_city is not None:
            result['ContactCity'] = self.contact_city
        if self.contact_county is not None:
            result['ContactCounty'] = self.contact_county
        if self.contact_district is not None:
            result['ContactDistrict'] = self.contact_district
        if self.contact_name is not None:
            result['ContactName'] = self.contact_name
        if self.contact_number is not None:
            result['ContactNumber'] = self.contact_number
        if self.contact_province is not None:
            result['ContactProvince'] = self.contact_province
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('ContactAddress') is not None:
            self.contact_address = m.get('ContactAddress')
        if m.get('ContactCity') is not None:
            self.contact_city = m.get('ContactCity')
        if m.get('ContactCounty') is not None:
            self.contact_county = m.get('ContactCounty')
        if m.get('ContactDistrict') is not None:
            self.contact_district = m.get('ContactDistrict')
        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')
        if m.get('ContactNumber') is not None:
            self.contact_number = m.get('ContactNumber')
        if m.get('ContactProvince') is not None:
            self.contact_province = m.get('ContactProvince')
        return self


class AskAdjudicationFileResponseBody(TeaModel):
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


class AskAdjudicationFileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AskAdjudicationFileResponseBody = None,
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
            temp_model = AskAdjudicationFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BindMaterialRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        legal_notice_key: str = None,
        loa_oss_key: str = None,
        material_id: str = None,
    ):
        self.biz_id = biz_id
        self.legal_notice_key = legal_notice_key
        self.loa_oss_key = loa_oss_key
        self.material_id = material_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.legal_notice_key is not None:
            result['LegalNoticeKey'] = self.legal_notice_key
        if self.loa_oss_key is not None:
            result['LoaOssKey'] = self.loa_oss_key
        if self.material_id is not None:
            result['MaterialId'] = self.material_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('LegalNoticeKey') is not None:
            self.legal_notice_key = m.get('LegalNoticeKey')
        if m.get('LoaOssKey') is not None:
            self.loa_oss_key = m.get('LoaOssKey')
        if m.get('MaterialId') is not None:
            self.material_id = m.get('MaterialId')
        return self


class BindMaterialResponseBody(TeaModel):
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


class BindMaterialResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BindMaterialResponseBody = None,
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
            temp_model = BindMaterialResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelTradeOrderRequest(TeaModel):
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


class CancelTradeOrderResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_msg = error_msg
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
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CancelTradeOrderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CancelTradeOrderResponseBody = None,
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
            temp_model = CancelTradeOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckFlsmFillRequest(TeaModel):
    def __init__(
        self,
        applicant_type: str = None,
        oss_key: str = None,
        personal_type: str = None,
        wtr_name: str = None,
    ):
        self.applicant_type = applicant_type
        self.oss_key = oss_key
        self.personal_type = personal_type
        self.wtr_name = wtr_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.applicant_type is not None:
            result['ApplicantType'] = self.applicant_type
        if self.oss_key is not None:
            result['OssKey'] = self.oss_key
        if self.personal_type is not None:
            result['PersonalType'] = self.personal_type
        if self.wtr_name is not None:
            result['WtrName'] = self.wtr_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicantType') is not None:
            self.applicant_type = m.get('ApplicantType')
        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')
        if m.get('PersonalType') is not None:
            self.personal_type = m.get('PersonalType')
        if m.get('WtrName') is not None:
            self.wtr_name = m.get('WtrName')
        return self


class CheckFlsmFillResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        tips: str = None,
    ):
        self.request_id = request_id
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
        if self.tips is not None:
            result['Tips'] = self.tips
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Tips') is not None:
            self.tips = m.get('Tips')
        return self


class CheckFlsmFillResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CheckFlsmFillResponseBody = None,
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
            temp_model = CheckFlsmFillResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckIfCollectedRequest(TeaModel):
    def __init__(
        self,
        item_id_list: str = None,
        page_num: int = None,
        page_size: int = None,
        type: int = None,
    ):
        self.item_id_list = item_id_list
        self.page_num = page_num
        self.page_size = page_size
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.item_id_list is not None:
            result['ItemIdList'] = self.item_id_list
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ItemIdList') is not None:
            self.item_id_list = m.get('ItemIdList')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CheckIfCollectedResponseBodyDataTrademark(TeaModel):
    def __init__(
        self,
        id: int = None,
        item_id_list: str = None,
        name: str = None,
        type: int = None,
    ):
        self.id = id
        self.item_id_list = item_id_list
        self.name = name
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.item_id_list is not None:
            result['ItemIdList'] = self.item_id_list
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ItemIdList') is not None:
            self.item_id_list = m.get('ItemIdList')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CheckIfCollectedResponseBodyData(TeaModel):
    def __init__(
        self,
        trademark: List[CheckIfCollectedResponseBodyDataTrademark] = None,
    ):
        self.trademark = trademark

    def validate(self):
        if self.trademark:
            for k in self.trademark:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Trademark'] = []
        if self.trademark is not None:
            for k in self.trademark:
                result['Trademark'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.trademark = []
        if m.get('Trademark') is not None:
            for k in m.get('Trademark'):
                temp_model = CheckIfCollectedResponseBodyDataTrademark()
                self.trademark.append(temp_model.from_map(k))
        return self


class CheckIfCollectedResponseBody(TeaModel):
    def __init__(
        self,
        current_page_num: int = None,
        data: CheckIfCollectedResponseBodyData = None,
        page_size: int = None,
        request_id: str = None,
        total_item_num: int = None,
        total_page_num: int = None,
    ):
        self.current_page_num = current_page_num
        self.data = data
        self.page_size = page_size
        self.request_id = request_id
        self.total_item_num = total_item_num
        self.total_page_num = total_page_num

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page_num is not None:
            result['CurrentPageNum'] = self.current_page_num
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_item_num is not None:
            result['TotalItemNum'] = self.total_item_num
        if self.total_page_num is not None:
            result['TotalPageNum'] = self.total_page_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPageNum') is not None:
            self.current_page_num = m.get('CurrentPageNum')
        if m.get('Data') is not None:
            temp_model = CheckIfCollectedResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalItemNum') is not None:
            self.total_item_num = m.get('TotalItemNum')
        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')
        return self


class CheckIfCollectedResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CheckIfCollectedResponseBody = None,
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
            temp_model = CheckIfCollectedResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckLoaFillRequest(TeaModel):
    def __init__(
        self,
        applicant_type: str = None,
        biz_type: str = None,
        contact_name: str = None,
        contact_number: str = None,
        contact_zipcode: str = None,
        oss_key: str = None,
        personal_type: str = None,
        principal_name: str = None,
        type: str = None,
        wtr_name: str = None,
    ):
        self.applicant_type = applicant_type
        self.biz_type = biz_type
        self.contact_name = contact_name
        self.contact_number = contact_number
        self.contact_zipcode = contact_zipcode
        self.oss_key = oss_key
        self.personal_type = personal_type
        self.principal_name = principal_name
        self.type = type
        self.wtr_name = wtr_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.applicant_type is not None:
            result['ApplicantType'] = self.applicant_type
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
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
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name
        if self.type is not None:
            result['Type'] = self.type
        if self.wtr_name is not None:
            result['WtrName'] = self.wtr_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicantType') is not None:
            self.applicant_type = m.get('ApplicantType')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
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
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('WtrName') is not None:
            self.wtr_name = m.get('WtrName')
        return self


class CheckLoaFillResponseBodyDataErrorMsgs(TeaModel):
    def __init__(
        self,
        error_msg: List[str] = None,
    ):
        self.error_msg = error_msg

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        return self


class CheckLoaFillResponseBodyData(TeaModel):
    def __init__(
        self,
        address_fill: bool = None,
        country_fill: bool = None,
        error_msgs: CheckLoaFillResponseBodyDataErrorMsgs = None,
        material_name_fill: bool = None,
        nationality_fill: bool = None,
        stamp_fill: bool = None,
        template_url: str = None,
        tips: str = None,
        trade_mark_name_fill: bool = None,
    ):
        self.address_fill = address_fill
        self.country_fill = country_fill
        self.error_msgs = error_msgs
        self.material_name_fill = material_name_fill
        self.nationality_fill = nationality_fill
        self.stamp_fill = stamp_fill
        self.template_url = template_url
        self.tips = tips
        self.trade_mark_name_fill = trade_mark_name_fill

    def validate(self):
        if self.error_msgs:
            self.error_msgs.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address_fill is not None:
            result['AddressFill'] = self.address_fill
        if self.country_fill is not None:
            result['CountryFill'] = self.country_fill
        if self.error_msgs is not None:
            result['ErrorMsgs'] = self.error_msgs.to_map()
        if self.material_name_fill is not None:
            result['MaterialNameFill'] = self.material_name_fill
        if self.nationality_fill is not None:
            result['NationalityFill'] = self.nationality_fill
        if self.stamp_fill is not None:
            result['StampFill'] = self.stamp_fill
        if self.template_url is not None:
            result['TemplateUrl'] = self.template_url
        if self.tips is not None:
            result['Tips'] = self.tips
        if self.trade_mark_name_fill is not None:
            result['TradeMarkNameFill'] = self.trade_mark_name_fill
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddressFill') is not None:
            self.address_fill = m.get('AddressFill')
        if m.get('CountryFill') is not None:
            self.country_fill = m.get('CountryFill')
        if m.get('ErrorMsgs') is not None:
            temp_model = CheckLoaFillResponseBodyDataErrorMsgs()
            self.error_msgs = temp_model.from_map(m['ErrorMsgs'])
        if m.get('MaterialNameFill') is not None:
            self.material_name_fill = m.get('MaterialNameFill')
        if m.get('NationalityFill') is not None:
            self.nationality_fill = m.get('NationalityFill')
        if m.get('StampFill') is not None:
            self.stamp_fill = m.get('StampFill')
        if m.get('TemplateUrl') is not None:
            self.template_url = m.get('TemplateUrl')
        if m.get('Tips') is not None:
            self.tips = m.get('Tips')
        if m.get('TradeMarkNameFill') is not None:
            self.trade_mark_name_fill = m.get('TradeMarkNameFill')
        return self


class CheckLoaFillResponseBody(TeaModel):
    def __init__(
        self,
        data: CheckLoaFillResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = CheckLoaFillResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CheckLoaFillResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CheckLoaFillResponseBody = None,
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
            temp_model = CheckLoaFillResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckTrademarkIconRequest(TeaModel):
    def __init__(
        self,
        event_scene_type: int = None,
        trademark_icon_oss_key: str = None,
    ):
        self.event_scene_type = event_scene_type
        self.trademark_icon_oss_key = trademark_icon_oss_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_scene_type is not None:
            result['EventSceneType'] = self.event_scene_type
        if self.trademark_icon_oss_key is not None:
            result['TrademarkIconOssKey'] = self.trademark_icon_oss_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventSceneType') is not None:
            self.event_scene_type = m.get('EventSceneType')
        if m.get('TrademarkIconOssKey') is not None:
            self.trademark_icon_oss_key = m.get('TrademarkIconOssKey')
        return self


class CheckTrademarkIconResponseBody(TeaModel):
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


class CheckTrademarkIconResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CheckTrademarkIconResponseBody = None,
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
            temp_model = CheckTrademarkIconResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckTrademarkOrderRequest(TeaModel):
    def __init__(
        self,
        agreement_id: str = None,
        biz_id: str = None,
        channel: str = None,
        is_black_icon: bool = None,
        loa_oss_key: str = None,
        logo_goods_id: str = None,
        material_id: str = None,
        order_data: str = None,
        partner_code: str = None,
        phone_num: str = None,
        real_user_name: str = None,
        register_name: str = None,
        register_number: str = None,
        renew_info_id: str = None,
        root_code: str = None,
        tm_comment: str = None,
        tm_icon: str = None,
        tm_name: str = None,
        tm_name_type: str = None,
        type: int = None,
        uid: str = None,
        user_id: int = None,
    ):
        self.agreement_id = agreement_id
        self.biz_id = biz_id
        self.channel = channel
        self.is_black_icon = is_black_icon
        self.loa_oss_key = loa_oss_key
        self.logo_goods_id = logo_goods_id
        self.material_id = material_id
        self.order_data = order_data
        self.partner_code = partner_code
        self.phone_num = phone_num
        self.real_user_name = real_user_name
        self.register_name = register_name
        self.register_number = register_number
        self.renew_info_id = renew_info_id
        self.root_code = root_code
        self.tm_comment = tm_comment
        self.tm_icon = tm_icon
        self.tm_name = tm_name
        self.tm_name_type = tm_name_type
        self.type = type
        self.uid = uid
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agreement_id is not None:
            result['AgreementId'] = self.agreement_id
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.channel is not None:
            result['Channel'] = self.channel
        if self.is_black_icon is not None:
            result['IsBlackIcon'] = self.is_black_icon
        if self.loa_oss_key is not None:
            result['LoaOssKey'] = self.loa_oss_key
        if self.logo_goods_id is not None:
            result['LogoGoodsId'] = self.logo_goods_id
        if self.material_id is not None:
            result['MaterialId'] = self.material_id
        if self.order_data is not None:
            result['OrderData'] = self.order_data
        if self.partner_code is not None:
            result['PartnerCode'] = self.partner_code
        if self.phone_num is not None:
            result['PhoneNum'] = self.phone_num
        if self.real_user_name is not None:
            result['RealUserName'] = self.real_user_name
        if self.register_name is not None:
            result['RegisterName'] = self.register_name
        if self.register_number is not None:
            result['RegisterNumber'] = self.register_number
        if self.renew_info_id is not None:
            result['RenewInfoId'] = self.renew_info_id
        if self.root_code is not None:
            result['RootCode'] = self.root_code
        if self.tm_comment is not None:
            result['TmComment'] = self.tm_comment
        if self.tm_icon is not None:
            result['TmIcon'] = self.tm_icon
        if self.tm_name is not None:
            result['TmName'] = self.tm_name
        if self.tm_name_type is not None:
            result['TmNameType'] = self.tm_name_type
        if self.type is not None:
            result['Type'] = self.type
        if self.uid is not None:
            result['Uid'] = self.uid
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgreementId') is not None:
            self.agreement_id = m.get('AgreementId')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Channel') is not None:
            self.channel = m.get('Channel')
        if m.get('IsBlackIcon') is not None:
            self.is_black_icon = m.get('IsBlackIcon')
        if m.get('LoaOssKey') is not None:
            self.loa_oss_key = m.get('LoaOssKey')
        if m.get('LogoGoodsId') is not None:
            self.logo_goods_id = m.get('LogoGoodsId')
        if m.get('MaterialId') is not None:
            self.material_id = m.get('MaterialId')
        if m.get('OrderData') is not None:
            self.order_data = m.get('OrderData')
        if m.get('PartnerCode') is not None:
            self.partner_code = m.get('PartnerCode')
        if m.get('PhoneNum') is not None:
            self.phone_num = m.get('PhoneNum')
        if m.get('RealUserName') is not None:
            self.real_user_name = m.get('RealUserName')
        if m.get('RegisterName') is not None:
            self.register_name = m.get('RegisterName')
        if m.get('RegisterNumber') is not None:
            self.register_number = m.get('RegisterNumber')
        if m.get('RenewInfoId') is not None:
            self.renew_info_id = m.get('RenewInfoId')
        if m.get('RootCode') is not None:
            self.root_code = m.get('RootCode')
        if m.get('TmComment') is not None:
            self.tm_comment = m.get('TmComment')
        if m.get('TmIcon') is not None:
            self.tm_icon = m.get('TmIcon')
        if m.get('TmName') is not None:
            self.tm_name = m.get('TmName')
        if m.get('TmNameType') is not None:
            self.tm_name_type = m.get('TmNameType')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class CheckTrademarkOrderResponseBody(TeaModel):
    def __init__(
        self,
        data: Dict[str, Any] = None,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.error_msg = error_msg
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
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CheckTrademarkOrderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CheckTrademarkOrderResponseBody = None,
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
            temp_model = CheckTrademarkOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CombineLoaRequest(TeaModel):
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
        tm_number: str = None,
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
        self.tm_number = tm_number
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
        if self.tm_number is not None:
            result['TmNumber'] = self.tm_number
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
        if m.get('TmNumber') is not None:
            self.tm_number = m.get('TmNumber')
        if m.get('TmProduceType') is not None:
            self.tm_produce_type = m.get('TmProduceType')
        if m.get('TrademarkName') is not None:
            self.trademark_name = m.get('TrademarkName')
        return self


class CombineLoaResponseBody(TeaModel):
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


class CombineLoaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CombineLoaResponseBody = None,
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
            temp_model = CombineLoaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CombineWTSRequest(TeaModel):
    def __init__(
        self,
        address: str = None,
        contact: str = None,
        contact_address_post: str = None,
        contact_mobile: str = None,
        material_id: str = None,
        material_name: str = None,
        nationality: str = None,
        principal_name: str = None,
        tm_num: str = None,
        tm_produce_type: str = None,
        trademark_name: str = None,
        wts_type: str = None,
    ):
        self.address = address
        self.contact = contact
        self.contact_address_post = contact_address_post
        self.contact_mobile = contact_mobile
        self.material_id = material_id
        self.material_name = material_name
        self.nationality = nationality
        self.principal_name = principal_name
        self.tm_num = tm_num
        self.tm_produce_type = tm_produce_type
        self.trademark_name = trademark_name
        self.wts_type = wts_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.contact is not None:
            result['Contact'] = self.contact
        if self.contact_address_post is not None:
            result['ContactAddressPost'] = self.contact_address_post
        if self.contact_mobile is not None:
            result['ContactMobile'] = self.contact_mobile
        if self.material_id is not None:
            result['MaterialId'] = self.material_id
        if self.material_name is not None:
            result['MaterialName'] = self.material_name
        if self.nationality is not None:
            result['Nationality'] = self.nationality
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name
        if self.tm_num is not None:
            result['TmNum'] = self.tm_num
        if self.tm_produce_type is not None:
            result['TmProduceType'] = self.tm_produce_type
        if self.trademark_name is not None:
            result['TrademarkName'] = self.trademark_name
        if self.wts_type is not None:
            result['WtsType'] = self.wts_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('Contact') is not None:
            self.contact = m.get('Contact')
        if m.get('ContactAddressPost') is not None:
            self.contact_address_post = m.get('ContactAddressPost')
        if m.get('ContactMobile') is not None:
            self.contact_mobile = m.get('ContactMobile')
        if m.get('MaterialId') is not None:
            self.material_id = m.get('MaterialId')
        if m.get('MaterialName') is not None:
            self.material_name = m.get('MaterialName')
        if m.get('Nationality') is not None:
            self.nationality = m.get('Nationality')
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')
        if m.get('TmNum') is not None:
            self.tm_num = m.get('TmNum')
        if m.get('TmProduceType') is not None:
            self.tm_produce_type = m.get('TmProduceType')
        if m.get('TrademarkName') is not None:
            self.trademark_name = m.get('TrademarkName')
        if m.get('WtsType') is not None:
            self.wts_type = m.get('WtsType')
        return self


class CombineWTSResponseBody(TeaModel):
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


class CombineWTSResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CombineWTSResponseBody = None,
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
            temp_model = CombineWTSResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ComplementIntentionUserIdRequest(TeaModel):
    def __init__(
        self,
        aliyun_kp: str = None,
        bid: str = None,
        biz_id: str = None,
        caller_parent_id: int = None,
        caller_type: str = None,
        complement_user_id: str = None,
        type: int = None,
    ):
        self.aliyun_kp = aliyun_kp
        self.bid = bid
        self.biz_id = biz_id
        self.caller_parent_id = caller_parent_id
        self.caller_type = caller_type
        self.complement_user_id = complement_user_id
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aliyun_kp is not None:
            result['AliyunKp'] = self.aliyun_kp
        if self.bid is not None:
            result['Bid'] = self.bid
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.caller_parent_id is not None:
            result['CallerParentId'] = self.caller_parent_id
        if self.caller_type is not None:
            result['CallerType'] = self.caller_type
        if self.complement_user_id is not None:
            result['ComplementUserId'] = self.complement_user_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunKp') is not None:
            self.aliyun_kp = m.get('AliyunKp')
        if m.get('Bid') is not None:
            self.bid = m.get('Bid')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('CallerParentId') is not None:
            self.caller_parent_id = m.get('CallerParentId')
        if m.get('CallerType') is not None:
            self.caller_type = m.get('CallerType')
        if m.get('ComplementUserId') is not None:
            self.complement_user_id = m.get('ComplementUserId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ComplementIntentionUserIdResponseBody(TeaModel):
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


class ComplementIntentionUserIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ComplementIntentionUserIdResponseBody = None,
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
            temp_model = ComplementIntentionUserIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConfirmAdditionalMaterialRequest(TeaModel):
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


class ConfirmAdditionalMaterialResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_msg = error_msg
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
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ConfirmAdditionalMaterialResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ConfirmAdditionalMaterialResponseBody = None,
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
            temp_model = ConfirmAdditionalMaterialResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConfirmApplicantRequest(TeaModel):
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


class ConfirmApplicantResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_msg = error_msg
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
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ConfirmApplicantResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ConfirmApplicantResponseBody = None,
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
            temp_model = ConfirmApplicantResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConfirmDissentOriginalRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        contact_address: str = None,
        contact_city: str = None,
        contact_county: str = None,
        contact_district: str = None,
        contact_name: str = None,
        contact_number: str = None,
        contact_province: str = None,
        operate_type: str = None,
    ):
        self.biz_id = biz_id
        self.contact_address = contact_address
        self.contact_city = contact_city
        self.contact_county = contact_county
        self.contact_district = contact_district
        self.contact_name = contact_name
        self.contact_number = contact_number
        self.contact_province = contact_province
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
        if self.contact_address is not None:
            result['ContactAddress'] = self.contact_address
        if self.contact_city is not None:
            result['ContactCity'] = self.contact_city
        if self.contact_county is not None:
            result['ContactCounty'] = self.contact_county
        if self.contact_district is not None:
            result['ContactDistrict'] = self.contact_district
        if self.contact_name is not None:
            result['ContactName'] = self.contact_name
        if self.contact_number is not None:
            result['ContactNumber'] = self.contact_number
        if self.contact_province is not None:
            result['ContactProvince'] = self.contact_province
        if self.operate_type is not None:
            result['OperateType'] = self.operate_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('ContactAddress') is not None:
            self.contact_address = m.get('ContactAddress')
        if m.get('ContactCity') is not None:
            self.contact_city = m.get('ContactCity')
        if m.get('ContactCounty') is not None:
            self.contact_county = m.get('ContactCounty')
        if m.get('ContactDistrict') is not None:
            self.contact_district = m.get('ContactDistrict')
        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')
        if m.get('ContactNumber') is not None:
            self.contact_number = m.get('ContactNumber')
        if m.get('ContactProvince') is not None:
            self.contact_province = m.get('ContactProvince')
        if m.get('OperateType') is not None:
            self.operate_type = m.get('OperateType')
        return self


class ConfirmDissentOriginalResponseBody(TeaModel):
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


class ConfirmDissentOriginalResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ConfirmDissentOriginalResponseBody = None,
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
            temp_model = ConfirmDissentOriginalResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConvertImageToGrayRequest(TeaModel):
    def __init__(
        self,
        oss_key: str = None,
    ):
        self.oss_key = oss_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.oss_key is not None:
            result['OssKey'] = self.oss_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')
        return self


class ConvertImageToGrayResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        signature_url: str = None,
    ):
        self.request_id = request_id
        self.signature_url = signature_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.signature_url is not None:
            result['SignatureUrl'] = self.signature_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SignatureUrl') is not None:
            self.signature_url = m.get('SignatureUrl')
        return self


class ConvertImageToGrayResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ConvertImageToGrayResponseBody = None,
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
            temp_model = ConvertImageToGrayResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CopyApplicantRequest(TeaModel):
    def __init__(
        self,
        id: int = None,
    ):
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


class CopyApplicantResponseBody(TeaModel):
    def __init__(
        self,
        id: int = None,
        request_id: str = None,
    ):
        self.id = id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CopyApplicantResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CopyApplicantResponseBody = None,
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
            temp_model = CopyApplicantResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateIntentionOrderRequest(TeaModel):
    def __init__(
        self,
        channel: str = None,
        intention_biz_id: str = None,
    ):
        self.channel = channel
        self.intention_biz_id = intention_biz_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel is not None:
            result['Channel'] = self.channel
        if self.intention_biz_id is not None:
            result['IntentionBizId'] = self.intention_biz_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Channel') is not None:
            self.channel = m.get('Channel')
        if m.get('IntentionBizId') is not None:
            self.intention_biz_id = m.get('IntentionBizId')
        return self


class CreateIntentionOrderResponseBodyData(TeaModel):
    def __init__(
        self,
        order_ids: List[str] = None,
    ):
        self.order_ids = order_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_ids is not None:
            result['OrderIds'] = self.order_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderIds') is not None:
            self.order_ids = m.get('OrderIds')
        return self


class CreateIntentionOrderResponseBody(TeaModel):
    def __init__(
        self,
        data: CreateIntentionOrderResponseBodyData = None,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.error_msg = error_msg
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
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = CreateIntentionOrderResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateIntentionOrderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateIntentionOrderResponseBody = None,
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
            temp_model = CreateIntentionOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateIntentionOrderGeneratingPayRequest(TeaModel):
    def __init__(
        self,
        channel: str = None,
        intention_biz_id: str = None,
        payment_callback: str = None,
    ):
        self.channel = channel
        self.intention_biz_id = intention_biz_id
        self.payment_callback = payment_callback

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel is not None:
            result['Channel'] = self.channel
        if self.intention_biz_id is not None:
            result['IntentionBizId'] = self.intention_biz_id
        if self.payment_callback is not None:
            result['PaymentCallback'] = self.payment_callback
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Channel') is not None:
            self.channel = m.get('Channel')
        if m.get('IntentionBizId') is not None:
            self.intention_biz_id = m.get('IntentionBizId')
        if m.get('PaymentCallback') is not None:
            self.payment_callback = m.get('PaymentCallback')
        return self


class CreateIntentionOrderGeneratingPayResponseBody(TeaModel):
    def __init__(
        self,
        error_msg: str = None,
        order_ids: List[int] = None,
        pay_url: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_msg = error_msg
        self.order_ids = order_ids
        self.pay_url = pay_url
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.order_ids is not None:
            result['OrderIds'] = self.order_ids
        if self.pay_url is not None:
            result['PayUrl'] = self.pay_url
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('OrderIds') is not None:
            self.order_ids = m.get('OrderIds')
        if m.get('PayUrl') is not None:
            self.pay_url = m.get('PayUrl')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateIntentionOrderGeneratingPayResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateIntentionOrderGeneratingPayResponseBody = None,
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
            temp_model = CreateIntentionOrderGeneratingPayResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTrademarkOrderRequest(TeaModel):
    def __init__(
        self,
        agreement_id: str = None,
        big_dipper_source: str = None,
        biz_id: str = None,
        channel: str = None,
        is_black_icon: bool = None,
        legal_notice_key: str = None,
        loa_oss_key: str = None,
        material_id: str = None,
        order_data: str = None,
        partner_code: str = None,
        phone_num: str = None,
        principal_name: int = None,
        real_user_name: str = None,
        register_name: str = None,
        register_number: str = None,
        renew_info_id: str = None,
        root_code: str = None,
        session_id: str = None,
        tm_comment: str = None,
        tm_icon: str = None,
        tm_name: str = None,
        tm_name_type: str = None,
        type: int = None,
        ua: str = None,
        uid: str = None,
        user_id: int = None,
    ):
        self.agreement_id = agreement_id
        self.big_dipper_source = big_dipper_source
        self.biz_id = biz_id
        self.channel = channel
        self.is_black_icon = is_black_icon
        self.legal_notice_key = legal_notice_key
        self.loa_oss_key = loa_oss_key
        self.material_id = material_id
        self.order_data = order_data
        self.partner_code = partner_code
        self.phone_num = phone_num
        self.principal_name = principal_name
        self.real_user_name = real_user_name
        self.register_name = register_name
        self.register_number = register_number
        self.renew_info_id = renew_info_id
        self.root_code = root_code
        self.session_id = session_id
        self.tm_comment = tm_comment
        self.tm_icon = tm_icon
        self.tm_name = tm_name
        self.tm_name_type = tm_name_type
        self.type = type
        self.ua = ua
        self.uid = uid
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agreement_id is not None:
            result['AgreementId'] = self.agreement_id
        if self.big_dipper_source is not None:
            result['BigDipperSource'] = self.big_dipper_source
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.channel is not None:
            result['Channel'] = self.channel
        if self.is_black_icon is not None:
            result['IsBlackIcon'] = self.is_black_icon
        if self.legal_notice_key is not None:
            result['LegalNoticeKey'] = self.legal_notice_key
        if self.loa_oss_key is not None:
            result['LoaOssKey'] = self.loa_oss_key
        if self.material_id is not None:
            result['MaterialId'] = self.material_id
        if self.order_data is not None:
            result['OrderData'] = self.order_data
        if self.partner_code is not None:
            result['PartnerCode'] = self.partner_code
        if self.phone_num is not None:
            result['PhoneNum'] = self.phone_num
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name
        if self.real_user_name is not None:
            result['RealUserName'] = self.real_user_name
        if self.register_name is not None:
            result['RegisterName'] = self.register_name
        if self.register_number is not None:
            result['RegisterNumber'] = self.register_number
        if self.renew_info_id is not None:
            result['RenewInfoId'] = self.renew_info_id
        if self.root_code is not None:
            result['RootCode'] = self.root_code
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.tm_comment is not None:
            result['TmComment'] = self.tm_comment
        if self.tm_icon is not None:
            result['TmIcon'] = self.tm_icon
        if self.tm_name is not None:
            result['TmName'] = self.tm_name
        if self.tm_name_type is not None:
            result['TmNameType'] = self.tm_name_type
        if self.type is not None:
            result['Type'] = self.type
        if self.ua is not None:
            result['Ua'] = self.ua
        if self.uid is not None:
            result['Uid'] = self.uid
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgreementId') is not None:
            self.agreement_id = m.get('AgreementId')
        if m.get('BigDipperSource') is not None:
            self.big_dipper_source = m.get('BigDipperSource')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Channel') is not None:
            self.channel = m.get('Channel')
        if m.get('IsBlackIcon') is not None:
            self.is_black_icon = m.get('IsBlackIcon')
        if m.get('LegalNoticeKey') is not None:
            self.legal_notice_key = m.get('LegalNoticeKey')
        if m.get('LoaOssKey') is not None:
            self.loa_oss_key = m.get('LoaOssKey')
        if m.get('MaterialId') is not None:
            self.material_id = m.get('MaterialId')
        if m.get('OrderData') is not None:
            self.order_data = m.get('OrderData')
        if m.get('PartnerCode') is not None:
            self.partner_code = m.get('PartnerCode')
        if m.get('PhoneNum') is not None:
            self.phone_num = m.get('PhoneNum')
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')
        if m.get('RealUserName') is not None:
            self.real_user_name = m.get('RealUserName')
        if m.get('RegisterName') is not None:
            self.register_name = m.get('RegisterName')
        if m.get('RegisterNumber') is not None:
            self.register_number = m.get('RegisterNumber')
        if m.get('RenewInfoId') is not None:
            self.renew_info_id = m.get('RenewInfoId')
        if m.get('RootCode') is not None:
            self.root_code = m.get('RootCode')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('TmComment') is not None:
            self.tm_comment = m.get('TmComment')
        if m.get('TmIcon') is not None:
            self.tm_icon = m.get('TmIcon')
        if m.get('TmName') is not None:
            self.tm_name = m.get('TmName')
        if m.get('TmNameType') is not None:
            self.tm_name_type = m.get('TmNameType')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Ua') is not None:
            self.ua = m.get('Ua')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class CreateTrademarkOrderResponseBody(TeaModel):
    def __init__(
        self,
        error_msg: str = None,
        order_id: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_msg = error_msg
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
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateTrademarkOrderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateTrademarkOrderResponseBody = None,
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
            temp_model = CreateTrademarkOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteMaterialRequest(TeaModel):
    def __init__(
        self,
        id: int = None,
    ):
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


class DeleteMaterialResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_msg = error_msg
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
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteMaterialResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteMaterialResponseBody = None,
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
            temp_model = DeleteMaterialResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTmMonitorRuleRequest(TeaModel):
    def __init__(
        self,
        id: int = None,
    ):
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


class DeleteTmMonitorRuleResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_msg = error_msg
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
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteTmMonitorRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteTmMonitorRuleResponseBody = None,
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
            temp_model = DeleteTmMonitorRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTrademarkApplicationRequest(TeaModel):
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


class DeleteTrademarkApplicationResponseBody(TeaModel):
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


class DeleteTrademarkApplicationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteTrademarkApplicationResponseBody = None,
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
            temp_model = DeleteTrademarkApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DenySupplementRequest(TeaModel):
    def __init__(
        self,
        id: int = None,
    ):
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


class DenySupplementResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_msg = error_msg
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
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DenySupplementResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DenySupplementResponseBody = None,
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
            temp_model = DenySupplementResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescirbeCombineTrademarkRequest(TeaModel):
    def __init__(
        self,
        accurate_match: bool = None,
        classification: str = None,
        name: str = None,
        owner_name: str = None,
        page_number: int = None,
        page_size: int = None,
        products: str = None,
        registration_number: str = None,
        similar_groups: str = None,
    ):
        self.accurate_match = accurate_match
        self.classification = classification
        self.name = name
        self.owner_name = owner_name
        self.page_number = page_number
        self.page_size = page_size
        self.products = products
        self.registration_number = registration_number
        self.similar_groups = similar_groups

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accurate_match is not None:
            result['AccurateMatch'] = self.accurate_match
        if self.classification is not None:
            result['Classification'] = self.classification
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_name is not None:
            result['OwnerName'] = self.owner_name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.products is not None:
            result['Products'] = self.products
        if self.registration_number is not None:
            result['RegistrationNumber'] = self.registration_number
        if self.similar_groups is not None:
            result['SimilarGroups'] = self.similar_groups
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccurateMatch') is not None:
            self.accurate_match = m.get('AccurateMatch')
        if m.get('Classification') is not None:
            self.classification = m.get('Classification')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerName') is not None:
            self.owner_name = m.get('OwnerName')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Products') is not None:
            self.products = m.get('Products')
        if m.get('RegistrationNumber') is not None:
            self.registration_number = m.get('RegistrationNumber')
        if m.get('SimilarGroups') is not None:
            self.similar_groups = m.get('SimilarGroups')
        return self


class DescirbeCombineTrademarkResponseBodyDataAnnouncementList(TeaModel):
    def __init__(
        self,
        ann_date: str = None,
        ann_number: str = None,
        ann_type_code: str = None,
        ann_type_name: str = None,
        image_url: str = None,
        original_image_url: str = None,
    ):
        self.ann_date = ann_date
        self.ann_number = ann_number
        self.ann_type_code = ann_type_code
        self.ann_type_name = ann_type_name
        self.image_url = image_url
        self.original_image_url = original_image_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ann_date is not None:
            result['AnnDate'] = self.ann_date
        if self.ann_number is not None:
            result['AnnNumber'] = self.ann_number
        if self.ann_type_code is not None:
            result['AnnTypeCode'] = self.ann_type_code
        if self.ann_type_name is not None:
            result['AnnTypeName'] = self.ann_type_name
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.original_image_url is not None:
            result['OriginalImageUrl'] = self.original_image_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AnnDate') is not None:
            self.ann_date = m.get('AnnDate')
        if m.get('AnnNumber') is not None:
            self.ann_number = m.get('AnnNumber')
        if m.get('AnnTypeCode') is not None:
            self.ann_type_code = m.get('AnnTypeCode')
        if m.get('AnnTypeName') is not None:
            self.ann_type_name = m.get('AnnTypeName')
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('OriginalImageUrl') is not None:
            self.original_image_url = m.get('OriginalImageUrl')
        return self


class DescirbeCombineTrademarkResponseBodyDataProcedures(TeaModel):
    def __init__(
        self,
        procedure_code: str = None,
        procedure_date: str = None,
        procedure_name: str = None,
        procedure_result: str = None,
        procedure_step: str = None,
    ):
        self.procedure_code = procedure_code
        self.procedure_date = procedure_date
        self.procedure_name = procedure_name
        self.procedure_result = procedure_result
        self.procedure_step = procedure_step

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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
        return self


class DescirbeCombineTrademarkResponseBodyData(TeaModel):
    def __init__(
        self,
        agency: str = None,
        announcement_list: List[DescirbeCombineTrademarkResponseBodyDataAnnouncementList] = None,
        apply_date: str = None,
        classification: str = None,
        exclusive_date_limit: str = None,
        first_anno_number: str = None,
        first_anno_type: str = None,
        image: str = None,
        index_id: str = None,
        intl_reg_date: str = None,
        last_procedure_status: str = None,
        law_final_status: str = None,
        name: str = None,
        on_sale: int = None,
        owner_address: str = None,
        owner_en_address: str = None,
        owner_en_name: str = None,
        owner_name: str = None,
        pre_ann_date: str = None,
        pre_ann_number: str = None,
        priority_date: str = None,
        procedures: List[DescirbeCombineTrademarkResponseBodyDataProcedures] = None,
        product_description: str = None,
        reg_ann_date: str = None,
        reg_ann_number: str = None,
        registration_number: str = None,
        registration_type: str = None,
        second_anno_number: str = None,
        second_anno_type: str = None,
        share: str = None,
        similar_group: str = None,
        status: str = None,
        subsequent_designation_date: str = None,
    ):
        self.agency = agency
        self.announcement_list = announcement_list
        self.apply_date = apply_date
        self.classification = classification
        self.exclusive_date_limit = exclusive_date_limit
        self.first_anno_number = first_anno_number
        self.first_anno_type = first_anno_type
        self.image = image
        self.index_id = index_id
        self.intl_reg_date = intl_reg_date
        self.last_procedure_status = last_procedure_status
        self.law_final_status = law_final_status
        self.name = name
        self.on_sale = on_sale
        self.owner_address = owner_address
        self.owner_en_address = owner_en_address
        self.owner_en_name = owner_en_name
        self.owner_name = owner_name
        self.pre_ann_date = pre_ann_date
        self.pre_ann_number = pre_ann_number
        self.priority_date = priority_date
        self.procedures = procedures
        self.product_description = product_description
        self.reg_ann_date = reg_ann_date
        self.reg_ann_number = reg_ann_number
        self.registration_number = registration_number
        self.registration_type = registration_type
        self.second_anno_number = second_anno_number
        self.second_anno_type = second_anno_type
        self.share = share
        self.similar_group = similar_group
        self.status = status
        self.subsequent_designation_date = subsequent_designation_date

    def validate(self):
        if self.announcement_list:
            for k in self.announcement_list:
                if k:
                    k.validate()
        if self.procedures:
            for k in self.procedures:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agency is not None:
            result['Agency'] = self.agency
        result['AnnouncementList'] = []
        if self.announcement_list is not None:
            for k in self.announcement_list:
                result['AnnouncementList'].append(k.to_map() if k else None)
        if self.apply_date is not None:
            result['ApplyDate'] = self.apply_date
        if self.classification is not None:
            result['Classification'] = self.classification
        if self.exclusive_date_limit is not None:
            result['ExclusiveDateLimit'] = self.exclusive_date_limit
        if self.first_anno_number is not None:
            result['FirstAnnoNumber'] = self.first_anno_number
        if self.first_anno_type is not None:
            result['FirstAnnoType'] = self.first_anno_type
        if self.image is not None:
            result['Image'] = self.image
        if self.index_id is not None:
            result['IndexId'] = self.index_id
        if self.intl_reg_date is not None:
            result['IntlRegDate'] = self.intl_reg_date
        if self.last_procedure_status is not None:
            result['LastProcedureStatus'] = self.last_procedure_status
        if self.law_final_status is not None:
            result['LawFinalStatus'] = self.law_final_status
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
        if self.pre_ann_number is not None:
            result['PreAnnNumber'] = self.pre_ann_number
        if self.priority_date is not None:
            result['PriorityDate'] = self.priority_date
        result['Procedures'] = []
        if self.procedures is not None:
            for k in self.procedures:
                result['Procedures'].append(k.to_map() if k else None)
        if self.product_description is not None:
            result['ProductDescription'] = self.product_description
        if self.reg_ann_date is not None:
            result['RegAnnDate'] = self.reg_ann_date
        if self.reg_ann_number is not None:
            result['RegAnnNumber'] = self.reg_ann_number
        if self.registration_number is not None:
            result['RegistrationNumber'] = self.registration_number
        if self.registration_type is not None:
            result['RegistrationType'] = self.registration_type
        if self.second_anno_number is not None:
            result['SecondAnnoNumber'] = self.second_anno_number
        if self.second_anno_type is not None:
            result['SecondAnnoType'] = self.second_anno_type
        if self.share is not None:
            result['Share'] = self.share
        if self.similar_group is not None:
            result['SimilarGroup'] = self.similar_group
        if self.status is not None:
            result['Status'] = self.status
        if self.subsequent_designation_date is not None:
            result['SubsequentDesignationDate'] = self.subsequent_designation_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Agency') is not None:
            self.agency = m.get('Agency')
        self.announcement_list = []
        if m.get('AnnouncementList') is not None:
            for k in m.get('AnnouncementList'):
                temp_model = DescirbeCombineTrademarkResponseBodyDataAnnouncementList()
                self.announcement_list.append(temp_model.from_map(k))
        if m.get('ApplyDate') is not None:
            self.apply_date = m.get('ApplyDate')
        if m.get('Classification') is not None:
            self.classification = m.get('Classification')
        if m.get('ExclusiveDateLimit') is not None:
            self.exclusive_date_limit = m.get('ExclusiveDateLimit')
        if m.get('FirstAnnoNumber') is not None:
            self.first_anno_number = m.get('FirstAnnoNumber')
        if m.get('FirstAnnoType') is not None:
            self.first_anno_type = m.get('FirstAnnoType')
        if m.get('Image') is not None:
            self.image = m.get('Image')
        if m.get('IndexId') is not None:
            self.index_id = m.get('IndexId')
        if m.get('IntlRegDate') is not None:
            self.intl_reg_date = m.get('IntlRegDate')
        if m.get('LastProcedureStatus') is not None:
            self.last_procedure_status = m.get('LastProcedureStatus')
        if m.get('LawFinalStatus') is not None:
            self.law_final_status = m.get('LawFinalStatus')
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
        if m.get('PreAnnNumber') is not None:
            self.pre_ann_number = m.get('PreAnnNumber')
        if m.get('PriorityDate') is not None:
            self.priority_date = m.get('PriorityDate')
        self.procedures = []
        if m.get('Procedures') is not None:
            for k in m.get('Procedures'):
                temp_model = DescirbeCombineTrademarkResponseBodyDataProcedures()
                self.procedures.append(temp_model.from_map(k))
        if m.get('ProductDescription') is not None:
            self.product_description = m.get('ProductDescription')
        if m.get('RegAnnDate') is not None:
            self.reg_ann_date = m.get('RegAnnDate')
        if m.get('RegAnnNumber') is not None:
            self.reg_ann_number = m.get('RegAnnNumber')
        if m.get('RegistrationNumber') is not None:
            self.registration_number = m.get('RegistrationNumber')
        if m.get('RegistrationType') is not None:
            self.registration_type = m.get('RegistrationType')
        if m.get('SecondAnnoNumber') is not None:
            self.second_anno_number = m.get('SecondAnnoNumber')
        if m.get('SecondAnnoType') is not None:
            self.second_anno_type = m.get('SecondAnnoType')
        if m.get('Share') is not None:
            self.share = m.get('Share')
        if m.get('SimilarGroup') is not None:
            self.similar_group = m.get('SimilarGroup')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubsequentDesignationDate') is not None:
            self.subsequent_designation_date = m.get('SubsequentDesignationDate')
        return self


class DescirbeCombineTrademarkResponseBody(TeaModel):
    def __init__(
        self,
        current_page_number: int = None,
        data: List[DescirbeCombineTrademarkResponseBodyData] = None,
        next_page: bool = None,
        page_size: int = None,
        pre_page: bool = None,
        request_id: str = None,
        total_item_number: int = None,
        total_page_number: int = None,
    ):
        self.current_page_number = current_page_number
        self.data = data
        self.next_page = next_page
        self.page_size = page_size
        self.pre_page = pre_page
        self.request_id = request_id
        self.total_item_number = total_item_number
        self.total_page_number = total_page_number

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
        if self.current_page_number is not None:
            result['CurrentPageNumber'] = self.current_page_number
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.next_page is not None:
            result['NextPage'] = self.next_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.pre_page is not None:
            result['PrePage'] = self.pre_page
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_item_number is not None:
            result['TotalItemNumber'] = self.total_item_number
        if self.total_page_number is not None:
            result['TotalPageNumber'] = self.total_page_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPageNumber') is not None:
            self.current_page_number = m.get('CurrentPageNumber')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescirbeCombineTrademarkResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('NextPage') is not None:
            self.next_page = m.get('NextPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PrePage') is not None:
            self.pre_page = m.get('PrePage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalItemNumber') is not None:
            self.total_item_number = m.get('TotalItemNumber')
        if m.get('TotalPageNumber') is not None:
            self.total_page_number = m.get('TotalPageNumber')
        return self


class DescirbeCombineTrademarkResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescirbeCombineTrademarkResponseBody = None,
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
            temp_model = DescirbeCombineTrademarkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FillLogisticsRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        logistics: str = None,
    ):
        self.biz_id = biz_id
        self.logistics = logistics

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.logistics is not None:
            result['Logistics'] = self.logistics
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Logistics') is not None:
            self.logistics = m.get('Logistics')
        return self


class FillLogisticsResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_msg = error_msg
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
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class FillLogisticsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: FillLogisticsResponseBody = None,
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
            temp_model = FillLogisticsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FilterUnavailableCodesRequest(TeaModel):
    def __init__(
        self,
        codes: Dict[str, Any] = None,
    ):
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


class FilterUnavailableCodesShrinkRequest(TeaModel):
    def __init__(
        self,
        codes_shrink: str = None,
    ):
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


class FilterUnavailableCodesResponseBodyData(TeaModel):
    def __init__(
        self,
        codes: List[str] = None,
    ):
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


class FilterUnavailableCodesResponseBody(TeaModel):
    def __init__(
        self,
        data: FilterUnavailableCodesResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = FilterUnavailableCodesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class FilterUnavailableCodesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: FilterUnavailableCodesResponseBody = None,
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
            temp_model = FilterUnavailableCodesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ForceUploadTrademarkOnsaleRequest(TeaModel):
    def __init__(
        self,
        begin_time: int = None,
        classification_code: str = None,
        description: str = None,
        end_time: int = None,
        label: str = None,
        original_price: float = None,
        owner_en_name: str = None,
        owner_name: str = None,
        reason: str = None,
        reg_ann_date: int = None,
        secondary_classification: str = None,
        third_classification: str = None,
        tm_icon: str = None,
        tm_name: str = None,
        tm_number: str = None,
        type: str = None,
    ):
        self.begin_time = begin_time
        self.classification_code = classification_code
        self.description = description
        self.end_time = end_time
        self.label = label
        self.original_price = original_price
        self.owner_en_name = owner_en_name
        self.owner_name = owner_name
        self.reason = reason
        self.reg_ann_date = reg_ann_date
        self.secondary_classification = secondary_classification
        self.third_classification = third_classification
        self.tm_icon = tm_icon
        self.tm_name = tm_name
        self.tm_number = tm_number
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.classification_code is not None:
            result['ClassificationCode'] = self.classification_code
        if self.description is not None:
            result['Description'] = self.description
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.label is not None:
            result['Label'] = self.label
        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price
        if self.owner_en_name is not None:
            result['OwnerEnName'] = self.owner_en_name
        if self.owner_name is not None:
            result['OwnerName'] = self.owner_name
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.reg_ann_date is not None:
            result['RegAnnDate'] = self.reg_ann_date
        if self.secondary_classification is not None:
            result['SecondaryClassification'] = self.secondary_classification
        if self.third_classification is not None:
            result['ThirdClassification'] = self.third_classification
        if self.tm_icon is not None:
            result['TmIcon'] = self.tm_icon
        if self.tm_name is not None:
            result['TmName'] = self.tm_name
        if self.tm_number is not None:
            result['TmNumber'] = self.tm_number
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('ClassificationCode') is not None:
            self.classification_code = m.get('ClassificationCode')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('OriginalPrice') is not None:
            self.original_price = m.get('OriginalPrice')
        if m.get('OwnerEnName') is not None:
            self.owner_en_name = m.get('OwnerEnName')
        if m.get('OwnerName') is not None:
            self.owner_name = m.get('OwnerName')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('RegAnnDate') is not None:
            self.reg_ann_date = m.get('RegAnnDate')
        if m.get('SecondaryClassification') is not None:
            self.secondary_classification = m.get('SecondaryClassification')
        if m.get('ThirdClassification') is not None:
            self.third_classification = m.get('ThirdClassification')
        if m.get('TmIcon') is not None:
            self.tm_icon = m.get('TmIcon')
        if m.get('TmName') is not None:
            self.tm_name = m.get('TmName')
        if m.get('TmNumber') is not None:
            self.tm_number = m.get('TmNumber')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ForceUploadTrademarkOnsaleResponseBody(TeaModel):
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


class ForceUploadTrademarkOnsaleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ForceUploadTrademarkOnsaleResponseBody = None,
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
            temp_model = ForceUploadTrademarkOnsaleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateQrCodeRequest(TeaModel):
    def __init__(
        self,
        field_key: str = None,
        oss_key: str = None,
        uuid: str = None,
    ):
        self.field_key = field_key
        self.oss_key = oss_key
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field_key is not None:
            result['FieldKey'] = self.field_key
        if self.oss_key is not None:
            result['OssKey'] = self.oss_key
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FieldKey') is not None:
            self.field_key = m.get('FieldKey')
        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class GenerateQrCodeResponseBody(TeaModel):
    def __init__(
        self,
        expire_time: int = None,
        field_key: str = None,
        qrcode_url: str = None,
        request_id: str = None,
        success: bool = None,
        uuid: str = None,
    ):
        self.expire_time = expire_time
        self.field_key = field_key
        self.qrcode_url = qrcode_url
        self.request_id = request_id
        self.success = success
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.field_key is not None:
            result['FieldKey'] = self.field_key
        if self.qrcode_url is not None:
            result['QrcodeUrl'] = self.qrcode_url
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('FieldKey') is not None:
            self.field_key = m.get('FieldKey')
        if m.get('QrcodeUrl') is not None:
            self.qrcode_url = m.get('QrcodeUrl')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class GenerateQrCodeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GenerateQrCodeResponseBody = None,
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
            temp_model = GenerateQrCodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateUploadFilePolicyRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        file_type: str = None,
    ):
        self.biz_id = biz_id
        self.file_type = file_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.file_type is not None:
            result['FileType'] = self.file_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
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
        # accessId
        self.access_id = access_id
        # osspolicy
        self.encoded_policy = encoded_policy
        self.expire_time = expire_time
        self.file_dir = file_dir
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
            temp_model = GenerateUploadFilePolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAuthorizationLetterVersionRequest(TeaModel):
    def __init__(
        self,
        oss_key: str = None,
    ):
        self.oss_key = oss_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.oss_key is not None:
            result['OssKey'] = self.oss_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')
        return self


class GetAuthorizationLetterVersionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        version: str = None,
    ):
        self.request_id = request_id
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class GetAuthorizationLetterVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAuthorizationLetterVersionResponseBody = None,
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
            temp_model = GetAuthorizationLetterVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDefaultPrincipalResponseBody(TeaModel):
    def __init__(
        self,
        principal_description: str = None,
        principal_name: str = None,
        principal_value: int = None,
        request_id: str = None,
    ):
        self.principal_description = principal_description
        self.principal_name = principal_name
        self.principal_value = principal_value
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.principal_description is not None:
            result['PrincipalDescription'] = self.principal_description
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name
        if self.principal_value is not None:
            result['PrincipalValue'] = self.principal_value
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PrincipalDescription') is not None:
            self.principal_description = m.get('PrincipalDescription')
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')
        if m.get('PrincipalValue') is not None:
            self.principal_value = m.get('PrincipalValue')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetDefaultPrincipalResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDefaultPrincipalResponseBody = None,
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
            temp_model = GetDefaultPrincipalResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDefaultPrincipalNameRequest(TeaModel):
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


class GetDefaultPrincipalNameResponseBody(TeaModel):
    def __init__(
        self,
        principal_name: int = None,
        request_id: str = None,
    ):
        self.principal_name = principal_name
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetDefaultPrincipalNameResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDefaultPrincipalNameResponseBody = None,
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
            temp_model = GetDefaultPrincipalNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetNotaryOrderRequest(TeaModel):
    def __init__(
        self,
        notary_order_id: int = None,
    ):
        self.notary_order_id = notary_order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.notary_order_id is not None:
            result['NotaryOrderId'] = self.notary_order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NotaryOrderId') is not None:
            self.notary_order_id = m.get('NotaryOrderId')
        return self


class GetNotaryOrderResponseBody(TeaModel):
    def __init__(
        self,
        aliyun_order_id: str = None,
        apply_post_status: int = None,
        biz_id: str = None,
        business_license: str = None,
        business_license_id: str = None,
        company_contact_name: str = None,
        company_contact_phone: str = None,
        error_code: str = None,
        error_msg: str = None,
        legal_person_id_card: str = None,
        legal_person_name: str = None,
        legal_person_phone: str = None,
        name: str = None,
        notary_accept_date: int = None,
        notary_certificate: str = None,
        notary_failed_date: int = None,
        notary_failed_reason: str = None,
        notary_order_id: int = None,
        notary_platform_name: str = None,
        notary_post_receipt: str = None,
        notary_status: int = None,
        notary_succeed_date: int = None,
        notary_type: int = None,
        order_date: int = None,
        order_price: float = None,
        phone: str = None,
        receiver_address: str = None,
        receiver_name: str = None,
        receiver_phone: str = None,
        receiver_postal_code: str = None,
        request_id: str = None,
        seller_back_of_id_card: str = None,
        seller_company_name: str = None,
        seller_front_of_id_card: str = None,
        success: bool = None,
        tm_accept_certificate: str = None,
        tm_classification: str = None,
        tm_image: str = None,
        tm_name: str = None,
        tm_register_certificate: str = None,
        tm_register_change_certificate: str = None,
        tm_register_no: str = None,
        type: str = None,
    ):
        self.aliyun_order_id = aliyun_order_id
        self.apply_post_status = apply_post_status
        self.biz_id = biz_id
        self.business_license = business_license
        self.business_license_id = business_license_id
        self.company_contact_name = company_contact_name
        self.company_contact_phone = company_contact_phone
        self.error_code = error_code
        self.error_msg = error_msg
        self.legal_person_id_card = legal_person_id_card
        self.legal_person_name = legal_person_name
        self.legal_person_phone = legal_person_phone
        self.name = name
        self.notary_accept_date = notary_accept_date
        self.notary_certificate = notary_certificate
        self.notary_failed_date = notary_failed_date
        self.notary_failed_reason = notary_failed_reason
        self.notary_order_id = notary_order_id
        self.notary_platform_name = notary_platform_name
        self.notary_post_receipt = notary_post_receipt
        self.notary_status = notary_status
        self.notary_succeed_date = notary_succeed_date
        self.notary_type = notary_type
        self.order_date = order_date
        self.order_price = order_price
        self.phone = phone
        self.receiver_address = receiver_address
        self.receiver_name = receiver_name
        self.receiver_phone = receiver_phone
        self.receiver_postal_code = receiver_postal_code
        self.request_id = request_id
        self.seller_back_of_id_card = seller_back_of_id_card
        self.seller_company_name = seller_company_name
        self.seller_front_of_id_card = seller_front_of_id_card
        self.success = success
        self.tm_accept_certificate = tm_accept_certificate
        self.tm_classification = tm_classification
        self.tm_image = tm_image
        self.tm_name = tm_name
        self.tm_register_certificate = tm_register_certificate
        self.tm_register_change_certificate = tm_register_change_certificate
        self.tm_register_no = tm_register_no
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aliyun_order_id is not None:
            result['AliyunOrderId'] = self.aliyun_order_id
        if self.apply_post_status is not None:
            result['ApplyPostStatus'] = self.apply_post_status
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.business_license is not None:
            result['BusinessLicense'] = self.business_license
        if self.business_license_id is not None:
            result['BusinessLicenseId'] = self.business_license_id
        if self.company_contact_name is not None:
            result['CompanyContactName'] = self.company_contact_name
        if self.company_contact_phone is not None:
            result['CompanyContactPhone'] = self.company_contact_phone
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.legal_person_id_card is not None:
            result['LegalPersonIdCard'] = self.legal_person_id_card
        if self.legal_person_name is not None:
            result['LegalPersonName'] = self.legal_person_name
        if self.legal_person_phone is not None:
            result['LegalPersonPhone'] = self.legal_person_phone
        if self.name is not None:
            result['Name'] = self.name
        if self.notary_accept_date is not None:
            result['NotaryAcceptDate'] = self.notary_accept_date
        if self.notary_certificate is not None:
            result['NotaryCertificate'] = self.notary_certificate
        if self.notary_failed_date is not None:
            result['NotaryFailedDate'] = self.notary_failed_date
        if self.notary_failed_reason is not None:
            result['NotaryFailedReason'] = self.notary_failed_reason
        if self.notary_order_id is not None:
            result['NotaryOrderId'] = self.notary_order_id
        if self.notary_platform_name is not None:
            result['NotaryPlatformName'] = self.notary_platform_name
        if self.notary_post_receipt is not None:
            result['NotaryPostReceipt'] = self.notary_post_receipt
        if self.notary_status is not None:
            result['NotaryStatus'] = self.notary_status
        if self.notary_succeed_date is not None:
            result['NotarySucceedDate'] = self.notary_succeed_date
        if self.notary_type is not None:
            result['NotaryType'] = self.notary_type
        if self.order_date is not None:
            result['OrderDate'] = self.order_date
        if self.order_price is not None:
            result['OrderPrice'] = self.order_price
        if self.phone is not None:
            result['Phone'] = self.phone
        if self.receiver_address is not None:
            result['ReceiverAddress'] = self.receiver_address
        if self.receiver_name is not None:
            result['ReceiverName'] = self.receiver_name
        if self.receiver_phone is not None:
            result['ReceiverPhone'] = self.receiver_phone
        if self.receiver_postal_code is not None:
            result['ReceiverPostalCode'] = self.receiver_postal_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.seller_back_of_id_card is not None:
            result['SellerBackOfIdCard'] = self.seller_back_of_id_card
        if self.seller_company_name is not None:
            result['SellerCompanyName'] = self.seller_company_name
        if self.seller_front_of_id_card is not None:
            result['SellerFrontOfIdCard'] = self.seller_front_of_id_card
        if self.success is not None:
            result['Success'] = self.success
        if self.tm_accept_certificate is not None:
            result['TmAcceptCertificate'] = self.tm_accept_certificate
        if self.tm_classification is not None:
            result['TmClassification'] = self.tm_classification
        if self.tm_image is not None:
            result['TmImage'] = self.tm_image
        if self.tm_name is not None:
            result['TmName'] = self.tm_name
        if self.tm_register_certificate is not None:
            result['TmRegisterCertificate'] = self.tm_register_certificate
        if self.tm_register_change_certificate is not None:
            result['TmRegisterChangeCertificate'] = self.tm_register_change_certificate
        if self.tm_register_no is not None:
            result['TmRegisterNo'] = self.tm_register_no
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunOrderId') is not None:
            self.aliyun_order_id = m.get('AliyunOrderId')
        if m.get('ApplyPostStatus') is not None:
            self.apply_post_status = m.get('ApplyPostStatus')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BusinessLicense') is not None:
            self.business_license = m.get('BusinessLicense')
        if m.get('BusinessLicenseId') is not None:
            self.business_license_id = m.get('BusinessLicenseId')
        if m.get('CompanyContactName') is not None:
            self.company_contact_name = m.get('CompanyContactName')
        if m.get('CompanyContactPhone') is not None:
            self.company_contact_phone = m.get('CompanyContactPhone')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('LegalPersonIdCard') is not None:
            self.legal_person_id_card = m.get('LegalPersonIdCard')
        if m.get('LegalPersonName') is not None:
            self.legal_person_name = m.get('LegalPersonName')
        if m.get('LegalPersonPhone') is not None:
            self.legal_person_phone = m.get('LegalPersonPhone')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NotaryAcceptDate') is not None:
            self.notary_accept_date = m.get('NotaryAcceptDate')
        if m.get('NotaryCertificate') is not None:
            self.notary_certificate = m.get('NotaryCertificate')
        if m.get('NotaryFailedDate') is not None:
            self.notary_failed_date = m.get('NotaryFailedDate')
        if m.get('NotaryFailedReason') is not None:
            self.notary_failed_reason = m.get('NotaryFailedReason')
        if m.get('NotaryOrderId') is not None:
            self.notary_order_id = m.get('NotaryOrderId')
        if m.get('NotaryPlatformName') is not None:
            self.notary_platform_name = m.get('NotaryPlatformName')
        if m.get('NotaryPostReceipt') is not None:
            self.notary_post_receipt = m.get('NotaryPostReceipt')
        if m.get('NotaryStatus') is not None:
            self.notary_status = m.get('NotaryStatus')
        if m.get('NotarySucceedDate') is not None:
            self.notary_succeed_date = m.get('NotarySucceedDate')
        if m.get('NotaryType') is not None:
            self.notary_type = m.get('NotaryType')
        if m.get('OrderDate') is not None:
            self.order_date = m.get('OrderDate')
        if m.get('OrderPrice') is not None:
            self.order_price = m.get('OrderPrice')
        if m.get('Phone') is not None:
            self.phone = m.get('Phone')
        if m.get('ReceiverAddress') is not None:
            self.receiver_address = m.get('ReceiverAddress')
        if m.get('ReceiverName') is not None:
            self.receiver_name = m.get('ReceiverName')
        if m.get('ReceiverPhone') is not None:
            self.receiver_phone = m.get('ReceiverPhone')
        if m.get('ReceiverPostalCode') is not None:
            self.receiver_postal_code = m.get('ReceiverPostalCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SellerBackOfIdCard') is not None:
            self.seller_back_of_id_card = m.get('SellerBackOfIdCard')
        if m.get('SellerCompanyName') is not None:
            self.seller_company_name = m.get('SellerCompanyName')
        if m.get('SellerFrontOfIdCard') is not None:
            self.seller_front_of_id_card = m.get('SellerFrontOfIdCard')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TmAcceptCertificate') is not None:
            self.tm_accept_certificate = m.get('TmAcceptCertificate')
        if m.get('TmClassification') is not None:
            self.tm_classification = m.get('TmClassification')
        if m.get('TmImage') is not None:
            self.tm_image = m.get('TmImage')
        if m.get('TmName') is not None:
            self.tm_name = m.get('TmName')
        if m.get('TmRegisterCertificate') is not None:
            self.tm_register_certificate = m.get('TmRegisterCertificate')
        if m.get('TmRegisterChangeCertificate') is not None:
            self.tm_register_change_certificate = m.get('TmRegisterChangeCertificate')
        if m.get('TmRegisterNo') is not None:
            self.tm_register_no = m.get('TmRegisterNo')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetNotaryOrderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetNotaryOrderResponseBody = None,
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
            temp_model = GetNotaryOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSupportPrincipalNameResponseBodyPrincipals(TeaModel):
    def __init__(
        self,
        default_principal: bool = None,
        principal_description: str = None,
        principal_value: int = None,
    ):
        self.default_principal = default_principal
        self.principal_description = principal_description
        self.principal_value = principal_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.default_principal is not None:
            result['DefaultPrincipal'] = self.default_principal
        if self.principal_description is not None:
            result['PrincipalDescription'] = self.principal_description
        if self.principal_value is not None:
            result['PrincipalValue'] = self.principal_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultPrincipal') is not None:
            self.default_principal = m.get('DefaultPrincipal')
        if m.get('PrincipalDescription') is not None:
            self.principal_description = m.get('PrincipalDescription')
        if m.get('PrincipalValue') is not None:
            self.principal_value = m.get('PrincipalValue')
        return self


class GetSupportPrincipalNameResponseBody(TeaModel):
    def __init__(
        self,
        principals: List[GetSupportPrincipalNameResponseBodyPrincipals] = None,
        request_id: str = None,
    ):
        self.principals = principals
        self.request_id = request_id

    def validate(self):
        if self.principals:
            for k in self.principals:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Principals'] = []
        if self.principals is not None:
            for k in self.principals:
                result['Principals'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.principals = []
        if m.get('Principals') is not None:
            for k in m.get('Principals'):
                temp_model = GetSupportPrincipalNameResponseBodyPrincipals()
                self.principals.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetSupportPrincipalNameResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetSupportPrincipalNameResponseBody = None,
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
            temp_model = GetSupportPrincipalNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InsertMaterialRequest(TeaModel):
    def __init__(
        self,
        address: str = None,
        business_licence_oss_key: str = None,
        card_number: str = None,
        city: str = None,
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
        loa_oss_key: str = None,
        name: str = None,
        passport_oss_key: str = None,
        personal_type: int = None,
        principal_name: int = None,
        province: str = None,
        region: int = None,
        town: str = None,
        type: int = None,
    ):
        self.address = address
        self.business_licence_oss_key = business_licence_oss_key
        self.card_number = card_number
        self.city = city
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
        self.loa_oss_key = loa_oss_key
        self.name = name
        self.passport_oss_key = passport_oss_key
        self.personal_type = personal_type
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
        if self.business_licence_oss_key is not None:
            result['BusinessLicenceOssKey'] = self.business_licence_oss_key
        if self.card_number is not None:
            result['CardNumber'] = self.card_number
        if self.city is not None:
            result['City'] = self.city
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
        if self.loa_oss_key is not None:
            result['LoaOssKey'] = self.loa_oss_key
        if self.name is not None:
            result['Name'] = self.name
        if self.passport_oss_key is not None:
            result['PassportOssKey'] = self.passport_oss_key
        if self.personal_type is not None:
            result['PersonalType'] = self.personal_type
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
        if m.get('BusinessLicenceOssKey') is not None:
            self.business_licence_oss_key = m.get('BusinessLicenceOssKey')
        if m.get('CardNumber') is not None:
            self.card_number = m.get('CardNumber')
        if m.get('City') is not None:
            self.city = m.get('City')
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
        if m.get('LoaOssKey') is not None:
            self.loa_oss_key = m.get('LoaOssKey')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PassportOssKey') is not None:
            self.passport_oss_key = m.get('PassportOssKey')
        if m.get('PersonalType') is not None:
            self.personal_type = m.get('PersonalType')
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


class InsertMaterialResponseBody(TeaModel):
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


class InsertMaterialResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: InsertMaterialResponseBody = None,
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
            temp_model = InsertMaterialResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InsertRenewInfoRequest(TeaModel):
    def __init__(
        self,
        address: str = None,
        eng_address: str = None,
        eng_name: str = None,
        name: str = None,
        register_time: int = None,
    ):
        self.address = address
        self.eng_address = eng_address
        self.eng_name = eng_name
        self.name = name
        self.register_time = register_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.eng_address is not None:
            result['EngAddress'] = self.eng_address
        if self.eng_name is not None:
            result['EngName'] = self.eng_name
        if self.name is not None:
            result['Name'] = self.name
        if self.register_time is not None:
            result['RegisterTime'] = self.register_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('EngAddress') is not None:
            self.eng_address = m.get('EngAddress')
        if m.get('EngName') is not None:
            self.eng_name = m.get('EngName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegisterTime') is not None:
            self.register_time = m.get('RegisterTime')
        return self


class InsertRenewInfoResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_msg: str = None,
        id: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_msg = error_msg
        self.id = id
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
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class InsertRenewInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: InsertRenewInfoResponseBody = None,
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
            temp_model = InsertRenewInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InsertTmMonitorRuleRequest(TeaModel):
    def __init__(
        self,
        classification: Dict[str, Any] = None,
        end_apply_date: str = None,
        notify_status: Dict[str, Any] = None,
        rule_keyword: str = None,
        rule_name: str = None,
        rule_source: str = None,
        rule_type: int = None,
        start_apply_date: str = None,
    ):
        self.classification = classification
        self.end_apply_date = end_apply_date
        self.notify_status = notify_status
        self.rule_keyword = rule_keyword
        self.rule_name = rule_name
        self.rule_source = rule_source
        self.rule_type = rule_type
        self.start_apply_date = start_apply_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.classification is not None:
            result['Classification'] = self.classification
        if self.end_apply_date is not None:
            result['EndApplyDate'] = self.end_apply_date
        if self.notify_status is not None:
            result['NotifyStatus'] = self.notify_status
        if self.rule_keyword is not None:
            result['RuleKeyword'] = self.rule_keyword
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.rule_source is not None:
            result['RuleSource'] = self.rule_source
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        if self.start_apply_date is not None:
            result['StartApplyDate'] = self.start_apply_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Classification') is not None:
            self.classification = m.get('Classification')
        if m.get('EndApplyDate') is not None:
            self.end_apply_date = m.get('EndApplyDate')
        if m.get('NotifyStatus') is not None:
            self.notify_status = m.get('NotifyStatus')
        if m.get('RuleKeyword') is not None:
            self.rule_keyword = m.get('RuleKeyword')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('RuleSource') is not None:
            self.rule_source = m.get('RuleSource')
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        if m.get('StartApplyDate') is not None:
            self.start_apply_date = m.get('StartApplyDate')
        return self


class InsertTmMonitorRuleShrinkRequest(TeaModel):
    def __init__(
        self,
        classification_shrink: str = None,
        end_apply_date: str = None,
        notify_status_shrink: str = None,
        rule_keyword: str = None,
        rule_name: str = None,
        rule_source: str = None,
        rule_type: int = None,
        start_apply_date: str = None,
    ):
        self.classification_shrink = classification_shrink
        self.end_apply_date = end_apply_date
        self.notify_status_shrink = notify_status_shrink
        self.rule_keyword = rule_keyword
        self.rule_name = rule_name
        self.rule_source = rule_source
        self.rule_type = rule_type
        self.start_apply_date = start_apply_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.classification_shrink is not None:
            result['Classification'] = self.classification_shrink
        if self.end_apply_date is not None:
            result['EndApplyDate'] = self.end_apply_date
        if self.notify_status_shrink is not None:
            result['NotifyStatus'] = self.notify_status_shrink
        if self.rule_keyword is not None:
            result['RuleKeyword'] = self.rule_keyword
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.rule_source is not None:
            result['RuleSource'] = self.rule_source
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        if self.start_apply_date is not None:
            result['StartApplyDate'] = self.start_apply_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Classification') is not None:
            self.classification_shrink = m.get('Classification')
        if m.get('EndApplyDate') is not None:
            self.end_apply_date = m.get('EndApplyDate')
        if m.get('NotifyStatus') is not None:
            self.notify_status_shrink = m.get('NotifyStatus')
        if m.get('RuleKeyword') is not None:
            self.rule_keyword = m.get('RuleKeyword')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('RuleSource') is not None:
            self.rule_source = m.get('RuleSource')
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        if m.get('StartApplyDate') is not None:
            self.start_apply_date = m.get('StartApplyDate')
        return self


class InsertTmMonitorRuleResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_msg = error_msg
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
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class InsertTmMonitorRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: InsertTmMonitorRuleResponseBody = None,
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
            temp_model = InsertTmMonitorRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListNotaryInfosRequest(TeaModel):
    def __init__(
        self,
        biz_order_no: str = None,
        notary_type: int = None,
        page_num: int = None,
        page_size: int = None,
        token: str = None,
    ):
        self.biz_order_no = biz_order_no
        self.notary_type = notary_type
        self.page_num = page_num
        self.page_size = page_size
        self.token = token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_order_no is not None:
            result['BizOrderNo'] = self.biz_order_no
        if self.notary_type is not None:
            result['NotaryType'] = self.notary_type
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.token is not None:
            result['Token'] = self.token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizOrderNo') is not None:
            self.biz_order_no = m.get('BizOrderNo')
        if m.get('NotaryType') is not None:
            self.notary_type = m.get('NotaryType')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        return self


class ListNotaryInfosResponseBodyDataNotaryInfo(TeaModel):
    def __init__(
        self,
        biz_order_no: str = None,
        gmt_modified: int = None,
        notary_failed_reason: str = None,
        notary_status: int = None,
        tm_classification: str = None,
        tm_register_no: str = None,
        token: str = None,
    ):
        self.biz_order_no = biz_order_no
        self.gmt_modified = gmt_modified
        self.notary_failed_reason = notary_failed_reason
        self.notary_status = notary_status
        self.tm_classification = tm_classification
        self.tm_register_no = tm_register_no
        # token
        self.token = token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_order_no is not None:
            result['BizOrderNo'] = self.biz_order_no
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.notary_failed_reason is not None:
            result['NotaryFailedReason'] = self.notary_failed_reason
        if self.notary_status is not None:
            result['NotaryStatus'] = self.notary_status
        if self.tm_classification is not None:
            result['TmClassification'] = self.tm_classification
        if self.tm_register_no is not None:
            result['TmRegisterNo'] = self.tm_register_no
        if self.token is not None:
            result['Token'] = self.token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizOrderNo') is not None:
            self.biz_order_no = m.get('BizOrderNo')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('NotaryFailedReason') is not None:
            self.notary_failed_reason = m.get('NotaryFailedReason')
        if m.get('NotaryStatus') is not None:
            self.notary_status = m.get('NotaryStatus')
        if m.get('TmClassification') is not None:
            self.tm_classification = m.get('TmClassification')
        if m.get('TmRegisterNo') is not None:
            self.tm_register_no = m.get('TmRegisterNo')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        return self


class ListNotaryInfosResponseBodyData(TeaModel):
    def __init__(
        self,
        notary_info: List[ListNotaryInfosResponseBodyDataNotaryInfo] = None,
    ):
        self.notary_info = notary_info

    def validate(self):
        if self.notary_info:
            for k in self.notary_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['NotaryInfo'] = []
        if self.notary_info is not None:
            for k in self.notary_info:
                result['NotaryInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.notary_info = []
        if m.get('NotaryInfo') is not None:
            for k in m.get('NotaryInfo'):
                temp_model = ListNotaryInfosResponseBodyDataNotaryInfo()
                self.notary_info.append(temp_model.from_map(k))
        return self


class ListNotaryInfosResponseBody(TeaModel):
    def __init__(
        self,
        current_page_num: int = None,
        data: ListNotaryInfosResponseBodyData = None,
        error_code: str = None,
        error_msg: str = None,
        next_page: bool = None,
        page_size: int = None,
        pre_page: bool = None,
        request_id: str = None,
        success: bool = None,
        total_item_num: int = None,
        total_page_num: int = None,
    ):
        self.current_page_num = current_page_num
        self.data = data
        self.error_code = error_code
        self.error_msg = error_msg
        self.next_page = next_page
        self.page_size = page_size
        self.pre_page = pre_page
        self.request_id = request_id
        self.success = success
        self.total_item_num = total_item_num
        self.total_page_num = total_page_num

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page_num is not None:
            result['CurrentPageNum'] = self.current_page_num
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.next_page is not None:
            result['NextPage'] = self.next_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.pre_page is not None:
            result['PrePage'] = self.pre_page
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_item_num is not None:
            result['TotalItemNum'] = self.total_item_num
        if self.total_page_num is not None:
            result['TotalPageNum'] = self.total_page_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPageNum') is not None:
            self.current_page_num = m.get('CurrentPageNum')
        if m.get('Data') is not None:
            temp_model = ListNotaryInfosResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('NextPage') is not None:
            self.next_page = m.get('NextPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PrePage') is not None:
            self.pre_page = m.get('PrePage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalItemNum') is not None:
            self.total_item_num = m.get('TotalItemNum')
        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')
        return self


class ListNotaryInfosResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListNotaryInfosResponseBody = None,
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
            temp_model = ListNotaryInfosResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListNotaryOrdersRequest(TeaModel):
    def __init__(
        self,
        aliyun_order_id: str = None,
        biz_id: str = None,
        end_order_date: int = None,
        notary_status: int = None,
        notary_type: int = None,
        page_num: int = None,
        page_size: int = None,
        sort_by_type: str = None,
        sort_key_type: int = None,
        start_order_date: int = None,
    ):
        self.aliyun_order_id = aliyun_order_id
        self.biz_id = biz_id
        self.end_order_date = end_order_date
        self.notary_status = notary_status
        self.notary_type = notary_type
        self.page_num = page_num
        self.page_size = page_size
        self.sort_by_type = sort_by_type
        self.sort_key_type = sort_key_type
        self.start_order_date = start_order_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aliyun_order_id is not None:
            result['AliyunOrderId'] = self.aliyun_order_id
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.end_order_date is not None:
            result['EndOrderDate'] = self.end_order_date
        if self.notary_status is not None:
            result['NotaryStatus'] = self.notary_status
        if self.notary_type is not None:
            result['NotaryType'] = self.notary_type
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sort_by_type is not None:
            result['SortByType'] = self.sort_by_type
        if self.sort_key_type is not None:
            result['SortKeyType'] = self.sort_key_type
        if self.start_order_date is not None:
            result['StartOrderDate'] = self.start_order_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunOrderId') is not None:
            self.aliyun_order_id = m.get('AliyunOrderId')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('EndOrderDate') is not None:
            self.end_order_date = m.get('EndOrderDate')
        if m.get('NotaryStatus') is not None:
            self.notary_status = m.get('NotaryStatus')
        if m.get('NotaryType') is not None:
            self.notary_type = m.get('NotaryType')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SortByType') is not None:
            self.sort_by_type = m.get('SortByType')
        if m.get('SortKeyType') is not None:
            self.sort_key_type = m.get('SortKeyType')
        if m.get('StartOrderDate') is not None:
            self.start_order_date = m.get('StartOrderDate')
        return self


class ListNotaryOrdersResponseBodyDataNotaryOrder(TeaModel):
    def __init__(
        self,
        aliyun_order_id: str = None,
        apply_post_status: str = None,
        biz_id: str = None,
        gmt_modified: int = None,
        notary_certificate: str = None,
        notary_order_id: int = None,
        notary_platform_name: str = None,
        notary_status: int = None,
        notary_type: int = None,
        order_date: int = None,
        order_price: float = None,
        tm_classification: str = None,
        tm_image: str = None,
        tm_name: str = None,
        tm_register_no: str = None,
    ):
        self.aliyun_order_id = aliyun_order_id
        self.apply_post_status = apply_post_status
        self.biz_id = biz_id
        self.gmt_modified = gmt_modified
        self.notary_certificate = notary_certificate
        self.notary_order_id = notary_order_id
        self.notary_platform_name = notary_platform_name
        self.notary_status = notary_status
        self.notary_type = notary_type
        self.order_date = order_date
        self.order_price = order_price
        self.tm_classification = tm_classification
        self.tm_image = tm_image
        self.tm_name = tm_name
        self.tm_register_no = tm_register_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aliyun_order_id is not None:
            result['AliyunOrderId'] = self.aliyun_order_id
        if self.apply_post_status is not None:
            result['ApplyPostStatus'] = self.apply_post_status
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.notary_certificate is not None:
            result['NotaryCertificate'] = self.notary_certificate
        if self.notary_order_id is not None:
            result['NotaryOrderId'] = self.notary_order_id
        if self.notary_platform_name is not None:
            result['NotaryPlatformName'] = self.notary_platform_name
        if self.notary_status is not None:
            result['NotaryStatus'] = self.notary_status
        if self.notary_type is not None:
            result['NotaryType'] = self.notary_type
        if self.order_date is not None:
            result['OrderDate'] = self.order_date
        if self.order_price is not None:
            result['OrderPrice'] = self.order_price
        if self.tm_classification is not None:
            result['TmClassification'] = self.tm_classification
        if self.tm_image is not None:
            result['TmImage'] = self.tm_image
        if self.tm_name is not None:
            result['TmName'] = self.tm_name
        if self.tm_register_no is not None:
            result['TmRegisterNo'] = self.tm_register_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunOrderId') is not None:
            self.aliyun_order_id = m.get('AliyunOrderId')
        if m.get('ApplyPostStatus') is not None:
            self.apply_post_status = m.get('ApplyPostStatus')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('NotaryCertificate') is not None:
            self.notary_certificate = m.get('NotaryCertificate')
        if m.get('NotaryOrderId') is not None:
            self.notary_order_id = m.get('NotaryOrderId')
        if m.get('NotaryPlatformName') is not None:
            self.notary_platform_name = m.get('NotaryPlatformName')
        if m.get('NotaryStatus') is not None:
            self.notary_status = m.get('NotaryStatus')
        if m.get('NotaryType') is not None:
            self.notary_type = m.get('NotaryType')
        if m.get('OrderDate') is not None:
            self.order_date = m.get('OrderDate')
        if m.get('OrderPrice') is not None:
            self.order_price = m.get('OrderPrice')
        if m.get('TmClassification') is not None:
            self.tm_classification = m.get('TmClassification')
        if m.get('TmImage') is not None:
            self.tm_image = m.get('TmImage')
        if m.get('TmName') is not None:
            self.tm_name = m.get('TmName')
        if m.get('TmRegisterNo') is not None:
            self.tm_register_no = m.get('TmRegisterNo')
        return self


class ListNotaryOrdersResponseBodyData(TeaModel):
    def __init__(
        self,
        notary_order: List[ListNotaryOrdersResponseBodyDataNotaryOrder] = None,
    ):
        self.notary_order = notary_order

    def validate(self):
        if self.notary_order:
            for k in self.notary_order:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['NotaryOrder'] = []
        if self.notary_order is not None:
            for k in self.notary_order:
                result['NotaryOrder'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.notary_order = []
        if m.get('NotaryOrder') is not None:
            for k in m.get('NotaryOrder'):
                temp_model = ListNotaryOrdersResponseBodyDataNotaryOrder()
                self.notary_order.append(temp_model.from_map(k))
        return self


class ListNotaryOrdersResponseBody(TeaModel):
    def __init__(
        self,
        current_page_num: int = None,
        data: ListNotaryOrdersResponseBodyData = None,
        error_code: str = None,
        error_msg: str = None,
        next_page: bool = None,
        page_size: int = None,
        pre_page: bool = None,
        request_id: str = None,
        success: bool = None,
        total_item_num: int = None,
        total_page_num: int = None,
    ):
        self.current_page_num = current_page_num
        self.data = data
        self.error_code = error_code
        self.error_msg = error_msg
        self.next_page = next_page
        self.page_size = page_size
        self.pre_page = pre_page
        self.request_id = request_id
        self.success = success
        self.total_item_num = total_item_num
        self.total_page_num = total_page_num

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page_num is not None:
            result['CurrentPageNum'] = self.current_page_num
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.next_page is not None:
            result['NextPage'] = self.next_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.pre_page is not None:
            result['PrePage'] = self.pre_page
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_item_num is not None:
            result['TotalItemNum'] = self.total_item_num
        if self.total_page_num is not None:
            result['TotalPageNum'] = self.total_page_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPageNum') is not None:
            self.current_page_num = m.get('CurrentPageNum')
        if m.get('Data') is not None:
            temp_model = ListNotaryOrdersResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('NextPage') is not None:
            self.next_page = m.get('NextPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PrePage') is not None:
            self.pre_page = m.get('PrePage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalItemNum') is not None:
            self.total_item_num = m.get('TotalItemNum')
        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')
        return self


class ListNotaryOrdersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListNotaryOrdersResponseBody = None,
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
            temp_model = ListNotaryOrdersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTrademarkSbjKeyRequest(TeaModel):
    def __init__(
        self,
        principal_key: str = None,
        principal_name: str = None,
    ):
        self.principal_key = principal_key
        self.principal_name = principal_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.principal_key is not None:
            result['PrincipalKey'] = self.principal_key
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PrincipalKey') is not None:
            self.principal_key = m.get('PrincipalKey')
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')
        return self


class ListTrademarkSbjKeyResponseBodyTmSbjKeyInfo(TeaModel):
    def __init__(
        self,
        agent_id: str = None,
        agree_prot: str = None,
        cert_info: str = None,
        clear_data: str = None,
        hash_data: str = None,
        key_type: int = None,
        name: str = None,
        pin: str = None,
        principal_key: str = None,
        principal_name: str = None,
        sign_cert: str = None,
        sign_data: str = None,
        start_valid_date: str = None,
        submit_sign_data: str = None,
        type_cert: str = None,
        username: str = None,
        valid_date: str = None,
        tmurl: str = None,
    ):
        self.agent_id = agent_id
        self.agree_prot = agree_prot
        self.cert_info = cert_info
        self.clear_data = clear_data
        self.hash_data = hash_data
        self.key_type = key_type
        self.name = name
        self.pin = pin
        self.principal_key = principal_key
        self.principal_name = principal_name
        self.sign_cert = sign_cert
        self.sign_data = sign_data
        self.start_valid_date = start_valid_date
        self.submit_sign_data = submit_sign_data
        self.type_cert = type_cert
        self.username = username
        self.valid_date = valid_date
        self.tmurl = tmurl

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_id is not None:
            result['AgentId'] = self.agent_id
        if self.agree_prot is not None:
            result['AgreeProt'] = self.agree_prot
        if self.cert_info is not None:
            result['CertInfo'] = self.cert_info
        if self.clear_data is not None:
            result['ClearData'] = self.clear_data
        if self.hash_data is not None:
            result['HashData'] = self.hash_data
        if self.key_type is not None:
            result['KeyType'] = self.key_type
        if self.name is not None:
            result['Name'] = self.name
        if self.pin is not None:
            result['Pin'] = self.pin
        if self.principal_key is not None:
            result['PrincipalKey'] = self.principal_key
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name
        if self.sign_cert is not None:
            result['SignCert'] = self.sign_cert
        if self.sign_data is not None:
            result['SignData'] = self.sign_data
        if self.start_valid_date is not None:
            result['StartValidDate'] = self.start_valid_date
        if self.submit_sign_data is not None:
            result['SubmitSignData'] = self.submit_sign_data
        if self.type_cert is not None:
            result['TypeCert'] = self.type_cert
        if self.username is not None:
            result['Username'] = self.username
        if self.valid_date is not None:
            result['ValidDate'] = self.valid_date
        if self.tmurl is not None:
            result['tmurl'] = self.tmurl
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')
        if m.get('AgreeProt') is not None:
            self.agree_prot = m.get('AgreeProt')
        if m.get('CertInfo') is not None:
            self.cert_info = m.get('CertInfo')
        if m.get('ClearData') is not None:
            self.clear_data = m.get('ClearData')
        if m.get('HashData') is not None:
            self.hash_data = m.get('HashData')
        if m.get('KeyType') is not None:
            self.key_type = m.get('KeyType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Pin') is not None:
            self.pin = m.get('Pin')
        if m.get('PrincipalKey') is not None:
            self.principal_key = m.get('PrincipalKey')
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')
        if m.get('SignCert') is not None:
            self.sign_cert = m.get('SignCert')
        if m.get('SignData') is not None:
            self.sign_data = m.get('SignData')
        if m.get('StartValidDate') is not None:
            self.start_valid_date = m.get('StartValidDate')
        if m.get('SubmitSignData') is not None:
            self.submit_sign_data = m.get('SubmitSignData')
        if m.get('TypeCert') is not None:
            self.type_cert = m.get('TypeCert')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        if m.get('ValidDate') is not None:
            self.valid_date = m.get('ValidDate')
        if m.get('tmurl') is not None:
            self.tmurl = m.get('tmurl')
        return self


class ListTrademarkSbjKeyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        tm_sbj_key_info: List[ListTrademarkSbjKeyResponseBodyTmSbjKeyInfo] = None,
    ):
        self.request_id = request_id
        self.tm_sbj_key_info = tm_sbj_key_info

    def validate(self):
        if self.tm_sbj_key_info:
            for k in self.tm_sbj_key_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TmSbjKeyInfo'] = []
        if self.tm_sbj_key_info is not None:
            for k in self.tm_sbj_key_info:
                result['TmSbjKeyInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.tm_sbj_key_info = []
        if m.get('TmSbjKeyInfo') is not None:
            for k in m.get('TmSbjKeyInfo'):
                temp_model = ListTrademarkSbjKeyResponseBodyTmSbjKeyInfo()
                self.tm_sbj_key_info.append(temp_model.from_map(k))
        return self


class ListTrademarkSbjKeyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTrademarkSbjKeyResponseBody = None,
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
            temp_model = ListTrademarkSbjKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifySubmitTransferMaterailRequest(TeaModel):
    def __init__(
        self,
        addr: str = None,
        assignee_proxy: str = None,
        biz_id: str = None,
        buyer_business_license: str = None,
        buyer_business_license_translation: str = None,
        buyer_id_card: str = None,
        card_no: str = None,
        card_type: str = None,
        complete: bool = None,
        contact_email: str = None,
        contact_mobile: str = None,
        contact_name: str = None,
        name: str = None,
        notarization: str = None,
        note: str = None,
        other: Dict[str, Any] = None,
        registration_cert: str = None,
        seller_apply: str = None,
        seller_business_license: str = None,
        seller_business_license_translation: str = None,
        seller_id_card: str = None,
        seller_proxy: str = None,
        trade_material_full_update: bool = None,
    ):
        self.addr = addr
        self.assignee_proxy = assignee_proxy
        self.biz_id = biz_id
        self.buyer_business_license = buyer_business_license
        self.buyer_business_license_translation = buyer_business_license_translation
        self.buyer_id_card = buyer_id_card
        self.card_no = card_no
        self.card_type = card_type
        self.complete = complete
        self.contact_email = contact_email
        self.contact_mobile = contact_mobile
        self.contact_name = contact_name
        self.name = name
        self.notarization = notarization
        self.note = note
        self.other = other
        self.registration_cert = registration_cert
        self.seller_apply = seller_apply
        self.seller_business_license = seller_business_license
        self.seller_business_license_translation = seller_business_license_translation
        self.seller_id_card = seller_id_card
        self.seller_proxy = seller_proxy
        self.trade_material_full_update = trade_material_full_update

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.addr is not None:
            result['Addr'] = self.addr
        if self.assignee_proxy is not None:
            result['AssigneeProxy'] = self.assignee_proxy
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.buyer_business_license is not None:
            result['BuyerBusinessLicense'] = self.buyer_business_license
        if self.buyer_business_license_translation is not None:
            result['BuyerBusinessLicenseTranslation'] = self.buyer_business_license_translation
        if self.buyer_id_card is not None:
            result['BuyerIdCard'] = self.buyer_id_card
        if self.card_no is not None:
            result['CardNo'] = self.card_no
        if self.card_type is not None:
            result['CardType'] = self.card_type
        if self.complete is not None:
            result['Complete'] = self.complete
        if self.contact_email is not None:
            result['ContactEmail'] = self.contact_email
        if self.contact_mobile is not None:
            result['ContactMobile'] = self.contact_mobile
        if self.contact_name is not None:
            result['ContactName'] = self.contact_name
        if self.name is not None:
            result['Name'] = self.name
        if self.notarization is not None:
            result['Notarization'] = self.notarization
        if self.note is not None:
            result['Note'] = self.note
        if self.other is not None:
            result['Other'] = self.other
        if self.registration_cert is not None:
            result['RegistrationCert'] = self.registration_cert
        if self.seller_apply is not None:
            result['SellerApply'] = self.seller_apply
        if self.seller_business_license is not None:
            result['SellerBusinessLicense'] = self.seller_business_license
        if self.seller_business_license_translation is not None:
            result['SellerBusinessLicenseTranslation'] = self.seller_business_license_translation
        if self.seller_id_card is not None:
            result['SellerIdCard'] = self.seller_id_card
        if self.seller_proxy is not None:
            result['SellerProxy'] = self.seller_proxy
        if self.trade_material_full_update is not None:
            result['TradeMaterialFullUpdate'] = self.trade_material_full_update
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Addr') is not None:
            self.addr = m.get('Addr')
        if m.get('AssigneeProxy') is not None:
            self.assignee_proxy = m.get('AssigneeProxy')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BuyerBusinessLicense') is not None:
            self.buyer_business_license = m.get('BuyerBusinessLicense')
        if m.get('BuyerBusinessLicenseTranslation') is not None:
            self.buyer_business_license_translation = m.get('BuyerBusinessLicenseTranslation')
        if m.get('BuyerIdCard') is not None:
            self.buyer_id_card = m.get('BuyerIdCard')
        if m.get('CardNo') is not None:
            self.card_no = m.get('CardNo')
        if m.get('CardType') is not None:
            self.card_type = m.get('CardType')
        if m.get('Complete') is not None:
            self.complete = m.get('Complete')
        if m.get('ContactEmail') is not None:
            self.contact_email = m.get('ContactEmail')
        if m.get('ContactMobile') is not None:
            self.contact_mobile = m.get('ContactMobile')
        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Notarization') is not None:
            self.notarization = m.get('Notarization')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        if m.get('Other') is not None:
            self.other = m.get('Other')
        if m.get('RegistrationCert') is not None:
            self.registration_cert = m.get('RegistrationCert')
        if m.get('SellerApply') is not None:
            self.seller_apply = m.get('SellerApply')
        if m.get('SellerBusinessLicense') is not None:
            self.seller_business_license = m.get('SellerBusinessLicense')
        if m.get('SellerBusinessLicenseTranslation') is not None:
            self.seller_business_license_translation = m.get('SellerBusinessLicenseTranslation')
        if m.get('SellerIdCard') is not None:
            self.seller_id_card = m.get('SellerIdCard')
        if m.get('SellerProxy') is not None:
            self.seller_proxy = m.get('SellerProxy')
        if m.get('TradeMaterialFullUpdate') is not None:
            self.trade_material_full_update = m.get('TradeMaterialFullUpdate')
        return self


class ModifySubmitTransferMaterailShrinkRequest(TeaModel):
    def __init__(
        self,
        addr: str = None,
        assignee_proxy: str = None,
        biz_id: str = None,
        buyer_business_license: str = None,
        buyer_business_license_translation: str = None,
        buyer_id_card: str = None,
        card_no: str = None,
        card_type: str = None,
        complete: bool = None,
        contact_email: str = None,
        contact_mobile: str = None,
        contact_name: str = None,
        name: str = None,
        notarization: str = None,
        note: str = None,
        other_shrink: str = None,
        registration_cert: str = None,
        seller_apply: str = None,
        seller_business_license: str = None,
        seller_business_license_translation: str = None,
        seller_id_card: str = None,
        seller_proxy: str = None,
        trade_material_full_update: bool = None,
    ):
        self.addr = addr
        self.assignee_proxy = assignee_proxy
        self.biz_id = biz_id
        self.buyer_business_license = buyer_business_license
        self.buyer_business_license_translation = buyer_business_license_translation
        self.buyer_id_card = buyer_id_card
        self.card_no = card_no
        self.card_type = card_type
        self.complete = complete
        self.contact_email = contact_email
        self.contact_mobile = contact_mobile
        self.contact_name = contact_name
        self.name = name
        self.notarization = notarization
        self.note = note
        self.other_shrink = other_shrink
        self.registration_cert = registration_cert
        self.seller_apply = seller_apply
        self.seller_business_license = seller_business_license
        self.seller_business_license_translation = seller_business_license_translation
        self.seller_id_card = seller_id_card
        self.seller_proxy = seller_proxy
        self.trade_material_full_update = trade_material_full_update

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.addr is not None:
            result['Addr'] = self.addr
        if self.assignee_proxy is not None:
            result['AssigneeProxy'] = self.assignee_proxy
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.buyer_business_license is not None:
            result['BuyerBusinessLicense'] = self.buyer_business_license
        if self.buyer_business_license_translation is not None:
            result['BuyerBusinessLicenseTranslation'] = self.buyer_business_license_translation
        if self.buyer_id_card is not None:
            result['BuyerIdCard'] = self.buyer_id_card
        if self.card_no is not None:
            result['CardNo'] = self.card_no
        if self.card_type is not None:
            result['CardType'] = self.card_type
        if self.complete is not None:
            result['Complete'] = self.complete
        if self.contact_email is not None:
            result['ContactEmail'] = self.contact_email
        if self.contact_mobile is not None:
            result['ContactMobile'] = self.contact_mobile
        if self.contact_name is not None:
            result['ContactName'] = self.contact_name
        if self.name is not None:
            result['Name'] = self.name
        if self.notarization is not None:
            result['Notarization'] = self.notarization
        if self.note is not None:
            result['Note'] = self.note
        if self.other_shrink is not None:
            result['Other'] = self.other_shrink
        if self.registration_cert is not None:
            result['RegistrationCert'] = self.registration_cert
        if self.seller_apply is not None:
            result['SellerApply'] = self.seller_apply
        if self.seller_business_license is not None:
            result['SellerBusinessLicense'] = self.seller_business_license
        if self.seller_business_license_translation is not None:
            result['SellerBusinessLicenseTranslation'] = self.seller_business_license_translation
        if self.seller_id_card is not None:
            result['SellerIdCard'] = self.seller_id_card
        if self.seller_proxy is not None:
            result['SellerProxy'] = self.seller_proxy
        if self.trade_material_full_update is not None:
            result['TradeMaterialFullUpdate'] = self.trade_material_full_update
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Addr') is not None:
            self.addr = m.get('Addr')
        if m.get('AssigneeProxy') is not None:
            self.assignee_proxy = m.get('AssigneeProxy')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BuyerBusinessLicense') is not None:
            self.buyer_business_license = m.get('BuyerBusinessLicense')
        if m.get('BuyerBusinessLicenseTranslation') is not None:
            self.buyer_business_license_translation = m.get('BuyerBusinessLicenseTranslation')
        if m.get('BuyerIdCard') is not None:
            self.buyer_id_card = m.get('BuyerIdCard')
        if m.get('CardNo') is not None:
            self.card_no = m.get('CardNo')
        if m.get('CardType') is not None:
            self.card_type = m.get('CardType')
        if m.get('Complete') is not None:
            self.complete = m.get('Complete')
        if m.get('ContactEmail') is not None:
            self.contact_email = m.get('ContactEmail')
        if m.get('ContactMobile') is not None:
            self.contact_mobile = m.get('ContactMobile')
        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Notarization') is not None:
            self.notarization = m.get('Notarization')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        if m.get('Other') is not None:
            self.other_shrink = m.get('Other')
        if m.get('RegistrationCert') is not None:
            self.registration_cert = m.get('RegistrationCert')
        if m.get('SellerApply') is not None:
            self.seller_apply = m.get('SellerApply')
        if m.get('SellerBusinessLicense') is not None:
            self.seller_business_license = m.get('SellerBusinessLicense')
        if m.get('SellerBusinessLicenseTranslation') is not None:
            self.seller_business_license_translation = m.get('SellerBusinessLicenseTranslation')
        if m.get('SellerIdCard') is not None:
            self.seller_id_card = m.get('SellerIdCard')
        if m.get('SellerProxy') is not None:
            self.seller_proxy = m.get('SellerProxy')
        if m.get('TradeMaterialFullUpdate') is not None:
            self.trade_material_full_update = m.get('TradeMaterialFullUpdate')
        return self


class ModifySubmitTransferMaterailResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_msg = error_msg
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
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ModifySubmitTransferMaterailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifySubmitTransferMaterailResponseBody = None,
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
            temp_model = ModifySubmitTransferMaterailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OperateProduceRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        biz_type: str = None,
        ext_map: str = None,
        operate_type: str = None,
    ):
        self.biz_id = biz_id
        self.biz_type = biz_type
        self.ext_map = ext_map
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
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.ext_map is not None:
            result['ExtMap'] = self.ext_map
        if self.operate_type is not None:
            result['OperateType'] = self.operate_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('ExtMap') is not None:
            self.ext_map = m.get('ExtMap')
        if m.get('OperateType') is not None:
            self.operate_type = m.get('OperateType')
        return self


class OperateProduceResponseBody(TeaModel):
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
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class OperateProduceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: OperateProduceResponseBody = None,
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
            temp_model = OperateProduceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PartnerUpdateTrademarkNameRequest(TeaModel):
    def __init__(
        self,
        aliyun_kp: str = None,
        bid: str = None,
        biz_id: str = None,
        caller_parent_id: int = None,
        caller_type: str = None,
        event_scene_type: int = None,
        intention_biz_id: str = None,
        tm_comment: str = None,
        tm_icon: str = None,
        tm_name: str = None,
        type: int = None,
    ):
        self.aliyun_kp = aliyun_kp
        self.bid = bid
        self.biz_id = biz_id
        self.caller_parent_id = caller_parent_id
        self.caller_type = caller_type
        self.event_scene_type = event_scene_type
        self.intention_biz_id = intention_biz_id
        self.tm_comment = tm_comment
        self.tm_icon = tm_icon
        self.tm_name = tm_name
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aliyun_kp is not None:
            result['AliyunKp'] = self.aliyun_kp
        if self.bid is not None:
            result['Bid'] = self.bid
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.caller_parent_id is not None:
            result['CallerParentId'] = self.caller_parent_id
        if self.caller_type is not None:
            result['CallerType'] = self.caller_type
        if self.event_scene_type is not None:
            result['EventSceneType'] = self.event_scene_type
        if self.intention_biz_id is not None:
            result['IntentionBizId'] = self.intention_biz_id
        if self.tm_comment is not None:
            result['TmComment'] = self.tm_comment
        if self.tm_icon is not None:
            result['TmIcon'] = self.tm_icon
        if self.tm_name is not None:
            result['TmName'] = self.tm_name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunKp') is not None:
            self.aliyun_kp = m.get('AliyunKp')
        if m.get('Bid') is not None:
            self.bid = m.get('Bid')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('CallerParentId') is not None:
            self.caller_parent_id = m.get('CallerParentId')
        if m.get('CallerType') is not None:
            self.caller_type = m.get('CallerType')
        if m.get('EventSceneType') is not None:
            self.event_scene_type = m.get('EventSceneType')
        if m.get('IntentionBizId') is not None:
            self.intention_biz_id = m.get('IntentionBizId')
        if m.get('TmComment') is not None:
            self.tm_comment = m.get('TmComment')
        if m.get('TmIcon') is not None:
            self.tm_icon = m.get('TmIcon')
        if m.get('TmName') is not None:
            self.tm_name = m.get('TmName')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class PartnerUpdateTrademarkNameResponseBody(TeaModel):
    def __init__(
        self,
        allow_retry: bool = None,
        app_name: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_code: str = None,
        error_msg: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.allow_retry = allow_retry
        self.app_name = app_name
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.error_code = error_code
        self.error_msg = error_msg
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_retry is not None:
            result['AllowRetry'] = self.allow_retry
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowRetry') is not None:
            self.allow_retry = m.get('AllowRetry')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class PartnerUpdateTrademarkNameResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PartnerUpdateTrademarkNameResponseBody = None,
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
            temp_model = PartnerUpdateTrademarkNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryCommunicationLogsRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        page_num: int = None,
        page_size: int = None,
        type: int = None,
    ):
        self.biz_id = biz_id
        self.page_num = page_num
        self.page_size = page_size
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class QueryCommunicationLogsResponseBodyDataTaskList(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        create_time: int = None,
        note: str = None,
        partner_code: str = None,
        update_time: int = None,
    ):
        self.biz_id = biz_id
        self.create_time = create_time
        self.note = note
        self.partner_code = partner_code
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.note is not None:
            result['Note'] = self.note
        if self.partner_code is not None:
            result['PartnerCode'] = self.partner_code
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        if m.get('PartnerCode') is not None:
            self.partner_code = m.get('PartnerCode')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class QueryCommunicationLogsResponseBodyData(TeaModel):
    def __init__(
        self,
        task_list: List[QueryCommunicationLogsResponseBodyDataTaskList] = None,
    ):
        self.task_list = task_list

    def validate(self):
        if self.task_list:
            for k in self.task_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TaskList'] = []
        if self.task_list is not None:
            for k in self.task_list:
                result['TaskList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.task_list = []
        if m.get('TaskList') is not None:
            for k in m.get('TaskList'):
                temp_model = QueryCommunicationLogsResponseBodyDataTaskList()
                self.task_list.append(temp_model.from_map(k))
        return self


class QueryCommunicationLogsResponseBody(TeaModel):
    def __init__(
        self,
        data: QueryCommunicationLogsResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = QueryCommunicationLogsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryCommunicationLogsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryCommunicationLogsResponseBody = None,
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
            temp_model = QueryCommunicationLogsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryCredentialsInfoRequest(TeaModel):
    def __init__(
        self,
        company_name: str = None,
        material_type: str = None,
        oss_key: str = None,
    ):
        self.company_name = company_name
        self.material_type = material_type
        self.oss_key = oss_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.company_name is not None:
            result['CompanyName'] = self.company_name
        if self.material_type is not None:
            result['MaterialType'] = self.material_type
        if self.oss_key is not None:
            result['OssKey'] = self.oss_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompanyName') is not None:
            self.company_name = m.get('CompanyName')
        if m.get('MaterialType') is not None:
            self.material_type = m.get('MaterialType')
        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')
        return self


class QueryCredentialsInfoResponseBodyCredentialsInfo(TeaModel):
    def __init__(
        self,
        address: str = None,
        card_number: str = None,
        company_name: str = None,
        person_name: str = None,
        province: str = None,
    ):
        self.address = address
        self.card_number = card_number
        self.company_name = company_name
        self.person_name = person_name
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
        if self.card_number is not None:
            result['CardNumber'] = self.card_number
        if self.company_name is not None:
            result['CompanyName'] = self.company_name
        if self.person_name is not None:
            result['PersonName'] = self.person_name
        if self.province is not None:
            result['Province'] = self.province
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('CardNumber') is not None:
            self.card_number = m.get('CardNumber')
        if m.get('CompanyName') is not None:
            self.company_name = m.get('CompanyName')
        if m.get('PersonName') is not None:
            self.person_name = m.get('PersonName')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        return self


class QueryCredentialsInfoResponseBody(TeaModel):
    def __init__(
        self,
        credentials_info: QueryCredentialsInfoResponseBodyCredentialsInfo = None,
        request_id: str = None,
    ):
        self.credentials_info = credentials_info
        self.request_id = request_id

    def validate(self):
        if self.credentials_info:
            self.credentials_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.credentials_info is not None:
            result['CredentialsInfo'] = self.credentials_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CredentialsInfo') is not None:
            temp_model = QueryCredentialsInfoResponseBodyCredentialsInfo()
            self.credentials_info = temp_model.from_map(m['CredentialsInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryCredentialsInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryCredentialsInfoResponseBody = None,
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
            temp_model = QueryCredentialsInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryExtensionAttributeRequest(TeaModel):
    def __init__(
        self,
        attribute_key: str = None,
        biz_id: str = None,
    ):
        self.attribute_key = attribute_key
        self.biz_id = biz_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attribute_key is not None:
            result['AttributeKey'] = self.attribute_key
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttributeKey') is not None:
            self.attribute_key = m.get('AttributeKey')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        return self


class QueryExtensionAttributeResponseBody(TeaModel):
    def __init__(
        self,
        attribute_value: str = None,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.attribute_value = attribute_value
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
        if self.attribute_value is not None:
            result['AttributeValue'] = self.attribute_value
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
        if m.get('AttributeValue') is not None:
            self.attribute_value = m.get('AttributeValue')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryExtensionAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryExtensionAttributeResponseBody = None,
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
            temp_model = QueryExtensionAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryIntentionDetailRequest(TeaModel):
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


class QueryIntentionDetailResponseBody(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        classification: str = None,
        create_time: int = None,
        description: str = None,
        mobile: str = None,
        partner_mobile: str = None,
        register_number: str = None,
        relation_biz_id: str = None,
        request_id: str = None,
        status: int = None,
        type: int = None,
        update_time: int = None,
        user_id: str = None,
        user_name: str = None,
    ):
        self.biz_id = biz_id
        self.classification = classification
        self.create_time = create_time
        self.description = description
        self.mobile = mobile
        self.partner_mobile = partner_mobile
        self.register_number = register_number
        self.relation_biz_id = relation_biz_id
        self.request_id = request_id
        self.status = status
        self.type = type
        self.update_time = update_time
        self.user_id = user_id
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.classification is not None:
            result['Classification'] = self.classification
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.partner_mobile is not None:
            result['PartnerMobile'] = self.partner_mobile
        if self.register_number is not None:
            result['RegisterNumber'] = self.register_number
        if self.relation_biz_id is not None:
            result['RelationBizId'] = self.relation_biz_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Classification') is not None:
            self.classification = m.get('Classification')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('PartnerMobile') is not None:
            self.partner_mobile = m.get('PartnerMobile')
        if m.get('RegisterNumber') is not None:
            self.register_number = m.get('RegisterNumber')
        if m.get('RelationBizId') is not None:
            self.relation_biz_id = m.get('RelationBizId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class QueryIntentionDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryIntentionDetailResponseBody = None,
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
            temp_model = QueryIntentionDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryIntentionListRequest(TeaModel):
    def __init__(
        self,
        page_num: int = None,
        page_size: int = None,
        sort_filed: str = None,
        sort_order: str = None,
        status: int = None,
        type: int = None,
    ):
        self.page_num = page_num
        self.page_size = page_size
        self.sort_filed = sort_filed
        self.sort_order = sort_order
        self.status = status
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sort_filed is not None:
            result['SortFiled'] = self.sort_filed
        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SortFiled') is not None:
            self.sort_filed = m.get('SortFiled')
        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class QueryIntentionListResponseBodyDataIntention(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        classification: str = None,
        create_time: int = None,
        description: str = None,
        register_number: str = None,
        status: int = None,
        type: int = None,
        update_time: int = None,
        user_id: str = None,
    ):
        self.biz_id = biz_id
        self.classification = classification
        self.create_time = create_time
        self.description = description
        self.register_number = register_number
        self.status = status
        self.type = type
        self.update_time = update_time
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.classification is not None:
            result['Classification'] = self.classification
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.register_number is not None:
            result['RegisterNumber'] = self.register_number
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Classification') is not None:
            self.classification = m.get('Classification')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('RegisterNumber') is not None:
            self.register_number = m.get('RegisterNumber')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class QueryIntentionListResponseBodyData(TeaModel):
    def __init__(
        self,
        intention: List[QueryIntentionListResponseBodyDataIntention] = None,
    ):
        self.intention = intention

    def validate(self):
        if self.intention:
            for k in self.intention:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Intention'] = []
        if self.intention is not None:
            for k in self.intention:
                result['Intention'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.intention = []
        if m.get('Intention') is not None:
            for k in m.get('Intention'):
                temp_model = QueryIntentionListResponseBodyDataIntention()
                self.intention.append(temp_model.from_map(k))
        return self


class QueryIntentionListResponseBody(TeaModel):
    def __init__(
        self,
        current_page_num: int = None,
        data: QueryIntentionListResponseBodyData = None,
        page_size: int = None,
        request_id: str = None,
        total_item_num: int = None,
        total_page_num: int = None,
    ):
        self.current_page_num = current_page_num
        self.data = data
        self.page_size = page_size
        self.request_id = request_id
        self.total_item_num = total_item_num
        self.total_page_num = total_page_num

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page_num is not None:
            result['CurrentPageNum'] = self.current_page_num
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_item_num is not None:
            result['TotalItemNum'] = self.total_item_num
        if self.total_page_num is not None:
            result['TotalPageNum'] = self.total_page_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPageNum') is not None:
            self.current_page_num = m.get('CurrentPageNum')
        if m.get('Data') is not None:
            temp_model = QueryIntentionListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalItemNum') is not None:
            self.total_item_num = m.get('TotalItemNum')
        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')
        return self


class QueryIntentionListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryIntentionListResponseBody = None,
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
            temp_model = QueryIntentionListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryIntentionOwnerRequest(TeaModel):
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


class QueryIntentionOwnerResponseBodyModule(TeaModel):
    def __init__(
        self,
        owner_id: float = None,
        owner_name: str = None,
    ):
        self.owner_id = owner_id
        self.owner_name = owner_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.owner_name is not None:
            result['OwnerName'] = self.owner_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('OwnerName') is not None:
            self.owner_name = m.get('OwnerName')
        return self


class QueryIntentionOwnerResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_msg: str = None,
        module: QueryIntentionOwnerResponseBodyModule = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_msg = error_msg
        self.module = module
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.module:
            self.module.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.module is not None:
            result['Module'] = self.module.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('Module') is not None:
            temp_model = QueryIntentionOwnerResponseBodyModule()
            self.module = temp_model.from_map(m['Module'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryIntentionOwnerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryIntentionOwnerResponseBody = None,
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
            temp_model = QueryIntentionOwnerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryIntentionPriceRequest(TeaModel):
    def __init__(
        self,
        channel: str = None,
        intention_biz_id: str = None,
    ):
        self.channel = channel
        self.intention_biz_id = intention_biz_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel is not None:
            result['Channel'] = self.channel
        if self.intention_biz_id is not None:
            result['IntentionBizId'] = self.intention_biz_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Channel') is not None:
            self.channel = m.get('Channel')
        if m.get('IntentionBizId') is not None:
            self.intention_biz_id = m.get('IntentionBizId')
        return self


class QueryIntentionPriceResponseBodyDataTmProducesFirstClassification(TeaModel):
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


class QueryIntentionPriceResponseBodyDataTmProducesThirdClassificationThirdClassifications(TeaModel):
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


class QueryIntentionPriceResponseBodyDataTmProducesThirdClassification(TeaModel):
    def __init__(
        self,
        third_classifications: List[QueryIntentionPriceResponseBodyDataTmProducesThirdClassificationThirdClassifications] = None,
    ):
        self.third_classifications = third_classifications

    def validate(self):
        if self.third_classifications:
            for k in self.third_classifications:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ThirdClassifications'] = []
        if self.third_classifications is not None:
            for k in self.third_classifications:
                result['ThirdClassifications'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.third_classifications = []
        if m.get('ThirdClassifications') is not None:
            for k in m.get('ThirdClassifications'):
                temp_model = QueryIntentionPriceResponseBodyDataTmProducesThirdClassificationThirdClassifications()
                self.third_classifications.append(temp_model.from_map(k))
        return self


class QueryIntentionPriceResponseBodyDataTmProduces(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        create_time: int = None,
        first_classification: QueryIntentionPriceResponseBodyDataTmProducesFirstClassification = None,
        loa_url: str = None,
        material_id: str = None,
        material_name: str = None,
        note: str = None,
        order_price: float = None,
        service_price: float = None,
        status: int = None,
        supplement_id: int = None,
        supplement_status: int = None,
        third_classification: QueryIntentionPriceResponseBodyDataTmProducesThirdClassification = None,
        tm_icon: str = None,
        tm_name: str = None,
        tm_number: str = None,
        total_price: float = None,
        type: int = None,
        update_time: int = None,
    ):
        self.biz_id = biz_id
        self.create_time = create_time
        self.first_classification = first_classification
        self.loa_url = loa_url
        self.material_id = material_id
        self.material_name = material_name
        self.note = note
        self.order_price = order_price
        self.service_price = service_price
        self.status = status
        self.supplement_id = supplement_id
        self.supplement_status = supplement_status
        self.third_classification = third_classification
        self.tm_icon = tm_icon
        self.tm_name = tm_name
        self.tm_number = tm_number
        self.total_price = total_price
        self.type = type
        self.update_time = update_time

    def validate(self):
        if self.first_classification:
            self.first_classification.validate()
        if self.third_classification:
            self.third_classification.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.first_classification is not None:
            result['FirstClassification'] = self.first_classification.to_map()
        if self.loa_url is not None:
            result['LoaUrl'] = self.loa_url
        if self.material_id is not None:
            result['MaterialId'] = self.material_id
        if self.material_name is not None:
            result['MaterialName'] = self.material_name
        if self.note is not None:
            result['Note'] = self.note
        if self.order_price is not None:
            result['OrderPrice'] = self.order_price
        if self.service_price is not None:
            result['ServicePrice'] = self.service_price
        if self.status is not None:
            result['Status'] = self.status
        if self.supplement_id is not None:
            result['SupplementId'] = self.supplement_id
        if self.supplement_status is not None:
            result['SupplementStatus'] = self.supplement_status
        if self.third_classification is not None:
            result['ThirdClassification'] = self.third_classification.to_map()
        if self.tm_icon is not None:
            result['TmIcon'] = self.tm_icon
        if self.tm_name is not None:
            result['TmName'] = self.tm_name
        if self.tm_number is not None:
            result['TmNumber'] = self.tm_number
        if self.total_price is not None:
            result['TotalPrice'] = self.total_price
        if self.type is not None:
            result['Type'] = self.type
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('FirstClassification') is not None:
            temp_model = QueryIntentionPriceResponseBodyDataTmProducesFirstClassification()
            self.first_classification = temp_model.from_map(m['FirstClassification'])
        if m.get('LoaUrl') is not None:
            self.loa_url = m.get('LoaUrl')
        if m.get('MaterialId') is not None:
            self.material_id = m.get('MaterialId')
        if m.get('MaterialName') is not None:
            self.material_name = m.get('MaterialName')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        if m.get('OrderPrice') is not None:
            self.order_price = m.get('OrderPrice')
        if m.get('ServicePrice') is not None:
            self.service_price = m.get('ServicePrice')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SupplementId') is not None:
            self.supplement_id = m.get('SupplementId')
        if m.get('SupplementStatus') is not None:
            self.supplement_status = m.get('SupplementStatus')
        if m.get('ThirdClassification') is not None:
            temp_model = QueryIntentionPriceResponseBodyDataTmProducesThirdClassification()
            self.third_classification = temp_model.from_map(m['ThirdClassification'])
        if m.get('TmIcon') is not None:
            self.tm_icon = m.get('TmIcon')
        if m.get('TmName') is not None:
            self.tm_name = m.get('TmName')
        if m.get('TmNumber') is not None:
            self.tm_number = m.get('TmNumber')
        if m.get('TotalPrice') is not None:
            self.total_price = m.get('TotalPrice')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class QueryIntentionPriceResponseBodyData(TeaModel):
    def __init__(
        self,
        tm_produces: List[QueryIntentionPriceResponseBodyDataTmProduces] = None,
    ):
        self.tm_produces = tm_produces

    def validate(self):
        if self.tm_produces:
            for k in self.tm_produces:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TmProduces'] = []
        if self.tm_produces is not None:
            for k in self.tm_produces:
                result['TmProduces'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tm_produces = []
        if m.get('TmProduces') is not None:
            for k in m.get('TmProduces'):
                temp_model = QueryIntentionPriceResponseBodyDataTmProduces()
                self.tm_produces.append(temp_model.from_map(k))
        return self


class QueryIntentionPriceResponseBody(TeaModel):
    def __init__(
        self,
        current_page_num: int = None,
        data: QueryIntentionPriceResponseBodyData = None,
        page_size: int = None,
        request_id: str = None,
        total_item_num: int = None,
        total_page_num: int = None,
    ):
        self.current_page_num = current_page_num
        self.data = data
        self.page_size = page_size
        self.request_id = request_id
        self.total_item_num = total_item_num
        self.total_page_num = total_page_num

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page_num is not None:
            result['CurrentPageNum'] = self.current_page_num
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_item_num is not None:
            result['TotalItemNum'] = self.total_item_num
        if self.total_page_num is not None:
            result['TotalPageNum'] = self.total_page_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPageNum') is not None:
            self.current_page_num = m.get('CurrentPageNum')
        if m.get('Data') is not None:
            temp_model = QueryIntentionPriceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalItemNum') is not None:
            self.total_item_num = m.get('TotalItemNum')
        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')
        return self


class QueryIntentionPriceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryIntentionPriceResponseBody = None,
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
            temp_model = QueryIntentionPriceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryMaterialRequest(TeaModel):
    def __init__(
        self,
        id: int = None,
        query_unconfirmed_info: bool = None,
    ):
        self.id = id
        self.query_unconfirmed_info = query_unconfirmed_info

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.query_unconfirmed_info is not None:
            result['QueryUnconfirmedInfo'] = self.query_unconfirmed_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('QueryUnconfirmedInfo') is not None:
            self.query_unconfirmed_info = m.get('QueryUnconfirmedInfo')
        return self


class QueryMaterialResponseBodyReviewAdditionalFiles(TeaModel):
    def __init__(
        self,
        review_additional_file: List[str] = None,
    ):
        self.review_additional_file = review_additional_file

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.review_additional_file is not None:
            result['ReviewAdditionalFile'] = self.review_additional_file
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReviewAdditionalFile') is not None:
            self.review_additional_file = m.get('ReviewAdditionalFile')
        return self


class QueryMaterialResponseBody(TeaModel):
    def __init__(
        self,
        address: str = None,
        business_licence_url: str = None,
        card_number: str = None,
        city: str = None,
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
        evidence_catalog_path: str = None,
        evidence_ofservice_path: str = None,
        evidence_path: str = None,
        expiration_date: int = None,
        factandreason_pdf_path: str = None,
        fgsq_path: str = None,
        file_bg_path: str = None,
        file_fs_sq_path: str = None,
        file_gt_path: str = None,
        file_yg_path: str = None,
        id: int = None,
        id_card_name: str = None,
        id_card_number: str = None,
        id_card_url: str = None,
        legal_notice_key: str = None,
        legal_notice_url: str = None,
        loa_status: int = None,
        loa_url: str = None,
        material_version: str = None,
        name: str = None,
        note: str = None,
        passport_url: str = None,
        personal_type: int = None,
        principal_description: str = None,
        principal_name: int = None,
        province: str = None,
        reason: str = None,
        region: int = None,
        request_id: str = None,
        review_additional_files: QueryMaterialResponseBodyReviewAdditionalFiles = None,
        review_application_file: str = None,
        status: int = None,
        supplement_evidence_catalog_file: str = None,
        supplement_evidence_material_file: str = None,
        supplement_reason_file: str = None,
        system_version: str = None,
        town: str = None,
        type: int = None,
        valid_date: int = None,
    ):
        self.address = address
        self.business_licence_url = business_licence_url
        self.card_number = card_number
        self.city = city
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
        self.evidence_catalog_path = evidence_catalog_path
        self.evidence_ofservice_path = evidence_ofservice_path
        self.evidence_path = evidence_path
        self.expiration_date = expiration_date
        self.factandreason_pdf_path = factandreason_pdf_path
        self.fgsq_path = fgsq_path
        self.file_bg_path = file_bg_path
        self.file_fs_sq_path = file_fs_sq_path
        self.file_gt_path = file_gt_path
        self.file_yg_path = file_yg_path
        # id
        self.id = id
        self.id_card_name = id_card_name
        self.id_card_number = id_card_number
        self.id_card_url = id_card_url
        self.legal_notice_key = legal_notice_key
        self.legal_notice_url = legal_notice_url
        self.loa_status = loa_status
        self.loa_url = loa_url
        self.material_version = material_version
        self.name = name
        self.note = note
        self.passport_url = passport_url
        self.personal_type = personal_type
        self.principal_description = principal_description
        self.principal_name = principal_name
        self.province = province
        self.reason = reason
        self.region = region
        self.request_id = request_id
        self.review_additional_files = review_additional_files
        self.review_application_file = review_application_file
        self.status = status
        self.supplement_evidence_catalog_file = supplement_evidence_catalog_file
        self.supplement_evidence_material_file = supplement_evidence_material_file
        self.supplement_reason_file = supplement_reason_file
        self.system_version = system_version
        self.town = town
        self.type = type
        self.valid_date = valid_date

    def validate(self):
        if self.review_additional_files:
            self.review_additional_files.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.business_licence_url is not None:
            result['BusinessLicenceUrl'] = self.business_licence_url
        if self.card_number is not None:
            result['CardNumber'] = self.card_number
        if self.city is not None:
            result['City'] = self.city
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
        if self.evidence_catalog_path is not None:
            result['EvidenceCatalogPath'] = self.evidence_catalog_path
        if self.evidence_ofservice_path is not None:
            result['EvidenceOfservicePath'] = self.evidence_ofservice_path
        if self.evidence_path is not None:
            result['EvidencePath'] = self.evidence_path
        if self.expiration_date is not None:
            result['ExpirationDate'] = self.expiration_date
        if self.factandreason_pdf_path is not None:
            result['FactandreasonPdfPath'] = self.factandreason_pdf_path
        if self.fgsq_path is not None:
            result['FgsqPath'] = self.fgsq_path
        if self.file_bg_path is not None:
            result['FileBgPath'] = self.file_bg_path
        if self.file_fs_sq_path is not None:
            result['FileFsSqPath'] = self.file_fs_sq_path
        if self.file_gt_path is not None:
            result['FileGtPath'] = self.file_gt_path
        if self.file_yg_path is not None:
            result['FileYgPath'] = self.file_yg_path
        if self.id is not None:
            result['Id'] = self.id
        if self.id_card_name is not None:
            result['IdCardName'] = self.id_card_name
        if self.id_card_number is not None:
            result['IdCardNumber'] = self.id_card_number
        if self.id_card_url is not None:
            result['IdCardUrl'] = self.id_card_url
        if self.legal_notice_key is not None:
            result['LegalNoticeKey'] = self.legal_notice_key
        if self.legal_notice_url is not None:
            result['LegalNoticeUrl'] = self.legal_notice_url
        if self.loa_status is not None:
            result['LoaStatus'] = self.loa_status
        if self.loa_url is not None:
            result['LoaUrl'] = self.loa_url
        if self.material_version is not None:
            result['MaterialVersion'] = self.material_version
        if self.name is not None:
            result['Name'] = self.name
        if self.note is not None:
            result['Note'] = self.note
        if self.passport_url is not None:
            result['PassportUrl'] = self.passport_url
        if self.personal_type is not None:
            result['PersonalType'] = self.personal_type
        if self.principal_description is not None:
            result['PrincipalDescription'] = self.principal_description
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name
        if self.province is not None:
            result['Province'] = self.province
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.region is not None:
            result['Region'] = self.region
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.review_additional_files is not None:
            result['ReviewAdditionalFiles'] = self.review_additional_files.to_map()
        if self.review_application_file is not None:
            result['ReviewApplicationFile'] = self.review_application_file
        if self.status is not None:
            result['Status'] = self.status
        if self.supplement_evidence_catalog_file is not None:
            result['SupplementEvidenceCatalogFile'] = self.supplement_evidence_catalog_file
        if self.supplement_evidence_material_file is not None:
            result['SupplementEvidenceMaterialFile'] = self.supplement_evidence_material_file
        if self.supplement_reason_file is not None:
            result['SupplementReasonFile'] = self.supplement_reason_file
        if self.system_version is not None:
            result['SystemVersion'] = self.system_version
        if self.town is not None:
            result['Town'] = self.town
        if self.type is not None:
            result['Type'] = self.type
        if self.valid_date is not None:
            result['ValidDate'] = self.valid_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('BusinessLicenceUrl') is not None:
            self.business_licence_url = m.get('BusinessLicenceUrl')
        if m.get('CardNumber') is not None:
            self.card_number = m.get('CardNumber')
        if m.get('City') is not None:
            self.city = m.get('City')
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
        if m.get('EvidenceCatalogPath') is not None:
            self.evidence_catalog_path = m.get('EvidenceCatalogPath')
        if m.get('EvidenceOfservicePath') is not None:
            self.evidence_ofservice_path = m.get('EvidenceOfservicePath')
        if m.get('EvidencePath') is not None:
            self.evidence_path = m.get('EvidencePath')
        if m.get('ExpirationDate') is not None:
            self.expiration_date = m.get('ExpirationDate')
        if m.get('FactandreasonPdfPath') is not None:
            self.factandreason_pdf_path = m.get('FactandreasonPdfPath')
        if m.get('FgsqPath') is not None:
            self.fgsq_path = m.get('FgsqPath')
        if m.get('FileBgPath') is not None:
            self.file_bg_path = m.get('FileBgPath')
        if m.get('FileFsSqPath') is not None:
            self.file_fs_sq_path = m.get('FileFsSqPath')
        if m.get('FileGtPath') is not None:
            self.file_gt_path = m.get('FileGtPath')
        if m.get('FileYgPath') is not None:
            self.file_yg_path = m.get('FileYgPath')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdCardName') is not None:
            self.id_card_name = m.get('IdCardName')
        if m.get('IdCardNumber') is not None:
            self.id_card_number = m.get('IdCardNumber')
        if m.get('IdCardUrl') is not None:
            self.id_card_url = m.get('IdCardUrl')
        if m.get('LegalNoticeKey') is not None:
            self.legal_notice_key = m.get('LegalNoticeKey')
        if m.get('LegalNoticeUrl') is not None:
            self.legal_notice_url = m.get('LegalNoticeUrl')
        if m.get('LoaStatus') is not None:
            self.loa_status = m.get('LoaStatus')
        if m.get('LoaUrl') is not None:
            self.loa_url = m.get('LoaUrl')
        if m.get('MaterialVersion') is not None:
            self.material_version = m.get('MaterialVersion')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        if m.get('PassportUrl') is not None:
            self.passport_url = m.get('PassportUrl')
        if m.get('PersonalType') is not None:
            self.personal_type = m.get('PersonalType')
        if m.get('PrincipalDescription') is not None:
            self.principal_description = m.get('PrincipalDescription')
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ReviewAdditionalFiles') is not None:
            temp_model = QueryMaterialResponseBodyReviewAdditionalFiles()
            self.review_additional_files = temp_model.from_map(m['ReviewAdditionalFiles'])
        if m.get('ReviewApplicationFile') is not None:
            self.review_application_file = m.get('ReviewApplicationFile')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SupplementEvidenceCatalogFile') is not None:
            self.supplement_evidence_catalog_file = m.get('SupplementEvidenceCatalogFile')
        if m.get('SupplementEvidenceMaterialFile') is not None:
            self.supplement_evidence_material_file = m.get('SupplementEvidenceMaterialFile')
        if m.get('SupplementReasonFile') is not None:
            self.supplement_reason_file = m.get('SupplementReasonFile')
        if m.get('SystemVersion') is not None:
            self.system_version = m.get('SystemVersion')
        if m.get('Town') is not None:
            self.town = m.get('Town')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('ValidDate') is not None:
            self.valid_date = m.get('ValidDate')
        return self


class QueryMaterialResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryMaterialResponseBody = None,
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
            temp_model = QueryMaterialResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryMaterialListRequest(TeaModel):
    def __init__(
        self,
        card_number: str = None,
        material_id: int = None,
        material_version: str = None,
        name: str = None,
        page_num: int = None,
        page_size: int = None,
        principal_name: int = None,
        region: int = None,
        status: int = None,
        system_version: str = None,
        type: int = None,
    ):
        self.card_number = card_number
        self.material_id = material_id
        self.material_version = material_version
        self.name = name
        self.page_num = page_num
        self.page_size = page_size
        self.principal_name = principal_name
        self.region = region
        self.status = status
        self.system_version = system_version
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.card_number is not None:
            result['CardNumber'] = self.card_number
        if self.material_id is not None:
            result['MaterialId'] = self.material_id
        if self.material_version is not None:
            result['MaterialVersion'] = self.material_version
        if self.name is not None:
            result['Name'] = self.name
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name
        if self.region is not None:
            result['Region'] = self.region
        if self.status is not None:
            result['Status'] = self.status
        if self.system_version is not None:
            result['SystemVersion'] = self.system_version
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CardNumber') is not None:
            self.card_number = m.get('CardNumber')
        if m.get('MaterialId') is not None:
            self.material_id = m.get('MaterialId')
        if m.get('MaterialVersion') is not None:
            self.material_version = m.get('MaterialVersion')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SystemVersion') is not None:
            self.system_version = m.get('SystemVersion')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class QueryMaterialListResponseBodyDataTrademark(TeaModel):
    def __init__(
        self,
        card_number: str = None,
        contact_name: str = None,
        id: int = None,
        loa_key: str = None,
        loa_status: int = None,
        material_version: str = None,
        name: str = None,
        principal_description: str = None,
        principal_name: int = None,
        reason: str = None,
        region: int = None,
        status: int = None,
        system_version: str = None,
        type: int = None,
        valid_date: int = None,
    ):
        self.card_number = card_number
        self.contact_name = contact_name
        self.id = id
        self.loa_key = loa_key
        self.loa_status = loa_status
        self.material_version = material_version
        self.name = name
        self.principal_description = principal_description
        self.principal_name = principal_name
        self.reason = reason
        self.region = region
        self.status = status
        self.system_version = system_version
        self.type = type
        self.valid_date = valid_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.card_number is not None:
            result['CardNumber'] = self.card_number
        if self.contact_name is not None:
            result['ContactName'] = self.contact_name
        if self.id is not None:
            result['Id'] = self.id
        if self.loa_key is not None:
            result['LoaKey'] = self.loa_key
        if self.loa_status is not None:
            result['LoaStatus'] = self.loa_status
        if self.material_version is not None:
            result['MaterialVersion'] = self.material_version
        if self.name is not None:
            result['Name'] = self.name
        if self.principal_description is not None:
            result['PrincipalDescription'] = self.principal_description
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.region is not None:
            result['Region'] = self.region
        if self.status is not None:
            result['Status'] = self.status
        if self.system_version is not None:
            result['SystemVersion'] = self.system_version
        if self.type is not None:
            result['Type'] = self.type
        if self.valid_date is not None:
            result['ValidDate'] = self.valid_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CardNumber') is not None:
            self.card_number = m.get('CardNumber')
        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LoaKey') is not None:
            self.loa_key = m.get('LoaKey')
        if m.get('LoaStatus') is not None:
            self.loa_status = m.get('LoaStatus')
        if m.get('MaterialVersion') is not None:
            self.material_version = m.get('MaterialVersion')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PrincipalDescription') is not None:
            self.principal_description = m.get('PrincipalDescription')
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SystemVersion') is not None:
            self.system_version = m.get('SystemVersion')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('ValidDate') is not None:
            self.valid_date = m.get('ValidDate')
        return self


class QueryMaterialListResponseBodyData(TeaModel):
    def __init__(
        self,
        trademark: List[QueryMaterialListResponseBodyDataTrademark] = None,
    ):
        self.trademark = trademark

    def validate(self):
        if self.trademark:
            for k in self.trademark:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Trademark'] = []
        if self.trademark is not None:
            for k in self.trademark:
                result['Trademark'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.trademark = []
        if m.get('Trademark') is not None:
            for k in m.get('Trademark'):
                temp_model = QueryMaterialListResponseBodyDataTrademark()
                self.trademark.append(temp_model.from_map(k))
        return self


class QueryMaterialListResponseBody(TeaModel):
    def __init__(
        self,
        current_page_num: int = None,
        data: QueryMaterialListResponseBodyData = None,
        page_size: int = None,
        request_id: str = None,
        total_item_num: int = None,
        total_page_num: int = None,
    ):
        self.current_page_num = current_page_num
        self.data = data
        self.page_size = page_size
        self.request_id = request_id
        self.total_item_num = total_item_num
        self.total_page_num = total_page_num

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page_num is not None:
            result['CurrentPageNum'] = self.current_page_num
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_item_num is not None:
            result['TotalItemNum'] = self.total_item_num
        if self.total_page_num is not None:
            result['TotalPageNum'] = self.total_page_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPageNum') is not None:
            self.current_page_num = m.get('CurrentPageNum')
        if m.get('Data') is not None:
            temp_model = QueryMaterialListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalItemNum') is not None:
            self.total_item_num = m.get('TotalItemNum')
        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')
        return self


class QueryMaterialListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryMaterialListResponseBody = None,
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
            temp_model = QueryMaterialListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryMonitorKeywordsRequest(TeaModel):
    def __init__(
        self,
        keywords: List[str] = None,
        rule_type: int = None,
    ):
        self.keywords = keywords
        self.rule_type = rule_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keywords is not None:
            result['Keywords'] = self.keywords
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Keywords') is not None:
            self.keywords = m.get('Keywords')
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        return self


class QueryMonitorKeywordsResponseBodyData(TeaModel):
    def __init__(
        self,
        keywords: List[str] = None,
    ):
        self.keywords = keywords

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keywords is not None:
            result['Keywords'] = self.keywords
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Keywords') is not None:
            self.keywords = m.get('Keywords')
        return self


class QueryMonitorKeywordsResponseBody(TeaModel):
    def __init__(
        self,
        data: QueryMonitorKeywordsResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = QueryMonitorKeywordsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryMonitorKeywordsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryMonitorKeywordsResponseBody = None,
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
            temp_model = QueryMonitorKeywordsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryOfficialFileCustomListRequest(TeaModel):
    def __init__(
        self,
        page_num: int = None,
        page_size: int = None,
    ):
        self.page_num = page_num
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class QueryOfficialFileCustomListResponseBodyDataCustomList(TeaModel):
    def __init__(
        self,
        create_time: int = None,
        download_url: str = None,
        end_accept_time: int = None,
        expire_time: int = None,
        remark: str = None,
        start_accept_time: int = None,
        status: str = None,
    ):
        self.create_time = create_time
        self.download_url = download_url
        self.end_accept_time = end_accept_time
        self.expire_time = expire_time
        self.remark = remark
        self.start_accept_time = start_accept_time
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.download_url is not None:
            result['DownloadUrl'] = self.download_url
        if self.end_accept_time is not None:
            result['EndAcceptTime'] = self.end_accept_time
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.start_accept_time is not None:
            result['StartAcceptTime'] = self.start_accept_time
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DownloadUrl') is not None:
            self.download_url = m.get('DownloadUrl')
        if m.get('EndAcceptTime') is not None:
            self.end_accept_time = m.get('EndAcceptTime')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('StartAcceptTime') is not None:
            self.start_accept_time = m.get('StartAcceptTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class QueryOfficialFileCustomListResponseBodyData(TeaModel):
    def __init__(
        self,
        custom_list: List[QueryOfficialFileCustomListResponseBodyDataCustomList] = None,
    ):
        self.custom_list = custom_list

    def validate(self):
        if self.custom_list:
            for k in self.custom_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CustomList'] = []
        if self.custom_list is not None:
            for k in self.custom_list:
                result['CustomList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.custom_list = []
        if m.get('CustomList') is not None:
            for k in m.get('CustomList'):
                temp_model = QueryOfficialFileCustomListResponseBodyDataCustomList()
                self.custom_list.append(temp_model.from_map(k))
        return self


class QueryOfficialFileCustomListResponseBody(TeaModel):
    def __init__(
        self,
        current_page_num: int = None,
        data: QueryOfficialFileCustomListResponseBodyData = None,
        page_size: int = None,
        request_id: str = None,
        total_item_num: int = None,
        total_page_num: int = None,
    ):
        self.current_page_num = current_page_num
        self.data = data
        self.page_size = page_size
        self.request_id = request_id
        self.total_item_num = total_item_num
        self.total_page_num = total_page_num

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page_num is not None:
            result['CurrentPageNum'] = self.current_page_num
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_item_num is not None:
            result['TotalItemNum'] = self.total_item_num
        if self.total_page_num is not None:
            result['TotalPageNum'] = self.total_page_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPageNum') is not None:
            self.current_page_num = m.get('CurrentPageNum')
        if m.get('Data') is not None:
            temp_model = QueryOfficialFileCustomListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalItemNum') is not None:
            self.total_item_num = m.get('TotalItemNum')
        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')
        return self


class QueryOfficialFileCustomListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryOfficialFileCustomListResponseBody = None,
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
            temp_model = QueryOfficialFileCustomListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryOrderLogisticsListRequest(TeaModel):
    def __init__(
        self,
        file_type: str = None,
        page_num: int = None,
        page_size: int = None,
        produce_order_id: str = None,
        register_number: str = None,
    ):
        self.file_type = file_type
        self.page_num = page_num
        self.page_size = page_size
        self.produce_order_id = produce_order_id
        self.register_number = register_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_type is not None:
            result['FileType'] = self.file_type
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.produce_order_id is not None:
            result['ProduceOrderId'] = self.produce_order_id
        if self.register_number is not None:
            result['RegisterNumber'] = self.register_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProduceOrderId') is not None:
            self.produce_order_id = m.get('ProduceOrderId')
        if m.get('RegisterNumber') is not None:
            self.register_number = m.get('RegisterNumber')
        return self


class QueryOrderLogisticsListResponseBodyData(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        file_identifier: str = None,
        file_type: str = None,
        logistics_no: str = None,
        produce_order_id: str = None,
        tm_icon: str = None,
        tm_name: str = None,
        tm_number: str = None,
    ):
        self.biz_id = biz_id
        self.file_identifier = file_identifier
        self.file_type = file_type
        self.logistics_no = logistics_no
        self.produce_order_id = produce_order_id
        self.tm_icon = tm_icon
        self.tm_name = tm_name
        self.tm_number = tm_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.file_identifier is not None:
            result['FileIdentifier'] = self.file_identifier
        if self.file_type is not None:
            result['FileType'] = self.file_type
        if self.logistics_no is not None:
            result['LogisticsNo'] = self.logistics_no
        if self.produce_order_id is not None:
            result['ProduceOrderId'] = self.produce_order_id
        if self.tm_icon is not None:
            result['TmIcon'] = self.tm_icon
        if self.tm_name is not None:
            result['TmName'] = self.tm_name
        if self.tm_number is not None:
            result['TmNumber'] = self.tm_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('FileIdentifier') is not None:
            self.file_identifier = m.get('FileIdentifier')
        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')
        if m.get('LogisticsNo') is not None:
            self.logistics_no = m.get('LogisticsNo')
        if m.get('ProduceOrderId') is not None:
            self.produce_order_id = m.get('ProduceOrderId')
        if m.get('TmIcon') is not None:
            self.tm_icon = m.get('TmIcon')
        if m.get('TmName') is not None:
            self.tm_name = m.get('TmName')
        if m.get('TmNumber') is not None:
            self.tm_number = m.get('TmNumber')
        return self


class QueryOrderLogisticsListResponseBody(TeaModel):
    def __init__(
        self,
        current_page_num: int = None,
        data: List[QueryOrderLogisticsListResponseBodyData] = None,
        page_size: int = None,
        request_id: str = None,
        total_item_num: int = None,
        total_page_num: int = None,
    ):
        self.current_page_num = current_page_num
        self.data = data
        self.page_size = page_size
        self.request_id = request_id
        self.total_item_num = total_item_num
        self.total_page_num = total_page_num

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
        if self.current_page_num is not None:
            result['CurrentPageNum'] = self.current_page_num
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_item_num is not None:
            result['TotalItemNum'] = self.total_item_num
        if self.total_page_num is not None:
            result['TotalPageNum'] = self.total_page_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPageNum') is not None:
            self.current_page_num = m.get('CurrentPageNum')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = QueryOrderLogisticsListResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalItemNum') is not None:
            self.total_item_num = m.get('TotalItemNum')
        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')
        return self


class QueryOrderLogisticsListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryOrderLogisticsListResponseBody = None,
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
            temp_model = QueryOrderLogisticsListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryOssResourcesRequest(TeaModel):
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


class QueryOssResourcesResponseBodyDataTaskList(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        create_time: int = None,
        name: str = None,
        oss_url: str = None,
        update_time: int = None,
    ):
        self.biz_id = biz_id
        self.create_time = create_time
        self.name = name
        self.oss_url = oss_url
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.name is not None:
            result['Name'] = self.name
        if self.oss_url is not None:
            result['OssUrl'] = self.oss_url
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OssUrl') is not None:
            self.oss_url = m.get('OssUrl')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class QueryOssResourcesResponseBodyData(TeaModel):
    def __init__(
        self,
        task_list: List[QueryOssResourcesResponseBodyDataTaskList] = None,
    ):
        self.task_list = task_list

    def validate(self):
        if self.task_list:
            for k in self.task_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TaskList'] = []
        if self.task_list is not None:
            for k in self.task_list:
                result['TaskList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.task_list = []
        if m.get('TaskList') is not None:
            for k in m.get('TaskList'):
                temp_model = QueryOssResourcesResponseBodyDataTaskList()
                self.task_list.append(temp_model.from_map(k))
        return self


class QueryOssResourcesResponseBody(TeaModel):
    def __init__(
        self,
        data: QueryOssResourcesResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = QueryOssResourcesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryOssResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryOssResourcesResponseBody = None,
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
            temp_model = QueryOssResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryProduceDetailRequest(TeaModel):
    def __init__(
        self,
        apply_no: str = None,
        biz_id: str = None,
        order_id: str = None,
    ):
        self.apply_no = apply_no
        self.biz_id = biz_id
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apply_no is not None:
            result['ApplyNo'] = self.apply_no
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplyNo') is not None:
            self.apply_no = m.get('ApplyNo')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class QueryProduceDetailResponseBodyFlags(TeaModel):
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


class QueryProduceDetailResponseBodyLeafCodesLeafCodes(TeaModel):
    def __init__(
        self,
        code: str = None,
        name: str = None,
    ):
        self.code = code
        self.name = name

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class QueryProduceDetailResponseBodyLeafCodes(TeaModel):
    def __init__(
        self,
        leaf_codes: List[QueryProduceDetailResponseBodyLeafCodesLeafCodes] = None,
    ):
        self.leaf_codes = leaf_codes

    def validate(self):
        if self.leaf_codes:
            for k in self.leaf_codes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['LeafCodes'] = []
        if self.leaf_codes is not None:
            for k in self.leaf_codes:
                result['LeafCodes'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.leaf_codes = []
        if m.get('LeafCodes') is not None:
            for k in m.get('LeafCodes'):
                temp_model = QueryProduceDetailResponseBodyLeafCodesLeafCodes()
                self.leaf_codes.append(temp_model.from_map(k))
        return self


class QueryProduceDetailResponseBodyMaterialDetail(TeaModel):
    def __init__(
        self,
        address: str = None,
        business_licence_url: str = None,
        card_number: str = None,
        city: str = None,
        contact_address: str = None,
        contact_email: str = None,
        contact_name: str = None,
        contact_number: str = None,
        contact_zipcode: str = None,
        country: str = None,
        eaddress: str = None,
        ename: str = None,
        expiration_date: str = None,
        id_card_url: str = None,
        loa_url: str = None,
        name: str = None,
        passport_url: str = None,
        province: str = None,
        region: int = None,
        status: int = None,
        town: str = None,
        type: int = None,
    ):
        self.address = address
        self.business_licence_url = business_licence_url
        self.card_number = card_number
        self.city = city
        self.contact_address = contact_address
        self.contact_email = contact_email
        self.contact_name = contact_name
        self.contact_number = contact_number
        self.contact_zipcode = contact_zipcode
        self.country = country
        self.eaddress = eaddress
        self.ename = ename
        self.expiration_date = expiration_date
        self.id_card_url = id_card_url
        self.loa_url = loa_url
        self.name = name
        self.passport_url = passport_url
        self.province = province
        self.region = region
        self.status = status
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
        if self.business_licence_url is not None:
            result['BusinessLicenceUrl'] = self.business_licence_url
        if self.card_number is not None:
            result['CardNumber'] = self.card_number
        if self.city is not None:
            result['City'] = self.city
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
        if self.expiration_date is not None:
            result['ExpirationDate'] = self.expiration_date
        if self.id_card_url is not None:
            result['IdCardUrl'] = self.id_card_url
        if self.loa_url is not None:
            result['LoaUrl'] = self.loa_url
        if self.name is not None:
            result['Name'] = self.name
        if self.passport_url is not None:
            result['PassportUrl'] = self.passport_url
        if self.province is not None:
            result['Province'] = self.province
        if self.region is not None:
            result['Region'] = self.region
        if self.status is not None:
            result['Status'] = self.status
        if self.town is not None:
            result['Town'] = self.town
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('BusinessLicenceUrl') is not None:
            self.business_licence_url = m.get('BusinessLicenceUrl')
        if m.get('CardNumber') is not None:
            self.card_number = m.get('CardNumber')
        if m.get('City') is not None:
            self.city = m.get('City')
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
        if m.get('ExpirationDate') is not None:
            self.expiration_date = m.get('ExpirationDate')
        if m.get('IdCardUrl') is not None:
            self.id_card_url = m.get('IdCardUrl')
        if m.get('LoaUrl') is not None:
            self.loa_url = m.get('LoaUrl')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PassportUrl') is not None:
            self.passport_url = m.get('PassportUrl')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Town') is not None:
            self.town = m.get('Town')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class QueryProduceDetailResponseBodyRootCode(TeaModel):
    def __init__(
        self,
        code: str = None,
        name: str = None,
    ):
        self.code = code
        self.name = name

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class QueryProduceDetailResponseBody(TeaModel):
    def __init__(
        self,
        accept_url: str = None,
        agreement_id: str = None,
        biz_id: str = None,
        cn_info_url: str = None,
        extend_info: Dict[str, Any] = None,
        flags: QueryProduceDetailResponseBodyFlags = None,
        gray_icon_url: str = None,
        issue_date: str = None,
        leaf_codes: QueryProduceDetailResponseBodyLeafCodes = None,
        loa_url: str = None,
        material_detail: QueryProduceDetailResponseBodyMaterialDetail = None,
        note: str = None,
        order_id: str = None,
        principal_name: int = None,
        request_id: str = None,
        root_code: QueryProduceDetailResponseBodyRootCode = None,
        status: int = None,
        submit_count: int = None,
        tm_icon: str = None,
        tm_name: str = None,
        tm_name_type: int = None,
        tm_number: str = None,
        tm_order_id: str = None,
        type: int = None,
    ):
        self.accept_url = accept_url
        self.agreement_id = agreement_id
        self.biz_id = biz_id
        self.cn_info_url = cn_info_url
        self.extend_info = extend_info
        self.flags = flags
        self.gray_icon_url = gray_icon_url
        self.issue_date = issue_date
        self.leaf_codes = leaf_codes
        self.loa_url = loa_url
        self.material_detail = material_detail
        self.note = note
        self.order_id = order_id
        self.principal_name = principal_name
        self.request_id = request_id
        self.root_code = root_code
        self.status = status
        self.submit_count = submit_count
        self.tm_icon = tm_icon
        self.tm_name = tm_name
        self.tm_name_type = tm_name_type
        self.tm_number = tm_number
        self.tm_order_id = tm_order_id
        self.type = type

    def validate(self):
        if self.flags:
            self.flags.validate()
        if self.leaf_codes:
            self.leaf_codes.validate()
        if self.material_detail:
            self.material_detail.validate()
        if self.root_code:
            self.root_code.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_url is not None:
            result['AcceptUrl'] = self.accept_url
        if self.agreement_id is not None:
            result['AgreementId'] = self.agreement_id
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.cn_info_url is not None:
            result['CnInfoUrl'] = self.cn_info_url
        if self.extend_info is not None:
            result['ExtendInfo'] = self.extend_info
        if self.flags is not None:
            result['Flags'] = self.flags.to_map()
        if self.gray_icon_url is not None:
            result['GrayIconUrl'] = self.gray_icon_url
        if self.issue_date is not None:
            result['IssueDate'] = self.issue_date
        if self.leaf_codes is not None:
            result['LeafCodes'] = self.leaf_codes.to_map()
        if self.loa_url is not None:
            result['LoaUrl'] = self.loa_url
        if self.material_detail is not None:
            result['MaterialDetail'] = self.material_detail.to_map()
        if self.note is not None:
            result['Note'] = self.note
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.root_code is not None:
            result['RootCode'] = self.root_code.to_map()
        if self.status is not None:
            result['Status'] = self.status
        if self.submit_count is not None:
            result['SubmitCount'] = self.submit_count
        if self.tm_icon is not None:
            result['TmIcon'] = self.tm_icon
        if self.tm_name is not None:
            result['TmName'] = self.tm_name
        if self.tm_name_type is not None:
            result['TmNameType'] = self.tm_name_type
        if self.tm_number is not None:
            result['TmNumber'] = self.tm_number
        if self.tm_order_id is not None:
            result['TmOrderId'] = self.tm_order_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptUrl') is not None:
            self.accept_url = m.get('AcceptUrl')
        if m.get('AgreementId') is not None:
            self.agreement_id = m.get('AgreementId')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('CnInfoUrl') is not None:
            self.cn_info_url = m.get('CnInfoUrl')
        if m.get('ExtendInfo') is not None:
            self.extend_info = m.get('ExtendInfo')
        if m.get('Flags') is not None:
            temp_model = QueryProduceDetailResponseBodyFlags()
            self.flags = temp_model.from_map(m['Flags'])
        if m.get('GrayIconUrl') is not None:
            self.gray_icon_url = m.get('GrayIconUrl')
        if m.get('IssueDate') is not None:
            self.issue_date = m.get('IssueDate')
        if m.get('LeafCodes') is not None:
            temp_model = QueryProduceDetailResponseBodyLeafCodes()
            self.leaf_codes = temp_model.from_map(m['LeafCodes'])
        if m.get('LoaUrl') is not None:
            self.loa_url = m.get('LoaUrl')
        if m.get('MaterialDetail') is not None:
            temp_model = QueryProduceDetailResponseBodyMaterialDetail()
            self.material_detail = temp_model.from_map(m['MaterialDetail'])
        if m.get('Note') is not None:
            self.note = m.get('Note')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RootCode') is not None:
            temp_model = QueryProduceDetailResponseBodyRootCode()
            self.root_code = temp_model.from_map(m['RootCode'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubmitCount') is not None:
            self.submit_count = m.get('SubmitCount')
        if m.get('TmIcon') is not None:
            self.tm_icon = m.get('TmIcon')
        if m.get('TmName') is not None:
            self.tm_name = m.get('TmName')
        if m.get('TmNameType') is not None:
            self.tm_name_type = m.get('TmNameType')
        if m.get('TmNumber') is not None:
            self.tm_number = m.get('TmNumber')
        if m.get('TmOrderId') is not None:
            self.tm_order_id = m.get('TmOrderId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class QueryProduceDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryProduceDetailResponseBody = None,
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
            temp_model = QueryProduceDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryProduceListRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        create_time_left: int = None,
        create_time_right: int = None,
        material_name: str = None,
        order_id: str = None,
        page_num: int = None,
        page_size: int = None,
        status: int = None,
        tm_name: str = None,
        tm_number: str = None,
        type: int = None,
        user_id: str = None,
    ):
        self.biz_id = biz_id
        self.create_time_left = create_time_left
        self.create_time_right = create_time_right
        self.material_name = material_name
        self.order_id = order_id
        self.page_num = page_num
        self.page_size = page_size
        self.status = status
        self.tm_name = tm_name
        self.tm_number = tm_number
        self.type = type
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.create_time_left is not None:
            result['CreateTimeLeft'] = self.create_time_left
        if self.create_time_right is not None:
            result['CreateTimeRight'] = self.create_time_right
        if self.material_name is not None:
            result['MaterialName'] = self.material_name
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.status is not None:
            result['Status'] = self.status
        if self.tm_name is not None:
            result['TmName'] = self.tm_name
        if self.tm_number is not None:
            result['TmNumber'] = self.tm_number
        if self.type is not None:
            result['Type'] = self.type
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('CreateTimeLeft') is not None:
            self.create_time_left = m.get('CreateTimeLeft')
        if m.get('CreateTimeRight') is not None:
            self.create_time_right = m.get('CreateTimeRight')
        if m.get('MaterialName') is not None:
            self.material_name = m.get('MaterialName')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TmName') is not None:
            self.tm_name = m.get('TmName')
        if m.get('TmNumber') is not None:
            self.tm_number = m.get('TmNumber')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class QueryProduceListResponseBodyDataTmProducesClassification(TeaModel):
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


class QueryProduceListResponseBodyDataTmProduces(TeaModel):
    def __init__(
        self,
        agreement_id: str = None,
        biz_id: str = None,
        classification: QueryProduceListResponseBodyDataTmProducesClassification = None,
        create_time: int = None,
        loa_url: str = None,
        material_name: str = None,
        note: str = None,
        order_id: str = None,
        order_price: float = None,
        principal_name: int = None,
        receipt_url: str = None,
        status: int = None,
        submit_count: int = None,
        tm_icon: str = None,
        tm_name: str = None,
        tm_number: str = None,
        type: int = None,
        update_time: int = None,
        user_id: str = None,
    ):
        self.agreement_id = agreement_id
        self.biz_id = biz_id
        self.classification = classification
        self.create_time = create_time
        self.loa_url = loa_url
        self.material_name = material_name
        self.note = note
        self.order_id = order_id
        self.order_price = order_price
        self.principal_name = principal_name
        self.receipt_url = receipt_url
        self.status = status
        self.submit_count = submit_count
        self.tm_icon = tm_icon
        self.tm_name = tm_name
        self.tm_number = tm_number
        self.type = type
        self.update_time = update_time
        self.user_id = user_id

    def validate(self):
        if self.classification:
            self.classification.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agreement_id is not None:
            result['AgreementId'] = self.agreement_id
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.classification is not None:
            result['Classification'] = self.classification.to_map()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.loa_url is not None:
            result['LoaUrl'] = self.loa_url
        if self.material_name is not None:
            result['MaterialName'] = self.material_name
        if self.note is not None:
            result['Note'] = self.note
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.order_price is not None:
            result['OrderPrice'] = self.order_price
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name
        if self.receipt_url is not None:
            result['ReceiptUrl'] = self.receipt_url
        if self.status is not None:
            result['Status'] = self.status
        if self.submit_count is not None:
            result['SubmitCount'] = self.submit_count
        if self.tm_icon is not None:
            result['TmIcon'] = self.tm_icon
        if self.tm_name is not None:
            result['TmName'] = self.tm_name
        if self.tm_number is not None:
            result['TmNumber'] = self.tm_number
        if self.type is not None:
            result['Type'] = self.type
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgreementId') is not None:
            self.agreement_id = m.get('AgreementId')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Classification') is not None:
            temp_model = QueryProduceListResponseBodyDataTmProducesClassification()
            self.classification = temp_model.from_map(m['Classification'])
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('LoaUrl') is not None:
            self.loa_url = m.get('LoaUrl')
        if m.get('MaterialName') is not None:
            self.material_name = m.get('MaterialName')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('OrderPrice') is not None:
            self.order_price = m.get('OrderPrice')
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')
        if m.get('ReceiptUrl') is not None:
            self.receipt_url = m.get('ReceiptUrl')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubmitCount') is not None:
            self.submit_count = m.get('SubmitCount')
        if m.get('TmIcon') is not None:
            self.tm_icon = m.get('TmIcon')
        if m.get('TmName') is not None:
            self.tm_name = m.get('TmName')
        if m.get('TmNumber') is not None:
            self.tm_number = m.get('TmNumber')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class QueryProduceListResponseBodyData(TeaModel):
    def __init__(
        self,
        tm_produces: List[QueryProduceListResponseBodyDataTmProduces] = None,
    ):
        self.tm_produces = tm_produces

    def validate(self):
        if self.tm_produces:
            for k in self.tm_produces:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TmProduces'] = []
        if self.tm_produces is not None:
            for k in self.tm_produces:
                result['TmProduces'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tm_produces = []
        if m.get('TmProduces') is not None:
            for k in m.get('TmProduces'):
                temp_model = QueryProduceListResponseBodyDataTmProduces()
                self.tm_produces.append(temp_model.from_map(k))
        return self


class QueryProduceListResponseBody(TeaModel):
    def __init__(
        self,
        current_page_num: int = None,
        data: QueryProduceListResponseBodyData = None,
        next_page: bool = None,
        page_size: int = None,
        pre_page: bool = None,
        request_id: str = None,
        total_item_num: int = None,
        total_page_num: int = None,
    ):
        self.current_page_num = current_page_num
        self.data = data
        self.next_page = next_page
        self.page_size = page_size
        self.pre_page = pre_page
        self.request_id = request_id
        self.total_item_num = total_item_num
        self.total_page_num = total_page_num

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page_num is not None:
            result['CurrentPageNum'] = self.current_page_num
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.next_page is not None:
            result['NextPage'] = self.next_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.pre_page is not None:
            result['PrePage'] = self.pre_page
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_item_num is not None:
            result['TotalItemNum'] = self.total_item_num
        if self.total_page_num is not None:
            result['TotalPageNum'] = self.total_page_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPageNum') is not None:
            self.current_page_num = m.get('CurrentPageNum')
        if m.get('Data') is not None:
            temp_model = QueryProduceListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('NextPage') is not None:
            self.next_page = m.get('NextPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PrePage') is not None:
            self.pre_page = m.get('PrePage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalItemNum') is not None:
            self.total_item_num = m.get('TotalItemNum')
        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')
        return self


class QueryProduceListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryProduceListResponseBody = None,
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
            temp_model = QueryProduceListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryQrCodeUploadStatusRequest(TeaModel):
    def __init__(
        self,
        field_key: str = None,
        oss_key: str = None,
        uuid: str = None,
    ):
        self.field_key = field_key
        self.oss_key = oss_key
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field_key is not None:
            result['FieldKey'] = self.field_key
        if self.oss_key is not None:
            result['OssKey'] = self.oss_key
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FieldKey') is not None:
            self.field_key = m.get('FieldKey')
        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class QueryQrCodeUploadStatusResponseBody(TeaModel):
    def __init__(
        self,
        oss_key: str = None,
        oss_url: str = None,
        request_id: str = None,
        status: int = None,
        success: bool = None,
    ):
        self.oss_key = oss_key
        self.oss_url = oss_url
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
        if self.oss_key is not None:
            result['OssKey'] = self.oss_key
        if self.oss_url is not None:
            result['OssUrl'] = self.oss_url
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')
        if m.get('OssUrl') is not None:
            self.oss_url = m.get('OssUrl')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryQrCodeUploadStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryQrCodeUploadStatusResponseBody = None,
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
            temp_model = QueryQrCodeUploadStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QuerySbjRuleRequest(TeaModel):
    def __init__(
        self,
        biz_type: str = None,
        rule_id: str = None,
    ):
        self.biz_type = biz_type
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class QuerySbjRuleResponseBodySbjRuleListSbjRuleItemFrontendOptionsFrontendOption(TeaModel):
    def __init__(
        self,
        title: str = None,
        value: str = None,
    ):
        self.title = title
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.title is not None:
            result['title'] = self.title
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('title') is not None:
            self.title = m.get('title')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class QuerySbjRuleResponseBodySbjRuleListSbjRuleItemFrontendOptions(TeaModel):
    def __init__(
        self,
        frontend_option: List[QuerySbjRuleResponseBodySbjRuleListSbjRuleItemFrontendOptionsFrontendOption] = None,
    ):
        self.frontend_option = frontend_option

    def validate(self):
        if self.frontend_option:
            for k in self.frontend_option:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FrontendOption'] = []
        if self.frontend_option is not None:
            for k in self.frontend_option:
                result['FrontendOption'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.frontend_option = []
        if m.get('FrontendOption') is not None:
            for k in m.get('FrontendOption'):
                temp_model = QuerySbjRuleResponseBodySbjRuleListSbjRuleItemFrontendOptionsFrontendOption()
                self.frontend_option.append(temp_model.from_map(k))
        return self


class QuerySbjRuleResponseBodySbjRuleListSbjRuleItem(TeaModel):
    def __init__(
        self,
        default_value: str = None,
        esp_ext_field_name: str = None,
        field_name: str = None,
        file_type: str = None,
        frontend_options: QuerySbjRuleResponseBodySbjRuleListSbjRuleItemFrontendOptions = None,
        frontend_type: str = None,
        required_expression: str = None,
        sbj_field_id: str = None,
        show_expression: str = None,
        trademark_service_expression: str = None,
        validate_regular_expression: str = None,
    ):
        self.default_value = default_value
        self.esp_ext_field_name = esp_ext_field_name
        self.field_name = field_name
        self.file_type = file_type
        self.frontend_options = frontend_options
        self.frontend_type = frontend_type
        self.required_expression = required_expression
        self.sbj_field_id = sbj_field_id
        self.show_expression = show_expression
        self.trademark_service_expression = trademark_service_expression
        self.validate_regular_expression = validate_regular_expression

    def validate(self):
        if self.frontend_options:
            self.frontend_options.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.default_value is not None:
            result['DefaultValue'] = self.default_value
        if self.esp_ext_field_name is not None:
            result['EspExtFieldName'] = self.esp_ext_field_name
        if self.field_name is not None:
            result['FieldName'] = self.field_name
        if self.file_type is not None:
            result['FileType'] = self.file_type
        if self.frontend_options is not None:
            result['FrontendOptions'] = self.frontend_options.to_map()
        if self.frontend_type is not None:
            result['FrontendType'] = self.frontend_type
        if self.required_expression is not None:
            result['RequiredExpression'] = self.required_expression
        if self.sbj_field_id is not None:
            result['SbjFieldId'] = self.sbj_field_id
        if self.show_expression is not None:
            result['ShowExpression'] = self.show_expression
        if self.trademark_service_expression is not None:
            result['TrademarkServiceExpression'] = self.trademark_service_expression
        if self.validate_regular_expression is not None:
            result['ValidateRegularExpression'] = self.validate_regular_expression
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')
        if m.get('EspExtFieldName') is not None:
            self.esp_ext_field_name = m.get('EspExtFieldName')
        if m.get('FieldName') is not None:
            self.field_name = m.get('FieldName')
        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')
        if m.get('FrontendOptions') is not None:
            temp_model = QuerySbjRuleResponseBodySbjRuleListSbjRuleItemFrontendOptions()
            self.frontend_options = temp_model.from_map(m['FrontendOptions'])
        if m.get('FrontendType') is not None:
            self.frontend_type = m.get('FrontendType')
        if m.get('RequiredExpression') is not None:
            self.required_expression = m.get('RequiredExpression')
        if m.get('SbjFieldId') is not None:
            self.sbj_field_id = m.get('SbjFieldId')
        if m.get('ShowExpression') is not None:
            self.show_expression = m.get('ShowExpression')
        if m.get('TrademarkServiceExpression') is not None:
            self.trademark_service_expression = m.get('TrademarkServiceExpression')
        if m.get('ValidateRegularExpression') is not None:
            self.validate_regular_expression = m.get('ValidateRegularExpression')
        return self


class QuerySbjRuleResponseBodySbjRuleList(TeaModel):
    def __init__(
        self,
        sbj_rule_item: List[QuerySbjRuleResponseBodySbjRuleListSbjRuleItem] = None,
    ):
        self.sbj_rule_item = sbj_rule_item

    def validate(self):
        if self.sbj_rule_item:
            for k in self.sbj_rule_item:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SbjRuleItem'] = []
        if self.sbj_rule_item is not None:
            for k in self.sbj_rule_item:
                result['SbjRuleItem'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.sbj_rule_item = []
        if m.get('SbjRuleItem') is not None:
            for k in m.get('SbjRuleItem'):
                temp_model = QuerySbjRuleResponseBodySbjRuleListSbjRuleItem()
                self.sbj_rule_item.append(temp_model.from_map(k))
        return self


class QuerySbjRuleResponseBody(TeaModel):
    def __init__(
        self,
        biz_type: str = None,
        request_id: str = None,
        rule_id: str = None,
        sbj_rule_list: QuerySbjRuleResponseBodySbjRuleList = None,
    ):
        self.biz_type = biz_type
        self.request_id = request_id
        self.rule_id = rule_id
        self.sbj_rule_list = sbj_rule_list

    def validate(self):
        if self.sbj_rule_list:
            self.sbj_rule_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.sbj_rule_list is not None:
            result['SbjRuleList'] = self.sbj_rule_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('SbjRuleList') is not None:
            temp_model = QuerySbjRuleResponseBodySbjRuleList()
            self.sbj_rule_list = temp_model.from_map(m['SbjRuleList'])
        return self


class QuerySbjRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QuerySbjRuleResponseBody = None,
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
            temp_model = QuerySbjRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QuerySupplementDetailRequest(TeaModel):
    def __init__(
        self,
        id: int = None,
    ):
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


class QuerySupplementDetailResponseBodyFileTemplateUrls(TeaModel):
    def __init__(
        self,
        file_template_urls: List[str] = None,
    ):
        self.file_template_urls = file_template_urls

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_template_urls is not None:
            result['FileTemplateUrls'] = self.file_template_urls
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileTemplateUrls') is not None:
            self.file_template_urls = m.get('FileTemplateUrls')
        return self


class QuerySupplementDetailResponseBody(TeaModel):
    def __init__(
        self,
        accept_dead_time: int = None,
        accept_time: int = None,
        content: str = None,
        file_name: str = None,
        file_template_urls: QuerySupplementDetailResponseBodyFileTemplateUrls = None,
        id: int = None,
        operate_time: int = None,
        reason: str = None,
        request_id: str = None,
        sbj_dead_time: int = None,
        send_time: int = None,
        serial_number: str = None,
        status: int = None,
        tm_number: str = None,
        type: int = None,
        upload_file_template_url: str = None,
    ):
        self.accept_dead_time = accept_dead_time
        self.accept_time = accept_time
        self.content = content
        self.file_name = file_name
        self.file_template_urls = file_template_urls
        self.id = id
        self.operate_time = operate_time
        self.reason = reason
        self.request_id = request_id
        self.sbj_dead_time = sbj_dead_time
        self.send_time = send_time
        self.serial_number = serial_number
        self.status = status
        self.tm_number = tm_number
        self.type = type
        self.upload_file_template_url = upload_file_template_url

    def validate(self):
        if self.file_template_urls:
            self.file_template_urls.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_dead_time is not None:
            result['AcceptDeadTime'] = self.accept_dead_time
        if self.accept_time is not None:
            result['AcceptTime'] = self.accept_time
        if self.content is not None:
            result['Content'] = self.content
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_template_urls is not None:
            result['FileTemplateUrls'] = self.file_template_urls.to_map()
        if self.id is not None:
            result['Id'] = self.id
        if self.operate_time is not None:
            result['OperateTime'] = self.operate_time
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sbj_dead_time is not None:
            result['SbjDeadTime'] = self.sbj_dead_time
        if self.send_time is not None:
            result['SendTime'] = self.send_time
        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number
        if self.status is not None:
            result['Status'] = self.status
        if self.tm_number is not None:
            result['TmNumber'] = self.tm_number
        if self.type is not None:
            result['Type'] = self.type
        if self.upload_file_template_url is not None:
            result['UploadFileTemplateUrl'] = self.upload_file_template_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptDeadTime') is not None:
            self.accept_dead_time = m.get('AcceptDeadTime')
        if m.get('AcceptTime') is not None:
            self.accept_time = m.get('AcceptTime')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileTemplateUrls') is not None:
            temp_model = QuerySupplementDetailResponseBodyFileTemplateUrls()
            self.file_template_urls = temp_model.from_map(m['FileTemplateUrls'])
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OperateTime') is not None:
            self.operate_time = m.get('OperateTime')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SbjDeadTime') is not None:
            self.sbj_dead_time = m.get('SbjDeadTime')
        if m.get('SendTime') is not None:
            self.send_time = m.get('SendTime')
        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TmNumber') is not None:
            self.tm_number = m.get('TmNumber')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UploadFileTemplateUrl') is not None:
            self.upload_file_template_url = m.get('UploadFileTemplateUrl')
        return self


class QuerySupplementDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QuerySupplementDetailResponseBody = None,
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
            temp_model = QuerySupplementDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTaskListRequest(TeaModel):
    def __init__(
        self,
        biz_type: str = None,
        page_num: int = None,
        page_size: int = None,
    ):
        self.biz_type = biz_type
        self.page_num = page_num
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class QueryTaskListResponseBodyDataTaskList(TeaModel):
    def __init__(
        self,
        complete_time: int = None,
        create_time: int = None,
        err_msg: str = None,
        file_name: str = None,
        result: str = None,
        task_status: str = None,
        task_type: str = None,
    ):
        self.complete_time = complete_time
        self.create_time = create_time
        self.err_msg = err_msg
        self.file_name = file_name
        self.result = result
        self.task_status = task_status
        self.task_type = task_type

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
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.result is not None:
            result['Result'] = self.result
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompleteTime') is not None:
            self.complete_time = m.get('CompleteTime')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        return self


class QueryTaskListResponseBodyData(TeaModel):
    def __init__(
        self,
        task_list: List[QueryTaskListResponseBodyDataTaskList] = None,
    ):
        self.task_list = task_list

    def validate(self):
        if self.task_list:
            for k in self.task_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TaskList'] = []
        if self.task_list is not None:
            for k in self.task_list:
                result['TaskList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.task_list = []
        if m.get('TaskList') is not None:
            for k in m.get('TaskList'):
                temp_model = QueryTaskListResponseBodyDataTaskList()
                self.task_list.append(temp_model.from_map(k))
        return self


class QueryTaskListResponseBody(TeaModel):
    def __init__(
        self,
        current_page_num: int = None,
        data: QueryTaskListResponseBodyData = None,
        page_size: int = None,
        request_id: str = None,
        total_item_num: int = None,
        total_page_num: int = None,
    ):
        self.current_page_num = current_page_num
        self.data = data
        self.page_size = page_size
        self.request_id = request_id
        self.total_item_num = total_item_num
        self.total_page_num = total_page_num

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page_num is not None:
            result['CurrentPageNum'] = self.current_page_num
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_item_num is not None:
            result['TotalItemNum'] = self.total_item_num
        if self.total_page_num is not None:
            result['TotalPageNum'] = self.total_page_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPageNum') is not None:
            self.current_page_num = m.get('CurrentPageNum')
        if m.get('Data') is not None:
            temp_model = QueryTaskListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalItemNum') is not None:
            self.total_item_num = m.get('TotalItemNum')
        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')
        return self


class QueryTaskListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryTaskListResponseBody = None,
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
            temp_model = QueryTaskListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTmCollectionPageListRequest(TeaModel):
    def __init__(
        self,
        page_num: int = None,
        page_size: int = None,
    ):
        self.page_num = page_num
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class QueryTmCollectionPageListResponseBodyDataTrademark(TeaModel):
    def __init__(
        self,
        classification: str = None,
        collected: bool = None,
        collection_content: str = None,
        id: int = None,
        item_id: str = None,
        tm_name: str = None,
    ):
        self.classification = classification
        self.collected = collected
        self.collection_content = collection_content
        self.id = id
        self.item_id = item_id
        self.tm_name = tm_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.classification is not None:
            result['Classification'] = self.classification
        if self.collected is not None:
            result['Collected'] = self.collected
        if self.collection_content is not None:
            result['CollectionContent'] = self.collection_content
        if self.id is not None:
            result['Id'] = self.id
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.tm_name is not None:
            result['TmName'] = self.tm_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Classification') is not None:
            self.classification = m.get('Classification')
        if m.get('Collected') is not None:
            self.collected = m.get('Collected')
        if m.get('CollectionContent') is not None:
            self.collection_content = m.get('CollectionContent')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('TmName') is not None:
            self.tm_name = m.get('TmName')
        return self


class QueryTmCollectionPageListResponseBodyData(TeaModel):
    def __init__(
        self,
        trademark: List[QueryTmCollectionPageListResponseBodyDataTrademark] = None,
    ):
        self.trademark = trademark

    def validate(self):
        if self.trademark:
            for k in self.trademark:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Trademark'] = []
        if self.trademark is not None:
            for k in self.trademark:
                result['Trademark'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.trademark = []
        if m.get('Trademark') is not None:
            for k in m.get('Trademark'):
                temp_model = QueryTmCollectionPageListResponseBodyDataTrademark()
                self.trademark.append(temp_model.from_map(k))
        return self


class QueryTmCollectionPageListResponseBody(TeaModel):
    def __init__(
        self,
        current_page_num: int = None,
        data: QueryTmCollectionPageListResponseBodyData = None,
        page_size: int = None,
        request_id: str = None,
        total_item_num: int = None,
        total_page_num: int = None,
    ):
        self.current_page_num = current_page_num
        self.data = data
        self.page_size = page_size
        self.request_id = request_id
        self.total_item_num = total_item_num
        self.total_page_num = total_page_num

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page_num is not None:
            result['CurrentPageNum'] = self.current_page_num
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_item_num is not None:
            result['TotalItemNum'] = self.total_item_num
        if self.total_page_num is not None:
            result['TotalPageNum'] = self.total_page_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPageNum') is not None:
            self.current_page_num = m.get('CurrentPageNum')
        if m.get('Data') is not None:
            temp_model = QueryTmCollectionPageListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalItemNum') is not None:
            self.total_item_num = m.get('TotalItemNum')
        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')
        return self


class QueryTmCollectionPageListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryTmCollectionPageListResponseBody = None,
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
            temp_model = QueryTmCollectionPageListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTmSbjProduceRequest(TeaModel):
    def __init__(
        self,
        high_priority_biz_type_str: str = None,
        high_priority_material_name_str: str = None,
        high_priority_order_id_str: str = None,
        high_priority_user_id_str: str = None,
        principal_key: str = None,
        principal_name: str = None,
        producer_type: str = None,
        query_order_page_size: int = None,
    ):
        self.high_priority_biz_type_str = high_priority_biz_type_str
        self.high_priority_material_name_str = high_priority_material_name_str
        self.high_priority_order_id_str = high_priority_order_id_str
        self.high_priority_user_id_str = high_priority_user_id_str
        self.principal_key = principal_key
        self.principal_name = principal_name
        self.producer_type = producer_type
        self.query_order_page_size = query_order_page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.high_priority_biz_type_str is not None:
            result['HighPriorityBizTypeStr'] = self.high_priority_biz_type_str
        if self.high_priority_material_name_str is not None:
            result['HighPriorityMaterialNameStr'] = self.high_priority_material_name_str
        if self.high_priority_order_id_str is not None:
            result['HighPriorityOrderIdStr'] = self.high_priority_order_id_str
        if self.high_priority_user_id_str is not None:
            result['HighPriorityUserIdStr'] = self.high_priority_user_id_str
        if self.principal_key is not None:
            result['PrincipalKey'] = self.principal_key
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name
        if self.producer_type is not None:
            result['ProducerType'] = self.producer_type
        if self.query_order_page_size is not None:
            result['QueryOrderPageSize'] = self.query_order_page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HighPriorityBizTypeStr') is not None:
            self.high_priority_biz_type_str = m.get('HighPriorityBizTypeStr')
        if m.get('HighPriorityMaterialNameStr') is not None:
            self.high_priority_material_name_str = m.get('HighPriorityMaterialNameStr')
        if m.get('HighPriorityOrderIdStr') is not None:
            self.high_priority_order_id_str = m.get('HighPriorityOrderIdStr')
        if m.get('HighPriorityUserIdStr') is not None:
            self.high_priority_user_id_str = m.get('HighPriorityUserIdStr')
        if m.get('PrincipalKey') is not None:
            self.principal_key = m.get('PrincipalKey')
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')
        if m.get('ProducerType') is not None:
            self.producer_type = m.get('ProducerType')
        if m.get('QueryOrderPageSize') is not None:
            self.query_order_page_size = m.get('QueryOrderPageSize')
        return self


class QueryTmSbjProduceResponseBodyMoudleTmSbjProduceListExtend(TeaModel):
    def __init__(
        self,
        bid: int = None,
        black_icon: bool = None,
        loa_oss_key: str = None,
        logo_goods_id: str = None,
        material_id: str = None,
        submit_count: int = None,
        tm_nametype: int = None,
    ):
        self.bid = bid
        self.black_icon = black_icon
        self.loa_oss_key = loa_oss_key
        self.logo_goods_id = logo_goods_id
        self.material_id = material_id
        self.submit_count = submit_count
        self.tm_nametype = tm_nametype

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bid is not None:
            result['Bid'] = self.bid
        if self.black_icon is not None:
            result['BlackIcon'] = self.black_icon
        if self.loa_oss_key is not None:
            result['LoaOssKey'] = self.loa_oss_key
        if self.logo_goods_id is not None:
            result['LogoGoodsId'] = self.logo_goods_id
        if self.material_id is not None:
            result['MaterialId'] = self.material_id
        if self.submit_count is not None:
            result['SubmitCount'] = self.submit_count
        if self.tm_nametype is not None:
            result['TmNametype'] = self.tm_nametype
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bid') is not None:
            self.bid = m.get('Bid')
        if m.get('BlackIcon') is not None:
            self.black_icon = m.get('BlackIcon')
        if m.get('LoaOssKey') is not None:
            self.loa_oss_key = m.get('LoaOssKey')
        if m.get('LogoGoodsId') is not None:
            self.logo_goods_id = m.get('LogoGoodsId')
        if m.get('MaterialId') is not None:
            self.material_id = m.get('MaterialId')
        if m.get('SubmitCount') is not None:
            self.submit_count = m.get('SubmitCount')
        if m.get('TmNametype') is not None:
            self.tm_nametype = m.get('TmNametype')
        return self


class QueryTmSbjProduceResponseBodyMoudleTmSbjProduceList(TeaModel):
    def __init__(
        self,
        bit_flag: int = None,
        biz_id: str = None,
        classification_code: str = None,
        delete_flag: str = None,
        env: str = None,
        extend: QueryTmSbjProduceResponseBodyMoudleTmSbjProduceListExtend = None,
        loa_id: int = None,
        main_order_id: str = None,
        material_id: int = None,
        material_name: str = None,
        order_id: str = None,
        order_price: float = None,
        principal_key: str = None,
        principal_name: str = None,
        product_type: str = None,
        risk_source: str = None,
        status: str = None,
        submit_audit_time: int = None,
        submit_status: str = None,
        submit_time: int = None,
        submit_times: int = None,
        tm_code: str = None,
        tm_icon: str = None,
        tm_name: str = None,
        type: str = None,
        user_id: str = None,
    ):
        self.bit_flag = bit_flag
        self.biz_id = biz_id
        self.classification_code = classification_code
        self.delete_flag = delete_flag
        self.env = env
        self.extend = extend
        self.loa_id = loa_id
        self.main_order_id = main_order_id
        self.material_id = material_id
        self.material_name = material_name
        self.order_id = order_id
        self.order_price = order_price
        self.principal_key = principal_key
        self.principal_name = principal_name
        self.product_type = product_type
        self.risk_source = risk_source
        self.status = status
        self.submit_audit_time = submit_audit_time
        self.submit_status = submit_status
        self.submit_time = submit_time
        self.submit_times = submit_times
        self.tm_code = tm_code
        self.tm_icon = tm_icon
        self.tm_name = tm_name
        self.type = type
        self.user_id = user_id

    def validate(self):
        if self.extend:
            self.extend.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bit_flag is not None:
            result['BitFlag'] = self.bit_flag
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.classification_code is not None:
            result['ClassificationCode'] = self.classification_code
        if self.delete_flag is not None:
            result['DeleteFlag'] = self.delete_flag
        if self.env is not None:
            result['Env'] = self.env
        if self.extend is not None:
            result['Extend'] = self.extend.to_map()
        if self.loa_id is not None:
            result['LoaId'] = self.loa_id
        if self.main_order_id is not None:
            result['MainOrderId'] = self.main_order_id
        if self.material_id is not None:
            result['MaterialId'] = self.material_id
        if self.material_name is not None:
            result['MaterialName'] = self.material_name
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.order_price is not None:
            result['OrderPrice'] = self.order_price
        if self.principal_key is not None:
            result['PrincipalKey'] = self.principal_key
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.risk_source is not None:
            result['RiskSource'] = self.risk_source
        if self.status is not None:
            result['Status'] = self.status
        if self.submit_audit_time is not None:
            result['SubmitAuditTime'] = self.submit_audit_time
        if self.submit_status is not None:
            result['SubmitStatus'] = self.submit_status
        if self.submit_time is not None:
            result['SubmitTime'] = self.submit_time
        if self.submit_times is not None:
            result['SubmitTimes'] = self.submit_times
        if self.tm_code is not None:
            result['TmCode'] = self.tm_code
        if self.tm_icon is not None:
            result['TmIcon'] = self.tm_icon
        if self.tm_name is not None:
            result['TmName'] = self.tm_name
        if self.type is not None:
            result['Type'] = self.type
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BitFlag') is not None:
            self.bit_flag = m.get('BitFlag')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('ClassificationCode') is not None:
            self.classification_code = m.get('ClassificationCode')
        if m.get('DeleteFlag') is not None:
            self.delete_flag = m.get('DeleteFlag')
        if m.get('Env') is not None:
            self.env = m.get('Env')
        if m.get('Extend') is not None:
            temp_model = QueryTmSbjProduceResponseBodyMoudleTmSbjProduceListExtend()
            self.extend = temp_model.from_map(m['Extend'])
        if m.get('LoaId') is not None:
            self.loa_id = m.get('LoaId')
        if m.get('MainOrderId') is not None:
            self.main_order_id = m.get('MainOrderId')
        if m.get('MaterialId') is not None:
            self.material_id = m.get('MaterialId')
        if m.get('MaterialName') is not None:
            self.material_name = m.get('MaterialName')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('OrderPrice') is not None:
            self.order_price = m.get('OrderPrice')
        if m.get('PrincipalKey') is not None:
            self.principal_key = m.get('PrincipalKey')
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('RiskSource') is not None:
            self.risk_source = m.get('RiskSource')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubmitAuditTime') is not None:
            self.submit_audit_time = m.get('SubmitAuditTime')
        if m.get('SubmitStatus') is not None:
            self.submit_status = m.get('SubmitStatus')
        if m.get('SubmitTime') is not None:
            self.submit_time = m.get('SubmitTime')
        if m.get('SubmitTimes') is not None:
            self.submit_times = m.get('SubmitTimes')
        if m.get('TmCode') is not None:
            self.tm_code = m.get('TmCode')
        if m.get('TmIcon') is not None:
            self.tm_icon = m.get('TmIcon')
        if m.get('TmName') is not None:
            self.tm_name = m.get('TmName')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class QueryTmSbjProduceResponseBodyMoudle(TeaModel):
    def __init__(
        self,
        tm_sbj_produce_list: List[QueryTmSbjProduceResponseBodyMoudleTmSbjProduceList] = None,
    ):
        self.tm_sbj_produce_list = tm_sbj_produce_list

    def validate(self):
        if self.tm_sbj_produce_list:
            for k in self.tm_sbj_produce_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TmSbjProduceList'] = []
        if self.tm_sbj_produce_list is not None:
            for k in self.tm_sbj_produce_list:
                result['TmSbjProduceList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tm_sbj_produce_list = []
        if m.get('TmSbjProduceList') is not None:
            for k in m.get('TmSbjProduceList'):
                temp_model = QueryTmSbjProduceResponseBodyMoudleTmSbjProduceList()
                self.tm_sbj_produce_list.append(temp_model.from_map(k))
        return self


class QueryTmSbjProduceResponseBody(TeaModel):
    def __init__(
        self,
        moudle: QueryTmSbjProduceResponseBodyMoudle = None,
        request_id: str = None,
    ):
        self.moudle = moudle
        self.request_id = request_id

    def validate(self):
        if self.moudle:
            self.moudle.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.moudle is not None:
            result['Moudle'] = self.moudle.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Moudle') is not None:
            temp_model = QueryTmSbjProduceResponseBodyMoudle()
            self.moudle = temp_model.from_map(m['Moudle'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryTmSbjProduceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryTmSbjProduceResponseBody = None,
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
            temp_model = QueryTmSbjProduceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTmSbjProduceDetailRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        order_id: str = None,
    ):
        self.biz_id = biz_id
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class QueryTmSbjProduceDetailResponseBodyFlags(TeaModel):
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


class QueryTmSbjProduceDetailResponseBodyLeafCodesLeafCodes(TeaModel):
    def __init__(
        self,
        code: str = None,
        name: str = None,
    ):
        self.code = code
        self.name = name

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class QueryTmSbjProduceDetailResponseBodyLeafCodes(TeaModel):
    def __init__(
        self,
        leaf_codes: List[QueryTmSbjProduceDetailResponseBodyLeafCodesLeafCodes] = None,
    ):
        self.leaf_codes = leaf_codes

    def validate(self):
        if self.leaf_codes:
            for k in self.leaf_codes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['LeafCodes'] = []
        if self.leaf_codes is not None:
            for k in self.leaf_codes:
                result['LeafCodes'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.leaf_codes = []
        if m.get('LeafCodes') is not None:
            for k in m.get('LeafCodes'):
                temp_model = QueryTmSbjProduceDetailResponseBodyLeafCodesLeafCodes()
                self.leaf_codes.append(temp_model.from_map(k))
        return self


class QueryTmSbjProduceDetailResponseBodyMaterialDetail(TeaModel):
    def __init__(
        self,
        address: str = None,
        business_licence_url: str = None,
        card_number: str = None,
        city: str = None,
        contact_address: str = None,
        contact_email: str = None,
        contact_name: str = None,
        contact_number: str = None,
        contact_province: str = None,
        contact_zipcode: str = None,
        country: str = None,
        detailed_contact_address: str = None,
        eaddress: str = None,
        ename: str = None,
        expiration_date: str = None,
        id_card_number: str = None,
        id_card_url: str = None,
        loa_url: str = None,
        name: str = None,
        passport_url: str = None,
        personal_type: int = None,
        province: str = None,
        region: int = None,
        status: int = None,
        town: str = None,
        type: int = None,
    ):
        self.address = address
        self.business_licence_url = business_licence_url
        self.card_number = card_number
        self.city = city
        self.contact_address = contact_address
        self.contact_email = contact_email
        self.contact_name = contact_name
        self.contact_number = contact_number
        self.contact_province = contact_province
        self.contact_zipcode = contact_zipcode
        self.country = country
        self.detailed_contact_address = detailed_contact_address
        self.eaddress = eaddress
        self.ename = ename
        self.expiration_date = expiration_date
        self.id_card_number = id_card_number
        self.id_card_url = id_card_url
        self.loa_url = loa_url
        self.name = name
        self.passport_url = passport_url
        self.personal_type = personal_type
        self.province = province
        self.region = region
        self.status = status
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
        if self.business_licence_url is not None:
            result['BusinessLicenceUrl'] = self.business_licence_url
        if self.card_number is not None:
            result['CardNumber'] = self.card_number
        if self.city is not None:
            result['City'] = self.city
        if self.contact_address is not None:
            result['ContactAddress'] = self.contact_address
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
        if self.detailed_contact_address is not None:
            result['DetailedContactAddress'] = self.detailed_contact_address
        if self.eaddress is not None:
            result['EAddress'] = self.eaddress
        if self.ename is not None:
            result['EName'] = self.ename
        if self.expiration_date is not None:
            result['ExpirationDate'] = self.expiration_date
        if self.id_card_number is not None:
            result['IdCardNumber'] = self.id_card_number
        if self.id_card_url is not None:
            result['IdCardUrl'] = self.id_card_url
        if self.loa_url is not None:
            result['LoaUrl'] = self.loa_url
        if self.name is not None:
            result['Name'] = self.name
        if self.passport_url is not None:
            result['PassportUrl'] = self.passport_url
        if self.personal_type is not None:
            result['PersonalType'] = self.personal_type
        if self.province is not None:
            result['Province'] = self.province
        if self.region is not None:
            result['Region'] = self.region
        if self.status is not None:
            result['Status'] = self.status
        if self.town is not None:
            result['Town'] = self.town
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('BusinessLicenceUrl') is not None:
            self.business_licence_url = m.get('BusinessLicenceUrl')
        if m.get('CardNumber') is not None:
            self.card_number = m.get('CardNumber')
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('ContactAddress') is not None:
            self.contact_address = m.get('ContactAddress')
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
        if m.get('DetailedContactAddress') is not None:
            self.detailed_contact_address = m.get('DetailedContactAddress')
        if m.get('EAddress') is not None:
            self.eaddress = m.get('EAddress')
        if m.get('EName') is not None:
            self.ename = m.get('EName')
        if m.get('ExpirationDate') is not None:
            self.expiration_date = m.get('ExpirationDate')
        if m.get('IdCardNumber') is not None:
            self.id_card_number = m.get('IdCardNumber')
        if m.get('IdCardUrl') is not None:
            self.id_card_url = m.get('IdCardUrl')
        if m.get('LoaUrl') is not None:
            self.loa_url = m.get('LoaUrl')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PassportUrl') is not None:
            self.passport_url = m.get('PassportUrl')
        if m.get('PersonalType') is not None:
            self.personal_type = m.get('PersonalType')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Town') is not None:
            self.town = m.get('Town')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class QueryTmSbjProduceDetailResponseBodyRootCode(TeaModel):
    def __init__(
        self,
        code: str = None,
        name: str = None,
    ):
        self.code = code
        self.name = name

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class QueryTmSbjProduceDetailResponseBody(TeaModel):
    def __init__(
        self,
        accept_url: str = None,
        biz_id: str = None,
        cn_info_url: str = None,
        extend_info: Dict[str, Any] = None,
        flags: QueryTmSbjProduceDetailResponseBodyFlags = None,
        gray_icon_url: str = None,
        issue_date: str = None,
        leaf_codes: QueryTmSbjProduceDetailResponseBodyLeafCodes = None,
        loa_url: str = None,
        material_detail: QueryTmSbjProduceDetailResponseBodyMaterialDetail = None,
        material_name: str = None,
        note: str = None,
        order_id: str = None,
        principal_name: int = None,
        request_id: str = None,
        root_code: QueryTmSbjProduceDetailResponseBodyRootCode = None,
        status: int = None,
        submit_count: int = None,
        submit_status: str = None,
        tm_icon: str = None,
        tm_name: str = None,
        tm_name_type: int = None,
        tm_number: str = None,
        tm_order_id: str = None,
        type: int = None,
    ):
        self.accept_url = accept_url
        self.biz_id = biz_id
        self.cn_info_url = cn_info_url
        self.extend_info = extend_info
        self.flags = flags
        self.gray_icon_url = gray_icon_url
        self.issue_date = issue_date
        self.leaf_codes = leaf_codes
        self.loa_url = loa_url
        self.material_detail = material_detail
        self.material_name = material_name
        self.note = note
        self.order_id = order_id
        self.principal_name = principal_name
        self.request_id = request_id
        self.root_code = root_code
        self.status = status
        self.submit_count = submit_count
        self.submit_status = submit_status
        self.tm_icon = tm_icon
        self.tm_name = tm_name
        self.tm_name_type = tm_name_type
        self.tm_number = tm_number
        self.tm_order_id = tm_order_id
        self.type = type

    def validate(self):
        if self.flags:
            self.flags.validate()
        if self.leaf_codes:
            self.leaf_codes.validate()
        if self.material_detail:
            self.material_detail.validate()
        if self.root_code:
            self.root_code.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_url is not None:
            result['AcceptUrl'] = self.accept_url
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.cn_info_url is not None:
            result['CnInfoUrl'] = self.cn_info_url
        if self.extend_info is not None:
            result['ExtendInfo'] = self.extend_info
        if self.flags is not None:
            result['Flags'] = self.flags.to_map()
        if self.gray_icon_url is not None:
            result['GrayIconUrl'] = self.gray_icon_url
        if self.issue_date is not None:
            result['IssueDate'] = self.issue_date
        if self.leaf_codes is not None:
            result['LeafCodes'] = self.leaf_codes.to_map()
        if self.loa_url is not None:
            result['LoaUrl'] = self.loa_url
        if self.material_detail is not None:
            result['MaterialDetail'] = self.material_detail.to_map()
        if self.material_name is not None:
            result['MaterialName'] = self.material_name
        if self.note is not None:
            result['Note'] = self.note
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.root_code is not None:
            result['RootCode'] = self.root_code.to_map()
        if self.status is not None:
            result['Status'] = self.status
        if self.submit_count is not None:
            result['SubmitCount'] = self.submit_count
        if self.submit_status is not None:
            result['SubmitStatus'] = self.submit_status
        if self.tm_icon is not None:
            result['TmIcon'] = self.tm_icon
        if self.tm_name is not None:
            result['TmName'] = self.tm_name
        if self.tm_name_type is not None:
            result['TmNameType'] = self.tm_name_type
        if self.tm_number is not None:
            result['TmNumber'] = self.tm_number
        if self.tm_order_id is not None:
            result['TmOrderId'] = self.tm_order_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptUrl') is not None:
            self.accept_url = m.get('AcceptUrl')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('CnInfoUrl') is not None:
            self.cn_info_url = m.get('CnInfoUrl')
        if m.get('ExtendInfo') is not None:
            self.extend_info = m.get('ExtendInfo')
        if m.get('Flags') is not None:
            temp_model = QueryTmSbjProduceDetailResponseBodyFlags()
            self.flags = temp_model.from_map(m['Flags'])
        if m.get('GrayIconUrl') is not None:
            self.gray_icon_url = m.get('GrayIconUrl')
        if m.get('IssueDate') is not None:
            self.issue_date = m.get('IssueDate')
        if m.get('LeafCodes') is not None:
            temp_model = QueryTmSbjProduceDetailResponseBodyLeafCodes()
            self.leaf_codes = temp_model.from_map(m['LeafCodes'])
        if m.get('LoaUrl') is not None:
            self.loa_url = m.get('LoaUrl')
        if m.get('MaterialDetail') is not None:
            temp_model = QueryTmSbjProduceDetailResponseBodyMaterialDetail()
            self.material_detail = temp_model.from_map(m['MaterialDetail'])
        if m.get('MaterialName') is not None:
            self.material_name = m.get('MaterialName')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RootCode') is not None:
            temp_model = QueryTmSbjProduceDetailResponseBodyRootCode()
            self.root_code = temp_model.from_map(m['RootCode'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubmitCount') is not None:
            self.submit_count = m.get('SubmitCount')
        if m.get('SubmitStatus') is not None:
            self.submit_status = m.get('SubmitStatus')
        if m.get('TmIcon') is not None:
            self.tm_icon = m.get('TmIcon')
        if m.get('TmName') is not None:
            self.tm_name = m.get('TmName')
        if m.get('TmNameType') is not None:
            self.tm_name_type = m.get('TmNameType')
        if m.get('TmNumber') is not None:
            self.tm_number = m.get('TmNumber')
        if m.get('TmOrderId') is not None:
            self.tm_order_id = m.get('TmOrderId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class QueryTmSbjProduceDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryTmSbjProduceDetailResponseBody = None,
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
            temp_model = QueryTmSbjProduceDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTradeIntentionUserListRequest(TeaModel):
    def __init__(
        self,
        begin: int = None,
        biz_id: str = None,
        end: int = None,
        page_num: int = None,
        page_size: int = None,
        status: int = None,
        type: int = None,
    ):
        self.begin = begin
        self.biz_id = biz_id
        self.end = end
        self.page_num = page_num
        self.page_size = page_size
        self.status = status
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin is not None:
            result['Begin'] = self.begin
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.end is not None:
            result['End'] = self.end
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Begin') is not None:
            self.begin = m.get('Begin')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('End') is not None:
            self.end = m.get('End')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class QueryTradeIntentionUserListResponseBodyDataTrademark(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        classification: str = None,
        description: str = None,
        document_date: str = None,
        document_name: str = None,
        document_url: str = None,
        grade: int = None,
        mobile: str = None,
        register_number: str = None,
        status: int = None,
        type: int = None,
        user_name: str = None,
    ):
        self.biz_id = biz_id
        self.classification = classification
        self.description = description
        self.document_date = document_date
        self.document_name = document_name
        self.document_url = document_url
        self.grade = grade
        self.mobile = mobile
        self.register_number = register_number
        self.status = status
        self.type = type
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.classification is not None:
            result['Classification'] = self.classification
        if self.description is not None:
            result['Description'] = self.description
        if self.document_date is not None:
            result['DocumentDate'] = self.document_date
        if self.document_name is not None:
            result['DocumentName'] = self.document_name
        if self.document_url is not None:
            result['DocumentUrl'] = self.document_url
        if self.grade is not None:
            result['Grade'] = self.grade
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.register_number is not None:
            result['RegisterNumber'] = self.register_number
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Classification') is not None:
            self.classification = m.get('Classification')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DocumentDate') is not None:
            self.document_date = m.get('DocumentDate')
        if m.get('DocumentName') is not None:
            self.document_name = m.get('DocumentName')
        if m.get('DocumentUrl') is not None:
            self.document_url = m.get('DocumentUrl')
        if m.get('Grade') is not None:
            self.grade = m.get('Grade')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('RegisterNumber') is not None:
            self.register_number = m.get('RegisterNumber')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class QueryTradeIntentionUserListResponseBodyData(TeaModel):
    def __init__(
        self,
        trademark: List[QueryTradeIntentionUserListResponseBodyDataTrademark] = None,
    ):
        self.trademark = trademark

    def validate(self):
        if self.trademark:
            for k in self.trademark:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Trademark'] = []
        if self.trademark is not None:
            for k in self.trademark:
                result['Trademark'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.trademark = []
        if m.get('Trademark') is not None:
            for k in m.get('Trademark'):
                temp_model = QueryTradeIntentionUserListResponseBodyDataTrademark()
                self.trademark.append(temp_model.from_map(k))
        return self


class QueryTradeIntentionUserListResponseBody(TeaModel):
    def __init__(
        self,
        current_page_num: int = None,
        data: QueryTradeIntentionUserListResponseBodyData = None,
        page_size: int = None,
        request_id: str = None,
        total_item_num: int = None,
        total_page_num: int = None,
    ):
        self.current_page_num = current_page_num
        self.data = data
        self.page_size = page_size
        self.request_id = request_id
        self.total_item_num = total_item_num
        self.total_page_num = total_page_num

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page_num is not None:
            result['CurrentPageNum'] = self.current_page_num
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_item_num is not None:
            result['TotalItemNum'] = self.total_item_num
        if self.total_page_num is not None:
            result['TotalPageNum'] = self.total_page_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPageNum') is not None:
            self.current_page_num = m.get('CurrentPageNum')
        if m.get('Data') is not None:
            temp_model = QueryTradeIntentionUserListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalItemNum') is not None:
            self.total_item_num = m.get('TotalItemNum')
        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')
        return self


class QueryTradeIntentionUserListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryTradeIntentionUserListResponseBody = None,
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
            temp_model = QueryTradeIntentionUserListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTradeMarkApplicationDetailRequest(TeaModel):
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


class QueryTradeMarkApplicationDetailResponseBodyAdminUploads(TeaModel):
    def __init__(
        self,
        license_pic_url: str = None,
        loa_pic_url: str = None,
    ):
        self.license_pic_url = license_pic_url
        self.loa_pic_url = loa_pic_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.license_pic_url is not None:
            result['LicensePicUrl'] = self.license_pic_url
        if self.loa_pic_url is not None:
            result['LoaPicUrl'] = self.loa_pic_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LicensePicUrl') is not None:
            self.license_pic_url = m.get('LicensePicUrl')
        if m.get('LoaPicUrl') is not None:
            self.loa_pic_url = m.get('LoaPicUrl')
        return self


class QueryTradeMarkApplicationDetailResponseBodyFirstClassification(TeaModel):
    def __init__(
        self,
        code: str = None,
        name: str = None,
    ):
        self.code = code
        self.name = name

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class QueryTradeMarkApplicationDetailResponseBodyFlags(TeaModel):
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


class QueryTradeMarkApplicationDetailResponseBodyJudgeResultUrl(TeaModel):
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


class QueryTradeMarkApplicationDetailResponseBodyMaterialDetailReviewAdditionalFiles(TeaModel):
    def __init__(
        self,
        review_additional_file: List[str] = None,
    ):
        self.review_additional_file = review_additional_file

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.review_additional_file is not None:
            result['ReviewAdditionalFile'] = self.review_additional_file
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReviewAdditionalFile') is not None:
            self.review_additional_file = m.get('ReviewAdditionalFile')
        return self


class QueryTradeMarkApplicationDetailResponseBodyMaterialDetail(TeaModel):
    def __init__(
        self,
        address: str = None,
        business_licence_url: str = None,
        card_number: str = None,
        city: str = None,
        contact_address: str = None,
        contact_city: str = None,
        contact_district: str = None,
        contact_email: str = None,
        contact_name: str = None,
        contact_number: str = None,
        contact_province: str = None,
        contact_zipcode: str = None,
        country: str = None,
        detailed_contact_address: str = None,
        eaddress: str = None,
        ename: str = None,
        expiration_date: str = None,
        fact_and_reason_pdf_path: str = None,
        id_card_name: str = None,
        id_card_number: str = None,
        id_card_url: str = None,
        legal_notice_url: str = None,
        loa_url: str = None,
        material_version: str = None,
        name: str = None,
        passport_url: str = None,
        personal_type: int = None,
        principal_name: int = None,
        province: str = None,
        region: int = None,
        review_additional_files: QueryTradeMarkApplicationDetailResponseBodyMaterialDetailReviewAdditionalFiles = None,
        review_application_file: str = None,
        status: int = None,
        supplement_evidence_catalog_file: str = None,
        supplement_evidence_material_file: str = None,
        supplement_reason_file: str = None,
        town: str = None,
        type: int = None,
    ):
        self.address = address
        self.business_licence_url = business_licence_url
        self.card_number = card_number
        self.city = city
        self.contact_address = contact_address
        self.contact_city = contact_city
        self.contact_district = contact_district
        self.contact_email = contact_email
        self.contact_name = contact_name
        self.contact_number = contact_number
        self.contact_province = contact_province
        self.contact_zipcode = contact_zipcode
        self.country = country
        self.detailed_contact_address = detailed_contact_address
        self.eaddress = eaddress
        self.ename = ename
        self.expiration_date = expiration_date
        self.fact_and_reason_pdf_path = fact_and_reason_pdf_path
        self.id_card_name = id_card_name
        self.id_card_number = id_card_number
        self.id_card_url = id_card_url
        self.legal_notice_url = legal_notice_url
        self.loa_url = loa_url
        self.material_version = material_version
        self.name = name
        self.passport_url = passport_url
        self.personal_type = personal_type
        self.principal_name = principal_name
        self.province = province
        self.region = region
        self.review_additional_files = review_additional_files
        self.review_application_file = review_application_file
        self.status = status
        self.supplement_evidence_catalog_file = supplement_evidence_catalog_file
        self.supplement_evidence_material_file = supplement_evidence_material_file
        self.supplement_reason_file = supplement_reason_file
        self.town = town
        self.type = type

    def validate(self):
        if self.review_additional_files:
            self.review_additional_files.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.business_licence_url is not None:
            result['BusinessLicenceUrl'] = self.business_licence_url
        if self.card_number is not None:
            result['CardNumber'] = self.card_number
        if self.city is not None:
            result['City'] = self.city
        if self.contact_address is not None:
            result['ContactAddress'] = self.contact_address
        if self.contact_city is not None:
            result['ContactCity'] = self.contact_city
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
        if self.detailed_contact_address is not None:
            result['DetailedContactAddress'] = self.detailed_contact_address
        if self.eaddress is not None:
            result['EAddress'] = self.eaddress
        if self.ename is not None:
            result['EName'] = self.ename
        if self.expiration_date is not None:
            result['ExpirationDate'] = self.expiration_date
        if self.fact_and_reason_pdf_path is not None:
            result['FactAndReasonPdfPath'] = self.fact_and_reason_pdf_path
        if self.id_card_name is not None:
            result['IdCardName'] = self.id_card_name
        if self.id_card_number is not None:
            result['IdCardNumber'] = self.id_card_number
        if self.id_card_url is not None:
            result['IdCardUrl'] = self.id_card_url
        if self.legal_notice_url is not None:
            result['LegalNoticeUrl'] = self.legal_notice_url
        if self.loa_url is not None:
            result['LoaUrl'] = self.loa_url
        if self.material_version is not None:
            result['MaterialVersion'] = self.material_version
        if self.name is not None:
            result['Name'] = self.name
        if self.passport_url is not None:
            result['PassportUrl'] = self.passport_url
        if self.personal_type is not None:
            result['PersonalType'] = self.personal_type
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name
        if self.province is not None:
            result['Province'] = self.province
        if self.region is not None:
            result['Region'] = self.region
        if self.review_additional_files is not None:
            result['ReviewAdditionalFiles'] = self.review_additional_files.to_map()
        if self.review_application_file is not None:
            result['ReviewApplicationFile'] = self.review_application_file
        if self.status is not None:
            result['Status'] = self.status
        if self.supplement_evidence_catalog_file is not None:
            result['SupplementEvidenceCatalogFile'] = self.supplement_evidence_catalog_file
        if self.supplement_evidence_material_file is not None:
            result['SupplementEvidenceMaterialFile'] = self.supplement_evidence_material_file
        if self.supplement_reason_file is not None:
            result['SupplementReasonFile'] = self.supplement_reason_file
        if self.town is not None:
            result['Town'] = self.town
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('BusinessLicenceUrl') is not None:
            self.business_licence_url = m.get('BusinessLicenceUrl')
        if m.get('CardNumber') is not None:
            self.card_number = m.get('CardNumber')
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('ContactAddress') is not None:
            self.contact_address = m.get('ContactAddress')
        if m.get('ContactCity') is not None:
            self.contact_city = m.get('ContactCity')
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
        if m.get('DetailedContactAddress') is not None:
            self.detailed_contact_address = m.get('DetailedContactAddress')
        if m.get('EAddress') is not None:
            self.eaddress = m.get('EAddress')
        if m.get('EName') is not None:
            self.ename = m.get('EName')
        if m.get('ExpirationDate') is not None:
            self.expiration_date = m.get('ExpirationDate')
        if m.get('FactAndReasonPdfPath') is not None:
            self.fact_and_reason_pdf_path = m.get('FactAndReasonPdfPath')
        if m.get('IdCardName') is not None:
            self.id_card_name = m.get('IdCardName')
        if m.get('IdCardNumber') is not None:
            self.id_card_number = m.get('IdCardNumber')
        if m.get('IdCardUrl') is not None:
            self.id_card_url = m.get('IdCardUrl')
        if m.get('LegalNoticeUrl') is not None:
            self.legal_notice_url = m.get('LegalNoticeUrl')
        if m.get('LoaUrl') is not None:
            self.loa_url = m.get('LoaUrl')
        if m.get('MaterialVersion') is not None:
            self.material_version = m.get('MaterialVersion')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PassportUrl') is not None:
            self.passport_url = m.get('PassportUrl')
        if m.get('PersonalType') is not None:
            self.personal_type = m.get('PersonalType')
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ReviewAdditionalFiles') is not None:
            temp_model = QueryTradeMarkApplicationDetailResponseBodyMaterialDetailReviewAdditionalFiles()
            self.review_additional_files = temp_model.from_map(m['ReviewAdditionalFiles'])
        if m.get('ReviewApplicationFile') is not None:
            self.review_application_file = m.get('ReviewApplicationFile')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SupplementEvidenceCatalogFile') is not None:
            self.supplement_evidence_catalog_file = m.get('SupplementEvidenceCatalogFile')
        if m.get('SupplementEvidenceMaterialFile') is not None:
            self.supplement_evidence_material_file = m.get('SupplementEvidenceMaterialFile')
        if m.get('SupplementReasonFile') is not None:
            self.supplement_reason_file = m.get('SupplementReasonFile')
        if m.get('Town') is not None:
            self.town = m.get('Town')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class QueryTradeMarkApplicationDetailResponseBodyReceiptUrl(TeaModel):
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


class QueryTradeMarkApplicationDetailResponseBodyRenewResponse(TeaModel):
    def __init__(
        self,
        address: str = None,
        eng_address: str = None,
        eng_name: str = None,
        name: str = None,
        register_time: int = None,
        submit_sbjtime: int = None,
    ):
        self.address = address
        self.eng_address = eng_address
        self.eng_name = eng_name
        self.name = name
        self.register_time = register_time
        self.submit_sbjtime = submit_sbjtime

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.eng_address is not None:
            result['EngAddress'] = self.eng_address
        if self.eng_name is not None:
            result['EngName'] = self.eng_name
        if self.name is not None:
            result['Name'] = self.name
        if self.register_time is not None:
            result['RegisterTime'] = self.register_time
        if self.submit_sbjtime is not None:
            result['SubmitSbjtime'] = self.submit_sbjtime
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('EngAddress') is not None:
            self.eng_address = m.get('EngAddress')
        if m.get('EngName') is not None:
            self.eng_name = m.get('EngName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegisterTime') is not None:
            self.register_time = m.get('RegisterTime')
        if m.get('SubmitSbjtime') is not None:
            self.submit_sbjtime = m.get('SubmitSbjtime')
        return self


class QueryTradeMarkApplicationDetailResponseBodyReviewOfficialFilesReviewSupplements(TeaModel):
    def __init__(
        self,
        review_supplement: List[str] = None,
    ):
        self.review_supplement = review_supplement

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.review_supplement is not None:
            result['ReviewSupplement'] = self.review_supplement
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReviewSupplement') is not None:
            self.review_supplement = m.get('ReviewSupplement')
        return self


class QueryTradeMarkApplicationDetailResponseBodyReviewOfficialFiles(TeaModel):
    def __init__(
        self,
        review_audit: str = None,
        review_keep: str = None,
        review_part: str = None,
        review_pass: str = None,
        review_supplements: QueryTradeMarkApplicationDetailResponseBodyReviewOfficialFilesReviewSupplements = None,
    ):
        self.review_audit = review_audit
        self.review_keep = review_keep
        self.review_part = review_part
        self.review_pass = review_pass
        self.review_supplements = review_supplements

    def validate(self):
        if self.review_supplements:
            self.review_supplements.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.review_audit is not None:
            result['ReviewAudit'] = self.review_audit
        if self.review_keep is not None:
            result['ReviewKeep'] = self.review_keep
        if self.review_part is not None:
            result['ReviewPart'] = self.review_part
        if self.review_pass is not None:
            result['ReviewPass'] = self.review_pass
        if self.review_supplements is not None:
            result['ReviewSupplements'] = self.review_supplements.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReviewAudit') is not None:
            self.review_audit = m.get('ReviewAudit')
        if m.get('ReviewKeep') is not None:
            self.review_keep = m.get('ReviewKeep')
        if m.get('ReviewPart') is not None:
            self.review_part = m.get('ReviewPart')
        if m.get('ReviewPass') is not None:
            self.review_pass = m.get('ReviewPass')
        if m.get('ReviewSupplements') is not None:
            temp_model = QueryTradeMarkApplicationDetailResponseBodyReviewOfficialFilesReviewSupplements()
            self.review_supplements = temp_model.from_map(m['ReviewSupplements'])
        return self


class QueryTradeMarkApplicationDetailResponseBodySupplementsSupplementsFileTemplateUrls(TeaModel):
    def __init__(
        self,
        file_template_urls: List[str] = None,
    ):
        self.file_template_urls = file_template_urls

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_template_urls is not None:
            result['FileTemplateUrls'] = self.file_template_urls
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileTemplateUrls') is not None:
            self.file_template_urls = m.get('FileTemplateUrls')
        return self


class QueryTradeMarkApplicationDetailResponseBodySupplementsSupplements(TeaModel):
    def __init__(
        self,
        accept_dead_time: int = None,
        accept_time: int = None,
        batch_num: str = None,
        content: str = None,
        file_template_urls: QueryTradeMarkApplicationDetailResponseBodySupplementsSupplementsFileTemplateUrls = None,
        filename: str = None,
        id: int = None,
        operate_time: int = None,
        order_id: str = None,
        sbj_dead_time: int = None,
        send_time: int = None,
        serial_number: str = None,
        status: int = None,
        tm_number: str = None,
        type: int = None,
        upload_file_template_url: str = None,
    ):
        self.accept_dead_time = accept_dead_time
        self.accept_time = accept_time
        self.batch_num = batch_num
        self.content = content
        self.file_template_urls = file_template_urls
        self.filename = filename
        self.id = id
        self.operate_time = operate_time
        self.order_id = order_id
        self.sbj_dead_time = sbj_dead_time
        self.send_time = send_time
        self.serial_number = serial_number
        self.status = status
        self.tm_number = tm_number
        self.type = type
        self.upload_file_template_url = upload_file_template_url

    def validate(self):
        if self.file_template_urls:
            self.file_template_urls.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_dead_time is not None:
            result['AcceptDeadTime'] = self.accept_dead_time
        if self.accept_time is not None:
            result['AcceptTime'] = self.accept_time
        if self.batch_num is not None:
            result['BatchNum'] = self.batch_num
        if self.content is not None:
            result['Content'] = self.content
        if self.file_template_urls is not None:
            result['FileTemplateUrls'] = self.file_template_urls.to_map()
        if self.filename is not None:
            result['Filename'] = self.filename
        if self.id is not None:
            result['Id'] = self.id
        if self.operate_time is not None:
            result['OperateTime'] = self.operate_time
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.sbj_dead_time is not None:
            result['SbjDeadTime'] = self.sbj_dead_time
        if self.send_time is not None:
            result['SendTime'] = self.send_time
        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number
        if self.status is not None:
            result['Status'] = self.status
        if self.tm_number is not None:
            result['TmNumber'] = self.tm_number
        if self.type is not None:
            result['Type'] = self.type
        if self.upload_file_template_url is not None:
            result['UploadFileTemplateUrl'] = self.upload_file_template_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptDeadTime') is not None:
            self.accept_dead_time = m.get('AcceptDeadTime')
        if m.get('AcceptTime') is not None:
            self.accept_time = m.get('AcceptTime')
        if m.get('BatchNum') is not None:
            self.batch_num = m.get('BatchNum')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('FileTemplateUrls') is not None:
            temp_model = QueryTradeMarkApplicationDetailResponseBodySupplementsSupplementsFileTemplateUrls()
            self.file_template_urls = temp_model.from_map(m['FileTemplateUrls'])
        if m.get('Filename') is not None:
            self.filename = m.get('Filename')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OperateTime') is not None:
            self.operate_time = m.get('OperateTime')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('SbjDeadTime') is not None:
            self.sbj_dead_time = m.get('SbjDeadTime')
        if m.get('SendTime') is not None:
            self.send_time = m.get('SendTime')
        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TmNumber') is not None:
            self.tm_number = m.get('TmNumber')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UploadFileTemplateUrl') is not None:
            self.upload_file_template_url = m.get('UploadFileTemplateUrl')
        return self


class QueryTradeMarkApplicationDetailResponseBodySupplements(TeaModel):
    def __init__(
        self,
        supplements: List[QueryTradeMarkApplicationDetailResponseBodySupplementsSupplements] = None,
    ):
        self.supplements = supplements

    def validate(self):
        if self.supplements:
            for k in self.supplements:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Supplements'] = []
        if self.supplements is not None:
            for k in self.supplements:
                result['Supplements'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.supplements = []
        if m.get('Supplements') is not None:
            for k in m.get('Supplements'):
                temp_model = QueryTradeMarkApplicationDetailResponseBodySupplementsSupplements()
                self.supplements.append(temp_model.from_map(k))
        return self


class QueryTradeMarkApplicationDetailResponseBodyThirdClassificationThirdClassifications(TeaModel):
    def __init__(
        self,
        code: str = None,
        name: str = None,
    ):
        self.code = code
        self.name = name

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class QueryTradeMarkApplicationDetailResponseBodyThirdClassification(TeaModel):
    def __init__(
        self,
        third_classifications: List[QueryTradeMarkApplicationDetailResponseBodyThirdClassificationThirdClassifications] = None,
    ):
        self.third_classifications = third_classifications

    def validate(self):
        if self.third_classifications:
            for k in self.third_classifications:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ThirdClassifications'] = []
        if self.third_classifications is not None:
            for k in self.third_classifications:
                result['ThirdClassifications'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.third_classifications = []
        if m.get('ThirdClassifications') is not None:
            for k in m.get('ThirdClassifications'):
                temp_model = QueryTradeMarkApplicationDetailResponseBodyThirdClassificationThirdClassifications()
                self.third_classifications.append(temp_model.from_map(k))
        return self


class QueryTradeMarkApplicationDetailResponseBody(TeaModel):
    def __init__(
        self,
        accept_url: str = None,
        admin_uploads: QueryTradeMarkApplicationDetailResponseBodyAdminUploads = None,
        biz_id: str = None,
        create_time: int = None,
        extend_info: Dict[str, Any] = None,
        first_classification: QueryTradeMarkApplicationDetailResponseBodyFirstClassification = None,
        flags: QueryTradeMarkApplicationDetailResponseBodyFlags = None,
        gray_icon_url: str = None,
        judge_result_url: QueryTradeMarkApplicationDetailResponseBodyJudgeResultUrl = None,
        legal_notice_url: str = None,
        loa_url: str = None,
        logistics_certificate_url: str = None,
        logistics_no: str = None,
        material_detail: QueryTradeMarkApplicationDetailResponseBodyMaterialDetail = None,
        material_id: int = None,
        not_accept_url: str = None,
        note: str = None,
        order_id: str = None,
        order_price: float = None,
        partner_code: str = None,
        partner_mobile: str = None,
        partner_name: str = None,
        principal_name: int = None,
        receipt_url: QueryTradeMarkApplicationDetailResponseBodyReceiptUrl = None,
        recv_user_logistics: str = None,
        renew_response: QueryTradeMarkApplicationDetailResponseBodyRenewResponse = None,
        request_id: str = None,
        review_official_files: QueryTradeMarkApplicationDetailResponseBodyReviewOfficialFiles = None,
        send_sbj_logistics: str = None,
        send_time: str = None,
        send_user_logistics: str = None,
        service_price: float = None,
        specification: int = None,
        status: int = None,
        submit_audit_time: int = None,
        submit_time: int = None,
        supplements: QueryTradeMarkApplicationDetailResponseBodySupplements = None,
        system_version: str = None,
        third_classification: QueryTradeMarkApplicationDetailResponseBodyThirdClassification = None,
        tm_icon: str = None,
        tm_name: str = None,
        tm_name_type: int = None,
        tm_number: str = None,
        total_price: float = None,
        type: int = None,
        update_time: int = None,
    ):
        self.accept_url = accept_url
        self.admin_uploads = admin_uploads
        self.biz_id = biz_id
        self.create_time = create_time
        self.extend_info = extend_info
        self.first_classification = first_classification
        self.flags = flags
        self.gray_icon_url = gray_icon_url
        self.judge_result_url = judge_result_url
        self.legal_notice_url = legal_notice_url
        self.loa_url = loa_url
        self.logistics_certificate_url = logistics_certificate_url
        self.logistics_no = logistics_no
        self.material_detail = material_detail
        self.material_id = material_id
        self.not_accept_url = not_accept_url
        self.note = note
        self.order_id = order_id
        self.order_price = order_price
        self.partner_code = partner_code
        self.partner_mobile = partner_mobile
        self.partner_name = partner_name
        self.principal_name = principal_name
        self.receipt_url = receipt_url
        self.recv_user_logistics = recv_user_logistics
        self.renew_response = renew_response
        self.request_id = request_id
        self.review_official_files = review_official_files
        self.send_sbj_logistics = send_sbj_logistics
        self.send_time = send_time
        self.send_user_logistics = send_user_logistics
        self.service_price = service_price
        self.specification = specification
        self.status = status
        self.submit_audit_time = submit_audit_time
        self.submit_time = submit_time
        self.supplements = supplements
        self.system_version = system_version
        self.third_classification = third_classification
        self.tm_icon = tm_icon
        self.tm_name = tm_name
        self.tm_name_type = tm_name_type
        self.tm_number = tm_number
        self.total_price = total_price
        self.type = type
        self.update_time = update_time

    def validate(self):
        if self.admin_uploads:
            self.admin_uploads.validate()
        if self.first_classification:
            self.first_classification.validate()
        if self.flags:
            self.flags.validate()
        if self.judge_result_url:
            self.judge_result_url.validate()
        if self.material_detail:
            self.material_detail.validate()
        if self.receipt_url:
            self.receipt_url.validate()
        if self.renew_response:
            self.renew_response.validate()
        if self.review_official_files:
            self.review_official_files.validate()
        if self.supplements:
            self.supplements.validate()
        if self.third_classification:
            self.third_classification.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_url is not None:
            result['AcceptUrl'] = self.accept_url
        if self.admin_uploads is not None:
            result['AdminUploads'] = self.admin_uploads.to_map()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.extend_info is not None:
            result['ExtendInfo'] = self.extend_info
        if self.first_classification is not None:
            result['FirstClassification'] = self.first_classification.to_map()
        if self.flags is not None:
            result['Flags'] = self.flags.to_map()
        if self.gray_icon_url is not None:
            result['GrayIconUrl'] = self.gray_icon_url
        if self.judge_result_url is not None:
            result['JudgeResultUrl'] = self.judge_result_url.to_map()
        if self.legal_notice_url is not None:
            result['LegalNoticeUrl'] = self.legal_notice_url
        if self.loa_url is not None:
            result['LoaUrl'] = self.loa_url
        if self.logistics_certificate_url is not None:
            result['LogisticsCertificateUrl'] = self.logistics_certificate_url
        if self.logistics_no is not None:
            result['LogisticsNo'] = self.logistics_no
        if self.material_detail is not None:
            result['MaterialDetail'] = self.material_detail.to_map()
        if self.material_id is not None:
            result['MaterialId'] = self.material_id
        if self.not_accept_url is not None:
            result['NotAcceptUrl'] = self.not_accept_url
        if self.note is not None:
            result['Note'] = self.note
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.order_price is not None:
            result['OrderPrice'] = self.order_price
        if self.partner_code is not None:
            result['PartnerCode'] = self.partner_code
        if self.partner_mobile is not None:
            result['PartnerMobile'] = self.partner_mobile
        if self.partner_name is not None:
            result['PartnerName'] = self.partner_name
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name
        if self.receipt_url is not None:
            result['ReceiptUrl'] = self.receipt_url.to_map()
        if self.recv_user_logistics is not None:
            result['RecvUserLogistics'] = self.recv_user_logistics
        if self.renew_response is not None:
            result['RenewResponse'] = self.renew_response.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.review_official_files is not None:
            result['ReviewOfficialFiles'] = self.review_official_files.to_map()
        if self.send_sbj_logistics is not None:
            result['SendSbjLogistics'] = self.send_sbj_logistics
        if self.send_time is not None:
            result['SendTime'] = self.send_time
        if self.send_user_logistics is not None:
            result['SendUserLogistics'] = self.send_user_logistics
        if self.service_price is not None:
            result['ServicePrice'] = self.service_price
        if self.specification is not None:
            result['Specification'] = self.specification
        if self.status is not None:
            result['Status'] = self.status
        if self.submit_audit_time is not None:
            result['SubmitAuditTime'] = self.submit_audit_time
        if self.submit_time is not None:
            result['SubmitTime'] = self.submit_time
        if self.supplements is not None:
            result['Supplements'] = self.supplements.to_map()
        if self.system_version is not None:
            result['SystemVersion'] = self.system_version
        if self.third_classification is not None:
            result['ThirdClassification'] = self.third_classification.to_map()
        if self.tm_icon is not None:
            result['TmIcon'] = self.tm_icon
        if self.tm_name is not None:
            result['TmName'] = self.tm_name
        if self.tm_name_type is not None:
            result['TmNameType'] = self.tm_name_type
        if self.tm_number is not None:
            result['TmNumber'] = self.tm_number
        if self.total_price is not None:
            result['TotalPrice'] = self.total_price
        if self.type is not None:
            result['Type'] = self.type
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptUrl') is not None:
            self.accept_url = m.get('AcceptUrl')
        if m.get('AdminUploads') is not None:
            temp_model = QueryTradeMarkApplicationDetailResponseBodyAdminUploads()
            self.admin_uploads = temp_model.from_map(m['AdminUploads'])
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ExtendInfo') is not None:
            self.extend_info = m.get('ExtendInfo')
        if m.get('FirstClassification') is not None:
            temp_model = QueryTradeMarkApplicationDetailResponseBodyFirstClassification()
            self.first_classification = temp_model.from_map(m['FirstClassification'])
        if m.get('Flags') is not None:
            temp_model = QueryTradeMarkApplicationDetailResponseBodyFlags()
            self.flags = temp_model.from_map(m['Flags'])
        if m.get('GrayIconUrl') is not None:
            self.gray_icon_url = m.get('GrayIconUrl')
        if m.get('JudgeResultUrl') is not None:
            temp_model = QueryTradeMarkApplicationDetailResponseBodyJudgeResultUrl()
            self.judge_result_url = temp_model.from_map(m['JudgeResultUrl'])
        if m.get('LegalNoticeUrl') is not None:
            self.legal_notice_url = m.get('LegalNoticeUrl')
        if m.get('LoaUrl') is not None:
            self.loa_url = m.get('LoaUrl')
        if m.get('LogisticsCertificateUrl') is not None:
            self.logistics_certificate_url = m.get('LogisticsCertificateUrl')
        if m.get('LogisticsNo') is not None:
            self.logistics_no = m.get('LogisticsNo')
        if m.get('MaterialDetail') is not None:
            temp_model = QueryTradeMarkApplicationDetailResponseBodyMaterialDetail()
            self.material_detail = temp_model.from_map(m['MaterialDetail'])
        if m.get('MaterialId') is not None:
            self.material_id = m.get('MaterialId')
        if m.get('NotAcceptUrl') is not None:
            self.not_accept_url = m.get('NotAcceptUrl')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('OrderPrice') is not None:
            self.order_price = m.get('OrderPrice')
        if m.get('PartnerCode') is not None:
            self.partner_code = m.get('PartnerCode')
        if m.get('PartnerMobile') is not None:
            self.partner_mobile = m.get('PartnerMobile')
        if m.get('PartnerName') is not None:
            self.partner_name = m.get('PartnerName')
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')
        if m.get('ReceiptUrl') is not None:
            temp_model = QueryTradeMarkApplicationDetailResponseBodyReceiptUrl()
            self.receipt_url = temp_model.from_map(m['ReceiptUrl'])
        if m.get('RecvUserLogistics') is not None:
            self.recv_user_logistics = m.get('RecvUserLogistics')
        if m.get('RenewResponse') is not None:
            temp_model = QueryTradeMarkApplicationDetailResponseBodyRenewResponse()
            self.renew_response = temp_model.from_map(m['RenewResponse'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ReviewOfficialFiles') is not None:
            temp_model = QueryTradeMarkApplicationDetailResponseBodyReviewOfficialFiles()
            self.review_official_files = temp_model.from_map(m['ReviewOfficialFiles'])
        if m.get('SendSbjLogistics') is not None:
            self.send_sbj_logistics = m.get('SendSbjLogistics')
        if m.get('SendTime') is not None:
            self.send_time = m.get('SendTime')
        if m.get('SendUserLogistics') is not None:
            self.send_user_logistics = m.get('SendUserLogistics')
        if m.get('ServicePrice') is not None:
            self.service_price = m.get('ServicePrice')
        if m.get('Specification') is not None:
            self.specification = m.get('Specification')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubmitAuditTime') is not None:
            self.submit_audit_time = m.get('SubmitAuditTime')
        if m.get('SubmitTime') is not None:
            self.submit_time = m.get('SubmitTime')
        if m.get('Supplements') is not None:
            temp_model = QueryTradeMarkApplicationDetailResponseBodySupplements()
            self.supplements = temp_model.from_map(m['Supplements'])
        if m.get('SystemVersion') is not None:
            self.system_version = m.get('SystemVersion')
        if m.get('ThirdClassification') is not None:
            temp_model = QueryTradeMarkApplicationDetailResponseBodyThirdClassification()
            self.third_classification = temp_model.from_map(m['ThirdClassification'])
        if m.get('TmIcon') is not None:
            self.tm_icon = m.get('TmIcon')
        if m.get('TmName') is not None:
            self.tm_name = m.get('TmName')
        if m.get('TmNameType') is not None:
            self.tm_name_type = m.get('TmNameType')
        if m.get('TmNumber') is not None:
            self.tm_number = m.get('TmNumber')
        if m.get('TotalPrice') is not None:
            self.total_price = m.get('TotalPrice')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class QueryTradeMarkApplicationDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryTradeMarkApplicationDetailResponseBody = None,
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
            temp_model = QueryTradeMarkApplicationDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTradeMarkApplicationLogsRequest(TeaModel):
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


class QueryTradeMarkApplicationLogsResponseBodyDataData(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        biz_status: int = None,
        extend_content: str = None,
        note: str = None,
        operate_time: int = None,
        operate_type: int = None,
        to_biz_status: int = None,
    ):
        self.biz_id = biz_id
        self.biz_status = biz_status
        self.extend_content = extend_content
        self.note = note
        self.operate_time = operate_time
        self.operate_type = operate_type
        self.to_biz_status = to_biz_status

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
        if self.extend_content is not None:
            result['ExtendContent'] = self.extend_content
        if self.note is not None:
            result['Note'] = self.note
        if self.operate_time is not None:
            result['OperateTime'] = self.operate_time
        if self.operate_type is not None:
            result['OperateType'] = self.operate_type
        if self.to_biz_status is not None:
            result['ToBizStatus'] = self.to_biz_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BizStatus') is not None:
            self.biz_status = m.get('BizStatus')
        if m.get('ExtendContent') is not None:
            self.extend_content = m.get('ExtendContent')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        if m.get('OperateTime') is not None:
            self.operate_time = m.get('OperateTime')
        if m.get('OperateType') is not None:
            self.operate_type = m.get('OperateType')
        if m.get('ToBizStatus') is not None:
            self.to_biz_status = m.get('ToBizStatus')
        return self


class QueryTradeMarkApplicationLogsResponseBodyData(TeaModel):
    def __init__(
        self,
        data: List[QueryTradeMarkApplicationLogsResponseBodyDataData] = None,
    ):
        self.data = data

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = QueryTradeMarkApplicationLogsResponseBodyDataData()
                self.data.append(temp_model.from_map(k))
        return self


class QueryTradeMarkApplicationLogsResponseBody(TeaModel):
    def __init__(
        self,
        data: QueryTradeMarkApplicationLogsResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = QueryTradeMarkApplicationLogsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryTradeMarkApplicationLogsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryTradeMarkApplicationLogsResponseBody = None,
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
            temp_model = QueryTradeMarkApplicationLogsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTradeMarkApplicationsRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        classification_code: str = None,
        hidden: int = None,
        intention_biz_id: str = None,
        logistics_no: str = None,
        material_name: str = None,
        order_id: str = None,
        page_num: int = None,
        page_size: int = None,
        product_type: int = None,
        sort_filed: str = None,
        sort_order: str = None,
        specification: int = None,
        status: int = None,
        status_list: List[int] = None,
        supplement_status: int = None,
        tm_name: str = None,
        tm_number: str = None,
        type: str = None,
    ):
        self.biz_id = biz_id
        self.classification_code = classification_code
        self.hidden = hidden
        self.intention_biz_id = intention_biz_id
        self.logistics_no = logistics_no
        self.material_name = material_name
        self.order_id = order_id
        self.page_num = page_num
        self.page_size = page_size
        self.product_type = product_type
        self.sort_filed = sort_filed
        self.sort_order = sort_order
        self.specification = specification
        self.status = status
        self.status_list = status_list
        self.supplement_status = supplement_status
        self.tm_name = tm_name
        self.tm_number = tm_number
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.classification_code is not None:
            result['ClassificationCode'] = self.classification_code
        if self.hidden is not None:
            result['Hidden'] = self.hidden
        if self.intention_biz_id is not None:
            result['IntentionBizId'] = self.intention_biz_id
        if self.logistics_no is not None:
            result['LogisticsNo'] = self.logistics_no
        if self.material_name is not None:
            result['MaterialName'] = self.material_name
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.sort_filed is not None:
            result['SortFiled'] = self.sort_filed
        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order
        if self.specification is not None:
            result['Specification'] = self.specification
        if self.status is not None:
            result['Status'] = self.status
        if self.status_list is not None:
            result['StatusList'] = self.status_list
        if self.supplement_status is not None:
            result['SupplementStatus'] = self.supplement_status
        if self.tm_name is not None:
            result['TmName'] = self.tm_name
        if self.tm_number is not None:
            result['TmNumber'] = self.tm_number
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('ClassificationCode') is not None:
            self.classification_code = m.get('ClassificationCode')
        if m.get('Hidden') is not None:
            self.hidden = m.get('Hidden')
        if m.get('IntentionBizId') is not None:
            self.intention_biz_id = m.get('IntentionBizId')
        if m.get('LogisticsNo') is not None:
            self.logistics_no = m.get('LogisticsNo')
        if m.get('MaterialName') is not None:
            self.material_name = m.get('MaterialName')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('SortFiled') is not None:
            self.sort_filed = m.get('SortFiled')
        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')
        if m.get('Specification') is not None:
            self.specification = m.get('Specification')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StatusList') is not None:
            self.status_list = m.get('StatusList')
        if m.get('SupplementStatus') is not None:
            self.supplement_status = m.get('SupplementStatus')
        if m.get('TmName') is not None:
            self.tm_name = m.get('TmName')
        if m.get('TmNumber') is not None:
            self.tm_number = m.get('TmNumber')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class QueryTradeMarkApplicationsShrinkRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        classification_code: str = None,
        hidden: int = None,
        intention_biz_id: str = None,
        logistics_no: str = None,
        material_name: str = None,
        order_id: str = None,
        page_num: int = None,
        page_size: int = None,
        product_type: int = None,
        sort_filed: str = None,
        sort_order: str = None,
        specification: int = None,
        status: int = None,
        status_list_shrink: str = None,
        supplement_status: int = None,
        tm_name: str = None,
        tm_number: str = None,
        type: str = None,
    ):
        self.biz_id = biz_id
        self.classification_code = classification_code
        self.hidden = hidden
        self.intention_biz_id = intention_biz_id
        self.logistics_no = logistics_no
        self.material_name = material_name
        self.order_id = order_id
        self.page_num = page_num
        self.page_size = page_size
        self.product_type = product_type
        self.sort_filed = sort_filed
        self.sort_order = sort_order
        self.specification = specification
        self.status = status
        self.status_list_shrink = status_list_shrink
        self.supplement_status = supplement_status
        self.tm_name = tm_name
        self.tm_number = tm_number
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.classification_code is not None:
            result['ClassificationCode'] = self.classification_code
        if self.hidden is not None:
            result['Hidden'] = self.hidden
        if self.intention_biz_id is not None:
            result['IntentionBizId'] = self.intention_biz_id
        if self.logistics_no is not None:
            result['LogisticsNo'] = self.logistics_no
        if self.material_name is not None:
            result['MaterialName'] = self.material_name
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.sort_filed is not None:
            result['SortFiled'] = self.sort_filed
        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order
        if self.specification is not None:
            result['Specification'] = self.specification
        if self.status is not None:
            result['Status'] = self.status
        if self.status_list_shrink is not None:
            result['StatusList'] = self.status_list_shrink
        if self.supplement_status is not None:
            result['SupplementStatus'] = self.supplement_status
        if self.tm_name is not None:
            result['TmName'] = self.tm_name
        if self.tm_number is not None:
            result['TmNumber'] = self.tm_number
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('ClassificationCode') is not None:
            self.classification_code = m.get('ClassificationCode')
        if m.get('Hidden') is not None:
            self.hidden = m.get('Hidden')
        if m.get('IntentionBizId') is not None:
            self.intention_biz_id = m.get('IntentionBizId')
        if m.get('LogisticsNo') is not None:
            self.logistics_no = m.get('LogisticsNo')
        if m.get('MaterialName') is not None:
            self.material_name = m.get('MaterialName')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('SortFiled') is not None:
            self.sort_filed = m.get('SortFiled')
        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')
        if m.get('Specification') is not None:
            self.specification = m.get('Specification')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StatusList') is not None:
            self.status_list_shrink = m.get('StatusList')
        if m.get('SupplementStatus') is not None:
            self.supplement_status = m.get('SupplementStatus')
        if m.get('TmName') is not None:
            self.tm_name = m.get('TmName')
        if m.get('TmNumber') is not None:
            self.tm_number = m.get('TmNumber')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class QueryTradeMarkApplicationsResponseBodyDataTmProducesFirstClassification(TeaModel):
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


class QueryTradeMarkApplicationsResponseBodyDataTmProducesFlags(TeaModel):
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


class QueryTradeMarkApplicationsResponseBodyDataTmProducesRenewResponse(TeaModel):
    def __init__(
        self,
        address: str = None,
        eng_address: str = None,
        eng_name: str = None,
        name: str = None,
        register_time: int = None,
        submit_sbjtime: int = None,
    ):
        self.address = address
        self.eng_address = eng_address
        self.eng_name = eng_name
        self.name = name
        self.register_time = register_time
        self.submit_sbjtime = submit_sbjtime

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.eng_address is not None:
            result['EngAddress'] = self.eng_address
        if self.eng_name is not None:
            result['EngName'] = self.eng_name
        if self.name is not None:
            result['Name'] = self.name
        if self.register_time is not None:
            result['RegisterTime'] = self.register_time
        if self.submit_sbjtime is not None:
            result['SubmitSbjtime'] = self.submit_sbjtime
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('EngAddress') is not None:
            self.eng_address = m.get('EngAddress')
        if m.get('EngName') is not None:
            self.eng_name = m.get('EngName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegisterTime') is not None:
            self.register_time = m.get('RegisterTime')
        if m.get('SubmitSbjtime') is not None:
            self.submit_sbjtime = m.get('SubmitSbjtime')
        return self


class QueryTradeMarkApplicationsResponseBodyDataTmProducesThirdClassificationThirdClassifications(TeaModel):
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


class QueryTradeMarkApplicationsResponseBodyDataTmProducesThirdClassification(TeaModel):
    def __init__(
        self,
        third_classifications: List[QueryTradeMarkApplicationsResponseBodyDataTmProducesThirdClassificationThirdClassifications] = None,
    ):
        self.third_classifications = third_classifications

    def validate(self):
        if self.third_classifications:
            for k in self.third_classifications:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ThirdClassifications'] = []
        if self.third_classifications is not None:
            for k in self.third_classifications:
                result['ThirdClassifications'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.third_classifications = []
        if m.get('ThirdClassifications') is not None:
            for k in m.get('ThirdClassifications'):
                temp_model = QueryTradeMarkApplicationsResponseBodyDataTmProducesThirdClassificationThirdClassifications()
                self.third_classifications.append(temp_model.from_map(k))
        return self


class QueryTradeMarkApplicationsResponseBodyDataTmProduces(TeaModel):
    def __init__(
        self,
        agreement_id: str = None,
        biz_id: str = None,
        create_time: int = None,
        first_classification: QueryTradeMarkApplicationsResponseBodyDataTmProducesFirstClassification = None,
        flags: QueryTradeMarkApplicationsResponseBodyDataTmProducesFlags = None,
        loa_url: str = None,
        material_id: int = None,
        material_name: str = None,
        note: str = None,
        order_id: str = None,
        order_price: float = None,
        principal_name: int = None,
        remark: str = None,
        renew_response: QueryTradeMarkApplicationsResponseBodyDataTmProducesRenewResponse = None,
        service_price: float = None,
        show_go_to_defend_button: bool = None,
        specification: int = None,
        status: int = None,
        submit_audit_time: int = None,
        submit_time: int = None,
        supplement_id: int = None,
        supplement_status: int = None,
        system_version: str = None,
        third_classification: QueryTradeMarkApplicationsResponseBodyDataTmProducesThirdClassification = None,
        tm_icon: str = None,
        tm_name: str = None,
        tm_number: str = None,
        total_price: float = None,
        type: int = None,
        update_time: int = None,
        user_id: str = None,
    ):
        self.agreement_id = agreement_id
        self.biz_id = biz_id
        self.create_time = create_time
        self.first_classification = first_classification
        self.flags = flags
        self.loa_url = loa_url
        self.material_id = material_id
        self.material_name = material_name
        self.note = note
        self.order_id = order_id
        self.order_price = order_price
        self.principal_name = principal_name
        self.remark = remark
        self.renew_response = renew_response
        self.service_price = service_price
        self.show_go_to_defend_button = show_go_to_defend_button
        self.specification = specification
        self.status = status
        self.submit_audit_time = submit_audit_time
        self.submit_time = submit_time
        self.supplement_id = supplement_id
        self.supplement_status = supplement_status
        self.system_version = system_version
        self.third_classification = third_classification
        self.tm_icon = tm_icon
        self.tm_name = tm_name
        self.tm_number = tm_number
        self.total_price = total_price
        self.type = type
        self.update_time = update_time
        self.user_id = user_id

    def validate(self):
        if self.first_classification:
            self.first_classification.validate()
        if self.flags:
            self.flags.validate()
        if self.renew_response:
            self.renew_response.validate()
        if self.third_classification:
            self.third_classification.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agreement_id is not None:
            result['AgreementId'] = self.agreement_id
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.first_classification is not None:
            result['FirstClassification'] = self.first_classification.to_map()
        if self.flags is not None:
            result['Flags'] = self.flags.to_map()
        if self.loa_url is not None:
            result['LoaUrl'] = self.loa_url
        if self.material_id is not None:
            result['MaterialId'] = self.material_id
        if self.material_name is not None:
            result['MaterialName'] = self.material_name
        if self.note is not None:
            result['Note'] = self.note
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.order_price is not None:
            result['OrderPrice'] = self.order_price
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.renew_response is not None:
            result['RenewResponse'] = self.renew_response.to_map()
        if self.service_price is not None:
            result['ServicePrice'] = self.service_price
        if self.show_go_to_defend_button is not None:
            result['ShowGoToDefendButton'] = self.show_go_to_defend_button
        if self.specification is not None:
            result['Specification'] = self.specification
        if self.status is not None:
            result['Status'] = self.status
        if self.submit_audit_time is not None:
            result['SubmitAuditTime'] = self.submit_audit_time
        if self.submit_time is not None:
            result['SubmitTime'] = self.submit_time
        if self.supplement_id is not None:
            result['SupplementId'] = self.supplement_id
        if self.supplement_status is not None:
            result['SupplementStatus'] = self.supplement_status
        if self.system_version is not None:
            result['SystemVersion'] = self.system_version
        if self.third_classification is not None:
            result['ThirdClassification'] = self.third_classification.to_map()
        if self.tm_icon is not None:
            result['TmIcon'] = self.tm_icon
        if self.tm_name is not None:
            result['TmName'] = self.tm_name
        if self.tm_number is not None:
            result['TmNumber'] = self.tm_number
        if self.total_price is not None:
            result['TotalPrice'] = self.total_price
        if self.type is not None:
            result['Type'] = self.type
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgreementId') is not None:
            self.agreement_id = m.get('AgreementId')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('FirstClassification') is not None:
            temp_model = QueryTradeMarkApplicationsResponseBodyDataTmProducesFirstClassification()
            self.first_classification = temp_model.from_map(m['FirstClassification'])
        if m.get('Flags') is not None:
            temp_model = QueryTradeMarkApplicationsResponseBodyDataTmProducesFlags()
            self.flags = temp_model.from_map(m['Flags'])
        if m.get('LoaUrl') is not None:
            self.loa_url = m.get('LoaUrl')
        if m.get('MaterialId') is not None:
            self.material_id = m.get('MaterialId')
        if m.get('MaterialName') is not None:
            self.material_name = m.get('MaterialName')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('OrderPrice') is not None:
            self.order_price = m.get('OrderPrice')
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('RenewResponse') is not None:
            temp_model = QueryTradeMarkApplicationsResponseBodyDataTmProducesRenewResponse()
            self.renew_response = temp_model.from_map(m['RenewResponse'])
        if m.get('ServicePrice') is not None:
            self.service_price = m.get('ServicePrice')
        if m.get('ShowGoToDefendButton') is not None:
            self.show_go_to_defend_button = m.get('ShowGoToDefendButton')
        if m.get('Specification') is not None:
            self.specification = m.get('Specification')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubmitAuditTime') is not None:
            self.submit_audit_time = m.get('SubmitAuditTime')
        if m.get('SubmitTime') is not None:
            self.submit_time = m.get('SubmitTime')
        if m.get('SupplementId') is not None:
            self.supplement_id = m.get('SupplementId')
        if m.get('SupplementStatus') is not None:
            self.supplement_status = m.get('SupplementStatus')
        if m.get('SystemVersion') is not None:
            self.system_version = m.get('SystemVersion')
        if m.get('ThirdClassification') is not None:
            temp_model = QueryTradeMarkApplicationsResponseBodyDataTmProducesThirdClassification()
            self.third_classification = temp_model.from_map(m['ThirdClassification'])
        if m.get('TmIcon') is not None:
            self.tm_icon = m.get('TmIcon')
        if m.get('TmName') is not None:
            self.tm_name = m.get('TmName')
        if m.get('TmNumber') is not None:
            self.tm_number = m.get('TmNumber')
        if m.get('TotalPrice') is not None:
            self.total_price = m.get('TotalPrice')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class QueryTradeMarkApplicationsResponseBodyData(TeaModel):
    def __init__(
        self,
        tm_produces: List[QueryTradeMarkApplicationsResponseBodyDataTmProduces] = None,
    ):
        self.tm_produces = tm_produces

    def validate(self):
        if self.tm_produces:
            for k in self.tm_produces:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TmProduces'] = []
        if self.tm_produces is not None:
            for k in self.tm_produces:
                result['TmProduces'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tm_produces = []
        if m.get('TmProduces') is not None:
            for k in m.get('TmProduces'):
                temp_model = QueryTradeMarkApplicationsResponseBodyDataTmProduces()
                self.tm_produces.append(temp_model.from_map(k))
        return self


class QueryTradeMarkApplicationsResponseBody(TeaModel):
    def __init__(
        self,
        current_page_num: int = None,
        data: QueryTradeMarkApplicationsResponseBodyData = None,
        page_size: int = None,
        request_id: str = None,
        total_item_num: int = None,
        total_page_num: int = None,
    ):
        self.current_page_num = current_page_num
        self.data = data
        self.page_size = page_size
        self.request_id = request_id
        self.total_item_num = total_item_num
        self.total_page_num = total_page_num

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page_num is not None:
            result['CurrentPageNum'] = self.current_page_num
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_item_num is not None:
            result['TotalItemNum'] = self.total_item_num
        if self.total_page_num is not None:
            result['TotalPageNum'] = self.total_page_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPageNum') is not None:
            self.current_page_num = m.get('CurrentPageNum')
        if m.get('Data') is not None:
            temp_model = QueryTradeMarkApplicationsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalItemNum') is not None:
            self.total_item_num = m.get('TotalItemNum')
        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')
        return self


class QueryTradeMarkApplicationsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryTradeMarkApplicationsResponseBody = None,
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
            temp_model = QueryTradeMarkApplicationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTradeMarkApplicationsByIntentionRequest(TeaModel):
    def __init__(
        self,
        channel: str = None,
        intention_biz_id: str = None,
        page_num: int = None,
        page_size: int = None,
        tm_produce_status: str = None,
    ):
        self.channel = channel
        self.intention_biz_id = intention_biz_id
        self.page_num = page_num
        self.page_size = page_size
        self.tm_produce_status = tm_produce_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel is not None:
            result['Channel'] = self.channel
        if self.intention_biz_id is not None:
            result['IntentionBizId'] = self.intention_biz_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.tm_produce_status is not None:
            result['TmProduceStatus'] = self.tm_produce_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Channel') is not None:
            self.channel = m.get('Channel')
        if m.get('IntentionBizId') is not None:
            self.intention_biz_id = m.get('IntentionBizId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TmProduceStatus') is not None:
            self.tm_produce_status = m.get('TmProduceStatus')
        return self


class QueryTradeMarkApplicationsByIntentionResponseBodyDataTmProducesFirstClassification(TeaModel):
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


class QueryTradeMarkApplicationsByIntentionResponseBodyDataTmProducesThirdClassificationThirdClassifications(TeaModel):
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


class QueryTradeMarkApplicationsByIntentionResponseBodyDataTmProducesThirdClassification(TeaModel):
    def __init__(
        self,
        third_classifications: List[QueryTradeMarkApplicationsByIntentionResponseBodyDataTmProducesThirdClassificationThirdClassifications] = None,
    ):
        self.third_classifications = third_classifications

    def validate(self):
        if self.third_classifications:
            for k in self.third_classifications:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ThirdClassifications'] = []
        if self.third_classifications is not None:
            for k in self.third_classifications:
                result['ThirdClassifications'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.third_classifications = []
        if m.get('ThirdClassifications') is not None:
            for k in m.get('ThirdClassifications'):
                temp_model = QueryTradeMarkApplicationsByIntentionResponseBodyDataTmProducesThirdClassificationThirdClassifications()
                self.third_classifications.append(temp_model.from_map(k))
        return self


class QueryTradeMarkApplicationsByIntentionResponseBodyDataTmProduces(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        create_time: int = None,
        first_classification: QueryTradeMarkApplicationsByIntentionResponseBodyDataTmProducesFirstClassification = None,
        loa_url: str = None,
        material_id: str = None,
        material_name: str = None,
        note: str = None,
        order_price: float = None,
        principal_description: str = None,
        principal_value: int = None,
        service_price: float = None,
        status: int = None,
        supplement_id: int = None,
        supplement_status: int = None,
        third_classification: QueryTradeMarkApplicationsByIntentionResponseBodyDataTmProducesThirdClassification = None,
        tm_icon: str = None,
        tm_name: str = None,
        tm_number: str = None,
        total_price: float = None,
        type: int = None,
        update_time: int = None,
    ):
        self.biz_id = biz_id
        self.create_time = create_time
        self.first_classification = first_classification
        self.loa_url = loa_url
        self.material_id = material_id
        self.material_name = material_name
        self.note = note
        self.order_price = order_price
        self.principal_description = principal_description
        self.principal_value = principal_value
        self.service_price = service_price
        self.status = status
        self.supplement_id = supplement_id
        self.supplement_status = supplement_status
        self.third_classification = third_classification
        self.tm_icon = tm_icon
        self.tm_name = tm_name
        self.tm_number = tm_number
        self.total_price = total_price
        self.type = type
        self.update_time = update_time

    def validate(self):
        if self.first_classification:
            self.first_classification.validate()
        if self.third_classification:
            self.third_classification.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.first_classification is not None:
            result['FirstClassification'] = self.first_classification.to_map()
        if self.loa_url is not None:
            result['LoaUrl'] = self.loa_url
        if self.material_id is not None:
            result['MaterialId'] = self.material_id
        if self.material_name is not None:
            result['MaterialName'] = self.material_name
        if self.note is not None:
            result['Note'] = self.note
        if self.order_price is not None:
            result['OrderPrice'] = self.order_price
        if self.principal_description is not None:
            result['PrincipalDescription'] = self.principal_description
        if self.principal_value is not None:
            result['PrincipalValue'] = self.principal_value
        if self.service_price is not None:
            result['ServicePrice'] = self.service_price
        if self.status is not None:
            result['Status'] = self.status
        if self.supplement_id is not None:
            result['SupplementId'] = self.supplement_id
        if self.supplement_status is not None:
            result['SupplementStatus'] = self.supplement_status
        if self.third_classification is not None:
            result['ThirdClassification'] = self.third_classification.to_map()
        if self.tm_icon is not None:
            result['TmIcon'] = self.tm_icon
        if self.tm_name is not None:
            result['TmName'] = self.tm_name
        if self.tm_number is not None:
            result['TmNumber'] = self.tm_number
        if self.total_price is not None:
            result['TotalPrice'] = self.total_price
        if self.type is not None:
            result['Type'] = self.type
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('FirstClassification') is not None:
            temp_model = QueryTradeMarkApplicationsByIntentionResponseBodyDataTmProducesFirstClassification()
            self.first_classification = temp_model.from_map(m['FirstClassification'])
        if m.get('LoaUrl') is not None:
            self.loa_url = m.get('LoaUrl')
        if m.get('MaterialId') is not None:
            self.material_id = m.get('MaterialId')
        if m.get('MaterialName') is not None:
            self.material_name = m.get('MaterialName')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        if m.get('OrderPrice') is not None:
            self.order_price = m.get('OrderPrice')
        if m.get('PrincipalDescription') is not None:
            self.principal_description = m.get('PrincipalDescription')
        if m.get('PrincipalValue') is not None:
            self.principal_value = m.get('PrincipalValue')
        if m.get('ServicePrice') is not None:
            self.service_price = m.get('ServicePrice')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SupplementId') is not None:
            self.supplement_id = m.get('SupplementId')
        if m.get('SupplementStatus') is not None:
            self.supplement_status = m.get('SupplementStatus')
        if m.get('ThirdClassification') is not None:
            temp_model = QueryTradeMarkApplicationsByIntentionResponseBodyDataTmProducesThirdClassification()
            self.third_classification = temp_model.from_map(m['ThirdClassification'])
        if m.get('TmIcon') is not None:
            self.tm_icon = m.get('TmIcon')
        if m.get('TmName') is not None:
            self.tm_name = m.get('TmName')
        if m.get('TmNumber') is not None:
            self.tm_number = m.get('TmNumber')
        if m.get('TotalPrice') is not None:
            self.total_price = m.get('TotalPrice')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class QueryTradeMarkApplicationsByIntentionResponseBodyData(TeaModel):
    def __init__(
        self,
        tm_produces: List[QueryTradeMarkApplicationsByIntentionResponseBodyDataTmProduces] = None,
    ):
        self.tm_produces = tm_produces

    def validate(self):
        if self.tm_produces:
            for k in self.tm_produces:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TmProduces'] = []
        if self.tm_produces is not None:
            for k in self.tm_produces:
                result['TmProduces'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tm_produces = []
        if m.get('TmProduces') is not None:
            for k in m.get('TmProduces'):
                temp_model = QueryTradeMarkApplicationsByIntentionResponseBodyDataTmProduces()
                self.tm_produces.append(temp_model.from_map(k))
        return self


class QueryTradeMarkApplicationsByIntentionResponseBody(TeaModel):
    def __init__(
        self,
        current_page_num: int = None,
        data: QueryTradeMarkApplicationsByIntentionResponseBodyData = None,
        page_size: int = None,
        request_id: str = None,
        total_item_num: int = None,
        total_page_num: int = None,
    ):
        self.current_page_num = current_page_num
        self.data = data
        self.page_size = page_size
        self.request_id = request_id
        self.total_item_num = total_item_num
        self.total_page_num = total_page_num

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page_num is not None:
            result['CurrentPageNum'] = self.current_page_num
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_item_num is not None:
            result['TotalItemNum'] = self.total_item_num
        if self.total_page_num is not None:
            result['TotalPageNum'] = self.total_page_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPageNum') is not None:
            self.current_page_num = m.get('CurrentPageNum')
        if m.get('Data') is not None:
            temp_model = QueryTradeMarkApplicationsByIntentionResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalItemNum') is not None:
            self.total_item_num = m.get('TotalItemNum')
        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')
        return self


class QueryTradeMarkApplicationsByIntentionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryTradeMarkApplicationsByIntentionResponseBody = None,
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
            temp_model = QueryTradeMarkApplicationsByIntentionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTradeProduceDetailRequest(TeaModel):
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


class QueryTradeProduceDetailResponseBodyData(TeaModel):
    def __init__(
        self,
        allow_cancel: bool = None,
        biz_id: str = None,
        buyer_status: int = None,
        classification: str = None,
        confiscate_amount: float = None,
        create_time: int = None,
        exclusive_date_limit: str = None,
        extend: Dict[str, Any] = None,
        final_amount: float = None,
        icon: str = None,
        operate_note: str = None,
        paid_amount: float = None,
        pre_amount: float = None,
        pre_order_id: str = None,
        refund_amount: float = None,
        register_number: str = None,
        share: str = None,
        source: int = None,
        third_code: str = None,
        tm_name: str = None,
        update_time: int = None,
        user_id: str = None,
    ):
        self.allow_cancel = allow_cancel
        self.biz_id = biz_id
        self.buyer_status = buyer_status
        self.classification = classification
        self.confiscate_amount = confiscate_amount
        self.create_time = create_time
        self.exclusive_date_limit = exclusive_date_limit
        self.extend = extend
        self.final_amount = final_amount
        self.icon = icon
        self.operate_note = operate_note
        self.paid_amount = paid_amount
        self.pre_amount = pre_amount
        self.pre_order_id = pre_order_id
        self.refund_amount = refund_amount
        self.register_number = register_number
        self.share = share
        self.source = source
        self.third_code = third_code
        self.tm_name = tm_name
        self.update_time = update_time
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_cancel is not None:
            result['AllowCancel'] = self.allow_cancel
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.buyer_status is not None:
            result['BuyerStatus'] = self.buyer_status
        if self.classification is not None:
            result['Classification'] = self.classification
        if self.confiscate_amount is not None:
            result['ConfiscateAmount'] = self.confiscate_amount
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.exclusive_date_limit is not None:
            result['ExclusiveDateLimit'] = self.exclusive_date_limit
        if self.extend is not None:
            result['Extend'] = self.extend
        if self.final_amount is not None:
            result['FinalAmount'] = self.final_amount
        if self.icon is not None:
            result['Icon'] = self.icon
        if self.operate_note is not None:
            result['OperateNote'] = self.operate_note
        if self.paid_amount is not None:
            result['PaidAmount'] = self.paid_amount
        if self.pre_amount is not None:
            result['PreAmount'] = self.pre_amount
        if self.pre_order_id is not None:
            result['PreOrderId'] = self.pre_order_id
        if self.refund_amount is not None:
            result['RefundAmount'] = self.refund_amount
        if self.register_number is not None:
            result['RegisterNumber'] = self.register_number
        if self.share is not None:
            result['Share'] = self.share
        if self.source is not None:
            result['Source'] = self.source
        if self.third_code is not None:
            result['ThirdCode'] = self.third_code
        if self.tm_name is not None:
            result['TmName'] = self.tm_name
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowCancel') is not None:
            self.allow_cancel = m.get('AllowCancel')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BuyerStatus') is not None:
            self.buyer_status = m.get('BuyerStatus')
        if m.get('Classification') is not None:
            self.classification = m.get('Classification')
        if m.get('ConfiscateAmount') is not None:
            self.confiscate_amount = m.get('ConfiscateAmount')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ExclusiveDateLimit') is not None:
            self.exclusive_date_limit = m.get('ExclusiveDateLimit')
        if m.get('Extend') is not None:
            self.extend = m.get('Extend')
        if m.get('FinalAmount') is not None:
            self.final_amount = m.get('FinalAmount')
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        if m.get('OperateNote') is not None:
            self.operate_note = m.get('OperateNote')
        if m.get('PaidAmount') is not None:
            self.paid_amount = m.get('PaidAmount')
        if m.get('PreAmount') is not None:
            self.pre_amount = m.get('PreAmount')
        if m.get('PreOrderId') is not None:
            self.pre_order_id = m.get('PreOrderId')
        if m.get('RefundAmount') is not None:
            self.refund_amount = m.get('RefundAmount')
        if m.get('RegisterNumber') is not None:
            self.register_number = m.get('RegisterNumber')
        if m.get('Share') is not None:
            self.share = m.get('Share')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('ThirdCode') is not None:
            self.third_code = m.get('ThirdCode')
        if m.get('TmName') is not None:
            self.tm_name = m.get('TmName')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class QueryTradeProduceDetailResponseBody(TeaModel):
    def __init__(
        self,
        data: QueryTradeProduceDetailResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = QueryTradeProduceDetailResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryTradeProduceDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryTradeProduceDetailResponseBody = None,
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
            temp_model = QueryTradeProduceDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTradeProduceListRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        buyer_status: int = None,
        page_num: int = None,
        page_size: int = None,
        pre_order_id: str = None,
        register_number: str = None,
        sort_filed: str = None,
        sort_order: str = None,
    ):
        self.biz_id = biz_id
        self.buyer_status = buyer_status
        self.page_num = page_num
        self.page_size = page_size
        self.pre_order_id = pre_order_id
        self.register_number = register_number
        self.sort_filed = sort_filed
        self.sort_order = sort_order

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.buyer_status is not None:
            result['BuyerStatus'] = self.buyer_status
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.pre_order_id is not None:
            result['PreOrderId'] = self.pre_order_id
        if self.register_number is not None:
            result['RegisterNumber'] = self.register_number
        if self.sort_filed is not None:
            result['SortFiled'] = self.sort_filed
        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BuyerStatus') is not None:
            self.buyer_status = m.get('BuyerStatus')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PreOrderId') is not None:
            self.pre_order_id = m.get('PreOrderId')
        if m.get('RegisterNumber') is not None:
            self.register_number = m.get('RegisterNumber')
        if m.get('SortFiled') is not None:
            self.sort_filed = m.get('SortFiled')
        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')
        return self


class QueryTradeProduceListResponseBodyDataTradeProduces(TeaModel):
    def __init__(
        self,
        allow_cancel: bool = None,
        biz_id: str = None,
        buyer_status: int = None,
        classification: str = None,
        create_time: int = None,
        fail_reason: int = None,
        final_amount: float = None,
        icon: str = None,
        operate_note: str = None,
        pre_amount: float = None,
        pre_order_id: str = None,
        register_number: str = None,
        source: int = None,
        update_time: int = None,
        user_id: str = None,
    ):
        self.allow_cancel = allow_cancel
        self.biz_id = biz_id
        self.buyer_status = buyer_status
        self.classification = classification
        self.create_time = create_time
        self.fail_reason = fail_reason
        self.final_amount = final_amount
        self.icon = icon
        self.operate_note = operate_note
        self.pre_amount = pre_amount
        self.pre_order_id = pre_order_id
        self.register_number = register_number
        self.source = source
        self.update_time = update_time
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_cancel is not None:
            result['AllowCancel'] = self.allow_cancel
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.buyer_status is not None:
            result['BuyerStatus'] = self.buyer_status
        if self.classification is not None:
            result['Classification'] = self.classification
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.fail_reason is not None:
            result['FailReason'] = self.fail_reason
        if self.final_amount is not None:
            result['FinalAmount'] = self.final_amount
        if self.icon is not None:
            result['Icon'] = self.icon
        if self.operate_note is not None:
            result['OperateNote'] = self.operate_note
        if self.pre_amount is not None:
            result['PreAmount'] = self.pre_amount
        if self.pre_order_id is not None:
            result['PreOrderId'] = self.pre_order_id
        if self.register_number is not None:
            result['RegisterNumber'] = self.register_number
        if self.source is not None:
            result['Source'] = self.source
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowCancel') is not None:
            self.allow_cancel = m.get('AllowCancel')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BuyerStatus') is not None:
            self.buyer_status = m.get('BuyerStatus')
        if m.get('Classification') is not None:
            self.classification = m.get('Classification')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('FailReason') is not None:
            self.fail_reason = m.get('FailReason')
        if m.get('FinalAmount') is not None:
            self.final_amount = m.get('FinalAmount')
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        if m.get('OperateNote') is not None:
            self.operate_note = m.get('OperateNote')
        if m.get('PreAmount') is not None:
            self.pre_amount = m.get('PreAmount')
        if m.get('PreOrderId') is not None:
            self.pre_order_id = m.get('PreOrderId')
        if m.get('RegisterNumber') is not None:
            self.register_number = m.get('RegisterNumber')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class QueryTradeProduceListResponseBodyData(TeaModel):
    def __init__(
        self,
        trade_produces: List[QueryTradeProduceListResponseBodyDataTradeProduces] = None,
    ):
        self.trade_produces = trade_produces

    def validate(self):
        if self.trade_produces:
            for k in self.trade_produces:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TradeProduces'] = []
        if self.trade_produces is not None:
            for k in self.trade_produces:
                result['TradeProduces'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.trade_produces = []
        if m.get('TradeProduces') is not None:
            for k in m.get('TradeProduces'):
                temp_model = QueryTradeProduceListResponseBodyDataTradeProduces()
                self.trade_produces.append(temp_model.from_map(k))
        return self


class QueryTradeProduceListResponseBody(TeaModel):
    def __init__(
        self,
        current_page_num: int = None,
        data: QueryTradeProduceListResponseBodyData = None,
        page_size: int = None,
        request_id: str = None,
        total_item_num: int = None,
        total_page_num: int = None,
    ):
        self.current_page_num = current_page_num
        self.data = data
        self.page_size = page_size
        self.request_id = request_id
        self.total_item_num = total_item_num
        self.total_page_num = total_page_num

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page_num is not None:
            result['CurrentPageNum'] = self.current_page_num
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_item_num is not None:
            result['TotalItemNum'] = self.total_item_num
        if self.total_page_num is not None:
            result['TotalPageNum'] = self.total_page_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPageNum') is not None:
            self.current_page_num = m.get('CurrentPageNum')
        if m.get('Data') is not None:
            temp_model = QueryTradeProduceListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalItemNum') is not None:
            self.total_item_num = m.get('TotalItemNum')
        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')
        return self


class QueryTradeProduceListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryTradeProduceListResponseBody = None,
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
            temp_model = QueryTradeProduceListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTrademarkDetailByApplyNumberRequest(TeaModel):
    def __init__(
        self,
        apply_number: str = None,
        env: str = None,
    ):
        self.apply_number = apply_number
        self.env = env

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apply_number is not None:
            result['ApplyNumber'] = self.apply_number
        if self.env is not None:
            result['Env'] = self.env
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplyNumber') is not None:
            self.apply_number = m.get('ApplyNumber')
        if m.get('Env') is not None:
            self.env = m.get('Env')
        return self


class QueryTrademarkDetailByApplyNumberResponseBodyMoudleLeafCodesLeafCode(TeaModel):
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


class QueryTrademarkDetailByApplyNumberResponseBodyMoudleLeafCodes(TeaModel):
    def __init__(
        self,
        leaf_code: List[QueryTrademarkDetailByApplyNumberResponseBodyMoudleLeafCodesLeafCode] = None,
    ):
        self.leaf_code = leaf_code

    def validate(self):
        if self.leaf_code:
            for k in self.leaf_code:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['leafCode'] = []
        if self.leaf_code is not None:
            for k in self.leaf_code:
                result['leafCode'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.leaf_code = []
        if m.get('leafCode') is not None:
            for k in m.get('leafCode'):
                temp_model = QueryTrademarkDetailByApplyNumberResponseBodyMoudleLeafCodesLeafCode()
                self.leaf_code.append(temp_model.from_map(k))
        return self


class QueryTrademarkDetailByApplyNumberResponseBodyMoudleMaterialInfo(TeaModel):
    def __init__(
        self,
        address: str = None,
        business_licence_url: str = None,
        card_number: str = None,
        cn_info_url: str = None,
        contact_address: str = None,
        contact_email: str = None,
        contact_name: str = None,
        contact_phone_number: str = None,
        contact_zip_code: str = None,
        country: str = None,
        eaddress: str = None,
        ename: str = None,
        id_card_number: str = None,
        id_card_url: str = None,
        loa_key: str = None,
        loa_url: str = None,
        name: str = None,
        passport_url: str = None,
        personal_type: int = None,
        post_code: str = None,
        province: str = None,
        reason_file_oss_key: str = None,
        region: int = None,
        review_file_map: Dict[str, Any] = None,
        type: int = None,
    ):
        self.address = address
        self.business_licence_url = business_licence_url
        self.card_number = card_number
        self.cn_info_url = cn_info_url
        self.contact_address = contact_address
        self.contact_email = contact_email
        self.contact_name = contact_name
        self.contact_phone_number = contact_phone_number
        self.contact_zip_code = contact_zip_code
        self.country = country
        self.eaddress = eaddress
        self.ename = ename
        self.id_card_number = id_card_number
        self.id_card_url = id_card_url
        self.loa_key = loa_key
        self.loa_url = loa_url
        self.name = name
        self.passport_url = passport_url
        self.personal_type = personal_type
        self.post_code = post_code
        self.province = province
        self.reason_file_oss_key = reason_file_oss_key
        self.region = region
        self.review_file_map = review_file_map
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
        if self.business_licence_url is not None:
            result['BusinessLicenceUrl'] = self.business_licence_url
        if self.card_number is not None:
            result['CardNumber'] = self.card_number
        if self.cn_info_url is not None:
            result['CnInfoUrl'] = self.cn_info_url
        if self.contact_address is not None:
            result['ContactAddress'] = self.contact_address
        if self.contact_email is not None:
            result['ContactEmail'] = self.contact_email
        if self.contact_name is not None:
            result['ContactName'] = self.contact_name
        if self.contact_phone_number is not None:
            result['ContactPhoneNumber'] = self.contact_phone_number
        if self.contact_zip_code is not None:
            result['ContactZipCode'] = self.contact_zip_code
        if self.country is not None:
            result['Country'] = self.country
        if self.eaddress is not None:
            result['EAddress'] = self.eaddress
        if self.ename is not None:
            result['EName'] = self.ename
        if self.id_card_number is not None:
            result['IdCardNumber'] = self.id_card_number
        if self.id_card_url is not None:
            result['IdCardUrl'] = self.id_card_url
        if self.loa_key is not None:
            result['LoaKey'] = self.loa_key
        if self.loa_url is not None:
            result['LoaUrl'] = self.loa_url
        if self.name is not None:
            result['Name'] = self.name
        if self.passport_url is not None:
            result['PassportUrl'] = self.passport_url
        if self.personal_type is not None:
            result['PersonalType'] = self.personal_type
        if self.post_code is not None:
            result['PostCode'] = self.post_code
        if self.province is not None:
            result['Province'] = self.province
        if self.reason_file_oss_key is not None:
            result['ReasonFileOssKey'] = self.reason_file_oss_key
        if self.region is not None:
            result['Region'] = self.region
        if self.review_file_map is not None:
            result['ReviewFileMap'] = self.review_file_map
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('BusinessLicenceUrl') is not None:
            self.business_licence_url = m.get('BusinessLicenceUrl')
        if m.get('CardNumber') is not None:
            self.card_number = m.get('CardNumber')
        if m.get('CnInfoUrl') is not None:
            self.cn_info_url = m.get('CnInfoUrl')
        if m.get('ContactAddress') is not None:
            self.contact_address = m.get('ContactAddress')
        if m.get('ContactEmail') is not None:
            self.contact_email = m.get('ContactEmail')
        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')
        if m.get('ContactPhoneNumber') is not None:
            self.contact_phone_number = m.get('ContactPhoneNumber')
        if m.get('ContactZipCode') is not None:
            self.contact_zip_code = m.get('ContactZipCode')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('EAddress') is not None:
            self.eaddress = m.get('EAddress')
        if m.get('EName') is not None:
            self.ename = m.get('EName')
        if m.get('IdCardNumber') is not None:
            self.id_card_number = m.get('IdCardNumber')
        if m.get('IdCardUrl') is not None:
            self.id_card_url = m.get('IdCardUrl')
        if m.get('LoaKey') is not None:
            self.loa_key = m.get('LoaKey')
        if m.get('LoaUrl') is not None:
            self.loa_url = m.get('LoaUrl')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PassportUrl') is not None:
            self.passport_url = m.get('PassportUrl')
        if m.get('PersonalType') is not None:
            self.personal_type = m.get('PersonalType')
        if m.get('PostCode') is not None:
            self.post_code = m.get('PostCode')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        if m.get('ReasonFileOssKey') is not None:
            self.reason_file_oss_key = m.get('ReasonFileOssKey')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ReviewFileMap') is not None:
            self.review_file_map = m.get('ReviewFileMap')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class QueryTrademarkDetailByApplyNumberResponseBodyMoudleRootCode(TeaModel):
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


class QueryTrademarkDetailByApplyNumberResponseBodyMoudle(TeaModel):
    def __init__(
        self,
        bit_flag: int = None,
        biz_id: str = None,
        biz_type: str = None,
        extend_info: Dict[str, Any] = None,
        gray_icon_url: str = None,
        icon: str = None,
        leaf_codes: QueryTrademarkDetailByApplyNumberResponseBodyMoudleLeafCodes = None,
        material_info: QueryTrademarkDetailByApplyNumberResponseBodyMoudleMaterialInfo = None,
        order_id: str = None,
        partner_code: str = None,
        principal_key: str = None,
        principal_name: str = None,
        produce_type: str = None,
        root_code: QueryTrademarkDetailByApplyNumberResponseBodyMoudleRootCode = None,
        status: str = None,
        status_str: str = None,
        submit_audit_time_str: str = None,
        submit_audit_time_value: int = None,
        submit_status: str = None,
        submit_time_str: str = None,
        submit_time_value: int = None,
        submit_times: int = None,
        trademark_name: str = None,
        trademark_name_type: int = None,
        trademark_number: str = None,
    ):
        self.bit_flag = bit_flag
        self.biz_id = biz_id
        self.biz_type = biz_type
        self.extend_info = extend_info
        self.gray_icon_url = gray_icon_url
        self.icon = icon
        self.leaf_codes = leaf_codes
        self.material_info = material_info
        self.order_id = order_id
        self.partner_code = partner_code
        self.principal_key = principal_key
        self.principal_name = principal_name
        self.produce_type = produce_type
        self.root_code = root_code
        self.status = status
        self.status_str = status_str
        self.submit_audit_time_str = submit_audit_time_str
        self.submit_audit_time_value = submit_audit_time_value
        self.submit_status = submit_status
        self.submit_time_str = submit_time_str
        self.submit_time_value = submit_time_value
        self.submit_times = submit_times
        self.trademark_name = trademark_name
        self.trademark_name_type = trademark_name_type
        self.trademark_number = trademark_number

    def validate(self):
        if self.leaf_codes:
            self.leaf_codes.validate()
        if self.material_info:
            self.material_info.validate()
        if self.root_code:
            self.root_code.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bit_flag is not None:
            result['BitFlag'] = self.bit_flag
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.extend_info is not None:
            result['ExtendInfo'] = self.extend_info
        if self.gray_icon_url is not None:
            result['GrayIconUrl'] = self.gray_icon_url
        if self.icon is not None:
            result['Icon'] = self.icon
        if self.leaf_codes is not None:
            result['LeafCodes'] = self.leaf_codes.to_map()
        if self.material_info is not None:
            result['MaterialInfo'] = self.material_info.to_map()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.partner_code is not None:
            result['PartnerCode'] = self.partner_code
        if self.principal_key is not None:
            result['PrincipalKey'] = self.principal_key
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name
        if self.produce_type is not None:
            result['ProduceType'] = self.produce_type
        if self.root_code is not None:
            result['RootCode'] = self.root_code.to_map()
        if self.status is not None:
            result['Status'] = self.status
        if self.status_str is not None:
            result['StatusStr'] = self.status_str
        if self.submit_audit_time_str is not None:
            result['SubmitAuditTimeStr'] = self.submit_audit_time_str
        if self.submit_audit_time_value is not None:
            result['SubmitAuditTimeValue'] = self.submit_audit_time_value
        if self.submit_status is not None:
            result['SubmitStatus'] = self.submit_status
        if self.submit_time_str is not None:
            result['SubmitTimeStr'] = self.submit_time_str
        if self.submit_time_value is not None:
            result['SubmitTimeValue'] = self.submit_time_value
        if self.submit_times is not None:
            result['SubmitTimes'] = self.submit_times
        if self.trademark_name is not None:
            result['TrademarkName'] = self.trademark_name
        if self.trademark_name_type is not None:
            result['TrademarkNameType'] = self.trademark_name_type
        if self.trademark_number is not None:
            result['TrademarkNumber'] = self.trademark_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BitFlag') is not None:
            self.bit_flag = m.get('BitFlag')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('ExtendInfo') is not None:
            self.extend_info = m.get('ExtendInfo')
        if m.get('GrayIconUrl') is not None:
            self.gray_icon_url = m.get('GrayIconUrl')
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        if m.get('LeafCodes') is not None:
            temp_model = QueryTrademarkDetailByApplyNumberResponseBodyMoudleLeafCodes()
            self.leaf_codes = temp_model.from_map(m['LeafCodes'])
        if m.get('MaterialInfo') is not None:
            temp_model = QueryTrademarkDetailByApplyNumberResponseBodyMoudleMaterialInfo()
            self.material_info = temp_model.from_map(m['MaterialInfo'])
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('PartnerCode') is not None:
            self.partner_code = m.get('PartnerCode')
        if m.get('PrincipalKey') is not None:
            self.principal_key = m.get('PrincipalKey')
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')
        if m.get('ProduceType') is not None:
            self.produce_type = m.get('ProduceType')
        if m.get('RootCode') is not None:
            temp_model = QueryTrademarkDetailByApplyNumberResponseBodyMoudleRootCode()
            self.root_code = temp_model.from_map(m['RootCode'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StatusStr') is not None:
            self.status_str = m.get('StatusStr')
        if m.get('SubmitAuditTimeStr') is not None:
            self.submit_audit_time_str = m.get('SubmitAuditTimeStr')
        if m.get('SubmitAuditTimeValue') is not None:
            self.submit_audit_time_value = m.get('SubmitAuditTimeValue')
        if m.get('SubmitStatus') is not None:
            self.submit_status = m.get('SubmitStatus')
        if m.get('SubmitTimeStr') is not None:
            self.submit_time_str = m.get('SubmitTimeStr')
        if m.get('SubmitTimeValue') is not None:
            self.submit_time_value = m.get('SubmitTimeValue')
        if m.get('SubmitTimes') is not None:
            self.submit_times = m.get('SubmitTimes')
        if m.get('TrademarkName') is not None:
            self.trademark_name = m.get('TrademarkName')
        if m.get('TrademarkNameType') is not None:
            self.trademark_name_type = m.get('TrademarkNameType')
        if m.get('TrademarkNumber') is not None:
            self.trademark_number = m.get('TrademarkNumber')
        return self


class QueryTrademarkDetailByApplyNumberResponseBody(TeaModel):
    def __init__(
        self,
        moudle: QueryTrademarkDetailByApplyNumberResponseBodyMoudle = None,
        request_id: str = None,
    ):
        self.moudle = moudle
        self.request_id = request_id

    def validate(self):
        if self.moudle:
            self.moudle.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.moudle is not None:
            result['Moudle'] = self.moudle.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Moudle') is not None:
            temp_model = QueryTrademarkDetailByApplyNumberResponseBodyMoudle()
            self.moudle = temp_model.from_map(m['Moudle'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryTrademarkDetailByApplyNumberResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryTrademarkDetailByApplyNumberResponseBody = None,
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
            temp_model = QueryTrademarkDetailByApplyNumberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTrademarkDetailByApplyNumberEspRequest(TeaModel):
    def __init__(
        self,
        apply_number: str = None,
        biz_type: str = None,
    ):
        self.apply_number = apply_number
        self.biz_type = biz_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apply_number is not None:
            result['ApplyNumber'] = self.apply_number
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplyNumber') is not None:
            self.apply_number = m.get('ApplyNumber')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        return self


class QueryTrademarkDetailByApplyNumberEspResponseBodyMoudleLeafCodesLeafCode(TeaModel):
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


class QueryTrademarkDetailByApplyNumberEspResponseBodyMoudleLeafCodes(TeaModel):
    def __init__(
        self,
        leaf_code: List[QueryTrademarkDetailByApplyNumberEspResponseBodyMoudleLeafCodesLeafCode] = None,
    ):
        self.leaf_code = leaf_code

    def validate(self):
        if self.leaf_code:
            for k in self.leaf_code:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['leafCode'] = []
        if self.leaf_code is not None:
            for k in self.leaf_code:
                result['leafCode'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.leaf_code = []
        if m.get('leafCode') is not None:
            for k in m.get('leafCode'):
                temp_model = QueryTrademarkDetailByApplyNumberEspResponseBodyMoudleLeafCodesLeafCode()
                self.leaf_code.append(temp_model.from_map(k))
        return self


class QueryTrademarkDetailByApplyNumberEspResponseBodyMoudleMaterialInfo(TeaModel):
    def __init__(
        self,
        address: str = None,
        business_licence_url: str = None,
        card_number: str = None,
        cn_info_url: str = None,
        contact_address: str = None,
        contact_email: str = None,
        contact_name: str = None,
        contact_phone_number: str = None,
        contact_zip_code: str = None,
        country: str = None,
        eaddress: str = None,
        ename: str = None,
        id_card_number: str = None,
        id_card_url: str = None,
        loa_key: str = None,
        loa_url: str = None,
        name: str = None,
        passport_url: str = None,
        personal_type: int = None,
        post_code: str = None,
        province: str = None,
        reason_file_oss_key: str = None,
        region: int = None,
        review_file_map: Dict[str, Any] = None,
        type: int = None,
    ):
        self.address = address
        self.business_licence_url = business_licence_url
        self.card_number = card_number
        self.cn_info_url = cn_info_url
        self.contact_address = contact_address
        self.contact_email = contact_email
        self.contact_name = contact_name
        self.contact_phone_number = contact_phone_number
        self.contact_zip_code = contact_zip_code
        self.country = country
        self.eaddress = eaddress
        self.ename = ename
        self.id_card_number = id_card_number
        self.id_card_url = id_card_url
        self.loa_key = loa_key
        self.loa_url = loa_url
        self.name = name
        self.passport_url = passport_url
        self.personal_type = personal_type
        self.post_code = post_code
        self.province = province
        self.reason_file_oss_key = reason_file_oss_key
        self.region = region
        self.review_file_map = review_file_map
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
        if self.business_licence_url is not None:
            result['BusinessLicenceUrl'] = self.business_licence_url
        if self.card_number is not None:
            result['CardNumber'] = self.card_number
        if self.cn_info_url is not None:
            result['CnInfoUrl'] = self.cn_info_url
        if self.contact_address is not None:
            result['ContactAddress'] = self.contact_address
        if self.contact_email is not None:
            result['ContactEmail'] = self.contact_email
        if self.contact_name is not None:
            result['ContactName'] = self.contact_name
        if self.contact_phone_number is not None:
            result['ContactPhoneNumber'] = self.contact_phone_number
        if self.contact_zip_code is not None:
            result['ContactZipCode'] = self.contact_zip_code
        if self.country is not None:
            result['Country'] = self.country
        if self.eaddress is not None:
            result['EAddress'] = self.eaddress
        if self.ename is not None:
            result['EName'] = self.ename
        if self.id_card_number is not None:
            result['IdCardNumber'] = self.id_card_number
        if self.id_card_url is not None:
            result['IdCardUrl'] = self.id_card_url
        if self.loa_key is not None:
            result['LoaKey'] = self.loa_key
        if self.loa_url is not None:
            result['LoaUrl'] = self.loa_url
        if self.name is not None:
            result['Name'] = self.name
        if self.passport_url is not None:
            result['PassportUrl'] = self.passport_url
        if self.personal_type is not None:
            result['PersonalType'] = self.personal_type
        if self.post_code is not None:
            result['PostCode'] = self.post_code
        if self.province is not None:
            result['Province'] = self.province
        if self.reason_file_oss_key is not None:
            result['ReasonFileOssKey'] = self.reason_file_oss_key
        if self.region is not None:
            result['Region'] = self.region
        if self.review_file_map is not None:
            result['ReviewFileMap'] = self.review_file_map
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('BusinessLicenceUrl') is not None:
            self.business_licence_url = m.get('BusinessLicenceUrl')
        if m.get('CardNumber') is not None:
            self.card_number = m.get('CardNumber')
        if m.get('CnInfoUrl') is not None:
            self.cn_info_url = m.get('CnInfoUrl')
        if m.get('ContactAddress') is not None:
            self.contact_address = m.get('ContactAddress')
        if m.get('ContactEmail') is not None:
            self.contact_email = m.get('ContactEmail')
        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')
        if m.get('ContactPhoneNumber') is not None:
            self.contact_phone_number = m.get('ContactPhoneNumber')
        if m.get('ContactZipCode') is not None:
            self.contact_zip_code = m.get('ContactZipCode')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('EAddress') is not None:
            self.eaddress = m.get('EAddress')
        if m.get('EName') is not None:
            self.ename = m.get('EName')
        if m.get('IdCardNumber') is not None:
            self.id_card_number = m.get('IdCardNumber')
        if m.get('IdCardUrl') is not None:
            self.id_card_url = m.get('IdCardUrl')
        if m.get('LoaKey') is not None:
            self.loa_key = m.get('LoaKey')
        if m.get('LoaUrl') is not None:
            self.loa_url = m.get('LoaUrl')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PassportUrl') is not None:
            self.passport_url = m.get('PassportUrl')
        if m.get('PersonalType') is not None:
            self.personal_type = m.get('PersonalType')
        if m.get('PostCode') is not None:
            self.post_code = m.get('PostCode')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        if m.get('ReasonFileOssKey') is not None:
            self.reason_file_oss_key = m.get('ReasonFileOssKey')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ReviewFileMap') is not None:
            self.review_file_map = m.get('ReviewFileMap')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class QueryTrademarkDetailByApplyNumberEspResponseBodyMoudleRootCode(TeaModel):
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


class QueryTrademarkDetailByApplyNumberEspResponseBodyMoudle(TeaModel):
    def __init__(
        self,
        bit_flag: int = None,
        biz_id: str = None,
        biz_type: str = None,
        extend_info: Dict[str, Any] = None,
        gray_icon_url: str = None,
        icon: str = None,
        leaf_codes: QueryTrademarkDetailByApplyNumberEspResponseBodyMoudleLeafCodes = None,
        material_info: QueryTrademarkDetailByApplyNumberEspResponseBodyMoudleMaterialInfo = None,
        order_id: str = None,
        partner_code: str = None,
        principal_key: str = None,
        principal_name: str = None,
        produce_type: str = None,
        root_code: QueryTrademarkDetailByApplyNumberEspResponseBodyMoudleRootCode = None,
        status: str = None,
        status_str: str = None,
        submit_audit_time_str: str = None,
        submit_audit_time_value: int = None,
        submit_status: str = None,
        submit_time_str: str = None,
        submit_time_value: int = None,
        submit_times: int = None,
        trademark_name: str = None,
        trademark_name_type: int = None,
        trademark_number: str = None,
    ):
        self.bit_flag = bit_flag
        self.biz_id = biz_id
        self.biz_type = biz_type
        self.extend_info = extend_info
        self.gray_icon_url = gray_icon_url
        self.icon = icon
        self.leaf_codes = leaf_codes
        self.material_info = material_info
        self.order_id = order_id
        self.partner_code = partner_code
        self.principal_key = principal_key
        self.principal_name = principal_name
        self.produce_type = produce_type
        self.root_code = root_code
        self.status = status
        self.status_str = status_str
        self.submit_audit_time_str = submit_audit_time_str
        self.submit_audit_time_value = submit_audit_time_value
        self.submit_status = submit_status
        self.submit_time_str = submit_time_str
        self.submit_time_value = submit_time_value
        self.submit_times = submit_times
        self.trademark_name = trademark_name
        self.trademark_name_type = trademark_name_type
        self.trademark_number = trademark_number

    def validate(self):
        if self.leaf_codes:
            self.leaf_codes.validate()
        if self.material_info:
            self.material_info.validate()
        if self.root_code:
            self.root_code.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bit_flag is not None:
            result['BitFlag'] = self.bit_flag
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.extend_info is not None:
            result['ExtendInfo'] = self.extend_info
        if self.gray_icon_url is not None:
            result['GrayIconUrl'] = self.gray_icon_url
        if self.icon is not None:
            result['Icon'] = self.icon
        if self.leaf_codes is not None:
            result['LeafCodes'] = self.leaf_codes.to_map()
        if self.material_info is not None:
            result['MaterialInfo'] = self.material_info.to_map()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.partner_code is not None:
            result['PartnerCode'] = self.partner_code
        if self.principal_key is not None:
            result['PrincipalKey'] = self.principal_key
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name
        if self.produce_type is not None:
            result['ProduceType'] = self.produce_type
        if self.root_code is not None:
            result['RootCode'] = self.root_code.to_map()
        if self.status is not None:
            result['Status'] = self.status
        if self.status_str is not None:
            result['StatusStr'] = self.status_str
        if self.submit_audit_time_str is not None:
            result['SubmitAuditTimeStr'] = self.submit_audit_time_str
        if self.submit_audit_time_value is not None:
            result['SubmitAuditTimeValue'] = self.submit_audit_time_value
        if self.submit_status is not None:
            result['SubmitStatus'] = self.submit_status
        if self.submit_time_str is not None:
            result['SubmitTimeStr'] = self.submit_time_str
        if self.submit_time_value is not None:
            result['SubmitTimeValue'] = self.submit_time_value
        if self.submit_times is not None:
            result['SubmitTimes'] = self.submit_times
        if self.trademark_name is not None:
            result['TrademarkName'] = self.trademark_name
        if self.trademark_name_type is not None:
            result['TrademarkNameType'] = self.trademark_name_type
        if self.trademark_number is not None:
            result['TrademarkNumber'] = self.trademark_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BitFlag') is not None:
            self.bit_flag = m.get('BitFlag')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('ExtendInfo') is not None:
            self.extend_info = m.get('ExtendInfo')
        if m.get('GrayIconUrl') is not None:
            self.gray_icon_url = m.get('GrayIconUrl')
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        if m.get('LeafCodes') is not None:
            temp_model = QueryTrademarkDetailByApplyNumberEspResponseBodyMoudleLeafCodes()
            self.leaf_codes = temp_model.from_map(m['LeafCodes'])
        if m.get('MaterialInfo') is not None:
            temp_model = QueryTrademarkDetailByApplyNumberEspResponseBodyMoudleMaterialInfo()
            self.material_info = temp_model.from_map(m['MaterialInfo'])
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('PartnerCode') is not None:
            self.partner_code = m.get('PartnerCode')
        if m.get('PrincipalKey') is not None:
            self.principal_key = m.get('PrincipalKey')
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')
        if m.get('ProduceType') is not None:
            self.produce_type = m.get('ProduceType')
        if m.get('RootCode') is not None:
            temp_model = QueryTrademarkDetailByApplyNumberEspResponseBodyMoudleRootCode()
            self.root_code = temp_model.from_map(m['RootCode'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StatusStr') is not None:
            self.status_str = m.get('StatusStr')
        if m.get('SubmitAuditTimeStr') is not None:
            self.submit_audit_time_str = m.get('SubmitAuditTimeStr')
        if m.get('SubmitAuditTimeValue') is not None:
            self.submit_audit_time_value = m.get('SubmitAuditTimeValue')
        if m.get('SubmitStatus') is not None:
            self.submit_status = m.get('SubmitStatus')
        if m.get('SubmitTimeStr') is not None:
            self.submit_time_str = m.get('SubmitTimeStr')
        if m.get('SubmitTimeValue') is not None:
            self.submit_time_value = m.get('SubmitTimeValue')
        if m.get('SubmitTimes') is not None:
            self.submit_times = m.get('SubmitTimes')
        if m.get('TrademarkName') is not None:
            self.trademark_name = m.get('TrademarkName')
        if m.get('TrademarkNameType') is not None:
            self.trademark_name_type = m.get('TrademarkNameType')
        if m.get('TrademarkNumber') is not None:
            self.trademark_number = m.get('TrademarkNumber')
        return self


class QueryTrademarkDetailByApplyNumberEspResponseBody(TeaModel):
    def __init__(
        self,
        moudle: QueryTrademarkDetailByApplyNumberEspResponseBodyMoudle = None,
        request_id: str = None,
    ):
        self.moudle = moudle
        self.request_id = request_id

    def validate(self):
        if self.moudle:
            self.moudle.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.moudle is not None:
            result['Moudle'] = self.moudle.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Moudle') is not None:
            temp_model = QueryTrademarkDetailByApplyNumberEspResponseBodyMoudle()
            self.moudle = temp_model.from_map(m['Moudle'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryTrademarkDetailByApplyNumberEspResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryTrademarkDetailByApplyNumberEspResponseBody = None,
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
            temp_model = QueryTrademarkDetailByApplyNumberEspResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTrademarkModelDetailRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        env: str = None,
        order_id: str = None,
        review_supplement_material: bool = None,
    ):
        self.biz_id = biz_id
        self.env = env
        self.order_id = order_id
        self.review_supplement_material = review_supplement_material

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.env is not None:
            result['Env'] = self.env
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.review_supplement_material is not None:
            result['ReviewSupplementMaterial'] = self.review_supplement_material
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Env') is not None:
            self.env = m.get('Env')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('ReviewSupplementMaterial') is not None:
            self.review_supplement_material = m.get('ReviewSupplementMaterial')
        return self


class QueryTrademarkModelDetailResponseBodyMoudleLeafCodesLeafCode(TeaModel):
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


class QueryTrademarkModelDetailResponseBodyMoudleLeafCodes(TeaModel):
    def __init__(
        self,
        leaf_code: List[QueryTrademarkModelDetailResponseBodyMoudleLeafCodesLeafCode] = None,
    ):
        self.leaf_code = leaf_code

    def validate(self):
        if self.leaf_code:
            for k in self.leaf_code:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['leafCode'] = []
        if self.leaf_code is not None:
            for k in self.leaf_code:
                result['leafCode'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.leaf_code = []
        if m.get('leafCode') is not None:
            for k in m.get('leafCode'):
                temp_model = QueryTrademarkModelDetailResponseBodyMoudleLeafCodesLeafCode()
                self.leaf_code.append(temp_model.from_map(k))
        return self


class QueryTrademarkModelDetailResponseBodyMoudleMaterialInfo(TeaModel):
    def __init__(
        self,
        address: str = None,
        business_licence_url: str = None,
        card_number: str = None,
        cn_info_url: str = None,
        contact_address: str = None,
        contact_email: str = None,
        contact_name: str = None,
        contact_phone_number: str = None,
        contact_zip_code: str = None,
        country: str = None,
        eaddress: str = None,
        ename: str = None,
        id_card_number: str = None,
        id_card_url: str = None,
        loa_key: str = None,
        loa_url: str = None,
        name: str = None,
        passport_url: str = None,
        personal_type: int = None,
        post_code: str = None,
        province: str = None,
        reason_file_oss_key: str = None,
        region: int = None,
        review_file_map: Dict[str, Any] = None,
        type: int = None,
    ):
        self.address = address
        self.business_licence_url = business_licence_url
        self.card_number = card_number
        self.cn_info_url = cn_info_url
        self.contact_address = contact_address
        self.contact_email = contact_email
        self.contact_name = contact_name
        self.contact_phone_number = contact_phone_number
        self.contact_zip_code = contact_zip_code
        self.country = country
        self.eaddress = eaddress
        self.ename = ename
        self.id_card_number = id_card_number
        self.id_card_url = id_card_url
        self.loa_key = loa_key
        self.loa_url = loa_url
        self.name = name
        self.passport_url = passport_url
        self.personal_type = personal_type
        self.post_code = post_code
        self.province = province
        self.reason_file_oss_key = reason_file_oss_key
        self.region = region
        self.review_file_map = review_file_map
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
        if self.business_licence_url is not None:
            result['BusinessLicenceUrl'] = self.business_licence_url
        if self.card_number is not None:
            result['CardNumber'] = self.card_number
        if self.cn_info_url is not None:
            result['CnInfoUrl'] = self.cn_info_url
        if self.contact_address is not None:
            result['ContactAddress'] = self.contact_address
        if self.contact_email is not None:
            result['ContactEmail'] = self.contact_email
        if self.contact_name is not None:
            result['ContactName'] = self.contact_name
        if self.contact_phone_number is not None:
            result['ContactPhoneNumber'] = self.contact_phone_number
        if self.contact_zip_code is not None:
            result['ContactZipCode'] = self.contact_zip_code
        if self.country is not None:
            result['Country'] = self.country
        if self.eaddress is not None:
            result['EAddress'] = self.eaddress
        if self.ename is not None:
            result['EName'] = self.ename
        if self.id_card_number is not None:
            result['IdCardNumber'] = self.id_card_number
        if self.id_card_url is not None:
            result['IdCardUrl'] = self.id_card_url
        if self.loa_key is not None:
            result['LoaKey'] = self.loa_key
        if self.loa_url is not None:
            result['LoaUrl'] = self.loa_url
        if self.name is not None:
            result['Name'] = self.name
        if self.passport_url is not None:
            result['PassportUrl'] = self.passport_url
        if self.personal_type is not None:
            result['PersonalType'] = self.personal_type
        if self.post_code is not None:
            result['PostCode'] = self.post_code
        if self.province is not None:
            result['Province'] = self.province
        if self.reason_file_oss_key is not None:
            result['ReasonFileOssKey'] = self.reason_file_oss_key
        if self.region is not None:
            result['Region'] = self.region
        if self.review_file_map is not None:
            result['ReviewFileMap'] = self.review_file_map
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('BusinessLicenceUrl') is not None:
            self.business_licence_url = m.get('BusinessLicenceUrl')
        if m.get('CardNumber') is not None:
            self.card_number = m.get('CardNumber')
        if m.get('CnInfoUrl') is not None:
            self.cn_info_url = m.get('CnInfoUrl')
        if m.get('ContactAddress') is not None:
            self.contact_address = m.get('ContactAddress')
        if m.get('ContactEmail') is not None:
            self.contact_email = m.get('ContactEmail')
        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')
        if m.get('ContactPhoneNumber') is not None:
            self.contact_phone_number = m.get('ContactPhoneNumber')
        if m.get('ContactZipCode') is not None:
            self.contact_zip_code = m.get('ContactZipCode')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('EAddress') is not None:
            self.eaddress = m.get('EAddress')
        if m.get('EName') is not None:
            self.ename = m.get('EName')
        if m.get('IdCardNumber') is not None:
            self.id_card_number = m.get('IdCardNumber')
        if m.get('IdCardUrl') is not None:
            self.id_card_url = m.get('IdCardUrl')
        if m.get('LoaKey') is not None:
            self.loa_key = m.get('LoaKey')
        if m.get('LoaUrl') is not None:
            self.loa_url = m.get('LoaUrl')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PassportUrl') is not None:
            self.passport_url = m.get('PassportUrl')
        if m.get('PersonalType') is not None:
            self.personal_type = m.get('PersonalType')
        if m.get('PostCode') is not None:
            self.post_code = m.get('PostCode')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        if m.get('ReasonFileOssKey') is not None:
            self.reason_file_oss_key = m.get('ReasonFileOssKey')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ReviewFileMap') is not None:
            self.review_file_map = m.get('ReviewFileMap')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class QueryTrademarkModelDetailResponseBodyMoudleRootCode(TeaModel):
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


class QueryTrademarkModelDetailResponseBodyMoudle(TeaModel):
    def __init__(
        self,
        bit_flag: int = None,
        biz_id: str = None,
        biz_type: str = None,
        extend_info: Dict[str, Any] = None,
        gray_icon_url: str = None,
        icon: str = None,
        leaf_codes: QueryTrademarkModelDetailResponseBodyMoudleLeafCodes = None,
        material_info: QueryTrademarkModelDetailResponseBodyMoudleMaterialInfo = None,
        order_id: str = None,
        partner_code: str = None,
        principal_key: str = None,
        principal_name: str = None,
        produce_type: str = None,
        request_id: str = None,
        root_code: QueryTrademarkModelDetailResponseBodyMoudleRootCode = None,
        status: str = None,
        status_str: str = None,
        submit_audit_time_str: str = None,
        submit_audit_time_value: int = None,
        submit_status: str = None,
        submit_time_str: str = None,
        submit_time_value: int = None,
        submit_times: int = None,
        trademark_name: str = None,
        trademark_name_type: int = None,
        trademark_number: str = None,
    ):
        self.bit_flag = bit_flag
        self.biz_id = biz_id
        self.biz_type = biz_type
        self.extend_info = extend_info
        self.gray_icon_url = gray_icon_url
        self.icon = icon
        self.leaf_codes = leaf_codes
        self.material_info = material_info
        self.order_id = order_id
        self.partner_code = partner_code
        self.principal_key = principal_key
        self.principal_name = principal_name
        self.produce_type = produce_type
        self.request_id = request_id
        self.root_code = root_code
        self.status = status
        self.status_str = status_str
        self.submit_audit_time_str = submit_audit_time_str
        self.submit_audit_time_value = submit_audit_time_value
        self.submit_status = submit_status
        self.submit_time_str = submit_time_str
        self.submit_time_value = submit_time_value
        self.submit_times = submit_times
        self.trademark_name = trademark_name
        self.trademark_name_type = trademark_name_type
        self.trademark_number = trademark_number

    def validate(self):
        if self.leaf_codes:
            self.leaf_codes.validate()
        if self.material_info:
            self.material_info.validate()
        if self.root_code:
            self.root_code.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bit_flag is not None:
            result['BitFlag'] = self.bit_flag
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.extend_info is not None:
            result['ExtendInfo'] = self.extend_info
        if self.gray_icon_url is not None:
            result['GrayIconUrl'] = self.gray_icon_url
        if self.icon is not None:
            result['Icon'] = self.icon
        if self.leaf_codes is not None:
            result['LeafCodes'] = self.leaf_codes.to_map()
        if self.material_info is not None:
            result['MaterialInfo'] = self.material_info.to_map()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.partner_code is not None:
            result['PartnerCode'] = self.partner_code
        if self.principal_key is not None:
            result['PrincipalKey'] = self.principal_key
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name
        if self.produce_type is not None:
            result['ProduceType'] = self.produce_type
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.root_code is not None:
            result['RootCode'] = self.root_code.to_map()
        if self.status is not None:
            result['Status'] = self.status
        if self.status_str is not None:
            result['StatusStr'] = self.status_str
        if self.submit_audit_time_str is not None:
            result['SubmitAuditTimeStr'] = self.submit_audit_time_str
        if self.submit_audit_time_value is not None:
            result['SubmitAuditTimeValue'] = self.submit_audit_time_value
        if self.submit_status is not None:
            result['SubmitStatus'] = self.submit_status
        if self.submit_time_str is not None:
            result['SubmitTimeStr'] = self.submit_time_str
        if self.submit_time_value is not None:
            result['SubmitTimeValue'] = self.submit_time_value
        if self.submit_times is not None:
            result['SubmitTimes'] = self.submit_times
        if self.trademark_name is not None:
            result['TrademarkName'] = self.trademark_name
        if self.trademark_name_type is not None:
            result['TrademarkNameType'] = self.trademark_name_type
        if self.trademark_number is not None:
            result['TrademarkNumber'] = self.trademark_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BitFlag') is not None:
            self.bit_flag = m.get('BitFlag')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('ExtendInfo') is not None:
            self.extend_info = m.get('ExtendInfo')
        if m.get('GrayIconUrl') is not None:
            self.gray_icon_url = m.get('GrayIconUrl')
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        if m.get('LeafCodes') is not None:
            temp_model = QueryTrademarkModelDetailResponseBodyMoudleLeafCodes()
            self.leaf_codes = temp_model.from_map(m['LeafCodes'])
        if m.get('MaterialInfo') is not None:
            temp_model = QueryTrademarkModelDetailResponseBodyMoudleMaterialInfo()
            self.material_info = temp_model.from_map(m['MaterialInfo'])
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('PartnerCode') is not None:
            self.partner_code = m.get('PartnerCode')
        if m.get('PrincipalKey') is not None:
            self.principal_key = m.get('PrincipalKey')
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')
        if m.get('ProduceType') is not None:
            self.produce_type = m.get('ProduceType')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RootCode') is not None:
            temp_model = QueryTrademarkModelDetailResponseBodyMoudleRootCode()
            self.root_code = temp_model.from_map(m['RootCode'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StatusStr') is not None:
            self.status_str = m.get('StatusStr')
        if m.get('SubmitAuditTimeStr') is not None:
            self.submit_audit_time_str = m.get('SubmitAuditTimeStr')
        if m.get('SubmitAuditTimeValue') is not None:
            self.submit_audit_time_value = m.get('SubmitAuditTimeValue')
        if m.get('SubmitStatus') is not None:
            self.submit_status = m.get('SubmitStatus')
        if m.get('SubmitTimeStr') is not None:
            self.submit_time_str = m.get('SubmitTimeStr')
        if m.get('SubmitTimeValue') is not None:
            self.submit_time_value = m.get('SubmitTimeValue')
        if m.get('SubmitTimes') is not None:
            self.submit_times = m.get('SubmitTimes')
        if m.get('TrademarkName') is not None:
            self.trademark_name = m.get('TrademarkName')
        if m.get('TrademarkNameType') is not None:
            self.trademark_name_type = m.get('TrademarkNameType')
        if m.get('TrademarkNumber') is not None:
            self.trademark_number = m.get('TrademarkNumber')
        return self


class QueryTrademarkModelDetailResponseBody(TeaModel):
    def __init__(
        self,
        moudle: QueryTrademarkModelDetailResponseBodyMoudle = None,
    ):
        self.moudle = moudle

    def validate(self):
        if self.moudle:
            self.moudle.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.moudle is not None:
            result['Moudle'] = self.moudle.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Moudle') is not None:
            temp_model = QueryTrademarkModelDetailResponseBodyMoudle()
            self.moudle = temp_model.from_map(m['Moudle'])
        return self


class QueryTrademarkModelDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryTrademarkModelDetailResponseBody = None,
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
            temp_model = QueryTrademarkModelDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTrademarkModelEspDetailRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        biz_type: str = None,
    ):
        self.biz_id = biz_id
        self.biz_type = biz_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        return self


class QueryTrademarkModelEspDetailResponseBodyMoudleLeafCodesLeafCode(TeaModel):
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


class QueryTrademarkModelEspDetailResponseBodyMoudleLeafCodes(TeaModel):
    def __init__(
        self,
        leaf_code: List[QueryTrademarkModelEspDetailResponseBodyMoudleLeafCodesLeafCode] = None,
    ):
        self.leaf_code = leaf_code

    def validate(self):
        if self.leaf_code:
            for k in self.leaf_code:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['leafCode'] = []
        if self.leaf_code is not None:
            for k in self.leaf_code:
                result['leafCode'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.leaf_code = []
        if m.get('leafCode') is not None:
            for k in m.get('leafCode'):
                temp_model = QueryTrademarkModelEspDetailResponseBodyMoudleLeafCodesLeafCode()
                self.leaf_code.append(temp_model.from_map(k))
        return self


class QueryTrademarkModelEspDetailResponseBodyMoudleMaterialInfo(TeaModel):
    def __init__(
        self,
        address: str = None,
        business_licence_url: str = None,
        card_number: str = None,
        cn_info_url: str = None,
        contact_address: str = None,
        contact_email: str = None,
        contact_zip_code: str = None,
        country: str = None,
        eaddress: str = None,
        ename: str = None,
        id_card_number: str = None,
        id_card_url: str = None,
        loa_key: str = None,
        loa_url: str = None,
        name: str = None,
        passport_url: str = None,
        personal_type: str = None,
        post_code: str = None,
        province: str = None,
        reason_file_oss_key: str = None,
        region: int = None,
        type: int = None,
    ):
        self.address = address
        self.business_licence_url = business_licence_url
        self.card_number = card_number
        self.cn_info_url = cn_info_url
        self.contact_address = contact_address
        self.contact_email = contact_email
        self.contact_zip_code = contact_zip_code
        self.country = country
        self.eaddress = eaddress
        self.ename = ename
        self.id_card_number = id_card_number
        self.id_card_url = id_card_url
        self.loa_key = loa_key
        self.loa_url = loa_url
        self.name = name
        self.passport_url = passport_url
        self.personal_type = personal_type
        self.post_code = post_code
        self.province = province
        self.reason_file_oss_key = reason_file_oss_key
        self.region = region
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
        if self.business_licence_url is not None:
            result['BusinessLicenceUrl'] = self.business_licence_url
        if self.card_number is not None:
            result['CardNumber'] = self.card_number
        if self.cn_info_url is not None:
            result['CnInfoUrl'] = self.cn_info_url
        if self.contact_address is not None:
            result['ContactAddress'] = self.contact_address
        if self.contact_email is not None:
            result['ContactEmail'] = self.contact_email
        if self.contact_zip_code is not None:
            result['ContactZipCode'] = self.contact_zip_code
        if self.country is not None:
            result['Country'] = self.country
        if self.eaddress is not None:
            result['EAddress'] = self.eaddress
        if self.ename is not None:
            result['EName'] = self.ename
        if self.id_card_number is not None:
            result['IdCardNumber'] = self.id_card_number
        if self.id_card_url is not None:
            result['IdCardUrl'] = self.id_card_url
        if self.loa_key is not None:
            result['LoaKey'] = self.loa_key
        if self.loa_url is not None:
            result['LoaUrl'] = self.loa_url
        if self.name is not None:
            result['Name'] = self.name
        if self.passport_url is not None:
            result['PassportUrl'] = self.passport_url
        if self.personal_type is not None:
            result['PersonalType'] = self.personal_type
        if self.post_code is not None:
            result['PostCode'] = self.post_code
        if self.province is not None:
            result['Province'] = self.province
        if self.reason_file_oss_key is not None:
            result['ReasonFileOssKey'] = self.reason_file_oss_key
        if self.region is not None:
            result['Region'] = self.region
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('BusinessLicenceUrl') is not None:
            self.business_licence_url = m.get('BusinessLicenceUrl')
        if m.get('CardNumber') is not None:
            self.card_number = m.get('CardNumber')
        if m.get('CnInfoUrl') is not None:
            self.cn_info_url = m.get('CnInfoUrl')
        if m.get('ContactAddress') is not None:
            self.contact_address = m.get('ContactAddress')
        if m.get('ContactEmail') is not None:
            self.contact_email = m.get('ContactEmail')
        if m.get('ContactZipCode') is not None:
            self.contact_zip_code = m.get('ContactZipCode')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('EAddress') is not None:
            self.eaddress = m.get('EAddress')
        if m.get('EName') is not None:
            self.ename = m.get('EName')
        if m.get('IdCardNumber') is not None:
            self.id_card_number = m.get('IdCardNumber')
        if m.get('IdCardUrl') is not None:
            self.id_card_url = m.get('IdCardUrl')
        if m.get('LoaKey') is not None:
            self.loa_key = m.get('LoaKey')
        if m.get('LoaUrl') is not None:
            self.loa_url = m.get('LoaUrl')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PassportUrl') is not None:
            self.passport_url = m.get('PassportUrl')
        if m.get('PersonalType') is not None:
            self.personal_type = m.get('PersonalType')
        if m.get('PostCode') is not None:
            self.post_code = m.get('PostCode')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        if m.get('ReasonFileOssKey') is not None:
            self.reason_file_oss_key = m.get('ReasonFileOssKey')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class QueryTrademarkModelEspDetailResponseBodyMoudleRootCode(TeaModel):
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


class QueryTrademarkModelEspDetailResponseBodyMoudle(TeaModel):
    def __init__(
        self,
        bit_flag: int = None,
        biz_id: str = None,
        biz_type: str = None,
        extend_info: Dict[str, Any] = None,
        gray_icon_url: str = None,
        icon: str = None,
        leaf_codes: QueryTrademarkModelEspDetailResponseBodyMoudleLeafCodes = None,
        material_info: QueryTrademarkModelEspDetailResponseBodyMoudleMaterialInfo = None,
        order_id: str = None,
        partner_code: str = None,
        principal_key: str = None,
        principal_name: str = None,
        produce_type: str = None,
        request_id: str = None,
        root_code: QueryTrademarkModelEspDetailResponseBodyMoudleRootCode = None,
        status: str = None,
        status_str: str = None,
        submit_audit_time: int = None,
        submit_status: str = None,
        submit_time: int = None,
        submit_times: int = None,
        trademark_name: str = None,
        trademark_name_type: int = None,
        trademark_number: str = None,
    ):
        self.bit_flag = bit_flag
        self.biz_id = biz_id
        self.biz_type = biz_type
        self.extend_info = extend_info
        self.gray_icon_url = gray_icon_url
        self.icon = icon
        self.leaf_codes = leaf_codes
        self.material_info = material_info
        self.order_id = order_id
        self.partner_code = partner_code
        self.principal_key = principal_key
        self.principal_name = principal_name
        self.produce_type = produce_type
        self.request_id = request_id
        self.root_code = root_code
        self.status = status
        self.status_str = status_str
        self.submit_audit_time = submit_audit_time
        self.submit_status = submit_status
        self.submit_time = submit_time
        self.submit_times = submit_times
        self.trademark_name = trademark_name
        self.trademark_name_type = trademark_name_type
        self.trademark_number = trademark_number

    def validate(self):
        if self.leaf_codes:
            self.leaf_codes.validate()
        if self.material_info:
            self.material_info.validate()
        if self.root_code:
            self.root_code.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bit_flag is not None:
            result['BitFlag'] = self.bit_flag
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.extend_info is not None:
            result['ExtendInfo'] = self.extend_info
        if self.gray_icon_url is not None:
            result['GrayIconUrl'] = self.gray_icon_url
        if self.icon is not None:
            result['Icon'] = self.icon
        if self.leaf_codes is not None:
            result['LeafCodes'] = self.leaf_codes.to_map()
        if self.material_info is not None:
            result['MaterialInfo'] = self.material_info.to_map()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.partner_code is not None:
            result['PartnerCode'] = self.partner_code
        if self.principal_key is not None:
            result['PrincipalKey'] = self.principal_key
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name
        if self.produce_type is not None:
            result['ProduceType'] = self.produce_type
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.root_code is not None:
            result['RootCode'] = self.root_code.to_map()
        if self.status is not None:
            result['Status'] = self.status
        if self.status_str is not None:
            result['StatusStr'] = self.status_str
        if self.submit_audit_time is not None:
            result['SubmitAuditTime'] = self.submit_audit_time
        if self.submit_status is not None:
            result['SubmitStatus'] = self.submit_status
        if self.submit_time is not None:
            result['SubmitTime'] = self.submit_time
        if self.submit_times is not None:
            result['SubmitTimes'] = self.submit_times
        if self.trademark_name is not None:
            result['TrademarkName'] = self.trademark_name
        if self.trademark_name_type is not None:
            result['TrademarkNameType'] = self.trademark_name_type
        if self.trademark_number is not None:
            result['TrademarkNumber'] = self.trademark_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BitFlag') is not None:
            self.bit_flag = m.get('BitFlag')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('ExtendInfo') is not None:
            self.extend_info = m.get('ExtendInfo')
        if m.get('GrayIconUrl') is not None:
            self.gray_icon_url = m.get('GrayIconUrl')
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        if m.get('LeafCodes') is not None:
            temp_model = QueryTrademarkModelEspDetailResponseBodyMoudleLeafCodes()
            self.leaf_codes = temp_model.from_map(m['LeafCodes'])
        if m.get('MaterialInfo') is not None:
            temp_model = QueryTrademarkModelEspDetailResponseBodyMoudleMaterialInfo()
            self.material_info = temp_model.from_map(m['MaterialInfo'])
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('PartnerCode') is not None:
            self.partner_code = m.get('PartnerCode')
        if m.get('PrincipalKey') is not None:
            self.principal_key = m.get('PrincipalKey')
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')
        if m.get('ProduceType') is not None:
            self.produce_type = m.get('ProduceType')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RootCode') is not None:
            temp_model = QueryTrademarkModelEspDetailResponseBodyMoudleRootCode()
            self.root_code = temp_model.from_map(m['RootCode'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StatusStr') is not None:
            self.status_str = m.get('StatusStr')
        if m.get('SubmitAuditTime') is not None:
            self.submit_audit_time = m.get('SubmitAuditTime')
        if m.get('SubmitStatus') is not None:
            self.submit_status = m.get('SubmitStatus')
        if m.get('SubmitTime') is not None:
            self.submit_time = m.get('SubmitTime')
        if m.get('SubmitTimes') is not None:
            self.submit_times = m.get('SubmitTimes')
        if m.get('TrademarkName') is not None:
            self.trademark_name = m.get('TrademarkName')
        if m.get('TrademarkNameType') is not None:
            self.trademark_name_type = m.get('TrademarkNameType')
        if m.get('TrademarkNumber') is not None:
            self.trademark_number = m.get('TrademarkNumber')
        return self


class QueryTrademarkModelEspDetailResponseBody(TeaModel):
    def __init__(
        self,
        moudle: QueryTrademarkModelEspDetailResponseBodyMoudle = None,
    ):
        self.moudle = moudle

    def validate(self):
        if self.moudle:
            self.moudle.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.moudle is not None:
            result['Moudle'] = self.moudle.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Moudle') is not None:
            temp_model = QueryTrademarkModelEspDetailResponseBodyMoudle()
            self.moudle = temp_model.from_map(m['Moudle'])
        return self


class QueryTrademarkModelEspDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryTrademarkModelEspDetailResponseBody = None,
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
            temp_model = QueryTrademarkModelEspDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTrademarkModelEspListRequest(TeaModel):
    def __init__(
        self,
        additional_submit_status: str = None,
        additional_submit_time: str = None,
        biz_id: str = None,
        biz_type: str = None,
        env: str = None,
        exist_status: List[str] = None,
        order_id: str = None,
        order_ids_str: str = None,
        order_instance_id: str = None,
        page_num: int = None,
        page_size: int = None,
        principal_key: str = None,
        principal_name: str = None,
        status: str = None,
        submit_status: str = None,
        submit_time: str = None,
    ):
        self.additional_submit_status = additional_submit_status
        self.additional_submit_time = additional_submit_time
        self.biz_id = biz_id
        self.biz_type = biz_type
        self.env = env
        self.exist_status = exist_status
        self.order_id = order_id
        self.order_ids_str = order_ids_str
        self.order_instance_id = order_instance_id
        self.page_num = page_num
        self.page_size = page_size
        self.principal_key = principal_key
        self.principal_name = principal_name
        self.status = status
        self.submit_status = submit_status
        self.submit_time = submit_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.additional_submit_status is not None:
            result['AdditionalSubmitStatus'] = self.additional_submit_status
        if self.additional_submit_time is not None:
            result['AdditionalSubmitTime'] = self.additional_submit_time
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.env is not None:
            result['Env'] = self.env
        if self.exist_status is not None:
            result['ExistStatus'] = self.exist_status
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.order_ids_str is not None:
            result['OrderIdsStr'] = self.order_ids_str
        if self.order_instance_id is not None:
            result['OrderInstanceId'] = self.order_instance_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.principal_key is not None:
            result['PrincipalKey'] = self.principal_key
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name
        if self.status is not None:
            result['Status'] = self.status
        if self.submit_status is not None:
            result['SubmitStatus'] = self.submit_status
        if self.submit_time is not None:
            result['SubmitTime'] = self.submit_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdditionalSubmitStatus') is not None:
            self.additional_submit_status = m.get('AdditionalSubmitStatus')
        if m.get('AdditionalSubmitTime') is not None:
            self.additional_submit_time = m.get('AdditionalSubmitTime')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('Env') is not None:
            self.env = m.get('Env')
        if m.get('ExistStatus') is not None:
            self.exist_status = m.get('ExistStatus')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('OrderIdsStr') is not None:
            self.order_ids_str = m.get('OrderIdsStr')
        if m.get('OrderInstanceId') is not None:
            self.order_instance_id = m.get('OrderInstanceId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PrincipalKey') is not None:
            self.principal_key = m.get('PrincipalKey')
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubmitStatus') is not None:
            self.submit_status = m.get('SubmitStatus')
        if m.get('SubmitTime') is not None:
            self.submit_time = m.get('SubmitTime')
        return self


class QueryTrademarkModelEspListShrinkRequest(TeaModel):
    def __init__(
        self,
        additional_submit_status: str = None,
        additional_submit_time: str = None,
        biz_id: str = None,
        biz_type: str = None,
        env: str = None,
        exist_status_shrink: str = None,
        order_id: str = None,
        order_ids_str: str = None,
        order_instance_id: str = None,
        page_num: int = None,
        page_size: int = None,
        principal_key: str = None,
        principal_name: str = None,
        status: str = None,
        submit_status: str = None,
        submit_time: str = None,
    ):
        self.additional_submit_status = additional_submit_status
        self.additional_submit_time = additional_submit_time
        self.biz_id = biz_id
        self.biz_type = biz_type
        self.env = env
        self.exist_status_shrink = exist_status_shrink
        self.order_id = order_id
        self.order_ids_str = order_ids_str
        self.order_instance_id = order_instance_id
        self.page_num = page_num
        self.page_size = page_size
        self.principal_key = principal_key
        self.principal_name = principal_name
        self.status = status
        self.submit_status = submit_status
        self.submit_time = submit_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.additional_submit_status is not None:
            result['AdditionalSubmitStatus'] = self.additional_submit_status
        if self.additional_submit_time is not None:
            result['AdditionalSubmitTime'] = self.additional_submit_time
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.env is not None:
            result['Env'] = self.env
        if self.exist_status_shrink is not None:
            result['ExistStatus'] = self.exist_status_shrink
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.order_ids_str is not None:
            result['OrderIdsStr'] = self.order_ids_str
        if self.order_instance_id is not None:
            result['OrderInstanceId'] = self.order_instance_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.principal_key is not None:
            result['PrincipalKey'] = self.principal_key
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name
        if self.status is not None:
            result['Status'] = self.status
        if self.submit_status is not None:
            result['SubmitStatus'] = self.submit_status
        if self.submit_time is not None:
            result['SubmitTime'] = self.submit_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdditionalSubmitStatus') is not None:
            self.additional_submit_status = m.get('AdditionalSubmitStatus')
        if m.get('AdditionalSubmitTime') is not None:
            self.additional_submit_time = m.get('AdditionalSubmitTime')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('Env') is not None:
            self.env = m.get('Env')
        if m.get('ExistStatus') is not None:
            self.exist_status_shrink = m.get('ExistStatus')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('OrderIdsStr') is not None:
            self.order_ids_str = m.get('OrderIdsStr')
        if m.get('OrderInstanceId') is not None:
            self.order_instance_id = m.get('OrderInstanceId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PrincipalKey') is not None:
            self.principal_key = m.get('PrincipalKey')
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubmitStatus') is not None:
            self.submit_status = m.get('SubmitStatus')
        if m.get('SubmitTime') is not None:
            self.submit_time = m.get('SubmitTime')
        return self


class QueryTrademarkModelEspListResponseBodyMoudleDataItemLeafCodesLeafCode(TeaModel):
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


class QueryTrademarkModelEspListResponseBodyMoudleDataItemLeafCodes(TeaModel):
    def __init__(
        self,
        leaf_code: List[QueryTrademarkModelEspListResponseBodyMoudleDataItemLeafCodesLeafCode] = None,
    ):
        self.leaf_code = leaf_code

    def validate(self):
        if self.leaf_code:
            for k in self.leaf_code:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['leafCode'] = []
        if self.leaf_code is not None:
            for k in self.leaf_code:
                result['leafCode'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.leaf_code = []
        if m.get('leafCode') is not None:
            for k in m.get('leafCode'):
                temp_model = QueryTrademarkModelEspListResponseBodyMoudleDataItemLeafCodesLeafCode()
                self.leaf_code.append(temp_model.from_map(k))
        return self


class QueryTrademarkModelEspListResponseBodyMoudleDataItemMaterialInfo(TeaModel):
    def __init__(
        self,
        address: str = None,
        business_licence_url: str = None,
        card_number: str = None,
        cn_info_url: str = None,
        contact_address: str = None,
        contact_email: str = None,
        contact_zip_code: str = None,
        country: str = None,
        eaddress: str = None,
        ename: str = None,
        id_card_number: str = None,
        id_card_url: str = None,
        loa_key: str = None,
        loa_url: str = None,
        name: str = None,
        passport_url: str = None,
        personal_type: str = None,
        post_code: str = None,
        province: str = None,
        reason_file_oss_key: str = None,
        region: int = None,
        type: int = None,
    ):
        self.address = address
        self.business_licence_url = business_licence_url
        self.card_number = card_number
        self.cn_info_url = cn_info_url
        self.contact_address = contact_address
        self.contact_email = contact_email
        self.contact_zip_code = contact_zip_code
        self.country = country
        self.eaddress = eaddress
        self.ename = ename
        self.id_card_number = id_card_number
        self.id_card_url = id_card_url
        self.loa_key = loa_key
        self.loa_url = loa_url
        self.name = name
        self.passport_url = passport_url
        self.personal_type = personal_type
        self.post_code = post_code
        self.province = province
        self.reason_file_oss_key = reason_file_oss_key
        self.region = region
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
        if self.business_licence_url is not None:
            result['BusinessLicenceUrl'] = self.business_licence_url
        if self.card_number is not None:
            result['CardNumber'] = self.card_number
        if self.cn_info_url is not None:
            result['CnInfoUrl'] = self.cn_info_url
        if self.contact_address is not None:
            result['ContactAddress'] = self.contact_address
        if self.contact_email is not None:
            result['ContactEmail'] = self.contact_email
        if self.contact_zip_code is not None:
            result['ContactZipCode'] = self.contact_zip_code
        if self.country is not None:
            result['Country'] = self.country
        if self.eaddress is not None:
            result['EAddress'] = self.eaddress
        if self.ename is not None:
            result['EName'] = self.ename
        if self.id_card_number is not None:
            result['IdCardNumber'] = self.id_card_number
        if self.id_card_url is not None:
            result['IdCardUrl'] = self.id_card_url
        if self.loa_key is not None:
            result['LoaKey'] = self.loa_key
        if self.loa_url is not None:
            result['LoaUrl'] = self.loa_url
        if self.name is not None:
            result['Name'] = self.name
        if self.passport_url is not None:
            result['PassportUrl'] = self.passport_url
        if self.personal_type is not None:
            result['PersonalType'] = self.personal_type
        if self.post_code is not None:
            result['PostCode'] = self.post_code
        if self.province is not None:
            result['Province'] = self.province
        if self.reason_file_oss_key is not None:
            result['ReasonFileOssKey'] = self.reason_file_oss_key
        if self.region is not None:
            result['Region'] = self.region
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('BusinessLicenceUrl') is not None:
            self.business_licence_url = m.get('BusinessLicenceUrl')
        if m.get('CardNumber') is not None:
            self.card_number = m.get('CardNumber')
        if m.get('CnInfoUrl') is not None:
            self.cn_info_url = m.get('CnInfoUrl')
        if m.get('ContactAddress') is not None:
            self.contact_address = m.get('ContactAddress')
        if m.get('ContactEmail') is not None:
            self.contact_email = m.get('ContactEmail')
        if m.get('ContactZipCode') is not None:
            self.contact_zip_code = m.get('ContactZipCode')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('EAddress') is not None:
            self.eaddress = m.get('EAddress')
        if m.get('EName') is not None:
            self.ename = m.get('EName')
        if m.get('IdCardNumber') is not None:
            self.id_card_number = m.get('IdCardNumber')
        if m.get('IdCardUrl') is not None:
            self.id_card_url = m.get('IdCardUrl')
        if m.get('LoaKey') is not None:
            self.loa_key = m.get('LoaKey')
        if m.get('LoaUrl') is not None:
            self.loa_url = m.get('LoaUrl')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PassportUrl') is not None:
            self.passport_url = m.get('PassportUrl')
        if m.get('PersonalType') is not None:
            self.personal_type = m.get('PersonalType')
        if m.get('PostCode') is not None:
            self.post_code = m.get('PostCode')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        if m.get('ReasonFileOssKey') is not None:
            self.reason_file_oss_key = m.get('ReasonFileOssKey')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class QueryTrademarkModelEspListResponseBodyMoudleDataItemRootCode(TeaModel):
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


class QueryTrademarkModelEspListResponseBodyMoudleDataItem(TeaModel):
    def __init__(
        self,
        bit_flag: int = None,
        biz_id: str = None,
        biz_type: str = None,
        extend_info: Dict[str, Any] = None,
        gray_icon_url: str = None,
        icon: str = None,
        leaf_codes: QueryTrademarkModelEspListResponseBodyMoudleDataItemLeafCodes = None,
        material_info: QueryTrademarkModelEspListResponseBodyMoudleDataItemMaterialInfo = None,
        order_id: str = None,
        partner_code: str = None,
        principal_key: str = None,
        principal_name: str = None,
        produce_type: str = None,
        root_code: QueryTrademarkModelEspListResponseBodyMoudleDataItemRootCode = None,
        status: str = None,
        status_str: str = None,
        submit_audit_time: int = None,
        submit_status: str = None,
        submit_time: int = None,
        submit_times: int = None,
        trademark_name: str = None,
        trademark_name_type: int = None,
        trademark_number: str = None,
    ):
        self.bit_flag = bit_flag
        self.biz_id = biz_id
        self.biz_type = biz_type
        self.extend_info = extend_info
        self.gray_icon_url = gray_icon_url
        self.icon = icon
        self.leaf_codes = leaf_codes
        self.material_info = material_info
        self.order_id = order_id
        self.partner_code = partner_code
        self.principal_key = principal_key
        self.principal_name = principal_name
        self.produce_type = produce_type
        self.root_code = root_code
        self.status = status
        self.status_str = status_str
        self.submit_audit_time = submit_audit_time
        self.submit_status = submit_status
        self.submit_time = submit_time
        self.submit_times = submit_times
        self.trademark_name = trademark_name
        self.trademark_name_type = trademark_name_type
        self.trademark_number = trademark_number

    def validate(self):
        if self.leaf_codes:
            self.leaf_codes.validate()
        if self.material_info:
            self.material_info.validate()
        if self.root_code:
            self.root_code.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bit_flag is not None:
            result['BitFlag'] = self.bit_flag
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.extend_info is not None:
            result['ExtendInfo'] = self.extend_info
        if self.gray_icon_url is not None:
            result['GrayIconUrl'] = self.gray_icon_url
        if self.icon is not None:
            result['Icon'] = self.icon
        if self.leaf_codes is not None:
            result['LeafCodes'] = self.leaf_codes.to_map()
        if self.material_info is not None:
            result['MaterialInfo'] = self.material_info.to_map()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.partner_code is not None:
            result['PartnerCode'] = self.partner_code
        if self.principal_key is not None:
            result['PrincipalKey'] = self.principal_key
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name
        if self.produce_type is not None:
            result['ProduceType'] = self.produce_type
        if self.root_code is not None:
            result['RootCode'] = self.root_code.to_map()
        if self.status is not None:
            result['Status'] = self.status
        if self.status_str is not None:
            result['StatusStr'] = self.status_str
        if self.submit_audit_time is not None:
            result['SubmitAuditTime'] = self.submit_audit_time
        if self.submit_status is not None:
            result['SubmitStatus'] = self.submit_status
        if self.submit_time is not None:
            result['SubmitTime'] = self.submit_time
        if self.submit_times is not None:
            result['SubmitTimes'] = self.submit_times
        if self.trademark_name is not None:
            result['TrademarkName'] = self.trademark_name
        if self.trademark_name_type is not None:
            result['TrademarkNameType'] = self.trademark_name_type
        if self.trademark_number is not None:
            result['TrademarkNumber'] = self.trademark_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BitFlag') is not None:
            self.bit_flag = m.get('BitFlag')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('ExtendInfo') is not None:
            self.extend_info = m.get('ExtendInfo')
        if m.get('GrayIconUrl') is not None:
            self.gray_icon_url = m.get('GrayIconUrl')
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        if m.get('LeafCodes') is not None:
            temp_model = QueryTrademarkModelEspListResponseBodyMoudleDataItemLeafCodes()
            self.leaf_codes = temp_model.from_map(m['LeafCodes'])
        if m.get('MaterialInfo') is not None:
            temp_model = QueryTrademarkModelEspListResponseBodyMoudleDataItemMaterialInfo()
            self.material_info = temp_model.from_map(m['MaterialInfo'])
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('PartnerCode') is not None:
            self.partner_code = m.get('PartnerCode')
        if m.get('PrincipalKey') is not None:
            self.principal_key = m.get('PrincipalKey')
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')
        if m.get('ProduceType') is not None:
            self.produce_type = m.get('ProduceType')
        if m.get('RootCode') is not None:
            temp_model = QueryTrademarkModelEspListResponseBodyMoudleDataItemRootCode()
            self.root_code = temp_model.from_map(m['RootCode'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StatusStr') is not None:
            self.status_str = m.get('StatusStr')
        if m.get('SubmitAuditTime') is not None:
            self.submit_audit_time = m.get('SubmitAuditTime')
        if m.get('SubmitStatus') is not None:
            self.submit_status = m.get('SubmitStatus')
        if m.get('SubmitTime') is not None:
            self.submit_time = m.get('SubmitTime')
        if m.get('SubmitTimes') is not None:
            self.submit_times = m.get('SubmitTimes')
        if m.get('TrademarkName') is not None:
            self.trademark_name = m.get('TrademarkName')
        if m.get('TrademarkNameType') is not None:
            self.trademark_name_type = m.get('TrademarkNameType')
        if m.get('TrademarkNumber') is not None:
            self.trademark_number = m.get('TrademarkNumber')
        return self


class QueryTrademarkModelEspListResponseBodyMoudleData(TeaModel):
    def __init__(
        self,
        item: List[QueryTrademarkModelEspListResponseBodyMoudleDataItem] = None,
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
                temp_model = QueryTrademarkModelEspListResponseBodyMoudleDataItem()
                self.item.append(temp_model.from_map(k))
        return self


class QueryTrademarkModelEspListResponseBodyMoudle(TeaModel):
    def __init__(
        self,
        data: QueryTrademarkModelEspListResponseBodyMoudleData = None,
        request_id: str = None,
        total_page_num: int = None,
    ):
        self.data = data
        self.request_id = request_id
        self.total_page_num = total_page_num

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_page_num is not None:
            result['TotalPageNum'] = self.total_page_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = QueryTrademarkModelEspListResponseBodyMoudleData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')
        return self


class QueryTrademarkModelEspListResponseBody(TeaModel):
    def __init__(
        self,
        moudle: QueryTrademarkModelEspListResponseBodyMoudle = None,
    ):
        self.moudle = moudle

    def validate(self):
        if self.moudle:
            self.moudle.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.moudle is not None:
            result['Moudle'] = self.moudle.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Moudle') is not None:
            temp_model = QueryTrademarkModelEspListResponseBodyMoudle()
            self.moudle = temp_model.from_map(m['Moudle'])
        return self


class QueryTrademarkModelEspListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryTrademarkModelEspListResponseBody = None,
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
            temp_model = QueryTrademarkModelEspListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTrademarkModelListRequest(TeaModel):
    def __init__(
        self,
        env: str = None,
        order_ids_str: str = None,
        page_num: int = None,
        page_size: int = None,
        principal_key: str = None,
        principal_name: str = None,
        produce_types_str: str = None,
        status: str = None,
        submit_start: str = None,
        submit_status: str = None,
        submit_time: str = None,
    ):
        self.env = env
        self.order_ids_str = order_ids_str
        self.page_num = page_num
        self.page_size = page_size
        self.principal_key = principal_key
        self.principal_name = principal_name
        self.produce_types_str = produce_types_str
        self.status = status
        self.submit_start = submit_start
        self.submit_status = submit_status
        self.submit_time = submit_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.env is not None:
            result['Env'] = self.env
        if self.order_ids_str is not None:
            result['OrderIdsStr'] = self.order_ids_str
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.principal_key is not None:
            result['PrincipalKey'] = self.principal_key
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name
        if self.produce_types_str is not None:
            result['ProduceTypesStr'] = self.produce_types_str
        if self.status is not None:
            result['Status'] = self.status
        if self.submit_start is not None:
            result['SubmitStart'] = self.submit_start
        if self.submit_status is not None:
            result['SubmitStatus'] = self.submit_status
        if self.submit_time is not None:
            result['SubmitTime'] = self.submit_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Env') is not None:
            self.env = m.get('Env')
        if m.get('OrderIdsStr') is not None:
            self.order_ids_str = m.get('OrderIdsStr')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PrincipalKey') is not None:
            self.principal_key = m.get('PrincipalKey')
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')
        if m.get('ProduceTypesStr') is not None:
            self.produce_types_str = m.get('ProduceTypesStr')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubmitStart') is not None:
            self.submit_start = m.get('SubmitStart')
        if m.get('SubmitStatus') is not None:
            self.submit_status = m.get('SubmitStatus')
        if m.get('SubmitTime') is not None:
            self.submit_time = m.get('SubmitTime')
        return self


class QueryTrademarkModelListResponseBodyMoudleDataItemLeafCodesLeafCode(TeaModel):
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


class QueryTrademarkModelListResponseBodyMoudleDataItemLeafCodes(TeaModel):
    def __init__(
        self,
        leaf_code: List[QueryTrademarkModelListResponseBodyMoudleDataItemLeafCodesLeafCode] = None,
    ):
        self.leaf_code = leaf_code

    def validate(self):
        if self.leaf_code:
            for k in self.leaf_code:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['leafCode'] = []
        if self.leaf_code is not None:
            for k in self.leaf_code:
                result['leafCode'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.leaf_code = []
        if m.get('leafCode') is not None:
            for k in m.get('leafCode'):
                temp_model = QueryTrademarkModelListResponseBodyMoudleDataItemLeafCodesLeafCode()
                self.leaf_code.append(temp_model.from_map(k))
        return self


class QueryTrademarkModelListResponseBodyMoudleDataItemMaterialInfo(TeaModel):
    def __init__(
        self,
        address: str = None,
        business_licence_url: str = None,
        card_number: str = None,
        cn_info_url: str = None,
        contact_address: str = None,
        contact_email: str = None,
        contact_zip_code: str = None,
        country: str = None,
        eaddress: str = None,
        ename: str = None,
        id_card_number: str = None,
        id_card_url: str = None,
        loa_key: str = None,
        loa_url: str = None,
        name: str = None,
        passport_url: str = None,
        personal_type: int = None,
        post_code: str = None,
        province: str = None,
        reason_file_oss_key: str = None,
        region: int = None,
        type: int = None,
    ):
        self.address = address
        self.business_licence_url = business_licence_url
        self.card_number = card_number
        self.cn_info_url = cn_info_url
        self.contact_address = contact_address
        self.contact_email = contact_email
        self.contact_zip_code = contact_zip_code
        self.country = country
        self.eaddress = eaddress
        self.ename = ename
        self.id_card_number = id_card_number
        self.id_card_url = id_card_url
        self.loa_key = loa_key
        self.loa_url = loa_url
        self.name = name
        self.passport_url = passport_url
        self.personal_type = personal_type
        self.post_code = post_code
        self.province = province
        self.reason_file_oss_key = reason_file_oss_key
        self.region = region
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
        if self.business_licence_url is not None:
            result['BusinessLicenceUrl'] = self.business_licence_url
        if self.card_number is not None:
            result['CardNumber'] = self.card_number
        if self.cn_info_url is not None:
            result['CnInfoUrl'] = self.cn_info_url
        if self.contact_address is not None:
            result['ContactAddress'] = self.contact_address
        if self.contact_email is not None:
            result['ContactEmail'] = self.contact_email
        if self.contact_zip_code is not None:
            result['ContactZipCode'] = self.contact_zip_code
        if self.country is not None:
            result['Country'] = self.country
        if self.eaddress is not None:
            result['EAddress'] = self.eaddress
        if self.ename is not None:
            result['EName'] = self.ename
        if self.id_card_number is not None:
            result['IdCardNumber'] = self.id_card_number
        if self.id_card_url is not None:
            result['IdCardUrl'] = self.id_card_url
        if self.loa_key is not None:
            result['LoaKey'] = self.loa_key
        if self.loa_url is not None:
            result['LoaUrl'] = self.loa_url
        if self.name is not None:
            result['Name'] = self.name
        if self.passport_url is not None:
            result['PassportUrl'] = self.passport_url
        if self.personal_type is not None:
            result['PersonalType'] = self.personal_type
        if self.post_code is not None:
            result['PostCode'] = self.post_code
        if self.province is not None:
            result['Province'] = self.province
        if self.reason_file_oss_key is not None:
            result['ReasonFileOssKey'] = self.reason_file_oss_key
        if self.region is not None:
            result['Region'] = self.region
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('BusinessLicenceUrl') is not None:
            self.business_licence_url = m.get('BusinessLicenceUrl')
        if m.get('CardNumber') is not None:
            self.card_number = m.get('CardNumber')
        if m.get('CnInfoUrl') is not None:
            self.cn_info_url = m.get('CnInfoUrl')
        if m.get('ContactAddress') is not None:
            self.contact_address = m.get('ContactAddress')
        if m.get('ContactEmail') is not None:
            self.contact_email = m.get('ContactEmail')
        if m.get('ContactZipCode') is not None:
            self.contact_zip_code = m.get('ContactZipCode')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('EAddress') is not None:
            self.eaddress = m.get('EAddress')
        if m.get('EName') is not None:
            self.ename = m.get('EName')
        if m.get('IdCardNumber') is not None:
            self.id_card_number = m.get('IdCardNumber')
        if m.get('IdCardUrl') is not None:
            self.id_card_url = m.get('IdCardUrl')
        if m.get('LoaKey') is not None:
            self.loa_key = m.get('LoaKey')
        if m.get('LoaUrl') is not None:
            self.loa_url = m.get('LoaUrl')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PassportUrl') is not None:
            self.passport_url = m.get('PassportUrl')
        if m.get('PersonalType') is not None:
            self.personal_type = m.get('PersonalType')
        if m.get('PostCode') is not None:
            self.post_code = m.get('PostCode')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        if m.get('ReasonFileOssKey') is not None:
            self.reason_file_oss_key = m.get('ReasonFileOssKey')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class QueryTrademarkModelListResponseBodyMoudleDataItemRootCode(TeaModel):
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


class QueryTrademarkModelListResponseBodyMoudleDataItem(TeaModel):
    def __init__(
        self,
        bit_flag: int = None,
        biz_id: str = None,
        biz_type: str = None,
        extend_info: Dict[str, Any] = None,
        gray_icon_url: str = None,
        icon: str = None,
        leaf_codes: QueryTrademarkModelListResponseBodyMoudleDataItemLeafCodes = None,
        material_info: QueryTrademarkModelListResponseBodyMoudleDataItemMaterialInfo = None,
        order_id: str = None,
        partner_code: str = None,
        principal_key: str = None,
        principal_name: str = None,
        produce_type: str = None,
        root_code: QueryTrademarkModelListResponseBodyMoudleDataItemRootCode = None,
        status: str = None,
        status_str: str = None,
        submit_audit_time_str: str = None,
        submit_audit_time_value: int = None,
        submit_status: str = None,
        submit_time_str: str = None,
        submit_time_value: int = None,
        submit_times: int = None,
        trademark_name: str = None,
        trademark_name_type: int = None,
        trademark_number: str = None,
    ):
        self.bit_flag = bit_flag
        self.biz_id = biz_id
        self.biz_type = biz_type
        self.extend_info = extend_info
        self.gray_icon_url = gray_icon_url
        self.icon = icon
        self.leaf_codes = leaf_codes
        self.material_info = material_info
        self.order_id = order_id
        self.partner_code = partner_code
        self.principal_key = principal_key
        self.principal_name = principal_name
        self.produce_type = produce_type
        self.root_code = root_code
        self.status = status
        self.status_str = status_str
        self.submit_audit_time_str = submit_audit_time_str
        self.submit_audit_time_value = submit_audit_time_value
        self.submit_status = submit_status
        self.submit_time_str = submit_time_str
        self.submit_time_value = submit_time_value
        self.submit_times = submit_times
        self.trademark_name = trademark_name
        self.trademark_name_type = trademark_name_type
        self.trademark_number = trademark_number

    def validate(self):
        if self.leaf_codes:
            self.leaf_codes.validate()
        if self.material_info:
            self.material_info.validate()
        if self.root_code:
            self.root_code.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bit_flag is not None:
            result['BitFlag'] = self.bit_flag
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.extend_info is not None:
            result['ExtendInfo'] = self.extend_info
        if self.gray_icon_url is not None:
            result['GrayIconUrl'] = self.gray_icon_url
        if self.icon is not None:
            result['Icon'] = self.icon
        if self.leaf_codes is not None:
            result['LeafCodes'] = self.leaf_codes.to_map()
        if self.material_info is not None:
            result['MaterialInfo'] = self.material_info.to_map()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.partner_code is not None:
            result['PartnerCode'] = self.partner_code
        if self.principal_key is not None:
            result['PrincipalKey'] = self.principal_key
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name
        if self.produce_type is not None:
            result['ProduceType'] = self.produce_type
        if self.root_code is not None:
            result['RootCode'] = self.root_code.to_map()
        if self.status is not None:
            result['Status'] = self.status
        if self.status_str is not None:
            result['StatusStr'] = self.status_str
        if self.submit_audit_time_str is not None:
            result['SubmitAuditTimeStr'] = self.submit_audit_time_str
        if self.submit_audit_time_value is not None:
            result['SubmitAuditTimeValue'] = self.submit_audit_time_value
        if self.submit_status is not None:
            result['SubmitStatus'] = self.submit_status
        if self.submit_time_str is not None:
            result['SubmitTimeStr'] = self.submit_time_str
        if self.submit_time_value is not None:
            result['SubmitTimeValue'] = self.submit_time_value
        if self.submit_times is not None:
            result['SubmitTimes'] = self.submit_times
        if self.trademark_name is not None:
            result['TrademarkName'] = self.trademark_name
        if self.trademark_name_type is not None:
            result['TrademarkNameType'] = self.trademark_name_type
        if self.trademark_number is not None:
            result['TrademarkNumber'] = self.trademark_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BitFlag') is not None:
            self.bit_flag = m.get('BitFlag')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('ExtendInfo') is not None:
            self.extend_info = m.get('ExtendInfo')
        if m.get('GrayIconUrl') is not None:
            self.gray_icon_url = m.get('GrayIconUrl')
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        if m.get('LeafCodes') is not None:
            temp_model = QueryTrademarkModelListResponseBodyMoudleDataItemLeafCodes()
            self.leaf_codes = temp_model.from_map(m['LeafCodes'])
        if m.get('MaterialInfo') is not None:
            temp_model = QueryTrademarkModelListResponseBodyMoudleDataItemMaterialInfo()
            self.material_info = temp_model.from_map(m['MaterialInfo'])
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('PartnerCode') is not None:
            self.partner_code = m.get('PartnerCode')
        if m.get('PrincipalKey') is not None:
            self.principal_key = m.get('PrincipalKey')
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')
        if m.get('ProduceType') is not None:
            self.produce_type = m.get('ProduceType')
        if m.get('RootCode') is not None:
            temp_model = QueryTrademarkModelListResponseBodyMoudleDataItemRootCode()
            self.root_code = temp_model.from_map(m['RootCode'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StatusStr') is not None:
            self.status_str = m.get('StatusStr')
        if m.get('SubmitAuditTimeStr') is not None:
            self.submit_audit_time_str = m.get('SubmitAuditTimeStr')
        if m.get('SubmitAuditTimeValue') is not None:
            self.submit_audit_time_value = m.get('SubmitAuditTimeValue')
        if m.get('SubmitStatus') is not None:
            self.submit_status = m.get('SubmitStatus')
        if m.get('SubmitTimeStr') is not None:
            self.submit_time_str = m.get('SubmitTimeStr')
        if m.get('SubmitTimeValue') is not None:
            self.submit_time_value = m.get('SubmitTimeValue')
        if m.get('SubmitTimes') is not None:
            self.submit_times = m.get('SubmitTimes')
        if m.get('TrademarkName') is not None:
            self.trademark_name = m.get('TrademarkName')
        if m.get('TrademarkNameType') is not None:
            self.trademark_name_type = m.get('TrademarkNameType')
        if m.get('TrademarkNumber') is not None:
            self.trademark_number = m.get('TrademarkNumber')
        return self


class QueryTrademarkModelListResponseBodyMoudleData(TeaModel):
    def __init__(
        self,
        item: List[QueryTrademarkModelListResponseBodyMoudleDataItem] = None,
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
                temp_model = QueryTrademarkModelListResponseBodyMoudleDataItem()
                self.item.append(temp_model.from_map(k))
        return self


class QueryTrademarkModelListResponseBodyMoudle(TeaModel):
    def __init__(
        self,
        data: QueryTrademarkModelListResponseBodyMoudleData = None,
        request_id: str = None,
        total_page_num: int = None,
    ):
        self.data = data
        self.request_id = request_id
        self.total_page_num = total_page_num

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_page_num is not None:
            result['TotalPageNum'] = self.total_page_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = QueryTrademarkModelListResponseBodyMoudleData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')
        return self


class QueryTrademarkModelListResponseBody(TeaModel):
    def __init__(
        self,
        moudle: QueryTrademarkModelListResponseBodyMoudle = None,
    ):
        self.moudle = moudle

    def validate(self):
        if self.moudle:
            self.moudle.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.moudle is not None:
            result['Moudle'] = self.moudle.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Moudle') is not None:
            temp_model = QueryTrademarkModelListResponseBodyMoudle()
            self.moudle = temp_model.from_map(m['Moudle'])
        return self


class QueryTrademarkModelListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryTrademarkModelListResponseBody = None,
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
            temp_model = QueryTrademarkModelListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTrademarkMonitorResultsRequest(TeaModel):
    def __init__(
        self,
        action_type: int = None,
        apply_year: str = None,
        classification: str = None,
        page_num: int = None,
        page_size: int = None,
        procedure_status: int = None,
        registration_number: str = None,
        rule_id: int = None,
        tm_name: str = None,
    ):
        self.action_type = action_type
        self.apply_year = apply_year
        self.classification = classification
        self.page_num = page_num
        self.page_size = page_size
        self.procedure_status = procedure_status
        self.registration_number = registration_number
        self.rule_id = rule_id
        self.tm_name = tm_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_type is not None:
            result['ActionType'] = self.action_type
        if self.apply_year is not None:
            result['ApplyYear'] = self.apply_year
        if self.classification is not None:
            result['Classification'] = self.classification
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.procedure_status is not None:
            result['ProcedureStatus'] = self.procedure_status
        if self.registration_number is not None:
            result['RegistrationNumber'] = self.registration_number
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.tm_name is not None:
            result['TmName'] = self.tm_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionType') is not None:
            self.action_type = m.get('ActionType')
        if m.get('ApplyYear') is not None:
            self.apply_year = m.get('ApplyYear')
        if m.get('Classification') is not None:
            self.classification = m.get('Classification')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProcedureStatus') is not None:
            self.procedure_status = m.get('ProcedureStatus')
        if m.get('RegistrationNumber') is not None:
            self.registration_number = m.get('RegistrationNumber')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('TmName') is not None:
            self.tm_name = m.get('TmName')
        return self


class QueryTrademarkMonitorResultsResponseBodyDataTmMonitorResult(TeaModel):
    def __init__(
        self,
        apply_date: str = None,
        chesan_end_date: str = None,
        classification: str = None,
        data_create_time: int = None,
        data_update_time: int = None,
        owner_en_name: str = None,
        owner_name: str = None,
        registration_number: str = None,
        rule_id: str = None,
        tm_image: str = None,
        tm_name: str = None,
        tm_procedure_status_desc: str = None,
        tm_uid: str = None,
        user_id: str = None,
        wuxiao_end_date: str = None,
        xuzhan_end_date: str = None,
        yiyi_end_date: str = None,
    ):
        self.apply_date = apply_date
        self.chesan_end_date = chesan_end_date
        self.classification = classification
        self.data_create_time = data_create_time
        self.data_update_time = data_update_time
        self.owner_en_name = owner_en_name
        self.owner_name = owner_name
        self.registration_number = registration_number
        self.rule_id = rule_id
        self.tm_image = tm_image
        self.tm_name = tm_name
        self.tm_procedure_status_desc = tm_procedure_status_desc
        self.tm_uid = tm_uid
        self.user_id = user_id
        self.wuxiao_end_date = wuxiao_end_date
        self.xuzhan_end_date = xuzhan_end_date
        self.yiyi_end_date = yiyi_end_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apply_date is not None:
            result['ApplyDate'] = self.apply_date
        if self.chesan_end_date is not None:
            result['ChesanEndDate'] = self.chesan_end_date
        if self.classification is not None:
            result['Classification'] = self.classification
        if self.data_create_time is not None:
            result['DataCreateTime'] = self.data_create_time
        if self.data_update_time is not None:
            result['DataUpdateTime'] = self.data_update_time
        if self.owner_en_name is not None:
            result['OwnerEnName'] = self.owner_en_name
        if self.owner_name is not None:
            result['OwnerName'] = self.owner_name
        if self.registration_number is not None:
            result['RegistrationNumber'] = self.registration_number
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.tm_image is not None:
            result['TmImage'] = self.tm_image
        if self.tm_name is not None:
            result['TmName'] = self.tm_name
        if self.tm_procedure_status_desc is not None:
            result['TmProcedureStatusDesc'] = self.tm_procedure_status_desc
        if self.tm_uid is not None:
            result['TmUid'] = self.tm_uid
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.wuxiao_end_date is not None:
            result['WuxiaoEndDate'] = self.wuxiao_end_date
        if self.xuzhan_end_date is not None:
            result['XuzhanEndDate'] = self.xuzhan_end_date
        if self.yiyi_end_date is not None:
            result['YiyiEndDate'] = self.yiyi_end_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplyDate') is not None:
            self.apply_date = m.get('ApplyDate')
        if m.get('ChesanEndDate') is not None:
            self.chesan_end_date = m.get('ChesanEndDate')
        if m.get('Classification') is not None:
            self.classification = m.get('Classification')
        if m.get('DataCreateTime') is not None:
            self.data_create_time = m.get('DataCreateTime')
        if m.get('DataUpdateTime') is not None:
            self.data_update_time = m.get('DataUpdateTime')
        if m.get('OwnerEnName') is not None:
            self.owner_en_name = m.get('OwnerEnName')
        if m.get('OwnerName') is not None:
            self.owner_name = m.get('OwnerName')
        if m.get('RegistrationNumber') is not None:
            self.registration_number = m.get('RegistrationNumber')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('TmImage') is not None:
            self.tm_image = m.get('TmImage')
        if m.get('TmName') is not None:
            self.tm_name = m.get('TmName')
        if m.get('TmProcedureStatusDesc') is not None:
            self.tm_procedure_status_desc = m.get('TmProcedureStatusDesc')
        if m.get('TmUid') is not None:
            self.tm_uid = m.get('TmUid')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('WuxiaoEndDate') is not None:
            self.wuxiao_end_date = m.get('WuxiaoEndDate')
        if m.get('XuzhanEndDate') is not None:
            self.xuzhan_end_date = m.get('XuzhanEndDate')
        if m.get('YiyiEndDate') is not None:
            self.yiyi_end_date = m.get('YiyiEndDate')
        return self


class QueryTrademarkMonitorResultsResponseBodyData(TeaModel):
    def __init__(
        self,
        tm_monitor_result: List[QueryTrademarkMonitorResultsResponseBodyDataTmMonitorResult] = None,
    ):
        self.tm_monitor_result = tm_monitor_result

    def validate(self):
        if self.tm_monitor_result:
            for k in self.tm_monitor_result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TmMonitorResult'] = []
        if self.tm_monitor_result is not None:
            for k in self.tm_monitor_result:
                result['TmMonitorResult'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tm_monitor_result = []
        if m.get('TmMonitorResult') is not None:
            for k in m.get('TmMonitorResult'):
                temp_model = QueryTrademarkMonitorResultsResponseBodyDataTmMonitorResult()
                self.tm_monitor_result.append(temp_model.from_map(k))
        return self


class QueryTrademarkMonitorResultsResponseBody(TeaModel):
    def __init__(
        self,
        current_page_num: int = None,
        data: QueryTrademarkMonitorResultsResponseBodyData = None,
        next_page: bool = None,
        page_size: int = None,
        pre_page: bool = None,
        request_id: str = None,
        total_item_num: int = None,
        total_page_num: int = None,
    ):
        self.current_page_num = current_page_num
        self.data = data
        self.next_page = next_page
        self.page_size = page_size
        self.pre_page = pre_page
        self.request_id = request_id
        self.total_item_num = total_item_num
        self.total_page_num = total_page_num

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page_num is not None:
            result['CurrentPageNum'] = self.current_page_num
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.next_page is not None:
            result['NextPage'] = self.next_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.pre_page is not None:
            result['PrePage'] = self.pre_page
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_item_num is not None:
            result['TotalItemNum'] = self.total_item_num
        if self.total_page_num is not None:
            result['TotalPageNum'] = self.total_page_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPageNum') is not None:
            self.current_page_num = m.get('CurrentPageNum')
        if m.get('Data') is not None:
            temp_model = QueryTrademarkMonitorResultsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('NextPage') is not None:
            self.next_page = m.get('NextPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PrePage') is not None:
            self.pre_page = m.get('PrePage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalItemNum') is not None:
            self.total_item_num = m.get('TotalItemNum')
        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')
        return self


class QueryTrademarkMonitorResultsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryTrademarkMonitorResultsResponseBody = None,
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
            temp_model = QueryTrademarkMonitorResultsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTrademarkMonitorRulesRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        notify_update: int = None,
        page_num: int = None,
        page_size: int = None,
        rule_name: str = None,
    ):
        self.id = id
        self.notify_update = notify_update
        self.page_num = page_num
        self.page_size = page_size
        self.rule_name = rule_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.notify_update is not None:
            result['NotifyUpdate'] = self.notify_update
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('NotifyUpdate') is not None:
            self.notify_update = m.get('NotifyUpdate')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        return self


class QueryTrademarkMonitorRulesResponseBodyDataTmMonitorRule(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        end_time: str = None,
        env: str = None,
        id: str = None,
        last_finish_time: str = None,
        last_run_time: str = None,
        last_update_time: str = None,
        notify_update: int = None,
        rule_detail: str = None,
        rule_extend: str = None,
        rule_keyword: str = None,
        rule_name: str = None,
        rule_source: str = None,
        rule_status: str = None,
        rule_type: int = None,
        start_time: str = None,
        update_time: str = None,
        user_id: str = None,
        version: int = None,
    ):
        self.create_time = create_time
        self.end_time = end_time
        self.env = env
        self.id = id
        self.last_finish_time = last_finish_time
        self.last_run_time = last_run_time
        self.last_update_time = last_update_time
        self.notify_update = notify_update
        self.rule_detail = rule_detail
        self.rule_extend = rule_extend
        self.rule_keyword = rule_keyword
        self.rule_name = rule_name
        self.rule_source = rule_source
        self.rule_status = rule_status
        self.rule_type = rule_type
        self.start_time = start_time
        self.update_time = update_time
        self.user_id = user_id
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.env is not None:
            result['Env'] = self.env
        if self.id is not None:
            result['Id'] = self.id
        if self.last_finish_time is not None:
            result['LastFinishTime'] = self.last_finish_time
        if self.last_run_time is not None:
            result['LastRunTime'] = self.last_run_time
        if self.last_update_time is not None:
            result['LastUpdateTime'] = self.last_update_time
        if self.notify_update is not None:
            result['NotifyUpdate'] = self.notify_update
        if self.rule_detail is not None:
            result['RuleDetail'] = self.rule_detail
        if self.rule_extend is not None:
            result['RuleExtend'] = self.rule_extend
        if self.rule_keyword is not None:
            result['RuleKeyword'] = self.rule_keyword
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.rule_source is not None:
            result['RuleSource'] = self.rule_source
        if self.rule_status is not None:
            result['RuleStatus'] = self.rule_status
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Env') is not None:
            self.env = m.get('Env')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LastFinishTime') is not None:
            self.last_finish_time = m.get('LastFinishTime')
        if m.get('LastRunTime') is not None:
            self.last_run_time = m.get('LastRunTime')
        if m.get('LastUpdateTime') is not None:
            self.last_update_time = m.get('LastUpdateTime')
        if m.get('NotifyUpdate') is not None:
            self.notify_update = m.get('NotifyUpdate')
        if m.get('RuleDetail') is not None:
            self.rule_detail = m.get('RuleDetail')
        if m.get('RuleExtend') is not None:
            self.rule_extend = m.get('RuleExtend')
        if m.get('RuleKeyword') is not None:
            self.rule_keyword = m.get('RuleKeyword')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('RuleSource') is not None:
            self.rule_source = m.get('RuleSource')
        if m.get('RuleStatus') is not None:
            self.rule_status = m.get('RuleStatus')
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class QueryTrademarkMonitorRulesResponseBodyData(TeaModel):
    def __init__(
        self,
        tm_monitor_rule: List[QueryTrademarkMonitorRulesResponseBodyDataTmMonitorRule] = None,
    ):
        self.tm_monitor_rule = tm_monitor_rule

    def validate(self):
        if self.tm_monitor_rule:
            for k in self.tm_monitor_rule:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TmMonitorRule'] = []
        if self.tm_monitor_rule is not None:
            for k in self.tm_monitor_rule:
                result['TmMonitorRule'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tm_monitor_rule = []
        if m.get('TmMonitorRule') is not None:
            for k in m.get('TmMonitorRule'):
                temp_model = QueryTrademarkMonitorRulesResponseBodyDataTmMonitorRule()
                self.tm_monitor_rule.append(temp_model.from_map(k))
        return self


class QueryTrademarkMonitorRulesResponseBody(TeaModel):
    def __init__(
        self,
        current_page_num: int = None,
        data: QueryTrademarkMonitorRulesResponseBodyData = None,
        next_page: bool = None,
        page_size: int = None,
        pre_page: bool = None,
        request_id: str = None,
        total_item_num: int = None,
        total_page_num: int = None,
    ):
        self.current_page_num = current_page_num
        self.data = data
        self.next_page = next_page
        self.page_size = page_size
        self.pre_page = pre_page
        self.request_id = request_id
        self.total_item_num = total_item_num
        self.total_page_num = total_page_num

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page_num is not None:
            result['CurrentPageNum'] = self.current_page_num
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.next_page is not None:
            result['NextPage'] = self.next_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.pre_page is not None:
            result['PrePage'] = self.pre_page
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_item_num is not None:
            result['TotalItemNum'] = self.total_item_num
        if self.total_page_num is not None:
            result['TotalPageNum'] = self.total_page_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPageNum') is not None:
            self.current_page_num = m.get('CurrentPageNum')
        if m.get('Data') is not None:
            temp_model = QueryTrademarkMonitorRulesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('NextPage') is not None:
            self.next_page = m.get('NextPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PrePage') is not None:
            self.pre_page = m.get('PrePage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalItemNum') is not None:
            self.total_item_num = m.get('TotalItemNum')
        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')
        return self


class QueryTrademarkMonitorRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryTrademarkMonitorRulesResponseBody = None,
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
            temp_model = QueryTrademarkMonitorRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTrademarkOnSaleRequest(TeaModel):
    def __init__(
        self,
        classification: str = None,
        page_num: int = None,
        page_size: int = None,
        register_code: str = None,
        register_number: str = None,
        tm_type: str = None,
    ):
        self.classification = classification
        self.page_num = page_num
        self.page_size = page_size
        self.register_code = register_code
        self.register_number = register_number
        self.tm_type = tm_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.classification is not None:
            result['Classification'] = self.classification
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.register_code is not None:
            result['RegisterCode'] = self.register_code
        if self.register_number is not None:
            result['RegisterNumber'] = self.register_number
        if self.tm_type is not None:
            result['TmType'] = self.tm_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Classification') is not None:
            self.classification = m.get('Classification')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegisterCode') is not None:
            self.register_code = m.get('RegisterCode')
        if m.get('RegisterNumber') is not None:
            self.register_number = m.get('RegisterNumber')
        if m.get('TmType') is not None:
            self.tm_type = m.get('TmType')
        return self


class QueryTrademarkOnSaleResponseBodyTrademarks(TeaModel):
    def __init__(
        self,
        audit_result: str = None,
        classification: str = None,
        icon: str = None,
        order_price: str = None,
        registration_number: str = None,
        status: int = None,
        tm_type: str = None,
        trademark_name: str = None,
    ):
        self.audit_result = audit_result
        self.classification = classification
        self.icon = icon
        self.order_price = order_price
        self.registration_number = registration_number
        self.status = status
        self.tm_type = tm_type
        self.trademark_name = trademark_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audit_result is not None:
            result['AuditResult'] = self.audit_result
        if self.classification is not None:
            result['Classification'] = self.classification
        if self.icon is not None:
            result['Icon'] = self.icon
        if self.order_price is not None:
            result['OrderPrice'] = self.order_price
        if self.registration_number is not None:
            result['RegistrationNumber'] = self.registration_number
        if self.status is not None:
            result['Status'] = self.status
        if self.tm_type is not None:
            result['TmType'] = self.tm_type
        if self.trademark_name is not None:
            result['TrademarkName'] = self.trademark_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuditResult') is not None:
            self.audit_result = m.get('AuditResult')
        if m.get('Classification') is not None:
            self.classification = m.get('Classification')
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        if m.get('OrderPrice') is not None:
            self.order_price = m.get('OrderPrice')
        if m.get('RegistrationNumber') is not None:
            self.registration_number = m.get('RegistrationNumber')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TmType') is not None:
            self.tm_type = m.get('TmType')
        if m.get('TrademarkName') is not None:
            self.trademark_name = m.get('TrademarkName')
        return self


class QueryTrademarkOnSaleResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        total_page_number: int = None,
        trademarks: List[QueryTrademarkOnSaleResponseBodyTrademarks] = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count
        self.total_page_number = total_page_number
        self.trademarks = trademarks

    def validate(self):
        if self.trademarks:
            for k in self.trademarks:
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
        if self.total_page_number is not None:
            result['TotalPageNumber'] = self.total_page_number
        result['Trademarks'] = []
        if self.trademarks is not None:
            for k in self.trademarks:
                result['Trademarks'].append(k.to_map() if k else None)
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
        if m.get('TotalPageNumber') is not None:
            self.total_page_number = m.get('TotalPageNumber')
        self.trademarks = []
        if m.get('Trademarks') is not None:
            for k in m.get('Trademarks'):
                temp_model = QueryTrademarkOnSaleResponseBodyTrademarks()
                self.trademarks.append(temp_model.from_map(k))
        return self


class QueryTrademarkOnSaleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryTrademarkOnSaleResponseBody = None,
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
            temp_model = QueryTrademarkOnSaleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTrademarkPriceRequest(TeaModel):
    def __init__(
        self,
        order_data: Dict[str, Any] = None,
        tm_icon: str = None,
        tm_name: str = None,
        type: int = None,
        user_id: int = None,
    ):
        self.order_data = order_data
        self.tm_icon = tm_icon
        self.tm_name = tm_name
        self.type = type
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_data is not None:
            result['OrderData'] = self.order_data
        if self.tm_icon is not None:
            result['TmIcon'] = self.tm_icon
        if self.tm_name is not None:
            result['TmName'] = self.tm_name
        if self.type is not None:
            result['Type'] = self.type
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderData') is not None:
            self.order_data = m.get('OrderData')
        if m.get('TmIcon') is not None:
            self.tm_icon = m.get('TmIcon')
        if m.get('TmName') is not None:
            self.tm_name = m.get('TmName')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class QueryTrademarkPriceShrinkRequest(TeaModel):
    def __init__(
        self,
        order_data_shrink: str = None,
        tm_icon: str = None,
        tm_name: str = None,
        type: int = None,
        user_id: int = None,
    ):
        self.order_data_shrink = order_data_shrink
        self.tm_icon = tm_icon
        self.tm_name = tm_name
        self.type = type
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_data_shrink is not None:
            result['OrderData'] = self.order_data_shrink
        if self.tm_icon is not None:
            result['TmIcon'] = self.tm_icon
        if self.tm_name is not None:
            result['TmName'] = self.tm_name
        if self.type is not None:
            result['Type'] = self.type
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderData') is not None:
            self.order_data_shrink = m.get('OrderData')
        if m.get('TmIcon') is not None:
            self.tm_icon = m.get('TmIcon')
        if m.get('TmName') is not None:
            self.tm_name = m.get('TmName')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class QueryTrademarkPriceResponseBodyPricesPrices(TeaModel):
    def __init__(
        self,
        classification_code: str = None,
        currency: str = None,
        discount_price: float = None,
        original_price: float = None,
        trade_price: float = None,
    ):
        self.classification_code = classification_code
        self.currency = currency
        self.discount_price = discount_price
        self.original_price = original_price
        self.trade_price = trade_price

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.classification_code is not None:
            result['ClassificationCode'] = self.classification_code
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.discount_price is not None:
            result['DiscountPrice'] = self.discount_price
        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price
        if self.trade_price is not None:
            result['TradePrice'] = self.trade_price
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClassificationCode') is not None:
            self.classification_code = m.get('ClassificationCode')
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('DiscountPrice') is not None:
            self.discount_price = m.get('DiscountPrice')
        if m.get('OriginalPrice') is not None:
            self.original_price = m.get('OriginalPrice')
        if m.get('TradePrice') is not None:
            self.trade_price = m.get('TradePrice')
        return self


class QueryTrademarkPriceResponseBodyPrices(TeaModel):
    def __init__(
        self,
        prices: List[QueryTrademarkPriceResponseBodyPricesPrices] = None,
    ):
        self.prices = prices

    def validate(self):
        if self.prices:
            for k in self.prices:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Prices'] = []
        if self.prices is not None:
            for k in self.prices:
                result['Prices'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.prices = []
        if m.get('Prices') is not None:
            for k in m.get('Prices'):
                temp_model = QueryTrademarkPriceResponseBodyPricesPrices()
                self.prices.append(temp_model.from_map(k))
        return self


class QueryTrademarkPriceResponseBody(TeaModel):
    def __init__(
        self,
        currency: str = None,
        discount_price: float = None,
        original_price: float = None,
        prices: QueryTrademarkPriceResponseBodyPrices = None,
        request_id: str = None,
        trade_price: float = None,
    ):
        self.currency = currency
        self.discount_price = discount_price
        self.original_price = original_price
        self.prices = prices
        self.request_id = request_id
        self.trade_price = trade_price

    def validate(self):
        if self.prices:
            self.prices.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.discount_price is not None:
            result['DiscountPrice'] = self.discount_price
        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price
        if self.prices is not None:
            result['Prices'] = self.prices.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.trade_price is not None:
            result['TradePrice'] = self.trade_price
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('DiscountPrice') is not None:
            self.discount_price = m.get('DiscountPrice')
        if m.get('OriginalPrice') is not None:
            self.original_price = m.get('OriginalPrice')
        if m.get('Prices') is not None:
            temp_model = QueryTrademarkPriceResponseBodyPrices()
            self.prices = temp_model.from_map(m['Prices'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TradePrice') is not None:
            self.trade_price = m.get('TradePrice')
        return self


class QueryTrademarkPriceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryTrademarkPriceResponseBody = None,
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
            temp_model = QueryTrademarkPriceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTrademarkUploadAuditResultRequest(TeaModel):
    def __init__(
        self,
        classification: str = None,
        page_num: int = None,
        page_size: int = None,
        register_code: str = None,
        register_number: str = None,
        tm_type: str = None,
    ):
        self.classification = classification
        self.page_num = page_num
        self.page_size = page_size
        self.register_code = register_code
        self.register_number = register_number
        self.tm_type = tm_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.classification is not None:
            result['Classification'] = self.classification
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.register_code is not None:
            result['RegisterCode'] = self.register_code
        if self.register_number is not None:
            result['RegisterNumber'] = self.register_number
        if self.tm_type is not None:
            result['TmType'] = self.tm_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Classification') is not None:
            self.classification = m.get('Classification')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegisterCode') is not None:
            self.register_code = m.get('RegisterCode')
        if m.get('RegisterNumber') is not None:
            self.register_number = m.get('RegisterNumber')
        if m.get('TmType') is not None:
            self.tm_type = m.get('TmType')
        return self


class QueryTrademarkUploadAuditResultResponseBodyTrademarks(TeaModel):
    def __init__(
        self,
        audit_result: str = None,
        classification: str = None,
        icon: str = None,
        order_price: str = None,
        registration_number: str = None,
        status: int = None,
        tm_type: str = None,
        trademark_name: str = None,
    ):
        self.audit_result = audit_result
        self.classification = classification
        self.icon = icon
        self.order_price = order_price
        self.registration_number = registration_number
        self.status = status
        self.tm_type = tm_type
        self.trademark_name = trademark_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audit_result is not None:
            result['AuditResult'] = self.audit_result
        if self.classification is not None:
            result['Classification'] = self.classification
        if self.icon is not None:
            result['Icon'] = self.icon
        if self.order_price is not None:
            result['OrderPrice'] = self.order_price
        if self.registration_number is not None:
            result['RegistrationNumber'] = self.registration_number
        if self.status is not None:
            result['Status'] = self.status
        if self.tm_type is not None:
            result['TmType'] = self.tm_type
        if self.trademark_name is not None:
            result['TrademarkName'] = self.trademark_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuditResult') is not None:
            self.audit_result = m.get('AuditResult')
        if m.get('Classification') is not None:
            self.classification = m.get('Classification')
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        if m.get('OrderPrice') is not None:
            self.order_price = m.get('OrderPrice')
        if m.get('RegistrationNumber') is not None:
            self.registration_number = m.get('RegistrationNumber')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TmType') is not None:
            self.tm_type = m.get('TmType')
        if m.get('TrademarkName') is not None:
            self.trademark_name = m.get('TrademarkName')
        return self


class QueryTrademarkUploadAuditResultResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        total_page_number: int = None,
        trademarks: List[QueryTrademarkUploadAuditResultResponseBodyTrademarks] = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count
        self.total_page_number = total_page_number
        self.trademarks = trademarks

    def validate(self):
        if self.trademarks:
            for k in self.trademarks:
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
        if self.total_page_number is not None:
            result['TotalPageNumber'] = self.total_page_number
        result['Trademarks'] = []
        if self.trademarks is not None:
            for k in self.trademarks:
                result['Trademarks'].append(k.to_map() if k else None)
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
        if m.get('TotalPageNumber') is not None:
            self.total_page_number = m.get('TotalPageNumber')
        self.trademarks = []
        if m.get('Trademarks') is not None:
            for k in m.get('Trademarks'):
                temp_model = QueryTrademarkUploadAuditResultResponseBodyTrademarks()
                self.trademarks.append(temp_model.from_map(k))
        return self


class QueryTrademarkUploadAuditResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryTrademarkUploadAuditResultResponseBody = None,
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
            temp_model = QueryTrademarkUploadAuditResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecordBankBalanceRequest(TeaModel):
    def __init__(
        self,
        action_date: int = None,
        balance: str = None,
        principal_name: str = None,
    ):
        self.action_date = action_date
        self.balance = balance
        self.principal_name = principal_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_date is not None:
            result['ActionDate'] = self.action_date
        if self.balance is not None:
            result['Balance'] = self.balance
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionDate') is not None:
            self.action_date = m.get('ActionDate')
        if m.get('Balance') is not None:
            self.balance = m.get('Balance')
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')
        return self


class RecordBankBalanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
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


class RecordBankBalanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RecordBankBalanceResponseBody = None,
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
            temp_model = RecordBankBalanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RefundProduceRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        refund_type: str = None,
    ):
        self.biz_id = biz_id
        self.refund_type = refund_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.refund_type is not None:
            result['RefundType'] = self.refund_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('RefundType') is not None:
            self.refund_type = m.get('RefundType')
        return self


class RefundProduceResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_msg = error_msg
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
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RefundProduceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RefundProduceResponseBody = None,
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
            temp_model = RefundProduceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RefuseAdditionalMaterialRequest(TeaModel):
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


class RefuseAdditionalMaterialResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_msg = error_msg
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
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RefuseAdditionalMaterialResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RefuseAdditionalMaterialResponseBody = None,
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
            temp_model = RefuseAdditionalMaterialResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RefuseApplicantRequest(TeaModel):
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


class RefuseApplicantResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_msg = error_msg
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
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RefuseApplicantResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RefuseApplicantResponseBody = None,
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
            temp_model = RefuseApplicantResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RejectApplicantRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        note: str = None,
    ):
        self.instance_id = instance_id
        self.note = note

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.note is not None:
            result['Note'] = self.note
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        return self


class RejectApplicantResponseBody(TeaModel):
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


class RejectApplicantResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RejectApplicantResponseBody = None,
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
            temp_model = RejectApplicantResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveClassificationConditionsRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        condition: str = None,
        type: int = None,
    ):
        self.biz_id = biz_id
        self.condition = condition
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.condition is not None:
            result['Condition'] = self.condition
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Condition') is not None:
            self.condition = m.get('Condition')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class SaveClassificationConditionsResponseBodyInvalidList(TeaModel):
    def __init__(
        self,
        classification_code: str = None,
        classification_name: str = None,
        official_code: str = None,
        parent_code: str = None,
    ):
        self.classification_code = classification_code
        self.classification_name = classification_name
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
        if m.get('OfficialCode') is not None:
            self.official_code = m.get('OfficialCode')
        if m.get('ParentCode') is not None:
            self.parent_code = m.get('ParentCode')
        return self


class SaveClassificationConditionsResponseBody(TeaModel):
    def __init__(
        self,
        error_msg: str = None,
        invalid_list: List[SaveClassificationConditionsResponseBodyInvalidList] = None,
        request_id: str = None,
        success: bool = None,
        tag_name: str = None,
    ):
        self.error_msg = error_msg
        self.invalid_list = invalid_list
        self.request_id = request_id
        self.success = success
        self.tag_name = tag_name

    def validate(self):
        if self.invalid_list:
            for k in self.invalid_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        result['InvalidList'] = []
        if self.invalid_list is not None:
            for k in self.invalid_list:
                result['InvalidList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.tag_name is not None:
            result['TagName'] = self.tag_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        self.invalid_list = []
        if m.get('InvalidList') is not None:
            for k in m.get('InvalidList'):
                temp_model = SaveClassificationConditionsResponseBodyInvalidList()
                self.invalid_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')
        return self


class SaveClassificationConditionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SaveClassificationConditionsResponseBody = None,
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
            temp_model = SaveClassificationConditionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveExtensionAttributeRequest(TeaModel):
    def __init__(
        self,
        attribute_key: str = None,
        attribute_value: str = None,
        biz_id: str = None,
    ):
        self.attribute_key = attribute_key
        self.attribute_value = attribute_value
        self.biz_id = biz_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attribute_key is not None:
            result['AttributeKey'] = self.attribute_key
        if self.attribute_value is not None:
            result['AttributeValue'] = self.attribute_value
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttributeKey') is not None:
            self.attribute_key = m.get('AttributeKey')
        if m.get('AttributeValue') is not None:
            self.attribute_value = m.get('AttributeValue')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        return self


class SaveExtensionAttributeResponseBody(TeaModel):
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


class SaveExtensionAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SaveExtensionAttributeResponseBody = None,
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
            temp_model = SaveExtensionAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveTaskRequest(TeaModel):
    def __init__(
        self,
        biz_type: str = None,
        request: str = None,
    ):
        self.biz_type = biz_type
        self.request = request

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.request is not None:
            result['Request'] = self.request
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('Request') is not None:
            self.request = m.get('Request')
        return self


class SaveTaskResponseBody(TeaModel):
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


class SaveTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SaveTaskResponseBody = None,
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
            temp_model = SaveTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveTaskForOfficialFileCustomRequest(TeaModel):
    def __init__(
        self,
        end_accept_time: int = None,
        start_accept_time: int = None,
    ):
        self.end_accept_time = end_accept_time
        self.start_accept_time = start_accept_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_accept_time is not None:
            result['EndAcceptTime'] = self.end_accept_time
        if self.start_accept_time is not None:
            result['StartAcceptTime'] = self.start_accept_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndAcceptTime') is not None:
            self.end_accept_time = m.get('EndAcceptTime')
        if m.get('StartAcceptTime') is not None:
            self.start_accept_time = m.get('StartAcceptTime')
        return self


class SaveTaskForOfficialFileCustomResponseBody(TeaModel):
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


class SaveTaskForOfficialFileCustomResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SaveTaskForOfficialFileCustomResponseBody = None,
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
            temp_model = SaveTaskForOfficialFileCustomResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveTradeMarkReviewMaterialDetailRequest(TeaModel):
    def __init__(
        self,
        additional_oss_key_list: Dict[str, Any] = None,
        address: str = None,
        application_oss_key: str = None,
        biz_id: str = None,
        business_licence_oss_key: str = None,
        card_number: str = None,
        change_name: bool = None,
        contact_address: str = None,
        contact_email: str = None,
        contact_name: str = None,
        contact_number: str = None,
        country: str = None,
        eng_address: str = None,
        eng_name: str = None,
        id_card_oss_key: str = None,
        legal_notice_oss_key: str = None,
        loa_oss_key: str = None,
        name: str = None,
        passport_oss_key: str = None,
        province: str = None,
        region: int = None,
        review_material_additional_json: str = None,
        separate: bool = None,
        submit_online: bool = None,
        submit_type: int = None,
        supplement_flag: bool = None,
        type: int = None,
    ):
        self.additional_oss_key_list = additional_oss_key_list
        self.address = address
        self.application_oss_key = application_oss_key
        self.biz_id = biz_id
        self.business_licence_oss_key = business_licence_oss_key
        self.card_number = card_number
        self.change_name = change_name
        self.contact_address = contact_address
        self.contact_email = contact_email
        self.contact_name = contact_name
        self.contact_number = contact_number
        self.country = country
        self.eng_address = eng_address
        self.eng_name = eng_name
        self.id_card_oss_key = id_card_oss_key
        self.legal_notice_oss_key = legal_notice_oss_key
        self.loa_oss_key = loa_oss_key
        self.name = name
        self.passport_oss_key = passport_oss_key
        self.province = province
        self.region = region
        self.review_material_additional_json = review_material_additional_json
        self.separate = separate
        self.submit_online = submit_online
        self.submit_type = submit_type
        self.supplement_flag = supplement_flag
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.additional_oss_key_list is not None:
            result['AdditionalOssKeyList'] = self.additional_oss_key_list
        if self.address is not None:
            result['Address'] = self.address
        if self.application_oss_key is not None:
            result['ApplicationOssKey'] = self.application_oss_key
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.business_licence_oss_key is not None:
            result['BusinessLicenceOssKey'] = self.business_licence_oss_key
        if self.card_number is not None:
            result['CardNumber'] = self.card_number
        if self.change_name is not None:
            result['ChangeName'] = self.change_name
        if self.contact_address is not None:
            result['ContactAddress'] = self.contact_address
        if self.contact_email is not None:
            result['ContactEmail'] = self.contact_email
        if self.contact_name is not None:
            result['ContactName'] = self.contact_name
        if self.contact_number is not None:
            result['ContactNumber'] = self.contact_number
        if self.country is not None:
            result['Country'] = self.country
        if self.eng_address is not None:
            result['EngAddress'] = self.eng_address
        if self.eng_name is not None:
            result['EngName'] = self.eng_name
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
        if self.province is not None:
            result['Province'] = self.province
        if self.region is not None:
            result['Region'] = self.region
        if self.review_material_additional_json is not None:
            result['ReviewMaterialAdditionalJson'] = self.review_material_additional_json
        if self.separate is not None:
            result['Separate'] = self.separate
        if self.submit_online is not None:
            result['SubmitOnline'] = self.submit_online
        if self.submit_type is not None:
            result['SubmitType'] = self.submit_type
        if self.supplement_flag is not None:
            result['SupplementFlag'] = self.supplement_flag
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdditionalOssKeyList') is not None:
            self.additional_oss_key_list = m.get('AdditionalOssKeyList')
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('ApplicationOssKey') is not None:
            self.application_oss_key = m.get('ApplicationOssKey')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BusinessLicenceOssKey') is not None:
            self.business_licence_oss_key = m.get('BusinessLicenceOssKey')
        if m.get('CardNumber') is not None:
            self.card_number = m.get('CardNumber')
        if m.get('ChangeName') is not None:
            self.change_name = m.get('ChangeName')
        if m.get('ContactAddress') is not None:
            self.contact_address = m.get('ContactAddress')
        if m.get('ContactEmail') is not None:
            self.contact_email = m.get('ContactEmail')
        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')
        if m.get('ContactNumber') is not None:
            self.contact_number = m.get('ContactNumber')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('EngAddress') is not None:
            self.eng_address = m.get('EngAddress')
        if m.get('EngName') is not None:
            self.eng_name = m.get('EngName')
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
        if m.get('Province') is not None:
            self.province = m.get('Province')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ReviewMaterialAdditionalJson') is not None:
            self.review_material_additional_json = m.get('ReviewMaterialAdditionalJson')
        if m.get('Separate') is not None:
            self.separate = m.get('Separate')
        if m.get('SubmitOnline') is not None:
            self.submit_online = m.get('SubmitOnline')
        if m.get('SubmitType') is not None:
            self.submit_type = m.get('SubmitType')
        if m.get('SupplementFlag') is not None:
            self.supplement_flag = m.get('SupplementFlag')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class SaveTradeMarkReviewMaterialDetailShrinkRequest(TeaModel):
    def __init__(
        self,
        additional_oss_key_list_shrink: str = None,
        address: str = None,
        application_oss_key: str = None,
        biz_id: str = None,
        business_licence_oss_key: str = None,
        card_number: str = None,
        change_name: bool = None,
        contact_address: str = None,
        contact_email: str = None,
        contact_name: str = None,
        contact_number: str = None,
        country: str = None,
        eng_address: str = None,
        eng_name: str = None,
        id_card_oss_key: str = None,
        legal_notice_oss_key: str = None,
        loa_oss_key: str = None,
        name: str = None,
        passport_oss_key: str = None,
        province: str = None,
        region: int = None,
        review_material_additional_json: str = None,
        separate: bool = None,
        submit_online: bool = None,
        submit_type: int = None,
        supplement_flag: bool = None,
        type: int = None,
    ):
        self.additional_oss_key_list_shrink = additional_oss_key_list_shrink
        self.address = address
        self.application_oss_key = application_oss_key
        self.biz_id = biz_id
        self.business_licence_oss_key = business_licence_oss_key
        self.card_number = card_number
        self.change_name = change_name
        self.contact_address = contact_address
        self.contact_email = contact_email
        self.contact_name = contact_name
        self.contact_number = contact_number
        self.country = country
        self.eng_address = eng_address
        self.eng_name = eng_name
        self.id_card_oss_key = id_card_oss_key
        self.legal_notice_oss_key = legal_notice_oss_key
        self.loa_oss_key = loa_oss_key
        self.name = name
        self.passport_oss_key = passport_oss_key
        self.province = province
        self.region = region
        self.review_material_additional_json = review_material_additional_json
        self.separate = separate
        self.submit_online = submit_online
        self.submit_type = submit_type
        self.supplement_flag = supplement_flag
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.additional_oss_key_list_shrink is not None:
            result['AdditionalOssKeyList'] = self.additional_oss_key_list_shrink
        if self.address is not None:
            result['Address'] = self.address
        if self.application_oss_key is not None:
            result['ApplicationOssKey'] = self.application_oss_key
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.business_licence_oss_key is not None:
            result['BusinessLicenceOssKey'] = self.business_licence_oss_key
        if self.card_number is not None:
            result['CardNumber'] = self.card_number
        if self.change_name is not None:
            result['ChangeName'] = self.change_name
        if self.contact_address is not None:
            result['ContactAddress'] = self.contact_address
        if self.contact_email is not None:
            result['ContactEmail'] = self.contact_email
        if self.contact_name is not None:
            result['ContactName'] = self.contact_name
        if self.contact_number is not None:
            result['ContactNumber'] = self.contact_number
        if self.country is not None:
            result['Country'] = self.country
        if self.eng_address is not None:
            result['EngAddress'] = self.eng_address
        if self.eng_name is not None:
            result['EngName'] = self.eng_name
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
        if self.province is not None:
            result['Province'] = self.province
        if self.region is not None:
            result['Region'] = self.region
        if self.review_material_additional_json is not None:
            result['ReviewMaterialAdditionalJson'] = self.review_material_additional_json
        if self.separate is not None:
            result['Separate'] = self.separate
        if self.submit_online is not None:
            result['SubmitOnline'] = self.submit_online
        if self.submit_type is not None:
            result['SubmitType'] = self.submit_type
        if self.supplement_flag is not None:
            result['SupplementFlag'] = self.supplement_flag
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdditionalOssKeyList') is not None:
            self.additional_oss_key_list_shrink = m.get('AdditionalOssKeyList')
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('ApplicationOssKey') is not None:
            self.application_oss_key = m.get('ApplicationOssKey')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BusinessLicenceOssKey') is not None:
            self.business_licence_oss_key = m.get('BusinessLicenceOssKey')
        if m.get('CardNumber') is not None:
            self.card_number = m.get('CardNumber')
        if m.get('ChangeName') is not None:
            self.change_name = m.get('ChangeName')
        if m.get('ContactAddress') is not None:
            self.contact_address = m.get('ContactAddress')
        if m.get('ContactEmail') is not None:
            self.contact_email = m.get('ContactEmail')
        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')
        if m.get('ContactNumber') is not None:
            self.contact_number = m.get('ContactNumber')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('EngAddress') is not None:
            self.eng_address = m.get('EngAddress')
        if m.get('EngName') is not None:
            self.eng_name = m.get('EngName')
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
        if m.get('Province') is not None:
            self.province = m.get('Province')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ReviewMaterialAdditionalJson') is not None:
            self.review_material_additional_json = m.get('ReviewMaterialAdditionalJson')
        if m.get('Separate') is not None:
            self.separate = m.get('Separate')
        if m.get('SubmitOnline') is not None:
            self.submit_online = m.get('SubmitOnline')
        if m.get('SubmitType') is not None:
            self.submit_type = m.get('SubmitType')
        if m.get('SupplementFlag') is not None:
            self.supplement_flag = m.get('SupplementFlag')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class SaveTradeMarkReviewMaterialDetailResponseBody(TeaModel):
    def __init__(
        self,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_msg = error_msg
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SaveTradeMarkReviewMaterialDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SaveTradeMarkReviewMaterialDetailResponseBody = None,
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
            temp_model = SaveTradeMarkReviewMaterialDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SbjOperateRequest(TeaModel):
    def __init__(
        self,
        amount: str = None,
        apply_no: str = None,
        audit_status: bool = None,
        biz_id: str = None,
        file_date: str = None,
        file_oss_key: str = None,
        message: str = None,
        operate_type: str = None,
        order_no: str = None,
        receipt_oss_key: str = None,
        submitted_success: bool = None,
    ):
        self.amount = amount
        self.apply_no = apply_no
        self.audit_status = audit_status
        self.biz_id = biz_id
        self.file_date = file_date
        self.file_oss_key = file_oss_key
        self.message = message
        self.operate_type = operate_type
        self.order_no = order_no
        self.receipt_oss_key = receipt_oss_key
        self.submitted_success = submitted_success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.apply_no is not None:
            result['ApplyNo'] = self.apply_no
        if self.audit_status is not None:
            result['AuditStatus'] = self.audit_status
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.file_date is not None:
            result['FileDate'] = self.file_date
        if self.file_oss_key is not None:
            result['FileOssKey'] = self.file_oss_key
        if self.message is not None:
            result['Message'] = self.message
        if self.operate_type is not None:
            result['OperateType'] = self.operate_type
        if self.order_no is not None:
            result['OrderNo'] = self.order_no
        if self.receipt_oss_key is not None:
            result['ReceiptOssKey'] = self.receipt_oss_key
        if self.submitted_success is not None:
            result['SubmittedSuccess'] = self.submitted_success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('ApplyNo') is not None:
            self.apply_no = m.get('ApplyNo')
        if m.get('AuditStatus') is not None:
            self.audit_status = m.get('AuditStatus')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('FileDate') is not None:
            self.file_date = m.get('FileDate')
        if m.get('FileOssKey') is not None:
            self.file_oss_key = m.get('FileOssKey')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('OperateType') is not None:
            self.operate_type = m.get('OperateType')
        if m.get('OrderNo') is not None:
            self.order_no = m.get('OrderNo')
        if m.get('ReceiptOssKey') is not None:
            self.receipt_oss_key = m.get('ReceiptOssKey')
        if m.get('SubmittedSuccess') is not None:
            self.submitted_success = m.get('SubmittedSuccess')
        return self


class SbjOperateResponseBody(TeaModel):
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


class SbjOperateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SbjOperateResponseBody = None,
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
            temp_model = SbjOperateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SbjOperateNewRequest(TeaModel):
    def __init__(
        self,
        add_submit_count: bool = None,
        allow_resubmit: bool = None,
        amount: str = None,
        apply_no: str = None,
        audit_status: bool = None,
        biz_id: str = None,
        change_status: bool = None,
        error_msg_screenshot: str = None,
        file_date: str = None,
        file_oss_key: str = None,
        message: str = None,
        operate_type: str = None,
        order_no: str = None,
        receipt_oss_key: str = None,
        submitted_success: bool = None,
        success_type: str = None,
    ):
        self.add_submit_count = add_submit_count
        self.allow_resubmit = allow_resubmit
        self.amount = amount
        self.apply_no = apply_no
        self.audit_status = audit_status
        self.biz_id = biz_id
        self.change_status = change_status
        self.error_msg_screenshot = error_msg_screenshot
        self.file_date = file_date
        self.file_oss_key = file_oss_key
        self.message = message
        self.operate_type = operate_type
        self.order_no = order_no
        self.receipt_oss_key = receipt_oss_key
        self.submitted_success = submitted_success
        self.success_type = success_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.add_submit_count is not None:
            result['AddSubmitCount'] = self.add_submit_count
        if self.allow_resubmit is not None:
            result['AllowResubmit'] = self.allow_resubmit
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.apply_no is not None:
            result['ApplyNo'] = self.apply_no
        if self.audit_status is not None:
            result['AuditStatus'] = self.audit_status
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.change_status is not None:
            result['ChangeStatus'] = self.change_status
        if self.error_msg_screenshot is not None:
            result['ErrorMsgScreenshot'] = self.error_msg_screenshot
        if self.file_date is not None:
            result['FileDate'] = self.file_date
        if self.file_oss_key is not None:
            result['FileOssKey'] = self.file_oss_key
        if self.message is not None:
            result['Message'] = self.message
        if self.operate_type is not None:
            result['OperateType'] = self.operate_type
        if self.order_no is not None:
            result['OrderNo'] = self.order_no
        if self.receipt_oss_key is not None:
            result['ReceiptOssKey'] = self.receipt_oss_key
        if self.submitted_success is not None:
            result['SubmittedSuccess'] = self.submitted_success
        if self.success_type is not None:
            result['SuccessType'] = self.success_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddSubmitCount') is not None:
            self.add_submit_count = m.get('AddSubmitCount')
        if m.get('AllowResubmit') is not None:
            self.allow_resubmit = m.get('AllowResubmit')
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('ApplyNo') is not None:
            self.apply_no = m.get('ApplyNo')
        if m.get('AuditStatus') is not None:
            self.audit_status = m.get('AuditStatus')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('ChangeStatus') is not None:
            self.change_status = m.get('ChangeStatus')
        if m.get('ErrorMsgScreenshot') is not None:
            self.error_msg_screenshot = m.get('ErrorMsgScreenshot')
        if m.get('FileDate') is not None:
            self.file_date = m.get('FileDate')
        if m.get('FileOssKey') is not None:
            self.file_oss_key = m.get('FileOssKey')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('OperateType') is not None:
            self.operate_type = m.get('OperateType')
        if m.get('OrderNo') is not None:
            self.order_no = m.get('OrderNo')
        if m.get('ReceiptOssKey') is not None:
            self.receipt_oss_key = m.get('ReceiptOssKey')
        if m.get('SubmittedSuccess') is not None:
            self.submitted_success = m.get('SubmittedSuccess')
        if m.get('SuccessType') is not None:
            self.success_type = m.get('SuccessType')
        return self


class SbjOperateNewResponseBody(TeaModel):
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


class SbjOperateNewResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SbjOperateNewResponseBody = None,
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
            temp_model = SbjOperateNewResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SbrainServiceExecuteRequest(TeaModel):
    def __init__(
        self,
        execute_params: Dict[str, Any] = None,
        product_code: str = None,
        reference_no: str = None,
        reference_type: str = None,
        scene_code: str = None,
        scheme_id: int = None,
        service_place: str = None,
        source: str = None,
        target: str = None,
    ):
        self.execute_params = execute_params
        self.product_code = product_code
        self.reference_no = reference_no
        self.reference_type = reference_type
        self.scene_code = scene_code
        self.scheme_id = scheme_id
        self.service_place = service_place
        self.source = source
        self.target = target

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.execute_params is not None:
            result['ExecuteParams'] = self.execute_params
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.reference_no is not None:
            result['ReferenceNo'] = self.reference_no
        if self.reference_type is not None:
            result['ReferenceType'] = self.reference_type
        if self.scene_code is not None:
            result['SceneCode'] = self.scene_code
        if self.scheme_id is not None:
            result['SchemeId'] = self.scheme_id
        if self.service_place is not None:
            result['ServicePlace'] = self.service_place
        if self.source is not None:
            result['Source'] = self.source
        if self.target is not None:
            result['Target'] = self.target
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExecuteParams') is not None:
            self.execute_params = m.get('ExecuteParams')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ReferenceNo') is not None:
            self.reference_no = m.get('ReferenceNo')
        if m.get('ReferenceType') is not None:
            self.reference_type = m.get('ReferenceType')
        if m.get('SceneCode') is not None:
            self.scene_code = m.get('SceneCode')
        if m.get('SchemeId') is not None:
            self.scheme_id = m.get('SchemeId')
        if m.get('ServicePlace') is not None:
            self.service_place = m.get('ServicePlace')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Target') is not None:
            self.target = m.get('Target')
        return self


class SbrainServiceExecuteShrinkRequest(TeaModel):
    def __init__(
        self,
        execute_params_shrink: str = None,
        product_code: str = None,
        reference_no: str = None,
        reference_type: str = None,
        scene_code: str = None,
        scheme_id: int = None,
        service_place: str = None,
        source: str = None,
        target: str = None,
    ):
        self.execute_params_shrink = execute_params_shrink
        self.product_code = product_code
        self.reference_no = reference_no
        self.reference_type = reference_type
        self.scene_code = scene_code
        self.scheme_id = scheme_id
        self.service_place = service_place
        self.source = source
        self.target = target

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.execute_params_shrink is not None:
            result['ExecuteParams'] = self.execute_params_shrink
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.reference_no is not None:
            result['ReferenceNo'] = self.reference_no
        if self.reference_type is not None:
            result['ReferenceType'] = self.reference_type
        if self.scene_code is not None:
            result['SceneCode'] = self.scene_code
        if self.scheme_id is not None:
            result['SchemeId'] = self.scheme_id
        if self.service_place is not None:
            result['ServicePlace'] = self.service_place
        if self.source is not None:
            result['Source'] = self.source
        if self.target is not None:
            result['Target'] = self.target
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExecuteParams') is not None:
            self.execute_params_shrink = m.get('ExecuteParams')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ReferenceNo') is not None:
            self.reference_no = m.get('ReferenceNo')
        if m.get('ReferenceType') is not None:
            self.reference_type = m.get('ReferenceType')
        if m.get('SceneCode') is not None:
            self.scene_code = m.get('SceneCode')
        if m.get('SchemeId') is not None:
            self.scheme_id = m.get('SchemeId')
        if m.get('ServicePlace') is not None:
            self.service_place = m.get('ServicePlace')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Target') is not None:
            self.target = m.get('Target')
        return self


class SbrainServiceExecuteResponseBody(TeaModel):
    def __init__(
        self,
        data: Any = None,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
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
        if self.data is not None:
            result['Data'] = self.data
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
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SbrainServiceExecuteResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SbrainServiceExecuteResponseBody = None,
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
            temp_model = SbrainServiceExecuteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SbrainServiceHasRunningTaskBatchQueryRequest(TeaModel):
    def __init__(
        self,
        product_code: str = None,
        reference_nos: List[str] = None,
        reference_type: str = None,
        source: str = None,
        task_type: str = None,
    ):
        self.product_code = product_code
        self.reference_nos = reference_nos
        self.reference_type = reference_type
        self.source = source
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.reference_nos is not None:
            result['ReferenceNos'] = self.reference_nos
        if self.reference_type is not None:
            result['ReferenceType'] = self.reference_type
        if self.source is not None:
            result['Source'] = self.source
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ReferenceNos') is not None:
            self.reference_nos = m.get('ReferenceNos')
        if m.get('ReferenceType') is not None:
            self.reference_type = m.get('ReferenceType')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        return self


class SbrainServiceHasRunningTaskBatchQueryShrinkRequest(TeaModel):
    def __init__(
        self,
        product_code: str = None,
        reference_nos_shrink: str = None,
        reference_type: str = None,
        source: str = None,
        task_type: str = None,
    ):
        self.product_code = product_code
        self.reference_nos_shrink = reference_nos_shrink
        self.reference_type = reference_type
        self.source = source
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.reference_nos_shrink is not None:
            result['ReferenceNos'] = self.reference_nos_shrink
        if self.reference_type is not None:
            result['ReferenceType'] = self.reference_type
        if self.source is not None:
            result['Source'] = self.source
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ReferenceNos') is not None:
            self.reference_nos_shrink = m.get('ReferenceNos')
        if m.get('ReferenceType') is not None:
            self.reference_type = m.get('ReferenceType')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        return self


class SbrainServiceHasRunningTaskBatchQueryResponseBody(TeaModel):
    def __init__(
        self,
        data: Any = None,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
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
        if self.data is not None:
            result['Data'] = self.data
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
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SbrainServiceHasRunningTaskBatchQueryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SbrainServiceHasRunningTaskBatchQueryResponseBody = None,
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
            temp_model = SbrainServiceHasRunningTaskBatchQueryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SbrainServiceSchemeMatchRequest(TeaModel):
    def __init__(
        self,
        match_params: Dict[str, Any] = None,
        product_code: str = None,
        reference_no: str = None,
        reference_type: str = None,
        scene_code: str = None,
        source: str = None,
    ):
        self.match_params = match_params
        self.product_code = product_code
        self.reference_no = reference_no
        self.reference_type = reference_type
        self.scene_code = scene_code
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match_params is not None:
            result['MatchParams'] = self.match_params
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.reference_no is not None:
            result['ReferenceNo'] = self.reference_no
        if self.reference_type is not None:
            result['ReferenceType'] = self.reference_type
        if self.scene_code is not None:
            result['SceneCode'] = self.scene_code
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MatchParams') is not None:
            self.match_params = m.get('MatchParams')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ReferenceNo') is not None:
            self.reference_no = m.get('ReferenceNo')
        if m.get('ReferenceType') is not None:
            self.reference_type = m.get('ReferenceType')
        if m.get('SceneCode') is not None:
            self.scene_code = m.get('SceneCode')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class SbrainServiceSchemeMatchShrinkRequest(TeaModel):
    def __init__(
        self,
        match_params_shrink: str = None,
        product_code: str = None,
        reference_no: str = None,
        reference_type: str = None,
        scene_code: str = None,
        source: str = None,
    ):
        self.match_params_shrink = match_params_shrink
        self.product_code = product_code
        self.reference_no = reference_no
        self.reference_type = reference_type
        self.scene_code = scene_code
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match_params_shrink is not None:
            result['MatchParams'] = self.match_params_shrink
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.reference_no is not None:
            result['ReferenceNo'] = self.reference_no
        if self.reference_type is not None:
            result['ReferenceType'] = self.reference_type
        if self.scene_code is not None:
            result['SceneCode'] = self.scene_code
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MatchParams') is not None:
            self.match_params_shrink = m.get('MatchParams')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ReferenceNo') is not None:
            self.reference_no = m.get('ReferenceNo')
        if m.get('ReferenceType') is not None:
            self.reference_type = m.get('ReferenceType')
        if m.get('SceneCode') is not None:
            self.scene_code = m.get('SceneCode')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class SbrainServiceSchemeMatchResponseBodyDataSchemeContentContentModules(TeaModel):
    def __init__(
        self,
        tag: str = None,
        action: str = None,
        module_data: str = None,
        module_data_source: str = None,
        module_data_source_type: str = None,
        name: str = None,
        target: str = None,
    ):
        self.tag = tag
        self.action = action
        self.module_data = module_data
        self.module_data_source = module_data_source
        self.module_data_source_type = module_data_source_type
        self.name = name
        self.target = target

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.action is not None:
            result['action'] = self.action
        if self.module_data is not None:
            result['moduleData'] = self.module_data
        if self.module_data_source is not None:
            result['moduleDataSource'] = self.module_data_source
        if self.module_data_source_type is not None:
            result['moduleDataSourceType'] = self.module_data_source_type
        if self.name is not None:
            result['name'] = self.name
        if self.target is not None:
            result['target'] = self.target
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('action') is not None:
            self.action = m.get('action')
        if m.get('moduleData') is not None:
            self.module_data = m.get('moduleData')
        if m.get('moduleDataSource') is not None:
            self.module_data_source = m.get('moduleDataSource')
        if m.get('moduleDataSourceType') is not None:
            self.module_data_source_type = m.get('moduleDataSourceType')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('target') is not None:
            self.target = m.get('target')
        return self


class SbrainServiceSchemeMatchResponseBodyDataSchemeContent(TeaModel):
    def __init__(
        self,
        content_index: int = None,
        content_modules: List[SbrainServiceSchemeMatchResponseBodyDataSchemeContentContentModules] = None,
        display: str = None,
    ):
        self.content_index = content_index
        self.content_modules = content_modules
        self.display = display

    def validate(self):
        if self.content_modules:
            for k in self.content_modules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content_index is not None:
            result['ContentIndex'] = self.content_index
        result['ContentModules'] = []
        if self.content_modules is not None:
            for k in self.content_modules:
                result['ContentModules'].append(k.to_map() if k else None)
        if self.display is not None:
            result['Display'] = self.display
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContentIndex') is not None:
            self.content_index = m.get('ContentIndex')
        self.content_modules = []
        if m.get('ContentModules') is not None:
            for k in m.get('ContentModules'):
                temp_model = SbrainServiceSchemeMatchResponseBodyDataSchemeContentContentModules()
                self.content_modules.append(temp_model.from_map(k))
        if m.get('Display') is not None:
            self.display = m.get('Display')
        return self


class SbrainServiceSchemeMatchResponseBodyData(TeaModel):
    def __init__(
        self,
        scene_code: str = None,
        scheme_content: SbrainServiceSchemeMatchResponseBodyDataSchemeContent = None,
        scheme_id: int = None,
    ):
        self.scene_code = scene_code
        self.scheme_content = scheme_content
        self.scheme_id = scheme_id

    def validate(self):
        if self.scheme_content:
            self.scheme_content.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scene_code is not None:
            result['SceneCode'] = self.scene_code
        if self.scheme_content is not None:
            result['SchemeContent'] = self.scheme_content.to_map()
        if self.scheme_id is not None:
            result['SchemeId'] = self.scheme_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SceneCode') is not None:
            self.scene_code = m.get('SceneCode')
        if m.get('SchemeContent') is not None:
            temp_model = SbrainServiceSchemeMatchResponseBodyDataSchemeContent()
            self.scheme_content = temp_model.from_map(m['SchemeContent'])
        if m.get('SchemeId') is not None:
            self.scheme_id = m.get('SchemeId')
        return self


class SbrainServiceSchemeMatchResponseBody(TeaModel):
    def __init__(
        self,
        data: SbrainServiceSchemeMatchResponseBodyData = None,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
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
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
        if m.get('Data') is not None:
            temp_model = SbrainServiceSchemeMatchResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SbrainServiceSchemeMatchResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SbrainServiceSchemeMatchResponseBody = None,
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
            temp_model = SbrainServiceSchemeMatchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchTmOnsalesRequest(TeaModel):
    def __init__(
        self,
        classification: str = None,
        keyword: str = None,
        order_price_left: int = None,
        order_price_right: int = None,
        page_num: int = None,
        page_size: int = None,
        product_code: str = None,
        query_all: bool = None,
        reg_left: int = None,
        reg_right: int = None,
        register_number: str = None,
        sort_name: str = None,
        sort_order: str = None,
        tag: str = None,
        tm_name: str = None,
        top_search: str = None,
    ):
        self.classification = classification
        self.keyword = keyword
        self.order_price_left = order_price_left
        self.order_price_right = order_price_right
        self.page_num = page_num
        self.page_size = page_size
        self.product_code = product_code
        self.query_all = query_all
        self.reg_left = reg_left
        self.reg_right = reg_right
        self.register_number = register_number
        self.sort_name = sort_name
        self.sort_order = sort_order
        self.tag = tag
        self.tm_name = tm_name
        self.top_search = top_search

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.classification is not None:
            result['Classification'] = self.classification
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.order_price_left is not None:
            result['OrderPriceLeft'] = self.order_price_left
        if self.order_price_right is not None:
            result['OrderPriceRight'] = self.order_price_right
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.query_all is not None:
            result['QueryAll'] = self.query_all
        if self.reg_left is not None:
            result['RegLeft'] = self.reg_left
        if self.reg_right is not None:
            result['RegRight'] = self.reg_right
        if self.register_number is not None:
            result['RegisterNumber'] = self.register_number
        if self.sort_name is not None:
            result['SortName'] = self.sort_name
        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.tm_name is not None:
            result['TmName'] = self.tm_name
        if self.top_search is not None:
            result['TopSearch'] = self.top_search
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Classification') is not None:
            self.classification = m.get('Classification')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('OrderPriceLeft') is not None:
            self.order_price_left = m.get('OrderPriceLeft')
        if m.get('OrderPriceRight') is not None:
            self.order_price_right = m.get('OrderPriceRight')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('QueryAll') is not None:
            self.query_all = m.get('QueryAll')
        if m.get('RegLeft') is not None:
            self.reg_left = m.get('RegLeft')
        if m.get('RegRight') is not None:
            self.reg_right = m.get('RegRight')
        if m.get('RegisterNumber') is not None:
            self.register_number = m.get('RegisterNumber')
        if m.get('SortName') is not None:
            self.sort_name = m.get('SortName')
        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('TmName') is not None:
            self.tm_name = m.get('TmName')
        if m.get('TopSearch') is not None:
            self.top_search = m.get('TopSearch')
        return self


class SearchTmOnsalesResponseBodyTrademarks(TeaModel):
    def __init__(
        self,
        classification: str = None,
        icon: str = None,
        order_price: str = None,
        partner_code: str = None,
        product_code: str = None,
        product_desc: str = None,
        registration_number: str = None,
        status: int = None,
        trademark_name: str = None,
        uid: str = None,
    ):
        self.classification = classification
        self.icon = icon
        self.order_price = order_price
        self.partner_code = partner_code
        self.product_code = product_code
        self.product_desc = product_desc
        self.registration_number = registration_number
        self.status = status
        self.trademark_name = trademark_name
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.classification is not None:
            result['Classification'] = self.classification
        if self.icon is not None:
            result['Icon'] = self.icon
        if self.order_price is not None:
            result['OrderPrice'] = self.order_price
        if self.partner_code is not None:
            result['PartnerCode'] = self.partner_code
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.product_desc is not None:
            result['ProductDesc'] = self.product_desc
        if self.registration_number is not None:
            result['RegistrationNumber'] = self.registration_number
        if self.status is not None:
            result['Status'] = self.status
        if self.trademark_name is not None:
            result['TrademarkName'] = self.trademark_name
        if self.uid is not None:
            result['Uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Classification') is not None:
            self.classification = m.get('Classification')
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        if m.get('OrderPrice') is not None:
            self.order_price = m.get('OrderPrice')
        if m.get('PartnerCode') is not None:
            self.partner_code = m.get('PartnerCode')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProductDesc') is not None:
            self.product_desc = m.get('ProductDesc')
        if m.get('RegistrationNumber') is not None:
            self.registration_number = m.get('RegistrationNumber')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TrademarkName') is not None:
            self.trademark_name = m.get('TrademarkName')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        return self


class SearchTmOnsalesResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        total_page_number: int = None,
        trademarks: List[SearchTmOnsalesResponseBodyTrademarks] = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count
        self.total_page_number = total_page_number
        self.trademarks = trademarks

    def validate(self):
        if self.trademarks:
            for k in self.trademarks:
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
        if self.total_page_number is not None:
            result['TotalPageNumber'] = self.total_page_number
        result['Trademarks'] = []
        if self.trademarks is not None:
            for k in self.trademarks:
                result['Trademarks'].append(k.to_map() if k else None)
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
        if m.get('TotalPageNumber') is not None:
            self.total_page_number = m.get('TotalPageNumber')
        self.trademarks = []
        if m.get('Trademarks') is not None:
            for k in m.get('Trademarks'):
                temp_model = SearchTmOnsalesResponseBodyTrademarks()
                self.trademarks.append(temp_model.from_map(k))
        return self


class SearchTmOnsalesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SearchTmOnsalesResponseBody = None,
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
            temp_model = SearchTmOnsalesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartNotaryRequest(TeaModel):
    def __init__(
        self,
        notary_order_id: int = None,
    ):
        self.notary_order_id = notary_order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.notary_order_id is not None:
            result['NotaryOrderId'] = self.notary_order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NotaryOrderId') is not None:
            self.notary_order_id = m.get('NotaryOrderId')
        return self


class StartNotaryResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_msg: str = None,
        notary_url: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_msg = error_msg
        self.notary_url = notary_url
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
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.notary_url is not None:
            result['NotaryUrl'] = self.notary_url
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('NotaryUrl') is not None:
            self.notary_url = m.get('NotaryUrl')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class StartNotaryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StartNotaryResponseBody = None,
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
            temp_model = StartNotaryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StoreMaterialTemporarilyRequest(TeaModel):
    def __init__(
        self,
        address: str = None,
        business_licence_oss_key: str = None,
        card_number: str = None,
        city: str = None,
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
        loa_oss_key: str = None,
        name: str = None,
        passport_oss_key: str = None,
        personal_type: int = None,
        principal_name: int = None,
        province: str = None,
        region: str = None,
        town: str = None,
        type: str = None,
    ):
        self.address = address
        self.business_licence_oss_key = business_licence_oss_key
        self.card_number = card_number
        self.city = city
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
        self.loa_oss_key = loa_oss_key
        self.name = name
        self.passport_oss_key = passport_oss_key
        self.personal_type = personal_type
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
        if self.business_licence_oss_key is not None:
            result['BusinessLicenceOssKey'] = self.business_licence_oss_key
        if self.card_number is not None:
            result['CardNumber'] = self.card_number
        if self.city is not None:
            result['City'] = self.city
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
        if self.loa_oss_key is not None:
            result['LoaOssKey'] = self.loa_oss_key
        if self.name is not None:
            result['Name'] = self.name
        if self.passport_oss_key is not None:
            result['PassportOssKey'] = self.passport_oss_key
        if self.personal_type is not None:
            result['PersonalType'] = self.personal_type
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
        if m.get('BusinessLicenceOssKey') is not None:
            self.business_licence_oss_key = m.get('BusinessLicenceOssKey')
        if m.get('CardNumber') is not None:
            self.card_number = m.get('CardNumber')
        if m.get('City') is not None:
            self.city = m.get('City')
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
        if m.get('LoaOssKey') is not None:
            self.loa_oss_key = m.get('LoaOssKey')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PassportOssKey') is not None:
            self.passport_oss_key = m.get('PassportOssKey')
        if m.get('PersonalType') is not None:
            self.personal_type = m.get('PersonalType')
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


class StoreMaterialTemporarilyResponseBody(TeaModel):
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


class StoreMaterialTemporarilyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StoreMaterialTemporarilyResponseBody = None,
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
            temp_model = StoreMaterialTemporarilyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitSupplementRequest(TeaModel):
    def __init__(
        self,
        content: str = None,
        id: int = None,
        operate_type: str = None,
        upload_oss_key_list: Dict[str, Any] = None,
    ):
        self.content = content
        self.id = id
        self.operate_type = operate_type
        self.upload_oss_key_list = upload_oss_key_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.id is not None:
            result['Id'] = self.id
        if self.operate_type is not None:
            result['OperateType'] = self.operate_type
        if self.upload_oss_key_list is not None:
            result['UploadOssKeyList'] = self.upload_oss_key_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OperateType') is not None:
            self.operate_type = m.get('OperateType')
        if m.get('UploadOssKeyList') is not None:
            self.upload_oss_key_list = m.get('UploadOssKeyList')
        return self


class SubmitSupplementShrinkRequest(TeaModel):
    def __init__(
        self,
        content: str = None,
        id: int = None,
        operate_type: str = None,
        upload_oss_key_list_shrink: str = None,
    ):
        self.content = content
        self.id = id
        self.operate_type = operate_type
        self.upload_oss_key_list_shrink = upload_oss_key_list_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.id is not None:
            result['Id'] = self.id
        if self.operate_type is not None:
            result['OperateType'] = self.operate_type
        if self.upload_oss_key_list_shrink is not None:
            result['UploadOssKeyList'] = self.upload_oss_key_list_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OperateType') is not None:
            self.operate_type = m.get('OperateType')
        if m.get('UploadOssKeyList') is not None:
            self.upload_oss_key_list_shrink = m.get('UploadOssKeyList')
        return self


class SubmitSupplementResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_msg = error_msg
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
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
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
            temp_model = SubmitSupplementResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitTrademarkApplicationComplaintRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        content: str = None,
        files: Dict[str, Any] = None,
    ):
        self.biz_id = biz_id
        self.content = content
        self.files = files

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.content is not None:
            result['Content'] = self.content
        if self.files is not None:
            result['Files'] = self.files
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Files') is not None:
            self.files = m.get('Files')
        return self


class SubmitTrademarkApplicationComplaintShrinkRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        content: str = None,
        files_shrink: str = None,
    ):
        self.biz_id = biz_id
        self.content = content
        self.files_shrink = files_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.content is not None:
            result['Content'] = self.content
        if self.files_shrink is not None:
            result['Files'] = self.files_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Files') is not None:
            self.files_shrink = m.get('Files')
        return self


class SubmitTrademarkApplicationComplaintResponseBody(TeaModel):
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


class SubmitTrademarkApplicationComplaintResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SubmitTrademarkApplicationComplaintResponseBody = None,
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
            temp_model = SubmitTrademarkApplicationComplaintResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SyncTrademarkRequest(TeaModel):
    def __init__(
        self,
        begin_time: int = None,
        classification_code: str = None,
        description: str = None,
        end_time: int = None,
        label: str = None,
        original_price: float = None,
        owner_en_name: str = None,
        owner_name: str = None,
        reason: str = None,
        reg_ann_date: int = None,
        secondary_classification: str = None,
        status: str = None,
        third_classification: str = None,
        tm_icon: str = None,
        tm_name: str = None,
        tm_number: str = None,
        type: str = None,
    ):
        self.begin_time = begin_time
        self.classification_code = classification_code
        self.description = description
        self.end_time = end_time
        self.label = label
        self.original_price = original_price
        self.owner_en_name = owner_en_name
        self.owner_name = owner_name
        self.reason = reason
        self.reg_ann_date = reg_ann_date
        self.secondary_classification = secondary_classification
        self.status = status
        self.third_classification = third_classification
        self.tm_icon = tm_icon
        self.tm_name = tm_name
        self.tm_number = tm_number
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.classification_code is not None:
            result['ClassificationCode'] = self.classification_code
        if self.description is not None:
            result['Description'] = self.description
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.label is not None:
            result['Label'] = self.label
        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price
        if self.owner_en_name is not None:
            result['OwnerEnName'] = self.owner_en_name
        if self.owner_name is not None:
            result['OwnerName'] = self.owner_name
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.reg_ann_date is not None:
            result['RegAnnDate'] = self.reg_ann_date
        if self.secondary_classification is not None:
            result['SecondaryClassification'] = self.secondary_classification
        if self.status is not None:
            result['Status'] = self.status
        if self.third_classification is not None:
            result['ThirdClassification'] = self.third_classification
        if self.tm_icon is not None:
            result['TmIcon'] = self.tm_icon
        if self.tm_name is not None:
            result['TmName'] = self.tm_name
        if self.tm_number is not None:
            result['TmNumber'] = self.tm_number
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('ClassificationCode') is not None:
            self.classification_code = m.get('ClassificationCode')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('OriginalPrice') is not None:
            self.original_price = m.get('OriginalPrice')
        if m.get('OwnerEnName') is not None:
            self.owner_en_name = m.get('OwnerEnName')
        if m.get('OwnerName') is not None:
            self.owner_name = m.get('OwnerName')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('RegAnnDate') is not None:
            self.reg_ann_date = m.get('RegAnnDate')
        if m.get('SecondaryClassification') is not None:
            self.secondary_classification = m.get('SecondaryClassification')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ThirdClassification') is not None:
            self.third_classification = m.get('ThirdClassification')
        if m.get('TmIcon') is not None:
            self.tm_icon = m.get('TmIcon')
        if m.get('TmName') is not None:
            self.tm_name = m.get('TmName')
        if m.get('TmNumber') is not None:
            self.tm_number = m.get('TmNumber')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class SyncTrademarkResponseBody(TeaModel):
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


class SyncTrademarkResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SyncTrademarkResponseBody = None,
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
            temp_model = SyncTrademarkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateApplicantContacterRequest(TeaModel):
    def __init__(
        self,
        applicant_id: int = None,
        biz_id: str = None,
        contact_address: str = None,
        contact_city: str = None,
        contact_district: str = None,
        contact_email: str = None,
        contact_name: str = None,
        contact_number: str = None,
        contact_province: str = None,
        contact_zip_code: str = None,
    ):
        self.applicant_id = applicant_id
        self.biz_id = biz_id
        self.contact_address = contact_address
        self.contact_city = contact_city
        self.contact_district = contact_district
        self.contact_email = contact_email
        self.contact_name = contact_name
        self.contact_number = contact_number
        self.contact_province = contact_province
        self.contact_zip_code = contact_zip_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.applicant_id is not None:
            result['ApplicantId'] = self.applicant_id
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.contact_address is not None:
            result['ContactAddress'] = self.contact_address
        if self.contact_city is not None:
            result['ContactCity'] = self.contact_city
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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicantId') is not None:
            self.applicant_id = m.get('ApplicantId')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('ContactAddress') is not None:
            self.contact_address = m.get('ContactAddress')
        if m.get('ContactCity') is not None:
            self.contact_city = m.get('ContactCity')
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
        return self


class UpdateApplicantContacterResponseBody(TeaModel):
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


class UpdateApplicantContacterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateApplicantContacterResponseBody = None,
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
            temp_model = UpdateApplicantContacterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateMaterialRequest(TeaModel):
    def __init__(
        self,
        address: str = None,
        business_licence_oss_key: str = None,
        card_number: str = None,
        city: str = None,
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
        id: int = None,
        id_card_name: str = None,
        id_card_number: str = None,
        id_card_oss_key: str = None,
        legal_notice_oss_key: str = None,
        loa_id: int = None,
        loa_oss_key: str = None,
        name: str = None,
        passport_oss_key: str = None,
        personal_type: int = None,
        province: str = None,
        town: str = None,
    ):
        self.address = address
        self.business_licence_oss_key = business_licence_oss_key
        self.card_number = card_number
        self.city = city
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
        self.id = id
        self.id_card_name = id_card_name
        self.id_card_number = id_card_number
        self.id_card_oss_key = id_card_oss_key
        self.legal_notice_oss_key = legal_notice_oss_key
        self.loa_id = loa_id
        self.loa_oss_key = loa_oss_key
        self.name = name
        self.passport_oss_key = passport_oss_key
        self.personal_type = personal_type
        self.province = province
        self.town = town

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.business_licence_oss_key is not None:
            result['BusinessLicenceOssKey'] = self.business_licence_oss_key
        if self.card_number is not None:
            result['CardNumber'] = self.card_number
        if self.city is not None:
            result['City'] = self.city
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
        if self.id is not None:
            result['Id'] = self.id
        if self.id_card_name is not None:
            result['IdCardName'] = self.id_card_name
        if self.id_card_number is not None:
            result['IdCardNumber'] = self.id_card_number
        if self.id_card_oss_key is not None:
            result['IdCardOssKey'] = self.id_card_oss_key
        if self.legal_notice_oss_key is not None:
            result['LegalNoticeOssKey'] = self.legal_notice_oss_key
        if self.loa_id is not None:
            result['LoaId'] = self.loa_id
        if self.loa_oss_key is not None:
            result['LoaOssKey'] = self.loa_oss_key
        if self.name is not None:
            result['Name'] = self.name
        if self.passport_oss_key is not None:
            result['PassportOssKey'] = self.passport_oss_key
        if self.personal_type is not None:
            result['PersonalType'] = self.personal_type
        if self.province is not None:
            result['Province'] = self.province
        if self.town is not None:
            result['Town'] = self.town
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('BusinessLicenceOssKey') is not None:
            self.business_licence_oss_key = m.get('BusinessLicenceOssKey')
        if m.get('CardNumber') is not None:
            self.card_number = m.get('CardNumber')
        if m.get('City') is not None:
            self.city = m.get('City')
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
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdCardName') is not None:
            self.id_card_name = m.get('IdCardName')
        if m.get('IdCardNumber') is not None:
            self.id_card_number = m.get('IdCardNumber')
        if m.get('IdCardOssKey') is not None:
            self.id_card_oss_key = m.get('IdCardOssKey')
        if m.get('LegalNoticeOssKey') is not None:
            self.legal_notice_oss_key = m.get('LegalNoticeOssKey')
        if m.get('LoaId') is not None:
            self.loa_id = m.get('LoaId')
        if m.get('LoaOssKey') is not None:
            self.loa_oss_key = m.get('LoaOssKey')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PassportOssKey') is not None:
            self.passport_oss_key = m.get('PassportOssKey')
        if m.get('PersonalType') is not None:
            self.personal_type = m.get('PersonalType')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        if m.get('Town') is not None:
            self.town = m.get('Town')
        return self


class UpdateMaterialResponseBody(TeaModel):
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


class UpdateMaterialResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateMaterialResponseBody = None,
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
            temp_model = UpdateMaterialResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateProduceRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        biz_type: str = None,
        ext_map: str = None,
        operate_type: str = None,
    ):
        self.biz_id = biz_id
        self.biz_type = biz_type
        self.ext_map = ext_map
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
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.ext_map is not None:
            result['ExtMap'] = self.ext_map
        if self.operate_type is not None:
            result['OperateType'] = self.operate_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('ExtMap') is not None:
            self.ext_map = m.get('ExtMap')
        if m.get('OperateType') is not None:
            self.operate_type = m.get('OperateType')
        return self


class UpdateProduceResponseBody(TeaModel):
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
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class UpdateProduceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateProduceResponseBody = None,
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
            temp_model = UpdateProduceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateProduceLoaIdRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        loa_oss_key: str = None,
    ):
        self.biz_id = biz_id
        self.loa_oss_key = loa_oss_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.loa_oss_key is not None:
            result['LoaOssKey'] = self.loa_oss_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('LoaOssKey') is not None:
            self.loa_oss_key = m.get('LoaOssKey')
        return self


class UpdateProduceLoaIdResponseBody(TeaModel):
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


class UpdateProduceLoaIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateProduceLoaIdResponseBody = None,
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
            temp_model = UpdateProduceLoaIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateSendMaterialNumRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        num: str = None,
        operate_type: int = None,
    ):
        self.biz_id = biz_id
        self.num = num
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
        if self.num is not None:
            result['Num'] = self.num
        if self.operate_type is not None:
            result['OperateType'] = self.operate_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Num') is not None:
            self.num = m.get('Num')
        if m.get('OperateType') is not None:
            self.operate_type = m.get('OperateType')
        return self


class UpdateSendMaterialNumResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_msg = error_msg
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
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateSendMaterialNumResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateSendMaterialNumResponseBody = None,
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
            temp_model = UpdateSendMaterialNumResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateTrademarkNameRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        client_token: str = None,
        tm_comment: str = None,
        tm_icon: str = None,
        tm_name: str = None,
        type: int = None,
    ):
        self.biz_id = biz_id
        self.client_token = client_token
        self.tm_comment = tm_comment
        self.tm_icon = tm_icon
        self.tm_name = tm_name
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.tm_comment is not None:
            result['TmComment'] = self.tm_comment
        if self.tm_icon is not None:
            result['TmIcon'] = self.tm_icon
        if self.tm_name is not None:
            result['TmName'] = self.tm_name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('TmComment') is not None:
            self.tm_comment = m.get('TmComment')
        if m.get('TmIcon') is not None:
            self.tm_icon = m.get('TmIcon')
        if m.get('TmName') is not None:
            self.tm_name = m.get('TmName')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class UpdateTrademarkNameResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_msg = error_msg
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
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateTrademarkNameResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateTrademarkNameResponseBody = None,
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
            temp_model = UpdateTrademarkNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateTrademarkOnsaleRequest(TeaModel):
    def __init__(
        self,
        begin_time: int = None,
        classification_code: str = None,
        description: str = None,
        end_time: int = None,
        label: str = None,
        original_price: float = None,
        owner_en_name: str = None,
        owner_name: str = None,
        reason: str = None,
        reg_ann_date: int = None,
        secondary_classification: str = None,
        third_classification: str = None,
        tm_icon: str = None,
        tm_name: str = None,
        tm_number: str = None,
        tm_type: str = None,
        trade_tm_detail_json: str = None,
        type: str = None,
    ):
        self.begin_time = begin_time
        self.classification_code = classification_code
        self.description = description
        self.end_time = end_time
        self.label = label
        self.original_price = original_price
        self.owner_en_name = owner_en_name
        self.owner_name = owner_name
        self.reason = reason
        self.reg_ann_date = reg_ann_date
        self.secondary_classification = secondary_classification
        self.third_classification = third_classification
        self.tm_icon = tm_icon
        self.tm_name = tm_name
        self.tm_number = tm_number
        self.tm_type = tm_type
        self.trade_tm_detail_json = trade_tm_detail_json
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.classification_code is not None:
            result['ClassificationCode'] = self.classification_code
        if self.description is not None:
            result['Description'] = self.description
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.label is not None:
            result['Label'] = self.label
        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price
        if self.owner_en_name is not None:
            result['OwnerEnName'] = self.owner_en_name
        if self.owner_name is not None:
            result['OwnerName'] = self.owner_name
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.reg_ann_date is not None:
            result['RegAnnDate'] = self.reg_ann_date
        if self.secondary_classification is not None:
            result['SecondaryClassification'] = self.secondary_classification
        if self.third_classification is not None:
            result['ThirdClassification'] = self.third_classification
        if self.tm_icon is not None:
            result['TmIcon'] = self.tm_icon
        if self.tm_name is not None:
            result['TmName'] = self.tm_name
        if self.tm_number is not None:
            result['TmNumber'] = self.tm_number
        if self.tm_type is not None:
            result['TmType'] = self.tm_type
        if self.trade_tm_detail_json is not None:
            result['TradeTmDetailJson'] = self.trade_tm_detail_json
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('ClassificationCode') is not None:
            self.classification_code = m.get('ClassificationCode')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('OriginalPrice') is not None:
            self.original_price = m.get('OriginalPrice')
        if m.get('OwnerEnName') is not None:
            self.owner_en_name = m.get('OwnerEnName')
        if m.get('OwnerName') is not None:
            self.owner_name = m.get('OwnerName')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('RegAnnDate') is not None:
            self.reg_ann_date = m.get('RegAnnDate')
        if m.get('SecondaryClassification') is not None:
            self.secondary_classification = m.get('SecondaryClassification')
        if m.get('ThirdClassification') is not None:
            self.third_classification = m.get('ThirdClassification')
        if m.get('TmIcon') is not None:
            self.tm_icon = m.get('TmIcon')
        if m.get('TmName') is not None:
            self.tm_name = m.get('TmName')
        if m.get('TmNumber') is not None:
            self.tm_number = m.get('TmNumber')
        if m.get('TmType') is not None:
            self.tm_type = m.get('TmType')
        if m.get('TradeTmDetailJson') is not None:
            self.trade_tm_detail_json = m.get('TradeTmDetailJson')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class UpdateTrademarkOnsaleResponseBody(TeaModel):
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


class UpdateTrademarkOnsaleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateTrademarkOnsaleResponseBody = None,
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
            temp_model = UpdateTrademarkOnsaleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UploadNotaryDataRequest(TeaModel):
    def __init__(
        self,
        biz_order_no: str = None,
        notary_type: int = None,
        upload_context: str = None,
    ):
        self.biz_order_no = biz_order_no
        self.notary_type = notary_type
        self.upload_context = upload_context

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_order_no is not None:
            result['BizOrderNo'] = self.biz_order_no
        if self.notary_type is not None:
            result['NotaryType'] = self.notary_type
        if self.upload_context is not None:
            result['UploadContext'] = self.upload_context
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizOrderNo') is not None:
            self.biz_order_no = m.get('BizOrderNo')
        if m.get('NotaryType') is not None:
            self.notary_type = m.get('NotaryType')
        if m.get('UploadContext') is not None:
            self.upload_context = m.get('UploadContext')
        return self


class UploadNotaryDataResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        user_auth_url: str = None,
    ):
        self.request_id = request_id
        self.user_auth_url = user_auth_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.user_auth_url is not None:
            result['UserAuthUrl'] = self.user_auth_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UserAuthUrl') is not None:
            self.user_auth_url = m.get('UserAuthUrl')
        return self


class UploadNotaryDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UploadNotaryDataResponseBody = None,
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
            temp_model = UploadNotaryDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UploadTrademarkOnSaleRequest(TeaModel):
    def __init__(
        self,
        begin_time: int = None,
        classification_code: str = None,
        description: str = None,
        end_time: int = None,
        label: str = None,
        original_price: float = None,
        owner_en_name: str = None,
        owner_name: str = None,
        reason: str = None,
        reg_ann_date: int = None,
        secondary_classification: str = None,
        status: str = None,
        third_classification: str = None,
        tm_icon: str = None,
        tm_name: str = None,
        tm_number: str = None,
        tm_type: str = None,
        trade_tm_detail_json: str = None,
        type: str = None,
    ):
        self.begin_time = begin_time
        self.classification_code = classification_code
        self.description = description
        self.end_time = end_time
        self.label = label
        self.original_price = original_price
        self.owner_en_name = owner_en_name
        self.owner_name = owner_name
        self.reason = reason
        self.reg_ann_date = reg_ann_date
        self.secondary_classification = secondary_classification
        self.status = status
        self.third_classification = third_classification
        self.tm_icon = tm_icon
        self.tm_name = tm_name
        self.tm_number = tm_number
        self.tm_type = tm_type
        self.trade_tm_detail_json = trade_tm_detail_json
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.classification_code is not None:
            result['ClassificationCode'] = self.classification_code
        if self.description is not None:
            result['Description'] = self.description
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.label is not None:
            result['Label'] = self.label
        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price
        if self.owner_en_name is not None:
            result['OwnerEnName'] = self.owner_en_name
        if self.owner_name is not None:
            result['OwnerName'] = self.owner_name
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.reg_ann_date is not None:
            result['RegAnnDate'] = self.reg_ann_date
        if self.secondary_classification is not None:
            result['SecondaryClassification'] = self.secondary_classification
        if self.status is not None:
            result['Status'] = self.status
        if self.third_classification is not None:
            result['ThirdClassification'] = self.third_classification
        if self.tm_icon is not None:
            result['TmIcon'] = self.tm_icon
        if self.tm_name is not None:
            result['TmName'] = self.tm_name
        if self.tm_number is not None:
            result['TmNumber'] = self.tm_number
        if self.tm_type is not None:
            result['TmType'] = self.tm_type
        if self.trade_tm_detail_json is not None:
            result['TradeTmDetailJson'] = self.trade_tm_detail_json
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('ClassificationCode') is not None:
            self.classification_code = m.get('ClassificationCode')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('OriginalPrice') is not None:
            self.original_price = m.get('OriginalPrice')
        if m.get('OwnerEnName') is not None:
            self.owner_en_name = m.get('OwnerEnName')
        if m.get('OwnerName') is not None:
            self.owner_name = m.get('OwnerName')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('RegAnnDate') is not None:
            self.reg_ann_date = m.get('RegAnnDate')
        if m.get('SecondaryClassification') is not None:
            self.secondary_classification = m.get('SecondaryClassification')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ThirdClassification') is not None:
            self.third_classification = m.get('ThirdClassification')
        if m.get('TmIcon') is not None:
            self.tm_icon = m.get('TmIcon')
        if m.get('TmName') is not None:
            self.tm_name = m.get('TmName')
        if m.get('TmNumber') is not None:
            self.tm_number = m.get('TmNumber')
        if m.get('TmType') is not None:
            self.tm_type = m.get('TmType')
        if m.get('TradeTmDetailJson') is not None:
            self.trade_tm_detail_json = m.get('TradeTmDetailJson')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class UploadTrademarkOnSaleResponseBody(TeaModel):
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


class UploadTrademarkOnSaleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UploadTrademarkOnSaleResponseBody = None,
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
            temp_model = UploadTrademarkOnSaleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class WriteCommunicationLogRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        note: str = None,
        target_id: str = None,
    ):
        self.biz_id = biz_id
        self.note = note
        self.target_id = target_id

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
        if self.target_id is not None:
            result['TargetId'] = self.target_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        if m.get('TargetId') is not None:
            self.target_id = m.get('TargetId')
        return self


class WriteCommunicationLogResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_msg = error_msg
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
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class WriteCommunicationLogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: WriteCommunicationLogResponseBody = None,
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
            temp_model = WriteCommunicationLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class WriteIntentionCommunicationLogRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        note: str = None,
        reject: bool = None,
    ):
        self.biz_id = biz_id
        self.note = note
        self.reject = reject

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
        if self.reject is not None:
            result['Reject'] = self.reject
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        if m.get('Reject') is not None:
            self.reject = m.get('Reject')
        return self


class WriteIntentionCommunicationLogResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_msg = error_msg
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
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class WriteIntentionCommunicationLogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: WriteIntentionCommunicationLogResponseBody = None,
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
            temp_model = WriteIntentionCommunicationLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


