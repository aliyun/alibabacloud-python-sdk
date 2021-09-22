# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict


class CalibRequestFeatureMatch(TeaModel):
    def __init__(
        self,
        img_0: str = None,
        img_1: str = None,
        match_num: int = None,
        img_0kpts: List[List[float]] = None,
        img_1kpts: List[List[float]] = None,
    ):
        self.img_0 = img_0
        self.img_1 = img_1
        self.match_num = match_num
        self.img_0kpts = img_0kpts
        self.img_1kpts = img_1kpts

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.img_0 is not None:
            result['img0'] = self.img_0
        if self.img_1 is not None:
            result['img1'] = self.img_1
        if self.match_num is not None:
            result['match_num'] = self.match_num
        if self.img_0kpts is not None:
            result['img0_kpts'] = self.img_0kpts
        if self.img_1kpts is not None:
            result['img1_kpts'] = self.img_1kpts
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('img0') is not None:
            self.img_0 = m.get('img0')
        if m.get('img1') is not None:
            self.img_1 = m.get('img1')
        if m.get('match_num') is not None:
            self.match_num = m.get('match_num')
        if m.get('img0_kpts') is not None:
            self.img_0kpts = m.get('img0_kpts')
        if m.get('img1_kpts') is not None:
            self.img_1kpts = m.get('img1_kpts')
        return self


class CalibRequest(TeaModel):
    def __init__(
        self,
        scene_id: str = None,
        floor_id: str = None,
        camera_id: str = None,
        feature_match: CalibRequestFeatureMatch = None,
        camera_type: str = None,
        zoom_level: str = None,
        kpts_num: str = None,
        reproject_thresh: str = None,
    ):
        self.scene_id = scene_id
        self.floor_id = floor_id
        self.camera_id = camera_id
        self.feature_match = feature_match
        self.camera_type = camera_type
        self.zoom_level = zoom_level
        self.kpts_num = kpts_num
        self.reproject_thresh = reproject_thresh

    def validate(self):
        if self.feature_match:
            self.feature_match.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scene_id is not None:
            result['sceneId'] = self.scene_id
        if self.floor_id is not None:
            result['floorId'] = self.floor_id
        if self.camera_id is not None:
            result['cameraId'] = self.camera_id
        if self.feature_match is not None:
            result['featureMatch'] = self.feature_match.to_map()
        if self.camera_type is not None:
            result['cameraType'] = self.camera_type
        if self.zoom_level is not None:
            result['zoomLevel'] = self.zoom_level
        if self.kpts_num is not None:
            result['kptsNum'] = self.kpts_num
        if self.reproject_thresh is not None:
            result['reprojectThresh'] = self.reproject_thresh
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('sceneId') is not None:
            self.scene_id = m.get('sceneId')
        if m.get('floorId') is not None:
            self.floor_id = m.get('floorId')
        if m.get('cameraId') is not None:
            self.camera_id = m.get('cameraId')
        if m.get('featureMatch') is not None:
            temp_model = CalibRequestFeatureMatch()
            self.feature_match = temp_model.from_map(m['featureMatch'])
        if m.get('cameraType') is not None:
            self.camera_type = m.get('cameraType')
        if m.get('zoomLevel') is not None:
            self.zoom_level = m.get('zoomLevel')
        if m.get('kptsNum') is not None:
            self.kpts_num = m.get('kptsNum')
        if m.get('reprojectThresh') is not None:
            self.reproject_thresh = m.get('reprojectThresh')
        return self


class CalibResponseBodyResults(TeaModel):
    def __init__(
        self,
        h_cam_2map: List[List[float]] = None,
        t: List[float] = None,
        q: List[float] = None,
        cam_inmap: List[float] = None,
    ):
        self.h_cam_2map = h_cam_2map
        self.t = t
        self.q = q
        self.cam_inmap = cam_inmap

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.h_cam_2map is not None:
            result['H_cam2map'] = self.h_cam_2map
        if self.t is not None:
            result['t'] = self.t
        if self.q is not None:
            result['Q'] = self.q
        if self.cam_inmap is not None:
            result['cam_inmap'] = self.cam_inmap
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('H_cam2map') is not None:
            self.h_cam_2map = m.get('H_cam2map')
        if m.get('t') is not None:
            self.t = m.get('t')
        if m.get('Q') is not None:
            self.q = m.get('Q')
        if m.get('cam_inmap') is not None:
            self.cam_inmap = m.get('cam_inmap')
        return self


class CalibResponseBody(TeaModel):
    def __init__(
        self,
        success: int = None,
        errmsg: str = None,
        results: CalibResponseBodyResults = None,
    ):
        self.success = success
        self.errmsg = errmsg
        self.results = results

    def validate(self):
        if self.results:
            self.results.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.success is not None:
            result['success'] = self.success
        if self.errmsg is not None:
            result['errmsg'] = self.errmsg
        if self.results is not None:
            result['results'] = self.results.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('errmsg') is not None:
            self.errmsg = m.get('errmsg')
        if m.get('results') is not None:
            temp_model = CalibResponseBodyResults()
            self.results = temp_model.from_map(m['results'])
        return self


class CalibResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CalibResponseBody = None,
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
            temp_model = CalibResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReidBodyRequest(TeaModel):
    def __init__(
        self,
        picture_url: List[str] = None,
    ):
        # pictureUrl list
        self.picture_url = picture_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.picture_url is not None:
            result['pictureUrl'] = self.picture_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pictureUrl') is not None:
            self.picture_url = m.get('pictureUrl')
        return self


class ReidBodyResponseBody(TeaModel):
    def __init__(
        self,
        success: int = None,
        errmsg: str = None,
        vector: List[List[float]] = None,
        valid: List[int] = None,
    ):
        self.success = success
        self.errmsg = errmsg
        self.vector = vector
        self.valid = valid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.success is not None:
            result['success'] = self.success
        if self.errmsg is not None:
            result['errmsg'] = self.errmsg
        if self.vector is not None:
            result['vector'] = self.vector
        if self.valid is not None:
            result['valid'] = self.valid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('errmsg') is not None:
            self.errmsg = m.get('errmsg')
        if m.get('vector') is not None:
            self.vector = m.get('vector')
        if m.get('valid') is not None:
            self.valid = m.get('valid')
        return self


class ReidBodyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ReidBodyResponseBody = None,
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
            temp_model = ReidBodyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AttrBodyRequest(TeaModel):
    def __init__(
        self,
        picture_url: List[str] = None,
    ):
        # pic list
        self.picture_url = picture_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.picture_url is not None:
            result['pictureUrl'] = self.picture_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pictureUrl') is not None:
            self.picture_url = m.get('pictureUrl')
        return self


class AttrBodyResponseBodyAttributes(TeaModel):
    def __init__(
        self,
        gender: str = None,
        gender_score: float = None,
        age: str = None,
        age_score: float = None,
        direction: str = None,
        direction_score: float = None,
        quality: float = None,
    ):
        self.gender = gender
        self.gender_score = gender_score
        self.age = age
        self.age_score = age_score
        self.direction = direction
        self.direction_score = direction_score
        self.quality = quality

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gender is not None:
            result['gender'] = self.gender
        if self.gender_score is not None:
            result['genderScore'] = self.gender_score
        if self.age is not None:
            result['age'] = self.age
        if self.age_score is not None:
            result['ageScore'] = self.age_score
        if self.direction is not None:
            result['direction'] = self.direction
        if self.direction_score is not None:
            result['directionScore'] = self.direction_score
        if self.quality is not None:
            result['quality'] = self.quality
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gender') is not None:
            self.gender = m.get('gender')
        if m.get('genderScore') is not None:
            self.gender_score = m.get('genderScore')
        if m.get('age') is not None:
            self.age = m.get('age')
        if m.get('ageScore') is not None:
            self.age_score = m.get('ageScore')
        if m.get('direction') is not None:
            self.direction = m.get('direction')
        if m.get('directionScore') is not None:
            self.direction_score = m.get('directionScore')
        if m.get('quality') is not None:
            self.quality = m.get('quality')
        return self


class AttrBodyResponseBody(TeaModel):
    def __init__(
        self,
        success: int = None,
        errmsg: str = None,
        attributes: List[AttrBodyResponseBodyAttributes] = None,
        valid: List[int] = None,
    ):
        self.success = success
        self.errmsg = errmsg
        self.attributes = attributes
        self.valid = valid

    def validate(self):
        if self.attributes:
            for k in self.attributes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.success is not None:
            result['success'] = self.success
        if self.errmsg is not None:
            result['errmsg'] = self.errmsg
        result['attributes'] = []
        if self.attributes is not None:
            for k in self.attributes:
                result['attributes'].append(k.to_map() if k else None)
        if self.valid is not None:
            result['valid'] = self.valid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('errmsg') is not None:
            self.errmsg = m.get('errmsg')
        self.attributes = []
        if m.get('attributes') is not None:
            for k in m.get('attributes'):
                temp_model = AttrBodyResponseBodyAttributes()
                self.attributes.append(temp_model.from_map(k))
        if m.get('valid') is not None:
            self.valid = m.get('valid')
        return self


class AttrBodyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AttrBodyResponseBody = None,
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
            temp_model = AttrBodyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReidFaceRequest(TeaModel):
    def __init__(
        self,
        picture_url: List[str] = None,
    ):
        # pic list
        self.picture_url = picture_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.picture_url is not None:
            result['pictureUrl'] = self.picture_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pictureUrl') is not None:
            self.picture_url = m.get('pictureUrl')
        return self


class ReidFaceResponseBody(TeaModel):
    def __init__(
        self,
        success: int = None,
        errmsg: str = None,
        vector: List[List[float]] = None,
        valid: List[int] = None,
    ):
        self.success = success
        self.errmsg = errmsg
        self.vector = vector
        self.valid = valid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.success is not None:
            result['success'] = self.success
        if self.errmsg is not None:
            result['errmsg'] = self.errmsg
        if self.vector is not None:
            result['vector'] = self.vector
        if self.valid is not None:
            result['valid'] = self.valid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('errmsg') is not None:
            self.errmsg = m.get('errmsg')
        if m.get('vector') is not None:
            self.vector = m.get('vector')
        if m.get('valid') is not None:
            self.valid = m.get('valid')
        return self


class ReidFaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ReidFaceResponseBody = None,
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
            temp_model = ReidFaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AttrFaceRequest(TeaModel):
    def __init__(
        self,
        picture_url: List[str] = None,
    ):
        # ["xxx1.jpg", "xxx2.jpg"]
        self.picture_url = picture_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.picture_url is not None:
            result['pictureUrl'] = self.picture_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pictureUrl') is not None:
            self.picture_url = m.get('pictureUrl')
        return self


class AttrFaceResponseBodyAttributes(TeaModel):
    def __init__(
        self,
        age: float = None,
        age_score: float = None,
        gender: str = None,
        gender_score: float = None,
        mask: str = None,
        angle: List[float] = None,
        score: float = None,
    ):
        self.age = age
        self.age_score = age_score
        self.gender = gender
        self.gender_score = gender_score
        self.mask = mask
        self.angle = angle
        self.score = score

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.age is not None:
            result['age'] = self.age
        if self.age_score is not None:
            result['ageScore'] = self.age_score
        if self.gender is not None:
            result['gender'] = self.gender
        if self.gender_score is not None:
            result['genderScore'] = self.gender_score
        if self.mask is not None:
            result['mask'] = self.mask
        if self.angle is not None:
            result['angle'] = self.angle
        if self.score is not None:
            result['score'] = self.score
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('age') is not None:
            self.age = m.get('age')
        if m.get('ageScore') is not None:
            self.age_score = m.get('ageScore')
        if m.get('gender') is not None:
            self.gender = m.get('gender')
        if m.get('genderScore') is not None:
            self.gender_score = m.get('genderScore')
        if m.get('mask') is not None:
            self.mask = m.get('mask')
        if m.get('angle') is not None:
            self.angle = m.get('angle')
        if m.get('score') is not None:
            self.score = m.get('score')
        return self


class AttrFaceResponseBody(TeaModel):
    def __init__(
        self,
        success: int = None,
        errmsg: str = None,
        attributes: List[AttrFaceResponseBodyAttributes] = None,
        valid: List[int] = None,
    ):
        self.success = success
        self.errmsg = errmsg
        self.attributes = attributes
        self.valid = valid

    def validate(self):
        if self.attributes:
            for k in self.attributes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.success is not None:
            result['success'] = self.success
        if self.errmsg is not None:
            result['errmsg'] = self.errmsg
        result['attributes'] = []
        if self.attributes is not None:
            for k in self.attributes:
                result['attributes'].append(k.to_map() if k else None)
        if self.valid is not None:
            result['valid'] = self.valid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('errmsg') is not None:
            self.errmsg = m.get('errmsg')
        self.attributes = []
        if m.get('attributes') is not None:
            for k in m.get('attributes'):
                temp_model = AttrFaceResponseBodyAttributes()
                self.attributes.append(temp_model.from_map(k))
        if m.get('valid') is not None:
            self.valid = m.get('valid')
        return self


class AttrFaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AttrFaceResponseBody = None,
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
            temp_model = AttrFaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MatchRequest(TeaModel):
    def __init__(
        self,
        picture_url: str = None,
        scene_id: str = None,
        floor_id: str = None,
        camera_id: str = None,
        camera_coord: List[float] = None,
    ):
        self.picture_url = picture_url
        self.scene_id = scene_id
        self.floor_id = floor_id
        self.camera_id = camera_id
        self.camera_coord = camera_coord

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.picture_url is not None:
            result['pictureUrl'] = self.picture_url
        if self.scene_id is not None:
            result['sceneId'] = self.scene_id
        if self.floor_id is not None:
            result['floorId'] = self.floor_id
        if self.camera_id is not None:
            result['cameraId'] = self.camera_id
        if self.camera_coord is not None:
            result['cameraCoord'] = self.camera_coord
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pictureUrl') is not None:
            self.picture_url = m.get('pictureUrl')
        if m.get('sceneId') is not None:
            self.scene_id = m.get('sceneId')
        if m.get('floorId') is not None:
            self.floor_id = m.get('floorId')
        if m.get('cameraId') is not None:
            self.camera_id = m.get('cameraId')
        if m.get('cameraCoord') is not None:
            self.camera_coord = m.get('cameraCoord')
        return self


class MatchResponseBody(TeaModel):
    def __init__(
        self,
        success: int = None,
        errmsg: str = None,
        results: str = None,
    ):
        self.success = success
        self.errmsg = errmsg
        self.results = results

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.success is not None:
            result['success'] = self.success
        if self.errmsg is not None:
            result['errmsg'] = self.errmsg
        if self.results is not None:
            result['results'] = self.results
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('errmsg') is not None:
            self.errmsg = m.get('errmsg')
        if m.get('results') is not None:
            self.results = m.get('results')
        return self


class MatchResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: MatchResponseBody = None,
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
            temp_model = MatchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


