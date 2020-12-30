# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import BinaryIO, List, Dict


class ClassifyCommodityRequest(TeaModel):
    def __init__(
        self,
        image_url: str = None,
    ):
        self.image_url = image_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        return self


class ClassifyCommodityAdvanceRequest(TeaModel):
    def __init__(
        self,
        image_urlobject: BinaryIO = None,
    ):
        self.image_urlobject = image_urlobject

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        result = dict()
        if self.image_urlobject is not None:
            result['ImageURLObject'] = self.image_urlobject
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURLObject') is not None:
            self.image_urlobject = m.get('ImageURLObject')
        return self


class ClassifyCommodityResponseBodyDataCategories(TeaModel):
    def __init__(
        self,
        score: float = None,
        category_id: str = None,
        category_name: str = None,
    ):
        self.score = score
        self.category_id = category_id
        self.category_name = category_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.score is not None:
            result['Score'] = self.score
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.category_name is not None:
            result['CategoryName'] = self.category_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('CategoryName') is not None:
            self.category_name = m.get('CategoryName')
        return self


class ClassifyCommodityResponseBodyData(TeaModel):
    def __init__(
        self,
        categories: List[ClassifyCommodityResponseBodyDataCategories] = None,
    ):
        self.categories = categories

    def validate(self):
        if self.categories:
            for k in self.categories:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Categories'] = []
        if self.categories is not None:
            for k in self.categories:
                result['Categories'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.categories = []
        if m.get('Categories') is not None:
            for k in m.get('Categories'):
                temp_model = ClassifyCommodityResponseBodyDataCategories()
                self.categories.append(temp_model.from_map(k))
        return self


class ClassifyCommodityResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: ClassifyCommodityResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = ClassifyCommodityResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class ClassifyCommodityResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ClassifyCommodityResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = ClassifyCommodityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeFurnitureAttributeRequest(TeaModel):
    def __init__(
        self,
        image_url: str = None,
    ):
        self.image_url = image_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        return self


class RecognizeFurnitureAttributeAdvanceRequest(TeaModel):
    def __init__(
        self,
        image_urlobject: BinaryIO = None,
    ):
        self.image_urlobject = image_urlobject

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        result = dict()
        if self.image_urlobject is not None:
            result['ImageURLObject'] = self.image_urlobject
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURLObject') is not None:
            self.image_urlobject = m.get('ImageURLObject')
        return self


class RecognizeFurnitureAttributeResponseBodyData(TeaModel):
    def __init__(
        self,
        pred_style: str = None,
        pred_probability: float = None,
        pred_style_id: str = None,
    ):
        self.pred_style = pred_style
        self.pred_probability = pred_probability
        self.pred_style_id = pred_style_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.pred_style is not None:
            result['PredStyle'] = self.pred_style
        if self.pred_probability is not None:
            result['PredProbability'] = self.pred_probability
        if self.pred_style_id is not None:
            result['PredStyleId'] = self.pred_style_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PredStyle') is not None:
            self.pred_style = m.get('PredStyle')
        if m.get('PredProbability') is not None:
            self.pred_probability = m.get('PredProbability')
        if m.get('PredStyleId') is not None:
            self.pred_style_id = m.get('PredStyleId')
        return self


class RecognizeFurnitureAttributeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: RecognizeFurnitureAttributeResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = RecognizeFurnitureAttributeResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class RecognizeFurnitureAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RecognizeFurnitureAttributeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = RecognizeFurnitureAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeFurnitureSpuRequest(TeaModel):
    def __init__(
        self,
        image_url: str = None,
        xlength: float = None,
        ylength: float = None,
        zlength: float = None,
    ):
        self.image_url = image_url
        self.xlength = xlength
        self.ylength = ylength
        self.zlength = zlength

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        if self.xlength is not None:
            result['XLength'] = self.xlength
        if self.ylength is not None:
            result['YLength'] = self.ylength
        if self.zlength is not None:
            result['ZLength'] = self.zlength
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        if m.get('XLength') is not None:
            self.xlength = m.get('XLength')
        if m.get('YLength') is not None:
            self.ylength = m.get('YLength')
        if m.get('ZLength') is not None:
            self.zlength = m.get('ZLength')
        return self


class RecognizeFurnitureSpuAdvanceRequest(TeaModel):
    def __init__(
        self,
        image_urlobject: BinaryIO = None,
        xlength: float = None,
        ylength: float = None,
        zlength: float = None,
    ):
        self.image_urlobject = image_urlobject
        self.xlength = xlength
        self.ylength = ylength
        self.zlength = zlength

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        result = dict()
        if self.image_urlobject is not None:
            result['ImageURLObject'] = self.image_urlobject
        if self.xlength is not None:
            result['XLength'] = self.xlength
        if self.ylength is not None:
            result['YLength'] = self.ylength
        if self.zlength is not None:
            result['ZLength'] = self.zlength
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURLObject') is not None:
            self.image_urlobject = m.get('ImageURLObject')
        if m.get('XLength') is not None:
            self.xlength = m.get('XLength')
        if m.get('YLength') is not None:
            self.ylength = m.get('YLength')
        if m.get('ZLength') is not None:
            self.zlength = m.get('ZLength')
        return self


class RecognizeFurnitureSpuResponseBodyData(TeaModel):
    def __init__(
        self,
        pred_cate_id: str = None,
        pred_cate: str = None,
        pred_probability: float = None,
    ):
        self.pred_cate_id = pred_cate_id
        self.pred_cate = pred_cate
        self.pred_probability = pred_probability

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.pred_cate_id is not None:
            result['PredCateId'] = self.pred_cate_id
        if self.pred_cate is not None:
            result['PredCate'] = self.pred_cate
        if self.pred_probability is not None:
            result['PredProbability'] = self.pred_probability
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PredCateId') is not None:
            self.pred_cate_id = m.get('PredCateId')
        if m.get('PredCate') is not None:
            self.pred_cate = m.get('PredCate')
        if m.get('PredProbability') is not None:
            self.pred_probability = m.get('PredProbability')
        return self


class RecognizeFurnitureSpuResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: RecognizeFurnitureSpuResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = RecognizeFurnitureSpuResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class RecognizeFurnitureSpuResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RecognizeFurnitureSpuResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = RecognizeFurnitureSpuResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


