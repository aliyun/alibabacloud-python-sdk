# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, Any, List


class CreateResourceRequest(TeaModel):
    def __init__(
        self,
        body: str = None,
        is_async: bool = None,
    ):
        self.body = body
        self.is_async = is_async

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body
        if self.is_async is not None:
            result['isAsync'] = self.is_async
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')
        if m.get('isAsync') is not None:
            self.is_async = m.get('isAsync')
        return self


class CreateResourceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        resource_id: str = None,
        task_id: str = None,
    ):
        # 请求id
        self.request_id = request_id
        # 资源id
        self.resource_id = resource_id
        # 任务id
        self.task_id = task_id

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
        if self.task_id is not None:
            result['taskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
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


class DeleteResourceRequest(TeaModel):
    def __init__(
        self,
        is_async: bool = None,
        region_id: str = None,
    ):
        self.is_async = is_async
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_async is not None:
            result['isAsync'] = self.is_async
        if self.region_id is not None:
            result['regionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('isAsync') is not None:
            self.is_async = m.get('isAsync')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        return self


class DeleteResourceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.task_id is not None:
            result['taskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
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
        region_id: str = None,
        resource_attributes: str = None,
        resource_id: str = None,
        resource_type_code: str = None,
    ):
        self.product_code = product_code
        self.region_id = region_id
        self.resource_attributes = resource_attributes
        self.resource_id = resource_id
        self.resource_type_code = resource_type_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product_code is not None:
            result['productCode'] = self.product_code
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.resource_attributes is not None:
            result['resourceAttributes'] = self.resource_attributes
        if self.resource_id is not None:
            result['resourceId'] = self.resource_id
        if self.resource_type_code is not None:
            result['resourceTypeCode'] = self.resource_type_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('productCode') is not None:
            self.product_code = m.get('productCode')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('resourceAttributes') is not None:
            self.resource_attributes = m.get('resourceAttributes')
        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')
        if m.get('resourceTypeCode') is not None:
            self.resource_type_code = m.get('resourceTypeCode')
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


class GetTaskResponseBodyTask(TeaModel):
    def __init__(
        self,
        failed_reason: str = None,
        resource_id: str = None,
        status: str = None,
        task_id: str = None,
    ):
        self.failed_reason = failed_reason
        self.resource_id = resource_id
        self.status = status
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.failed_reason is not None:
            result['failedReason'] = self.failed_reason
        if self.resource_id is not None:
            result['resourceId'] = self.resource_id
        if self.status is not None:
            result['status'] = self.status
        if self.task_id is not None:
            result['taskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('failedReason') is not None:
            self.failed_reason = m.get('failedReason')
        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        return self


class GetTaskResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task: GetTaskResponseBodyTask = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.task = task

    def validate(self):
        if self.task:
            self.task.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.task is not None:
            result['task'] = self.task.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('task') is not None:
            temp_model = GetTaskResponseBodyTask()
            self.task = temp_model.from_map(m['task'])
        return self


class GetTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetTaskResponseBody = None,
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
            temp_model = GetTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDataSourcesRequest(TeaModel):
    def __init__(
        self,
        filter: Dict[str, Any] = None,
    ):
        self.filter = filter

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filter is not None:
            result['filter'] = self.filter
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('filter') is not None:
            self.filter = m.get('filter')
        return self


class ListDataSourcesShrinkRequest(TeaModel):
    def __init__(
        self,
        filter_shrink: str = None,
    ):
        self.filter_shrink = filter_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filter_shrink is not None:
            result['filter'] = self.filter_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('filter') is not None:
            self.filter_shrink = m.get('filter')
        return self


class ListDataSourcesResponseBodyDataSources(TeaModel):
    def __init__(
        self,
        id: str = None,
        data_source_attributes: str = None,
    ):
        self.id = id
        self.data_source_attributes = data_source_attributes

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.data_source_attributes is not None:
            result['dataSourceAttributes'] = self.data_source_attributes
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('dataSourceAttributes') is not None:
            self.data_source_attributes = m.get('dataSourceAttributes')
        return self


class ListDataSourcesResponseBody(TeaModel):
    def __init__(
        self,
        data_sources: List[ListDataSourcesResponseBodyDataSources] = None,
        request_id: str = None,
    ):
        self.data_sources = data_sources
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.data_sources:
            for k in self.data_sources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['dataSources'] = []
        if self.data_sources is not None:
            for k in self.data_sources:
                result['dataSources'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_sources = []
        if m.get('dataSources') is not None:
            for k in m.get('dataSources'):
                temp_model = ListDataSourcesResponseBodyDataSources()
                self.data_sources.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListDataSourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListDataSourcesResponseBody = None,
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
            temp_model = ListDataSourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProductsRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
    ):
        self.max_results = max_results
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
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
        max_results: int = None,
        next_token: str = None,
        products: List[ListProductsResponseBodyProducts] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.max_results = max_results
        # 表示当前调用返回读取到的位置，空代表数据已经读取完毕
        self.next_token = next_token
        self.products = products
        # Id of the request
        self.request_id = request_id
        # TotalCount本次请求条件下的数据总量，此参数为可选参数，默认可不返回
        self.total_count = total_count

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
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        result['products'] = []
        if self.products is not None:
            for k in self.products:
                result['products'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        self.products = []
        if m.get('products') is not None:
            for k in m.get('products'):
                temp_model = ListProductsResponseBodyProducts()
                self.products.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
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


class ListResourceTypesRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        resource_type_codes: List[str] = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.resource_type_codes = resource_type_codes

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.resource_type_codes is not None:
            result['resourceTypeCodes'] = self.resource_type_codes
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('resourceTypeCodes') is not None:
            self.resource_type_codes = m.get('resourceTypeCodes')
        return self


class ListResourceTypesShrinkRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        resource_type_codes_shrink: str = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.resource_type_codes_shrink = resource_type_codes_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.resource_type_codes_shrink is not None:
            result['resourceTypeCodes'] = self.resource_type_codes_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('resourceTypeCodes') is not None:
            self.resource_type_codes_shrink = m.get('resourceTypeCodes')
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
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        resource_types: List[ListResourceTypesResponseBodyResourceTypes] = None,
        total_count: int = None,
    ):
        self.max_results = max_results
        # 表示当前调用返回读取到的位置，空代表数据已经读取完毕
        self.next_token = next_token
        # Id of the request
        self.request_id = request_id
        self.resource_types = resource_types
        # TotalCount本次请求条件下的数据总量，此参数为可选参数，默认可不返回
        self.total_count = total_count

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
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['resourceTypes'] = []
        if self.resource_types is not None:
            for k in self.resource_types:
                result['resourceTypes'].append(k.to_map() if k else None)
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
            for k in m.get('resourceTypes'):
                temp_model = ListResourceTypesResponseBodyResourceTypes()
                self.resource_types.append(temp_model.from_map(k))
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
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


class ListResourcesRequest(TeaModel):
    def __init__(
        self,
        filter: Dict[str, Any] = None,
        is_reload: bool = None,
        page_num: int = None,
        page_size: int = None,
        region_ids: List[str] = None,
    ):
        self.filter = filter
        self.is_reload = is_reload
        self.page_num = page_num
        self.page_size = page_size
        self.region_ids = region_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filter is not None:
            result['filter'] = self.filter
        if self.is_reload is not None:
            result['isReload'] = self.is_reload
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.region_ids is not None:
            result['regionIds'] = self.region_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('filter') is not None:
            self.filter = m.get('filter')
        if m.get('isReload') is not None:
            self.is_reload = m.get('isReload')
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('regionIds') is not None:
            self.region_ids = m.get('regionIds')
        return self


class ListResourcesShrinkRequest(TeaModel):
    def __init__(
        self,
        filter_shrink: str = None,
        is_reload: bool = None,
        page_num: int = None,
        page_size: int = None,
        region_ids_shrink: str = None,
    ):
        self.filter_shrink = filter_shrink
        self.is_reload = is_reload
        self.page_num = page_num
        self.page_size = page_size
        self.region_ids_shrink = region_ids_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filter_shrink is not None:
            result['filter'] = self.filter_shrink
        if self.is_reload is not None:
            result['isReload'] = self.is_reload
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.region_ids_shrink is not None:
            result['regionIds'] = self.region_ids_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('filter') is not None:
            self.filter_shrink = m.get('filter')
        if m.get('isReload') is not None:
            self.is_reload = m.get('isReload')
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('regionIds') is not None:
            self.region_ids_shrink = m.get('regionIds')
        return self


class ListResourcesResponseBodyResources(TeaModel):
    def __init__(
        self,
        product_code: str = None,
        resource_type_code: str = None,
        region_id: str = None,
        resource_id: str = None,
        resource_attributes: str = None,
    ):
        self.product_code = product_code
        self.resource_type_code = resource_type_code
        self.region_id = region_id
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
        if self.region_id is not None:
            result['regionId'] = self.region_id
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
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')
        if m.get('resourceAttributes') is not None:
            self.resource_attributes = m.get('resourceAttributes')
        return self


class ListResourcesResponseBody(TeaModel):
    def __init__(
        self,
        page_num: int = None,
        page_size: int = None,
        request_id: str = None,
        resources: List[ListResourcesResponseBodyResources] = None,
        total_count: int = None,
    ):
        self.page_num = page_num
        self.page_size = page_size
        # Id of the request
        self.request_id = request_id
        self.resources = resources
        self.total_count = total_count

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
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['resources'] = []
        if self.resources is not None:
            for k in self.resources:
                result['resources'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.resources = []
        if m.get('resources') is not None:
            for k in m.get('resources'):
                temp_model = ListResourcesResponseBodyResources()
                self.resources.append(temp_model.from_map(k))
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
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


class ReloadResourcesRequest(TeaModel):
    def __init__(
        self,
        region_ids: List[str] = None,
    ):
        self.region_ids = region_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_ids is not None:
            result['regionIds'] = self.region_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('regionIds') is not None:
            self.region_ids = m.get('regionIds')
        return self


class ReloadResourcesShrinkRequest(TeaModel):
    def __init__(
        self,
        region_ids_shrink: str = None,
    ):
        self.region_ids_shrink = region_ids_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_ids_shrink is not None:
            result['regionIds'] = self.region_ids_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('regionIds') is not None:
            self.region_ids_shrink = m.get('regionIds')
        return self


class ReloadResourcesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.task_id is not None:
            result['taskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        return self


class ReloadResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ReloadResourcesResponseBody = None,
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
            temp_model = ReloadResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateResourceRequest(TeaModel):
    def __init__(
        self,
        body: str = None,
        is_async: bool = None,
    ):
        self.body = body
        self.is_async = is_async

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body
        if self.is_async is not None:
            result['isAsync'] = self.is_async
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')
        if m.get('isAsync') is not None:
            self.is_async = m.get('isAsync')
        return self


class UpdateResourceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_id: str = None,
    ):
        # 请求id
        self.request_id = request_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.task_id is not None:
            result['taskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
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


