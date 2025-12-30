# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class GetProjectResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        project_info: main_models.GetProjectResponseBodyProjectInfo = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.project_info = project_info
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.project_info:
            self.project_info.validate()

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

        if self.project_info is not None:
            result['ProjectInfo'] = self.project_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

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

        if m.get('ProjectInfo') is not None:
            temp_model = main_models.GetProjectResponseBodyProjectInfo()
            self.project_info = temp_model.from_map(m.get('ProjectInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetProjectResponseBodyProjectInfo(DaraModel):
    def __init__(
        self,
        biz_unit_display_name: str = None,
        biz_unit_id: int = None,
        compute_source_id: int = None,
        compute_source_name: str = None,
        description: str = None,
        display_name: str = None,
        env: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        mode: str = None,
        name: str = None,
        name_space_tag: str = None,
        owner: str = None,
        owner_name: str = None,
        stream_compute_source_id: int = None,
        stream_compute_source_name: str = None,
        type: str = None,
        white_lists: List[main_models.GetProjectResponseBodyProjectInfoWhiteLists] = None,
    ):
        self.biz_unit_display_name = biz_unit_display_name
        self.biz_unit_id = biz_unit_id
        self.compute_source_id = compute_source_id
        self.compute_source_name = compute_source_name
        self.description = description
        self.display_name = display_name
        self.env = env
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.mode = mode
        self.name = name
        self.name_space_tag = name_space_tag
        self.owner = owner
        self.owner_name = owner_name
        self.stream_compute_source_id = stream_compute_source_id
        self.stream_compute_source_name = stream_compute_source_name
        self.type = type
        self.white_lists = white_lists

    def validate(self):
        if self.white_lists:
            for v1 in self.white_lists:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_unit_display_name is not None:
            result['BizUnitDisplayName'] = self.biz_unit_display_name

        if self.biz_unit_id is not None:
            result['BizUnitId'] = self.biz_unit_id

        if self.compute_source_id is not None:
            result['ComputeSourceId'] = self.compute_source_id

        if self.compute_source_name is not None:
            result['ComputeSourceName'] = self.compute_source_name

        if self.description is not None:
            result['Description'] = self.description

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.env is not None:
            result['Env'] = self.env

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.id is not None:
            result['Id'] = self.id

        if self.mode is not None:
            result['Mode'] = self.mode

        if self.name is not None:
            result['Name'] = self.name

        if self.name_space_tag is not None:
            result['NameSpaceTag'] = self.name_space_tag

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.owner_name is not None:
            result['OwnerName'] = self.owner_name

        if self.stream_compute_source_id is not None:
            result['StreamComputeSourceId'] = self.stream_compute_source_id

        if self.stream_compute_source_name is not None:
            result['StreamComputeSourceName'] = self.stream_compute_source_name

        if self.type is not None:
            result['Type'] = self.type

        result['WhiteLists'] = []
        if self.white_lists is not None:
            for k1 in self.white_lists:
                result['WhiteLists'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizUnitDisplayName') is not None:
            self.biz_unit_display_name = m.get('BizUnitDisplayName')

        if m.get('BizUnitId') is not None:
            self.biz_unit_id = m.get('BizUnitId')

        if m.get('ComputeSourceId') is not None:
            self.compute_source_id = m.get('ComputeSourceId')

        if m.get('ComputeSourceName') is not None:
            self.compute_source_name = m.get('ComputeSourceName')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('Env') is not None:
            self.env = m.get('Env')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NameSpaceTag') is not None:
            self.name_space_tag = m.get('NameSpaceTag')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('OwnerName') is not None:
            self.owner_name = m.get('OwnerName')

        if m.get('StreamComputeSourceId') is not None:
            self.stream_compute_source_id = m.get('StreamComputeSourceId')

        if m.get('StreamComputeSourceName') is not None:
            self.stream_compute_source_name = m.get('StreamComputeSourceName')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        self.white_lists = []
        if m.get('WhiteLists') is not None:
            for k1 in m.get('WhiteLists'):
                temp_model = main_models.GetProjectResponseBodyProjectInfoWhiteLists()
                self.white_lists.append(temp_model.from_map(k1))

        return self

class GetProjectResponseBodyProjectInfoWhiteLists(DaraModel):
    def __init__(
        self,
        description: str = None,
        ip: str = None,
        port: str = None,
    ):
        self.description = description
        # ip
        self.ip = ip
        self.port = port

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.ip is not None:
            result['Ip'] = self.ip

        if self.port is not None:
            result['Port'] = self.port

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        return self

