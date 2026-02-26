# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from alibabacloud_imm20200930 import models as main_models
from darabonba.model import DaraModel

class FigureCluster(DaraModel):
    def __init__(
        self,
        average_age: float = None,
        cover: main_models.File = None,
        create_time: str = None,
        custom_id: str = None,
        custom_labels: Dict[str, Any] = None,
        dataset_name: str = None,
        face_count: int = None,
        gender: str = None,
        image_count: int = None,
        max_age: float = None,
        meta_lock_version: int = None,
        min_age: float = None,
        name: str = None,
        object_id: str = None,
        object_type: str = None,
        owner_id: str = None,
        project_name: str = None,
        update_time: str = None,
        video_count: int = None,
    ):
        # The average age.
        self.average_age = average_age
        # The cover image.
        self.cover = cover
        # The creation time.
        self.create_time = create_time
        # The custom ID.
        self.custom_id = custom_id
        # The custom labels. You can search for clusters by label.
        self.custom_labels = custom_labels
        # The name of the dataset.
        self.dataset_name = dataset_name
        # The number of faces.
        self.face_count = face_count
        # The gender.
        self.gender = gender
        # The number of images.
        self.image_count = image_count
        # The maximum age.
        self.max_age = max_age
        # The version of the metadata lock. A metadata lock version can be obtained by using a get or list operation. If you include the MetaLockVersion parameter in a request to update the cluster, the server checks consistency between the MetaLockVersion parameter value sent in the request and the one on the server side and updates the cluster only when they are consistent. This parameter prevents update conflicts in concurrent scenarios. The initial version is 0. The version is automatically increased by 1 after each successful update.
        self.meta_lock_version = meta_lock_version
        # The minimum age.
        self.min_age = min_age
        # The name of the cluster.
        self.name = name
        # The ID of the cluster.
        self.object_id = object_id
        # The type of the cluster.
        self.object_type = object_type
        # The user ID.
        self.owner_id = owner_id
        # The name of the project.
        self.project_name = project_name
        # The update time.
        self.update_time = update_time
        # The number of videos.
        self.video_count = video_count

    def validate(self):
        if self.cover:
            self.cover.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.average_age is not None:
            result['AverageAge'] = self.average_age

        if self.cover is not None:
            result['Cover'] = self.cover.to_map()

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.custom_id is not None:
            result['CustomId'] = self.custom_id

        if self.custom_labels is not None:
            result['CustomLabels'] = self.custom_labels

        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name

        if self.face_count is not None:
            result['FaceCount'] = self.face_count

        if self.gender is not None:
            result['Gender'] = self.gender

        if self.image_count is not None:
            result['ImageCount'] = self.image_count

        if self.max_age is not None:
            result['MaxAge'] = self.max_age

        if self.meta_lock_version is not None:
            result['MetaLockVersion'] = self.meta_lock_version

        if self.min_age is not None:
            result['MinAge'] = self.min_age

        if self.name is not None:
            result['Name'] = self.name

        if self.object_id is not None:
            result['ObjectId'] = self.object_id

        if self.object_type is not None:
            result['ObjectType'] = self.object_type

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.video_count is not None:
            result['VideoCount'] = self.video_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AverageAge') is not None:
            self.average_age = m.get('AverageAge')

        if m.get('Cover') is not None:
            temp_model = main_models.File()
            self.cover = temp_model.from_map(m.get('Cover'))

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CustomId') is not None:
            self.custom_id = m.get('CustomId')

        if m.get('CustomLabels') is not None:
            self.custom_labels = m.get('CustomLabels')

        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')

        if m.get('FaceCount') is not None:
            self.face_count = m.get('FaceCount')

        if m.get('Gender') is not None:
            self.gender = m.get('Gender')

        if m.get('ImageCount') is not None:
            self.image_count = m.get('ImageCount')

        if m.get('MaxAge') is not None:
            self.max_age = m.get('MaxAge')

        if m.get('MetaLockVersion') is not None:
            self.meta_lock_version = m.get('MetaLockVersion')

        if m.get('MinAge') is not None:
            self.min_age = m.get('MinAge')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')

        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('VideoCount') is not None:
            self.video_count = m.get('VideoCount')

        return self

