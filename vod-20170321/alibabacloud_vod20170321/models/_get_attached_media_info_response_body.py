# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vod20170321 import models as main_models
from darabonba.model import DaraModel

class GetAttachedMediaInfoResponseBody(DaraModel):
    def __init__(
        self,
        attached_media_list: List[main_models.GetAttachedMediaInfoResponseBodyAttachedMediaList] = None,
        non_exist_media_ids: List[str] = None,
        request_id: str = None,
    ):
        # The information about the media assets.
        self.attached_media_list = attached_media_list
        # The IDs of the auxiliary media assets that do not exist.
        self.non_exist_media_ids = non_exist_media_ids
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.attached_media_list:
            for v1 in self.attached_media_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AttachedMediaList'] = []
        if self.attached_media_list is not None:
            for k1 in self.attached_media_list:
                result['AttachedMediaList'].append(k1.to_map() if k1 else None)

        if self.non_exist_media_ids is not None:
            result['NonExistMediaIds'] = self.non_exist_media_ids

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.attached_media_list = []
        if m.get('AttachedMediaList') is not None:
            for k1 in m.get('AttachedMediaList'):
                temp_model = main_models.GetAttachedMediaInfoResponseBodyAttachedMediaList()
                self.attached_media_list.append(temp_model.from_map(k1))

        if m.get('NonExistMediaIds') is not None:
            self.non_exist_media_ids = m.get('NonExistMediaIds')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetAttachedMediaInfoResponseBodyAttachedMediaList(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        categories: List[main_models.GetAttachedMediaInfoResponseBodyAttachedMediaListCategories] = None,
        creation_time: str = None,
        description: str = None,
        media_id: str = None,
        modification_time: str = None,
        status: str = None,
        storage_location: str = None,
        tags: str = None,
        title: str = None,
        type: str = None,
        url: str = None,
    ):
        # The ID of the application.
        self.app_id = app_id
        # The categories.
        self.categories = categories
        # The time when the auxiliary media asset was created. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.creation_time = creation_time
        # The description of the auxiliary media asset.
        # 
        # >  This parameter is returned only when a description is specified for the auxiliary media asset.
        self.description = description
        # The ID of the auxiliary media asset.
        self.media_id = media_id
        # The time when the auxiliary media asset was last updated. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.modification_time = modification_time
        # The status of the auxiliary media asset. Valid values:
        # 
        # *   **Uploading**
        # *   **Normal**
        # *   **UploadFail**
        self.status = status
        # The storage address of the auxiliary media asset.
        self.storage_location = storage_location
        # The tags of the auxiliary media asset.
        # 
        # >  This parameter is returned only when tags are specified for the auxiliary media asset.
        self.tags = tags
        # The title of the auxiliary media asset.
        self.title = title
        # The type of the auxiliary media asset.
        # 
        # *   **watermark**
        # *   **subtitle**
        # *   **material**
        self.type = type
        # The URL of the auxiliary media asset.
        # 
        # >  If a CDN domain name is specified, a CDN URL is returned. Otherwise, an OSS URL is returned.
        self.url = url

    def validate(self):
        if self.categories:
            for v1 in self.categories:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        result['Categories'] = []
        if self.categories is not None:
            for k1 in self.categories:
                result['Categories'].append(k1.to_map() if k1 else None)

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.description is not None:
            result['Description'] = self.description

        if self.media_id is not None:
            result['MediaId'] = self.media_id

        if self.modification_time is not None:
            result['ModificationTime'] = self.modification_time

        if self.status is not None:
            result['Status'] = self.status

        if self.storage_location is not None:
            result['StorageLocation'] = self.storage_location

        if self.tags is not None:
            result['Tags'] = self.tags

        if self.title is not None:
            result['Title'] = self.title

        if self.type is not None:
            result['Type'] = self.type

        if self.url is not None:
            result['URL'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        self.categories = []
        if m.get('Categories') is not None:
            for k1 in m.get('Categories'):
                temp_model = main_models.GetAttachedMediaInfoResponseBodyAttachedMediaListCategories()
                self.categories.append(temp_model.from_map(k1))

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')

        if m.get('ModificationTime') is not None:
            self.modification_time = m.get('ModificationTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StorageLocation') is not None:
            self.storage_location = m.get('StorageLocation')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('URL') is not None:
            self.url = m.get('URL')

        return self

class GetAttachedMediaInfoResponseBodyAttachedMediaListCategories(DaraModel):
    def __init__(
        self,
        cate_id: int = None,
        cate_name: str = None,
        level: int = None,
        parent_id: int = None,
    ):
        # The ID of the category.
        self.cate_id = cate_id
        # The name of the category.
        self.cate_name = cate_name
        # The level of the category.
        self.level = level
        # The ID of the parent category.
        self.parent_id = parent_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cate_id is not None:
            result['CateId'] = self.cate_id

        if self.cate_name is not None:
            result['CateName'] = self.cate_name

        if self.level is not None:
            result['Level'] = self.level

        if self.parent_id is not None:
            result['ParentId'] = self.parent_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CateId') is not None:
            self.cate_id = m.get('CateId')

        if m.get('CateName') is not None:
            self.cate_name = m.get('CateName')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')

        return self

