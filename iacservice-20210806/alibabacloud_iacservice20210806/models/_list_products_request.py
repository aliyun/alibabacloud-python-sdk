# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListProductsRequest(DaraModel):
    def __init__(
        self,
        keyword: str = None,
        max_results: int = None,
        next_token: str = None,
        sort: str = None,
        status: str = None,
        support_terraformer: bool = None,
        terraform_provider_version: str = None,
    ):
        self.keyword = keyword
        self.max_results = max_results
        self.next_token = next_token
        self.sort = sort
        self.status = status
        self.support_terraformer = support_terraformer
        self.terraform_provider_version = terraform_provider_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.keyword is not None:
            result['keyword'] = self.keyword

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.sort is not None:
            result['sort'] = self.sort

        if self.status is not None:
            result['status'] = self.status

        if self.support_terraformer is not None:
            result['supportTerraformer'] = self.support_terraformer

        if self.terraform_provider_version is not None:
            result['terraformProviderVersion'] = self.terraform_provider_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('sort') is not None:
            self.sort = m.get('sort')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('supportTerraformer') is not None:
            self.support_terraformer = m.get('supportTerraformer')

        if m.get('terraformProviderVersion') is not None:
            self.terraform_provider_version = m.get('terraformProviderVersion')

        return self

