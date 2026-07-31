# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddKnowledgeFileRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        file_location: str = None,
        file_type: str = None,
        is_dir: bool = None,
        tags: str = None,
        upload_user: str = None,
    ):
        # The ID of the AnalyticDB for MySQL cluster.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The file address. Currently, only OSS paths are supported.
        # 
        # This parameter is required.
        self.file_location = file_location
        # The file type.
        self.file_type = file_type
        # Specifies whether the file is a folder.
        self.is_dir = is_dir
        # The file tags in JSON format.
        self.tags = tags
        # The user who uploads the knowledge base file.
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

        if self.file_location is not None:
            result['FileLocation'] = self.file_location

        if self.file_type is not None:
            result['FileType'] = self.file_type

        if self.is_dir is not None:
            result['IsDir'] = self.is_dir

        if self.tags is not None:
            result['Tags'] = self.tags

        if self.upload_user is not None:
            result['UploadUser'] = self.upload_user

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('FileLocation') is not None:
            self.file_location = m.get('FileLocation')

        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')

        if m.get('IsDir') is not None:
            self.is_dir = m.get('IsDir')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('UploadUser') is not None:
            self.upload_user = m.get('UploadUser')

        return self

