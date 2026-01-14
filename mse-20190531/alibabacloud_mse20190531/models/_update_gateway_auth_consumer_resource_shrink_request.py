# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateGatewayAuthConsumerResourceShrinkRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        consumer_id: int = None,
        gateway_unique_id: str = None,
        resource_list_shrink: str = None,
    ):
        # The language of the response. Valid values:
        # 
        # *   zh: Chinese
        # *   en: English
        self.accept_language = accept_language
        # The gateway authentication consumer ID.
        # 
        # This parameter is required.
        self.consumer_id = consumer_id
        # The unique ID of the gateway.
        # 
        # This parameter is required.
        self.gateway_unique_id = gateway_unique_id
        # The gateway authentication consumer ID.
        self.resource_list_shrink = resource_list_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language

        if self.consumer_id is not None:
            result['ConsumerId'] = self.consumer_id

        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id

        if self.resource_list_shrink is not None:
            result['ResourceList'] = self.resource_list_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('ConsumerId') is not None:
            self.consumer_id = m.get('ConsumerId')

        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')

        if m.get('ResourceList') is not None:
            self.resource_list_shrink = m.get('ResourceList')

        return self

