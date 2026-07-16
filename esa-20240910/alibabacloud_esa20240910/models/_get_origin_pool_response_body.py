# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class GetOriginPoolResponseBody(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
        id: int = None,
        name: str = None,
        origins: List[main_models.GetOriginPoolResponseBodyOrigins] = None,
        record_name: str = None,
        reference_lbcount: int = None,
        references: main_models.GetOriginPoolResponseBodyReferences = None,
        request_id: str = None,
        site_id: int = None,
    ):
        # Specifies if the origin pool is enabled.
        # 
        # - true: The origin pool is enabled.
        # 
        # - false: The origin pool is disabled.
        self.enabled = enabled
        # The origin pool ID.
        self.id = id
        # The name of the origin pool. The name must be unique within a site.
        self.name = name
        # The origins in the origin pool.
        self.origins = origins
        # The domain name assigned to the origin pool. It serves as the origin address for records within the site.
        self.record_name = record_name
        # The number of load balancers that reference this origin pool.
        self.reference_lbcount = reference_lbcount
        # Resources that reference the origin pool. An origin pool is referenced if a load balancer or record uses it as an origin.
        self.references = references
        # The request ID.
        self.request_id = request_id
        # The ID of the site that contains the origin pool.
        self.site_id = site_id

    def validate(self):
        if self.origins:
            for v1 in self.origins:
                 if v1:
                    v1.validate()
        if self.references:
            self.references.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        result['Origins'] = []
        if self.origins is not None:
            for k1 in self.origins:
                result['Origins'].append(k1.to_map() if k1 else None)

        if self.record_name is not None:
            result['RecordName'] = self.record_name

        if self.reference_lbcount is not None:
            result['ReferenceLBCount'] = self.reference_lbcount

        if self.references is not None:
            result['References'] = self.references.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        self.origins = []
        if m.get('Origins') is not None:
            for k1 in m.get('Origins'):
                temp_model = main_models.GetOriginPoolResponseBodyOrigins()
                self.origins.append(temp_model.from_map(k1))

        if m.get('RecordName') is not None:
            self.record_name = m.get('RecordName')

        if m.get('ReferenceLBCount') is not None:
            self.reference_lbcount = m.get('ReferenceLBCount')

        if m.get('References') is not None:
            temp_model = main_models.GetOriginPoolResponseBodyReferences()
            self.references = temp_model.from_map(m.get('References'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        return self

class GetOriginPoolResponseBodyReferences(DaraModel):
    def __init__(
        self,
        dns_records: List[main_models.GetOriginPoolResponseBodyReferencesDnsRecords] = None,
        iparecords: List[main_models.GetOriginPoolResponseBodyReferencesIPARecords] = None,
        load_balancers: List[main_models.GetOriginPoolResponseBodyReferencesLoadBalancers] = None,
    ):
        # The Layer 7 records that use this origin pool as their origin.
        self.dns_records = dns_records
        # The Layer 4 records that use this origin pool as their origin.
        self.iparecords = iparecords
        # The load balancers that use this origin pool.
        self.load_balancers = load_balancers

    def validate(self):
        if self.dns_records:
            for v1 in self.dns_records:
                 if v1:
                    v1.validate()
        if self.iparecords:
            for v1 in self.iparecords:
                 if v1:
                    v1.validate()
        if self.load_balancers:
            for v1 in self.load_balancers:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DnsRecords'] = []
        if self.dns_records is not None:
            for k1 in self.dns_records:
                result['DnsRecords'].append(k1.to_map() if k1 else None)

        result['IPARecords'] = []
        if self.iparecords is not None:
            for k1 in self.iparecords:
                result['IPARecords'].append(k1.to_map() if k1 else None)

        result['LoadBalancers'] = []
        if self.load_balancers is not None:
            for k1 in self.load_balancers:
                result['LoadBalancers'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dns_records = []
        if m.get('DnsRecords') is not None:
            for k1 in m.get('DnsRecords'):
                temp_model = main_models.GetOriginPoolResponseBodyReferencesDnsRecords()
                self.dns_records.append(temp_model.from_map(k1))

        self.iparecords = []
        if m.get('IPARecords') is not None:
            for k1 in m.get('IPARecords'):
                temp_model = main_models.GetOriginPoolResponseBodyReferencesIPARecords()
                self.iparecords.append(temp_model.from_map(k1))

        self.load_balancers = []
        if m.get('LoadBalancers') is not None:
            for k1 in m.get('LoadBalancers'):
                temp_model = main_models.GetOriginPoolResponseBodyReferencesLoadBalancers()
                self.load_balancers.append(temp_model.from_map(k1))

        return self

class GetOriginPoolResponseBodyReferencesLoadBalancers(DaraModel):
    def __init__(
        self,
        id: int = None,
        name: str = None,
    ):
        # The ID of the load balancer.
        self.id = id
        # The name of the load balancer.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class GetOriginPoolResponseBodyReferencesIPARecords(DaraModel):
    def __init__(
        self,
        id: int = None,
        name: str = None,
    ):
        # The ID of the record.
        self.id = id
        # The name of the record.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class GetOriginPoolResponseBodyReferencesDnsRecords(DaraModel):
    def __init__(
        self,
        id: int = None,
        name: str = None,
    ):
        # The ID of the record.
        self.id = id
        # The name of the record.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class GetOriginPoolResponseBodyOrigins(DaraModel):
    def __init__(
        self,
        address: str = None,
        auth_conf: main_models.GetOriginPoolResponseBodyOriginsAuthConf = None,
        enabled: bool = None,
        header: Any = None,
        id: int = None,
        ip_version_policy: str = None,
        name: str = None,
        type: str = None,
        weight: int = None,
    ):
        # The origin address. For example, www\\.example.com.
        self.address = address
        # The authentication configuration. This parameter is required if the origin is an OSS or S3 bucket that requires authentication.
        self.auth_conf = auth_conf
        # Specifies if the origin is enabled.
        # 
        # - true: The origin is enabled.
        # 
        # - false: The origin is disabled.
        self.enabled = enabled
        # The request header to include in origin requests. Only the Host header is supported.
        self.header = header
        # The origin ID.
        self.id = id
        # The IP version policy for origin requests.
        # 
        # - round_robin: Default policy. Routes requests to IPv4 and IPv6 origins on a round-robin basis.
        # 
        # - ipv4_first: Prioritizes IPv4. Routes requests to IPv4 origins first.
        # 
        # - ipv6_first: Prioritizes IPv6. Routes requests to IPv6 origins first.
        # 
        # - follow: Matches the client\\"s IP version. The origin request uses the same IP version as the incoming request.
        self.ip_version_policy = ip_version_policy
        # The origin name.
        self.name = name
        # The type of the origin.
        # 
        # - ip_domain: An IP address or a domain name.
        # 
        # - OSS: An OSS bucket.
        # 
        # - S3: An AWS S3 bucket.
        self.type = type
        # The weight of the origin. Must be an integer from 0 to 100.
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

        if self.id is not None:
            result['Id'] = self.id

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
            temp_model = main_models.GetOriginPoolResponseBodyOriginsAuthConf()
            self.auth_conf = temp_model.from_map(m.get('AuthConf'))

        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('Header') is not None:
            self.header = m.get('Header')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('IpVersionPolicy') is not None:
            self.ip_version_policy = m.get('IpVersionPolicy')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Weight') is not None:
            self.weight = m.get('Weight')

        return self

class GetOriginPoolResponseBodyOriginsAuthConf(DaraModel):
    def __init__(
        self,
        access_key: str = None,
        auth_type: str = None,
        region: str = None,
        secret_key: str = None,
        version: str = None,
    ):
        # The AccessKey ID. This parameter is required if `AuthType` is set to `private_cross_account` or `private`.
        self.access_key = access_key
        # The authentication type.
        # 
        # - public: Public access. For OSS or S3 origins with public read access.
        # 
        # - private_same_account: Private, same account. For private OSS origins in the same account.
        # 
        # - private_cross_account: Private, cross-account. For private OSS origins in a different account.
        # 
        # - private: Private. For private S3 origins.
        self.auth_type = auth_type
        # The AWS Region of the origin. Required if the origin is an AWS S3 bucket.
        self.region = region
        # The AccessKey secret. This parameter is required if `AuthType` is set to `private_cross_account` or `private`.
        self.secret_key = secret_key
        # The signature version. Required if the origin is an AWS S3 bucket.
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

