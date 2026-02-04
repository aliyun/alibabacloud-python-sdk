# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateDataSetRecordRequest(DaraModel):
    def __init__(
        self,
        data_set_file_name: str = None,
        data_set_id: str = None,
        data_set_records: str = None,
        lang: str = None,
        region_id: str = None,
        role_for: int = None,
    ):
        self.data_set_file_name = data_set_file_name
        # This parameter is required.
        self.data_set_id = data_set_id
        self.data_set_records = data_set_records
        self.lang = lang
        self.region_id = region_id
        self.role_for = role_for

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_set_file_name is not None:
            result['DataSetFileName'] = self.data_set_file_name

        if self.data_set_id is not None:
            result['DataSetId'] = self.data_set_id

        if self.data_set_records is not None:
            result['DataSetRecords'] = self.data_set_records

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.role_for is not None:
            result['RoleFor'] = self.role_for

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSetFileName') is not None:
            self.data_set_file_name = m.get('DataSetFileName')

        if m.get('DataSetId') is not None:
            self.data_set_id = m.get('DataSetId')

        if m.get('DataSetRecords') is not None:
            self.data_set_records = m.get('DataSetRecords')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')

        return self

