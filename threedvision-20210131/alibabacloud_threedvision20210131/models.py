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


