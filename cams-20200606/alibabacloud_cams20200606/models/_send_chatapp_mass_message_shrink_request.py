# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SendChatappMassMessageShrinkRequest(DaraModel):
    def __init__(
        self,
        channel_type: str = None,
        cust_space_id: str = None,
        cust_waba_id: str = None,
        fall_back_content: str = None,
        fall_back_duration: int = None,
        fall_back_id: str = None,
        fall_back_rule: str = None,
        from_: str = None,
        isv_code: str = None,
        label: str = None,
        language: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        sender_list_shrink: str = None,
        tag: str = None,
        task_id: str = None,
        template_code: str = None,
        template_name: str = None,
        ttl: int = None,
    ):
        # The channel type. Valid values:
        # 
        # - **whatsapp**
        # 
        # - **messenger**
        # 
        # - **instagram**
        # 
        # <props="intl">
        # 
        # - **viber**
        # 
        # This parameter is required.
        self.channel_type = channel_type
        # The Space ID of the ISV sub-customer, or the instance ID for a direct customer. View it on the <props="china">[**Channel Management**](https://chatapp.console.aliyun.com/ChannelsManagement)<props="intl">[**Channel Management**](https://chatapp.console.alibabacloud.com/CustomerList) page.
        self.cust_space_id = cust_space_id
        # The WhatsApp Business Account (WABA) ID of the Independent Software Vendor (ISV) customer. This is a deprecated parameter. Use CustSpaceId instead, which is the direct customer\\"s instance ID. View the ID on the <props="china">[**Channel Management**](https://chatapp.console.aliyun.com/ChannelsManagement)<props="intl">[**Channel Management**](https://chatapp.console.alibabacloud.com/CustomerList) page.
        self.cust_waba_id = cust_waba_id
        # The custom fallback content. This parameter is for the international site (alibabacloud.com). You can ignore it for the China site (aliyun.com).
        self.fall_back_content = fall_back_content
        # The time to trigger a fallback. This parameter is for the international site (alibabacloud.com). You can ignore it for the China site (aliyun.com).<props="intl">If a delivery receipt is not returned within the specified time, a fallback is triggered. If you leave this parameter empty, the fallback is not determined by time. A fallback is triggered only when the message fails to be sent or a failed status report is received. Unit: seconds. Minimum value: 60. Maximum value: 43200.
        self.fall_back_duration = fall_back_duration
        # The fallback policy ID. This parameter is for the international site (alibabacloud.com). You can ignore it for the China site (aliyun.com).<props="intl">View the policy ID on the [**Fallback Policy**](https://chatapp.console.alibabacloud.com/FallbackStrategy) page.
        self.fall_back_id = fall_back_id
        # The fallback rule. This parameter is for the international site (alibabacloud.com). You can ignore it for the China site (aliyun.com). <props="intl">Valid values:
        # 
        # <props="intl">
        # 
        # - **undelivered**: A fallback is triggered if the message cannot be delivered to the recipient. This rule requires that the template and parameters pass verification before sending. The rule does not apply if the message is blocked from sending, for example, due to a blacklisted template or phone number. This is the default rule if this parameter is empty.
        # 
        # 
        # 
        # <props="intl">
        # 
        # - **sentFailed**: A fallback is triggered if the template, template variables, or other parameters fail verification. Only the channelType, type, messageType, to, and the existence of the from parameter are strictly verified.
        self.fall_back_rule = fall_back_rule
        # The sender\\"s number.
        # 
        # - If ChannelType is **whatsapp**, this is the phone number registered and bound with WhatsApp. View the number on the <props="china">[**Channel Management**](https://chatapp.console.aliyun.com/ChannelsManagement)<props="intl">[**Channel Management**](https://chatapp.console.alibabacloud.com/CustomerList) > **Manage** > **WABA Management** > **Phone Number Management** page.
        # 
        # - If ChannelType is **messenger**, this is the Page ID. View the ID on the <props="china">[**Channel Management**](https://chatapp.console.aliyun.com/ChannelsManagement)<props="intl">[**Channel Management**](https://chatapp.console.alibabacloud.com/CustomerList) > **Manage** > **Facebook Homepage** page.
        # 
        # - If ChannelType is **instagram**, this is the Instagram professional account ID. View the ID on the <props="china">[**Channel Management**](https://chatapp.console.aliyun.com/ChannelsManagement)<props="intl">[**Channel Management**](https://chatapp.console.alibabacloud.com/CustomerList) > **Manage** > **Professional Account** page.
        # 
        # <props="intl">
        # 
        # - If ChannelType is **viber**, this is the Viber service ID. View the ID on the [**Channel Management**](https://chatapp.console.alibabacloud.com/CustomerList) > **Manage** > **Service Number Management&#x20;**&#x70;age.
        # 
        # This parameter is required.
        self.from_ = from_
        # ISV verification code, used to verify if the user is authorized by an ISV. This parameter is deprecated.
        self.isv_code = isv_code
        # The Viber message type. This parameter is for the international site (alibabacloud.com). You can ignore it for the China site (aliyun.com). <props="intl">Valid values:
        # 
        # <props="intl">
        # 
        # - **promotion**: marketing messages.
        # 
        # 
        # 
        # <props="intl">
        # 
        # - **transaction**: notification messages.
        self.label = label
        # The language. For language codes, see [Language codes](https://help.aliyun.com/document_detail/463420.html).
        # 
        # This parameter is required.
        self.language = language
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # A list of recipients.
        self.sender_list_shrink = sender_list_shrink
        # A custom tag for a Viber message.
        self.tag = tag
        # The custom task ID.
        self.task_id = task_id
        # The template code. View the template code on the <props="china">[**Channel Management**](https://chatapp.console.aliyun.com/ChannelsManagement)<props="intl">[**Channel Management**](https://chatapp.console.alibabacloud.com/CustomerList) > **Manage** > **Template Design** page.
        self.template_code = template_code
        # The template name. View the template name on the <props="china">[**Channel Management**](https://chatapp.console.aliyun.com/ChannelsManagement)<props="intl">[**Channel Management**](https://chatapp.console.alibabacloud.com/CustomerList) > **Manage** > **Template Design** page.
        self.template_name = template_name
        # The timeout period for sending a Viber message. This parameter is for the international site (alibabacloud.com). You can ignore it for the China site (aliyun.com).<props="intl">Unit: seconds. Valid values: 30 to 1209600.
        self.ttl = ttl

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channel_type is not None:
            result['ChannelType'] = self.channel_type

        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id

        if self.cust_waba_id is not None:
            result['CustWabaId'] = self.cust_waba_id

        if self.fall_back_content is not None:
            result['FallBackContent'] = self.fall_back_content

        if self.fall_back_duration is not None:
            result['FallBackDuration'] = self.fall_back_duration

        if self.fall_back_id is not None:
            result['FallBackId'] = self.fall_back_id

        if self.fall_back_rule is not None:
            result['FallBackRule'] = self.fall_back_rule

        if self.from_ is not None:
            result['From'] = self.from_

        if self.isv_code is not None:
            result['IsvCode'] = self.isv_code

        if self.label is not None:
            result['Label'] = self.label

        if self.language is not None:
            result['Language'] = self.language

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.sender_list_shrink is not None:
            result['SenderList'] = self.sender_list_shrink

        if self.tag is not None:
            result['Tag'] = self.tag

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.template_code is not None:
            result['TemplateCode'] = self.template_code

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        if self.ttl is not None:
            result['Ttl'] = self.ttl

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelType') is not None:
            self.channel_type = m.get('ChannelType')

        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')

        if m.get('CustWabaId') is not None:
            self.cust_waba_id = m.get('CustWabaId')

        if m.get('FallBackContent') is not None:
            self.fall_back_content = m.get('FallBackContent')

        if m.get('FallBackDuration') is not None:
            self.fall_back_duration = m.get('FallBackDuration')

        if m.get('FallBackId') is not None:
            self.fall_back_id = m.get('FallBackId')

        if m.get('FallBackRule') is not None:
            self.fall_back_rule = m.get('FallBackRule')

        if m.get('From') is not None:
            self.from_ = m.get('From')

        if m.get('IsvCode') is not None:
            self.isv_code = m.get('IsvCode')

        if m.get('Label') is not None:
            self.label = m.get('Label')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SenderList') is not None:
            self.sender_list_shrink = m.get('SenderList')

        if m.get('Tag') is not None:
            self.tag = m.get('Tag')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')

        return self

