# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_iacservice20210806 import models as main_models
from darabonba.model import DaraModel

class ListResourceTypesResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        resource_types: List[main_models.ListResourceTypesResponseBodyResourceTypes] = None,
        total_count: int = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id
        self.resource_types = resource_types
        self.total_count = total_count

    def validate(self):
        if self.resource_types:
            for v1 in self.resource_types:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.request_id is not None:
            result['requestId'] = self.request_id

        result['resourceTypes'] = []
        if self.resource_types is not None:
            for k1 in self.resource_types:
                result['resourceTypes'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        self.resource_types = []
        if m.get('resourceTypes') is not None:
            for k1 in m.get('resourceTypes'):
                temp_model = main_models.ListResourceTypesResponseBodyResourceTypes()
                self.resource_types.append(temp_model.from_map(k1))

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class ListResourceTypesResponseBodyResourceTypes(DaraModel):
    def __init__(
        self,
        description: str = None,
        product: str = None,
        product_name: str = None,
        resource_detail_page_url: str = None,
        resource_list_page_url: str = None,
        status: str = None,
        status_start_version: str = None,
        subcategory: str = None,
        support_terraformer: str = None,
        terraform_provider_version: str = None,
        terraform_resource_type: str = None,
        title: str = None,
    ):
        self.description = description
        self.product = product
        self.product_name = product_name
        self.resource_detail_page_url = resource_detail_page_url
        self.resource_list_page_url = resource_list_page_url
        self.status = status
        self.status_start_version = status_start_version
        self.subcategory = subcategory
        self.support_terraformer = support_terraformer
        self.terraform_provider_version = terraform_provider_version
        self.terraform_resource_type = terraform_resource_type
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['description'] = self.description

        if self.product is not None:
            result['product'] = self.product

        if self.product_name is not None:
            result['productName'] = self.product_name

        if self.resource_detail_page_url is not None:
            result['resourceDetailPageUrl'] = self.resource_detail_page_url

        if self.resource_list_page_url is not None:
            result['resourceListPageUrl'] = self.resource_list_page_url

        if self.status is not None:
            result['status'] = self.status

        if self.status_start_version is not None:
            result['statusStartVersion'] = self.status_start_version

        if self.subcategory is not None:
            result['subcategory'] = self.subcategory

        if self.support_terraformer is not None:
            result['supportTerraformer'] = self.support_terraformer

        if self.terraform_provider_version is not None:
            result['terraformProviderVersion'] = self.terraform_provider_version

        if self.terraform_resource_type is not None:
            result['terraformResourceType'] = self.terraform_resource_type

        if self.title is not None:
            result['title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('product') is not None:
            self.product = m.get('product')

        if m.get('productName') is not None:
            self.product_name = m.get('productName')

        if m.get('resourceDetailPageUrl') is not None:
            self.resource_detail_page_url = m.get('resourceDetailPageUrl')

        if m.get('resourceListPageUrl') is not None:
            self.resource_list_page_url = m.get('resourceListPageUrl')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('statusStartVersion') is not None:
            self.status_start_version = m.get('statusStartVersion')

        if m.get('subcategory') is not None:
            self.subcategory = m.get('subcategory')

        if m.get('supportTerraformer') is not None:
            self.support_terraformer = m.get('supportTerraformer')

        if m.get('terraformProviderVersion') is not None:
            self.terraform_provider_version = m.get('terraformProviderVersion')

        if m.get('terraformResourceType') is not None:
            self.terraform_resource_type = m.get('terraformResourceType')

        if m.get('title') is not None:
            self.title = m.get('title')

        return self

