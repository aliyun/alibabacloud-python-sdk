# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddSmsTemplateRequest(DaraModel):
    def __init__(
        self,
        owner_id: int = None,
        remark: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        template_content: str = None,
        template_name: str = None,
        template_type: int = None,
    ):
        self.owner_id = owner_id
        # The description for the SMS template application. The length must not exceed 100 characters.
        # 
        # This is reference information for template review. Providing a complete application description helps reviewers understand your business scenario and improves review efficiency. Guidelines:
        # 
        # - You can provide the usage scenario of business that has been launched.
        # - You can provide SMS examples for real scenarios to demonstrate your business scenario.
        # - You can provide the variable parameter content, describing the business usage scenario in detail and the reason for choosing this variable attribute.
        # - You can provide website links of actual business, registered domain addresses, app market download links, and so on.
        # - For login scenarios, you can provide a test account and password.
        # 
        # This parameter is required.
        self.remark = remark
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The template content. The length must not exceed 500 characters.
        # 
        # The template content and variable content must comply with the [SMS template specifications](https://help.aliyun.com/document_detail/463161.html); otherwise, the template review will fail. You can also view common template examples on the [Apply for template](https://dysms.console.aliyun.com/domestic/text/template/add) page. Using example templates can improve review efficiency and success rate. For variable specifications, see [TemplateContent parameter variable specifications](https://help.aliyun.com/document_detail/2806243.html).
        # 
        # This parameter is required.
        self.template_content = template_content
        # The template name. The length must not exceed 30 characters.
        # 
        # This parameter is required.
        self.template_name = template_name
        # The SMS type. Valid values:
        # 
        # - **0**: verification code.
        # - **1**: notification SMS.
        # - **2**: promotional SMS.
        # - **3**: international/Hong Kong, Macao, and Taiwan messages.
        # 
        # > Only enterprise-verified users can apply for promotional SMS and international/Hong Kong, Macao, and Taiwan messages. For details about the differences between individual and enterprise user privileges, see [Usage notes](https://help.aliyun.com/document_detail/55324.html).
        # 
        # This parameter is required.
        self.template_type = template_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.template_content is not None:
            result['TemplateContent'] = self.template_content

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        if self.template_type is not None:
            result['TemplateType'] = self.template_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('TemplateContent') is not None:
            self.template_content = m.get('TemplateContent')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')

        return self

