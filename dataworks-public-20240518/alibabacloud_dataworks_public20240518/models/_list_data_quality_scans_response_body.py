# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class ListDataQualityScansResponseBody(DaraModel):
    def __init__(
        self,
        page_info: main_models.ListDataQualityScansResponseBodyPageInfo = None,
        request_id: str = None,
    ):
        # The page information.
        self.page_info = page_info
        # The API request ID, which is generated as a UUID.
        self.request_id = request_id

    def validate(self):
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageInfo') is not None:
            temp_model = main_models.ListDataQualityScansResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListDataQualityScansResponseBodyPageInfo(DaraModel):
    def __init__(
        self,
        data_quality_scans: List[main_models.ListDataQualityScansResponseBodyPageInfoDataQualityScans] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The list of data quality monitors.
        self.data_quality_scans = data_quality_scans
        # The page number.
        self.page_number = page_number
        # The number of records per page. Default value: 10.
        self.page_size = page_size
        # The total number of records returned.
        self.total_count = total_count

    def validate(self):
        if self.data_quality_scans:
            for v1 in self.data_quality_scans:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DataQualityScans'] = []
        if self.data_quality_scans is not None:
            for k1 in self.data_quality_scans:
                result['DataQualityScans'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_quality_scans = []
        if m.get('DataQualityScans') is not None:
            for k1 in m.get('DataQualityScans'):
                temp_model = main_models.ListDataQualityScansResponseBodyPageInfoDataQualityScans()
                self.data_quality_scans.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListDataQualityScansResponseBodyPageInfoDataQualityScans(DaraModel):
    def __init__(
        self,
        compute_resource: main_models.ListDataQualityScansResponseBodyPageInfoDataQualityScansComputeResource = None,
        create_time: int = None,
        create_user: str = None,
        description: str = None,
        hooks: List[main_models.ListDataQualityScansResponseBodyPageInfoDataQualityScansHooks] = None,
        id: int = None,
        modify_time: int = None,
        modify_user: str = None,
        name: str = None,
        owner: str = None,
        parameters: List[main_models.ListDataQualityScansResponseBodyPageInfoDataQualityScansParameters] = None,
        project_id: int = None,
        runtime_resource: main_models.ListDataQualityScansResponseBodyPageInfoDataQualityScansRuntimeResource = None,
        trigger: main_models.ListDataQualityScansResponseBodyPageInfoDataQualityScansTrigger = None,
    ):
        # The compute engine used during execution. If it is not specified, the data source connection defined in the Spec will be used.
        self.compute_resource = compute_resource
        # The creation time of the data quality monitor.
        self.create_time = create_time
        # The creator of the data quality monitor.
        self.create_user = create_user
        # The description of the data quality scan task. Maximum length: 65,535 characters.
        self.description = description
        # The hook configuration after the data quality monitor stops.
        self.hooks = hooks
        # The ID of the data quality monitor.
        self.id = id
        # Last update time of the data quality monitor.
        self.modify_time = modify_time
        # The user ID of the last person who updated the data quality monitor.
        self.modify_user = modify_user
        # The name of the data quality scan task. Can include digits, letters, Chinese characters, and both half-width and full-width punctuation marks. Maximum length: 255 characters.
        self.name = name
        # The user ID of the owner responsible for the data quality monitor.
        self.owner = owner
        # Execution parameter definitions for the data quality monitor.
        self.parameters = parameters
        # The project ID.
        self.project_id = project_id
        # The resource group used during the execution of the data quality monitor.
        self.runtime_resource = runtime_resource
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

        if self.trigger is not None:
            result['Trigger'] = self.trigger.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComputeResource') is not None:
            temp_model = main_models.ListDataQualityScansResponseBodyPageInfoDataQualityScansComputeResource()
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
                temp_model = main_models.ListDataQualityScansResponseBodyPageInfoDataQualityScansHooks()
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
                temp_model = main_models.ListDataQualityScansResponseBodyPageInfoDataQualityScansParameters()
                self.parameters.append(temp_model.from_map(k1))

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('RuntimeResource') is not None:
            temp_model = main_models.ListDataQualityScansResponseBodyPageInfoDataQualityScansRuntimeResource()
            self.runtime_resource = temp_model.from_map(m.get('RuntimeResource'))

        if m.get('Trigger') is not None:
            temp_model = main_models.ListDataQualityScansResponseBodyPageInfoDataQualityScansTrigger()
            self.trigger = temp_model.from_map(m.get('Trigger'))

        return self

class ListDataQualityScansResponseBodyPageInfoDataQualityScansTrigger(DaraModel):
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

class ListDataQualityScansResponseBodyPageInfoDataQualityScansRuntimeResource(DaraModel):
    def __init__(
        self,
        cu: float = None,
        id: str = None,
        image: str = None,
    ):
        # CU consumption for task running.
        self.cu = cu
        # The ID of the resource group.
        self.id = id
        # The ID of the image configured for task running.
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

class ListDataQualityScansResponseBodyPageInfoDataQualityScansParameters(DaraModel):
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

class ListDataQualityScansResponseBodyPageInfoDataQualityScansHooks(DaraModel):
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
        # *   BlockTaskInstance: Blocks the scheduling of the task instance.
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

class ListDataQualityScansResponseBodyPageInfoDataQualityScansComputeResource(DaraModel):
    def __init__(
        self,
        env_type: str = None,
        name: str = None,
        runtime: main_models.ListDataQualityScansResponseBodyPageInfoDataQualityScansComputeResourceRuntime = None,
    ):
        # Workspace environment of the compute engine. Valid values:
        # 
        # *   Prod
        # *   Dev
        self.env_type = env_type
        # The name of the computing engine. Uniquely identifies the engine.
        self.name = name
        # Additional runtime settings for the data quality monitor.
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
            temp_model = main_models.ListDataQualityScansResponseBodyPageInfoDataQualityScansComputeResourceRuntime()
            self.runtime = temp_model.from_map(m.get('Runtime'))

        return self

class ListDataQualityScansResponseBodyPageInfoDataQualityScansComputeResourceRuntime(DaraModel):
    def __init__(
        self,
        engine: str = None,
        hive_conf: str = None,
        spark_conf: str = None,
    ):
        # The engine type. These settings are only supported for the EMR compute engine. Valid values:
        # 
        # *   Hive: Hive SQL
        # *   Spark: Spark SQL
        # *   Kyuubi
        self.engine = engine
        # Additional parameters for the Hive engine. Currently, only mapreduce.job.queuename is supported to set the queue.
        self.hive_conf = hive_conf
        # Additional parameters for the Spark engine. Currently, only spark.yarn.queue is supported to set the queue.
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

