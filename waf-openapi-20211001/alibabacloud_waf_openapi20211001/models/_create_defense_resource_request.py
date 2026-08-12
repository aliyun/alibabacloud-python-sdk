# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class CreateDefenseResourceRequest(DaraModel):
    def __init__(
        self,
        custom_headers: List[str] = None,
        description: str = None,
        detail: str = None,
        instance_id: str = None,
        owner_user_id: str = None,
        pattern: str = None,
        product: str = None,
        region_id: str = None,
        resource: str = None,
        resource_group: str = None,
        resource_manager_resource_group_id: str = None,
        resource_origin: str = None,
        tag: List[main_models.CreateDefenseResourceRequestTag] = None,
        xff_status: int = None,
    ):
        # The list of specified header fields.
        # > When XffStatus is set to 1, the first IP in the specified header field is used as the client source IP to prevent XFF spoofing. When multiple headers are specified, the system attempts to obtain the source IP from each header in order. If the first header does not contain an IP, the system tries the second header, and so on. If no specified header contains an IP, the first IP in the X-Forwarded-For header is used. When XffStatus is set to 1, the IP is obtained from the first available header.
        self.custom_headers = custom_headers
        # The description of the protected object.
        self.description = description
        # The specific parameter information of the protected object, which is a string converted from a JSON object constructed with a series of parameters.
        # 
        # > The parameters vary depending on the specified **cloud product** (**Product**) and **protection mode** (**Pattern**). For more information, see **Detail parameter description for protected objects**.
        # 
        # >Notice: When **Product** is set to **ecs**, **clb4**, **clb7**, or **nlb**, domain names connected to regions in the Chinese mainland must have completed ICP filing.</notice>
        # 
        # This parameter is required.
        self.detail = detail
        # The ID of the WAF instance.
        # 
        # > You can call [DescribeInstance](https://help.aliyun.com/document_detail/433756.html) to query the ID of the current WAF instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The ID of the account to which the protected object belongs in multi-account scenarios. By default, the protected object belongs to the WAF administrator account.
        self.owner_user_id = owner_user_id
        # The protection mode of the protected object. Valid values:
        # 
        # - **domain**: domain name-based protection.
        # 
        # - **multi_service**: hybrid cloud service-based protection.
        # 
        # > Currently, only the following combinations are supported: when **Product** is set to **alb**, **ecs**, **clb4**, **clb7**, or **nlb**, **Pattern** must be set to **domain**. When **Product** is set to **waf**, **Pattern** must be set to **multi_service**.
        # 
        # This parameter is required.
        self.pattern = pattern
        # The cloud product name. Valid values:
        # 
        # - **alb**: Application Load Balancer (ALB).
        # 
        # - **ecs**: Elastic Compute Service (ECS).
        # 
        # - **clb4**: Classic Load Balancer (CLB) Layer 4 access.
        # 
        # - **clb7**: Classic Load Balancer (CLB) Layer 7 access.
        # 
        # - **nlb**: Network Load Balancer (NLB).
        # 
        # - **waf**: Web Application Firewall (WAF).
        # 
        # This parameter is required.
        self.product = product
        # The region where the WAF instance resides. Valid values:
        # 
        # - **cn-hangzhou**: the Chinese mainland.
        # 
        # - **ap-southeast-1**: outside the Chinese mainland.
        self.region_id = region_id
        # The name of the protected object.
        # > 
        # > - Only protected objects in hybrid cloud service mode support custom protected object names.
        self.resource = resource
        # The name of the protection group to which the protected object is added. This parameter is optional.
        self.resource_group = resource_group
        # The Alibaba Cloud resource group ID.
        self.resource_manager_resource_group_id = resource_manager_resource_group_id
        # The source of the protected object. Valid values:
        # 
        # - **custom**: user-defined.
        # 
        # This parameter is required.
        self.resource_origin = resource_origin
        # The tag list, which contains up to 20 items.
        self.tag = tag
        # Specifies whether XFF proxy is enabled for the protected object. Valid values:
        # 
        # - **0**: Disabled (default).
        # 
        # - **1**: Enabled.
        self.xff_status = xff_status

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
        if self.custom_headers is not None:
            result['CustomHeaders'] = self.custom_headers

        if self.description is not None:
            result['Description'] = self.description

        if self.detail is not None:
            result['Detail'] = self.detail

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.owner_user_id is not None:
            result['OwnerUserId'] = self.owner_user_id

        if self.pattern is not None:
            result['Pattern'] = self.pattern

        if self.product is not None:
            result['Product'] = self.product

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource is not None:
            result['Resource'] = self.resource

        if self.resource_group is not None:
            result['ResourceGroup'] = self.resource_group

        if self.resource_manager_resource_group_id is not None:
            result['ResourceManagerResourceGroupId'] = self.resource_manager_resource_group_id

        if self.resource_origin is not None:
            result['ResourceOrigin'] = self.resource_origin

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.xff_status is not None:
            result['XffStatus'] = self.xff_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomHeaders') is not None:
            self.custom_headers = m.get('CustomHeaders')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Detail') is not None:
            self.detail = m.get('Detail')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('OwnerUserId') is not None:
            self.owner_user_id = m.get('OwnerUserId')

        if m.get('Pattern') is not None:
            self.pattern = m.get('Pattern')

        if m.get('Product') is not None:
            self.product = m.get('Product')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Resource') is not None:
            self.resource = m.get('Resource')

        if m.get('ResourceGroup') is not None:
            self.resource_group = m.get('ResourceGroup')

        if m.get('ResourceManagerResourceGroupId') is not None:
            self.resource_manager_resource_group_id = m.get('ResourceManagerResourceGroupId')

        if m.get('ResourceOrigin') is not None:
            self.resource_origin = m.get('ResourceOrigin')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateDefenseResourceRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('XffStatus') is not None:
            self.xff_status = m.get('XffStatus')

        return self

class CreateDefenseResourceRequestTag(DaraModel):
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

