# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class GetAdHocFileResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        file_info: main_models.GetAdHocFileResponseBodyFileInfo = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.file_info = file_info
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.file_info:
            self.file_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.file_info is not None:
            result['FileInfo'] = self.file_info.to_map()

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('FileInfo') is not None:
            temp_model = main_models.GetAdHocFileResponseBodyFileInfo()
            self.file_info = temp_model.from_map(m.get('FileInfo'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetAdHocFileResponseBodyFileInfo(DaraModel):
    def __init__(
        self,
        content: str = None,
        creator: str = None,
        directory: str = None,
        id: int = None,
        last_modifier: str = None,
        name: str = None,
        project_id: int = None,
    ):
        self.content = content
        self.creator = creator
        self.directory = directory
        self.id = id
        self.last_modifier = last_modifier
        self.name = name
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.creator is not None:
            result['Creator'] = self.creator

        if self.directory is not None:
            result['Directory'] = self.directory

        if self.id is not None:
            result['Id'] = self.id

        if self.last_modifier is not None:
            result['LastModifier'] = self.last_modifier

        if self.name is not None:
            result['Name'] = self.name

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('Creator') is not None:
            self.creator = m.get('Creator')

        if m.get('Directory') is not None:
            self.directory = m.get('Directory')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('LastModifier') is not None:
            self.last_modifier = m.get('LastModifier')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        return self

