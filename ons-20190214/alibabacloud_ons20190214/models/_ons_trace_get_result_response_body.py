# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ons20190214 import models as main_models
from darabonba.model import DaraModel

class OnsTraceGetResultResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        trace_data: main_models.OnsTraceGetResultResponseBodyTraceData = None,
    ):
        # The ID of the request. This parameter is a common parameter. Each request has a unique ID. You can use this ID to troubleshoot issues.
        self.request_id = request_id
        # The details of the message trace.
        self.trace_data = trace_data

    def validate(self):
        if self.trace_data:
            self.trace_data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.trace_data is not None:
            result['TraceData'] = self.trace_data.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TraceData') is not None:
            temp_model = main_models.OnsTraceGetResultResponseBodyTraceData()
            self.trace_data = temp_model.from_map(m.get('TraceData'))

        return self

class OnsTraceGetResultResponseBodyTraceData(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        instance_id: str = None,
        msg_id: str = None,
        msg_key: str = None,
        query_id: str = None,
        status: str = None,
        topic: str = None,
        trace_list: main_models.OnsTraceGetResultResponseBodyTraceDataTraceList = None,
        update_time: int = None,
        user_id: str = None,
    ):
        # The point in time when the task was created.
        self.create_time = create_time
        # The ID of the instance
        self.instance_id = instance_id
        # The ID of the message that is queried.
        self.msg_id = msg_id
        # The key of the message that is queried.
        self.msg_key = msg_key
        # The ID of the task.
        self.query_id = query_id
        # The status of the task. Valid values:
        # 
        # *   **finish**: The task is complete.
        # *   **working**: The task is in progress.
        # *   **removed**: The task is deleted.
        self.status = status
        # The topic in which the message is stored.
        self.topic = topic
        self.trace_list = trace_list
        # The most recent point in time when the task was updated.
        self.update_time = update_time
        # The ID of the user who created the task.
        self.user_id = user_id

    def validate(self):
        if self.trace_list:
            self.trace_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.msg_id is not None:
            result['MsgId'] = self.msg_id

        if self.msg_key is not None:
            result['MsgKey'] = self.msg_key

        if self.query_id is not None:
            result['QueryId'] = self.query_id

        if self.status is not None:
            result['Status'] = self.status

        if self.topic is not None:
            result['Topic'] = self.topic

        if self.trace_list is not None:
            result['TraceList'] = self.trace_list.to_map()

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('MsgId') is not None:
            self.msg_id = m.get('MsgId')

        if m.get('MsgKey') is not None:
            self.msg_key = m.get('MsgKey')

        if m.get('QueryId') is not None:
            self.query_id = m.get('QueryId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Topic') is not None:
            self.topic = m.get('Topic')

        if m.get('TraceList') is not None:
            temp_model = main_models.OnsTraceGetResultResponseBodyTraceDataTraceList()
            self.trace_list = temp_model.from_map(m.get('TraceList'))

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

class OnsTraceGetResultResponseBodyTraceDataTraceList(DaraModel):
    def __init__(
        self,
        trace_map_do: List[main_models.OnsTraceGetResultResponseBodyTraceDataTraceListTraceMapDo] = None,
    ):
        self.trace_map_do = trace_map_do

    def validate(self):
        if self.trace_map_do:
            for v1 in self.trace_map_do:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['TraceMapDo'] = []
        if self.trace_map_do is not None:
            for k1 in self.trace_map_do:
                result['TraceMapDo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.trace_map_do = []
        if m.get('TraceMapDo') is not None:
            for k1 in m.get('TraceMapDo'):
                temp_model = main_models.OnsTraceGetResultResponseBodyTraceDataTraceListTraceMapDo()
                self.trace_map_do.append(temp_model.from_map(k1))

        return self

class OnsTraceGetResultResponseBodyTraceDataTraceListTraceMapDo(DaraModel):
    def __init__(
        self,
        born_host: str = None,
        cost_time: int = None,
        msg_id: str = None,
        msg_key: str = None,
        pub_group_name: str = None,
        pub_time: int = None,
        status: str = None,
        sub_list: main_models.OnsTraceGetResultResponseBodyTraceDataTraceListTraceMapDoSubList = None,
        tag: str = None,
        topic: str = None,
    ):
        self.born_host = born_host
        self.cost_time = cost_time
        self.msg_id = msg_id
        self.msg_key = msg_key
        self.pub_group_name = pub_group_name
        self.pub_time = pub_time
        self.status = status
        self.sub_list = sub_list
        self.tag = tag
        self.topic = topic

    def validate(self):
        if self.sub_list:
            self.sub_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.born_host is not None:
            result['BornHost'] = self.born_host

        if self.cost_time is not None:
            result['CostTime'] = self.cost_time

        if self.msg_id is not None:
            result['MsgId'] = self.msg_id

        if self.msg_key is not None:
            result['MsgKey'] = self.msg_key

        if self.pub_group_name is not None:
            result['PubGroupName'] = self.pub_group_name

        if self.pub_time is not None:
            result['PubTime'] = self.pub_time

        if self.status is not None:
            result['Status'] = self.status

        if self.sub_list is not None:
            result['SubList'] = self.sub_list.to_map()

        if self.tag is not None:
            result['Tag'] = self.tag

        if self.topic is not None:
            result['Topic'] = self.topic

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BornHost') is not None:
            self.born_host = m.get('BornHost')

        if m.get('CostTime') is not None:
            self.cost_time = m.get('CostTime')

        if m.get('MsgId') is not None:
            self.msg_id = m.get('MsgId')

        if m.get('MsgKey') is not None:
            self.msg_key = m.get('MsgKey')

        if m.get('PubGroupName') is not None:
            self.pub_group_name = m.get('PubGroupName')

        if m.get('PubTime') is not None:
            self.pub_time = m.get('PubTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SubList') is not None:
            temp_model = main_models.OnsTraceGetResultResponseBodyTraceDataTraceListTraceMapDoSubList()
            self.sub_list = temp_model.from_map(m.get('SubList'))

        if m.get('Tag') is not None:
            self.tag = m.get('Tag')

        if m.get('Topic') is not None:
            self.topic = m.get('Topic')

        return self

class OnsTraceGetResultResponseBodyTraceDataTraceListTraceMapDoSubList(DaraModel):
    def __init__(
        self,
        sub_map_do: List[main_models.OnsTraceGetResultResponseBodyTraceDataTraceListTraceMapDoSubListSubMapDo] = None,
    ):
        self.sub_map_do = sub_map_do

    def validate(self):
        if self.sub_map_do:
            for v1 in self.sub_map_do:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SubMapDo'] = []
        if self.sub_map_do is not None:
            for k1 in self.sub_map_do:
                result['SubMapDo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.sub_map_do = []
        if m.get('SubMapDo') is not None:
            for k1 in m.get('SubMapDo'):
                temp_model = main_models.OnsTraceGetResultResponseBodyTraceDataTraceListTraceMapDoSubListSubMapDo()
                self.sub_map_do.append(temp_model.from_map(k1))

        return self

class OnsTraceGetResultResponseBodyTraceDataTraceListTraceMapDoSubListSubMapDo(DaraModel):
    def __init__(
        self,
        client_list: main_models.OnsTraceGetResultResponseBodyTraceDataTraceListTraceMapDoSubListSubMapDoClientList = None,
        fail_count: int = None,
        sub_group_name: str = None,
        success_count: int = None,
    ):
        self.client_list = client_list
        self.fail_count = fail_count
        self.sub_group_name = sub_group_name
        self.success_count = success_count

    def validate(self):
        if self.client_list:
            self.client_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_list is not None:
            result['ClientList'] = self.client_list.to_map()

        if self.fail_count is not None:
            result['FailCount'] = self.fail_count

        if self.sub_group_name is not None:
            result['SubGroupName'] = self.sub_group_name

        if self.success_count is not None:
            result['SuccessCount'] = self.success_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientList') is not None:
            temp_model = main_models.OnsTraceGetResultResponseBodyTraceDataTraceListTraceMapDoSubListSubMapDoClientList()
            self.client_list = temp_model.from_map(m.get('ClientList'))

        if m.get('FailCount') is not None:
            self.fail_count = m.get('FailCount')

        if m.get('SubGroupName') is not None:
            self.sub_group_name = m.get('SubGroupName')

        if m.get('SuccessCount') is not None:
            self.success_count = m.get('SuccessCount')

        return self

class OnsTraceGetResultResponseBodyTraceDataTraceListTraceMapDoSubListSubMapDoClientList(DaraModel):
    def __init__(
        self,
        sub_client_info_do: List[main_models.OnsTraceGetResultResponseBodyTraceDataTraceListTraceMapDoSubListSubMapDoClientListSubClientInfoDo] = None,
    ):
        self.sub_client_info_do = sub_client_info_do

    def validate(self):
        if self.sub_client_info_do:
            for v1 in self.sub_client_info_do:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SubClientInfoDo'] = []
        if self.sub_client_info_do is not None:
            for k1 in self.sub_client_info_do:
                result['SubClientInfoDo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.sub_client_info_do = []
        if m.get('SubClientInfoDo') is not None:
            for k1 in m.get('SubClientInfoDo'):
                temp_model = main_models.OnsTraceGetResultResponseBodyTraceDataTraceListTraceMapDoSubListSubMapDoClientListSubClientInfoDo()
                self.sub_client_info_do.append(temp_model.from_map(k1))

        return self

class OnsTraceGetResultResponseBodyTraceDataTraceListTraceMapDoSubListSubMapDoClientListSubClientInfoDo(DaraModel):
    def __init__(
        self,
        client_host: str = None,
        cost_time: int = None,
        reconsume_times: int = None,
        status: str = None,
        sub_group_name: str = None,
        sub_time: int = None,
    ):
        self.client_host = client_host
        self.cost_time = cost_time
        self.reconsume_times = reconsume_times
        self.status = status
        self.sub_group_name = sub_group_name
        self.sub_time = sub_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_host is not None:
            result['ClientHost'] = self.client_host

        if self.cost_time is not None:
            result['CostTime'] = self.cost_time

        if self.reconsume_times is not None:
            result['ReconsumeTimes'] = self.reconsume_times

        if self.status is not None:
            result['Status'] = self.status

        if self.sub_group_name is not None:
            result['SubGroupName'] = self.sub_group_name

        if self.sub_time is not None:
            result['SubTime'] = self.sub_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientHost') is not None:
            self.client_host = m.get('ClientHost')

        if m.get('CostTime') is not None:
            self.cost_time = m.get('CostTime')

        if m.get('ReconsumeTimes') is not None:
            self.reconsume_times = m.get('ReconsumeTimes')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SubGroupName') is not None:
            self.sub_group_name = m.get('SubGroupName')

        if m.get('SubTime') is not None:
            self.sub_time = m.get('SubTime')

        return self

