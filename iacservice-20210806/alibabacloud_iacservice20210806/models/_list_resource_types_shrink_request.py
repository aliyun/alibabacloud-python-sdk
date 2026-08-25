# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListResourceTypesShrinkRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        keyword: str = None,
        max_results: int = None,
        next_token: str = None,
        product: str = None,
        sort: str = None,
        status: str = None,
        subcategory: str = None,
        support_terraformer: bool = None,
        terraform_provider_version: str = None,
        terraform_resource_types_shrink: str = None,
    ):
        # The language of the response. Valid values:
        # - zh-CN: Chinese.
        # - en-US: English.
        # 
        # Default value: zh-CN.
        self.accept_language = accept_language
        # The keyword for searching resource code or name. Fuzzy match is supported.
        self.keyword = keyword
        # The maximum number of entries per page. Valid values: 0 to 200. Default value: 100.
        self.max_results = max_results
        # The pagination token.
        self.next_token = next_token
        # The product code. Fuzzy match is supported.
        self.product = product
        # The order in which resource types are returned. Valid values:
        # - Normal (default): returned in normal order.
        # - Top: returned in order of popular access.
        self.sort = sort
        # The status list for filtering. Valid values:
        # - Available
        # - Deprecated
        self.status = status
        # The product subcategory in Terraform.
        self.subcategory = subcategory
        # Specifies whether Terraformer is supported.
        self.support_terraformer = support_terraformer
        # The Terraform Provider version. If this parameter is left empty, the latest version is used by default.
        self.terraform_provider_version = terraform_provider_version
        # The list of Terraform resources.
        self.terraform_resource_types_shrink = terraform_resource_types_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept_language is not None:
            result['acceptLanguage'] = self.accept_language

        if self.keyword is not None:
            result['keyword'] = self.keyword

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.product is not None:
            result['product'] = self.product

        if self.sort is not None:
            result['sort'] = self.sort

        if self.status is not None:
            result['status'] = self.status

        if self.subcategory is not None:
            result['subcategory'] = self.subcategory

        if self.support_terraformer is not None:
            result['supportTerraformer'] = self.support_terraformer

        if self.terraform_provider_version is not None:
            result['terraformProviderVersion'] = self.terraform_provider_version

        if self.terraform_resource_types_shrink is not None:
            result['terraformResourceTypes'] = self.terraform_resource_types_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('acceptLanguage') is not None:
            self.accept_language = m.get('acceptLanguage')

        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('product') is not None:
            self.product = m.get('product')

        if m.get('sort') is not None:
            self.sort = m.get('sort')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('subcategory') is not None:
            self.subcategory = m.get('subcategory')

        if m.get('supportTerraformer') is not None:
            self.support_terraformer = m.get('supportTerraformer')

        if m.get('terraformProviderVersion') is not None:
            self.terraform_provider_version = m.get('terraformProviderVersion')

        if m.get('terraformResourceTypes') is not None:
            self.terraform_resource_types_shrink = m.get('terraformResourceTypes')

        return self

