# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateInstanceCustomizedDomainRequest(DaraModel):
    def __init__(
        self,
        cert_id: str = None,
        cert_region_id: str = None,
        domain: str = None,
        instance_id: str = None,
        module_name: str = None,
    ):
        # The certificate ID.
        # 
        # This parameter is required.
        self.cert_id = cert_id
        # The region where the certificate resides.
        self.cert_region_id = cert_region_id
        # The custom domain name.
        # 
        # This parameter is required.
        self.domain = domain
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The modified domain name.
        # 
        # This parameter is required.
        self.module_name = module_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cert_id is not None:
            result['CertId'] = self.cert_id

        if self.cert_region_id is not None:
            result['CertRegionId'] = self.cert_region_id

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.module_name is not None:
            result['ModuleName'] = self.module_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertId') is not None:
            self.cert_id = m.get('CertId')

        if m.get('CertRegionId') is not None:
            self.cert_region_id = m.get('CertRegionId')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('ModuleName') is not None:
            self.module_name = m.get('ModuleName')

        return self

