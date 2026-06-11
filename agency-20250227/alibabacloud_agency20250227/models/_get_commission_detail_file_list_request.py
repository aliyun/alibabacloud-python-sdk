# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetCommissionDetailFileListRequest(DaraModel):
    def __init__(
        self,
        bill_month: str = None,
        oss_access_key_id: str = None,
        oss_access_key_secret: str = None,
        oss_bucket_name: str = None,
        oss_endpoint: str = None,
        oss_region: str = None,
        oss_security_token: str = None,
    ):
        # Billing month
        self.bill_month = bill_month
        # AccessKeyID used to upload files to OSS
        self.oss_access_key_id = oss_access_key_id
        # AccessKeySecret used to upload files to OSS
        self.oss_access_key_secret = oss_access_key_secret
        # OSS bucket
        self.oss_bucket_name = oss_bucket_name
        # Edge zone of the Region where the OSS bucket for file sharing is located
        self.oss_endpoint = oss_endpoint
        # Region to which the current OSS bucket belongs
        self.oss_region = oss_region
        # STS token used to upload files to OSS
        self.oss_security_token = oss_security_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bill_month is not None:
            result['BillMonth'] = self.bill_month

        if self.oss_access_key_id is not None:
            result['OssAccessKeyId'] = self.oss_access_key_id

        if self.oss_access_key_secret is not None:
            result['OssAccessKeySecret'] = self.oss_access_key_secret

        if self.oss_bucket_name is not None:
            result['OssBucketName'] = self.oss_bucket_name

        if self.oss_endpoint is not None:
            result['OssEndpoint'] = self.oss_endpoint

        if self.oss_region is not None:
            result['OssRegion'] = self.oss_region

        if self.oss_security_token is not None:
            result['OssSecurityToken'] = self.oss_security_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillMonth') is not None:
            self.bill_month = m.get('BillMonth')

        if m.get('OssAccessKeyId') is not None:
            self.oss_access_key_id = m.get('OssAccessKeyId')

        if m.get('OssAccessKeySecret') is not None:
            self.oss_access_key_secret = m.get('OssAccessKeySecret')

        if m.get('OssBucketName') is not None:
            self.oss_bucket_name = m.get('OssBucketName')

        if m.get('OssEndpoint') is not None:
            self.oss_endpoint = m.get('OssEndpoint')

        if m.get('OssRegion') is not None:
            self.oss_region = m.get('OssRegion')

        if m.get('OssSecurityToken') is not None:
            self.oss_security_token = m.get('OssSecurityToken')

        return self

