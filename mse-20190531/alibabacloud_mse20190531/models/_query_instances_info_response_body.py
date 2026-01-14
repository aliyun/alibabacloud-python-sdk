# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mse20190531 import models as main_models
from darabonba.model import DaraModel

class QueryInstancesInfoResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.QueryInstancesInfoResponseBodyData] = None,
        error_code: str = None,
        http_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The details of the data.
        self.data = data
        # The error code returned if the request failed.
        self.error_code = error_code
        # The HTTP status code.
        self.http_code = http_code
        # The message that is returned.
        # 
        # *   If the request is successful, a success message is returned.
        # *   If the request fails, an error message is returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   `true`: The request was successful.
        # *   `false`: The request failed.
        self.success = success

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

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.http_code is not None:
            result['HttpCode'] = self.http_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.QueryInstancesInfoResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryInstancesInfoResponseBodyData(DaraModel):
    def __init__(
        self,
        client_port: str = None,
        creation_timestamp: str = None,
        health_status: str = None,
        internet_ip: str = None,
        ip: str = None,
        pod_name: str = None,
        role: str = None,
        single_tunnel_vip: str = None,
        zone: str = None,
        zone_distributed: bool = None,
    ):
        # The enabled port.
        self.client_port = client_port
        # The creation time.
        self.creation_timestamp = creation_timestamp
        # A reserved parameter.
        self.health_status = health_status
        # The public IP address.
        self.internet_ip = internet_ip
        # The IP address of the pod.
        self.ip = ip
        # The pod name.
        self.pod_name = pod_name
        # A reserved parameter.
        self.role = role
        # The internal IP address.
        self.single_tunnel_vip = single_tunnel_vip
        # The zone ID.
        self.zone = zone
        # Indicates whether all pods in the cluster are distributed in the specified zones.
        self.zone_distributed = zone_distributed

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_port is not None:
            result['ClientPort'] = self.client_port

        if self.creation_timestamp is not None:
            result['CreationTimestamp'] = self.creation_timestamp

        if self.health_status is not None:
            result['HealthStatus'] = self.health_status

        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip

        if self.ip is not None:
            result['Ip'] = self.ip

        if self.pod_name is not None:
            result['PodName'] = self.pod_name

        if self.role is not None:
            result['Role'] = self.role

        if self.single_tunnel_vip is not None:
            result['SingleTunnelVip'] = self.single_tunnel_vip

        if self.zone is not None:
            result['Zone'] = self.zone

        if self.zone_distributed is not None:
            result['ZoneDistributed'] = self.zone_distributed

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientPort') is not None:
            self.client_port = m.get('ClientPort')

        if m.get('CreationTimestamp') is not None:
            self.creation_timestamp = m.get('CreationTimestamp')

        if m.get('HealthStatus') is not None:
            self.health_status = m.get('HealthStatus')

        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('PodName') is not None:
            self.pod_name = m.get('PodName')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        if m.get('SingleTunnelVip') is not None:
            self.single_tunnel_vip = m.get('SingleTunnelVip')

        if m.get('Zone') is not None:
            self.zone = m.get('Zone')

        if m.get('ZoneDistributed') is not None:
            self.zone_distributed = m.get('ZoneDistributed')

        return self

