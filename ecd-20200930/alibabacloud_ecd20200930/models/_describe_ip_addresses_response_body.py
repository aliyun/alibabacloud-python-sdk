# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class DescribeIpAddressesResponseBody(DaraModel):
    def __init__(
        self,
        ip_addresses: List[main_models.DescribeIpAddressesResponseBodyIpAddresses] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
    ):
        self.ip_addresses = ip_addresses
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id

    def validate(self):
        if self.ip_addresses:
            for v1 in self.ip_addresses:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['IpAddresses'] = []
        if self.ip_addresses is not None:
            for k1 in self.ip_addresses:
                result['IpAddresses'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ip_addresses = []
        if m.get('IpAddresses') is not None:
            for k1 in m.get('IpAddresses'):
                temp_model = main_models.DescribeIpAddressesResponseBodyIpAddresses()
                self.ip_addresses.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeIpAddressesResponseBodyIpAddresses(DaraModel):
    def __init__(
        self,
        create_by_wuying: bool = None,
        eip_address: str = None,
        eip_id: str = None,
        eip_status: str = None,
        instance_id: str = None,
        instance_type: str = None,
    ):
        self.create_by_wuying = create_by_wuying
        self.eip_address = eip_address
        self.eip_id = eip_id
        self.eip_status = eip_status
        self.instance_id = instance_id
        self.instance_type = instance_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_by_wuying is not None:
            result['CreateByWuying'] = self.create_by_wuying

        if self.eip_address is not None:
            result['EipAddress'] = self.eip_address

        if self.eip_id is not None:
            result['EipId'] = self.eip_id

        if self.eip_status is not None:
            result['EipStatus'] = self.eip_status

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateByWuying') is not None:
            self.create_by_wuying = m.get('CreateByWuying')

        if m.get('EipAddress') is not None:
            self.eip_address = m.get('EipAddress')

        if m.get('EipId') is not None:
            self.eip_id = m.get('EipId')

        if m.get('EipStatus') is not None:
            self.eip_status = m.get('EipStatus')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        return self

