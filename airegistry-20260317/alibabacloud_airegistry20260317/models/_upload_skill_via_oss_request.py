# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UploadSkillViaOssRequest(DaraModel):
    def __init__(
        self,
        commit_msg: str = None,
        namespace_id: str = None,
        oss_object_name: str = None,
        overwrite: bool = None,
    ):
        self.commit_msg = commit_msg
        # This parameter is required.
        self.namespace_id = namespace_id
        # This parameter is required.
        self.oss_object_name = oss_object_name
        self.overwrite = overwrite

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.commit_msg is not None:
            result['CommitMsg'] = self.commit_msg

        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id

        if self.oss_object_name is not None:
            result['OssObjectName'] = self.oss_object_name

        if self.overwrite is not None:
            result['Overwrite'] = self.overwrite

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommitMsg') is not None:
            self.commit_msg = m.get('CommitMsg')

        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')

        if m.get('OssObjectName') is not None:
            self.oss_object_name = m.get('OssObjectName')

        if m.get('Overwrite') is not None:
            self.overwrite = m.get('Overwrite')

        return self

