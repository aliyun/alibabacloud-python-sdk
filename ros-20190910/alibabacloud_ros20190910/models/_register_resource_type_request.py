# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RegisterResourceTypeRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        description: str = None,
        entity_type: str = None,
        resource_type: str = None,
        template_body: str = None,
        template_url: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests.\\
        # The token can be up to 64 characters in length, and can contain letters, digits, hyphens (-), and underscores (_).\\
        # For more information, see [Ensure idempotence](https://help.aliyun.com/document_detail/134212.html).
        self.client_token = client_token
        # The description of the resource type. The description can be up to 512 characters in length.
        self.description = description
        # The entity type. Set the value to Module.
        # 
        # This parameter is required.
        self.entity_type = entity_type
        # The resource type.
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The structure that contains the template body. The template body must be 1 to 524,288 bytes in length. The template body is used as the module content. If the length of the template body exceeds the upper limit, we recommend that you add parameters to the HTTP POST request body to prevent request failures caused by excessively long URLs.
        # 
        # 
        # > - This parameter takes effect only when EntityType is set to Module.
        # > - You can specify only one of the TemplateBody and TemplateURL parameters.
        self.template_body = template_body
        # The URL of the file that contains the template body. The URL must point to a template that is located on an HTTP or HTTPS web server or in an Object Storage Service (OSS) bucket, such as oss://ros/template/demo or oss://ros/template/demo?RegionId=cn-hangzhou. The template body can be up to 524,288 bytes in length. The template body is used as the module content.
        # 
        # > - If you do not specify the region ID of the OSS bucket, the value of RegionId is used.
        # > -  This parameter takes effect only when EntityType is set to Module.
        # > -  You can specify only one of the TemplateBody and TemplateURL parameters.
        # 
        # The URL can be up to 1,024 bytes in length.
        self.template_url = template_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.description is not None:
            result['Description'] = self.description

        if self.entity_type is not None:
            result['EntityType'] = self.entity_type

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.template_body is not None:
            result['TemplateBody'] = self.template_body

        if self.template_url is not None:
            result['TemplateURL'] = self.template_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('TemplateBody') is not None:
            self.template_body = m.get('TemplateBody')

        if m.get('TemplateURL') is not None:
            self.template_url = m.get('TemplateURL')

        return self

