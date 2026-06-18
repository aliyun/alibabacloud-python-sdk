# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class UpdateOriginPoolRequest(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
        id: int = None,
        origins: List[main_models.UpdateOriginPoolRequestOrigins] = None,
        site_id: int = None,
    ):
        # Specifies whether to enable the origin pool:
        # 
        # - true: Enables the origin pool.
        # 
        # - false: Disables the origin pool.
        self.enabled = enabled
        # The origin pool ID. Get this ID by calling the [ListOriginPools](~~ListOriginPools~~) operation.
        # 
        # This parameter is required.
        self.id = id
        # An array of origin configurations.
        self.origins = origins
        # The site ID. Get this ID by calling the [ListSites](~~ListSites~~) operation.
        # 
        # This parameter is required.
        self.site_id = site_id

    def validate(self):
        if self.origins:
            for v1 in self.origins:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.id is not None:
            result['Id'] = self.id

        result['Origins'] = []
        if self.origins is not None:
            for k1 in self.origins:
                result['Origins'].append(k1.to_map() if k1 else None)

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        self.origins = []
        if m.get('Origins') is not None:
            for k1 in m.get('Origins'):
                temp_model = main_models.UpdateOriginPoolRequestOrigins()
                self.origins.append(temp_model.from_map(k1))

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        return self

class UpdateOriginPoolRequestOrigins(DaraModel):
    def __init__(
        self,
        address: str = None,
        auth_conf: main_models.UpdateOriginPoolRequestOriginsAuthConf = None,
        enabled: bool = None,
        header: Any = None,
        ip_version_policy: str = None,
        name: str = None,
        type: str = None,
        weight: int = None,
    ):
        # The origin\\"s domain name or IP address.
        self.address = address
        # The authentication configuration. Required for private OSS or S3 origins.
        self.auth_conf = auth_conf
        # Specifies whether to enable the origin:
        # 
        # - true: Enables the origin.
        # 
        # - false: Disables the origin.
        self.enabled = enabled
        # The request header to add to back-to-origin requests. Only the Host header is supported.
        self.header = header
        # The IP version policy for back-to-origin requests. Valid values:
        # 
        # - round_robin: (Default) Randomly selects an IPv4 or IPv6 origin.
        # 
        # - ipv4_first: Prioritizes IPv4 origins.
        # 
        # - ipv6_first: Prioritizes IPv6 origins.
        # 
        # - follow: Uses the same IP version as the client request.
        self.ip_version_policy = ip_version_policy
        # The name of the origin. The name must be unique within the origin pool.
        self.name = name
        # The origin type. Valid values:
        # 
        # - ip_domain: An IP address or a domain name.
        # 
        # - OSS: An OSS origin.
        # 
        # - S3: An AWS S3 origin.
        self.type = type
        # The weight of the origin. The value must be an integer from 0 to 100.
        self.weight = weight

    def validate(self):
        if self.auth_conf:
            self.auth_conf.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address is not None:
            result['Address'] = self.address

        if self.auth_conf is not None:
            result['AuthConf'] = self.auth_conf.to_map()

        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.header is not None:
            result['Header'] = self.header

        if self.ip_version_policy is not None:
            result['IpVersionPolicy'] = self.ip_version_policy

        if self.name is not None:
            result['Name'] = self.name

        if self.type is not None:
            result['Type'] = self.type

        if self.weight is not None:
            result['Weight'] = self.weight

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')

        if m.get('AuthConf') is not None:
            temp_model = main_models.UpdateOriginPoolRequestOriginsAuthConf()
            self.auth_conf = temp_model.from_map(m.get('AuthConf'))

        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('Header') is not None:
            self.header = m.get('Header')

        if m.get('IpVersionPolicy') is not None:
            self.ip_version_policy = m.get('IpVersionPolicy')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Weight') is not None:
            self.weight = m.get('Weight')

        return self

class UpdateOriginPoolRequestOriginsAuthConf(DaraModel):
    def __init__(
        self,
        access_key: str = None,
        auth_type: str = None,
        region: str = None,
        secret_key: str = None,
        version: str = None,
    ):
        # The access key for private authentication. Required for private origins.
        self.access_key = access_key
        # The authentication type. Valid values:
        # 
        # - public: For public OSS or S3 origins.
        # 
        # - private_same_account: For private OSS origins in the same account.
        # 
        # - private_cross_account: For private OSS origins that use cross-account authentication.
        # 
        # - private: For private S3 origins.
        self.auth_type = auth_type
        # The region of the origin. This parameter is required if the origin type is S3.
        self.region = region
        # The secret key for private authentication. Required for private origins.
        self.secret_key = secret_key
        # The signature version. This parameter is required if the origin type is S3.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_key is not None:
            result['AccessKey'] = self.access_key

        if self.auth_type is not None:
            result['AuthType'] = self.auth_type

        if self.region is not None:
            result['Region'] = self.region

        if self.secret_key is not None:
            result['SecretKey'] = self.secret_key

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessKey') is not None:
            self.access_key = m.get('AccessKey')

        if m.get('AuthType') is not None:
            self.auth_type = m.get('AuthType')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('SecretKey') is not None:
            self.secret_key = m.get('SecretKey')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

