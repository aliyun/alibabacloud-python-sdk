# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class CreateDataQualityScanRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        compute_resource: main_models.CreateDataQualityScanRequestComputeResource = None,
        description: str = None,
        hooks: List[main_models.CreateDataQualityScanRequestHooks] = None,
        name: str = None,
        owner: str = None,
        parameters: List[main_models.CreateDataQualityScanRequestParameters] = None,
        project_id: int = None,
        runtime_resource: main_models.CreateDataQualityScanRequestRuntimeResource = None,
        spec: str = None,
        trigger: main_models.CreateDataQualityScanRequestTrigger = None,
    ):
        # The idempotency token.
        # 
        # This parameter is required.
        self.client_token = client_token
        # The compute engine used when the data quality monitor runs. This parameter is optional. If it is not specified, the data source connection specified in the Spec is used.
        self.compute_resource = compute_resource
        # The description of the data quality monitor.
        self.description = description
        # The configuration for hooks that run after the data quality monitor finishes.
        self.hooks = hooks
        # The name of the data quality monitor.
        self.name = name
        # The user ID of the owner of the data quality monitor.
        self.owner = owner
        # The execution parameter definitions of the data quality monitor.
        self.parameters = parameters
        # The ID of the DataWorks workspace. You can log on to the [DataWorks console](https://dataworks.console.aliyun.com/overview) and go to the Workspace Management page to obtain the workspace ID. This parameter specifies the DataWorks workspace for the API call.
        self.project_id = project_id
        # The resource group used when the data quality monitor runs.
        self.runtime_resource = runtime_resource
        # The Spec code that defines the data quality monitor. For more information, see [Data quality spec configuration guide](https://help.aliyun.com/document_detail/2963394.html).
        self.spec = spec
        # The trigger settings of the data quality monitor.
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
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.compute_resource is not None:
            result['ComputeResource'] = self.compute_resource.to_map()

        if self.description is not None:
            result['Description'] = self.description

        result['Hooks'] = []
        if self.hooks is not None:
            for k1 in self.hooks:
                result['Hooks'].append(k1.to_map() if k1 else None)

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
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('ComputeResource') is not None:
            temp_model = main_models.CreateDataQualityScanRequestComputeResource()
            self.compute_resource = temp_model.from_map(m.get('ComputeResource'))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        self.hooks = []
        if m.get('Hooks') is not None:
            for k1 in m.get('Hooks'):
                temp_model = main_models.CreateDataQualityScanRequestHooks()
                self.hooks.append(temp_model.from_map(k1))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        self.parameters = []
        if m.get('Parameters') is not None:
            for k1 in m.get('Parameters'):
                temp_model = main_models.CreateDataQualityScanRequestParameters()
                self.parameters.append(temp_model.from_map(k1))

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('RuntimeResource') is not None:
            temp_model = main_models.CreateDataQualityScanRequestRuntimeResource()
            self.runtime_resource = temp_model.from_map(m.get('RuntimeResource'))

        if m.get('Spec') is not None:
            self.spec = m.get('Spec')

        if m.get('Trigger') is not None:
            temp_model = main_models.CreateDataQualityScanRequestTrigger()
            self.trigger = temp_model.from_map(m.get('Trigger'))

        return self

class CreateDataQualityScanRequestTrigger(DaraModel):
    def __init__(
        self,
        task_ids: List[int] = None,
        type: str = None,
    ):
        # The IDs of the scheduled tasks that trigger the data quality monitor when the trigger method is set to BySchedule.
        self.task_ids = task_ids
        # The trigger method of the data quality monitor. Valid values:
        # - ByManual: manual trigger. This is the default value.
        # - BySchedule: scheduled task instance trigger.
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

class CreateDataQualityScanRequestRuntimeResource(DaraModel):
    def __init__(
        self,
        cu: float = None,
        id: str = None,
        image: str = None,
    ):
        # The compute unit (CU) consumption of the runtime configuration.
        self.cu = cu
        # The ID of the resource group.
        self.id = id
        # The image ID of the runtime configuration.
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

class CreateDataQualityScanRequestParameters(DaraModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        # The name of the parameter.
        self.name = name
        # The value of the parameter.
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

class CreateDataQualityScanRequestHooks(DaraModel):
    def __init__(
        self,
        condition: str = None,
        type: str = None,
    ):
        # The condition that triggers the hook. When this condition is met, the hook is triggered. Currently, only one expression syntax is supported:
        # 
        # Specify multiple groups of rule severity levels and rule check statuses. For example, `results.any { r -> r.status == \\"Fail\\" && r.rule.severity == \\"Normal\\" || r.status == \\"Error\\" && r.rule.severity == \\"High\\" || r.status == \\"Warn\\" && r.rule.severity == \\"High\\" }` indicates that among the executed rules, if the check result of a rule with the severity of Normal is Fail, the check result of a rule with the severity of High is Error, or the check result of a rule with the severity of High is Warn, the condition is met. The enumerations of severity in the conditional expression are consistent with those in the spec, and the enumerations of status are consistent with those in DataQualityResult.
        self.condition = condition
        # The type of the hook. Valid values:
        # - BlockTaskInstance: blocks task instance scheduling.
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

class CreateDataQualityScanRequestComputeResource(DaraModel):
    def __init__(
        self,
        env_type: str = None,
        name: str = None,
        runtime: main_models.CreateDataQualityScanRequestComputeResourceRuntime = None,
    ):
        # The workspace environment to which the compute engine belongs. Valid values:
        # - Prod: production environment
        # - Dev: development environment
        self.env_type = env_type
        # The name of the compute engine, which serves as a unique identifier.
        self.name = name
        # The additional settings for the data quality monitor at runtime.
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
            temp_model = main_models.CreateDataQualityScanRequestComputeResourceRuntime()
            self.runtime = temp_model.from_map(m.get('Runtime'))

        return self

class CreateDataQualityScanRequestComputeResourceRuntime(DaraModel):
    def __init__(
        self,
        engine: str = None,
        hive_conf: Dict[str, Any] = None,
        spark_conf: Dict[str, Any] = None,
    ):
        # The type of the engine used. Only the E-MapReduce (EMR) compute engine supports this setting. Valid values:
        # - Hive: Hive SQL
        # - Spark: Spark SQL
        # - Kyuubi
        self.engine = engine
        # The additional parameter settings when the Hive engine is used. Currently, only the queue can be set by using mapreduce.job.queuename.
        self.hive_conf = hive_conf
        # The additional parameter settings when the Spark engine is used. Currently, only the queue can be set by using spark.yarn.queue.
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

