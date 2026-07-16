# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_xtee20210910 import models as main_models
from darabonba.model import DaraModel

class ListSampleResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        current_page: int = None,
        http_status_code: str = None,
        message: str = None,
        page_size: int = None,
        request_id: str = None,
        result_object: List[main_models.ListSampleResponseBodyResultObject] = None,
        total_item: int = None,
        total_page: int = None,
    ):
        # Status code.
        self.code = code
        # Current page number.
        self.current_page = current_page
        # HTTP status code.
        self.http_status_code = http_status_code
        # Error message.
        self.message = message
        # Page size.
        self.page_size = page_size
        # Request ID.
        self.request_id = request_id
        # Return Result.
        self.result_object = result_object
        # Total Number of Returned Items.
        self.total_item = total_item
        # Total number of pages.
        self.total_page = total_page

    def validate(self):
        if self.result_object:
            for v1 in self.result_object:
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

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['ResultObject'] = []
        if self.result_object is not None:
            for k1 in self.result_object:
                result['ResultObject'].append(k1.to_map() if k1 else None)

        if self.total_item is not None:
            result['TotalItem'] = self.total_item

        if self.total_page is not None:
            result['TotalPage'] = self.total_page

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.result_object = []
        if m.get('ResultObject') is not None:
            for k1 in m.get('ResultObject'):
                temp_model = main_models.ListSampleResponseBodyResultObject()
                self.result_object.append(temp_model.from_map(k1))

        if m.get('TotalItem') is not None:
            self.total_item = m.get('TotalItem')

        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')

        return self

class ListSampleResponseBodyResultObject(DaraModel):
    def __init__(
        self,
        file_name: str = None,
        file_size: int = None,
        remark: str = None,
        row_count: int = None,
        sample_id: int = None,
        sample_name: str = None,
        tab: str = None,
        upload_time: str = None,
        upload_user_name: str = None,
    ):
        # File Name.
        self.file_name = file_name
        # File Size. Unit: bytes.
        self.file_size = file_size
        # Remarks.
        self.remark = remark
        # Table Row Count.
        self.row_count = row_count
        # Sample ID.
        self.sample_id = sample_id
        # Sample Name.
        self.sample_name = sample_name
        # Scenario.
        self.tab = tab
        # File Upload Time.
        self.upload_time = upload_time
        # Uploader.
        self.upload_user_name = upload_user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.file_size is not None:
            result['FileSize'] = self.file_size

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.row_count is not None:
            result['RowCount'] = self.row_count

        if self.sample_id is not None:
            result['SampleId'] = self.sample_id

        if self.sample_name is not None:
            result['SampleName'] = self.sample_name

        if self.tab is not None:
            result['Tab'] = self.tab

        if self.upload_time is not None:
            result['UploadTime'] = self.upload_time

        if self.upload_user_name is not None:
            result['UploadUserName'] = self.upload_user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('RowCount') is not None:
            self.row_count = m.get('RowCount')

        if m.get('SampleId') is not None:
            self.sample_id = m.get('SampleId')

        if m.get('SampleName') is not None:
            self.sample_name = m.get('SampleName')

        if m.get('Tab') is not None:
            self.tab = m.get('Tab')

        if m.get('UploadTime') is not None:
            self.upload_time = m.get('UploadTime')

        if m.get('UploadUserName') is not None:
            self.upload_user_name = m.get('UploadUserName')

        return self

