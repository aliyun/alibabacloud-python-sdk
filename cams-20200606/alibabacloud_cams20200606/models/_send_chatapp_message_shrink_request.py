# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SendChatappMessageShrinkRequest(DaraModel):
    def __init__(
        self,
        ad_account_id: str = None,
        category: str = None,
        channel_type: str = None,
        content: str = None,
        context_message_id: str = None,
        cust_space_id: str = None,
        cust_waba_id: str = None,
        fall_back_content: str = None,
        fall_back_duration: int = None,
        fall_back_id: str = None,
        fall_back_rule: str = None,
        flow_action_shrink: str = None,
        from_: str = None,
        isv_code: str = None,
        label: str = None,
        language: str = None,
        message_campaign_id: str = None,
        message_type: str = None,
        owner_id: int = None,
        payload_shrink: str = None,
        product_action_shrink: str = None,
        recipient_type: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        tag: str = None,
        task_id: str = None,
        template_code: str = None,
        template_name: str = None,
        template_params_shrink: str = None,
        to: str = None,
        token_type: str = None,
        tracking_data: str = None,
        ttl: int = None,
        type: str = None,
    ):
        self.ad_account_id = ad_account_id
        self.category = category
        # The channel type. Valid values:
        # 
        # *   **whatsapp**
        # *   **viber**
        # *   **line** (under development)
        # 
        # This parameter is required.
        self.channel_type = channel_type
        # The message content.
        # 
        # **Notes on WhatsApp messages:**
        # 
        # *   If you set **messageType** to **text**, you must specify **text** and must not specify **Caption**.
        # *   If you set **messageType** to **image**, you must specify **Link**.
        # *   If you set **messageType** to **video**, you must specify **Link**.
        # *   If you set **messageType** to **audio**, **Link** is required and **Caption** is invalid.
        # *   If you set **messageType** to **document**, **Link** and **FileName** are required and **Caption** is invalid.
        # *   If you set **messageType** to **interactive**, you must specify **type** and **action**.
        # *   If you set **messageType** to **contacts**, you must specify **name**.
        # *   If you set **messageType** to **location**, you must specify **longitude** and **latitude**.
        # *   If you set **messageType** to **sticker**, you must specify **Link**, and **Caption** and **FileName** are invalid.
        # *   If you set **messageType** to **reaction**, you must specify **messageId** and **emoji**.
        # 
        # **Notes on Viber messages:**
        # 
        # *   If you set **messageType** to **text**, you must specify **text**.
        # *   If you set **messageType** to **image**, you must specify **link**.
        # *   If you set **messageType** to **video**, you must specify **link**, **thumbnail**, **fileSize**, and **duration**.
        # *   If you set **messageType** to **document**, you must specify **link**, **fileName**, and **fileType**.
        # *   If you set **messageType** to **text_button**, you must specify **text**, **caption**, and **action**.
        # *   If you set **messageType** to **text_image_button**, you must specify **text**, **link**, **caption**, and **action**.
        # *   If you set **messageType** to **text_video**, you must specify **text**, **link**, **thumbnail**, **fileSize**, and **duration**.
        # *   If you set **messageType** to **text_video_button**, you must specify **text**, **link**, **thumbnail**, **fileSize**, **duration**, and **caption**. In addition, you must not specify **action**.
        self.content = content
        # The ID of the reply message.
        self.context_message_id = context_message_id
        # The space ID of the user.
        self.cust_space_id = cust_space_id
        # The WhatsApp Business Account (WABA) ID of the RAM user within the independent software vendor (ISV) account.
        # 
        # >  CustWabaId is an obsolete parameter. Use CustSpaceId instead.
        self.cust_waba_id = cust_waba_id
        # The content of the fallback message.
        self.fall_back_content = fall_back_content
        # Specifies the period of time after which the fallback message is sent if the message receipt that indicates the message is delivered to clients is not received. If this parameter is left empty, the fallback message is sent only when the **message fails to be sent** or **the message receipt that indicates the message is not delivered to clients** is received. Unit: seconds. Valid values: 60 to 43200.
        self.fall_back_duration = fall_back_duration
        # The ID of the fallback policy. You can create a fallback policy and view the information in the Chat App Message Service console.
        self.fall_back_id = fall_back_id
        # The fallback rule. Valid values:
        # 
        # *   **undelivered**: A fallback is triggered if the message is not delivered to clients. When the message is being sent, the template parameters are verified. If the parameters fail to pass the verification, the message fails to be sent. Whether the template and phone number are prohibited is not verified. By default, this value is used when FallBackRule is left empty.
        # *   **sentFailed**: A fallback is triggered even if the template parameters including variables fail to pass the verification. If the channelType, type, messageType, to, and from parameters fail to pass the verification, a fallback is not triggered.
        self.fall_back_rule = fall_back_rule
        # The Flow action.
        self.flow_action_shrink = flow_action_shrink
        # The mobile phone number of the message sender.
        # 
        # >  You can specify a mobile phone number that is registered for a WhatsApp account and is approved in the Chat App Message Service console.
        # 
        # This parameter is required.
        self.from_ = from_
        # The ISV verification code. This parameter is used to verify whether the RAM user is authorized by the ISV account.
        self.isv_code = isv_code
        # The type of the Viber message. This parameter is required if ChannelType is set to viber. Valid values:
        # 
        # *   **promotion**
        # *   **transaction**
        self.label = label
        # The language that is used in the message template. This parameter is required only if you set the Type parameter to **template**. For more information about language codes, see [Language codes](https://help.aliyun.com/document_detail/463420.html).
        self.language = language
        self.message_campaign_id = message_campaign_id
        # The specific type of the message. This parameter is required only if you set the Type parameter to **message**.
        # 
        # **Valid values of MessageType when you set the ChannelType parameter to whatsapp:**
        # 
        # *   **text**: a text message.
        # *   **image**: an image message.
        # *   **video**: a video message.
        # *   **audio**: an audio message.
        # *   **document**: a document message.
        # *   **interactive**: an interactive message.
        # *   **contacts**: a contact message.
        # *   **location**: a location message.
        # *   **sticker**: a sticker message.
        # *   **reaction**: a reaction message.
        # 
        # **Valid values of MessageType when you set the ChannelType parameter to viber:**
        # 
        # *   **text**: a text message.
        # *   **image**: an image message.
        # *   **video**: a video message.
        # *   **document**: a document message.
        # *   **text_button**: a message that contains the text and button media objects.
        # *   **text_image_button**: a message that contains multiple media objects, including the text, image, and button.
        # *   **text_video**: a message that contains the text and video media objects.
        # *   **text_video_button**: a message that contains multiple media objects, including text, video, and button.
        # *   **text_image**: a message that contains the text and image media objects.
        # 
        # > For more information, see [Parameters of a message template](https://help.aliyun.com/document_detail/454530.html).
        self.message_type = message_type
        self.owner_id = owner_id
        # The payload of the button.
        self.payload_shrink = payload_shrink
        # The information about the products included in the WhatsApp catalog message or multi-product message (MPM).
        self.product_action_shrink = product_action_shrink
        self.recipient_type = recipient_type
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The tag information of the Viber message.
        self.tag = tag
        # The task ID.
        self.task_id = task_id
        # The code of the message template. This parameter is required only if you set the Type parameter to **template**.
        self.template_code = template_code
        # The name of the message template.
        self.template_name = template_name
        # The variables of the message template.
        self.template_params_shrink = template_params_shrink
        # The mobile phone number of the message receiver.
        # 
        # This parameter is required.
        self.to = to
        self.token_type = token_type
        # The tracking data of the Viber message.
        self.tracking_data = tracking_data
        # The timeout period for sending the Viber message. Valid values: 30 to 1209600. Unit: seconds.
        self.ttl = ttl
        # The message type. Valid values:
        # 
        # *   **template**: the template message. A template message is sent based on a template that is created and approved in the Chat App Message Service console. You can send template messages based on your business requirements.
        # *   **message**: the custom message. You can send a custom WhatsApp message to a user only within 24 hours after you receive the last message from the user. This limit does not apply to custom Viber messages.
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ad_account_id is not None:
            result['AdAccountId'] = self.ad_account_id

        if self.category is not None:
            result['Category'] = self.category

        if self.channel_type is not None:
            result['ChannelType'] = self.channel_type

        if self.content is not None:
            result['Content'] = self.content

        if self.context_message_id is not None:
            result['ContextMessageId'] = self.context_message_id

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

        if self.flow_action_shrink is not None:
            result['FlowAction'] = self.flow_action_shrink

        if self.from_ is not None:
            result['From'] = self.from_

        if self.isv_code is not None:
            result['IsvCode'] = self.isv_code

        if self.label is not None:
            result['Label'] = self.label

        if self.language is not None:
            result['Language'] = self.language

        if self.message_campaign_id is not None:
            result['MessageCampaignId'] = self.message_campaign_id

        if self.message_type is not None:
            result['MessageType'] = self.message_type

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.payload_shrink is not None:
            result['Payload'] = self.payload_shrink

        if self.product_action_shrink is not None:
            result['ProductAction'] = self.product_action_shrink

        if self.recipient_type is not None:
            result['RecipientType'] = self.recipient_type

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.tag is not None:
            result['Tag'] = self.tag

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.template_code is not None:
            result['TemplateCode'] = self.template_code

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        if self.template_params_shrink is not None:
            result['TemplateParams'] = self.template_params_shrink

        if self.to is not None:
            result['To'] = self.to

        if self.token_type is not None:
            result['TokenType'] = self.token_type

        if self.tracking_data is not None:
            result['TrackingData'] = self.tracking_data

        if self.ttl is not None:
            result['Ttl'] = self.ttl

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdAccountId') is not None:
            self.ad_account_id = m.get('AdAccountId')

        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('ChannelType') is not None:
            self.channel_type = m.get('ChannelType')

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('ContextMessageId') is not None:
            self.context_message_id = m.get('ContextMessageId')

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

        if m.get('FlowAction') is not None:
            self.flow_action_shrink = m.get('FlowAction')

        if m.get('From') is not None:
            self.from_ = m.get('From')

        if m.get('IsvCode') is not None:
            self.isv_code = m.get('IsvCode')

        if m.get('Label') is not None:
            self.label = m.get('Label')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('MessageCampaignId') is not None:
            self.message_campaign_id = m.get('MessageCampaignId')

        if m.get('MessageType') is not None:
            self.message_type = m.get('MessageType')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Payload') is not None:
            self.payload_shrink = m.get('Payload')

        if m.get('ProductAction') is not None:
            self.product_action_shrink = m.get('ProductAction')

        if m.get('RecipientType') is not None:
            self.recipient_type = m.get('RecipientType')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('Tag') is not None:
            self.tag = m.get('Tag')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        if m.get('TemplateParams') is not None:
            self.template_params_shrink = m.get('TemplateParams')

        if m.get('To') is not None:
            self.to = m.get('To')

        if m.get('TokenType') is not None:
            self.token_type = m.get('TokenType')

        if m.get('TrackingData') is not None:
            self.tracking_data = m.get('TrackingData')

        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

