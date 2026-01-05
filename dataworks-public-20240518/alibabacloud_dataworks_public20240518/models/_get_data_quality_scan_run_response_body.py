# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class GetDataQualityScanRunResponseBody(DaraModel):
    def __init__(
        self,
        data_quality_scan_run: main_models.GetDataQualityScanRunResponseBodyDataQualityScanRun = None,
        request_id: str = None,
    ):
        # Data quality monitoring running records.
        self.data_quality_scan_run = data_quality_scan_run
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data_quality_scan_run:
            self.data_quality_scan_run.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_quality_scan_run is not None:
            result['DataQualityScanRun'] = self.data_quality_scan_run.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataQualityScanRun') is not None:
            temp_model = main_models.GetDataQualityScanRunResponseBodyDataQualityScanRun()
            self.data_quality_scan_run = temp_model.from_map(m.get('DataQualityScanRun'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetDataQualityScanRunResponseBodyDataQualityScanRun(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        finish_time: int = None,
        id: int = None,
        parameters: List[main_models.GetDataQualityScanRunResponseBodyDataQualityScanRunParameters] = None,
        results: List[main_models.GetDataQualityScanRunResponseBodyDataQualityScanRunResults] = None,
        scan: main_models.GetDataQualityScanRunResponseBodyDataQualityScanRunScan = None,
        status: str = None,
    ):
        # The time when the data quality monitor starts running.
        self.create_time = create_time
        # The time when the data quality monitor stops.
        self.finish_time = finish_time
        # The running record ID.
        self.id = id
        # The parameter settings used during the actual running.
        self.parameters = parameters
        # The validation results of each rule.
        self.results = results
        # The snapshot of the data quality monitor configuration at the start of the validation.
        self.scan = scan
        # The current running status.
        # 
        # *   Pass
        # *   Running
        # *   Error
        # *   Warn
        # *   Fail
        self.status = status

    def validate(self):
        if self.parameters:
            for v1 in self.parameters:
                 if v1:
                    v1.validate()
        if self.results:
            for v1 in self.results:
                 if v1:
                    v1.validate()
        if self.scan:
            self.scan.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time

        if self.id is not None:
            result['Id'] = self.id

        result['Parameters'] = []
        if self.parameters is not None:
            for k1 in self.parameters:
                result['Parameters'].append(k1.to_map() if k1 else None)

        result['Results'] = []
        if self.results is not None:
            for k1 in self.results:
                result['Results'].append(k1.to_map() if k1 else None)

        if self.scan is not None:
            result['Scan'] = self.scan.to_map()

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        self.parameters = []
        if m.get('Parameters') is not None:
            for k1 in m.get('Parameters'):
                temp_model = main_models.GetDataQualityScanRunResponseBodyDataQualityScanRunParameters()
                self.parameters.append(temp_model.from_map(k1))

        self.results = []
        if m.get('Results') is not None:
            for k1 in m.get('Results'):
                temp_model = main_models.GetDataQualityScanRunResponseBodyDataQualityScanRunResults()
                self.results.append(temp_model.from_map(k1))

        if m.get('Scan') is not None:
            temp_model = main_models.GetDataQualityScanRunResponseBodyDataQualityScanRunScan()
            self.scan = temp_model.from_map(m.get('Scan'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class GetDataQualityScanRunResponseBodyDataQualityScanRunScan(DaraModel):
    def __init__(
        self,
        compute_resource: main_models.GetDataQualityScanRunResponseBodyDataQualityScanRunScanComputeResource = None,
        create_time: int = None,
        create_user: str = None,
        description: str = None,
        hooks: List[main_models.GetDataQualityScanRunResponseBodyDataQualityScanRunScanHooks] = None,
        id: int = None,
        modify_time: int = None,
        modify_user: str = None,
        name: str = None,
        owner: str = None,
        parameters: List[main_models.GetDataQualityScanRunResponseBodyDataQualityScanRunScanParameters] = None,
        project_id: int = None,
        runtime_resource: main_models.GetDataQualityScanRunResponseBodyDataQualityScanRunScanRuntimeResource = None,
        spec: str = None,
        trigger: main_models.GetDataQualityScanRunResponseBodyDataQualityScanRunScanTrigger = None,
    ):
        # The computing resource settings of the data quality monitor.
        self.compute_resource = compute_resource
        # The creation time of the data quality monitor.
        self.create_time = create_time
        # The creator of the data quality monitor.
        self.create_user = create_user
        # The description of the data quality validation task. Maximum length: 65,535 characters.
        self.description = description
        # The hook configurations after the data quality monitor stops.
        self.hooks = hooks
        # The data quality monitor ID.
        self.id = id
        # The last update time of the data quality monitor.
        self.modify_time = modify_time
        # The last updater of the data quality monitor.
        self.modify_user = modify_user
        # The name of the data quality validation task. It can contain digits, letters, Chinese characters, and both half-width and full-width punctuation marks, with a maximum length of 255 characters.
        self.name = name
        # The owner of the data quality monitor.
        self.owner = owner
        # The parameter settings of the data quality monitor.
        self.parameters = parameters
        # The project ID.
        self.project_id = project_id
        # The resource group used for running the data quality monitor.
        self.runtime_resource = runtime_resource
        # The data quality monitor Spec. For more information, see [Data quality Spec configuration description](https://help.aliyun.com/document_detail/2963394.html).
        self.spec = spec
        # The trigger configurations of the data quality monitor.
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
            temp_model = main_models.GetDataQualityScanRunResponseBodyDataQualityScanRunScanComputeResource()
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
                temp_model = main_models.GetDataQualityScanRunResponseBodyDataQualityScanRunScanHooks()
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
                temp_model = main_models.GetDataQualityScanRunResponseBodyDataQualityScanRunScanParameters()
                self.parameters.append(temp_model.from_map(k1))

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('RuntimeResource') is not None:
            temp_model = main_models.GetDataQualityScanRunResponseBodyDataQualityScanRunScanRuntimeResource()
            self.runtime_resource = temp_model.from_map(m.get('RuntimeResource'))

        if m.get('Spec') is not None:
            self.spec = m.get('Spec')

        if m.get('Trigger') is not None:
            temp_model = main_models.GetDataQualityScanRunResponseBodyDataQualityScanRunScanTrigger()
            self.trigger = temp_model.from_map(m.get('Trigger'))

        return self

class GetDataQualityScanRunResponseBodyDataQualityScanRunScanTrigger(DaraModel):
    def __init__(
        self,
        task_ids: List[int] = None,
        type: str = None,
    ):
        # If the trigger mode is set to BySchedule, the scheduling task ID must be specified.
        self.task_ids = task_ids
        # The trigger method of the data quality monitor.
        # 
        # *   ByManual
        # *   BySchedule
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

class GetDataQualityScanRunResponseBodyDataQualityScanRunScanRuntimeResource(DaraModel):
    def __init__(
        self,
        cu: float = None,
        id: str = None,
        image: str = None,
    ):
        # Reserved CUs for the resource group.
        self.cu = cu
        # The resource group ID.
        self.id = id
        # The image ID of the run configuration.
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

class GetDataQualityScanRunResponseBodyDataQualityScanRunScanParameters(DaraModel):
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

class GetDataQualityScanRunResponseBodyDataQualityScanRunScanHooks(DaraModel):
    def __init__(
        self,
        condition: str = None,
        type: str = None,
    ):
        # The hook trigger condition. Currently, only one type of expression syntax is supported:
        # 
        # *   Specify combinations of severity levels and validation statuses for multiple rules, such as `results.any { r -> r.status == \\"Fail\\" && r.rule.severity == \\"Normal\\" || r.status == \\"Error\\" && r.rule.severity == \\"High\\" || r.status == \\"Warn\\" && r.rule.severity == \\"High\\" }`. This means the hook is triggered if any executed rule has Fail with Normal severity, Error with High severity, or Warn with High severity. In the conditional expression, the severity value matches that in the Spec code, and the status value matches that in DataQualityResult.
        self.condition = condition
        # The type of the hook.
        # 
        # *   BlockTaskInstance
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

class GetDataQualityScanRunResponseBodyDataQualityScanRunScanComputeResource(DaraModel):
    def __init__(
        self,
        env_type: str = None,
        name: str = None,
        runtime: main_models.GetDataQualityScanRunResponseBodyDataQualityScanRunScanComputeResourceRuntime = None,
    ):
        # The workspace environment to which the compute engine belongs.
        # 
        # *   Prod
        # *   Dev
        self.env_type = env_type
        # The name of the computing resource, which corresponds to the Name attribute in the ComputeResource data structure of the computing resource API.
        self.name = name
        # The additional runtime settings of the data quality monitor.
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
            temp_model = main_models.GetDataQualityScanRunResponseBodyDataQualityScanRunScanComputeResourceRuntime()
            self.runtime = temp_model.from_map(m.get('Runtime'))

        return self

class GetDataQualityScanRunResponseBodyDataQualityScanRunScanComputeResourceRuntime(DaraModel):
    def __init__(
        self,
        engine: str = None,
        hive_conf: Dict[str, Any] = None,
        spark_conf: Dict[str, Any] = None,
    ):
        # The type of the compute engine. Only EMR compute engines support these settings.
        # 
        # *   Hive
        # *   Spark
        # *   Kyuubi
        self.engine = engine
        # Additional parameters for the Hive engine. Currently, only mapreduce.job.queuename is supported to specify the queue.
        self.hive_conf = hive_conf
        # Additional parameters for the Spark engine. Currently, only spark.yarn.queue is supported to specify the queue.
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

class GetDataQualityScanRunResponseBodyDataQualityScanRunResults(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        details: List[main_models.GetDataQualityScanRunResponseBodyDataQualityScanRunResultsDetails] = None,
        rule: str = None,
        sample: str = None,
        status: str = None,
    ):
        # The time when the validation result is generated.
        self.create_time = create_time
        # The information about the data quality check.
        self.details = details
        # The snapshot of the rule Spec at the start of the validation.
        self.rule = rule
        # The sample value used in the validation.
        self.sample = sample
        # The validation result status.
        # 
        # *   Pass
        # *   Running
        # *   Error
        # *   Warn
        # *   Fail
        self.status = status

    def validate(self):
        if self.details:
            for v1 in self.details:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        result['Details'] = []
        if self.details is not None:
            for k1 in self.details:
                result['Details'].append(k1.to_map() if k1 else None)

        if self.rule is not None:
            result['Rule'] = self.rule

        if self.sample is not None:
            result['Sample'] = self.sample

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        self.details = []
        if m.get('Details') is not None:
            for k1 in m.get('Details'):
                temp_model = main_models.GetDataQualityScanRunResponseBodyDataQualityScanRunResultsDetails()
                self.details.append(temp_model.from_map(k1))

        if m.get('Rule') is not None:
            self.rule = m.get('Rule')

        if m.get('Sample') is not None:
            self.sample = m.get('Sample')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class GetDataQualityScanRunResponseBodyDataQualityScanRunResultsDetails(DaraModel):
    def __init__(
        self,
        check_value: str = None,
        reference_value: str = None,
        status: str = None,
    ):
        # The final value used for comparison with the threshold.
        self.check_value = check_value
        # The reference sample used as the baseline for calculating the CheckedValue.
        self.reference_value = reference_value
        # The final comparison result status.
        # 
        # *   Pass
        # *   Error
        # *   Warn
        # *   Fail
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_value is not None:
            result['CheckValue'] = self.check_value

        if self.reference_value is not None:
            result['ReferenceValue'] = self.reference_value

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckValue') is not None:
            self.check_value = m.get('CheckValue')

        if m.get('ReferenceValue') is not None:
            self.reference_value = m.get('ReferenceValue')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class GetDataQualityScanRunResponseBodyDataQualityScanRunParameters(DaraModel):
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

