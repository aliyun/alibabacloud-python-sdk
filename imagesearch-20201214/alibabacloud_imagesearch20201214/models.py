# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import BinaryIO, Dict, List


class AddImageRequest(TeaModel):
    def __init__(
        self,
        instance_name: str = None,
        product_id: str = None,
        pic_name: str = None,
        pic_content: str = None,
        category_id: int = None,
        crop: bool = None,
        region: str = None,
        custom_content: str = None,
        int_attr: int = None,
        str_attr: str = None,
    ):
        self.instance_name = instance_name
        self.product_id = product_id
        self.pic_name = pic_name
        self.pic_content = pic_content
        self.category_id = category_id
        self.crop = crop
        self.region = region
        self.custom_content = custom_content
        self.int_attr = int_attr
        self.str_attr = str_attr

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.pic_name is not None:
            result['PicName'] = self.pic_name
        if self.pic_content is not None:
            result['PicContent'] = self.pic_content
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.crop is not None:
            result['Crop'] = self.crop
        if self.region is not None:
            result['Region'] = self.region
        if self.custom_content is not None:
            result['CustomContent'] = self.custom_content
        if self.int_attr is not None:
            result['IntAttr'] = self.int_attr
        if self.str_attr is not None:
            result['StrAttr'] = self.str_attr
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('PicName') is not None:
            self.pic_name = m.get('PicName')
        if m.get('PicContent') is not None:
            self.pic_content = m.get('PicContent')
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('Crop') is not None:
            self.crop = m.get('Crop')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('CustomContent') is not None:
            self.custom_content = m.get('CustomContent')
        if m.get('IntAttr') is not None:
            self.int_attr = m.get('IntAttr')
        if m.get('StrAttr') is not None:
            self.str_attr = m.get('StrAttr')
        return self


class AddImageAdvanceRequest(TeaModel):
    def __init__(
        self,
        pic_content_object: BinaryIO = None,
        instance_name: str = None,
        product_id: str = None,
        pic_name: str = None,
        category_id: int = None,
        crop: bool = None,
        region: str = None,
        custom_content: str = None,
        int_attr: int = None,
        str_attr: str = None,
    ):
        self.pic_content_object = pic_content_object
        self.instance_name = instance_name
        self.product_id = product_id
        self.pic_name = pic_name
        self.category_id = category_id
        self.crop = crop
        self.region = region
        self.custom_content = custom_content
        self.int_attr = int_attr
        self.str_attr = str_attr

    def validate(self):
        self.validate_required(self.pic_content_object, 'pic_content_object')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pic_content_object is not None:
            result['PicContentObject'] = self.pic_content_object
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.pic_name is not None:
            result['PicName'] = self.pic_name
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.crop is not None:
            result['Crop'] = self.crop
        if self.region is not None:
            result['Region'] = self.region
        if self.custom_content is not None:
            result['CustomContent'] = self.custom_content
        if self.int_attr is not None:
            result['IntAttr'] = self.int_attr
        if self.str_attr is not None:
            result['StrAttr'] = self.str_attr
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PicContentObject') is not None:
            self.pic_content_object = m.get('PicContentObject')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('PicName') is not None:
            self.pic_name = m.get('PicName')
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('Crop') is not None:
            self.crop = m.get('Crop')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('CustomContent') is not None:
            self.custom_content = m.get('CustomContent')
        if m.get('IntAttr') is not None:
            self.int_attr = m.get('IntAttr')
        if m.get('StrAttr') is not None:
            self.str_attr = m.get('StrAttr')
        return self


class AddImageResponseBodyPicInfo(TeaModel):
    def __init__(
        self,
        region: str = None,
        category_id: int = None,
    ):
        self.region = region
        self.category_id = category_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region is not None:
            result['Region'] = self.region
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        return self


class AddImageResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: int = None,
        pic_info: AddImageResponseBodyPicInfo = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.code = code
        self.pic_info = pic_info
        self.success = success

    def validate(self):
        if self.pic_info:
            self.pic_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.pic_info is not None:
            result['PicInfo'] = self.pic_info.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('PicInfo') is not None:
            temp_model = AddImageResponseBodyPicInfo()
            self.pic_info = temp_model.from_map(m['PicInfo'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddImageResponseBody = None,
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
            temp_model = AddImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteImageRequest(TeaModel):
    def __init__(
        self,
        instance_name: str = None,
        product_id: str = None,
        pic_name: str = None,
    ):
        self.instance_name = instance_name
        self.product_id = product_id
        self.pic_name = pic_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.pic_name is not None:
            result['PicName'] = self.pic_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('PicName') is not None:
            self.pic_name = m.get('PicName')
        return self


class DeleteImageResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: int = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.code = code
        self.success = success

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
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteImageResponseBody = None,
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
            temp_model = DeleteImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchImageByNameRequest(TeaModel):
    def __init__(
        self,
        instance_name: str = None,
        product_id: str = None,
        pic_name: str = None,
        category_id: int = None,
        num: int = None,
        start: int = None,
        filter: str = None,
    ):
        self.instance_name = instance_name
        self.product_id = product_id
        self.pic_name = pic_name
        self.category_id = category_id
        self.num = num
        self.start = start
        self.filter = filter

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.pic_name is not None:
            result['PicName'] = self.pic_name
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.num is not None:
            result['Num'] = self.num
        if self.start is not None:
            result['Start'] = self.start
        if self.filter is not None:
            result['Filter'] = self.filter
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('PicName') is not None:
            self.pic_name = m.get('PicName')
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('Num') is not None:
            self.num = m.get('Num')
        if m.get('Start') is not None:
            self.start = m.get('Start')
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        return self


class SearchImageByNameResponseBodyHead(TeaModel):
    def __init__(
        self,
        docs_found: int = None,
        docs_return: int = None,
        search_time: int = None,
    ):
        self.docs_found = docs_found
        self.docs_return = docs_return
        self.search_time = search_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.docs_found is not None:
            result['DocsFound'] = self.docs_found
        if self.docs_return is not None:
            result['DocsReturn'] = self.docs_return
        if self.search_time is not None:
            result['SearchTime'] = self.search_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DocsFound') is not None:
            self.docs_found = m.get('DocsFound')
        if m.get('DocsReturn') is not None:
            self.docs_return = m.get('DocsReturn')
        if m.get('SearchTime') is not None:
            self.search_time = m.get('SearchTime')
        return self


class SearchImageByNameResponseBodyAuctions(TeaModel):
    def __init__(
        self,
        pic_name: str = None,
        int_attr: int = None,
        category_id: int = None,
        product_id: str = None,
        str_attr: str = None,
        sort_expr_values: str = None,
        custom_content: str = None,
        score: float = None,
    ):
        self.pic_name = pic_name
        self.int_attr = int_attr
        self.category_id = category_id
        self.product_id = product_id
        self.str_attr = str_attr
        self.sort_expr_values = sort_expr_values
        self.custom_content = custom_content
        self.score = score

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pic_name is not None:
            result['PicName'] = self.pic_name
        if self.int_attr is not None:
            result['IntAttr'] = self.int_attr
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.str_attr is not None:
            result['StrAttr'] = self.str_attr
        if self.sort_expr_values is not None:
            result['SortExprValues'] = self.sort_expr_values
        if self.custom_content is not None:
            result['CustomContent'] = self.custom_content
        if self.score is not None:
            result['Score'] = self.score
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PicName') is not None:
            self.pic_name = m.get('PicName')
        if m.get('IntAttr') is not None:
            self.int_attr = m.get('IntAttr')
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('StrAttr') is not None:
            self.str_attr = m.get('StrAttr')
        if m.get('SortExprValues') is not None:
            self.sort_expr_values = m.get('SortExprValues')
        if m.get('CustomContent') is not None:
            self.custom_content = m.get('CustomContent')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        return self


class SearchImageByNameResponseBodyPicInfoMultiRegion(TeaModel):
    def __init__(
        self,
        region: str = None,
    ):
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class SearchImageByNameResponseBodyPicInfoAllCategories(TeaModel):
    def __init__(
        self,
        name: str = None,
        id: int = None,
    ):
        self.name = name
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class SearchImageByNameResponseBodyPicInfo(TeaModel):
    def __init__(
        self,
        region: str = None,
        category_id: int = None,
        multi_region: List[SearchImageByNameResponseBodyPicInfoMultiRegion] = None,
        all_categories: List[SearchImageByNameResponseBodyPicInfoAllCategories] = None,
    ):
        self.region = region
        self.category_id = category_id
        self.multi_region = multi_region
        self.all_categories = all_categories

    def validate(self):
        if self.multi_region:
            for k in self.multi_region:
                if k:
                    k.validate()
        if self.all_categories:
            for k in self.all_categories:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region is not None:
            result['Region'] = self.region
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        result['MultiRegion'] = []
        if self.multi_region is not None:
            for k in self.multi_region:
                result['MultiRegion'].append(k.to_map() if k else None)
        result['AllCategories'] = []
        if self.all_categories is not None:
            for k in self.all_categories:
                result['AllCategories'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        self.multi_region = []
        if m.get('MultiRegion') is not None:
            for k in m.get('MultiRegion'):
                temp_model = SearchImageByNameResponseBodyPicInfoMultiRegion()
                self.multi_region.append(temp_model.from_map(k))
        self.all_categories = []
        if m.get('AllCategories') is not None:
            for k in m.get('AllCategories'):
                temp_model = SearchImageByNameResponseBodyPicInfoAllCategories()
                self.all_categories.append(temp_model.from_map(k))
        return self


class SearchImageByNameResponseBody(TeaModel):
    def __init__(
        self,
        msg: str = None,
        head: SearchImageByNameResponseBodyHead = None,
        request_id: str = None,
        auctions: List[SearchImageByNameResponseBodyAuctions] = None,
        code: int = None,
        pic_info: SearchImageByNameResponseBodyPicInfo = None,
        success: bool = None,
    ):
        self.msg = msg
        self.head = head
        self.request_id = request_id
        self.auctions = auctions
        self.code = code
        self.pic_info = pic_info
        self.success = success

    def validate(self):
        if self.head:
            self.head.validate()
        if self.auctions:
            for k in self.auctions:
                if k:
                    k.validate()
        if self.pic_info:
            self.pic_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.head is not None:
            result['Head'] = self.head.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Auctions'] = []
        if self.auctions is not None:
            for k in self.auctions:
                result['Auctions'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        if self.pic_info is not None:
            result['PicInfo'] = self.pic_info.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('Head') is not None:
            temp_model = SearchImageByNameResponseBodyHead()
            self.head = temp_model.from_map(m['Head'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.auctions = []
        if m.get('Auctions') is not None:
            for k in m.get('Auctions'):
                temp_model = SearchImageByNameResponseBodyAuctions()
                self.auctions.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('PicInfo') is not None:
            temp_model = SearchImageByNameResponseBodyPicInfo()
            self.pic_info = temp_model.from_map(m['PicInfo'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SearchImageByNameResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SearchImageByNameResponseBody = None,
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
            temp_model = SearchImageByNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchImageByPicRequest(TeaModel):
    def __init__(
        self,
        instance_name: str = None,
        pic_content: str = None,
        category_id: int = None,
        crop: bool = None,
        region: str = None,
        num: int = None,
        start: int = None,
        filter: str = None,
    ):
        self.instance_name = instance_name
        self.pic_content = pic_content
        self.category_id = category_id
        self.crop = crop
        self.region = region
        self.num = num
        self.start = start
        self.filter = filter

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.pic_content is not None:
            result['PicContent'] = self.pic_content
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.crop is not None:
            result['Crop'] = self.crop
        if self.region is not None:
            result['Region'] = self.region
        if self.num is not None:
            result['Num'] = self.num
        if self.start is not None:
            result['Start'] = self.start
        if self.filter is not None:
            result['Filter'] = self.filter
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('PicContent') is not None:
            self.pic_content = m.get('PicContent')
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('Crop') is not None:
            self.crop = m.get('Crop')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Num') is not None:
            self.num = m.get('Num')
        if m.get('Start') is not None:
            self.start = m.get('Start')
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        return self


class SearchImageByPicAdvanceRequest(TeaModel):
    def __init__(
        self,
        pic_content_object: BinaryIO = None,
        instance_name: str = None,
        category_id: int = None,
        crop: bool = None,
        region: str = None,
        num: int = None,
        start: int = None,
        filter: str = None,
    ):
        self.pic_content_object = pic_content_object
        self.instance_name = instance_name
        self.category_id = category_id
        self.crop = crop
        self.region = region
        self.num = num
        self.start = start
        self.filter = filter

    def validate(self):
        self.validate_required(self.pic_content_object, 'pic_content_object')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pic_content_object is not None:
            result['PicContentObject'] = self.pic_content_object
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.crop is not None:
            result['Crop'] = self.crop
        if self.region is not None:
            result['Region'] = self.region
        if self.num is not None:
            result['Num'] = self.num
        if self.start is not None:
            result['Start'] = self.start
        if self.filter is not None:
            result['Filter'] = self.filter
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PicContentObject') is not None:
            self.pic_content_object = m.get('PicContentObject')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('Crop') is not None:
            self.crop = m.get('Crop')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Num') is not None:
            self.num = m.get('Num')
        if m.get('Start') is not None:
            self.start = m.get('Start')
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        return self


class SearchImageByPicResponseBodyHead(TeaModel):
    def __init__(
        self,
        docs_found: int = None,
        docs_return: int = None,
        search_time: int = None,
    ):
        self.docs_found = docs_found
        self.docs_return = docs_return
        self.search_time = search_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.docs_found is not None:
            result['DocsFound'] = self.docs_found
        if self.docs_return is not None:
            result['DocsReturn'] = self.docs_return
        if self.search_time is not None:
            result['SearchTime'] = self.search_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DocsFound') is not None:
            self.docs_found = m.get('DocsFound')
        if m.get('DocsReturn') is not None:
            self.docs_return = m.get('DocsReturn')
        if m.get('SearchTime') is not None:
            self.search_time = m.get('SearchTime')
        return self


class SearchImageByPicResponseBodyAuctions(TeaModel):
    def __init__(
        self,
        pic_name: str = None,
        int_attr: int = None,
        category_id: int = None,
        product_id: str = None,
        str_attr: str = None,
        sort_expr_values: str = None,
        custom_content: str = None,
        score: float = None,
    ):
        self.pic_name = pic_name
        self.int_attr = int_attr
        self.category_id = category_id
        self.product_id = product_id
        self.str_attr = str_attr
        self.sort_expr_values = sort_expr_values
        self.custom_content = custom_content
        self.score = score

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pic_name is not None:
            result['PicName'] = self.pic_name
        if self.int_attr is not None:
            result['IntAttr'] = self.int_attr
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.str_attr is not None:
            result['StrAttr'] = self.str_attr
        if self.sort_expr_values is not None:
            result['SortExprValues'] = self.sort_expr_values
        if self.custom_content is not None:
            result['CustomContent'] = self.custom_content
        if self.score is not None:
            result['Score'] = self.score
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PicName') is not None:
            self.pic_name = m.get('PicName')
        if m.get('IntAttr') is not None:
            self.int_attr = m.get('IntAttr')
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('StrAttr') is not None:
            self.str_attr = m.get('StrAttr')
        if m.get('SortExprValues') is not None:
            self.sort_expr_values = m.get('SortExprValues')
        if m.get('CustomContent') is not None:
            self.custom_content = m.get('CustomContent')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        return self


class SearchImageByPicResponseBodyPicInfoMultiRegion(TeaModel):
    def __init__(
        self,
        region: str = None,
    ):
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class SearchImageByPicResponseBodyPicInfoAllCategories(TeaModel):
    def __init__(
        self,
        name: str = None,
        id: int = None,
    ):
        self.name = name
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class SearchImageByPicResponseBodyPicInfo(TeaModel):
    def __init__(
        self,
        region: str = None,
        category_id: int = None,
        multi_region: List[SearchImageByPicResponseBodyPicInfoMultiRegion] = None,
        all_categories: List[SearchImageByPicResponseBodyPicInfoAllCategories] = None,
    ):
        self.region = region
        self.category_id = category_id
        self.multi_region = multi_region
        self.all_categories = all_categories

    def validate(self):
        if self.multi_region:
            for k in self.multi_region:
                if k:
                    k.validate()
        if self.all_categories:
            for k in self.all_categories:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region is not None:
            result['Region'] = self.region
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        result['MultiRegion'] = []
        if self.multi_region is not None:
            for k in self.multi_region:
                result['MultiRegion'].append(k.to_map() if k else None)
        result['AllCategories'] = []
        if self.all_categories is not None:
            for k in self.all_categories:
                result['AllCategories'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        self.multi_region = []
        if m.get('MultiRegion') is not None:
            for k in m.get('MultiRegion'):
                temp_model = SearchImageByPicResponseBodyPicInfoMultiRegion()
                self.multi_region.append(temp_model.from_map(k))
        self.all_categories = []
        if m.get('AllCategories') is not None:
            for k in m.get('AllCategories'):
                temp_model = SearchImageByPicResponseBodyPicInfoAllCategories()
                self.all_categories.append(temp_model.from_map(k))
        return self


class SearchImageByPicResponseBody(TeaModel):
    def __init__(
        self,
        msg: str = None,
        head: SearchImageByPicResponseBodyHead = None,
        request_id: str = None,
        auctions: List[SearchImageByPicResponseBodyAuctions] = None,
        code: int = None,
        pic_info: SearchImageByPicResponseBodyPicInfo = None,
        success: bool = None,
    ):
        self.msg = msg
        self.head = head
        self.request_id = request_id
        self.auctions = auctions
        self.code = code
        self.pic_info = pic_info
        self.success = success

    def validate(self):
        if self.head:
            self.head.validate()
        if self.auctions:
            for k in self.auctions:
                if k:
                    k.validate()
        if self.pic_info:
            self.pic_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.head is not None:
            result['Head'] = self.head.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Auctions'] = []
        if self.auctions is not None:
            for k in self.auctions:
                result['Auctions'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        if self.pic_info is not None:
            result['PicInfo'] = self.pic_info.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('Head') is not None:
            temp_model = SearchImageByPicResponseBodyHead()
            self.head = temp_model.from_map(m['Head'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.auctions = []
        if m.get('Auctions') is not None:
            for k in m.get('Auctions'):
                temp_model = SearchImageByPicResponseBodyAuctions()
                self.auctions.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('PicInfo') is not None:
            temp_model = SearchImageByPicResponseBodyPicInfo()
            self.pic_info = temp_model.from_map(m['PicInfo'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SearchImageByPicResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SearchImageByPicResponseBody = None,
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
            temp_model = SearchImageByPicResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


