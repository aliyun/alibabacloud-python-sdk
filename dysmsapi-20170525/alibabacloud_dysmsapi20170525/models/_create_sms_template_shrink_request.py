# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateSmsTemplateShrinkRequest(DaraModel):
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
        template_content: str = None,
        template_name: str = None,
        template_rule: str = None,
        template_type: int = None,
        traffic_driving: str = None,
    ):
        # The business scenario.
        # 
        # - If the associated signature\\"s use case is "Live App", `ApplySceneContent` must be an app URL that starts with `http://` or `https://`.
        # 
        # - This parameter is required if the associated signature\\"s use case is "Registered Trademark Name" or "organization name".
        self.apply_scene_content = apply_scene_content
        # The type of the template for international/Hong Kong, Macao, and Taiwan messages. This parameter is required when **TemplateType** is set to **3**. Valid values:
        # 
        # - **0**: notification message.
        # 
        # - **1**: promotional message.
        # 
        # - **2**: verification code.
        self.intl_type = intl_type
        # Additional information. You can upload supporting documents or business screenshots to help reviewers better understand your business scenario. If you are applying for a promotional message template (where `TemplateType` is `2`), you must upload user authorization materials. For more information, see [Specifications for Uploading User Authorization Materials](https://help.aliyun.com/document_detail/312341.html).
        self.more_data_shrink = more_data_shrink
        self.owner_id = owner_id
        # The name of the signature to associate with the template. The signature must be an approved signature.
        # 
        # >Notice: 
        # 
        # - This parameter is required if **TemplateType** is set to **0**, **1**, or **2**.
        # 
        # - Associating a signature can expedite the review process. The signature associated here is unrelated to the one you select when sending SMS messages.
        self.related_sign_name = related_sign_name
        # Describe the business scenario for the SMS messages, or provide a URL for online scenarios. You must also provide a complete SMS example with actual values for any variables. Complete information increases the chance of template approval. Templates that do not provide this information as specified may be rejected.
        self.remark = remark
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The template content. The content must be 500 characters or less.
        # 
        # The template content and variables must comply with the [SMS Template Specifications](https://help.aliyun.com/document_detail/463161.html). Templates that do not comply may be rejected. You can find common template examples on the [Apply for Template](https://dysms.console.aliyun.com/domestic/text/template/add) page. Using these examples can speed up the review process and increase the approval rate. For variable specifications, see [Variable Specifications for the TemplateContent Parameter](https://help.aliyun.com/document_detail/2806243.html).
        # 
        # This parameter is required.
        self.template_content = template_content
        # The template name. The name must be 30 characters or less.
        # 
        # This parameter is required.
        self.template_name = template_name
        # The rules for variables in the template. For instructions on how to define these rules, see [Sample Document](https://help.aliyun.com/document_detail/2806243.html).
        # 
        # > - This parameter is required if the message template contains variables.
        self.template_rule = template_rule
        # The SMS type. Valid values:
        # 
        # - **0**: verification code.
        # 
        # - **1**: notification message.
        # 
        # - **2**: promotional message.
        # 
        # - **3**: international/Hong Kong, Macao, and Taiwan messages.
        # 
        # > Only enterprise-verified users can apply for promotional messages or international/Hong Kong, Macao, and Taiwan messages. For more information about the differences in privileges between individual and enterprise users, see [Usage Notes](https://help.aliyun.com/zh/sms/user-guide/usage-notes?spm=a2c4g.11186623.0.0.67447f576NJnE8).
        # 
        # This parameter is required.
        self.template_type = template_type
        # >Warning: 
        # 
        # To control the security of SMS content, messages that contain traffic-driving information, such as phone numbers and links, may be blocked by carriers, which can lead to delivery failures. To reduce this risk, we recommend that you avoid including such information in message templates.
        # 
        # 
        # 
        # A JSON string that contains a list of traffic-driving information.
        # >Notice: The value must be a JSON array serialized into a string.
        # 
        # ### 1. Fields
        # 
        # {
        # "trafficDrivingType":"traffic driving type",
        # "trafficDrivingContent":"traffic driving content",
        # "variableName":"variable name",
        # "companyName":"organization name",
        # "organizationCode":"unified social credit code",
        # "icpNo":"ICP filing or license number",
        # "icpPicOssKey":"OSS key of the ICP filing screenshot",
        # "companyDifferentFromSignQuaReason":"Reason for the discrepancy between the organization name and the signature qualification"
        # }
        # 
        # ### 2. Notes
        # 
        # - If the content is not a variable, do not pass the `variableName` parameter.
        # 
        # - If the organization name is different from the one in the signature qualification, pass the `companyDifferentFromSignQuaReason` parameter.
        # 
        # - If `trafficDrivingType` is set to `DOMAIN`, all parameters in this object are required.
        # 
        # - If `trafficDrivingType` is set to another value, pass the `trafficDrivingType`, `trafficDrivingContent`, `variableName` (if applicable), `companyName`, `organizationCode`, and `companyDifferentFromSignQuaReason` (if applicable) parameters.
        # 
        # ### 3. trafficDrivingType enum values
        # 
        # >Warning: 
        # 
        # Due to regulatory requirements, mobile phone numbers are not supported.
        # 
        # 
        # 
        # - DOMAIN: A domain link.
        # 
        # - FIXED_PHONE: Fixed-line phone.
        # 
        # - 400_PHONE: Phone number prefixed with 400.
        # 
        # - 800_PHONE: Phone number prefixed with 800.
        # 
        # - 95_PHONE: Phone number prefixed with 95.
        # 
        # - 96_PHONE: Phone number prefixed with 96.
        # 
        # - 1_PHONE: A 3- to 8-digit phone number that starts with 1.
        # 
        # - OTHER_PHONE: Other phone number.
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

