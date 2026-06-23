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
        # The list of client information.
        self.client_info_list = client_info_list
        # The page number of the list.
        self.page_number = page_number
        # The maximum number of entries per page in a paged query.
        self.page_size = page_size
        # The region ID of the VPN gateway instance.
        self.region_id = region_id
        # The request ID.
        self.request_id = request_id
        # The total number of entries in the list.
        self.total_count = total_count
        # The VPN gateway instance ID.
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
        # The SSL client certificate used by the client to establish the SSL-VPN connection to Alibaba Cloud.
        # 
        # > If the client uses two-factor identity authentication to establish the SSL-VPN connection to Alibaba Cloud, the value of this parameter is the username of the client.
        self.common_name = common_name
        # The timestamp when the client established the SSL-VPN connection to Alibaba Cloud. Unit: milliseconds.
        # 
        # The timestamp is in the UNIX format and represents the total number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC to the time when the SSL-VPN connection was established.
        self.connected_time = connected_time
        # The public IP address that the client used to establish the SSL-VPN connection to Alibaba Cloud.
        self.ip = ip
        # The port number that the client used to establish the SSL-VPN connection to Alibaba Cloud.
        self.port = port
        # The private IP address that the VPN gateway assigned to the client when the client established an SSL-VPN connection to Alibaba Cloud.
        self.private_ip = private_ip
        # The traffic that the VPN gateway received from the client over the SSL-VPN connection. Unit: bytes.
        self.receive_bytes = receive_bytes
        # The traffic that the VPN gateway sent to the client over the SSL-VPN connection. Unit: bytes.
        self.send_bytes = send_bytes
        # The status of the SSL-VPN connection.
        # 
        # Valid values: **online**, which indicates that the client has successfully established an SSL-VPN connection to Alibaba Cloud.
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

