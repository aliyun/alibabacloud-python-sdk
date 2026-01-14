# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_quickbi_public20220101 import models as main_models
from darabonba.model import DaraModel

class GetUserGroupInfoResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[main_models.GetUserGroupInfoResponseBodyResult] = None,
        success: bool = None,
    ):
        # Request ID.
        self.request_id = request_id
        # User group information.
        self.result = result
        # Indicates whether the request was successful. Possible values:
        # 
        # - true: The request was successful.
        # - false: The request failed.
        self.success = success

    def validate(self):
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['Result'].append(k1.to_map() if k1 else None)

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.GetUserGroupInfoResponseBodyResult()
                self.result.append(temp_model.from_map(k1))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetUserGroupInfoResponseBodyResult(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        create_user: str = None,
        identified_path: str = None,
        modified_time: str = None,
        modify_user: str = None,
        parent_usergroup_id: str = None,
        usergroup_desc: str = None,
        usergroup_id: str = None,
        usergroup_name: str = None,
    ):
        # Creation time of the user group.
        self.create_time = create_time
        # Creator of the sub-user group. This is the UserID in Quick BI, not the UID in Alibaba Cloud.
        self.create_user = create_user
        # Directory level of the user group.
        self.identified_path = identified_path
        # Last modified time of the user group.
        self.modified_time = modified_time
        # Modifier of the user group. This is the UserID in Quick BI, not the UID in Alibaba Cloud.
        self.modify_user = modify_user
        # Parent user group ID.
        self.parent_usergroup_id = parent_usergroup_id
        # Description of the user group.
        self.usergroup_desc = usergroup_desc
        # User group ID.
        self.usergroup_id = usergroup_id
        # Name of the user group.
        self.usergroup_name = usergroup_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.create_user is not None:
            result['CreateUser'] = self.create_user

        if self.identified_path is not None:
            result['IdentifiedPath'] = self.identified_path

        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time

        if self.modify_user is not None:
            result['ModifyUser'] = self.modify_user

        if self.parent_usergroup_id is not None:
            result['ParentUsergroupId'] = self.parent_usergroup_id

        if self.usergroup_desc is not None:
            result['UsergroupDesc'] = self.usergroup_desc

        if self.usergroup_id is not None:
            result['UsergroupId'] = self.usergroup_id

        if self.usergroup_name is not None:
            result['UsergroupName'] = self.usergroup_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CreateUser') is not None:
            self.create_user = m.get('CreateUser')

        if m.get('IdentifiedPath') is not None:
            self.identified_path = m.get('IdentifiedPath')

        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')

        if m.get('ModifyUser') is not None:
            self.modify_user = m.get('ModifyUser')

        if m.get('ParentUsergroupId') is not None:
            self.parent_usergroup_id = m.get('ParentUsergroupId')

        if m.get('UsergroupDesc') is not None:
            self.usergroup_desc = m.get('UsergroupDesc')

        if m.get('UsergroupId') is not None:
            self.usergroup_id = m.get('UsergroupId')

        if m.get('UsergroupName') is not None:
            self.usergroup_name = m.get('UsergroupName')

        return self

