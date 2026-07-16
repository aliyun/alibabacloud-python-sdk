# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aisc20260101 import models as main_models
from darabonba.model import DaraModel

class CreateSkillFileCheckRequest(DaraModel):
    def __init__(
        self,
        files: List[main_models.CreateSkillFileCheckRequestFiles] = None,
    ):
        self.files = files

    def validate(self):
        if self.files:
            for v1 in self.files:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Files'] = []
        if self.files is not None:
            for k1 in self.files:
                result['Files'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.files = []
        if m.get('Files') is not None:
            for k1 in m.get('Files'):
                temp_model = main_models.CreateSkillFileCheckRequestFiles()
                self.files.append(temp_model.from_map(k1))

        return self



class CreateSkillFileCheckRequestFiles(DaraModel):
    def __init__(
        self,
        download_url: str = None,
        file_name: str = None,
    ):
        self.download_url = download_url
        self.file_name = file_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.download_url is not None:
            result['DownloadUrl'] = self.download_url

        if self.file_name is not None:
            result['FileName'] = self.file_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DownloadUrl') is not None:
            self.download_url = m.get('DownloadUrl')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        return self

