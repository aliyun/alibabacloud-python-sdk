# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_green20220926 import models as main_models
from darabonba.model import DaraModel

class OssCheckResultListResponseBody(DaraModel):
    def __init__(
        self,
        auth_status: str = None,
        current_page: int = None,
        items: List[main_models.OssCheckResultListResponseBodyItems] = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # Backend-assigned ID, used to uniquely identify a request. Can be used for troubleshooting.
        self.auth_status = auth_status
        # Page size.
        self.current_page = current_page
        # Current page number.
        self.items = items
        # Total number of records.
        self.page_size = page_size
        # Task status.
        self.request_id = request_id
        # Authorization status.
        self.total_count = total_count

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
        if self.auth_status is not None:
            result['AuthStatus'] = self.auth_status

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthStatus') is not None:
            self.auth_status = m.get('AuthStatus')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.OssCheckResultListResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class OssCheckResultListResponseBodyItems(DaraModel):
    def __init__(
        self,
        bucket: str = None,
        code: str = None,
        content_type: str = None,
        copy_from: str = None,
        image_url: str = None,
        is_copy: bool = None,
        job_name: str = None,
        labels: List[str] = None,
        labels_2: List[str] = None,
        md_5: str = None,
        msg: str = None,
        object: str = None,
        scan_result: str = None,
        service_code: str = None,
        service_name: str = None,
        task_id: str = None,
        url: str = None,
    ):
        # Data of the current page.
        self.bucket = bucket
        # Service code.
        self.code = code
        # Primary service.
        self.content_type = content_type
        # Whether to copy.
        self.copy_from = copy_from
        # Details of the result.
        self.image_url = image_url
        # Service name.
        self.is_copy = is_copy
        # Image URL.
        self.job_name = job_name
        # Further description of the error code.
        self.labels = labels
        # Job name.
        self.labels_2 = labels_2
        # Object name.
        self.md_5 = md_5
        # Status code. 200 indicates success.
        self.msg = msg
        # OSS Bucket name.
        self.object = object
        # Image labels.
        self.scan_result = scan_result
        # File MD5.
        self.service_code = service_code
        # Task ID.
        self.service_name = service_name
        # Task URL.
        self.task_id = task_id
        # Text labels.
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bucket is not None:
            result['Bucket'] = self.bucket

        if self.code is not None:
            result['Code'] = self.code

        if self.content_type is not None:
            result['ContentType'] = self.content_type

        if self.copy_from is not None:
            result['CopyFrom'] = self.copy_from

        if self.image_url is not None:
            result['ImageUrl'] = self.image_url

        if self.is_copy is not None:
            result['IsCopy'] = self.is_copy

        if self.job_name is not None:
            result['JobName'] = self.job_name

        if self.labels is not None:
            result['Labels'] = self.labels

        if self.labels_2 is not None:
            result['Labels2'] = self.labels_2

        if self.md_5 is not None:
            result['Md5'] = self.md_5

        if self.msg is not None:
            result['Msg'] = self.msg

        if self.object is not None:
            result['Object'] = self.object

        if self.scan_result is not None:
            result['ScanResult'] = self.scan_result

        if self.service_code is not None:
            result['ServiceCode'] = self.service_code

        if self.service_name is not None:
            result['ServiceName'] = self.service_name

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')

        if m.get('CopyFrom') is not None:
            self.copy_from = m.get('CopyFrom')

        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')

        if m.get('IsCopy') is not None:
            self.is_copy = m.get('IsCopy')

        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')

        if m.get('Labels') is not None:
            self.labels = m.get('Labels')

        if m.get('Labels2') is not None:
            self.labels_2 = m.get('Labels2')

        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')

        if m.get('Msg') is not None:
            self.msg = m.get('Msg')

        if m.get('Object') is not None:
            self.object = m.get('Object')

        if m.get('ScanResult') is not None:
            self.scan_result = m.get('ScanResult')

        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')

        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

