# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict


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
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        sign_name: str = None,
        sign_source: int = None,
        remark: str = None,
        sign_file_list: List[AddSmsSignRequestSignFileList] = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.sign_name = sign_name
        self.sign_source = sign_source
        self.remark = remark
        self.sign_file_list = sign_file_list

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
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.sign_name is not None:
            result['SignName'] = self.sign_name
        if self.sign_source is not None:
            result['SignSource'] = self.sign_source
        if self.remark is not None:
            result['Remark'] = self.remark
        result['SignFileList'] = []
        if self.sign_file_list is not None:
            for k in self.sign_file_list:
                result['SignFileList'].append(k.to_map() if k else None)
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
        if m.get('SignSource') is not None:
            self.sign_source = m.get('SignSource')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        self.sign_file_list = []
        if m.get('SignFileList') is not None:
            for k in m.get('SignFileList'):
                temp_model = AddSmsSignRequestSignFileList()
                self.sign_file_list.append(temp_model.from_map(k))
        return self


class AddSmsSignResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: str = None,
        sign_name: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.code = code
        self.sign_name = sign_name

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
        if self.code is not None:
            result['Code'] = self.code
        if self.sign_name is not None:
            result['SignName'] = self.sign_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('SignName') is not None:
            self.sign_name = m.get('SignName')
        return self


class AddSmsSignResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddSmsSignResponseBody = None,
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
            temp_model = AddSmsSignResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddSmsTemplateRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        template_type: int = None,
        template_name: str = None,
        template_content: str = None,
        remark: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.template_type = template_type
        self.template_name = template_name
        self.template_content = template_content
        self.remark = remark

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
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_content is not None:
            result['TemplateContent'] = self.template_content
        if self.remark is not None:
            result['Remark'] = self.remark
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateContent') is not None:
            self.template_content = m.get('TemplateContent')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        return self


class AddSmsTemplateResponseBody(TeaModel):
    def __init__(
        self,
        template_code: str = None,
        message: str = None,
        request_id: str = None,
        code: str = None,
    ):
        self.template_code = template_code
        self.message = message
        self.request_id = request_id
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class AddSmsTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddSmsTemplateResponseBody = None,
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
            temp_model = AddSmsTemplateResponseBody()
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
        message: str = None,
        request_id: str = None,
        code: str = None,
        sign_name: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.code = code
        self.sign_name = sign_name

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
        if self.code is not None:
            result['Code'] = self.code
        if self.sign_name is not None:
            result['SignName'] = self.sign_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('SignName') is not None:
            self.sign_name = m.get('SignName')
        return self


class DeleteSmsSignResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteSmsSignResponseBody = None,
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
        template_code: str = None,
        message: str = None,
        request_id: str = None,
        code: str = None,
    ):
        self.template_code = template_code
        self.message = message
        self.request_id = request_id
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class DeleteSmsTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteSmsTemplateResponseBody = None,
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
            temp_model = DeleteSmsTemplateResponseBody()
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
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        sign_name: str = None,
        sign_source: int = None,
        remark: str = None,
        sign_file_list: List[ModifySmsSignRequestSignFileList] = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.sign_name = sign_name
        self.sign_source = sign_source
        self.remark = remark
        self.sign_file_list = sign_file_list

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
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.sign_name is not None:
            result['SignName'] = self.sign_name
        if self.sign_source is not None:
            result['SignSource'] = self.sign_source
        if self.remark is not None:
            result['Remark'] = self.remark
        result['SignFileList'] = []
        if self.sign_file_list is not None:
            for k in self.sign_file_list:
                result['SignFileList'].append(k.to_map() if k else None)
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
        if m.get('SignSource') is not None:
            self.sign_source = m.get('SignSource')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        self.sign_file_list = []
        if m.get('SignFileList') is not None:
            for k in m.get('SignFileList'):
                temp_model = ModifySmsSignRequestSignFileList()
                self.sign_file_list.append(temp_model.from_map(k))
        return self


class ModifySmsSignResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: str = None,
        sign_name: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.code = code
        self.sign_name = sign_name

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
        if self.code is not None:
            result['Code'] = self.code
        if self.sign_name is not None:
            result['SignName'] = self.sign_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('SignName') is not None:
            self.sign_name = m.get('SignName')
        return self


class ModifySmsSignResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifySmsSignResponseBody = None,
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
            temp_model = ModifySmsSignResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifySmsTemplateRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        template_type: int = None,
        template_name: str = None,
        template_code: str = None,
        template_content: str = None,
        remark: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.template_type = template_type
        self.template_name = template_name
        self.template_code = template_code
        self.template_content = template_content
        self.remark = remark

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
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.template_content is not None:
            result['TemplateContent'] = self.template_content
        if self.remark is not None:
            result['Remark'] = self.remark
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('TemplateContent') is not None:
            self.template_content = m.get('TemplateContent')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        return self


class ModifySmsTemplateResponseBody(TeaModel):
    def __init__(
        self,
        template_code: str = None,
        message: str = None,
        request_id: str = None,
        code: str = None,
    ):
        self.template_code = template_code
        self.message = message
        self.request_id = request_id
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class ModifySmsTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifySmsTemplateResponseBody = None,
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
            temp_model = ModifySmsTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QuerySendDetailsRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        phone_number: str = None,
        biz_id: str = None,
        send_date: str = None,
        page_size: int = None,
        current_page: int = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.phone_number = phone_number
        self.biz_id = biz_id
        self.send_date = send_date
        self.page_size = page_size
        self.current_page = current_page

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
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.send_date is not None:
            result['SendDate'] = self.send_date
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('SendDate') is not None:
            self.send_date = m.get('SendDate')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        return self


class QuerySendDetailsResponseBodySmsSendDetailDTOsSmsSendDetailDTO(TeaModel):
    def __init__(
        self,
        err_code: str = None,
        template_code: str = None,
        out_id: str = None,
        receive_date: str = None,
        send_date: str = None,
        phone_num: str = None,
        content: str = None,
        send_status: int = None,
    ):
        self.err_code = err_code
        self.template_code = template_code
        self.out_id = out_id
        self.receive_date = receive_date
        self.send_date = send_date
        self.phone_num = phone_num
        self.content = content
        self.send_status = send_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.out_id is not None:
            result['OutId'] = self.out_id
        if self.receive_date is not None:
            result['ReceiveDate'] = self.receive_date
        if self.send_date is not None:
            result['SendDate'] = self.send_date
        if self.phone_num is not None:
            result['PhoneNum'] = self.phone_num
        if self.content is not None:
            result['Content'] = self.content
        if self.send_status is not None:
            result['SendStatus'] = self.send_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('OutId') is not None:
            self.out_id = m.get('OutId')
        if m.get('ReceiveDate') is not None:
            self.receive_date = m.get('ReceiveDate')
        if m.get('SendDate') is not None:
            self.send_date = m.get('SendDate')
        if m.get('PhoneNum') is not None:
            self.phone_num = m.get('PhoneNum')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('SendStatus') is not None:
            self.send_status = m.get('SendStatus')
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
        total_count: str = None,
        message: str = None,
        request_id: str = None,
        code: str = None,
        sms_send_detail_dtos: QuerySendDetailsResponseBodySmsSendDetailDTOs = None,
    ):
        self.total_count = total_count
        self.message = message
        self.request_id = request_id
        self.code = code
        self.sms_send_detail_dtos = sms_send_detail_dtos

    def validate(self):
        if self.sms_send_detail_dtos:
            self.sms_send_detail_dtos.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.sms_send_detail_dtos is not None:
            result['SmsSendDetailDTOs'] = self.sms_send_detail_dtos.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('SmsSendDetailDTOs') is not None:
            temp_model = QuerySendDetailsResponseBodySmsSendDetailDTOs()
            self.sms_send_detail_dtos = temp_model.from_map(m['SmsSendDetailDTOs'])
        return self


class QuerySendDetailsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QuerySendDetailsResponseBody = None,
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
            temp_model = QuerySendDetailsResponseBody()
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
        request_id: str = None,
        message: str = None,
        sign_status: int = None,
        code: str = None,
        create_date: str = None,
        reason: str = None,
        sign_name: str = None,
    ):
        self.request_id = request_id
        self.message = message
        self.sign_status = sign_status
        self.code = code
        self.create_date = create_date
        self.reason = reason
        self.sign_name = sign_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.sign_status is not None:
            result['SignStatus'] = self.sign_status
        if self.code is not None:
            result['Code'] = self.code
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.sign_name is not None:
            result['SignName'] = self.sign_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('SignStatus') is not None:
            self.sign_status = m.get('SignStatus')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('SignName') is not None:
            self.sign_name = m.get('SignName')
        return self


class QuerySmsSignResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QuerySmsSignResponseBody = None,
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
            temp_model = QuerySmsSignResponseBody()
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
        template_code: str = None,
        request_id: str = None,
        message: str = None,
        template_content: str = None,
        template_name: str = None,
        template_type: int = None,
        code: str = None,
        create_date: str = None,
        reason: str = None,
        template_status: int = None,
    ):
        self.template_code = template_code
        self.request_id = request_id
        self.message = message
        self.template_content = template_content
        self.template_name = template_name
        self.template_type = template_type
        self.code = code
        self.create_date = create_date
        self.reason = reason
        self.template_status = template_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.template_content is not None:
            result['TemplateContent'] = self.template_content
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        if self.code is not None:
            result['Code'] = self.code
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.template_status is not None:
            result['TemplateStatus'] = self.template_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('TemplateContent') is not None:
            self.template_content = m.get('TemplateContent')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('TemplateStatus') is not None:
            self.template_status = m.get('TemplateStatus')
        return self


class QuerySmsTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QuerySmsTemplateResponseBody = None,
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
            temp_model = QuerySmsTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendBatchSmsRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        phone_number_json: str = None,
        sign_name_json: str = None,
        template_code: str = None,
        template_param_json: str = None,
        sms_up_extend_code_json: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.phone_number_json = phone_number_json
        self.sign_name_json = sign_name_json
        self.template_code = template_code
        self.template_param_json = template_param_json
        self.sms_up_extend_code_json = sms_up_extend_code_json

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
        if self.phone_number_json is not None:
            result['PhoneNumberJson'] = self.phone_number_json
        if self.sign_name_json is not None:
            result['SignNameJson'] = self.sign_name_json
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.template_param_json is not None:
            result['TemplateParamJson'] = self.template_param_json
        if self.sms_up_extend_code_json is not None:
            result['SmsUpExtendCodeJson'] = self.sms_up_extend_code_json
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('PhoneNumberJson') is not None:
            self.phone_number_json = m.get('PhoneNumberJson')
        if m.get('SignNameJson') is not None:
            self.sign_name_json = m.get('SignNameJson')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('TemplateParamJson') is not None:
            self.template_param_json = m.get('TemplateParamJson')
        if m.get('SmsUpExtendCodeJson') is not None:
            self.sms_up_extend_code_json = m.get('SmsUpExtendCodeJson')
        return self


class SendBatchSmsResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: str = None,
        biz_id: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.code = code
        self.biz_id = biz_id

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
        if self.code is not None:
            result['Code'] = self.code
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        return self


class SendBatchSmsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SendBatchSmsResponseBody = None,
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
            temp_model = SendBatchSmsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendMessageToGlobeRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        to: str = None,
        from_: str = None,
        message: str = None,
        type: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.to = to
        self.from_ = from_
        self.message = message
        self.type = type

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
        if self.to is not None:
            result['To'] = self.to
        if self.from_ is not None:
            result['From'] = self.from_
        if self.message is not None:
            result['Message'] = self.message
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('To') is not None:
            self.to = m.get('To')
        if m.get('From') is not None:
            self.from_ = m.get('From')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class SendMessageToGlobeResponseBodyNumberDetail(TeaModel):
    def __init__(
        self,
        carrier: str = None,
        region: str = None,
        country: str = None,
    ):
        self.carrier = carrier
        self.region = region
        self.country = country

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.carrier is not None:
            result['Carrier'] = self.carrier
        if self.region is not None:
            result['Region'] = self.region
        if self.country is not None:
            result['Country'] = self.country
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Carrier') is not None:
            self.carrier = m.get('Carrier')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        return self


class SendMessageToGlobeResponseBody(TeaModel):
    def __init__(
        self,
        number_detail: SendMessageToGlobeResponseBodyNumberDetail = None,
        request_id: str = None,
        segments: str = None,
        from_: str = None,
        to: str = None,
        code: str = None,
        message_id: str = None,
    ):
        self.number_detail = number_detail
        self.request_id = request_id
        self.segments = segments
        self.from_ = from_
        self.to = to
        self.code = code
        self.message_id = message_id

    def validate(self):
        if self.number_detail:
            self.number_detail.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.number_detail is not None:
            result['NumberDetail'] = self.number_detail.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.segments is not None:
            result['Segments'] = self.segments
        if self.from_ is not None:
            result['From'] = self.from_
        if self.to is not None:
            result['To'] = self.to
        if self.code is not None:
            result['Code'] = self.code
        if self.message_id is not None:
            result['MessageId'] = self.message_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NumberDetail') is not None:
            temp_model = SendMessageToGlobeResponseBodyNumberDetail()
            self.number_detail = temp_model.from_map(m['NumberDetail'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Segments') is not None:
            self.segments = m.get('Segments')
        if m.get('From') is not None:
            self.from_ = m.get('From')
        if m.get('To') is not None:
            self.to = m.get('To')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')
        return self


class SendMessageToGlobeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SendMessageToGlobeResponseBody = None,
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
            temp_model = SendMessageToGlobeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendSmsRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        phone_numbers: str = None,
        sign_name: str = None,
        template_code: str = None,
        template_param: str = None,
        sms_up_extend_code: str = None,
        out_id: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.phone_numbers = phone_numbers
        self.sign_name = sign_name
        self.template_code = template_code
        self.template_param = template_param
        self.sms_up_extend_code = sms_up_extend_code
        self.out_id = out_id

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
        if self.phone_numbers is not None:
            result['PhoneNumbers'] = self.phone_numbers
        if self.sign_name is not None:
            result['SignName'] = self.sign_name
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.template_param is not None:
            result['TemplateParam'] = self.template_param
        if self.sms_up_extend_code is not None:
            result['SmsUpExtendCode'] = self.sms_up_extend_code
        if self.out_id is not None:
            result['OutId'] = self.out_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('PhoneNumbers') is not None:
            self.phone_numbers = m.get('PhoneNumbers')
        if m.get('SignName') is not None:
            self.sign_name = m.get('SignName')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('TemplateParam') is not None:
            self.template_param = m.get('TemplateParam')
        if m.get('SmsUpExtendCode') is not None:
            self.sms_up_extend_code = m.get('SmsUpExtendCode')
        if m.get('OutId') is not None:
            self.out_id = m.get('OutId')
        return self


class SendSmsResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: str = None,
        biz_id: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.code = code
        self.biz_id = biz_id

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
        if self.code is not None:
            result['Code'] = self.code
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        return self


class SendSmsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SendSmsResponseBody = None,
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
            temp_model = SendSmsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


