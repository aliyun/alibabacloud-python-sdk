# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class AuthorizeFileUploadRequest(TeaModel):
    def __init__(self, product=None, region_id=None):
        self.product = product          # type: str
        self.region_id = region_id      # type: str

    def validate(self):
        self.validate_required(self.product, 'product')

    def to_map(self):
        result = {}
        if self.product is not None:
            result['Product'] = self.product
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, map={}):
        if map.get('Product') is not None:
            self.product = map.get('Product')
        if map.get('RegionId') is not None:
            self.region_id = map.get('RegionId')
        return self


class AuthorizeFileUploadResponse(TeaModel):
    def __init__(self, access_key_id=None, bucket=None, encoded_policy=None, endpoint=None, object_key=None,
                 request_id=None, signature=None, use_accelerate=None):
        self.access_key_id = access_key_id  # type: str
        self.bucket = bucket            # type: str
        self.encoded_policy = encoded_policy  # type: str
        self.endpoint = endpoint        # type: str
        self.object_key = object_key    # type: str
        self.request_id = request_id    # type: str
        self.signature = signature      # type: str
        self.use_accelerate = use_accelerate  # type: bool

    def validate(self):
        self.validate_required(self.access_key_id, 'access_key_id')
        self.validate_required(self.bucket, 'bucket')
        self.validate_required(self.encoded_policy, 'encoded_policy')
        self.validate_required(self.endpoint, 'endpoint')
        self.validate_required(self.object_key, 'object_key')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.signature, 'signature')
        self.validate_required(self.use_accelerate, 'use_accelerate')

    def to_map(self):
        result = {}
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

    def from_map(self, map={}):
        if map.get('AccessKeyId') is not None:
            self.access_key_id = map.get('AccessKeyId')
        if map.get('Bucket') is not None:
            self.bucket = map.get('Bucket')
        if map.get('EncodedPolicy') is not None:
            self.encoded_policy = map.get('EncodedPolicy')
        if map.get('Endpoint') is not None:
            self.endpoint = map.get('Endpoint')
        if map.get('ObjectKey') is not None:
            self.object_key = map.get('ObjectKey')
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('Signature') is not None:
            self.signature = map.get('Signature')
        if map.get('UseAccelerate') is not None:
            self.use_accelerate = map.get('UseAccelerate')
        return self
