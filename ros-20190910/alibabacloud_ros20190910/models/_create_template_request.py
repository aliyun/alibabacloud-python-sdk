# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ros20190910 import models as main_models
from darabonba.model import DaraModel

class CreateTemplateRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        resource_group_id: str = None,
        tags: List[main_models.CreateTemplateRequestTags] = None,
        template_body: str = None,
        template_name: str = None,
        template_url: str = None,
        validation_options: List[str] = None,
    ):
        # The description of the template. The description can be up to 256 characters in length.
        self.description = description
        # The ID of the resource group.\\
        # For more information about resource groups, see [Resource groups](https://help.aliyun.com/document_detail/94475.html).
        self.resource_group_id = resource_group_id
        # The tags of the template.
        self.tags = tags
        # The structure of the template body. The template body must be 1 to 524,288 bytes in length. If the length of the template body exceeds the upper limit, we recommend that you add parameters to the HTTP POST request body to prevent request failures caused by excessively long URLs.
        # 
        # > You must specify TemplateBody or TemplateURL.
        # 
        # You can create a Terraform template based on your business requirements. The following sample code provides an example on how to create a Terraform template:
        # 
        #     {
        #       "ROSTemplateFormatVersion": "2015-09-01",
        #       "Transform": "Aliyun::Terraform-v1.0",
        #       "Workspace": {
        #         "main.tf": "variable  \\"name\\" {  default = \\"auto_provisioning_group\\"}"
        #       },
        #       "Outputs": {}
        #     }
        # 
        # For more information about Terraform templates, see [Structure of Terraform templates](https://help.aliyun.com/document_detail/184397.html).
        self.template_body = template_body
        # The name of the template.\\
        # The name can be up to 255 characters in length and can contain digits, letters, hyphens (-), and underscores (_). It must start with a digit or a letter.
        # 
        # This parameter is required.
        self.template_name = template_name
        # The URL of the file that contains the template body. The URL must point to a template that is located on an HTTP or HTTPS web server or in an Alibaba Cloud Object Storage Service (OSS) bucket, such as oss://ros/stack-policy/demo or oss://ros/stack-policy/demo?RegionId=cn-hangzhou. The template body must be 1 to 1,024 bytes in length. If you do not specify the region of the OSS bucket, the value of RegionId is used.
        # 
        # > You must specify TemplateBody or TemplateURL.
        self.template_url = template_url
        self.validation_options = validation_options

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.template_body is not None:
            result['TemplateBody'] = self.template_body

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        if self.template_url is not None:
            result['TemplateURL'] = self.template_url

        if self.validation_options is not None:
            result['ValidationOptions'] = self.validation_options

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.CreateTemplateRequestTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('TemplateBody') is not None:
            self.template_body = m.get('TemplateBody')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        if m.get('TemplateURL') is not None:
            self.template_url = m.get('TemplateURL')

        if m.get('ValidationOptions') is not None:
            self.validation_options = m.get('ValidationOptions')

        return self

class CreateTemplateRequestTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of the template.
        # 
        # > Tags is optional. If you need to specify Tags, you must also specify Key.
        # 
        # This parameter is required.
        self.key = key
        # The tag value of the template.
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

