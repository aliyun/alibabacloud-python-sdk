# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_quickbi_public20220101 import models as main_models
from darabonba.model import DaraModel

class ListByUserGroupIdResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: main_models.ListByUserGroupIdResponseBodyResult = None,
        success: bool = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The user group query result is returned.
        self.result = result
        # Indicates whether the request is successful. Valid values:
        # 
        # *   true: The request was successful.
        # *   false: The request failed.
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result is not None:
            result['Result'] = self.result.to_map()

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            temp_model = main_models.ListByUserGroupIdResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListByUserGroupIdResponseBodyResult(DaraModel):
    def __init__(
        self,
        failed_user_group_ids: List[str] = None,
        user_group_models: List[main_models.ListByUserGroupIdResponseBodyResultUserGroupModels] = None,
    ):
        # List of failed user groups.
        self.failed_user_group_ids = failed_user_group_ids
        # The details of the user group that was queried.
        self.user_group_models = user_group_models

    def validate(self):
        if self.user_group_models:
            for v1 in self.user_group_models:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.failed_user_group_ids is not None:
            result['FailedUserGroupIds'] = self.failed_user_group_ids

        result['UserGroupModels'] = []
        if self.user_group_models is not None:
            for k1 in self.user_group_models:
                result['UserGroupModels'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FailedUserGroupIds') is not None:
            self.failed_user_group_ids = m.get('FailedUserGroupIds')

        self.user_group_models = []
        if m.get('UserGroupModels') is not None:
            for k1 in m.get('UserGroupModels'):
                temp_model = main_models.ListByUserGroupIdResponseBodyResultUserGroupModels()
                self.user_group_models.append(temp_model.from_map(k1))

        return self

class ListByUserGroupIdResponseBodyResultUserGroupModels(DaraModel):
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
        # The time when the Secret was created.
        self.create_time = create_time
        # The UserID of the creator in the Quick BI.
        self.create_user = create_user
        # The path of the user group.
        self.identified_path = identified_path
        # The time when the protection policy was last modified.
        self.modified_time = modified_time
        # The UserID of the modifier in the Quick BI.
        self.modify_user = modify_user
        # The ID of the parent user group.
        self.parent_usergroup_id = parent_usergroup_id
        # The description of the user group.
        self.usergroup_desc = usergroup_desc
        # The ID of the user group.
        self.usergroup_id = usergroup_id
        # The name of the user group.
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

