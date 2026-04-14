# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_emr_serverless_spark20230808 import models as main_models
from darabonba.model import DaraModel

class ListNetworkServicesResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        network_services: List[main_models.ListNetworkServicesResponseBodyNetworkServices] = None,
        next_token: str = None,
        queues: List[main_models.ListNetworkServicesResponseBodyQueues] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # 一次获取的最大记录数。
        self.max_results = max_results
        self.network_services = network_services
        # 下一页TOKEN。
        self.next_token = next_token
        self.queues = queues
        self.request_id = request_id
        # 记录总数。
        self.total_count = total_count

    def validate(self):
        if self.network_services:
            for v1 in self.network_services:
                 if v1:
                    v1.validate()
        if self.queues:
            for v1 in self.queues:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['maxResults'] = self.max_results

        result['networkServices'] = []
        if self.network_services is not None:
            for k1 in self.network_services:
                result['networkServices'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        result['queues'] = []
        if self.queues is not None:
            for k1 in self.queues:
                result['queues'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        self.network_services = []
        if m.get('networkServices') is not None:
            for k1 in m.get('networkServices'):
                temp_model = main_models.ListNetworkServicesResponseBodyNetworkServices()
                self.network_services.append(temp_model.from_map(k1))

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        self.queues = []
        if m.get('queues') is not None:
            for k1 in m.get('queues'):
                temp_model = main_models.ListNetworkServicesResponseBodyQueues()
                self.queues.append(temp_model.from_map(k1))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class ListNetworkServicesResponseBodyQueues(DaraModel):
    def __init__(
        self,
        name: str = None,
        network_service_id: str = None,
        state: str = None,
        state_change_reason: main_models.ListNetworkServicesResponseBodyQueuesStateChangeReason = None,
        type: str = None,
        vpc_id: str = None,
        vswitch_ids: List[str] = None,
        workspace_id: str = None,
    ):
        self.name = name
        self.network_service_id = network_service_id
        self.state = state
        self.state_change_reason = state_change_reason
        self.type = type
        self.vpc_id = vpc_id
        self.vswitch_ids = vswitch_ids
        self.workspace_id = workspace_id

    def validate(self):
        if self.state_change_reason:
            self.state_change_reason.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['name'] = self.name

        if self.network_service_id is not None:
            result['networkServiceId'] = self.network_service_id

        if self.state is not None:
            result['state'] = self.state

        if self.state_change_reason is not None:
            result['stateChangeReason'] = self.state_change_reason.to_map()

        if self.type is not None:
            result['type'] = self.type

        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id

        if self.vswitch_ids is not None:
            result['vswitchIds'] = self.vswitch_ids

        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('networkServiceId') is not None:
            self.network_service_id = m.get('networkServiceId')

        if m.get('state') is not None:
            self.state = m.get('state')

        if m.get('stateChangeReason') is not None:
            temp_model = main_models.ListNetworkServicesResponseBodyQueuesStateChangeReason()
            self.state_change_reason = temp_model.from_map(m.get('stateChangeReason'))

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')

        if m.get('vswitchIds') is not None:
            self.vswitch_ids = m.get('vswitchIds')

        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')

        return self

class ListNetworkServicesResponseBodyQueuesStateChangeReason(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
    ):
        self.code = code
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.message is not None:
            result['message'] = self.message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('message') is not None:
            self.message = m.get('message')

        return self

class ListNetworkServicesResponseBodyNetworkServices(DaraModel):
    def __init__(
        self,
        name: str = None,
        network_service_id: str = None,
        state: str = None,
        state_change_reason: main_models.ListNetworkServicesResponseBodyNetworkServicesStateChangeReason = None,
        type: str = None,
        vpc_id: str = None,
        vswitch_ids: List[str] = None,
        workspace_id: str = None,
    ):
        self.name = name
        self.network_service_id = network_service_id
        self.state = state
        self.state_change_reason = state_change_reason
        self.type = type
        # VPC id。
        self.vpc_id = vpc_id
        self.vswitch_ids = vswitch_ids
        self.workspace_id = workspace_id

    def validate(self):
        if self.state_change_reason:
            self.state_change_reason.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['name'] = self.name

        if self.network_service_id is not None:
            result['networkServiceId'] = self.network_service_id

        if self.state is not None:
            result['state'] = self.state

        if self.state_change_reason is not None:
            result['stateChangeReason'] = self.state_change_reason.to_map()

        if self.type is not None:
            result['type'] = self.type

        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id

        if self.vswitch_ids is not None:
            result['vswitchIds'] = self.vswitch_ids

        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('networkServiceId') is not None:
            self.network_service_id = m.get('networkServiceId')

        if m.get('state') is not None:
            self.state = m.get('state')

        if m.get('stateChangeReason') is not None:
            temp_model = main_models.ListNetworkServicesResponseBodyNetworkServicesStateChangeReason()
            self.state_change_reason = temp_model.from_map(m.get('stateChangeReason'))

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')

        if m.get('vswitchIds') is not None:
            self.vswitch_ids = m.get('vswitchIds')

        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')

        return self

class ListNetworkServicesResponseBodyNetworkServicesStateChangeReason(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
    ):
        self.code = code
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.message is not None:
            result['message'] = self.message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('message') is not None:
            self.message = m.get('message')

        return self

