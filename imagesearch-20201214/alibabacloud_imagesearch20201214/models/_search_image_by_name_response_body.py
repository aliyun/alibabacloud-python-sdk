# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_imagesearch20201214 import models as main_models
from darabonba.model import DaraModel

class SearchImageByNameResponseBody(DaraModel):
    def __init__(
        self,
        auctions: List[main_models.SearchImageByNameResponseBodyAuctions] = None,
        code: int = None,
        head: main_models.SearchImageByNameResponseBodyHead = None,
        msg: str = None,
        pic_info: main_models.SearchImageByNameResponseBodyPicInfo = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The product descriptions returned.
        self.auctions = auctions
        # The error code returned.
        # 
        # *   A value of 0 indicates that the operation is successful.
        # *   Values other than 0 indicate errors.
        self.code = code
        # The summary of the search result.
        self.head = head
        # The error message returned.
        self.msg = msg
        # The information such as the system-selected category and result of subject recognition.
        self.pic_info = pic_info
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request is successful.
        self.success = success

    def validate(self):
        if self.auctions:
            for v1 in self.auctions:
                 if v1:
                    v1.validate()
        if self.head:
            self.head.validate()
        if self.pic_info:
            self.pic_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Auctions'] = []
        if self.auctions is not None:
            for k1 in self.auctions:
                result['Auctions'].append(k1.to_map() if k1 else None)

        if self.code is not None:
            result['Code'] = self.code

        if self.head is not None:
            result['Head'] = self.head.to_map()

        if self.msg is not None:
            result['Msg'] = self.msg

        if self.pic_info is not None:
            result['PicInfo'] = self.pic_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.auctions = []
        if m.get('Auctions') is not None:
            for k1 in m.get('Auctions'):
                temp_model = main_models.SearchImageByNameResponseBodyAuctions()
                self.auctions.append(temp_model.from_map(k1))

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Head') is not None:
            temp_model = main_models.SearchImageByNameResponseBodyHead()
            self.head = temp_model.from_map(m.get('Head'))

        if m.get('Msg') is not None:
            self.msg = m.get('Msg')

        if m.get('PicInfo') is not None:
            temp_model = main_models.SearchImageByNameResponseBodyPicInfo()
            self.pic_info = temp_model.from_map(m.get('PicInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class SearchImageByNameResponseBodyPicInfo(DaraModel):
    def __init__(
        self,
        all_categories: List[main_models.SearchImageByNameResponseBodyPicInfoAllCategories] = None,
        category_id: int = None,
        multi_region: List[main_models.SearchImageByNameResponseBodyPicInfoMultiRegion] = None,
        region: str = None,
    ):
        # The categories that are supported by the system.
        self.all_categories = all_categories
        # The category selected by the system.
        # 
        # If a category is specified in the request, the specified category prevails.
        self.category_id = category_id
        # The recognized subjects.
        self.multi_region = multi_region
        # The result of subject recognition.
        # 
        # The subject area of the image, in the format of x1,x2,y1,y2. Specifically, x1 and y1 specify the upper-left pixel, and x2 and y2 specify the lower-right pixel. If a subject area is specified in the request, the specified subject area prevails.
        self.region = region

    def validate(self):
        if self.all_categories:
            for v1 in self.all_categories:
                 if v1:
                    v1.validate()
        if self.multi_region:
            for v1 in self.multi_region:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AllCategories'] = []
        if self.all_categories is not None:
            for k1 in self.all_categories:
                result['AllCategories'].append(k1.to_map() if k1 else None)

        if self.category_id is not None:
            result['CategoryId'] = self.category_id

        result['MultiRegion'] = []
        if self.multi_region is not None:
            for k1 in self.multi_region:
                result['MultiRegion'].append(k1.to_map() if k1 else None)

        if self.region is not None:
            result['Region'] = self.region

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.all_categories = []
        if m.get('AllCategories') is not None:
            for k1 in m.get('AllCategories'):
                temp_model = main_models.SearchImageByNameResponseBodyPicInfoAllCategories()
                self.all_categories.append(temp_model.from_map(k1))

        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')

        self.multi_region = []
        if m.get('MultiRegion') is not None:
            for k1 in m.get('MultiRegion'):
                temp_model = main_models.SearchImageByNameResponseBodyPicInfoMultiRegion()
                self.multi_region.append(temp_model.from_map(k1))

        if m.get('Region') is not None:
            self.region = m.get('Region')

        return self

class SearchImageByNameResponseBodyPicInfoMultiRegion(DaraModel):
    def __init__(
        self,
        region: str = None,
    ):
        # The result of subject recognition.
        # 
        # The subject area of the image, in the format of x1,x2,y1,y2. Specifically, x1 and y1 specify the upper-left pixel, and x2 and y2 specify the lower-right pixel. If a subject area is specified in the request, the specified subject area prevails.
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region is not None:
            result['Region'] = self.region

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Region') is not None:
            self.region = m.get('Region')

        return self

class SearchImageByNameResponseBodyPicInfoAllCategories(DaraModel):
    def __init__(
        self,
        id: int = None,
        name: str = None,
    ):
        # The ID of the category.
        self.id = id
        # The name of the category.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class SearchImageByNameResponseBodyHead(DaraModel):
    def __init__(
        self,
        docs_found: int = None,
        docs_return: int = None,
        search_time: int = None,
    ):
        # The number of images returned.
        self.docs_found = docs_found
        # The number of images that match the search conditions on the Image Search instance.
        self.docs_return = docs_return
        # The time it takes to complete the search process. Unit: milliseconds.
        self.search_time = search_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

class SearchImageByNameResponseBodyAuctions(DaraModel):
    def __init__(
        self,
        category_id: int = None,
        custom_content: str = None,
        int_attr: int = None,
        int_attr_2: int = None,
        int_attr_3: int = None,
        int_attr_4: int = None,
        pic_name: str = None,
        product_id: str = None,
        score: float = None,
        sort_expr_values: str = None,
        str_attr: str = None,
        str_attr_2: str = None,
        str_attr_3: str = None,
        str_attr_4: str = None,
    ):
        # The category of the image.
        self.category_id = category_id
        # The user-defined content.
        self.custom_content = custom_content
        # The attribute, which is an integer.
        self.int_attr = int_attr
        self.int_attr_2 = int_attr_2
        self.int_attr_3 = int_attr_3
        self.int_attr_4 = int_attr_4
        # The name of the image.
        self.pic_name = pic_name
        # The ID of the product.
        self.product_id = product_id
        # The similarity score of the returned image. Valid values: 0 to 1.
        # 
        # >  To use this feature, you must upgrade the SDK to version 3.1.1.
        self.score = score
        # The score information about the image.
        # 
        # > *   This parameter is not supported. We recommend that you use the Score parameter.
        # >*   The SortExprValues parameter indicates a 2-tuple in which values are separated by a semicolon (;). The first value indicates the correlation score of the returned image. A greater value indicates a higher correlation with the sample image. Different algorithms are used.
        # >*   If the value of CategoryId is within the value range from 0 to 2, the value range of SortExprValues is from 0 to 7.33136443711219e+24.
        # >*   If the value of CategoryId is not within the value range from 0 to 2, the value range of SortExprValues is from 0 to 5.37633353624177e+24. If the returned image is identical with the sample image, the highest correlation score is generated.
        self.sort_expr_values = sort_expr_values
        # The attribute, which is a string.
        self.str_attr = str_attr
        self.str_attr_2 = str_attr_2
        self.str_attr_3 = str_attr_3
        self.str_attr_4 = str_attr_4

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category_id is not None:
            result['CategoryId'] = self.category_id

        if self.custom_content is not None:
            result['CustomContent'] = self.custom_content

        if self.int_attr is not None:
            result['IntAttr'] = self.int_attr

        if self.int_attr_2 is not None:
            result['IntAttr2'] = self.int_attr_2

        if self.int_attr_3 is not None:
            result['IntAttr3'] = self.int_attr_3

        if self.int_attr_4 is not None:
            result['IntAttr4'] = self.int_attr_4

        if self.pic_name is not None:
            result['PicName'] = self.pic_name

        if self.product_id is not None:
            result['ProductId'] = self.product_id

        if self.score is not None:
            result['Score'] = self.score

        if self.sort_expr_values is not None:
            result['SortExprValues'] = self.sort_expr_values

        if self.str_attr is not None:
            result['StrAttr'] = self.str_attr

        if self.str_attr_2 is not None:
            result['StrAttr2'] = self.str_attr_2

        if self.str_attr_3 is not None:
            result['StrAttr3'] = self.str_attr_3

        if self.str_attr_4 is not None:
            result['StrAttr4'] = self.str_attr_4

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')

        if m.get('CustomContent') is not None:
            self.custom_content = m.get('CustomContent')

        if m.get('IntAttr') is not None:
            self.int_attr = m.get('IntAttr')

        if m.get('IntAttr2') is not None:
            self.int_attr_2 = m.get('IntAttr2')

        if m.get('IntAttr3') is not None:
            self.int_attr_3 = m.get('IntAttr3')

        if m.get('IntAttr4') is not None:
            self.int_attr_4 = m.get('IntAttr4')

        if m.get('PicName') is not None:
            self.pic_name = m.get('PicName')

        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')

        if m.get('Score') is not None:
            self.score = m.get('Score')

        if m.get('SortExprValues') is not None:
            self.sort_expr_values = m.get('SortExprValues')

        if m.get('StrAttr') is not None:
            self.str_attr = m.get('StrAttr')

        if m.get('StrAttr2') is not None:
            self.str_attr_2 = m.get('StrAttr2')

        if m.get('StrAttr3') is not None:
            self.str_attr_3 = m.get('StrAttr3')

        if m.get('StrAttr4') is not None:
            self.str_attr_4 = m.get('StrAttr4')

        return self

