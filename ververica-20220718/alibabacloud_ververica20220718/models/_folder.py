# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ververica20220718 import models as main_models
from darabonba.model import DaraModel

class Folder(DaraModel):
    def __init__(
        self,
        created_at: int = None,
        folder_id: str = None,
        modified_at: int = None,
        name: str = None,
        namespace: str = None,
        parent_id: str = None,
        sub_folder: List[main_models.SubFolder] = None,
        workspace: str = None,
    ):
        # The time when the folder was created.
        self.created_at = created_at
        # The ID of the folder.
        self.folder_id = folder_id
        # The time when the folder was modified.
        self.modified_at = modified_at
        # The name of the folder.
        self.name = name
        # The name of the namespace.
        self.namespace = namespace
        # The ID of the parent folder.
        self.parent_id = parent_id
        # The list of subfolders.
        self.sub_folder = sub_folder
        # The workspace ID.
        self.workspace = workspace

    def validate(self):
        if self.sub_folder:
            for v1 in self.sub_folder:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.folder_id is not None:
            result['folderId'] = self.folder_id

        if self.modified_at is not None:
            result['modifiedAt'] = self.modified_at

        if self.name is not None:
            result['name'] = self.name

        if self.namespace is not None:
            result['namespace'] = self.namespace

        if self.parent_id is not None:
            result['parentId'] = self.parent_id

        result['subFolder'] = []
        if self.sub_folder is not None:
            for k1 in self.sub_folder:
                result['subFolder'].append(k1.to_map() if k1 else None)

        if self.workspace is not None:
            result['workspace'] = self.workspace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('folderId') is not None:
            self.folder_id = m.get('folderId')

        if m.get('modifiedAt') is not None:
            self.modified_at = m.get('modifiedAt')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')

        if m.get('parentId') is not None:
            self.parent_id = m.get('parentId')

        self.sub_folder = []
        if m.get('subFolder') is not None:
            for k1 in m.get('subFolder'):
                temp_model = main_models.SubFolder()
                self.sub_folder.append(temp_model.from_map(k1))

        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')

        return self

