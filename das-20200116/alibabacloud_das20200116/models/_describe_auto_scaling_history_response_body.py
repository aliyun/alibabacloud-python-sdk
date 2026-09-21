# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_das20200116 import models as main_models
from darabonba.model import DaraModel

class DescribeAutoScalingHistoryResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.DescribeAutoScalingHistoryResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        # The status code. A value of 200 indicates success.
        self.code = code
        # The elastic scaling history records.
        self.data = data
        # The returned message.
        # > If the request is successful, **Successful** is returned. If the request fails, an error message such as an error code is returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # - **true**: The request was successful.
        # - **false**: The request failed.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.DescribeAutoScalingHistoryResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeAutoScalingHistoryResponseBodyData(DaraModel):
    def __init__(
        self,
        bandwidth: List[Dict[str, Any]] = None,
        instance_id: str = None,
        resource: List[Dict[str, Any]] = None,
        shard: List[Dict[str, Any]] = None,
        spec_history: List[main_models.DescribeAutoScalingHistoryResponseBodyDataSpecHistory] = None,
        storage: List[Dict[str, Any]] = None,
    ):
        # The Redis bandwidth elastic scaling history records. This parameter is not supported.
        self.bandwidth = bandwidth
        # The instance ID.
        self.instance_id = instance_id
        # The Redis resource scaling history records. This parameter is not supported.
        self.resource = resource
        # The Redis automatic shard scaling history records. This parameter is not supported.
        self.shard = shard
        # The automatic performance extension history records.
        self.spec_history = spec_history
        # The storage expansion history records. This parameter is not supported.
        self.storage = storage

    def validate(self):
        if self.spec_history:
            for v1 in self.spec_history:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.resource is not None:
            result['Resource'] = self.resource

        if self.shard is not None:
            result['Shard'] = self.shard

        result['SpecHistory'] = []
        if self.spec_history is not None:
            for k1 in self.spec_history:
                result['SpecHistory'].append(k1.to_map() if k1 else None)

        if self.storage is not None:
            result['Storage'] = self.storage

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Resource') is not None:
            self.resource = m.get('Resource')

        if m.get('Shard') is not None:
            self.shard = m.get('Shard')

        self.spec_history = []
        if m.get('SpecHistory') is not None:
            for k1 in m.get('SpecHistory'):
                temp_model = main_models.DescribeAutoScalingHistoryResponseBodyDataSpecHistory()
                self.spec_history.append(temp_model.from_map(k1))

        if m.get('Storage') is not None:
            self.storage = m.get('Storage')

        return self

class DescribeAutoScalingHistoryResponseBodyDataSpecHistory(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        origin_core: int = None,
        origin_instance_class: str = None,
        origin_memory: float = None,
        scale_type: str = None,
        target_core: int = None,
        target_instance_class: str = None,
        target_memory: float = None,
        task_excute_status: bool = None,
        task_time: int = None,
    ):
        # The error code returned by the internal scaling task. Valid values:
        # 
        # - **Insufficient_Balance**: The account balance is insufficient or there are unpaid orders.
        # - **REACH_SPEC_UPPERBOUND**: The upper limit of the instance specification has been reached.
        # - **Control_Error_Timeout_Msg**: The control task timed out.
        # - **Invoke_Rds_Api_Error_Msg**: Failed to call the RDS API.
        self.error_code = error_code
        # The number of CPU cores of the original instance.
        self.origin_core = origin_core
        # The original instance type.
        self.origin_instance_class = origin_instance_class
        # The memory size of the original instance. Unit: GB.
        self.origin_memory = origin_memory
        # The type of the automatic performance extension task. Valid values:
        # - **SCALE_UP**: Automatic specification extension.
        # - **SCALE_DOWN**: Automatic specification scale-down.
        self.scale_type = scale_type
        # The number of CPU cores of the target instance.
        self.target_core = target_core
        # The target instance type.
        self.target_instance_class = target_instance_class
        # The memory size of the target instance. Unit: GB.
        self.target_memory = target_memory
        # The task execution status. Valid values:
        # - **true**: The task was executed successfully.
        # - **false**: The task failed.
        self.task_excute_status = task_excute_status
        # The task execution time. The value is a UNIX timestamp. Unit: milliseconds.
        self.task_time = task_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.origin_core is not None:
            result['OriginCore'] = self.origin_core

        if self.origin_instance_class is not None:
            result['OriginInstanceClass'] = self.origin_instance_class

        if self.origin_memory is not None:
            result['OriginMemory'] = self.origin_memory

        if self.scale_type is not None:
            result['ScaleType'] = self.scale_type

        if self.target_core is not None:
            result['TargetCore'] = self.target_core

        if self.target_instance_class is not None:
            result['TargetInstanceClass'] = self.target_instance_class

        if self.target_memory is not None:
            result['TargetMemory'] = self.target_memory

        if self.task_excute_status is not None:
            result['TaskExcuteStatus'] = self.task_excute_status

        if self.task_time is not None:
            result['TaskTime'] = self.task_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('OriginCore') is not None:
            self.origin_core = m.get('OriginCore')

        if m.get('OriginInstanceClass') is not None:
            self.origin_instance_class = m.get('OriginInstanceClass')

        if m.get('OriginMemory') is not None:
            self.origin_memory = m.get('OriginMemory')

        if m.get('ScaleType') is not None:
            self.scale_type = m.get('ScaleType')

        if m.get('TargetCore') is not None:
            self.target_core = m.get('TargetCore')

        if m.get('TargetInstanceClass') is not None:
            self.target_instance_class = m.get('TargetInstanceClass')

        if m.get('TargetMemory') is not None:
            self.target_memory = m.get('TargetMemory')

        if m.get('TaskExcuteStatus') is not None:
            self.task_excute_status = m.get('TaskExcuteStatus')

        if m.get('TaskTime') is not None:
            self.task_time = m.get('TaskTime')

        return self

