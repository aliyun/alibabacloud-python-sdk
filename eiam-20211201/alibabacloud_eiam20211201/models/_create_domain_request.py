# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class CreateDomainRequest(DaraModel):
    def __init__(
        self,
        domain: str = None,
        filing: main_models.CreateDomainRequestFiling = None,
        instance_id: str = None,
    ):
        # The domain name of the website.
        # 
        # This parameter is required.
        self.domain = domain
        # Registration information parameters.
        self.filing = filing
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        if self.filing:
            self.filing.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain is not None:
            result['Domain'] = self.domain

        if self.filing is not None:
            result['Filing'] = self.filing.to_map()

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('Filing') is not None:
            temp_model = main_models.CreateDomainRequestFiling()
            self.filing = temp_model.from_map(m.get('Filing'))

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

class CreateDomainRequestFiling(DaraModel):
    def __init__(
        self,
        icp_number: str = None,
    ):
        # Record number associated with the domain name.
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

