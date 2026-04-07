# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListFoldersRequest(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        parent_folder_path: str = None,
        project_id: int = None,
        project_identifier: str = None,
    ):
        # The error code.
        # 
        # This parameter is required.
        self.page_number = page_number
        # Indicates whether the request was successful.
        # 
        # This parameter is required.
        self.page_size = page_size
        # 0000-ABCD-EFG****
        # 
        # This parameter is required.
        self.parent_folder_path = parent_folder_path
        # The error message.
        self.project_id = project_id
        # The request ID. You can troubleshoot issues based on the ID.
        self.project_identifier = project_identifier

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.parent_folder_path is not None:
            result['ParentFolderPath'] = self.parent_folder_path

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.project_identifier is not None:
            result['ProjectIdentifier'] = self.project_identifier

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ParentFolderPath') is not None:
            self.parent_folder_path = m.get('ParentFolderPath')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('ProjectIdentifier') is not None:
            self.project_identifier = m.get('ProjectIdentifier')

        return self

