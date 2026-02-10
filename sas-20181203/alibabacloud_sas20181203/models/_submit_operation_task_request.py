# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class SubmitOperationTaskRequest(DaraModel):
    def __init__(
        self,
        check_id: int = None,
        dimension_type: str = None,
        operation_task_instances: List[main_models.SubmitOperationTaskRequestOperationTaskInstances] = None,
        relation_key: str = None,
        repair_temp_param: List[main_models.SubmitOperationTaskRequestRepairTempParam] = None,
        type: str = None,
    ):
        # The ID of the check item.
        # 
        # >  You can call the [ListCheckResult](~~ListCheckResult~~) operation to obtain the ID of the check item.
        # 
        # This parameter is required.
        self.check_id = check_id
        # The dimension of the task that you want to submit. Valid values:
        # 
        # *   Instance dimension: INSTANCE
        # *   Check item dimension: CHECK_ID
        self.dimension_type = dimension_type
        # The asset information required to submit the tasks for instances.
        self.operation_task_instances = operation_task_instances
        # The key linked to cross-page selections during task submission.
        # 
        # >  You can call the [CreateAssetSelectionConfig](~~CreateAssetSelectionConfig~~) operation to query the associated key from the BusinessType field.
        self.relation_key = relation_key
        # The temporary parameters required for the repair task.
        self.repair_temp_param = repair_temp_param
        # The type of the task that you want to submit. Valid values:
        # 
        # *   Repair task: REPAIR
        # *   Rollback task: ROLLBACK
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        if self.operation_task_instances:
            for v1 in self.operation_task_instances:
                 if v1:
                    v1.validate()
        if self.repair_temp_param:
            for v1 in self.repair_temp_param:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_id is not None:
            result['CheckId'] = self.check_id

        if self.dimension_type is not None:
            result['DimensionType'] = self.dimension_type

        result['OperationTaskInstances'] = []
        if self.operation_task_instances is not None:
            for k1 in self.operation_task_instances:
                result['OperationTaskInstances'].append(k1.to_map() if k1 else None)

        if self.relation_key is not None:
            result['RelationKey'] = self.relation_key

        result['RepairTempParam'] = []
        if self.repair_temp_param is not None:
            for k1 in self.repair_temp_param:
                result['RepairTempParam'].append(k1.to_map() if k1 else None)

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckId') is not None:
            self.check_id = m.get('CheckId')

        if m.get('DimensionType') is not None:
            self.dimension_type = m.get('DimensionType')

        self.operation_task_instances = []
        if m.get('OperationTaskInstances') is not None:
            for k1 in m.get('OperationTaskInstances'):
                temp_model = main_models.SubmitOperationTaskRequestOperationTaskInstances()
                self.operation_task_instances.append(temp_model.from_map(k1))

        if m.get('RelationKey') is not None:
            self.relation_key = m.get('RelationKey')

        self.repair_temp_param = []
        if m.get('RepairTempParam') is not None:
            for k1 in m.get('RepairTempParam'):
                temp_model = main_models.SubmitOperationTaskRequestRepairTempParam()
                self.repair_temp_param.append(temp_model.from_map(k1))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class SubmitOperationTaskRequestRepairTempParam(DaraModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        # The name of the temporary repair parameter.
        self.name = name
        # The value of the temporary repair parameter.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class SubmitOperationTaskRequestOperationTaskInstances(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        region_id: str = None,
        task_id: str = None,
        vendor: str = None,
    ):
        # The instance ID of the server.
        self.instance_id = instance_id
        # The region ID of the server.
        self.region_id = region_id
        # The ID of the task that you want to roll back
        self.task_id = task_id
        # The service provider of the asset. Valid values:
        # 
        # *   **0**: an asset provided by Alibaba Cloud.
        # *   **1**: an asset outside Alibaba Cloud.
        # *   **2**: an asset in a data center.
        # *   **3**, **4**, **5**, and **7**: an asset from a third-party cloud service provider.
        # *   **8**: a lightweight asset.
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

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.vendor is not None:
            result['Vendor'] = self.vendor

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')

        return self

