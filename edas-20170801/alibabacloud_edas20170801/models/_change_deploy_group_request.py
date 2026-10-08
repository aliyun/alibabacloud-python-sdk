# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ChangeDeployGroupRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        ecc_info: str = None,
        force_status: bool = None,
        group_name: str = None,
    ):
        # The application ID.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The Elastic Compute Container (ECC) ID of the ECS instance whose group you want to change. Call the ListApplicationEcc operation to query the ECC ID of an application. For more information, see [ListApplicationEcc](https://help.aliyun.com/document_detail/199277.html).
        # 
        # > You can change the group for only one ECS instance at a time.
        # 
        # This parameter is required.
        self.ecc_info = ecc_info
        # Specifies whether to force the change when the deployment package version of the ECC is different from the deployment package version of the application group.
        self.force_status = force_status
        # The name of the application group, such as \\`group_a\\` and \\`group_b\\`. The GroupName for the default group is `_DEFAULT_GROUP`. The name can be up to 64 characters long.
        # 
        # This parameter is required.
        self.group_name = group_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.ecc_info is not None:
            result['EccInfo'] = self.ecc_info

        if self.force_status is not None:
            result['ForceStatus'] = self.force_status

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('EccInfo') is not None:
            self.ecc_info = m.get('EccInfo')

        if m.get('ForceStatus') is not None:
            self.force_status = m.get('ForceStatus')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        return self

