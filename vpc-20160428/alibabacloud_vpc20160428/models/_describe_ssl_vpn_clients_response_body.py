# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class DescribeSslVpnClientsResponseBody(DaraModel):
    def __init__(
        self,
        client_info_list: List[main_models.DescribeSslVpnClientsResponseBodyClientInfoList] = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        request_id: str = None,
        total_count: int = None,
        vpn_gateway_id: str = None,
    ):
        # The list of clients.
        self.client_info_list = client_info_list
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The region ID.
        self.region_id = region_id
        # The request ID.
        self.request_id = request_id
        # The number of returned entries.
        self.total_count = total_count
        # The ID of the VPN gateway.
        self.vpn_gateway_id = vpn_gateway_id

    def validate(self):
        if self.client_info_list:
            for v1 in self.client_info_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ClientInfoList'] = []
        if self.client_info_list is not None:
            for k1 in self.client_info_list:
                result['ClientInfoList'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.vpn_gateway_id is not None:
            result['VpnGatewayId'] = self.vpn_gateway_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.client_info_list = []
        if m.get('ClientInfoList') is not None:
            for k1 in m.get('ClientInfoList'):
                temp_model = main_models.DescribeSslVpnClientsResponseBodyClientInfoList()
                self.client_info_list.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('VpnGatewayId') is not None:
            self.vpn_gateway_id = m.get('VpnGatewayId')

        return self

class DescribeSslVpnClientsResponseBodyClientInfoList(DaraModel):
    def __init__(
        self,
        common_name: str = None,
        connected_time: int = None,
        ip: str = None,
        port: str = None,
        private_ip: str = None,
        receive_bytes: int = None,
        send_bytes: int = None,
        status: str = None,
    ):
        # The SSL client certificate used by the client.
        # 
        # >  If the client uses two-factor authentication to establish an SSL-VPN connection to Alibaba Cloud, the return value is the username of the client.
        self.common_name = common_name
        # The timestamp that indicates when the client connected to Alibaba Cloud through an SSL-VPN connection. Unit: milliseconds.
        # 
        # This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.connected_time = connected_time
        # The actual public IP address used by the client when the client established an SSL-VPN connection to Alibaba Cloud.
        self.ip = ip
        # The port used by the client when the client established an SSL-VPN connection to Alibaba Cloud.
        self.port = port
        # The private IP address allocated to the client by the VPN gateway when the client established an SSL-VPN connection to Alibaba Cloud.
        self.private_ip = private_ip
        # The amount of data transferred from the client to the VPN gateway through the SSL-VPN connection. Unit: bytes.
        self.receive_bytes = receive_bytes
        # The amount of data transferred from the VPN gateway to the client through the SSL-VPN connection. Unit: bytes.
        self.send_bytes = send_bytes
        # The status of the SSL-VPN connection.
        # 
        # The value is set to **online**, which indicates that the client has connected to Alibaba Cloud through an SSL-VPN connection.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.common_name is not None:
            result['CommonName'] = self.common_name

        if self.connected_time is not None:
            result['ConnectedTime'] = self.connected_time

        if self.ip is not None:
            result['Ip'] = self.ip

        if self.port is not None:
            result['Port'] = self.port

        if self.private_ip is not None:
            result['PrivateIp'] = self.private_ip

        if self.receive_bytes is not None:
            result['ReceiveBytes'] = self.receive_bytes

        if self.send_bytes is not None:
            result['SendBytes'] = self.send_bytes

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommonName') is not None:
            self.common_name = m.get('CommonName')

        if m.get('ConnectedTime') is not None:
            self.connected_time = m.get('ConnectedTime')

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('PrivateIp') is not None:
            self.private_ip = m.get('PrivateIp')

        if m.get('ReceiveBytes') is not None:
            self.receive_bytes = m.get('ReceiveBytes')

        if m.get('SendBytes') is not None:
            self.send_bytes = m.get('SendBytes')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

