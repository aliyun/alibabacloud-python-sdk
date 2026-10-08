# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_edas20170801 import models as main_models
from darabonba.model import DaraModel

class GetPackageStorageCredentialResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        credential: main_models.GetPackageStorageCredentialResponseBodyCredential = None,
        message: str = None,
        request_id: str = None,
    ):
        # The HTTP status code that is returned.
        self.code = code
        # The STS credential.
        self.credential = credential
        # The message that is returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.credential:
            self.credential.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.credential is not None:
            result['Credential'] = self.credential.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Credential') is not None:
            temp_model = main_models.GetPackageStorageCredentialResponseBodyCredential()
            self.credential = temp_model.from_map(m.get('Credential'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetPackageStorageCredentialResponseBodyCredential(DaraModel):
    def __init__(
        self,
        access_key_id: str = None,
        access_key_secret: str = None,
        bucket: str = None,
        expiration: str = None,
        key_prefix: str = None,
        oss_internal_endpoint: str = None,
        oss_public_endpoint: str = None,
        oss_vpc_endpoint: str = None,
        region_id: str = None,
        security_token: str = None,
    ):
        # The AccessKey ID of your account.
        self.access_key_id = access_key_id
        # The AccessKey secret of your account.
        self.access_key_secret = access_key_secret
        # The name of the OSS bucket.
        self.bucket = bucket
        # The time when the STS credential expires. Example: 2019-11-10T07:20:19Z.
        self.expiration = expiration
        # The object key prefix in Object Storage Service (OSS).
        self.key_prefix = key_prefix
        # The private endpoint of OSS.
        self.oss_internal_endpoint = oss_internal_endpoint
        # The public endpoint of OSS.
        self.oss_public_endpoint = oss_public_endpoint
        # The VPC endpoint of OSS.
        self.oss_vpc_endpoint = oss_vpc_endpoint
        # The ID of the region.
        self.region_id = region_id
        # The security token issued by STS.
        self.security_token = security_token

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

        if self.key_prefix is not None:
            result['KeyPrefix'] = self.key_prefix

        if self.oss_internal_endpoint is not None:
            result['OssInternalEndpoint'] = self.oss_internal_endpoint

        if self.oss_public_endpoint is not None:
            result['OssPublicEndpoint'] = self.oss_public_endpoint

        if self.oss_vpc_endpoint is not None:
            result['OssVpcEndpoint'] = self.oss_vpc_endpoint

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

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

        if m.get('KeyPrefix') is not None:
            self.key_prefix = m.get('KeyPrefix')

        if m.get('OssInternalEndpoint') is not None:
            self.oss_internal_endpoint = m.get('OssInternalEndpoint')

        if m.get('OssPublicEndpoint') is not None:
            self.oss_public_endpoint = m.get('OssPublicEndpoint')

        if m.get('OssVpcEndpoint') is not None:
            self.oss_vpc_endpoint = m.get('OssVpcEndpoint')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        return self

