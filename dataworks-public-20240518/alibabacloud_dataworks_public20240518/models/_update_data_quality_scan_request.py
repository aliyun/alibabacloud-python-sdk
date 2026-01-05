# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class UpdateDataQualityScanRequest(DaraModel):
    def __init__(
        self,
        compute_resource: main_models.UpdateDataQualityScanRequestComputeResource = None,
        description: str = None,
        hooks: List[main_models.UpdateDataQualityScanRequestHooks] = None,
        id: int = None,
        name: str = None,
        owner: str = None,
        parameters: List[main_models.UpdateDataQualityScanRequestParameters] = None,
        project_id: int = None,
        runtime_resource: main_models.UpdateDataQualityScanRequestRuntimeResource = None,
        spec: str = None,
        trigger: main_models.UpdateDataQualityScanRequestTrigger = None,
    ):
        # The compute engine used during execution. If it\\"s not specified, the data source connection defined in the Spec will be used.
        self.compute_resource = compute_resource
        # Description of the data quality monitor.
        self.description = description
        # The hook configuration after the data quality monitor stops.
        self.hooks = hooks
        # The ID of the data quality monitor.
        self.id = id
        # The name of the data quality monitor.
        self.name = name
        # The user ID of the owner of the data quality monitor.
        self.owner = owner
        # The definition of execution parameters for the data quality monitor.
        self.parameters = parameters
        # The ID of the DataWorks workspace where the data quality monitor resides. You can obtain the workspace ID by calling the [ListProjects](https://help.aliyun.com/document_detail/2852607.html) operation.
        self.project_id = project_id
        # The resource group used during the execution of the data quality monitor.
        self.runtime_resource = runtime_resource
        # The Spec code of the data quality monitoring content. For more information, see [Data quality Spec configuration description](https://help.aliyun.com/document_detail/2963394.html).
        self.spec = spec
        # Trigger settings for the data quality monitor.
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

        if self.description is not None:
            result['Description'] = self.description

        result['Hooks'] = []
        if self.hooks is not None:
            for k1 in self.hooks:
                result['Hooks'].append(k1.to_map() if k1 else None)

        if self.id is not None:
            result['Id'] = self.id

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
            temp_model = main_models.UpdateDataQualityScanRequestComputeResource()
            self.compute_resource = temp_model.from_map(m.get('ComputeResource'))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        self.hooks = []
        if m.get('Hooks') is not None:
            for k1 in m.get('Hooks'):
                temp_model = main_models.UpdateDataQualityScanRequestHooks()
                self.hooks.append(temp_model.from_map(k1))

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        self.parameters = []
        if m.get('Parameters') is not None:
            for k1 in m.get('Parameters'):
                temp_model = main_models.UpdateDataQualityScanRequestParameters()
                self.parameters.append(temp_model.from_map(k1))

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('RuntimeResource') is not None:
            temp_model = main_models.UpdateDataQualityScanRequestRuntimeResource()
            self.runtime_resource = temp_model.from_map(m.get('RuntimeResource'))

        if m.get('Spec') is not None:
            self.spec = m.get('Spec')

        if m.get('Trigger') is not None:
            temp_model = main_models.UpdateDataQualityScanRequestTrigger()
            self.trigger = temp_model.from_map(m.get('Trigger'))

        return self

class UpdateDataQualityScanRequestTrigger(DaraModel):
    def __init__(
        self,
        task_ids: List[int] = None,
        type: str = None,
    ):
        # If the trigger mode is BySchedule, the ID of the scheduling task that triggers the monitor must be configured.
        self.task_ids = task_ids
        # The trigger mode of the data quality monitor. Valid values:
        # 
        # *   ByManual: Manually triggered. Default setting.
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

class UpdateDataQualityScanRequestRuntimeResource(DaraModel):
    def __init__(
        self,
        cu: float = None,
        id: str = None,
        image: str = None,
    ):
        # The default number of CUs configured for task running.
        self.cu = cu
        # The ID of the resource group.
        self.id = id
        # The image ID of the task runtime configuration.
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

class UpdateDataQualityScanRequestParameters(DaraModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        # The parameter name.
        self.name = name
        # The parameter value.
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

class UpdateDataQualityScanRequestHooks(DaraModel):
    def __init__(
        self,
        condition: str = None,
        type: str = None,
    ):
        # The hook trigger condition. When this condition is met, the hook is triggered. Valid expression format:
        # 
        # Specifies multiple combinations of rule severity levels and rule validation statuses, such as `results.any { r -> r.status == \\"Fail\\" && r.rule.severity == \\"Normal\\" || r.status == \\"Error\\" && r.rule.severity == \\"High\\" || r.status == \\"Warn\\" && r.rule.severity == \\"High\\" }`. This means the hook is triggered if any executed rule has Fail with Normal severity, Error with High severity, or Warn with High severity. The severity values must match those defined in the Spec. The status values must match those in DataQualityResult.
        self.condition = condition
        # The type of the hook. Valid values:
        # 
        # *   BlockTaskInstance: Block the scheduling of the task instance.
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

class UpdateDataQualityScanRequestComputeResource(DaraModel):
    def __init__(
        self,
        env_type: str = None,
        name: str = None,
        runtime: main_models.UpdateDataQualityScanRequestComputeResourceRuntime = None,
    ):
        # Workspace environment of the compute engine. Valid values:
        # 
        # *   Prod
        # *   Dev
        self.env_type = env_type
        # The name of the compute engine, which is a unique identifier.
        self.name = name
        # Additional settings for the compute engine.
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
            temp_model = main_models.UpdateDataQualityScanRequestComputeResourceRuntime()
            self.runtime = temp_model.from_map(m.get('Runtime'))

        return self

class UpdateDataQualityScanRequestComputeResourceRuntime(DaraModel):
    def __init__(
        self,
        engine: str = None,
        hive_conf: Dict[str, Any] = None,
        spark_conf: Dict[str, Any] = None,
    ):
        # The engine type. These settings are only supported for the EMR compute engine.This setting? Valid values:
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

