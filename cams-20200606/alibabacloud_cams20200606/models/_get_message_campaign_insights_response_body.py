# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cams20200606 import models as main_models
from darabonba.model import DaraModel

class GetMessageCampaignInsightsResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: List[main_models.GetMessageCampaignInsightsResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The request status code. Valid values:
        # 
        # - OK: The request was successful.
        # 
        # - For other error codes, see [Error codes](https://help.aliyun.com/document_detail/196974.html).
        self.code = code
        # The returned data.
        self.data = data
        # The error description.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the operation was successful. Valid values:
        # 
        # - true: successful.
        # 
        # - false: failed.
        self.success = success

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.GetMessageCampaignInsightsResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetMessageCampaignInsightsResponseBodyData(DaraModel):
    def __init__(
        self,
        date_start: str = None,
        date_stop: str = None,
        marketing_messages_cost_per_delivered: str = None,
        marketing_messages_cost_per_link_btn_click: str = None,
        marketing_messages_delivered: str = None,
        marketing_messages_delivery_rate: str = None,
        marketing_messages_link_btn_click: str = None,
        marketing_messages_link_btn_click_rate: str = None,
        marketing_messages_read_rate: str = None,
        marketing_messages_spend: str = None,
    ):
        # The start time.
        self.date_start = date_start
        # The end time.
        self.date_stop = date_stop
        # The average cost per delivered message.
        self.marketing_messages_cost_per_delivered = marketing_messages_cost_per_delivered
        # The average cost per message link click. This metric excludes messages sent to Europe, Argentina, Türkiye, South Korea, and Japan.
        self.marketing_messages_cost_per_link_btn_click = marketing_messages_cost_per_link_btn_click
        # The number of messages that are sent by the business and successfully delivered to users. Some messages may fail to deliver if a user\\"s device is unavailable. This metric excludes messages delivered to Europe and Japan. In some cases, this metric is an estimate. The value may differ from the data on your bill due to minor discrepancies during data processing.
        self.marketing_messages_delivered = marketing_messages_delivered
        # The message delivery rate.
        self.marketing_messages_delivery_rate = marketing_messages_delivery_rate
        # The number of times users click or tap a marketing message that take users to an on-Meta or off-Meta destination, as specified by the advertiser. This metric excludes messages sent to Europe, Argentina, Türkiye, South Korea, and Japan.
        self.marketing_messages_link_btn_click = marketing_messages_link_btn_click
        # The percentage of delivered messages that received a link click. This metric excludes messages sent to Europe, Argentina, Türkiye, South Korea, and Japan.
        self.marketing_messages_link_btn_click_rate = marketing_messages_link_btn_click_rate
        # The number of read messages divided by the number of delivered messages. The read status of some messages may not be captured if a customer disables read receipts. This metric excludes messages sent to Europe and Japan.
        self.marketing_messages_read_rate = marketing_messages_read_rate
        # The total amount spent on a campaign, message group, or message during over its lifetime.
        self.marketing_messages_spend = marketing_messages_spend

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.date_start is not None:
            result['DateStart'] = self.date_start

        if self.date_stop is not None:
            result['DateStop'] = self.date_stop

        if self.marketing_messages_cost_per_delivered is not None:
            result['MarketingMessagesCostPerDelivered'] = self.marketing_messages_cost_per_delivered

        if self.marketing_messages_cost_per_link_btn_click is not None:
            result['MarketingMessagesCostPerLinkBtnClick'] = self.marketing_messages_cost_per_link_btn_click

        if self.marketing_messages_delivered is not None:
            result['MarketingMessagesDelivered'] = self.marketing_messages_delivered

        if self.marketing_messages_delivery_rate is not None:
            result['MarketingMessagesDeliveryRate'] = self.marketing_messages_delivery_rate

        if self.marketing_messages_link_btn_click is not None:
            result['MarketingMessagesLinkBtnClick'] = self.marketing_messages_link_btn_click

        if self.marketing_messages_link_btn_click_rate is not None:
            result['MarketingMessagesLinkBtnClickRate'] = self.marketing_messages_link_btn_click_rate

        if self.marketing_messages_read_rate is not None:
            result['MarketingMessagesReadRate'] = self.marketing_messages_read_rate

        if self.marketing_messages_spend is not None:
            result['MarketingMessagesSpend'] = self.marketing_messages_spend

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DateStart') is not None:
            self.date_start = m.get('DateStart')

        if m.get('DateStop') is not None:
            self.date_stop = m.get('DateStop')

        if m.get('MarketingMessagesCostPerDelivered') is not None:
            self.marketing_messages_cost_per_delivered = m.get('MarketingMessagesCostPerDelivered')

        if m.get('MarketingMessagesCostPerLinkBtnClick') is not None:
            self.marketing_messages_cost_per_link_btn_click = m.get('MarketingMessagesCostPerLinkBtnClick')

        if m.get('MarketingMessagesDelivered') is not None:
            self.marketing_messages_delivered = m.get('MarketingMessagesDelivered')

        if m.get('MarketingMessagesDeliveryRate') is not None:
            self.marketing_messages_delivery_rate = m.get('MarketingMessagesDeliveryRate')

        if m.get('MarketingMessagesLinkBtnClick') is not None:
            self.marketing_messages_link_btn_click = m.get('MarketingMessagesLinkBtnClick')

        if m.get('MarketingMessagesLinkBtnClickRate') is not None:
            self.marketing_messages_link_btn_click_rate = m.get('MarketingMessagesLinkBtnClickRate')

        if m.get('MarketingMessagesReadRate') is not None:
            self.marketing_messages_read_rate = m.get('MarketingMessagesReadRate')

        if m.get('MarketingMessagesSpend') is not None:
            self.marketing_messages_spend = m.get('MarketingMessagesSpend')

        return self

