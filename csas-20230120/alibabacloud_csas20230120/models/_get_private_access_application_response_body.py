# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_csas20230120 import models as main_models
from darabonba.model import DaraModel

class GetPrivateAccessApplicationResponseBody(DaraModel):
    def __init__(
        self,
        application: main_models.GetPrivateAccessApplicationResponseBodyApplication = None,
        request_id: str = None,
    ):
        # The office application.
        self.application = application
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.application:
            self.application.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application is not None:
            result['Application'] = self.application.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Application') is not None:
            temp_model = main_models.GetPrivateAccessApplicationResponseBodyApplication()
            self.application = temp_model.from_map(m.get('Application'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetPrivateAccessApplicationResponseBodyApplication(DaraModel):
    def __init__(
        self,
        address_groups: List[main_models.AddressGroup] = None,
        addresses: List[str] = None,
        application_id: str = None,
        auto_generated: int = None,
        browser_access_status: str = None,
        config_mode: str = None,
        connector_ids: List[str] = None,
        create_time: str = None,
        description: str = None,
        l_7config: main_models.PAL7Config = None,
        l_7proxy_domain_automatic: str = None,
        l_7proxy_domain_custom: str = None,
        name: str = None,
        policy_ids: List[str] = None,
        port_ranges: List[main_models.GetPrivateAccessApplicationResponseBodyApplicationPortRanges] = None,
        protocol: str = None,
        status: str = None,
        tag_ids: List[str] = None,
    ):
        self.address_groups = address_groups
        # The addresses of the office applications.
        self.addresses = addresses
        # The ID of the office application.
        self.application_id = application_id
        self.auto_generated = auto_generated
        # The browser access mode. Valid values:
        # 
        # *   **Enabled**
        # *   **Disabled**
        self.browser_access_status = browser_access_status
        self.config_mode = config_mode
        # The IDs of connectors.
        self.connector_ids = connector_ids
        # The creation time of the office application.
        self.create_time = create_time
        # The description of the office application.
        self.description = description
        # The browser access mode parameter. The parameter indicates the configurations of Layer 7 applications.
        self.l_7config = l_7config
        # The browser access mode parameter. The parameter indicates the domain name that the proxy gateway uses.
        self.l_7proxy_domain_automatic = l_7proxy_domain_automatic
        # The browser access mode parameter. The parameter indicates the custom domain name of the proxy gateway.
        self.l_7proxy_domain_custom = l_7proxy_domain_custom
        # The name of the office application.
        self.name = name
        # The IDs of the private access policies.
        self.policy_ids = policy_ids
        # The port ranges of the office applications. Multiple port ranges cannot be duplicated or overlapped.
        self.port_ranges = port_ranges
        # The protocol that is used by the office application. Valid values:
        # 
        # *   **All**
        # *   **TCP**
        # *   **UDP**
        self.protocol = protocol
        # The status of the office application. Valid values:
        # 
        # *   **Enabled**
        # *   **Disabled**
        self.status = status
        # The IDs of the tags for the office applications.
        self.tag_ids = tag_ids

    def validate(self):
        if self.address_groups:
            for v1 in self.address_groups:
                 if v1:
                    v1.validate()
        if self.l_7config:
            self.l_7config.validate()
        if self.port_ranges:
            for v1 in self.port_ranges:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AddressGroups'] = []
        if self.address_groups is not None:
            for k1 in self.address_groups:
                result['AddressGroups'].append(k1.to_map() if k1 else None)

        if self.addresses is not None:
            result['Addresses'] = self.addresses

        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.auto_generated is not None:
            result['AutoGenerated'] = self.auto_generated

        if self.browser_access_status is not None:
            result['BrowserAccessStatus'] = self.browser_access_status

        if self.config_mode is not None:
            result['ConfigMode'] = self.config_mode

        if self.connector_ids is not None:
            result['ConnectorIds'] = self.connector_ids

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.l_7config is not None:
            result['L7Config'] = self.l_7config.to_map()

        if self.l_7proxy_domain_automatic is not None:
            result['L7ProxyDomainAutomatic'] = self.l_7proxy_domain_automatic

        if self.l_7proxy_domain_custom is not None:
            result['L7ProxyDomainCustom'] = self.l_7proxy_domain_custom

        if self.name is not None:
            result['Name'] = self.name

        if self.policy_ids is not None:
            result['PolicyIds'] = self.policy_ids

        result['PortRanges'] = []
        if self.port_ranges is not None:
            for k1 in self.port_ranges:
                result['PortRanges'].append(k1.to_map() if k1 else None)

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        if self.status is not None:
            result['Status'] = self.status

        if self.tag_ids is not None:
            result['TagIds'] = self.tag_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.address_groups = []
        if m.get('AddressGroups') is not None:
            for k1 in m.get('AddressGroups'):
                temp_model = main_models.AddressGroup()
                self.address_groups.append(temp_model.from_map(k1))

        if m.get('Addresses') is not None:
            self.addresses = m.get('Addresses')

        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('AutoGenerated') is not None:
            self.auto_generated = m.get('AutoGenerated')

        if m.get('BrowserAccessStatus') is not None:
            self.browser_access_status = m.get('BrowserAccessStatus')

        if m.get('ConfigMode') is not None:
            self.config_mode = m.get('ConfigMode')

        if m.get('ConnectorIds') is not None:
            self.connector_ids = m.get('ConnectorIds')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('L7Config') is not None:
            temp_model = main_models.PAL7Config()
            self.l_7config = temp_model.from_map(m.get('L7Config'))

        if m.get('L7ProxyDomainAutomatic') is not None:
            self.l_7proxy_domain_automatic = m.get('L7ProxyDomainAutomatic')

        if m.get('L7ProxyDomainCustom') is not None:
            self.l_7proxy_domain_custom = m.get('L7ProxyDomainCustom')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PolicyIds') is not None:
            self.policy_ids = m.get('PolicyIds')

        self.port_ranges = []
        if m.get('PortRanges') is not None:
            for k1 in m.get('PortRanges'):
                temp_model = main_models.GetPrivateAccessApplicationResponseBodyApplicationPortRanges()
                self.port_ranges.append(temp_model.from_map(k1))

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TagIds') is not None:
            self.tag_ids = m.get('TagIds')

        return self

class GetPrivateAccessApplicationResponseBodyApplicationPortRanges(DaraModel):
    def __init__(
        self,
        begin: int = None,
        end: int = None,
    ):
        # The start port.
        self.begin = begin
        # The end port.
        self.end = end

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.begin is not None:
            result['Begin'] = self.begin

        if self.end is not None:
            result['End'] = self.end

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Begin') is not None:
            self.begin = m.get('Begin')

        if m.get('End') is not None:
            self.end = m.get('End')

        return self

