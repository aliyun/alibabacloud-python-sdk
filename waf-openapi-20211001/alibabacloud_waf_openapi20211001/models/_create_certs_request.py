# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateCertsRequest(DaraModel):
    def __init__(
        self,
        cert_content: str = None,
        cert_key: str = None,
        cert_name: str = None,
        instance_id: str = None,
        region_id: str = None,
        resource_manager_resource_group_id: str = None,
    ):
        # The content of the certificate.
        self.cert_content = cert_content
        # The private key that corresponds to the certificate.
        self.cert_key = cert_key
        # The name of the certificate.
        self.cert_name = cert_name
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

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cert_content is not None:
            result['CertContent'] = self.cert_content

        if self.cert_key is not None:
            result['CertKey'] = self.cert_key

        if self.cert_name is not None:
            result['CertName'] = self.cert_name

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_manager_resource_group_id is not None:
            result['ResourceManagerResourceGroupId'] = self.resource_manager_resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertContent') is not None:
            self.cert_content = m.get('CertContent')

        if m.get('CertKey') is not None:
            self.cert_key = m.get('CertKey')

        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceManagerResourceGroupId') is not None:
            self.resource_manager_resource_group_id = m.get('ResourceManagerResourceGroupId')

        return self

