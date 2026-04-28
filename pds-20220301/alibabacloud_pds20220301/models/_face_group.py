# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_pds20220301 import models as main_models
from darabonba.model import DaraModel

class FaceGroup(DaraModel):
    def __init__(
        self,
        created_at: str = None,
        group_cover_face_boundary: main_models.FaceGroupGroupCoverFaceBoundary = None,
        group_cover_file_id: str = None,
        group_cover_height: int = None,
        group_cover_url: str = None,
        group_cover_width: int = None,
        group_id: str = None,
        group_name: str = None,
        image_count: int = None,
        remarks: str = None,
        updated_at: str = None,
    ):
        # The time when the face-based group was generated.
        self.created_at = created_at
        # The border of the image used as the cover the face-based group.
        self.group_cover_face_boundary = group_cover_face_boundary
        # The ID of the file used as the cover of the face-based group.
        self.group_cover_file_id = group_cover_file_id
        # The height of the image used as the cover of the face-based group.
        self.group_cover_height = group_cover_height
        # The URL of the image used as the cover of the face-based group.
        self.group_cover_url = group_cover_url
        # The width of the image used as the cover of the face-based group.
        self.group_cover_width = group_cover_width
        # The ID of the face-based group.
        self.group_id = group_id
        # The name of the face-based group.
        self.group_name = group_name
        # The number of photos in the face-based group.
        self.image_count = image_count
        # The remarks.
        self.remarks = remarks
        # The time when the face-based group was modified.
        self.updated_at = updated_at

    def validate(self):
        if self.group_cover_face_boundary:
            self.group_cover_face_boundary.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_at is not None:
            result['created_at'] = self.created_at

        if self.group_cover_face_boundary is not None:
            result['group_cover_face_boundary'] = self.group_cover_face_boundary.to_map()

        if self.group_cover_file_id is not None:
            result['group_cover_file_id'] = self.group_cover_file_id

        if self.group_cover_height is not None:
            result['group_cover_height'] = self.group_cover_height

        if self.group_cover_url is not None:
            result['group_cover_url'] = self.group_cover_url

        if self.group_cover_width is not None:
            result['group_cover_width'] = self.group_cover_width

        if self.group_id is not None:
            result['group_id'] = self.group_id

        if self.group_name is not None:
            result['group_name'] = self.group_name

        if self.image_count is not None:
            result['image_count'] = self.image_count

        if self.remarks is not None:
            result['remarks'] = self.remarks

        if self.updated_at is not None:
            result['updated_at'] = self.updated_at

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('created_at') is not None:
            self.created_at = m.get('created_at')

        if m.get('group_cover_face_boundary') is not None:
            temp_model = main_models.FaceGroupGroupCoverFaceBoundary()
            self.group_cover_face_boundary = temp_model.from_map(m.get('group_cover_face_boundary'))

        if m.get('group_cover_file_id') is not None:
            self.group_cover_file_id = m.get('group_cover_file_id')

        if m.get('group_cover_height') is not None:
            self.group_cover_height = m.get('group_cover_height')

        if m.get('group_cover_url') is not None:
            self.group_cover_url = m.get('group_cover_url')

        if m.get('group_cover_width') is not None:
            self.group_cover_width = m.get('group_cover_width')

        if m.get('group_id') is not None:
            self.group_id = m.get('group_id')

        if m.get('group_name') is not None:
            self.group_name = m.get('group_name')

        if m.get('image_count') is not None:
            self.image_count = m.get('image_count')

        if m.get('remarks') is not None:
            self.remarks = m.get('remarks')

        if m.get('updated_at') is not None:
            self.updated_at = m.get('updated_at')

        return self

class FaceGroupGroupCoverFaceBoundary(DaraModel):
    def __init__(
        self,
        height: int = None,
        left: int = None,
        top: int = None,
        width: int = None,
    ):
        # The height of the border. Unit: pixel.
        self.height = height
        # The distance from the left side of the photo to the border. Unit: pixel.
        self.left = left
        # The distance from the top of the photo to the border. Unit: pixel.
        self.top = top
        # The width of the border. Unit: pixel.
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.height is not None:
            result['Height'] = self.height

        if self.left is not None:
            result['Left'] = self.left

        if self.top is not None:
            result['Top'] = self.top

        if self.width is not None:
            result['Width'] = self.width

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Height') is not None:
            self.height = m.get('Height')

        if m.get('Left') is not None:
            self.left = m.get('Left')

        if m.get('Top') is not None:
            self.top = m.get('Top')

        if m.get('Width') is not None:
            self.width = m.get('Width')

        return self

