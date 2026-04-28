# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pds20220301 import models as main_models
from darabonba.model import DaraModel

class InvestigateFileRequest(DaraModel):
    def __init__(
        self,
        drive_file_ids: List[main_models.InvestigateFileRequestDriveFileIds] = None,
    ):
        # This parameter is required.
        self.drive_file_ids = drive_file_ids

    def validate(self):
        if self.drive_file_ids:
            for v1 in self.drive_file_ids:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['drive_file_ids'] = []
        if self.drive_file_ids is not None:
            for k1 in self.drive_file_ids:
                result['drive_file_ids'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.drive_file_ids = []
        if m.get('drive_file_ids') is not None:
            for k1 in m.get('drive_file_ids'):
                temp_model = main_models.InvestigateFileRequestDriveFileIds()
                self.drive_file_ids.append(temp_model.from_map(k1))

        return self

class InvestigateFileRequestDriveFileIds(DaraModel):
    def __init__(
        self,
        drive_id: str = None,
        file_id: str = None,
    ):
        # This parameter is required.
        self.drive_id = drive_id
        # This parameter is required.
        self.file_id = file_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id

        if self.file_id is not None:
            result['file_id'] = self.file_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')

        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')

        return self

