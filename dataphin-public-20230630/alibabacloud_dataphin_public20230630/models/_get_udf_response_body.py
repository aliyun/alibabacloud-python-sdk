# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class GetUdfResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        udf_info: main_models.GetUdfResponseBodyUdfInfo = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.success = success
        self.udf_info = udf_info

    def validate(self):
        if self.udf_info:
            self.udf_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.udf_info is not None:
            result['UdfInfo'] = self.udf_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('UdfInfo') is not None:
            temp_model = main_models.GetUdfResponseBodyUdfInfo()
            self.udf_info = temp_model.from_map(m.get('UdfInfo'))

        return self

class GetUdfResponseBodyUdfInfo(DaraModel):
    def __init__(
        self,
        category: int = None,
        class_name: str = None,
        command_help: str = None,
        compute_engine_type: str = None,
        creator: str = None,
        description: str = None,
        directory: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        last_modifier: str = None,
        name: str = None,
    ):
        self.category = category
        self.class_name = class_name
        self.command_help = command_help
        self.compute_engine_type = compute_engine_type
        self.creator = creator
        self.description = description
        self.directory = directory
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.last_modifier = last_modifier
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.class_name is not None:
            result['ClassName'] = self.class_name

        if self.command_help is not None:
            result['CommandHelp'] = self.command_help

        if self.compute_engine_type is not None:
            result['ComputeEngineType'] = self.compute_engine_type

        if self.creator is not None:
            result['Creator'] = self.creator

        if self.description is not None:
            result['Description'] = self.description

        if self.directory is not None:
            result['Directory'] = self.directory

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.id is not None:
            result['Id'] = self.id

        if self.last_modifier is not None:
            result['LastModifier'] = self.last_modifier

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('ClassName') is not None:
            self.class_name = m.get('ClassName')

        if m.get('CommandHelp') is not None:
            self.command_help = m.get('CommandHelp')

        if m.get('ComputeEngineType') is not None:
            self.compute_engine_type = m.get('ComputeEngineType')

        if m.get('Creator') is not None:
            self.creator = m.get('Creator')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Directory') is not None:
            self.directory = m.get('Directory')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('LastModifier') is not None:
            self.last_modifier = m.get('LastModifier')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

