# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class UpdateDevProdProjectRequest(DaraModel):
    def __init__(
        self,
        op_tenant_id: int = None,
        update_command: main_models.UpdateDevProdProjectRequestUpdateCommand = None,
    ):
        # The tenant ID.
        # 
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # The update command.
        # 
        # This parameter is required.
        self.update_command = update_command

    def validate(self):
        if self.update_command:
            self.update_command.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        if self.update_command is not None:
            result['UpdateCommand'] = self.update_command.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('UpdateCommand') is not None:
            temp_model = main_models.UpdateDevProdProjectRequestUpdateCommand()
            self.update_command = temp_model.from_map(m.get('UpdateCommand'))

        return self

class UpdateDevProdProjectRequestUpdateCommand(DaraModel):
    def __init__(
        self,
        biz_unit_id: int = None,
        dev_compute_source_id: int = None,
        dev_description: str = None,
        dev_stream_compute_source_id: int = None,
        display_name: str = None,
        id: int = None,
        name: str = None,
        name_space_tag: str = None,
        prod_compute_source_id: int = None,
        prod_description: str = None,
        prod_stream_compute_source_id: int = None,
        white_lists: List[main_models.UpdateDevProdProjectRequestUpdateCommandWhiteLists] = None,
    ):
        # The business unit ID.
        self.biz_unit_id = biz_unit_id
        # The ID of the offline compute source in the development environment.
        self.dev_compute_source_id = dev_compute_source_id
        # The description of the development environment.
        self.dev_description = dev_description
        # The ID of the real-time compute source in the development environment.
        self.dev_stream_compute_source_id = dev_stream_compute_source_id
        # The display name of the project.
        self.display_name = display_name
        # The project ID.
        # 
        # This parameter is required.
        self.id = id
        # The project name.
        self.name = name
        # The namespace identifier.
        self.name_space_tag = name_space_tag
        # The ID of the offline compute source in the production environment.
        self.prod_compute_source_id = prod_compute_source_id
        # The description of the production environment.
        self.prod_description = prod_description
        # The ID of the real-time compute source in the production environment.
        self.prod_stream_compute_source_id = prod_stream_compute_source_id
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

        if self.dev_compute_source_id is not None:
            result['DevComputeSourceId'] = self.dev_compute_source_id

        if self.dev_description is not None:
            result['DevDescription'] = self.dev_description

        if self.dev_stream_compute_source_id is not None:
            result['DevStreamComputeSourceId'] = self.dev_stream_compute_source_id

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.name_space_tag is not None:
            result['NameSpaceTag'] = self.name_space_tag

        if self.prod_compute_source_id is not None:
            result['ProdComputeSourceId'] = self.prod_compute_source_id

        if self.prod_description is not None:
            result['ProdDescription'] = self.prod_description

        if self.prod_stream_compute_source_id is not None:
            result['ProdStreamComputeSourceId'] = self.prod_stream_compute_source_id

        result['WhiteLists'] = []
        if self.white_lists is not None:
            for k1 in self.white_lists:
                result['WhiteLists'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizUnitId') is not None:
            self.biz_unit_id = m.get('BizUnitId')

        if m.get('DevComputeSourceId') is not None:
            self.dev_compute_source_id = m.get('DevComputeSourceId')

        if m.get('DevDescription') is not None:
            self.dev_description = m.get('DevDescription')

        if m.get('DevStreamComputeSourceId') is not None:
            self.dev_stream_compute_source_id = m.get('DevStreamComputeSourceId')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NameSpaceTag') is not None:
            self.name_space_tag = m.get('NameSpaceTag')

        if m.get('ProdComputeSourceId') is not None:
            self.prod_compute_source_id = m.get('ProdComputeSourceId')

        if m.get('ProdDescription') is not None:
            self.prod_description = m.get('ProdDescription')

        if m.get('ProdStreamComputeSourceId') is not None:
            self.prod_stream_compute_source_id = m.get('ProdStreamComputeSourceId')

        self.white_lists = []
        if m.get('WhiteLists') is not None:
            for k1 in m.get('WhiteLists'):
                temp_model = main_models.UpdateDevProdProjectRequestUpdateCommandWhiteLists()
                self.white_lists.append(temp_model.from_map(k1))

        return self

class UpdateDevProdProjectRequestUpdateCommandWhiteLists(DaraModel):
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

