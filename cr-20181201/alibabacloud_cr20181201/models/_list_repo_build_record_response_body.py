# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cr20181201 import models as main_models
from darabonba.model import DaraModel

class ListRepoBuildRecordResponseBody(DaraModel):
    def __init__(
        self,
        build_records: List[main_models.ListRepoBuildRecordResponseBodyBuildRecords] = None,
        code: str = None,
        is_success: bool = None,
        page_no: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: str = None,
    ):
        # The list of image building records.
        self.build_records = build_records
        # The return value.
        self.code = code
        # Indicates whether the request is successful. Valid values:
        # 
        # *   `true`: The request is successful.
        # *   `false`: The request fails.
        self.is_success = is_success
        # The page number of the returned page.
        self.page_no = page_no
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The total number of returned entries.
        self.total_count = total_count

    def validate(self):
        if self.build_records:
            for v1 in self.build_records:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['BuildRecords'] = []
        if self.build_records is not None:
            for k1 in self.build_records:
                result['BuildRecords'].append(k1.to_map() if k1 else None)

        if self.code is not None:
            result['Code'] = self.code

        if self.is_success is not None:
            result['IsSuccess'] = self.is_success

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.build_records = []
        if m.get('BuildRecords') is not None:
            for k1 in m.get('BuildRecords'):
                temp_model = main_models.ListRepoBuildRecordResponseBodyBuildRecords()
                self.build_records.append(temp_model.from_map(k1))

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListRepoBuildRecordResponseBodyBuildRecords(DaraModel):
    def __init__(
        self,
        build_record_id: str = None,
        build_status: str = None,
        end_time: str = None,
        image: main_models.ListRepoBuildRecordResponseBodyBuildRecordsImage = None,
        start_time: str = None,
    ):
        # The ID of the image building record.
        self.build_record_id = build_record_id
        # The status of the image building.
        self.build_status = build_status
        # The time when the image building ended.
        self.end_time = end_time
        # The information about the image.
        self.image = image
        # The time when the image building started.
        self.start_time = start_time

    def validate(self):
        if self.image:
            self.image.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.build_record_id is not None:
            result['BuildRecordId'] = self.build_record_id

        if self.build_status is not None:
            result['BuildStatus'] = self.build_status

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.image is not None:
            result['Image'] = self.image.to_map()

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BuildRecordId') is not None:
            self.build_record_id = m.get('BuildRecordId')

        if m.get('BuildStatus') is not None:
            self.build_status = m.get('BuildStatus')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Image') is not None:
            temp_model = main_models.ListRepoBuildRecordResponseBodyBuildRecordsImage()
            self.image = temp_model.from_map(m.get('Image'))

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

class ListRepoBuildRecordResponseBodyBuildRecordsImage(DaraModel):
    def __init__(
        self,
        image_tag: str = None,
        repo_id: str = None,
        repo_name: str = None,
        repo_namespace_name: str = None,
    ):
        # The tag of the image.
        self.image_tag = image_tag
        # The ID of the repository.
        self.repo_id = repo_id
        # The name of the repository.
        self.repo_name = repo_name
        # The name of the namespace to which the repository belongs.
        self.repo_namespace_name = repo_namespace_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image_tag is not None:
            result['ImageTag'] = self.image_tag

        if self.repo_id is not None:
            result['RepoId'] = self.repo_id

        if self.repo_name is not None:
            result['RepoName'] = self.repo_name

        if self.repo_namespace_name is not None:
            result['RepoNamespaceName'] = self.repo_namespace_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageTag') is not None:
            self.image_tag = m.get('ImageTag')

        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')

        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')

        if m.get('RepoNamespaceName') is not None:
            self.repo_namespace_name = m.get('RepoNamespaceName')

        return self

