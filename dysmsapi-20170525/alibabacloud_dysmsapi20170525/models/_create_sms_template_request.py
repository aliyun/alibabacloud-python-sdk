# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateSmsTemplateRequest(DaraModel):
    def __init__(
        self,
        apply_scene_content: str = None,
        intl_type: int = None,
        more_data: List[str] = None,
        owner_id: int = None,
        related_sign_name: str = None,
        remark: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        template_content: str = None,
        template_name: str = None,
        template_rule: str = None,
        template_type: int = None,
        traffic_driving: str = None,
    ):
        # If there is an applicable scenario, you can fill it in.
        self.apply_scene_content = apply_scene_content
        # International/Hong Kong, Macao, and Taiwan template type. When the **TemplateType** parameter is **3**, this parameter is required for international/Hong Kong, Macao, and Taiwan templates, with values:
        # - **0**: Verification code.
        # - **1**: SMS notification.
        # - **2**: Promotional message.
        self.intl_type = intl_type
        # Additional materials you can upload, such as business proof documents or screenshots, to help reviewers understand your business details.
        # 
        # This parameter is optional; please fill it in according to actual needs.
        self.more_data = more_data
        self.owner_id = owner_id
        # The signature name that the template needs to be associated with. The associated SMS signature must have passed the review.
        # 
        # This parameter is mandatory when the TemplateType parameter is **0**, **1**, or **2**.
        # 
        # <notice>Associating a signature can expedite the review process. Note that this associated signature is unrelated to the signature selected when sending SMS messages.</notice>
        self.related_sign_name = related_sign_name
        # Please describe the business scenario where you use SMS or provide an online link to the scenario, along with a complete example of the SMS (with variable contents filled), as complete information helps increase the template approval rate. Failure to follow guidelines or leaving this field blank may affect the approval of your template.
        self.remark = remark
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Template content, up to 500 characters in length.
        # 
        # Both the template content and variable content must comply with SMS specifications; otherwise, the template will fail the review. You can also view common template examples on the template application page. Using sample templates can enhance review efficiency and success rates. For variable specifications, see [TemplateContent Variable Parameter Filling Specifications](https://help.aliyun.com/zh/sms/templaterule-template-variable-parameter-filling-example).
        # 
        # This parameter is required.
        self.template_content = template_content
        # Template name, up to 30 characters in length.
        # 
        # This parameter is required.
        self.template_name = template_name
        # Template variable rules.
        # 
        # For filling in variable rules, refer to the [Sample Documentation](https://help.aliyun.com/zh/sms/templaterule-template-variable-parameter-filling-example).
        self.template_rule = template_rule
        # SMS type. Values:
        # 
        # - **0**: Verification code.
        # - **1**: SMS notification.
        # - **2**: Promotional message.
        # - **3**: International/Hong Kong, Macao, and Taiwan messages.
        # 
        # > Only enterprise-verified users can apply for promotional messages and international/Hong Kong, Macao, and Taiwan messages. For details on the differences between personal and enterprise user rights, please refer to [Usage Instructions](https://help.aliyun.com/zh/sms/user-guide/usage-notes?spm=a2c4g.11186623.0.0.67447f576NJnE8).
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

        if self.more_data is not None:
            result['MoreData'] = self.more_data

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
            self.more_data = m.get('MoreData')

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

