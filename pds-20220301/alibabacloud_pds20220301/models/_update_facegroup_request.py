# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateFacegroupRequest(DaraModel):
    def __init__(
        self,
        drive_id: str = None,
        group_cover_face_id: str = None,
        group_id: str = None,
        group_name: str = None,
        remarks: str = None,
    ):
        # The drive ID.
        # 
        # This parameter is required.
        self.drive_id = drive_id
        # The face ID of the thumbnail of the face-based group. You can obtain the face ID from the **image_media_metadata** parameter in the returned results of the GetFile, ListFile, or SearchFile operation.
        self.group_cover_face_id = group_cover_face_id
        # The ID of the face-based group. You can call the ListFacegroups operation to query the group ID.
        # 
        # This parameter is required.
        self.group_id = group_id
        # The name of the face-based group. The name can be up to 128 characters in length.
        self.group_name = group_name
        # The remarks. The remarks can be up to 128 characters in length.
        self.remarks = remarks

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id

        if self.group_cover_face_id is not None:
            result['group_cover_face_id'] = self.group_cover_face_id

        if self.group_id is not None:
            result['group_id'] = self.group_id

        if self.group_name is not None:
            result['group_name'] = self.group_name

        if self.remarks is not None:
            result['remarks'] = self.remarks

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')

        if m.get('group_cover_face_id') is not None:
            self.group_cover_face_id = m.get('group_cover_face_id')

        if m.get('group_id') is not None:
            self.group_id = m.get('group_id')

        if m.get('group_name') is not None:
            self.group_name = m.get('group_name')

        if m.get('remarks') is not None:
            self.remarks = m.get('remarks')

        return self

