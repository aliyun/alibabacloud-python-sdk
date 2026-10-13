# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class SubscribeProductResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.SubscribeProductResponseBodyData = None,
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
            temp_model = main_models.SubscribeProductResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class SubscribeProductResponseBodyData(DaraModel):
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
        # The ID of the consumer to which the subscription belongs. This is the same identifier as the consumerId path parameter in the request and refers to the same consumer as the consumerName field returned at the same level.
        self.consumer_id = consumer_id
        # The name of the consumer to which the subscription belongs. This refers to the same consumer as the consumerId field returned at the same level.
        self.consumer_name = consumer_name
        # The ID of the subscribed API product. This is the primary ID of the API product resource and is the same identifier as the productId passed in the request body.
        self.product_id = product_id
        # The name of the subscribed API product. This is the Name property of the API product resource.
        self.product_name = product_name
        # The type of the subscribed API product. The valid values are not declared in this operation definition. The response parameter with the same name in the related ListProductSubscriptions operation includes the following valid values: REST_API, HTTP_API, MCP_SERVER, AGENT_API, and MODEL_API.
        self.product_type = product_type
        # The subscription status. Valid values: PENDING and APPROVED. These valid values are declared in the status request parameter of the related ListProductSubscriptions operation.
        self.status = status
        # The subscription ID. Identifies the API product subscription record corresponding to this subscription. You can use this ID to cancel the subscription by calling UnsubscribeHiMarketProduct or approve the subscription by calling ApproveProductSubscription. Both operations locate the record by using the /himarket/v1/consumers/{consumerId}/subscriptions/{subscriptionId} path.
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

