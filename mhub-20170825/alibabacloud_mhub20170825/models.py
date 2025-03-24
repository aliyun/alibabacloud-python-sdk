# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class CreateAppRequest(TeaModel):
    def __init__(
        self,
        bundle_id: str = None,
        encoded_icon: str = None,
        industry_id: str = None,
        name: str = None,
        package_name: str = None,
        product_id: str = None,
        type: int = None,
    ):
        self.bundle_id = bundle_id
        self.encoded_icon = encoded_icon
        self.industry_id = industry_id
        # This parameter is required.
        self.name = name
        self.package_name = package_name
        # This parameter is required.
        self.product_id = product_id
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bundle_id is not None:
            result['BundleId'] = self.bundle_id
        if self.encoded_icon is not None:
            result['EncodedIcon'] = self.encoded_icon
        if self.industry_id is not None:
            result['IndustryId'] = self.industry_id
        if self.name is not None:
            result['Name'] = self.name
        if self.package_name is not None:
            result['PackageName'] = self.package_name
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BundleId') is not None:
            self.bundle_id = m.get('BundleId')
        if m.get('EncodedIcon') is not None:
            self.encoded_icon = m.get('EncodedIcon')
        if m.get('IndustryId') is not None:
            self.industry_id = m.get('IndustryId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PackageName') is not None:
            self.package_name = m.get('PackageName')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateAppResponseBodyAppInfo(TeaModel):
    def __init__(
        self,
        app_key: str = None,
        bundle_id: str = None,
        create_time: str = None,
        description: str = None,
        modify_time: str = None,
        name: str = None,
        package_name: str = None,
        product_id: int = None,
        type: int = None,
    ):
        self.app_key = app_key
        self.bundle_id = bundle_id
        self.create_time = create_time
        self.description = description
        self.modify_time = modify_time
        self.name = name
        self.package_name = package_name
        self.product_id = product_id
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.bundle_id is not None:
            result['BundleId'] = self.bundle_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.name is not None:
            result['Name'] = self.name
        if self.package_name is not None:
            result['PackageName'] = self.package_name
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('BundleId') is not None:
            self.bundle_id = m.get('BundleId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PackageName') is not None:
            self.package_name = m.get('PackageName')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateAppResponseBody(TeaModel):
    def __init__(
        self,
        app_info: CreateAppResponseBodyAppInfo = None,
        request_id: str = None,
    ):
        self.app_info = app_info
        self.request_id = request_id

    def validate(self):
        if self.app_info:
            self.app_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_info is not None:
            result['AppInfo'] = self.app_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInfo') is not None:
            temp_model = CreateAppResponseBodyAppInfo()
            self.app_info = temp_model.from_map(m['AppInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateAppResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateProductRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
    ):
        self.description = description
        # This parameter is required.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class CreateProductResponseBody(TeaModel):
    def __init__(
        self,
        product_id: int = None,
        request_id: str = None,
    ):
        self.product_id = product_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateProductResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateProductResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateProductResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAppRequest(TeaModel):
    def __init__(
        self,
        app_key: str = None,
    ):
        # This parameter is required.
        self.app_key = app_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        return self


class DeleteAppResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteAppResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteProductRequest(TeaModel):
    def __init__(
        self,
        product_id: str = None,
    ):
        # This parameter is required.
        self.product_id = product_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        return self


class DeleteProductResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
    ):
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteProductResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteProductResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteProductResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDashboardRequest(TeaModel):
    def __init__(
        self,
        app_key: str = None,
        app_type: int = None,
        app_version: str = None,
        end_time: int = None,
        keyword: str = None,
        proxy_action: str = None,
        service_name: str = None,
        start_time: int = None,
    ):
        self.app_key = app_key
        self.app_type = app_type
        self.app_version = app_version
        self.end_time = end_time
        self.keyword = keyword
        self.proxy_action = proxy_action
        self.service_name = service_name
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.app_type is not None:
            result['AppType'] = self.app_type
        if self.app_version is not None:
            result['AppVersion'] = self.app_version
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.proxy_action is not None:
            result['ProxyAction'] = self.proxy_action
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('ProxyAction') is not None:
            self.proxy_action = m.get('ProxyAction')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDashboardResponseBody(TeaModel):
    def __init__(
        self,
        model: str = None,
        request_id: str = None,
    ):
        self.model = model
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.model is not None:
            result['Model'] = self.model
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDashboardResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDashboardResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDashboardResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAppsRequest(TeaModel):
    def __init__(
        self,
        os_type: int = None,
        page: str = None,
        page_size: str = None,
        product_id: str = None,
    ):
        self.os_type = os_type
        self.page = page
        self.page_size = page_size
        # This parameter is required.
        self.product_id = product_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.os_type is not None:
            result['OsType'] = self.os_type
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        return self


class ListAppsResponseBodyAppInfosAppInfo(TeaModel):
    def __init__(
        self,
        app_key: str = None,
        bundle_id: str = None,
        encoded_icon: str = None,
        industry_id: int = None,
        name: str = None,
        package_name: str = None,
        readonly: bool = None,
        type: int = None,
    ):
        self.app_key = app_key
        self.bundle_id = bundle_id
        self.encoded_icon = encoded_icon
        self.industry_id = industry_id
        self.name = name
        self.package_name = package_name
        self.readonly = readonly
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.bundle_id is not None:
            result['BundleId'] = self.bundle_id
        if self.encoded_icon is not None:
            result['EncodedIcon'] = self.encoded_icon
        if self.industry_id is not None:
            result['IndustryId'] = self.industry_id
        if self.name is not None:
            result['Name'] = self.name
        if self.package_name is not None:
            result['PackageName'] = self.package_name
        if self.readonly is not None:
            result['Readonly'] = self.readonly
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('BundleId') is not None:
            self.bundle_id = m.get('BundleId')
        if m.get('EncodedIcon') is not None:
            self.encoded_icon = m.get('EncodedIcon')
        if m.get('IndustryId') is not None:
            self.industry_id = m.get('IndustryId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PackageName') is not None:
            self.package_name = m.get('PackageName')
        if m.get('Readonly') is not None:
            self.readonly = m.get('Readonly')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListAppsResponseBodyAppInfos(TeaModel):
    def __init__(
        self,
        app_info: List[ListAppsResponseBodyAppInfosAppInfo] = None,
    ):
        self.app_info = app_info

    def validate(self):
        if self.app_info:
            for k in self.app_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AppInfo'] = []
        if self.app_info is not None:
            for k in self.app_info:
                result['AppInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.app_info = []
        if m.get('AppInfo') is not None:
            for k in m.get('AppInfo'):
                temp_model = ListAppsResponseBodyAppInfosAppInfo()
                self.app_info.append(temp_model.from_map(k))
        return self


class ListAppsResponseBody(TeaModel):
    def __init__(
        self,
        app_infos: ListAppsResponseBodyAppInfos = None,
        request_id: str = None,
        total: int = None,
        ubsms_status: str = None,
    ):
        self.app_infos = app_infos
        self.request_id = request_id
        self.total = total
        self.ubsms_status = ubsms_status

    def validate(self):
        if self.app_infos:
            self.app_infos.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_infos is not None:
            result['AppInfos'] = self.app_infos.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        if self.ubsms_status is not None:
            result['UbsmsStatus'] = self.ubsms_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInfos') is not None:
            temp_model = ListAppsResponseBodyAppInfos()
            self.app_infos = temp_model.from_map(m['AppInfos'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('UbsmsStatus') is not None:
            self.ubsms_status = m.get('UbsmsStatus')
        return self


class ListAppsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAppsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListAppsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProductsRequest(TeaModel):
    def __init__(
        self,
        offset: int = None,
        product_name: str = None,
        simple: bool = None,
        size: int = None,
    ):
        self.offset = offset
        self.product_name = product_name
        self.simple = simple
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.offset is not None:
            result['Offset'] = self.offset
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        if self.simple is not None:
            result['Simple'] = self.simple
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Offset') is not None:
            self.offset = m.get('Offset')
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        if m.get('Simple') is not None:
            self.simple = m.get('Simple')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class ListProductsResponseBodyProductInfosProductInfo(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        encoded_icon: str = None,
        industry_id: int = None,
        name: str = None,
        platforms: str = None,
        product_id: int = None,
        readonly: bool = None,
    ):
        self.create_time = create_time
        self.description = description
        self.encoded_icon = encoded_icon
        self.industry_id = industry_id
        self.name = name
        self.platforms = platforms
        self.product_id = product_id
        self.readonly = readonly

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.encoded_icon is not None:
            result['EncodedIcon'] = self.encoded_icon
        if self.industry_id is not None:
            result['IndustryId'] = self.industry_id
        if self.name is not None:
            result['Name'] = self.name
        if self.platforms is not None:
            result['Platforms'] = self.platforms
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.readonly is not None:
            result['Readonly'] = self.readonly
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EncodedIcon') is not None:
            self.encoded_icon = m.get('EncodedIcon')
        if m.get('IndustryId') is not None:
            self.industry_id = m.get('IndustryId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Platforms') is not None:
            self.platforms = m.get('Platforms')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('Readonly') is not None:
            self.readonly = m.get('Readonly')
        return self


class ListProductsResponseBodyProductInfos(TeaModel):
    def __init__(
        self,
        product_info: List[ListProductsResponseBodyProductInfosProductInfo] = None,
    ):
        self.product_info = product_info

    def validate(self):
        if self.product_info:
            for k in self.product_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ProductInfo'] = []
        if self.product_info is not None:
            for k in self.product_info:
                result['ProductInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.product_info = []
        if m.get('ProductInfo') is not None:
            for k in m.get('ProductInfo'):
                temp_model = ListProductsResponseBodyProductInfosProductInfo()
                self.product_info.append(temp_model.from_map(k))
        return self


class ListProductsResponseBody(TeaModel):
    def __init__(
        self,
        product_infos: ListProductsResponseBodyProductInfos = None,
        request_id: str = None,
        total: int = None,
        ubsms_status: str = None,
    ):
        self.product_infos = product_infos
        self.request_id = request_id
        self.total = total
        self.ubsms_status = ubsms_status

    def validate(self):
        if self.product_infos:
            self.product_infos.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product_infos is not None:
            result['ProductInfos'] = self.product_infos.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        if self.ubsms_status is not None:
            result['UbsmsStatus'] = self.ubsms_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProductInfos') is not None:
            temp_model = ListProductsResponseBodyProductInfos()
            self.product_infos = temp_model.from_map(m['ProductInfos'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('UbsmsStatus') is not None:
            self.ubsms_status = m.get('UbsmsStatus')
        return self


class ListProductsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListProductsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListProductsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyAppRequest(TeaModel):
    def __init__(
        self,
        app_key: str = None,
        bundle_id: str = None,
        encoded_icon: str = None,
        industry_id: int = None,
        name: str = None,
        package_name: str = None,
    ):
        # This parameter is required.
        self.app_key = app_key
        self.bundle_id = bundle_id
        self.encoded_icon = encoded_icon
        self.industry_id = industry_id
        self.name = name
        self.package_name = package_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.bundle_id is not None:
            result['BundleId'] = self.bundle_id
        if self.encoded_icon is not None:
            result['EncodedIcon'] = self.encoded_icon
        if self.industry_id is not None:
            result['IndustryId'] = self.industry_id
        if self.name is not None:
            result['Name'] = self.name
        if self.package_name is not None:
            result['PackageName'] = self.package_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('BundleId') is not None:
            self.bundle_id = m.get('BundleId')
        if m.get('EncodedIcon') is not None:
            self.encoded_icon = m.get('EncodedIcon')
        if m.get('IndustryId') is not None:
            self.industry_id = m.get('IndustryId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PackageName') is not None:
            self.package_name = m.get('PackageName')
        return self


class ModifyAppResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyAppResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyProductRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        product_id: str = None,
    ):
        self.description = description
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.product_id = product_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        return self


class ModifyProductResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyProductResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyProductResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyProductResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OpenEmasServiceRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
    ):
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class OpenEmasServiceResponseBody(TeaModel):
    def __init__(
        self,
        order_id: str = None,
        request_id: str = None,
    ):
        self.order_id = order_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class OpenEmasServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: OpenEmasServiceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = OpenEmasServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryAppInfoRequest(TeaModel):
    def __init__(
        self,
        app_key: str = None,
    ):
        # This parameter is required.
        self.app_key = app_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        return self


class QueryAppInfoResponseBodyAppInfo(TeaModel):
    def __init__(
        self,
        app_key: str = None,
        app_name: str = None,
        bundle_id: str = None,
        cert_develop_avail: bool = None,
        cert_develop_expiration: str = None,
        cert_product_avail: bool = None,
        cert_product_expiration: str = None,
        create_time: str = None,
        encoded_icon: str = None,
        industry_id: int = None,
        package_name: str = None,
        product_id: int = None,
        readonly: bool = None,
        status: int = None,
        type: int = None,
    ):
        self.app_key = app_key
        self.app_name = app_name
        self.bundle_id = bundle_id
        self.cert_develop_avail = cert_develop_avail
        self.cert_develop_expiration = cert_develop_expiration
        self.cert_product_avail = cert_product_avail
        self.cert_product_expiration = cert_product_expiration
        self.create_time = create_time
        self.encoded_icon = encoded_icon
        self.industry_id = industry_id
        self.package_name = package_name
        self.product_id = product_id
        self.readonly = readonly
        self.status = status
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.bundle_id is not None:
            result['BundleId'] = self.bundle_id
        if self.cert_develop_avail is not None:
            result['CertDevelopAvail'] = self.cert_develop_avail
        if self.cert_develop_expiration is not None:
            result['CertDevelopExpiration'] = self.cert_develop_expiration
        if self.cert_product_avail is not None:
            result['CertProductAvail'] = self.cert_product_avail
        if self.cert_product_expiration is not None:
            result['CertProductExpiration'] = self.cert_product_expiration
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.encoded_icon is not None:
            result['EncodedIcon'] = self.encoded_icon
        if self.industry_id is not None:
            result['IndustryId'] = self.industry_id
        if self.package_name is not None:
            result['PackageName'] = self.package_name
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.readonly is not None:
            result['Readonly'] = self.readonly
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('BundleId') is not None:
            self.bundle_id = m.get('BundleId')
        if m.get('CertDevelopAvail') is not None:
            self.cert_develop_avail = m.get('CertDevelopAvail')
        if m.get('CertDevelopExpiration') is not None:
            self.cert_develop_expiration = m.get('CertDevelopExpiration')
        if m.get('CertProductAvail') is not None:
            self.cert_product_avail = m.get('CertProductAvail')
        if m.get('CertProductExpiration') is not None:
            self.cert_product_expiration = m.get('CertProductExpiration')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('EncodedIcon') is not None:
            self.encoded_icon = m.get('EncodedIcon')
        if m.get('IndustryId') is not None:
            self.industry_id = m.get('IndustryId')
        if m.get('PackageName') is not None:
            self.package_name = m.get('PackageName')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('Readonly') is not None:
            self.readonly = m.get('Readonly')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class QueryAppInfoResponseBody(TeaModel):
    def __init__(
        self,
        app_info: QueryAppInfoResponseBodyAppInfo = None,
        request_id: str = None,
    ):
        self.app_info = app_info
        self.request_id = request_id

    def validate(self):
        if self.app_info:
            self.app_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_info is not None:
            result['AppInfo'] = self.app_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInfo') is not None:
            temp_model = QueryAppInfoResponseBodyAppInfo()
            self.app_info = temp_model.from_map(m['AppInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryAppInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryAppInfoResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryAppInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryAppSecurityInfoRequest(TeaModel):
    def __init__(
        self,
        app_key: str = None,
    ):
        # This parameter is required.
        self.app_key = app_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        return self


class QueryAppSecurityInfoResponseBodyAppSecurityInfoExtConfig(TeaModel):
    def __init__(
        self,
        tlog_rsa_secret: str = None,
    ):
        self.tlog_rsa_secret = tlog_rsa_secret

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tlog_rsa_secret is not None:
            result['TlogRsaSecret'] = self.tlog_rsa_secret
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TlogRsaSecret') is not None:
            self.tlog_rsa_secret = m.get('TlogRsaSecret')
        return self


class QueryAppSecurityInfoResponseBodyAppSecurityInfo(TeaModel):
    def __init__(
        self,
        app_key: str = None,
        app_secret: str = None,
        ext_config: QueryAppSecurityInfoResponseBodyAppSecurityInfoExtConfig = None,
    ):
        self.app_key = app_key
        self.app_secret = app_secret
        self.ext_config = ext_config

    def validate(self):
        if self.ext_config:
            self.ext_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.app_secret is not None:
            result['AppSecret'] = self.app_secret
        if self.ext_config is not None:
            result['ExtConfig'] = self.ext_config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('AppSecret') is not None:
            self.app_secret = m.get('AppSecret')
        if m.get('ExtConfig') is not None:
            temp_model = QueryAppSecurityInfoResponseBodyAppSecurityInfoExtConfig()
            self.ext_config = temp_model.from_map(m['ExtConfig'])
        return self


class QueryAppSecurityInfoResponseBody(TeaModel):
    def __init__(
        self,
        app_security_info: QueryAppSecurityInfoResponseBodyAppSecurityInfo = None,
        request_id: str = None,
    ):
        self.app_security_info = app_security_info
        self.request_id = request_id

    def validate(self):
        if self.app_security_info:
            self.app_security_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_security_info is not None:
            result['AppSecurityInfo'] = self.app_security_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppSecurityInfo') is not None:
            temp_model = QueryAppSecurityInfoResponseBodyAppSecurityInfo()
            self.app_security_info = temp_model.from_map(m['AppSecurityInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryAppSecurityInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryAppSecurityInfoResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryAppSecurityInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryProductInfoRequest(TeaModel):
    def __init__(
        self,
        product_id: str = None,
    ):
        # This parameter is required.
        self.product_id = product_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        return self


class QueryProductInfoResponseBodyProductInfo(TeaModel):
    def __init__(
        self,
        encoded_icon: str = None,
        icon_name: str = None,
        industry_id: int = None,
        name: str = None,
        readonly: bool = None,
    ):
        self.encoded_icon = encoded_icon
        self.icon_name = icon_name
        self.industry_id = industry_id
        self.name = name
        self.readonly = readonly

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encoded_icon is not None:
            result['EncodedIcon'] = self.encoded_icon
        if self.icon_name is not None:
            result['IconName'] = self.icon_name
        if self.industry_id is not None:
            result['IndustryId'] = self.industry_id
        if self.name is not None:
            result['Name'] = self.name
        if self.readonly is not None:
            result['Readonly'] = self.readonly
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncodedIcon') is not None:
            self.encoded_icon = m.get('EncodedIcon')
        if m.get('IconName') is not None:
            self.icon_name = m.get('IconName')
        if m.get('IndustryId') is not None:
            self.industry_id = m.get('IndustryId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Readonly') is not None:
            self.readonly = m.get('Readonly')
        return self


class QueryProductInfoResponseBody(TeaModel):
    def __init__(
        self,
        product_info: QueryProductInfoResponseBodyProductInfo = None,
        request_id: str = None,
    ):
        self.product_info = product_info
        self.request_id = request_id

    def validate(self):
        if self.product_info:
            self.product_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product_info is not None:
            result['ProductInfo'] = self.product_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProductInfo') is not None:
            temp_model = QueryProductInfoResponseBodyProductInfo()
            self.product_info = temp_model.from_map(m['ProductInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryProductInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryProductInfoResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryProductInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


