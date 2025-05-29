# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class GetOpenApiListRequest(TeaModel):
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


class GetOpenApiListResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        open_api_string: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.open_api_string = open_api_string
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.open_api_string is not None:
            result['OpenApiString'] = self.open_api_string
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('OpenApiString') is not None:
            self.open_api_string = m.get('OpenApiString')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetOpenApiListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetOpenApiListResponseBody = None,
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
            temp_model = GetOpenApiListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListConsoleProductResponseBodyData(TeaModel):
    def __init__(
        self,
        belonged_category: str = None,
        categories: List[str] = None,
        channel_links: List[str] = None,
        doc_id: str = None,
        keywords: List[str] = None,
        names: str = None,
        pinyin: str = None,
        product_id: str = None,
        related_console_app_id: str = None,
        related_pip_id: str = None,
        show_in_nav: bool = None,
        supported_accounts: List[str] = None,
        supported_channels: List[str] = None,
        tag: str = None,
        tag_expire_time: str = None,
    ):
        self.belonged_category = belonged_category
        self.categories = categories
        self.channel_links = channel_links
        self.doc_id = doc_id
        self.keywords = keywords
        self.names = names
        self.pinyin = pinyin
        self.product_id = product_id
        self.related_console_app_id = related_console_app_id
        self.related_pip_id = related_pip_id
        self.show_in_nav = show_in_nav
        self.supported_accounts = supported_accounts
        self.supported_channels = supported_channels
        self.tag = tag
        self.tag_expire_time = tag_expire_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.belonged_category is not None:
            result['BelongedCategory'] = self.belonged_category
        if self.categories is not None:
            result['Categories'] = self.categories
        if self.channel_links is not None:
            result['ChannelLinks'] = self.channel_links
        if self.doc_id is not None:
            result['DocId'] = self.doc_id
        if self.keywords is not None:
            result['Keywords'] = self.keywords
        if self.names is not None:
            result['Names'] = self.names
        if self.pinyin is not None:
            result['Pinyin'] = self.pinyin
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.related_console_app_id is not None:
            result['RelatedConsoleAppId'] = self.related_console_app_id
        if self.related_pip_id is not None:
            result['RelatedPipId'] = self.related_pip_id
        if self.show_in_nav is not None:
            result['ShowInNav'] = self.show_in_nav
        if self.supported_accounts is not None:
            result['SupportedAccounts'] = self.supported_accounts
        if self.supported_channels is not None:
            result['SupportedChannels'] = self.supported_channels
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.tag_expire_time is not None:
            result['TagExpireTime'] = self.tag_expire_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BelongedCategory') is not None:
            self.belonged_category = m.get('BelongedCategory')
        if m.get('Categories') is not None:
            self.categories = m.get('Categories')
        if m.get('ChannelLinks') is not None:
            self.channel_links = m.get('ChannelLinks')
        if m.get('DocId') is not None:
            self.doc_id = m.get('DocId')
        if m.get('Keywords') is not None:
            self.keywords = m.get('Keywords')
        if m.get('Names') is not None:
            self.names = m.get('Names')
        if m.get('Pinyin') is not None:
            self.pinyin = m.get('Pinyin')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('RelatedConsoleAppId') is not None:
            self.related_console_app_id = m.get('RelatedConsoleAppId')
        if m.get('RelatedPipId') is not None:
            self.related_pip_id = m.get('RelatedPipId')
        if m.get('ShowInNav') is not None:
            self.show_in_nav = m.get('ShowInNav')
        if m.get('SupportedAccounts') is not None:
            self.supported_accounts = m.get('SupportedAccounts')
        if m.get('SupportedChannels') is not None:
            self.supported_channels = m.get('SupportedChannels')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('TagExpireTime') is not None:
            self.tag_expire_time = m.get('TagExpireTime')
        return self


class ListConsoleProductResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[ListConsoleProductResponseBodyData] = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListConsoleProductResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListConsoleProductResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListConsoleProductResponseBody = None,
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
            temp_model = ListConsoleProductResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


