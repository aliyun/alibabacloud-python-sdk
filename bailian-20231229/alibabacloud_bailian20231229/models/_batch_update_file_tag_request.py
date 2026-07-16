# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bailian20231229 import models as main_models
from darabonba.model import DaraModel

class BatchUpdateFileTagRequest(DaraModel):
    def __init__(
        self,
        file_infos: List[main_models.BatchUpdateFileTagRequestFileInfos] = None,
        update_mode: str = None,
    ):
        # A list of files to update.
        # 
        # This parameter is required.
        self.file_infos = file_infos
        # The update mode. Valid values are APPEND and OVERWRITE.
        self.update_mode = update_mode

    def validate(self):
        if self.file_infos:
            for v1 in self.file_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['FileInfos'] = []
        if self.file_infos is not None:
            for k1 in self.file_infos:
                result['FileInfos'].append(k1.to_map() if k1 else None)

        if self.update_mode is not None:
            result['UpdateMode'] = self.update_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.file_infos = []
        if m.get('FileInfos') is not None:
            for k1 in m.get('FileInfos'):
                temp_model = main_models.BatchUpdateFileTagRequestFileInfos()
                self.file_infos.append(temp_model.from_map(k1))

        if m.get('UpdateMode') is not None:
            self.update_mode = m.get('UpdateMode')

        return self

class BatchUpdateFileTagRequestFileInfos(DaraModel):
    def __init__(
        self,
        file_id: str = None,
        tags: List[str] = None,
    ):
        # The file ID. To get this ID, go to the <props="china">[application data](https://bailian.console.aliyun.com/?tab=app#/data-center)<props="intl">[application data](https://modelstudio.console.alibabacloud.com/?tab=app#/data-center) page and click the ID icon next to the file name.
        # 
        # This parameter is required.
        self.file_id = file_id
        # - A list of up to 100 tags to associate with the file. The total length of all tags cannot exceed 700 characters.
        # 
        # This parameter is required.
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_id is not None:
            result['FileId'] = self.file_id

        if self.tags is not None:
            result['tags'] = self.tags

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')

        if m.get('tags') is not None:
            self.tags = m.get('tags')

        return self

