# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class FaceThumbnail(DaraModel):
    def __init__(
        self,
        face_group_id: str = None,
        face_id: str = None,
        face_thumbnail: str = None,
    ):
        # The ID of the group to which the face belongs.
        # 
        # The following specific IDs are included:
        # 
        # *   figure-cluster-id-independent: The face does not belong to a group. When you perform face clustering after an image is added to the dataset, this face may be grouped.
        # *   figure-cluster-id-unavailable: No clustering has been performed on this face. In other words, no face clustering is performed after an image is added to the dataset.
        self.face_group_id = face_group_id
        # The face ID.
        self.face_id = face_id
        # The thumbnail of the face.
        self.face_thumbnail = face_thumbnail

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.face_group_id is not None:
            result['face_group_id'] = self.face_group_id

        if self.face_id is not None:
            result['face_id'] = self.face_id

        if self.face_thumbnail is not None:
            result['face_thumbnail'] = self.face_thumbnail

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('face_group_id') is not None:
            self.face_group_id = m.get('face_group_id')

        if m.get('face_id') is not None:
            self.face_id = m.get('face_id')

        if m.get('face_thumbnail') is not None:
            self.face_thumbnail = m.get('face_thumbnail')

        return self

