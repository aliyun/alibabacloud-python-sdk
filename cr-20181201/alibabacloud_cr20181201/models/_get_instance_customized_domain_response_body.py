# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetInstanceCustomizedDomainResponseBody(DaraModel):
    def __init__(
        self,
        cert_id: str = None,
        code: str = None,
        create_time: int = None,
        domain: str = None,
        domain_type: str = None,
        endpoint_type: str = None,
        instance_id: str = None,
        is_success: bool = None,
        modified_time: int = None,
        module_name: str = None,
        region_id: str = None,
        request_id: str = None,
    ):
        self.cert_id = cert_id
        self.code = code
        self.create_time = create_time
        self.domain = domain
        self.domain_type = domain_type
        self.endpoint_type = endpoint_type
        self.instance_id = instance_id
        self.is_success = is_success
        self.modified_time = modified_time
        self.module_name = module_name
        self.region_id = region_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cert_id is not None:
            result['CertId'] = self.cert_id

        if self.code is not None:
            result['Code'] = self.code

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.domain_type is not None:
            result['DomainType'] = self.domain_type

        if self.endpoint_type is not None:
            result['EndpointType'] = self.endpoint_type

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.is_success is not None:
            result['IsSuccess'] = self.is_success

        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time

        if self.module_name is not None:
            result['ModuleName'] = self.module_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertId') is not None:
            self.cert_id = m.get('CertId')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('DomainType') is not None:
            self.domain_type = m.get('DomainType')

        if m.get('EndpointType') is not None:
            self.endpoint_type = m.get('EndpointType')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')

        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')

        if m.get('ModuleName') is not None:
            self.module_name = m.get('ModuleName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

