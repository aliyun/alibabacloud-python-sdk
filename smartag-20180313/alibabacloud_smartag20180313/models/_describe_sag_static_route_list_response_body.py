# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_smartag20180313 import models as main_models
from darabonba.model import DaraModel

class DescribeSagStaticRouteListResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        static_routes: List[main_models.DescribeSagStaticRouteListResponseBodyStaticRoutes] = None,
        task_states: List[main_models.DescribeSagStaticRouteListResponseBodyTaskStates] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The list of static routes.
        self.static_routes = static_routes
        # The status of the query tasks.
        self.task_states = task_states

    def validate(self):
        if self.static_routes:
            for v1 in self.static_routes:
                 if v1:
                    v1.validate()
        if self.task_states:
            for v1 in self.task_states:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['StaticRoutes'] = []
        if self.static_routes is not None:
            for k1 in self.static_routes:
                result['StaticRoutes'].append(k1.to_map() if k1 else None)

        result['TaskStates'] = []
        if self.task_states is not None:
            for k1 in self.task_states:
                result['TaskStates'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.static_routes = []
        if m.get('StaticRoutes') is not None:
            for k1 in m.get('StaticRoutes'):
                temp_model = main_models.DescribeSagStaticRouteListResponseBodyStaticRoutes()
                self.static_routes.append(temp_model.from_map(k1))

        self.task_states = []
        if m.get('TaskStates') is not None:
            for k1 in m.get('TaskStates'):
                temp_model = main_models.DescribeSagStaticRouteListResponseBodyTaskStates()
                self.task_states.append(temp_model.from_map(k1))

        return self

class DescribeSagStaticRouteListResponseBodyTaskStates(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        error_code: str = None,
        error_message: str = None,
        state: str = None,
    ):
        # The time when the query task was created.
        self.create_time = create_time
        # The error code. A value of 200 indicates that the query task is successful.
        self.error_code = error_code
        # The error message. A value of Successful indicates that the query task is successful.
        self.error_message = error_message
        # The status of the asynchronous task. Valid values:
        # - **Initialized**: The query task is initialized.
        # - **Offline**: The Smart Access Gateway device is offline and the query task is not delivered. The task will be delivered after the device goes online.
        # - **Succeed**: The query task is delivered successfully.
        # - **Processing**: The query task is being delivered.
        # - **VersionNotSupport**: The current version of the Smart Access Gateway device does not support this feature.
        # - **BuildRequestError**: The management and control system does not support the request.
        # - **HardwareError**: The query task failed to be delivered due to a device error.
        # - **TaskNotExist**: The query task does not exist.
        # - **OfflineNotConfiged**: The Smart Access Gateway device is offline and the query task is not delivered. The task will not be delivered even after the device goes online.
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.state is not None:
            result['State'] = self.state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('State') is not None:
            self.state = m.get('State')

        return self

class DescribeSagStaticRouteListResponseBodyStaticRoutes(DaraModel):
    def __init__(
        self,
        destination_cidr: str = None,
        next_hop: str = None,
        port_name: str = None,
        vlan: str = None,
    ):
        # The destination CIDR block.
        self.destination_cidr = destination_cidr
        # The next hop.
        self.next_hop = next_hop
        # The port name.
        self.port_name = port_name
        # The VLAN ID.
        self.vlan = vlan

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.destination_cidr is not None:
            result['DestinationCidr'] = self.destination_cidr

        if self.next_hop is not None:
            result['NextHop'] = self.next_hop

        if self.port_name is not None:
            result['PortName'] = self.port_name

        if self.vlan is not None:
            result['Vlan'] = self.vlan

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationCidr') is not None:
            self.destination_cidr = m.get('DestinationCidr')

        if m.get('NextHop') is not None:
            self.next_hop = m.get('NextHop')

        if m.get('PortName') is not None:
            self.port_name = m.get('PortName')

        if m.get('Vlan') is not None:
            self.vlan = m.get('Vlan')

        return self

