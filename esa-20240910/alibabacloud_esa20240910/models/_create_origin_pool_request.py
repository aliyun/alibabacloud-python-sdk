# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class CreateOriginPoolRequest(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
        name: str = None,
        origins: List[main_models.CreateOriginPoolRequestOrigins] = None,
        site_id: int = None,
    ):
        # Whether the origin address pool is enabled:
        # 
        # - true: Enabled;
        # - false: Disabled.
        self.enabled = enabled
        # The name of the origin address pool, which must be unique within a site.
        # 
        # This parameter is required.
        self.name = name
        # Information about the origins added to the origin address pool, with multiple origins passed as an array.
        self.origins = origins
        # The site ID, which can be obtained by calling the [ListSites](https://help.aliyun.com/document_detail/2850189.html) API.
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

        if self.name is not None:
            result['Name'] = self.name

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

        if m.get('Name') is not None:
            self.name = m.get('Name')

        self.origins = []
        if m.get('Origins') is not None:
            for k1 in m.get('Origins'):
                temp_model = main_models.CreateOriginPoolRequestOrigins()
                self.origins.append(temp_model.from_map(k1))

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        return self

class CreateOriginPoolRequestOrigins(DaraModel):
    def __init__(
        self,
        address: str = None,
        auth_conf: main_models.CreateOriginPoolRequestOriginsAuthConf = None,
        enabled: bool = None,
        header: Any = None,
        ip_version_policy: str = None,
        name: str = None,
        type: str = None,
        weight: int = None,
    ):
        # The address of the origin, e.g., www.example.com.
        self.address = address
        # Authentication information, required when the origin is OSS or S3 and needs authentication, including related configuration details.
        self.auth_conf = auth_conf
        # Whether the origin is enabled:
        # 
        # - true: Enabled;
        # - false: Disabled.
        self.enabled = enabled
        # The request header to be included when fetching from the origin, only Host is supported.
        self.header = header
        self.ip_version_policy = ip_version_policy
        # The name of the origin, which must be unique within an origin address.
        self.name = name
        # The type of the origin:
        # 
        # - ip_domain: IP or domain name type origin;
        # - OSS: OSS address origin;
        # - S3: AWS S3 origin.
        self.type = type
        # The weight, an integer between 0 and 100.
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
            temp_model = main_models.CreateOriginPoolRequestOriginsAuthConf()
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

class CreateOriginPoolRequestOriginsAuthConf(DaraModel):
    def __init__(
        self,
        access_key: str = None,
        auth_type: str = None,
        region: str = None,
        secret_key: str = None,
        version: str = None,
    ):
        # The access key required for private authentication.
        self.access_key = access_key
        # The type of authentication.
        # 
        # - public: Public read/write, used when the origin is OSS or S3 and is set to public read/write;
        # - private_same_account: Private same account, used when the origin is OSS and the authentication type is private within the same account;
        # - private_cross_account: Private cross-account, used when the origin is OSS and the authentication type is private across accounts;
        # - private: Used when the origin is S3 and the authentication type is private.
        self.auth_type = auth_type
        # The region of the origin required when the origin is AWS S3.
        self.region = region
        # The secret key required for private authentication.
        self.secret_key = secret_key
        # The signature version required when the origin is AWS S3.
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

