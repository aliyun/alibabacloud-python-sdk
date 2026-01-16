# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_elasticsearch20170613 import models as main_models
from darabonba.model import DaraModel

class ListActionRecordsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[main_models.ListActionRecordsResponseBodyResult] = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['Result'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.ListActionRecordsResponseBodyResult()
                self.result.append(temp_model.from_map(k1))

        return self

class ListActionRecordsResponseBodyResult(DaraModel):
    def __init__(
        self,
        action_name: str = None,
        action_params: Dict[str, Any] = None,
        action_result_access_list: List[str] = None,
        end_time: int = None,
        instance_id: str = None,
        meta_now: str = None,
        meta_old: str = None,
        owner_id: str = None,
        process: str = None,
        record_diff: Dict[str, Any] = None,
        record_ids: List[str] = None,
        request_id: str = None,
        start_time: int = None,
        state_type: str = None,
        status_info: List[main_models.ListActionRecordsResponseBodyResultStatusInfo] = None,
        user_id: str = None,
        user_info: str = None,
        user_type: str = None,
    ):
        self.action_name = action_name
        self.action_params = action_params
        self.action_result_access_list = action_result_access_list
        self.end_time = end_time
        self.instance_id = instance_id
        self.meta_now = meta_now
        self.meta_old = meta_old
        self.owner_id = owner_id
        self.process = process
        self.record_diff = record_diff
        self.record_ids = record_ids
        self.request_id = request_id
        self.start_time = start_time
        self.state_type = state_type
        self.status_info = status_info
        self.user_id = user_id
        self.user_info = user_info
        self.user_type = user_type

    def validate(self):
        if self.status_info:
            for v1 in self.status_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action_name is not None:
            result['actionName'] = self.action_name

        if self.action_params is not None:
            result['actionParams'] = self.action_params

        if self.action_result_access_list is not None:
            result['actionResultAccessList'] = self.action_result_access_list

        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.meta_now is not None:
            result['metaNow'] = self.meta_now

        if self.meta_old is not None:
            result['metaOld'] = self.meta_old

        if self.owner_id is not None:
            result['ownerId'] = self.owner_id

        if self.process is not None:
            result['process'] = self.process

        if self.record_diff is not None:
            result['recordDiff'] = self.record_diff

        if self.record_ids is not None:
            result['recordIds'] = self.record_ids

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.start_time is not None:
            result['startTime'] = self.start_time

        if self.state_type is not None:
            result['stateType'] = self.state_type

        result['statusInfo'] = []
        if self.status_info is not None:
            for k1 in self.status_info:
                result['statusInfo'].append(k1.to_map() if k1 else None)

        if self.user_id is not None:
            result['userId'] = self.user_id

        if self.user_info is not None:
            result['userInfo'] = self.user_info

        if self.user_type is not None:
            result['userType'] = self.user_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('actionName') is not None:
            self.action_name = m.get('actionName')

        if m.get('actionParams') is not None:
            self.action_params = m.get('actionParams')

        if m.get('actionResultAccessList') is not None:
            self.action_result_access_list = m.get('actionResultAccessList')

        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('metaNow') is not None:
            self.meta_now = m.get('metaNow')

        if m.get('metaOld') is not None:
            self.meta_old = m.get('metaOld')

        if m.get('ownerId') is not None:
            self.owner_id = m.get('ownerId')

        if m.get('process') is not None:
            self.process = m.get('process')

        if m.get('recordDiff') is not None:
            self.record_diff = m.get('recordDiff')

        if m.get('recordIds') is not None:
            self.record_ids = m.get('recordIds')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        if m.get('stateType') is not None:
            self.state_type = m.get('stateType')

        self.status_info = []
        if m.get('statusInfo') is not None:
            for k1 in m.get('statusInfo'):
                temp_model = main_models.ListActionRecordsResponseBodyResultStatusInfo()
                self.status_info.append(temp_model.from_map(k1))

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        if m.get('userInfo') is not None:
            self.user_info = m.get('userInfo')

        if m.get('userType') is not None:
            self.user_type = m.get('userType')

        return self

class ListActionRecordsResponseBodyResultStatusInfo(DaraModel):
    def __init__(
        self,
        complete_node_count: int = None,
        end_time: int = None,
        exception: str = None,
        latency_mills: int = None,
        node_count: int = None,
        process: str = None,
        start_time: int = None,
        state_type: str = None,
        sub_state: str = None,
        sub_status_info: List[main_models.ListActionRecordsResponseBodyResultStatusInfoSubStatusInfo] = None,
    ):
        self.complete_node_count = complete_node_count
        self.end_time = end_time
        self.exception = exception
        self.latency_mills = latency_mills
        self.node_count = node_count
        self.process = process
        self.start_time = start_time
        self.state_type = state_type
        self.sub_state = sub_state
        self.sub_status_info = sub_status_info

    def validate(self):
        if self.sub_status_info:
            for v1 in self.sub_status_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.complete_node_count is not None:
            result['completeNodeCount'] = self.complete_node_count

        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.exception is not None:
            result['exception'] = self.exception

        if self.latency_mills is not None:
            result['latencyMills'] = self.latency_mills

        if self.node_count is not None:
            result['nodeCount'] = self.node_count

        if self.process is not None:
            result['process'] = self.process

        if self.start_time is not None:
            result['startTime'] = self.start_time

        if self.state_type is not None:
            result['stateType'] = self.state_type

        if self.sub_state is not None:
            result['subState'] = self.sub_state

        result['subStatusInfo'] = []
        if self.sub_status_info is not None:
            for k1 in self.sub_status_info:
                result['subStatusInfo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('completeNodeCount') is not None:
            self.complete_node_count = m.get('completeNodeCount')

        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('exception') is not None:
            self.exception = m.get('exception')

        if m.get('latencyMills') is not None:
            self.latency_mills = m.get('latencyMills')

        if m.get('nodeCount') is not None:
            self.node_count = m.get('nodeCount')

        if m.get('process') is not None:
            self.process = m.get('process')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        if m.get('stateType') is not None:
            self.state_type = m.get('stateType')

        if m.get('subState') is not None:
            self.sub_state = m.get('subState')

        self.sub_status_info = []
        if m.get('subStatusInfo') is not None:
            for k1 in m.get('subStatusInfo'):
                temp_model = main_models.ListActionRecordsResponseBodyResultStatusInfoSubStatusInfo()
                self.sub_status_info.append(temp_model.from_map(k1))

        return self

class ListActionRecordsResponseBodyResultStatusInfoSubStatusInfo(DaraModel):
    def __init__(
        self,
        complete_node_count: int = None,
        end_time: int = None,
        exception: str = None,
        latency_mills: int = None,
        node_count: int = None,
        process: str = None,
        start_time: int = None,
        state_type: str = None,
        sub_state: str = None,
    ):
        self.complete_node_count = complete_node_count
        self.end_time = end_time
        self.exception = exception
        self.latency_mills = latency_mills
        self.node_count = node_count
        self.process = process
        self.start_time = start_time
        self.state_type = state_type
        self.sub_state = sub_state

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.complete_node_count is not None:
            result['completeNodeCount'] = self.complete_node_count

        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.exception is not None:
            result['exception'] = self.exception

        if self.latency_mills is not None:
            result['latencyMills'] = self.latency_mills

        if self.node_count is not None:
            result['nodeCount'] = self.node_count

        if self.process is not None:
            result['process'] = self.process

        if self.start_time is not None:
            result['startTime'] = self.start_time

        if self.state_type is not None:
            result['stateType'] = self.state_type

        if self.sub_state is not None:
            result['subState'] = self.sub_state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('completeNodeCount') is not None:
            self.complete_node_count = m.get('completeNodeCount')

        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('exception') is not None:
            self.exception = m.get('exception')

        if m.get('latencyMills') is not None:
            self.latency_mills = m.get('latencyMills')

        if m.get('nodeCount') is not None:
            self.node_count = m.get('nodeCount')

        if m.get('process') is not None:
            self.process = m.get('process')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        if m.get('stateType') is not None:
            self.state_type = m.get('stateType')

        if m.get('subState') is not None:
            self.sub_state = m.get('subState')

        return self

