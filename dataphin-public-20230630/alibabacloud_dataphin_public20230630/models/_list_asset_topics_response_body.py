# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class ListAssetTopicsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListAssetTopicsResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The backend response code.
        self.code = code
        # The paginated result of asset topics.
        self.data = data
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The details of the backend exception.
        self.message = message
        # Id of the request
        self.request_id = request_id
        # Indicates whether the request was successful.
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

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

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
            temp_model = main_models.ListAssetTopicsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListAssetTopicsResponseBodyData(DaraModel):
    def __init__(
        self,
        topic_list: List[main_models.ListAssetTopicsResponseBodyDataTopicList] = None,
        total_count: int = None,
    ):
        # The list of topics.
        self.topic_list = topic_list
        # The total number of records that match the query conditions.
        self.total_count = total_count

    def validate(self):
        if self.topic_list:
            for v1 in self.topic_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['TopicList'] = []
        if self.topic_list is not None:
            for k1 in self.topic_list:
                result['TopicList'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.topic_list = []
        if m.get('TopicList') is not None:
            for k1 in m.get('TopicList'):
                temp_model = main_models.ListAssetTopicsResponseBodyDataTopicList()
                self.topic_list.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListAssetTopicsResponseBodyDataTopicList(DaraModel):
    def __init__(
        self,
        asset_type: str = None,
        modify_time: str = None,
        owners: List[main_models.ListAssetTopicsResponseBodyDataTopicListOwners] = None,
        topic_description: str = None,
        topic_id: int = None,
        topic_name: str = None,
        visibility_type: str = None,
        visible_user_groups: List[main_models.ListAssetTopicsResponseBodyDataTopicListVisibleUserGroups] = None,
        visible_users: List[main_models.ListAssetTopicsResponseBodyDataTopicListVisibleUsers] = None,
    ):
        # The asset type.
        self.asset_type = asset_type
        # The last modified time.
        self.modify_time = modify_time
        # The topic administrators.
        self.owners = owners
        # The topic description.
        self.topic_description = topic_description
        # The topic ID.
        self.topic_id = topic_id
        # The topic name.
        self.topic_name = topic_name
        # The visibility scope. Valid values: PUBLIC, SPECIFIED.
        self.visibility_type = visibility_type
        # The explicitly visible user groups. Returns null for PUBLIC topics.
        self.visible_user_groups = visible_user_groups
        # The explicitly visible users. Returns null for PUBLIC topics.
        self.visible_users = visible_users

    def validate(self):
        if self.owners:
            for v1 in self.owners:
                 if v1:
                    v1.validate()
        if self.visible_user_groups:
            for v1 in self.visible_user_groups:
                 if v1:
                    v1.validate()
        if self.visible_users:
            for v1 in self.visible_users:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.asset_type is not None:
            result['AssetType'] = self.asset_type

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        result['Owners'] = []
        if self.owners is not None:
            for k1 in self.owners:
                result['Owners'].append(k1.to_map() if k1 else None)

        if self.topic_description is not None:
            result['TopicDescription'] = self.topic_description

        if self.topic_id is not None:
            result['TopicId'] = self.topic_id

        if self.topic_name is not None:
            result['TopicName'] = self.topic_name

        if self.visibility_type is not None:
            result['VisibilityType'] = self.visibility_type

        result['VisibleUserGroups'] = []
        if self.visible_user_groups is not None:
            for k1 in self.visible_user_groups:
                result['VisibleUserGroups'].append(k1.to_map() if k1 else None)

        result['VisibleUsers'] = []
        if self.visible_users is not None:
            for k1 in self.visible_users:
                result['VisibleUsers'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssetType') is not None:
            self.asset_type = m.get('AssetType')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        self.owners = []
        if m.get('Owners') is not None:
            for k1 in m.get('Owners'):
                temp_model = main_models.ListAssetTopicsResponseBodyDataTopicListOwners()
                self.owners.append(temp_model.from_map(k1))

        if m.get('TopicDescription') is not None:
            self.topic_description = m.get('TopicDescription')

        if m.get('TopicId') is not None:
            self.topic_id = m.get('TopicId')

        if m.get('TopicName') is not None:
            self.topic_name = m.get('TopicName')

        if m.get('VisibilityType') is not None:
            self.visibility_type = m.get('VisibilityType')

        self.visible_user_groups = []
        if m.get('VisibleUserGroups') is not None:
            for k1 in m.get('VisibleUserGroups'):
                temp_model = main_models.ListAssetTopicsResponseBodyDataTopicListVisibleUserGroups()
                self.visible_user_groups.append(temp_model.from_map(k1))

        self.visible_users = []
        if m.get('VisibleUsers') is not None:
            for k1 in m.get('VisibleUsers'):
                temp_model = main_models.ListAssetTopicsResponseBodyDataTopicListVisibleUsers()
                self.visible_users.append(temp_model.from_map(k1))

        return self

class ListAssetTopicsResponseBodyDataTopicListVisibleUsers(DaraModel):
    def __init__(
        self,
        user_id: str = None,
        user_name: str = None,
    ):
        # The user ID.
        self.user_id = user_id
        # The username.
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.user_name is not None:
            result['UserName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

class ListAssetTopicsResponseBodyDataTopicListVisibleUserGroups(DaraModel):
    def __init__(
        self,
        user_group_id: str = None,
        user_group_name: str = None,
    ):
        # The user group ID.
        self.user_group_id = user_group_id
        # The user group name.
        self.user_group_name = user_group_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id

        if self.user_group_name is not None:
            result['UserGroupName'] = self.user_group_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')

        if m.get('UserGroupName') is not None:
            self.user_group_name = m.get('UserGroupName')

        return self

class ListAssetTopicsResponseBodyDataTopicListOwners(DaraModel):
    def __init__(
        self,
        user_id: str = None,
        user_name: str = None,
    ):
        # The user ID.
        self.user_id = user_id
        # The username.
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.user_name is not None:
            result['UserName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

