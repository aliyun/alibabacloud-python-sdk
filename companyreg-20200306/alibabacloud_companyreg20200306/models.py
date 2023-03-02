# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict, Any


class BindProduceAuthorizationRequest(TeaModel):
    def __init__(
        self,
        authorized_user_ids: str = None,
        biz_id: str = None,
        biz_type: str = None,
    ):
        self.authorized_user_ids = authorized_user_ids
        self.biz_id = biz_id
        self.biz_type = biz_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorized_user_ids is not None:
            result['AuthorizedUserIds'] = self.authorized_user_ids
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorizedUserIds') is not None:
            self.authorized_user_ids = m.get('AuthorizedUserIds')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        return self


class BindProduceAuthorizationResponseBodyDataAuthorizedUserList(TeaModel):
    def __init__(
        self,
        account_valid_type: int = None,
        user_id: str = None,
        user_name: str = None,
    ):
        self.account_valid_type = account_valid_type
        self.user_id = user_id
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_valid_type is not None:
            result['AccountValidType'] = self.account_valid_type
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountValidType') is not None:
            self.account_valid_type = m.get('AccountValidType')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class BindProduceAuthorizationResponseBodyData(TeaModel):
    def __init__(
        self,
        authorized_user_list: List[BindProduceAuthorizationResponseBodyDataAuthorizedUserList] = None,
        message: str = None,
        success: bool = None,
    ):
        self.authorized_user_list = authorized_user_list
        self.message = message
        self.success = success

    def validate(self):
        if self.authorized_user_list:
            for k in self.authorized_user_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AuthorizedUserList'] = []
        if self.authorized_user_list is not None:
            for k in self.authorized_user_list:
                result['AuthorizedUserList'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.authorized_user_list = []
        if m.get('AuthorizedUserList') is not None:
            for k in m.get('AuthorizedUserList'):
                temp_model = BindProduceAuthorizationResponseBodyDataAuthorizedUserList()
                self.authorized_user_list.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class BindProduceAuthorizationResponseBody(TeaModel):
    def __init__(
        self,
        data: BindProduceAuthorizationResponseBodyData = None,
        error_code: str = None,
        error_msg: str = None,
        request_id: str = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_msg = error_msg
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
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = BindProduceAuthorizationResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class BindProduceAuthorizationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BindProduceAuthorizationResponseBody = None,
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
            temp_model = BindProduceAuthorizationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CloseIntentionForPartnerRequest(TeaModel):
    def __init__(
        self,
        biz_type: str = None,
        intention_biz_id: str = None,
        note: str = None,
    ):
        self.biz_type = biz_type
        self.intention_biz_id = intention_biz_id
        self.note = note

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.intention_biz_id is not None:
            result['IntentionBizId'] = self.intention_biz_id
        if self.note is not None:
            result['Note'] = self.note
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('IntentionBizId') is not None:
            self.intention_biz_id = m.get('IntentionBizId')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        return self


class CloseIntentionForPartnerResponseBody(TeaModel):
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


class CloseIntentionForPartnerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CloseIntentionForPartnerResponseBody = None,
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
            temp_model = CloseIntentionForPartnerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CloseUserIntentionRequest(TeaModel):
    def __init__(
        self,
        biz_type: str = None,
        intention_biz_id: str = None,
        note: str = None,
    ):
        self.biz_type = biz_type
        self.intention_biz_id = intention_biz_id
        self.note = note

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.intention_biz_id is not None:
            result['IntentionBizId'] = self.intention_biz_id
        if self.note is not None:
            result['Note'] = self.note
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('IntentionBizId') is not None:
            self.intention_biz_id = m.get('IntentionBizId')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        return self


class CloseUserIntentionResponseBody(TeaModel):
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


class CloseUserIntentionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CloseUserIntentionResponseBody = None,
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
            temp_model = CloseUserIntentionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateBusinessOpportunityRequest(TeaModel):
    def __init__(
        self,
        biz_type: str = None,
        contact_name: str = None,
        mobile: str = None,
        source: int = None,
        vcode: str = None,
    ):
        self.biz_type = biz_type
        self.contact_name = contact_name
        self.mobile = mobile
        self.source = source
        self.vcode = vcode

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.contact_name is not None:
            result['ContactName'] = self.contact_name
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.source is not None:
            result['Source'] = self.source
        if self.vcode is not None:
            result['VCode'] = self.vcode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('VCode') is not None:
            self.vcode = m.get('VCode')
        return self


class CreateBusinessOpportunityResponseBody(TeaModel):
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


class CreateBusinessOpportunityResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateBusinessOpportunityResponseBody = None,
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
            temp_model = CreateBusinessOpportunityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateProduceForPartnerRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        biz_type: str = None,
        ext_info: str = None,
    ):
        self.biz_id = biz_id
        self.biz_type = biz_type
        self.ext_info = ext_info

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
        if self.ext_info is not None:
            result['ExtInfo'] = self.ext_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('ExtInfo') is not None:
            self.ext_info = m.get('ExtInfo')
        return self


class CreateProduceForPartnerResponseBody(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        error_code: str = None,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.biz_id = biz_id
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
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
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
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateProduceForPartnerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateProduceForPartnerResponseBody = None,
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
            temp_model = CreateProduceForPartnerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePartnerConfigRequest(TeaModel):
    def __init__(
        self,
        biz_type: str = None,
        partner_code: str = None,
    ):
        self.biz_type = biz_type
        self.partner_code = partner_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.partner_code is not None:
            result['PartnerCode'] = self.partner_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('PartnerCode') is not None:
            self.partner_code = m.get('PartnerCode')
        return self


class DescribePartnerConfigResponseBody(TeaModel):
    def __init__(
        self,
        contact: str = None,
        partner_code: str = None,
        partner_name: str = None,
        request_id: str = None,
    ):
        self.contact = contact
        self.partner_code = partner_code
        self.partner_name = partner_name
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact is not None:
            result['Contact'] = self.contact
        if self.partner_code is not None:
            result['PartnerCode'] = self.partner_code
        if self.partner_name is not None:
            result['PartnerName'] = self.partner_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Contact') is not None:
            self.contact = m.get('Contact')
        if m.get('PartnerCode') is not None:
            self.partner_code = m.get('PartnerCode')
        if m.get('PartnerName') is not None:
            self.partner_name = m.get('PartnerName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribePartnerConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribePartnerConfigResponseBody = None,
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
            temp_model = DescribePartnerConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateUploadFilePolicyRequest(TeaModel):
    def __init__(
        self,
        biz_type: str = None,
        file_name: str = None,
        file_type: str = None,
    ):
        self.biz_type = biz_type
        self.file_name = file_name
        self.file_type = file_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_type is not None:
            result['FileType'] = self.file_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')
        return self


class GenerateUploadFilePolicyResponseBody(TeaModel):
    def __init__(
        self,
        access_id: str = None,
        encoded_policy: str = None,
        expire_time: str = None,
        file_dir: str = None,
        file_url: str = None,
        host: str = None,
        request_id: str = None,
        signature: str = None,
    ):
        # OSSAccessKeyId
        self.access_id = access_id
        self.encoded_policy = encoded_policy
        self.expire_time = expire_time
        self.file_dir = file_dir
        self.file_url = file_url
        # OSS Endpoint。
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
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
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
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
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
            temp_model = GetAlipayUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListIntentionNoteRequest(TeaModel):
    def __init__(
        self,
        begin_time: int = None,
        end_time: int = None,
        intention_biz_id: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.begin_time = begin_time
        self.end_time = end_time
        self.intention_biz_id = intention_biz_id
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.intention_biz_id is not None:
            result['IntentionBizId'] = self.intention_biz_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('IntentionBizId') is not None:
            self.intention_biz_id = m.get('IntentionBizId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListIntentionNoteResponseBodyData(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        intention_biz_id: str = None,
        note: str = None,
        source: int = None,
        type: str = None,
    ):
        self.create_time = create_time
        self.intention_biz_id = intention_biz_id
        self.note = note
        self.source = source
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.intention_biz_id is not None:
            result['IntentionBizId'] = self.intention_biz_id
        if self.note is not None:
            result['Note'] = self.note
        if self.source is not None:
            result['Source'] = self.source
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('IntentionBizId') is not None:
            self.intention_biz_id = m.get('IntentionBizId')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListIntentionNoteResponseBody(TeaModel):
    def __init__(
        self,
        current_page_num: int = None,
        data: List[ListIntentionNoteResponseBodyData] = None,
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
                temp_model = ListIntentionNoteResponseBodyData()
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


class ListIntentionNoteResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListIntentionNoteResponseBody = None,
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
            temp_model = ListIntentionNoteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProduceAuthorizationRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        biz_type: str = None,
        page_num: int = None,
        page_size: int = None,
    ):
        self.biz_id = biz_id
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
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListProduceAuthorizationResponseBodyData(TeaModel):
    def __init__(
        self,
        authorized_user_id: str = None,
        authorized_user_name: str = None,
    ):
        self.authorized_user_id = authorized_user_id
        self.authorized_user_name = authorized_user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorized_user_id is not None:
            result['AuthorizedUserId'] = self.authorized_user_id
        if self.authorized_user_name is not None:
            result['AuthorizedUserName'] = self.authorized_user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorizedUserId') is not None:
            self.authorized_user_id = m.get('AuthorizedUserId')
        if m.get('AuthorizedUserName') is not None:
            self.authorized_user_name = m.get('AuthorizedUserName')
        return self


class ListProduceAuthorizationResponseBody(TeaModel):
    def __init__(
        self,
        current_page_num: int = None,
        data: List[ListProduceAuthorizationResponseBodyData] = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_item_num: int = None,
        total_page_num: int = None,
    ):
        self.current_page_num = current_page_num
        self.data = data
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
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
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListProduceAuthorizationResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalItemNum') is not None:
            self.total_item_num = m.get('TotalItemNum')
        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')
        return self


class ListProduceAuthorizationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListProduceAuthorizationResponseBody = None,
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
            temp_model = ListProduceAuthorizationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUserDetailSolutionsRequest(TeaModel):
    def __init__(
        self,
        biz_type: str = None,
        intention_biz_id: str = None,
        page_num: int = None,
        page_size: int = None,
    ):
        self.biz_type = biz_type
        self.intention_biz_id = intention_biz_id
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
        if self.intention_biz_id is not None:
            result['IntentionBizId'] = self.intention_biz_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('IntentionBizId') is not None:
            self.intention_biz_id = m.get('IntentionBizId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListUserDetailSolutionsResponseBodyData(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        biz_type: str = None,
        create_time: int = None,
        delivery_order_biz_id: str = None,
        ext_info: str = None,
        intention_assign_biz_id: str = None,
        intention_biz_id: str = None,
        partner_code: str = None,
        reason: str = None,
        status: int = None,
        update_time: int = None,
        user_id: str = None,
    ):
        self.biz_id = biz_id
        self.biz_type = biz_type
        self.create_time = create_time
        self.delivery_order_biz_id = delivery_order_biz_id
        self.ext_info = ext_info
        self.intention_assign_biz_id = intention_assign_biz_id
        self.intention_biz_id = intention_biz_id
        self.partner_code = partner_code
        self.reason = reason
        self.status = status
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
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.delivery_order_biz_id is not None:
            result['DeliveryOrderBizId'] = self.delivery_order_biz_id
        if self.ext_info is not None:
            result['ExtInfo'] = self.ext_info
        if self.intention_assign_biz_id is not None:
            result['IntentionAssignBizId'] = self.intention_assign_biz_id
        if self.intention_biz_id is not None:
            result['IntentionBizId'] = self.intention_biz_id
        if self.partner_code is not None:
            result['PartnerCode'] = self.partner_code
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.status is not None:
            result['Status'] = self.status
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DeliveryOrderBizId') is not None:
            self.delivery_order_biz_id = m.get('DeliveryOrderBizId')
        if m.get('ExtInfo') is not None:
            self.ext_info = m.get('ExtInfo')
        if m.get('IntentionAssignBizId') is not None:
            self.intention_assign_biz_id = m.get('IntentionAssignBizId')
        if m.get('IntentionBizId') is not None:
            self.intention_biz_id = m.get('IntentionBizId')
        if m.get('PartnerCode') is not None:
            self.partner_code = m.get('PartnerCode')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ListUserDetailSolutionsResponseBody(TeaModel):
    def __init__(
        self,
        current_page_num: int = None,
        data: List[ListUserDetailSolutionsResponseBodyData] = None,
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
                temp_model = ListUserDetailSolutionsResponseBodyData()
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


class ListUserDetailSolutionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListUserDetailSolutionsResponseBody = None,
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
            temp_model = ListUserDetailSolutionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUserIntentionNotesRequest(TeaModel):
    def __init__(
        self,
        biz_type: str = None,
        intention_biz_id: str = None,
        page_num: int = None,
        page_size: int = None,
    ):
        self.biz_type = biz_type
        self.intention_biz_id = intention_biz_id
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
        if self.intention_biz_id is not None:
            result['IntentionBizId'] = self.intention_biz_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('IntentionBizId') is not None:
            self.intention_biz_id = m.get('IntentionBizId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListUserIntentionNotesResponseBodyData(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        note: str = None,
    ):
        self.create_time = create_time
        self.note = note

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.note is not None:
            result['Note'] = self.note
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        return self


class ListUserIntentionNotesResponseBody(TeaModel):
    def __init__(
        self,
        data: List[ListUserIntentionNotesResponseBodyData] = None,
        page_num: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_item_num: int = None,
        total_page_num: int = None,
    ):
        self.data = data
        self.page_num = page_num
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
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
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
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
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListUserIntentionNotesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalItemNum') is not None:
            self.total_item_num = m.get('TotalItemNum')
        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')
        return self


class ListUserIntentionNotesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListUserIntentionNotesResponseBody = None,
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
            temp_model = ListUserIntentionNotesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUserIntentionsRequest(TeaModel):
    def __init__(
        self,
        area: str = None,
        biz_type: str = None,
        biz_types: str = None,
        intention_biz_id: str = None,
        page_num: int = None,
        page_size: int = None,
        sort_filed: str = None,
        sort_order: str = None,
        status: int = None,
        with_ext_info: bool = None,
    ):
        self.area = area
        self.biz_type = biz_type
        self.biz_types = biz_types
        self.intention_biz_id = intention_biz_id
        self.page_num = page_num
        self.page_size = page_size
        self.sort_filed = sort_filed
        self.sort_order = sort_order
        self.status = status
        self.with_ext_info = with_ext_info

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.area is not None:
            result['Area'] = self.area
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.biz_types is not None:
            result['BizTypes'] = self.biz_types
        if self.intention_biz_id is not None:
            result['IntentionBizId'] = self.intention_biz_id
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
        if self.with_ext_info is not None:
            result['WithExtInfo'] = self.with_ext_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Area') is not None:
            self.area = m.get('Area')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('BizTypes') is not None:
            self.biz_types = m.get('BizTypes')
        if m.get('IntentionBizId') is not None:
            self.intention_biz_id = m.get('IntentionBizId')
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
        if m.get('WithExtInfo') is not None:
            self.with_ext_info = m.get('WithExtInfo')
        return self


class ListUserIntentionsResponseBodyData(TeaModel):
    def __init__(
        self,
        area: str = None,
        biz_id: str = None,
        biz_type: str = None,
        contact_name: str = None,
        create_time: int = None,
        description: str = None,
        ext: str = None,
        mobile: str = None,
        reason: str = None,
        status: int = None,
        update_time: int = None,
        user_id: str = None,
    ):
        self.area = area
        self.biz_id = biz_id
        self.biz_type = biz_type
        self.contact_name = contact_name
        self.create_time = create_time
        self.description = description
        self.ext = ext
        self.mobile = mobile
        self.reason = reason
        self.status = status
        self.update_time = update_time
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.area is not None:
            result['Area'] = self.area
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.contact_name is not None:
            result['ContactName'] = self.contact_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.ext is not None:
            result['Ext'] = self.ext
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.status is not None:
            result['Status'] = self.status
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Area') is not None:
            self.area = m.get('Area')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Ext') is not None:
            self.ext = m.get('Ext')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ListUserIntentionsResponseBody(TeaModel):
    def __init__(
        self,
        current_page_num: int = None,
        data: List[ListUserIntentionsResponseBodyData] = None,
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
                temp_model = ListUserIntentionsResponseBodyData()
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


class ListUserIntentionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListUserIntentionsResponseBody = None,
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
            temp_model = ListUserIntentionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUserProduceOperateLogsRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        biz_type: str = None,
        page_num: int = None,
        page_size: int = None,
    ):
        self.biz_id = biz_id
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
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListUserProduceOperateLogsResponseBodyData(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        biz_status: int = None,
        biz_type: str = None,
        note: str = None,
        operate_name: str = None,
        operate_time: int = None,
        operate_user_type: str = None,
        to_biz_status: int = None,
    ):
        self.biz_id = biz_id
        self.biz_status = biz_status
        self.biz_type = biz_type
        self.note = note
        self.operate_name = operate_name
        self.operate_time = operate_time
        self.operate_user_type = operate_user_type
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
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.note is not None:
            result['Note'] = self.note
        if self.operate_name is not None:
            result['OperateName'] = self.operate_name
        if self.operate_time is not None:
            result['OperateTime'] = self.operate_time
        if self.operate_user_type is not None:
            result['OperateUserType'] = self.operate_user_type
        if self.to_biz_status is not None:
            result['ToBizStatus'] = self.to_biz_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BizStatus') is not None:
            self.biz_status = m.get('BizStatus')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        if m.get('OperateName') is not None:
            self.operate_name = m.get('OperateName')
        if m.get('OperateTime') is not None:
            self.operate_time = m.get('OperateTime')
        if m.get('OperateUserType') is not None:
            self.operate_user_type = m.get('OperateUserType')
        if m.get('ToBizStatus') is not None:
            self.to_biz_status = m.get('ToBizStatus')
        return self


class ListUserProduceOperateLogsResponseBody(TeaModel):
    def __init__(
        self,
        data: List[ListUserProduceOperateLogsResponseBodyData] = None,
        page_num: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_item_num: int = None,
        total_page_num: int = None,
    ):
        self.data = data
        self.page_num = page_num
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
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
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
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
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListUserProduceOperateLogsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalItemNum') is not None:
            self.total_item_num = m.get('TotalItemNum')
        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')
        return self


class ListUserProduceOperateLogsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListUserProduceOperateLogsResponseBody = None,
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
            temp_model = ListUserProduceOperateLogsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUserSolutionsRequest(TeaModel):
    def __init__(
        self,
        exist_status: List[int] = None,
        intention_biz_id: str = None,
        page_num: int = None,
        page_size: int = None,
    ):
        self.exist_status = exist_status
        self.intention_biz_id = intention_biz_id
        self.page_num = page_num
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exist_status is not None:
            result['ExistStatus'] = self.exist_status
        if self.intention_biz_id is not None:
            result['IntentionBizId'] = self.intention_biz_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExistStatus') is not None:
            self.exist_status = m.get('ExistStatus')
        if m.get('IntentionBizId') is not None:
            self.intention_biz_id = m.get('IntentionBizId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListUserSolutionsShrinkRequest(TeaModel):
    def __init__(
        self,
        exist_status_shrink: str = None,
        intention_biz_id: str = None,
        page_num: int = None,
        page_size: int = None,
    ):
        self.exist_status_shrink = exist_status_shrink
        self.intention_biz_id = intention_biz_id
        self.page_num = page_num
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exist_status_shrink is not None:
            result['ExistStatus'] = self.exist_status_shrink
        if self.intention_biz_id is not None:
            result['IntentionBizId'] = self.intention_biz_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExistStatus') is not None:
            self.exist_status_shrink = m.get('ExistStatus')
        if m.get('IntentionBizId') is not None:
            self.intention_biz_id = m.get('IntentionBizId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListUserSolutionsResponseBodyData(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        biz_type: str = None,
        create_time: int = None,
        delivery_order_biz_id: str = None,
        intention_assign_biz_id: str = None,
        intention_biz_id: str = None,
        partner_code: str = None,
        reason: str = None,
        status: int = None,
        update_time: int = None,
        user_id: str = None,
    ):
        self.biz_id = biz_id
        self.biz_type = biz_type
        self.create_time = create_time
        self.delivery_order_biz_id = delivery_order_biz_id
        self.intention_assign_biz_id = intention_assign_biz_id
        self.intention_biz_id = intention_biz_id
        self.partner_code = partner_code
        self.reason = reason
        self.status = status
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
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.delivery_order_biz_id is not None:
            result['DeliveryOrderBizId'] = self.delivery_order_biz_id
        if self.intention_assign_biz_id is not None:
            result['IntentionAssignBizId'] = self.intention_assign_biz_id
        if self.intention_biz_id is not None:
            result['IntentionBizId'] = self.intention_biz_id
        if self.partner_code is not None:
            result['PartnerCode'] = self.partner_code
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.status is not None:
            result['Status'] = self.status
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DeliveryOrderBizId') is not None:
            self.delivery_order_biz_id = m.get('DeliveryOrderBizId')
        if m.get('IntentionAssignBizId') is not None:
            self.intention_assign_biz_id = m.get('IntentionAssignBizId')
        if m.get('IntentionBizId') is not None:
            self.intention_biz_id = m.get('IntentionBizId')
        if m.get('PartnerCode') is not None:
            self.partner_code = m.get('PartnerCode')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ListUserSolutionsResponseBody(TeaModel):
    def __init__(
        self,
        current_page_num: int = None,
        data: List[ListUserSolutionsResponseBodyData] = None,
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
                temp_model = ListUserSolutionsResponseBodyData()
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


class ListUserSolutionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListUserSolutionsResponseBody = None,
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
            temp_model = ListUserSolutionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OperateProduceForPartnerRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        biz_type: str = None,
        ext_info: str = None,
        operate_type: str = None,
    ):
        self.biz_id = biz_id
        self.biz_type = biz_type
        self.ext_info = ext_info
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
        if self.ext_info is not None:
            result['ExtInfo'] = self.ext_info
        if self.operate_type is not None:
            result['OperateType'] = self.operate_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('ExtInfo') is not None:
            self.ext_info = m.get('ExtInfo')
        if m.get('OperateType') is not None:
            self.operate_type = m.get('OperateType')
        return self


class OperateProduceForPartnerResponseBody(TeaModel):
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


class OperateProduceForPartnerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: OperateProduceForPartnerResponseBody = None,
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
            temp_model = OperateProduceForPartnerResponseBody()
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
            temp_model = PutMeasureReadyFlagResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryAvailableNumbersRequest(TeaModel):
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


class QueryAvailableNumbersResponseBody(TeaModel):
    def __init__(
        self,
        data: List[str] = None,
        error_code: str = None,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
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
        if self.data is not None:
            result['Data'] = self.data
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
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryAvailableNumbersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryAvailableNumbersResponseBody = None,
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
            temp_model = QueryAvailableNumbersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryBagRemainingRequest(TeaModel):
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


class QueryBagRemainingResponseBody(TeaModel):
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


class QueryBagRemainingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryBagRemainingResponseBody = None,
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
            temp_model = QueryBagRemainingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryCommodityConfigRequest(TeaModel):
    def __init__(
        self,
        biz_type: str = None,
        commodity_code: str = None,
        query_module: bool = None,
    ):
        self.biz_type = biz_type
        self.commodity_code = commodity_code
        self.query_module = query_module

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        if self.query_module is not None:
            result['QueryModule'] = self.query_module
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        if m.get('QueryModule') is not None:
            self.query_module = m.get('QueryModule')
        return self


class QueryCommodityConfigResponseBodyDataCommodityModules(TeaModel):
    def __init__(
        self,
        lx_module_code: str = None,
        module_code: str = None,
        module_description: str = None,
        module_name: str = None,
        module_tip: str = None,
        module_type: str = None,
        module_url: str = None,
        module_value: str = None,
        sort_number: int = None,
    ):
        self.lx_module_code = lx_module_code
        self.module_code = module_code
        self.module_description = module_description
        self.module_name = module_name
        self.module_tip = module_tip
        self.module_type = module_type
        self.module_url = module_url
        self.module_value = module_value
        self.sort_number = sort_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lx_module_code is not None:
            result['LxModuleCode'] = self.lx_module_code
        if self.module_code is not None:
            result['ModuleCode'] = self.module_code
        if self.module_description is not None:
            result['ModuleDescription'] = self.module_description
        if self.module_name is not None:
            result['ModuleName'] = self.module_name
        if self.module_tip is not None:
            result['ModuleTip'] = self.module_tip
        if self.module_type is not None:
            result['ModuleType'] = self.module_type
        if self.module_url is not None:
            result['ModuleUrl'] = self.module_url
        if self.module_value is not None:
            result['ModuleValue'] = self.module_value
        if self.sort_number is not None:
            result['SortNumber'] = self.sort_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LxModuleCode') is not None:
            self.lx_module_code = m.get('LxModuleCode')
        if m.get('ModuleCode') is not None:
            self.module_code = m.get('ModuleCode')
        if m.get('ModuleDescription') is not None:
            self.module_description = m.get('ModuleDescription')
        if m.get('ModuleName') is not None:
            self.module_name = m.get('ModuleName')
        if m.get('ModuleTip') is not None:
            self.module_tip = m.get('ModuleTip')
        if m.get('ModuleType') is not None:
            self.module_type = m.get('ModuleType')
        if m.get('ModuleUrl') is not None:
            self.module_url = m.get('ModuleUrl')
        if m.get('ModuleValue') is not None:
            self.module_value = m.get('ModuleValue')
        if m.get('SortNumber') is not None:
            self.sort_number = m.get('SortNumber')
        return self


class QueryCommodityConfigResponseBodyData(TeaModel):
    def __init__(
        self,
        commodity_code: str = None,
        commodity_modules: List[QueryCommodityConfigResponseBodyDataCommodityModules] = None,
        description: str = None,
        icon_url: str = None,
        product_line: str = None,
        protocol_url: str = None,
        starting_price: str = None,
        type: int = None,
    ):
        self.commodity_code = commodity_code
        self.commodity_modules = commodity_modules
        self.description = description
        self.icon_url = icon_url
        self.product_line = product_line
        self.protocol_url = protocol_url
        self.starting_price = starting_price
        self.type = type

    def validate(self):
        if self.commodity_modules:
            for k in self.commodity_modules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        result['CommodityModules'] = []
        if self.commodity_modules is not None:
            for k in self.commodity_modules:
                result['CommodityModules'].append(k.to_map() if k else None)
        if self.description is not None:
            result['Description'] = self.description
        if self.icon_url is not None:
            result['IconUrl'] = self.icon_url
        if self.product_line is not None:
            result['ProductLine'] = self.product_line
        if self.protocol_url is not None:
            result['ProtocolUrl'] = self.protocol_url
        if self.starting_price is not None:
            result['StartingPrice'] = self.starting_price
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        self.commodity_modules = []
        if m.get('CommodityModules') is not None:
            for k in m.get('CommodityModules'):
                temp_model = QueryCommodityConfigResponseBodyDataCommodityModules()
                self.commodity_modules.append(temp_model.from_map(k))
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('IconUrl') is not None:
            self.icon_url = m.get('IconUrl')
        if m.get('ProductLine') is not None:
            self.product_line = m.get('ProductLine')
        if m.get('ProtocolUrl') is not None:
            self.protocol_url = m.get('ProtocolUrl')
        if m.get('StartingPrice') is not None:
            self.starting_price = m.get('StartingPrice')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class QueryCommodityConfigResponseBody(TeaModel):
    def __init__(
        self,
        data: QueryCommodityConfigResponseBodyData = None,
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
            temp_model = QueryCommodityConfigResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryCommodityConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryCommodityConfigResponseBody = None,
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
            temp_model = QueryCommodityConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryInstanceRequest(TeaModel):
    def __init__(
        self,
        biz_type: str = None,
        instance_id: str = None,
    ):
        self.biz_type = biz_type
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class QueryInstanceResponseBody(TeaModel):
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


class QueryInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryInstanceResponseBody = None,
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
            temp_model = QueryInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryPartnerIntentionListRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        biz_type: str = None,
        page_num: int = None,
        page_size: int = None,
    ):
        self.biz_id = biz_id
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
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class QueryPartnerIntentionListResponseBodyData(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        biz_type: str = None,
        mobile: str = None,
    ):
        self.biz_id = biz_id
        self.biz_type = biz_type
        self.mobile = mobile

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
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        return self


class QueryPartnerIntentionListResponseBody(TeaModel):
    def __init__(
        self,
        current_page_num: int = None,
        data: List[QueryPartnerIntentionListResponseBodyData] = None,
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
                temp_model = QueryPartnerIntentionListResponseBodyData()
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


class QueryPartnerIntentionListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryPartnerIntentionListResponseBody = None,
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
            temp_model = QueryPartnerIntentionListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryPartnerProduceListRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        biz_type: str = None,
        page_num: int = None,
        page_size: int = None,
    ):
        self.biz_id = biz_id
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
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class QueryPartnerProduceListResponseBodyData(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        biz_type: str = None,
        mobile: str = None,
    ):
        self.biz_id = biz_id
        self.biz_type = biz_type
        self.mobile = mobile

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
        if self.mobile is not None:
            result['mobile'] = self.mobile
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('mobile') is not None:
            self.mobile = m.get('mobile')
        return self


class QueryPartnerProduceListResponseBody(TeaModel):
    def __init__(
        self,
        current_page_num: int = None,
        data: List[QueryPartnerProduceListResponseBodyData] = None,
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
                temp_model = QueryPartnerProduceListResponseBodyData()
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


class QueryPartnerProduceListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryPartnerProduceListResponseBody = None,
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
            temp_model = QueryPartnerProduceListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryUserNeedAuthResponseBody(TeaModel):
    def __init__(
        self,
        need_auth: bool = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.need_auth = need_auth
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.need_auth is not None:
            result['NeedAuth'] = self.need_auth
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NeedAuth') is not None:
            self.need_auth = m.get('NeedAuth')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryUserNeedAuthResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryUserNeedAuthResponseBody = None,
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
            temp_model = QueryUserNeedAuthResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecordPostBackRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        biz_type: str = None,
        contactor: str = None,
        content: str = None,
        entity_key: str = None,
    ):
        self.biz_id = biz_id
        self.biz_type = biz_type
        self.contactor = contactor
        self.content = content
        self.entity_key = entity_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['bizId'] = self.biz_id
        if self.biz_type is not None:
            result['bizType'] = self.biz_type
        if self.contactor is not None:
            result['contactor'] = self.contactor
        if self.content is not None:
            result['content'] = self.content
        if self.entity_key is not None:
            result['entityKey'] = self.entity_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bizId') is not None:
            self.biz_id = m.get('bizId')
        if m.get('bizType') is not None:
            self.biz_type = m.get('bizType')
        if m.get('contactor') is not None:
            self.contactor = m.get('contactor')
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('entityKey') is not None:
            self.entity_key = m.get('entityKey')
        return self


class RecordPostBackResponseBody(TeaModel):
    def __init__(
        self,
        allow_retry: bool = None,
        app_name: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_args: List[Any] = None,
        error_code: str = None,
        error_msg: str = None,
        http_status_code: int = None,
        module: bool = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.allow_retry = allow_retry
        self.app_name = app_name
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.error_args = error_args
        self.error_code = error_code
        self.error_msg = error_msg
        self.http_status_code = http_status_code
        self.module = module
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
        if self.error_args is not None:
            result['ErrorArgs'] = self.error_args
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.module is not None:
            result['Module'] = self.module
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
        if m.get('ErrorArgs') is not None:
            self.error_args = m.get('ErrorArgs')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Module') is not None:
            self.module = m.get('Module')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RecordPostBackResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RecordPostBackResponseBody = None,
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
            temp_model = RecordPostBackResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RejectSolutionRequest(TeaModel):
    def __init__(
        self,
        note: str = None,
        solution_biz_id: str = None,
    ):
        self.note = note
        self.solution_biz_id = solution_biz_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.note is not None:
            result['Note'] = self.note
        if self.solution_biz_id is not None:
            result['SolutionBizId'] = self.solution_biz_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Note') is not None:
            self.note = m.get('Note')
        if m.get('SolutionBizId') is not None:
            self.solution_biz_id = m.get('SolutionBizId')
        return self


class RejectSolutionResponseBody(TeaModel):
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


class RejectSolutionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RejectSolutionResponseBody = None,
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
            temp_model = RejectSolutionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RejectUserSolutionRequest(TeaModel):
    def __init__(
        self,
        biz_type: str = None,
        note: str = None,
        solution_biz_id: str = None,
    ):
        self.biz_type = biz_type
        self.note = note
        self.solution_biz_id = solution_biz_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.note is not None:
            result['Note'] = self.note
        if self.solution_biz_id is not None:
            result['SolutionBizId'] = self.solution_biz_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        if m.get('SolutionBizId') is not None:
            self.solution_biz_id = m.get('SolutionBizId')
        return self


class RejectUserSolutionResponseBody(TeaModel):
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


class RejectUserSolutionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RejectUserSolutionResponseBody = None,
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
            temp_model = RejectUserSolutionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReleaseProduceAuthorizationRequest(TeaModel):
    def __init__(
        self,
        authorized_user_id: str = None,
        biz_id: str = None,
        biz_type: str = None,
    ):
        self.authorized_user_id = authorized_user_id
        self.biz_id = biz_id
        self.biz_type = biz_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorized_user_id is not None:
            result['AuthorizedUserId'] = self.authorized_user_id
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorizedUserId') is not None:
            self.authorized_user_id = m.get('AuthorizedUserId')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        return self


class ReleaseProduceAuthorizationResponseBody(TeaModel):
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


class ReleaseProduceAuthorizationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ReleaseProduceAuthorizationResponseBody = None,
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
            temp_model = ReleaseProduceAuthorizationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartBackToBackCallRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        biz_type: str = None,
        call_center_number: str = None,
        caller: str = None,
        mobile_key: str = None,
        skill_type: int = None,
    ):
        self.biz_id = biz_id
        self.biz_type = biz_type
        self.call_center_number = call_center_number
        self.caller = caller
        self.mobile_key = mobile_key
        self.skill_type = skill_type

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
        if self.call_center_number is not None:
            result['CallCenterNumber'] = self.call_center_number
        if self.caller is not None:
            result['Caller'] = self.caller
        if self.mobile_key is not None:
            result['MobileKey'] = self.mobile_key
        if self.skill_type is not None:
            result['SkillType'] = self.skill_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('CallCenterNumber') is not None:
            self.call_center_number = m.get('CallCenterNumber')
        if m.get('Caller') is not None:
            self.caller = m.get('Caller')
        if m.get('MobileKey') is not None:
            self.mobile_key = m.get('MobileKey')
        if m.get('SkillType') is not None:
            self.skill_type = m.get('SkillType')
        return self


class StartBackToBackCallResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        error_code: str = None,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
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
        if self.data is not None:
            result['Data'] = self.data
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
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class StartBackToBackCallResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StartBackToBackCallResponseBody = None,
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
            temp_model = StartBackToBackCallResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitIntentionNoteRequest(TeaModel):
    def __init__(
        self,
        intention_biz_id: str = None,
        note: str = None,
    ):
        self.intention_biz_id = intention_biz_id
        self.note = note

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.intention_biz_id is not None:
            result['IntentionBizId'] = self.intention_biz_id
        if self.note is not None:
            result['Note'] = self.note
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IntentionBizId') is not None:
            self.intention_biz_id = m.get('IntentionBizId')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        return self


class SubmitIntentionNoteResponseBody(TeaModel):
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


class SubmitIntentionNoteResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SubmitIntentionNoteResponseBody = None,
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
            temp_model = SubmitIntentionNoteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitSolutionRequest(TeaModel):
    def __init__(
        self,
        biz_type: str = None,
        intention_biz_id: str = None,
        solution: str = None,
        user_id: str = None,
    ):
        self.biz_type = biz_type
        self.intention_biz_id = intention_biz_id
        self.solution = solution
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.intention_biz_id is not None:
            result['IntentionBizId'] = self.intention_biz_id
        if self.solution is not None:
            result['Solution'] = self.solution
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('IntentionBizId') is not None:
            self.intention_biz_id = m.get('IntentionBizId')
        if m.get('Solution') is not None:
            self.solution = m.get('Solution')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class SubmitSolutionResponseBody(TeaModel):
    def __init__(
        self,
        confirm_url: str = None,
        error_code: str = None,
        error_msg: str = None,
        request_id: str = None,
        solution_biz_id: str = None,
        success: bool = None,
    ):
        self.confirm_url = confirm_url
        self.error_code = error_code
        self.error_msg = error_msg
        self.request_id = request_id
        self.solution_biz_id = solution_biz_id
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
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.solution_biz_id is not None:
            result['SolutionBizId'] = self.solution_biz_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfirmUrl') is not None:
            self.confirm_url = m.get('ConfirmUrl')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SolutionBizId') is not None:
            self.solution_biz_id = m.get('SolutionBizId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SubmitSolutionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SubmitSolutionResponseBody = None,
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
            temp_model = SubmitSolutionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TransferIntentionOwnerRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        biz_type: str = None,
        person_id: int = None,
        remark: str = None,
    ):
        self.biz_id = biz_id
        self.biz_type = biz_type
        self.person_id = person_id
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
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.person_id is not None:
            result['PersonId'] = self.person_id
        if self.remark is not None:
            result['Remark'] = self.remark
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('PersonId') is not None:
            self.person_id = m.get('PersonId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        return self


class TransferIntentionOwnerResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        error_code: str = None,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
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
        if self.data is not None:
            result['Data'] = self.data
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
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class TransferIntentionOwnerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: TransferIntentionOwnerResponseBody = None,
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
            temp_model = TransferIntentionOwnerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TransferProduceOwnerRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        biz_type: str = None,
        person_id: int = None,
        remark: str = None,
    ):
        self.biz_id = biz_id
        self.biz_type = biz_type
        self.person_id = person_id
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
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.person_id is not None:
            result['PersonId'] = self.person_id
        if self.remark is not None:
            result['Remark'] = self.remark
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('PersonId') is not None:
            self.person_id = m.get('PersonId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        return self


class TransferProduceOwnerResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        error_code: str = None,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
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
        if self.data is not None:
            result['Data'] = self.data
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
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class TransferProduceOwnerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: TransferProduceOwnerResponseBody = None,
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
            temp_model = TransferProduceOwnerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


