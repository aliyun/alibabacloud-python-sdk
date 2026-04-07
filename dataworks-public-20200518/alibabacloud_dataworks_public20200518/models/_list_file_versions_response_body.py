# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20200518 import models as main_models
from darabonba.model import DaraModel

class ListFileVersionsResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ListFileVersionsResponseBodyData = None,
        error_code: str = None,
        error_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The file versions.
        self.data = data
        # The error code returned.
        self.error_code = error_code
        # The error message returned.
        self.error_message = error_message
        # The HTTP status code returned.
        self.http_status_code = http_status_code
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request is successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.ListFileVersionsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListFileVersionsResponseBodyData(DaraModel):
    def __init__(
        self,
        file_versions: List[main_models.ListFileVersionsResponseBodyDataFileVersions] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The details of file versions.
        self.file_versions = file_versions
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.file_versions:
            for v1 in self.file_versions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['FileVersions'] = []
        if self.file_versions is not None:
            for k1 in self.file_versions:
                result['FileVersions'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.file_versions = []
        if m.get('FileVersions') is not None:
            for k1 in m.get('FileVersions'):
                temp_model = main_models.ListFileVersionsResponseBodyDataFileVersions()
                self.file_versions.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListFileVersionsResponseBodyDataFileVersions(DaraModel):
    def __init__(
        self,
        change_type: str = None,
        comment: str = None,
        commit_time: int = None,
        commit_user: str = None,
        file_content: str = None,
        file_name: str = None,
        file_property_content: str = None,
        file_version: int = None,
        is_current_prod: bool = None,
        node_content: str = None,
        node_id: int = None,
        status: str = None,
        use_type: str = None,
    ):
        # The type of the change to the file of the current version. Valid values: CREATE, UPDATE, and DELETE.
        self.change_type = change_type
        # The description of the file version.
        self.comment = comment
        # The time when the file version was created. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.commit_time = commit_time
        # The ID of the Alibaba Cloud account used to create the file of the current version.
        self.commit_user = commit_user
        # The code in the file of the current version.
        self.file_content = file_content
        # The name of the file of the current version.
        self.file_name = file_name
        # The basic information about the file of the current version.
        self.file_property_content = file_property_content
        # The version of the file.
        self.file_version = file_version
        # Indicates whether the file version is the same as the latest file version in the production environment.
        self.is_current_prod = is_current_prod
        # The scheduling configurations for the node that corresponds to the file of the current version.
        self.node_content = node_content
        # The ID of the auto triggered node that corresponds to the file of the current version.
        self.node_id = node_id
        # The status of the file of the current version. Valid values: COMMITTING, COMMITTED, CHECK_OK, PACKAGED, DEPLOYING, DEPLOYED, and CANCELLED.
        self.status = status
        # The functional module to which the file belongs. Valid values: NORMAL, MANUAL, MANUAL_BIZ, SKIP, ADHOCQUERY, and COMPONENT. The value SKIP indicates that the node corresponding to the file is run in dry-run mode.
        self.use_type = use_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.change_type is not None:
            result['ChangeType'] = self.change_type

        if self.comment is not None:
            result['Comment'] = self.comment

        if self.commit_time is not None:
            result['CommitTime'] = self.commit_time

        if self.commit_user is not None:
            result['CommitUser'] = self.commit_user

        if self.file_content is not None:
            result['FileContent'] = self.file_content

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.file_property_content is not None:
            result['FilePropertyContent'] = self.file_property_content

        if self.file_version is not None:
            result['FileVersion'] = self.file_version

        if self.is_current_prod is not None:
            result['IsCurrentProd'] = self.is_current_prod

        if self.node_content is not None:
            result['NodeContent'] = self.node_content

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.status is not None:
            result['Status'] = self.status

        if self.use_type is not None:
            result['UseType'] = self.use_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChangeType') is not None:
            self.change_type = m.get('ChangeType')

        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('CommitTime') is not None:
            self.commit_time = m.get('CommitTime')

        if m.get('CommitUser') is not None:
            self.commit_user = m.get('CommitUser')

        if m.get('FileContent') is not None:
            self.file_content = m.get('FileContent')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('FilePropertyContent') is not None:
            self.file_property_content = m.get('FilePropertyContent')

        if m.get('FileVersion') is not None:
            self.file_version = m.get('FileVersion')

        if m.get('IsCurrentProd') is not None:
            self.is_current_prod = m.get('IsCurrentProd')

        if m.get('NodeContent') is not None:
            self.node_content = m.get('NodeContent')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UseType') is not None:
            self.use_type = m.get('UseType')

        return self

