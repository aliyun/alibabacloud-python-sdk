# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateCloudGtmAddressManualAvailableStatusRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        address_id: str = None,
        available_mode: str = None,
        client_token: str = None,
        manual_available_status: str = None,
    ):
        # The language of the response. Valid values:
        # 
        # *   zh-CN: Chinese
        # *   en-US (default): English
        self.accept_language = accept_language
        # The ID of the address. This ID uniquely identifies the address.
        # 
        # This parameter is required.
        self.address_id = address_id
        # The failover mode that is used when address exceptions are identified. Valid values:
        # 
        # *   auto: the automatic mode. The system determines whether to return an address based on health check results. If the address fails health checks, the system does not return the address. If the address passes health checks, the system returns the address.
        # *   manual: the manual mode. If an address is in the unavailable state, the address is not returned for DNS requests even if the address passes health checks. If an address is in the available state, the address is returned for DNS requests even if an alert is triggered when the address fails health checks.
        self.available_mode = available_mode
        # The client token that is used to ensure the idempotence of the request. You can specify a custom value for this parameter, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The availability state of the address when AvailableMode is set to manual. Valid values:
        # 
        # *   available: The address is normal. In this state, the address is returned for DNS requests even if an alert is triggered when the address fails health checks.
        # *   unavailable: The address is abnormal. In this state, the address is not returned for DNS requests even if the address passes health checks.
        self.manual_available_status = manual_available_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language

        if self.address_id is not None:
            result['AddressId'] = self.address_id

        if self.available_mode is not None:
            result['AvailableMode'] = self.available_mode

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.manual_available_status is not None:
            result['ManualAvailableStatus'] = self.manual_available_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('AddressId') is not None:
            self.address_id = m.get('AddressId')

        if m.get('AvailableMode') is not None:
            self.available_mode = m.get('AvailableMode')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('ManualAvailableStatus') is not None:
            self.manual_available_status = m.get('ManualAvailableStatus')

        return self

