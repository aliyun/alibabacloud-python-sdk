# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dysmsapi20170525 import models as main_models
from darabonba.model import DaraModel

class SendCardSmsRequest(DaraModel):
    def __init__(
        self,
        card_objects: List[main_models.SendCardSmsRequestCardObjects] = None,
        card_template_code: str = None,
        digital_template_code: str = None,
        digital_template_param: str = None,
        fallback_type: str = None,
        out_id: str = None,
        sign_name: str = None,
        sms_template_code: str = None,
        sms_template_param: str = None,
        sms_up_extend_code: str = None,
        template_code: str = None,
        template_param: str = None,
    ):
        # The objects of the message template.
        # 
        # This parameter is required.
        self.card_objects = card_objects
        # The code of the message template. You can view the template code in the **Template Code** column on the **Templates** tab of the **Go China** page in the Alibaba Cloud SMS console.
        # 
        # > Make sure that the message template has been approved.
        # 
        # This parameter is required.
        self.card_template_code = card_template_code
        # The code of the digital message template that applies when the card message is rolled back. You can view the template code in the **Template Code** column on the **Templates** tab of the **Go China** page in the Alibaba Cloud SMS console.
        # 
        # > Make sure that the message template has been approved.
        self.digital_template_code = digital_template_code
        # The variables of the digital message template.
        # 
        # > If you need to add line breaks to the JSON template, make sure that the format is valid.
        self.digital_template_param = digital_template_param
        # The rollback type. Valid values:
        # 
        # *   **SMS**: text message
        # *   **DIGITALSMS**: digital message
        # *   **NONE**: none
        # 
        # This parameter is required.
        self.fallback_type = fallback_type
        # The ID that is reserved for the caller of the operation.
        self.out_id = out_id
        # The signature. You can view the template code in the **Signature** column on the **Signaturess** tab of the **Go China** page in the Alibaba Cloud SMS console.
        # 
        # > The signature must be approved.
        # 
        # This parameter is required.
        self.sign_name = sign_name
        # The code of the text message template that applies when the card message is rolled back. You can view the template code in the **Template Code** column on the **Templates** tab of the **Go China** page in the Alibaba Cloud SMS console.
        # 
        # > Make sure that the message template has been approved. If you set the **FallbackType** parameter to **SMS**, this parameter is required.
        self.sms_template_code = sms_template_code
        # The variables of the text message template.
        # 
        # > If you need to add line breaks to the JSON template, make sure that the format is valid.
        self.sms_template_param = sms_template_param
        # The extension code of the upstream message. Upstream messages are messages sent to the communication service provider. Upstream messages are used to customize a service, complete an inquiry, or send a request. You are charged for sending upstream messages based on the billing standards of the service provider.
        # 
        # > If you do not need upstream messages, ignore this parameter.
        self.sms_up_extend_code = sms_up_extend_code
        # The code of the text message template.
        # 
        # Log on to the Alibaba Cloud SMS console. In the left-side navigation pane, click **Go Globe** or **Go China**. You can view the message template in the **Template Code** column on the **Message Templates** tab.
        # 
        # > The message templates must be created on the Go Globe page and approved.
        self.template_code = template_code
        # The variables of the message template. Format: JSON.
        # 
        # > If you need to add line breaks to the JSON template, make sure that the format is valid.
        self.template_param = template_param

    def validate(self):
        if self.card_objects:
            for v1 in self.card_objects:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CardObjects'] = []
        if self.card_objects is not None:
            for k1 in self.card_objects:
                result['CardObjects'].append(k1.to_map() if k1 else None)

        if self.card_template_code is not None:
            result['CardTemplateCode'] = self.card_template_code

        if self.digital_template_code is not None:
            result['DigitalTemplateCode'] = self.digital_template_code

        if self.digital_template_param is not None:
            result['DigitalTemplateParam'] = self.digital_template_param

        if self.fallback_type is not None:
            result['FallbackType'] = self.fallback_type

        if self.out_id is not None:
            result['OutId'] = self.out_id

        if self.sign_name is not None:
            result['SignName'] = self.sign_name

        if self.sms_template_code is not None:
            result['SmsTemplateCode'] = self.sms_template_code

        if self.sms_template_param is not None:
            result['SmsTemplateParam'] = self.sms_template_param

        if self.sms_up_extend_code is not None:
            result['SmsUpExtendCode'] = self.sms_up_extend_code

        if self.template_code is not None:
            result['TemplateCode'] = self.template_code

        if self.template_param is not None:
            result['TemplateParam'] = self.template_param

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.card_objects = []
        if m.get('CardObjects') is not None:
            for k1 in m.get('CardObjects'):
                temp_model = main_models.SendCardSmsRequestCardObjects()
                self.card_objects.append(temp_model.from_map(k1))

        if m.get('CardTemplateCode') is not None:
            self.card_template_code = m.get('CardTemplateCode')

        if m.get('DigitalTemplateCode') is not None:
            self.digital_template_code = m.get('DigitalTemplateCode')

        if m.get('DigitalTemplateParam') is not None:
            self.digital_template_param = m.get('DigitalTemplateParam')

        if m.get('FallbackType') is not None:
            self.fallback_type = m.get('FallbackType')

        if m.get('OutId') is not None:
            self.out_id = m.get('OutId')

        if m.get('SignName') is not None:
            self.sign_name = m.get('SignName')

        if m.get('SmsTemplateCode') is not None:
            self.sms_template_code = m.get('SmsTemplateCode')

        if m.get('SmsTemplateParam') is not None:
            self.sms_template_param = m.get('SmsTemplateParam')

        if m.get('SmsUpExtendCode') is not None:
            self.sms_up_extend_code = m.get('SmsUpExtendCode')

        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')

        if m.get('TemplateParam') is not None:
            self.template_param = m.get('TemplateParam')

        return self

class SendCardSmsRequestCardObjects(DaraModel):
    def __init__(
        self,
        custom_url: str = None,
        dync_params: str = None,
        mobile: str = None,
    ):
        # The URL to which the message is redirected if the message fails to be rendered.
        self.custom_url = custom_url
        # The variables. Special characters, such as $ and {}, do not need to be entered.
        self.dync_params = dync_params
        # The mobile phone number.
        self.mobile = mobile

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.custom_url is not None:
            result['customUrl'] = self.custom_url

        if self.dync_params is not None:
            result['dyncParams'] = self.dync_params

        if self.mobile is not None:
            result['mobile'] = self.mobile

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('customUrl') is not None:
            self.custom_url = m.get('customUrl')

        if m.get('dyncParams') is not None:
            self.dync_params = m.get('dyncParams')

        if m.get('mobile') is not None:
            self.mobile = m.get('mobile')

        return self

