# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_yike20260707 import models as main_models
from darabonba.model import DaraModel

class CreateOssUploadResponseBody(DaraModel):
    def __init__(
        self,
        object_key: str = None,
        oss_url: str = None,
        request_id: str = None,
        upload_credentials: main_models.CreateOssUploadResponseBodyUploadCredentials = None,
    ):
        # OSS ObjectKey
        self.object_key = object_key
        # The **OSS presigned GET URL**, which is valid for 24 hours and uses the public endpoint. If signature generation fails, null is returned, which does not affect direct upload with the credentials.
        self.oss_url = oss_url
        # The **request ID**.
        self.request_id = request_id
        # The upload credentials. Some fields may be empty depending on the CredentialType.
        self.upload_credentials = upload_credentials

    def validate(self):
        if self.upload_credentials:
            self.upload_credentials.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.object_key is not None:
            result['ObjectKey'] = self.object_key

        if self.oss_url is not None:
            result['OssUrl'] = self.oss_url

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.upload_credentials is not None:
            result['UploadCredentials'] = self.upload_credentials.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ObjectKey') is not None:
            self.object_key = m.get('ObjectKey')

        if m.get('OssUrl') is not None:
            self.oss_url = m.get('OssUrl')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('UploadCredentials') is not None:
            temp_model = main_models.CreateOssUploadResponseBodyUploadCredentials()
            self.upload_credentials = temp_model.from_map(m.get('UploadCredentials'))

        return self

class CreateOssUploadResponseBodyUploadCredentials(DaraModel):
    def __init__(
        self,
        access_key_id: str = None,
        access_key_secret: str = None,
        bucket: str = None,
        expiration: str = None,
        policy: str = None,
        post_access_key_id: str = None,
        post_endpoint: str = None,
        region: str = None,
        security_token: str = None,
        signature: str = None,
        signed_url: str = None,
    ):
        # The STS temporary AccessKey ID.
        self.access_key_id = access_key_id
        # The STS temporary AccessKey secret.
        self.access_key_secret = access_key_secret
        # OSS Bucket
        self.bucket = bucket
        # The expiration time of the credentials. The time is in UTC and follows the ISO 8601 standard. The actual return value prevails.
        self.expiration = expiration
        # The PostObject policy, which is Base64-encoded. This field is returned when POST_POLICY is used.
        self.policy = policy
        # The AccessKey ID used for signing. This field is returned when POST_POLICY is used.
        self.post_access_key_id = post_access_key_id
        # The destination endpoint for POST requests. This field is returned when POST_POLICY is used.
        self.post_endpoint = post_endpoint
        # The OSS region, such as cn-shanghai.
        self.region = region
        # The STS security token.
        self.security_token = security_token
        # The PostObject signature. This field is returned when POST_POLICY is used.
        self.signature = signature
        # The presigned PUT URL. This field is returned when PRESIGNED_URL is used.
        self.signed_url = signed_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_key_id is not None:
            result['AccessKeyId'] = self.access_key_id

        if self.access_key_secret is not None:
            result['AccessKeySecret'] = self.access_key_secret

        if self.bucket is not None:
            result['Bucket'] = self.bucket

        if self.expiration is not None:
            result['Expiration'] = self.expiration

        if self.policy is not None:
            result['Policy'] = self.policy

        if self.post_access_key_id is not None:
            result['PostAccessKeyId'] = self.post_access_key_id

        if self.post_endpoint is not None:
            result['PostEndpoint'] = self.post_endpoint

        if self.region is not None:
            result['Region'] = self.region

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        if self.signature is not None:
            result['Signature'] = self.signature

        if self.signed_url is not None:
            result['SignedUrl'] = self.signed_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessKeyId') is not None:
            self.access_key_id = m.get('AccessKeyId')

        if m.get('AccessKeySecret') is not None:
            self.access_key_secret = m.get('AccessKeySecret')

        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')

        if m.get('Expiration') is not None:
            self.expiration = m.get('Expiration')

        if m.get('Policy') is not None:
            self.policy = m.get('Policy')

        if m.get('PostAccessKeyId') is not None:
            self.post_access_key_id = m.get('PostAccessKeyId')

        if m.get('PostEndpoint') is not None:
            self.post_endpoint = m.get('PostEndpoint')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        if m.get('Signature') is not None:
            self.signature = m.get('Signature')

        if m.get('SignedUrl') is not None:
            self.signed_url = m.get('SignedUrl')

        return self

