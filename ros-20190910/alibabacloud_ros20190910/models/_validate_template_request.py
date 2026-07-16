# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ValidateTemplateRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        region_id: str = None,
        template_body: str = None,
        template_url: str = None,
        update_info_options: List[str] = None,
        validation_option: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests.
        # 
        # The token can be up to 64 characters in length, and can contain letters, digits, hyphens (-), and underscores (_).
        # 
        # For more information, see [Ensure idempotence](https://help.aliyun.com/document_detail/134212.html).
        self.client_token = client_token
        # The region ID of the template. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/131035.html) operation to query the most recent region list.
        self.region_id = region_id
        # The structure that contains the template body. The template body must be 1 to 524,288 bytes in length.\\
        # If the length of the template body exceeds the upper limit, we recommend that you add parameters to the HTTP POST request body to prevent request failures caused by excessively long URLs.\\
        # You can specify the TemplateBody or TemplateURL parameter, but not both parameters.
        self.template_body = template_body
        # The URL of the file that contains the template body. The URL must point to a template that is located on an HTTP web server or in an Object Storage Service (OSS) bucket, such as oss://ros/template/demo or oss://ros/template/demo?RegionId=cn-hangzhou. The template body can be up to 524,288 bytes in length.
        # 
        # > If you do not specify the region ID of the OSS bucket, the value of RegionId is used.
        # 
        # You can specify one of TemplateBody and TemplateURL, but not both of them. The URL can be up to 1,024 bytes in length.\\
        self.template_url = template_url
        # The options that are used to control the generation of information about the stack update. You can specify up to two options.
        self.update_info_options = update_info_options
        # Specifies whether to enable additional validation for the template. Valid values:
        # 
        # *   None (default): does not enable additional validation.
        # *   EnableTerraformValidation: runs the `terraform validate` command in the Terraform CLI to enable additional validation for a Terraform template.
        # *   EnableFastTerraformValidation: runs a command that is similar to the `terraform validate` command in the Terraform CLI to enable additional validation for a Terraform template.
        # 
        # > Compared with the EnableTerraformValidation method, the EnableFastTerraformValidation method validates a template at a faster speed but a lower integrity level.
        self.validation_option = validation_option

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.template_body is not None:
            result['TemplateBody'] = self.template_body

        if self.template_url is not None:
            result['TemplateURL'] = self.template_url

        if self.update_info_options is not None:
            result['UpdateInfoOptions'] = self.update_info_options

        if self.validation_option is not None:
            result['ValidationOption'] = self.validation_option

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('TemplateBody') is not None:
            self.template_body = m.get('TemplateBody')

        if m.get('TemplateURL') is not None:
            self.template_url = m.get('TemplateURL')

        if m.get('UpdateInfoOptions') is not None:
            self.update_info_options = m.get('UpdateInfoOptions')

        if m.get('ValidationOption') is not None:
            self.validation_option = m.get('ValidationOption')

        return self

