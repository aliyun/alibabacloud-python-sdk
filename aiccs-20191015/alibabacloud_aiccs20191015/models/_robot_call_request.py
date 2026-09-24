# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RobotCallRequest(DaraModel):
    def __init__(
        self,
        called_number: str = None,
        called_show_number: str = None,
        early_media_asr: bool = None,
        out_id: str = None,
        owner_id: int = None,
        params: str = None,
        record_flag: bool = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        robot_id: int = None,
    ):
        # The called number.
        # 
        # This parameter is required.
        self.called_number = called_number
        # The caller number for the outbound call. You can view this number on the [Real Number Management](https://dyvmsnext.console.aliyun.com/number/list/normal) page of the voice messaging service.
        # 
        # This parameter is required.
        self.called_show_number = called_show_number
        # Specifies whether to enable the number status identification feature. Valid values:
        # 
        # - **false** (default): Disabled.
        # - **true**: Enabled.
        # >After this feature is enabled, the reason why a call is not answered is recorded.
        self.early_media_asr = early_media_asr
        # The ID reserved for the caller. This ID is returned to the caller through a receipt message. The value is 1 to 15 bytes in length.
        self.out_id = out_id
        self.owner_id = owner_id
        # The parameter list of the robot in JSON format. The total length cannot exceed 512 bytes. You can view the parameters on the [Script Management](https://aiccs.console.aliyun.com/patter/list) > **Details** > **Input/Output Parameters** page or by calling the [ListRobotParams](https://help.aliyun.com/document_detail/2717999.html) operation.
        self.params = params
        # Specifies whether to record the call. Valid values:
        # 
        # - **false** (default): Do not record.
        # - **true**: Record.
        self.record_flag = record_flag
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The robot ID, which is the script ID. You can view approved script IDs on the [Script Management](https://aiccs.console.aliyun.com/patter/list) page.
        # 
        # This parameter is required.
        self.robot_id = robot_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.called_number is not None:
            result['CalledNumber'] = self.called_number

        if self.called_show_number is not None:
            result['CalledShowNumber'] = self.called_show_number

        if self.early_media_asr is not None:
            result['EarlyMediaAsr'] = self.early_media_asr

        if self.out_id is not None:
            result['OutId'] = self.out_id

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.params is not None:
            result['Params'] = self.params

        if self.record_flag is not None:
            result['RecordFlag'] = self.record_flag

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.robot_id is not None:
            result['RobotId'] = self.robot_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CalledNumber') is not None:
            self.called_number = m.get('CalledNumber')

        if m.get('CalledShowNumber') is not None:
            self.called_show_number = m.get('CalledShowNumber')

        if m.get('EarlyMediaAsr') is not None:
            self.early_media_asr = m.get('EarlyMediaAsr')

        if m.get('OutId') is not None:
            self.out_id = m.get('OutId')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Params') is not None:
            self.params = m.get('Params')

        if m.get('RecordFlag') is not None:
            self.record_flag = m.get('RecordFlag')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('RobotId') is not None:
            self.robot_id = m.get('RobotId')

        return self

