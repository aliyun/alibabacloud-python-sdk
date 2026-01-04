# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateDomainIcpNumberRequest(DaraModel):
    def __init__(
        self,
        domain_id: str = None,
        icp_number: str = None,
        instance_id: str = None,
    ):
        # 域名ID。
        # 
        # This parameter is required.
        self.domain_id = domain_id
        # 域名关联的备案号，长度最大限制64。
        # 
        # This parameter is required.
        self.icp_number = icp_number
        # IDaaS EIAM实例的ID。
        # 
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_id is not None:
            result['DomainId'] = self.domain_id

        if self.icp_number is not None:
            result['IcpNumber'] = self.icp_number

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainId') is not None:
            self.domain_id = m.get('DomainId')

        if m.get('IcpNumber') is not None:
            self.icp_number = m.get('IcpNumber')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

