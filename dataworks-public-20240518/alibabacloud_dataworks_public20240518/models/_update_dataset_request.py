# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateDatasetRequest(DaraModel):
    def __init__(
        self,
        comment: str = None,
        id: str = None,
        name: str = None,
        readme: str = None,
    ):
        # The dataset description. Length not exceeding 1024.
        self.comment = comment
        # The dataset ID. Only DataWorks datasets are supported for update.
        # 
        # This parameter is required.
        self.id = id
        # The dataset name. A non-empty string, length not exceeding 128.
        self.name = name
        # The user guide, supports Markdown formatted rich text.
        self.readme = readme

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comment is not None:
            result['Comment'] = self.comment

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.readme is not None:
            result['Readme'] = self.readme

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Readme') is not None:
            self.readme = m.get('Readme')

        return self

