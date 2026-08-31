# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class ListAssetDirectoriesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListAssetDirectoriesResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The backend response code.
        self.code = code
        # The paginated result of asset topic folders.
        self.data = data
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The backend exception details.
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
            temp_model = main_models.ListAssetDirectoriesResponseBodyData()
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

class ListAssetDirectoriesResponseBodyData(DaraModel):
    def __init__(
        self,
        directory_list: List[main_models.ListAssetDirectoriesResponseBodyDataDirectoryList] = None,
        topic_id: int = None,
        topic_name: str = None,
        total_count: int = None,
    ):
        # The folder list.
        self.directory_list = directory_list
        # The topic ID.
        self.topic_id = topic_id
        # The topic name.
        self.topic_name = topic_name
        # The total number of records that match the conditions.
        self.total_count = total_count

    def validate(self):
        if self.directory_list:
            for v1 in self.directory_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DirectoryList'] = []
        if self.directory_list is not None:
            for k1 in self.directory_list:
                result['DirectoryList'].append(k1.to_map() if k1 else None)

        if self.topic_id is not None:
            result['TopicId'] = self.topic_id

        if self.topic_name is not None:
            result['TopicName'] = self.topic_name

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.directory_list = []
        if m.get('DirectoryList') is not None:
            for k1 in m.get('DirectoryList'):
                temp_model = main_models.ListAssetDirectoriesResponseBodyDataDirectoryList()
                self.directory_list.append(temp_model.from_map(k1))

        if m.get('TopicId') is not None:
            self.topic_id = m.get('TopicId')

        if m.get('TopicName') is not None:
            self.topic_name = m.get('TopicName')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListAssetDirectoriesResponseBodyDataDirectoryList(DaraModel):
    def __init__(
        self,
        directory_description: str = None,
        directory_id: int = None,
        directory_name: str = None,
        full_path: str = None,
        full_path_ids: List[int] = None,
        full_path_names: List[str] = None,
        has_children: bool = None,
        level: int = None,
        modifier: main_models.ListAssetDirectoriesResponseBodyDataDirectoryListModifier = None,
        modify_time: str = None,
        parent_directory_id: int = None,
    ):
        # The folder description.
        self.directory_description = directory_description
        # The folder ID.
        self.directory_id = directory_id
        # The folder name.
        self.directory_name = directory_name
        # The display path.
        self.full_path = full_path
        # The ID path from the top level to the current folder.
        self.full_path_ids = full_path_ids
        # The name path from the top level to the current folder.
        self.full_path_names = full_path_names
        # Indicates whether published direct child folders exist.
        self.has_children = has_children
        # The absolute level of the folder.
        self.level = level
        # The last modifier.
        self.modifier = modifier
        # The last modified time.
        self.modify_time = modify_time
        # The parent folder ID.
        self.parent_directory_id = parent_directory_id

    def validate(self):
        if self.modifier:
            self.modifier.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.directory_description is not None:
            result['DirectoryDescription'] = self.directory_description

        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id

        if self.directory_name is not None:
            result['DirectoryName'] = self.directory_name

        if self.full_path is not None:
            result['FullPath'] = self.full_path

        if self.full_path_ids is not None:
            result['FullPathIds'] = self.full_path_ids

        if self.full_path_names is not None:
            result['FullPathNames'] = self.full_path_names

        if self.has_children is not None:
            result['HasChildren'] = self.has_children

        if self.level is not None:
            result['Level'] = self.level

        if self.modifier is not None:
            result['Modifier'] = self.modifier.to_map()

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.parent_directory_id is not None:
            result['ParentDirectoryId'] = self.parent_directory_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DirectoryDescription') is not None:
            self.directory_description = m.get('DirectoryDescription')

        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')

        if m.get('DirectoryName') is not None:
            self.directory_name = m.get('DirectoryName')

        if m.get('FullPath') is not None:
            self.full_path = m.get('FullPath')

        if m.get('FullPathIds') is not None:
            self.full_path_ids = m.get('FullPathIds')

        if m.get('FullPathNames') is not None:
            self.full_path_names = m.get('FullPathNames')

        if m.get('HasChildren') is not None:
            self.has_children = m.get('HasChildren')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('Modifier') is not None:
            temp_model = main_models.ListAssetDirectoriesResponseBodyDataDirectoryListModifier()
            self.modifier = temp_model.from_map(m.get('Modifier'))

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('ParentDirectoryId') is not None:
            self.parent_directory_id = m.get('ParentDirectoryId')

        return self

class ListAssetDirectoriesResponseBodyDataDirectoryListModifier(DaraModel):
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

