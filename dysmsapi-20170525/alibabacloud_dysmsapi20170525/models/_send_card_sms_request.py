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
        # The card message objects.
        # 
        # This parameter is required.
        self.card_objects = card_objects
        # The code of the card message template. On the [Template Management](https://dysms.console.aliyun.com/domestic/card) page of the **Card Messages** module in the console, select the code of an approved card message template.
        # 
        # This parameter is required.
        self.card_template_code = card_template_code
        # The code of the fallback digital message template. This parameter is required if you set **FallbackType** to **DIGITALSMS**.
        # 
        # You can view the digital message template list on the [Template Management](https://dysms.console.aliyun.com/domestic/digit) page of the **Digital Messages** module in the console.
        # 
        # > The template must be added and approved.
        self.digital_template_code = digital_template_code
        # The actual values of the variables in the fallback digital message template. This parameter is required if the digital message template specified by **DigitalTemplateCode** contains variables.
        # 
        # > If the JSON value contains line breaks, follow the standard JSON protocol.
        self.digital_template_param = digital_template_param
        # The fallback type. Valid values:
        # - **SMS**: Falls back to a text message for phone numbers that do not support card messages.
        # - **DIGITALSMS**: Falls back to a digital message for phone numbers that do not support card messages.
        # - **NONE**: No fallback is required.
        # 
        # This parameter is required.
        self.fallback_type = fallback_type
        # The ID reserved for the caller.
        self.out_id = out_id
        # The signature name. You can call the [QuerySmsSignList](https://help.aliyun.com/document_detail/419282.html) operation to query the signatures applied for under the current account or view the signature list in the [Short Message Service (SMS) console](https://dysms.console.aliyun.com/domestic/text/sign).
        # > The signature must be approved.
        # 
        # This parameter is required.
        self.sign_name = sign_name
        # The code of the fallback text message template. This parameter is required if you set **FallbackType** to **SMS**.
        # 
        # You can call the [QuerySmsTemplateList](https://help.aliyun.com/document_detail/419288.html) operation to query the templates applied for under the current account or view the template list in the [SMS console](https://dysms.console.aliyun.com/domestic/text/template).
        # > The template must be added and approved.
        self.sms_template_code = sms_template_code
        # The actual values of the variables in the fallback text message template. This parameter is required if the text message template specified by **SmsTemplateCode** contains variables.
        # 
        # > If the JSON value contains line breaks, follow the standard JSON protocol.
        self.sms_template_param = sms_template_param
        # The extension code of the MO message. An MO message is a message sent to the communications service provider to customize a service, perform a query, or handle other business. The message is charged at the standard rate of the carrier.
        # > If you do not have such requirements, ignore this parameter.
        self.sms_up_extend_code = sms_up_extend_code
        # The code of the custom content template.
        # 
        # The custom content is sent to the recipient as a text message template combined with a card parsing link. Log on to the [SMS console](https://dysms.console.aliyun.com/overview), choose **Domestic Messages** or **International/HK/MO/TW Messages**, and view the **Template Code** on the **Template Management** tab.
        # 
        # > - The template code must be added and approved. To send international or Hong Kong, Macao, or Taiwan messages, use an international or Hong Kong, Macao, or Taiwan message template.
        # > - For example, if the selected text message template is "You have a new message" and the card parsing link is `1*.cn/2**d`, the final content is `You have a new message 1*.cn/2**d`. Test the message and control the word count before sending.
        self.template_code = template_code
        # The actual values of the variables in the custom content template. This parameter is required if the message template specified by **TemplateCode** contains variables.
        # 
        # > If the JSON value contains line breaks, follow the standard JSON protocol.
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
        # 渲染失败后跳转链接。
        self.custom_url = custom_url
        # 动态参数。动参变量不需要${}
        self.dync_params = dync_params
        # 接收卡片短信的手机号码。
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

