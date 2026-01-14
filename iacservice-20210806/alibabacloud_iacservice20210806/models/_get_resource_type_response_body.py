# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_iacservice20210806 import models as main_models
from darabonba.model import DaraModel

class GetResourceTypeResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        resource_type: main_models.GetResourceTypeResponseBodyResourceType = None,
    ):
        self.request_id = request_id
        self.resource_type = resource_type

    def validate(self):
        if self.resource_type:
            self.resource_type.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.resource_type is not None:
            result['resourceType'] = self.resource_type.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('resourceType') is not None:
            temp_model = main_models.GetResourceTypeResponseBodyResourceType()
            self.resource_type = temp_model.from_map(m.get('resourceType'))

        return self

class GetResourceTypeResponseBodyResourceType(DaraModel):
    def __init__(
        self,
        description: str = None,
        operations: List[main_models.GetResourceTypeResponseBodyResourceTypeOperations] = None,
        product: str = None,
        product_name: str = None,
        product_name_en: str = None,
        properties: Dict[str, Any] = None,
        resource_detail_page_url: str = None,
        resource_list_page_url: str = None,
        status: str = None,
        status_start_version: str = None,
        subcategory: str = None,
        support_exported: bool = None,
        terraform_provider_version: str = None,
        terraform_resource_type: str = None,
        title: str = None,
    ):
        self.description = description
        self.operations = operations
        self.product = product
        self.product_name = product_name
        self.product_name_en = product_name_en
        self.properties = properties
        self.resource_detail_page_url = resource_detail_page_url
        self.resource_list_page_url = resource_list_page_url
        self.status = status
        self.status_start_version = status_start_version
        self.subcategory = subcategory
        self.support_exported = support_exported
        self.terraform_provider_version = terraform_provider_version
        self.terraform_resource_type = terraform_resource_type
        self.title = title

    def validate(self):
        if self.operations:
            for v1 in self.operations:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['description'] = self.description

        result['operations'] = []
        if self.operations is not None:
            for k1 in self.operations:
                result['operations'].append(k1.to_map() if k1 else None)

        if self.product is not None:
            result['product'] = self.product

        if self.product_name is not None:
            result['productName'] = self.product_name

        if self.product_name_en is not None:
            result['productNameEn'] = self.product_name_en

        if self.properties is not None:
            result['properties'] = self.properties

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

        if self.support_exported is not None:
            result['supportExported'] = self.support_exported

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

        self.operations = []
        if m.get('operations') is not None:
            for k1 in m.get('operations'):
                temp_model = main_models.GetResourceTypeResponseBodyResourceTypeOperations()
                self.operations.append(temp_model.from_map(k1))

        if m.get('product') is not None:
            self.product = m.get('product')

        if m.get('productName') is not None:
            self.product_name = m.get('productName')

        if m.get('productNameEn') is not None:
            self.product_name_en = m.get('productNameEn')

        if m.get('properties') is not None:
            self.properties = m.get('properties')

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

        if m.get('supportExported') is not None:
            self.support_exported = m.get('supportExported')

        if m.get('terraformProviderVersion') is not None:
            self.terraform_provider_version = m.get('terraformProviderVersion')

        if m.get('terraformResourceType') is not None:
            self.terraform_resource_type = m.get('terraformResourceType')

        if m.get('title') is not None:
            self.title = m.get('title')

        return self

class GetResourceTypeResponseBodyResourceTypeOperations(DaraModel):
    def __init__(
        self,
        api_name: str = None,
        api_version: str = None,
        operation_type: str = None,
        service_code: str = None,
    ):
        self.api_name = api_name
        self.api_version = api_version
        self.operation_type = operation_type
        # serviceCode
        self.service_code = service_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_name is not None:
            result['apiName'] = self.api_name

        if self.api_version is not None:
            result['apiVersion'] = self.api_version

        if self.operation_type is not None:
            result['operationType'] = self.operation_type

        if self.service_code is not None:
            result['serviceCode'] = self.service_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiName') is not None:
            self.api_name = m.get('apiName')

        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')

        if m.get('operationType') is not None:
            self.operation_type = m.get('operationType')

        if m.get('serviceCode') is not None:
            self.service_code = m.get('serviceCode')

        return self

