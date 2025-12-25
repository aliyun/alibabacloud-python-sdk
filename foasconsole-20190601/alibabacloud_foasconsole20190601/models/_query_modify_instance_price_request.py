# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_foasconsole20190601 import models as main_models
from darabonba.model import DaraModel

class QueryModifyInstancePriceRequest(DaraModel):
    def __init__(
        self,
        modify_prepay_instance_spec_request: main_models.QueryModifyInstancePriceRequestModifyPrepayInstanceSpecRequest = None,
    ):
        # This parameter is required.
        self.modify_prepay_instance_spec_request = modify_prepay_instance_spec_request

    def validate(self):
        if self.modify_prepay_instance_spec_request:
            self.modify_prepay_instance_spec_request.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.modify_prepay_instance_spec_request is not None:
            result['ModifyPrepayInstanceSpecRequest'] = self.modify_prepay_instance_spec_request.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModifyPrepayInstanceSpecRequest') is not None:
            temp_model = main_models.QueryModifyInstancePriceRequestModifyPrepayInstanceSpecRequest()
            self.modify_prepay_instance_spec_request = temp_model.from_map(m.get('ModifyPrepayInstanceSpecRequest'))

        return self

class QueryModifyInstancePriceRequestModifyPrepayInstanceSpecRequest(DaraModel):
    def __init__(
        self,
        ha: bool = None,
        ha_resource_spec: main_models.QueryModifyInstancePriceRequestModifyPrepayInstanceSpecRequestHaResourceSpec = None,
        ha_vswitch_ids: List[str] = None,
        ha_zone_id: str = None,
        instance_id: str = None,
        region: str = None,
        resource_spec: main_models.QueryModifyInstancePriceRequestModifyPrepayInstanceSpecRequestResourceSpec = None,
    ):
        self.ha = ha
        self.ha_resource_spec = ha_resource_spec
        self.ha_vswitch_ids = ha_vswitch_ids
        self.ha_zone_id = ha_zone_id
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.region = region
        # This parameter is required.
        self.resource_spec = resource_spec

    def validate(self):
        if self.ha_resource_spec:
            self.ha_resource_spec.validate()
        if self.resource_spec:
            self.resource_spec.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ha is not None:
            result['Ha'] = self.ha

        if self.ha_resource_spec is not None:
            result['HaResourceSpec'] = self.ha_resource_spec.to_map()

        if self.ha_vswitch_ids is not None:
            result['HaVSwitchIds'] = self.ha_vswitch_ids

        if self.ha_zone_id is not None:
            result['HaZoneId'] = self.ha_zone_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.region is not None:
            result['Region'] = self.region

        if self.resource_spec is not None:
            result['ResourceSpec'] = self.resource_spec.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ha') is not None:
            self.ha = m.get('Ha')

        if m.get('HaResourceSpec') is not None:
            temp_model = main_models.QueryModifyInstancePriceRequestModifyPrepayInstanceSpecRequestHaResourceSpec()
            self.ha_resource_spec = temp_model.from_map(m.get('HaResourceSpec'))

        if m.get('HaVSwitchIds') is not None:
            self.ha_vswitch_ids = m.get('HaVSwitchIds')

        if m.get('HaZoneId') is not None:
            self.ha_zone_id = m.get('HaZoneId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('ResourceSpec') is not None:
            temp_model = main_models.QueryModifyInstancePriceRequestModifyPrepayInstanceSpecRequestResourceSpec()
            self.resource_spec = temp_model.from_map(m.get('ResourceSpec'))

        return self

class QueryModifyInstancePriceRequestModifyPrepayInstanceSpecRequestResourceSpec(DaraModel):
    def __init__(
        self,
        cpu: int = None,
        memory_gb: int = None,
    ):
        # This parameter is required.
        self.cpu = cpu
        # This parameter is required.
        self.memory_gb = memory_gb

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cpu is not None:
            result['Cpu'] = self.cpu

        if self.memory_gb is not None:
            result['MemoryGB'] = self.memory_gb

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')

        if m.get('MemoryGB') is not None:
            self.memory_gb = m.get('MemoryGB')

        return self

class QueryModifyInstancePriceRequestModifyPrepayInstanceSpecRequestHaResourceSpec(DaraModel):
    def __init__(
        self,
        cpu: int = None,
        memory_gb: int = None,
    ):
        self.cpu = cpu
        self.memory_gb = memory_gb

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cpu is not None:
            result['Cpu'] = self.cpu

        if self.memory_gb is not None:
            result['MemoryGB'] = self.memory_gb

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')

        if m.get('MemoryGB') is not None:
            self.memory_gb = m.get('MemoryGB')

        return self

