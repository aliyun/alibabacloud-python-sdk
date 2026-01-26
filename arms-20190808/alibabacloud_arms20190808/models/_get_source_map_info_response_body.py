# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_arms20190808 import models as main_models
from darabonba.model import DaraModel

class GetSourceMapInfoResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        source_map_list: List[main_models.GetSourceMapInfoResponseBodySourceMapList] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The details of the SourceMap file.
        self.source_map_list = source_map_list

    def validate(self):
        if self.source_map_list:
            for v1 in self.source_map_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['SourceMapList'] = []
        if self.source_map_list is not None:
            for k1 in self.source_map_list:
                result['SourceMapList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.source_map_list = []
        if m.get('SourceMapList') is not None:
            for k1 in m.get('SourceMapList'):
                temp_model = main_models.GetSourceMapInfoResponseBodySourceMapList()
                self.source_map_list.append(temp_model.from_map(k1))

        return self

class GetSourceMapInfoResponseBodySourceMapList(DaraModel):
    def __init__(
        self,
        fid: str = None,
        file_name: str = None,
        size: str = None,
        upload_time: str = None,
        version: str = None,
    ):
        # The ID of the SourceMap file.
        self.fid = fid
        # The name of the SourceMap file.
        self.file_name = file_name
        # The size of the file. Unit: KB.
        self.size = size
        # The timestamp that indicates when the file was uploaded.
        self.upload_time = upload_time
        # The version of the file.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.fid is not None:
            result['Fid'] = self.fid

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.size is not None:
            result['Size'] = self.size

        if self.upload_time is not None:
            result['UploadTime'] = self.upload_time

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Fid') is not None:
            self.fid = m.get('Fid')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('UploadTime') is not None:
            self.upload_time = m.get('UploadTime')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

