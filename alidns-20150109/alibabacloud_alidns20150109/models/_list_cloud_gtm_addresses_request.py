# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListCloudGtmAddressesRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        address: str = None,
        address_id: str = None,
        client_token: str = None,
        enable_status: str = None,
        health_status: str = None,
        monitor_template_id: str = None,
        name: str = None,
        page_number: int = None,
        page_size: int = None,
        type: str = None,
    ):
        # The language of the return value. Valid values:
        # 
        # - zh-CN: Chinese.
        # 
        # - en-US: English.
        self.accept_language = accept_language
        # The IP address or domain name.
        self.address = address
        # The unique ID of the address.
        self.address_id = address_id
        # A client token that is used to ensure the idempotence of the request. The client must generate a unique token for each request. The token can contain a maximum of 64 ASCII characters.
        self.client_token = client_token
        # The state of the address. Valid values:
        # 
        # - enable: The address is enabled.
        # 
        # - disable: The address is disabled.
        self.enable_status = enable_status
        # The health status of the address. Valid values:
        # 
        # - ok: All health check tasks that are associated with the address are normal.
        # 
        # - ok_alert: Some health check tasks that are associated with the address are abnormal, but the address is still considered normal.
        # 
        # - ok_no_monitor: No health check template is associated with the address.
        # 
        # - exceptional: Some or all health check tasks that are associated with the address are abnormal, and the address is considered abnormal.
        self.health_status = health_status
        # The unique ID of the health check template.
        self.monitor_template_id = monitor_template_id
        # The name of the address.
        self.name = name
        # The page number. The value starts from **1**. The default value is **1**.
        # 
        # This parameter is required.
        self.page_number = page_number
        # The number of entries to return on each page for a paged query. The maximum value is 100. The default value is 20.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The type of the address. Valid values:
        # 
        # - IPv4
        # 
        # - IPv6
        # 
        # - domain
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language

        if self.address is not None:
            result['Address'] = self.address

        if self.address_id is not None:
            result['AddressId'] = self.address_id

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.enable_status is not None:
            result['EnableStatus'] = self.enable_status

        if self.health_status is not None:
            result['HealthStatus'] = self.health_status

        if self.monitor_template_id is not None:
            result['MonitorTemplateId'] = self.monitor_template_id

        if self.name is not None:
            result['Name'] = self.name

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('Address') is not None:
            self.address = m.get('Address')

        if m.get('AddressId') is not None:
            self.address_id = m.get('AddressId')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('EnableStatus') is not None:
            self.enable_status = m.get('EnableStatus')

        if m.get('HealthStatus') is not None:
            self.health_status = m.get('HealthStatus')

        if m.get('MonitorTemplateId') is not None:
            self.monitor_template_id = m.get('MonitorTemplateId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

