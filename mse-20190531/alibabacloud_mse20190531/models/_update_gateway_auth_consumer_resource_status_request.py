# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateGatewayAuthConsumerResourceStatusRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        consumer_id: int = None,
        gateway_unique_id: str = None,
        id_list: str = None,
        resource_status: bool = None,
    ):
        # The language of the response. Valid values:
        # 
        # *   zh: Chinese
        # *   en: English
        self.accept_language = accept_language
        # The ID of the consumer.
        # 
        # This parameter is required.
        self.consumer_id = consumer_id
        # The unique ID of the gateway.
        # 
        # This parameter is required.
        self.gateway_unique_id = gateway_unique_id
        # The list of IDs of the authorized resources that a user wants to update.
        # 
        # This parameter is required.
        self.id_list = id_list
        # The resource authorization status. Valid values:
        # 
        # *   true: enabled
        # *   false: disabled
        # 
        # This parameter is required.
        self.resource_status = resource_status

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

        if self.id_list is not None:
            result['IdList'] = self.id_list

        if self.resource_status is not None:
            result['ResourceStatus'] = self.resource_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('ConsumerId') is not None:
            self.consumer_id = m.get('ConsumerId')

        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')

        if m.get('IdList') is not None:
            self.id_list = m.get('IdList')

        if m.get('ResourceStatus') is not None:
            self.resource_status = m.get('ResourceStatus')

        return self

