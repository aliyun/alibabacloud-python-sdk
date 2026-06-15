# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dm20151123 import models as main_models
from darabonba.model import DaraModel

class ListValidateFileResponseBody(DaraModel):
    def __init__(
        self,
        files: List[main_models.ListValidateFileResponseBodyFiles] = None,
        has_next: bool = None,
        page: int = None,
        page_size: int = None,
        request_id: str = None,
        total_pages: int = None,
        total_size: int = None,
    ):
        # The list of files.
        self.files = files
        # Indicates whether a next page of data exists.
        self.has_next = has_next
        # The page number.
        self.page = page
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of pages.
        self.total_pages = total_pages
        # The total number of entries.
        self.total_size = total_size

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

        if self.has_next is not None:
            result['HasNext'] = self.has_next

        if self.page is not None:
            result['Page'] = self.page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages

        if self.total_size is not None:
            result['TotalSize'] = self.total_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.files = []
        if m.get('Files') is not None:
            for k1 in m.get('Files'):
                temp_model = main_models.ListValidateFileResponseBodyFiles()
                self.files.append(temp_model.from_map(k1))

        if m.get('HasNext') is not None:
            self.has_next = m.get('HasNext')

        if m.get('Page') is not None:
            self.page = m.get('Page')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')

        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')

        return self

class ListValidateFileResponseBodyFiles(DaraModel):
    def __init__(
        self,
        catch_all_num: str = None,
        complete_time: str = None,
        do_not_mail_num: str = None,
        file_id: str = None,
        file_name: str = None,
        invalid_num: str = None,
        is_downloadable: bool = None,
        percentage: str = None,
        processed_num: str = None,
        status: str = None,
        total_num: str = None,
        unknown_num: str = None,
        upload_time: str = None,
        valid_num: str = None,
    ):
        # The number of addresses with the validation result \\"CatchAll\\".
        self.catch_all_num = catch_all_num
        # The time when the task was completed.
        self.complete_time = complete_time
        # The number of addresses with the validation result \\"DoNotMail\\".
        self.do_not_mail_num = do_not_mail_num
        # The file ID.
        self.file_id = file_id
        # The file name.
        self.file_name = file_name
        # The number of addresses with the validation result \\"Invalid\\".
        self.invalid_num = invalid_num
        # Indicates whether the result can be downloaded.
        self.is_downloadable = is_downloadable
        # The task execution progress.
        self.percentage = percentage
        # The number of addresses that have been validated.
        self.processed_num = processed_num
        # The status of the task.
        self.status = status
        # The number of addresses to validate in the task.
        self.total_num = total_num
        # The number of addresses with the validation result \\"Unknown\\".
        self.unknown_num = unknown_num
        # The time when the file was submitted.
        self.upload_time = upload_time
        # The number of addresses with the validation result \\"Valid\\".
        self.valid_num = valid_num

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.catch_all_num is not None:
            result['CatchAllNum'] = self.catch_all_num

        if self.complete_time is not None:
            result['CompleteTime'] = self.complete_time

        if self.do_not_mail_num is not None:
            result['DoNotMailNum'] = self.do_not_mail_num

        if self.file_id is not None:
            result['FileId'] = self.file_id

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.invalid_num is not None:
            result['InvalidNum'] = self.invalid_num

        if self.is_downloadable is not None:
            result['IsDownloadable'] = self.is_downloadable

        if self.percentage is not None:
            result['Percentage'] = self.percentage

        if self.processed_num is not None:
            result['ProcessedNum'] = self.processed_num

        if self.status is not None:
            result['Status'] = self.status

        if self.total_num is not None:
            result['TotalNum'] = self.total_num

        if self.unknown_num is not None:
            result['UnknownNum'] = self.unknown_num

        if self.upload_time is not None:
            result['UploadTime'] = self.upload_time

        if self.valid_num is not None:
            result['ValidNum'] = self.valid_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatchAllNum') is not None:
            self.catch_all_num = m.get('CatchAllNum')

        if m.get('CompleteTime') is not None:
            self.complete_time = m.get('CompleteTime')

        if m.get('DoNotMailNum') is not None:
            self.do_not_mail_num = m.get('DoNotMailNum')

        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('InvalidNum') is not None:
            self.invalid_num = m.get('InvalidNum')

        if m.get('IsDownloadable') is not None:
            self.is_downloadable = m.get('IsDownloadable')

        if m.get('Percentage') is not None:
            self.percentage = m.get('Percentage')

        if m.get('ProcessedNum') is not None:
            self.processed_num = m.get('ProcessedNum')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')

        if m.get('UnknownNum') is not None:
            self.unknown_num = m.get('UnknownNum')

        if m.get('UploadTime') is not None:
            self.upload_time = m.get('UploadTime')

        if m.get('ValidNum') is not None:
            self.valid_num = m.get('ValidNum')

        return self

