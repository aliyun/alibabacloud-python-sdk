# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetCoordinateTicketRequest(DaraModel):
    def __init__(
        self,
        co_id: str = None,
        end_user_id: str = None,
        region_id: str = None,
        task_id: str = None,
        user_type: str = None,
    ):
        # The ID of the stream collaboration. You can obtain the value of this parameter based on the value of `Coid` that is returned by the `ApplyCoordinationForMonitoring` operation.
        # 
        # This parameter is required.
        self.co_id = co_id
        # The name of the convenience user account. If you initiate the request as an administrator, you do not need to specify this parameter.
        self.end_user_id = end_user_id
        # The region ID. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/436773.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the cloud computer connection task. The first time you initiate the request, you do not need to specify the ID of the cloud computer connection task. If no ticket is returned after you initiate the first request, you must specify the value of taskId that is returned for the first request in the subsequent request.
        self.task_id = task_id
        # The type of the user.
        # 
        # Set the value to TENANT_ADMIN.
        # 
        # *   The value of
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     TENANT_ADMIN
        # 
        #     <!-- -->
        # 
        #     specifies an administrator.
        # 
        # This parameter is required.
        self.user_type = user_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.co_id is not None:
            result['CoId'] = self.co_id

        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.user_type is not None:
            result['UserType'] = self.user_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CoId') is not None:
            self.co_id = m.get('CoId')

        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')

        return self

