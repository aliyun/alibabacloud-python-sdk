# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_imagesearch20201214 import models as main_models
from darabonba.model import DaraModel

class SearchImageByPicResponseBody(DaraModel):
    def __init__(
        self,
        auctions: List[main_models.SearchImageByPicResponseBodyAuctions] = None,
        code: int = None,
        head: main_models.SearchImageByPicResponseBodyHead = None,
        msg: str = None,
        pic_info: main_models.SearchImageByPicResponseBodyPicInfo = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The descriptions of all returned products.
        self.auctions = auctions
        # The error code.
        # - 0: successful.
        # - Non-zero: failed.
        self.code = code
        # The overview of the search results.
        self.head = head
        # The error message.
        self.msg = msg
        # The information such as category prediction and subject identification results.
        self.pic_info = pic_info
        # The request ID.
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
                temp_model = main_models.SearchImageByPicResponseBodyAuctions()
                self.auctions.append(temp_model.from_map(k1))

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Head') is not None:
            temp_model = main_models.SearchImageByPicResponseBodyHead()
            self.head = temp_model.from_map(m.get('Head'))

        if m.get('Msg') is not None:
            self.msg = m.get('Msg')

        if m.get('PicInfo') is not None:
            temp_model = main_models.SearchImageByPicResponseBodyPicInfo()
            self.pic_info = temp_model.from_map(m.get('PicInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class SearchImageByPicResponseBodyPicInfo(DaraModel):
    def __init__(
        self,
        all_categories: List[main_models.SearchImageByPicResponseBodyPicInfoAllCategories] = None,
        category_id: int = None,
        multi_region: List[main_models.SearchImageByPicResponseBodyPicInfoMultiRegion] = None,
        region: str = None,
    ):
        # The information about all categories supported by the system.
        self.all_categories = all_categories
        # The category prediction result. If the category is specified in the request, the value specified in the request is used.
        self.category_id = category_id
        # The collection of subject identification results.
        # > You must upgrade to V3.1.1 to use this feature.
        self.multi_region = multi_region
        # The subject identification result. The subject region of the image, in the format of x1,x2,y1,y2, where x1,y1 is the upper-left point and x2,y2 is the lower-right point. If the subject region is specified in the request, the value specified in the request is used.
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
                temp_model = main_models.SearchImageByPicResponseBodyPicInfoAllCategories()
                self.all_categories.append(temp_model.from_map(k1))

        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')

        self.multi_region = []
        if m.get('MultiRegion') is not None:
            for k1 in m.get('MultiRegion'):
                temp_model = main_models.SearchImageByPicResponseBodyPicInfoMultiRegion()
                self.multi_region.append(temp_model.from_map(k1))

        if m.get('Region') is not None:
            self.region = m.get('Region')

        return self

class SearchImageByPicResponseBodyPicInfoMultiRegion(DaraModel):
    def __init__(
        self,
        region: str = None,
    ):
        # The subject identification result. The subject region of the image, in the format of x1,x2,y1,y2, where x1,y1 is the upper-left point and x2,y2 is the lower-right point. If the subject region is specified in the request, the value specified in the request is used.
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

class SearchImageByPicResponseBodyPicInfoAllCategories(DaraModel):
    def __init__(
        self,
        id: int = None,
        name: str = None,
    ):
        # The category ID.
        self.id = id
        # The category name.
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

class SearchImageByPicResponseBodyHead(DaraModel):
    def __init__(
        self,
        docs_found: int = None,
        docs_return: int = None,
        search_time: int = None,
    ):
        # The number of results returned.
        self.docs_found = docs_found
        # The number of results matched in the instance.
        self.docs_return = docs_return
        # The search duration, in milliseconds.
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

class SearchImageByPicResponseBodyAuctions(DaraModel):
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
        # The image category.
        self.category_id = category_id
        # The user-defined content.
        self.custom_content = custom_content
        # The integer type attribute.
        self.int_attr = int_attr
        # The integer type attribute.
        self.int_attr_2 = int_attr_2
        # The integer type attribute.
        self.int_attr_3 = int_attr_3
        # The integer type attribute.
        self.int_attr_4 = int_attr_4
        # The image name.
        self.pic_name = pic_name
        # The product ID.
        self.product_id = product_id
        # The image similarity score. Valid values: 0 to 1.
        # > You must upgrade to V3.1.1 to use this feature.
        self.score = score
        # The system scoring information.
        # > - This field is deprecated. Use Score instead. 
        # - SortExprValues is a semicolon-separated tuple. The first value indicates the relevance score of the image. A higher value indicates higher relevance to the query image. The scoring varies depending on the algorithm model.
        # - When the category is 0 to 2, the value range of SortExprValues is 0 to 7.33136443711219e+24.
        # - For other category values, the value range of SortExprValues is 0 to 5.37633353624177e+24. This score reaches its maximum when two images are identical.
        self.sort_expr_values = sort_expr_values
        # The string type attribute.
        self.str_attr = str_attr
        # The string type attribute.
        self.str_attr_2 = str_attr_2
        # The string type attribute.
        self.str_attr_3 = str_attr_3
        # The string type attribute.
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

