# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_yundun_bastionhost20191209 import models as main_models
from darabonba.model import DaraModel

class ListApproveCommandsResponseBody(DaraModel):
    def __init__(
        self,
        approve_commands: List[main_models.ListApproveCommandsResponseBodyApproveCommands] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The commands to be reviewed.
        self.approve_commands = approve_commands
        # The request ID.
        self.request_id = request_id
        # The total number of commands to be reviewed.
        self.total_count = total_count

    def validate(self):
        if self.approve_commands:
            for v1 in self.approve_commands:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ApproveCommands'] = []
        if self.approve_commands is not None:
            for k1 in self.approve_commands:
                result['ApproveCommands'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.approve_commands = []
        if m.get('ApproveCommands') is not None:
            for k1 in m.get('ApproveCommands'):
                temp_model = main_models.ListApproveCommandsResponseBodyApproveCommands()
                self.approve_commands.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListApproveCommandsResponseBodyApproveCommands(DaraModel):
    def __init__(
        self,
        approve_command_id: str = None,
        asset_account_name: str = None,
        asset_ip: str = None,
        asset_name: str = None,
        client_ip: str = None,
        client_user: str = None,
        command: str = None,
        create_time: str = None,
        protocol_name: str = None,
        session_id: str = None,
        state: str = None,
    ):
        # The ID of the command to be reviewed.
        self.approve_command_id = approve_command_id
        # The username of the asset account that is used for O\\&M.
        self.asset_account_name = asset_account_name
        # The IP address of the asset for O\\&M.
        self.asset_ip = asset_ip
        # The name of the asset.
        self.asset_name = asset_name
        # The source IP address from which the application is submitted.
        self.client_ip = client_ip
        # The Bastionhost user who submitted the O\\&M application.
        self.client_user = client_user
        # The command to be reviewed.
        self.command = command
        # The time when the O\\&M application was submitted. The value is a UNIX timestamp. Unit: seconds.
        self.create_time = create_time
        # The O\\&M protocol.
        self.protocol_name = protocol_name
        # The ID of the O\\&M session that triggered the review.
        self.session_id = session_id
        # The status of the review. Valid values: **Wait**: The command is pending review.
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.approve_command_id is not None:
            result['ApproveCommandId'] = self.approve_command_id

        if self.asset_account_name is not None:
            result['AssetAccountName'] = self.asset_account_name

        if self.asset_ip is not None:
            result['AssetIp'] = self.asset_ip

        if self.asset_name is not None:
            result['AssetName'] = self.asset_name

        if self.client_ip is not None:
            result['ClientIp'] = self.client_ip

        if self.client_user is not None:
            result['ClientUser'] = self.client_user

        if self.command is not None:
            result['Command'] = self.command

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.protocol_name is not None:
            result['ProtocolName'] = self.protocol_name

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        if self.state is not None:
            result['State'] = self.state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApproveCommandId') is not None:
            self.approve_command_id = m.get('ApproveCommandId')

        if m.get('AssetAccountName') is not None:
            self.asset_account_name = m.get('AssetAccountName')

        if m.get('AssetIp') is not None:
            self.asset_ip = m.get('AssetIp')

        if m.get('AssetName') is not None:
            self.asset_name = m.get('AssetName')

        if m.get('ClientIp') is not None:
            self.client_ip = m.get('ClientIp')

        if m.get('ClientUser') is not None:
            self.client_user = m.get('ClientUser')

        if m.get('Command') is not None:
            self.command = m.get('Command')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('ProtocolName') is not None:
            self.protocol_name = m.get('ProtocolName')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        if m.get('State') is not None:
            self.state = m.get('State')

        return self

