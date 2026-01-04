# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class ListDomainsResponseBody(DaraModel):
    def __init__(
        self,
        domains: List[main_models.ListDomainsResponseBodyDomains] = None,
        request_id: str = None,
    ):
        # The information about the domain names.
        self.domains = domains
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.domains:
            for v1 in self.domains:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Domains'] = []
        if self.domains is not None:
            for k1 in self.domains:
                result['Domains'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.domains = []
        if m.get('Domains') is not None:
            for k1 in m.get('Domains'):
                temp_model = main_models.ListDomainsResponseBodyDomains()
                self.domains.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListDomainsResponseBodyDomains(DaraModel):
    def __init__(
        self,
        brand_id: str = None,
        create_time: int = None,
        default_domain: bool = None,
        domain: str = None,
        domain_id: str = None,
        domain_type: str = None,
        filing: main_models.ListDomainsResponseBodyDomainsFiling = None,
        instance_id: str = None,
        lock_mode: str = None,
        update_time: int = None,
    ):
        self.brand_id = brand_id
        # The time when the domain name was created. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.create_time = create_time
        # Indicates whether the domain name is the default domain.
        self.default_domain = default_domain
        # The domain.
        self.domain = domain
        # The domain ID.
        self.domain_id = domain_id
        # The type of the domain name. Valid values:
        # 
        # *   system_init: an initial domain name.
        # *   user_custom: a custom domain name.
        self.domain_type = domain_type
        # The information about the Internet content provider (ICP) filing of the domain name.
        self.filing = filing
        # The instance ID.
        self.instance_id = instance_id
        # Indicates whether the domain name is locked. Valid values:
        # 
        # *   unlock
        # *   lockByLicense
        self.lock_mode = lock_mode
        # The time when the domain name was last updated. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.update_time = update_time

    def validate(self):
        if self.filing:
            self.filing.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.brand_id is not None:
            result['BrandId'] = self.brand_id

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.default_domain is not None:
            result['DefaultDomain'] = self.default_domain

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.domain_id is not None:
            result['DomainId'] = self.domain_id

        if self.domain_type is not None:
            result['DomainType'] = self.domain_type

        if self.filing is not None:
            result['Filing'] = self.filing.to_map()

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.lock_mode is not None:
            result['LockMode'] = self.lock_mode

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BrandId') is not None:
            self.brand_id = m.get('BrandId')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DefaultDomain') is not None:
            self.default_domain = m.get('DefaultDomain')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('DomainId') is not None:
            self.domain_id = m.get('DomainId')

        if m.get('DomainType') is not None:
            self.domain_type = m.get('DomainType')

        if m.get('Filing') is not None:
            temp_model = main_models.ListDomainsResponseBodyDomainsFiling()
            self.filing = temp_model.from_map(m.get('Filing'))

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('LockMode') is not None:
            self.lock_mode = m.get('LockMode')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

class ListDomainsResponseBodyDomainsFiling(DaraModel):
    def __init__(
        self,
        icp_number: str = None,
    ):
        # The ICP number associated with the domain name. Both the entity ICP number and website ICP number are supported.
        self.icp_number = icp_number

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.icp_number is not None:
            result['IcpNumber'] = self.icp_number

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IcpNumber') is not None:
            self.icp_number = m.get('IcpNumber')

        return self

