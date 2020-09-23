# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, BinaryIO


class SearchImageByNameRequest(TeaModel):
    def __init__(self, category_id=None, instance_name=None, product_id=None, pic_name=None, num=None, start=None,
                 filter=None):
        self.category_id = category_id  # type: int
        self.instance_name = instance_name  # type: str
        self.product_id = product_id    # type: str
        self.pic_name = pic_name        # type: str
        self.num = num                  # type: int
        self.start = start              # type: int
        self.filter = filter            # type: str

    def validate(self):
        self.validate_required(self.instance_name, 'instance_name')
        self.validate_required(self.product_id, 'product_id')
        self.validate_required(self.pic_name, 'pic_name')

    def to_map(self):
        result = {}
        result['CategoryId'] = self.category_id
        result['InstanceName'] = self.instance_name
        result['ProductId'] = self.product_id
        result['PicName'] = self.pic_name
        result['Num'] = self.num
        result['Start'] = self.start
        result['Filter'] = self.filter
        return result

    def from_map(self, map={}):
        self.category_id = map.get('CategoryId')
        self.instance_name = map.get('InstanceName')
        self.product_id = map.get('ProductId')
        self.pic_name = map.get('PicName')
        self.num = map.get('Num')
        self.start = map.get('Start')
        self.filter = map.get('Filter')
        return self


class SearchImageByNameResponse(TeaModel):
    def __init__(self, request_id=None, success=None, code=None, msg=None, auctions=None, head=None, pic_info=None):
        self.request_id = request_id    # type: str
        self.success = success          # type: bool
        self.code = code                # type: int
        self.msg = msg                  # type: str
        self.auctions = auctions        # type: List[SearchImageByNameResponseAuctions]
        self.head = head                # type: SearchImageByNameResponseHead
        self.pic_info = pic_info        # type: SearchImageByNameResponsePicInfo

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.code, 'code')
        self.validate_required(self.msg, 'msg')
        self.validate_required(self.auctions, 'auctions')
        if self.auctions:
            for k in self.auctions:
                if k:
                    k.validate()
        self.validate_required(self.head, 'head')
        if self.head:
            self.head.validate()
        self.validate_required(self.pic_info, 'pic_info')
        if self.pic_info:
            self.pic_info.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        result['Code'] = self.code
        result['Msg'] = self.msg
        result['Auctions'] = []
        if self.auctions is not None:
            for k in self.auctions:
                result['Auctions'].append(k.to_map() if k else None)
        else:
            result['Auctions'] = None
        if self.head is not None:
            result['Head'] = self.head.to_map()
        else:
            result['Head'] = None
        if self.pic_info is not None:
            result['PicInfo'] = self.pic_info.to_map()
        else:
            result['PicInfo'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        self.code = map.get('Code')
        self.msg = map.get('Msg')
        self.auctions = []
        if map.get('Auctions') is not None:
            for k in map.get('Auctions'):
                temp_model = SearchImageByNameResponseAuctions()
                self.auctions.append(temp_model.from_map(k))
        else:
            self.auctions = None
        if map.get('Head') is not None:
            temp_model = SearchImageByNameResponseHead()
            self.head = temp_model.from_map(map['Head'])
        else:
            self.head = None
        if map.get('PicInfo') is not None:
            temp_model = SearchImageByNameResponsePicInfo()
            self.pic_info = temp_model.from_map(map['PicInfo'])
        else:
            self.pic_info = None
        return self


class SearchImageByNameResponseAuctions(TeaModel):
    def __init__(self, category_id=None, product_id=None, pic_name=None, custom_content=None, sort_expr_values=None,
                 int_attr=None, str_attr=None):
        self.category_id = category_id  # type: int
        self.product_id = product_id    # type: str
        self.pic_name = pic_name        # type: str
        self.custom_content = custom_content  # type: str
        self.sort_expr_values = sort_expr_values  # type: str
        self.int_attr = int_attr        # type: int
        self.str_attr = str_attr        # type: str

    def validate(self):
        self.validate_required(self.category_id, 'category_id')
        self.validate_required(self.product_id, 'product_id')
        self.validate_required(self.pic_name, 'pic_name')
        self.validate_required(self.custom_content, 'custom_content')
        self.validate_required(self.sort_expr_values, 'sort_expr_values')
        self.validate_required(self.int_attr, 'int_attr')
        self.validate_required(self.str_attr, 'str_attr')

    def to_map(self):
        result = {}
        result['CategoryId'] = self.category_id
        result['ProductId'] = self.product_id
        result['PicName'] = self.pic_name
        result['CustomContent'] = self.custom_content
        result['SortExprValues'] = self.sort_expr_values
        result['IntAttr'] = self.int_attr
        result['StrAttr'] = self.str_attr
        return result

    def from_map(self, map={}):
        self.category_id = map.get('CategoryId')
        self.product_id = map.get('ProductId')
        self.pic_name = map.get('PicName')
        self.custom_content = map.get('CustomContent')
        self.sort_expr_values = map.get('SortExprValues')
        self.int_attr = map.get('IntAttr')
        self.str_attr = map.get('StrAttr')
        return self


class SearchImageByNameResponseHead(TeaModel):
    def __init__(self, docs_return=None, docs_found=None, search_time=None):
        self.docs_return = docs_return  # type: int
        self.docs_found = docs_found    # type: int
        self.search_time = search_time  # type: int

    def validate(self):
        self.validate_required(self.docs_return, 'docs_return')
        self.validate_required(self.docs_found, 'docs_found')
        self.validate_required(self.search_time, 'search_time')

    def to_map(self):
        result = {}
        result['DocsReturn'] = self.docs_return
        result['DocsFound'] = self.docs_found
        result['SearchTime'] = self.search_time
        return result

    def from_map(self, map={}):
        self.docs_return = map.get('DocsReturn')
        self.docs_found = map.get('DocsFound')
        self.search_time = map.get('SearchTime')
        return self


class SearchImageByNameResponsePicInfoAllCategories(TeaModel):
    def __init__(self, id=None, name=None):
        self.id = id                    # type: int
        self.name = name                # type: str

    def validate(self):
        self.validate_required(self.id, 'id')
        self.validate_required(self.name, 'name')

    def to_map(self):
        result = {}
        result['Id'] = self.id
        result['Name'] = self.name
        return result

    def from_map(self, map={}):
        self.id = map.get('Id')
        self.name = map.get('Name')
        return self


class SearchImageByNameResponsePicInfo(TeaModel):
    def __init__(self, category_id=None, region=None, all_categories=None):
        self.category_id = category_id  # type: int
        self.region = region            # type: str
        self.all_categories = all_categories  # type: List[SearchImageByNameResponsePicInfoAllCategories]

    def validate(self):
        self.validate_required(self.category_id, 'category_id')
        self.validate_required(self.region, 'region')
        self.validate_required(self.all_categories, 'all_categories')
        if self.all_categories:
            for k in self.all_categories:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['CategoryId'] = self.category_id
        result['Region'] = self.region
        result['AllCategories'] = []
        if self.all_categories is not None:
            for k in self.all_categories:
                result['AllCategories'].append(k.to_map() if k else None)
        else:
            result['AllCategories'] = None
        return result

    def from_map(self, map={}):
        self.category_id = map.get('CategoryId')
        self.region = map.get('Region')
        self.all_categories = []
        if map.get('AllCategories') is not None:
            for k in map.get('AllCategories'):
                temp_model = SearchImageByNameResponsePicInfoAllCategories()
                self.all_categories.append(temp_model.from_map(k))
        else:
            self.all_categories = None
        return self


class SearchImageByPicRequest(TeaModel):
    def __init__(self, category_id=None, instance_name=None, pic_content=None, crop=None, region=None, num=None,
                 start=None, filter=None):
        self.category_id = category_id  # type: int
        self.instance_name = instance_name  # type: str
        self.pic_content = pic_content  # type: str
        self.crop = crop                # type: bool
        self.region = region            # type: str
        self.num = num                  # type: int
        self.start = start              # type: int
        self.filter = filter            # type: str

    def validate(self):
        self.validate_required(self.instance_name, 'instance_name')
        self.validate_required(self.pic_content, 'pic_content')

    def to_map(self):
        result = {}
        result['CategoryId'] = self.category_id
        result['InstanceName'] = self.instance_name
        result['PicContent'] = self.pic_content
        result['Crop'] = self.crop
        result['Region'] = self.region
        result['Num'] = self.num
        result['Start'] = self.start
        result['Filter'] = self.filter
        return result

    def from_map(self, map={}):
        self.category_id = map.get('CategoryId')
        self.instance_name = map.get('InstanceName')
        self.pic_content = map.get('PicContent')
        self.crop = map.get('Crop')
        self.region = map.get('Region')
        self.num = map.get('Num')
        self.start = map.get('Start')
        self.filter = map.get('Filter')
        return self


class SearchImageByPicResponse(TeaModel):
    def __init__(self, request_id=None, success=None, code=None, msg=None, auctions=None, head=None, pic_info=None):
        self.request_id = request_id    # type: str
        self.success = success          # type: bool
        self.code = code                # type: int
        self.msg = msg                  # type: str
        self.auctions = auctions        # type: List[SearchImageByPicResponseAuctions]
        self.head = head                # type: SearchImageByPicResponseHead
        self.pic_info = pic_info        # type: SearchImageByPicResponsePicInfo

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.code, 'code')
        self.validate_required(self.msg, 'msg')
        self.validate_required(self.auctions, 'auctions')
        if self.auctions:
            for k in self.auctions:
                if k:
                    k.validate()
        self.validate_required(self.head, 'head')
        if self.head:
            self.head.validate()
        self.validate_required(self.pic_info, 'pic_info')
        if self.pic_info:
            self.pic_info.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        result['Code'] = self.code
        result['Msg'] = self.msg
        result['Auctions'] = []
        if self.auctions is not None:
            for k in self.auctions:
                result['Auctions'].append(k.to_map() if k else None)
        else:
            result['Auctions'] = None
        if self.head is not None:
            result['Head'] = self.head.to_map()
        else:
            result['Head'] = None
        if self.pic_info is not None:
            result['PicInfo'] = self.pic_info.to_map()
        else:
            result['PicInfo'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        self.code = map.get('Code')
        self.msg = map.get('Msg')
        self.auctions = []
        if map.get('Auctions') is not None:
            for k in map.get('Auctions'):
                temp_model = SearchImageByPicResponseAuctions()
                self.auctions.append(temp_model.from_map(k))
        else:
            self.auctions = None
        if map.get('Head') is not None:
            temp_model = SearchImageByPicResponseHead()
            self.head = temp_model.from_map(map['Head'])
        else:
            self.head = None
        if map.get('PicInfo') is not None:
            temp_model = SearchImageByPicResponsePicInfo()
            self.pic_info = temp_model.from_map(map['PicInfo'])
        else:
            self.pic_info = None
        return self


class SearchImageByPicResponseAuctions(TeaModel):
    def __init__(self, category_id=None, product_id=None, pic_name=None, custom_content=None, sort_expr_values=None,
                 int_attr=None, str_attr=None):
        self.category_id = category_id  # type: int
        self.product_id = product_id    # type: str
        self.pic_name = pic_name        # type: str
        self.custom_content = custom_content  # type: str
        self.sort_expr_values = sort_expr_values  # type: str
        self.int_attr = int_attr        # type: int
        self.str_attr = str_attr        # type: str

    def validate(self):
        self.validate_required(self.category_id, 'category_id')
        self.validate_required(self.product_id, 'product_id')
        self.validate_required(self.pic_name, 'pic_name')
        self.validate_required(self.custom_content, 'custom_content')
        self.validate_required(self.sort_expr_values, 'sort_expr_values')
        self.validate_required(self.int_attr, 'int_attr')
        self.validate_required(self.str_attr, 'str_attr')

    def to_map(self):
        result = {}
        result['CategoryId'] = self.category_id
        result['ProductId'] = self.product_id
        result['PicName'] = self.pic_name
        result['CustomContent'] = self.custom_content
        result['SortExprValues'] = self.sort_expr_values
        result['IntAttr'] = self.int_attr
        result['StrAttr'] = self.str_attr
        return result

    def from_map(self, map={}):
        self.category_id = map.get('CategoryId')
        self.product_id = map.get('ProductId')
        self.pic_name = map.get('PicName')
        self.custom_content = map.get('CustomContent')
        self.sort_expr_values = map.get('SortExprValues')
        self.int_attr = map.get('IntAttr')
        self.str_attr = map.get('StrAttr')
        return self


class SearchImageByPicResponseHead(TeaModel):
    def __init__(self, docs_return=None, docs_found=None, search_time=None):
        self.docs_return = docs_return  # type: int
        self.docs_found = docs_found    # type: int
        self.search_time = search_time  # type: int

    def validate(self):
        self.validate_required(self.docs_return, 'docs_return')
        self.validate_required(self.docs_found, 'docs_found')
        self.validate_required(self.search_time, 'search_time')

    def to_map(self):
        result = {}
        result['DocsReturn'] = self.docs_return
        result['DocsFound'] = self.docs_found
        result['SearchTime'] = self.search_time
        return result

    def from_map(self, map={}):
        self.docs_return = map.get('DocsReturn')
        self.docs_found = map.get('DocsFound')
        self.search_time = map.get('SearchTime')
        return self


class SearchImageByPicResponsePicInfoAllCategories(TeaModel):
    def __init__(self, id=None, name=None):
        self.id = id                    # type: int
        self.name = name                # type: str

    def validate(self):
        self.validate_required(self.id, 'id')
        self.validate_required(self.name, 'name')

    def to_map(self):
        result = {}
        result['Id'] = self.id
        result['Name'] = self.name
        return result

    def from_map(self, map={}):
        self.id = map.get('Id')
        self.name = map.get('Name')
        return self


class SearchImageByPicResponsePicInfo(TeaModel):
    def __init__(self, category_id=None, region=None, all_categories=None):
        self.category_id = category_id  # type: int
        self.region = region            # type: str
        self.all_categories = all_categories  # type: List[SearchImageByPicResponsePicInfoAllCategories]

    def validate(self):
        self.validate_required(self.category_id, 'category_id')
        self.validate_required(self.region, 'region')
        self.validate_required(self.all_categories, 'all_categories')
        if self.all_categories:
            for k in self.all_categories:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['CategoryId'] = self.category_id
        result['Region'] = self.region
        result['AllCategories'] = []
        if self.all_categories is not None:
            for k in self.all_categories:
                result['AllCategories'].append(k.to_map() if k else None)
        else:
            result['AllCategories'] = None
        return result

    def from_map(self, map={}):
        self.category_id = map.get('CategoryId')
        self.region = map.get('Region')
        self.all_categories = []
        if map.get('AllCategories') is not None:
            for k in map.get('AllCategories'):
                temp_model = SearchImageByPicResponsePicInfoAllCategories()
                self.all_categories.append(temp_model.from_map(k))
        else:
            self.all_categories = None
        return self


class SearchImageByPicAdvanceRequest(TeaModel):
    def __init__(self, pic_content_object=None, category_id=None, instance_name=None, crop=None, region=None,
                 num=None, start=None, filter=None):
        self.pic_content_object = pic_content_object  # type: BinaryIO
        self.category_id = category_id  # type: int
        self.instance_name = instance_name  # type: str
        self.crop = crop                # type: bool
        self.region = region            # type: str
        self.num = num                  # type: int
        self.start = start              # type: int
        self.filter = filter            # type: str

    def validate(self):
        self.validate_required(self.pic_content_object, 'pic_content_object')
        self.validate_required(self.instance_name, 'instance_name')

    def to_map(self):
        result = {}
        result['PicContentObject'] = self.pic_content_object
        result['CategoryId'] = self.category_id
        result['InstanceName'] = self.instance_name
        result['Crop'] = self.crop
        result['Region'] = self.region
        result['Num'] = self.num
        result['Start'] = self.start
        result['Filter'] = self.filter
        return result

    def from_map(self, map={}):
        self.pic_content_object = map.get('PicContentObject')
        self.category_id = map.get('CategoryId')
        self.instance_name = map.get('InstanceName')
        self.crop = map.get('Crop')
        self.region = map.get('Region')
        self.num = map.get('Num')
        self.start = map.get('Start')
        self.filter = map.get('Filter')
        return self


class DeleteImageRequest(TeaModel):
    def __init__(self, instance_name=None, product_id=None, pic_name=None):
        self.instance_name = instance_name  # type: str
        self.product_id = product_id    # type: str
        self.pic_name = pic_name        # type: str

    def validate(self):
        self.validate_required(self.instance_name, 'instance_name')
        self.validate_required(self.product_id, 'product_id')

    def to_map(self):
        result = {}
        result['InstanceName'] = self.instance_name
        result['ProductId'] = self.product_id
        result['PicName'] = self.pic_name
        return result

    def from_map(self, map={}):
        self.instance_name = map.get('InstanceName')
        self.product_id = map.get('ProductId')
        self.pic_name = map.get('PicName')
        return self


class DeleteImageResponse(TeaModel):
    def __init__(self, request_id=None, success=None, message=None, code=None):
        self.request_id = request_id    # type: str
        self.success = success          # type: bool
        self.message = message          # type: str
        self.code = code                # type: int

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.message, 'message')
        self.validate_required(self.code, 'code')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        result['Message'] = self.message
        result['Code'] = self.code
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        self.message = map.get('Message')
        self.code = map.get('Code')
        return self


class AddImageRequest(TeaModel):
    def __init__(self, instance_name=None, category_id=None, product_id=None, pic_name=None, pic_content=None,
                 crop=None, region=None, custom_content=None, int_attr=None, str_attr=None):
        self.instance_name = instance_name  # type: str
        self.category_id = category_id  # type: int
        self.product_id = product_id    # type: str
        self.pic_name = pic_name        # type: str
        self.pic_content = pic_content  # type: str
        self.crop = crop                # type: bool
        self.region = region            # type: str
        self.custom_content = custom_content  # type: str
        self.int_attr = int_attr        # type: int
        self.str_attr = str_attr        # type: str

    def validate(self):
        self.validate_required(self.instance_name, 'instance_name')
        self.validate_required(self.product_id, 'product_id')
        self.validate_required(self.pic_name, 'pic_name')
        self.validate_required(self.pic_content, 'pic_content')

    def to_map(self):
        result = {}
        result['InstanceName'] = self.instance_name
        result['CategoryId'] = self.category_id
        result['ProductId'] = self.product_id
        result['PicName'] = self.pic_name
        result['PicContent'] = self.pic_content
        result['Crop'] = self.crop
        result['Region'] = self.region
        result['CustomContent'] = self.custom_content
        result['IntAttr'] = self.int_attr
        result['StrAttr'] = self.str_attr
        return result

    def from_map(self, map={}):
        self.instance_name = map.get('InstanceName')
        self.category_id = map.get('CategoryId')
        self.product_id = map.get('ProductId')
        self.pic_name = map.get('PicName')
        self.pic_content = map.get('PicContent')
        self.crop = map.get('Crop')
        self.region = map.get('Region')
        self.custom_content = map.get('CustomContent')
        self.int_attr = map.get('IntAttr')
        self.str_attr = map.get('StrAttr')
        return self


class AddImageResponse(TeaModel):
    def __init__(self, request_id=None, success=None, message=None, code=None, pic_info=None):
        self.request_id = request_id    # type: str
        self.success = success          # type: bool
        self.message = message          # type: str
        self.code = code                # type: int
        self.pic_info = pic_info        # type: AddImageResponsePicInfo

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.message, 'message')
        self.validate_required(self.code, 'code')
        self.validate_required(self.pic_info, 'pic_info')
        if self.pic_info:
            self.pic_info.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        result['Message'] = self.message
        result['Code'] = self.code
        if self.pic_info is not None:
            result['PicInfo'] = self.pic_info.to_map()
        else:
            result['PicInfo'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        self.message = map.get('Message')
        self.code = map.get('Code')
        if map.get('PicInfo') is not None:
            temp_model = AddImageResponsePicInfo()
            self.pic_info = temp_model.from_map(map['PicInfo'])
        else:
            self.pic_info = None
        return self


class AddImageResponsePicInfo(TeaModel):
    def __init__(self, category_id=None, region=None):
        self.category_id = category_id  # type: int
        self.region = region            # type: str

    def validate(self):
        self.validate_required(self.category_id, 'category_id')
        self.validate_required(self.region, 'region')

    def to_map(self):
        result = {}
        result['CategoryId'] = self.category_id
        result['Region'] = self.region
        return result

    def from_map(self, map={}):
        self.category_id = map.get('CategoryId')
        self.region = map.get('Region')
        return self


class AddImageAdvanceRequest(TeaModel):
    def __init__(self, pic_content_object=None, instance_name=None, category_id=None, product_id=None,
                 pic_name=None, crop=None, region=None, custom_content=None, int_attr=None, str_attr=None):
        self.pic_content_object = pic_content_object  # type: BinaryIO
        self.instance_name = instance_name  # type: str
        self.category_id = category_id  # type: int
        self.product_id = product_id    # type: str
        self.pic_name = pic_name        # type: str
        self.crop = crop                # type: bool
        self.region = region            # type: str
        self.custom_content = custom_content  # type: str
        self.int_attr = int_attr        # type: int
        self.str_attr = str_attr        # type: str

    def validate(self):
        self.validate_required(self.pic_content_object, 'pic_content_object')
        self.validate_required(self.instance_name, 'instance_name')
        self.validate_required(self.product_id, 'product_id')
        self.validate_required(self.pic_name, 'pic_name')

    def to_map(self):
        result = {}
        result['PicContentObject'] = self.pic_content_object
        result['InstanceName'] = self.instance_name
        result['CategoryId'] = self.category_id
        result['ProductId'] = self.product_id
        result['PicName'] = self.pic_name
        result['Crop'] = self.crop
        result['Region'] = self.region
        result['CustomContent'] = self.custom_content
        result['IntAttr'] = self.int_attr
        result['StrAttr'] = self.str_attr
        return result

    def from_map(self, map={}):
        self.pic_content_object = map.get('PicContentObject')
        self.instance_name = map.get('InstanceName')
        self.category_id = map.get('CategoryId')
        self.product_id = map.get('ProductId')
        self.pic_name = map.get('PicName')
        self.crop = map.get('Crop')
        self.region = map.get('Region')
        self.custom_content = map.get('CustomContent')
        self.int_attr = map.get('IntAttr')
        self.str_attr = map.get('StrAttr')
        return self
