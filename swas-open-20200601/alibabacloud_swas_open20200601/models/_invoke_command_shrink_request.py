# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class InvokeCommandShrinkRequest(DaraModel):
    def __init__(
        self,
        command_id: str = None,
        instance_ids: str = None,
        parameters_shrink: str = None,
        region_id: str = None,
        username: str = None,
    ):
        # The command ID. You can call the DescribeCommands operation to query all available command IDs.
        # 
        # This parameter is required.
        self.command_id = command_id
        # The IDs of the simple application servers. The value can be a JSON array that consists of up to 50 IDs of simple application servers. Separate multiple IDs with commas (,).
        # 
        # This parameter is required.
        self.instance_ids = instance_ids
        # The key-value pairs of custom parameters to specify when the custom parameter feature is enabled.
        # 
        # *   You can specify up to 10 custom parameters. Each key in a Map collection cannot be an empty string and can be up to 64 characters in length.
        # *   Values in a Map collection can be empty strings. The total length of the custom parameters and the original command cannot exceed 18 KB after they are encoded in Base64.
        # *   The custom parameter names that you specify for the Parameters parameter must be included in the custom parameter names that you specified when you created the command.
        # *   You can use empty strings to represent the custom parameters that are not specified. If you want to disable the custom parameter feature, you can leave this parameter empty.
        self.parameters_shrink = parameters_shrink
        # The region ID. You can call the [ListRegions](https://help.aliyun.com/document_detail/189315.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The name of the user who runs the command in a simple application server. The username cannot exceed 255 characters in length.
        # 
        # *   For Linux servers, the default value is the root username.
        # *   For Windows servers, the default value is the system username.
        # 
        # You can change the user to run the command only for Linux simple application servers.
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.command_id is not None:
            result['CommandId'] = self.command_id

        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.parameters_shrink is not None:
            result['Parameters'] = self.parameters_shrink

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.username is not None:
            result['Username'] = self.username

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommandId') is not None:
            self.command_id = m.get('CommandId')

        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('Parameters') is not None:
            self.parameters_shrink = m.get('Parameters')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Username') is not None:
            self.username = m.get('Username')

        return self

