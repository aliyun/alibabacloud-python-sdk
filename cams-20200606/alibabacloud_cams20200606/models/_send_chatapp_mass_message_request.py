# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_cams20200606 import models as main_models
from darabonba.model import DaraModel

class SendChatappMassMessageRequest(DaraModel):
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
        sender_list: List[main_models.SendChatappMassMessageRequestSenderList] = None,
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
        # - **instagram**
        # 
        # <props="intl">- **viber**
        # 
        # This parameter is required.
        self.channel_type = channel_type
        # The ISV sub-customer SpaceId or direct customer instance ID. You can view it on the <props="china">[**Channel Management**](https://chatapp.console.aliyun.com/ChannelsManagement)<props="intl">[**Channel Management**](https://chatapp.console.alibabacloud.com/CustomerList) page.
        self.cust_space_id = cust_space_id
        # The ISV customer WABA ID. This parameter is deprecated. Use CustSpaceId instead, which is the direct customer instance ID. You can view it on the <props="china">[**Channel Management**](https://chatapp.console.aliyun.com/ChannelsManagement)<props="intl">[**Channel Management**](https://chatapp.console.alibabacloud.com/CustomerList) page.
        self.cust_waba_id = cust_waba_id
        # The custom fallback content. This parameter is for the China site (Chinese). China site users can ignore this parameter.
        self.fall_back_content = fall_back_content
        # The fallback trigger time. This parameter is for the international site. China site users can ignore this parameter. <props="intl">If no delivery receipt is returned within the specified time, the fallback is triggered. If this parameter is not specified, the fallback is triggered only when the message fails to send or a failure status report is received. Unit: seconds. Minimum value: 60. Maximum value: 43200.
        self.fall_back_duration = fall_back_duration
        # The fallback policy ID. This parameter is for the China site (Chinese). China site users can ignore this parameter. <props="intl">You can view the policy ID on the [**Fallback Policy**](https://chatapp.console.alibabacloud.com/FallbackStrategy) page.
        self.fall_back_id = fall_back_id
        # The fallback rule. This parameter is for the international site. China site users can ignore this parameter.
        # <props="intl">Valid values:
        # <props="intl">- **undelivered**: the fallback is triggered when the message cannot be delivered to the device. During sending, the template and parameters must pass validation. Blocked templates or blocked numbers are not validated. This rule is used by default if the parameter value is empty.
        # <props="intl">- **sentFailed**: the fallback is triggered when validation of the template or template variables fails. Only channelType, type, messageType, to, and from (whether it exists) are strictly validated.
        self.fall_back_rule = fall_back_rule
        # The sender phone number.
        # 
        # - If ChannelType is **whatsapp**, this is the phone number registered and bindng with WhatsApp. You can view it on the <props="china">[**Channel Management**](https://chatapp.console.aliyun.com/ChannelsManagement)<props="intl">[**Channel Management**](https://chatapp.console.alibabacloud.com/CustomerList) > **Management** > **WABA Management** > **Phone Number Management** page.
        # - If ChannelType is **messenger**, this is the Page ID. You can view it on the <props="china">[**Channel Management**](https://chatapp.console.aliyun.com/ChannelsManagement)<props="intl">[**Channel Management**](https://chatapp.console.alibabacloud.com/CustomerList) > **Management** > **Public Page** page.
        # - If ChannelType is **instagram**, this is the Instagram professional Account ID. You can view it on the <props="china">[**Channel Management**](https://chatapp.console.aliyun.com/ChannelsManagement)<props="intl">[**Channel Management**](https://chatapp.console.alibabacloud.com/CustomerList) > **Management** > **Professional Account** page.
        # <props="intl">- If ChannelType is **viber**, this is the Viber Service ID. You can view it on the [**Channel Management**](https://chatapp.console.alibabacloud.com/CustomerList) > **Management** > **Service ID Management** page.
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
        # 
        # This parameter is required.
        self.language = language
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The list of recipient phone numbers.
        self.sender_list = sender_list
        # The tag information. Custom tag information for Viber message sending.
        self.tag = tag
        # The custom task ID.
        self.task_id = task_id
        # The template code. You can view the template code on the <props="china">[**Channel Management**](https://chatapp.console.aliyun.com/ChannelsManagement)<props="intl">[**Channel Management**](https://chatapp.console.alibabacloud.com/CustomerList) > **Management** > **Template Design** page.
        self.template_code = template_code
        # The template name. You can view the template name on the <props="china">[**Channel Management**](https://chatapp.console.aliyun.com/ChannelsManagement)<props="intl">[**Channel Management**](https://chatapp.console.alibabacloud.com/CustomerList) > **Management** > **Template Design** page.
        self.template_name = template_name
        # The timeout period for Viber message sending. This parameter is for the international site. China site users can ignore this parameter. <props="intl">Unit: seconds. Valid values: 30 to 1209600.
        self.ttl = ttl

    def validate(self):
        if self.sender_list:
            for v1 in self.sender_list:
                 if v1:
                    v1.validate()

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

        result['SenderList'] = []
        if self.sender_list is not None:
            for k1 in self.sender_list:
                result['SenderList'].append(k1.to_map() if k1 else None)

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

        self.sender_list = []
        if m.get('SenderList') is not None:
            for k1 in m.get('SenderList'):
                temp_model = main_models.SendChatappMassMessageRequestSenderList()
                self.sender_list.append(temp_model.from_map(k1))

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

class SendChatappMassMessageRequestSenderList(DaraModel):
    def __init__(
        self,
        flow_action: main_models.SendChatappMassMessageRequestSenderListFlowAction = None,
        payload: List[str] = None,
        product_action: main_models.SendChatappMassMessageRequestSenderListProductAction = None,
        recipient_type: str = None,
        template_params: Dict[str, str] = None,
        to: str = None,
    ):
        # The Flow message object.
        self.flow_action = flow_action
        # The list of button trigger message identifiers.
        self.payload = payload
        # The product information. This parameter applies only to WhatsApp channels and refers to the product information you uploaded on Meta.
        self.product_action = product_action
        self.recipient_type = recipient_type
        # The collection of template parameters.
        self.template_params = template_params
        # The recipient phone number.
        # 
        # - If ChannelType is **whatsapp**, this is the phone number of the message recipient.
        # - If ChannelType is **messenger**, this is the Page-Scoped User ID generated when the user interacts with the Facebook page.
        # - If ChannelType is **instagram**, this is the Instagram User ID generated when the user interacts with the Instagram business or creator account.
        # <props="intl">- If ChannelType is **viber**, this is the phone number of the message recipient.
        self.to = to

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
        if self.flow_action is not None:
            result['FlowAction'] = self.flow_action.to_map()

        if self.payload is not None:
            result['Payload'] = self.payload

        if self.product_action is not None:
            result['ProductAction'] = self.product_action.to_map()

        if self.recipient_type is not None:
            result['RecipientType'] = self.recipient_type

        if self.template_params is not None:
            result['TemplateParams'] = self.template_params

        if self.to is not None:
            result['To'] = self.to

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FlowAction') is not None:
            temp_model = main_models.SendChatappMassMessageRequestSenderListFlowAction()
            self.flow_action = temp_model.from_map(m.get('FlowAction'))

        if m.get('Payload') is not None:
            self.payload = m.get('Payload')

        if m.get('ProductAction') is not None:
            temp_model = main_models.SendChatappMassMessageRequestSenderListProductAction()
            self.product_action = temp_model.from_map(m.get('ProductAction'))

        if m.get('RecipientType') is not None:
            self.recipient_type = m.get('RecipientType')

        if m.get('TemplateParams') is not None:
            self.template_params = m.get('TemplateParams')

        if m.get('To') is not None:
            self.to = m.get('To')

        return self

class SendChatappMassMessageRequestSenderListProductAction(DaraModel):
    def __init__(
        self,
        sections: List[main_models.SendChatappMassMessageRequestSenderListProductActionSections] = None,
        thumbnail_product_retailer_id: str = None,
    ):
        # The list of product categories. A maximum of 10 categories and 30 products are supported.
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
                temp_model = main_models.SendChatappMassMessageRequestSenderListProductActionSections()
                self.sections.append(temp_model.from_map(k1))

        if m.get('ThumbnailProductRetailerId') is not None:
            self.thumbnail_product_retailer_id = m.get('ThumbnailProductRetailerId')

        return self

class SendChatappMassMessageRequestSenderListProductActionSections(DaraModel):
    def __init__(
        self,
        product_items: List[main_models.SendChatappMassMessageRequestSenderListProductActionSectionsProductItems] = None,
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
                temp_model = main_models.SendChatappMassMessageRequestSenderListProductActionSectionsProductItems()
                self.product_items.append(temp_model.from_map(k1))

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

class SendChatappMassMessageRequestSenderListProductActionSectionsProductItems(DaraModel):
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

class SendChatappMassMessageRequestSenderListFlowAction(DaraModel):
    def __init__(
        self,
        flow_action_data: Dict[str, Any] = None,
        flow_token: str = None,
    ):
        # The collection of flow default parameters.
        self.flow_action_data = flow_action_data
        # The custom flow token information.
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

