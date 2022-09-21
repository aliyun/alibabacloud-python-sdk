# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict


class AuthorizeFileUploadRequest(TeaModel):
    def __init__(
        self,
        product: str = None,
        region_id: str = None,
    ):
        self.product = product
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product is not None:
            result['Product'] = self.product
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class AuthorizeFileUploadResponseBody(TeaModel):
    def __init__(
        self,
        access_key_id: str = None,
        bucket: str = None,
        encoded_policy: str = None,
        endpoint: str = None,
        object_key: str = None,
        request_id: str = None,
        signature: str = None,
        use_accelerate: bool = None,
    ):
        self.access_key_id = access_key_id
        self.bucket = bucket
        self.encoded_policy = encoded_policy
        self.endpoint = endpoint
        self.object_key = object_key
        self.request_id = request_id
        self.signature = signature
        self.use_accelerate = use_accelerate

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
        if self.encoded_policy is not None:
            result['EncodedPolicy'] = self.encoded_policy
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.object_key is not None:
            result['ObjectKey'] = self.object_key
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.signature is not None:
            result['Signature'] = self.signature
        if self.use_accelerate is not None:
            result['UseAccelerate'] = self.use_accelerate
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessKeyId') is not None:
            self.access_key_id = m.get('AccessKeyId')
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')
        if m.get('EncodedPolicy') is not None:
            self.encoded_policy = m.get('EncodedPolicy')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('ObjectKey') is not None:
            self.object_key = m.get('ObjectKey')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Signature') is not None:
            self.signature = m.get('Signature')
        if m.get('UseAccelerate') is not None:
            self.use_accelerate = m.get('UseAccelerate')
        return self


class AuthorizeFileUploadResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AuthorizeFileUploadResponseBody = None,
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
            temp_model = AuthorizeFileUploadResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


