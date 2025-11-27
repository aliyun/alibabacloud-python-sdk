# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List, Any


class AddExtCodeSignRequest(TeaModel):
    def __init__(
        self,
        ext_code: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        sign_name: str = None,
    ):
        # 扩展码A3
        # 
        # This parameter is required.
        self.ext_code = ext_code
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # 签名
        # 
        # This parameter is required.
        self.sign_name = sign_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ext_code is not None:
            result['ExtCode'] = self.ext_code
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
        if m.get('ExtCode') is not None:
            self.ext_code = m.get('ExtCode')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SignName') is not None:
            self.sign_name = m.get('SignName')
        return self


class AddExtCodeSignResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: bool = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.data = data
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
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddExtCodeSignResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddExtCodeSignResponseBody = None,
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
            temp_model = AddExtCodeSignResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


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
        # The validity period of the short URL. Unit: days. The maximum validity period is 90 days.
        # 
        # This parameter is required.
        self.effective_days = effective_days
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The service name of the short URL. The name cannot exceed 13 characters in length.
        # 
        # This parameter is required.
        self.short_url_name = short_url_name
        # The source URL. The URL cannot exceed 1,000 characters in length.
        # 
        # This parameter is required.
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
        # The time when the short URL expires.
        # 
        # > The value of **ExpireDate** is on the hour.
        self.expire_date = expire_date
        # The short URL.
        self.short_url = short_url
        # The source URL.
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
        # The response code.
        # 
        # *   The value OK indicates that the request was successful.
        # *   Other values indicate that the request failed. For more information, see [Error codes](https://help.aliyun.com/document_detail/101346.html).
        self.code = code
        # The details of the short URL.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # The Base64-encoded string of the qualification document. An image cannot exceed 2 MB in size. In some scenarios, you must upload supporting documents to apply for signatures. For more information, see [SMS signature specifications](https://help.aliyun.com/document_detail/108076.html).
        # 
        # This parameter is required.
        self.file_contents = file_contents
        # The format of the qualification document. You can upload multiple images. Images in JPG, PNG, GIF, or JPEG format are supported.
        # 
        # In some scenarios, you must upload supporting documents to apply for signatures. For more information, see [SMS signature specifications](https://help.aliyun.com/document_detail/108076.html).
        # 
        # > If you apply for a signature for other users or if the signature source is the name of an enterprise or public institution, you must upload a certificate and a letter of authorization. For more information, see [Certificate](https://help.aliyun.com/document_detail/108076.html) and [Letter of authorization](https://help.aliyun.com/document_detail/56741.html).
        # 
        # This parameter is required.
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
        # The description of the signature application. The description cannot exceed 200 characters in length. The description is one of the reference information for signature review. We recommend that you describe the use scenarios of your services in detail, and provide information that can verify the services, such as a website URL, a domain name with an ICP filing, an app download URL, an official account name, or a mini program name. For sign-in scenarios, you must also provide an account and password for tests. A detailed description can improve the review efficiency of signatures and templates.
        # 
        # This parameter is required.
        self.remark = remark
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The signature files.
        # 
        # This parameter is required.
        self.sign_file_list = sign_file_list
        # The name of the signature.
        # 
        # > 
        # 
        # *   The signature name is not case-sensitive. For example, [Alibaba Cloud Communication] and [alibaba cloud communication] are considered as the same name.
        # 
        # *   If your verification code signature and general-purpose signature have the same name, the system uses the general-purpose signature to send messages by default.
        # 
        # This parameter is required.
        self.sign_name = sign_name
        # The source of the signature. Valid values:
        # 
        # *   **0**: the full name or abbreviation of an enterprise or institution
        # *   **1**: the full name or abbreviation of a website that has obtained an ICP filing from the Ministry of Industry and Information Technology (MIIT) of China
        # *   **2**: the full name or abbreviation of an app
        # *   **3**: the full name or abbreviation of an official account or mini-program
        # *   **4**: the full name or abbreviation of an e-commerce store
        # *   **5**: the full name or abbreviation of a trademark
        # 
        # This parameter is required.
        self.sign_source = sign_source
        # The type of the signature. Valid values:
        # 
        # *   **0**: verification code
        # *   **1**: general-purpose
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
        # The response code.
        # 
        # *   The value OK indicates that the request was successful.
        # *   Other values indicate that the request failed. For more information, see [Error codes](https://help.aliyun.com/document_detail/101346.html).
        self.code = code
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The name of the signature.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # The description of the message template. It is one of the reference information for template review. The description cannot exceed 100 characters in length.
        # 
        # This parameter is required.
        self.remark = remark
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The content of the template. The content can be up to 500 characters in length. For more information, see [Message template specifications](https://help.aliyun.com/document_detail/108253.html).
        # 
        # This parameter is required.
        self.template_content = template_content
        # The name of the template. The name can be up to 30 characters in length.
        # 
        # This parameter is required.
        self.template_name = template_name
        # The type of the message. Valid values:
        # 
        # *   **0**: verification code
        # *   **1**: notification
        # *   **2**: promotional message
        # *   **3**: message sent to countries or regions outside the Chinese mainland
        # 
        # > Only enterprise users can send promotional messages, or send messages to countries or regions outside the Chinese mainland.
        # 
        # This parameter is required.
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
        # The response code.
        # 
        # *   The value OK indicates that the request was successful.
        # *   For more information about other response codes, see [API error codes](https://help.aliyun.com/document_detail/101346.html).
        self.code = code
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The code of the message template.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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


class ChangeSignatureQualificationRequest(TeaModel):
    def __init__(
        self,
        authorization_letter_id: int = None,
        owner_id: int = None,
        qualification_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        signature_name: str = None,
    ):
        # 授权委托书id
        self.authorization_letter_id = authorization_letter_id
        self.owner_id = owner_id
        # 资质id
        # 
        # This parameter is required.
        self.qualification_id = qualification_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # 签名
        # 
        # This parameter is required.
        self.signature_name = signature_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorization_letter_id is not None:
            result['AuthorizationLetterId'] = self.authorization_letter_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.qualification_id is not None:
            result['QualificationId'] = self.qualification_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.signature_name is not None:
            result['SignatureName'] = self.signature_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorizationLetterId') is not None:
            self.authorization_letter_id = m.get('AuthorizationLetterId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('QualificationId') is not None:
            self.qualification_id = m.get('QualificationId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SignatureName') is not None:
            self.signature_name = m.get('SignatureName')
        return self


class ChangeSignatureQualificationResponseBodyData(TeaModel):
    def __init__(
        self,
        data: Dict[str, Any] = None,
        err_code: str = None,
        err_message: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_message = err_message
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
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ChangeSignatureQualificationResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: ChangeSignatureQualificationResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.data = data
        self.message = message
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
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
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
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ChangeSignatureQualificationResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ChangeSignatureQualificationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ChangeSignatureQualificationResponseBody = None,
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
            temp_model = ChangeSignatureQualificationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckMobilesCardSupportRequest(TeaModel):
    def __init__(
        self,
        mobiles: List[Dict[str, Any]] = None,
        template_code: str = None,
    ):
        # The list of mobile phone numbers that receive messages.
        # 
        # This parameter is required.
        self.mobiles = mobiles
        # The code of the message template. You can view the template code in the **Template Code** column on the **Templates** tab of the **Go China** page in the Alibaba Cloud SMS console.
        # 
        # > Make sure that the message template has been approved.
        # 
        # This parameter is required.
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
        # The mobile phone number.
        self.mobile = mobile
        # Indicates whether the mobile phone number supports card messages.
        # 
        # *   **true**\
        # *   **false**\
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
        # The list of returned results.
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
        # The HTTP status code.
        # 
        # *   The value OK indicates that the request was successful.
        # *   Other values indicate that the request failed. For more information, see [Error codes](https://help.aliyun.com/document_detail/101346.html).
        self.code = code
        # The data returned.
        self.data = data
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request is successful. Valid values:
        # 
        # *   **true**\
        # *   **false**\
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # The conversion rate.
        # 
        # > The value of this parameter is a double, and ranges from 0 to 1.
        # 
        # This parameter is required.
        self.conversion_rate = conversion_rate
        self.owner_id = owner_id
        # The time point at which the conversion rate is monitored. The value is a UNIX timestamp. Unit: milliseconds.
        # 
        # > If you do not specify this parameter, the current timestamp is used by default.
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
        # The status code. If OK is returned, the request is successful. For more information, see [Error codes](https://help.aliyun.com/document_detail/101346.html?spm=a2c4g.101345.0.0.74326ff2J5EZyt).
        self.code = code
        # The returned message.
        self.message = message
        # The request ID.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # The mobile phone manufacturer. Valid values:
        # 
        # *   **HuaWei**: HUAWEI
        # *   **XiaoMi**: Xiaomi
        # *   **OPPO**: OPPO
        # *   **VIVO**: vivo
        # *   **MEIZU**: MEIZU
        # 
        # > If this parameter is not specified, the system automatically specifies a supported mobile phone manufacturer.
        self.factorys = factorys
        # The description of the message template.
        self.memo = memo
        # The content of the card message template.
        # 
        # > 
        # 
        # *   For information about fields such as Template, ExtendInfo, TemplateContent, TmpCard, and Action, see [Parameters of card message templates](https://help.aliyun.com/document_detail/434929.html).
        # 
        # *   Message template content varies based on the template type. For more information, see [Sample message templates](https://help.aliyun.com/document_detail/435361.html).
        # 
        # This parameter is required.
        self.template = template
        # The name of the card message template.
        # 
        # This parameter is required.
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
        # The mobile phone manufacturer. Valid values:
        # 
        # *   **HuaWei**: HUAWEI
        # *   **XiaoMi**: Xiaomi
        # *   **OPPO**: OPPO
        # *   **VIVO**: vivo
        # *   **MEIZU**: MEIZU
        # 
        # > If this parameter is not specified, the system automatically specifies a supported mobile phone manufacturer.
        self.factorys = factorys
        # The description of the message template.
        self.memo = memo
        # The content of the card message template.
        # 
        # > 
        # 
        # *   For information about fields such as Template, ExtendInfo, TemplateContent, TmpCard, and Action, see [Parameters of card message templates](https://help.aliyun.com/document_detail/434929.html).
        # 
        # *   Message template content varies based on the template type. For more information, see [Sample message templates](https://help.aliyun.com/document_detail/435361.html).
        # 
        # This parameter is required.
        self.template_shrink = template_shrink
        # The name of the card message template.
        # 
        # This parameter is required.
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
        # The code of the message template.
        # 
        # You can view the template code in the **Template Code** column on the **Templates** tab of the **Go China** page in the [Alibaba Cloud SMS console](https://dysms.console.aliyun.com/dysms.htm?spm=5176.12818093.categories-n-products.ddysms.3b2816d0xml2NA#/overview).
        # 
        # > Make sure that the message template has been approved.
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
        # The response code.
        # 
        # *   If OK is returned, the request is successful.
        # *   Other values indicate that the request fails. For more information, see [Error codes](https://help.aliyun.com/document_detail/101346.html).
        self.code = code
        # The data returned.
        self.data = data
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**\
        # *   **false**\
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        out_id: str = None,
        owner_id: int = None,
        phone_numbers: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        source_url: str = None,
    ):
        self.out_id = out_id
        self.owner_id = owner_id
        # This parameter is required.
        self.phone_numbers = phone_numbers
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # This parameter is required.
        self.source_url = source_url

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
        if self.source_url is not None:
            result['SourceUrl'] = self.source_url
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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


class CreateSmsAuthorizationLetterRequest(TeaModel):
    def __init__(
        self,
        authorization: str = None,
        authorization_letter_exp_date: str = None,
        authorization_letter_name: str = None,
        authorization_letter_pic: str = None,
        organization_code: str = None,
        owner_id: int = None,
        proxy_authorization: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        sign_list: List[str] = None,
    ):
        # 授权方，授权方命名长度不超过1000个字符，暂不支持包含除中点（·）、空格、中文括号【】、英文括号()外的任何符号或纯数字输入
        # 
        # This parameter is required.
        self.authorization = authorization
        # 委托授权书有效期
        # 
        # This parameter is required.
        self.authorization_letter_exp_date = authorization_letter_exp_date
        # 委托授权书命名非空，不超过100个字符，支持中文、英文或与数字组合进行命名，暂不支持任何符号或纯数字输入
        # 
        # This parameter is required.
        self.authorization_letter_name = authorization_letter_name
        # 上传oss的委托授权书图片标识
        # 
        # This parameter is required.
        self.authorization_letter_pic = authorization_letter_pic
        # 授权方社会统一信用代码，长度不超过150个字符
        # 
        # This parameter is required.
        self.organization_code = organization_code
        self.owner_id = owner_id
        # 被授权方，被授权方命名长度不超过1000个字符，暂不支持包含除中点（·）、空格、中文括号【】、英文括号()外的任何符号或纯数字输入
        # 
        # This parameter is required.
        self.proxy_authorization = proxy_authorization
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # 委托授权签名列表，签名数量限制100个以内
        # 
        # This parameter is required.
        self.sign_list = sign_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        if self.authorization_letter_exp_date is not None:
            result['AuthorizationLetterExpDate'] = self.authorization_letter_exp_date
        if self.authorization_letter_name is not None:
            result['AuthorizationLetterName'] = self.authorization_letter_name
        if self.authorization_letter_pic is not None:
            result['AuthorizationLetterPic'] = self.authorization_letter_pic
        if self.organization_code is not None:
            result['OrganizationCode'] = self.organization_code
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.proxy_authorization is not None:
            result['ProxyAuthorization'] = self.proxy_authorization
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.sign_list is not None:
            result['SignList'] = self.sign_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        if m.get('AuthorizationLetterExpDate') is not None:
            self.authorization_letter_exp_date = m.get('AuthorizationLetterExpDate')
        if m.get('AuthorizationLetterName') is not None:
            self.authorization_letter_name = m.get('AuthorizationLetterName')
        if m.get('AuthorizationLetterPic') is not None:
            self.authorization_letter_pic = m.get('AuthorizationLetterPic')
        if m.get('OrganizationCode') is not None:
            self.organization_code = m.get('OrganizationCode')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProxyAuthorization') is not None:
            self.proxy_authorization = m.get('ProxyAuthorization')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SignList') is not None:
            self.sign_list = m.get('SignList')
        return self


class CreateSmsAuthorizationLetterShrinkRequest(TeaModel):
    def __init__(
        self,
        authorization: str = None,
        authorization_letter_exp_date: str = None,
        authorization_letter_name: str = None,
        authorization_letter_pic: str = None,
        organization_code: str = None,
        owner_id: int = None,
        proxy_authorization: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        sign_list_shrink: str = None,
    ):
        # 授权方，授权方命名长度不超过1000个字符，暂不支持包含除中点（·）、空格、中文括号【】、英文括号()外的任何符号或纯数字输入
        # 
        # This parameter is required.
        self.authorization = authorization
        # 委托授权书有效期
        # 
        # This parameter is required.
        self.authorization_letter_exp_date = authorization_letter_exp_date
        # 委托授权书命名非空，不超过100个字符，支持中文、英文或与数字组合进行命名，暂不支持任何符号或纯数字输入
        # 
        # This parameter is required.
        self.authorization_letter_name = authorization_letter_name
        # 上传oss的委托授权书图片标识
        # 
        # This parameter is required.
        self.authorization_letter_pic = authorization_letter_pic
        # 授权方社会统一信用代码，长度不超过150个字符
        # 
        # This parameter is required.
        self.organization_code = organization_code
        self.owner_id = owner_id
        # 被授权方，被授权方命名长度不超过1000个字符，暂不支持包含除中点（·）、空格、中文括号【】、英文括号()外的任何符号或纯数字输入
        # 
        # This parameter is required.
        self.proxy_authorization = proxy_authorization
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # 委托授权签名列表，签名数量限制100个以内
        # 
        # This parameter is required.
        self.sign_list_shrink = sign_list_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        if self.authorization_letter_exp_date is not None:
            result['AuthorizationLetterExpDate'] = self.authorization_letter_exp_date
        if self.authorization_letter_name is not None:
            result['AuthorizationLetterName'] = self.authorization_letter_name
        if self.authorization_letter_pic is not None:
            result['AuthorizationLetterPic'] = self.authorization_letter_pic
        if self.organization_code is not None:
            result['OrganizationCode'] = self.organization_code
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.proxy_authorization is not None:
            result['ProxyAuthorization'] = self.proxy_authorization
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.sign_list_shrink is not None:
            result['SignList'] = self.sign_list_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        if m.get('AuthorizationLetterExpDate') is not None:
            self.authorization_letter_exp_date = m.get('AuthorizationLetterExpDate')
        if m.get('AuthorizationLetterName') is not None:
            self.authorization_letter_name = m.get('AuthorizationLetterName')
        if m.get('AuthorizationLetterPic') is not None:
            self.authorization_letter_pic = m.get('AuthorizationLetterPic')
        if m.get('OrganizationCode') is not None:
            self.organization_code = m.get('OrganizationCode')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProxyAuthorization') is not None:
            self.proxy_authorization = m.get('ProxyAuthorization')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SignList') is not None:
            self.sign_list_shrink = m.get('SignList')
        return self


class CreateSmsAuthorizationLetterResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.data = data
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
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateSmsAuthorizationLetterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateSmsAuthorizationLetterResponseBody = None,
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
            temp_model = CreateSmsAuthorizationLetterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSmsSignRequest(TeaModel):
    def __init__(
        self,
        apply_scene_content: str = None,
        authorization_letter_id: int = None,
        more_data: List[str] = None,
        owner_id: int = None,
        qualification_id: int = None,
        remark: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        sign_name: str = None,
        sign_source: int = None,
        sign_type: int = None,
        third_party: bool = None,
    ):
        # Application scenarios, instructions as follows:
        # - For registered websites, enter the domain name with HTTP or HTTPS that has been registered with the MIIT.
        # 
        # - For launched apps, provide a display link from the app store with HTTP or HTTPS, ensuring the app is online.
        # 
        # - For public accounts or mini-programs, input the full name, ensuring they are online.
        # 
        # - For e-commerce platform store names, applicable only to enterprise users, provide a display link with HTTP or HTTPS for the store.
        self.apply_scene_content = apply_scene_content
        self.authorization_letter_id = authorization_letter_id
        # Additional information to supplement uploaded business proof documents or screenshots, which helps reviewers understand your business details.
        # 
        # This parameter is optional; please fill it out based on your actual needs.
        self.more_data = more_data
        self.owner_id = owner_id
        # Approved or under-review qualification ID.
        # 
        # > - Before applying for an SMS signature, please first [Apply for Qualification](https://help.aliyun.com/zh/sms/user-guide/new-qualification?spm=a2c4g.11186623.0.0.718d187bbkpMRK).
        # > - You can view the qualification ID on the [Qualification Management](https://dysms.console.aliyun.com/domestic/text/qualification) page.
        # 
        # This parameter is required.
        self.qualification_id = qualification_id
        # Explanation of the SMS signature scenario, with a maximum length of 200 characters.
        # 
        # > The scenario explanation is one of the reference materials for signature review. Please provide a detailed description of the usage scenarios for your live services, along with links to verify these services such as website URLs with MIIT备案, app store display links, full names of public accounts or mini-programs, etc. For login scenarios, test account credentials are also required. A comprehensive application explanation enhances the efficiency of signature and template reviews. Refer to the **Application Scenario** column in the [Signature Source](https://help.aliyun.com/zh/sms/user-guide/signature-specifications-1?spm=a2c4g.11186623.0.i2#section-xup-k46-yi4) table for filling in SMS scenarios.
        self.remark = remark
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Signature name. Please adhere to the [Signature Specifications](https://help.aliyun.com/zh/sms/user-guide/signature-specifications-1?spm=a2c4g.11186623.0.0.4f9710fder2gR7#section-0p8-qn8-mmy).
        # 
        # > - Signature names are case-insensitive; e.g., 【Aliyun Communication】 and 【aliyun communication】 are considered identical.
        # > - If your verification code signature and general signature names are the same, the system defaults to using the general signature for sending SMS messages.
        # 
        # This parameter is required.
        self.sign_name = sign_name
        # Signature source. Values:
        # 
        # - **0**: Full name or abbreviation of an enterprise or institution.
        # - **1**: Full name or abbreviation of a MIIT-registered website.
        # - **2**: Full name or abbreviation of an App.
        # - **3**: Full name or abbreviation of an official account or mini-program.
        # - **4**: Full name or abbreviation of an e-commerce platform store.
        # - **5**: Full name or abbreviation of a trademark.
        # 
        # For detailed information on signature sources, refer to [Signature Source](https://help.aliyun.com/zh/sms/user-guide/signature-specifications-1?spm=a2c4g.11186623.0.0.4f9710fder2gR7#section-xup-k46-yi4).
        # 
        # > This interface does not support applying for signatures with sources as **Test or Learning** and **Trial Use**. If you need to apply for signatures with these sources, please go to the [SMS Service Console](https://dysms.console.aliyun.com/domestic/text/sign/add/qualification).
        # 
        # This parameter is required.
        self.sign_source = sign_source
        # Signature type. Values:
        # 
        # - **0**: Verification Code
        # 
        # - **1**: General (Default)
        # 
        # > It is recommended to use the default value: **General**.
        self.sign_type = sign_type
        # Choose whether the applied signature is for self-use or third-party use.
        # 
        # - false: Self-use (default)
        # 
        # - true: Third-party use
        # >Notice: Please select self-use qualification ID when the signature is for self-use; choose third-party use qualification ID when it\\"s for third-party use.
        self.third_party = third_party

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apply_scene_content is not None:
            result['ApplySceneContent'] = self.apply_scene_content
        if self.authorization_letter_id is not None:
            result['AuthorizationLetterId'] = self.authorization_letter_id
        if self.more_data is not None:
            result['MoreData'] = self.more_data
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.qualification_id is not None:
            result['QualificationId'] = self.qualification_id
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.sign_name is not None:
            result['SignName'] = self.sign_name
        if self.sign_source is not None:
            result['SignSource'] = self.sign_source
        if self.sign_type is not None:
            result['SignType'] = self.sign_type
        if self.third_party is not None:
            result['ThirdParty'] = self.third_party
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplySceneContent') is not None:
            self.apply_scene_content = m.get('ApplySceneContent')
        if m.get('AuthorizationLetterId') is not None:
            self.authorization_letter_id = m.get('AuthorizationLetterId')
        if m.get('MoreData') is not None:
            self.more_data = m.get('MoreData')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('QualificationId') is not None:
            self.qualification_id = m.get('QualificationId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SignName') is not None:
            self.sign_name = m.get('SignName')
        if m.get('SignSource') is not None:
            self.sign_source = m.get('SignSource')
        if m.get('SignType') is not None:
            self.sign_type = m.get('SignType')
        if m.get('ThirdParty') is not None:
            self.third_party = m.get('ThirdParty')
        return self


class CreateSmsSignShrinkRequest(TeaModel):
    def __init__(
        self,
        apply_scene_content: str = None,
        authorization_letter_id: int = None,
        more_data_shrink: str = None,
        owner_id: int = None,
        qualification_id: int = None,
        remark: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        sign_name: str = None,
        sign_source: int = None,
        sign_type: int = None,
        third_party: bool = None,
    ):
        # Application scenarios, instructions as follows:
        # - For registered websites, enter the domain name with HTTP or HTTPS that has been registered with the MIIT.
        # 
        # - For launched apps, provide a display link from the app store with HTTP or HTTPS, ensuring the app is online.
        # 
        # - For public accounts or mini-programs, input the full name, ensuring they are online.
        # 
        # - For e-commerce platform store names, applicable only to enterprise users, provide a display link with HTTP or HTTPS for the store.
        self.apply_scene_content = apply_scene_content
        self.authorization_letter_id = authorization_letter_id
        # Additional information to supplement uploaded business proof documents or screenshots, which helps reviewers understand your business details.
        # 
        # This parameter is optional; please fill it out based on your actual needs.
        self.more_data_shrink = more_data_shrink
        self.owner_id = owner_id
        # Approved or under-review qualification ID.
        # 
        # > - Before applying for an SMS signature, please first [Apply for Qualification](https://help.aliyun.com/zh/sms/user-guide/new-qualification?spm=a2c4g.11186623.0.0.718d187bbkpMRK).
        # > - You can view the qualification ID on the [Qualification Management](https://dysms.console.aliyun.com/domestic/text/qualification) page.
        # 
        # This parameter is required.
        self.qualification_id = qualification_id
        # Explanation of the SMS signature scenario, with a maximum length of 200 characters.
        # 
        # > The scenario explanation is one of the reference materials for signature review. Please provide a detailed description of the usage scenarios for your live services, along with links to verify these services such as website URLs with MIIT备案, app store display links, full names of public accounts or mini-programs, etc. For login scenarios, test account credentials are also required. A comprehensive application explanation enhances the efficiency of signature and template reviews. Refer to the **Application Scenario** column in the [Signature Source](https://help.aliyun.com/zh/sms/user-guide/signature-specifications-1?spm=a2c4g.11186623.0.i2#section-xup-k46-yi4) table for filling in SMS scenarios.
        self.remark = remark
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Signature name. Please adhere to the [Signature Specifications](https://help.aliyun.com/zh/sms/user-guide/signature-specifications-1?spm=a2c4g.11186623.0.0.4f9710fder2gR7#section-0p8-qn8-mmy).
        # 
        # > - Signature names are case-insensitive; e.g., 【Aliyun Communication】 and 【aliyun communication】 are considered identical.
        # > - If your verification code signature and general signature names are the same, the system defaults to using the general signature for sending SMS messages.
        # 
        # This parameter is required.
        self.sign_name = sign_name
        # Signature source. Values:
        # 
        # - **0**: Full name or abbreviation of an enterprise or institution.
        # - **1**: Full name or abbreviation of a MIIT-registered website.
        # - **2**: Full name or abbreviation of an App.
        # - **3**: Full name or abbreviation of an official account or mini-program.
        # - **4**: Full name or abbreviation of an e-commerce platform store.
        # - **5**: Full name or abbreviation of a trademark.
        # 
        # For detailed information on signature sources, refer to [Signature Source](https://help.aliyun.com/zh/sms/user-guide/signature-specifications-1?spm=a2c4g.11186623.0.0.4f9710fder2gR7#section-xup-k46-yi4).
        # 
        # > This interface does not support applying for signatures with sources as **Test or Learning** and **Trial Use**. If you need to apply for signatures with these sources, please go to the [SMS Service Console](https://dysms.console.aliyun.com/domestic/text/sign/add/qualification).
        # 
        # This parameter is required.
        self.sign_source = sign_source
        # Signature type. Values:
        # 
        # - **0**: Verification Code
        # 
        # - **1**: General (Default)
        # 
        # > It is recommended to use the default value: **General**.
        self.sign_type = sign_type
        # Choose whether the applied signature is for self-use or third-party use.
        # 
        # - false: Self-use (default)
        # 
        # - true: Third-party use
        # >Notice: Please select self-use qualification ID when the signature is for self-use; choose third-party use qualification ID when it\\"s for third-party use.
        self.third_party = third_party

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apply_scene_content is not None:
            result['ApplySceneContent'] = self.apply_scene_content
        if self.authorization_letter_id is not None:
            result['AuthorizationLetterId'] = self.authorization_letter_id
        if self.more_data_shrink is not None:
            result['MoreData'] = self.more_data_shrink
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.qualification_id is not None:
            result['QualificationId'] = self.qualification_id
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.sign_name is not None:
            result['SignName'] = self.sign_name
        if self.sign_source is not None:
            result['SignSource'] = self.sign_source
        if self.sign_type is not None:
            result['SignType'] = self.sign_type
        if self.third_party is not None:
            result['ThirdParty'] = self.third_party
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplySceneContent') is not None:
            self.apply_scene_content = m.get('ApplySceneContent')
        if m.get('AuthorizationLetterId') is not None:
            self.authorization_letter_id = m.get('AuthorizationLetterId')
        if m.get('MoreData') is not None:
            self.more_data_shrink = m.get('MoreData')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('QualificationId') is not None:
            self.qualification_id = m.get('QualificationId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SignName') is not None:
            self.sign_name = m.get('SignName')
        if m.get('SignSource') is not None:
            self.sign_source = m.get('SignSource')
        if m.get('SignType') is not None:
            self.sign_type = m.get('SignType')
        if m.get('ThirdParty') is not None:
            self.third_party = m.get('ThirdParty')
        return self


class CreateSmsSignResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        order_id: str = None,
        request_id: str = None,
        sign_name: str = None,
    ):
        # Request status code.
        # 
        # - OK indicates a successful request.
        # - For other error codes, refer to the [Error Code List](https://help.aliyun.com/document_detail/101346.html).
        self.code = code
        # Description of the status code.
        self.message = message
        # Work order number.
        # 
        # This parameter is used by auditors when querying the audit. You will need to provide this work order number if you require expedited review.
        self.order_id = order_id
        # The ID of this call request, which is a unique identifier generated by Alibaba Cloud for the request and can be used for troubleshooting and issue localization.
        self.request_id = request_id
        # Signature name.
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
        if self.order_id is not None:
            result['OrderId'] = self.order_id
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
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SignName') is not None:
            self.sign_name = m.get('SignName')
        return self


class CreateSmsSignResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateSmsSignResponseBody = None,
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
            temp_model = CreateSmsSignResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSmsTemplateRequest(TeaModel):
    def __init__(
        self,
        apply_scene_content: str = None,
        intl_type: int = None,
        more_data: List[str] = None,
        owner_id: int = None,
        related_sign_name: str = None,
        remark: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        template_content: str = None,
        template_name: str = None,
        template_rule: str = None,
        template_type: int = None,
        traffic_driving: str = None,
    ):
        # If there is an applicable scenario, you can fill it in.
        self.apply_scene_content = apply_scene_content
        # International/Hong Kong, Macao, and Taiwan template type. When the **TemplateType** parameter is **3**, this parameter is required for international/Hong Kong, Macao, and Taiwan templates, with values:
        # - **0**: Verification code.
        # - **1**: SMS notification.
        # - **2**: Promotional message.
        self.intl_type = intl_type
        # Additional materials you can upload, such as business proof documents or screenshots, to help reviewers understand your business details.
        # 
        # This parameter is optional; please fill it in according to actual needs.
        self.more_data = more_data
        self.owner_id = owner_id
        # The signature name that the template needs to be associated with. The associated SMS signature must have passed the review.
        # 
        # This parameter is mandatory when the TemplateType parameter is **0**, **1**, or **2**.
        # 
        # <notice>Associating a signature can expedite the review process. Note that this associated signature is unrelated to the signature selected when sending SMS messages.</notice>
        self.related_sign_name = related_sign_name
        # Please describe the business scenario where you use SMS or provide an online link to the scenario, along with a complete example of the SMS (with variable contents filled), as complete information helps increase the template approval rate. Failure to follow guidelines or leaving this field blank may affect the approval of your template.
        self.remark = remark
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Template content, up to 500 characters in length.
        # 
        # Both the template content and variable content must comply with SMS specifications; otherwise, the template will fail the review. You can also view common template examples on the template application page. Using sample templates can enhance review efficiency and success rates. For variable specifications, see [TemplateContent Variable Parameter Filling Specifications](https://help.aliyun.com/zh/sms/templaterule-template-variable-parameter-filling-example).
        # 
        # This parameter is required.
        self.template_content = template_content
        # Template name, up to 30 characters in length.
        # 
        # This parameter is required.
        self.template_name = template_name
        # Template variable rules.
        # 
        # For filling in variable rules, refer to the [Sample Documentation](https://help.aliyun.com/zh/sms/templaterule-template-variable-parameter-filling-example).
        self.template_rule = template_rule
        # SMS type. Values:
        # 
        # - **0**: Verification code.
        # - **1**: SMS notification.
        # - **2**: Promotional message.
        # - **3**: International/Hong Kong, Macao, and Taiwan messages.
        # 
        # > Only enterprise-verified users can apply for promotional messages and international/Hong Kong, Macao, and Taiwan messages. For details on the differences between personal and enterprise user rights, please refer to [Usage Instructions](https://help.aliyun.com/zh/sms/user-guide/usage-notes?spm=a2c4g.11186623.0.0.67447f576NJnE8).
        # 
        # This parameter is required.
        self.template_type = template_type
        self.traffic_driving = traffic_driving

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apply_scene_content is not None:
            result['ApplySceneContent'] = self.apply_scene_content
        if self.intl_type is not None:
            result['IntlType'] = self.intl_type
        if self.more_data is not None:
            result['MoreData'] = self.more_data
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.related_sign_name is not None:
            result['RelatedSignName'] = self.related_sign_name
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
        if self.template_rule is not None:
            result['TemplateRule'] = self.template_rule
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        if self.traffic_driving is not None:
            result['TrafficDriving'] = self.traffic_driving
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplySceneContent') is not None:
            self.apply_scene_content = m.get('ApplySceneContent')
        if m.get('IntlType') is not None:
            self.intl_type = m.get('IntlType')
        if m.get('MoreData') is not None:
            self.more_data = m.get('MoreData')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RelatedSignName') is not None:
            self.related_sign_name = m.get('RelatedSignName')
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
        if m.get('TemplateRule') is not None:
            self.template_rule = m.get('TemplateRule')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        if m.get('TrafficDriving') is not None:
            self.traffic_driving = m.get('TrafficDriving')
        return self


class CreateSmsTemplateShrinkRequest(TeaModel):
    def __init__(
        self,
        apply_scene_content: str = None,
        intl_type: int = None,
        more_data_shrink: str = None,
        owner_id: int = None,
        related_sign_name: str = None,
        remark: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        template_content: str = None,
        template_name: str = None,
        template_rule: str = None,
        template_type: int = None,
        traffic_driving: str = None,
    ):
        # If there is an applicable scenario, you can fill it in.
        self.apply_scene_content = apply_scene_content
        # International/Hong Kong, Macao, and Taiwan template type. When the **TemplateType** parameter is **3**, this parameter is required for international/Hong Kong, Macao, and Taiwan templates, with values:
        # - **0**: Verification code.
        # - **1**: SMS notification.
        # - **2**: Promotional message.
        self.intl_type = intl_type
        # Additional materials you can upload, such as business proof documents or screenshots, to help reviewers understand your business details.
        # 
        # This parameter is optional; please fill it in according to actual needs.
        self.more_data_shrink = more_data_shrink
        self.owner_id = owner_id
        # The signature name that the template needs to be associated with. The associated SMS signature must have passed the review.
        # 
        # This parameter is mandatory when the TemplateType parameter is **0**, **1**, or **2**.
        # 
        # <notice>Associating a signature can expedite the review process. Note that this associated signature is unrelated to the signature selected when sending SMS messages.</notice>
        self.related_sign_name = related_sign_name
        # Please describe the business scenario where you use SMS or provide an online link to the scenario, along with a complete example of the SMS (with variable contents filled), as complete information helps increase the template approval rate. Failure to follow guidelines or leaving this field blank may affect the approval of your template.
        self.remark = remark
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Template content, up to 500 characters in length.
        # 
        # Both the template content and variable content must comply with SMS specifications; otherwise, the template will fail the review. You can also view common template examples on the template application page. Using sample templates can enhance review efficiency and success rates. For variable specifications, see [TemplateContent Variable Parameter Filling Specifications](https://help.aliyun.com/zh/sms/templaterule-template-variable-parameter-filling-example).
        # 
        # This parameter is required.
        self.template_content = template_content
        # Template name, up to 30 characters in length.
        # 
        # This parameter is required.
        self.template_name = template_name
        # Template variable rules.
        # 
        # For filling in variable rules, refer to the [Sample Documentation](https://help.aliyun.com/zh/sms/templaterule-template-variable-parameter-filling-example).
        self.template_rule = template_rule
        # SMS type. Values:
        # 
        # - **0**: Verification code.
        # - **1**: SMS notification.
        # - **2**: Promotional message.
        # - **3**: International/Hong Kong, Macao, and Taiwan messages.
        # 
        # > Only enterprise-verified users can apply for promotional messages and international/Hong Kong, Macao, and Taiwan messages. For details on the differences between personal and enterprise user rights, please refer to [Usage Instructions](https://help.aliyun.com/zh/sms/user-guide/usage-notes?spm=a2c4g.11186623.0.0.67447f576NJnE8).
        # 
        # This parameter is required.
        self.template_type = template_type
        self.traffic_driving = traffic_driving

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apply_scene_content is not None:
            result['ApplySceneContent'] = self.apply_scene_content
        if self.intl_type is not None:
            result['IntlType'] = self.intl_type
        if self.more_data_shrink is not None:
            result['MoreData'] = self.more_data_shrink
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.related_sign_name is not None:
            result['RelatedSignName'] = self.related_sign_name
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
        if self.template_rule is not None:
            result['TemplateRule'] = self.template_rule
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        if self.traffic_driving is not None:
            result['TrafficDriving'] = self.traffic_driving
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplySceneContent') is not None:
            self.apply_scene_content = m.get('ApplySceneContent')
        if m.get('IntlType') is not None:
            self.intl_type = m.get('IntlType')
        if m.get('MoreData') is not None:
            self.more_data_shrink = m.get('MoreData')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RelatedSignName') is not None:
            self.related_sign_name = m.get('RelatedSignName')
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
        if m.get('TemplateRule') is not None:
            self.template_rule = m.get('TemplateRule')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        if m.get('TrafficDriving') is not None:
            self.traffic_driving = m.get('TrafficDriving')
        return self


class CreateSmsTemplateResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        order_id: str = None,
        request_id: str = None,
        template_code: str = None,
        template_name: str = None,
    ):
        # Request status code.
        # 
        # * OK indicates a successful request.
        # * For other error codes, refer to the **Error Codes** section of this chapter or the product\\"s [API Error Codes](https://help.aliyun.com/document_detail/101346.html).
        self.code = code
        # Description of the status code.
        self.message = message
        # Work order ID.
        # 
        # This parameter is used by auditors when querying audits. If you need expedited review, you must provide this work order number.
        self.order_id = order_id
        # The ID generated by Alibaba Cloud for this request, which is a unique identifier that can be used for troubleshooting and issue定位.
        self.request_id = request_id
        # SMS template code.
        # 
        # After submitting the template application, you can use the SMS template code to query the template audit details via the [GetSmsTemplate](https://help.aliyun.com/zh/sms/developer-reference/api-dysmsapi-2017-05-25-getsmstemplate?) API. You can also [configure delivery receipts](https://help.aliyun.com/zh/sms/developer-reference/configure-delivery-receipts-1?spm), and obtain the template audit status messages through TemplateSmsReport.
        self.template_code = template_code
        # SMS template name.
        self.template_name = template_name

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
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        return self


class CreateSmsTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateSmsTemplateResponseBody = None,
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
            temp_model = CreateSmsTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteExtCodeSignRequest(TeaModel):
    def __init__(
        self,
        ext_code: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        sign_name: str = None,
    ):
        # 扩展码A3
        # 
        # This parameter is required.
        self.ext_code = ext_code
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # 签名
        # 
        # This parameter is required.
        self.sign_name = sign_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ext_code is not None:
            result['ExtCode'] = self.ext_code
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
        if m.get('ExtCode') is not None:
            self.ext_code = m.get('ExtCode')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SignName') is not None:
            self.sign_name = m.get('SignName')
        return self


class DeleteExtCodeSignResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: bool = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.data = data
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
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteExtCodeSignResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteExtCodeSignResponseBody = None,
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
            temp_model = DeleteExtCodeSignResponseBody()
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
        # The source address. The address can be up to 1,000 characters in length.
        # 
        # This parameter is required.
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
        # The response code.
        # 
        # *   If OK is returned, the request is successful.
        # *   Other values indicate that the request fails. For more information, see [Error codes](https://help.aliyun.com/document_detail/101346.html).
        self.code = code
        # The returned message.
        self.message = message
        # The request ID.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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


class DeleteSmsQualificationRequest(TeaModel):
    def __init__(
        self,
        order_id: int = None,
        owner_id: int = None,
        qualification_group_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # 工单ID
        # 
        # This parameter is required.
        self.order_id = order_id
        self.owner_id = owner_id
        # 资质组ID
        # 
        # This parameter is required.
        self.qualification_group_id = qualification_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.qualification_group_id is not None:
            result['QualificationGroupId'] = self.qualification_group_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('QualificationGroupId') is not None:
            self.qualification_group_id = m.get('QualificationGroupId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DeleteSmsQualificationResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: bool = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.data = data
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
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteSmsQualificationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteSmsQualificationResponseBody = None,
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
            temp_model = DeleteSmsQualificationResponseBody()
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
        # The signature.
        # 
        # > The signature must be submitted by the current Alibaba Cloud account, and has been approved.
        # 
        # This parameter is required.
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
        # The response code.
        # 
        # *   If OK is returned, the request is successful.
        # *   Other values indicate that the request fails. For more information, see [Error codes](https://help.aliyun.com/document_detail/101346.html).
        self.code = code
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The signature.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # The code of the message template.
        # 
        # You can log on to the [Alibaba Cloud SMS console](https://dysms.console.aliyun.com/dysms.htm) and obtain the message template code on the **Message Templates** tab. You can also obtain the message template code by calling the [AddSmsTemplate](https://help.aliyun.com/document_detail/121208.html) operation.
        # 
        # This parameter is required.
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
        # The response code.
        # 
        # *   The value OK indicates that the request was successful.
        # *   For more information about other response codes, see [API error codes](https://help.aliyun.com/document_detail/101346.html).
        self.code = code
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The code of the message template.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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


class GetCardSmsDetailsRequest(TeaModel):
    def __init__(
        self,
        biz_card_id: str = None,
        biz_digit_id: str = None,
        biz_sms_id: str = None,
        current_page: int = None,
        owner_id: int = None,
        page_size: int = None,
        phone_number: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        send_date: str = None,
    ):
        # Card SMS sending ID, which is the BizCardId field in the response when calling SendCardSms or SendBatchCardSms.
        self.biz_card_id = biz_card_id
        # Digital SMS sending ID, which is the BizDigitalId field in the response when calling SendCardSms or SendBatchCardSms.
        self.biz_digit_id = biz_digit_id
        # Text SMS sending ID, which is the BizSmsId field in the response when calling SendCardSms or SendBatchCardSms.
        self.biz_sms_id = biz_sms_id
        # For paginated viewing of sending records, specify the current page number of the sending records.
        self.current_page = current_page
        self.owner_id = owner_id
        # For paginated viewing of sending records, specify the number of card SMS records to display per page.
        # 
        # The value range is 1~50.
        self.page_size = page_size
        # Domestic phone number that received the SMS. Format: 11-digit phone number, for example, 1390000****.
        # 
        # This parameter is required.
        self.phone_number = phone_number
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Card SMS sending date, supports querying records from the last 30 days.
        # 
        # Format: yyyyMMdd, for example, 20240112.
        # 
        # This parameter is required.
        self.send_date = send_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_card_id is not None:
            result['BizCardId'] = self.biz_card_id
        if self.biz_digit_id is not None:
            result['BizDigitId'] = self.biz_digit_id
        if self.biz_sms_id is not None:
            result['BizSmsId'] = self.biz_sms_id
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
        if m.get('BizCardId') is not None:
            self.biz_card_id = m.get('BizCardId')
        if m.get('BizDigitId') is not None:
            self.biz_digit_id = m.get('BizDigitId')
        if m.get('BizSmsId') is not None:
            self.biz_sms_id = m.get('BizSmsId')
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


class GetCardSmsDetailsResponseBodyCardSendDetailDTORecords(TeaModel):
    def __init__(
        self,
        err_code: str = None,
        out_id: str = None,
        phone_number: str = None,
        receive_date: str = None,
        receive_type: str = None,
        render_date: str = None,
        render_status: int = None,
        send_date: str = None,
        send_status: int = None,
        sms_content: str = None,
        template_code: str = None,
    ):
        # Error code for sending
        self.err_code = err_code
        # Customer-transmitted outId
        self.out_id = out_id
        # Phone number that received the SMS
        self.phone_number = phone_number
        # Receive date
        self.receive_date = receive_date
        # Receive SMS type
        self.receive_type = receive_type
        # Render date
        self.render_date = render_date
        # Render status. 0: Not rendered; 1: Rendered successfully; 3: Not rendered
        self.render_status = render_status
        # Time when the SMS was sent
        self.send_date = send_date
        # Sending status. 1: Sending; 2: Send failed; 3: Sent successfully; 4: Addressing failed
        self.send_status = send_status
        # SMS content. Only applicable for text messages.
        self.sms_content = sms_content
        # Template code
        self.template_code = template_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.out_id is not None:
            result['OutId'] = self.out_id
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.receive_date is not None:
            result['ReceiveDate'] = self.receive_date
        if self.receive_type is not None:
            result['ReceiveType'] = self.receive_type
        if self.render_date is not None:
            result['RenderDate'] = self.render_date
        if self.render_status is not None:
            result['RenderStatus'] = self.render_status
        if self.send_date is not None:
            result['SendDate'] = self.send_date
        if self.send_status is not None:
            result['SendStatus'] = self.send_status
        if self.sms_content is not None:
            result['SmsContent'] = self.sms_content
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('OutId') is not None:
            self.out_id = m.get('OutId')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('ReceiveDate') is not None:
            self.receive_date = m.get('ReceiveDate')
        if m.get('ReceiveType') is not None:
            self.receive_type = m.get('ReceiveType')
        if m.get('RenderDate') is not None:
            self.render_date = m.get('RenderDate')
        if m.get('RenderStatus') is not None:
            self.render_status = m.get('RenderStatus')
        if m.get('SendDate') is not None:
            self.send_date = m.get('SendDate')
        if m.get('SendStatus') is not None:
            self.send_status = m.get('SendStatus')
        if m.get('SmsContent') is not None:
            self.sms_content = m.get('SmsContent')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        return self


class GetCardSmsDetailsResponseBodyCardSendDetailDTO(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        records: List[GetCardSmsDetailsResponseBodyCardSendDetailDTORecords] = None,
        total_count: int = None,
    ):
        # Current page number
        self.current_page = current_page
        # Page size
        self.page_size = page_size
        # List of card SMS sending records
        self.records = records
        # Total count
        self.total_count = total_count

    def validate(self):
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['Records'] = []
        if self.records is not None:
            for k in self.records:
                result['Records'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.records = []
        if m.get('Records') is not None:
            for k in m.get('Records'):
                temp_model = GetCardSmsDetailsResponseBodyCardSendDetailDTORecords()
                self.records.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class GetCardSmsDetailsResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        card_send_detail_dto: GetCardSmsDetailsResponseBodyCardSendDetailDTO = None,
        code: str = None,
        message: str = None,
        success: bool = None,
    ):
        # Access denied detail; this field is returned only if the RAM check fails.
        self.access_denied_detail = access_denied_detail
        # Card SMS sending result
        self.card_send_detail_dto = card_send_detail_dto
        # Request status code.
        # * OK indicates a successful request.
        # * For other error codes, see [API Error Codes](https://help.aliyun.com/document_detail/101346.html).
        self.code = code
        # Description of the status code.
        self.message = message
        # Indicates whether the API call was successful. Values:
        # - **true** - **false**\
        self.success = success

    def validate(self):
        if self.card_send_detail_dto:
            self.card_send_detail_dto.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.card_send_detail_dto is not None:
            result['CardSendDetailDTO'] = self.card_send_detail_dto.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('CardSendDetailDTO') is not None:
            temp_model = GetCardSmsDetailsResponseBodyCardSendDetailDTO()
            self.card_send_detail_dto = temp_model.from_map(m['CardSendDetailDTO'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetCardSmsDetailsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetCardSmsDetailsResponseBody = None,
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
            temp_model = GetCardSmsDetailsResponseBody()
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
        # The code type of the URLs.
        # 
        # *   **1**: group texting
        # *   **2**: personalization
        self.card_code_type = card_code_type
        # The type of the short URLs.
        # 
        # *   1: standard short code.
        # *   2: custom short code.
        # 
        # > If the **CardLinkType** is not specified, standard short codes are generated. If you need to generate custom short codes, contact Alibaba Cloud SMS technical support.
        self.card_link_type = card_link_type
        # The code of the message template. You can view the template code in the **Template Code** column on the **Templates** tab of the **Go China** page in the Alibaba Cloud SMS console.
        # 
        # > Make sure that the message template has been approved.
        # 
        # This parameter is required.
        self.card_template_code = card_template_code
        # The variables of the message template.
        self.card_template_param_json = card_template_param_json
        # The custom short code. It can contain 4 to 8 digits or letters.
        # 
        # > If the CardLinkType parameter is set to 2, the CustomShortCodeJson parameter is required.
        self.custom_short_code_json = custom_short_code_json
        # The original domain name. You must submit domain names for approval in advance.
        # 
        # > 
        # 
        # *   If the **CardLinkType** parameter is set to **2**, the **Domain** parameter is required.
        # 
        # *   The **Domain** parameter cannot exceed 100 characters in length. If the parameter is not specified, a default domain name is used.
        self.domain = domain
        # The extension field.
        self.out_id = out_id
        # The mobile phone numbers of recipients, custom identifiers, or system identifiers.
        # 
        # > 
        # 
        # *   A maximum of 10,000 mobile phone numbers are supported.
        # 
        # *   You can enter custom identifier. Each identifier can be a maximum of 60 characters in length.
        # 
        # *   You can apply for a maximum of 10 OPPO templates at a time.
        self.phone_number_json = phone_number_json
        # The signature. You can view the template code in the **Signature** column on the **Signaturess** tab of the **Go China** page in the Alibaba Cloud SMS console.
        # 
        # > The signatures must be approved and correspond to the mobile numbers in sequence.
        # 
        # This parameter is required.
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
        # The mobile phone numbers that support card messages.
        self.card_phone_numbers = card_phone_numbers
        # The signatures must correspond to the mobile numbers and short URLs in sequence.
        self.card_sign_names = card_sign_names
        # The short URLs.
        self.card_sms_links = card_sms_links
        # The review status of the card message template.
        # 
        # *   **0**: pending approval
        # *   **1**: approved
        # *   **2**: rejected
        # 
        # > Unapproved card messages are rolled back.
        self.card_tmp_state = card_tmp_state
        # The mobile phone numbers that do not support card messages.
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
        # The HTTP status code.
        # 
        # *   The value OK indicates that the request was successful.
        # *   Other values indicate that the request failed. For more information, see [Error codes](https://help.aliyun.com/document_detail/101346.html).
        self.code = code
        # The data returned.
        self.data = data
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request is successful. Valid values:
        # 
        # *   **true**\
        # *   **false**\
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # The extended fields.
        # 
        # > If you set the ResourceType parameter to **2**, this parameter is required.
        self.extend_info = extend_info
        # The size of the resource. Unit: bytes.
        # 
        # This parameter is required.
        self.file_size = file_size
        # The description of the resource.
        self.memo = memo
        # The address of the resource.
        # 
        # This parameter is required.
        self.oss_key = oss_key
        # The type of the resource.
        # 
        # *   **1**: text.
        # *   **2**: image. A small image cannot exceed 100 KB in size, and a large image cannot exceed 2 MB in size. The image must be clear. Supported format: JPG, JPEG, and PNG.
        # *   **3**: audio.
        # *   **4**: video. Supported format: MP4.
        # 
        # > 
        # 
        # *   If you set the ResourceType parameter to 2, the **img_rate** required is required. Valid values:
        # 
        # *   1:1
        # 
        # *   16:9
        # 
        # *   3:1
        # 
        # *   48:65
        # 
        # This parameter is required.
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
        # The download URL of the resource.
        self.res_url_download = res_url_download
        # The resource ID.
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
        # The response code.
        # 
        # *   If OK is returned, the request is successful.
        # *   Other values indicate that the request fails. For more information, see [Error codes](https://help.aliyun.com/document_detail/101346.html).
        self.code = code
        # The data returned.
        self.data = data
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**\
        # *   **false**\
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # The AccessKey ID.
        self.access_key_id = access_key_id
        # The ID of the Alibaba Cloud account.
        self.ali_uid = ali_uid
        # The name of the OSS bucket.
        self.bucket = bucket
        # The timeout period.
        self.expire_time = expire_time
        # The hostname.
        self.host = host
        # The signature policy.
        self.policy = policy
        # The signature.
        self.signature = signature
        # The path of the policy.
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
        # The HTTP status code.
        # 
        # *   The value OK indicates that the request was successful.
        # *   For more information about other response codes, see [API error codes](https://help.aliyun.com/document_detail/101346.html).
        self.code = code
        # The data returned.
        self.data = data
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request is successful. Valid values:
        # 
        # *   **true**\
        # *   **false**\
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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


class GetOSSInfoForUploadFileRequest(TeaModel):
    def __init__(
        self,
        biz_type: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # Business type, default value is **fcMediaSms**.
        # 
        # When creating signatures and templates, and uploading **additional materials**, this value is **fcMediaSms**.
        self.biz_type = biz_type
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
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class GetOSSInfoForUploadFileResponseBodyModel(TeaModel):
    def __init__(
        self,
        access_key_id: str = None,
        expire_time: str = None,
        host: str = None,
        policy: str = None,
        signature: str = None,
        start_path: str = None,
    ):
        # AccessKey ID used for signing.
        self.access_key_id = access_key_id
        # Expiration time.
        self.expire_time = expire_time
        # Host address.
        self.host = host
        # Signature policy.
        self.policy = policy
        # Signature information calculated based on **AccessKey Secret** and **Policy**. When calling the OSS API, OSS verifies this signature information to confirm the legitimacy of the Post request.
        self.signature = signature
        # Policy path.
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


class GetOSSInfoForUploadFileResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        model: GetOSSInfoForUploadFileResponseBodyModel = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Request status code.
        # 
        # - OK return represents a successful request.
        # - For other error codes, please refer to the [Error Code List](https://help.aliyun.com/document_detail/101346.htm).
        self.code = code
        # Description of the status code.
        self.message = message
        # Return result.
        self.model = model
        # The ID of this call request, which is a unique identifier generated by Alibaba Cloud for the request, can be used for troubleshooting and issue定位.
        self.request_id = request_id
        # Indicates success. Values:
        # 
        # - **true**\
        # - **false**\
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
            temp_model = GetOSSInfoForUploadFileResponseBodyModel()
            self.model = temp_model.from_map(m['Model'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetOSSInfoForUploadFileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetOSSInfoForUploadFileResponseBody = None,
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
            temp_model = GetOSSInfoForUploadFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetQualificationOssInfoRequest(TeaModel):
    def __init__(
        self,
        biz_type: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # 业务，非空
        # 
        # This parameter is required.
        self.biz_type = biz_type
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
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class GetQualificationOssInfoResponseBodyData(TeaModel):
    def __init__(
        self,
        access_key_id: str = None,
        expire: int = None,
        host: str = None,
        policy: str = None,
        signature: str = None,
        start_path: str = None,
    ):
        # ak
        self.access_key_id = access_key_id
        # 过期时间
        self.expire = expire
        # 域名
        self.host = host
        # 策略
        self.policy = policy
        # 签名
        self.signature = signature
        # 前缀
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
        if self.expire is not None:
            result['Expire'] = self.expire
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
        if m.get('Expire') is not None:
            self.expire = m.get('Expire')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('Signature') is not None:
            self.signature = m.get('Signature')
        if m.get('StartPath') is not None:
            self.start_path = m.get('StartPath')
        return self


class GetQualificationOssInfoResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: GetQualificationOssInfoResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.data = data
        self.message = message
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
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
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
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetQualificationOssInfoResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetQualificationOssInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetQualificationOssInfoResponseBody = None,
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
            temp_model = GetQualificationOssInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSmsOcrOssInfoRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        task_type: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # OCR任务类型
        self.task_type = task_type

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
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        return self


class GetSmsOcrOssInfoResponseBodyModel(TeaModel):
    def __init__(
        self,
        access_key_id: str = None,
        bucket: str = None,
        expire_time: str = None,
        host: str = None,
        policy: str = None,
        signature: str = None,
        start_path: str = None,
    ):
        self.access_key_id = access_key_id
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


class GetSmsOcrOssInfoResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        message: str = None,
        model: GetSmsOcrOssInfoResponseBodyModel = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
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
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
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
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Model') is not None:
            temp_model = GetSmsOcrOssInfoResponseBodyModel()
            self.model = temp_model.from_map(m['Model'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetSmsOcrOssInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetSmsOcrOssInfoResponseBody = None,
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
            temp_model = GetSmsOcrOssInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSmsSignRequest(TeaModel):
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
        # Signature name. Must be an SMS signature already applied for by this account.
        # 
        # - Obtain from the return parameters after calling the [CreateSmsSign](https://help.aliyun.com/zh/sms/developer-reference/api-dysmsapi-2017-05-25-createsmssign?spm) API.
        # - View the signature on the [Signature Management](https://dysms.console.aliyun.com/domestic/text/sign) page.
        # 
        # This parameter is required.
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


class GetSmsSignResponseBodyAuditInfo(TeaModel):
    def __init__(
        self,
        audit_date: str = None,
        reject_info: str = None,
    ):
        # Audit date and time.
        self.audit_date = audit_date
        # Reasons for not passing the review.
        self.reject_info = reject_info

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audit_date is not None:
            result['AuditDate'] = self.audit_date
        if self.reject_info is not None:
            result['RejectInfo'] = self.reject_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuditDate') is not None:
            self.audit_date = m.get('AuditDate')
        if m.get('RejectInfo') is not None:
            self.reject_info = m.get('RejectInfo')
        return self


class GetSmsSignResponseBodySignIspRegisterDetailListRegisterStatusReasons(TeaModel):
    def __init__(
        self,
        reason_code: str = None,
        reason_desc_list: List[str] = None,
    ):
        self.reason_code = reason_code
        self.reason_desc_list = reason_desc_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.reason_code is not None:
            result['ReasonCode'] = self.reason_code
        if self.reason_desc_list is not None:
            result['ReasonDescList'] = self.reason_desc_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReasonCode') is not None:
            self.reason_code = m.get('ReasonCode')
        if m.get('ReasonDescList') is not None:
            self.reason_desc_list = m.get('ReasonDescList')
        return self


class GetSmsSignResponseBodySignIspRegisterDetailList(TeaModel):
    def __init__(
        self,
        operator_code: str = None,
        operator_complete_time: str = None,
        register_status: int = None,
        register_status_reasons: List[GetSmsSignResponseBodySignIspRegisterDetailListRegisterStatusReasons] = None,
    ):
        self.operator_code = operator_code
        self.operator_complete_time = operator_complete_time
        self.register_status = register_status
        self.register_status_reasons = register_status_reasons

    def validate(self):
        if self.register_status_reasons:
            for k in self.register_status_reasons:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operator_code is not None:
            result['OperatorCode'] = self.operator_code
        if self.operator_complete_time is not None:
            result['OperatorCompleteTime'] = self.operator_complete_time
        if self.register_status is not None:
            result['RegisterStatus'] = self.register_status
        result['RegisterStatusReasons'] = []
        if self.register_status_reasons is not None:
            for k in self.register_status_reasons:
                result['RegisterStatusReasons'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OperatorCode') is not None:
            self.operator_code = m.get('OperatorCode')
        if m.get('OperatorCompleteTime') is not None:
            self.operator_complete_time = m.get('OperatorCompleteTime')
        if m.get('RegisterStatus') is not None:
            self.register_status = m.get('RegisterStatus')
        self.register_status_reasons = []
        if m.get('RegisterStatusReasons') is not None:
            for k in m.get('RegisterStatusReasons'):
                temp_model = GetSmsSignResponseBodySignIspRegisterDetailListRegisterStatusReasons()
                self.register_status_reasons.append(temp_model.from_map(k))
        return self


class GetSmsSignResponseBody(TeaModel):
    def __init__(
        self,
        apply_scene: str = None,
        audit_info: GetSmsSignResponseBodyAuditInfo = None,
        authorization_letter_audit_pass: bool = None,
        authorization_letter_id: int = None,
        code: str = None,
        create_date: str = None,
        file_url_list: List[str] = None,
        message: str = None,
        order_id: str = None,
        qualification_id: int = None,
        register_result: int = None,
        remark: str = None,
        request_id: str = None,
        sign_code: str = None,
        sign_isp_register_detail_list: List[GetSmsSignResponseBodySignIspRegisterDetailList] = None,
        sign_name: str = None,
        sign_status: int = None,
        sign_tag: str = None,
        sign_usage: str = None,
        third_party: bool = None,
    ):
        # Content of application scenarios.
        self.apply_scene = apply_scene
        # Audit information.
        self.audit_info = audit_info
        self.authorization_letter_audit_pass = authorization_letter_audit_pass
        self.authorization_letter_id = authorization_letter_id
        # Request status code.
        # 
        # - OK indicates a successful request.
        # - For other error codes, see [API Error Codes](https://help.aliyun.com/document_detail/101346.html).
        self.code = code
        # Creation date and time of the SMS signature.
        self.create_date = create_date
        # 更多资料信息，补充上传业务证明文件或业务截图文件列表。
        self.file_url_list = file_url_list
        # Description of the status code.
        self.message = message
        # Work order number.
        # 
        # Used by reviewers when querying the review. You need to provide this work order number if you require expedited review.
        self.order_id = order_id
        # Credential ID, the credential ID associated when applying for the signature.
        self.qualification_id = qualification_id
        self.register_result = register_result
        # Explanation of the SMS signature scenario, with a maximum length of 200 characters.
        self.remark = remark
        # The ID of this call request, which is a unique identifier generated by Alibaba Cloud for the request and can be used for troubleshooting and issue localization.
        self.request_id = request_id
        # SMS signature code.
        self.sign_code = sign_code
        self.sign_isp_register_detail_list = sign_isp_register_detail_list
        # SMS signature name.
        self.sign_name = sign_name
        # Signature review status. Values:
        # 
        # - **0**: Under review.
        # - **1**: Approved.
        # - **2**: Review failed, please check the Reason parameter for the failure cause.
        # - **10**: Review canceled.
        self.sign_status = sign_status
        # Signature tag indicating whether the signature is user-defined, system-provided, test, or trial. Values:
        # 
        # - 2: User-defined signature
        # - 3: System-provided signature
        # - 4: Test signature
        # - 5: Trial signature
        self.sign_tag = sign_tag
        # scenarios for using signatures.
        self.sign_usage = sign_usage
        # Signature usage indication—self-use or third-party use.
        # 
        # - false: Self-use (default)
        # 
        # - true: Third-party use
        self.third_party = third_party

    def validate(self):
        if self.audit_info:
            self.audit_info.validate()
        if self.sign_isp_register_detail_list:
            for k in self.sign_isp_register_detail_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apply_scene is not None:
            result['ApplyScene'] = self.apply_scene
        if self.audit_info is not None:
            result['AuditInfo'] = self.audit_info.to_map()
        if self.authorization_letter_audit_pass is not None:
            result['AuthorizationLetterAuditPass'] = self.authorization_letter_audit_pass
        if self.authorization_letter_id is not None:
            result['AuthorizationLetterId'] = self.authorization_letter_id
        if self.code is not None:
            result['Code'] = self.code
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.file_url_list is not None:
            result['FileUrlList'] = self.file_url_list
        if self.message is not None:
            result['Message'] = self.message
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.qualification_id is not None:
            result['QualificationId'] = self.qualification_id
        if self.register_result is not None:
            result['RegisterResult'] = self.register_result
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sign_code is not None:
            result['SignCode'] = self.sign_code
        result['SignIspRegisterDetailList'] = []
        if self.sign_isp_register_detail_list is not None:
            for k in self.sign_isp_register_detail_list:
                result['SignIspRegisterDetailList'].append(k.to_map() if k else None)
        if self.sign_name is not None:
            result['SignName'] = self.sign_name
        if self.sign_status is not None:
            result['SignStatus'] = self.sign_status
        if self.sign_tag is not None:
            result['SignTag'] = self.sign_tag
        if self.sign_usage is not None:
            result['SignUsage'] = self.sign_usage
        if self.third_party is not None:
            result['ThirdParty'] = self.third_party
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplyScene') is not None:
            self.apply_scene = m.get('ApplyScene')
        if m.get('AuditInfo') is not None:
            temp_model = GetSmsSignResponseBodyAuditInfo()
            self.audit_info = temp_model.from_map(m['AuditInfo'])
        if m.get('AuthorizationLetterAuditPass') is not None:
            self.authorization_letter_audit_pass = m.get('AuthorizationLetterAuditPass')
        if m.get('AuthorizationLetterId') is not None:
            self.authorization_letter_id = m.get('AuthorizationLetterId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('FileUrlList') is not None:
            self.file_url_list = m.get('FileUrlList')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('QualificationId') is not None:
            self.qualification_id = m.get('QualificationId')
        if m.get('RegisterResult') is not None:
            self.register_result = m.get('RegisterResult')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SignCode') is not None:
            self.sign_code = m.get('SignCode')
        self.sign_isp_register_detail_list = []
        if m.get('SignIspRegisterDetailList') is not None:
            for k in m.get('SignIspRegisterDetailList'):
                temp_model = GetSmsSignResponseBodySignIspRegisterDetailList()
                self.sign_isp_register_detail_list.append(temp_model.from_map(k))
        if m.get('SignName') is not None:
            self.sign_name = m.get('SignName')
        if m.get('SignStatus') is not None:
            self.sign_status = m.get('SignStatus')
        if m.get('SignTag') is not None:
            self.sign_tag = m.get('SignTag')
        if m.get('SignUsage') is not None:
            self.sign_usage = m.get('SignUsage')
        if m.get('ThirdParty') is not None:
            self.third_party = m.get('ThirdParty')
        return self


class GetSmsSignResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetSmsSignResponseBody = None,
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
            temp_model = GetSmsSignResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSmsTemplateRequest(TeaModel):
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
        # SMS template code.
        # 
        # - Obtain the SMS template code from the return parameters of the [CreateSmsTemplate](https://help.aliyun.com/zh/sms/developer-reference/api-dysmsapi-2017-05-25-createsmstemplate?spm) API.
        # - View the SMS template code on the [Template Management](https://dysms.console.aliyun.com/domestic/text/template) page.
        # 
        # This parameter is required.
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


class GetSmsTemplateResponseBodyAuditInfo(TeaModel):
    def __init__(
        self,
        audit_date: str = None,
        reject_info: str = None,
    ):
        # Audit date and time.
        self.audit_date = audit_date
        # Reasons for failed audit.
        self.reject_info = reject_info

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audit_date is not None:
            result['AuditDate'] = self.audit_date
        if self.reject_info is not None:
            result['RejectInfo'] = self.reject_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuditDate') is not None:
            self.audit_date = m.get('AuditDate')
        if m.get('RejectInfo') is not None:
            self.reject_info = m.get('RejectInfo')
        return self


class GetSmsTemplateResponseBodyFileUrlList(TeaModel):
    def __init__(
        self,
        file_url: List[str] = None,
    ):
        self.file_url = file_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        return self


class GetSmsTemplateResponseBodyMoreDataFileUrlList(TeaModel):
    def __init__(
        self,
        more_data_file_url: List[str] = None,
    ):
        self.more_data_file_url = more_data_file_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.more_data_file_url is not None:
            result['MoreDataFileUrl'] = self.more_data_file_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MoreDataFileUrl') is not None:
            self.more_data_file_url = m.get('MoreDataFileUrl')
        return self


class GetSmsTemplateResponseBody(TeaModel):
    def __init__(
        self,
        apply_scene: str = None,
        audit_info: GetSmsTemplateResponseBodyAuditInfo = None,
        code: str = None,
        create_date: str = None,
        file_url_list: GetSmsTemplateResponseBodyFileUrlList = None,
        intl_type: int = None,
        message: str = None,
        more_data_file_url_list: GetSmsTemplateResponseBodyMoreDataFileUrlList = None,
        order_id: str = None,
        related_sign_name: str = None,
        remark: str = None,
        request_id: str = None,
        template_code: str = None,
        template_content: str = None,
        template_name: str = None,
        template_status: str = None,
        template_tag: int = None,
        template_type: str = None,
        variable_attribute: str = None,
        vendor_audit_status: Dict[str, Any] = None,
    ):
        # Application scenario content.
        self.apply_scene = apply_scene
        # Audit information.
        self.audit_info = audit_info
        # Request status code.
        # 
        # * OK indicates a successful request.
        # * For other error codes, please refer to [API Error Codes](https://help.aliyun.com/document_detail/101346.html).
        self.code = code
        # The time when the SMS template was created.
        self.create_date = create_date
        # File information, compatible with signatures created by the [AddSmsSign](https://help.aliyun.com/zh/sms/developer-reference/api-dysmsapi-2017-05-25-addsmstemplate?spm) API.
        self.file_url_list = file_url_list
        # International/Hong Kong, Macao, and Taiwan template type. When the **TemplateType** parameter is **3**, this parameter is required for international/Hong Kong, Macao, and Taiwan templates, with values:
        # - **0**: Verification code.
        # - **1**: SMS notification.
        # - **2**: Promotional SMS.
        self.intl_type = intl_type
        # Description of the status code.
        self.message = message
        # Additional documentation information, supplementing uploaded business proof files or operational screenshots file list.
        self.more_data_file_url_list = more_data_file_url_list
        # Work order number.
        # 
        # This parameter is used by auditors when querying the audit. You need to provide this work order number when requesting expedited review.
        self.order_id = order_id
        # The SMS signature associated with the template when applied.
        self.related_sign_name = related_sign_name
        # Explanation for the SMS template application, which is one of the reference information for template review.
        self.remark = remark
        # The ID of this call request, which is a unique identifier generated by Alibaba Cloud for the request and can be used for troubleshooting and issue定位.
        self.request_id = request_id
        # SMS template code.
        self.template_code = template_code
        # Content of the SMS template.
        self.template_content = template_content
        # Name of the SMS template.
        self.template_name = template_name
        # Template review status. Return values:
        # 
        # - **0**: Under review.
        # - **1**: Approved.
        # - **2**: Not approved, with reasons for failure returned. Please refer to [Handling Suggestions for Failed SMS Reviews](https://help.aliyun.com/zh/sms/user-guide/causes-of-application-failures-and-suggestions?spm=a2c4g.11186623.0.0.41fd339f3bPSCQ), invoke the [UpdateSmsTemplate](https://help.aliyun.com/zh/sms/developer-reference/api-dysmsapi-2017-05-25-updatesmstemplate?spm) API or modify the SMS template on the [Template Management](https://dysms.console.aliyun.com/domestic/text/template) page.
        # - **10**: Review canceled.
        self.template_status = template_status
        # Template identifier, indicating whether the template is user-defined or system-provided. Values:
        # 
        # - **2**: User-defined template.
        # 
        # - **3**: System-provided template.
        self.template_tag = template_tag
        # SMS type. Values:
        # 
        # - **0**: Verification code.
        # - **1**: SMS notification.
        # - **2**: Promotional SMS.
        # - **3**: International/Hong Kong, Macao, and Taiwan messages.
        # 
        # > Only enterprise-certified users can apply for promotional SMS and international/Hong Kong, Macao, and Taiwan messages. For details on the differences between personal and enterprise user rights, please refer to [Usage Notes](https://help.aliyun.com/zh/sms/user-guide/usage-notes?spm=a2c4g.11186623.0.0.67447f576NJnE8).
        self.template_type = template_type
        # Template variable rules.
        # 
        # For detailed rules of template variables, refer to the [Example Document](https://help.aliyun.com/zh/sms/templaterule-template-variable-parameter-filling-example).
        self.variable_attribute = variable_attribute
        self.vendor_audit_status = vendor_audit_status

    def validate(self):
        if self.audit_info:
            self.audit_info.validate()
        if self.file_url_list:
            self.file_url_list.validate()
        if self.more_data_file_url_list:
            self.more_data_file_url_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apply_scene is not None:
            result['ApplyScene'] = self.apply_scene
        if self.audit_info is not None:
            result['AuditInfo'] = self.audit_info.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.file_url_list is not None:
            result['FileUrlList'] = self.file_url_list.to_map()
        if self.intl_type is not None:
            result['IntlType'] = self.intl_type
        if self.message is not None:
            result['Message'] = self.message
        if self.more_data_file_url_list is not None:
            result['MoreDataFileUrlList'] = self.more_data_file_url_list.to_map()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.related_sign_name is not None:
            result['RelatedSignName'] = self.related_sign_name
        if self.remark is not None:
            result['Remark'] = self.remark
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
        if self.template_tag is not None:
            result['TemplateTag'] = self.template_tag
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        if self.variable_attribute is not None:
            result['VariableAttribute'] = self.variable_attribute
        if self.vendor_audit_status is not None:
            result['VendorAuditStatus'] = self.vendor_audit_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplyScene') is not None:
            self.apply_scene = m.get('ApplyScene')
        if m.get('AuditInfo') is not None:
            temp_model = GetSmsTemplateResponseBodyAuditInfo()
            self.audit_info = temp_model.from_map(m['AuditInfo'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('FileUrlList') is not None:
            temp_model = GetSmsTemplateResponseBodyFileUrlList()
            self.file_url_list = temp_model.from_map(m['FileUrlList'])
        if m.get('IntlType') is not None:
            self.intl_type = m.get('IntlType')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('MoreDataFileUrlList') is not None:
            temp_model = GetSmsTemplateResponseBodyMoreDataFileUrlList()
            self.more_data_file_url_list = temp_model.from_map(m['MoreDataFileUrlList'])
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RelatedSignName') is not None:
            self.related_sign_name = m.get('RelatedSignName')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
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
        if m.get('TemplateTag') is not None:
            self.template_tag = m.get('TemplateTag')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        if m.get('VariableAttribute') is not None:
            self.variable_attribute = m.get('VariableAttribute')
        if m.get('VendorAuditStatus') is not None:
            self.vendor_audit_status = m.get('VendorAuditStatus')
        return self


class GetSmsTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetSmsTemplateResponseBody = None,
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
            temp_model = GetSmsTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagResourcesRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag.
        self.key = key
        # The value of the tag.
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
        # The token used to query the next page.
        self.next_token = next_token
        self.owner_id = owner_id
        # The number of entries per page.
        self.page_size = page_size
        # The name of the cloud service. Set the value to **dysms**.
        self.prod_code = prod_code
        # The region ID. Set the value to **cn-hangzhou**.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The code of the message template. Specify either the Tag or the ResourceId parameter.
        self.resource_id = resource_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The type of the resource. Set the value to TEMPLATE.
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The tag list. Specify either the Tag or the ResourceId parameter. You can specify a maximum of 20 tags.
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
        # The code of the message template.
        self.resource_id = resource_id
        # The type of resource.
        self.resource_type = resource_type
        # The tag key.
        self.tag_key = tag_key
        # The tag value.
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
        # The response code.
        # 
        # *   If OK is returned, the request is successful.
        # *   Other values indicate that the request fails. For more information, see [Error codes](https://help.aliyun.com/document_detail/101346.html).
        self.code = code
        # The token used to query the next page.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The list of tags.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # The base64-encoded string of the signed files. The size of the image cannot exceed 2 MB.
        # 
        # In some scenarios, documents are required to prove your identity. For more information, see [Signature specifications](https://help.aliyun.com/document_detail/108076.html).
        # 
        # This parameter is required.
        self.file_contents = file_contents
        # The format of the documents. You can upload multiple images. JPG, PNG, GIF, and JPEG are supported.
        # 
        # In some scenarios, documents are required to prove your identity. For more information, see [Signature specifications](https://help.aliyun.com/document_detail/108076.html).
        # 
        # > If the signature is used for other purposes or the signature source is an enterprise or public institution, you must upload some documents and an authorization letter. For more information, see [Documents](https://help.aliyun.com/document_detail/108076.html) and [Letter of authorization](https://help.aliyun.com/document_detail/56741.html).
        # 
        # This parameter is required.
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
        # The scenario description of your released services. Provide the information of your services, such as a website URL, a domain name with an ICP filing, an app download URL, or the name of your WeChat official account or mini program. For sign-in scenarios, you must also provide an account and password for tests. A detailed description can improve the review efficiency of signatures and templates.
        # 
        # > The description can be up to 200 characters in length.
        # 
        # This parameter is required.
        self.remark = remark
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The list of signature files.
        # 
        # This parameter is required.
        self.sign_file_list = sign_file_list
        # The signature.
        # 
        # This parameter is required.
        self.sign_name = sign_name
        # The source of the signature. Valid values:
        # 
        # *   **0**: full name or abbreviation of an enterprise or institution.
        # *   **1**: full name or abbreviation of a website with Ministry of Industry and Information Technology (MIIT) filing.
        # *   **2**: full name or abbreviation of an app.
        # *   **3**: full name or abbreviation of a WeChat official account or applet.
        # *   **4**: full name or abbreviation of an e-commerce store.
        # *   **5**: full name or abbreviation of a trademark.
        # 
        # This parameter is required.
        self.sign_source = sign_source
        # The type of the signature. Valid values:
        # 
        # *   **0**: verification-code signature
        # *   **1**: general-purpose signature
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
        # The response code.
        # 
        # *   The value OK indicates that the request was successful.
        # *   For more information about other response codes, see [API error codes](https://help.aliyun.com/document_detail/101346.html).
        self.code = code
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The signature.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # The description of the message template. It is one of the reference information for template review. The description cannot exceed 100 characters in length.
        # 
        # This parameter is required.
        self.remark = remark
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The code of the message template.
        # 
        # You can log on to the [Short Message Service (SMS) console](https://dysms.console.aliyun.com/dysms.htm), click **Go China** or **Go Globe** in the left-side navigation pane, and then view the template code on the **Templates** tab. You can also call the [AddSmsTemplate](https://help.aliyun.com/document_detail/121208.html) operation to obtain the template code.
        # 
        # This parameter is required.
        self.template_code = template_code
        # The content of the template. The content must be 1 to 500 characters in length.
        # 
        # > When you modify a template, design the template content based on the review comments.
        # 
        # This parameter is required.
        self.template_content = template_content
        # The name of the template. The name must be 1 to 30 characters in length.
        # 
        # This parameter is required.
        self.template_name = template_name
        # The type of the message. Valid values:
        # 
        # *   **0**: verification code
        # *   **1**: text message
        # *   **2**: promotional message
        # *   **3**: message sent to countries or regions outside the Chinese mainland
        # 
        # This parameter is required.
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
        # The response code.
        # 
        # *   The value OK indicates that the request was successful.
        # *   Other values indicate that the request failed. For more information, see [Error codes](https://help.aliyun.com/document_detail/101346.html).
        self.code = code
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The code of the message template.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # The code of the message template.
        # 
        # You can view the template code in the **Template Code** column on the **Templates** tab of the **Go China** page in the Alibaba Cloud SMS console.
        # 
        # > Make sure that the message template has been approved.
        # 
        # This parameter is required.
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
        # The array of objects.
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
        # The HTTP status code.
        # 
        # *   The value OK indicates that the request was successful.
        # *   For more information about other response codes, see [API error codes](https://help.aliyun.com/document_detail/101346.html).
        self.code = code
        # The data returned.
        self.data = data
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request is successful. Valid values:
        # 
        # *   **true**\
        # *   **false**\
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # The end of the time range to query. Specify the time in the yyyy-MM-dd HH:mm:ss format.
        self.end_date = end_date
        # The beginning of the time range to query. Specify the time in the yyyy-MM-dd HH:mm:ss format.
        self.start_date = start_date
        # The array of message templates.
        # 
        # This parameter is required.
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
        # The details of the data returned.
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
        # The HTTP status code.
        # 
        # *   The value OK indicates that the request was successful.
        # *   Other values indicate that the request failed. For more information, see [Error codes](https://help.aliyun.com/document_detail/101346.html).
        self.code = code
        # The data returned.
        self.data = data
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request is successful. Valid values:
        # 
        # *   **true**\
        # *   **false**\
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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


class QueryExtCodeSignRequest(TeaModel):
    def __init__(
        self,
        ext_code: str = None,
        owner_id: int = None,
        page_no: int = None,
        page_size: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        sign_name: str = None,
    ):
        # 扩展码A3
        self.ext_code = ext_code
        self.owner_id = owner_id
        self.page_no = page_no
        self.page_size = page_size
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # 签名
        self.sign_name = sign_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ext_code is not None:
            result['ExtCode'] = self.ext_code
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.sign_name is not None:
            result['SignName'] = self.sign_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExtCode') is not None:
            self.ext_code = m.get('ExtCode')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SignName') is not None:
            self.sign_name = m.get('SignName')
        return self


class QueryExtCodeSignResponseBodyDataList(TeaModel):
    def __init__(
        self,
        active: int = None,
        ext_code: str = None,
        send_count: int = None,
        sign_name: str = None,
        source: str = None,
    ):
        # 是否可回收
        self.active = active
        # 扩展码A3
        self.ext_code = ext_code
        # 近1个月发送成功条数（只读）
        self.send_count = send_count
        # 签名
        self.sign_name = sign_name
        # 来源
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active is not None:
            result['Active'] = self.active
        if self.ext_code is not None:
            result['ExtCode'] = self.ext_code
        if self.send_count is not None:
            result['SendCount'] = self.send_count
        if self.sign_name is not None:
            result['SignName'] = self.sign_name
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Active') is not None:
            self.active = m.get('Active')
        if m.get('ExtCode') is not None:
            self.ext_code = m.get('ExtCode')
        if m.get('SendCount') is not None:
            self.send_count = m.get('SendCount')
        if m.get('SignName') is not None:
            self.sign_name = m.get('SignName')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class QueryExtCodeSignResponseBodyData(TeaModel):
    def __init__(
        self,
        list: List[QueryExtCodeSignResponseBodyDataList] = None,
        page_no: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.list = list
        self.page_no = page_no
        self.page_size = page_size
        self.total = total

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
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = QueryExtCodeSignResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class QueryExtCodeSignResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: QueryExtCodeSignResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.data = data
        self.message = message
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
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
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
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = QueryExtCodeSignResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryExtCodeSignResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryExtCodeSignResponseBody = None,
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
            temp_model = QueryExtCodeSignResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryMobilesCardSupportRequest(TeaModel):
    def __init__(
        self,
        encrypt_type: str = None,
        mobiles: List[Dict[str, Any]] = None,
        template_code: str = None,
    ):
        self.encrypt_type = encrypt_type
        # The list of mobile phone numbers.
        # 
        # This parameter is required.
        self.mobiles = mobiles
        # The code of the message template. You can view the template code in the **Template Code** column on the **Templates** tab of the **Go China** page in the Alibaba Cloud SMS console.
        # 
        # > Make sure that the message template has been approved.
        # 
        # This parameter is required.
        self.template_code = template_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encrypt_type is not None:
            result['EncryptType'] = self.encrypt_type
        if self.mobiles is not None:
            result['Mobiles'] = self.mobiles
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncryptType') is not None:
            self.encrypt_type = m.get('EncryptType')
        if m.get('Mobiles') is not None:
            self.mobiles = m.get('Mobiles')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        return self


class QueryMobilesCardSupportShrinkRequest(TeaModel):
    def __init__(
        self,
        encrypt_type: str = None,
        mobiles_shrink: str = None,
        template_code: str = None,
    ):
        self.encrypt_type = encrypt_type
        # The list of mobile phone numbers.
        # 
        # This parameter is required.
        self.mobiles_shrink = mobiles_shrink
        # The code of the message template. You can view the template code in the **Template Code** column on the **Templates** tab of the **Go China** page in the Alibaba Cloud SMS console.
        # 
        # > Make sure that the message template has been approved.
        # 
        # This parameter is required.
        self.template_code = template_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encrypt_type is not None:
            result['EncryptType'] = self.encrypt_type
        if self.mobiles_shrink is not None:
            result['Mobiles'] = self.mobiles_shrink
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncryptType') is not None:
            self.encrypt_type = m.get('EncryptType')
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
        # The mobile phone number.
        self.mobile = mobile
        # Indicates whether the mobile phone number supports card messages. Valid values:
        # 
        # *   **true**\
        # *   **false**\
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
        # The list of returned results.
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
        # The HTTP status code.
        # 
        # *   The value OK indicates that the request was successful.
        # *   Other values indicate that the request failed. For more information, see [Error codes](https://help.aliyun.com/document_detail/101346.html).
        self.code = code
        # The data returned.
        self.data = data
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request is successful. Valid values:
        # 
        # *   **true**\
        # *   **false**\
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        create_date_end: int = None,
        create_date_start: int = None,
        owner_id: int = None,
        page_no: int = None,
        page_size: int = None,
        phone_number: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        short_url: str = None,
    ):
        # This parameter is required.
        self.create_date_end = create_date_end
        # This parameter is required.
        self.create_date_start = create_date_start
        self.owner_id = owner_id
        # This parameter is required.
        self.page_no = page_no
        # This parameter is required.
        self.page_size = page_size
        self.phone_number = phone_number
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
        if self.create_date_end is not None:
            result['CreateDateEnd'] = self.create_date_end
        if self.create_date_start is not None:
            result['CreateDateStart'] = self.create_date_start
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
        if self.short_url is not None:
            result['ShortUrl'] = self.short_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateDateEnd') is not None:
            self.create_date_end = m.get('CreateDateEnd')
        if m.get('CreateDateStart') is not None:
            self.create_date_start = m.get('CreateDateStart')
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
        if m.get('ShortUrl') is not None:
            self.short_url = m.get('ShortUrl')
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # The ID of the delivery receipt. The delivery receipt ID is the value of the BizId parameter that is returned when you call the SendSms or SendBatchSms operation.
        self.biz_id = biz_id
        # The page number of the first page.
        # 
        # This parameter is required.
        self.current_page = current_page
        self.owner_id = owner_id
        # The number of items displayed per page.
        # 
        # Valid values: 1 to 50.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The mobile numbers of the recipients. Format:
        # 
        # *   If you send messages in the Chinese mainland, specify an 11-digit mobile number, for example, 1390000\\*\\*\\*\\*.
        # *   If you send messages to countries or regions outside the Chinese mainland, specify this parameter in the \\<Area code>\\<Mobile number> format. Example: 8520000\\*\\*\\*\\*.
        # 
        # This parameter is required.
        self.phone_number = phone_number
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The date when the message was sent. You can query messages that were sent within the last 30 days.
        # 
        # Format: yyyyMMdd. Example: 20181225.
        # 
        # This parameter is required.
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
        # The content of the message.
        self.content = content
        # The status code returned by the carrier.
        # 
        # *   If the message is delivered, "DELIVERED" is returned.
        # *   For information about the error codes that may be returned if the message is not delivered, see [error codes](https://help.aliyun.com/document_detail/101347.html).
        self.err_code = err_code
        # The extended field.
        self.out_id = out_id
        # The mobile numbers of the recipients.
        self.phone_num = phone_num
        # The date and time when the message was received.
        self.receive_date = receive_date
        # The date and time when the message was sent.
        self.send_date = send_date
        # The delivery status of the message. Valid values:
        # 
        # *   **1**: The message has not received a delivery receipt yet.
        # *   **2**: The message failed to be delivered.
        # *   **3**: The message was delivered.
        self.send_status = send_status
        # The ID of the message template.
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
        # The response code.
        # 
        # *   The value OK indicates that the request was successful.
        # *   Other values indicate that the request failed. For more information, see [Error codes](https://help.aliyun.com/document_detail/101346.html).
        self.code = code
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The details of the message.
        self.sms_send_detail_dtos = sms_send_detail_dtos
        # The number of sent messages.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # The end of the time range to query. Format: yyyyMMdd. Example: 20181225.
        # 
        # This parameter is required.
        self.end_date = end_date
        # The site from where the message is sent. Valid values:
        # 
        # *   **1**: China site
        # *   **2**: international site
        # 
        # This parameter is required.
        self.is_globe = is_globe
        self.owner_id = owner_id
        # The page number. Default value: **1**.
        # 
        # This parameter is required.
        self.page_index = page_index
        # The number of entries to return on each page. Valid values: **1 to 50**.
        # 
        # This parameter is required.
        self.page_size = page_size
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The signature.
        self.sign_name = sign_name
        # The beginning of the time range to query. Format: yyyyMMdd. Example: 20181225.
        # 
        # This parameter is required.
        self.start_date = start_date
        # The type of the message template. Valid values: Valid values:
        # 
        # *   **0**: verification code
        # *   **1**: notification
        # *   **2**: promotional message (Enterprise users only)
        # *   **3**: international purpose (Enterprise users only)
        # *   **7**: digital message
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
        # The number of messages without a delivery receipt.
        self.no_responded_count = no_responded_count
        # The number of messages with a delivery receipt that indicates a failure.
        self.responded_fail_count = responded_fail_count
        # The number of messages with a delivery receipt that indicates a success.
        self.responded_success_count = responded_success_count
        # The date when the message is sent. Format: yyyyMMdd. Example: 20181225.
        self.send_date = send_date
        # The number of delivered messages.
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
        # The details of the data returned.
        self.target_list = target_list
        # The total number of entries returned.
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
        # The response code.
        # 
        # *   If OK is returned, the request is successful.
        # *   Other values indicate that the request fails. For more information, see [Error codes](https://help.aliyun.com/document_detail/101346.html).
        self.code = code
        # The data returned.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # The short URL. You can query the short URL by calling the [AddShortUrl](https://help.aliyun.com/document_detail/186774.html) operation.
        # 
        # This parameter is required.
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
        # The time when the short URL was created.
        self.create_date = create_date
        # The time when the short URL expires.
        self.expire_date = expire_date
        # The PV.
        self.page_view_count = page_view_count
        # The short URL.
        self.short_url = short_url
        # The service name of the short URL.
        self.short_url_name = short_url_name
        # The status of the short URL. Valid values:
        # 
        # *   **expired**\
        # *   **effective**\
        # *   **audit**\
        # *   **reject**\
        self.short_url_status = short_url_status
        # The source address.
        self.source_url = source_url
        # The UV.
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
        # The response code.
        # 
        # *   If OK is returned, the request is successful.
        # *   Other values indicate that the request fails. For more information, see [Error codes](https://help.aliyun.com/document_detail/101346.html).
        self.code = code
        # The details of the short URL.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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


class QuerySingleSmsQualificationRequest(TeaModel):
    def __init__(
        self,
        order_id: int = None,
        owner_id: int = None,
        qualification_group_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # 工单id
        self.order_id = order_id
        self.owner_id = owner_id
        # 资质id
        # 
        # This parameter is required.
        self.qualification_group_id = qualification_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.qualification_group_id is not None:
            result['QualificationGroupId'] = self.qualification_group_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('QualificationGroupId') is not None:
            self.qualification_group_id = m.get('QualificationGroupId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class QuerySingleSmsQualificationResponseBodyDataBusinessLicensePics(TeaModel):
    def __init__(
        self,
        license_pic: str = None,
        pic_url: str = None,
        type: str = None,
    ):
        self.license_pic = license_pic
        # 文件的完整路径
        self.pic_url = pic_url
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.license_pic is not None:
            result['LicensePic'] = self.license_pic
        if self.pic_url is not None:
            result['PicUrl'] = self.pic_url
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LicensePic') is not None:
            self.license_pic = m.get('LicensePic')
        if m.get('PicUrl') is not None:
            self.pic_url = m.get('PicUrl')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class QuerySingleSmsQualificationResponseBodyDataOtherFiles(TeaModel):
    def __init__(
        self,
        license_pic: str = None,
        pic_url: str = None,
    ):
        self.license_pic = license_pic
        # 文件的完整路径
        self.pic_url = pic_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.license_pic is not None:
            result['LicensePic'] = self.license_pic
        if self.pic_url is not None:
            result['PicUrl'] = self.pic_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LicensePic') is not None:
            self.license_pic = m.get('LicensePic')
        if m.get('PicUrl') is not None:
            self.pic_url = m.get('PicUrl')
        return self


class QuerySingleSmsQualificationResponseBodyData(TeaModel):
    def __init__(
        self,
        admin_idcard_exp_date: str = None,
        admin_idcard_front_face: str = None,
        admin_idcard_no: str = None,
        admin_idcard_pic: str = None,
        admin_idcard_type: str = None,
        admin_name: str = None,
        admin_phone_no: str = None,
        business_license_pics: List[QuerySingleSmsQualificationResponseBodyDataBusinessLicensePics] = None,
        business_type: str = None,
        company_name: str = None,
        company_type: str = None,
        eff_time_str: str = None,
        legal_person_idcard_no: str = None,
        legal_person_idcard_type: str = None,
        legal_person_id_card_eff_time: str = None,
        legal_person_name: str = None,
        organization_code: str = None,
        other_files: List[QuerySingleSmsQualificationResponseBodyDataOtherFiles] = None,
        qualification_group_id: int = None,
        qualification_name: str = None,
        remark: str = None,
        state: str = None,
        use_by_self: bool = None,
        whether_share: bool = None,
        work_order_id: int = None,
    ):
        # 经办人身份证有效期
        self.admin_idcard_exp_date = admin_idcard_exp_date
        # 经办人身份证国徽面，产品需求，要求身份证可以分正反面上传
        self.admin_idcard_front_face = admin_idcard_front_face
        # 经办人身份证号码
        self.admin_idcard_no = admin_idcard_no
        # 经办人身份证图片地址，正反面合一
        self.admin_idcard_pic = admin_idcard_pic
        # 管理员身份证类型
        self.admin_idcard_type = admin_idcard_type
        # 经办人姓名
        self.admin_name = admin_name
        # 经办人手机号码
        self.admin_phone_no = admin_phone_no
        # 证件信息
        self.business_license_pics = business_license_pics
        # 行业类型，在当前模式下是可以用产品线code来区分
        self.business_type = business_type
        # 公司名称
        self.company_name = company_name
        # 企业类型, COMPANY:公司，政府或者事业单位:NON_PROFIT_ORGANIZATION
        self.company_type = company_type
        self.eff_time_str = eff_time_str
        # 法人身份证号码
        self.legal_person_idcard_no = legal_person_idcard_no
        # 法人身份证类型
        self.legal_person_idcard_type = legal_person_idcard_type
        # 法人身份证有效期
        self.legal_person_id_card_eff_time = legal_person_id_card_eff_time
        # 法人姓名
        self.legal_person_name = legal_person_name
        # 社会统一信用代码
        self.organization_code = organization_code
        # 更多资料
        self.other_files = other_files
        self.qualification_group_id = qualification_group_id
        # 资质名称
        self.qualification_name = qualification_name
        # 备注
        self.remark = remark
        # 当前审核状态
        self.state = state
        # 是否自用
        self.use_by_self = use_by_self
        self.whether_share = whether_share
        # 乾坤袋工单ID
        self.work_order_id = work_order_id

    def validate(self):
        if self.business_license_pics:
            for k in self.business_license_pics:
                if k:
                    k.validate()
        if self.other_files:
            for k in self.other_files:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.admin_idcard_exp_date is not None:
            result['AdminIDCardExpDate'] = self.admin_idcard_exp_date
        if self.admin_idcard_front_face is not None:
            result['AdminIDCardFrontFace'] = self.admin_idcard_front_face
        if self.admin_idcard_no is not None:
            result['AdminIDCardNo'] = self.admin_idcard_no
        if self.admin_idcard_pic is not None:
            result['AdminIDCardPic'] = self.admin_idcard_pic
        if self.admin_idcard_type is not None:
            result['AdminIDCardType'] = self.admin_idcard_type
        if self.admin_name is not None:
            result['AdminName'] = self.admin_name
        if self.admin_phone_no is not None:
            result['AdminPhoneNo'] = self.admin_phone_no
        result['BusinessLicensePics'] = []
        if self.business_license_pics is not None:
            for k in self.business_license_pics:
                result['BusinessLicensePics'].append(k.to_map() if k else None)
        if self.business_type is not None:
            result['BusinessType'] = self.business_type
        if self.company_name is not None:
            result['CompanyName'] = self.company_name
        if self.company_type is not None:
            result['CompanyType'] = self.company_type
        if self.eff_time_str is not None:
            result['EffTimeStr'] = self.eff_time_str
        if self.legal_person_idcard_no is not None:
            result['LegalPersonIDCardNo'] = self.legal_person_idcard_no
        if self.legal_person_idcard_type is not None:
            result['LegalPersonIDCardType'] = self.legal_person_idcard_type
        if self.legal_person_id_card_eff_time is not None:
            result['LegalPersonIdCardEffTime'] = self.legal_person_id_card_eff_time
        if self.legal_person_name is not None:
            result['LegalPersonName'] = self.legal_person_name
        if self.organization_code is not None:
            result['OrganizationCode'] = self.organization_code
        result['OtherFiles'] = []
        if self.other_files is not None:
            for k in self.other_files:
                result['OtherFiles'].append(k.to_map() if k else None)
        if self.qualification_group_id is not None:
            result['QualificationGroupId'] = self.qualification_group_id
        if self.qualification_name is not None:
            result['QualificationName'] = self.qualification_name
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.state is not None:
            result['State'] = self.state
        if self.use_by_self is not None:
            result['UseBySelf'] = self.use_by_self
        if self.whether_share is not None:
            result['WhetherShare'] = self.whether_share
        if self.work_order_id is not None:
            result['WorkOrderId'] = self.work_order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdminIDCardExpDate') is not None:
            self.admin_idcard_exp_date = m.get('AdminIDCardExpDate')
        if m.get('AdminIDCardFrontFace') is not None:
            self.admin_idcard_front_face = m.get('AdminIDCardFrontFace')
        if m.get('AdminIDCardNo') is not None:
            self.admin_idcard_no = m.get('AdminIDCardNo')
        if m.get('AdminIDCardPic') is not None:
            self.admin_idcard_pic = m.get('AdminIDCardPic')
        if m.get('AdminIDCardType') is not None:
            self.admin_idcard_type = m.get('AdminIDCardType')
        if m.get('AdminName') is not None:
            self.admin_name = m.get('AdminName')
        if m.get('AdminPhoneNo') is not None:
            self.admin_phone_no = m.get('AdminPhoneNo')
        self.business_license_pics = []
        if m.get('BusinessLicensePics') is not None:
            for k in m.get('BusinessLicensePics'):
                temp_model = QuerySingleSmsQualificationResponseBodyDataBusinessLicensePics()
                self.business_license_pics.append(temp_model.from_map(k))
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')
        if m.get('CompanyName') is not None:
            self.company_name = m.get('CompanyName')
        if m.get('CompanyType') is not None:
            self.company_type = m.get('CompanyType')
        if m.get('EffTimeStr') is not None:
            self.eff_time_str = m.get('EffTimeStr')
        if m.get('LegalPersonIDCardNo') is not None:
            self.legal_person_idcard_no = m.get('LegalPersonIDCardNo')
        if m.get('LegalPersonIDCardType') is not None:
            self.legal_person_idcard_type = m.get('LegalPersonIDCardType')
        if m.get('LegalPersonIdCardEffTime') is not None:
            self.legal_person_id_card_eff_time = m.get('LegalPersonIdCardEffTime')
        if m.get('LegalPersonName') is not None:
            self.legal_person_name = m.get('LegalPersonName')
        if m.get('OrganizationCode') is not None:
            self.organization_code = m.get('OrganizationCode')
        self.other_files = []
        if m.get('OtherFiles') is not None:
            for k in m.get('OtherFiles'):
                temp_model = QuerySingleSmsQualificationResponseBodyDataOtherFiles()
                self.other_files.append(temp_model.from_map(k))
        if m.get('QualificationGroupId') is not None:
            self.qualification_group_id = m.get('QualificationGroupId')
        if m.get('QualificationName') is not None:
            self.qualification_name = m.get('QualificationName')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('UseBySelf') is not None:
            self.use_by_self = m.get('UseBySelf')
        if m.get('WhetherShare') is not None:
            self.whether_share = m.get('WhetherShare')
        if m.get('WorkOrderId') is not None:
            self.work_order_id = m.get('WorkOrderId')
        return self


class QuerySingleSmsQualificationResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: QuerySingleSmsQualificationResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.data = data
        self.message = message
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
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
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
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = QuerySingleSmsQualificationResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QuerySingleSmsQualificationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QuerySingleSmsQualificationResponseBody = None,
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
            temp_model = QuerySingleSmsQualificationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QuerySmsAuthorizationLetterRequest(TeaModel):
    def __init__(
        self,
        authorization_letter_id_list: List[int] = None,
        organization_code: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        sign_name: str = None,
        state: str = None,
        status: str = None,
    ):
        # 委托授权书id列表
        self.authorization_letter_id_list = authorization_letter_id_list
        # 授权方社会统一信用代码
        self.organization_code = organization_code
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # 签名名称（支持命中签名范围查询）
        self.sign_name = sign_name
        # 授权书审核状态，INT:审核中，PASSED:审核通过
        self.state = state
        # 授权书可用状态，VALID可用，INVALID不可用
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorization_letter_id_list is not None:
            result['AuthorizationLetterIdList'] = self.authorization_letter_id_list
        if self.organization_code is not None:
            result['OrganizationCode'] = self.organization_code
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.sign_name is not None:
            result['SignName'] = self.sign_name
        if self.state is not None:
            result['State'] = self.state
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorizationLetterIdList') is not None:
            self.authorization_letter_id_list = m.get('AuthorizationLetterIdList')
        if m.get('OrganizationCode') is not None:
            self.organization_code = m.get('OrganizationCode')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SignName') is not None:
            self.sign_name = m.get('SignName')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class QuerySmsAuthorizationLetterShrinkRequest(TeaModel):
    def __init__(
        self,
        authorization_letter_id_list_shrink: str = None,
        organization_code: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        sign_name: str = None,
        state: str = None,
        status: str = None,
    ):
        # 委托授权书id列表
        self.authorization_letter_id_list_shrink = authorization_letter_id_list_shrink
        # 授权方社会统一信用代码
        self.organization_code = organization_code
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # 签名名称（支持命中签名范围查询）
        self.sign_name = sign_name
        # 授权书审核状态，INT:审核中，PASSED:审核通过
        self.state = state
        # 授权书可用状态，VALID可用，INVALID不可用
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorization_letter_id_list_shrink is not None:
            result['AuthorizationLetterIdList'] = self.authorization_letter_id_list_shrink
        if self.organization_code is not None:
            result['OrganizationCode'] = self.organization_code
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.sign_name is not None:
            result['SignName'] = self.sign_name
        if self.state is not None:
            result['State'] = self.state
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorizationLetterIdList') is not None:
            self.authorization_letter_id_list_shrink = m.get('AuthorizationLetterIdList')
        if m.get('OrganizationCode') is not None:
            self.organization_code = m.get('OrganizationCode')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SignName') is not None:
            self.sign_name = m.get('SignName')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class QuerySmsAuthorizationLetterResponseBodyData(TeaModel):
    def __init__(
        self,
        authorization: str = None,
        authorization_letter_exp_date: str = None,
        authorization_letter_id: int = None,
        authorization_letter_name: str = None,
        authorization_letter_pic: str = None,
        organization_code: str = None,
        proxy_authorization: str = None,
        sign_scope: str = None,
        state: str = None,
        status: str = None,
    ):
        # 委托授权方
        self.authorization = authorization
        # 委托授权书有效期
        self.authorization_letter_exp_date = authorization_letter_exp_date
        # 委托授权书id
        self.authorization_letter_id = authorization_letter_id
        # 委托授权书命名
        self.authorization_letter_name = authorization_letter_name
        # 委托授权书图片地址
        self.authorization_letter_pic = authorization_letter_pic
        # 授权方统一社会信用代码
        self.organization_code = organization_code
        # 被委托授权方
        self.proxy_authorization = proxy_authorization
        # 委托授权签名范围
        self.sign_scope = sign_scope
        # 委托授权书审核状态（初始化INT/审核通过PASSED）
        self.state = state
        # 委托授权书可用状态（可用VALID/不可用INVALID）
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        if self.authorization_letter_exp_date is not None:
            result['AuthorizationLetterExpDate'] = self.authorization_letter_exp_date
        if self.authorization_letter_id is not None:
            result['AuthorizationLetterId'] = self.authorization_letter_id
        if self.authorization_letter_name is not None:
            result['AuthorizationLetterName'] = self.authorization_letter_name
        if self.authorization_letter_pic is not None:
            result['AuthorizationLetterPic'] = self.authorization_letter_pic
        if self.organization_code is not None:
            result['OrganizationCode'] = self.organization_code
        if self.proxy_authorization is not None:
            result['ProxyAuthorization'] = self.proxy_authorization
        if self.sign_scope is not None:
            result['SignScope'] = self.sign_scope
        if self.state is not None:
            result['State'] = self.state
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        if m.get('AuthorizationLetterExpDate') is not None:
            self.authorization_letter_exp_date = m.get('AuthorizationLetterExpDate')
        if m.get('AuthorizationLetterId') is not None:
            self.authorization_letter_id = m.get('AuthorizationLetterId')
        if m.get('AuthorizationLetterName') is not None:
            self.authorization_letter_name = m.get('AuthorizationLetterName')
        if m.get('AuthorizationLetterPic') is not None:
            self.authorization_letter_pic = m.get('AuthorizationLetterPic')
        if m.get('OrganizationCode') is not None:
            self.organization_code = m.get('OrganizationCode')
        if m.get('ProxyAuthorization') is not None:
            self.proxy_authorization = m.get('ProxyAuthorization')
        if m.get('SignScope') is not None:
            self.sign_scope = m.get('SignScope')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class QuerySmsAuthorizationLetterResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: List[QuerySmsAuthorizationLetterResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.data = data
        self.message = message
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
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
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
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = QuerySmsAuthorizationLetterResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QuerySmsAuthorizationLetterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QuerySmsAuthorizationLetterResponseBody = None,
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
            temp_model = QuerySmsAuthorizationLetterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QuerySmsQualificationRecordRequest(TeaModel):
    def __init__(
        self,
        company_name: str = None,
        legal_person_name: str = None,
        owner_id: int = None,
        page_no: int = None,
        page_size: int = None,
        qualification_group_name: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        state: str = None,
        use_by_self: bool = None,
        work_order_id: int = None,
    ):
        # 公司名
        self.company_name = company_name
        # 法人姓名
        self.legal_person_name = legal_person_name
        self.owner_id = owner_id
        self.page_no = page_no
        self.page_size = page_size
        # 资质组名称
        self.qualification_group_name = qualification_group_name
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # 审核状态。INT:审核中FAILED:审核失败,PASSED:审核通过,NOT_FINISH:资料待补充,CANCELED:已撤回
        self.state = state
        # 是否自用
        self.use_by_self = use_by_self
        # 工单ID
        self.work_order_id = work_order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.company_name is not None:
            result['CompanyName'] = self.company_name
        if self.legal_person_name is not None:
            result['LegalPersonName'] = self.legal_person_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.qualification_group_name is not None:
            result['QualificationGroupName'] = self.qualification_group_name
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.state is not None:
            result['State'] = self.state
        if self.use_by_self is not None:
            result['UseBySelf'] = self.use_by_self
        if self.work_order_id is not None:
            result['WorkOrderId'] = self.work_order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompanyName') is not None:
            self.company_name = m.get('CompanyName')
        if m.get('LegalPersonName') is not None:
            self.legal_person_name = m.get('LegalPersonName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('QualificationGroupName') is not None:
            self.qualification_group_name = m.get('QualificationGroupName')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('UseBySelf') is not None:
            self.use_by_self = m.get('UseBySelf')
        if m.get('WorkOrderId') is not None:
            self.work_order_id = m.get('WorkOrderId')
        return self


class QuerySmsQualificationRecordResponseBodyDataList(TeaModel):
    def __init__(
        self,
        audit_remark: str = None,
        audit_time: str = None,
        company_name: str = None,
        create_date: str = None,
        group_id: int = None,
        legal_person_name: str = None,
        qualification_group_name: str = None,
        state_name: str = None,
        use_by_self: str = None,
        work_order_id: int = None,
    ):
        # 审核备注
        self.audit_remark = audit_remark
        # 审核时间
        self.audit_time = audit_time
        # 公司名称或实人认证姓名
        self.company_name = company_name
        # 创建时间
        self.create_date = create_date
        # 资质组ID
        self.group_id = group_id
        # 法人名称
        self.legal_person_name = legal_person_name
        # 资质组名称
        self.qualification_group_name = qualification_group_name
        # 审核状态名
        self.state_name = state_name
        # 是否自用
        self.use_by_self = use_by_self
        # 工单ID
        self.work_order_id = work_order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audit_remark is not None:
            result['AuditRemark'] = self.audit_remark
        if self.audit_time is not None:
            result['AuditTime'] = self.audit_time
        if self.company_name is not None:
            result['CompanyName'] = self.company_name
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.legal_person_name is not None:
            result['LegalPersonName'] = self.legal_person_name
        if self.qualification_group_name is not None:
            result['QualificationGroupName'] = self.qualification_group_name
        if self.state_name is not None:
            result['StateName'] = self.state_name
        if self.use_by_self is not None:
            result['UseBySelf'] = self.use_by_self
        if self.work_order_id is not None:
            result['WorkOrderId'] = self.work_order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuditRemark') is not None:
            self.audit_remark = m.get('AuditRemark')
        if m.get('AuditTime') is not None:
            self.audit_time = m.get('AuditTime')
        if m.get('CompanyName') is not None:
            self.company_name = m.get('CompanyName')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('LegalPersonName') is not None:
            self.legal_person_name = m.get('LegalPersonName')
        if m.get('QualificationGroupName') is not None:
            self.qualification_group_name = m.get('QualificationGroupName')
        if m.get('StateName') is not None:
            self.state_name = m.get('StateName')
        if m.get('UseBySelf') is not None:
            self.use_by_self = m.get('UseBySelf')
        if m.get('WorkOrderId') is not None:
            self.work_order_id = m.get('WorkOrderId')
        return self


class QuerySmsQualificationRecordResponseBodyData(TeaModel):
    def __init__(
        self,
        list: List[QuerySmsQualificationRecordResponseBodyDataList] = None,
        page_no: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.list = list
        self.page_no = page_no
        self.page_size = page_size
        self.total = total

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
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = QuerySmsQualificationRecordResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class QuerySmsQualificationRecordResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: QuerySmsQualificationRecordResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.data = data
        self.message = message
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
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
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
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = QuerySmsQualificationRecordResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QuerySmsQualificationRecordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QuerySmsQualificationRecordResponseBody = None,
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
            temp_model = QuerySmsQualificationRecordResponseBody()
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
        # The signature.
        # 
        # This parameter is required.
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
        # The response code.
        # 
        # *   If OK is returned, the request is successful.
        # *   Other values indicate that the request fails. For more information, see [Error codes](https://help.aliyun.com/document_detail/101346.html).
        self.code = code
        # The date and time when the signature was created.
        self.create_date = create_date
        # The returned message.
        self.message = message
        # The remarks of the review. Valid values:
        # 
        # *   If the signature is in the **Approved** or **Pending Approval** state, No Remarks is returned.
        # *   If the signature is in the **Not Approved** state, the reason why the signature is rejected is returned.
        self.reason = reason
        # The request ID.
        self.request_id = request_id
        # The signature.
        self.sign_name = sign_name
        # The status of the signature. Valid values:
        # 
        # *   **0**: The signature is pending approval.
        # *   **1**: The signature is approved.
        # *   **2**: The signature is rejected. The Reason parameter indicates the reason why the signature is rejected.
        # *   **10**: The signature is cancelled.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # The page number. Default value: **1**.
        self.page_index = page_index
        # The number of signatures per page. Valid values: **1 to 50**.
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
        # The time when the signature was rejected. Format: yyyy-MM-dd HH:mm:ss.
        self.reject_date = reject_date
        # The reason why the signature was rejected.
        self.reject_info = reject_info
        # The remarks about the rejection.
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
        authorization_letter_id: int = None,
        business_type: str = None,
        create_date: str = None,
        order_id: str = None,
        reason: QuerySmsSignListResponseBodySmsSignListReason = None,
        sign_name: str = None,
        authorization_letter_audit_pass: bool = None,
    ):
        # The approval status of the signature. Valid values:
        # 
        # *   **AUDIT_STATE_INIT**: The signature is pending approval.
        # *   **AUDIT_STATE_PASS**: The signature is approved.
        # *   **AUDIT_STATE_NOT_PASS**: The signature is rejected. You can view the reason in the Reason response parameter.
        # *   **AUDIT_STATE_CANCEL**: The approval is canceled.
        self.audit_status = audit_status
        self.authorization_letter_id = authorization_letter_id
        # The type of the signature scenario. The return value ends with "type". Valid values:
        # 
        # *   Verification code type
        # *   General-purpose type
        self.business_type = business_type
        # The time when the signature was created. Format: yyyy-MM-dd HH:mm:ss.
        self.create_date = create_date
        # The ticket ID.
        self.order_id = order_id
        # The approval remarks.
        # 
        # *   If the value of AuditStatus is **AUDIT_STATE_PASS** or **AUDIT_STATE_INIT**, the value of Reason is No Approval Remarks.
        # *   If the value of AuditStatus is **AUDIT_STATE_NOT_PASS**, the reason why the signature is rejected is returned.
        self.reason = reason
        # The name of the signature.
        self.sign_name = sign_name
        self.authorization_letter_audit_pass = authorization_letter_audit_pass

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
        if self.authorization_letter_id is not None:
            result['AuthorizationLetterId'] = self.authorization_letter_id
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
        if self.authorization_letter_audit_pass is not None:
            result['authorizationLetterAuditPass'] = self.authorization_letter_audit_pass
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuditStatus') is not None:
            self.audit_status = m.get('AuditStatus')
        if m.get('AuthorizationLetterId') is not None:
            self.authorization_letter_id = m.get('AuthorizationLetterId')
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
        if m.get('authorizationLetterAuditPass') is not None:
            self.authorization_letter_audit_pass = m.get('authorizationLetterAuditPass')
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
        # The HTTP status code.
        # 
        # *   The value OK indicates that the request was successful.
        # *   Other values indicate that the request failed. For more information, see [Error codes](https://help.aliyun.com/document_detail/101346.html).
        self.code = code
        # The page number. Default value: **1**.
        self.current_page = current_page
        # The returned message.
        self.message = message
        # The number of signatures per page. Valid values: **1 to 50**.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The queried message signatures.
        self.sms_sign_list = sms_sign_list
        # The total number of signatures.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # The code of the message template.
        # 
        # You can log on to the [Short Message Service (SMS) console](https://dysms.console.aliyun.com/dysms.htm), click **Go China** or **Go Globe** in the left-side navigation pane, and then view the template code on the **Templates** tab. You can also call the [AddSmsTemplate](https://help.aliyun.com/document_detail/121208.html) operation to obtain the template code.
        # 
        # This parameter is required.
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
        # The HTTP status code.
        # 
        # *   The value OK indicates that the request was successful.
        # *   Other values indicate that the request failed. For more information, see [Error codes](https://help.aliyun.com/document_detail/101346.html).
        self.code = code
        # The time when the message template was created.
        self.create_date = create_date
        # The returned message.
        self.message = message
        # The approval remarks.
        # 
        # *   If the value of AuditStatus is **AUDIT_STATE_PASS** or **AUDIT_STATE_INIT**, the value of Reason is No Approval Remarks.
        # *   If the value of AuditStatus is **AUDIT_STATE_NOT_PASS**, the reason why the message template is rejected is returned.
        self.reason = reason
        # The request ID.
        self.request_id = request_id
        # The code of the message template.
        self.template_code = template_code
        # The content of the message template.
        self.template_content = template_content
        # The name of the message template.
        self.template_name = template_name
        # The approval status of the message template. Valid values:
        # 
        # *   **0**: The message template is pending approval.
        # *   **1**: The message template is approved.
        # *   **AUDIT_STATE_NOT_PASS**: The message template is rejected. You can view the reason in the Reason response parameter.
        # *   **10**: The approval is canceled.
        self.template_status = template_status
        # The type of the message. Valid values:
        # 
        # *   **0**: verification code
        # *   **1**: notification message
        # *   **2**: promotional message
        # *   **3**: message sent to countries or regions outside the Chinese mainland
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # The page number. Default value: **1**.
        self.page_index = page_index
        # The number of templates per page. Valid values: **1 to 50**.
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
        # The time when the message template was rejected. Format: yyyy-MM-dd HH:mm:ss.
        self.reject_date = reject_date
        # The reason why the message template was rejected.
        self.reject_info = reject_info
        # The remarks about the rejection.
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
        signature_name: str = None,
        template_code: str = None,
        template_content: str = None,
        template_name: str = None,
        template_type: int = None,
        traffic_driving: str = None,
    ):
        # The approval status of the message template. Valid values:
        # 
        # *   **AUDIT_STATE_INIT**: The message template is pending approval.
        # *   **AUDIT_STATE_PASS**: The message template is approved.
        # *   **AUDIT_STATE_NOT_PASS**: The message template is rejected. You can view the reason in the Reason response parameter.
        # *   **AUDIT_STATE_CANCEL** or **AUDIT_SATE_CANCEL**: The approval is canceled.
        self.audit_status = audit_status
        # The time when the message template was created. The time is in the yyyy-MM-dd HH:mm:ss format.
        self.create_date = create_date
        # The ticket ID.
        self.order_id = order_id
        # The type of the message template. We recommend that you specify this parameter. Valid values:
        # 
        # *   **0**: verification code
        # *   **1**: notification message
        # *   **2**: promotional message
        # *   **3**: message sent to countries or regions outside the Chinese mainland
        # *   **7**: digital message
        # 
        # > The template type is the same as the value of the TemplateType parameter in the AddSmsTemplate and ModifySmsTemplate operations.
        self.outer_template_type = outer_template_type
        # The approval remarks.
        # 
        # *   If the value of AuditStatus is **AUDIT_STATE_PASS** or **AUDIT_STATE_INIT**, the value of Reason is No Approval Remarks.
        # *   If the value of AuditStatus is **AUDIT_STATE_NOT_PASS**, the reason why the message template is rejected is returned.
        self.reason = reason
        self.signature_name = signature_name
        # The code of the message template.
        # 
        # You can log on to the [Short Message Service (SMS) console](https://dysms.console.aliyun.com/dysms.htm), click **Go China** or **Go Globe** in the left-side navigation pane, and then view the template code on the **Templates** tab. You can also call the [AddSmsTemplate](https://help.aliyun.com/document_detail/121208.html) operation to obtain the template code.
        self.template_code = template_code
        # The content of the message template.
        self.template_content = template_content
        # The name of the message template.
        self.template_name = template_name
        # The type of the message template. Valid values:
        # 
        # *   **0**: notification message
        # *   **1**: promotional message
        # *   **2**: verification code
        # *   **6**: message sent to countries or regions outside the Chinese mainland
        # *   **7**: digital message
        self.template_type = template_type
        self.traffic_driving = traffic_driving

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
        if self.signature_name is not None:
            result['SignatureName'] = self.signature_name
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.template_content is not None:
            result['TemplateContent'] = self.template_content
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        if self.traffic_driving is not None:
            result['TrafficDriving'] = self.traffic_driving
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
        if m.get('SignatureName') is not None:
            self.signature_name = m.get('SignatureName')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('TemplateContent') is not None:
            self.template_content = m.get('TemplateContent')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        if m.get('TrafficDriving') is not None:
            self.traffic_driving = m.get('TrafficDriving')
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
        # The HTTP status code.
        # 
        # *   The value OK indicates that the request was successful.
        # *   Other values indicate that the request failed. For more information, see [Error codes](https://help.aliyun.com/document_detail/101346.html).
        self.code = code
        # The page number. Default value: **1**.
        self.current_page = current_page
        # The returned message.
        self.message = message
        # The number of templates per page. Valid values: **1 to 50**.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The queried message templates.
        self.sms_template_list = sms_template_list
        # The total number of templates.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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


class RequiredPhoneCodeRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        phone_no: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.owner_id = owner_id
        # This parameter is required.
        self.phone_no = phone_no
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
        if self.phone_no is not None:
            result['PhoneNo'] = self.phone_no
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PhoneNo') is not None:
            self.phone_no = m.get('PhoneNo')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class RequiredPhoneCodeResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.data = data
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
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RequiredPhoneCodeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RequiredPhoneCodeResponseBody = None,
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
            temp_model = RequiredPhoneCodeResponseBody()
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
        # The code of the message template. You can view the template code in the **Template Code** column on the **Templates** tab of the **Go China** page in the Alibaba Cloud SMS console.
        # 
        # > Make sure that the message template has been approved.
        # 
        # This parameter is required.
        self.card_template_code = card_template_code
        # The variables of the card message template.
        self.card_template_param_json = card_template_param_json
        # The code of the digital message template that applies when the card message is rolled back. You can view the template code in the **Template Code** column on the **Templates** tab of the **Go China** page in the Alibaba Cloud SMS console.
        # 
        # > Make sure that the message template has been approved.
        self.digital_template_code = digital_template_code
        # The variables of the digital message template.
        self.digital_template_param_json = digital_template_param_json
        # The rollback type. Valid values:
        # 
        # *   **SMS**: text message
        # *   **DIGITALSMS**: digital message
        # *   **NONE**: none
        # 
        # This parameter is required.
        self.fallback_type = fallback_type
        # The ID that is reserved for the caller of the operation.
        self.out_id = out_id
        # The mobile numbers of the recipients.
        # 
        # This parameter is required.
        self.phone_number_json = phone_number_json
        # The signature. You can view the template code in the **Signature** column on the **Signaturess** tab of the **Go China** page in the Alibaba Cloud SMS console.
        # 
        # > The signatures must be approved and correspond to the mobile numbers in sequence.
        # 
        # This parameter is required.
        self.sign_name_json = sign_name_json
        # The code of the text message template that applies when the card message is rolled back. You can view the template code in the **Template Code** column on the **Templates** tab of the **Go China** page in the Alibaba Cloud SMS console.
        # 
        # > Make sure that the message template has been approved.
        self.sms_template_code = sms_template_code
        # The variables of the text message template.
        self.sms_template_param_json = sms_template_param_json
        # The extension code of the upstream message.
        self.sms_up_extend_code_json = sms_up_extend_code_json
        # The code of the message template.
        # 
        # You can log on to the [Alibaba Cloud console](https://dysms.console.aliyun.com/dysms.htm?spm=5176.12818093.categories-n-products.ddysms.3b2816d0xml2NA#/overview), click **Go China** or **Go Globe** in the left-side navigation pane, and then view the **template code** on the **Templates** tab.
        # 
        # > You must specify a message template that is created in the SMS console and approved by Alibaba Cloud. If you send messages to countries or regions outside the Chinese mainland, use the corresponding message templates.
        self.template_code = template_code
        # The value of the variable in the message template.
        # 
        # > If you need to add line breaks to the JSON template, make sure that the format is valid. In addition, the sequence of variable values must be the same as that of the mobile numbers and signatures.
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
        # The ID of the card message.
        self.biz_card_id = biz_card_id
        # The ID of the digital message.
        self.biz_digital_id = biz_digital_id
        # The ID of the text message.
        self.biz_sms_id = biz_sms_id
        # The review status of the card message template.
        # 
        # *   **0**: pending approval
        # *   **1**: approved
        # *   **2**: rejected
        # 
        # > Unapproved card messages are rolled back.
        self.card_tmp_state = card_tmp_state
        # The mobile phone number from which the card message is sent.
        self.media_mobiles = media_mobiles
        # The mobile phone number whose card message is rolled back.
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
        # The HTTP status code.
        # 
        # *   The value OK indicates that the request was successful.
        # *   For more information about other response codes, see [API error codes](https://help.aliyun.com/document_detail/101346.html).
        self.code = code
        # The data returned.
        self.data = data
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request is successful. Valid values:
        # 
        # *   **true**\
        # *   **false**\
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # The extension field of the external record. The value is a string that contains no more than 256 characters.
        # 
        # > The parameter is optional.
        self.out_id = out_id
        self.owner_id = owner_id
        # The mobile number of the recipient. Format:
        # 
        # *   Message delivery to the Chinese mainland: +/+86/0086/86 or an 11-digit mobile number without a prefix. Example: 1590000\\*\\*\\*\\*.
        # *   Message delivery to countries or regions outside the Chinese mainland: Dialing code + Mobile number. Example: 852000012\\*\\*\\*\\*.
        # 
        # > We recommend that you call the SendSms operation to send verification codes.
        # 
        # This parameter is required.
        self.phone_number_json = phone_number_json
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The signature.
        # 
        # Log on to the Alibaba Cloud SMS console. In the left-side navigation pane, click **Go Globe** or **Go China**. You can view the signature in the **Signature** column on the **Signatures** tab.
        # 
        # > The signatures must be approved and correspond to the mobile numbers in sequence.
        # 
        # This parameter is required.
        self.sign_name_json = sign_name_json
        # The extension code of the MO message. Format: JSON array.
        # 
        # > The parameter is optional.
        self.sms_up_extend_code_json = sms_up_extend_code_json
        # The code of the message template.
        # 
        # Log on to the Alibaba Cloud SMS console. In the left-side navigation pane, click **Go Globe** or **Go China**. You can view the message template in the **Template Code** column on the **Message Templates** tab.
        # 
        # > The message templates must be created on the Go Globe page and approved.
        # 
        # This parameter is required.
        self.template_code = template_code
        # The value of the variable in the message template.
        # 
        # > If you need to add line breaks to the JSON template, make sure that the format is valid. In addition, the sequence of variable values must be the same as that of the mobile numbers and signatures.
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
        # The ID of the delivery receipt. You can use one of the following methods to query the delivery status of a message based on the ID.
        # 
        # *   Call the [QuerySendDetails](https://help.aliyun.com/document_detail/102352.html) operation.
        # *   Log on to the [Alibaba Cloud SMS console](https://dysms.console.aliyun.com/dysms.htm#/overview). In the left-side navigation pane, choose **Analytics** > **Delivery Report**.
        self.biz_id = biz_id
        # The response code.
        # 
        # *   If OK is returned, the request is successful.
        # *   Other values indicate that the request fails. For more information, see [Error codes](https://help.aliyun.com/document_detail/101346.html).
        self.code = code
        # The returned message.
        self.message = message
        # The request ID.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # The URL to which the message is redirected if the message fails to be rendered.
        self.custom_url = custom_url
        # The variables. Special characters, such as $ and {}, do not need to be entered.
        self.dync_params = dync_params
        # The mobile phone number.
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
        # The objects of the message template.
        # 
        # This parameter is required.
        self.card_objects = card_objects
        # The code of the message template. You can view the template code in the **Template Code** column on the **Templates** tab of the **Go China** page in the Alibaba Cloud SMS console.
        # 
        # > Make sure that the message template has been approved.
        # 
        # This parameter is required.
        self.card_template_code = card_template_code
        # The code of the digital message template that applies when the card message is rolled back. You can view the template code in the **Template Code** column on the **Templates** tab of the **Go China** page in the Alibaba Cloud SMS console.
        # 
        # > Make sure that the message template has been approved.
        self.digital_template_code = digital_template_code
        # The variables of the digital message template.
        # 
        # > If you need to add line breaks to the JSON template, make sure that the format is valid.
        self.digital_template_param = digital_template_param
        # The rollback type. Valid values:
        # 
        # *   **SMS**: text message
        # *   **DIGITALSMS**: digital message
        # *   **NONE**: none
        # 
        # This parameter is required.
        self.fallback_type = fallback_type
        # The ID that is reserved for the caller of the operation.
        self.out_id = out_id
        # The signature. You can view the template code in the **Signature** column on the **Signaturess** tab of the **Go China** page in the Alibaba Cloud SMS console.
        # 
        # > The signature must be approved.
        # 
        # This parameter is required.
        self.sign_name = sign_name
        # The code of the text message template that applies when the card message is rolled back. You can view the template code in the **Template Code** column on the **Templates** tab of the **Go China** page in the Alibaba Cloud SMS console.
        # 
        # > Make sure that the message template has been approved. If you set the **FallbackType** parameter to **SMS**, this parameter is required.
        self.sms_template_code = sms_template_code
        # The variables of the text message template.
        # 
        # > If you need to add line breaks to the JSON template, make sure that the format is valid.
        self.sms_template_param = sms_template_param
        # The extension code of the upstream message. Upstream messages are messages sent to the communication service provider. Upstream messages are used to customize a service, complete an inquiry, or send a request. You are charged for sending upstream messages based on the billing standards of the service provider.
        # 
        # > If you do not need upstream messages, ignore this parameter.
        self.sms_up_extend_code = sms_up_extend_code
        # The code of the text message template.
        # 
        # Log on to the Alibaba Cloud SMS console. In the left-side navigation pane, click **Go Globe** or **Go China**. You can view the message template in the **Template Code** column on the **Message Templates** tab.
        # 
        # > The message templates must be created on the Go Globe page and approved.
        self.template_code = template_code
        # The variables of the message template. Format: JSON.
        # 
        # > If you need to add line breaks to the JSON template, make sure that the format is valid.
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
        # The ID of the card message.
        self.biz_card_id = biz_card_id
        # The ID of the digital message.
        self.biz_digital_id = biz_digital_id
        # The ID of the text message.
        self.biz_sms_id = biz_sms_id
        # The review status of the card message template.
        # 
        # *   **0**: pending approval
        # *   **1**: approved
        # *   **2**: rejected
        # 
        # > Unapproved card messages are rolled back.
        self.card_tmp_state = card_tmp_state
        # The mobile phone number from which the card message is sent.
        self.media_mobiles = media_mobiles
        # The mobile phone number whose card message is rolled back.
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
        # The response code.
        # 
        # *   If OK is returned, the request is successful.
        # *   Other values indicate that the request fails. For more information, see [Error codes](https://help.aliyun.com/document_detail/101346.html).
        self.code = code
        # The data returned.
        self.data = data
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**\
        # *   **false**\
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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


class SendLogisticsSmsRequest(TeaModel):
    def __init__(
        self,
        express_company_code: str = None,
        mail_no: str = None,
        out_id: str = None,
        owner_id: int = None,
        platform_company_code: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        sign_name: str = None,
        template_code: str = None,
        template_param: str = None,
    ):
        # This parameter is required.
        self.express_company_code = express_company_code
        # This parameter is required.
        self.mail_no = mail_no
        self.out_id = out_id
        self.owner_id = owner_id
        self.platform_company_code = platform_company_code
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # This parameter is required.
        self.sign_name = sign_name
        # This parameter is required.
        self.template_code = template_code
        self.template_param = template_param

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.express_company_code is not None:
            result['ExpressCompanyCode'] = self.express_company_code
        if self.mail_no is not None:
            result['MailNo'] = self.mail_no
        if self.out_id is not None:
            result['OutId'] = self.out_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.platform_company_code is not None:
            result['PlatformCompanyCode'] = self.platform_company_code
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.sign_name is not None:
            result['SignName'] = self.sign_name
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.template_param is not None:
            result['TemplateParam'] = self.template_param
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpressCompanyCode') is not None:
            self.express_company_code = m.get('ExpressCompanyCode')
        if m.get('MailNo') is not None:
            self.mail_no = m.get('MailNo')
        if m.get('OutId') is not None:
            self.out_id = m.get('OutId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PlatformCompanyCode') is not None:
            self.platform_company_code = m.get('PlatformCompanyCode')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SignName') is not None:
            self.sign_name = m.get('SignName')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('TemplateParam') is not None:
            self.template_param = m.get('TemplateParam')
        return self


class SendLogisticsSmsResponseBodyData(TeaModel):
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


class SendLogisticsSmsResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: SendLogisticsSmsResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.data = data
        self.message = message
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
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
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
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = SendLogisticsSmsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SendLogisticsSmsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SendLogisticsSmsResponseBody = None,
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
            temp_model = SendLogisticsSmsResponseBody()
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
        # The extension field.
        # 
        # > You can ignore this parameter if you do not have special requirements.
        self.out_id = out_id
        self.owner_id = owner_id
        # The mobile numbers of the recipients. Format:
        # 
        # *   If you send messages to the Chinese mainland, specify mobile numbers that are prefixed with +, +86, 0086, or 86, or 11-digit mobile numbers without prefixes. Example: 1390000\\*\\*\\*\\*.
        # *   If you send messages to countries or regions outside the Chinese mainland, specify this parameter in the \\<Area code>\\<Mobile number> format. Example: 852000012\\*\\*\\*\\*.
        # 
        # You can send messages to multiple mobile numbers, separate the mobile numbers with commas (,). You can specify up to 1,000 mobile numbers in each request. Compared with sending messages to a single mobile number, sending messages to multiple mobile numbers requires longer response time.
        # 
        # > We recommend that you send one verification code message to a mobile number in each request.
        # 
        # This parameter is required.
        self.phone_numbers = phone_numbers
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The signature.
        # 
        # You can log on to the [Short Message Service (SMS) console](https://dysms.console.aliyun.com/dysms.htm?spm=5176.12818093.categories-n-products.ddysms.3b2816d0xml2NA#/overview), click **Go China** or **Go Globe** in the left-side navigation pane, and then view the signature on the **Signatures** tab.
        # 
        # > You must specify a signature that is created in the SMS console and approved by Alibaba Cloud. For more information about SMS signature specifications, see [SMS signature specifications](https://help.aliyun.com/document_detail/108076.html).
        # 
        # This parameter is required.
        self.sign_name = sign_name
        # The extension code of the upstream message. Upstream messages are messages sent to the communication service provider. Upstream messages are used to customize a service, complete an inquiry, or send a request. You are charged for sending upstream messages based on the billing standards of the service provider.
        # 
        # > The extension code is automatically generated by the system when the signature is generated. You do not need to specify the extension code. You can ignore this parameter if you do not have special requirements.
        self.sms_up_extend_code = sms_up_extend_code
        # The code of the message template.
        # 
        # You can log on to the [Short Message Service (SMS) console](https://dysms.console.aliyun.com/dysms.htm?spm=5176.12818093.categories-n-products.ddysms.3b2816d0xml2NA#/overview), click **Go China** or **Go Globe** in the left-side navigation pane, and then view the **template code** on the **Templates** tab.
        # 
        # > You must specify a message template that is created in the SMS console and approved by Alibaba Cloud. If you send messages to countries or regions outside the Chinese mainland, use the corresponding message templates.
        # 
        # This parameter is required.
        self.template_code = template_code
        # The value of the variable in the message template. You can specify multiple parameter values. Example:{"name":"Sam","number":"1390000\\*\\*\\*\\*"}.
        # 
        # > 
        # 
        # *   If line breaks are required in JSON-formatted data, they must meet the relevant requirements that are specified in the standard JSON protocol.
        # 
        # *   For more information about template variables, see [SMS template specifications](https://help.aliyun.com/document_detail/108253.html).
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
        # The ID of the delivery receipt.
        # 
        # You can call the [QuerySendDetails](~~QuerySendDetails~~) operation to query the delivery status based on the receipt ID.
        self.biz_id = biz_id
        # The HTTP status code.
        # 
        # *   The value OK indicates that the request was successful.
        # *   Other values indicate that the request failed. For more information, see [Error codes](https://help.aliyun.com/document_detail/101346.html).
        self.code = code
        # The returned message.
        self.message = message
        # The request ID.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # The time when the OTP message was delivered. The value is a UNIX timestamp. Unit: milliseconds.
        # 
        # *   If you leave the parameter empty, the current timestamp is specified by default.
        # *   If you specify the parameter, the timestamp must be greater than the message sending time and less than the current timestamp.
        self.conversion_time = conversion_time
        # Specifies whether customers replied to the OTP message. Valid values: true and false.
        # 
        # This parameter is required.
        self.delivered = delivered
        # The ID of the message.
        # 
        # This parameter is required.
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
        # The response code. If OK is returned, the request is successful. For more information, see [Error codes](https://help.aliyun.com/document_detail/101346.html?spm=a2c4g.101345.0.0.74326ff2J5EZyt).
        self.code = code
        # The returned message.
        self.message = message
        # The request ID.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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


class SubmitSmsQualificationRequestBusinessLicensePics(TeaModel):
    def __init__(
        self,
        license_pic: str = None,
        type: str = None,
    ):
        # 营业证件图片标识的osskey
        self.license_pic = license_pic
        # 营业证件类型，businessLicense:营业执照;organizationCodeLicense:组织机构代码证;taxRegistrationLicense:税务登记证;socialCreditLicense:社会信用代码证书;newStyleBusinessLicense:三证合一;signLegalLicense:签名归属方的事业单位法人证书;otherLicense:其他类型执照证书
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.license_pic is not None:
            result['LicensePic'] = self.license_pic
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LicensePic') is not None:
            self.license_pic = m.get('LicensePic')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class SubmitSmsQualificationRequestOtherFiles(TeaModel):
    def __init__(
        self,
        license_pic: str = None,
    ):
        self.license_pic = license_pic

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.license_pic is not None:
            result['LicensePic'] = self.license_pic
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LicensePic') is not None:
            self.license_pic = m.get('LicensePic')
        return self


class SubmitSmsQualificationRequest(TeaModel):
    def __init__(
        self,
        admin_idcard_exp_date: str = None,
        admin_idcard_front_face: str = None,
        admin_idcard_no: str = None,
        admin_idcard_pic: str = None,
        admin_idcard_type: str = None,
        admin_name: str = None,
        admin_phone_no: str = None,
        business_license_pics: List[SubmitSmsQualificationRequestBusinessLicensePics] = None,
        bussiness_license_exp_date: str = None,
        certify_code: str = None,
        company_name: str = None,
        company_type: str = None,
        legal_person_idcard_no: str = None,
        legal_person_idcard_type: str = None,
        legal_person_id_card_back_side: str = None,
        legal_person_id_card_eff_time: str = None,
        legal_person_id_card_front_side: str = None,
        legal_person_name: str = None,
        organization_code: str = None,
        other_files: List[SubmitSmsQualificationRequestOtherFiles] = None,
        owner_id: int = None,
        qualification_name: str = None,
        remark: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        use_by_self: bool = None,
        whether_share: bool = None,
    ):
        # 经办人身份证有效期，格式示例2023-01-01~2033-01-01
        # 
        # This parameter is required.
        self.admin_idcard_exp_date = admin_idcard_exp_date
        # 经办人身份证照片国徽面
        # 
        # This parameter is required.
        self.admin_idcard_front_face = admin_idcard_front_face
        # 经办人身份证号码
        # 
        # This parameter is required.
        self.admin_idcard_no = admin_idcard_no
        # 经办人身份证照片人像面
        # 
        # This parameter is required.
        self.admin_idcard_pic = admin_idcard_pic
        # 管理员身份证类型。identityCard:中国居民身份证;passport:护照;homeReturnPermit:港澳居民来往内地通行证;TaiwanCompatriotPermit:台湾居民来往大陆通行证;residencePermit:港澳台居民居住证";other:其他
        # 
        # This parameter is required.
        self.admin_idcard_type = admin_idcard_type
        # 经办人姓名
        # 
        # This parameter is required.
        self.admin_name = admin_name
        # 经办人手机号码
        # 
        # This parameter is required.
        self.admin_phone_no = admin_phone_no
        # 企业营业证件信息，非大客户必填
        self.business_license_pics = business_license_pics
        # 企业营业时间开始和结束字符串，格式示例2023-01-01~2033-01-01
        # 
        # This parameter is required.
        self.bussiness_license_exp_date = bussiness_license_exp_date
        # 手机号验证码
        # 
        # This parameter is required.
        self.certify_code = certify_code
        # 公司名称
        # 
        # This parameter is required.
        self.company_name = company_name
        # 企业类型, COMPANY:公司;NON_PROFIT_ORGANIZATION:政府或者事业单位
        # 
        # This parameter is required.
        self.company_type = company_type
        # 法人身份证号码
        # 
        # This parameter is required.
        self.legal_person_idcard_no = legal_person_idcard_no
        # 法人身份证类型。identityCard:中国居民身份证;passport:护照;homeReturnPermit:港澳居民来往内地通行证;TaiwanCompatriotPermit:台湾居民来往大陆通行证;residencePermit:港澳台居民居住证";other:其他
        # 
        # This parameter is required.
        self.legal_person_idcard_type = legal_person_idcard_type
        # 法人身份证照片人像面
        self.legal_person_id_card_back_side = legal_person_id_card_back_side
        # 法人身份证有效期
        # 
        # This parameter is required.
        self.legal_person_id_card_eff_time = legal_person_id_card_eff_time
        # 法人身份证照片国徽面
        self.legal_person_id_card_front_side = legal_person_id_card_front_side
        # 法人姓名
        # 
        # This parameter is required.
        self.legal_person_name = legal_person_name
        # 社会统一信用代码
        # 
        # This parameter is required.
        self.organization_code = organization_code
        # 更多资料
        self.other_files = other_files
        self.owner_id = owner_id
        # 资质名称,名称不能重复
        # 
        # This parameter is required.
        self.qualification_name = qualification_name
        # 备注
        self.remark = remark
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # 资质是自用还是他用，true：自用，false：他用
        # 
        # This parameter is required.
        self.use_by_self = use_by_self
        # 是否同意与其他业务线共享
        # 
        # This parameter is required.
        self.whether_share = whether_share

    def validate(self):
        if self.business_license_pics:
            for k in self.business_license_pics:
                if k:
                    k.validate()
        if self.other_files:
            for k in self.other_files:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.admin_idcard_exp_date is not None:
            result['AdminIDCardExpDate'] = self.admin_idcard_exp_date
        if self.admin_idcard_front_face is not None:
            result['AdminIDCardFrontFace'] = self.admin_idcard_front_face
        if self.admin_idcard_no is not None:
            result['AdminIDCardNo'] = self.admin_idcard_no
        if self.admin_idcard_pic is not None:
            result['AdminIDCardPic'] = self.admin_idcard_pic
        if self.admin_idcard_type is not None:
            result['AdminIDCardType'] = self.admin_idcard_type
        if self.admin_name is not None:
            result['AdminName'] = self.admin_name
        if self.admin_phone_no is not None:
            result['AdminPhoneNo'] = self.admin_phone_no
        result['BusinessLicensePics'] = []
        if self.business_license_pics is not None:
            for k in self.business_license_pics:
                result['BusinessLicensePics'].append(k.to_map() if k else None)
        if self.bussiness_license_exp_date is not None:
            result['BussinessLicenseExpDate'] = self.bussiness_license_exp_date
        if self.certify_code is not None:
            result['CertifyCode'] = self.certify_code
        if self.company_name is not None:
            result['CompanyName'] = self.company_name
        if self.company_type is not None:
            result['CompanyType'] = self.company_type
        if self.legal_person_idcard_no is not None:
            result['LegalPersonIDCardNo'] = self.legal_person_idcard_no
        if self.legal_person_idcard_type is not None:
            result['LegalPersonIDCardType'] = self.legal_person_idcard_type
        if self.legal_person_id_card_back_side is not None:
            result['LegalPersonIdCardBackSide'] = self.legal_person_id_card_back_side
        if self.legal_person_id_card_eff_time is not None:
            result['LegalPersonIdCardEffTime'] = self.legal_person_id_card_eff_time
        if self.legal_person_id_card_front_side is not None:
            result['LegalPersonIdCardFrontSide'] = self.legal_person_id_card_front_side
        if self.legal_person_name is not None:
            result['LegalPersonName'] = self.legal_person_name
        if self.organization_code is not None:
            result['OrganizationCode'] = self.organization_code
        result['OtherFiles'] = []
        if self.other_files is not None:
            for k in self.other_files:
                result['OtherFiles'].append(k.to_map() if k else None)
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.qualification_name is not None:
            result['QualificationName'] = self.qualification_name
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.use_by_self is not None:
            result['UseBySelf'] = self.use_by_self
        if self.whether_share is not None:
            result['WhetherShare'] = self.whether_share
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdminIDCardExpDate') is not None:
            self.admin_idcard_exp_date = m.get('AdminIDCardExpDate')
        if m.get('AdminIDCardFrontFace') is not None:
            self.admin_idcard_front_face = m.get('AdminIDCardFrontFace')
        if m.get('AdminIDCardNo') is not None:
            self.admin_idcard_no = m.get('AdminIDCardNo')
        if m.get('AdminIDCardPic') is not None:
            self.admin_idcard_pic = m.get('AdminIDCardPic')
        if m.get('AdminIDCardType') is not None:
            self.admin_idcard_type = m.get('AdminIDCardType')
        if m.get('AdminName') is not None:
            self.admin_name = m.get('AdminName')
        if m.get('AdminPhoneNo') is not None:
            self.admin_phone_no = m.get('AdminPhoneNo')
        self.business_license_pics = []
        if m.get('BusinessLicensePics') is not None:
            for k in m.get('BusinessLicensePics'):
                temp_model = SubmitSmsQualificationRequestBusinessLicensePics()
                self.business_license_pics.append(temp_model.from_map(k))
        if m.get('BussinessLicenseExpDate') is not None:
            self.bussiness_license_exp_date = m.get('BussinessLicenseExpDate')
        if m.get('CertifyCode') is not None:
            self.certify_code = m.get('CertifyCode')
        if m.get('CompanyName') is not None:
            self.company_name = m.get('CompanyName')
        if m.get('CompanyType') is not None:
            self.company_type = m.get('CompanyType')
        if m.get('LegalPersonIDCardNo') is not None:
            self.legal_person_idcard_no = m.get('LegalPersonIDCardNo')
        if m.get('LegalPersonIDCardType') is not None:
            self.legal_person_idcard_type = m.get('LegalPersonIDCardType')
        if m.get('LegalPersonIdCardBackSide') is not None:
            self.legal_person_id_card_back_side = m.get('LegalPersonIdCardBackSide')
        if m.get('LegalPersonIdCardEffTime') is not None:
            self.legal_person_id_card_eff_time = m.get('LegalPersonIdCardEffTime')
        if m.get('LegalPersonIdCardFrontSide') is not None:
            self.legal_person_id_card_front_side = m.get('LegalPersonIdCardFrontSide')
        if m.get('LegalPersonName') is not None:
            self.legal_person_name = m.get('LegalPersonName')
        if m.get('OrganizationCode') is not None:
            self.organization_code = m.get('OrganizationCode')
        self.other_files = []
        if m.get('OtherFiles') is not None:
            for k in m.get('OtherFiles'):
                temp_model = SubmitSmsQualificationRequestOtherFiles()
                self.other_files.append(temp_model.from_map(k))
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('QualificationName') is not None:
            self.qualification_name = m.get('QualificationName')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('UseBySelf') is not None:
            self.use_by_self = m.get('UseBySelf')
        if m.get('WhetherShare') is not None:
            self.whether_share = m.get('WhetherShare')
        return self


class SubmitSmsQualificationShrinkRequest(TeaModel):
    def __init__(
        self,
        admin_idcard_exp_date: str = None,
        admin_idcard_front_face: str = None,
        admin_idcard_no: str = None,
        admin_idcard_pic: str = None,
        admin_idcard_type: str = None,
        admin_name: str = None,
        admin_phone_no: str = None,
        business_license_pics_shrink: str = None,
        bussiness_license_exp_date: str = None,
        certify_code: str = None,
        company_name: str = None,
        company_type: str = None,
        legal_person_idcard_no: str = None,
        legal_person_idcard_type: str = None,
        legal_person_id_card_back_side: str = None,
        legal_person_id_card_eff_time: str = None,
        legal_person_id_card_front_side: str = None,
        legal_person_name: str = None,
        organization_code: str = None,
        other_files_shrink: str = None,
        owner_id: int = None,
        qualification_name: str = None,
        remark: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        use_by_self: bool = None,
        whether_share: bool = None,
    ):
        # 经办人身份证有效期，格式示例2023-01-01~2033-01-01
        # 
        # This parameter is required.
        self.admin_idcard_exp_date = admin_idcard_exp_date
        # 经办人身份证照片国徽面
        # 
        # This parameter is required.
        self.admin_idcard_front_face = admin_idcard_front_face
        # 经办人身份证号码
        # 
        # This parameter is required.
        self.admin_idcard_no = admin_idcard_no
        # 经办人身份证照片人像面
        # 
        # This parameter is required.
        self.admin_idcard_pic = admin_idcard_pic
        # 管理员身份证类型。identityCard:中国居民身份证;passport:护照;homeReturnPermit:港澳居民来往内地通行证;TaiwanCompatriotPermit:台湾居民来往大陆通行证;residencePermit:港澳台居民居住证";other:其他
        # 
        # This parameter is required.
        self.admin_idcard_type = admin_idcard_type
        # 经办人姓名
        # 
        # This parameter is required.
        self.admin_name = admin_name
        # 经办人手机号码
        # 
        # This parameter is required.
        self.admin_phone_no = admin_phone_no
        # 企业营业证件信息，非大客户必填
        self.business_license_pics_shrink = business_license_pics_shrink
        # 企业营业时间开始和结束字符串，格式示例2023-01-01~2033-01-01
        # 
        # This parameter is required.
        self.bussiness_license_exp_date = bussiness_license_exp_date
        # 手机号验证码
        # 
        # This parameter is required.
        self.certify_code = certify_code
        # 公司名称
        # 
        # This parameter is required.
        self.company_name = company_name
        # 企业类型, COMPANY:公司;NON_PROFIT_ORGANIZATION:政府或者事业单位
        # 
        # This parameter is required.
        self.company_type = company_type
        # 法人身份证号码
        # 
        # This parameter is required.
        self.legal_person_idcard_no = legal_person_idcard_no
        # 法人身份证类型。identityCard:中国居民身份证;passport:护照;homeReturnPermit:港澳居民来往内地通行证;TaiwanCompatriotPermit:台湾居民来往大陆通行证;residencePermit:港澳台居民居住证";other:其他
        # 
        # This parameter is required.
        self.legal_person_idcard_type = legal_person_idcard_type
        # 法人身份证照片人像面
        self.legal_person_id_card_back_side = legal_person_id_card_back_side
        # 法人身份证有效期
        # 
        # This parameter is required.
        self.legal_person_id_card_eff_time = legal_person_id_card_eff_time
        # 法人身份证照片国徽面
        self.legal_person_id_card_front_side = legal_person_id_card_front_side
        # 法人姓名
        # 
        # This parameter is required.
        self.legal_person_name = legal_person_name
        # 社会统一信用代码
        # 
        # This parameter is required.
        self.organization_code = organization_code
        # 更多资料
        self.other_files_shrink = other_files_shrink
        self.owner_id = owner_id
        # 资质名称,名称不能重复
        # 
        # This parameter is required.
        self.qualification_name = qualification_name
        # 备注
        self.remark = remark
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # 资质是自用还是他用，true：自用，false：他用
        # 
        # This parameter is required.
        self.use_by_self = use_by_self
        # 是否同意与其他业务线共享
        # 
        # This parameter is required.
        self.whether_share = whether_share

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.admin_idcard_exp_date is not None:
            result['AdminIDCardExpDate'] = self.admin_idcard_exp_date
        if self.admin_idcard_front_face is not None:
            result['AdminIDCardFrontFace'] = self.admin_idcard_front_face
        if self.admin_idcard_no is not None:
            result['AdminIDCardNo'] = self.admin_idcard_no
        if self.admin_idcard_pic is not None:
            result['AdminIDCardPic'] = self.admin_idcard_pic
        if self.admin_idcard_type is not None:
            result['AdminIDCardType'] = self.admin_idcard_type
        if self.admin_name is not None:
            result['AdminName'] = self.admin_name
        if self.admin_phone_no is not None:
            result['AdminPhoneNo'] = self.admin_phone_no
        if self.business_license_pics_shrink is not None:
            result['BusinessLicensePics'] = self.business_license_pics_shrink
        if self.bussiness_license_exp_date is not None:
            result['BussinessLicenseExpDate'] = self.bussiness_license_exp_date
        if self.certify_code is not None:
            result['CertifyCode'] = self.certify_code
        if self.company_name is not None:
            result['CompanyName'] = self.company_name
        if self.company_type is not None:
            result['CompanyType'] = self.company_type
        if self.legal_person_idcard_no is not None:
            result['LegalPersonIDCardNo'] = self.legal_person_idcard_no
        if self.legal_person_idcard_type is not None:
            result['LegalPersonIDCardType'] = self.legal_person_idcard_type
        if self.legal_person_id_card_back_side is not None:
            result['LegalPersonIdCardBackSide'] = self.legal_person_id_card_back_side
        if self.legal_person_id_card_eff_time is not None:
            result['LegalPersonIdCardEffTime'] = self.legal_person_id_card_eff_time
        if self.legal_person_id_card_front_side is not None:
            result['LegalPersonIdCardFrontSide'] = self.legal_person_id_card_front_side
        if self.legal_person_name is not None:
            result['LegalPersonName'] = self.legal_person_name
        if self.organization_code is not None:
            result['OrganizationCode'] = self.organization_code
        if self.other_files_shrink is not None:
            result['OtherFiles'] = self.other_files_shrink
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.qualification_name is not None:
            result['QualificationName'] = self.qualification_name
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.use_by_self is not None:
            result['UseBySelf'] = self.use_by_self
        if self.whether_share is not None:
            result['WhetherShare'] = self.whether_share
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdminIDCardExpDate') is not None:
            self.admin_idcard_exp_date = m.get('AdminIDCardExpDate')
        if m.get('AdminIDCardFrontFace') is not None:
            self.admin_idcard_front_face = m.get('AdminIDCardFrontFace')
        if m.get('AdminIDCardNo') is not None:
            self.admin_idcard_no = m.get('AdminIDCardNo')
        if m.get('AdminIDCardPic') is not None:
            self.admin_idcard_pic = m.get('AdminIDCardPic')
        if m.get('AdminIDCardType') is not None:
            self.admin_idcard_type = m.get('AdminIDCardType')
        if m.get('AdminName') is not None:
            self.admin_name = m.get('AdminName')
        if m.get('AdminPhoneNo') is not None:
            self.admin_phone_no = m.get('AdminPhoneNo')
        if m.get('BusinessLicensePics') is not None:
            self.business_license_pics_shrink = m.get('BusinessLicensePics')
        if m.get('BussinessLicenseExpDate') is not None:
            self.bussiness_license_exp_date = m.get('BussinessLicenseExpDate')
        if m.get('CertifyCode') is not None:
            self.certify_code = m.get('CertifyCode')
        if m.get('CompanyName') is not None:
            self.company_name = m.get('CompanyName')
        if m.get('CompanyType') is not None:
            self.company_type = m.get('CompanyType')
        if m.get('LegalPersonIDCardNo') is not None:
            self.legal_person_idcard_no = m.get('LegalPersonIDCardNo')
        if m.get('LegalPersonIDCardType') is not None:
            self.legal_person_idcard_type = m.get('LegalPersonIDCardType')
        if m.get('LegalPersonIdCardBackSide') is not None:
            self.legal_person_id_card_back_side = m.get('LegalPersonIdCardBackSide')
        if m.get('LegalPersonIdCardEffTime') is not None:
            self.legal_person_id_card_eff_time = m.get('LegalPersonIdCardEffTime')
        if m.get('LegalPersonIdCardFrontSide') is not None:
            self.legal_person_id_card_front_side = m.get('LegalPersonIdCardFrontSide')
        if m.get('LegalPersonName') is not None:
            self.legal_person_name = m.get('LegalPersonName')
        if m.get('OrganizationCode') is not None:
            self.organization_code = m.get('OrganizationCode')
        if m.get('OtherFiles') is not None:
            self.other_files_shrink = m.get('OtherFiles')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('QualificationName') is not None:
            self.qualification_name = m.get('QualificationName')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('UseBySelf') is not None:
            self.use_by_self = m.get('UseBySelf')
        if m.get('WhetherShare') is not None:
            self.whether_share = m.get('WhetherShare')
        return self


class SubmitSmsQualificationResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.data = data
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
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SubmitSmsQualificationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SubmitSmsQualificationResponseBody = None,
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
            temp_model = SubmitSmsQualificationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TagResourcesRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The array of tag keys. Valid values of N: 1 to 20.
        self.key = key
        # The array of tag values. Valid values of N: 1 to 20.
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
        # The name of the cloud service. Set the value to **dysms**.
        self.prod_code = prod_code
        # The region ID. Set the value to **cn-hangzhou**.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The code of the message template.
        self.resource_id = resource_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The type of the resource. Set the value to **TEMPLATE**.
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The tag.
        # 
        # This parameter is required.
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
        # The response code.
        # 
        # *   If OK is returned, the request is successful.
        # *   Other values indicate that the request fails. For more information, see [Error codes](https://help.aliyun.com/document_detail/101346.html).
        self.code = code
        # Indicates whether tags were attached. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.data = data
        # The request ID.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # Specifies whether to delete all tags from the message template. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.all = all
        self.owner_id = owner_id
        # The name of the cloud service. Set the value to **dysms**.
        self.prod_code = prod_code
        # The region. Set the value to cn-hangzhou.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The array of message template codes. You can specify 1 to 20 message templates.
        self.resource_id = resource_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The type of the resource. Set the value to TEMPLATE.
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The array of tag keys. You can specify 1 to 20 tag keys.
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
        # The HTTP status code.
        # 
        # *   The value OK indicates that the request was successful.
        # *   Other values indicate that the request failed. For more information, see [Error codes](https://help.aliyun.com/document_detail/101346.html).
        self.code = code
        # Indicates whether the request is successful. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.data = data
        # The request ID.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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


class UpdateExtCodeSignRequest(TeaModel):
    def __init__(
        self,
        exist_ext_code: str = None,
        new_ext_code: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        sign_name: str = None,
    ):
        # 要修改的扩展码A3
        # 
        # This parameter is required.
        self.exist_ext_code = exist_ext_code
        # 修改后的扩展码A3
        # 
        # This parameter is required.
        self.new_ext_code = new_ext_code
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # 签名
        # 
        # This parameter is required.
        self.sign_name = sign_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exist_ext_code is not None:
            result['ExistExtCode'] = self.exist_ext_code
        if self.new_ext_code is not None:
            result['NewExtCode'] = self.new_ext_code
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
        if m.get('ExistExtCode') is not None:
            self.exist_ext_code = m.get('ExistExtCode')
        if m.get('NewExtCode') is not None:
            self.new_ext_code = m.get('NewExtCode')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SignName') is not None:
            self.sign_name = m.get('SignName')
        return self


class UpdateExtCodeSignResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: bool = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.data = data
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
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateExtCodeSignResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateExtCodeSignResponseBody = None,
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
            temp_model = UpdateExtCodeSignResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateSmsQualificationRequestBusinessLicensePics(TeaModel):
    def __init__(
        self,
        license_pic: str = None,
        type: str = None,
    ):
        # 证件图片标识的osskey
        self.license_pic = license_pic
        # 企业证件类型，businessLicense:营业执照;organizationCodeLicense:组织机构代码证;taxRegistrationLicense:税务登记证;socialCreditLicense:社会信用代码证书;newStyleBusinessLicense:三证合一;signLegalLicense:签名归属方的事业单位法人证书;otherLicense:其他类型执照证书
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.license_pic is not None:
            result['LicensePic'] = self.license_pic
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LicensePic') is not None:
            self.license_pic = m.get('LicensePic')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class UpdateSmsQualificationRequestOtherFiles(TeaModel):
    def __init__(
        self,
        license_pic: str = None,
    ):
        self.license_pic = license_pic

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.license_pic is not None:
            result['LicensePic'] = self.license_pic
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LicensePic') is not None:
            self.license_pic = m.get('LicensePic')
        return self


class UpdateSmsQualificationRequest(TeaModel):
    def __init__(
        self,
        admin_idcard_exp_date: str = None,
        admin_idcard_front_face: str = None,
        admin_idcard_no: str = None,
        admin_idcard_pic: str = None,
        admin_idcard_type: str = None,
        admin_name: str = None,
        admin_phone_no: str = None,
        business_license_pics: List[UpdateSmsQualificationRequestBusinessLicensePics] = None,
        bussiness_license_exp_date: str = None,
        certify_code: str = None,
        company_name: str = None,
        legal_person_idcard_no: str = None,
        legal_person_idcard_type: str = None,
        legal_person_id_card_back_side: str = None,
        legal_person_id_card_eff_time: str = None,
        legal_person_id_card_front_side: str = None,
        legal_person_name: str = None,
        order_id: int = None,
        other_files: List[UpdateSmsQualificationRequestOtherFiles] = None,
        owner_id: int = None,
        qualification_group_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # 经办人身份证有效期，格式示例2023-01-01~2033-01-01
        self.admin_idcard_exp_date = admin_idcard_exp_date
        # 经办人身份证照片国徽面
        self.admin_idcard_front_face = admin_idcard_front_face
        # 经办人身份证号码
        self.admin_idcard_no = admin_idcard_no
        # 经办人身份证照片人像面
        self.admin_idcard_pic = admin_idcard_pic
        # 管理员身份证类型。identityCard:中国居民身份证;passport:护照;homeReturnPermit:港澳居民来往内地通行证;TaiwanCompatriotPermit:台湾居民来往大陆通行证;residencePermit:港澳台居民居住证";other:其他
        self.admin_idcard_type = admin_idcard_type
        # 经办人姓名
        self.admin_name = admin_name
        # 经办人手机号码
        # 
        # This parameter is required.
        self.admin_phone_no = admin_phone_no
        # 企业证件信息
        self.business_license_pics = business_license_pics
        # 企业营业时间开始和结束字符串，格式示例2023-01-01~2033-01-01
        self.bussiness_license_exp_date = bussiness_license_exp_date
        # 手机号验证码
        # 
        # This parameter is required.
        self.certify_code = certify_code
        # 公司名称
        self.company_name = company_name
        # 法人身份证号码
        self.legal_person_idcard_no = legal_person_idcard_no
        # 法人身份证类型。identityCard:中国居民身份证;passport:护照;homeReturnPermit:港澳居民来往内地通行证;TaiwanCompatriotPermit:台湾居民来往大陆通行证;residencePermit:港澳台居民居住证";other:其他
        self.legal_person_idcard_type = legal_person_idcard_type
        # 法人身份证照片人像面
        self.legal_person_id_card_back_side = legal_person_id_card_back_side
        # 法人身份证有效期，格式示例2023-01-01~2033-01-01
        self.legal_person_id_card_eff_time = legal_person_id_card_eff_time
        # 法人身份照片证国徽面
        self.legal_person_id_card_front_side = legal_person_id_card_front_side
        # 法人姓名
        self.legal_person_name = legal_person_name
        # 工单ID
        # 
        # This parameter is required.
        self.order_id = order_id
        # 更多资料
        self.other_files = other_files
        self.owner_id = owner_id
        # 资质组ID
        # 
        # This parameter is required.
        self.qualification_group_id = qualification_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        if self.business_license_pics:
            for k in self.business_license_pics:
                if k:
                    k.validate()
        if self.other_files:
            for k in self.other_files:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.admin_idcard_exp_date is not None:
            result['AdminIDCardExpDate'] = self.admin_idcard_exp_date
        if self.admin_idcard_front_face is not None:
            result['AdminIDCardFrontFace'] = self.admin_idcard_front_face
        if self.admin_idcard_no is not None:
            result['AdminIDCardNo'] = self.admin_idcard_no
        if self.admin_idcard_pic is not None:
            result['AdminIDCardPic'] = self.admin_idcard_pic
        if self.admin_idcard_type is not None:
            result['AdminIDCardType'] = self.admin_idcard_type
        if self.admin_name is not None:
            result['AdminName'] = self.admin_name
        if self.admin_phone_no is not None:
            result['AdminPhoneNo'] = self.admin_phone_no
        result['BusinessLicensePics'] = []
        if self.business_license_pics is not None:
            for k in self.business_license_pics:
                result['BusinessLicensePics'].append(k.to_map() if k else None)
        if self.bussiness_license_exp_date is not None:
            result['BussinessLicenseExpDate'] = self.bussiness_license_exp_date
        if self.certify_code is not None:
            result['CertifyCode'] = self.certify_code
        if self.company_name is not None:
            result['CompanyName'] = self.company_name
        if self.legal_person_idcard_no is not None:
            result['LegalPersonIDCardNo'] = self.legal_person_idcard_no
        if self.legal_person_idcard_type is not None:
            result['LegalPersonIDCardType'] = self.legal_person_idcard_type
        if self.legal_person_id_card_back_side is not None:
            result['LegalPersonIdCardBackSide'] = self.legal_person_id_card_back_side
        if self.legal_person_id_card_eff_time is not None:
            result['LegalPersonIdCardEffTime'] = self.legal_person_id_card_eff_time
        if self.legal_person_id_card_front_side is not None:
            result['LegalPersonIdCardFrontSide'] = self.legal_person_id_card_front_side
        if self.legal_person_name is not None:
            result['LegalPersonName'] = self.legal_person_name
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        result['OtherFiles'] = []
        if self.other_files is not None:
            for k in self.other_files:
                result['OtherFiles'].append(k.to_map() if k else None)
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.qualification_group_id is not None:
            result['QualificationGroupId'] = self.qualification_group_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdminIDCardExpDate') is not None:
            self.admin_idcard_exp_date = m.get('AdminIDCardExpDate')
        if m.get('AdminIDCardFrontFace') is not None:
            self.admin_idcard_front_face = m.get('AdminIDCardFrontFace')
        if m.get('AdminIDCardNo') is not None:
            self.admin_idcard_no = m.get('AdminIDCardNo')
        if m.get('AdminIDCardPic') is not None:
            self.admin_idcard_pic = m.get('AdminIDCardPic')
        if m.get('AdminIDCardType') is not None:
            self.admin_idcard_type = m.get('AdminIDCardType')
        if m.get('AdminName') is not None:
            self.admin_name = m.get('AdminName')
        if m.get('AdminPhoneNo') is not None:
            self.admin_phone_no = m.get('AdminPhoneNo')
        self.business_license_pics = []
        if m.get('BusinessLicensePics') is not None:
            for k in m.get('BusinessLicensePics'):
                temp_model = UpdateSmsQualificationRequestBusinessLicensePics()
                self.business_license_pics.append(temp_model.from_map(k))
        if m.get('BussinessLicenseExpDate') is not None:
            self.bussiness_license_exp_date = m.get('BussinessLicenseExpDate')
        if m.get('CertifyCode') is not None:
            self.certify_code = m.get('CertifyCode')
        if m.get('CompanyName') is not None:
            self.company_name = m.get('CompanyName')
        if m.get('LegalPersonIDCardNo') is not None:
            self.legal_person_idcard_no = m.get('LegalPersonIDCardNo')
        if m.get('LegalPersonIDCardType') is not None:
            self.legal_person_idcard_type = m.get('LegalPersonIDCardType')
        if m.get('LegalPersonIdCardBackSide') is not None:
            self.legal_person_id_card_back_side = m.get('LegalPersonIdCardBackSide')
        if m.get('LegalPersonIdCardEffTime') is not None:
            self.legal_person_id_card_eff_time = m.get('LegalPersonIdCardEffTime')
        if m.get('LegalPersonIdCardFrontSide') is not None:
            self.legal_person_id_card_front_side = m.get('LegalPersonIdCardFrontSide')
        if m.get('LegalPersonName') is not None:
            self.legal_person_name = m.get('LegalPersonName')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        self.other_files = []
        if m.get('OtherFiles') is not None:
            for k in m.get('OtherFiles'):
                temp_model = UpdateSmsQualificationRequestOtherFiles()
                self.other_files.append(temp_model.from_map(k))
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('QualificationGroupId') is not None:
            self.qualification_group_id = m.get('QualificationGroupId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class UpdateSmsQualificationShrinkRequest(TeaModel):
    def __init__(
        self,
        admin_idcard_exp_date: str = None,
        admin_idcard_front_face: str = None,
        admin_idcard_no: str = None,
        admin_idcard_pic: str = None,
        admin_idcard_type: str = None,
        admin_name: str = None,
        admin_phone_no: str = None,
        business_license_pics_shrink: str = None,
        bussiness_license_exp_date: str = None,
        certify_code: str = None,
        company_name: str = None,
        legal_person_idcard_no: str = None,
        legal_person_idcard_type: str = None,
        legal_person_id_card_back_side: str = None,
        legal_person_id_card_eff_time: str = None,
        legal_person_id_card_front_side: str = None,
        legal_person_name: str = None,
        order_id: int = None,
        other_files_shrink: str = None,
        owner_id: int = None,
        qualification_group_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # 经办人身份证有效期，格式示例2023-01-01~2033-01-01
        self.admin_idcard_exp_date = admin_idcard_exp_date
        # 经办人身份证照片国徽面
        self.admin_idcard_front_face = admin_idcard_front_face
        # 经办人身份证号码
        self.admin_idcard_no = admin_idcard_no
        # 经办人身份证照片人像面
        self.admin_idcard_pic = admin_idcard_pic
        # 管理员身份证类型。identityCard:中国居民身份证;passport:护照;homeReturnPermit:港澳居民来往内地通行证;TaiwanCompatriotPermit:台湾居民来往大陆通行证;residencePermit:港澳台居民居住证";other:其他
        self.admin_idcard_type = admin_idcard_type
        # 经办人姓名
        self.admin_name = admin_name
        # 经办人手机号码
        # 
        # This parameter is required.
        self.admin_phone_no = admin_phone_no
        # 企业证件信息
        self.business_license_pics_shrink = business_license_pics_shrink
        # 企业营业时间开始和结束字符串，格式示例2023-01-01~2033-01-01
        self.bussiness_license_exp_date = bussiness_license_exp_date
        # 手机号验证码
        # 
        # This parameter is required.
        self.certify_code = certify_code
        # 公司名称
        self.company_name = company_name
        # 法人身份证号码
        self.legal_person_idcard_no = legal_person_idcard_no
        # 法人身份证类型。identityCard:中国居民身份证;passport:护照;homeReturnPermit:港澳居民来往内地通行证;TaiwanCompatriotPermit:台湾居民来往大陆通行证;residencePermit:港澳台居民居住证";other:其他
        self.legal_person_idcard_type = legal_person_idcard_type
        # 法人身份证照片人像面
        self.legal_person_id_card_back_side = legal_person_id_card_back_side
        # 法人身份证有效期，格式示例2023-01-01~2033-01-01
        self.legal_person_id_card_eff_time = legal_person_id_card_eff_time
        # 法人身份照片证国徽面
        self.legal_person_id_card_front_side = legal_person_id_card_front_side
        # 法人姓名
        self.legal_person_name = legal_person_name
        # 工单ID
        # 
        # This parameter is required.
        self.order_id = order_id
        # 更多资料
        self.other_files_shrink = other_files_shrink
        self.owner_id = owner_id
        # 资质组ID
        # 
        # This parameter is required.
        self.qualification_group_id = qualification_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.admin_idcard_exp_date is not None:
            result['AdminIDCardExpDate'] = self.admin_idcard_exp_date
        if self.admin_idcard_front_face is not None:
            result['AdminIDCardFrontFace'] = self.admin_idcard_front_face
        if self.admin_idcard_no is not None:
            result['AdminIDCardNo'] = self.admin_idcard_no
        if self.admin_idcard_pic is not None:
            result['AdminIDCardPic'] = self.admin_idcard_pic
        if self.admin_idcard_type is not None:
            result['AdminIDCardType'] = self.admin_idcard_type
        if self.admin_name is not None:
            result['AdminName'] = self.admin_name
        if self.admin_phone_no is not None:
            result['AdminPhoneNo'] = self.admin_phone_no
        if self.business_license_pics_shrink is not None:
            result['BusinessLicensePics'] = self.business_license_pics_shrink
        if self.bussiness_license_exp_date is not None:
            result['BussinessLicenseExpDate'] = self.bussiness_license_exp_date
        if self.certify_code is not None:
            result['CertifyCode'] = self.certify_code
        if self.company_name is not None:
            result['CompanyName'] = self.company_name
        if self.legal_person_idcard_no is not None:
            result['LegalPersonIDCardNo'] = self.legal_person_idcard_no
        if self.legal_person_idcard_type is not None:
            result['LegalPersonIDCardType'] = self.legal_person_idcard_type
        if self.legal_person_id_card_back_side is not None:
            result['LegalPersonIdCardBackSide'] = self.legal_person_id_card_back_side
        if self.legal_person_id_card_eff_time is not None:
            result['LegalPersonIdCardEffTime'] = self.legal_person_id_card_eff_time
        if self.legal_person_id_card_front_side is not None:
            result['LegalPersonIdCardFrontSide'] = self.legal_person_id_card_front_side
        if self.legal_person_name is not None:
            result['LegalPersonName'] = self.legal_person_name
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.other_files_shrink is not None:
            result['OtherFiles'] = self.other_files_shrink
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.qualification_group_id is not None:
            result['QualificationGroupId'] = self.qualification_group_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdminIDCardExpDate') is not None:
            self.admin_idcard_exp_date = m.get('AdminIDCardExpDate')
        if m.get('AdminIDCardFrontFace') is not None:
            self.admin_idcard_front_face = m.get('AdminIDCardFrontFace')
        if m.get('AdminIDCardNo') is not None:
            self.admin_idcard_no = m.get('AdminIDCardNo')
        if m.get('AdminIDCardPic') is not None:
            self.admin_idcard_pic = m.get('AdminIDCardPic')
        if m.get('AdminIDCardType') is not None:
            self.admin_idcard_type = m.get('AdminIDCardType')
        if m.get('AdminName') is not None:
            self.admin_name = m.get('AdminName')
        if m.get('AdminPhoneNo') is not None:
            self.admin_phone_no = m.get('AdminPhoneNo')
        if m.get('BusinessLicensePics') is not None:
            self.business_license_pics_shrink = m.get('BusinessLicensePics')
        if m.get('BussinessLicenseExpDate') is not None:
            self.bussiness_license_exp_date = m.get('BussinessLicenseExpDate')
        if m.get('CertifyCode') is not None:
            self.certify_code = m.get('CertifyCode')
        if m.get('CompanyName') is not None:
            self.company_name = m.get('CompanyName')
        if m.get('LegalPersonIDCardNo') is not None:
            self.legal_person_idcard_no = m.get('LegalPersonIDCardNo')
        if m.get('LegalPersonIDCardType') is not None:
            self.legal_person_idcard_type = m.get('LegalPersonIDCardType')
        if m.get('LegalPersonIdCardBackSide') is not None:
            self.legal_person_id_card_back_side = m.get('LegalPersonIdCardBackSide')
        if m.get('LegalPersonIdCardEffTime') is not None:
            self.legal_person_id_card_eff_time = m.get('LegalPersonIdCardEffTime')
        if m.get('LegalPersonIdCardFrontSide') is not None:
            self.legal_person_id_card_front_side = m.get('LegalPersonIdCardFrontSide')
        if m.get('LegalPersonName') is not None:
            self.legal_person_name = m.get('LegalPersonName')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('OtherFiles') is not None:
            self.other_files_shrink = m.get('OtherFiles')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('QualificationGroupId') is not None:
            self.qualification_group_id = m.get('QualificationGroupId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class UpdateSmsQualificationResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.data = data
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
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateSmsQualificationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateSmsQualificationResponseBody = None,
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
            temp_model = UpdateSmsQualificationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateSmsSignRequest(TeaModel):
    def __init__(
        self,
        apply_scene_content: str = None,
        authorization_letter_id: int = None,
        more_data: List[str] = None,
        owner_id: int = None,
        qualification_id: int = None,
        remark: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        sign_name: str = None,
        sign_source: int = None,
        sign_type: int = None,
        third_party: bool = None,
    ):
        # Application scenarios, instructions as follows:
        # - For registered websites, please enter the domain name registered with MIIT, including HTTP or HTTPS.
        # - For launched apps, provide the display link from the app store with HTTP or HTTPS, ensuring the app is online.
        # - For public accounts or mini-programs, fill in the full name, ensuring they are online.
        # - For e-commerce platform store names (for enterprise users only), provide the display link with HTTP or HTTPS.
        self.apply_scene_content = apply_scene_content
        self.authorization_letter_id = authorization_letter_id
        # Additional materials, such as uploading business proof documents or screenshots of business operations, to help reviewers understand your business details.
        self.more_data = more_data
        self.owner_id = owner_id
        # Approved or under-review qualification ID.
        # 
        # > - Before applying for an SMS signature, please first [apply for qualifications](https://help.aliyun.com/zh/sms/user-guide/new-qualification?spm=a2c4g.11186623.0.0.718d187bbkpMRK).
        # > - You can view the qualification ID on the [Qualification Management](https://dysms.console.aliyun.com/domestic/text/qualification) page.
        # 
        # This parameter is required.
        self.qualification_id = qualification_id
        # Explanation of the SMS signature scenario, with a maximum length of 200 characters.
        # 
        # > The scenario explanation is one of the reference information for signature review. Please provide a detailed description of the usage scenarios of the launched business, along with verifiable information such as website links, registered domain addresses, app store download links, full names of public accounts or mini-programs, etc. For login scenarios, test account credentials are also required. A well-informed application explanation will enhance the efficiency of signature and template reviews. Refer to the **Application Scenarios** column in the [Signature Source](https://help.aliyun.com/zh/sms/user-guide/signature-specifications-1?spm=a2c4g.11186623.0.i2#section-xup-k46-yi4) table for filling in SMS scenarios.
        self.remark = remark
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Signature not yet approved.
        # 
        # This parameter is required.
        self.sign_name = sign_name
        # Source of the signature. Values:
        # 
        # - **0**: Full name or abbreviation of enterprises and institutions.
        # - **1**: Full name or abbreviation of MIIT-registered websites.
        # - **2**: Full name or abbreviation of app applications.
        # - **3**: Full name or abbreviation of public accounts or mini-programs.
        # - **4**: Full name or abbreviation of e-commerce platform store names.
        # - **5**: Full name or abbreviation of trademarks.
        # 
        # This parameter is required.
        self.sign_source = sign_source
        # Signature type. It is recommended to use the default value.
        # 
        # - **0**: Verification code
        # - **1**: General (default)
        self.sign_type = sign_type
        # Whether the signature is for self-use or others.
        # 
        # - false: Self-use
        # - true: Others
        # >Notice: When the signature is for self-use, select the self-use qualification ID; when it\\"s for others, choose the others\\" qualification ID.
        self.third_party = third_party

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apply_scene_content is not None:
            result['ApplySceneContent'] = self.apply_scene_content
        if self.authorization_letter_id is not None:
            result['AuthorizationLetterId'] = self.authorization_letter_id
        if self.more_data is not None:
            result['MoreData'] = self.more_data
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.qualification_id is not None:
            result['QualificationId'] = self.qualification_id
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.sign_name is not None:
            result['SignName'] = self.sign_name
        if self.sign_source is not None:
            result['SignSource'] = self.sign_source
        if self.sign_type is not None:
            result['SignType'] = self.sign_type
        if self.third_party is not None:
            result['ThirdParty'] = self.third_party
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplySceneContent') is not None:
            self.apply_scene_content = m.get('ApplySceneContent')
        if m.get('AuthorizationLetterId') is not None:
            self.authorization_letter_id = m.get('AuthorizationLetterId')
        if m.get('MoreData') is not None:
            self.more_data = m.get('MoreData')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('QualificationId') is not None:
            self.qualification_id = m.get('QualificationId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SignName') is not None:
            self.sign_name = m.get('SignName')
        if m.get('SignSource') is not None:
            self.sign_source = m.get('SignSource')
        if m.get('SignType') is not None:
            self.sign_type = m.get('SignType')
        if m.get('ThirdParty') is not None:
            self.third_party = m.get('ThirdParty')
        return self


class UpdateSmsSignShrinkRequest(TeaModel):
    def __init__(
        self,
        apply_scene_content: str = None,
        authorization_letter_id: int = None,
        more_data_shrink: str = None,
        owner_id: int = None,
        qualification_id: int = None,
        remark: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        sign_name: str = None,
        sign_source: int = None,
        sign_type: int = None,
        third_party: bool = None,
    ):
        # Application scenarios, instructions as follows:
        # - For registered websites, please enter the domain name registered with MIIT, including HTTP or HTTPS.
        # - For launched apps, provide the display link from the app store with HTTP or HTTPS, ensuring the app is online.
        # - For public accounts or mini-programs, fill in the full name, ensuring they are online.
        # - For e-commerce platform store names (for enterprise users only), provide the display link with HTTP or HTTPS.
        self.apply_scene_content = apply_scene_content
        self.authorization_letter_id = authorization_letter_id
        # Additional materials, such as uploading business proof documents or screenshots of business operations, to help reviewers understand your business details.
        self.more_data_shrink = more_data_shrink
        self.owner_id = owner_id
        # Approved or under-review qualification ID.
        # 
        # > - Before applying for an SMS signature, please first [apply for qualifications](https://help.aliyun.com/zh/sms/user-guide/new-qualification?spm=a2c4g.11186623.0.0.718d187bbkpMRK).
        # > - You can view the qualification ID on the [Qualification Management](https://dysms.console.aliyun.com/domestic/text/qualification) page.
        # 
        # This parameter is required.
        self.qualification_id = qualification_id
        # Explanation of the SMS signature scenario, with a maximum length of 200 characters.
        # 
        # > The scenario explanation is one of the reference information for signature review. Please provide a detailed description of the usage scenarios of the launched business, along with verifiable information such as website links, registered domain addresses, app store download links, full names of public accounts or mini-programs, etc. For login scenarios, test account credentials are also required. A well-informed application explanation will enhance the efficiency of signature and template reviews. Refer to the **Application Scenarios** column in the [Signature Source](https://help.aliyun.com/zh/sms/user-guide/signature-specifications-1?spm=a2c4g.11186623.0.i2#section-xup-k46-yi4) table for filling in SMS scenarios.
        self.remark = remark
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Signature not yet approved.
        # 
        # This parameter is required.
        self.sign_name = sign_name
        # Source of the signature. Values:
        # 
        # - **0**: Full name or abbreviation of enterprises and institutions.
        # - **1**: Full name or abbreviation of MIIT-registered websites.
        # - **2**: Full name or abbreviation of app applications.
        # - **3**: Full name or abbreviation of public accounts or mini-programs.
        # - **4**: Full name or abbreviation of e-commerce platform store names.
        # - **5**: Full name or abbreviation of trademarks.
        # 
        # This parameter is required.
        self.sign_source = sign_source
        # Signature type. It is recommended to use the default value.
        # 
        # - **0**: Verification code
        # - **1**: General (default)
        self.sign_type = sign_type
        # Whether the signature is for self-use or others.
        # 
        # - false: Self-use
        # - true: Others
        # >Notice: When the signature is for self-use, select the self-use qualification ID; when it\\"s for others, choose the others\\" qualification ID.
        self.third_party = third_party

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apply_scene_content is not None:
            result['ApplySceneContent'] = self.apply_scene_content
        if self.authorization_letter_id is not None:
            result['AuthorizationLetterId'] = self.authorization_letter_id
        if self.more_data_shrink is not None:
            result['MoreData'] = self.more_data_shrink
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.qualification_id is not None:
            result['QualificationId'] = self.qualification_id
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.sign_name is not None:
            result['SignName'] = self.sign_name
        if self.sign_source is not None:
            result['SignSource'] = self.sign_source
        if self.sign_type is not None:
            result['SignType'] = self.sign_type
        if self.third_party is not None:
            result['ThirdParty'] = self.third_party
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplySceneContent') is not None:
            self.apply_scene_content = m.get('ApplySceneContent')
        if m.get('AuthorizationLetterId') is not None:
            self.authorization_letter_id = m.get('AuthorizationLetterId')
        if m.get('MoreData') is not None:
            self.more_data_shrink = m.get('MoreData')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('QualificationId') is not None:
            self.qualification_id = m.get('QualificationId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SignName') is not None:
            self.sign_name = m.get('SignName')
        if m.get('SignSource') is not None:
            self.sign_source = m.get('SignSource')
        if m.get('SignType') is not None:
            self.sign_type = m.get('SignType')
        if m.get('ThirdParty') is not None:
            self.third_party = m.get('ThirdParty')
        return self


class UpdateSmsSignResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        order_id: str = None,
        request_id: str = None,
        sign_name: str = None,
    ):
        # Request status code.
        # 
        # * OK indicates a successful request.
        # * For other error codes, refer to [Error Code List](https://help.aliyun.com/document_detail/101346.html).
        self.code = code
        # Description of the status code.
        self.message = message
        # Work order number.
        # 
        # This parameter is used by auditors when querying audits. You need to provide this work order number for expedited review.
        self.order_id = order_id
        # The ID of this call request, uniquely generated by Alibaba Cloud, which can be used for troubleshooting and issue localization.
        self.request_id = request_id
        # The modified signature name.
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
        if self.order_id is not None:
            result['OrderId'] = self.order_id
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
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SignName') is not None:
            self.sign_name = m.get('SignName')
        return self


class UpdateSmsSignResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateSmsSignResponseBody = None,
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
            temp_model = UpdateSmsSignResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateSmsTemplateRequest(TeaModel):
    def __init__(
        self,
        apply_scene_content: str = None,
        intl_type: int = None,
        more_data: List[str] = None,
        owner_id: int = None,
        related_sign_name: str = None,
        remark: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        template_code: str = None,
        template_content: str = None,
        template_name: str = None,
        template_rule: str = None,
        template_type: int = None,
        traffic_driving: str = None,
    ):
        # Application scenarios, instructions as follows:
        # - For registered websites, please enter the MIIT-registered domain with HTTP or HTTPS.
        # - For launched apps, provide the app store display link with HTTP or HTTPS, ensuring the app is online.
        # - For public accounts or mini-programs, enter the full name of the public account or mini-program, ensuring they are online.
        # - For e-commerce platform stores, applicable only to enterprise users, enter the display link of the e-commerce store with HTTP or HTTPS.
        self.apply_scene_content = apply_scene_content
        # International/Hong Kong, Macao, and Taiwan template type. When the **TemplateType** parameter is **3**, this parameter is required for international/Hong Kong, Macao, and Taiwan templates, with values:
        # - **0**: Verification code.
        # - **1**: SMS notification.
        # - **2**: Promotional SMS.
        self.intl_type = intl_type
        # Additional information, such as uploading business proof documents or screenshots, to help reviewers understand your business details. Optional and can be left unset.
        self.more_data = more_data
        self.owner_id = owner_id
        # SMS signature associated with the template during the application.
        self.related_sign_name = related_sign_name
        # Explanation for the SMS template application, which serves as a reference for template review.
        self.remark = remark
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Template Code of an unapproved template.
        # 
        # This parameter is required.
        self.template_code = template_code
        # Template content, up to 500 characters in length.
        # 
        # Both the template content and variable content must comply with SMS regulations; otherwise, the template will fail the review. You can also view common template examples on the template application page. Using sample templates can enhance review efficiency and success rates. Variable specifications can be found in [TemplateContent Parameter Variable Specifications](https://help.aliyun.com/zh/sms/templaterule-template-variable-parameter-filling-example?spm).
        # 
        # This parameter is required.
        self.template_content = template_content
        # Template name, up to 30 characters in length.
        # 
        # This parameter is required.
        self.template_name = template_name
        # Template variable rules.
        # 
        # For guidance on filling variable rules, refer to the [Sample Documentation](https://help.aliyun.com/zh/sms/templaterule-template-variable-parameter-filling-example?spm).
        self.template_rule = template_rule
        # SMS type. Values:
        # 
        # - **0**: Verification code.
        # - **1**: SMS notification.
        # - **2**: Promotional SMS.
        # - **3**: International/Hong Kong, Macao, and Taiwan messages.
        # 
        # > Only enterprise-certified users can apply for promotional SMS and international/Hong Kong, Macao, and Taiwan messages. Details on differences between personal and enterprise user rights are available in [Usage Guidelines](https://help.aliyun.com/zh/sms/user-guide/usage-notes?spm=a2c4g.11186623.0.0.67447f576NJnE8).
        # 
        # This parameter is required.
        self.template_type = template_type
        self.traffic_driving = traffic_driving

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apply_scene_content is not None:
            result['ApplySceneContent'] = self.apply_scene_content
        if self.intl_type is not None:
            result['IntlType'] = self.intl_type
        if self.more_data is not None:
            result['MoreData'] = self.more_data
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.related_sign_name is not None:
            result['RelatedSignName'] = self.related_sign_name
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
        if self.template_rule is not None:
            result['TemplateRule'] = self.template_rule
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        if self.traffic_driving is not None:
            result['TrafficDriving'] = self.traffic_driving
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplySceneContent') is not None:
            self.apply_scene_content = m.get('ApplySceneContent')
        if m.get('IntlType') is not None:
            self.intl_type = m.get('IntlType')
        if m.get('MoreData') is not None:
            self.more_data = m.get('MoreData')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RelatedSignName') is not None:
            self.related_sign_name = m.get('RelatedSignName')
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
        if m.get('TemplateRule') is not None:
            self.template_rule = m.get('TemplateRule')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        if m.get('TrafficDriving') is not None:
            self.traffic_driving = m.get('TrafficDriving')
        return self


class UpdateSmsTemplateShrinkRequest(TeaModel):
    def __init__(
        self,
        apply_scene_content: str = None,
        intl_type: int = None,
        more_data_shrink: str = None,
        owner_id: int = None,
        related_sign_name: str = None,
        remark: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        template_code: str = None,
        template_content: str = None,
        template_name: str = None,
        template_rule: str = None,
        template_type: int = None,
        traffic_driving: str = None,
    ):
        # Application scenarios, instructions as follows:
        # - For registered websites, please enter the MIIT-registered domain with HTTP or HTTPS.
        # - For launched apps, provide the app store display link with HTTP or HTTPS, ensuring the app is online.
        # - For public accounts or mini-programs, enter the full name of the public account or mini-program, ensuring they are online.
        # - For e-commerce platform stores, applicable only to enterprise users, enter the display link of the e-commerce store with HTTP or HTTPS.
        self.apply_scene_content = apply_scene_content
        # International/Hong Kong, Macao, and Taiwan template type. When the **TemplateType** parameter is **3**, this parameter is required for international/Hong Kong, Macao, and Taiwan templates, with values:
        # - **0**: Verification code.
        # - **1**: SMS notification.
        # - **2**: Promotional SMS.
        self.intl_type = intl_type
        # Additional information, such as uploading business proof documents or screenshots, to help reviewers understand your business details. Optional and can be left unset.
        self.more_data_shrink = more_data_shrink
        self.owner_id = owner_id
        # SMS signature associated with the template during the application.
        self.related_sign_name = related_sign_name
        # Explanation for the SMS template application, which serves as a reference for template review.
        self.remark = remark
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Template Code of an unapproved template.
        # 
        # This parameter is required.
        self.template_code = template_code
        # Template content, up to 500 characters in length.
        # 
        # Both the template content and variable content must comply with SMS regulations; otherwise, the template will fail the review. You can also view common template examples on the template application page. Using sample templates can enhance review efficiency and success rates. Variable specifications can be found in [TemplateContent Parameter Variable Specifications](https://help.aliyun.com/zh/sms/templaterule-template-variable-parameter-filling-example?spm).
        # 
        # This parameter is required.
        self.template_content = template_content
        # Template name, up to 30 characters in length.
        # 
        # This parameter is required.
        self.template_name = template_name
        # Template variable rules.
        # 
        # For guidance on filling variable rules, refer to the [Sample Documentation](https://help.aliyun.com/zh/sms/templaterule-template-variable-parameter-filling-example?spm).
        self.template_rule = template_rule
        # SMS type. Values:
        # 
        # - **0**: Verification code.
        # - **1**: SMS notification.
        # - **2**: Promotional SMS.
        # - **3**: International/Hong Kong, Macao, and Taiwan messages.
        # 
        # > Only enterprise-certified users can apply for promotional SMS and international/Hong Kong, Macao, and Taiwan messages. Details on differences between personal and enterprise user rights are available in [Usage Guidelines](https://help.aliyun.com/zh/sms/user-guide/usage-notes?spm=a2c4g.11186623.0.0.67447f576NJnE8).
        # 
        # This parameter is required.
        self.template_type = template_type
        self.traffic_driving = traffic_driving

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apply_scene_content is not None:
            result['ApplySceneContent'] = self.apply_scene_content
        if self.intl_type is not None:
            result['IntlType'] = self.intl_type
        if self.more_data_shrink is not None:
            result['MoreData'] = self.more_data_shrink
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.related_sign_name is not None:
            result['RelatedSignName'] = self.related_sign_name
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
        if self.template_rule is not None:
            result['TemplateRule'] = self.template_rule
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        if self.traffic_driving is not None:
            result['TrafficDriving'] = self.traffic_driving
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplySceneContent') is not None:
            self.apply_scene_content = m.get('ApplySceneContent')
        if m.get('IntlType') is not None:
            self.intl_type = m.get('IntlType')
        if m.get('MoreData') is not None:
            self.more_data_shrink = m.get('MoreData')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RelatedSignName') is not None:
            self.related_sign_name = m.get('RelatedSignName')
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
        if m.get('TemplateRule') is not None:
            self.template_rule = m.get('TemplateRule')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        if m.get('TrafficDriving') is not None:
            self.traffic_driving = m.get('TrafficDriving')
        return self


class UpdateSmsTemplateResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        order_id: str = None,
        request_id: str = None,
        template_code: str = None,
        template_name: str = None,
    ):
        # Request status code.
        # 
        # * OK indicates a successful request.
        # * For other error codes, refer to the **Error Codes** section of this chapter or the product\\"s [API Error Codes](https://help.aliyun.com/document_detail/101346.html).
        self.code = code
        # Description of the status code.
        self.message = message
        # Work order number.
        # 
        # This parameter is used by auditors when querying audits. You need to provide this work order number when requesting expedited review.
        self.order_id = order_id
        # The ID of this call request, which is a unique identifier generated by Alibaba Cloud for the request and can be used to troubleshoot and locate issues.
        self.request_id = request_id
        # Code of the SMS template.
        self.template_code = template_code
        # Name of the SMS template.
        self.template_name = template_name

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
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        return self


class UpdateSmsTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateSmsTemplateResponseBody = None,
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
            temp_model = UpdateSmsTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ValidPhoneCodeRequest(TeaModel):
    def __init__(
        self,
        certify_code: str = None,
        owner_id: int = None,
        phone_no: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # 验证码
        # 
        # This parameter is required.
        self.certify_code = certify_code
        self.owner_id = owner_id
        # 手机号
        # 
        # This parameter is required.
        self.phone_no = phone_no
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certify_code is not None:
            result['CertifyCode'] = self.certify_code
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.phone_no is not None:
            result['PhoneNo'] = self.phone_no
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertifyCode') is not None:
            self.certify_code = m.get('CertifyCode')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PhoneNo') is not None:
            self.phone_no = m.get('PhoneNo')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class ValidPhoneCodeResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: bool = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.data = data
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
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ValidPhoneCodeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ValidPhoneCodeResponseBody = None,
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
            temp_model = ValidPhoneCodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class VerifyLogisticsSmsMailNoRequest(TeaModel):
    def __init__(
        self,
        express_company_code: str = None,
        mail_no: str = None,
        owner_id: int = None,
        platform_company_code: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # This parameter is required.
        self.express_company_code = express_company_code
        # This parameter is required.
        self.mail_no = mail_no
        self.owner_id = owner_id
        self.platform_company_code = platform_company_code
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.express_company_code is not None:
            result['ExpressCompanyCode'] = self.express_company_code
        if self.mail_no is not None:
            result['MailNo'] = self.mail_no
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.platform_company_code is not None:
            result['PlatformCompanyCode'] = self.platform_company_code
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpressCompanyCode') is not None:
            self.express_company_code = m.get('ExpressCompanyCode')
        if m.get('MailNo') is not None:
            self.mail_no = m.get('MailNo')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PlatformCompanyCode') is not None:
            self.platform_company_code = m.get('PlatformCompanyCode')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class VerifyLogisticsSmsMailNoResponseBodyData(TeaModel):
    def __init__(
        self,
        express_company_code: str = None,
        mobile_suffix: str = None,
        verify_result: bool = None,
    ):
        self.express_company_code = express_company_code
        self.mobile_suffix = mobile_suffix
        self.verify_result = verify_result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.express_company_code is not None:
            result['ExpressCompanyCode'] = self.express_company_code
        if self.mobile_suffix is not None:
            result['MobileSuffix'] = self.mobile_suffix
        if self.verify_result is not None:
            result['VerifyResult'] = self.verify_result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpressCompanyCode') is not None:
            self.express_company_code = m.get('ExpressCompanyCode')
        if m.get('MobileSuffix') is not None:
            self.mobile_suffix = m.get('MobileSuffix')
        if m.get('VerifyResult') is not None:
            self.verify_result = m.get('VerifyResult')
        return self


class VerifyLogisticsSmsMailNoResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: VerifyLogisticsSmsMailNoResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.data = data
        self.message = message
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
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
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
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = VerifyLogisticsSmsMailNoResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class VerifyLogisticsSmsMailNoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: VerifyLogisticsSmsMailNoResponseBody = None,
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
            temp_model = VerifyLogisticsSmsMailNoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


