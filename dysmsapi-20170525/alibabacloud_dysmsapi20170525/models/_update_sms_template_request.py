# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UpdateSmsTemplateRequest(DaraModel):
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
        template_code: str = None,
        template_content: str = None,
        template_name: str = None,
        template_rule: str = None,
        template_type: int = None,
        traffic_driving: str = None,
    ):
        # The business scenario.
        # 
        # - If the associated SMS signature\\"s business scenario is "Live App", the `ApplySceneContent` parameter must be an app URL starting with `http://` or `https://`.
        # 
        # - The `ApplySceneContent` parameter is required if the associated SMS signature\\"s business scenario is "Registered Trademark" or "Name of Enterprise or Public Institution".
        self.apply_scene_content = apply_scene_content
        # The type of the international/regional template. This parameter is required when the **TemplateType** parameter is set to **3**. Valid values:
        # 
        # - **0**: SMS notification.
        # 
        # - **1**: promotional SMS.
        # 
        # - **2**: verification code.
        self.intl_type = intl_type
        # Additional materials, such as supporting documents or business screenshots, to help reviewers understand your business. If `TemplateType` is set to `2` (promotional SMS), you must upload proof of user authorization. For more information, see [Upload specifications for user authorization materials](https://help.aliyun.com/document_detail/312341.html).
        self.more_data = more_data
        self.owner_id = owner_id
        # The SMS signature associated with the template.
        self.related_sign_name = related_sign_name
        # Describe your business scenario, including a URL if applicable. You must also provide a complete SMS message example with populated variables. Providing this information as required is critical for template approval.
        self.remark = remark
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The code of the rejected SMS template. You can find the template code on the [Messages in Chinese Mainland > Template Management](https://dysms.console.aliyun.com/domestic/text/template) tab in the console or by calling the [QuerySmsTemplateList](~~QuerySmsTemplateList~~) operation.
        # 
        # This parameter is required.
        self.template_code = template_code
        # The new template content, up to 500 characters long.
        # 
        # The template content and its variables must comply with [SMS template specifications](https://help.aliyun.com/document_detail/463161.html) to be approved. To increase the approval rate and efficiency, refer to the common examples on the [Apply for Template](https://dysms.console.aliyun.com/domestic/text/template/add) page. For more information about variable specifications, see [TemplateContent parameter variable specifications](https://help.aliyun.com/document_detail/2806243.html).
        # 
        # This parameter is required.
        self.template_content = template_content
        # The name of the SMS template, up to 30 characters long. You can find the names of rejected templates on the [Messages in Chinese Mainland > Template Management](https://dysms.console.aliyun.com/domestic/text/template) tab in the console or by calling the [QuerySmsTemplateList](~~QuerySmsTemplateList~~) operation.
        # 
        # This parameter is required.
        self.template_name = template_name
        # The rules for the variables in the template. For details on how to define these rules, see the [example document](https://help.aliyun.com/document_detail/2806243.html).
        self.template_rule = template_rule
        # The SMS type. Valid values:
        # 
        # - **0**: verification code.
        # 
        # - **1**: SMS notification.
        # 
        # - **2**: promotional SMS.
        # 
        # - **3**: international/regional message.
        # 
        # > Only enterprise-verified users can apply for promotional SMS and international/regional messages. For more information about the differences between personal and enterprise accounts, see [Usage notes](https://help.aliyun.com/zh/sms/user-guide/usage-notes?spm=a2c4g.11186623.0.0.67447f576NJnE8).
        # 
        # This parameter is required.
        self.template_type = template_type
        # >Warning: 
        # 
        # To manage SMS content security, messages that contain traffic-driving information such as phone numbers and URLs may be blocked by carriers, which can cause delivery failures. We recommend that you avoid including such information in your SMS templates to prevent delivery failures.
        # 
        # 
        # 
        # A JSON string that contains a list of traffic-driving information.
        # >Notice: The value must be in the JSON format. Convert the value to a string before you pass it in.
        # 
        # ### 1. Fields
        # 
        # {
        # "trafficDrivingType":"Traffic-driving type",
        # "trafficDrivingContent":"Traffic-driving content",
        # "variableName":"variable name",
        # "companyName":"Name of the enterprise or public institution",
        # "organizationCode":"Unified Social Credit Code",
        # "icpNo":"ICP filing/permit number",
        # "icpPicOssKey":"OSS key of the ICP filing screenshot",
        # "companyDifferentFromSignQuaReason":"The reason why the name of the enterprise or public institution is different from that in the SMS signature qualification"
        # }
        # 
        # ### 2. Notes
        # 
        # - If the content is not a variable, do not pass the `variableName` field.
        # 
        # - If the name of the enterprise or public institution is different from that in the SMS signature qualification, provide the `companyDifferentFromSignQuaReason` field.
        # 
        # - If `trafficDrivingType` is set to `DOMAIN`, you must provide all the fields.
        # 
        # - For `trafficDrivingType` values other than `DOMAIN`, the `trafficDrivingType`, `trafficDrivingContent`, `companyName`, and `organizationCode` fields are required. The `variableName` and `companyDifferentFromSignQuaReason` fields are optional.
        # 
        # ### 3. TrafficDrivingType enumeration
        # 
        # >Warning: 
        # 
        # Due to regulatory requirements, mobile numbers are not supported.
        # 
        # 
        # 
        # - `DOMAIN`: A domain name.
        # 
        # - `FIXED_PHONE`: A fixed-line phone number.
        # 
        # - `400_PHONE`: A phone number that starts with 400.
        # 
        # - `800_PHONE`: A phone number that starts with 800.
        # 
        # - `95_PHONE`: A phone number that starts with 95.
        # 
        # - `96_PHONE`: A phone number that starts with 96.
        # 
        # - `1_PHONE`: A 3-digit to 8-digit phone number that starts with 1.
        # 
        # - `OTHER_PHONE`: Another type of phone number.
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

