# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class GetDomainResponseBody(DaraModel):
    def __init__(
        self,
        domain: main_models.GetDomainResponseBodyDomain = None,
        request_id: str = None,
    ):
        # The domain name.
        self.domain = domain
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.domain:
            self.domain.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain is not None:
            result['Domain'] = self.domain.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            temp_model = main_models.GetDomainResponseBodyDomain()
            self.domain = temp_model.from_map(m.get('Domain'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetDomainResponseBodyDomain(DaraModel):
    def __init__(
        self,
        brand_id: str = None,
        create_time: int = None,
        default_domain: bool = None,
        domain: str = None,
        domain_id: str = None,
        domain_type: str = None,
        filing: main_models.GetDomainResponseBodyDomainFiling = None,
        instance_id: str = None,
        lock_mode: str = None,
        update_time: int = None,
    ):
        self.brand_id = brand_id
        # The start time when the change order was created.
        self.create_time = create_time
        # Whether it is the default domain.
        self.default_domain = default_domain
        # The domain.
        self.domain = domain
        # Domain ID.
        self.domain_id = domain_id
        # The type of the domain name. Valid values:
        # 
        # *   **system_init**: Initialize domain
        # *   **user_custom**: user custom domain
        self.domain_type = domain_type
        # Domain registration information.
        self.filing = filing
        # The instance ID.
        self.instance_id = instance_id
        # The lock status of the instance. Valid values:
        # 
        # *   **Unlock**: The instance is normal.
        # *   **lockByLicense**: Not available due to license restrictions.
        self.lock_mode = lock_mode
        # The time when the service was updated.
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
            temp_model = main_models.GetDomainResponseBodyDomainFiling()
            self.filing = temp_model.from_map(m.get('Filing'))

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('LockMode') is not None:
            self.lock_mode = m.get('LockMode')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

class GetDomainResponseBodyDomainFiling(DaraModel):
    def __init__(
        self,
        icp_number: str = None,
    ):
        # <notice>The ICP filing number is only applicable for services in the China region.  For non-China regions, no validation or display of this record number will be performed.</notice>
        # The ICP filing number associated with the domain name, with a maximum length of 64 characters.
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

