# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class ListUserRoutinesResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        quota_routine_number: int = None,
        request_id: str = None,
        routines: List[main_models.ListUserRoutinesResponseBodyRoutines] = None,
        total_count: int = None,
        used_routine_number: int = None,
    ):
        # The page number. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The maximum number of functions supported by the billing plan.
        self.quota_routine_number = quota_routine_number
        # The request ID.
        self.request_id = request_id
        # The functions.
        self.routines = routines
        # The total count.
        self.total_count = total_count
        # The number of functions that were already created.
        self.used_routine_number = used_routine_number

    def validate(self):
        if self.routines:
            for v1 in self.routines:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.quota_routine_number is not None:
            result['QuotaRoutineNumber'] = self.quota_routine_number

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Routines'] = []
        if self.routines is not None:
            for k1 in self.routines:
                result['Routines'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.used_routine_number is not None:
            result['UsedRoutineNumber'] = self.used_routine_number

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('QuotaRoutineNumber') is not None:
            self.quota_routine_number = m.get('QuotaRoutineNumber')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.routines = []
        if m.get('Routines') is not None:
            for k1 in m.get('Routines'):
                temp_model = main_models.ListUserRoutinesResponseBodyRoutines()
                self.routines.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('UsedRoutineNumber') is not None:
            self.used_routine_number = m.get('UsedRoutineNumber')

        return self

class ListUserRoutinesResponseBodyRoutines(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        default_related_record: str = None,
        description: str = None,
        has_assets: bool = None,
        routine_name: str = None,
    ):
        # The time when the function was created.
        self.create_time = create_time
        # The default record name to access.
        self.default_related_record = default_related_record
        # The function description.
        self.description = description
        # Specifies whether to include the Assets file tag.
        self.has_assets = has_assets
        # The function name.
        self.routine_name = routine_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.default_related_record is not None:
            result['DefaultRelatedRecord'] = self.default_related_record

        if self.description is not None:
            result['Description'] = self.description

        if self.has_assets is not None:
            result['HasAssets'] = self.has_assets

        if self.routine_name is not None:
            result['RoutineName'] = self.routine_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DefaultRelatedRecord') is not None:
            self.default_related_record = m.get('DefaultRelatedRecord')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('HasAssets') is not None:
            self.has_assets = m.get('HasAssets')

        if m.get('RoutineName') is not None:
            self.routine_name = m.get('RoutineName')

        return self

