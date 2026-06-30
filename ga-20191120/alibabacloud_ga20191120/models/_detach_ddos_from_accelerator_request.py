# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ga20191120 import models as main_models
from darabonba.model import DaraModel

class DetachDdosFromAcceleratorRequest(DaraModel):
    def __init__(
        self,
        accelerator_id: str = None,
        ddos_config_list: List[main_models.DetachDdosFromAcceleratorRequestDdosConfigList] = None,
        dry_run: bool = None,
        region_id: str = None,
    ):
        # The ID of the Global Accelerator instance.
        # 
        # This parameter is required.
        self.accelerator_id = accelerator_id
        # A list of Anti-DDoS Pro or Anti-DDoS Premium instances that are associated with the Global Accelerator instance.
        self.ddos_config_list = ddos_config_list
        # Specifies whether to perform a dry run. Valid values:
        # 
        # - **true**: performs a dry run. The system checks the required parameters, request format, and service limits. If the request fails the dry run, an error message is returned. If the request passes the dry run, the system returns an HTTP 2xx status code.
        # 
        # - **false** (default): sends a normal request. After the request passes the check, an HTTP 2xx status code is returned and the instance is detached.
        self.dry_run = dry_run
        # The ID of the region where the Global Accelerator instance is deployed. Set the value to **cn-hangzhou**.
        self.region_id = region_id

    def validate(self):
        if self.ddos_config_list:
            for v1 in self.ddos_config_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id

        result['DdosConfigList'] = []
        if self.ddos_config_list is not None:
            for k1 in self.ddos_config_list:
                result['DdosConfigList'].append(k1.to_map() if k1 else None)

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')

        self.ddos_config_list = []
        if m.get('DdosConfigList') is not None:
            for k1 in m.get('DdosConfigList'):
                temp_model = main_models.DetachDdosFromAcceleratorRequestDdosConfigList()
                self.ddos_config_list.append(temp_model.from_map(k1))

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

class DetachDdosFromAcceleratorRequestDdosConfigList(DaraModel):
    def __init__(
        self,
        ddos_id: str = None,
        ddos_region_id: str = None,
    ):
        # The ID of the Anti-DDoS Pro or Anti-DDoS Premium instance that is associated with the Global Accelerator instance.
        self.ddos_id = ddos_id
        # The region where the Anti-DDoS Pro or Anti-DDoS Premium instance is deployed. Valid values:
        # 
        # - **cn-hangzhou**: the Chinese mainland.
        # 
        # - **ap-southeast-1**: outside the Chinese mainland.
        self.ddos_region_id = ddos_region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ddos_id is not None:
            result['DdosId'] = self.ddos_id

        if self.ddos_region_id is not None:
            result['DdosRegionId'] = self.ddos_region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DdosId') is not None:
            self.ddos_id = m.get('DdosId')

        if m.get('DdosRegionId') is not None:
            self.ddos_region_id = m.get('DdosRegionId')

        return self

