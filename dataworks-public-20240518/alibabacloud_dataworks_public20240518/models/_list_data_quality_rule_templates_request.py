# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDataQualityRuleTemplatesRequest(DaraModel):
    def __init__(
        self,
        creation_source: str = None,
        directory_path: str = None,
        name: str = None,
        page_number: int = None,
        page_size: int = None,
        project_id: int = None,
    ):
        # The creation source of the rule template. This parameter is required.
        # - System: system template
        # - UserDefined: user-defined template
        self.creation_source = creation_source
        # The category directory in which the custom template is stored. Levels are separated by forward slashes (/). Each level name can be up to 1,024 characters in length and cannot contain whitespace characters or backslashes.
        self.directory_path = directory_path
        # The fuzzy match of the template rule name. For a system template, the internationalized name of the system template is fuzzy matched based on the language.
        self.name = name
        # The number of entries per page in a paginated query. Default value: 10.
        self.page_number = page_number
        # The page number of a paginated query. Default value: 1.
        self.page_size = page_size
        # The DataWorks workspace ID.
        # 
        # This parameter is required.
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creation_source is not None:
            result['CreationSource'] = self.creation_source

        if self.directory_path is not None:
            result['DirectoryPath'] = self.directory_path

        if self.name is not None:
            result['Name'] = self.name

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationSource') is not None:
            self.creation_source = m.get('CreationSource')

        if m.get('DirectoryPath') is not None:
            self.directory_path = m.get('DirectoryPath')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        return self

