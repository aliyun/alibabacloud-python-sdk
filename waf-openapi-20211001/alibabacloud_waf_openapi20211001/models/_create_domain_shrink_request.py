# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class CreateDomainShrinkRequest(DaraModel):
    def __init__(
        self,
        access_type: str = None,
        domain: str = None,
        instance_id: str = None,
        listen_shrink: str = None,
        redirect_shrink: str = None,
        region_id: str = None,
        resource_manager_resource_group_id: str = None,
        tag: List[main_models.CreateDomainShrinkRequestTag] = None,
    ):
        # The access type of the WAF instance. Valid values:
        # 
        # - **share** (default): onboarding by using a CNAME record.
        # 
        # - **hybrid_cloud_cname**: onboarding by using a hybrid cloud CNAME record.
        self.access_type = access_type
        # The domain name that you want to add.
        # 
        # This parameter is required.
        self.domain = domain
        # The ID of the WAF instance.
        # 
        # > Call the [DescribeInstance](https://help.aliyun.com/document_detail/433756.html) operation to query the ID of the WAF instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The listening configurations.
        # 
        # This parameter is required.
        self.listen_shrink = listen_shrink
        # The forwarding configurations.
        # 
        # This parameter is required.
        self.redirect_shrink = redirect_shrink
        # The region where the WAF instance resides. Valid values:
        # 
        # - **cn-hangzhou**: The Chinese mainland.
        # 
        # - **ap-southeast-1**: Outside the Chinese mainland.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the Alibaba Cloud resource group.
        self.resource_manager_resource_group_id = resource_manager_resource_group_id
        # The tags. You can specify up to 20 tags.
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
        if self.access_type is not None:
            result['AccessType'] = self.access_type

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.listen_shrink is not None:
            result['Listen'] = self.listen_shrink

        if self.redirect_shrink is not None:
            result['Redirect'] = self.redirect_shrink

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_manager_resource_group_id is not None:
            result['ResourceManagerResourceGroupId'] = self.resource_manager_resource_group_id

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessType') is not None:
            self.access_type = m.get('AccessType')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Listen') is not None:
            self.listen_shrink = m.get('Listen')

        if m.get('Redirect') is not None:
            self.redirect_shrink = m.get('Redirect')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceManagerResourceGroupId') is not None:
            self.resource_manager_resource_group_id = m.get('ResourceManagerResourceGroupId')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateDomainShrinkRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class CreateDomainShrinkRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
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

