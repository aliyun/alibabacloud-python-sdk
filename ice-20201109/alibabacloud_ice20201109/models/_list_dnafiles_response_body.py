# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class ListDNAFilesResponseBody(DaraModel):
    def __init__(
        self,
        file_list: List[main_models.ListDNAFilesResponseBodyFileList] = None,
        next_page_token: str = None,
        request_id: str = None,
    ):
        # The queried files.
        self.file_list = file_list
        # A pagination token. It can be used in the next request to retrieve a new page of results.
        self.next_page_token = next_page_token
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.file_list:
            for v1 in self.file_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['FileList'] = []
        if self.file_list is not None:
            for k1 in self.file_list:
                result['FileList'].append(k1.to_map() if k1 else None)

        if self.next_page_token is not None:
            result['NextPageToken'] = self.next_page_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.file_list = []
        if m.get('FileList') is not None:
            for k1 in m.get('FileList'):
                temp_model = main_models.ListDNAFilesResponseBodyFileList()
                self.file_list.append(temp_model.from_map(k1))

        if m.get('NextPageToken') is not None:
            self.next_page_token = m.get('NextPageToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListDNAFilesResponseBodyFileList(DaraModel):
    def __init__(
        self,
        input_file: main_models.ListDNAFilesResponseBodyFileListInputFile = None,
        primary_key: str = None,
    ):
        # The Object Storage Service (OSS) information about the input file.
        self.input_file = input_file
        # The primary key of the file.
        self.primary_key = primary_key

    def validate(self):
        if self.input_file:
            self.input_file.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.input_file is not None:
            result['InputFile'] = self.input_file.to_map()

        if self.primary_key is not None:
            result['PrimaryKey'] = self.primary_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InputFile') is not None:
            temp_model = main_models.ListDNAFilesResponseBodyFileListInputFile()
            self.input_file = temp_model.from_map(m.get('InputFile'))

        if m.get('PrimaryKey') is not None:
            self.primary_key = m.get('PrimaryKey')

        return self

class ListDNAFilesResponseBodyFileListInputFile(DaraModel):
    def __init__(
        self,
        bucket: str = None,
        location: str = None,
        object: str = None,
    ):
        # The name of the OSS bucket in which the input file is stored.
        self.bucket = bucket
        # The OSS region in which the input file resides.
        self.location = location
        # The name of the OSS object that is used as the input file.
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

