# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class Library(DaraModel):
    def __init__(
        self,
        artifact_id: str = None,
        asset_type: str = None,
        company: str = None,
        company_id: int = None,
        depend_count: int = None,
        description: str = None,
        group_id: str = None,
        id: int = None,
        industry: str = None,
        is_watched: bool = None,
        name: str = None,
        provider: str = None,
        provider_name: str = None,
        repo_url: str = None,
        request_id: str = None,
        review_id: int = None,
        status: str = None,
        step_status: str = None,
        watch_count: int = None,
    ):
        self.artifact_id = artifact_id
        self.asset_type = asset_type
        self.company = company
        self.company_id = company_id
        self.depend_count = depend_count
        self.description = description
        self.group_id = group_id
        self.id = id
        self.industry = industry
        self.is_watched = is_watched
        self.name = name
        self.provider = provider
        self.provider_name = provider_name
        self.repo_url = repo_url
        self.request_id = request_id
        self.review_id = review_id
        self.status = status
        self.step_status = step_status
        self.watch_count = watch_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.artifact_id is not None:
            result['artifactId'] = self.artifact_id

        if self.asset_type is not None:
            result['assetType'] = self.asset_type

        if self.company is not None:
            result['company'] = self.company

        if self.company_id is not None:
            result['companyId'] = self.company_id

        if self.depend_count is not None:
            result['dependCount'] = self.depend_count

        if self.description is not None:
            result['description'] = self.description

        if self.group_id is not None:
            result['groupId'] = self.group_id

        if self.id is not None:
            result['id'] = self.id

        if self.industry is not None:
            result['industry'] = self.industry

        if self.is_watched is not None:
            result['isWatched'] = self.is_watched

        if self.name is not None:
            result['name'] = self.name

        if self.provider is not None:
            result['provider'] = self.provider

        if self.provider_name is not None:
            result['providerName'] = self.provider_name

        if self.repo_url is not None:
            result['repoUrl'] = self.repo_url

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.review_id is not None:
            result['reviewId'] = self.review_id

        if self.status is not None:
            result['status'] = self.status

        if self.step_status is not None:
            result['stepStatus'] = self.step_status

        if self.watch_count is not None:
            result['watchCount'] = self.watch_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('artifactId') is not None:
            self.artifact_id = m.get('artifactId')

        if m.get('assetType') is not None:
            self.asset_type = m.get('assetType')

        if m.get('company') is not None:
            self.company = m.get('company')

        if m.get('companyId') is not None:
            self.company_id = m.get('companyId')

        if m.get('dependCount') is not None:
            self.depend_count = m.get('dependCount')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('industry') is not None:
            self.industry = m.get('industry')

        if m.get('isWatched') is not None:
            self.is_watched = m.get('isWatched')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('provider') is not None:
            self.provider = m.get('provider')

        if m.get('providerName') is not None:
            self.provider_name = m.get('providerName')

        if m.get('repoUrl') is not None:
            self.repo_url = m.get('repoUrl')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('reviewId') is not None:
            self.review_id = m.get('reviewId')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('stepStatus') is not None:
            self.step_status = m.get('stepStatus')

        if m.get('watchCount') is not None:
            self.watch_count = m.get('watchCount')

        return self

