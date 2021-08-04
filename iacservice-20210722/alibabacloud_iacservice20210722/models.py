# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict


class ListResourceTypesRequest(TeaModel):
    def __init__(
        self,
        resource_type_codes: List[str] = None,
        next_token: str = None,
        max_results: int = None,
    ):
        self.resource_type_codes = resource_type_codes
        self.next_token = next_token
        self.max_results = max_results

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_type_codes is not None:
            result['resourceTypeCodes'] = self.resource_type_codes
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('resourceTypeCodes') is not None:
            self.resource_type_codes = m.get('resourceTypeCodes')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        return self


class ListResourceTypesShrinkRequest(TeaModel):
    def __init__(
        self,
        resource_type_codes_shrink: str = None,
        next_token: str = None,
        max_results: int = None,
    ):
        self.resource_type_codes_shrink = resource_type_codes_shrink
        self.next_token = next_token
        self.max_results = max_results

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_type_codes_shrink is not None:
            result['resourceTypeCodes'] = self.resource_type_codes_shrink
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('resourceTypeCodes') is not None:
            self.resource_type_codes_shrink = m.get('resourceTypeCodes')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        return self


class ListResourceTypesResponseBodyResourceTypesInfo(TeaModel):
    def __init__(
        self,
        title: str = None,
        description: str = None,
        category: str = None,
        delivery_scope: str = None,
        charge_type: str = None,
        available_sites: List[str] = None,
    ):
        # 资源类型的中文名称，如实例
        self.title = title
        # 描述
        self.description = description
        # 资源分类 枚举:normal(普通资源)/singleton(单例资源)/virtual(虚拟资源)/readonly(只读资源)
        self.category = category
        # 交付级别 枚举:center(中心化部署级别)/region(地域部署级别)/zone(可用区部署级别)
        self.delivery_scope = delivery_scope
        # 付费形式  枚举:paid(付费)/free(免费)
        self.charge_type = charge_type
        # 允许资源展示的站点  枚举:china(中国站)/intl(国际站)/japan(日本站)
        self.available_sites = available_sites

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.title is not None:
            result['title'] = self.title
        if self.description is not None:
            result['description'] = self.description
        if self.category is not None:
            result['category'] = self.category
        if self.delivery_scope is not None:
            result['deliveryScope'] = self.delivery_scope
        if self.charge_type is not None:
            result['chargeType'] = self.charge_type
        if self.available_sites is not None:
            result['availableSites'] = self.available_sites
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('title') is not None:
            self.title = m.get('title')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('deliveryScope') is not None:
            self.delivery_scope = m.get('deliveryScope')
        if m.get('chargeType') is not None:
            self.charge_type = m.get('chargeType')
        if m.get('availableSites') is not None:
            self.available_sites = m.get('availableSites')
        return self


class ListResourceTypesResponseBodyResourceTypesIdentityDefinition(TeaModel):
    def __init__(
        self,
        unique_key_fields: List[str] = None,
        second_unique_key_fields: List[str] = None,
        arn_pattern: str = None,
    ):
        # uniqueKey的字段列表，有顺序
        self.unique_key_fields = unique_key_fields
        # 备选Id字段列表，有顺序
        self.second_unique_key_fields = second_unique_key_fields
        # 资源ARN
        self.arn_pattern = arn_pattern

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.unique_key_fields is not None:
            result['uniqueKeyFields'] = self.unique_key_fields
        if self.second_unique_key_fields is not None:
            result['secondUniqueKeyFields'] = self.second_unique_key_fields
        if self.arn_pattern is not None:
            result['arnPattern'] = self.arn_pattern
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('uniqueKeyFields') is not None:
            self.unique_key_fields = m.get('uniqueKeyFields')
        if m.get('secondUniqueKeyFields') is not None:
            self.second_unique_key_fields = m.get('secondUniqueKeyFields')
        if m.get('arnPattern') is not None:
            self.arn_pattern = m.get('arnPattern')
        return self


class ListResourceTypesResponseBodyResourceTypesStatusDefinition(TeaModel):
    def __init__(
        self,
        code: str = None,
        description: str = None,
        type: str = None,
    ):
        # 状态code
        self.code = code
        # 描述
        self.description = description
        # 资源状态分类，必须对代表资源创建后的初始状态进行initial标识。枚举:initial(初始状态)
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.description is not None:
            result['description'] = self.description
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ListResourceTypesResponseBodyResourceTypesResourceRelations(TeaModel):
    def __init__(
        self,
        product: str = None,
        resource_type: str = None,
        relation: str = None,
        description: str = None,
    ):
        # 云产品B
        self.product = product
        # 资源类型B
        self.resource_type = resource_type
        # 资源关系  枚举:relevance(关联关系)/dependency(依赖关系)/childParent(子父关系)
        self.relation = relation
        # 资源关系描述 枚举：枚举:关联关系/依赖关系/子父关系
        self.description = description

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product is not None:
            result['product'] = self.product
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        if self.relation is not None:
            result['relation'] = self.relation
        if self.description is not None:
            result['description'] = self.description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('product') is not None:
            self.product = m.get('product')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        if m.get('relation') is not None:
            self.relation = m.get('relation')
        if m.get('description') is not None:
            self.description = m.get('description')
        return self


class ListResourceTypesResponseBodyResourceTypes(TeaModel):
    def __init__(
        self,
        product_code: str = None,
        resource_type_code: str = None,
        info: ListResourceTypesResponseBodyResourceTypesInfo = None,
        identity_definition: ListResourceTypesResponseBodyResourceTypesIdentityDefinition = None,
        status_definition: List[ListResourceTypesResponseBodyResourceTypesStatusDefinition] = None,
        resource_properties: str = None,
        resource_relations: List[ListResourceTypesResponseBodyResourceTypesResourceRelations] = None,
    ):
        self.product_code = product_code
        self.resource_type_code = resource_type_code
        self.info = info
        self.identity_definition = identity_definition
        self.status_definition = status_definition
        self.resource_properties = resource_properties
        self.resource_relations = resource_relations

    def validate(self):
        if self.info:
            self.info.validate()
        if self.identity_definition:
            self.identity_definition.validate()
        if self.status_definition:
            for k in self.status_definition:
                if k:
                    k.validate()
        if self.resource_relations:
            for k in self.resource_relations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product_code is not None:
            result['productCode'] = self.product_code
        if self.resource_type_code is not None:
            result['resourceTypeCode'] = self.resource_type_code
        if self.info is not None:
            result['info'] = self.info.to_map()
        if self.identity_definition is not None:
            result['identityDefinition'] = self.identity_definition.to_map()
        result['statusDefinition'] = []
        if self.status_definition is not None:
            for k in self.status_definition:
                result['statusDefinition'].append(k.to_map() if k else None)
        if self.resource_properties is not None:
            result['resourceProperties'] = self.resource_properties
        result['resourceRelations'] = []
        if self.resource_relations is not None:
            for k in self.resource_relations:
                result['resourceRelations'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('productCode') is not None:
            self.product_code = m.get('productCode')
        if m.get('resourceTypeCode') is not None:
            self.resource_type_code = m.get('resourceTypeCode')
        if m.get('info') is not None:
            temp_model = ListResourceTypesResponseBodyResourceTypesInfo()
            self.info = temp_model.from_map(m['info'])
        if m.get('identityDefinition') is not None:
            temp_model = ListResourceTypesResponseBodyResourceTypesIdentityDefinition()
            self.identity_definition = temp_model.from_map(m['identityDefinition'])
        self.status_definition = []
        if m.get('statusDefinition') is not None:
            for k in m.get('statusDefinition'):
                temp_model = ListResourceTypesResponseBodyResourceTypesStatusDefinition()
                self.status_definition.append(temp_model.from_map(k))
        if m.get('resourceProperties') is not None:
            self.resource_properties = m.get('resourceProperties')
        self.resource_relations = []
        if m.get('resourceRelations') is not None:
            for k in m.get('resourceRelations'):
                temp_model = ListResourceTypesResponseBodyResourceTypesResourceRelations()
                self.resource_relations.append(temp_model.from_map(k))
        return self


class ListResourceTypesResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        next_token: str = None,
        request_id: str = None,
        max_results: int = None,
        resource_types: List[ListResourceTypesResponseBodyResourceTypes] = None,
    ):
        # TotalCount本次请求条件下的数据总量，此参数为可选参数，默认可不返回
        self.total_count = total_count
        # 表示当前调用返回读取到的位置，空代表数据已经读取完毕
        self.next_token = next_token
        # Id of the request
        self.request_id = request_id
        self.max_results = max_results
        self.resource_types = resource_types

    def validate(self):
        if self.resource_types:
            for k in self.resource_types:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        result['resourceTypes'] = []
        if self.resource_types is not None:
            for k in self.resource_types:
                result['resourceTypes'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        self.resource_types = []
        if m.get('resourceTypes') is not None:
            for k in m.get('resourceTypes'):
                temp_model = ListResourceTypesResponseBodyResourceTypes()
                self.resource_types.append(temp_model.from_map(k))
        return self


class ListResourceTypesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListResourceTypesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListResourceTypesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProductsRequest(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        max_results: int = None,
    ):
        self.next_token = next_token
        self.max_results = max_results

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        return self


class ListProductsResponseBodyProductsProductName(TeaModel):
    def __init__(
        self,
        zh_cn: str = None,
        en_us: str = None,
    ):
        self.zh_cn = zh_cn
        self.en_us = en_us

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.zh_cn is not None:
            result['zh_CN'] = self.zh_cn
        if self.en_us is not None:
            result['en_US'] = self.en_us
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('zh_CN') is not None:
            self.zh_cn = m.get('zh_CN')
        if m.get('en_US') is not None:
            self.en_us = m.get('en_US')
        return self


class ListProductsResponseBodyProducts(TeaModel):
    def __init__(
        self,
        product_code: str = None,
        product_name: ListProductsResponseBodyProductsProductName = None,
    ):
        self.product_code = product_code
        self.product_name = product_name

    def validate(self):
        if self.product_name:
            self.product_name.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product_code is not None:
            result['productCode'] = self.product_code
        if self.product_name is not None:
            result['productName'] = self.product_name.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('productCode') is not None:
            self.product_code = m.get('productCode')
        if m.get('productName') is not None:
            temp_model = ListProductsResponseBodyProductsProductName()
            self.product_name = temp_model.from_map(m['productName'])
        return self


class ListProductsResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        next_token: str = None,
        request_id: str = None,
        max_results: int = None,
        products: List[ListProductsResponseBodyProducts] = None,
    ):
        # TotalCount本次请求条件下的数据总量，此参数为可选参数，默认可不返回
        self.total_count = total_count
        # 表示当前调用返回读取到的位置，空代表数据已经读取完毕
        self.next_token = next_token
        # Id of the request
        self.request_id = request_id
        self.max_results = max_results
        self.products = products

    def validate(self):
        if self.products:
            for k in self.products:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        result['products'] = []
        if self.products is not None:
            for k in self.products:
                result['products'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        self.products = []
        if m.get('products') is not None:
            for k in m.get('products'):
                temp_model = ListProductsResponseBodyProducts()
                self.products.append(temp_model.from_map(k))
        return self


class ListProductsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListProductsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListProductsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListResourcesRequest(TeaModel):
    def __init__(
        self,
        region_ids: List[str] = None,
        resource_group_id: str = None,
    ):
        self.region_ids = region_ids
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_ids is not None:
            result['regionIds'] = self.region_ids
        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('regionIds') is not None:
            self.region_ids = m.get('regionIds')
        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')
        return self


class ListResourcesShrinkRequest(TeaModel):
    def __init__(
        self,
        region_ids_shrink: str = None,
        resource_group_id: str = None,
    ):
        self.region_ids_shrink = region_ids_shrink
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_ids_shrink is not None:
            result['regionIds'] = self.region_ids_shrink
        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('regionIds') is not None:
            self.region_ids_shrink = m.get('regionIds')
        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')
        return self


class ListResourcesResponseBodyResources(TeaModel):
    def __init__(
        self,
        product_code: str = None,
        resource_type_code: str = None,
        resource_id: str = None,
        resource_attributes: str = None,
    ):
        self.product_code = product_code
        self.resource_type_code = resource_type_code
        self.resource_id = resource_id
        self.resource_attributes = resource_attributes

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product_code is not None:
            result['productCode'] = self.product_code
        if self.resource_type_code is not None:
            result['resourceTypeCode'] = self.resource_type_code
        if self.resource_id is not None:
            result['resourceId'] = self.resource_id
        if self.resource_attributes is not None:
            result['resourceAttributes'] = self.resource_attributes
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('productCode') is not None:
            self.product_code = m.get('productCode')
        if m.get('resourceTypeCode') is not None:
            self.resource_type_code = m.get('resourceTypeCode')
        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')
        if m.get('resourceAttributes') is not None:
            self.resource_attributes = m.get('resourceAttributes')
        return self


class ListResourcesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total_count: int = None,
        resources: List[ListResourcesResponseBodyResources] = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.total_count = total_count
        self.resources = resources

    def validate(self):
        if self.resources:
            for k in self.resources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        result['resources'] = []
        if self.resources is not None:
            for k in self.resources:
                result['resources'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        self.resources = []
        if m.get('resources') is not None:
            for k in m.get('resources'):
                temp_model = ListResourcesResponseBodyResources()
                self.resources.append(temp_model.from_map(k))
        return self


class ListResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListResourcesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateResourceRequest(TeaModel):
    def __init__(
        self,
        body: str = None,
    ):
        self.body = body

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class CreateResourceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        resource_id: str = None,
    ):
        # 请求id
        self.request_id = request_id
        # 资源id
        self.resource_id = resource_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_id is not None:
            result['resourceId'] = self.resource_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')
        return self


class CreateResourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateResourceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateResourceRequest(TeaModel):
    def __init__(
        self,
        body: str = None,
    ):
        self.body = body

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class UpdateResourceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # 请求id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class UpdateResourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateResourceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetResourceRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['regionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        return self


class GetResourceResponseBodyResource(TeaModel):
    def __init__(
        self,
        product_code: str = None,
        resource_type_code: str = None,
        resource_id: str = None,
        resource_attributes: str = None,
    ):
        self.product_code = product_code
        self.resource_type_code = resource_type_code
        self.resource_id = resource_id
        self.resource_attributes = resource_attributes

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product_code is not None:
            result['productCode'] = self.product_code
        if self.resource_type_code is not None:
            result['resourceTypeCode'] = self.resource_type_code
        if self.resource_id is not None:
            result['resourceId'] = self.resource_id
        if self.resource_attributes is not None:
            result['resourceAttributes'] = self.resource_attributes
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('productCode') is not None:
            self.product_code = m.get('productCode')
        if m.get('resourceTypeCode') is not None:
            self.resource_type_code = m.get('resourceTypeCode')
        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')
        if m.get('resourceAttributes') is not None:
            self.resource_attributes = m.get('resourceAttributes')
        return self


class GetResourceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        resource: GetResourceResponseBodyResource = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.resource = resource

    def validate(self):
        if self.resource:
            self.resource.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.resource is not None:
            result['resource'] = self.resource.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('resource') is not None:
            temp_model = GetResourceResponseBodyResource()
            self.resource = temp_model.from_map(m['resource'])
        return self


class GetResourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetResourceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteResourceRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['regionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        return self


class DeleteResourceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DeleteResourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteResourceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


