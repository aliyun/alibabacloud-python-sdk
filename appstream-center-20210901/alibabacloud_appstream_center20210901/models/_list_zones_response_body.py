# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_appstream_center20210901 import models as main_models
from darabonba.model import DaraModel

class ListZonesResponseBody(DaraModel):
    def __init__(
        self,
        list_zones_model: main_models.ListZonesResponseBodyListZonesModel = None,
        request_id: str = None,
    ):
        # The zone query result.
        self.list_zones_model = list_zones_model
        # The request ID. You can use this ID to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.list_zones_model:
            self.list_zones_model.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.list_zones_model is not None:
            result['ListZonesModel'] = self.list_zones_model.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ListZonesModel') is not None:
            temp_model = main_models.ListZonesResponseBodyListZonesModel()
            self.list_zones_model = temp_model.from_map(m.get('ListZonesModel'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListZonesResponseBodyListZonesModel(DaraModel):
    def __init__(
        self,
        zones: List[str] = None,
    ):
        # The list of available zone IDs for the specified product type and operating system type in the current region. When creating a resource that requires a vSwitch, select a vSwitch in one of these zones.
        self.zones = zones

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.zones is not None:
            result['Zones'] = self.zones

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Zones') is not None:
            self.zones = m.get('Zones')

        return self

