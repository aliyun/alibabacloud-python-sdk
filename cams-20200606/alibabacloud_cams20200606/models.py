# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict


class CheckContactsRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        from_: str = None,
        channel_type: str = None,
        contacts: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.from_ = from_
        self.channel_type = channel_type
        self.contacts = contacts

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
        if self.from_ is not None:
            result['From'] = self.from_
        if self.channel_type is not None:
            result['ChannelType'] = self.channel_type
        if self.contacts is not None:
            result['Contacts'] = self.contacts
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('From') is not None:
            self.from_ = m.get('From')
        if m.get('ChannelType') is not None:
            self.channel_type = m.get('ChannelType')
        if m.get('Contacts') is not None:
            self.contacts = m.get('Contacts')
        return self


class CheckContactsResponseBodyContacts(TeaModel):
    def __init__(
        self,
        status: str = None,
        phone_number: str = None,
    ):
        self.status = status
        self.phone_number = phone_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        return self


class CheckContactsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        contacts: List[CheckContactsResponseBodyContacts] = None,
        result_message: str = None,
        result_code: str = None,
    ):
        self.request_id = request_id
        self.contacts = contacts
        self.result_message = result_message
        self.result_code = result_code

    def validate(self):
        if self.contacts:
            for k in self.contacts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Contacts'] = []
        if self.contacts is not None:
            for k in self.contacts:
                result['Contacts'].append(k.to_map() if k else None)
        if self.result_message is not None:
            result['ResultMessage'] = self.result_message
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.contacts = []
        if m.get('Contacts') is not None:
            for k in m.get('Contacts'):
                temp_model = CheckContactsResponseBodyContacts()
                self.contacts.append(temp_model.from_map(k))
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        return self


class CheckContactsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CheckContactsResponseBody = None,
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
            temp_model = CheckContactsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendMessageRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        to: str = None,
        from_: str = None,
        channel_type: str = None,
        type: str = None,
        template_code: str = None,
        template_body_params: str = None,
        message_type: str = None,
        link: str = None,
        text: str = None,
        caption: str = None,
        file_name: str = None,
        template_header_params: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.to = to
        self.from_ = from_
        self.channel_type = channel_type
        self.type = type
        self.template_code = template_code
        self.template_body_params = template_body_params
        self.message_type = message_type
        self.link = link
        self.text = text
        self.caption = caption
        self.file_name = file_name
        self.template_header_params = template_header_params

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
        if self.channel_type is not None:
            result['ChannelType'] = self.channel_type
        if self.type is not None:
            result['Type'] = self.type
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.template_body_params is not None:
            result['TemplateBodyParams'] = self.template_body_params
        if self.message_type is not None:
            result['MessageType'] = self.message_type
        if self.link is not None:
            result['Link'] = self.link
        if self.text is not None:
            result['Text'] = self.text
        if self.caption is not None:
            result['Caption'] = self.caption
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.template_header_params is not None:
            result['TemplateHeaderParams'] = self.template_header_params
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
        if m.get('ChannelType') is not None:
            self.channel_type = m.get('ChannelType')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('TemplateBodyParams') is not None:
            self.template_body_params = m.get('TemplateBodyParams')
        if m.get('MessageType') is not None:
            self.message_type = m.get('MessageType')
        if m.get('Link') is not None:
            self.link = m.get('Link')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('Caption') is not None:
            self.caption = m.get('Caption')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('TemplateHeaderParams') is not None:
            self.template_header_params = m.get('TemplateHeaderParams')
        return self


class SendMessageResponseBodyModule(TeaModel):
    def __init__(
        self,
        from_id: str = None,
        to_id: str = None,
        message_id: str = None,
    ):
        self.from_id = from_id
        self.to_id = to_id
        self.message_id = message_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.from_id is not None:
            result['FromId'] = self.from_id
        if self.to_id is not None:
            result['ToId'] = self.to_id
        if self.message_id is not None:
            result['MessageId'] = self.message_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FromId') is not None:
            self.from_id = m.get('FromId')
        if m.get('ToId') is not None:
            self.to_id = m.get('ToId')
        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')
        return self


class SendMessageResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result_message: str = None,
        module: SendMessageResponseBodyModule = None,
        result_code: str = None,
    ):
        self.request_id = request_id
        self.result_message = result_message
        self.module = module
        self.result_code = result_code

    def validate(self):
        if self.module:
            self.module.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_message is not None:
            result['ResultMessage'] = self.result_message
        if self.module is not None:
            result['Module'] = self.module.to_map()
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        if m.get('Module') is not None:
            temp_model = SendMessageResponseBodyModule()
            self.module = temp_model.from_map(m['Module'])
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        return self


class SendMessageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SendMessageResponseBody = None,
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
            temp_model = SendMessageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


