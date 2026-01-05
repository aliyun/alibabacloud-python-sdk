# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class GetDataQualityScanResponseBody(DaraModel):
    def __init__(
        self,
        data_quality_scan: main_models.GetDataQualityScanResponseBodyDataQualityScan = None,
        request_id: str = None,
    ):
        # Data quality monitoring details.
        self.data_quality_scan = data_quality_scan
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.data_quality_scan:
            self.data_quality_scan.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_quality_scan is not None:
            result['DataQualityScan'] = self.data_quality_scan.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataQualityScan') is not None:
            temp_model = main_models.GetDataQualityScanResponseBodyDataQualityScan()
            self.data_quality_scan = temp_model.from_map(m.get('DataQualityScan'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetDataQualityScanResponseBodyDataQualityScan(DaraModel):
    def __init__(
        self,
        compute_resource: main_models.GetDataQualityScanResponseBodyDataQualityScanComputeResource = None,
        create_time: int = None,
        create_user: str = None,
        description: str = None,
        hooks: List[main_models.GetDataQualityScanResponseBodyDataQualityScanHooks] = None,
        id: int = None,
        modify_time: int = None,
        modify_user: str = None,
        name: str = None,
        owner: str = None,
        parameters: List[main_models.GetDataQualityScanResponseBodyDataQualityScanParameters] = None,
        project_id: int = None,
        runtime_resource: main_models.GetDataQualityScanResponseBodyDataQualityScanRuntimeResource = None,
        spec: str = None,
        trigger: main_models.GetDataQualityScanResponseBodyDataQualityScanTrigger = None,
    ):
        # The compute engine used at runtime. Optional. If not specified, the data source defined in the Spec is used.
        self.compute_resource = compute_resource
        # The creation time of the data quality monitor.
        self.create_time = create_time
        # The ID of the user who creates the data quality monitor.
        self.create_user = create_user
        # The data quality monitor description.
        self.description = description
        # The Hook configurations after the data quality monitoring run ends.
        self.hooks = hooks
        # The data quality monitoring ID.
        self.id = id
        # Last modified time of the data quality monitor.
        self.modify_time = modify_time
        # The ID of the user who last modifies the data quality monitor.
        self.modify_user = modify_user
        # The data quality monitor name.
        self.name = name
        # The ID of the user who owns the data quality monitor.
        self.owner = owner
        # The definition of execution parameters for the data quality monitor.
        self.parameters = parameters
        # The workspace ID where the data quality monitor resides. You can obtain the workspace ID by calling the [ListProjects](https://help.aliyun.com/document_detail/2780068.html) operation.
        self.project_id = project_id
        # The resource group used during the running of the data quality monitor.
        self.runtime_resource = runtime_resource
        # Spec code for the content of the data quality monitoring.
        self.spec = spec
        # The trigger configurations of the data quality monitoring task.
        self.trigger = trigger

    def validate(self):
        if self.compute_resource:
            self.compute_resource.validate()
        if self.hooks:
            for v1 in self.hooks:
                 if v1:
                    v1.validate()
        if self.parameters:
            for v1 in self.parameters:
                 if v1:
                    v1.validate()
        if self.runtime_resource:
            self.runtime_resource.validate()
        if self.trigger:
            self.trigger.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.compute_resource is not None:
            result['ComputeResource'] = self.compute_resource.to_map()

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.create_user is not None:
            result['CreateUser'] = self.create_user

        if self.description is not None:
            result['Description'] = self.description

        result['Hooks'] = []
        if self.hooks is not None:
            for k1 in self.hooks:
                result['Hooks'].append(k1.to_map() if k1 else None)

        if self.id is not None:
            result['Id'] = self.id

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.modify_user is not None:
            result['ModifyUser'] = self.modify_user

        if self.name is not None:
            result['Name'] = self.name

        if self.owner is not None:
            result['Owner'] = self.owner

        result['Parameters'] = []
        if self.parameters is not None:
            for k1 in self.parameters:
                result['Parameters'].append(k1.to_map() if k1 else None)

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.runtime_resource is not None:
            result['RuntimeResource'] = self.runtime_resource.to_map()

        if self.spec is not None:
            result['Spec'] = self.spec

        if self.trigger is not None:
            result['Trigger'] = self.trigger.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComputeResource') is not None:
            temp_model = main_models.GetDataQualityScanResponseBodyDataQualityScanComputeResource()
            self.compute_resource = temp_model.from_map(m.get('ComputeResource'))

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CreateUser') is not None:
            self.create_user = m.get('CreateUser')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        self.hooks = []
        if m.get('Hooks') is not None:
            for k1 in m.get('Hooks'):
                temp_model = main_models.GetDataQualityScanResponseBodyDataQualityScanHooks()
                self.hooks.append(temp_model.from_map(k1))

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('ModifyUser') is not None:
            self.modify_user = m.get('ModifyUser')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        self.parameters = []
        if m.get('Parameters') is not None:
            for k1 in m.get('Parameters'):
                temp_model = main_models.GetDataQualityScanResponseBodyDataQualityScanParameters()
                self.parameters.append(temp_model.from_map(k1))

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('RuntimeResource') is not None:
            temp_model = main_models.GetDataQualityScanResponseBodyDataQualityScanRuntimeResource()
            self.runtime_resource = temp_model.from_map(m.get('RuntimeResource'))

        if m.get('Spec') is not None:
            self.spec = m.get('Spec')

        if m.get('Trigger') is not None:
            temp_model = main_models.GetDataQualityScanResponseBodyDataQualityScanTrigger()
            self.trigger = temp_model.from_map(m.get('Trigger'))

        return self

class GetDataQualityScanResponseBodyDataQualityScanTrigger(DaraModel):
    def __init__(
        self,
        task_ids: List[int] = None,
        type: str = None,
    ):
        # If the trigger mode is set to BySchedule, the scheduling task ID must be specified.
        self.task_ids = task_ids
        # The trigger mode of the monitoring task.
        # 
        # Valid values:
        # 
        # *   ByManual: Manual trigger. This is the default setting.
        # *   BySchedule: Triggered by a scheduled task instance.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.task_ids is not None:
            result['TaskIds'] = self.task_ids

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskIds') is not None:
            self.task_ids = m.get('TaskIds')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class GetDataQualityScanResponseBodyDataQualityScanRuntimeResource(DaraModel):
    def __init__(
        self,
        cu: float = None,
        id: str = None,
        image: str = None,
    ):
        # Reserved compute units (CU) for the resource group.
        self.cu = cu
        # The resource group ID.
        self.id = id
        # The image ID used in the runtime configuration.
        self.image = image

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cu is not None:
            result['Cu'] = self.cu

        if self.id is not None:
            result['Id'] = self.id

        if self.image is not None:
            result['Image'] = self.image

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cu') is not None:
            self.cu = m.get('Cu')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Image') is not None:
            self.image = m.get('Image')

        return self

class GetDataQualityScanResponseBodyDataQualityScanParameters(DaraModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        # The parameter value.
        self.name = name
        # The parameter name.
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

class GetDataQualityScanResponseBodyDataQualityScanHooks(DaraModel):
    def __init__(
        self,
        condition: str = None,
        type: str = None,
    ):
        # The Hook trigger condition. The hook will run if the condition is met. Currently, only one type of expression syntax is supported:
        # 
        # *   You can specify multiple combinations of rule severity levels and validation statuses using an expression such as `results.any { r -> r.status == \\"Fail\\" && r.rule.severity == \\"Normal\\" || r.status == \\"Error\\" && r.rule.severity == \\"High\\" || r.status == \\"Warn\\" && r.rule.severity == \\"High\\" }`. This expression means the condition is met if any executed rule has a result of Fail with severity Normal, Error with severity High, or Warn with severity High. In the condition expression, the values of severity and status are predefined enums. The values of severity must match those defined in the Spec, and the values of status must match those in DataQualityResult.
        self.condition = condition
        # The type of the Hook.
        # 
        # Valid values:
        # 
        # *   BlockTaskInstance: BlockTaskInstance: Blocks the scheduling of the task instance.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.condition is not None:
            result['Condition'] = self.condition

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Condition') is not None:
            self.condition = m.get('Condition')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class GetDataQualityScanResponseBodyDataQualityScanComputeResource(DaraModel):
    def __init__(
        self,
        env_type: str = None,
        name: str = None,
        runtime: main_models.GetDataQualityScanResponseBodyDataQualityScanComputeResourceRuntime = None,
    ):
        # The workspace environment to which the compute engine belongs.
        # 
        # Valid values:
        # 
        # *   Prod: production environment .
        # *   Dev: development environment.
        self.env_type = env_type
        # The name of the compute engine, which is a unique identifier.
        self.name = name
        # More settings for data quality monitor at runtime.
        self.runtime = runtime

    def validate(self):
        if self.runtime:
            self.runtime.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.env_type is not None:
            result['EnvType'] = self.env_type

        if self.name is not None:
            result['Name'] = self.name

        if self.runtime is not None:
            result['Runtime'] = self.runtime.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Runtime') is not None:
            temp_model = main_models.GetDataQualityScanResponseBodyDataQualityScanComputeResourceRuntime()
            self.runtime = temp_model.from_map(m.get('Runtime'))

        return self

class GetDataQualityScanResponseBodyDataQualityScanComputeResourceRuntime(DaraModel):
    def __init__(
        self,
        engine: str = None,
        hive_conf: Dict[str, Any] = None,
        spark_conf: Dict[str, Any] = None,
    ):
        # The type of the compute engine. Only EMR compute engines support these settings.
        # 
        # Valid values:
        # 
        # *   Hive: Hive SQL
        # *   Spark: Spark SQL
        # *   Kyuubi
        self.engine = engine
        # Additional Hive engine parameters. Currently, only the mapreduce.job.queuename parameter is supported.
        self.hive_conf = hive_conf
        # Additional Spark engine parameters. Currently, only the spark.yarn.queue parameter is supported.
        self.spark_conf = spark_conf

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.engine is not None:
            result['Engine'] = self.engine

        if self.hive_conf is not None:
            result['HiveConf'] = self.hive_conf

        if self.spark_conf is not None:
            result['SparkConf'] = self.spark_conf

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('HiveConf') is not None:
            self.hive_conf = m.get('HiveConf')

        if m.get('SparkConf') is not None:
            self.spark_conf = m.get('SparkConf')

        return self

