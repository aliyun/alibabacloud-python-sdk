# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateSmsTemplateShrinkRequest(DaraModel):
    def __init__(
        self,
        apply_scene_content: str = None,
        intl_type: int = None,
        more_data_shrink: str = None,
        owner_id: int = None,
        related_sign_name: str = None,
        remark: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        template_code: str = None,
        template_content: str = None,
        template_name: str = None,
        template_rule: str = None,
        template_type: int = None,
        traffic_driving: str = None,
    ):
        # Application scenarios, instructions as follows:
        # - For registered websites, please enter the MIIT-registered domain with HTTP or HTTPS.
        # - For launched apps, provide the app store display link with HTTP or HTTPS, ensuring the app is online.
        # - For public accounts or mini-programs, enter the full name of the public account or mini-program, ensuring they are online.
        # - For e-commerce platform stores, applicable only to enterprise users, enter the display link of the e-commerce store with HTTP or HTTPS.
        self.apply_scene_content = apply_scene_content
        # International/Hong Kong, Macao, and Taiwan template type. When the **TemplateType** parameter is **3**, this parameter is required for international/Hong Kong, Macao, and Taiwan templates, with values:
        # - **0**: Verification code.
        # - **1**: SMS notification.
        # - **2**: Promotional SMS.
        self.intl_type = intl_type
        # Additional information, such as uploading business proof documents or screenshots, to help reviewers understand your business details. Optional and can be left unset.
        self.more_data_shrink = more_data_shrink
        self.owner_id = owner_id
        # SMS signature associated with the template during the application.
        self.related_sign_name = related_sign_name
        # Explanation for the SMS template application, which serves as a reference for template review.
        self.remark = remark
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Template Code of an unapproved template.
        # 
        # This parameter is required.
        self.template_code = template_code
        # Template content, up to 500 characters in length.
        # 
        # Both the template content and variable content must comply with SMS regulations; otherwise, the template will fail the review. You can also view common template examples on the template application page. Using sample templates can enhance review efficiency and success rates. Variable specifications can be found in [TemplateContent Parameter Variable Specifications](https://help.aliyun.com/zh/sms/templaterule-template-variable-parameter-filling-example?spm).
        # 
        # This parameter is required.
        self.template_content = template_content
        # Template name, up to 30 characters in length.
        # 
        # This parameter is required.
        self.template_name = template_name
        # Template variable rules.
        # 
        # For guidance on filling variable rules, refer to the [Sample Documentation](https://help.aliyun.com/zh/sms/templaterule-template-variable-parameter-filling-example?spm).
        self.template_rule = template_rule
        # SMS type. Values:
        # 
        # - **0**: Verification code.
        # - **1**: SMS notification.
        # - **2**: Promotional SMS.
        # - **3**: International/Hong Kong, Macao, and Taiwan messages.
        # 
        # > Only enterprise-certified users can apply for promotional SMS and international/Hong Kong, Macao, and Taiwan messages. Details on differences between personal and enterprise user rights are available in [Usage Guidelines](https://help.aliyun.com/zh/sms/user-guide/usage-notes?spm=a2c4g.11186623.0.0.67447f576NJnE8).
        # 
        # This parameter is required.
        self.template_type = template_type
        self.traffic_driving = traffic_driving

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.apply_scene_content is not None:
            result['ApplySceneContent'] = self.apply_scene_content

        if self.intl_type is not None:
            result['IntlType'] = self.intl_type

        if self.more_data_shrink is not None:
            result['MoreData'] = self.more_data_shrink

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.related_sign_name is not None:
            result['RelatedSignName'] = self.related_sign_name

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

        if self.template_rule is not None:
            result['TemplateRule'] = self.template_rule

        if self.template_type is not None:
            result['TemplateType'] = self.template_type

        if self.traffic_driving is not None:
            result['TrafficDriving'] = self.traffic_driving

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplySceneContent') is not None:
            self.apply_scene_content = m.get('ApplySceneContent')

        if m.get('IntlType') is not None:
            self.intl_type = m.get('IntlType')

        if m.get('MoreData') is not None:
            self.more_data_shrink = m.get('MoreData')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RelatedSignName') is not None:
            self.related_sign_name = m.get('RelatedSignName')

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

        if m.get('TemplateRule') is not None:
            self.template_rule = m.get('TemplateRule')

        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')

        if m.get('TrafficDriving') is not None:
            self.traffic_driving = m.get('TrafficDriving')

        return self

