# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eds_aic20230930 import models as main_models
from darabonba.model import DaraModel

class BackupAppResponseBody(DaraModel):
    def __init__(
        self,
        count: int = None,
        data: List[main_models.BackupAppResponseBodyData] = None,
        request_id: str = None,
        task_id: str = None,
    ):
        self.count = count
        self.data = data
        self.request_id = request_id
        self.task_id = task_id

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.BackupAppResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

class BackupAppResponseBodyData(DaraModel):
    def __init__(
        self,
        android_instance_id: str = None,
        backup_file_id: str = None,
        backup_file_name: str = None,
        task_id: str = None,
    ):
        self.android_instance_id = android_instance_id
        self.backup_file_id = backup_file_id
        self.backup_file_name = backup_file_name
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.android_instance_id is not None:
            result['AndroidInstanceId'] = self.android_instance_id

        if self.backup_file_id is not None:
            result['BackupFileId'] = self.backup_file_id

        if self.backup_file_name is not None:
            result['BackupFileName'] = self.backup_file_name

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AndroidInstanceId') is not None:
            self.android_instance_id = m.get('AndroidInstanceId')

        if m.get('BackupFileId') is not None:
            self.backup_file_id = m.get('BackupFileId')

        if m.get('BackupFileName') is not None:
            self.backup_file_name = m.get('BackupFileName')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

