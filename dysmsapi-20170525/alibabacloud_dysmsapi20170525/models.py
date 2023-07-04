# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List, Any


class AddShortUrlRequest(TeaModel):
    def __init__(
        self,
        effective_days: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        short_url_name: str = None,
        source_url: str = None,
    ):
        self.effective_days = effective_days
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.short_url_name = short_url_name
        self.source_url = source_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.effective_days is not None:
            result['EffectiveDays'] = self.effective_days
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.short_url_name is not None:
            result['ShortUrlName'] = self.short_url_name
        if self.source_url is not None:
            result['SourceUrl'] = self.source_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EffectiveDays') is not None:
            self.effective_days = m.get('EffectiveDays')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ShortUrlName') is not None:
            self.short_url_name = m.get('ShortUrlName')
        if m.get('SourceUrl') is not None:
            self.source_url = m.get('SourceUrl')
        return self


class AddShortUrlResponseBodyData(TeaModel):
    def __init__(
        self,
        expire_date: str = None,
        short_url: str = None,
        source_url: str = None,
    ):
        self.expire_date = expire_date
        self.short_url = short_url
        self.source_url = source_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expire_date is not None:
            result['ExpireDate'] = self.expire_date
        if self.short_url is not None:
            result['ShortUrl'] = self.short_url
        if self.source_url is not None:
            result['SourceUrl'] = self.source_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpireDate') is not None:
            self.expire_date = m.get('ExpireDate')
        if m.get('ShortUrl') is not None:
            self.short_url = m.get('ShortUrl')
        if m.get('SourceUrl') is not None:
            self.source_url = m.get('SourceUrl')
        return self


class AddShortUrlResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: AddShortUrlResponseBodyData = None,
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
            temp_model = AddShortUrlResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddShortUrlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddShortUrlResponseBody = None,
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
            temp_model = AddShortUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddSmsSignRequestSignFileList(TeaModel):
    def __init__(
        self,
        file_contents: str = None,
        file_suffix: str = None,
    ):
        self.file_contents = file_contents
        self.file_suffix = file_suffix

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_contents is not None:
            result['FileContents'] = self.file_contents
        if self.file_suffix is not None:
            result['FileSuffix'] = self.file_suffix
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileContents') is not None:
            self.file_contents = m.get('FileContents')
        if m.get('FileSuffix') is not None:
            self.file_suffix = m.get('FileSuffix')
        return self


class AddSmsSignRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        remark: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        sign_file_list: List[AddSmsSignRequestSignFileList] = None,
        sign_name: str = None,
        sign_source: int = None,
        sign_type: int = None,
    ):
        self.owner_id = owner_id
        self.remark = remark
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.sign_file_list = sign_file_list
        self.sign_name = sign_name
        self.sign_source = sign_source
        self.sign_type = sign_type

    def validate(self):
        if self.sign_file_list:
            for k in self.sign_file_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        result['SignFileList'] = []
        if self.sign_file_list is not None:
            for k in self.sign_file_list:
                result['SignFileList'].append(k.to_map() if k else None)
        if self.sign_name is not None:
            result['SignName'] = self.sign_name
        if self.sign_source is not None:
            result['SignSource'] = self.sign_source
        if self.sign_type is not None:
            result['SignType'] = self.sign_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        self.sign_file_list = []
        if m.get('SignFileList') is not None:
            for k in m.get('SignFileList'):
                temp_model = AddSmsSignRequestSignFileList()
                self.sign_file_list.append(temp_model.from_map(k))
        if m.get('SignName') is not None:
            self.sign_name = m.get('SignName')
        if m.get('SignSource') is not None:
            self.sign_source = m.get('SignSource')
        if m.get('SignType') is not None:
            self.sign_type = m.get('SignType')
        return self


class AddSmsSignResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        sign_name: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.sign_name = sign_name

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
        if self.sign_name is not None:
            result['SignName'] = self.sign_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SignName') is not None:
            self.sign_name = m.get('SignName')
        return self


class AddSmsSignResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddSmsSignResponseBody = None,
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
            temp_model = AddSmsSignResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddSmsTemplateRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        remark: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        template_content: str = None,
        template_name: str = None,
        template_type: int = None,
    ):
        self.owner_id = owner_id
        self.remark = remark
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.template_content = template_content
        self.template_name = template_name
        self.template_type = template_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.template_content is not None:
            result['TemplateContent'] = self.template_content
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TemplateContent') is not None:
            self.template_content = m.get('TemplateContent')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        return self


class AddSmsTemplateResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        template_code: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.template_code = template_code

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
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        return self


class AddSmsTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddSmsTemplateResponseBody = None,
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
            temp_model = AddSmsTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckMobilesCardSupportRequest(TeaModel):
    def __init__(
        self,
        mobiles: List[Dict[str, Any]] = None,
        template_code: str = None,
    ):
        self.mobiles = mobiles
        self.template_code = template_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mobiles is not None:
            result['Mobiles'] = self.mobiles
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Mobiles') is not None:
            self.mobiles = m.get('Mobiles')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        return self


class CheckMobilesCardSupportResponseBodyDataQueryResult(TeaModel):
    def __init__(
        self,
        mobile: str = None,
        support: bool = None,
    ):
        self.mobile = mobile
        self.support = support

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mobile is not None:
            result['mobile'] = self.mobile
        if self.support is not None:
            result['support'] = self.support
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('mobile') is not None:
            self.mobile = m.get('mobile')
        if m.get('support') is not None:
            self.support = m.get('support')
        return self


class CheckMobilesCardSupportResponseBodyData(TeaModel):
    def __init__(
        self,
        query_result: List[CheckMobilesCardSupportResponseBodyDataQueryResult] = None,
    ):
        self.query_result = query_result

    def validate(self):
        if self.query_result:
            for k in self.query_result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['queryResult'] = []
        if self.query_result is not None:
            for k in self.query_result:
                result['queryResult'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.query_result = []
        if m.get('queryResult') is not None:
            for k in m.get('queryResult'):
                temp_model = CheckMobilesCardSupportResponseBodyDataQueryResult()
                self.query_result.append(temp_model.from_map(k))
        return self


class CheckMobilesCardSupportResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CheckMobilesCardSupportResponseBodyData = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
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
            temp_model = CheckMobilesCardSupportResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CheckMobilesCardSupportResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CheckMobilesCardSupportResponseBody = None,
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
            temp_model = CheckMobilesCardSupportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConversionDataIntlRequest(TeaModel):
    def __init__(
        self,
        conversion_rate: str = None,
        owner_id: int = None,
        report_time: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.conversion_rate = conversion_rate
        self.owner_id = owner_id
        self.report_time = report_time
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.conversion_rate is not None:
            result['ConversionRate'] = self.conversion_rate
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.report_time is not None:
            result['ReportTime'] = self.report_time
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConversionRate') is not None:
            self.conversion_rate = m.get('ConversionRate')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ReportTime') is not None:
            self.report_time = m.get('ReportTime')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class ConversionDataIntlResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ConversionDataIntlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ConversionDataIntlResponseBody = None,
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
            temp_model = ConversionDataIntlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCardSmsTemplateRequest(TeaModel):
    def __init__(
        self,
        factorys: str = None,
        memo: str = None,
        template: Dict[str, Any] = None,
        template_name: str = None,
    ):
        self.factorys = factorys
        self.memo = memo
        self.template = template
        self.template_name = template_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.factorys is not None:
            result['Factorys'] = self.factorys
        if self.memo is not None:
            result['Memo'] = self.memo
        if self.template is not None:
            result['Template'] = self.template
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Factorys') is not None:
            self.factorys = m.get('Factorys')
        if m.get('Memo') is not None:
            self.memo = m.get('Memo')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        return self


class CreateCardSmsTemplateShrinkRequest(TeaModel):
    def __init__(
        self,
        factorys: str = None,
        memo: str = None,
        template_shrink: str = None,
        template_name: str = None,
    ):
        self.factorys = factorys
        self.memo = memo
        self.template_shrink = template_shrink
        self.template_name = template_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.factorys is not None:
            result['Factorys'] = self.factorys
        if self.memo is not None:
            result['Memo'] = self.memo
        if self.template_shrink is not None:
            result['Template'] = self.template_shrink
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Factorys') is not None:
            self.factorys = m.get('Factorys')
        if m.get('Memo') is not None:
            self.memo = m.get('Memo')
        if m.get('Template') is not None:
            self.template_shrink = m.get('Template')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        return self


class CreateCardSmsTemplateResponseBodyData(TeaModel):
    def __init__(
        self,
        template_code: str = None,
    ):
        self.template_code = template_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        return self


class CreateCardSmsTemplateResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CreateCardSmsTemplateResponseBodyData = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
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
            temp_model = CreateCardSmsTemplateResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateCardSmsTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateCardSmsTemplateResponseBody = None,
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
            temp_model = CreateCardSmsTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSmartShortUrlRequest(TeaModel):
    def __init__(
        self,
        expiration: int = None,
        owner_id: int = None,
        phone_numbers: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        source_name: str = None,
        source_url: str = None,
    ):
        self.expiration = expiration
        self.owner_id = owner_id
        self.phone_numbers = phone_numbers
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.source_name = source_name
        self.source_url = source_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expiration is not None:
            result['Expiration'] = self.expiration
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.phone_numbers is not None:
            result['PhoneNumbers'] = self.phone_numbers
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.source_name is not None:
            result['SourceName'] = self.source_name
        if self.source_url is not None:
            result['SourceUrl'] = self.source_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Expiration') is not None:
            self.expiration = m.get('Expiration')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PhoneNumbers') is not None:
            self.phone_numbers = m.get('PhoneNumbers')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SourceName') is not None:
            self.source_name = m.get('SourceName')
        if m.get('SourceUrl') is not None:
            self.source_url = m.get('SourceUrl')
        return self


class CreateSmartShortUrlResponseBodyModel(TeaModel):
    def __init__(
        self,
        domain: str = None,
        expiration: int = None,
        phone_number: str = None,
        short_name: str = None,
        short_url: str = None,
    ):
        self.domain = domain
        self.expiration = expiration
        self.phone_number = phone_number
        self.short_name = short_name
        self.short_url = short_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.expiration is not None:
            result['Expiration'] = self.expiration
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.short_name is not None:
            result['ShortName'] = self.short_name
        if self.short_url is not None:
            result['ShortUrl'] = self.short_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Expiration') is not None:
            self.expiration = m.get('Expiration')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('ShortName') is not None:
            self.short_name = m.get('ShortName')
        if m.get('ShortUrl') is not None:
            self.short_url = m.get('ShortUrl')
        return self


class CreateSmartShortUrlResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        model: List[CreateSmartShortUrlResponseBodyModel] = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.model = model
        self.request_id = request_id

    def validate(self):
        if self.model:
            for k in self.model:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        result['Model'] = []
        if self.model is not None:
            for k in self.model:
                result['Model'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        self.model = []
        if m.get('Model') is not None:
            for k in m.get('Model'):
                temp_model = CreateSmartShortUrlResponseBodyModel()
                self.model.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateSmartShortUrlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateSmartShortUrlResponseBody = None,
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
            temp_model = CreateSmartShortUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteShortUrlRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        source_url: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.source_url = source_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.source_url is not None:
            result['SourceUrl'] = self.source_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SourceUrl') is not None:
            self.source_url = m.get('SourceUrl')
        return self


class DeleteShortUrlResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteShortUrlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteShortUrlResponseBody = None,
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
            temp_model = DeleteShortUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSmsSignRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        sign_name: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.sign_name = sign_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.sign_name is not None:
            result['SignName'] = self.sign_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SignName') is not None:
            self.sign_name = m.get('SignName')
        return self


class DeleteSmsSignResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        sign_name: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.sign_name = sign_name

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
        if self.sign_name is not None:
            result['SignName'] = self.sign_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SignName') is not None:
            self.sign_name = m.get('SignName')
        return self


class DeleteSmsSignResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteSmsSignResponseBody = None,
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
            temp_model = DeleteSmsSignResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSmsTemplateRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        template_code: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.template_code = template_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        return self


class DeleteSmsTemplateResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        template_code: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.template_code = template_code

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
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        return self


class DeleteSmsTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteSmsTemplateResponseBody = None,
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
            temp_model = DeleteSmsTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCardSmsLinkRequest(TeaModel):
    def __init__(
        self,
        card_code_type: int = None,
        card_link_type: int = None,
        card_template_code: str = None,
        card_template_param_json: str = None,
        custom_short_code_json: str = None,
        domain: str = None,
        out_id: str = None,
        phone_number_json: str = None,
        sign_name_json: str = None,
    ):
        self.card_code_type = card_code_type
        self.card_link_type = card_link_type
        self.card_template_code = card_template_code
        self.card_template_param_json = card_template_param_json
        self.custom_short_code_json = custom_short_code_json
        self.domain = domain
        self.out_id = out_id
        self.phone_number_json = phone_number_json
        self.sign_name_json = sign_name_json

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.card_code_type is not None:
            result['CardCodeType'] = self.card_code_type
        if self.card_link_type is not None:
            result['CardLinkType'] = self.card_link_type
        if self.card_template_code is not None:
            result['CardTemplateCode'] = self.card_template_code
        if self.card_template_param_json is not None:
            result['CardTemplateParamJson'] = self.card_template_param_json
        if self.custom_short_code_json is not None:
            result['CustomShortCodeJson'] = self.custom_short_code_json
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.out_id is not None:
            result['OutId'] = self.out_id
        if self.phone_number_json is not None:
            result['PhoneNumberJson'] = self.phone_number_json
        if self.sign_name_json is not None:
            result['SignNameJson'] = self.sign_name_json
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CardCodeType') is not None:
            self.card_code_type = m.get('CardCodeType')
        if m.get('CardLinkType') is not None:
            self.card_link_type = m.get('CardLinkType')
        if m.get('CardTemplateCode') is not None:
            self.card_template_code = m.get('CardTemplateCode')
        if m.get('CardTemplateParamJson') is not None:
            self.card_template_param_json = m.get('CardTemplateParamJson')
        if m.get('CustomShortCodeJson') is not None:
            self.custom_short_code_json = m.get('CustomShortCodeJson')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('OutId') is not None:
            self.out_id = m.get('OutId')
        if m.get('PhoneNumberJson') is not None:
            self.phone_number_json = m.get('PhoneNumberJson')
        if m.get('SignNameJson') is not None:
            self.sign_name_json = m.get('SignNameJson')
        return self


class GetCardSmsLinkResponseBodyData(TeaModel):
    def __init__(
        self,
        card_phone_numbers: str = None,
        card_sign_names: str = None,
        card_sms_links: str = None,
        card_tmp_state: int = None,
        not_media_mobiles: str = None,
    ):
        self.card_phone_numbers = card_phone_numbers
        self.card_sign_names = card_sign_names
        self.card_sms_links = card_sms_links
        self.card_tmp_state = card_tmp_state
        self.not_media_mobiles = not_media_mobiles

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.card_phone_numbers is not None:
            result['CardPhoneNumbers'] = self.card_phone_numbers
        if self.card_sign_names is not None:
            result['CardSignNames'] = self.card_sign_names
        if self.card_sms_links is not None:
            result['CardSmsLinks'] = self.card_sms_links
        if self.card_tmp_state is not None:
            result['CardTmpState'] = self.card_tmp_state
        if self.not_media_mobiles is not None:
            result['NotMediaMobiles'] = self.not_media_mobiles
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CardPhoneNumbers') is not None:
            self.card_phone_numbers = m.get('CardPhoneNumbers')
        if m.get('CardSignNames') is not None:
            self.card_sign_names = m.get('CardSignNames')
        if m.get('CardSmsLinks') is not None:
            self.card_sms_links = m.get('CardSmsLinks')
        if m.get('CardTmpState') is not None:
            self.card_tmp_state = m.get('CardTmpState')
        if m.get('NotMediaMobiles') is not None:
            self.not_media_mobiles = m.get('NotMediaMobiles')
        return self


class GetCardSmsLinkResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetCardSmsLinkResponseBodyData = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
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
            temp_model = GetCardSmsLinkResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetCardSmsLinkResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetCardSmsLinkResponseBody = None,
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
            temp_model = GetCardSmsLinkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMediaResourceIdRequest(TeaModel):
    def __init__(
        self,
        extend_info: str = None,
        file_size: int = None,
        memo: str = None,
        oss_key: str = None,
        resource_type: int = None,
    ):
        self.extend_info = extend_info
        self.file_size = file_size
        self.memo = memo
        self.oss_key = oss_key
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extend_info is not None:
            result['ExtendInfo'] = self.extend_info
        if self.file_size is not None:
            result['FileSize'] = self.file_size
        if self.memo is not None:
            result['Memo'] = self.memo
        if self.oss_key is not None:
            result['OssKey'] = self.oss_key
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExtendInfo') is not None:
            self.extend_info = m.get('ExtendInfo')
        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')
        if m.get('Memo') is not None:
            self.memo = m.get('Memo')
        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class GetMediaResourceIdResponseBodyData(TeaModel):
    def __init__(
        self,
        res_url_download: str = None,
        resource_id: int = None,
    ):
        self.res_url_download = res_url_download
        self.resource_id = resource_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.res_url_download is not None:
            result['ResUrlDownload'] = self.res_url_download
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResUrlDownload') is not None:
            self.res_url_download = m.get('ResUrlDownload')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        return self


class GetMediaResourceIdResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetMediaResourceIdResponseBodyData = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
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
            temp_model = GetMediaResourceIdResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetMediaResourceIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetMediaResourceIdResponseBody = None,
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
            temp_model = GetMediaResourceIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOSSInfoForCardTemplateResponseBodyData(TeaModel):
    def __init__(
        self,
        access_key_id: str = None,
        ali_uid: str = None,
        bucket: str = None,
        expire_time: str = None,
        host: str = None,
        policy: str = None,
        signature: str = None,
        start_path: str = None,
    ):
        self.access_key_id = access_key_id
        self.ali_uid = ali_uid
        self.bucket = bucket
        self.expire_time = expire_time
        self.host = host
        self.policy = policy
        self.signature = signature
        self.start_path = start_path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key_id is not None:
            result['AccessKeyId'] = self.access_key_id
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.bucket is not None:
            result['Bucket'] = self.bucket
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.host is not None:
            result['Host'] = self.host
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.signature is not None:
            result['Signature'] = self.signature
        if self.start_path is not None:
            result['StartPath'] = self.start_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessKeyId') is not None:
            self.access_key_id = m.get('AccessKeyId')
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('Signature') is not None:
            self.signature = m.get('Signature')
        if m.get('StartPath') is not None:
            self.start_path = m.get('StartPath')
        return self


class GetOSSInfoForCardTemplateResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetOSSInfoForCardTemplateResponseBodyData = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
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
            temp_model = GetOSSInfoForCardTemplateResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetOSSInfoForCardTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetOSSInfoForCardTemplateResponseBody = None,
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
            temp_model = GetOSSInfoForCardTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagResourcesRequestTag(TeaModel):
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


class ListTagResourcesRequest(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        owner_id: int = None,
        page_size: int = None,
        prod_code: str = None,
        region_id: str = None,
        resource_id: List[str] = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        resource_type: str = None,
        tag: List[ListTagResourcesRequestTag] = None,
    ):
        self.next_token = next_token
        self.owner_id = owner_id
        self.page_size = page_size
        self.prod_code = prod_code
        self.region_id = region_id
        self.resource_id = resource_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.resource_type = resource_type
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListTagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponseBodyTagResourcesTagResource(TeaModel):
    def __init__(
        self,
        resource_id: str = None,
        resource_type: str = None,
        tag_key: str = None,
        tag_value: str = None,
    ):
        self.resource_id = resource_id
        self.resource_type = resource_type
        self.tag_key = tag_key
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class ListTagResourcesResponseBodyTagResources(TeaModel):
    def __init__(
        self,
        tag_resource: List[ListTagResourcesResponseBodyTagResourcesTagResource] = None,
    ):
        self.tag_resource = tag_resource

    def validate(self):
        if self.tag_resource:
            for k in self.tag_resource:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TagResource'] = []
        if self.tag_resource is not None:
            for k in self.tag_resource:
                result['TagResource'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag_resource = []
        if m.get('TagResource') is not None:
            for k in m.get('TagResource'):
                temp_model = ListTagResourcesResponseBodyTagResourcesTagResource()
                self.tag_resource.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        next_token: str = None,
        request_id: str = None,
        tag_resources: ListTagResourcesResponseBodyTagResources = None,
    ):
        self.code = code
        self.next_token = next_token
        self.request_id = request_id
        self.tag_resources = tag_resources

    def validate(self):
        if self.tag_resources:
            self.tag_resources.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tag_resources is not None:
            result['TagResources'] = self.tag_resources.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TagResources') is not None:
            temp_model = ListTagResourcesResponseBodyTagResources()
            self.tag_resources = temp_model.from_map(m['TagResources'])
        return self


class ListTagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTagResourcesResponseBody = None,
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
            temp_model = ListTagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifySmsSignRequestSignFileList(TeaModel):
    def __init__(
        self,
        file_contents: str = None,
        file_suffix: str = None,
    ):
        self.file_contents = file_contents
        self.file_suffix = file_suffix

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_contents is not None:
            result['FileContents'] = self.file_contents
        if self.file_suffix is not None:
            result['FileSuffix'] = self.file_suffix
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileContents') is not None:
            self.file_contents = m.get('FileContents')
        if m.get('FileSuffix') is not None:
            self.file_suffix = m.get('FileSuffix')
        return self


class ModifySmsSignRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        remark: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        sign_file_list: List[ModifySmsSignRequestSignFileList] = None,
        sign_name: str = None,
        sign_source: int = None,
        sign_type: int = None,
    ):
        self.owner_id = owner_id
        self.remark = remark
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.sign_file_list = sign_file_list
        self.sign_name = sign_name
        self.sign_source = sign_source
        self.sign_type = sign_type

    def validate(self):
        if self.sign_file_list:
            for k in self.sign_file_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        result['SignFileList'] = []
        if self.sign_file_list is not None:
            for k in self.sign_file_list:
                result['SignFileList'].append(k.to_map() if k else None)
        if self.sign_name is not None:
            result['SignName'] = self.sign_name
        if self.sign_source is not None:
            result['SignSource'] = self.sign_source
        if self.sign_type is not None:
            result['SignType'] = self.sign_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        self.sign_file_list = []
        if m.get('SignFileList') is not None:
            for k in m.get('SignFileList'):
                temp_model = ModifySmsSignRequestSignFileList()
                self.sign_file_list.append(temp_model.from_map(k))
        if m.get('SignName') is not None:
            self.sign_name = m.get('SignName')
        if m.get('SignSource') is not None:
            self.sign_source = m.get('SignSource')
        if m.get('SignType') is not None:
            self.sign_type = m.get('SignType')
        return self


class ModifySmsSignResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        sign_name: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.sign_name = sign_name

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
        if self.sign_name is not None:
            result['SignName'] = self.sign_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SignName') is not None:
            self.sign_name = m.get('SignName')
        return self


class ModifySmsSignResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifySmsSignResponseBody = None,
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
            temp_model = ModifySmsSignResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifySmsTemplateRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        remark: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        template_code: str = None,
        template_content: str = None,
        template_name: str = None,
        template_type: int = None,
    ):
        self.owner_id = owner_id
        self.remark = remark
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.template_code = template_code
        self.template_content = template_content
        self.template_name = template_name
        self.template_type = template_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.template_content is not None:
            result['TemplateContent'] = self.template_content
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('TemplateContent') is not None:
            self.template_content = m.get('TemplateContent')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        return self


class ModifySmsTemplateResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        template_code: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.template_code = template_code

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
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        return self


class ModifySmsTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifySmsTemplateResponseBody = None,
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
            temp_model = ModifySmsTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryCardSmsTemplateRequest(TeaModel):
    def __init__(
        self,
        template_code: str = None,
    ):
        self.template_code = template_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        return self


class QueryCardSmsTemplateResponseBodyData(TeaModel):
    def __init__(
        self,
        templates: List[Dict[str, Any]] = None,
    ):
        self.templates = templates

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.templates is not None:
            result['Templates'] = self.templates
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Templates') is not None:
            self.templates = m.get('Templates')
        return self


class QueryCardSmsTemplateResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: QueryCardSmsTemplateResponseBodyData = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
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
            temp_model = QueryCardSmsTemplateResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryCardSmsTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryCardSmsTemplateResponseBody = None,
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
            temp_model = QueryCardSmsTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryCardSmsTemplateReportRequest(TeaModel):
    def __init__(
        self,
        end_date: str = None,
        start_date: str = None,
        template_codes: List[str] = None,
    ):
        self.end_date = end_date
        self.start_date = start_date
        self.template_codes = template_codes

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.template_codes is not None:
            result['TemplateCodes'] = self.template_codes
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('TemplateCodes') is not None:
            self.template_codes = m.get('TemplateCodes')
        return self


class QueryCardSmsTemplateReportResponseBodyData(TeaModel):
    def __init__(
        self,
        model: List[Dict[str, Any]] = None,
    ):
        self.model = model

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.model is not None:
            result['model'] = self.model
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('model') is not None:
            self.model = m.get('model')
        return self


class QueryCardSmsTemplateReportResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: QueryCardSmsTemplateReportResponseBodyData = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
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
            temp_model = QueryCardSmsTemplateReportResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryCardSmsTemplateReportResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryCardSmsTemplateReportResponseBody = None,
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
            temp_model = QueryCardSmsTemplateReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryMobilesCardSupportRequest(TeaModel):
    def __init__(
        self,
        mobiles: List[Dict[str, Any]] = None,
        template_code: str = None,
    ):
        self.mobiles = mobiles
        self.template_code = template_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mobiles is not None:
            result['Mobiles'] = self.mobiles
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Mobiles') is not None:
            self.mobiles = m.get('Mobiles')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        return self


class QueryMobilesCardSupportShrinkRequest(TeaModel):
    def __init__(
        self,
        mobiles_shrink: str = None,
        template_code: str = None,
    ):
        self.mobiles_shrink = mobiles_shrink
        self.template_code = template_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mobiles_shrink is not None:
            result['Mobiles'] = self.mobiles_shrink
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Mobiles') is not None:
            self.mobiles_shrink = m.get('Mobiles')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        return self


class QueryMobilesCardSupportResponseBodyDataQueryResult(TeaModel):
    def __init__(
        self,
        mobile: str = None,
        support: bool = None,
    ):
        self.mobile = mobile
        self.support = support

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.support is not None:
            result['Support'] = self.support
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('Support') is not None:
            self.support = m.get('Support')
        return self


class QueryMobilesCardSupportResponseBodyData(TeaModel):
    def __init__(
        self,
        query_result: List[QueryMobilesCardSupportResponseBodyDataQueryResult] = None,
    ):
        self.query_result = query_result

    def validate(self):
        if self.query_result:
            for k in self.query_result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['QueryResult'] = []
        if self.query_result is not None:
            for k in self.query_result:
                result['QueryResult'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.query_result = []
        if m.get('QueryResult') is not None:
            for k in m.get('QueryResult'):
                temp_model = QueryMobilesCardSupportResponseBodyDataQueryResult()
                self.query_result.append(temp_model.from_map(k))
        return self


class QueryMobilesCardSupportResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: QueryMobilesCardSupportResponseBodyData = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
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
            temp_model = QueryMobilesCardSupportResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryMobilesCardSupportResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryMobilesCardSupportResponseBody = None,
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
            temp_model = QueryMobilesCardSupportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryPageSmartShortUrlLogRequest(TeaModel):
    def __init__(
        self,
        click_state: int = None,
        create_date_end: int = None,
        create_date_start: int = None,
        end_id: int = None,
        owner_id: int = None,
        page_no: int = None,
        page_size: int = None,
        phone_number: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        short_name: str = None,
        short_url: str = None,
        start_id: int = None,
    ):
        self.click_state = click_state
        self.create_date_end = create_date_end
        self.create_date_start = create_date_start
        self.end_id = end_id
        self.owner_id = owner_id
        self.page_no = page_no
        self.page_size = page_size
        self.phone_number = phone_number
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.short_name = short_name
        self.short_url = short_url
        self.start_id = start_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.click_state is not None:
            result['ClickState'] = self.click_state
        if self.create_date_end is not None:
            result['CreateDateEnd'] = self.create_date_end
        if self.create_date_start is not None:
            result['CreateDateStart'] = self.create_date_start
        if self.end_id is not None:
            result['EndId'] = self.end_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.short_name is not None:
            result['ShortName'] = self.short_name
        if self.short_url is not None:
            result['ShortUrl'] = self.short_url
        if self.start_id is not None:
            result['StartId'] = self.start_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClickState') is not None:
            self.click_state = m.get('ClickState')
        if m.get('CreateDateEnd') is not None:
            self.create_date_end = m.get('CreateDateEnd')
        if m.get('CreateDateStart') is not None:
            self.create_date_start = m.get('CreateDateStart')
        if m.get('EndId') is not None:
            self.end_id = m.get('EndId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ShortName') is not None:
            self.short_name = m.get('ShortName')
        if m.get('ShortUrl') is not None:
            self.short_url = m.get('ShortUrl')
        if m.get('StartId') is not None:
            self.start_id = m.get('StartId')
        return self


class QueryPageSmartShortUrlLogResponseBodyModelList(TeaModel):
    def __init__(
        self,
        click_state: int = None,
        click_time: int = None,
        create_time: int = None,
        phone_number: str = None,
        short_name: str = None,
        short_url: str = None,
    ):
        self.click_state = click_state
        self.click_time = click_time
        self.create_time = create_time
        self.phone_number = phone_number
        self.short_name = short_name
        self.short_url = short_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.click_state is not None:
            result['ClickState'] = self.click_state
        if self.click_time is not None:
            result['ClickTime'] = self.click_time
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.short_name is not None:
            result['ShortName'] = self.short_name
        if self.short_url is not None:
            result['ShortUrl'] = self.short_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClickState') is not None:
            self.click_state = m.get('ClickState')
        if m.get('ClickTime') is not None:
            self.click_time = m.get('ClickTime')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('ShortName') is not None:
            self.short_name = m.get('ShortName')
        if m.get('ShortUrl') is not None:
            self.short_url = m.get('ShortUrl')
        return self


class QueryPageSmartShortUrlLogResponseBodyModel(TeaModel):
    def __init__(
        self,
        list: List[QueryPageSmartShortUrlLogResponseBodyModelList] = None,
        page_no: int = None,
        page_size: int = None,
        total_count: int = None,
        total_page: int = None,
    ):
        self.list = list
        self.page_no = page_no
        self.page_size = page_size
        self.total_count = total_count
        self.total_page = total_page

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = QueryPageSmartShortUrlLogResponseBodyModelList()
                self.list.append(temp_model.from_map(k))
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        return self


class QueryPageSmartShortUrlLogResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        model: QueryPageSmartShortUrlLogResponseBodyModel = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.model = model
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.model:
            self.model.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.model is not None:
            result['Model'] = self.model.to_map()
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
        if m.get('Model') is not None:
            temp_model = QueryPageSmartShortUrlLogResponseBodyModel()
            self.model = temp_model.from_map(m['Model'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryPageSmartShortUrlLogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryPageSmartShortUrlLogResponseBody = None,
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
            temp_model = QueryPageSmartShortUrlLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QuerySendDetailsRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        current_page: int = None,
        owner_id: int = None,
        page_size: int = None,
        phone_number: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        send_date: str = None,
    ):
        self.biz_id = biz_id
        self.current_page = current_page
        self.owner_id = owner_id
        self.page_size = page_size
        self.phone_number = phone_number
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.send_date = send_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.send_date is not None:
            result['SendDate'] = self.send_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SendDate') is not None:
            self.send_date = m.get('SendDate')
        return self


class QuerySendDetailsResponseBodySmsSendDetailDTOsSmsSendDetailDTO(TeaModel):
    def __init__(
        self,
        content: str = None,
        err_code: str = None,
        out_id: str = None,
        phone_num: str = None,
        receive_date: str = None,
        send_date: str = None,
        send_status: int = None,
        template_code: str = None,
    ):
        self.content = content
        self.err_code = err_code
        self.out_id = out_id
        self.phone_num = phone_num
        self.receive_date = receive_date
        self.send_date = send_date
        self.send_status = send_status
        self.template_code = template_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.out_id is not None:
            result['OutId'] = self.out_id
        if self.phone_num is not None:
            result['PhoneNum'] = self.phone_num
        if self.receive_date is not None:
            result['ReceiveDate'] = self.receive_date
        if self.send_date is not None:
            result['SendDate'] = self.send_date
        if self.send_status is not None:
            result['SendStatus'] = self.send_status
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('OutId') is not None:
            self.out_id = m.get('OutId')
        if m.get('PhoneNum') is not None:
            self.phone_num = m.get('PhoneNum')
        if m.get('ReceiveDate') is not None:
            self.receive_date = m.get('ReceiveDate')
        if m.get('SendDate') is not None:
            self.send_date = m.get('SendDate')
        if m.get('SendStatus') is not None:
            self.send_status = m.get('SendStatus')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        return self


class QuerySendDetailsResponseBodySmsSendDetailDTOs(TeaModel):
    def __init__(
        self,
        sms_send_detail_dto: List[QuerySendDetailsResponseBodySmsSendDetailDTOsSmsSendDetailDTO] = None,
    ):
        self.sms_send_detail_dto = sms_send_detail_dto

    def validate(self):
        if self.sms_send_detail_dto:
            for k in self.sms_send_detail_dto:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SmsSendDetailDTO'] = []
        if self.sms_send_detail_dto is not None:
            for k in self.sms_send_detail_dto:
                result['SmsSendDetailDTO'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.sms_send_detail_dto = []
        if m.get('SmsSendDetailDTO') is not None:
            for k in m.get('SmsSendDetailDTO'):
                temp_model = QuerySendDetailsResponseBodySmsSendDetailDTOsSmsSendDetailDTO()
                self.sms_send_detail_dto.append(temp_model.from_map(k))
        return self


class QuerySendDetailsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        sms_send_detail_dtos: QuerySendDetailsResponseBodySmsSendDetailDTOs = None,
        total_count: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.sms_send_detail_dtos = sms_send_detail_dtos
        self.total_count = total_count

    def validate(self):
        if self.sms_send_detail_dtos:
            self.sms_send_detail_dtos.validate()

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
        if self.sms_send_detail_dtos is not None:
            result['SmsSendDetailDTOs'] = self.sms_send_detail_dtos.to_map()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SmsSendDetailDTOs') is not None:
            temp_model = QuerySendDetailsResponseBodySmsSendDetailDTOs()
            self.sms_send_detail_dtos = temp_model.from_map(m['SmsSendDetailDTOs'])
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class QuerySendDetailsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QuerySendDetailsResponseBody = None,
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
            temp_model = QuerySendDetailsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QuerySendStatisticsRequest(TeaModel):
    def __init__(
        self,
        end_date: str = None,
        is_globe: int = None,
        owner_id: int = None,
        page_index: int = None,
        page_size: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        sign_name: str = None,
        start_date: str = None,
        template_type: int = None,
    ):
        self.end_date = end_date
        self.is_globe = is_globe
        self.owner_id = owner_id
        self.page_index = page_index
        self.page_size = page_size
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.sign_name = sign_name
        self.start_date = start_date
        self.template_type = template_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.is_globe is not None:
            result['IsGlobe'] = self.is_globe
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.sign_name is not None:
            result['SignName'] = self.sign_name
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('IsGlobe') is not None:
            self.is_globe = m.get('IsGlobe')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SignName') is not None:
            self.sign_name = m.get('SignName')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        return self


class QuerySendStatisticsResponseBodyDataTargetList(TeaModel):
    def __init__(
        self,
        no_responded_count: int = None,
        responded_fail_count: int = None,
        responded_success_count: int = None,
        send_date: str = None,
        total_count: int = None,
    ):
        self.no_responded_count = no_responded_count
        self.responded_fail_count = responded_fail_count
        self.responded_success_count = responded_success_count
        self.send_date = send_date
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.no_responded_count is not None:
            result['NoRespondedCount'] = self.no_responded_count
        if self.responded_fail_count is not None:
            result['RespondedFailCount'] = self.responded_fail_count
        if self.responded_success_count is not None:
            result['RespondedSuccessCount'] = self.responded_success_count
        if self.send_date is not None:
            result['SendDate'] = self.send_date
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NoRespondedCount') is not None:
            self.no_responded_count = m.get('NoRespondedCount')
        if m.get('RespondedFailCount') is not None:
            self.responded_fail_count = m.get('RespondedFailCount')
        if m.get('RespondedSuccessCount') is not None:
            self.responded_success_count = m.get('RespondedSuccessCount')
        if m.get('SendDate') is not None:
            self.send_date = m.get('SendDate')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class QuerySendStatisticsResponseBodyData(TeaModel):
    def __init__(
        self,
        target_list: List[QuerySendStatisticsResponseBodyDataTargetList] = None,
        total_size: int = None,
    ):
        self.target_list = target_list
        self.total_size = total_size

    def validate(self):
        if self.target_list:
            for k in self.target_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TargetList'] = []
        if self.target_list is not None:
            for k in self.target_list:
                result['TargetList'].append(k.to_map() if k else None)
        if self.total_size is not None:
            result['TotalSize'] = self.total_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.target_list = []
        if m.get('TargetList') is not None:
            for k in m.get('TargetList'):
                temp_model = QuerySendStatisticsResponseBodyDataTargetList()
                self.target_list.append(temp_model.from_map(k))
        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')
        return self


class QuerySendStatisticsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: QuerySendStatisticsResponseBodyData = None,
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
            temp_model = QuerySendStatisticsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QuerySendStatisticsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QuerySendStatisticsResponseBody = None,
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
            temp_model = QuerySendStatisticsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryShortUrlRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        short_url: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.short_url = short_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.short_url is not None:
            result['ShortUrl'] = self.short_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ShortUrl') is not None:
            self.short_url = m.get('ShortUrl')
        return self


class QueryShortUrlResponseBodyData(TeaModel):
    def __init__(
        self,
        create_date: str = None,
        expire_date: str = None,
        page_view_count: str = None,
        short_url: str = None,
        short_url_name: str = None,
        short_url_status: str = None,
        source_url: str = None,
        unique_visitor_count: str = None,
    ):
        self.create_date = create_date
        self.expire_date = expire_date
        self.page_view_count = page_view_count
        self.short_url = short_url
        self.short_url_name = short_url_name
        self.short_url_status = short_url_status
        self.source_url = source_url
        self.unique_visitor_count = unique_visitor_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.expire_date is not None:
            result['ExpireDate'] = self.expire_date
        if self.page_view_count is not None:
            result['PageViewCount'] = self.page_view_count
        if self.short_url is not None:
            result['ShortUrl'] = self.short_url
        if self.short_url_name is not None:
            result['ShortUrlName'] = self.short_url_name
        if self.short_url_status is not None:
            result['ShortUrlStatus'] = self.short_url_status
        if self.source_url is not None:
            result['SourceUrl'] = self.source_url
        if self.unique_visitor_count is not None:
            result['UniqueVisitorCount'] = self.unique_visitor_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('ExpireDate') is not None:
            self.expire_date = m.get('ExpireDate')
        if m.get('PageViewCount') is not None:
            self.page_view_count = m.get('PageViewCount')
        if m.get('ShortUrl') is not None:
            self.short_url = m.get('ShortUrl')
        if m.get('ShortUrlName') is not None:
            self.short_url_name = m.get('ShortUrlName')
        if m.get('ShortUrlStatus') is not None:
            self.short_url_status = m.get('ShortUrlStatus')
        if m.get('SourceUrl') is not None:
            self.source_url = m.get('SourceUrl')
        if m.get('UniqueVisitorCount') is not None:
            self.unique_visitor_count = m.get('UniqueVisitorCount')
        return self


class QueryShortUrlResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: QueryShortUrlResponseBodyData = None,
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
            temp_model = QueryShortUrlResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryShortUrlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryShortUrlResponseBody = None,
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
            temp_model = QueryShortUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QuerySmsSignRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        sign_name: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.sign_name = sign_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.sign_name is not None:
            result['SignName'] = self.sign_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SignName') is not None:
            self.sign_name = m.get('SignName')
        return self


class QuerySmsSignResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        create_date: str = None,
        message: str = None,
        reason: str = None,
        request_id: str = None,
        sign_name: str = None,
        sign_status: int = None,
    ):
        self.code = code
        self.create_date = create_date
        self.message = message
        self.reason = reason
        self.request_id = request_id
        self.sign_name = sign_name
        self.sign_status = sign_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.message is not None:
            result['Message'] = self.message
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sign_name is not None:
            result['SignName'] = self.sign_name
        if self.sign_status is not None:
            result['SignStatus'] = self.sign_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SignName') is not None:
            self.sign_name = m.get('SignName')
        if m.get('SignStatus') is not None:
            self.sign_status = m.get('SignStatus')
        return self


class QuerySmsSignResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QuerySmsSignResponseBody = None,
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
            temp_model = QuerySmsSignResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QuerySmsSignListRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        page_index: int = None,
        page_size: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.owner_id = owner_id
        self.page_index = page_index
        self.page_size = page_size
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class QuerySmsSignListResponseBodySmsSignListReason(TeaModel):
    def __init__(
        self,
        reject_date: str = None,
        reject_info: str = None,
        reject_sub_info: str = None,
    ):
        self.reject_date = reject_date
        self.reject_info = reject_info
        self.reject_sub_info = reject_sub_info

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.reject_date is not None:
            result['RejectDate'] = self.reject_date
        if self.reject_info is not None:
            result['RejectInfo'] = self.reject_info
        if self.reject_sub_info is not None:
            result['RejectSubInfo'] = self.reject_sub_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RejectDate') is not None:
            self.reject_date = m.get('RejectDate')
        if m.get('RejectInfo') is not None:
            self.reject_info = m.get('RejectInfo')
        if m.get('RejectSubInfo') is not None:
            self.reject_sub_info = m.get('RejectSubInfo')
        return self


class QuerySmsSignListResponseBodySmsSignList(TeaModel):
    def __init__(
        self,
        audit_status: str = None,
        business_type: str = None,
        create_date: str = None,
        order_id: str = None,
        reason: QuerySmsSignListResponseBodySmsSignListReason = None,
        sign_name: str = None,
    ):
        self.audit_status = audit_status
        self.business_type = business_type
        self.create_date = create_date
        self.order_id = order_id
        self.reason = reason
        self.sign_name = sign_name

    def validate(self):
        if self.reason:
            self.reason.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audit_status is not None:
            result['AuditStatus'] = self.audit_status
        if self.business_type is not None:
            result['BusinessType'] = self.business_type
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.reason is not None:
            result['Reason'] = self.reason.to_map()
        if self.sign_name is not None:
            result['SignName'] = self.sign_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuditStatus') is not None:
            self.audit_status = m.get('AuditStatus')
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('Reason') is not None:
            temp_model = QuerySmsSignListResponseBodySmsSignListReason()
            self.reason = temp_model.from_map(m['Reason'])
        if m.get('SignName') is not None:
            self.sign_name = m.get('SignName')
        return self


class QuerySmsSignListResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        current_page: int = None,
        message: str = None,
        page_size: int = None,
        request_id: str = None,
        sms_sign_list: List[QuerySmsSignListResponseBodySmsSignList] = None,
        total_count: int = None,
    ):
        self.code = code
        self.current_page = current_page
        self.message = message
        self.page_size = page_size
        self.request_id = request_id
        self.sms_sign_list = sms_sign_list
        self.total_count = total_count

    def validate(self):
        if self.sms_sign_list:
            for k in self.sms_sign_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.message is not None:
            result['Message'] = self.message
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SmsSignList'] = []
        if self.sms_sign_list is not None:
            for k in self.sms_sign_list:
                result['SmsSignList'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.sms_sign_list = []
        if m.get('SmsSignList') is not None:
            for k in m.get('SmsSignList'):
                temp_model = QuerySmsSignListResponseBodySmsSignList()
                self.sms_sign_list.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class QuerySmsSignListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QuerySmsSignListResponseBody = None,
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
            temp_model = QuerySmsSignListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QuerySmsTemplateRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        template_code: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.template_code = template_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        return self


class QuerySmsTemplateResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        create_date: str = None,
        message: str = None,
        reason: str = None,
        request_id: str = None,
        template_code: str = None,
        template_content: str = None,
        template_name: str = None,
        template_status: int = None,
        template_type: int = None,
    ):
        self.code = code
        self.create_date = create_date
        self.message = message
        self.reason = reason
        self.request_id = request_id
        self.template_code = template_code
        self.template_content = template_content
        self.template_name = template_name
        self.template_status = template_status
        self.template_type = template_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.message is not None:
            result['Message'] = self.message
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.template_content is not None:
            result['TemplateContent'] = self.template_content
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_status is not None:
            result['TemplateStatus'] = self.template_status
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('TemplateContent') is not None:
            self.template_content = m.get('TemplateContent')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateStatus') is not None:
            self.template_status = m.get('TemplateStatus')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        return self


class QuerySmsTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QuerySmsTemplateResponseBody = None,
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
            temp_model = QuerySmsTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QuerySmsTemplateListRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        page_index: int = None,
        page_size: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.owner_id = owner_id
        self.page_index = page_index
        self.page_size = page_size
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class QuerySmsTemplateListResponseBodySmsTemplateListReason(TeaModel):
    def __init__(
        self,
        reject_date: str = None,
        reject_info: str = None,
        reject_sub_info: str = None,
    ):
        self.reject_date = reject_date
        self.reject_info = reject_info
        self.reject_sub_info = reject_sub_info

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.reject_date is not None:
            result['RejectDate'] = self.reject_date
        if self.reject_info is not None:
            result['RejectInfo'] = self.reject_info
        if self.reject_sub_info is not None:
            result['RejectSubInfo'] = self.reject_sub_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RejectDate') is not None:
            self.reject_date = m.get('RejectDate')
        if m.get('RejectInfo') is not None:
            self.reject_info = m.get('RejectInfo')
        if m.get('RejectSubInfo') is not None:
            self.reject_sub_info = m.get('RejectSubInfo')
        return self


class QuerySmsTemplateListResponseBodySmsTemplateList(TeaModel):
    def __init__(
        self,
        audit_status: str = None,
        create_date: str = None,
        order_id: str = None,
        outer_template_type: int = None,
        reason: QuerySmsTemplateListResponseBodySmsTemplateListReason = None,
        template_code: str = None,
        template_content: str = None,
        template_name: str = None,
        template_type: int = None,
    ):
        self.audit_status = audit_status
        self.create_date = create_date
        self.order_id = order_id
        self.outer_template_type = outer_template_type
        self.reason = reason
        self.template_code = template_code
        self.template_content = template_content
        self.template_name = template_name
        self.template_type = template_type

    def validate(self):
        if self.reason:
            self.reason.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audit_status is not None:
            result['AuditStatus'] = self.audit_status
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.outer_template_type is not None:
            result['OuterTemplateType'] = self.outer_template_type
        if self.reason is not None:
            result['Reason'] = self.reason.to_map()
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.template_content is not None:
            result['TemplateContent'] = self.template_content
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuditStatus') is not None:
            self.audit_status = m.get('AuditStatus')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('OuterTemplateType') is not None:
            self.outer_template_type = m.get('OuterTemplateType')
        if m.get('Reason') is not None:
            temp_model = QuerySmsTemplateListResponseBodySmsTemplateListReason()
            self.reason = temp_model.from_map(m['Reason'])
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('TemplateContent') is not None:
            self.template_content = m.get('TemplateContent')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        return self


class QuerySmsTemplateListResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        current_page: int = None,
        message: str = None,
        page_size: int = None,
        request_id: str = None,
        sms_template_list: List[QuerySmsTemplateListResponseBodySmsTemplateList] = None,
        total_count: int = None,
    ):
        self.code = code
        self.current_page = current_page
        self.message = message
        self.page_size = page_size
        self.request_id = request_id
        self.sms_template_list = sms_template_list
        self.total_count = total_count

    def validate(self):
        if self.sms_template_list:
            for k in self.sms_template_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.message is not None:
            result['Message'] = self.message
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SmsTemplateList'] = []
        if self.sms_template_list is not None:
            for k in self.sms_template_list:
                result['SmsTemplateList'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.sms_template_list = []
        if m.get('SmsTemplateList') is not None:
            for k in m.get('SmsTemplateList'):
                temp_model = QuerySmsTemplateListResponseBodySmsTemplateList()
                self.sms_template_list.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class QuerySmsTemplateListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QuerySmsTemplateListResponseBody = None,
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
            temp_model = QuerySmsTemplateListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendBatchCardSmsRequest(TeaModel):
    def __init__(
        self,
        card_template_code: str = None,
        card_template_param_json: str = None,
        digital_template_code: str = None,
        digital_template_param_json: str = None,
        fallback_type: str = None,
        out_id: str = None,
        phone_number_json: str = None,
        sign_name_json: str = None,
        sms_template_code: str = None,
        sms_template_param_json: str = None,
        sms_up_extend_code_json: str = None,
        template_code: str = None,
        template_param_json: str = None,
    ):
        self.card_template_code = card_template_code
        self.card_template_param_json = card_template_param_json
        self.digital_template_code = digital_template_code
        self.digital_template_param_json = digital_template_param_json
        self.fallback_type = fallback_type
        self.out_id = out_id
        self.phone_number_json = phone_number_json
        self.sign_name_json = sign_name_json
        self.sms_template_code = sms_template_code
        self.sms_template_param_json = sms_template_param_json
        self.sms_up_extend_code_json = sms_up_extend_code_json
        self.template_code = template_code
        self.template_param_json = template_param_json

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.card_template_code is not None:
            result['CardTemplateCode'] = self.card_template_code
        if self.card_template_param_json is not None:
            result['CardTemplateParamJson'] = self.card_template_param_json
        if self.digital_template_code is not None:
            result['DigitalTemplateCode'] = self.digital_template_code
        if self.digital_template_param_json is not None:
            result['DigitalTemplateParamJson'] = self.digital_template_param_json
        if self.fallback_type is not None:
            result['FallbackType'] = self.fallback_type
        if self.out_id is not None:
            result['OutId'] = self.out_id
        if self.phone_number_json is not None:
            result['PhoneNumberJson'] = self.phone_number_json
        if self.sign_name_json is not None:
            result['SignNameJson'] = self.sign_name_json
        if self.sms_template_code is not None:
            result['SmsTemplateCode'] = self.sms_template_code
        if self.sms_template_param_json is not None:
            result['SmsTemplateParamJson'] = self.sms_template_param_json
        if self.sms_up_extend_code_json is not None:
            result['SmsUpExtendCodeJson'] = self.sms_up_extend_code_json
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.template_param_json is not None:
            result['TemplateParamJson'] = self.template_param_json
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CardTemplateCode') is not None:
            self.card_template_code = m.get('CardTemplateCode')
        if m.get('CardTemplateParamJson') is not None:
            self.card_template_param_json = m.get('CardTemplateParamJson')
        if m.get('DigitalTemplateCode') is not None:
            self.digital_template_code = m.get('DigitalTemplateCode')
        if m.get('DigitalTemplateParamJson') is not None:
            self.digital_template_param_json = m.get('DigitalTemplateParamJson')
        if m.get('FallbackType') is not None:
            self.fallback_type = m.get('FallbackType')
        if m.get('OutId') is not None:
            self.out_id = m.get('OutId')
        if m.get('PhoneNumberJson') is not None:
            self.phone_number_json = m.get('PhoneNumberJson')
        if m.get('SignNameJson') is not None:
            self.sign_name_json = m.get('SignNameJson')
        if m.get('SmsTemplateCode') is not None:
            self.sms_template_code = m.get('SmsTemplateCode')
        if m.get('SmsTemplateParamJson') is not None:
            self.sms_template_param_json = m.get('SmsTemplateParamJson')
        if m.get('SmsUpExtendCodeJson') is not None:
            self.sms_up_extend_code_json = m.get('SmsUpExtendCodeJson')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('TemplateParamJson') is not None:
            self.template_param_json = m.get('TemplateParamJson')
        return self


class SendBatchCardSmsResponseBodyData(TeaModel):
    def __init__(
        self,
        biz_card_id: str = None,
        biz_digital_id: str = None,
        biz_sms_id: str = None,
        card_tmp_state: int = None,
        media_mobiles: str = None,
        not_media_mobiles: str = None,
    ):
        self.biz_card_id = biz_card_id
        self.biz_digital_id = biz_digital_id
        self.biz_sms_id = biz_sms_id
        self.card_tmp_state = card_tmp_state
        self.media_mobiles = media_mobiles
        self.not_media_mobiles = not_media_mobiles

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_card_id is not None:
            result['BizCardId'] = self.biz_card_id
        if self.biz_digital_id is not None:
            result['BizDigitalId'] = self.biz_digital_id
        if self.biz_sms_id is not None:
            result['BizSmsId'] = self.biz_sms_id
        if self.card_tmp_state is not None:
            result['CardTmpState'] = self.card_tmp_state
        if self.media_mobiles is not None:
            result['MediaMobiles'] = self.media_mobiles
        if self.not_media_mobiles is not None:
            result['NotMediaMobiles'] = self.not_media_mobiles
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizCardId') is not None:
            self.biz_card_id = m.get('BizCardId')
        if m.get('BizDigitalId') is not None:
            self.biz_digital_id = m.get('BizDigitalId')
        if m.get('BizSmsId') is not None:
            self.biz_sms_id = m.get('BizSmsId')
        if m.get('CardTmpState') is not None:
            self.card_tmp_state = m.get('CardTmpState')
        if m.get('MediaMobiles') is not None:
            self.media_mobiles = m.get('MediaMobiles')
        if m.get('NotMediaMobiles') is not None:
            self.not_media_mobiles = m.get('NotMediaMobiles')
        return self


class SendBatchCardSmsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: SendBatchCardSmsResponseBodyData = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
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
            temp_model = SendBatchCardSmsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SendBatchCardSmsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SendBatchCardSmsResponseBody = None,
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
            temp_model = SendBatchCardSmsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendBatchSmsRequest(TeaModel):
    def __init__(
        self,
        out_id: str = None,
        owner_id: int = None,
        phone_number_json: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        sign_name_json: str = None,
        sms_up_extend_code_json: str = None,
        template_code: str = None,
        template_param_json: str = None,
    ):
        self.out_id = out_id
        self.owner_id = owner_id
        self.phone_number_json = phone_number_json
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.sign_name_json = sign_name_json
        self.sms_up_extend_code_json = sms_up_extend_code_json
        self.template_code = template_code
        self.template_param_json = template_param_json

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.out_id is not None:
            result['OutId'] = self.out_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.phone_number_json is not None:
            result['PhoneNumberJson'] = self.phone_number_json
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.sign_name_json is not None:
            result['SignNameJson'] = self.sign_name_json
        if self.sms_up_extend_code_json is not None:
            result['SmsUpExtendCodeJson'] = self.sms_up_extend_code_json
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.template_param_json is not None:
            result['TemplateParamJson'] = self.template_param_json
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OutId') is not None:
            self.out_id = m.get('OutId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PhoneNumberJson') is not None:
            self.phone_number_json = m.get('PhoneNumberJson')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SignNameJson') is not None:
            self.sign_name_json = m.get('SignNameJson')
        if m.get('SmsUpExtendCodeJson') is not None:
            self.sms_up_extend_code_json = m.get('SmsUpExtendCodeJson')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('TemplateParamJson') is not None:
            self.template_param_json = m.get('TemplateParamJson')
        return self


class SendBatchSmsResponseBody(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.biz_id = biz_id
        self.code = code
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SendBatchSmsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SendBatchSmsResponseBody = None,
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
            temp_model = SendBatchSmsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendCardSmsRequestCardObjects(TeaModel):
    def __init__(
        self,
        custom_url: str = None,
        dync_params: str = None,
        mobile: str = None,
    ):
        self.custom_url = custom_url
        self.dync_params = dync_params
        self.mobile = mobile

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_url is not None:
            result['customUrl'] = self.custom_url
        if self.dync_params is not None:
            result['dyncParams'] = self.dync_params
        if self.mobile is not None:
            result['mobile'] = self.mobile
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('customUrl') is not None:
            self.custom_url = m.get('customUrl')
        if m.get('dyncParams') is not None:
            self.dync_params = m.get('dyncParams')
        if m.get('mobile') is not None:
            self.mobile = m.get('mobile')
        return self


class SendCardSmsRequest(TeaModel):
    def __init__(
        self,
        card_objects: List[SendCardSmsRequestCardObjects] = None,
        card_template_code: str = None,
        digital_template_code: str = None,
        digital_template_param: str = None,
        fallback_type: str = None,
        out_id: str = None,
        sign_name: str = None,
        sms_template_code: str = None,
        sms_template_param: str = None,
        sms_up_extend_code: str = None,
        template_code: str = None,
        template_param: str = None,
    ):
        self.card_objects = card_objects
        self.card_template_code = card_template_code
        self.digital_template_code = digital_template_code
        self.digital_template_param = digital_template_param
        self.fallback_type = fallback_type
        self.out_id = out_id
        self.sign_name = sign_name
        self.sms_template_code = sms_template_code
        self.sms_template_param = sms_template_param
        self.sms_up_extend_code = sms_up_extend_code
        self.template_code = template_code
        self.template_param = template_param

    def validate(self):
        if self.card_objects:
            for k in self.card_objects:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CardObjects'] = []
        if self.card_objects is not None:
            for k in self.card_objects:
                result['CardObjects'].append(k.to_map() if k else None)
        if self.card_template_code is not None:
            result['CardTemplateCode'] = self.card_template_code
        if self.digital_template_code is not None:
            result['DigitalTemplateCode'] = self.digital_template_code
        if self.digital_template_param is not None:
            result['DigitalTemplateParam'] = self.digital_template_param
        if self.fallback_type is not None:
            result['FallbackType'] = self.fallback_type
        if self.out_id is not None:
            result['OutId'] = self.out_id
        if self.sign_name is not None:
            result['SignName'] = self.sign_name
        if self.sms_template_code is not None:
            result['SmsTemplateCode'] = self.sms_template_code
        if self.sms_template_param is not None:
            result['SmsTemplateParam'] = self.sms_template_param
        if self.sms_up_extend_code is not None:
            result['SmsUpExtendCode'] = self.sms_up_extend_code
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.template_param is not None:
            result['TemplateParam'] = self.template_param
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.card_objects = []
        if m.get('CardObjects') is not None:
            for k in m.get('CardObjects'):
                temp_model = SendCardSmsRequestCardObjects()
                self.card_objects.append(temp_model.from_map(k))
        if m.get('CardTemplateCode') is not None:
            self.card_template_code = m.get('CardTemplateCode')
        if m.get('DigitalTemplateCode') is not None:
            self.digital_template_code = m.get('DigitalTemplateCode')
        if m.get('DigitalTemplateParam') is not None:
            self.digital_template_param = m.get('DigitalTemplateParam')
        if m.get('FallbackType') is not None:
            self.fallback_type = m.get('FallbackType')
        if m.get('OutId') is not None:
            self.out_id = m.get('OutId')
        if m.get('SignName') is not None:
            self.sign_name = m.get('SignName')
        if m.get('SmsTemplateCode') is not None:
            self.sms_template_code = m.get('SmsTemplateCode')
        if m.get('SmsTemplateParam') is not None:
            self.sms_template_param = m.get('SmsTemplateParam')
        if m.get('SmsUpExtendCode') is not None:
            self.sms_up_extend_code = m.get('SmsUpExtendCode')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('TemplateParam') is not None:
            self.template_param = m.get('TemplateParam')
        return self


class SendCardSmsResponseBodyData(TeaModel):
    def __init__(
        self,
        biz_card_id: str = None,
        biz_digital_id: str = None,
        biz_sms_id: str = None,
        card_tmp_state: int = None,
        media_mobiles: str = None,
        not_media_mobiles: str = None,
    ):
        self.biz_card_id = biz_card_id
        self.biz_digital_id = biz_digital_id
        self.biz_sms_id = biz_sms_id
        self.card_tmp_state = card_tmp_state
        self.media_mobiles = media_mobiles
        self.not_media_mobiles = not_media_mobiles

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_card_id is not None:
            result['BizCardId'] = self.biz_card_id
        if self.biz_digital_id is not None:
            result['BizDigitalId'] = self.biz_digital_id
        if self.biz_sms_id is not None:
            result['BizSmsId'] = self.biz_sms_id
        if self.card_tmp_state is not None:
            result['CardTmpState'] = self.card_tmp_state
        if self.media_mobiles is not None:
            result['MediaMobiles'] = self.media_mobiles
        if self.not_media_mobiles is not None:
            result['NotMediaMobiles'] = self.not_media_mobiles
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizCardId') is not None:
            self.biz_card_id = m.get('BizCardId')
        if m.get('BizDigitalId') is not None:
            self.biz_digital_id = m.get('BizDigitalId')
        if m.get('BizSmsId') is not None:
            self.biz_sms_id = m.get('BizSmsId')
        if m.get('CardTmpState') is not None:
            self.card_tmp_state = m.get('CardTmpState')
        if m.get('MediaMobiles') is not None:
            self.media_mobiles = m.get('MediaMobiles')
        if m.get('NotMediaMobiles') is not None:
            self.not_media_mobiles = m.get('NotMediaMobiles')
        return self


class SendCardSmsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: SendCardSmsResponseBodyData = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
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
            temp_model = SendCardSmsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SendCardSmsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SendCardSmsResponseBody = None,
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
            temp_model = SendCardSmsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendSmsRequest(TeaModel):
    def __init__(
        self,
        out_id: str = None,
        owner_id: int = None,
        phone_numbers: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        sign_name: str = None,
        sms_up_extend_code: str = None,
        template_code: str = None,
        template_param: str = None,
    ):
        self.out_id = out_id
        self.owner_id = owner_id
        self.phone_numbers = phone_numbers
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.sign_name = sign_name
        self.sms_up_extend_code = sms_up_extend_code
        self.template_code = template_code
        self.template_param = template_param

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.out_id is not None:
            result['OutId'] = self.out_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.phone_numbers is not None:
            result['PhoneNumbers'] = self.phone_numbers
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.sign_name is not None:
            result['SignName'] = self.sign_name
        if self.sms_up_extend_code is not None:
            result['SmsUpExtendCode'] = self.sms_up_extend_code
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.template_param is not None:
            result['TemplateParam'] = self.template_param
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OutId') is not None:
            self.out_id = m.get('OutId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PhoneNumbers') is not None:
            self.phone_numbers = m.get('PhoneNumbers')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SignName') is not None:
            self.sign_name = m.get('SignName')
        if m.get('SmsUpExtendCode') is not None:
            self.sms_up_extend_code = m.get('SmsUpExtendCode')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('TemplateParam') is not None:
            self.template_param = m.get('TemplateParam')
        return self


class SendSmsResponseBody(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.biz_id = biz_id
        self.code = code
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SendSmsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SendSmsResponseBody = None,
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
            temp_model = SendSmsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SmsConversionIntlRequest(TeaModel):
    def __init__(
        self,
        conversion_time: int = None,
        delivered: bool = None,
        message_id: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.conversion_time = conversion_time
        self.delivered = delivered
        self.message_id = message_id
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.conversion_time is not None:
            result['ConversionTime'] = self.conversion_time
        if self.delivered is not None:
            result['Delivered'] = self.delivered
        if self.message_id is not None:
            result['MessageId'] = self.message_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConversionTime') is not None:
            self.conversion_time = m.get('ConversionTime')
        if m.get('Delivered') is not None:
            self.delivered = m.get('Delivered')
        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class SmsConversionIntlResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SmsConversionIntlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SmsConversionIntlResponseBody = None,
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
            temp_model = SmsConversionIntlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TagResourcesRequestTag(TeaModel):
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


class TagResourcesRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        prod_code: str = None,
        region_id: str = None,
        resource_id: List[str] = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        resource_type: str = None,
        tag: List[TagResourcesRequestTag] = None,
    ):
        self.owner_id = owner_id
        self.prod_code = prod_code
        self.region_id = region_id
        self.resource_id = resource_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.resource_type = resource_type
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = TagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class TagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.request_id = request_id

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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class TagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: TagResourcesResponseBody = None,
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
            temp_model = TagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UntagResourcesRequest(TeaModel):
    def __init__(
        self,
        all: bool = None,
        owner_id: int = None,
        prod_code: str = None,
        region_id: str = None,
        resource_id: List[str] = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        resource_type: str = None,
        tag_key: List[str] = None,
    ):
        self.all = all
        self.owner_id = owner_id
        self.prod_code = prod_code
        self.region_id = region_id
        self.resource_id = resource_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.resource_type = resource_type
        self.tag_key = tag_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all is not None:
            result['All'] = self.all
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('All') is not None:
            self.all = m.get('All')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class UntagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.request_id = request_id

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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UntagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UntagResourcesResponseBody = None,
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
            temp_model = UntagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


