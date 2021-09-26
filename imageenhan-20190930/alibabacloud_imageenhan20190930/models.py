# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, BinaryIO, List


class ExtendImageStyleRequest(TeaModel):
    def __init__(
        self,
        style_url: str = None,
        major_url: str = None,
    ):
        self.style_url = style_url
        self.major_url = major_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.style_url is not None:
            result['StyleUrl'] = self.style_url
        if self.major_url is not None:
            result['MajorUrl'] = self.major_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StyleUrl') is not None:
            self.style_url = m.get('StyleUrl')
        if m.get('MajorUrl') is not None:
            self.major_url = m.get('MajorUrl')
        return self


class ExtendImageStyleResponseBodyData(TeaModel):
    def __init__(
        self,
        url: str = None,
        major_url: str = None,
    ):
        self.url = url
        self.major_url = major_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        if self.major_url is not None:
            result['MajorUrl'] = self.major_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('MajorUrl') is not None:
            self.major_url = m.get('MajorUrl')
        return self


class ExtendImageStyleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: ExtendImageStyleResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = ExtendImageStyleResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class ExtendImageStyleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ExtendImageStyleResponseBody = None,
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
            temp_model = ExtendImageStyleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ImageBlindCharacterWatermarkRequest(TeaModel):
    def __init__(
        self,
        function_type: str = None,
        text: str = None,
        watermark_image_url: str = None,
        output_file_type: str = None,
        quality_factor: int = None,
        origin_image_url: str = None,
    ):
        self.function_type = function_type
        self.text = text
        self.watermark_image_url = watermark_image_url
        self.output_file_type = output_file_type
        self.quality_factor = quality_factor
        self.origin_image_url = origin_image_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.function_type is not None:
            result['FunctionType'] = self.function_type
        if self.text is not None:
            result['Text'] = self.text
        if self.watermark_image_url is not None:
            result['WatermarkImageURL'] = self.watermark_image_url
        if self.output_file_type is not None:
            result['OutputFileType'] = self.output_file_type
        if self.quality_factor is not None:
            result['QualityFactor'] = self.quality_factor
        if self.origin_image_url is not None:
            result['OriginImageURL'] = self.origin_image_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FunctionType') is not None:
            self.function_type = m.get('FunctionType')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('WatermarkImageURL') is not None:
            self.watermark_image_url = m.get('WatermarkImageURL')
        if m.get('OutputFileType') is not None:
            self.output_file_type = m.get('OutputFileType')
        if m.get('QualityFactor') is not None:
            self.quality_factor = m.get('QualityFactor')
        if m.get('OriginImageURL') is not None:
            self.origin_image_url = m.get('OriginImageURL')
        return self


class ImageBlindCharacterWatermarkAdvanceRequest(TeaModel):
    def __init__(
        self,
        origin_image_urlobject: BinaryIO = None,
        function_type: str = None,
        text: str = None,
        watermark_image_url: str = None,
        output_file_type: str = None,
        quality_factor: int = None,
    ):
        self.origin_image_urlobject = origin_image_urlobject
        self.function_type = function_type
        self.text = text
        self.watermark_image_url = watermark_image_url
        self.output_file_type = output_file_type
        self.quality_factor = quality_factor

    def validate(self):
        self.validate_required(self.origin_image_urlobject, 'origin_image_urlobject')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.origin_image_urlobject is not None:
            result['OriginImageURLObject'] = self.origin_image_urlobject
        if self.function_type is not None:
            result['FunctionType'] = self.function_type
        if self.text is not None:
            result['Text'] = self.text
        if self.watermark_image_url is not None:
            result['WatermarkImageURL'] = self.watermark_image_url
        if self.output_file_type is not None:
            result['OutputFileType'] = self.output_file_type
        if self.quality_factor is not None:
            result['QualityFactor'] = self.quality_factor
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OriginImageURLObject') is not None:
            self.origin_image_urlobject = m.get('OriginImageURLObject')
        if m.get('FunctionType') is not None:
            self.function_type = m.get('FunctionType')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('WatermarkImageURL') is not None:
            self.watermark_image_url = m.get('WatermarkImageURL')
        if m.get('OutputFileType') is not None:
            self.output_file_type = m.get('OutputFileType')
        if m.get('QualityFactor') is not None:
            self.quality_factor = m.get('QualityFactor')
        return self


class ImageBlindCharacterWatermarkResponseBodyData(TeaModel):
    def __init__(
        self,
        watermark_image_url: str = None,
        text_image_url: str = None,
    ):
        self.watermark_image_url = watermark_image_url
        self.text_image_url = text_image_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.watermark_image_url is not None:
            result['WatermarkImageURL'] = self.watermark_image_url
        if self.text_image_url is not None:
            result['TextImageURL'] = self.text_image_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('WatermarkImageURL') is not None:
            self.watermark_image_url = m.get('WatermarkImageURL')
        if m.get('TextImageURL') is not None:
            self.text_image_url = m.get('TextImageURL')
        return self


class ImageBlindCharacterWatermarkResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: ImageBlindCharacterWatermarkResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = ImageBlindCharacterWatermarkResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class ImageBlindCharacterWatermarkResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ImageBlindCharacterWatermarkResponseBody = None,
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
            temp_model = ImageBlindCharacterWatermarkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveImageWatermarkRequest(TeaModel):
    def __init__(
        self,
        image_url: str = None,
    ):
        self.image_url = image_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        return self


class RemoveImageWatermarkAdvanceRequest(TeaModel):
    def __init__(
        self,
        image_urlobject: BinaryIO = None,
    ):
        self.image_urlobject = image_urlobject

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_urlobject is not None:
            result['ImageURLObject'] = self.image_urlobject
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURLObject') is not None:
            self.image_urlobject = m.get('ImageURLObject')
        return self


class RemoveImageWatermarkResponseBodyData(TeaModel):
    def __init__(
        self,
        image_url: str = None,
    ):
        self.image_url = image_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        return self


class RemoveImageWatermarkResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: RemoveImageWatermarkResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = RemoveImageWatermarkResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class RemoveImageWatermarkResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RemoveImageWatermarkResponseBody = None,
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
            temp_model = RemoveImageWatermarkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateDynamicImageRequest(TeaModel):
    def __init__(
        self,
        url: str = None,
        operation: str = None,
    ):
        self.url = url
        self.operation = operation

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        if self.operation is not None:
            result['Operation'] = self.operation
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('Operation') is not None:
            self.operation = m.get('Operation')
        return self


class GenerateDynamicImageAdvanceRequest(TeaModel):
    def __init__(
        self,
        url_object: BinaryIO = None,
        operation: str = None,
    ):
        self.url_object = url_object
        self.operation = operation

    def validate(self):
        self.validate_required(self.url_object, 'url_object')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url_object is not None:
            result['UrlObject'] = self.url_object
        if self.operation is not None:
            result['Operation'] = self.operation
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UrlObject') is not None:
            self.url_object = m.get('UrlObject')
        if m.get('Operation') is not None:
            self.operation = m.get('Operation')
        return self


class GenerateDynamicImageResponseBodyData(TeaModel):
    def __init__(
        self,
        url: str = None,
    ):
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class GenerateDynamicImageResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: GenerateDynamicImageResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = GenerateDynamicImageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class GenerateDynamicImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GenerateDynamicImageResponseBody = None,
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
            temp_model = GenerateDynamicImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ImageBlindPicWatermarkRequest(TeaModel):
    def __init__(
        self,
        function_type: str = None,
        logo_url: str = None,
        watermark_image_url: str = None,
        output_file_type: str = None,
        quality_factor: int = None,
        origin_image_url: str = None,
    ):
        self.function_type = function_type
        self.logo_url = logo_url
        self.watermark_image_url = watermark_image_url
        self.output_file_type = output_file_type
        self.quality_factor = quality_factor
        self.origin_image_url = origin_image_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.function_type is not None:
            result['FunctionType'] = self.function_type
        if self.logo_url is not None:
            result['LogoURL'] = self.logo_url
        if self.watermark_image_url is not None:
            result['WatermarkImageURL'] = self.watermark_image_url
        if self.output_file_type is not None:
            result['OutputFileType'] = self.output_file_type
        if self.quality_factor is not None:
            result['QualityFactor'] = self.quality_factor
        if self.origin_image_url is not None:
            result['OriginImageURL'] = self.origin_image_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FunctionType') is not None:
            self.function_type = m.get('FunctionType')
        if m.get('LogoURL') is not None:
            self.logo_url = m.get('LogoURL')
        if m.get('WatermarkImageURL') is not None:
            self.watermark_image_url = m.get('WatermarkImageURL')
        if m.get('OutputFileType') is not None:
            self.output_file_type = m.get('OutputFileType')
        if m.get('QualityFactor') is not None:
            self.quality_factor = m.get('QualityFactor')
        if m.get('OriginImageURL') is not None:
            self.origin_image_url = m.get('OriginImageURL')
        return self


class ImageBlindPicWatermarkAdvanceRequest(TeaModel):
    def __init__(
        self,
        origin_image_urlobject: BinaryIO = None,
        function_type: str = None,
        logo_url: str = None,
        watermark_image_url: str = None,
        output_file_type: str = None,
        quality_factor: int = None,
    ):
        self.origin_image_urlobject = origin_image_urlobject
        self.function_type = function_type
        self.logo_url = logo_url
        self.watermark_image_url = watermark_image_url
        self.output_file_type = output_file_type
        self.quality_factor = quality_factor

    def validate(self):
        self.validate_required(self.origin_image_urlobject, 'origin_image_urlobject')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.origin_image_urlobject is not None:
            result['OriginImageURLObject'] = self.origin_image_urlobject
        if self.function_type is not None:
            result['FunctionType'] = self.function_type
        if self.logo_url is not None:
            result['LogoURL'] = self.logo_url
        if self.watermark_image_url is not None:
            result['WatermarkImageURL'] = self.watermark_image_url
        if self.output_file_type is not None:
            result['OutputFileType'] = self.output_file_type
        if self.quality_factor is not None:
            result['QualityFactor'] = self.quality_factor
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OriginImageURLObject') is not None:
            self.origin_image_urlobject = m.get('OriginImageURLObject')
        if m.get('FunctionType') is not None:
            self.function_type = m.get('FunctionType')
        if m.get('LogoURL') is not None:
            self.logo_url = m.get('LogoURL')
        if m.get('WatermarkImageURL') is not None:
            self.watermark_image_url = m.get('WatermarkImageURL')
        if m.get('OutputFileType') is not None:
            self.output_file_type = m.get('OutputFileType')
        if m.get('QualityFactor') is not None:
            self.quality_factor = m.get('QualityFactor')
        return self


class ImageBlindPicWatermarkResponseBodyData(TeaModel):
    def __init__(
        self,
        watermark_image_url: str = None,
        logo_url: str = None,
    ):
        self.watermark_image_url = watermark_image_url
        self.logo_url = logo_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.watermark_image_url is not None:
            result['WatermarkImageURL'] = self.watermark_image_url
        if self.logo_url is not None:
            result['LogoURL'] = self.logo_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('WatermarkImageURL') is not None:
            self.watermark_image_url = m.get('WatermarkImageURL')
        if m.get('LogoURL') is not None:
            self.logo_url = m.get('LogoURL')
        return self


class ImageBlindPicWatermarkResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: ImageBlindPicWatermarkResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = ImageBlindPicWatermarkResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class ImageBlindPicWatermarkResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ImageBlindPicWatermarkResponseBody = None,
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
            temp_model = ImageBlindPicWatermarkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveImageSubtitlesRequest(TeaModel):
    def __init__(
        self,
        image_url: str = None,
        bx: float = None,
        by: float = None,
        bw: float = None,
        bh: float = None,
    ):
        self.image_url = image_url
        self.bx = bx
        self.by = by
        self.bw = bw
        self.bh = bh

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        if self.bx is not None:
            result['BX'] = self.bx
        if self.by is not None:
            result['BY'] = self.by
        if self.bw is not None:
            result['BW'] = self.bw
        if self.bh is not None:
            result['BH'] = self.bh
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        if m.get('BX') is not None:
            self.bx = m.get('BX')
        if m.get('BY') is not None:
            self.by = m.get('BY')
        if m.get('BW') is not None:
            self.bw = m.get('BW')
        if m.get('BH') is not None:
            self.bh = m.get('BH')
        return self


class RemoveImageSubtitlesAdvanceRequest(TeaModel):
    def __init__(
        self,
        image_urlobject: BinaryIO = None,
        bx: float = None,
        by: float = None,
        bw: float = None,
        bh: float = None,
    ):
        self.image_urlobject = image_urlobject
        self.bx = bx
        self.by = by
        self.bw = bw
        self.bh = bh

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_urlobject is not None:
            result['ImageURLObject'] = self.image_urlobject
        if self.bx is not None:
            result['BX'] = self.bx
        if self.by is not None:
            result['BY'] = self.by
        if self.bw is not None:
            result['BW'] = self.bw
        if self.bh is not None:
            result['BH'] = self.bh
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURLObject') is not None:
            self.image_urlobject = m.get('ImageURLObject')
        if m.get('BX') is not None:
            self.bx = m.get('BX')
        if m.get('BY') is not None:
            self.by = m.get('BY')
        if m.get('BW') is not None:
            self.bw = m.get('BW')
        if m.get('BH') is not None:
            self.bh = m.get('BH')
        return self


class RemoveImageSubtitlesResponseBodyData(TeaModel):
    def __init__(
        self,
        image_url: str = None,
    ):
        self.image_url = image_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        return self


class RemoveImageSubtitlesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: RemoveImageSubtitlesResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = RemoveImageSubtitlesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class RemoveImageSubtitlesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RemoveImageSubtitlesResponseBody = None,
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
            temp_model = RemoveImageSubtitlesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecolorHDImageRequestColorTemplate(TeaModel):
    def __init__(
        self,
        color: str = None,
    ):
        self.color = color

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.color is not None:
            result['Color'] = self.color
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Color') is not None:
            self.color = m.get('Color')
        return self


class RecolorHDImageRequest(TeaModel):
    def __init__(
        self,
        url: str = None,
        mode: str = None,
        ref_url: str = None,
        color_count: int = None,
        degree: str = None,
        color_template: List[RecolorHDImageRequestColorTemplate] = None,
    ):
        self.url = url
        self.mode = mode
        self.ref_url = ref_url
        self.color_count = color_count
        self.degree = degree
        self.color_template = color_template

    def validate(self):
        if self.color_template:
            for k in self.color_template:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.ref_url is not None:
            result['RefUrl'] = self.ref_url
        if self.color_count is not None:
            result['ColorCount'] = self.color_count
        if self.degree is not None:
            result['Degree'] = self.degree
        result['ColorTemplate'] = []
        if self.color_template is not None:
            for k in self.color_template:
                result['ColorTemplate'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('RefUrl') is not None:
            self.ref_url = m.get('RefUrl')
        if m.get('ColorCount') is not None:
            self.color_count = m.get('ColorCount')
        if m.get('Degree') is not None:
            self.degree = m.get('Degree')
        self.color_template = []
        if m.get('ColorTemplate') is not None:
            for k in m.get('ColorTemplate'):
                temp_model = RecolorHDImageRequestColorTemplate()
                self.color_template.append(temp_model.from_map(k))
        return self


class RecolorHDImageAdvanceRequestColorTemplate(TeaModel):
    def __init__(
        self,
        color: str = None,
    ):
        self.color = color

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.color is not None:
            result['Color'] = self.color
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Color') is not None:
            self.color = m.get('Color')
        return self


class RecolorHDImageAdvanceRequest(TeaModel):
    def __init__(
        self,
        url_object: BinaryIO = None,
        mode: str = None,
        ref_url: str = None,
        color_count: int = None,
        degree: str = None,
        color_template: List[RecolorHDImageAdvanceRequestColorTemplate] = None,
    ):
        self.url_object = url_object
        self.mode = mode
        self.ref_url = ref_url
        self.color_count = color_count
        self.degree = degree
        self.color_template = color_template

    def validate(self):
        self.validate_required(self.url_object, 'url_object')
        if self.color_template:
            for k in self.color_template:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url_object is not None:
            result['UrlObject'] = self.url_object
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.ref_url is not None:
            result['RefUrl'] = self.ref_url
        if self.color_count is not None:
            result['ColorCount'] = self.color_count
        if self.degree is not None:
            result['Degree'] = self.degree
        result['ColorTemplate'] = []
        if self.color_template is not None:
            for k in self.color_template:
                result['ColorTemplate'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UrlObject') is not None:
            self.url_object = m.get('UrlObject')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('RefUrl') is not None:
            self.ref_url = m.get('RefUrl')
        if m.get('ColorCount') is not None:
            self.color_count = m.get('ColorCount')
        if m.get('Degree') is not None:
            self.degree = m.get('Degree')
        self.color_template = []
        if m.get('ColorTemplate') is not None:
            for k in m.get('ColorTemplate'):
                temp_model = RecolorHDImageAdvanceRequestColorTemplate()
                self.color_template.append(temp_model.from_map(k))
        return self


class RecolorHDImageResponseBodyData(TeaModel):
    def __init__(
        self,
        image_list: List[str] = None,
    ):
        self.image_list = image_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_list is not None:
            result['ImageList'] = self.image_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageList') is not None:
            self.image_list = m.get('ImageList')
        return self


class RecolorHDImageResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: RecolorHDImageResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = RecolorHDImageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class RecolorHDImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RecolorHDImageResponseBody = None,
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
            temp_model = RecolorHDImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ColorizeImageRequest(TeaModel):
    def __init__(
        self,
        image_url: str = None,
    ):
        self.image_url = image_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        return self


class ColorizeImageAdvanceRequest(TeaModel):
    def __init__(
        self,
        image_urlobject: BinaryIO = None,
    ):
        self.image_urlobject = image_urlobject

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_urlobject is not None:
            result['ImageURLObject'] = self.image_urlobject
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURLObject') is not None:
            self.image_urlobject = m.get('ImageURLObject')
        return self


class ColorizeImageResponseBodyData(TeaModel):
    def __init__(
        self,
        image_url: str = None,
    ):
        self.image_url = image_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        return self


class ColorizeImageResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: ColorizeImageResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = ColorizeImageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class ColorizeImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ColorizeImageResponseBody = None,
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
            temp_model = ColorizeImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecolorImageRequestColorTemplate(TeaModel):
    def __init__(
        self,
        color: str = None,
    ):
        self.color = color

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.color is not None:
            result['Color'] = self.color
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Color') is not None:
            self.color = m.get('Color')
        return self


class RecolorImageRequest(TeaModel):
    def __init__(
        self,
        url: str = None,
        mode: str = None,
        ref_url: str = None,
        color_count: int = None,
        color_template: List[RecolorImageRequestColorTemplate] = None,
    ):
        self.url = url
        self.mode = mode
        self.ref_url = ref_url
        self.color_count = color_count
        self.color_template = color_template

    def validate(self):
        if self.color_template:
            for k in self.color_template:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.ref_url is not None:
            result['RefUrl'] = self.ref_url
        if self.color_count is not None:
            result['ColorCount'] = self.color_count
        result['ColorTemplate'] = []
        if self.color_template is not None:
            for k in self.color_template:
                result['ColorTemplate'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('RefUrl') is not None:
            self.ref_url = m.get('RefUrl')
        if m.get('ColorCount') is not None:
            self.color_count = m.get('ColorCount')
        self.color_template = []
        if m.get('ColorTemplate') is not None:
            for k in m.get('ColorTemplate'):
                temp_model = RecolorImageRequestColorTemplate()
                self.color_template.append(temp_model.from_map(k))
        return self


class RecolorImageResponseBodyData(TeaModel):
    def __init__(
        self,
        image_list: List[str] = None,
    ):
        self.image_list = image_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_list is not None:
            result['ImageList'] = self.image_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageList') is not None:
            self.image_list = m.get('ImageList')
        return self


class RecolorImageResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: RecolorImageResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = RecolorImageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class RecolorImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RecolorImageResponseBody = None,
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
            temp_model = RecolorImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AssessCompositionRequest(TeaModel):
    def __init__(
        self,
        image_url: str = None,
    ):
        self.image_url = image_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        return self


class AssessCompositionAdvanceRequest(TeaModel):
    def __init__(
        self,
        image_urlobject: BinaryIO = None,
    ):
        self.image_urlobject = image_urlobject

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_urlobject is not None:
            result['ImageURLObject'] = self.image_urlobject
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURLObject') is not None:
            self.image_urlobject = m.get('ImageURLObject')
        return self


class AssessCompositionResponseBodyData(TeaModel):
    def __init__(
        self,
        score: float = None,
    ):
        self.score = score

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.score is not None:
            result['Score'] = self.score
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Score') is not None:
            self.score = m.get('Score')
        return self


class AssessCompositionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: AssessCompositionResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = AssessCompositionResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class AssessCompositionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AssessCompositionResponseBody = None,
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
            temp_model = AssessCompositionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AssessSharpnessRequest(TeaModel):
    def __init__(
        self,
        image_url: str = None,
    ):
        self.image_url = image_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        return self


class AssessSharpnessAdvanceRequest(TeaModel):
    def __init__(
        self,
        image_urlobject: BinaryIO = None,
    ):
        self.image_urlobject = image_urlobject

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_urlobject is not None:
            result['ImageURLObject'] = self.image_urlobject
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURLObject') is not None:
            self.image_urlobject = m.get('ImageURLObject')
        return self


class AssessSharpnessResponseBodyData(TeaModel):
    def __init__(
        self,
        sharpness: float = None,
    ):
        self.sharpness = sharpness

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sharpness is not None:
            result['Sharpness'] = self.sharpness
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Sharpness') is not None:
            self.sharpness = m.get('Sharpness')
        return self


class AssessSharpnessResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: AssessSharpnessResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = AssessSharpnessResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class AssessSharpnessResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AssessSharpnessResponseBody = None,
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
            temp_model = AssessSharpnessResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ErasePersonRequest(TeaModel):
    def __init__(
        self,
        image_url: str = None,
        user_mask: str = None,
    ):
        self.image_url = image_url
        self.user_mask = user_mask

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        if self.user_mask is not None:
            result['UserMask'] = self.user_mask
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        if m.get('UserMask') is not None:
            self.user_mask = m.get('UserMask')
        return self


class ErasePersonAdvanceRequest(TeaModel):
    def __init__(
        self,
        image_urlobject: BinaryIO = None,
        user_mask: str = None,
    ):
        self.image_urlobject = image_urlobject
        self.user_mask = user_mask

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_urlobject is not None:
            result['ImageURLObject'] = self.image_urlobject
        if self.user_mask is not None:
            result['UserMask'] = self.user_mask
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURLObject') is not None:
            self.image_urlobject = m.get('ImageURLObject')
        if m.get('UserMask') is not None:
            self.user_mask = m.get('UserMask')
        return self


class ErasePersonResponseBodyData(TeaModel):
    def __init__(
        self,
        image_url: str = None,
    ):
        self.image_url = image_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        return self


class ErasePersonResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: ErasePersonResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = ErasePersonResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class ErasePersonResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ErasePersonResponseBody = None,
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
            temp_model = ErasePersonResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAsyncJobResultRequest(TeaModel):
    def __init__(
        self,
        job_id: str = None,
    ):
        self.job_id = job_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class GetAsyncJobResultResponseBodyData(TeaModel):
    def __init__(
        self,
        status: str = None,
        error_message: str = None,
        result: str = None,
        error_code: str = None,
        job_id: str = None,
    ):
        self.status = status
        self.error_message = error_message
        self.result = result
        self.error_code = error_code
        self.job_id = job_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.result is not None:
            result['Result'] = self.result
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class GetAsyncJobResultResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: GetAsyncJobResultResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = GetAsyncJobResultResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class GetAsyncJobResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetAsyncJobResultResponseBody = None,
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
            temp_model = GetAsyncJobResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ImitatePhotoStyleRequest(TeaModel):
    def __init__(
        self,
        style_url: str = None,
        image_url: str = None,
    ):
        self.style_url = style_url
        self.image_url = image_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.style_url is not None:
            result['StyleUrl'] = self.style_url
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StyleUrl') is not None:
            self.style_url = m.get('StyleUrl')
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        return self


class ImitatePhotoStyleAdvanceRequest(TeaModel):
    def __init__(
        self,
        image_urlobject: BinaryIO = None,
        style_url: str = None,
    ):
        self.image_urlobject = image_urlobject
        self.style_url = style_url

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_urlobject is not None:
            result['ImageURLObject'] = self.image_urlobject
        if self.style_url is not None:
            result['StyleUrl'] = self.style_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURLObject') is not None:
            self.image_urlobject = m.get('ImageURLObject')
        if m.get('StyleUrl') is not None:
            self.style_url = m.get('StyleUrl')
        return self


class ImitatePhotoStyleResponseBodyData(TeaModel):
    def __init__(
        self,
        image_url: str = None,
    ):
        self.image_url = image_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        return self


class ImitatePhotoStyleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: ImitatePhotoStyleResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = ImitatePhotoStyleResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class ImitatePhotoStyleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ImitatePhotoStyleResponseBody = None,
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
            temp_model = ImitatePhotoStyleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ChangeImageSizeRequest(TeaModel):
    def __init__(
        self,
        width: int = None,
        height: int = None,
        url: str = None,
    ):
        self.width = width
        self.height = height
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class ChangeImageSizeAdvanceRequest(TeaModel):
    def __init__(
        self,
        url_object: BinaryIO = None,
        width: int = None,
        height: int = None,
    ):
        self.url_object = url_object
        self.width = width
        self.height = height

    def validate(self):
        self.validate_required(self.url_object, 'url_object')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url_object is not None:
            result['UrlObject'] = self.url_object
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UrlObject') is not None:
            self.url_object = m.get('UrlObject')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        return self


class ChangeImageSizeResponseBodyDataRetainLocation(TeaModel):
    def __init__(
        self,
        width: int = None,
        height: int = None,
        y: int = None,
        x: int = None,
    ):
        self.width = width
        self.height = height
        self.y = y
        self.x = x

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        if self.y is not None:
            result['Y'] = self.y
        if self.x is not None:
            result['X'] = self.x
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        if m.get('X') is not None:
            self.x = m.get('X')
        return self


class ChangeImageSizeResponseBodyData(TeaModel):
    def __init__(
        self,
        url: str = None,
        retain_location: ChangeImageSizeResponseBodyDataRetainLocation = None,
    ):
        self.url = url
        self.retain_location = retain_location

    def validate(self):
        if self.retain_location:
            self.retain_location.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        if self.retain_location is not None:
            result['RetainLocation'] = self.retain_location.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('RetainLocation') is not None:
            temp_model = ChangeImageSizeResponseBodyDataRetainLocation()
            self.retain_location = temp_model.from_map(m['RetainLocation'])
        return self


class ChangeImageSizeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: ChangeImageSizeResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = ChangeImageSizeResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class ChangeImageSizeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ChangeImageSizeResponseBody = None,
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
            temp_model = ChangeImageSizeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnhanceImageColorRequest(TeaModel):
    def __init__(
        self,
        image_url: str = None,
        output_format: str = None,
        mode: str = None,
    ):
        self.image_url = image_url
        self.output_format = output_format
        self.mode = mode

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        if self.output_format is not None:
            result['OutputFormat'] = self.output_format
        if self.mode is not None:
            result['Mode'] = self.mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        if m.get('OutputFormat') is not None:
            self.output_format = m.get('OutputFormat')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        return self


class EnhanceImageColorAdvanceRequest(TeaModel):
    def __init__(
        self,
        image_urlobject: BinaryIO = None,
        output_format: str = None,
        mode: str = None,
    ):
        self.image_urlobject = image_urlobject
        self.output_format = output_format
        self.mode = mode

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_urlobject is not None:
            result['ImageURLObject'] = self.image_urlobject
        if self.output_format is not None:
            result['OutputFormat'] = self.output_format
        if self.mode is not None:
            result['Mode'] = self.mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURLObject') is not None:
            self.image_urlobject = m.get('ImageURLObject')
        if m.get('OutputFormat') is not None:
            self.output_format = m.get('OutputFormat')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        return self


class EnhanceImageColorResponseBodyData(TeaModel):
    def __init__(
        self,
        image_url: str = None,
    ):
        self.image_url = image_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        return self


class EnhanceImageColorResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: EnhanceImageColorResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = EnhanceImageColorResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class EnhanceImageColorResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: EnhanceImageColorResponseBody = None,
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
            temp_model = EnhanceImageColorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AssessExposureRequest(TeaModel):
    def __init__(
        self,
        image_url: str = None,
    ):
        self.image_url = image_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        return self


class AssessExposureAdvanceRequest(TeaModel):
    def __init__(
        self,
        image_urlobject: BinaryIO = None,
    ):
        self.image_urlobject = image_urlobject

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_urlobject is not None:
            result['ImageURLObject'] = self.image_urlobject
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURLObject') is not None:
            self.image_urlobject = m.get('ImageURLObject')
        return self


class AssessExposureResponseBodyData(TeaModel):
    def __init__(
        self,
        exposure: float = None,
    ):
        self.exposure = exposure

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exposure is not None:
            result['Exposure'] = self.exposure
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Exposure') is not None:
            self.exposure = m.get('Exposure')
        return self


class AssessExposureResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: AssessExposureResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = AssessExposureResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class AssessExposureResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AssessExposureResponseBody = None,
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
            temp_model = AssessExposureResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MakeSuperResolutionImageRequest(TeaModel):
    def __init__(
        self,
        url: str = None,
        mode: str = None,
        upscale_factor: int = None,
    ):
        self.url = url
        self.mode = mode
        self.upscale_factor = upscale_factor

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.upscale_factor is not None:
            result['UpscaleFactor'] = self.upscale_factor
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('UpscaleFactor') is not None:
            self.upscale_factor = m.get('UpscaleFactor')
        return self


class MakeSuperResolutionImageAdvanceRequest(TeaModel):
    def __init__(
        self,
        url_object: BinaryIO = None,
        mode: str = None,
        upscale_factor: int = None,
    ):
        self.url_object = url_object
        self.mode = mode
        self.upscale_factor = upscale_factor

    def validate(self):
        self.validate_required(self.url_object, 'url_object')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url_object is not None:
            result['UrlObject'] = self.url_object
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.upscale_factor is not None:
            result['UpscaleFactor'] = self.upscale_factor
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UrlObject') is not None:
            self.url_object = m.get('UrlObject')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('UpscaleFactor') is not None:
            self.upscale_factor = m.get('UpscaleFactor')
        return self


class MakeSuperResolutionImageResponseBodyData(TeaModel):
    def __init__(
        self,
        url: str = None,
    ):
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class MakeSuperResolutionImageResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: MakeSuperResolutionImageResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = MakeSuperResolutionImageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class MakeSuperResolutionImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: MakeSuperResolutionImageResponseBody = None,
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
            temp_model = MakeSuperResolutionImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class IntelligentCompositionRequest(TeaModel):
    def __init__(
        self,
        num_boxes: int = None,
        image_url: str = None,
    ):
        self.num_boxes = num_boxes
        self.image_url = image_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.num_boxes is not None:
            result['NumBoxes'] = self.num_boxes
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NumBoxes') is not None:
            self.num_boxes = m.get('NumBoxes')
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        return self


class IntelligentCompositionAdvanceRequest(TeaModel):
    def __init__(
        self,
        image_urlobject: BinaryIO = None,
        num_boxes: int = None,
    ):
        self.image_urlobject = image_urlobject
        self.num_boxes = num_boxes

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_urlobject is not None:
            result['ImageURLObject'] = self.image_urlobject
        if self.num_boxes is not None:
            result['NumBoxes'] = self.num_boxes
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURLObject') is not None:
            self.image_urlobject = m.get('ImageURLObject')
        if m.get('NumBoxes') is not None:
            self.num_boxes = m.get('NumBoxes')
        return self


class IntelligentCompositionResponseBodyDataElements(TeaModel):
    def __init__(
        self,
        min_x: int = None,
        score: float = None,
        max_y: int = None,
        max_x: int = None,
        min_y: int = None,
    ):
        self.min_x = min_x
        self.score = score
        self.max_y = max_y
        self.max_x = max_x
        self.min_y = min_y

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.min_x is not None:
            result['MinX'] = self.min_x
        if self.score is not None:
            result['Score'] = self.score
        if self.max_y is not None:
            result['MaxY'] = self.max_y
        if self.max_x is not None:
            result['MaxX'] = self.max_x
        if self.min_y is not None:
            result['MinY'] = self.min_y
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MinX') is not None:
            self.min_x = m.get('MinX')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('MaxY') is not None:
            self.max_y = m.get('MaxY')
        if m.get('MaxX') is not None:
            self.max_x = m.get('MaxX')
        if m.get('MinY') is not None:
            self.min_y = m.get('MinY')
        return self


class IntelligentCompositionResponseBodyData(TeaModel):
    def __init__(
        self,
        elements: List[IntelligentCompositionResponseBodyDataElements] = None,
    ):
        self.elements = elements

    def validate(self):
        if self.elements:
            for k in self.elements:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Elements'] = []
        if self.elements is not None:
            for k in self.elements:
                result['Elements'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.elements = []
        if m.get('Elements') is not None:
            for k in m.get('Elements'):
                temp_model = IntelligentCompositionResponseBodyDataElements()
                self.elements.append(temp_model.from_map(k))
        return self


class IntelligentCompositionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: IntelligentCompositionResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = IntelligentCompositionResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class IntelligentCompositionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: IntelligentCompositionResponseBody = None,
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
            temp_model = IntelligentCompositionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


