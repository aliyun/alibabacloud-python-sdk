# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class GetInstanceResponseBody(DaraModel):
    def __init__(
        self,
        instance: main_models.GetInstanceResponseBodyInstance = None,
        request_id: str = None,
    ):
        # The details of the instance.
        self.instance = instance
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.instance:
            self.instance.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance is not None:
            result['Instance'] = self.instance.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Instance') is not None:
            temp_model = main_models.GetInstanceResponseBodyInstance()
            self.instance = temp_model.from_map(m.get('Instance'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetInstanceResponseBodyInstance(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        default_endpoint: main_models.GetInstanceResponseBodyInstanceDefaultEndpoint = None,
        description: str = None,
        domain_config: main_models.GetInstanceResponseBodyInstanceDomainConfig = None,
        egress_addresses: List[str] = None,
        instance_id: str = None,
        managed_service_code: str = None,
        service_managed: bool = None,
        status: str = None,
    ):
        # The time when the instance was created. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.create_time = create_time
        # The default endpoint of the instance.
        self.default_endpoint = default_endpoint
        # The description of the instance.
        self.description = description
        # The default domain of the instance.
        self.domain_config = domain_config
        # The outbound public CIDR blocks of the instance. For example, when you synchronize Active Directory (AD) accounts, the IDaaS EIAM instance accesses your AD service by using the outbound public CIDR blocks.
        self.egress_addresses = egress_addresses
        # The instance ID.
        self.instance_id = instance_id
        self.managed_service_code = managed_service_code
        self.service_managed = service_managed
        # The status of the instance. Valid values:
        # 
        # *   creating
        # *   running
        self.status = status

    def validate(self):
        if self.default_endpoint:
            self.default_endpoint.validate()
        if self.domain_config:
            self.domain_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.default_endpoint is not None:
            result['DefaultEndpoint'] = self.default_endpoint.to_map()

        if self.description is not None:
            result['Description'] = self.description

        if self.domain_config is not None:
            result['DomainConfig'] = self.domain_config.to_map()

        if self.egress_addresses is not None:
            result['EgressAddresses'] = self.egress_addresses

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.managed_service_code is not None:
            result['ManagedServiceCode'] = self.managed_service_code

        if self.service_managed is not None:
            result['ServiceManaged'] = self.service_managed

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DefaultEndpoint') is not None:
            temp_model = main_models.GetInstanceResponseBodyInstanceDefaultEndpoint()
            self.default_endpoint = temp_model.from_map(m.get('DefaultEndpoint'))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DomainConfig') is not None:
            temp_model = main_models.GetInstanceResponseBodyInstanceDomainConfig()
            self.domain_config = temp_model.from_map(m.get('DomainConfig'))

        if m.get('EgressAddresses') is not None:
            self.egress_addresses = m.get('EgressAddresses')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('ManagedServiceCode') is not None:
            self.managed_service_code = m.get('ManagedServiceCode')

        if m.get('ServiceManaged') is not None:
            self.service_managed = m.get('ServiceManaged')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class GetInstanceResponseBodyInstanceDomainConfig(DaraModel):
    def __init__(
        self,
        default_domain: str = None,
        init_domain: str = None,
        init_domain_auto_redirect_status: str = None,
    ):
        # The default domain of the instance.
        self.default_domain = default_domain
        # The init domain of the instance.
        self.init_domain = init_domain
        # Valid values:
        # 
        # *   true
        # *   false
        self.init_domain_auto_redirect_status = init_domain_auto_redirect_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.default_domain is not None:
            result['DefaultDomain'] = self.default_domain

        if self.init_domain is not None:
            result['InitDomain'] = self.init_domain

        if self.init_domain_auto_redirect_status is not None:
            result['InitDomainAutoRedirectStatus'] = self.init_domain_auto_redirect_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultDomain') is not None:
            self.default_domain = m.get('DefaultDomain')

        if m.get('InitDomain') is not None:
            self.init_domain = m.get('InitDomain')

        if m.get('InitDomainAutoRedirectStatus') is not None:
            self.init_domain_auto_redirect_status = m.get('InitDomainAutoRedirectStatus')

        return self

class GetInstanceResponseBodyInstanceDefaultEndpoint(DaraModel):
    def __init__(
        self,
        endpoint: str = None,
        status: str = None,
    ):
        # The endpoint of the instance.
        self.endpoint = endpoint
        # The status of the endpoint. Valid values:
        # 
        # *   resolved
        # *   unresolved
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

