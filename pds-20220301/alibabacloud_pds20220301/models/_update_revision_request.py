# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateRevisionRequest(DaraModel):
    def __init__(
        self,
        drive_id: str = None,
        file_id: str = None,
        keep_forever: bool = None,
        revision_description: str = None,
        revision_id: str = None,
    ):
        # The drive ID.
        # 
        # This parameter is required.
        self.drive_id = drive_id
        # The file ID.
        # 
        # This parameter is required.
        self.file_id = file_id
        # Specifies whether to permanently retain a version.
        # 
        # By default, this parameter is not specified, which indicates that you do not modify the permanent retention configuration of the version.
        self.keep_forever = keep_forever
        # The description of the version. The description can be up to 1,024 characters in length.
        # 
        # By default, this parameter is not specified, which indicates that you do not modify the description of the version.
        self.revision_description = revision_description
        # The version ID.
        # 
        # This parameter is required.
        self.revision_id = revision_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id

        if self.file_id is not None:
            result['file_id'] = self.file_id

        if self.keep_forever is not None:
            result['keep_forever'] = self.keep_forever

        if self.revision_description is not None:
            result['revision_description'] = self.revision_description

        if self.revision_id is not None:
            result['revision_id'] = self.revision_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')

        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')

        if m.get('keep_forever') is not None:
            self.keep_forever = m.get('keep_forever')

        if m.get('revision_description') is not None:
            self.revision_description = m.get('revision_description')

        if m.get('revision_id') is not None:
            self.revision_id = m.get('revision_id')

        return self

