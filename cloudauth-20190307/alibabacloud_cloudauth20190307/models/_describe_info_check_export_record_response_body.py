# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudauth20190307 import models as main_models
from darabonba.model import DaraModel

class DescribeInfoCheckExportRecordResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        current_page: int = None,
        items: List[main_models.DescribeInfoCheckExportRecordResponseBodyItems] = None,
        message: str = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
        total_page: int = None,
    ):
        self.code = code
        self.current_page = current_page
        self.items = items
        self.message = message
        self.page_size = page_size
        # Id of the request
        self.request_id = request_id
        self.success = success
        self.total_count = total_count
        self.total_page = total_page

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['Message'] = self.message

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.total_page is not None:
            result['TotalPage'] = self.total_page

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.DescribeInfoCheckExportRecordResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')

        return self

class DescribeInfoCheckExportRecordResponseBodyItems(DaraModel):
    def __init__(
        self,
        download_date: str = None,
        download_task_id: str = None,
        error_code: str = None,
        file_name: str = None,
        file_type: str = None,
        product_type: str = None,
        status: int = None,
        url: str = None,
    ):
        self.download_date = download_date
        self.download_task_id = download_task_id
        self.error_code = error_code
        self.file_name = file_name
        self.file_type = file_type
        self.product_type = product_type
        self.status = status
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.download_date is not None:
            result['DownloadDate'] = self.download_date

        if self.download_task_id is not None:
            result['DownloadTaskId'] = self.download_task_id

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.file_type is not None:
            result['FileType'] = self.file_type

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        if self.status is not None:
            result['Status'] = self.status

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DownloadDate') is not None:
            self.download_date = m.get('DownloadDate')

        if m.get('DownloadTaskId') is not None:
            self.download_task_id = m.get('DownloadTaskId')

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

