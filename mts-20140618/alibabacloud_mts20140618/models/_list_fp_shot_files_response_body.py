# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mts20140618 import models as main_models
from darabonba.model import DaraModel

class ListFpShotFilesResponseBody(DaraModel):
    def __init__(
        self,
        fp_shot_file_list: main_models.ListFpShotFilesResponseBodyFpShotFileList = None,
        next_page_token: str = None,
        request_id: str = None,
    ):
        self.fp_shot_file_list = fp_shot_file_list
        # The returned value of NextPageToken is a pagination token, which can be used in the next request to retrieve a new page of results.
        self.next_page_token = next_page_token
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.fp_shot_file_list:
            self.fp_shot_file_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.fp_shot_file_list is not None:
            result['FpShotFileList'] = self.fp_shot_file_list.to_map()

        if self.next_page_token is not None:
            result['NextPageToken'] = self.next_page_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FpShotFileList') is not None:
            temp_model = main_models.ListFpShotFilesResponseBodyFpShotFileList()
            self.fp_shot_file_list = temp_model.from_map(m.get('FpShotFileList'))

        if m.get('NextPageToken') is not None:
            self.next_page_token = m.get('NextPageToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListFpShotFilesResponseBodyFpShotFileList(DaraModel):
    def __init__(
        self,
        fp_shot_file: List[main_models.ListFpShotFilesResponseBodyFpShotFileListFpShotFile] = None,
    ):
        self.fp_shot_file = fp_shot_file

    def validate(self):
        if self.fp_shot_file:
            for v1 in self.fp_shot_file:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['FpShotFile'] = []
        if self.fp_shot_file is not None:
            for k1 in self.fp_shot_file:
                result['FpShotFile'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.fp_shot_file = []
        if m.get('FpShotFile') is not None:
            for k1 in m.get('FpShotFile'):
                temp_model = main_models.ListFpShotFilesResponseBodyFpShotFileListFpShotFile()
                self.fp_shot_file.append(temp_model.from_map(k1))

        return self

class ListFpShotFilesResponseBodyFpShotFileListFpShotFile(DaraModel):
    def __init__(
        self,
        file_id: str = None,
        input_file: main_models.ListFpShotFilesResponseBodyFpShotFileListFpShotFileInputFile = None,
        primary_key: str = None,
        store_time: str = None,
    ):
        self.file_id = file_id
        self.input_file = input_file
        self.primary_key = primary_key
        self.store_time = store_time

    def validate(self):
        if self.input_file:
            self.input_file.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_id is not None:
            result['FileId'] = self.file_id

        if self.input_file is not None:
            result['InputFile'] = self.input_file.to_map()

        if self.primary_key is not None:
            result['PrimaryKey'] = self.primary_key

        if self.store_time is not None:
            result['StoreTime'] = self.store_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')

        if m.get('InputFile') is not None:
            temp_model = main_models.ListFpShotFilesResponseBodyFpShotFileListFpShotFileInputFile()
            self.input_file = temp_model.from_map(m.get('InputFile'))

        if m.get('PrimaryKey') is not None:
            self.primary_key = m.get('PrimaryKey')

        if m.get('StoreTime') is not None:
            self.store_time = m.get('StoreTime')

        return self

class ListFpShotFilesResponseBodyFpShotFileListFpShotFileInputFile(DaraModel):
    def __init__(
        self,
        bucket: str = None,
        location: str = None,
        object: str = None,
    ):
        self.bucket = bucket
        self.location = location
        self.object = object

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bucket is not None:
            result['Bucket'] = self.bucket

        if self.location is not None:
            result['Location'] = self.location

        if self.object is not None:
            result['Object'] = self.object

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')

        if m.get('Location') is not None:
            self.location = m.get('Location')

        if m.get('Object') is not None:
            self.object = m.get('Object')

        return self

