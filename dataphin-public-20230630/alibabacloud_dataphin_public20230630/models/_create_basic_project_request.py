# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class CreateBasicProjectRequest(DaraModel):
    def __init__(
        self,
        create_command: main_models.CreateBasicProjectRequestCreateCommand = None,
        op_tenant_id: int = None,
        op_user_id: str = None,
    ):
        # The create command.
        # 
        # This parameter is required.
        self.create_command = create_command
        # The tenant ID.
        # 
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        self.op_user_id = op_user_id

    def validate(self):
        if self.create_command:
            self.create_command.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_command is not None:
            result['CreateCommand'] = self.create_command.to_map()

        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        if self.op_user_id is not None:
            result['OpUserId'] = self.op_user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateCommand') is not None:
            temp_model = main_models.CreateBasicProjectRequestCreateCommand()
            self.create_command = temp_model.from_map(m.get('CreateCommand'))

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('OpUserId') is not None:
            self.op_user_id = m.get('OpUserId')

        return self

class CreateBasicProjectRequestCreateCommand(DaraModel):
    def __init__(
        self,
        biz_unit_id: int = None,
        compute_source_id: int = None,
        description: str = None,
        display_name: str = None,
        name: str = None,
        name_space_tag: str = None,
        stream_compute_source_id: int = None,
        type: str = None,
        white_lists: List[main_models.CreateBasicProjectRequestCreateCommandWhiteLists] = None,
    ):
        # The business unit ID.
        self.biz_unit_id = biz_unit_id
        # The offline compute source ID.
        self.compute_source_id = compute_source_id
        # The project description.
        self.description = description
        # The project display name.
        self.display_name = display_name
        # The project name.
        # 
        # This parameter is required.
        self.name = name
        # The namespace identifier.
        self.name_space_tag = name_space_tag
        # The real-time compute source ID.
        self.stream_compute_source_id = stream_compute_source_id
        # The project type. If this parameter is left empty, the default value GENERAL is used.
        self.type = type
        # The sandbox whitelist.
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
        if self.biz_unit_id is not None:
            result['BizUnitId'] = self.biz_unit_id

        if self.compute_source_id is not None:
            result['ComputeSourceId'] = self.compute_source_id

        if self.description is not None:
            result['Description'] = self.description

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.name is not None:
            result['Name'] = self.name

        if self.name_space_tag is not None:
            result['NameSpaceTag'] = self.name_space_tag

        if self.stream_compute_source_id is not None:
            result['StreamComputeSourceId'] = self.stream_compute_source_id

        if self.type is not None:
            result['Type'] = self.type

        result['WhiteLists'] = []
        if self.white_lists is not None:
            for k1 in self.white_lists:
                result['WhiteLists'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizUnitId') is not None:
            self.biz_unit_id = m.get('BizUnitId')

        if m.get('ComputeSourceId') is not None:
            self.compute_source_id = m.get('ComputeSourceId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NameSpaceTag') is not None:
            self.name_space_tag = m.get('NameSpaceTag')

        if m.get('StreamComputeSourceId') is not None:
            self.stream_compute_source_id = m.get('StreamComputeSourceId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        self.white_lists = []
        if m.get('WhiteLists') is not None:
            for k1 in m.get('WhiteLists'):
                temp_model = main_models.CreateBasicProjectRequestCreateCommandWhiteLists()
                self.white_lists.append(temp_model.from_map(k1))

        return self

class CreateBasicProjectRequestCreateCommandWhiteLists(DaraModel):
    def __init__(
        self,
        description: str = None,
        ip: str = None,
        port: str = None,
    ):
        # The description.
        self.description = description
        # IP
        self.ip = ip
        # The port.
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

