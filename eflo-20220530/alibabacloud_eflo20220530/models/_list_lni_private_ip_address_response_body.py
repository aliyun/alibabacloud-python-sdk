# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eflo20220530 import models as main_models
from darabonba.model import DaraModel

class ListLniPrivateIpAddressResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: int = None,
        content: main_models.ListLniPrivateIpAddressResponseBodyContent = None,
        message: str = None,
        request_id: str = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The response status code.
        self.code = code
        # The response parameters.
        self.content = content
        # The error message. (If the instance is in the Exception state, the exception cause is prompted.)
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.code is not None:
            result['Code'] = self.code

        if self.content is not None:
            result['Content'] = self.content.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Content') is not None:
            temp_model = main_models.ListLniPrivateIpAddressResponseBodyContent()
            self.content = temp_model.from_map(m.get('Content'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListLniPrivateIpAddressResponseBodyContent(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListLniPrivateIpAddressResponseBodyContentData] = None,
        resource_group_id: str = None,
        total: int = None,
    ):
        # The returned result.
        self.data = data
        # Resource group instance ID
        self.resource_group_id = resource_group_id
        # The total number of entries returned.
        self.total = total

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListLniPrivateIpAddressResponseBodyContentData()
                self.data.append(temp_model.from_map(k1))

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class ListLniPrivateIpAddressResponseBodyContentData(DaraModel):
    def __init__(
        self,
        description: str = None,
        gmt_create: str = None,
        ip_address_mac: str = None,
        ip_name: str = None,
        message: str = None,
        network_interface_id: str = None,
        private_ip_address: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        status: str = None,
    ):
        # The instance description.
        self.description = description
        # The time when the data address was created.
        self.gmt_create = gmt_create
        # MAC address of the secondary private network
        self.ip_address_mac = ip_address_mac
        # IP unique identifier
        self.ip_name = ip_name
        # The error message. (If the instance is in the Exception state, the exception cause is prompted.)
        self.message = message
        # Lingjun network interface controller ID
        self.network_interface_id = network_interface_id
        # Secondary private IP address of Lingjun network interface controller
        self.private_ip_address = private_ip_address
        # The region ID.
        self.region_id = region_id
        # Resource group instance ID
        self.resource_group_id = resource_group_id
        # The status of the intervention entry. Valid value:
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.ip_address_mac is not None:
            result['IpAddressMac'] = self.ip_address_mac

        if self.ip_name is not None:
            result['IpName'] = self.ip_name

        if self.message is not None:
            result['Message'] = self.message

        if self.network_interface_id is not None:
            result['NetworkInterfaceId'] = self.network_interface_id

        if self.private_ip_address is not None:
            result['PrivateIpAddress'] = self.private_ip_address

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('IpAddressMac') is not None:
            self.ip_address_mac = m.get('IpAddressMac')

        if m.get('IpName') is not None:
            self.ip_name = m.get('IpName')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('NetworkInterfaceId') is not None:
            self.network_interface_id = m.get('NetworkInterfaceId')

        if m.get('PrivateIpAddress') is not None:
            self.private_ip_address = m.get('PrivateIpAddress')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

