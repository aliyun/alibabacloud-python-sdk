# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class ListOperationCheckRequest(DaraModel):
    def __init__(
        self,
        check_id: int = None,
        end_time: int = None,
        lang: str = None,
        operation_task_instances: List[main_models.ListOperationCheckRequestOperationTaskInstances] = None,
        start_time: int = None,
        type: str = None,
    ):
        # The check item ID.
        # > Call the [ListCheckResult](~~ListCheckResult~~) operation to obtain this parameter.
        # This parameter is required. If you do not specify this parameter, the API returns a 400 error.
        self.check_id = check_id
        # The timestamp of the task end time to query. Unit: milliseconds.
        self.end_time = end_time
        # The language of the request and response. Default value: zh. Valid values:
        # - **zh**: Chinese
        # - **en**: English
        self.lang = lang
        # The information about the instances on which the operation is performed.
        # 
        # This parameter is required.
        self.operation_task_instances = operation_task_instances
        # The timestamp of the task start time to query. Unit: milliseconds.
        self.start_time = start_time
        # The task type. Valid values:
        # - **REPAIR**: fix task
        # - **ROLLBACK**: rollback task
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        if self.operation_task_instances:
            for v1 in self.operation_task_instances:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_id is not None:
            result['CheckId'] = self.check_id

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.lang is not None:
            result['Lang'] = self.lang

        result['OperationTaskInstances'] = []
        if self.operation_task_instances is not None:
            for k1 in self.operation_task_instances:
                result['OperationTaskInstances'].append(k1.to_map() if k1 else None)

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckId') is not None:
            self.check_id = m.get('CheckId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        self.operation_task_instances = []
        if m.get('OperationTaskInstances') is not None:
            for k1 in m.get('OperationTaskInstances'):
                temp_model = main_models.ListOperationCheckRequestOperationTaskInstances()
                self.operation_task_instances.append(temp_model.from_map(k1))

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class ListOperationCheckRequestOperationTaskInstances(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        region_id: str = None,
        vendor: str = None,
    ):
        # The cloud asset instance ID.
        self.instance_id = instance_id
        # The region ID.
        self.region_id = region_id
        # The asset vendor. Valid values:
        # 
        # - **ALIYUN**: Alibaba Cloud
        self.vendor = vendor

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.vendor is not None:
            result['Vendor'] = self.vendor

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')

        return self

