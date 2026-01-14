# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mse20190531 import models as main_models
from darabonba.model import DaraModel

class ListNamingTrackResponseBody(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        http_code: str = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
        traces: List[main_models.ListNamingTrackResponseBodyTraces] = None,
    ):
        # The error code returned if the request failed.
        self.error_code = error_code
        # The HTTP status code returned.
        self.http_code = http_code
        # The message returned.
        self.message = message
        # The number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   `true`: The request was successful.
        # *   `false`: The request failed.
        self.success = success
        # The total number of returned entries.
        self.total_count = total_count
        # The data information.
        self.traces = traces

    def validate(self):
        if self.traces:
            for v1 in self.traces:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.http_code is not None:
            result['HttpCode'] = self.http_code

        if self.message is not None:
            result['Message'] = self.message

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        result['Traces'] = []
        if self.traces is not None:
            for k1 in self.traces:
                result['Traces'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        self.traces = []
        if m.get('Traces') is not None:
            for k1 in m.get('Traces'):
                temp_model = main_models.ListNamingTrackResponseBodyTraces()
                self.traces.append(temp_model.from_map(k1))

        return self

class ListNamingTrackResponseBodyTraces(DaraModel):
    def __init__(
        self,
        client_ip: str = None,
        group: str = None,
        instance_size: str = None,
        node_name: str = None,
        push_time: str = None,
        push_time_all: str = None,
        push_time_network: str = None,
        server_name: str = None,
        sla_time: str = None,
    ):
        # The IP address of the client.
        self.client_ip = client_ip
        # The group.
        self.group = group
        # The number of instances.
        self.instance_size = instance_size
        # The name of the node.
        self.node_name = node_name
        # The push time.
        self.push_time = push_time
        # The total push time.
        self.push_time_all = push_time_all
        # The push time for the network.
        self.push_time_network = push_time_network
        # The name of the service.
        self.server_name = server_name
        # The duration that is specified in the service-level agreement (SLA).
        self.sla_time = sla_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_ip is not None:
            result['ClientIp'] = self.client_ip

        if self.group is not None:
            result['Group'] = self.group

        if self.instance_size is not None:
            result['InstanceSize'] = self.instance_size

        if self.node_name is not None:
            result['NodeName'] = self.node_name

        if self.push_time is not None:
            result['PushTime'] = self.push_time

        if self.push_time_all is not None:
            result['PushTimeAll'] = self.push_time_all

        if self.push_time_network is not None:
            result['PushTimeNetwork'] = self.push_time_network

        if self.server_name is not None:
            result['ServerName'] = self.server_name

        if self.sla_time is not None:
            result['SlaTime'] = self.sla_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientIp') is not None:
            self.client_ip = m.get('ClientIp')

        if m.get('Group') is not None:
            self.group = m.get('Group')

        if m.get('InstanceSize') is not None:
            self.instance_size = m.get('InstanceSize')

        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')

        if m.get('PushTime') is not None:
            self.push_time = m.get('PushTime')

        if m.get('PushTimeAll') is not None:
            self.push_time_all = m.get('PushTimeAll')

        if m.get('PushTimeNetwork') is not None:
            self.push_time_network = m.get('PushTimeNetwork')

        if m.get('ServerName') is not None:
            self.server_name = m.get('ServerName')

        if m.get('SlaTime') is not None:
            self.sla_time = m.get('SlaTime')

        return self

