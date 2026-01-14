# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_energyexpertexternal20220923 import models as main_models
from darabonba.model import DaraModel

class EditUnfavorableAreaDevicesRequest(DaraModel):
    def __init__(
        self,
        factory_id: str = None,
        hvac_device_config_volist: List[main_models.EditUnfavorableAreaDevicesRequestHvacDeviceConfigVOList] = None,
        system_id: str = None,
    ):
        # This parameter is required.
        self.factory_id = factory_id
        # This parameter is required.
        self.hvac_device_config_volist = hvac_device_config_volist
        # This parameter is required.
        self.system_id = system_id

    def validate(self):
        if self.hvac_device_config_volist:
            for v1 in self.hvac_device_config_volist:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.factory_id is not None:
            result['factoryId'] = self.factory_id

        result['hvacDeviceConfigVOList'] = []
        if self.hvac_device_config_volist is not None:
            for k1 in self.hvac_device_config_volist:
                result['hvacDeviceConfigVOList'].append(k1.to_map() if k1 else None)

        if self.system_id is not None:
            result['systemId'] = self.system_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('factoryId') is not None:
            self.factory_id = m.get('factoryId')

        self.hvac_device_config_volist = []
        if m.get('hvacDeviceConfigVOList') is not None:
            for k1 in m.get('hvacDeviceConfigVOList'):
                temp_model = main_models.EditUnfavorableAreaDevicesRequestHvacDeviceConfigVOList()
                self.hvac_device_config_volist.append(temp_model.from_map(k1))

        if m.get('systemId') is not None:
            self.system_id = m.get('systemId')

        return self

class EditUnfavorableAreaDevicesRequestHvacDeviceConfigVOList(DaraModel):
    def __init__(
        self,
        building_id: str = None,
        device_id: str = None,
        device_name: str = None,
        device_type: str = None,
        fence_id: str = None,
        floor_id: str = None,
        is_forbidden: int = None,
        is_unfavorable_area: int = None,
    ):
        self.building_id = building_id
        self.device_id = device_id
        self.device_name = device_name
        # This parameter is required.
        self.device_type = device_type
        self.fence_id = fence_id
        self.floor_id = floor_id
        self.is_forbidden = is_forbidden
        # This parameter is required.
        self.is_unfavorable_area = is_unfavorable_area

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.building_id is not None:
            result['buildingId'] = self.building_id

        if self.device_id is not None:
            result['deviceId'] = self.device_id

        if self.device_name is not None:
            result['deviceName'] = self.device_name

        if self.device_type is not None:
            result['deviceType'] = self.device_type

        if self.fence_id is not None:
            result['fenceId'] = self.fence_id

        if self.floor_id is not None:
            result['floorId'] = self.floor_id

        if self.is_forbidden is not None:
            result['isForbidden'] = self.is_forbidden

        if self.is_unfavorable_area is not None:
            result['isUnfavorableArea'] = self.is_unfavorable_area

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('buildingId') is not None:
            self.building_id = m.get('buildingId')

        if m.get('deviceId') is not None:
            self.device_id = m.get('deviceId')

        if m.get('deviceName') is not None:
            self.device_name = m.get('deviceName')

        if m.get('deviceType') is not None:
            self.device_type = m.get('deviceType')

        if m.get('fenceId') is not None:
            self.fence_id = m.get('fenceId')

        if m.get('floorId') is not None:
            self.floor_id = m.get('floorId')

        if m.get('isForbidden') is not None:
            self.is_forbidden = m.get('isForbidden')

        if m.get('isUnfavorableArea') is not None:
            self.is_unfavorable_area = m.get('isUnfavorableArea')

        return self

