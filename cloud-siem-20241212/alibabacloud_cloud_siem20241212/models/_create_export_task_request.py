# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateExportTaskRequest(DaraModel):
    def __init__(
        self,
        export_task_parameter: str = None,
        export_task_type: str = None,
        lang: str = None,
        region_id: str = None,
        role_for: int = None,
    ):
        # The export task parameters, which are concatenated based on query conditions in JSON format.
        self.export_task_parameter = export_task_parameter
        # The export type. Valid values:
        # - incident_list: Event list.
        self.export_task_type = export_task_type
        # The language of the response. Valid values:
        # - **zh** (default): Chinese.
        # - **en**: English.
        # > Note: This parameter is required. If you do not specify this parameter, the API returns a 400 error: "The specified Lang can not be empty."
        self.lang = lang
        # The region where the threat analysis data management center resides. Specify the management center region based on the region of your assets. Valid values:
        # - cn-hangzhou: Your assets reside in the Chinese mainland.
        # - ap-southeast-1: Your assets reside outside China.
        self.region_id = region_id
        # The ID of the member to which the administrator switches the view.
        self.role_for = role_for

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.export_task_parameter is not None:
            result['ExportTaskParameter'] = self.export_task_parameter

        if self.export_task_type is not None:
            result['ExportTaskType'] = self.export_task_type

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.role_for is not None:
            result['RoleFor'] = self.role_for

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExportTaskParameter') is not None:
            self.export_task_parameter = m.get('ExportTaskParameter')

        if m.get('ExportTaskType') is not None:
            self.export_task_type = m.get('ExportTaskType')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')

        return self

