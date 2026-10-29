# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vs20181212 import models as main_models
from darabonba.model import DaraModel

class ListFilesResponseBody(DaraModel):
    def __init__(
        self,
        files: List[main_models.ListFilesResponseBodyFiles] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The list of file information.
        self.files = files
        # The page number of the returned list.
        self.page_number = page_number
        # The Settings for the number of entries per page during paging in a paged query.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The total number of matched file records.
        self.total_count = total_count

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

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.files = []
        if m.get('Files') is not None:
            for k1 in m.get('Files'):
                temp_model = main_models.ListFilesResponseBodyFiles()
                self.files.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListFilesResponseBodyFiles(DaraModel):
    def __init__(
        self,
        description: str = None,
        file_id: str = None,
        file_name: str = None,
        status: str = None,
        status_description: str = None,
        target_path: str = None,
        update_time: str = None,
        upload_time: str = None,
    ):
        # The description of the file.
        self.description = description
        # The ID of the file.
        self.file_id = file_id
        # The name of the file.
        self.file_name = file_name
        # The upload status of the file. Valid values:
        # - Created
        # - Doing
        # - Success: final state
        # - Failed: final state
        self.status = status
        # The description of the status.
        self.status_description = status_description
        # The target path for pushing the file to the cloud application service instance.
        self.target_path = target_path
        # The time when the status was last updated. The time follows the ISO 8601 standard and includes the time zone offset in the YYYY-MM-DDTHH:mm:ss+HH:mm format.
        self.update_time = update_time
        # The time when the upload started. The time follows the ISO 8601 standard and includes the time zone offset in the YYYY-MM-DDTHH:mm:ss+HH:mm format.
        self.upload_time = upload_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.file_id is not None:
            result['FileId'] = self.file_id

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.status is not None:
            result['Status'] = self.status

        if self.status_description is not None:
            result['StatusDescription'] = self.status_description

        if self.target_path is not None:
            result['TargetPath'] = self.target_path

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.upload_time is not None:
            result['UploadTime'] = self.upload_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StatusDescription') is not None:
            self.status_description = m.get('StatusDescription')

        if m.get('TargetPath') is not None:
            self.target_path = m.get('TargetPath')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('UploadTime') is not None:
            self.upload_time = m.get('UploadTime')

        return self

