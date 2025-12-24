# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_slb20140515 import models as main_models
from darabonba.model import DaraModel

class UploadServerCertificateRequest(DaraModel):
    def __init__(
        self,
        ali_cloud_certificate_id: str = None,
        ali_cloud_certificate_name: str = None,
        ali_cloud_certificate_region_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        private_key: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        server_certificate: str = None,
        server_certificate_name: str = None,
        tag: List[main_models.UploadServerCertificateRequestTag] = None,
    ):
        # AliCloud certificate ID.
        self.ali_cloud_certificate_id = ali_cloud_certificate_id
        # AliCloud certificate name.
        self.ali_cloud_certificate_name = ali_cloud_certificate_name
        # The region ID of AliCloud certificate.
        self.ali_cloud_certificate_region_id = ali_cloud_certificate_region_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The private key of the certificate.
        self.private_key = private_key
        # The region ID of the CLB instance.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/27584.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The server certificate to be uploaded.
        self.server_certificate = server_certificate
        # The name of the server certificate.
        # 
        # The name must be 1 to 80 characters in length. It must start with an English letter. It can contain letters, numbers, periods (.), underscores (_), and hyphens (-).
        self.server_certificate_name = server_certificate_name
        # The tags.
        self.tag = tag

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ali_cloud_certificate_id is not None:
            result['AliCloudCertificateId'] = self.ali_cloud_certificate_id

        if self.ali_cloud_certificate_name is not None:
            result['AliCloudCertificateName'] = self.ali_cloud_certificate_name

        if self.ali_cloud_certificate_region_id is not None:
            result['AliCloudCertificateRegionId'] = self.ali_cloud_certificate_region_id

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.private_key is not None:
            result['PrivateKey'] = self.private_key

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.server_certificate is not None:
            result['ServerCertificate'] = self.server_certificate

        if self.server_certificate_name is not None:
            result['ServerCertificateName'] = self.server_certificate_name

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliCloudCertificateId') is not None:
            self.ali_cloud_certificate_id = m.get('AliCloudCertificateId')

        if m.get('AliCloudCertificateName') is not None:
            self.ali_cloud_certificate_name = m.get('AliCloudCertificateName')

        if m.get('AliCloudCertificateRegionId') is not None:
            self.ali_cloud_certificate_region_id = m.get('AliCloudCertificateRegionId')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PrivateKey') is not None:
            self.private_key = m.get('PrivateKey')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('ServerCertificate') is not None:
            self.server_certificate = m.get('ServerCertificate')

        if m.get('ServerCertificateName') is not None:
            self.server_certificate_name = m.get('ServerCertificateName')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.UploadServerCertificateRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class UploadServerCertificateRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of tag N. Valid values of N: **1 to 20**. The tag key cannot be an empty string.
        # 
        # The tag key can be up to 64 characters in length, and cannot contain `http://` or `https://`. The tag key cannot start with `aliyun` or `acs:`.
        self.key = key
        # The value of tag N. Valid values of N: **1 to 20**. The tag value can be an empty string. The tag value can be up to 128 characters in length and cannot contain `http://` or `https://`. The tag value cannot start with `aliyun` and `acs:`.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

