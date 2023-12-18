# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict, Any


class DescribeImageModerationResultRequest(TeaModel):
    def __init__(
        self,
        req_id: str = None,
    ):
        self.req_id = req_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.req_id is not None:
            result['ReqId'] = self.req_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReqId') is not None:
            self.req_id = m.get('ReqId')
        return self


class DescribeImageModerationResultResponseBodyDataResult(TeaModel):
    def __init__(
        self,
        confidence: float = None,
        label: str = None,
    ):
        self.confidence = confidence
        self.label = label

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.confidence is not None:
            result['Confidence'] = self.confidence
        if self.label is not None:
            result['Label'] = self.label
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        return self


class DescribeImageModerationResultResponseBodyData(TeaModel):
    def __init__(
        self,
        data_id: str = None,
        frame: str = None,
        frame_num: int = None,
        req_id: str = None,
        result: List[DescribeImageModerationResultResponseBodyDataResult] = None,
    ):
        self.data_id = data_id
        self.frame = frame
        self.frame_num = frame_num
        self.req_id = req_id
        self.result = result

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
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.frame is not None:
            result['Frame'] = self.frame
        if self.frame_num is not None:
            result['FrameNum'] = self.frame_num
        if self.req_id is not None:
            result['ReqId'] = self.req_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('Frame') is not None:
            self.frame = m.get('Frame')
        if m.get('FrameNum') is not None:
            self.frame_num = m.get('FrameNum')
        if m.get('ReqId') is not None:
            self.req_id = m.get('ReqId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = DescribeImageModerationResultResponseBodyDataResult()
                self.result.append(temp_model.from_map(k))
        return self


class DescribeImageModerationResultResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: DescribeImageModerationResultResponseBodyData = None,
        msg: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.msg = msg
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
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = DescribeImageModerationResultResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeImageModerationResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeImageModerationResultResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DescribeImageModerationResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeImageResultExtRequest(TeaModel):
    def __init__(
        self,
        info_type: str = None,
        req_id: str = None,
    ):
        self.info_type = info_type
        self.req_id = req_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.info_type is not None:
            result['InfoType'] = self.info_type
        if self.req_id is not None:
            result['ReqId'] = self.req_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InfoType') is not None:
            self.info_type = m.get('InfoType')
        if m.get('ReqId') is not None:
            self.req_id = m.get('ReqId')
        return self


class DescribeImageResultExtResponseBodyDataCustomImage(TeaModel):
    def __init__(
        self,
        image_id: str = None,
        lib_id: str = None,
        lib_name: str = None,
    ):
        # 图片ID。
        self.image_id = image_id
        # 图库ID。
        self.lib_id = lib_id
        # 图库名。
        self.lib_name = lib_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.lib_id is not None:
            result['LibId'] = self.lib_id
        if self.lib_name is not None:
            result['LibName'] = self.lib_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('LibId') is not None:
            self.lib_id = m.get('LibId')
        if m.get('LibName') is not None:
            self.lib_name = m.get('LibName')
        return self


class DescribeImageResultExtResponseBodyDataPublicFigure(TeaModel):
    def __init__(
        self,
        figure_id: str = None,
    ):
        # 人物ID。
        self.figure_id = figure_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.figure_id is not None:
            result['FigureId'] = self.figure_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FigureId') is not None:
            self.figure_id = m.get('FigureId')
        return self


class DescribeImageResultExtResponseBodyDataTextInImage(TeaModel):
    def __init__(
        self,
        ocr_datas: List[str] = None,
        risk_words: List[str] = None,
    ):
        self.ocr_datas = ocr_datas
        self.risk_words = risk_words

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ocr_datas is not None:
            result['OcrDatas'] = self.ocr_datas
        if self.risk_words is not None:
            result['RiskWords'] = self.risk_words
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OcrDatas') is not None:
            self.ocr_datas = m.get('OcrDatas')
        if m.get('RiskWords') is not None:
            self.risk_words = m.get('RiskWords')
        return self


class DescribeImageResultExtResponseBodyData(TeaModel):
    def __init__(
        self,
        custom_image: List[DescribeImageResultExtResponseBodyDataCustomImage] = None,
        public_figure: List[DescribeImageResultExtResponseBodyDataPublicFigure] = None,
        text_in_image: DescribeImageResultExtResponseBodyDataTextInImage = None,
    ):
        self.custom_image = custom_image
        self.public_figure = public_figure
        self.text_in_image = text_in_image

    def validate(self):
        if self.custom_image:
            for k in self.custom_image:
                if k:
                    k.validate()
        if self.public_figure:
            for k in self.public_figure:
                if k:
                    k.validate()
        if self.text_in_image:
            self.text_in_image.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CustomImage'] = []
        if self.custom_image is not None:
            for k in self.custom_image:
                result['CustomImage'].append(k.to_map() if k else None)
        result['PublicFigure'] = []
        if self.public_figure is not None:
            for k in self.public_figure:
                result['PublicFigure'].append(k.to_map() if k else None)
        if self.text_in_image is not None:
            result['TextInImage'] = self.text_in_image.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.custom_image = []
        if m.get('CustomImage') is not None:
            for k in m.get('CustomImage'):
                temp_model = DescribeImageResultExtResponseBodyDataCustomImage()
                self.custom_image.append(temp_model.from_map(k))
        self.public_figure = []
        if m.get('PublicFigure') is not None:
            for k in m.get('PublicFigure'):
                temp_model = DescribeImageResultExtResponseBodyDataPublicFigure()
                self.public_figure.append(temp_model.from_map(k))
        if m.get('TextInImage') is not None:
            temp_model = DescribeImageResultExtResponseBodyDataTextInImage()
            self.text_in_image = temp_model.from_map(m['TextInImage'])
        return self


class DescribeImageResultExtResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: DescribeImageResultExtResponseBodyData = None,
        msg: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.msg = msg
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
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = DescribeImageResultExtResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeImageResultExtResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeImageResultExtResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DescribeImageResultExtResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUploadTokenResponseBodyData(TeaModel):
    def __init__(
        self,
        access_key_id: str = None,
        access_key_secret: str = None,
        bucket_name: str = None,
        expiration: int = None,
        file_name_prefix: str = None,
        oss_internal_end_point: str = None,
        oss_internet_end_point: str = None,
        security_token: str = None,
    ):
        self.access_key_id = access_key_id
        self.access_key_secret = access_key_secret
        self.bucket_name = bucket_name
        self.expiration = expiration
        self.file_name_prefix = file_name_prefix
        self.oss_internal_end_point = oss_internal_end_point
        self.oss_internet_end_point = oss_internet_end_point
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key_id is not None:
            result['AccessKeyId'] = self.access_key_id
        if self.access_key_secret is not None:
            result['AccessKeySecret'] = self.access_key_secret
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.expiration is not None:
            result['Expiration'] = self.expiration
        if self.file_name_prefix is not None:
            result['FileNamePrefix'] = self.file_name_prefix
        if self.oss_internal_end_point is not None:
            result['OssInternalEndPoint'] = self.oss_internal_end_point
        if self.oss_internet_end_point is not None:
            result['OssInternetEndPoint'] = self.oss_internet_end_point
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessKeyId') is not None:
            self.access_key_id = m.get('AccessKeyId')
        if m.get('AccessKeySecret') is not None:
            self.access_key_secret = m.get('AccessKeySecret')
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('Expiration') is not None:
            self.expiration = m.get('Expiration')
        if m.get('FileNamePrefix') is not None:
            self.file_name_prefix = m.get('FileNamePrefix')
        if m.get('OssInternalEndPoint') is not None:
            self.oss_internal_end_point = m.get('OssInternalEndPoint')
        if m.get('OssInternetEndPoint') is not None:
            self.oss_internet_end_point = m.get('OssInternetEndPoint')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeUploadTokenResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: DescribeUploadTokenResponseBodyData = None,
        msg: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.msg = msg
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
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = DescribeUploadTokenResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeUploadTokenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeUploadTokenResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DescribeUploadTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ImageAsyncModerationRequest(TeaModel):
    def __init__(
        self,
        service: str = None,
        service_parameters: str = None,
    ):
        self.service = service
        self.service_parameters = service_parameters

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service is not None:
            result['Service'] = self.service
        if self.service_parameters is not None:
            result['ServiceParameters'] = self.service_parameters
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Service') is not None:
            self.service = m.get('Service')
        if m.get('ServiceParameters') is not None:
            self.service_parameters = m.get('ServiceParameters')
        return self


class ImageAsyncModerationResponseBodyData(TeaModel):
    def __init__(
        self,
        data_id: str = None,
        req_id: str = None,
    ):
        self.data_id = data_id
        self.req_id = req_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.req_id is not None:
            result['ReqId'] = self.req_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('ReqId') is not None:
            self.req_id = m.get('ReqId')
        return self


class ImageAsyncModerationResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: ImageAsyncModerationResponseBodyData = None,
        msg: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.msg = msg
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
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ImageAsyncModerationResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ImageAsyncModerationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ImageAsyncModerationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ImageAsyncModerationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ImageModerationRequest(TeaModel):
    def __init__(
        self,
        service: str = None,
        service_parameters: str = None,
    ):
        self.service = service
        self.service_parameters = service_parameters

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service is not None:
            result['Service'] = self.service
        if self.service_parameters is not None:
            result['ServiceParameters'] = self.service_parameters
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Service') is not None:
            self.service = m.get('Service')
        if m.get('ServiceParameters') is not None:
            self.service_parameters = m.get('ServiceParameters')
        return self


class ImageModerationResponseBodyDataResult(TeaModel):
    def __init__(
        self,
        confidence: float = None,
        label: str = None,
    ):
        self.confidence = confidence
        self.label = label

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.confidence is not None:
            result['Confidence'] = self.confidence
        if self.label is not None:
            result['Label'] = self.label
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        return self


class ImageModerationResponseBodyData(TeaModel):
    def __init__(
        self,
        data_id: str = None,
        result: List[ImageModerationResponseBodyDataResult] = None,
    ):
        self.data_id = data_id
        self.result = result

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
        if self.data_id is not None:
            result['DataId'] = self.data_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ImageModerationResponseBodyDataResult()
                self.result.append(temp_model.from_map(k))
        return self


class ImageModerationResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: ImageModerationResponseBodyData = None,
        msg: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.msg = msg
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
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ImageModerationResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ImageModerationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ImageModerationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ImageModerationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TextModerationRequest(TeaModel):
    def __init__(
        self,
        service: str = None,
        service_parameters: str = None,
    ):
        self.service = service
        self.service_parameters = service_parameters

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service is not None:
            result['Service'] = self.service
        if self.service_parameters is not None:
            result['ServiceParameters'] = self.service_parameters
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Service') is not None:
            self.service = m.get('Service')
        if m.get('ServiceParameters') is not None:
            self.service_parameters = m.get('ServiceParameters')
        return self


class TextModerationResponseBodyData(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        device_id: str = None,
        labels: str = None,
        reason: str = None,
    ):
        self.account_id = account_id
        self.device_id = device_id
        self.labels = labels
        self.reason = reason

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['accountId'] = self.account_id
        if self.device_id is not None:
            result['deviceId'] = self.device_id
        if self.labels is not None:
            result['labels'] = self.labels
        if self.reason is not None:
            result['reason'] = self.reason
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')
        if m.get('deviceId') is not None:
            self.device_id = m.get('deviceId')
        if m.get('labels') is not None:
            self.labels = m.get('labels')
        if m.get('reason') is not None:
            self.reason = m.get('reason')
        return self


class TextModerationResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: TextModerationResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
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
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = TextModerationResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class TextModerationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: TextModerationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = TextModerationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class VideoModerationRequest(TeaModel):
    def __init__(
        self,
        service: str = None,
        service_parameters: str = None,
    ):
        self.service = service
        self.service_parameters = service_parameters

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service is not None:
            result['Service'] = self.service
        if self.service_parameters is not None:
            result['ServiceParameters'] = self.service_parameters
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Service') is not None:
            self.service = m.get('Service')
        if m.get('ServiceParameters') is not None:
            self.service_parameters = m.get('ServiceParameters')
        return self


class VideoModerationResponseBodyData(TeaModel):
    def __init__(
        self,
        task_id: str = None,
    ):
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class VideoModerationResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: VideoModerationResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        # Id of the request
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
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = VideoModerationResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class VideoModerationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: VideoModerationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = VideoModerationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class VideoModerationCancelRequest(TeaModel):
    def __init__(
        self,
        service: str = None,
        service_parameters: str = None,
    ):
        self.service = service
        self.service_parameters = service_parameters

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service is not None:
            result['Service'] = self.service
        if self.service_parameters is not None:
            result['ServiceParameters'] = self.service_parameters
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Service') is not None:
            self.service = m.get('Service')
        if m.get('ServiceParameters') is not None:
            self.service_parameters = m.get('ServiceParameters')
        return self


class VideoModerationCancelResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        # Id of the request
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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class VideoModerationCancelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: VideoModerationCancelResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = VideoModerationCancelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class VideoModerationResultRequest(TeaModel):
    def __init__(
        self,
        service: str = None,
        service_parameters: str = None,
    ):
        self.service = service
        self.service_parameters = service_parameters

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service is not None:
            result['Service'] = self.service
        if self.service_parameters is not None:
            result['ServiceParameters'] = self.service_parameters
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Service') is not None:
            self.service = m.get('Service')
        if m.get('ServiceParameters') is not None:
            self.service_parameters = m.get('ServiceParameters')
        return self


class VideoModerationResultResponseBodyDataAudioResultSliceDetails(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        end_timestamp: int = None,
        extend: str = None,
        labels: str = None,
        risk_tips: str = None,
        risk_words: str = None,
        score: float = None,
        start_time: int = None,
        start_timestamp: int = None,
        text: str = None,
        url: str = None,
    ):
        self.end_time = end_time
        self.end_timestamp = end_timestamp
        self.extend = extend
        self.labels = labels
        self.risk_tips = risk_tips
        self.risk_words = risk_words
        self.score = score
        self.start_time = start_time
        self.start_timestamp = start_timestamp
        self.text = text
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.end_timestamp is not None:
            result['EndTimestamp'] = self.end_timestamp
        if self.extend is not None:
            result['Extend'] = self.extend
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.risk_tips is not None:
            result['RiskTips'] = self.risk_tips
        if self.risk_words is not None:
            result['RiskWords'] = self.risk_words
        if self.score is not None:
            result['Score'] = self.score
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.start_timestamp is not None:
            result['StartTimestamp'] = self.start_timestamp
        if self.text is not None:
            result['Text'] = self.text
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('EndTimestamp') is not None:
            self.end_timestamp = m.get('EndTimestamp')
        if m.get('Extend') is not None:
            self.extend = m.get('Extend')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('RiskTips') is not None:
            self.risk_tips = m.get('RiskTips')
        if m.get('RiskWords') is not None:
            self.risk_words = m.get('RiskWords')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('StartTimestamp') is not None:
            self.start_timestamp = m.get('StartTimestamp')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class VideoModerationResultResponseBodyDataAudioResult(TeaModel):
    def __init__(
        self,
        slice_details: List[VideoModerationResultResponseBodyDataAudioResultSliceDetails] = None,
    ):
        self.slice_details = slice_details

    def validate(self):
        if self.slice_details:
            for k in self.slice_details:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SliceDetails'] = []
        if self.slice_details is not None:
            for k in self.slice_details:
                result['SliceDetails'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.slice_details = []
        if m.get('SliceDetails') is not None:
            for k in m.get('SliceDetails'):
                temp_model = VideoModerationResultResponseBodyDataAudioResultSliceDetails()
                self.slice_details.append(temp_model.from_map(k))
        return self


class VideoModerationResultResponseBodyDataFrameResultFramesResultsResult(TeaModel):
    def __init__(
        self,
        confidence: float = None,
        label: str = None,
    ):
        self.confidence = confidence
        self.label = label

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.confidence is not None:
            result['Confidence'] = self.confidence
        if self.label is not None:
            result['Label'] = self.label
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        return self


class VideoModerationResultResponseBodyDataFrameResultFramesResults(TeaModel):
    def __init__(
        self,
        result: List[VideoModerationResultResponseBodyDataFrameResultFramesResultsResult] = None,
        service: str = None,
    ):
        self.result = result
        self.service = service

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
        if self.service is not None:
            result['Service'] = self.service
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = VideoModerationResultResponseBodyDataFrameResultFramesResultsResult()
                self.result.append(temp_model.from_map(k))
        if m.get('Service') is not None:
            self.service = m.get('Service')
        return self


class VideoModerationResultResponseBodyDataFrameResultFrames(TeaModel):
    def __init__(
        self,
        offset: float = None,
        results: List[VideoModerationResultResponseBodyDataFrameResultFramesResults] = None,
        temp_url: str = None,
    ):
        self.offset = offset
        self.results = results
        self.temp_url = temp_url

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.offset is not None:
            result['Offset'] = self.offset
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        if self.temp_url is not None:
            result['TempUrl'] = self.temp_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Offset') is not None:
            self.offset = m.get('Offset')
        self.results = []
        if m.get('Results') is not None:
            for k in m.get('Results'):
                temp_model = VideoModerationResultResponseBodyDataFrameResultFramesResults()
                self.results.append(temp_model.from_map(k))
        if m.get('TempUrl') is not None:
            self.temp_url = m.get('TempUrl')
        return self


class VideoModerationResultResponseBodyDataFrameResult(TeaModel):
    def __init__(
        self,
        frame_num: int = None,
        frames: List[VideoModerationResultResponseBodyDataFrameResultFrames] = None,
    ):
        self.frame_num = frame_num
        self.frames = frames

    def validate(self):
        if self.frames:
            for k in self.frames:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.frame_num is not None:
            result['FrameNum'] = self.frame_num
        result['Frames'] = []
        if self.frames is not None:
            for k in self.frames:
                result['Frames'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FrameNum') is not None:
            self.frame_num = m.get('FrameNum')
        self.frames = []
        if m.get('Frames') is not None:
            for k in m.get('Frames'):
                temp_model = VideoModerationResultResponseBodyDataFrameResultFrames()
                self.frames.append(temp_model.from_map(k))
        return self


class VideoModerationResultResponseBodyData(TeaModel):
    def __init__(
        self,
        audio_result: VideoModerationResultResponseBodyDataAudioResult = None,
        data_id: str = None,
        frame_result: VideoModerationResultResponseBodyDataFrameResult = None,
        live_id: str = None,
    ):
        self.audio_result = audio_result
        self.data_id = data_id
        self.frame_result = frame_result
        self.live_id = live_id

    def validate(self):
        if self.audio_result:
            self.audio_result.validate()
        if self.frame_result:
            self.frame_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audio_result is not None:
            result['AudioResult'] = self.audio_result.to_map()
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.frame_result is not None:
            result['FrameResult'] = self.frame_result.to_map()
        if self.live_id is not None:
            result['LiveId'] = self.live_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AudioResult') is not None:
            temp_model = VideoModerationResultResponseBodyDataAudioResult()
            self.audio_result = temp_model.from_map(m['AudioResult'])
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('FrameResult') is not None:
            temp_model = VideoModerationResultResponseBodyDataFrameResult()
            self.frame_result = temp_model.from_map(m['FrameResult'])
        if m.get('LiveId') is not None:
            self.live_id = m.get('LiveId')
        return self


class VideoModerationResultResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: VideoModerationResultResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        # Id of the request
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
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = VideoModerationResultResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class VideoModerationResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: VideoModerationResultResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = VideoModerationResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class VoiceModerationRequest(TeaModel):
    def __init__(
        self,
        service: str = None,
        service_parameters: str = None,
    ):
        self.service = service
        self.service_parameters = service_parameters

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service is not None:
            result['Service'] = self.service
        if self.service_parameters is not None:
            result['ServiceParameters'] = self.service_parameters
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Service') is not None:
            self.service = m.get('Service')
        if m.get('ServiceParameters') is not None:
            self.service_parameters = m.get('ServiceParameters')
        return self


class VoiceModerationResponseBodyData(TeaModel):
    def __init__(
        self,
        task_id: str = None,
    ):
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class VoiceModerationResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: VoiceModerationResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        # Id of the request
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
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = VoiceModerationResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class VoiceModerationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: VoiceModerationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = VoiceModerationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class VoiceModerationCancelRequest(TeaModel):
    def __init__(
        self,
        service: str = None,
        service_parameters: str = None,
    ):
        self.service = service
        self.service_parameters = service_parameters

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service is not None:
            result['Service'] = self.service
        if self.service_parameters is not None:
            result['ServiceParameters'] = self.service_parameters
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Service') is not None:
            self.service = m.get('Service')
        if m.get('ServiceParameters') is not None:
            self.service_parameters = m.get('ServiceParameters')
        return self


class VoiceModerationCancelResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        # Id of the request
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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class VoiceModerationCancelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: VoiceModerationCancelResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = VoiceModerationCancelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class VoiceModerationResultRequest(TeaModel):
    def __init__(
        self,
        service: str = None,
        service_parameters: str = None,
    ):
        self.service = service
        self.service_parameters = service_parameters

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service is not None:
            result['Service'] = self.service
        if self.service_parameters is not None:
            result['ServiceParameters'] = self.service_parameters
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Service') is not None:
            self.service = m.get('Service')
        if m.get('ServiceParameters') is not None:
            self.service_parameters = m.get('ServiceParameters')
        return self


class VoiceModerationResultResponseBodyDataSliceDetails(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        end_timestamp: int = None,
        extend: str = None,
        labels: str = None,
        origin_algo_result: Dict[str, Any] = None,
        risk_tips: str = None,
        risk_words: str = None,
        score: float = None,
        start_time: int = None,
        start_timestamp: int = None,
        text: str = None,
        url: str = None,
    ):
        self.end_time = end_time
        self.end_timestamp = end_timestamp
        self.extend = extend
        self.labels = labels
        self.origin_algo_result = origin_algo_result
        self.risk_tips = risk_tips
        self.risk_words = risk_words
        self.score = score
        self.start_time = start_time
        self.start_timestamp = start_timestamp
        self.text = text
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.end_timestamp is not None:
            result['EndTimestamp'] = self.end_timestamp
        if self.extend is not None:
            result['Extend'] = self.extend
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.origin_algo_result is not None:
            result['OriginAlgoResult'] = self.origin_algo_result
        if self.risk_tips is not None:
            result['RiskTips'] = self.risk_tips
        if self.risk_words is not None:
            result['RiskWords'] = self.risk_words
        if self.score is not None:
            result['Score'] = self.score
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.start_timestamp is not None:
            result['StartTimestamp'] = self.start_timestamp
        if self.text is not None:
            result['Text'] = self.text
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('EndTimestamp') is not None:
            self.end_timestamp = m.get('EndTimestamp')
        if m.get('Extend') is not None:
            self.extend = m.get('Extend')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('OriginAlgoResult') is not None:
            self.origin_algo_result = m.get('OriginAlgoResult')
        if m.get('RiskTips') is not None:
            self.risk_tips = m.get('RiskTips')
        if m.get('RiskWords') is not None:
            self.risk_words = m.get('RiskWords')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('StartTimestamp') is not None:
            self.start_timestamp = m.get('StartTimestamp')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class VoiceModerationResultResponseBodyData(TeaModel):
    def __init__(
        self,
        live_id: str = None,
        slice_details: List[VoiceModerationResultResponseBodyDataSliceDetails] = None,
        task_id: str = None,
        url: str = None,
    ):
        self.live_id = live_id
        self.slice_details = slice_details
        self.task_id = task_id
        self.url = url

    def validate(self):
        if self.slice_details:
            for k in self.slice_details:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.live_id is not None:
            result['LiveId'] = self.live_id
        result['SliceDetails'] = []
        if self.slice_details is not None:
            for k in self.slice_details:
                result['SliceDetails'].append(k.to_map() if k else None)
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LiveId') is not None:
            self.live_id = m.get('LiveId')
        self.slice_details = []
        if m.get('SliceDetails') is not None:
            for k in m.get('SliceDetails'):
                temp_model = VoiceModerationResultResponseBodyDataSliceDetails()
                self.slice_details.append(temp_model.from_map(k))
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class VoiceModerationResultResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: VoiceModerationResultResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        # Id of the request
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
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = VoiceModerationResultResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class VoiceModerationResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: VoiceModerationResultResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = VoiceModerationResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


