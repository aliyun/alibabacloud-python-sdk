# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_neuron20211115 import models as main_models
from darabonba.model import DaraModel

class LibrarySchema(DaraModel):
    def __init__(
        self,
        artifact_id: str = None,
        company_id: int = None,
        description: str = None,
        git_group: str = None,
        group_id: str = None,
        id: int = None,
        industry: str = None,
        library_id: int = None,
        market_id: int = None,
        name: str = None,
        provider: main_models.Provider = None,
        request_id: str = None,
    ):
        self.artifact_id = artifact_id
        self.company_id = company_id
        self.description = description
        self.git_group = git_group
        self.group_id = group_id
        self.id = id
        self.industry = industry
        self.library_id = library_id
        self.market_id = market_id
        self.name = name
        self.provider = provider
        self.request_id = request_id

    def validate(self):
        if self.provider:
            self.provider.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.artifact_id is not None:
            result['artifactId'] = self.artifact_id

        if self.company_id is not None:
            result['companyId'] = self.company_id

        if self.description is not None:
            result['description'] = self.description

        if self.git_group is not None:
            result['gitGroup'] = self.git_group

        if self.group_id is not None:
            result['groupId'] = self.group_id

        if self.id is not None:
            result['id'] = self.id

        if self.industry is not None:
            result['industry'] = self.industry

        if self.library_id is not None:
            result['libraryId'] = self.library_id

        if self.market_id is not None:
            result['marketId'] = self.market_id

        if self.name is not None:
            result['name'] = self.name

        if self.provider is not None:
            result['provider'] = self.provider.to_map()

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('artifactId') is not None:
            self.artifact_id = m.get('artifactId')

        if m.get('companyId') is not None:
            self.company_id = m.get('companyId')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('gitGroup') is not None:
            self.git_group = m.get('gitGroup')

        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('industry') is not None:
            self.industry = m.get('industry')

        if m.get('libraryId') is not None:
            self.library_id = m.get('libraryId')

        if m.get('marketId') is not None:
            self.market_id = m.get('marketId')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('provider') is not None:
            temp_model = main_models.Provider()
            self.provider = temp_model.from_map(m.get('provider'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

