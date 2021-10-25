# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict, BinaryIO


class ImageCategoryRequest(TeaModel):
    def __init__(
        self,
        instance_name: str = None,
        pic_url: str = None,
    ):
        self.instance_name = instance_name
        self.pic_url = pic_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.pic_url is not None:
            result['PicUrl'] = self.pic_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('PicUrl') is not None:
            self.pic_url = m.get('PicUrl')
        return self


class ImageCategoryResponseBodyDataCateResult(TeaModel):
    def __init__(
        self,
        score: float = None,
        name: str = None,
        id: int = None,
    ):
        self.score = score
        self.name = name
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.score is not None:
            result['Score'] = self.score
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class ImageCategoryResponseBodyData(TeaModel):
    def __init__(
        self,
        cate_result: List[ImageCategoryResponseBodyDataCateResult] = None,
    ):
        self.cate_result = cate_result

    def validate(self):
        if self.cate_result:
            for k in self.cate_result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CateResult'] = []
        if self.cate_result is not None:
            for k in self.cate_result:
                result['CateResult'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cate_result = []
        if m.get('CateResult') is not None:
            for k in m.get('CateResult'):
                temp_model = ImageCategoryResponseBodyDataCateResult()
                self.cate_result.append(temp_model.from_map(k))
        return self


class ImageCategoryResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        data: ImageCategoryResponseBodyData = None,
        success: bool = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.data = data
        self.success = success
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.success is not None:
            result['Success'] = self.success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Data') is not None:
            temp_model = ImageCategoryResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ImageCategoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ImageCategoryResponseBody = None,
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
            temp_model = ImageCategoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GeneralRecognitionRequest(TeaModel):
    def __init__(
        self,
        instance_name: str = None,
        pic_content: str = None,
    ):
        self.instance_name = instance_name
        self.pic_content = pic_content

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('PicContent') is not None:
            self.pic_content = m.get('PicContent')
        return self


class GeneralRecognitionAdvanceRequest(TeaModel):
    def __init__(
        self,
        pic_content_object: BinaryIO = None,
        instance_name: str = None,
    ):
        self.pic_content_object = pic_content_object
        self.instance_name = instance_name

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PicContentObject') is not None:
            self.pic_content_object = m.get('PicContentObject')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        return self


class GeneralRecognitionResponseBodyDataResult(TeaModel):
    def __init__(
        self,
        tag: str = None,
        score: str = None,
    ):
        self.tag = tag
        self.score = score

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.score is not None:
            result['Score'] = self.score
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        return self


class GeneralRecognitionResponseBodyData(TeaModel):
    def __init__(
        self,
        result: List[GeneralRecognitionResponseBodyDataResult] = None,
        regions: List[str] = None,
    ):
        self.result = result
        self.regions = regions

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.regions is not None:
            result['Regions'] = self.regions
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = GeneralRecognitionResponseBodyDataResult()
                self.result.append(temp_model.from_map(k))
        if m.get('Regions') is not None:
            self.regions = m.get('Regions')
        return self


class GeneralRecognitionResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        data: GeneralRecognitionResponseBodyData = None,
        success: bool = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.data = data
        self.success = success
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.success is not None:
            result['Success'] = self.success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Data') is not None:
            temp_model = GeneralRecognitionResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GeneralRecognitionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GeneralRecognitionResponseBody = None,
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
            temp_model = GeneralRecognitionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ImagePropertyRequest(TeaModel):
    def __init__(
        self,
        instance_name: str = None,
        pic_url: str = None,
    ):
        self.instance_name = instance_name
        self.pic_url = pic_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.pic_url is not None:
            result['PicUrl'] = self.pic_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('PicUrl') is not None:
            self.pic_url = m.get('PicUrl')
        return self


class ImagePropertyResponseBodyDataPropertyResultsValues(TeaModel):
    def __init__(
        self,
        value_id: str = None,
        probability: float = None,
        value_name: str = None,
    ):
        self.value_id = value_id
        self.probability = probability
        self.value_name = value_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.value_id is not None:
            result['ValueId'] = self.value_id
        if self.probability is not None:
            result['Probability'] = self.probability
        if self.value_name is not None:
            result['ValueName'] = self.value_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ValueId') is not None:
            self.value_id = m.get('ValueId')
        if m.get('Probability') is not None:
            self.probability = m.get('Probability')
        if m.get('ValueName') is not None:
            self.value_name = m.get('ValueName')
        return self


class ImagePropertyResponseBodyDataPropertyResults(TeaModel):
    def __init__(
        self,
        property_name: str = None,
        property_id: str = None,
        values: List[ImagePropertyResponseBodyDataPropertyResultsValues] = None,
    ):
        self.property_name = property_name
        self.property_id = property_id
        self.values = values

    def validate(self):
        if self.values:
            for k in self.values:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.property_name is not None:
            result['PropertyName'] = self.property_name
        if self.property_id is not None:
            result['PropertyId'] = self.property_id
        result['Values'] = []
        if self.values is not None:
            for k in self.values:
                result['Values'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PropertyName') is not None:
            self.property_name = m.get('PropertyName')
        if m.get('PropertyId') is not None:
            self.property_id = m.get('PropertyId')
        self.values = []
        if m.get('Values') is not None:
            for k in m.get('Values'):
                temp_model = ImagePropertyResponseBodyDataPropertyResultsValues()
                self.values.append(temp_model.from_map(k))
        return self


class ImagePropertyResponseBodyData(TeaModel):
    def __init__(
        self,
        property_results: List[ImagePropertyResponseBodyDataPropertyResults] = None,
    ):
        self.property_results = property_results

    def validate(self):
        if self.property_results:
            for k in self.property_results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PropertyResults'] = []
        if self.property_results is not None:
            for k in self.property_results:
                result['PropertyResults'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.property_results = []
        if m.get('PropertyResults') is not None:
            for k in m.get('PropertyResults'):
                temp_model = ImagePropertyResponseBodyDataPropertyResults()
                self.property_results.append(temp_model.from_map(k))
        return self


class ImagePropertyResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        data: ImagePropertyResponseBodyData = None,
        success: bool = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.data = data
        self.success = success
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.success is not None:
            result['Success'] = self.success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Data') is not None:
            temp_model = ImagePropertyResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ImagePropertyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ImagePropertyResponseBody = None,
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
            temp_model = ImagePropertyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ImageDuplicationRequest(TeaModel):
    def __init__(
        self,
        instance_name: str = None,
        pic_url_list: str = None,
        pic_num_list: str = None,
        image_height: int = None,
        image_width: int = None,
        output_image_num: int = None,
    ):
        self.instance_name = instance_name
        self.pic_url_list = pic_url_list
        self.pic_num_list = pic_num_list
        self.image_height = image_height
        self.image_width = image_width
        self.output_image_num = output_image_num

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.pic_url_list is not None:
            result['PicUrlList'] = self.pic_url_list
        if self.pic_num_list is not None:
            result['PicNumList'] = self.pic_num_list
        if self.image_height is not None:
            result['ImageHeight'] = self.image_height
        if self.image_width is not None:
            result['ImageWidth'] = self.image_width
        if self.output_image_num is not None:
            result['OutputImageNum'] = self.output_image_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('PicUrlList') is not None:
            self.pic_url_list = m.get('PicUrlList')
        if m.get('PicNumList') is not None:
            self.pic_num_list = m.get('PicNumList')
        if m.get('ImageHeight') is not None:
            self.image_height = m.get('ImageHeight')
        if m.get('ImageWidth') is not None:
            self.image_width = m.get('ImageWidth')
        if m.get('OutputImageNum') is not None:
            self.output_image_num = m.get('OutputImageNum')
        return self


class ImageDuplicationResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        data: List[str] = None,
        success: bool = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.data = data
        self.success = success
        self.request_id = request_id

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
        if self.data is not None:
            result['Data'] = self.data
        if self.success is not None:
            result['Success'] = self.success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ImageDuplicationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ImageDuplicationResponseBody = None,
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
            temp_model = ImageDuplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ImageSegmentationRequest(TeaModel):
    def __init__(
        self,
        instance_name: str = None,
        pic_content: str = None,
        return_pic_format: str = None,
        return_pic_type: str = None,
    ):
        self.instance_name = instance_name
        self.pic_content = pic_content
        self.return_pic_format = return_pic_format
        self.return_pic_type = return_pic_type

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
        if self.return_pic_format is not None:
            result['ReturnPicFormat'] = self.return_pic_format
        if self.return_pic_type is not None:
            result['ReturnPicType'] = self.return_pic_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('PicContent') is not None:
            self.pic_content = m.get('PicContent')
        if m.get('ReturnPicFormat') is not None:
            self.return_pic_format = m.get('ReturnPicFormat')
        if m.get('ReturnPicType') is not None:
            self.return_pic_type = m.get('ReturnPicType')
        return self


class ImageSegmentationAdvanceRequest(TeaModel):
    def __init__(
        self,
        pic_content_object: BinaryIO = None,
        instance_name: str = None,
        return_pic_format: str = None,
        return_pic_type: str = None,
    ):
        self.pic_content_object = pic_content_object
        self.instance_name = instance_name
        self.return_pic_format = return_pic_format
        self.return_pic_type = return_pic_type

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
        if self.return_pic_format is not None:
            result['ReturnPicFormat'] = self.return_pic_format
        if self.return_pic_type is not None:
            result['ReturnPicType'] = self.return_pic_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PicContentObject') is not None:
            self.pic_content_object = m.get('PicContentObject')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('ReturnPicFormat') is not None:
            self.return_pic_format = m.get('ReturnPicFormat')
        if m.get('ReturnPicType') is not None:
            self.return_pic_type = m.get('ReturnPicType')
        return self


class ImageSegmentationResponseBodyData(TeaModel):
    def __init__(
        self,
        pic_url: str = None,
    ):
        self.pic_url = pic_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pic_url is not None:
            result['PicUrl'] = self.pic_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PicUrl') is not None:
            self.pic_url = m.get('PicUrl')
        return self


class ImageSegmentationResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        data: ImageSegmentationResponseBodyData = None,
        success: bool = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.data = data
        self.success = success
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.success is not None:
            result['Success'] = self.success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Data') is not None:
            temp_model = ImageSegmentationResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ImageSegmentationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ImageSegmentationResponseBody = None,
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
            temp_model = ImageSegmentationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CommodityTitleRequest(TeaModel):
    def __init__(
        self,
        instance_name: str = None,
        pic_content: str = None,
        title_index: int = None,
    ):
        self.instance_name = instance_name
        self.pic_content = pic_content
        self.title_index = title_index

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
        if self.title_index is not None:
            result['TitleIndex'] = self.title_index
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('PicContent') is not None:
            self.pic_content = m.get('PicContent')
        if m.get('TitleIndex') is not None:
            self.title_index = m.get('TitleIndex')
        return self


class CommodityTitleAdvanceRequest(TeaModel):
    def __init__(
        self,
        pic_content_object: BinaryIO = None,
        instance_name: str = None,
        title_index: int = None,
    ):
        self.pic_content_object = pic_content_object
        self.instance_name = instance_name
        self.title_index = title_index

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
        if self.title_index is not None:
            result['TitleIndex'] = self.title_index
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PicContentObject') is not None:
            self.pic_content_object = m.get('PicContentObject')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('TitleIndex') is not None:
            self.title_index = m.get('TitleIndex')
        return self


class CommodityTitleResponseBodyData(TeaModel):
    def __init__(
        self,
        title: str = None,
    ):
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class CommodityTitleResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        data: CommodityTitleResponseBodyData = None,
        success: bool = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.data = data
        self.success = success
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.success is not None:
            result['Success'] = self.success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Data') is not None:
            temp_model = CommodityTitleResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CommodityTitleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CommodityTitleResponseBody = None,
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
            temp_model = CommodityTitleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


