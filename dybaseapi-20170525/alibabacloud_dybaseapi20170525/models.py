# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict


class QueryTokenForMnsQueueRequest(TeaModel):
    def __init__(
        self,
        message_type: str = None,
        owner_id: int = None,
        queue_name: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # This parameter is required.
        self.message_type = message_type
        self.owner_id = owner_id
        self.queue_name = queue_name
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message_type is not None:
            result['MessageType'] = self.message_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MessageType') is not None:
            self.message_type = m.get('MessageType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class QueryTokenForMnsQueueResponseBodyMessageTokenDTO(TeaModel):
    def __init__(
        self,
        access_key_id: str = None,
        access_key_secret: str = None,
        create_time: str = None,
        expire_time: str = None,
        security_token: str = None,
    ):
        self.access_key_id = access_key_id
        self.access_key_secret = access_key_secret
        self.create_time = create_time
        self.expire_time = expire_time
        self.security_token = security_token

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
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessKeyId') is not None:
            self.access_key_id = m.get('AccessKeyId')
        if m.get('AccessKeySecret') is not None:
            self.access_key_secret = m.get('AccessKeySecret')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class QueryTokenForMnsQueueResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        message_token_dto: QueryTokenForMnsQueueResponseBodyMessageTokenDTO = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.message_token_dto = message_token_dto
        self.request_id = request_id

    def validate(self):
        if self.message_token_dto:
            self.message_token_dto.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.message_token_dto is not None:
            result['MessageTokenDTO'] = self.message_token_dto.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('MessageTokenDTO') is not None:
            temp_model = QueryTokenForMnsQueueResponseBodyMessageTokenDTO()
            self.message_token_dto = temp_model.from_map(m['MessageTokenDTO'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryTokenForMnsQueueResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryTokenForMnsQueueResponseBody = None,
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
            temp_model = QueryTokenForMnsQueueResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


