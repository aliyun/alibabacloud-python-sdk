# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bssopenapi20171214 import models as main_models
from darabonba.model import DaraModel

class QueryPermissionListResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.QueryPermissionListResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The status code returned.
        self.code = code
        # The data returned.
        self.data = data
        # The message returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request is successful.
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
            temp_model = main_models.QueryPermissionListResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryPermissionListResponseBodyData(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        master_id: int = None,
        member_id: int = None,
        permission_list: List[main_models.QueryPermissionListResponseBodyDataPermissionList] = None,
        relation_type: str = None,
        setup_time: str = None,
        start_time: str = None,
        state: str = None,
    ):
        # The time when the relationship expired. If no value is returned, the relationship is still valid.
        self.end_time = end_time
        # The ID of the management account.
        self.master_id = master_id
        # The ID of the member.
        self.member_id = member_id
        # The list of permissions.
        self.permission_list = permission_list
        # The type of the relationship. Valid values: FinancialManagement and FinancialTrusteeship.
        self.relation_type = relation_type
        # The time when the relationship was established. The time follows the ISO 8601 standard in the yyyy-MM-ddThh:mm:ssZ format. The time is displayed in UTC. For example, 2016-05-23T12:00:00Z indicates that the relationship was established at 20:00:00 on May 23, 2016 (UTC+8).
        self.setup_time = setup_time
        # The time when the relationship took effect. The time follows the ISO 8601 standard in the yyyy-MM-ddThh:mm:ssZ format. The time is displayed in UTC. For example, 2016-05-23T12:00:00Z indicates that the relationship took effect at 20:00:00 on May 23, 2016 (UTC+8).
        self.start_time = start_time
        # The status of the relationship. For more information about valid values of this parameter, see the enumeration values of the RelationshipStatusEnum type in the following table.
        self.state = state

    def validate(self):
        if self.permission_list:
            for v1 in self.permission_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.master_id is not None:
            result['MasterId'] = self.master_id

        if self.member_id is not None:
            result['MemberId'] = self.member_id

        result['PermissionList'] = []
        if self.permission_list is not None:
            for k1 in self.permission_list:
                result['PermissionList'].append(k1.to_map() if k1 else None)

        if self.relation_type is not None:
            result['RelationType'] = self.relation_type

        if self.setup_time is not None:
            result['SetupTime'] = self.setup_time

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.state is not None:
            result['State'] = self.state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('MasterId') is not None:
            self.master_id = m.get('MasterId')

        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')

        self.permission_list = []
        if m.get('PermissionList') is not None:
            for k1 in m.get('PermissionList'):
                temp_model = main_models.QueryPermissionListResponseBodyDataPermissionList()
                self.permission_list.append(temp_model.from_map(k1))

        if m.get('RelationType') is not None:
            self.relation_type = m.get('RelationType')

        if m.get('SetupTime') is not None:
            self.setup_time = m.get('SetupTime')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('State') is not None:
            self.state = m.get('State')

        return self

class QueryPermissionListResponseBodyDataPermissionList(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        permission_code: str = None,
        permission_name: str = None,
        start_time: str = None,
    ):
        # The time when the permission expired. If no value is returned, the permission is still valid. The time follows the ISO 8601 standard in the yyyy-MM-ddThh:mm:ssZ format. The time is displayed in UTC. For example, 2016-05-23T12:00:00Z indicates that the permission expired at 20:00:00 on May 23, 2016 (UTC+8).
        self.end_time = end_time
        # The code of the permission.
        self.permission_code = permission_code
        # The name of the permission.
        self.permission_name = permission_name
        # The time when the permission took effect. The time follows the ISO 8601 standard in the yyyy-MM-ddThh:mm:ssZ format. The time is displayed in UTC. For example, 2016-05-23T12:00:00Z indicates that the permission took effect at 20:00:00 on May 23, 2016 (UTC+8).
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.permission_code is not None:
            result['PermissionCode'] = self.permission_code

        if self.permission_name is not None:
            result['PermissionName'] = self.permission_name

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('PermissionCode') is not None:
            self.permission_code = m.get('PermissionCode')

        if m.get('PermissionName') is not None:
            self.permission_name = m.get('PermissionName')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

