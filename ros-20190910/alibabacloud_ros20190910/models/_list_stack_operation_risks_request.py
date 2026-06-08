# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListStackOperationRisksRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        operation_type: str = None,
        ram_role_name: str = None,
        region_id: str = None,
        retain_all_resources: bool = None,
        retain_resources: List[str] = None,
        stack_id: str = None,
        template_body: str = None,
        template_id: str = None,
        template_url: str = None,
        template_version: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can be up to 64 characters in length, and can contain letters, digits, hyphens (-), and underscores (_). For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/134212.html).
        self.client_token = client_token
        # The type of the operation of which you want to detect risks. Valid values:
        # 
        # *   DeleteStack: detects high risks that may arise in resources when you delete a stack.
        # *   CreateStack: detects the missing permissions when you fail to create a stack.
        self.operation_type = operation_type
        # The name of the RAM role.
        # 
        # *   If you specify a RAM role, ROS creates stacks based on the permissions that are granted to the RAM role and uses the credentials of the RAM role to call the API operations of Alibaba Cloud services.
        # *   If you do not specify a RAM role, ROS creates stacks based on the permissions of your Alibaba Cloud account.
        # 
        # The name of the RAM role can be up to 64 bytes in length.
        self.ram_role_name = ram_role_name
        # The region ID of the stack. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/131035.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # Specifies whether to retain all resources in the stack. Valid values:
        # 
        # *   true
        # *   false (default)
        # 
        # > This parameter takes effect only if you set OperationType to DeleteStack.
        self.retain_all_resources = retain_all_resources
        # The list of resources to retain.
        # 
        # > This parameter takes effect only if you set OperationType to DeleteStack.
        self.retain_resources = retain_resources
        # The ID of the stack.
        self.stack_id = stack_id
        # The structure that contains the template body. The template body must be 1 to 524,288 bytes in length. If the length of the template body exceeds the upper limit, we recommend that you add parameters to the HTTP POST request body to prevent request failures caused by excessively long URLs.
        # 
        # >  You must and can specify only one of the following parameters: TemplateBody, TemplateURL, TemplateId, and TemplateScratchId.
        self.template_body = template_body
        # The ID of the template. This parameter applies to shared and private templates.
        # 
        # > You must specify one of TemplateBody, TemplateURL, TemplateId, and TemplateScratchId.
        self.template_id = template_id
        # The URL of the file that contains the template body. The URL must point to a template that is located on an HTTP or HTTPS web server or in an Object Storage Service (OSS) bucket, such as oss://ros/stack-policy/demo and oss://ros/stack-policy/demo?RegionId=cn-hangzhou. The template body can be up to 524,288 bytes in length. If you do not specify RegionId in the URL, the region ID of the stack is used.
        # 
        # > You must specify one of TemplateBody, TemplateURL, TemplateId, and TemplateScratchId.
        self.template_url = template_url
        # The version of the template.
        # 
        # > This parameter takes effect only if you specify TemplateId.
        self.template_version = template_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.operation_type is not None:
            result['OperationType'] = self.operation_type

        if self.ram_role_name is not None:
            result['RamRoleName'] = self.ram_role_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.retain_all_resources is not None:
            result['RetainAllResources'] = self.retain_all_resources

        if self.retain_resources is not None:
            result['RetainResources'] = self.retain_resources

        if self.stack_id is not None:
            result['StackId'] = self.stack_id

        if self.template_body is not None:
            result['TemplateBody'] = self.template_body

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.template_url is not None:
            result['TemplateURL'] = self.template_url

        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('OperationType') is not None:
            self.operation_type = m.get('OperationType')

        if m.get('RamRoleName') is not None:
            self.ram_role_name = m.get('RamRoleName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RetainAllResources') is not None:
            self.retain_all_resources = m.get('RetainAllResources')

        if m.get('RetainResources') is not None:
            self.retain_resources = m.get('RetainResources')

        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')

        if m.get('TemplateBody') is not None:
            self.template_body = m.get('TemplateBody')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('TemplateURL') is not None:
            self.template_url = m.get('TemplateURL')

        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')

        return self

