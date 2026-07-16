# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class GetFileVersionResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetFileVersionResponseBodyData = None,
        error_code: str = None,
        error_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Version details of the file.
        self.data = data
        # The error code.
        self.error_code = error_code
        # The error message.
        self.error_message = error_message
        # HTTP status code.
        self.http_status_code = http_status_code
        # The unique ID of this request. If an error occurs, you can troubleshoot the issue using this ID.
        self.request_id = request_id
        # Indicates whether the API call succeeded.
        # 
        # - true: Succeeded.
        # 
        # - false: Failed.
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
            temp_model = main_models.GetFileVersionResponseBodyData()
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

class GetFileVersionResponseBodyData(DaraModel):
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
        # The change type of this file version, including CREATE, UPDATE, and DELETE.
        self.change_type = change_type
        # Description of this file version.
        self.comment = comment
        # UNIX timestamp (in milliseconds) when the file version was generated.
        self.commit_time = commit_time
        # User ID of the Alibaba Cloud user who generated this file version.
        self.commit_user = commit_user
        # The code of the file for this version.
        self.file_content = file_content
        # File name used to generate this file version.
        self.file_name = file_name
        # Basic information of the file used to generate this file version.
        self.file_property_content = file_property_content
        # The version of the file.
        self.file_version = file_version
        # Indicates whether this file version is the latest version in the current production environment.
        # 
        # - true: It is the latest version.
        # 
        # - false: It is not the latest version.
        self.is_current_prod = is_current_prod
        # The scan configuration at the time this file version was generated.
        self.node_content = node_content
        # The ID of the scheduling task corresponding to the generation of this file version.
        self.node_id = node_id
        # Current status of the file version. Valid values:
        # 
        # - COMMITTING (Submitting)
        # 
        # - COMMITTED or CHECK_OK (Submitted)
        # 
        # - PACKAGED (Preparing for publish)
        # 
        # - DEPLOYING (In Publish)
        # 
        # - DEPLOYED (Published)
        # 
        # - CANCELLED (Publish canceled)
        self.status = status
        # Function module to which the file belongs. Valid values:
        # 
        # - 0: NORMAL (Data Development)
        # 
        # - 1: MANUAL (one-time task)
        # 
        # - 2: MANUAL_BIZ (manual pipeline)
        # 
        # - 3: SKIP (Dry-Run scheduling in Data Development)
        # 
        # - 10: ADHOCQUERY (Ad Hoc Query)
        # 
        # - 30: COMPONENT (widget Management)
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

