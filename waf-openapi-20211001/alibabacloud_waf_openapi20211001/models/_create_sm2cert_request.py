# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateSM2CertRequest(DaraModel):
    def __init__(
        self,
        cert_name: str = None,
        encrypt_certificate: str = None,
        encrypt_private_key: str = None,
        instance_id: str = None,
        region_id: str = None,
        resource_manager_resource_group_id: str = None,
        sign_certificate: str = None,
        sign_private_key: str = None,
    ):
        # The name of the SM certificate.
        self.cert_name = cert_name
        # The content of the SM certificate.
        self.encrypt_certificate = encrypt_certificate
        # The private key of the SM certificate.
        self.encrypt_private_key = encrypt_private_key
        # The ID of the WAF instance.
        # 
        # >  You can call the [DescribeInstance](https://help.aliyun.com/document_detail/433756.html) operation to query the ID of the WAF instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The region in which the WAF instance is deployed. Valid values:
        # 
        # *   **cn-hangzhou**: Chinese mainland.
        # *   **ap-southeast-1**: outside the Chinese mainland.
        self.region_id = region_id
        # The ID of the Alibaba Cloud resource group.
        self.resource_manager_resource_group_id = resource_manager_resource_group_id
        # The content of the signing certificate for the SM certificate.
        self.sign_certificate = sign_certificate
        # The private key of the signing certificate for the SM certificate.
        self.sign_private_key = sign_private_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cert_name is not None:
            result['CertName'] = self.cert_name

        if self.encrypt_certificate is not None:
            result['EncryptCertificate'] = self.encrypt_certificate

        if self.encrypt_private_key is not None:
            result['EncryptPrivateKey'] = self.encrypt_private_key

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_manager_resource_group_id is not None:
            result['ResourceManagerResourceGroupId'] = self.resource_manager_resource_group_id

        if self.sign_certificate is not None:
            result['SignCertificate'] = self.sign_certificate

        if self.sign_private_key is not None:
            result['SignPrivateKey'] = self.sign_private_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')

        if m.get('EncryptCertificate') is not None:
            self.encrypt_certificate = m.get('EncryptCertificate')

        if m.get('EncryptPrivateKey') is not None:
            self.encrypt_private_key = m.get('EncryptPrivateKey')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceManagerResourceGroupId') is not None:
            self.resource_manager_resource_group_id = m.get('ResourceManagerResourceGroupId')

        if m.get('SignCertificate') is not None:
            self.sign_certificate = m.get('SignCertificate')

        if m.get('SignPrivateKey') is not None:
            self.sign_private_key = m.get('SignPrivateKey')

        return self

