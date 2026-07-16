# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class GetFileProtectClientEventDashboardResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetFileProtectClientEventDashboardResponseBodyData = None,
        request_id: str = None,
    ):
        # The returned data.
        self.data = data
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.GetFileProtectClientEventDashboardResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetFileProtectClientEventDashboardResponseBodyData(DaraModel):
    def __init__(
        self,
        file_path_stats: List[main_models.GetFileProtectClientEventDashboardResponseBodyDataFilePathStats] = None,
        file_type_stats: List[main_models.GetFileProtectClientEventDashboardResponseBodyDataFileTypeStats] = None,
        one_day_file_change_count: int = None,
        process_name_stats: List[main_models.GetFileProtectClientEventDashboardResponseBodyDataProcessNameStats] = None,
        recent_file_change_count: int = None,
        server_count: int = None,
    ):
        # The tamper-proofing event statistics grouped by file path.
        self.file_path_stats = file_path_stats
        # The event statistics grouped by file type.
        self.file_type_stats = file_type_stats
        # The number of file tamper-proofing events for today.
        self.one_day_file_change_count = one_day_file_change_count
        # The event statistics grouped by process name.
        self.process_name_stats = process_name_stats
        # The number of file tamper-proofing events in the last 15 days.
        self.recent_file_change_count = recent_file_change_count
        # The number of affected servers.
        self.server_count = server_count

    def validate(self):
        if self.file_path_stats:
            for v1 in self.file_path_stats:
                 if v1:
                    v1.validate()
        if self.file_type_stats:
            for v1 in self.file_type_stats:
                 if v1:
                    v1.validate()
        if self.process_name_stats:
            for v1 in self.process_name_stats:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['FilePathStats'] = []
        if self.file_path_stats is not None:
            for k1 in self.file_path_stats:
                result['FilePathStats'].append(k1.to_map() if k1 else None)

        result['FileTypeStats'] = []
        if self.file_type_stats is not None:
            for k1 in self.file_type_stats:
                result['FileTypeStats'].append(k1.to_map() if k1 else None)

        if self.one_day_file_change_count is not None:
            result['OneDayFileChangeCount'] = self.one_day_file_change_count

        result['ProcessNameStats'] = []
        if self.process_name_stats is not None:
            for k1 in self.process_name_stats:
                result['ProcessNameStats'].append(k1.to_map() if k1 else None)

        if self.recent_file_change_count is not None:
            result['RecentFileChangeCount'] = self.recent_file_change_count

        if self.server_count is not None:
            result['ServerCount'] = self.server_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.file_path_stats = []
        if m.get('FilePathStats') is not None:
            for k1 in m.get('FilePathStats'):
                temp_model = main_models.GetFileProtectClientEventDashboardResponseBodyDataFilePathStats()
                self.file_path_stats.append(temp_model.from_map(k1))

        self.file_type_stats = []
        if m.get('FileTypeStats') is not None:
            for k1 in m.get('FileTypeStats'):
                temp_model = main_models.GetFileProtectClientEventDashboardResponseBodyDataFileTypeStats()
                self.file_type_stats.append(temp_model.from_map(k1))

        if m.get('OneDayFileChangeCount') is not None:
            self.one_day_file_change_count = m.get('OneDayFileChangeCount')

        self.process_name_stats = []
        if m.get('ProcessNameStats') is not None:
            for k1 in m.get('ProcessNameStats'):
                temp_model = main_models.GetFileProtectClientEventDashboardResponseBodyDataProcessNameStats()
                self.process_name_stats.append(temp_model.from_map(k1))

        if m.get('RecentFileChangeCount') is not None:
            self.recent_file_change_count = m.get('RecentFileChangeCount')

        if m.get('ServerCount') is not None:
            self.server_count = m.get('ServerCount')

        return self

class GetFileProtectClientEventDashboardResponseBodyDataProcessNameStats(DaraModel):
    def __init__(
        self,
        key: str = None,
        num: int = None,
    ):
        # The process name.
        self.key = key
        # The number of events.
        self.num = num

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.num is not None:
            result['Num'] = self.num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Num') is not None:
            self.num = m.get('Num')

        return self

class GetFileProtectClientEventDashboardResponseBodyDataFileTypeStats(DaraModel):
    def __init__(
        self,
        key: str = None,
        num: int = None,
    ):
        # The file type name.
        self.key = key
        # The count.
        self.num = num

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.num is not None:
            result['Num'] = self.num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Num') is not None:
            self.num = m.get('Num')

        return self

class GetFileProtectClientEventDashboardResponseBodyDataFilePathStats(DaraModel):
    def __init__(
        self,
        key: str = None,
        num: int = None,
    ):
        # The file path.
        self.key = key
        # The total number of events.
        self.num = num

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.num is not None:
            result['Num'] = self.num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Num') is not None:
            self.num = m.get('Num')

        return self

