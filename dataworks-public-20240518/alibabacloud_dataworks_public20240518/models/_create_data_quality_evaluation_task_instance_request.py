# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class CreateDataQualityEvaluationTaskInstanceRequest(DaraModel):
    def __init__(
        self,
        data_quality_evaluation_task_id: int = None,
        parameters: str = None,
        project_id: int = None,
        runtime_resource: main_models.CreateDataQualityEvaluationTaskInstanceRequestRuntimeResource = None,
    ):
        # The ID of the data quality monitoring task.
        # 
        # This parameter is required.
        self.data_quality_evaluation_task_id = data_quality_evaluation_task_id
        # Data quality verification execution parameters in JSON format. The available keys are as follows:
        # - triggerTime: the millisecond timestamp of the trigger time. The baseline time of the $[yyyymmdd] expression in the data range of data quality monitoring. Required.
        # 
        # This parameter is required.
        self.parameters = parameters
        # The ID of the DataWorks workspace. You can log on to the [DataWorks console](https://workbench.data.aliyun.com/console) and go to the workspace management page to obtain the ID.
        # 
        # This parameter is used to determine the DataWorks workspaces used for this API call.
        # 
        # This parameter is required.
        self.project_id = project_id
        # Resource Group information, which must be filled in when running non-MaxCompute data quality verification.
        self.runtime_resource = runtime_resource

    def validate(self):
        if self.runtime_resource:
            self.runtime_resource.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_quality_evaluation_task_id is not None:
            result['DataQualityEvaluationTaskId'] = self.data_quality_evaluation_task_id

        if self.parameters is not None:
            result['Parameters'] = self.parameters

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.runtime_resource is not None:
            result['RuntimeResource'] = self.runtime_resource.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataQualityEvaluationTaskId') is not None:
            self.data_quality_evaluation_task_id = m.get('DataQualityEvaluationTaskId')

        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('RuntimeResource') is not None:
            temp_model = main_models.CreateDataQualityEvaluationTaskInstanceRequestRuntimeResource()
            self.runtime_resource = temp_model.from_map(m.get('RuntimeResource'))

        return self

class CreateDataQualityEvaluationTaskInstanceRequestRuntimeResource(DaraModel):
    def __init__(
        self,
        cu: float = None,
        resource_group_id: str = None,
    ):
        # The task runs to configure CU consumption. If Serverless resource groups are used, you must specify this parameter.
        self.cu = cu
        # The identifier of the scheduling resource group configured for running the task.
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cu is not None:
            result['Cu'] = self.cu

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cu') is not None:
            self.cu = m.get('Cu')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        return self

