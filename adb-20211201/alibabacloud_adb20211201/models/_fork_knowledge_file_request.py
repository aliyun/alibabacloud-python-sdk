# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ForkKnowledgeFileRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        file_id: str = None,
        file_location: str = None,
        tags: str = None,
        upload_user: str = None,
    ):
        # The ADB instance ID.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The ID of the knowledge base file. You must specify either this parameter or FileLocation, but not both. Use a decimal positive integer string without leading zeros. Valid values: 1 to 9223372036854775807.
        self.file_id = file_id
        # The address of a single file in the knowledge base. You must specify either this parameter or FileId, but not both. You cannot specify a directory. The address must uniquely locate an active file.
        self.file_location = file_location
        # The initial business tags for the new record. Use a JSON string of a JSON object or an array of tag_key/tag_value objects. If omitted, the source tags are not inherited.
        self.tags = tags
        # The initial authorized user for the new record. You can pass a JSON string of a single user identifier or a user array. If omitted, no initial user authorization is applied, and the source authorization is not inherited.
        self.upload_user = upload_user

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.file_id is not None:
            result['FileId'] = self.file_id

        if self.file_location is not None:
            result['FileLocation'] = self.file_location

        if self.tags is not None:
            result['Tags'] = self.tags

        if self.upload_user is not None:
            result['UploadUser'] = self.upload_user

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')

        if m.get('FileLocation') is not None:
            self.file_location = m.get('FileLocation')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('UploadUser') is not None:
            self.upload_user = m.get('UploadUser')

        return self

