# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import BinaryIO, Dict


class ReconstructBodyBySingleImageRequest(TeaModel):
    def __init__(
        self,
        image_url: str = None,
    ):
        # A short description of struct
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


class ReconstructBodyBySingleImageAdvanceRequest(TeaModel):
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


class ReconstructBodyBySingleImageResponseBodyData(TeaModel):
    def __init__(
        self,
        depth_url: str = None,
        mesh_url: str = None,
    ):
        self.depth_url = depth_url
        self.mesh_url = mesh_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.depth_url is not None:
            result['DepthURL'] = self.depth_url
        if self.mesh_url is not None:
            result['MeshURL'] = self.mesh_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DepthURL') is not None:
            self.depth_url = m.get('DepthURL')
        if m.get('MeshURL') is not None:
            self.mesh_url = m.get('MeshURL')
        return self


class ReconstructBodyBySingleImageResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: ReconstructBodyBySingleImageResponseBodyData = None,
    ):
        # Id of the request
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
            temp_model = ReconstructBodyBySingleImageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class ReconstructBodyBySingleImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ReconstructBodyBySingleImageResponseBody = None,
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
            temp_model = ReconstructBodyBySingleImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReconstructThreeDMultiViewRequest(TeaModel):
    def __init__(
        self,
        zip_file_url: str = None,
        mode: str = None,
    ):
        # A short description of struct
        self.zip_file_url = zip_file_url
        self.mode = mode

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.zip_file_url is not None:
            result['ZipFileUrl'] = self.zip_file_url
        if self.mode is not None:
            result['Mode'] = self.mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ZipFileUrl') is not None:
            self.zip_file_url = m.get('ZipFileUrl')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        return self


class ReconstructThreeDMultiViewAdvanceRequest(TeaModel):
    def __init__(
        self,
        zip_file_url_object: BinaryIO = None,
        mode: str = None,
    ):
        self.zip_file_url_object = zip_file_url_object
        self.mode = mode

    def validate(self):
        self.validate_required(self.zip_file_url_object, 'zip_file_url_object')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.zip_file_url_object is not None:
            result['ZipFileUrlObject'] = self.zip_file_url_object
        if self.mode is not None:
            result['Mode'] = self.mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ZipFileUrlObject') is not None:
            self.zip_file_url_object = m.get('ZipFileUrlObject')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        return self


class ReconstructThreeDMultiViewResponseBodyData(TeaModel):
    def __init__(
        self,
        point_cloud_url: str = None,
    ):
        self.point_cloud_url = point_cloud_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.point_cloud_url is not None:
            result['PointCloudURL'] = self.point_cloud_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PointCloudURL') is not None:
            self.point_cloud_url = m.get('PointCloudURL')
        return self


class ReconstructThreeDMultiViewResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: ReconstructThreeDMultiViewResponseBodyData = None,
    ):
        # Id of the request
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
            temp_model = ReconstructThreeDMultiViewResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class ReconstructThreeDMultiViewResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ReconstructThreeDMultiViewResponseBody = None,
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
            temp_model = ReconstructThreeDMultiViewResponseBody()
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


class EstimateMonocularImageDepthRequest(TeaModel):
    def __init__(
        self,
        image_url: str = None,
    ):
        # A short description of struct
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


class EstimateMonocularImageDepthAdvanceRequest(TeaModel):
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


class EstimateMonocularImageDepthResponseBodyData(TeaModel):
    def __init__(
        self,
        depth_map_url: str = None,
        depth_to_color_url: str = None,
    ):
        self.depth_map_url = depth_map_url
        self.depth_to_color_url = depth_to_color_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.depth_map_url is not None:
            result['DepthMapUrl'] = self.depth_map_url
        if self.depth_to_color_url is not None:
            result['DepthToColorUrl'] = self.depth_to_color_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DepthMapUrl') is not None:
            self.depth_map_url = m.get('DepthMapUrl')
        if m.get('DepthToColorUrl') is not None:
            self.depth_to_color_url = m.get('DepthToColorUrl')
        return self


class EstimateMonocularImageDepthResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: EstimateMonocularImageDepthResponseBodyData = None,
    ):
        # Id of the request
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
            temp_model = EstimateMonocularImageDepthResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class EstimateMonocularImageDepthResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: EstimateMonocularImageDepthResponseBody = None,
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
            temp_model = EstimateMonocularImageDepthResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EstimateStereoImageDepthRequest(TeaModel):
    def __init__(
        self,
        left_image_url: str = None,
        right_image_url: str = None,
    ):
        # A short description of struct
        self.left_image_url = left_image_url
        self.right_image_url = right_image_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.left_image_url is not None:
            result['LeftImageURL'] = self.left_image_url
        if self.right_image_url is not None:
            result['RightImageURL'] = self.right_image_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LeftImageURL') is not None:
            self.left_image_url = m.get('LeftImageURL')
        if m.get('RightImageURL') is not None:
            self.right_image_url = m.get('RightImageURL')
        return self


class EstimateStereoImageDepthResponseBodyData(TeaModel):
    def __init__(
        self,
        disparity_map_url: str = None,
        disparity_vis_url: str = None,
    ):
        self.disparity_map_url = disparity_map_url
        self.disparity_vis_url = disparity_vis_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.disparity_map_url is not None:
            result['DisparityMapURL'] = self.disparity_map_url
        if self.disparity_vis_url is not None:
            result['DisparityVisURL'] = self.disparity_vis_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisparityMapURL') is not None:
            self.disparity_map_url = m.get('DisparityMapURL')
        if m.get('DisparityVisURL') is not None:
            self.disparity_vis_url = m.get('DisparityVisURL')
        return self


class EstimateStereoImageDepthResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: EstimateStereoImageDepthResponseBodyData = None,
    ):
        # Id of the request
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
            temp_model = EstimateStereoImageDepthResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class EstimateStereoImageDepthResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: EstimateStereoImageDepthResponseBody = None,
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
            temp_model = EstimateStereoImageDepthResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EstimateStereoVideoDepthRequest(TeaModel):
    def __init__(
        self,
        video_url: str = None,
        sample_rate: str = None,
    ):
        # A short description of struct
        self.video_url = video_url
        self.sample_rate = sample_rate

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.video_url is not None:
            result['VideoURL'] = self.video_url
        if self.sample_rate is not None:
            result['SampleRate'] = self.sample_rate
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VideoURL') is not None:
            self.video_url = m.get('VideoURL')
        if m.get('SampleRate') is not None:
            self.sample_rate = m.get('SampleRate')
        return self


class EstimateStereoVideoDepthAdvanceRequest(TeaModel):
    def __init__(
        self,
        video_urlobject: BinaryIO = None,
        sample_rate: str = None,
    ):
        self.video_urlobject = video_urlobject
        self.sample_rate = sample_rate

    def validate(self):
        self.validate_required(self.video_urlobject, 'video_urlobject')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.video_urlobject is not None:
            result['VideoURLObject'] = self.video_urlobject
        if self.sample_rate is not None:
            result['SampleRate'] = self.sample_rate
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VideoURLObject') is not None:
            self.video_urlobject = m.get('VideoURLObject')
        if m.get('SampleRate') is not None:
            self.sample_rate = m.get('SampleRate')
        return self


class EstimateStereoVideoDepthResponseBodyData(TeaModel):
    def __init__(
        self,
        depth_url: str = None,
        depth_vis_url: str = None,
    ):
        self.depth_url = depth_url
        self.depth_vis_url = depth_vis_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.depth_url is not None:
            result['DepthUrl'] = self.depth_url
        if self.depth_vis_url is not None:
            result['DepthVisUrl'] = self.depth_vis_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DepthUrl') is not None:
            self.depth_url = m.get('DepthUrl')
        if m.get('DepthVisUrl') is not None:
            self.depth_vis_url = m.get('DepthVisUrl')
        return self


class EstimateStereoVideoDepthResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: EstimateStereoVideoDepthResponseBodyData = None,
    ):
        # Id of the request
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
            temp_model = EstimateStereoVideoDepthResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class EstimateStereoVideoDepthResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: EstimateStereoVideoDepthResponseBody = None,
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
            temp_model = EstimateStereoVideoDepthResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


