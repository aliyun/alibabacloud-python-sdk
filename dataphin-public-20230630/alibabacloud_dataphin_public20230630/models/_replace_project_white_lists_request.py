# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class ReplaceProjectWhiteListsRequest(DaraModel):
    def __init__(
        self,
        id: int = None,
        op_tenant_id: int = None,
        replace_command: main_models.ReplaceProjectWhiteListsRequestReplaceCommand = None,
    ):
        # This parameter is required.
        self.id = id
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # This parameter is required.
        self.replace_command = replace_command

    def validate(self):
        if self.replace_command:
            self.replace_command.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        if self.replace_command is not None:
            result['ReplaceCommand'] = self.replace_command.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('ReplaceCommand') is not None:
            temp_model = main_models.ReplaceProjectWhiteListsRequestReplaceCommand()
            self.replace_command = temp_model.from_map(m.get('ReplaceCommand'))

        return self

class ReplaceProjectWhiteListsRequestReplaceCommand(DaraModel):
    def __init__(
        self,
        white_lists: List[main_models.ReplaceProjectWhiteListsRequestReplaceCommandWhiteLists] = None,
    ):
        # This parameter is required.
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
        result['WhiteLists'] = []
        if self.white_lists is not None:
            for k1 in self.white_lists:
                result['WhiteLists'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.white_lists = []
        if m.get('WhiteLists') is not None:
            for k1 in m.get('WhiteLists'):
                temp_model = main_models.ReplaceProjectWhiteListsRequestReplaceCommandWhiteLists()
                self.white_lists.append(temp_model.from_map(k1))

        return self

class ReplaceProjectWhiteListsRequestReplaceCommandWhiteLists(DaraModel):
    def __init__(
        self,
        description: str = None,
        ip: str = None,
        port: str = None,
    ):
        self.description = description
        # ip
        # 
        # This parameter is required.
        self.ip = ip
        # This parameter is required.
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

