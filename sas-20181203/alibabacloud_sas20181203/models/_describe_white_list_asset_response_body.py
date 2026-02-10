# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeWhiteListAssetResponseBody(DaraModel):
    def __init__(
        self,
        assets: List[main_models.DescribeWhiteListAssetResponseBodyAssets] = None,
        request_id: str = None,
    ):
        # The information about the servers.
        self.assets = assets
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.assets:
            for v1 in self.assets:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Assets'] = []
        if self.assets is not None:
            for k1 in self.assets:
                result['Assets'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.assets = []
        if m.get('Assets') is not None:
            for k1 in m.get('Assets'):
                temp_model = main_models.DescribeWhiteListAssetResponseBodyAssets()
                self.assets.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeWhiteListAssetResponseBodyAssets(DaraModel):
    def __init__(
        self,
        allow_selected: int = None,
        group_id: int = None,
        id: int = None,
        machine_ip: str = None,
        machine_name: str = None,
        selected: int = None,
        uuid: str = None,
    ):
        # Indicates whether the server can be selected. Valid values:
        # 
        # *   **0**: no
        # *   **1**: yes
        self.allow_selected = allow_selected
        # The group ID of the server.
        self.group_id = group_id
        # The ID of the server.
        self.id = id
        # The IP address of the server.
        self.machine_ip = machine_ip
        # The name of the server.
        self.machine_name = machine_name
        # Indicates whether the server is selected. Valid values:
        # 
        # *   **0**: no
        # *   **1**: yes
        self.selected = selected
        # The UUID of the server.
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allow_selected is not None:
            result['AllowSelected'] = self.allow_selected

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.id is not None:
            result['Id'] = self.id

        if self.machine_ip is not None:
            result['MachineIp'] = self.machine_ip

        if self.machine_name is not None:
            result['MachineName'] = self.machine_name

        if self.selected is not None:
            result['Selected'] = self.selected

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowSelected') is not None:
            self.allow_selected = m.get('AllowSelected')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('MachineIp') is not None:
            self.machine_ip = m.get('MachineIp')

        if m.get('MachineName') is not None:
            self.machine_name = m.get('MachineName')

        if m.get('Selected') is not None:
            self.selected = m.get('Selected')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

