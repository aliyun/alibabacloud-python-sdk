# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class GetStandardGroupResponseBody(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        standard_group: main_models.GetStandardGroupResponseBodyStandardGroup = None,
        success: bool = None,
    ):
        # The error code that is returned if the request failed.
        self.error_code = error_code
        # The error message that is returned if the request failed.
        self.error_message = error_message
        # The request ID. You can use the ID to query logs and troubleshoot issues.
        self.request_id = request_id
        # The information about the security rule set.
        self.standard_group = standard_group
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**: The request was successful.
        # *   **false**: The request failed.
        self.success = success

    def validate(self):
        if self.standard_group:
            self.standard_group.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.standard_group is not None:
            result['StandardGroup'] = self.standard_group.to_map()

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StandardGroup') is not None:
            temp_model = main_models.GetStandardGroupResponseBodyStandardGroup()
            self.standard_group = temp_model.from_map(m.get('StandardGroup'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetStandardGroupResponseBodyStandardGroup(DaraModel):
    def __init__(
        self,
        db_type: str = None,
        description: str = None,
        group_id: int = None,
        group_mode: str = None,
        group_name: str = None,
        last_mender_id: int = None,
    ):
        # The engine type.
        self.db_type = db_type
        # The description of the security rule set.
        self.description = description
        # The ID of the security rule set.
        self.group_id = group_id
        # The control mode. Valid values:
        # 
        # *   **NONE_CONTROL**: Flexible Management
        # *   **STABLE**: Stable Change
        # *   **COMMON**: Security Collaboration
        self.group_mode = group_mode
        # The name of the security rule set.
        self.group_name = group_name
        # The ID of the user who last modified the security rules.
        self.last_mender_id = last_mender_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.db_type is not None:
            result['DbType'] = self.db_type

        if self.description is not None:
            result['Description'] = self.description

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.group_mode is not None:
            result['GroupMode'] = self.group_mode

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.last_mender_id is not None:
            result['LastMenderId'] = self.last_mender_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('GroupMode') is not None:
            self.group_mode = m.get('GroupMode')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('LastMenderId') is not None:
            self.last_mender_id = m.get('LastMenderId')

        return self

