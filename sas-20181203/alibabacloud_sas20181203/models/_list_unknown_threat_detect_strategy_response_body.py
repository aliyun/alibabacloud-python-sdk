# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class ListUnknownThreatDetectStrategyResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListUnknownThreatDetectStrategyResponseBodyData] = None,
        page_info: main_models.ListUnknownThreatDetectStrategyResponseBodyPageInfo = None,
        request_id: str = None,
    ):
        self.data = data
        self.page_info = page_info
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListUnknownThreatDetectStrategyResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('PageInfo') is not None:
            temp_model = main_models.ListUnknownThreatDetectStrategyResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListUnknownThreatDetectStrategyResponseBodyPageInfo(DaraModel):
    def __init__(
        self,
        count: int = None,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.count = count
        self.current_page = current_page
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListUnknownThreatDetectStrategyResponseBodyData(DaraModel):
    def __init__(
        self,
        asset_selection_type: str = None,
        duration_days_after_init: int = None,
        duration_days_after_stop: int = None,
        id: int = None,
        machine_count: int = None,
        name: str = None,
        study_mode: str = None,
    ):
        self.asset_selection_type = asset_selection_type
        self.duration_days_after_init = duration_days_after_init
        self.duration_days_after_stop = duration_days_after_stop
        self.id = id
        self.machine_count = machine_count
        self.name = name
        self.study_mode = study_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.asset_selection_type is not None:
            result['AssetSelectionType'] = self.asset_selection_type

        if self.duration_days_after_init is not None:
            result['DurationDaysAfterInit'] = self.duration_days_after_init

        if self.duration_days_after_stop is not None:
            result['DurationDaysAfterStop'] = self.duration_days_after_stop

        if self.id is not None:
            result['Id'] = self.id

        if self.machine_count is not None:
            result['MachineCount'] = self.machine_count

        if self.name is not None:
            result['Name'] = self.name

        if self.study_mode is not None:
            result['StudyMode'] = self.study_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssetSelectionType') is not None:
            self.asset_selection_type = m.get('AssetSelectionType')

        if m.get('DurationDaysAfterInit') is not None:
            self.duration_days_after_init = m.get('DurationDaysAfterInit')

        if m.get('DurationDaysAfterStop') is not None:
            self.duration_days_after_stop = m.get('DurationDaysAfterStop')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('MachineCount') is not None:
            self.machine_count = m.get('MachineCount')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('StudyMode') is not None:
            self.study_mode = m.get('StudyMode')

        return self

