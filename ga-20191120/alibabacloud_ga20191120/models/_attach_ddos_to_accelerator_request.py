# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ga20191120 import models as main_models
from darabonba.model import DaraModel

class AttachDdosToAcceleratorRequest(DaraModel):
    def __init__(
        self,
        accelerator_id: str = None,
        ddos_config_list: List[main_models.AttachDdosToAcceleratorRequestDdosConfigList] = None,
        ddos_id: str = None,
        ddos_region_id: str = None,
        dry_run: bool = None,
        region_id: str = None,
    ):
        # The ID of the GA instance with which the Anti-DDoS Pro/Premium instance is associated.
        # 
        # This parameter is required.
        self.accelerator_id = accelerator_id
        self.ddos_config_list = ddos_config_list
        # The ID of the Anti-DDoS Pro/Premium instance to be associated with the GA instance.
        self.ddos_id = ddos_id
        # The region where the Anti-DDoS Pro/Premium instance is deployed. Valid values:
        # 
        # *   **cn-hangzhou**: regions in the Chinese mainland
        # *   **ap-southeast-1**: regions outside the Chinese mainland
        self.ddos_region_id = ddos_region_id
        self.dry_run = dry_run
        # The ID of the region where the GA instance is deployed. Set the value to **cn-hangzhou**.
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

        if self.ddos_id is not None:
            result['DdosId'] = self.ddos_id

        if self.ddos_region_id is not None:
            result['DdosRegionId'] = self.ddos_region_id

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
                temp_model = main_models.AttachDdosToAcceleratorRequestDdosConfigList()
                self.ddos_config_list.append(temp_model.from_map(k1))

        if m.get('DdosId') is not None:
            self.ddos_id = m.get('DdosId')

        if m.get('DdosRegionId') is not None:
            self.ddos_region_id = m.get('DdosRegionId')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

class AttachDdosToAcceleratorRequestDdosConfigList(DaraModel):
    def __init__(
        self,
        ddos_id: str = None,
        ddos_region_id: str = None,
    ):
        self.ddos_id = ddos_id
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

