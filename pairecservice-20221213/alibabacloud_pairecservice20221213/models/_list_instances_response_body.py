# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_pairecservice20221213 import models as main_models
from darabonba.model import DaraModel

class ListInstancesResponseBody(DaraModel):
    def __init__(
        self,
        instances: List[main_models.ListInstancesResponseBodyInstances] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # A list of instances.
        self.instances = instances
        # The request ID.
        self.request_id = request_id
        # The total number of returned instances.
        self.total_count = total_count

    def validate(self):
        if self.instances:
            for v1 in self.instances:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Instances'] = []
        if self.instances is not None:
            for k1 in self.instances:
                result['Instances'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instances = []
        if m.get('Instances') is not None:
            for k1 in m.get('Instances'):
                temp_model = main_models.ListInstancesResponseBodyInstances()
                self.instances.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListInstancesResponseBodyInstances(DaraModel):
    def __init__(
        self,
        charge_type: str = None,
        commodity_code: str = None,
        config: main_models.ListInstancesResponseBodyInstancesConfig = None,
        expired_time: str = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        instance_id: str = None,
        operating_tool: main_models.ListInstancesResponseBodyInstancesOperatingTool = None,
        region_id: str = None,
        status: str = None,
        type: str = None,
    ):
        # The billing method of the instance. Only `Subscription` (prepaid) is supported.
        self.charge_type = charge_type
        # The commodity code of the instance.
        self.commodity_code = commodity_code
        # The instance configuration.
        self.config = config
        # The time when the instance expires.
        self.expired_time = expired_time
        # The time when the instance was created.
        self.gmt_create_time = gmt_create_time
        # The time when the instance was last modified.
        self.gmt_modified_time = gmt_modified_time
        # The instance ID.
        self.instance_id = instance_id
        # The configuration of the operating tool.
        self.operating_tool = operating_tool
        # The region ID. Valid values:
        # 
        # - `cn-shenzhen`: China (Shenzhen)
        # 
        # - `cn-hangzhou`: China (Hangzhou)
        # 
        # - `cn-beijing`: China (Beijing)
        # 
        # - `cn-shanghai`: China (Shanghai)
        self.region_id = region_id
        # The instance status. Valid values:
        # 
        # - `Initializing`: The instance is initializing.
        # 
        # - `Stopped`: The instance is stopped.
        # 
        # - `Running`: The instance is running.
        self.status = status
        # The instance type. Valid values:
        # 
        # - `basic`: Basic Edition
        # 
        # - `high-level`: High-level Edition
        # 
        # - `advanced`: Advanced Edition
        # 
        # - `standard`: Standard Edition
        self.type = type

    def validate(self):
        if self.config:
            self.config.validate()
        if self.operating_tool:
            self.operating_tool.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code

        if self.config is not None:
            result['Config'] = self.config.to_map()

        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time

        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time

        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.operating_tool is not None:
            result['OperatingTool'] = self.operating_tool.to_map()

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')

        if m.get('Config') is not None:
            temp_model = main_models.ListInstancesResponseBodyInstancesConfig()
            self.config = temp_model.from_map(m.get('Config'))

        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')

        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')

        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('OperatingTool') is not None:
            temp_model = main_models.ListInstancesResponseBodyInstancesOperatingTool()
            self.operating_tool = temp_model.from_map(m.get('OperatingTool'))

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class ListInstancesResponseBodyInstancesOperatingTool(DaraModel):
    def __init__(
        self,
        is_enable: bool = None,
    ):
        # Specifies whether the operating tool is enabled for the instance. Valid values:
        # 
        # - `true`: The tool is enabled.
        # 
        # - `false`: The tool is disabled.
        self.is_enable = is_enable

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.is_enable is not None:
            result['IsEnable'] = self.is_enable

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsEnable') is not None:
            self.is_enable = m.get('IsEnable')

        return self

class ListInstancesResponseBodyInstancesConfig(DaraModel):
    def __init__(
        self,
        data_managements: List[main_models.ListInstancesResponseBodyInstancesConfigDataManagements] = None,
        engines: List[main_models.ListInstancesResponseBodyInstancesConfigEngines] = None,
        monitors: List[main_models.ListInstancesResponseBodyInstancesConfigMonitors] = None,
    ):
        # A list of data management configurations.
        self.data_managements = data_managements
        # A list of service engines.
        self.engines = engines
        # A list of monitoring components.
        self.monitors = monitors

    def validate(self):
        if self.data_managements:
            for v1 in self.data_managements:
                 if v1:
                    v1.validate()
        if self.engines:
            for v1 in self.engines:
                 if v1:
                    v1.validate()
        if self.monitors:
            for v1 in self.monitors:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DataManagements'] = []
        if self.data_managements is not None:
            for k1 in self.data_managements:
                result['DataManagements'].append(k1.to_map() if k1 else None)

        result['Engines'] = []
        if self.engines is not None:
            for k1 in self.engines:
                result['Engines'].append(k1.to_map() if k1 else None)

        result['Monitors'] = []
        if self.monitors is not None:
            for k1 in self.monitors:
                result['Monitors'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_managements = []
        if m.get('DataManagements') is not None:
            for k1 in m.get('DataManagements'):
                temp_model = main_models.ListInstancesResponseBodyInstancesConfigDataManagements()
                self.data_managements.append(temp_model.from_map(k1))

        self.engines = []
        if m.get('Engines') is not None:
            for k1 in m.get('Engines'):
                temp_model = main_models.ListInstancesResponseBodyInstancesConfigEngines()
                self.engines.append(temp_model.from_map(k1))

        self.monitors = []
        if m.get('Monitors') is not None:
            for k1 in m.get('Monitors'):
                temp_model = main_models.ListInstancesResponseBodyInstancesConfigMonitors()
                self.monitors.append(temp_model.from_map(k1))

        return self

class ListInstancesResponseBodyInstancesConfigMonitors(DaraModel):
    def __init__(
        self,
        component_code: str = None,
        meta: Dict[str, Any] = None,
        type: str = None,
    ):
        # The component code.
        self.component_code = component_code
        # The metadata of the component.
        self.meta = meta
        # The component type.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.component_code is not None:
            result['ComponentCode'] = self.component_code

        if self.meta is not None:
            result['Meta'] = self.meta

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComponentCode') is not None:
            self.component_code = m.get('ComponentCode')

        if m.get('Meta') is not None:
            self.meta = m.get('Meta')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class ListInstancesResponseBodyInstancesConfigEngines(DaraModel):
    def __init__(
        self,
        component_code: str = None,
        meta: Dict[str, Any] = None,
        type: str = None,
    ):
        # The component code.
        self.component_code = component_code
        # The metadata of the component.
        self.meta = meta
        # The component type.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.component_code is not None:
            result['ComponentCode'] = self.component_code

        if self.meta is not None:
            result['Meta'] = self.meta

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComponentCode') is not None:
            self.component_code = m.get('ComponentCode')

        if m.get('Meta') is not None:
            self.meta = m.get('Meta')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class ListInstancesResponseBodyInstancesConfigDataManagements(DaraModel):
    def __init__(
        self,
        component_code: str = None,
        meta: Dict[str, Any] = None,
        type: str = None,
    ):
        # The component code.
        self.component_code = component_code
        # The metadata of the component.
        self.meta = meta
        # The component type.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.component_code is not None:
            result['ComponentCode'] = self.component_code

        if self.meta is not None:
            result['Meta'] = self.meta

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComponentCode') is not None:
            self.component_code = m.get('ComponentCode')

        if m.get('Meta') is not None:
            self.meta = m.get('Meta')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

