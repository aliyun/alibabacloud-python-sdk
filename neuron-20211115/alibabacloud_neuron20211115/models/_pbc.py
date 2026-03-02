# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class Pbc(DaraModel):
    def __init__(
        self,
        alias: str = None,
        asset_type: str = None,
        company: str = None,
        company_id: int = None,
        description: str = None,
        developer_id: str = None,
        developer_name: str = None,
        fork_count: int = None,
        id: int = None,
        industry: str = None,
        invork_count: int = None,
        is_watched: bool = None,
        latest_version_id: int = None,
        market_id: int = None,
        name: str = None,
        request_id: str = None,
        type: str = None,
        watch_count: int = None,
    ):
        self.alias = alias
        self.asset_type = asset_type
        self.company = company
        self.company_id = company_id
        self.description = description
        self.developer_id = developer_id
        self.developer_name = developer_name
        self.fork_count = fork_count
        self.id = id
        self.industry = industry
        self.invork_count = invork_count
        self.is_watched = is_watched
        self.latest_version_id = latest_version_id
        self.market_id = market_id
        self.name = name
        self.request_id = request_id
        self.type = type
        self.watch_count = watch_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alias is not None:
            result['alias'] = self.alias

        if self.asset_type is not None:
            result['assetType'] = self.asset_type

        if self.company is not None:
            result['company'] = self.company

        if self.company_id is not None:
            result['companyId'] = self.company_id

        if self.description is not None:
            result['description'] = self.description

        if self.developer_id is not None:
            result['developerId'] = self.developer_id

        if self.developer_name is not None:
            result['developerName'] = self.developer_name

        if self.fork_count is not None:
            result['forkCount'] = self.fork_count

        if self.id is not None:
            result['id'] = self.id

        if self.industry is not None:
            result['industry'] = self.industry

        if self.invork_count is not None:
            result['invorkCount'] = self.invork_count

        if self.is_watched is not None:
            result['isWatched'] = self.is_watched

        if self.latest_version_id is not None:
            result['latestVersionId'] = self.latest_version_id

        if self.market_id is not None:
            result['marketId'] = self.market_id

        if self.name is not None:
            result['name'] = self.name

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.type is not None:
            result['type'] = self.type

        if self.watch_count is not None:
            result['watchCount'] = self.watch_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alias') is not None:
            self.alias = m.get('alias')

        if m.get('assetType') is not None:
            self.asset_type = m.get('assetType')

        if m.get('company') is not None:
            self.company = m.get('company')

        if m.get('companyId') is not None:
            self.company_id = m.get('companyId')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('developerId') is not None:
            self.developer_id = m.get('developerId')

        if m.get('developerName') is not None:
            self.developer_name = m.get('developerName')

        if m.get('forkCount') is not None:
            self.fork_count = m.get('forkCount')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('industry') is not None:
            self.industry = m.get('industry')

        if m.get('invorkCount') is not None:
            self.invork_count = m.get('invorkCount')

        if m.get('isWatched') is not None:
            self.is_watched = m.get('isWatched')

        if m.get('latestVersionId') is not None:
            self.latest_version_id = m.get('latestVersionId')

        if m.get('marketId') is not None:
            self.market_id = m.get('marketId')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('watchCount') is not None:
            self.watch_count = m.get('watchCount')

        return self

