# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifySmsTemplateRequest(DaraModel):
    def __init__(
        self,
        owner_id: int = None,
        remark: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        template_code: str = None,
        template_content: str = None,
        template_name: str = None,
        template_type: int = None,
    ):
        self.owner_id = owner_id
        # The description of the SMS template application. The description cannot exceed 100 characters in length.
        # 
        # This information helps reviewers understand your business scenarios and improves review efficiency. Guidelines:
        # 
        # - Provide the use case of your live business.
        # - Provide SMS examples for real scenarios to reflect your business scenarios.
        # - Provide variable values and describe in detail the business use case and the reason for choosing the variable attributes.
        # - Provide the website URL, registered domain name, or application marketplace download link of the actual business.
        # - For logon scenarios, provide the test account and password.
        # 
        # This parameter is required.
        self.remark = remark
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The code of the SMS template that failed the review.
        # 
        # - Call the [QuerySmsTemplateList](https://help.aliyun.com/document_detail/419288.html) operation to obtain the code of the SMS template that failed the review.
        # - View the code of the SMS template that failed the review on the [Templates](https://dysms.console.aliyun.com/domestic/text/template) page.
        # 
        # This parameter is required.
        self.template_code = template_code
        # The template content. The content cannot exceed 500 characters in length.
        # 
        # The template content and variable content must comply with the [SMS template specifications](https://help.aliyun.com/document_detail/463161.html). Otherwise, the template fails the review. You can view common template examples on the [Apply for Template](https://dysms.console.aliyun.com/domestic/text/template/add) page. Using sample templates can improve review efficiency and success rate. For variable specifications, see [TemplateContent variable specifications](https://help.aliyun.com/document_detail/2806243.html).
        # 
        # This parameter is required.
        self.template_content = template_content
        # The template name. The name must be 1 to 30 characters in length.
        # 
        # This parameter is required.
        self.template_name = template_name
        # The SMS type. Valid values:
        # 
        # - **0**: verification code.
        # - **1**: SMS notification.
        # - **2**: promotional message.
        # - **3**: international or Hong Kong, Macao, and Taiwan message.
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

        if self.template_code is not None:
            result['TemplateCode'] = self.template_code

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

        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')

        if m.get('TemplateContent') is not None:
            self.template_content = m.get('TemplateContent')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')

        return self

