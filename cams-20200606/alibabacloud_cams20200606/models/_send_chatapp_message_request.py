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
        self.ad_account_id = ad_account_id
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
        self.context_message_id = context_message_id
        self.cust_space_id = cust_space_id
        self.cust_waba_id = cust_waba_id
        self.fall_back_content = fall_back_content
        self.fall_back_duration = fall_back_duration
        self.fall_back_id = fall_back_id
        self.fall_back_rule = fall_back_rule
        self.flow_action = flow_action
        # This parameter is required.
        self.from_ = from_
        self.isv_code = isv_code
        self.label = label
        self.language = language
        self.message_campaign_id = message_campaign_id
        self.message_type = message_type
        self.owner_id = owner_id
        # The payload of the button.
        self.payload = payload
        self.product_action = product_action
        self.recipient_type = recipient_type
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.tag = tag
        self.task_id = task_id
        self.template_code = template_code
        self.template_name = template_name
        self.template_params = template_params
        # This parameter is required.
        self.to = to
        self.token_type = token_type
        self.tracking_data = tracking_data
        self.ttl = ttl
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
        self.sections = sections
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
        self.product_items = product_items
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
        self.flow_action_data = flow_action_data
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

