# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pvtz20180101 import models as main_models
from darabonba.model import DaraModel

class UpdateSyncEcsHostTaskRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        region: List[main_models.UpdateSyncEcsHostTaskRequestRegion] = None,
        status: str = None,
        zone_id: str = None,
    ):
        # The language of the response. Valid values:
        # 
        # *   zh: Chinese
        # *   en: English
        # 
        # Default value: en.
        self.lang = lang
        # The regions to be synchronized.
        # 
        # This parameter is required.
        self.region = region
        # The state of the hostname synchronization task. Valid values:
        # 
        # *   ON: The task is started.
        # *   OFF: The task is ended.
        # 
        # This parameter is required.
        self.status = status
        # The zone ID. This ID uniquely identifies the zone.
        # 
        # This parameter is required.
        self.zone_id = zone_id

    def validate(self):
        if self.region:
            for v1 in self.region:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        result['Region'] = []
        if self.region is not None:
            for k1 in self.region:
                result['Region'].append(k1.to_map() if k1 else None)

        if self.status is not None:
            result['Status'] = self.status

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        self.region = []
        if m.get('Region') is not None:
            for k1 in m.get('Region'):
                temp_model = main_models.UpdateSyncEcsHostTaskRequestRegion()
                self.region.append(temp_model.from_map(k1))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class UpdateSyncEcsHostTaskRequestRegion(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        user_id: int = None,
    ):
        # The region ID.
        self.region_id = region_id
        # The user ID to which the region belongs. This parameter is used in cross-account synchronization scenarios.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

