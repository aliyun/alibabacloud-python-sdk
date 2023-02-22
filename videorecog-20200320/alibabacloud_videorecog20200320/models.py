# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import BinaryIO, List, Dict, Any


class DetectVideoShotRequest(TeaModel):
    def __init__(
        self,
        video_url: str = None,
    ):
        self.video_url = video_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.video_url is not None:
            result['VideoUrl'] = self.video_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VideoUrl') is not None:
            self.video_url = m.get('VideoUrl')
        return self


class DetectVideoShotAdvanceRequest(TeaModel):
    def __init__(
        self,
        video_url_object: BinaryIO = None,
    ):
        self.video_url_object = video_url_object

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.video_url_object is not None:
            result['VideoUrl'] = self.video_url_object
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VideoUrl') is not None:
            self.video_url_object = m.get('VideoUrl')
        return self


class DetectVideoShotResponseBodyData(TeaModel):
    def __init__(
        self,
        shot_frame_ids: List[int] = None,
    ):
        # 1
        self.shot_frame_ids = shot_frame_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.shot_frame_ids is not None:
            result['ShotFrameIds'] = self.shot_frame_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ShotFrameIds') is not None:
            self.shot_frame_ids = m.get('ShotFrameIds')
        return self


class DetectVideoShotResponseBody(TeaModel):
    def __init__(
        self,
        data: DetectVideoShotResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
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
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DetectVideoShotResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DetectVideoShotResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DetectVideoShotResponseBody = None,
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
            temp_model = DetectVideoShotResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EvaluateVideoQualityRequest(TeaModel):
    def __init__(
        self,
        mode: str = None,
        video_url: str = None,
    ):
        self.mode = mode
        self.video_url = video_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.video_url is not None:
            result['VideoUrl'] = self.video_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('VideoUrl') is not None:
            self.video_url = m.get('VideoUrl')
        return self


class EvaluateVideoQualityAdvanceRequest(TeaModel):
    def __init__(
        self,
        mode: str = None,
        video_url_object: BinaryIO = None,
    ):
        self.mode = mode
        self.video_url_object = video_url_object

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.video_url_object is not None:
            result['VideoUrl'] = self.video_url_object
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('VideoUrl') is not None:
            self.video_url_object = m.get('VideoUrl')
        return self


class EvaluateVideoQualityResponseBodyDataVideoQualityInfo(TeaModel):
    def __init__(
        self,
        blurriness: float = None,
        color_contrast: float = None,
        color_saturation: float = None,
        colorfulness: float = None,
        compressive_strength: float = None,
        luminance: float = None,
        mos_score: float = None,
        noise_intensity: float = None,
    ):
        self.blurriness = blurriness
        self.color_contrast = color_contrast
        self.color_saturation = color_saturation
        self.colorfulness = colorfulness
        self.compressive_strength = compressive_strength
        self.luminance = luminance
        self.mos_score = mos_score
        self.noise_intensity = noise_intensity

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.blurriness is not None:
            result['Blurriness'] = self.blurriness
        if self.color_contrast is not None:
            result['ColorContrast'] = self.color_contrast
        if self.color_saturation is not None:
            result['ColorSaturation'] = self.color_saturation
        if self.colorfulness is not None:
            result['Colorfulness'] = self.colorfulness
        if self.compressive_strength is not None:
            result['CompressiveStrength'] = self.compressive_strength
        if self.luminance is not None:
            result['Luminance'] = self.luminance
        if self.mos_score is not None:
            result['MosScore'] = self.mos_score
        if self.noise_intensity is not None:
            result['NoiseIntensity'] = self.noise_intensity
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Blurriness') is not None:
            self.blurriness = m.get('Blurriness')
        if m.get('ColorContrast') is not None:
            self.color_contrast = m.get('ColorContrast')
        if m.get('ColorSaturation') is not None:
            self.color_saturation = m.get('ColorSaturation')
        if m.get('Colorfulness') is not None:
            self.colorfulness = m.get('Colorfulness')
        if m.get('CompressiveStrength') is not None:
            self.compressive_strength = m.get('CompressiveStrength')
        if m.get('Luminance') is not None:
            self.luminance = m.get('Luminance')
        if m.get('MosScore') is not None:
            self.mos_score = m.get('MosScore')
        if m.get('NoiseIntensity') is not None:
            self.noise_intensity = m.get('NoiseIntensity')
        return self


class EvaluateVideoQualityResponseBodyData(TeaModel):
    def __init__(
        self,
        json_url: str = None,
        pdf_url: str = None,
        video_quality_info: EvaluateVideoQualityResponseBodyDataVideoQualityInfo = None,
    ):
        self.json_url = json_url
        self.pdf_url = pdf_url
        self.video_quality_info = video_quality_info

    def validate(self):
        if self.video_quality_info:
            self.video_quality_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.json_url is not None:
            result['JsonUrl'] = self.json_url
        if self.pdf_url is not None:
            result['PdfUrl'] = self.pdf_url
        if self.video_quality_info is not None:
            result['VideoQualityInfo'] = self.video_quality_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JsonUrl') is not None:
            self.json_url = m.get('JsonUrl')
        if m.get('PdfUrl') is not None:
            self.pdf_url = m.get('PdfUrl')
        if m.get('VideoQualityInfo') is not None:
            temp_model = EvaluateVideoQualityResponseBodyDataVideoQualityInfo()
            self.video_quality_info = temp_model.from_map(m['VideoQualityInfo'])
        return self


class EvaluateVideoQualityResponseBody(TeaModel):
    def __init__(
        self,
        data: EvaluateVideoQualityResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
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
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = EvaluateVideoQualityResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class EvaluateVideoQualityResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EvaluateVideoQualityResponseBody = None,
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
            temp_model = EvaluateVideoQualityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateVideoCoverRequest(TeaModel):
    def __init__(
        self,
        is_gif: bool = None,
        video_url: str = None,
    ):
        self.is_gif = is_gif
        self.video_url = video_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_gif is not None:
            result['IsGif'] = self.is_gif
        if self.video_url is not None:
            result['VideoUrl'] = self.video_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsGif') is not None:
            self.is_gif = m.get('IsGif')
        if m.get('VideoUrl') is not None:
            self.video_url = m.get('VideoUrl')
        return self


class GenerateVideoCoverAdvanceRequest(TeaModel):
    def __init__(
        self,
        is_gif: bool = None,
        video_url_object: BinaryIO = None,
    ):
        self.is_gif = is_gif
        self.video_url_object = video_url_object

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_gif is not None:
            result['IsGif'] = self.is_gif
        if self.video_url_object is not None:
            result['VideoUrl'] = self.video_url_object
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsGif') is not None:
            self.is_gif = m.get('IsGif')
        if m.get('VideoUrl') is not None:
            self.video_url_object = m.get('VideoUrl')
        return self


class GenerateVideoCoverResponseBodyDataOutputs(TeaModel):
    def __init__(
        self,
        confidence: float = None,
        image_url: str = None,
    ):
        self.confidence = confidence
        self.image_url = image_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.confidence is not None:
            result['Confidence'] = self.confidence
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        return self


class GenerateVideoCoverResponseBodyData(TeaModel):
    def __init__(
        self,
        outputs: List[GenerateVideoCoverResponseBodyDataOutputs] = None,
    ):
        self.outputs = outputs

    def validate(self):
        if self.outputs:
            for k in self.outputs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Outputs'] = []
        if self.outputs is not None:
            for k in self.outputs:
                result['Outputs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.outputs = []
        if m.get('Outputs') is not None:
            for k in m.get('Outputs'):
                temp_model = GenerateVideoCoverResponseBodyDataOutputs()
                self.outputs.append(temp_model.from_map(k))
        return self


class GenerateVideoCoverResponseBody(TeaModel):
    def __init__(
        self,
        data: GenerateVideoCoverResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
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
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GenerateVideoCoverResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GenerateVideoCoverResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GenerateVideoCoverResponseBody = None,
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
            temp_model = GenerateVideoCoverResponseBody()
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
        error_code: str = None,
        error_message: str = None,
        job_id: str = None,
        result: str = None,
        status: str = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.job_id = job_id
        self.result = result
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.result is not None:
            result['Result'] = self.result
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetAsyncJobResultResponseBody(TeaModel):
    def __init__(
        self,
        data: GetAsyncJobResultResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetAsyncJobResultResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetAsyncJobResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAsyncJobResultResponseBody = None,
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
            temp_model = GetAsyncJobResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeVideoCastCrewListRequestParams(TeaModel):
    def __init__(
        self,
        type: str = None,
    ):
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class RecognizeVideoCastCrewListRequest(TeaModel):
    def __init__(
        self,
        params: List[RecognizeVideoCastCrewListRequestParams] = None,
        video_url: str = None,
    ):
        self.params = params
        self.video_url = video_url

    def validate(self):
        if self.params:
            for k in self.params:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Params'] = []
        if self.params is not None:
            for k in self.params:
                result['Params'].append(k.to_map() if k else None)
        if self.video_url is not None:
            result['VideoUrl'] = self.video_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.params = []
        if m.get('Params') is not None:
            for k in m.get('Params'):
                temp_model = RecognizeVideoCastCrewListRequestParams()
                self.params.append(temp_model.from_map(k))
        if m.get('VideoUrl') is not None:
            self.video_url = m.get('VideoUrl')
        return self


class RecognizeVideoCastCrewListAdvanceRequestParams(TeaModel):
    def __init__(
        self,
        type: str = None,
    ):
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class RecognizeVideoCastCrewListAdvanceRequest(TeaModel):
    def __init__(
        self,
        params: List[RecognizeVideoCastCrewListAdvanceRequestParams] = None,
        video_url_object: BinaryIO = None,
    ):
        self.params = params
        self.video_url_object = video_url_object

    def validate(self):
        if self.params:
            for k in self.params:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Params'] = []
        if self.params is not None:
            for k in self.params:
                result['Params'].append(k.to_map() if k else None)
        if self.video_url_object is not None:
            result['VideoUrl'] = self.video_url_object
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.params = []
        if m.get('Params') is not None:
            for k in m.get('Params'):
                temp_model = RecognizeVideoCastCrewListAdvanceRequestParams()
                self.params.append(temp_model.from_map(k))
        if m.get('VideoUrl') is not None:
            self.video_url_object = m.get('VideoUrl')
        return self


class RecognizeVideoCastCrewListShrinkRequest(TeaModel):
    def __init__(
        self,
        params_shrink: str = None,
        video_url: str = None,
    ):
        self.params_shrink = params_shrink
        self.video_url = video_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.params_shrink is not None:
            result['Params'] = self.params_shrink
        if self.video_url is not None:
            result['VideoUrl'] = self.video_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Params') is not None:
            self.params_shrink = m.get('Params')
        if m.get('VideoUrl') is not None:
            self.video_url = m.get('VideoUrl')
        return self


class RecognizeVideoCastCrewListResponseBodyDataCastResults(TeaModel):
    def __init__(
        self,
        detail_info: Dict[str, str] = None,
        end_time: float = None,
        start_time: float = None,
    ):
        self.detail_info = detail_info
        self.end_time = end_time
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.detail_info is not None:
            result['DetailInfo'] = self.detail_info
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DetailInfo') is not None:
            self.detail_info = m.get('DetailInfo')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class RecognizeVideoCastCrewListResponseBodyDataOcrResultsDetailInfoPosition(TeaModel):
    def __init__(
        self,
        x: int = None,
        y: int = None,
    ):
        self.x = x
        self.y = y

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        return self


class RecognizeVideoCastCrewListResponseBodyDataOcrResultsDetailInfo(TeaModel):
    def __init__(
        self,
        boxes: List[int] = None,
        char_probs: List[List[float]] = None,
        frame_index: int = None,
        position: List[RecognizeVideoCastCrewListResponseBodyDataOcrResultsDetailInfoPosition] = None,
        score: float = None,
        text: str = None,
        text_prob: float = None,
        time_stamp: float = None,
        track_id: int = None,
    ):
        self.boxes = boxes
        self.char_probs = char_probs
        self.frame_index = frame_index
        self.position = position
        self.score = score
        self.text = text
        self.text_prob = text_prob
        self.time_stamp = time_stamp
        self.track_id = track_id

    def validate(self):
        if self.position:
            for k in self.position:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.boxes is not None:
            result['Boxes'] = self.boxes
        if self.char_probs is not None:
            result['CharProbs'] = self.char_probs
        if self.frame_index is not None:
            result['FrameIndex'] = self.frame_index
        result['Position'] = []
        if self.position is not None:
            for k in self.position:
                result['Position'].append(k.to_map() if k else None)
        if self.score is not None:
            result['Score'] = self.score
        if self.text is not None:
            result['Text'] = self.text
        if self.text_prob is not None:
            result['TextProb'] = self.text_prob
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.track_id is not None:
            result['TrackId'] = self.track_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Boxes') is not None:
            self.boxes = m.get('Boxes')
        if m.get('CharProbs') is not None:
            self.char_probs = m.get('CharProbs')
        if m.get('FrameIndex') is not None:
            self.frame_index = m.get('FrameIndex')
        self.position = []
        if m.get('Position') is not None:
            for k in m.get('Position'):
                temp_model = RecognizeVideoCastCrewListResponseBodyDataOcrResultsDetailInfoPosition()
                self.position.append(temp_model.from_map(k))
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('TextProb') is not None:
            self.text_prob = m.get('TextProb')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('TrackId') is not None:
            self.track_id = m.get('TrackId')
        return self


class RecognizeVideoCastCrewListResponseBodyDataOcrResults(TeaModel):
    def __init__(
        self,
        detail_info: List[RecognizeVideoCastCrewListResponseBodyDataOcrResultsDetailInfo] = None,
        end_time: float = None,
        start_time: float = None,
    ):
        self.detail_info = detail_info
        self.end_time = end_time
        self.start_time = start_time

    def validate(self):
        if self.detail_info:
            for k in self.detail_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DetailInfo'] = []
        if self.detail_info is not None:
            for k in self.detail_info:
                result['DetailInfo'].append(k.to_map() if k else None)
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.detail_info = []
        if m.get('DetailInfo') is not None:
            for k in m.get('DetailInfo'):
                temp_model = RecognizeVideoCastCrewListResponseBodyDataOcrResultsDetailInfo()
                self.detail_info.append(temp_model.from_map(k))
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class RecognizeVideoCastCrewListResponseBodyDataSubtitlesResults(TeaModel):
    def __init__(
        self,
        subtitles_all_results: Dict[str, str] = None,
        subtitles_all_results_url: str = None,
        subtitles_chinese_results: Dict[str, str] = None,
        subtitles_chinese_results_url: str = None,
        subtitles_english_results: Dict[str, Any] = None,
        subtitles_english_results_url: str = None,
    ):
        self.subtitles_all_results = subtitles_all_results
        self.subtitles_all_results_url = subtitles_all_results_url
        self.subtitles_chinese_results = subtitles_chinese_results
        self.subtitles_chinese_results_url = subtitles_chinese_results_url
        self.subtitles_english_results = subtitles_english_results
        self.subtitles_english_results_url = subtitles_english_results_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.subtitles_all_results is not None:
            result['SubtitlesAllResults'] = self.subtitles_all_results
        if self.subtitles_all_results_url is not None:
            result['SubtitlesAllResultsUrl'] = self.subtitles_all_results_url
        if self.subtitles_chinese_results is not None:
            result['SubtitlesChineseResults'] = self.subtitles_chinese_results
        if self.subtitles_chinese_results_url is not None:
            result['SubtitlesChineseResultsUrl'] = self.subtitles_chinese_results_url
        if self.subtitles_english_results is not None:
            result['SubtitlesEnglishResults'] = self.subtitles_english_results
        if self.subtitles_english_results_url is not None:
            result['SubtitlesEnglishResultsUrl'] = self.subtitles_english_results_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SubtitlesAllResults') is not None:
            self.subtitles_all_results = m.get('SubtitlesAllResults')
        if m.get('SubtitlesAllResultsUrl') is not None:
            self.subtitles_all_results_url = m.get('SubtitlesAllResultsUrl')
        if m.get('SubtitlesChineseResults') is not None:
            self.subtitles_chinese_results = m.get('SubtitlesChineseResults')
        if m.get('SubtitlesChineseResultsUrl') is not None:
            self.subtitles_chinese_results_url = m.get('SubtitlesChineseResultsUrl')
        if m.get('SubtitlesEnglishResults') is not None:
            self.subtitles_english_results = m.get('SubtitlesEnglishResults')
        if m.get('SubtitlesEnglishResultsUrl') is not None:
            self.subtitles_english_results_url = m.get('SubtitlesEnglishResultsUrl')
        return self


class RecognizeVideoCastCrewListResponseBodyDataVideoOcrResultsDetailInfoPosition(TeaModel):
    def __init__(
        self,
        x: int = None,
        y: int = None,
    ):
        self.x = x
        self.y = y

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        return self


class RecognizeVideoCastCrewListResponseBodyDataVideoOcrResultsDetailInfo(TeaModel):
    def __init__(
        self,
        boxes: List[int] = None,
        position: List[RecognizeVideoCastCrewListResponseBodyDataVideoOcrResultsDetailInfoPosition] = None,
        score: float = None,
        text: str = None,
        text_type: int = None,
    ):
        self.boxes = boxes
        self.position = position
        self.score = score
        self.text = text
        self.text_type = text_type

    def validate(self):
        if self.position:
            for k in self.position:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.boxes is not None:
            result['Boxes'] = self.boxes
        result['Position'] = []
        if self.position is not None:
            for k in self.position:
                result['Position'].append(k.to_map() if k else None)
        if self.score is not None:
            result['Score'] = self.score
        if self.text is not None:
            result['Text'] = self.text
        if self.text_type is not None:
            result['TextType'] = self.text_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Boxes') is not None:
            self.boxes = m.get('Boxes')
        self.position = []
        if m.get('Position') is not None:
            for k in m.get('Position'):
                temp_model = RecognizeVideoCastCrewListResponseBodyDataVideoOcrResultsDetailInfoPosition()
                self.position.append(temp_model.from_map(k))
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('TextType') is not None:
            self.text_type = m.get('TextType')
        return self


class RecognizeVideoCastCrewListResponseBodyDataVideoOcrResults(TeaModel):
    def __init__(
        self,
        detail_info: List[RecognizeVideoCastCrewListResponseBodyDataVideoOcrResultsDetailInfo] = None,
        end_time: float = None,
        start_time: float = None,
    ):
        self.detail_info = detail_info
        self.end_time = end_time
        self.start_time = start_time

    def validate(self):
        if self.detail_info:
            for k in self.detail_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DetailInfo'] = []
        if self.detail_info is not None:
            for k in self.detail_info:
                result['DetailInfo'].append(k.to_map() if k else None)
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.detail_info = []
        if m.get('DetailInfo') is not None:
            for k in m.get('DetailInfo'):
                temp_model = RecognizeVideoCastCrewListResponseBodyDataVideoOcrResultsDetailInfo()
                self.detail_info.append(temp_model.from_map(k))
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class RecognizeVideoCastCrewListResponseBodyData(TeaModel):
    def __init__(
        self,
        cast_results: List[RecognizeVideoCastCrewListResponseBodyDataCastResults] = None,
        ocr_results: List[RecognizeVideoCastCrewListResponseBodyDataOcrResults] = None,
        ocr_results_url: str = None,
        ocr_video_results_url: str = None,
        subtitles_results: List[RecognizeVideoCastCrewListResponseBodyDataSubtitlesResults] = None,
        video_ocr_results: List[RecognizeVideoCastCrewListResponseBodyDataVideoOcrResults] = None,
    ):
        self.cast_results = cast_results
        self.ocr_results = ocr_results
        self.ocr_results_url = ocr_results_url
        self.ocr_video_results_url = ocr_video_results_url
        self.subtitles_results = subtitles_results
        self.video_ocr_results = video_ocr_results

    def validate(self):
        if self.cast_results:
            for k in self.cast_results:
                if k:
                    k.validate()
        if self.ocr_results:
            for k in self.ocr_results:
                if k:
                    k.validate()
        if self.subtitles_results:
            for k in self.subtitles_results:
                if k:
                    k.validate()
        if self.video_ocr_results:
            for k in self.video_ocr_results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CastResults'] = []
        if self.cast_results is not None:
            for k in self.cast_results:
                result['CastResults'].append(k.to_map() if k else None)
        result['OcrResults'] = []
        if self.ocr_results is not None:
            for k in self.ocr_results:
                result['OcrResults'].append(k.to_map() if k else None)
        if self.ocr_results_url is not None:
            result['OcrResultsUrl'] = self.ocr_results_url
        if self.ocr_video_results_url is not None:
            result['OcrVideoResultsUrl'] = self.ocr_video_results_url
        result['SubtitlesResults'] = []
        if self.subtitles_results is not None:
            for k in self.subtitles_results:
                result['SubtitlesResults'].append(k.to_map() if k else None)
        result['VideoOcrResults'] = []
        if self.video_ocr_results is not None:
            for k in self.video_ocr_results:
                result['VideoOcrResults'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cast_results = []
        if m.get('CastResults') is not None:
            for k in m.get('CastResults'):
                temp_model = RecognizeVideoCastCrewListResponseBodyDataCastResults()
                self.cast_results.append(temp_model.from_map(k))
        self.ocr_results = []
        if m.get('OcrResults') is not None:
            for k in m.get('OcrResults'):
                temp_model = RecognizeVideoCastCrewListResponseBodyDataOcrResults()
                self.ocr_results.append(temp_model.from_map(k))
        if m.get('OcrResultsUrl') is not None:
            self.ocr_results_url = m.get('OcrResultsUrl')
        if m.get('OcrVideoResultsUrl') is not None:
            self.ocr_video_results_url = m.get('OcrVideoResultsUrl')
        self.subtitles_results = []
        if m.get('SubtitlesResults') is not None:
            for k in m.get('SubtitlesResults'):
                temp_model = RecognizeVideoCastCrewListResponseBodyDataSubtitlesResults()
                self.subtitles_results.append(temp_model.from_map(k))
        self.video_ocr_results = []
        if m.get('VideoOcrResults') is not None:
            for k in m.get('VideoOcrResults'):
                temp_model = RecognizeVideoCastCrewListResponseBodyDataVideoOcrResults()
                self.video_ocr_results.append(temp_model.from_map(k))
        return self


class RecognizeVideoCastCrewListResponseBody(TeaModel):
    def __init__(
        self,
        data: RecognizeVideoCastCrewListResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
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
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = RecognizeVideoCastCrewListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RecognizeVideoCastCrewListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RecognizeVideoCastCrewListResponseBody = None,
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
            temp_model = RecognizeVideoCastCrewListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SplitVideoPartsRequest(TeaModel):
    def __init__(
        self,
        template: str = None,
        video_url: str = None,
    ):
        self.template = template
        self.video_url = video_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.template is not None:
            result['Template'] = self.template
        if self.video_url is not None:
            result['VideoUrl'] = self.video_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('VideoUrl') is not None:
            self.video_url = m.get('VideoUrl')
        return self


class SplitVideoPartsAdvanceRequest(TeaModel):
    def __init__(
        self,
        template: str = None,
        video_url_object: BinaryIO = None,
    ):
        self.template = template
        self.video_url_object = video_url_object

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.template is not None:
            result['Template'] = self.template
        if self.video_url_object is not None:
            result['VideoUrl'] = self.video_url_object
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('VideoUrl') is not None:
            self.video_url_object = m.get('VideoUrl')
        return self


class SplitVideoPartsResponseBodyDataElements(TeaModel):
    def __init__(
        self,
        begin_time: float = None,
        end_time: float = None,
        index: int = None,
    ):
        self.begin_time = begin_time
        self.end_time = end_time
        self.index = index

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.index is not None:
            result['Index'] = self.index
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Index') is not None:
            self.index = m.get('Index')
        return self


class SplitVideoPartsResponseBodyDataSplitVideoPartResults(TeaModel):
    def __init__(
        self,
        begin_time: float = None,
        by: str = None,
        end_time: float = None,
        theme: str = None,
        type: str = None,
    ):
        self.begin_time = begin_time
        self.by = by
        self.end_time = end_time
        self.theme = theme
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.by is not None:
            result['By'] = self.by
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.theme is not None:
            result['Theme'] = self.theme
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('By') is not None:
            self.by = m.get('By')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Theme') is not None:
            self.theme = m.get('Theme')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class SplitVideoPartsResponseBodyData(TeaModel):
    def __init__(
        self,
        elements: List[SplitVideoPartsResponseBodyDataElements] = None,
        split_video_part_results: List[SplitVideoPartsResponseBodyDataSplitVideoPartResults] = None,
    ):
        self.elements = elements
        self.split_video_part_results = split_video_part_results

    def validate(self):
        if self.elements:
            for k in self.elements:
                if k:
                    k.validate()
        if self.split_video_part_results:
            for k in self.split_video_part_results:
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
        result['SplitVideoPartResults'] = []
        if self.split_video_part_results is not None:
            for k in self.split_video_part_results:
                result['SplitVideoPartResults'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.elements = []
        if m.get('Elements') is not None:
            for k in m.get('Elements'):
                temp_model = SplitVideoPartsResponseBodyDataElements()
                self.elements.append(temp_model.from_map(k))
        self.split_video_part_results = []
        if m.get('SplitVideoPartResults') is not None:
            for k in m.get('SplitVideoPartResults'):
                temp_model = SplitVideoPartsResponseBodyDataSplitVideoPartResults()
                self.split_video_part_results.append(temp_model.from_map(k))
        return self


class SplitVideoPartsResponseBody(TeaModel):
    def __init__(
        self,
        data: SplitVideoPartsResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
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
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = SplitVideoPartsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SplitVideoPartsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SplitVideoPartsResponseBody = None,
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
            temp_model = SplitVideoPartsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnderstandVideoContentRequest(TeaModel):
    def __init__(
        self,
        video_url: str = None,
    ):
        self.video_url = video_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.video_url is not None:
            result['VideoURL'] = self.video_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VideoURL') is not None:
            self.video_url = m.get('VideoURL')
        return self


class UnderstandVideoContentAdvanceRequest(TeaModel):
    def __init__(
        self,
        video_urlobject: BinaryIO = None,
    ):
        self.video_urlobject = video_urlobject

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.video_urlobject is not None:
            result['VideoURL'] = self.video_urlobject
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VideoURL') is not None:
            self.video_urlobject = m.get('VideoURL')
        return self


class UnderstandVideoContentResponseBodyDataVideoInfo(TeaModel):
    def __init__(
        self,
        duration: int = None,
        fps: float = None,
        height: int = None,
        width: int = None,
    ):
        self.duration = duration
        self.fps = fps
        self.height = height
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.fps is not None:
            result['Fps'] = self.fps
        if self.height is not None:
            result['Height'] = self.height
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Fps') is not None:
            self.fps = m.get('Fps')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class UnderstandVideoContentResponseBodyData(TeaModel):
    def __init__(
        self,
        tag_info: Dict[str, Any] = None,
        video_info: UnderstandVideoContentResponseBodyDataVideoInfo = None,
    ):
        self.tag_info = tag_info
        self.video_info = video_info

    def validate(self):
        if self.video_info:
            self.video_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_info is not None:
            result['TagInfo'] = self.tag_info
        if self.video_info is not None:
            result['VideoInfo'] = self.video_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagInfo') is not None:
            self.tag_info = m.get('TagInfo')
        if m.get('VideoInfo') is not None:
            temp_model = UnderstandVideoContentResponseBodyDataVideoInfo()
            self.video_info = temp_model.from_map(m['VideoInfo'])
        return self


class UnderstandVideoContentResponseBody(TeaModel):
    def __init__(
        self,
        data: UnderstandVideoContentResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
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
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = UnderstandVideoContentResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UnderstandVideoContentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UnderstandVideoContentResponseBody = None,
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
            temp_model = UnderstandVideoContentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


