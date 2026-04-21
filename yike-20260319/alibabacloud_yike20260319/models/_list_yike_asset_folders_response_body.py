# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_yike20260319 import models as main_models
from darabonba.model import DaraModel

class ListYikeAssetFoldersResponseBody(DaraModel):
    def __init__(
        self,
        folder_list: List[main_models.ListYikeAssetFoldersResponseBodyFolderList] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total: int = None,
    ):
        self.folder_list = folder_list
        self.max_results = max_results
        self.next_token = next_token
        # Id of the request
        self.request_id = request_id
        self.total = total

    def validate(self):
        if self.folder_list:
            for v1 in self.folder_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['FolderList'] = []
        if self.folder_list is not None:
            for k1 in self.folder_list:
                result['FolderList'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.folder_list = []
        if m.get('FolderList') is not None:
            for k1 in m.get('FolderList'):
                temp_model = main_models.ListYikeAssetFoldersResponseBodyFolderList()
                self.folder_list.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class ListYikeAssetFoldersResponseBodyFolderList(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        folder_id: str = None,
        folder_name: str = None,
        is_default: bool = None,
        production_id: str = None,
        workspace_id: str = None,
    ):
        self.create_time = create_time
        self.folder_id = folder_id
        self.folder_name = folder_name
        self.is_default = is_default
        self.production_id = production_id
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.folder_id is not None:
            result['FolderId'] = self.folder_id

        if self.folder_name is not None:
            result['FolderName'] = self.folder_name

        if self.is_default is not None:
            result['IsDefault'] = self.is_default

        if self.production_id is not None:
            result['ProductionId'] = self.production_id

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')

        if m.get('FolderName') is not None:
            self.folder_name = m.get('FolderName')

        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')

        if m.get('ProductionId') is not None:
            self.production_id = m.get('ProductionId')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

