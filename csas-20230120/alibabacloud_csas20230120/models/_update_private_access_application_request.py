# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_csas20230120 import models as main_models
from darabonba.model import DaraModel

class UpdatePrivateAccessApplicationRequest(DaraModel):
    def __init__(
        self,
        address_groups: List[main_models.AddressGroup] = None,
        addresses: List[str] = None,
        application_id: str = None,
        config_mode: str = None,
        description: str = None,
        health_check_config: main_models.HealthCheckConfig = None,
        health_check_mode: str = None,
        l_7config: main_models.PAL7Config = None,
        l_7proxy_domain_automatic_prefix: str = None,
        l_7proxy_domain_custom: str = None,
        l_7proxy_domain_private: str = None,
        modify_type: str = None,
        name: str = None,
        port_ranges: List[main_models.UpdatePrivateAccessApplicationRequestPortRanges] = None,
        protocol: str = None,
        status: str = None,
        tag_ids: List[str] = None,
        unauthorized_access_config: main_models.PAApplicationUnauthorizedAccessConfig = None,
    ):
        # The application address groups. You can specify this parameter when ConfigMode is Precise. You cannot specify this parameter when ConfigMode is an empty string.
        self.address_groups = address_groups
        # The collection of private access application addresses. You can enter up to 1,000 private access application addresses.
        self.addresses = addresses
        # The ID of the private access application. You can obtain the value from the following operations:
        # - [ListPrivateAccessApplications](~~ListPrivateAccessApplications~~): Lists private access applications.
        # - [CreatePrivateAccessApplication](~~CreatePrivateAccessApplication~~): Creates a private access application.
        # 
        # This parameter is required.
        self.application_id = application_id
        # The configuration mode. Valid values:
        # * Empty string: the default mode.
        # * Precise: the precise mode.
        self.config_mode = config_mode
        # The description of the private access application. The description must be 1 to 128 characters in length, and can contain Chinese characters, uppercase and lowercase letters, digits, periods (.), underscores (_), hyphens (-), and spaces.
        self.description = description
        # The health check configuration. This parameter is valid only when HealthCheckMode is set to Continuous. You cannot specify this parameter when HealthCheckMode is set to OnAccess.
        self.health_check_config = health_check_config
        # The health check mode. Valid values:
        # * OnAccess: Checks upon access without active probing.
        # * Continuous: Performs continuous checks and periodically probes based on the configurations in HealthCheckConfig.
        # If this parameter is not specified, the default value is OnAccess. When the application addresses include wildcard domain names or CIDR blocks, or when the number of application addresses exceeds 10, only OnAccess is supported.
        self.health_check_mode = health_check_mode
        # The Layer 7 application configuration in browser access mode.
        self.l_7config = l_7config
        # The prefix of the mapped proxy domain name in browser access mode. The prefix must be 3 to 20 characters in length, and can contain lowercase letters, digits, and hyphens (-).
        self.l_7proxy_domain_automatic_prefix = l_7proxy_domain_automatic_prefix
        # The custom proxy domain name in browser access mode.
        self.l_7proxy_domain_custom = l_7proxy_domain_custom
        # The private proxy domain name in browser access mode.
        self.l_7proxy_domain_private = l_7proxy_domain_private
        # The modification type of the private access application. Valid values:
        # - **Cover** (default): Overwrites the original addresses, port ranges, and tag IDs with the values of the **Addresses**, **PortRanges**, and **TagIds** parameters.
        # - **Append**: Appends the values specified in the **Addresses**, **PortRanges**, and **TagIds** parameters to the original addresses, port ranges, and tag IDs.
        self.modify_type = modify_type
        # The name of the application.
        self.name = name
        # The collection of port ranges for the private access application. You can enter up to 65,535 port ranges. Multiple port ranges cannot be duplicate or overlap.
        self.port_ranges = port_ranges
        # The protocol of the private access application. Valid values:
        # - **All**: All protocols.
        # - **TCP**
        # - **UDP**
        self.protocol = protocol
        # The status of the private access application. Valid values:
        # - **Enabled**: Enabled.
        # - **Disabled**: Disabled.
        self.status = status
        # The collection of private access tag IDs. You can associate up to six custom private access tags with a single private access application.
        self.tag_ids = tag_ids
        # The configuration for unauthorized application access requests.
        self.unauthorized_access_config = unauthorized_access_config

    def validate(self):
        if self.address_groups:
            for v1 in self.address_groups:
                 if v1:
                    v1.validate()
        if self.health_check_config:
            self.health_check_config.validate()
        if self.l_7config:
            self.l_7config.validate()
        if self.port_ranges:
            for v1 in self.port_ranges:
                 if v1:
                    v1.validate()
        if self.unauthorized_access_config:
            self.unauthorized_access_config.validate()

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

        if self.config_mode is not None:
            result['ConfigMode'] = self.config_mode

        if self.description is not None:
            result['Description'] = self.description

        if self.health_check_config is not None:
            result['HealthCheckConfig'] = self.health_check_config.to_map()

        if self.health_check_mode is not None:
            result['HealthCheckMode'] = self.health_check_mode

        if self.l_7config is not None:
            result['L7Config'] = self.l_7config.to_map()

        if self.l_7proxy_domain_automatic_prefix is not None:
            result['L7ProxyDomainAutomaticPrefix'] = self.l_7proxy_domain_automatic_prefix

        if self.l_7proxy_domain_custom is not None:
            result['L7ProxyDomainCustom'] = self.l_7proxy_domain_custom

        if self.l_7proxy_domain_private is not None:
            result['L7ProxyDomainPrivate'] = self.l_7proxy_domain_private

        if self.modify_type is not None:
            result['ModifyType'] = self.modify_type

        if self.name is not None:
            result['Name'] = self.name

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

        if self.unauthorized_access_config is not None:
            result['UnauthorizedAccessConfig'] = self.unauthorized_access_config.to_map()

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

        if m.get('ConfigMode') is not None:
            self.config_mode = m.get('ConfigMode')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('HealthCheckConfig') is not None:
            temp_model = main_models.HealthCheckConfig()
            self.health_check_config = temp_model.from_map(m.get('HealthCheckConfig'))

        if m.get('HealthCheckMode') is not None:
            self.health_check_mode = m.get('HealthCheckMode')

        if m.get('L7Config') is not None:
            temp_model = main_models.PAL7Config()
            self.l_7config = temp_model.from_map(m.get('L7Config'))

        if m.get('L7ProxyDomainAutomaticPrefix') is not None:
            self.l_7proxy_domain_automatic_prefix = m.get('L7ProxyDomainAutomaticPrefix')

        if m.get('L7ProxyDomainCustom') is not None:
            self.l_7proxy_domain_custom = m.get('L7ProxyDomainCustom')

        if m.get('L7ProxyDomainPrivate') is not None:
            self.l_7proxy_domain_private = m.get('L7ProxyDomainPrivate')

        if m.get('ModifyType') is not None:
            self.modify_type = m.get('ModifyType')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        self.port_ranges = []
        if m.get('PortRanges') is not None:
            for k1 in m.get('PortRanges'):
                temp_model = main_models.UpdatePrivateAccessApplicationRequestPortRanges()
                self.port_ranges.append(temp_model.from_map(k1))

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TagIds') is not None:
            self.tag_ids = m.get('TagIds')

        if m.get('UnauthorizedAccessConfig') is not None:
            temp_model = main_models.PAApplicationUnauthorizedAccessConfig()
            self.unauthorized_access_config = temp_model.from_map(m.get('UnauthorizedAccessConfig'))

        return self

class UpdatePrivateAccessApplicationRequestPortRanges(DaraModel):
    def __init__(
        self,
        begin: int = None,
        end: int = None,
    ):
        # The start port. The value must be less than or equal to the end port.
        self.begin = begin
        # The end port. The value must be greater than or equal to the start port.
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

