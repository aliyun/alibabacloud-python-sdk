# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class ListProductSubscriptionsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListProductSubscriptionsResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The response status code.
        self.code = code
        # The response data.
        self.data = data
        # The response message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.ListProductSubscriptionsResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class ListProductSubscriptionsResponseBodyData(DaraModel):
    def __init__(
        self,
        content: List[main_models.ListProductSubscriptionsResponseBodyDataContent] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The subscription list of the API product. The list element is named subscription, and each element represents an API product subscription record.
        self.content = content
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The total number of entries.
        self.total_count = total_count

    def validate(self):
        if self.content:
            for v1 in self.content:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['content'] = []
        if self.content is not None:
            for k1 in self.content:
                result['content'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.content = []
        if m.get('content') is not None:
            for k1 in m.get('content'):
                temp_model = main_models.ListProductSubscriptionsResponseBodyDataContent()
                self.content.append(temp_model.from_map(k1))

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class ListProductSubscriptionsResponseBodyDataContent(DaraModel):
    def __init__(
        self,
        consumer_id: str = None,
        consumer_name: str = None,
        product_id: str = None,
        product_name: str = None,
        product_type: str = None,
        status: str = None,
        subscription_id: str = None,
    ):
        # The ID of the consumer to which the subscription belongs. This ID and the consumerName returned in the same element refer to the same consumer.
        self.consumer_id = consumer_id
        # The name of the consumer to which the subscription belongs. This corresponds to the keyword search for the consumerName request parameter.
        self.consumer_name = consumer_name
        # The ID of the subscribed API product. This is the primary ID of the API product resource and is the same as the productId path parameter in this operation.
        self.product_id = product_id
        # The name of the subscribed API product. This is the Name property of the API product resource.
        self.product_name = product_name
        # The type of the subscribed API product. Valid values: REST_API, HTTP_API, MCP_SERVER, AGENT_API, and MODEL_API.
        self.product_type = product_type
        # The subscription status. Valid values: PENDING and APPROVED. (These values are defined in the enumeration for the status request parameter. This response parameter is not annotated with @enums.)
        self.status = status
        # The subscription ID, which identifies an API product subscription record. You can use this ID to cancel the subscription by calling UnsubscribeHiMarketProduct or approve the subscription by calling ApproveProductSubscription. Both operations locate the record by using the /himarket/v1/consumers/{consumerId}/subscriptions/{subscriptionId} path.
        self.subscription_id = subscription_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.consumer_id is not None:
            result['consumerId'] = self.consumer_id

        if self.consumer_name is not None:
            result['consumerName'] = self.consumer_name

        if self.product_id is not None:
            result['productId'] = self.product_id

        if self.product_name is not None:
            result['productName'] = self.product_name

        if self.product_type is not None:
            result['productType'] = self.product_type

        if self.status is not None:
            result['status'] = self.status

        if self.subscription_id is not None:
            result['subscriptionId'] = self.subscription_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('consumerId') is not None:
            self.consumer_id = m.get('consumerId')

        if m.get('consumerName') is not None:
            self.consumer_name = m.get('consumerName')

        if m.get('productId') is not None:
            self.product_id = m.get('productId')

        if m.get('productName') is not None:
            self.product_name = m.get('productName')

        if m.get('productType') is not None:
            self.product_type = m.get('productType')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('subscriptionId') is not None:
            self.subscription_id = m.get('subscriptionId')

        return self

