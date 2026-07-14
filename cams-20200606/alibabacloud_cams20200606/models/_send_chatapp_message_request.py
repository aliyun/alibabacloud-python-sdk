# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_cams20200606 import models as main_models
from darabonba.model import DaraModel

class SendChatappMessageRequest(DaraModel):
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
        flow_action: main_models.SendChatappMessageRequestFlowAction = None,
        from_: str = None,
        isv_code: str = None,
        label: str = None,
        language: str = None,
        message_campaign_id: str = None,
        message_type: str = None,
        owner_id: int = None,
        payload: List[str] = None,
        product_action: main_models.SendChatappMessageRequestProductAction = None,
        recipient_type: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        tag: str = None,
        task_id: str = None,
        template_code: str = None,
        template_name: str = None,
        template_params: Dict[str, str] = None,
        to: str = None,
        token_type: str = None,
        tracking_data: str = None,
        ttl: int = None,
        type: str = None,
    ):
        # The Meta ad account ID.
        # > This parameter is a test parameter that is not fully available. Ignore this parameter.
        self.ad_account_id = ad_account_id
        # The message category (for WhatsApp direct send).
        # 
        # >Warning: Do not specify this parameter unless you are a Meta-invited customer. Otherwise, message delivery will fail.
        self.category = category
        # The channel type. Valid values:  
        # 
        # - **whatsapp** 
        # 
        # - **messenger** 
        # 
        # - **instagram**
        # 
        # - **telegram**
        # 
        # <props="intl">- **viber**
        # 
        # This parameter is required.
        self.channel_type = channel_type
        # The message content.
        # 
        # **WhatsApp message notes:**
        # - If **messageType** is **text**, the **text** field is required and the **Caption** field must not be specified.
        # - If **messageType** is **image**, the **Link** field is required.
        # - If **messageType** is **video**, the **Link** field is required.
        # - If **messageType** is **audio**, the **Link** field is required and the **Caption** field is invalid.
        # - If **messageType** is **document**, the **Link** and **FileName** fields are required and the **Caption** field is invalid.
        # - If **messageType** is **interactive**, the **type** and **action** fields are required.
        # - If **messageType** is **contacts**, the **name** field is required.
        # - If **messageType** is **location**, the **longitude** and **latitude** fields are required.
        # - If **messageType** is **sticker**, the **Link** field is required and the **Caption** and **FileName** fields are invalid.
        # - If **messageType** is **reaction**, the **messageId** and **emoji** fields are required.
        # 
        # 
        # **Messenger message notes:**
        # - If **messageType** is **text**, the **text** field is required.
        # - If **messageType** is **image**, **video**, **audio**, or **document**, the **link** field is required.
        # 
        # **Instagram message notes:**
        # - If **messageType** is **text**, the **text** field is required.
        # - If **messageType** is **image**, **video**, or **audio**, the **link** field is required.
        # 
        # 
        # <props="intl">**Viber message notes:**
        # <props="intl">- If **messageType** is **text**, the **text** field is required.
        # <props="intl">- If **messageType** is **image**, the **link** field is required.
        # <props="intl">- If **messageType** is **video**, the **link**, **thumbnail**, **fileSize**, and **duration** fields are required.
        # <props="intl">- If **messageType** is **document**, the **link**, **fileName**, and **fileType** fields are required.
        # <props="intl">- If **messageType** is **text_button**, the **text**, **caption**, and **action** fields are required.
        # <props="intl">- If **messageType** is **text_image_button**, the **text**, **link**, **caption**, and **action** fields are required.
        # <props="intl">- If **messageType** is **text_video**, the **text**, **link**, **thumbnail**, **fileSize**, and **duration** fields are required.
        # <props="intl">- If **messageType** is **text_video_button**, the **text**, **link**, **thumbnail**, **fileSize**, **duration**, and **caption** fields are required, and the **action** field must not be empty.
        self.content = content
        # The ID of the message to reply to. This is the ID of a previously sent or received message.
        self.context_message_id = context_message_id
        # The SpaceId of the ISV sub-customer, or the direct customer instance ID. You can view it on the <props="china">[**Channel Management**](https://chatapp.console.aliyun.com/ChannelsManagement)<props="intl">[**Channel Management**](https://chatapp.console.alibabacloud.com/CustomerList) page.
        self.cust_space_id = cust_space_id
        # The ISV customer WABA ID. This parameter is deprecated. Use CustSpaceId instead, which is the direct customer instance ID. You can view it on the <props="china">[**Channel Management**](https://chatapp.console.aliyun.com/ChannelsManagement)<props="intl">[**Channel Management**](https://chatapp.console.alibabacloud.com/CustomerList) page.
        self.cust_waba_id = cust_waba_id
        # The custom fallback content. This parameter is for the China site (Chinese mainland). China site users can ignore this parameter.
        self.fall_back_content = fall_back_content
        # The fallback trigger time. This parameter is for the international site. China site users can ignore this parameter. <props="intl">If the message does not return a delivered receipt within the specified time, fallback is triggered. If this parameter is not specified, fallback is not triggered based on time and occurs only when the message fails to send or a failure status report is received. Unit: seconds. Minimum value: 60. Maximum value: 43200.
        self.fall_back_duration = fall_back_duration
        # The fallback policy ID. This parameter is for the China site (Chinese mainland). China site users can ignore this parameter. <props="intl">You can view the policy ID on the [**Fallback Policy**](https://chatapp.console.alibabacloud.com/FallbackStrategy) page.
        self.fall_back_id = fall_back_id
        # The fallback rule. This parameter is for the international site. China site users can ignore this parameter.
        # <props="intl">Valid values:
        # <props="intl">- **undelivered**: fallback is triggered when the message cannot be delivered to the device (template and parameter validation must pass at the sending stage; template bans or number bans are not validated). This rule is used by default if the parameter value is empty.
        # <props="intl">- **sentFailed**: fallback is also triggered when template or template variable validation fails. Only the channelType, type, messageType, to, and from (existence check) parameters are strictly validated.
        self.fall_back_rule = fall_back_rule
        # The Flow message object.
        self.flow_action = flow_action
        # The sender number.
        # 
        # - If ChannelType is set to **whatsapp**, this is the phone number registered and bindded with WhatsApp. You can view it on the <props="china">[**Channel Management**](https://chatapp.console.aliyun.com/ChannelsManagement)<props="intl">[**Channel Management**](https://chatapp.console.alibabacloud.com/CustomerList) > **Management** > **WABA Management** > **Phone Number Management** page.
        # - If ChannelType is set to **messenger**, this is the Page ID. You can view it on the <props="china">[**Channel Management**](https://chatapp.console.aliyun.com/ChannelsManagement)<props="intl">[**Channel Management**](https://chatapp.console.alibabacloud.com/CustomerList) > **Management** > **Public Page** page.
        # - If ChannelType is set to **instagram**, this is the Instagram professional account ID (Account ID). You can view it on the <props="china">[**Channel Management**](https://chatapp.console.aliyun.com/ChannelsManagement)<props="intl">[**Channel Management**](https://chatapp.console.alibabacloud.com/CustomerList) > **Management** > **Professional Account** page.
        # <props="intl">- If ChannelType is set to **viber**, this is the Viber Service ID. You can view it on the [**Channel Management**](https://chatapp.console.alibabacloud.com/CustomerList) > **Management** > **Service ID Management** page.
        # 
        # This parameter is required.
        self.from_ = from_
        # The ISV verification code used to verify whether a RAM user is authorized by the ISV. This parameter is deprecated and can be ignored.
        self.isv_code = isv_code
        # The Viber message type. This parameter is for the international site. China site users can ignore this parameter.
        # <props="intl">Valid values:
        # <props="intl">- **pormotion**: marketing or promotional messages.
        # <props="intl">- **transaction**: notification messages.
        self.label = label
        # The language. For a list of language codes, see [Language codes](https://help.aliyun.com/document_detail/463420.html).
        self.language = language
        # The campaign message ID.
        # 
        # > This parameter is a test parameter that is not fully available. Ignore this parameter.
        self.message_campaign_id = message_campaign_id
        # The detailed message type when Type is set to message. Valid values:
        # 
        # <details>
        # <summary>WHATSAPP</summary>
        # 
        # - text: text message.
        # 
        # - image: image message.
        # 
        # - video: video message.
        # 
        # - audio: audio message.
        # 
        # - document: document message.
        # 
        # - interactive: interactive message.
        # 
        # - location: location message.
        # 
        # - contacts: contacts message.
        # 
        # - reaction: reaction message.
        # 
        # - sticker: sticker message.
        # 
        # - typing_indicator: typing indicator message.
        # 
        # - pin: pin or unpin message (available only for group messages).
        # 
        # - carousel: carousel message.
        # </details>
        # 
        # <details>
        # <summary>VIBER</summary>
        # 
        # - text: text message.
        # 
        # - image: image message.
        # 
        # - text_image_button: text + image + button message.
        # 
        # - text_button: text + button message.
        # 
        # - document: document message.
        # 
        # - video: video message.
        # 
        # - text_video: text + video message.
        # 
        # - text_video_button: text + video + button message.
        # 
        # - text_image: text + image message.
        # </details>
        # 
        # 
        # <details>
        # <summary>MESSENGER / INSTAGRAM</summary>
        # 
        # - text: text message.
        # 
        # - image: image message.
        # 
        # - video: video message.
        # 
        # - document: document message.
        # 
        # - audio: audio message.
        # 
        # - interactive: interactive message.
        # 
        # - couponTemplate: coupon template message.
        # 
        # - regularTemplate: regular template message.
        # 
        # - quickReply: quick reply message.
        # 
        # - buttonTemplate: button template message.
        # </details>
        # 
        # <details>
        # <summary>TELEGRAM</summary>
        # 
        # - text: text message.
        # 
        # - image: image message.
        # 
        # - video: video message.
        # 
        # - audio: audio message.
        # 
        # - document: document message.
        # 
        # - location: location message.
        # 
        # - gif: animated GIF message.
        # 
        # - sticker: sticker message.
        # 
        # </details>
        self.message_type = message_type
        self.owner_id = owner_id
        # The collection of button trigger messages.
        self.payload = payload
        # The product information. This parameter applies only to the WhatsApp channel type and refers to the product information you uploaded on Meta.
        self.product_action = product_action
        # The recipient type. Valid values:
        # 
        # - individual: an individual.
        # 
        # - group: a group.
        self.recipient_type = recipient_type
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The tag information. Custom tag information for Viber message delivery.
        self.tag = tag
        # The custom task ID.
        self.task_id = task_id
        # The template code. You can view the template code on the <props="china">[**Channel Management**](https://chatapp.console.aliyun.com/ChannelsManagement)<props="intl">[**Channel Management**](https://chatapp.console.alibabacloud.com/CustomerList) > **Management** > **Template Design** page.
        self.template_code = template_code
        # The template name. You can view the template name on the <props="china">[**Channel Management**](https://chatapp.console.aliyun.com/ChannelsManagement)<props="intl">[**Channel Management**](https://chatapp.console.alibabacloud.com/CustomerList) > **Management** > **Template Design** page.
        self.template_name = template_name
        # The collection of template parameters.
        self.template_params = template_params
        # The recipient number.
        # 
        # - If ChannelType is set to **whatsapp**, this is the phone number of the message recipient.
        # - If ChannelType is set to **messenger**, this is the Page-Scoped User ID generated when the user interacts with the Facebook page.
        # - If ChannelType is set to **instagram**, this is the Instagram User ID generated when the user interacts with the Instagram business or creator account.
        # <props="intl">- If ChannelType is set to **viber**, this is the phone number of the message recipient.
        # 
        # This parameter is required.
        self.to = to
        # The token type.
        # > This parameter is a test parameter that is not fully available. Ignore this parameter.
        self.token_type = token_type
        # The custom tracking data passed in for Viber message types. This parameter is for the international site. China site users can ignore this parameter.
        self.tracking_data = tracking_data
        # The timeout period for Viber message delivery. This parameter is for the international site. China site users can ignore this parameter. <props="intl">Unit: seconds. Valid values: 30 to 1209600.
        self.ttl = ttl
        # The message type. Valid values:
        # 
        # - template: a message template that has been approved in the console. This type of message can be sent at any time.
        # 
        # - message: a message in any format. This type of message can be sent only within 24 hours after the last message is received from the user.
        # 
        # >Notice: If Type is set to template, you must specify TemplateCode. If Type is set to message, you must specify MessageType.
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        if self.flow_action:
            self.flow_action.validate()
        if self.product_action:
            self.product_action.validate()

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

        if self.flow_action is not None:
            result['FlowAction'] = self.flow_action.to_map()

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

        if self.payload is not None:
            result['Payload'] = self.payload

        if self.product_action is not None:
            result['ProductAction'] = self.product_action.to_map()

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

        if self.template_params is not None:
            result['TemplateParams'] = self.template_params

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
            temp_model = main_models.SendChatappMessageRequestFlowAction()
            self.flow_action = temp_model.from_map(m.get('FlowAction'))

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
            self.payload = m.get('Payload')

        if m.get('ProductAction') is not None:
            temp_model = main_models.SendChatappMessageRequestProductAction()
            self.product_action = temp_model.from_map(m.get('ProductAction'))

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
            self.template_params = m.get('TemplateParams')

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

class SendChatappMessageRequestProductAction(DaraModel):
    def __init__(
        self,
        sections: List[main_models.SendChatappMessageRequestProductActionSections] = None,
        thumbnail_product_retailer_id: str = None,
    ):
        # The list of product categories (up to 10 categories and 30 products).
        self.sections = sections
        # The product catalog ID. You can obtain this ID by calling the [ListProductCatalog](https://help.aliyun.com/document_detail/2539783.html) operation.
        self.thumbnail_product_retailer_id = thumbnail_product_retailer_id

    def validate(self):
        if self.sections:
            for v1 in self.sections:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Sections'] = []
        if self.sections is not None:
            for k1 in self.sections:
                result['Sections'].append(k1.to_map() if k1 else None)

        if self.thumbnail_product_retailer_id is not None:
            result['ThumbnailProductRetailerId'] = self.thumbnail_product_retailer_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.sections = []
        if m.get('Sections') is not None:
            for k1 in m.get('Sections'):
                temp_model = main_models.SendChatappMessageRequestProductActionSections()
                self.sections.append(temp_model.from_map(k1))

        if m.get('ThumbnailProductRetailerId') is not None:
            self.thumbnail_product_retailer_id = m.get('ThumbnailProductRetailerId')

        return self

class SendChatappMessageRequestProductActionSections(DaraModel):
    def __init__(
        self,
        product_items: List[main_models.SendChatappMessageRequestProductActionSectionsProductItems] = None,
        title: str = None,
    ):
        # The list of product information.
        self.product_items = product_items
        # The category name. You can view it on the <props="china">[**Channel Management**](https://chatapp.console.aliyun.com/ChannelsManagement)<props="intl">[**Channel Management**](https://chatapp.console.alibabacloud.com/CustomerList) > **Management** > **Catalog Management** > **Product Management** page, or obtain it by calling the [ListProduct](https://help.aliyun.com/document_detail/2557786.html) operation.
        self.title = title

    def validate(self):
        if self.product_items:
            for v1 in self.product_items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ProductItems'] = []
        if self.product_items is not None:
            for k1 in self.product_items:
                result['ProductItems'].append(k1.to_map() if k1 else None)

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.product_items = []
        if m.get('ProductItems') is not None:
            for k1 in m.get('ProductItems'):
                temp_model = main_models.SendChatappMessageRequestProductActionSectionsProductItems()
                self.product_items.append(temp_model.from_map(k1))

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

class SendChatappMessageRequestProductActionSectionsProductItems(DaraModel):
    def __init__(
        self,
        product_retailer_id: str = None,
    ):
        # The product ID. You can view it on the <props="china">[**Channel Management**](https://chatapp.console.aliyun.com/ChannelsManagement)<props="intl">[**Channel Management**](https://chatapp.console.alibabacloud.com/CustomerList) > **Management** > **Catalog Management** > **Product Management** page, or obtain it by calling the [ListProduct](https://help.aliyun.com/document_detail/2557786.html) operation.
        self.product_retailer_id = product_retailer_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.product_retailer_id is not None:
            result['ProductRetailerId'] = self.product_retailer_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProductRetailerId') is not None:
            self.product_retailer_id = m.get('ProductRetailerId')

        return self

class SendChatappMessageRequestFlowAction(DaraModel):
    def __init__(
        self,
        flow_action_data: Dict[str, Any] = None,
        flow_token: str = None,
    ):
        # The collection of Flow default parameters.
        self.flow_action_data = flow_action_data
        # The custom Flow token information.
        self.flow_token = flow_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.flow_action_data is not None:
            result['FlowActionData'] = self.flow_action_data

        if self.flow_token is not None:
            result['FlowToken'] = self.flow_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FlowActionData') is not None:
            self.flow_action_data = m.get('FlowActionData')

        if m.get('FlowToken') is not None:
            self.flow_token = m.get('FlowToken')

        return self

