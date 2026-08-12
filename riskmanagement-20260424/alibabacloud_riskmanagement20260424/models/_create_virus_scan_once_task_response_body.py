# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_riskmanagement20260424 import models as main_models
from darabonba.model import DaraModel

class CreateVirusScanOnceTaskResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.CreateVirusScanOnceTaskResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code returned if the call fails. For more information, refer to error codes.
        self.code = code
        # The returned data.
        self.data = data
        # The message information.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the call is successful. Valid values:
        # 
        # - **true**: The call is successful.                               
        # - **false**: The call fails.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.CreateVirusScanOnceTaskResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class CreateVirusScanOnceTaskResponseBodyData(DaraModel):
    def __init__(
        self,
        business_type: str = None,
        platform: str = None,
        request_id: str = None,
        selection_key: int = None,
        target_type: str = None,
        uuid: str = None,
    ):
        # The asset selection business type. Valid values:
        # 
        # - **VIRUS_SCAN_CYCLE_CONFIG**: virus scan configuration
        # - **VIRUS_SCAN_ONCE_TASK**: virus scan one-time task
        self.business_type = business_type
        # The operating system of the target asset. Valid values:
        # 
        # - **windows**: Windows operating system
        # - **linux**: Linux operating system
        self.platform = platform
        # The request ID.
        self.request_id = request_id
        # The unique identifier of this asset selection, which can be used to query or modify the assets corresponding to this selection.
        self.selection_key = selection_key
        # The target asset type. Valid values:
        # 
        # - **all_instance**: all servers
        # - **instance**: select by server
        # - **group**: select by group
        # - **vpc**: select by VPC
        self.target_type = target_type
        # The server ID.
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.business_type is not None:
            result['BusinessType'] = self.business_type

        if self.platform is not None:
            result['Platform'] = self.platform

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.selection_key is not None:
            result['SelectionKey'] = self.selection_key

        if self.target_type is not None:
            result['TargetType'] = self.target_type

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')

        if m.get('Platform') is not None:
            self.platform = m.get('Platform')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SelectionKey') is not None:
            self.selection_key = m.get('SelectionKey')

        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

