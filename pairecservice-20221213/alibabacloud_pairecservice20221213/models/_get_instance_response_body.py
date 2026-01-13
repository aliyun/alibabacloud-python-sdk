# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_pairecservice20221213 import models as main_models
from darabonba.model import DaraModel

class GetInstanceResponseBody(DaraModel):
    def __init__(
        self,
        charge_type: str = None,
        commodity_code: str = None,
        config: main_models.GetInstanceResponseBodyConfig = None,
        expired_time: str = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        instance_id: str = None,
        operating_tool: main_models.GetInstanceResponseBodyOperatingTool = None,
        region_id: str = None,
        request_id: str = None,
        status: str = None,
        type: str = None,
    ):
        self.charge_type = charge_type
        self.commodity_code = commodity_code
        self.config = config
        self.expired_time = expired_time
        self.gmt_create_time = gmt_create_time
        self.gmt_modified_time = gmt_modified_time
        self.instance_id = instance_id
        self.operating_tool = operating_tool
        self.region_id = region_id
        self.request_id = request_id
        self.status = status
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

        if self.request_id is not None:
            result['RequestId'] = self.request_id

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
            temp_model = main_models.GetInstanceResponseBodyConfig()
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
            temp_model = main_models.GetInstanceResponseBodyOperatingTool()
            self.operating_tool = temp_model.from_map(m.get('OperatingTool'))

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class GetInstanceResponseBodyOperatingTool(DaraModel):
    def __init__(
        self,
        is_enable: bool = None,
    ):
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

class GetInstanceResponseBodyConfig(DaraModel):
    def __init__(
        self,
        data_managements: List[main_models.GetInstanceResponseBodyConfigDataManagements] = None,
        engines: List[main_models.GetInstanceResponseBodyConfigEngines] = None,
        monitors: List[main_models.GetInstanceResponseBodyConfigMonitors] = None,
    ):
        self.data_managements = data_managements
        self.engines = engines
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
                temp_model = main_models.GetInstanceResponseBodyConfigDataManagements()
                self.data_managements.append(temp_model.from_map(k1))

        self.engines = []
        if m.get('Engines') is not None:
            for k1 in m.get('Engines'):
                temp_model = main_models.GetInstanceResponseBodyConfigEngines()
                self.engines.append(temp_model.from_map(k1))

        self.monitors = []
        if m.get('Monitors') is not None:
            for k1 in m.get('Monitors'):
                temp_model = main_models.GetInstanceResponseBodyConfigMonitors()
                self.monitors.append(temp_model.from_map(k1))

        return self

class GetInstanceResponseBodyConfigMonitors(DaraModel):
    def __init__(
        self,
        component_code: str = None,
        meta: Dict[str, Any] = None,
        type: str = None,
    ):
        self.component_code = component_code
        self.meta = meta
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

class GetInstanceResponseBodyConfigEngines(DaraModel):
    def __init__(
        self,
        component_code: str = None,
        meta: Dict[str, Any] = None,
        type: str = None,
    ):
        self.component_code = component_code
        self.meta = meta
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

class GetInstanceResponseBodyConfigDataManagements(DaraModel):
    def __init__(
        self,
        component_code: str = None,
        meta: Dict[str, Any] = None,
        type: str = None,
    ):
        self.component_code = component_code
        self.meta = meta
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

