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
        # The Meta ad account ID.
        # 
        # > This parameter is for internal testing, is not generally available, and can be ignored.
        self.ad_account_id = ad_account_id
        # The message category for direct WhatsApp sending.
        # 
        # >Warning: 
        # 
        # Specify this parameter only if you are a Meta-invited customer. Otherwise, the message may fail to send.
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
        # <props="intl">
        # 
        # - **viber**
        # 
        # This parameter is required.
        self.channel_type = channel_type
        # The message content, in a JSON-formatted string.
        # 
        # **Notes for WhatsApp messages:**
        # 
        # - If `MessageType` is `text`, the `text` field is required, and the `Caption` field is not supported.
        # 
        # - If `MessageType` is `image`, the `Link` field is required.
        # 
        # - If `MessageType` is `video`, the `Link` field is required.
        # 
        # - If `MessageType` is `audio`, the `Link` field is required. The `Caption` field is not supported.
        # 
        # - If `MessageType` is `document`, the `Link` and `FileName` fields are required. The `Caption` field is not supported.
        # 
        # - If `MessageType` is `interactive`, the `type` and `action` fields are required.
        # 
        # - If `MessageType` is `contacts`, the `name` field is required.
        # 
        # - If `MessageType` is `location`, the `longitude` and `latitude` fields are required.
        # 
        # - If `MessageType` is `sticker`, the `Link` field is required. The `Caption` and `FileName` fields are not supported.
        # 
        # - If `MessageType` is `reaction`, the `messageId` and `emoji` fields are required.
        # 
        # **Notes for Messenger messages:**
        # 
        # - If `MessageType` is `text`, the `text` field is required.
        # 
        # - If `MessageType` is `image`, `video`, `audio`, or `document`, the `link` field is required.
        # 
        # **Notes for Instagram messages:**
        # 
        # - If `MessageType` is `text`, the `text` field is required.
        # 
        # - If `MessageType` is `image`, `video`, or `audio`, the `link` field is required.
        # 
        # <props="intl">
        # 
        # **Notes for Viber messages:**
        # 
        # 
        # 
        # <props="intl">
        # 
        # - If `MessageType` is `text`, the `text` field is required.
        # 
        # 
        # 
        # <props="intl">
        # 
        # - If `MessageType` is `image`, the `link` field is required.
        # 
        # 
        # 
        # <props="intl">
        # 
        # - If `MessageType` is `video`, the `link`, `thumbnail`, `fileSize`, and `duration` fields are required.
        # 
        # 
        # 
        # <props="intl">
        # 
        # - If `MessageType` is `document`, the `link`, `fileName`, and `fileType` fields are required.
        # 
        # 
        # 
        # <props="intl">
        # 
        # - If `MessageType` is `text_button`, the `text`, `caption`, and `action` fields are required.
        # 
        # 
        # 
        # <props="intl">
        # 
        # - If `MessageType` is `text_image_button`, the `text`, `link`, `caption`, and `action` fields are required.
        # 
        # 
        # 
        # <props="intl">
        # 
        # - If `MessageType` is `text_video`, the `text`, `link`, `thumbnail`, `fileSize`, and `duration` fields are required.
        # 
        # 
        # 
        # <props="intl">
        # 
        # - If `MessageType` is `text_video_button`, the `text`, `link`, `thumbnail`, `fileSize`, `duration`, and `caption` fields are required. The `action` field is not supported.
        self.content = content
        # The ID of the message to which you are replying.
        self.context_message_id = context_message_id
        # The Space ID of the ISV\\"s sub-account. For a direct customer, this is the Instance ID. You can find the ID on the <props="china">[**Channel Management**](https://chatapp.console.aliyun.com/ChannelsManagement)<props="intl">[**Channel Management**](https://chatapp.console.alibabacloud.com/CustomerList) page.
        self.cust_space_id = cust_space_id
        # **Deprecated.** Use `CustSpaceId` instead. The WABA ID of an ISV\\"s customer. For a direct customer, this is the Instance ID. You can find the ID on the <props="china">[**Channel Management**](https://chatapp.console.aliyun.com/ChannelsManagement)<props="intl">[**Channel Management**](https://chatapp.console.alibabacloud.com/CustomerList) page.
        self.cust_waba_id = cust_waba_id
        # The custom content of the fallback message. This parameter is available only on the International Site and can be ignored if you are using the China site.
        self.fall_back_content = fall_back_content
        # The duration after which a fallback is triggered. This parameter is available only on the International Site and can be ignored if you are using the China site.<props="intl"> If a delivery receipt is not returned within the specified period, a fallback is triggered. If this parameter is omitted, a fallback is triggered only if the message fails to send or a failed delivery receipt is returned. Unit: seconds. The value must be between 60 and 43200.
        self.fall_back_duration = fall_back_duration
        # The ID of the fallback strategy. This parameter is available only on the International Site and can be ignored if you are using the China site.<props="intl"> You can find the strategy ID on the [**Fallback Policy**](https://chatapp.console.alibabacloud.com/FallbackStrategy) page.
        self.fall_back_id = fall_back_id
        # The fallback rule. This parameter is available only on the International Site and can be ignored if you are using the China site.
        # <props="intl">Valid values:
        # 
        # <props="intl">
        # 
        # - **undelivered**: A fallback is triggered if message delivery fails. The template and parameters must be valid at the time of sending. Blocked templates or phone numbers are not validated. This is the default rule if the parameter is empty.
        # 
        # 
        # 
        # <props="intl">
        # 
        # - **sentFailed**: A fallback is triggered if the message fails parameter validation, such as for the template or template parameters. Only the existence of `channelType`, `type`, `messageType`, `to`, and `from` is strictly validated.
        self.fall_back_rule = fall_back_rule
        # The Flow message object.
        self.flow_action_shrink = flow_action_shrink
        # The sender\\"s number or ID.
        # 
        # - If `ChannelType` is **whatsapp**, this is the phone number registered with WhatsApp. You can find the number on the <props="china">[**Channel Management**](https://chatapp.console.aliyun.com/ChannelsManagement)<props="intl">[**Channel Management**](https://chatapp.console.alibabacloud.com/CustomerList) > **Manage** > **WABA Management** > **Phone Number Management** page.
        # 
        # - If `ChannelType` is **messenger**, this is the Facebook Page ID. You can find this ID on your <props="china">[**Channel Management**](https://chatapp.console.aliyun.com/ChannelsManagement)<props="intl">[**Channel Management**](https://chatapp.console.alibabacloud.com/CustomerList) > **Manage** > **Facebook Page** page.
        # 
        # - If `ChannelType` is **instagram**, this is the Instagram professional account ID (Account ID). You can find the ID on the <props="china">[**Channel Management**](https://chatapp.console.aliyun.com/ChannelsManagement)<props="intl">[**Channel Management**](https://chatapp.console.alibabacloud.com/CustomerList) > **Manage** > **Professional Account** page.
        # 
        # <props="intl">
        # 
        # - If `ChannelType` is **viber**, this is the Viber service ID (Service ID). You can find the ID on the [**Channel Management**](https://chatapp.console.alibabacloud.com/CustomerList) > **Manage** > **Service Number Management** page.
        # 
        # This parameter is required.
        self.from_ = from_
        # **Deprecated.** A verification code used to authorize an ISV\\"s sub-account. You can ignore this parameter.
        self.isv_code = isv_code
        # The Viber message type. This parameter is available only on the International Site and can be ignored if you are using the China site.
        # <props="intl">Valid values:
        # 
        # <props="intl">
        # 
        # - **promotion**: A promotional or marketing message.
        # 
        # 
        # 
        # <props="intl">
        # 
        # - **transaction**: A notification message.
        self.label = label
        # The language of the message template. For a list of supported languages and their corresponding codes, see [language code](https://help.aliyun.com/document_detail/463420.html).
        self.language = language
        # The ID of the message campaign.
        # 
        # > This parameter is for internal testing, is not generally available, and can be ignored.
        self.message_campaign_id = message_campaign_id
        # The message type to use when `Type` is set to `message`. The valid values vary based on the channel type:
        # 
        # <details>
        # 
        # <summary>
        # 
        # WHATSAPP
        # 
        # </summary>
        # 
        # - `text`: A text message.
        # 
        # - `image`: An image message.
        # 
        # - `video`: A video message.
        # 
        # - `audio`: An audio message.
        # 
        # - `document`: A document message.
        # 
        # - `interactive`: An interactive message.
        # 
        # - `location`: A location message.
        # 
        # - `contacts`: A contacts message.
        # 
        # - `reaction`: A reaction message.
        # 
        # - `sticker`: A sticker message.
        # 
        # - `typing_indicator`: A typing indicator message.
        # 
        # - `pin`: A message to pin or unpin. This type is available only for group messages.
        # 
        # - `carousel`: A carousel message.
        # 
        # </details>
        # 
        # <details>
        # 
        # <summary>
        # 
        # VIBER
        # 
        # </summary>
        # 
        # - `text`: A text message.
        # 
        # - `image`: An image message.
        # 
        # - `text_image_button`: A message with text, an image, and a button.
        # 
        # - `text_button`: A message with text and a button.
        # 
        # - `document`: A document message.
        # 
        # - `video`: A video message.
        # 
        # - `text_video`: A message with text and a video.
        # 
        # - `text_video_button`: A message with text, a video, and a button.
        # 
        # - `text_image`: A message with text and an image.
        # 
        # </details>
        # 
        # <details>
        # 
        # <summary>
        # 
        # MESSENGER / INSTAGRAM
        # 
        # </summary>
        # 
        # - `text`: A text message.
        # 
        # - `image`: An image message.
        # 
        # - `video`: A video message.
        # 
        # - `document`: A document message.
        # 
        # - `audio`: An audio message.
        # 
        # - `interactive`: An interactive message.
        # 
        # - `couponTemplate`: A coupon template message.
        # 
        # - `regularTemplate`: A regular template message.
        # 
        # - `quickReply`: A quick reply message.
        # 
        # - `buttonTemplate`: A button template message.
        # 
        # </details>
        # 
        # <details>
        # 
        # <summary>
        # 
        # TELEGRAM
        # 
        # </summary>
        # 
        # - `text`: A text message.
        # 
        # - `image`: An image message.
        # 
        # - `video`: A video message.
        # 
        # - `audio`: An audio message.
        # 
        # - `document`: A document message.
        # 
        # - `location`: A location message.
        # 
        # - `gif`: An animated GIF message.
        # 
        # - `sticker`: A sticker message.
        # 
        # </details>
        self.message_type = message_type
        self.owner_id = owner_id
        # An array of custom data strings that are sent to your webhook when a user clicks a corresponding button.
        self.payload_shrink = payload_shrink
        # Product information that you have uploaded to Meta. This parameter applies to WhatsApp channels only.
        self.product_action_shrink = product_action_shrink
        # The recipient type. Valid values:
        # 
        # - `individual`: A single recipient.
        # 
        # - `group`: A group.
        self.recipient_type = recipient_type
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # A custom tag for the Viber message.
        self.tag = tag
        # A custom task ID.
        self.task_id = task_id
        # The message template code. You can find the code on the <props="china">[**Channel Management**](https://chatapp.console.aliyun.com/ChannelsManagement)<props="intl">[**Channel Management**](https://chatapp.console.alibabacloud.com/CustomerList) > **Manage** > **Template Design** page.
        self.template_code = template_code
        # The template name. You can find the template name on the <props="china">[**Channel Management**](https://chatapp.console.aliyun.com/ChannelsManagement)<props="intl">[**Channel Management**](https://chatapp.console.alibabacloud.com/CustomerList) > **Manage** > **Template Design** page.
        self.template_name = template_name
        # The parameters for the message template.
        self.template_params_shrink = template_params_shrink
        # The recipient\\"s number or ID.
        # 
        # - If `ChannelType` is **whatsapp**, this is the recipient\\"s phone number.
        # 
        # - If `ChannelType` is **messenger**, this is a Page-Scoped User ID (PSID) generated when a user interacts with your Facebook Page.
        # 
        # - If `ChannelType` is **instagram**, this is an Instagram-Scoped User ID (IGSID) generated when a user interacts with your Instagram business or creator account.
        # 
        # <props="intl">
        # 
        # - If `ChannelType` is **viber**, this is the recipient\\"s phone number.
        # 
        # This parameter is required.
        self.to = to
        # The token type.
        # 
        # > This parameter is for internal testing, is not generally available, and can be ignored.
        self.token_type = token_type
        # Custom tracking data for a Viber message. This parameter is available only on the International Site and can be ignored if you are using the China site.
        self.tracking_data = tracking_data
        # The time-to-live (TTL) for a Viber message. This parameter is available only on the International Site and can be ignored if you are using the China site.<props="intl"> Unit: seconds. The value must be between 30 and 1209600.
        self.ttl = ttl
        # The message type. Valid values:
        # 
        # - `template`: A message template approved in the console. You can send this type of message at any time.
        # 
        # - `message`: A message of any format. You can send this type of message only within 24 hours of receiving the last message from a user.
        # 
        # >Notice: 
        # 
        # If you set `Type` to `template`, you must set the `TemplateCode` parameter. If you set `Type` to `message`, you must set the `MessageType` parameter.
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

