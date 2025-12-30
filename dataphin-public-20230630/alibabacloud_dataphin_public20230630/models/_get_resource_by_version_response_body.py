# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class GetResourceByVersionResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        resource_info: main_models.GetResourceByVersionResponseBodyResourceInfo = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.resource_info = resource_info
        self.success = success

    def validate(self):
        if self.resource_info:
            self.resource_info.validate()

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

        if self.resource_info is not None:
            result['ResourceInfo'] = self.resource_info.to_map()

        if self.success is not None:
            result['Success'] = self.success

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

        if m.get('ResourceInfo') is not None:
            temp_model = main_models.GetResourceByVersionResponseBodyResourceInfo()
            self.resource_info = temp_model.from_map(m.get('ResourceInfo'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetResourceByVersionResponseBodyResourceInfo(DaraModel):
    def __init__(
        self,
        compute_engine_type: str = None,
        creator: str = None,
        description: str = None,
        directory: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        last_modifier: str = None,
        name: str = None,
        project_id: int = None,
        resource_type: str = None,
        size: int = None,
        storage_address: str = None,
    ):
        self.compute_engine_type = compute_engine_type
        self.creator = creator
        self.description = description
        self.directory = directory
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.last_modifier = last_modifier
        self.name = name
        self.project_id = project_id
        self.resource_type = resource_type
        self.size = size
        self.storage_address = storage_address

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.size is not None:
            result['Size'] = self.size

        if self.storage_address is not None:
            result['StorageAddress'] = self.storage_address

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('StorageAddress') is not None:
            self.storage_address = m.get('StorageAddress')

        return self

