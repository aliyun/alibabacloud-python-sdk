# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import BinaryIO, Dict, List


class AddFaceRequest(TeaModel):
    def __init__(
        self,
        db_name: str = None,
        entity_id: str = None,
        extra_data: str = None,
        image_url: str = None,
        quality_score_threshold: float = None,
        similarity_score_threshold_between_entity: float = None,
        similarity_score_threshold_in_entity: float = None,
    ):
        # This parameter is required.
        self.db_name = db_name
        # This parameter is required.
        self.entity_id = entity_id
        self.extra_data = extra_data
        # This parameter is required.
        self.image_url = image_url
        self.quality_score_threshold = quality_score_threshold
        self.similarity_score_threshold_between_entity = similarity_score_threshold_between_entity
        self.similarity_score_threshold_in_entity = similarity_score_threshold_in_entity

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.extra_data is not None:
            result['ExtraData'] = self.extra_data
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.quality_score_threshold is not None:
            result['QualityScoreThreshold'] = self.quality_score_threshold
        if self.similarity_score_threshold_between_entity is not None:
            result['SimilarityScoreThresholdBetweenEntity'] = self.similarity_score_threshold_between_entity
        if self.similarity_score_threshold_in_entity is not None:
            result['SimilarityScoreThresholdInEntity'] = self.similarity_score_threshold_in_entity
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('ExtraData') is not None:
            self.extra_data = m.get('ExtraData')
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('QualityScoreThreshold') is not None:
            self.quality_score_threshold = m.get('QualityScoreThreshold')
        if m.get('SimilarityScoreThresholdBetweenEntity') is not None:
            self.similarity_score_threshold_between_entity = m.get('SimilarityScoreThresholdBetweenEntity')
        if m.get('SimilarityScoreThresholdInEntity') is not None:
            self.similarity_score_threshold_in_entity = m.get('SimilarityScoreThresholdInEntity')
        return self


class AddFaceAdvanceRequest(TeaModel):
    def __init__(
        self,
        db_name: str = None,
        entity_id: str = None,
        extra_data: str = None,
        image_url_object: BinaryIO = None,
        quality_score_threshold: float = None,
        similarity_score_threshold_between_entity: float = None,
        similarity_score_threshold_in_entity: float = None,
    ):
        # This parameter is required.
        self.db_name = db_name
        # This parameter is required.
        self.entity_id = entity_id
        self.extra_data = extra_data
        # This parameter is required.
        self.image_url_object = image_url_object
        self.quality_score_threshold = quality_score_threshold
        self.similarity_score_threshold_between_entity = similarity_score_threshold_between_entity
        self.similarity_score_threshold_in_entity = similarity_score_threshold_in_entity

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.extra_data is not None:
            result['ExtraData'] = self.extra_data
        if self.image_url_object is not None:
            result['ImageUrl'] = self.image_url_object
        if self.quality_score_threshold is not None:
            result['QualityScoreThreshold'] = self.quality_score_threshold
        if self.similarity_score_threshold_between_entity is not None:
            result['SimilarityScoreThresholdBetweenEntity'] = self.similarity_score_threshold_between_entity
        if self.similarity_score_threshold_in_entity is not None:
            result['SimilarityScoreThresholdInEntity'] = self.similarity_score_threshold_in_entity
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('ExtraData') is not None:
            self.extra_data = m.get('ExtraData')
        if m.get('ImageUrl') is not None:
            self.image_url_object = m.get('ImageUrl')
        if m.get('QualityScoreThreshold') is not None:
            self.quality_score_threshold = m.get('QualityScoreThreshold')
        if m.get('SimilarityScoreThresholdBetweenEntity') is not None:
            self.similarity_score_threshold_between_entity = m.get('SimilarityScoreThresholdBetweenEntity')
        if m.get('SimilarityScoreThresholdInEntity') is not None:
            self.similarity_score_threshold_in_entity = m.get('SimilarityScoreThresholdInEntity')
        return self


class AddFaceResponseBodyData(TeaModel):
    def __init__(
        self,
        face_id: str = None,
        qualitie_score: float = None,
    ):
        self.face_id = face_id
        self.qualitie_score = qualitie_score

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.face_id is not None:
            result['FaceId'] = self.face_id
        if self.qualitie_score is not None:
            result['QualitieScore'] = self.qualitie_score
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FaceId') is not None:
            self.face_id = m.get('FaceId')
        if m.get('QualitieScore') is not None:
            self.qualitie_score = m.get('QualitieScore')
        return self


class AddFaceResponseBody(TeaModel):
    def __init__(
        self,
        data: AddFaceResponseBodyData = None,
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
            temp_model = AddFaceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddFaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddFaceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = AddFaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddFaceEntityRequest(TeaModel):
    def __init__(
        self,
        db_name: str = None,
        entity_id: str = None,
        labels: str = None,
    ):
        # This parameter is required.
        self.db_name = db_name
        # This parameter is required.
        self.entity_id = entity_id
        self.labels = labels

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.labels is not None:
            result['Labels'] = self.labels
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        return self


class AddFaceEntityResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddFaceEntityResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddFaceEntityResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = AddFaceEntityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddFaceImageTemplateRequest(TeaModel):
    def __init__(
        self,
        image_url: str = None,
    ):
        # This parameter is required.
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


class AddFaceImageTemplateAdvanceRequest(TeaModel):
    def __init__(
        self,
        image_urlobject: BinaryIO = None,
    ):
        # This parameter is required.
        self.image_urlobject = image_urlobject

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_urlobject is not None:
            result['ImageURL'] = self.image_urlobject
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_urlobject = m.get('ImageURL')
        return self


class AddFaceImageTemplateResponseBodyDataFaceInfosFaceRect(TeaModel):
    def __init__(
        self,
        height: str = None,
        width: str = None,
        x: str = None,
        y: str = None,
    ):
        self.height = height
        self.width = width
        self.x = x
        self.y = y

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.height is not None:
            result['Height'] = self.height
        if self.width is not None:
            result['Width'] = self.width
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        return self


class AddFaceImageTemplateResponseBodyDataFaceInfos(TeaModel):
    def __init__(
        self,
        face_rect: AddFaceImageTemplateResponseBodyDataFaceInfosFaceRect = None,
        template_face_id: str = None,
    ):
        self.face_rect = face_rect
        self.template_face_id = template_face_id

    def validate(self):
        if self.face_rect:
            self.face_rect.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.face_rect is not None:
            result['FaceRect'] = self.face_rect.to_map()
        if self.template_face_id is not None:
            result['TemplateFaceID'] = self.template_face_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FaceRect') is not None:
            temp_model = AddFaceImageTemplateResponseBodyDataFaceInfosFaceRect()
            self.face_rect = temp_model.from_map(m['FaceRect'])
        if m.get('TemplateFaceID') is not None:
            self.template_face_id = m.get('TemplateFaceID')
        return self


class AddFaceImageTemplateResponseBodyData(TeaModel):
    def __init__(
        self,
        face_infos: List[AddFaceImageTemplateResponseBodyDataFaceInfos] = None,
        template_id: str = None,
    ):
        self.face_infos = face_infos
        self.template_id = template_id

    def validate(self):
        if self.face_infos:
            for k in self.face_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FaceInfos'] = []
        if self.face_infos is not None:
            for k in self.face_infos:
                result['FaceInfos'].append(k.to_map() if k else None)
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.face_infos = []
        if m.get('FaceInfos') is not None:
            for k in m.get('FaceInfos'):
                temp_model = AddFaceImageTemplateResponseBodyDataFaceInfos()
                self.face_infos.append(temp_model.from_map(k))
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class AddFaceImageTemplateResponseBody(TeaModel):
    def __init__(
        self,
        data: AddFaceImageTemplateResponseBodyData = None,
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
            temp_model = AddFaceImageTemplateResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddFaceImageTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddFaceImageTemplateResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = AddFaceImageTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchAddFacesRequestFaces(TeaModel):
    def __init__(
        self,
        extra_data: str = None,
        image_url: str = None,
    ):
        self.extra_data = extra_data
        # This parameter is required.
        self.image_url = image_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extra_data is not None:
            result['ExtraData'] = self.extra_data
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExtraData') is not None:
            self.extra_data = m.get('ExtraData')
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        return self


class BatchAddFacesRequest(TeaModel):
    def __init__(
        self,
        db_name: str = None,
        entity_id: str = None,
        faces: List[BatchAddFacesRequestFaces] = None,
        quality_score_threshold: float = None,
        similarity_score_threshold_between_entity: float = None,
        similarity_score_threshold_in_entity: float = None,
    ):
        # This parameter is required.
        self.db_name = db_name
        # This parameter is required.
        self.entity_id = entity_id
        # This parameter is required.
        self.faces = faces
        self.quality_score_threshold = quality_score_threshold
        self.similarity_score_threshold_between_entity = similarity_score_threshold_between_entity
        self.similarity_score_threshold_in_entity = similarity_score_threshold_in_entity

    def validate(self):
        if self.faces:
            for k in self.faces:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        result['Faces'] = []
        if self.faces is not None:
            for k in self.faces:
                result['Faces'].append(k.to_map() if k else None)
        if self.quality_score_threshold is not None:
            result['QualityScoreThreshold'] = self.quality_score_threshold
        if self.similarity_score_threshold_between_entity is not None:
            result['SimilarityScoreThresholdBetweenEntity'] = self.similarity_score_threshold_between_entity
        if self.similarity_score_threshold_in_entity is not None:
            result['SimilarityScoreThresholdInEntity'] = self.similarity_score_threshold_in_entity
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        self.faces = []
        if m.get('Faces') is not None:
            for k in m.get('Faces'):
                temp_model = BatchAddFacesRequestFaces()
                self.faces.append(temp_model.from_map(k))
        if m.get('QualityScoreThreshold') is not None:
            self.quality_score_threshold = m.get('QualityScoreThreshold')
        if m.get('SimilarityScoreThresholdBetweenEntity') is not None:
            self.similarity_score_threshold_between_entity = m.get('SimilarityScoreThresholdBetweenEntity')
        if m.get('SimilarityScoreThresholdInEntity') is not None:
            self.similarity_score_threshold_in_entity = m.get('SimilarityScoreThresholdInEntity')
        return self


class BatchAddFacesAdvanceRequestFaces(TeaModel):
    def __init__(
        self,
        extra_data: str = None,
        image_urlobject: BinaryIO = None,
    ):
        self.extra_data = extra_data
        # This parameter is required.
        self.image_urlobject = image_urlobject

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extra_data is not None:
            result['ExtraData'] = self.extra_data
        if self.image_urlobject is not None:
            result['ImageURL'] = self.image_urlobject
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExtraData') is not None:
            self.extra_data = m.get('ExtraData')
        if m.get('ImageURL') is not None:
            self.image_urlobject = m.get('ImageURL')
        return self


class BatchAddFacesAdvanceRequest(TeaModel):
    def __init__(
        self,
        db_name: str = None,
        entity_id: str = None,
        faces: List[BatchAddFacesAdvanceRequestFaces] = None,
        quality_score_threshold: float = None,
        similarity_score_threshold_between_entity: float = None,
        similarity_score_threshold_in_entity: float = None,
    ):
        # This parameter is required.
        self.db_name = db_name
        # This parameter is required.
        self.entity_id = entity_id
        # This parameter is required.
        self.faces = faces
        self.quality_score_threshold = quality_score_threshold
        self.similarity_score_threshold_between_entity = similarity_score_threshold_between_entity
        self.similarity_score_threshold_in_entity = similarity_score_threshold_in_entity

    def validate(self):
        if self.faces:
            for k in self.faces:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        result['Faces'] = []
        if self.faces is not None:
            for k in self.faces:
                result['Faces'].append(k.to_map() if k else None)
        if self.quality_score_threshold is not None:
            result['QualityScoreThreshold'] = self.quality_score_threshold
        if self.similarity_score_threshold_between_entity is not None:
            result['SimilarityScoreThresholdBetweenEntity'] = self.similarity_score_threshold_between_entity
        if self.similarity_score_threshold_in_entity is not None:
            result['SimilarityScoreThresholdInEntity'] = self.similarity_score_threshold_in_entity
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        self.faces = []
        if m.get('Faces') is not None:
            for k in m.get('Faces'):
                temp_model = BatchAddFacesAdvanceRequestFaces()
                self.faces.append(temp_model.from_map(k))
        if m.get('QualityScoreThreshold') is not None:
            self.quality_score_threshold = m.get('QualityScoreThreshold')
        if m.get('SimilarityScoreThresholdBetweenEntity') is not None:
            self.similarity_score_threshold_between_entity = m.get('SimilarityScoreThresholdBetweenEntity')
        if m.get('SimilarityScoreThresholdInEntity') is not None:
            self.similarity_score_threshold_in_entity = m.get('SimilarityScoreThresholdInEntity')
        return self


class BatchAddFacesShrinkRequest(TeaModel):
    def __init__(
        self,
        db_name: str = None,
        entity_id: str = None,
        faces_shrink: str = None,
        quality_score_threshold: float = None,
        similarity_score_threshold_between_entity: float = None,
        similarity_score_threshold_in_entity: float = None,
    ):
        # This parameter is required.
        self.db_name = db_name
        # This parameter is required.
        self.entity_id = entity_id
        # This parameter is required.
        self.faces_shrink = faces_shrink
        self.quality_score_threshold = quality_score_threshold
        self.similarity_score_threshold_between_entity = similarity_score_threshold_between_entity
        self.similarity_score_threshold_in_entity = similarity_score_threshold_in_entity

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.faces_shrink is not None:
            result['Faces'] = self.faces_shrink
        if self.quality_score_threshold is not None:
            result['QualityScoreThreshold'] = self.quality_score_threshold
        if self.similarity_score_threshold_between_entity is not None:
            result['SimilarityScoreThresholdBetweenEntity'] = self.similarity_score_threshold_between_entity
        if self.similarity_score_threshold_in_entity is not None:
            result['SimilarityScoreThresholdInEntity'] = self.similarity_score_threshold_in_entity
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('Faces') is not None:
            self.faces_shrink = m.get('Faces')
        if m.get('QualityScoreThreshold') is not None:
            self.quality_score_threshold = m.get('QualityScoreThreshold')
        if m.get('SimilarityScoreThresholdBetweenEntity') is not None:
            self.similarity_score_threshold_between_entity = m.get('SimilarityScoreThresholdBetweenEntity')
        if m.get('SimilarityScoreThresholdInEntity') is not None:
            self.similarity_score_threshold_in_entity = m.get('SimilarityScoreThresholdInEntity')
        return self


class BatchAddFacesResponseBodyDataFailedFaces(TeaModel):
    def __init__(
        self,
        code: str = None,
        image_url: str = None,
        message: str = None,
    ):
        self.code = code
        self.image_url = image_url
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class BatchAddFacesResponseBodyDataInsertedFaces(TeaModel):
    def __init__(
        self,
        face_id: str = None,
        image_url: str = None,
        qualitie_score: float = None,
    ):
        self.face_id = face_id
        self.image_url = image_url
        self.qualitie_score = qualitie_score

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.face_id is not None:
            result['FaceId'] = self.face_id
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        if self.qualitie_score is not None:
            result['QualitieScore'] = self.qualitie_score
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FaceId') is not None:
            self.face_id = m.get('FaceId')
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        if m.get('QualitieScore') is not None:
            self.qualitie_score = m.get('QualitieScore')
        return self


class BatchAddFacesResponseBodyData(TeaModel):
    def __init__(
        self,
        failed_faces: List[BatchAddFacesResponseBodyDataFailedFaces] = None,
        inserted_faces: List[BatchAddFacesResponseBodyDataInsertedFaces] = None,
    ):
        self.failed_faces = failed_faces
        self.inserted_faces = inserted_faces

    def validate(self):
        if self.failed_faces:
            for k in self.failed_faces:
                if k:
                    k.validate()
        if self.inserted_faces:
            for k in self.inserted_faces:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FailedFaces'] = []
        if self.failed_faces is not None:
            for k in self.failed_faces:
                result['FailedFaces'].append(k.to_map() if k else None)
        result['InsertedFaces'] = []
        if self.inserted_faces is not None:
            for k in self.inserted_faces:
                result['InsertedFaces'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.failed_faces = []
        if m.get('FailedFaces') is not None:
            for k in m.get('FailedFaces'):
                temp_model = BatchAddFacesResponseBodyDataFailedFaces()
                self.failed_faces.append(temp_model.from_map(k))
        self.inserted_faces = []
        if m.get('InsertedFaces') is not None:
            for k in m.get('InsertedFaces'):
                temp_model = BatchAddFacesResponseBodyDataInsertedFaces()
                self.inserted_faces.append(temp_model.from_map(k))
        return self


class BatchAddFacesResponseBody(TeaModel):
    def __init__(
        self,
        data: BatchAddFacesResponseBodyData = None,
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
            temp_model = BatchAddFacesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class BatchAddFacesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BatchAddFacesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = BatchAddFacesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BlurFaceRequest(TeaModel):
    def __init__(
        self,
        image_url: str = None,
    ):
        # This parameter is required.
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


class BlurFaceAdvanceRequest(TeaModel):
    def __init__(
        self,
        image_urlobject: BinaryIO = None,
    ):
        # This parameter is required.
        self.image_urlobject = image_urlobject

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_urlobject is not None:
            result['ImageURL'] = self.image_urlobject
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_urlobject = m.get('ImageURL')
        return self


class BlurFaceResponseBodyData(TeaModel):
    def __init__(
        self,
        image_url: str = None,
        mask_url: str = None,
    ):
        self.image_url = image_url
        self.mask_url = mask_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        if self.mask_url is not None:
            result['MaskURL'] = self.mask_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        if m.get('MaskURL') is not None:
            self.mask_url = m.get('MaskURL')
        return self


class BlurFaceResponseBody(TeaModel):
    def __init__(
        self,
        data: BlurFaceResponseBodyData = None,
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
            temp_model = BlurFaceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class BlurFaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BlurFaceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = BlurFaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BodyPostureRequest(TeaModel):
    def __init__(
        self,
        image_url: str = None,
    ):
        # This parameter is required.
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


class BodyPostureAdvanceRequest(TeaModel):
    def __init__(
        self,
        image_urlobject: BinaryIO = None,
    ):
        # This parameter is required.
        self.image_urlobject = image_urlobject

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_urlobject is not None:
            result['ImageURL'] = self.image_urlobject
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_urlobject = m.get('ImageURL')
        return self


class BodyPostureResponseBodyDataMetaObject(TeaModel):
    def __init__(
        self,
        height: int = None,
        width: int = None,
    ):
        self.height = height
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.height is not None:
            result['Height'] = self.height
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class BodyPostureResponseBodyDataOutputsResultsBodiesPositions(TeaModel):
    def __init__(
        self,
        points: List[float] = None,
    ):
        self.points = points

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.points is not None:
            result['Points'] = self.points
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Points') is not None:
            self.points = m.get('Points')
        return self


class BodyPostureResponseBodyDataOutputsResultsBodies(TeaModel):
    def __init__(
        self,
        confident: float = None,
        label: str = None,
        positions: List[BodyPostureResponseBodyDataOutputsResultsBodiesPositions] = None,
    ):
        self.confident = confident
        self.label = label
        self.positions = positions

    def validate(self):
        if self.positions:
            for k in self.positions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.confident is not None:
            result['Confident'] = self.confident
        if self.label is not None:
            result['Label'] = self.label
        result['Positions'] = []
        if self.positions is not None:
            for k in self.positions:
                result['Positions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Confident') is not None:
            self.confident = m.get('Confident')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        self.positions = []
        if m.get('Positions') is not None:
            for k in m.get('Positions'):
                temp_model = BodyPostureResponseBodyDataOutputsResultsBodiesPositions()
                self.positions.append(temp_model.from_map(k))
        return self


class BodyPostureResponseBodyDataOutputsResults(TeaModel):
    def __init__(
        self,
        bodies: List[BodyPostureResponseBodyDataOutputsResultsBodies] = None,
    ):
        self.bodies = bodies

    def validate(self):
        if self.bodies:
            for k in self.bodies:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Bodies'] = []
        if self.bodies is not None:
            for k in self.bodies:
                result['Bodies'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.bodies = []
        if m.get('Bodies') is not None:
            for k in m.get('Bodies'):
                temp_model = BodyPostureResponseBodyDataOutputsResultsBodies()
                self.bodies.append(temp_model.from_map(k))
        return self


class BodyPostureResponseBodyDataOutputs(TeaModel):
    def __init__(
        self,
        human_count: int = None,
        results: List[BodyPostureResponseBodyDataOutputsResults] = None,
    ):
        self.human_count = human_count
        self.results = results

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
        if self.human_count is not None:
            result['HumanCount'] = self.human_count
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HumanCount') is not None:
            self.human_count = m.get('HumanCount')
        self.results = []
        if m.get('Results') is not None:
            for k in m.get('Results'):
                temp_model = BodyPostureResponseBodyDataOutputsResults()
                self.results.append(temp_model.from_map(k))
        return self


class BodyPostureResponseBodyData(TeaModel):
    def __init__(
        self,
        meta_object: BodyPostureResponseBodyDataMetaObject = None,
        outputs: List[BodyPostureResponseBodyDataOutputs] = None,
    ):
        self.meta_object = meta_object
        self.outputs = outputs

    def validate(self):
        if self.meta_object:
            self.meta_object.validate()
        if self.outputs:
            for k in self.outputs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.meta_object is not None:
            result['MetaObject'] = self.meta_object.to_map()
        result['Outputs'] = []
        if self.outputs is not None:
            for k in self.outputs:
                result['Outputs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MetaObject') is not None:
            temp_model = BodyPostureResponseBodyDataMetaObject()
            self.meta_object = temp_model.from_map(m['MetaObject'])
        self.outputs = []
        if m.get('Outputs') is not None:
            for k in m.get('Outputs'):
                temp_model = BodyPostureResponseBodyDataOutputs()
                self.outputs.append(temp_model.from_map(k))
        return self


class BodyPostureResponseBody(TeaModel):
    def __init__(
        self,
        data: BodyPostureResponseBodyData = None,
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
            temp_model = BodyPostureResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class BodyPostureResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BodyPostureResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = BodyPostureResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CompareFaceRequest(TeaModel):
    def __init__(
        self,
        image_data_a: str = None,
        image_data_b: str = None,
        image_urla: str = None,
        image_urlb: str = None,
        quality_score_threshold: float = None,
    ):
        self.image_data_a = image_data_a
        self.image_data_b = image_data_b
        self.image_urla = image_urla
        self.image_urlb = image_urlb
        self.quality_score_threshold = quality_score_threshold

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_data_a is not None:
            result['ImageDataA'] = self.image_data_a
        if self.image_data_b is not None:
            result['ImageDataB'] = self.image_data_b
        if self.image_urla is not None:
            result['ImageURLA'] = self.image_urla
        if self.image_urlb is not None:
            result['ImageURLB'] = self.image_urlb
        if self.quality_score_threshold is not None:
            result['QualityScoreThreshold'] = self.quality_score_threshold
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageDataA') is not None:
            self.image_data_a = m.get('ImageDataA')
        if m.get('ImageDataB') is not None:
            self.image_data_b = m.get('ImageDataB')
        if m.get('ImageURLA') is not None:
            self.image_urla = m.get('ImageURLA')
        if m.get('ImageURLB') is not None:
            self.image_urlb = m.get('ImageURLB')
        if m.get('QualityScoreThreshold') is not None:
            self.quality_score_threshold = m.get('QualityScoreThreshold')
        return self


class CompareFaceAdvanceRequest(TeaModel):
    def __init__(
        self,
        image_data_a: str = None,
        image_data_b: str = None,
        image_urlaobject: BinaryIO = None,
        image_urlbobject: BinaryIO = None,
        quality_score_threshold: float = None,
    ):
        self.image_data_a = image_data_a
        self.image_data_b = image_data_b
        self.image_urlaobject = image_urlaobject
        self.image_urlbobject = image_urlbobject
        self.quality_score_threshold = quality_score_threshold

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_data_a is not None:
            result['ImageDataA'] = self.image_data_a
        if self.image_data_b is not None:
            result['ImageDataB'] = self.image_data_b
        if self.image_urlaobject is not None:
            result['ImageURLA'] = self.image_urlaobject
        if self.image_urlbobject is not None:
            result['ImageURLB'] = self.image_urlbobject
        if self.quality_score_threshold is not None:
            result['QualityScoreThreshold'] = self.quality_score_threshold
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageDataA') is not None:
            self.image_data_a = m.get('ImageDataA')
        if m.get('ImageDataB') is not None:
            self.image_data_b = m.get('ImageDataB')
        if m.get('ImageURLA') is not None:
            self.image_urlaobject = m.get('ImageURLA')
        if m.get('ImageURLB') is not None:
            self.image_urlbobject = m.get('ImageURLB')
        if m.get('QualityScoreThreshold') is not None:
            self.quality_score_threshold = m.get('QualityScoreThreshold')
        return self


class CompareFaceResponseBodyData(TeaModel):
    def __init__(
        self,
        confidence: float = None,
        is_mask_a: int = None,
        is_mask_b: int = None,
        landmarks_alist: List[int] = None,
        landmarks_blist: List[int] = None,
        message_tips: str = None,
        quality_score_a: float = None,
        quality_score_b: float = None,
        rect_alist: List[int] = None,
        rect_blist: List[int] = None,
        thresholds: List[float] = None,
    ):
        self.confidence = confidence
        self.is_mask_a = is_mask_a
        self.is_mask_b = is_mask_b
        self.landmarks_alist = landmarks_alist
        self.landmarks_blist = landmarks_blist
        self.message_tips = message_tips
        self.quality_score_a = quality_score_a
        self.quality_score_b = quality_score_b
        # 1
        self.rect_alist = rect_alist
        # 1
        self.rect_blist = rect_blist
        # 1
        self.thresholds = thresholds

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.confidence is not None:
            result['Confidence'] = self.confidence
        if self.is_mask_a is not None:
            result['IsMaskA'] = self.is_mask_a
        if self.is_mask_b is not None:
            result['IsMaskB'] = self.is_mask_b
        if self.landmarks_alist is not None:
            result['LandmarksAList'] = self.landmarks_alist
        if self.landmarks_blist is not None:
            result['LandmarksBList'] = self.landmarks_blist
        if self.message_tips is not None:
            result['MessageTips'] = self.message_tips
        if self.quality_score_a is not None:
            result['QualityScoreA'] = self.quality_score_a
        if self.quality_score_b is not None:
            result['QualityScoreB'] = self.quality_score_b
        if self.rect_alist is not None:
            result['RectAList'] = self.rect_alist
        if self.rect_blist is not None:
            result['RectBList'] = self.rect_blist
        if self.thresholds is not None:
            result['Thresholds'] = self.thresholds
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')
        if m.get('IsMaskA') is not None:
            self.is_mask_a = m.get('IsMaskA')
        if m.get('IsMaskB') is not None:
            self.is_mask_b = m.get('IsMaskB')
        if m.get('LandmarksAList') is not None:
            self.landmarks_alist = m.get('LandmarksAList')
        if m.get('LandmarksBList') is not None:
            self.landmarks_blist = m.get('LandmarksBList')
        if m.get('MessageTips') is not None:
            self.message_tips = m.get('MessageTips')
        if m.get('QualityScoreA') is not None:
            self.quality_score_a = m.get('QualityScoreA')
        if m.get('QualityScoreB') is not None:
            self.quality_score_b = m.get('QualityScoreB')
        if m.get('RectAList') is not None:
            self.rect_alist = m.get('RectAList')
        if m.get('RectBList') is not None:
            self.rect_blist = m.get('RectBList')
        if m.get('Thresholds') is not None:
            self.thresholds = m.get('Thresholds')
        return self


class CompareFaceResponseBody(TeaModel):
    def __init__(
        self,
        data: CompareFaceResponseBodyData = None,
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
            temp_model = CompareFaceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CompareFaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CompareFaceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = CompareFaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CompareFaceWithMaskRequest(TeaModel):
    def __init__(
        self,
        image_urla: str = None,
        image_urlb: str = None,
        quality_score_threshold: float = None,
    ):
        # This parameter is required.
        self.image_urla = image_urla
        # This parameter is required.
        self.image_urlb = image_urlb
        self.quality_score_threshold = quality_score_threshold

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_urla is not None:
            result['ImageURLA'] = self.image_urla
        if self.image_urlb is not None:
            result['ImageURLB'] = self.image_urlb
        if self.quality_score_threshold is not None:
            result['QualityScoreThreshold'] = self.quality_score_threshold
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURLA') is not None:
            self.image_urla = m.get('ImageURLA')
        if m.get('ImageURLB') is not None:
            self.image_urlb = m.get('ImageURLB')
        if m.get('QualityScoreThreshold') is not None:
            self.quality_score_threshold = m.get('QualityScoreThreshold')
        return self


class CompareFaceWithMaskAdvanceRequest(TeaModel):
    def __init__(
        self,
        image_urlaobject: BinaryIO = None,
        image_urlbobject: BinaryIO = None,
        quality_score_threshold: float = None,
    ):
        # This parameter is required.
        self.image_urlaobject = image_urlaobject
        # This parameter is required.
        self.image_urlbobject = image_urlbobject
        self.quality_score_threshold = quality_score_threshold

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_urlaobject is not None:
            result['ImageURLA'] = self.image_urlaobject
        if self.image_urlbobject is not None:
            result['ImageURLB'] = self.image_urlbobject
        if self.quality_score_threshold is not None:
            result['QualityScoreThreshold'] = self.quality_score_threshold
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURLA') is not None:
            self.image_urlaobject = m.get('ImageURLA')
        if m.get('ImageURLB') is not None:
            self.image_urlbobject = m.get('ImageURLB')
        if m.get('QualityScoreThreshold') is not None:
            self.quality_score_threshold = m.get('QualityScoreThreshold')
        return self


class CompareFaceWithMaskResponseBodyData(TeaModel):
    def __init__(
        self,
        confidence: float = None,
        is_mask_a: int = None,
        is_mask_b: int = None,
        landmarks_alist: List[int] = None,
        landmarks_blist: List[int] = None,
        message_tips: str = None,
        quality_score_a: float = None,
        quality_score_b: float = None,
        rect_alist: List[int] = None,
        rect_blist: List[int] = None,
        thresholds: List[int] = None,
    ):
        self.confidence = confidence
        self.is_mask_a = is_mask_a
        self.is_mask_b = is_mask_b
        self.landmarks_alist = landmarks_alist
        self.landmarks_blist = landmarks_blist
        self.message_tips = message_tips
        self.quality_score_a = quality_score_a
        self.quality_score_b = quality_score_b
        self.rect_alist = rect_alist
        self.rect_blist = rect_blist
        self.thresholds = thresholds

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.confidence is not None:
            result['Confidence'] = self.confidence
        if self.is_mask_a is not None:
            result['IsMaskA'] = self.is_mask_a
        if self.is_mask_b is not None:
            result['IsMaskB'] = self.is_mask_b
        if self.landmarks_alist is not None:
            result['LandmarksAList'] = self.landmarks_alist
        if self.landmarks_blist is not None:
            result['LandmarksBList'] = self.landmarks_blist
        if self.message_tips is not None:
            result['MessageTips'] = self.message_tips
        if self.quality_score_a is not None:
            result['QualityScoreA'] = self.quality_score_a
        if self.quality_score_b is not None:
            result['QualityScoreB'] = self.quality_score_b
        if self.rect_alist is not None:
            result['RectAList'] = self.rect_alist
        if self.rect_blist is not None:
            result['RectBList'] = self.rect_blist
        if self.thresholds is not None:
            result['Thresholds'] = self.thresholds
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')
        if m.get('IsMaskA') is not None:
            self.is_mask_a = m.get('IsMaskA')
        if m.get('IsMaskB') is not None:
            self.is_mask_b = m.get('IsMaskB')
        if m.get('LandmarksAList') is not None:
            self.landmarks_alist = m.get('LandmarksAList')
        if m.get('LandmarksBList') is not None:
            self.landmarks_blist = m.get('LandmarksBList')
        if m.get('MessageTips') is not None:
            self.message_tips = m.get('MessageTips')
        if m.get('QualityScoreA') is not None:
            self.quality_score_a = m.get('QualityScoreA')
        if m.get('QualityScoreB') is not None:
            self.quality_score_b = m.get('QualityScoreB')
        if m.get('RectAList') is not None:
            self.rect_alist = m.get('RectAList')
        if m.get('RectBList') is not None:
            self.rect_blist = m.get('RectBList')
        if m.get('Thresholds') is not None:
            self.thresholds = m.get('Thresholds')
        return self


class CompareFaceWithMaskResponseBody(TeaModel):
    def __init__(
        self,
        data: CompareFaceWithMaskResponseBodyData = None,
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
            temp_model = CompareFaceWithMaskResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CompareFaceWithMaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CompareFaceWithMaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = CompareFaceWithMaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFaceDbRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
    ):
        # This parameter is required.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class CreateFaceDbResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateFaceDbResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateFaceDbResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = CreateFaceDbResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeepfakeFaceRequestTasks(TeaModel):
    def __init__(
        self,
        image_data: str = None,
        image_url: str = None,
    ):
        self.image_data = image_data
        self.image_url = image_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_data is not None:
            result['ImageData'] = self.image_data
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageData') is not None:
            self.image_data = m.get('ImageData')
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        return self


class DeepfakeFaceRequest(TeaModel):
    def __init__(
        self,
        tasks: List[DeepfakeFaceRequestTasks] = None,
    ):
        # This parameter is required.
        self.tasks = tasks

    def validate(self):
        if self.tasks:
            for k in self.tasks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Tasks'] = []
        if self.tasks is not None:
            for k in self.tasks:
                result['Tasks'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tasks = []
        if m.get('Tasks') is not None:
            for k in m.get('Tasks'):
                temp_model = DeepfakeFaceRequestTasks()
                self.tasks.append(temp_model.from_map(k))
        return self


class DeepfakeFaceAdvanceRequestTasks(TeaModel):
    def __init__(
        self,
        image_data: str = None,
        image_urlobject: BinaryIO = None,
    ):
        self.image_data = image_data
        self.image_urlobject = image_urlobject

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_data is not None:
            result['ImageData'] = self.image_data
        if self.image_urlobject is not None:
            result['ImageURL'] = self.image_urlobject
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageData') is not None:
            self.image_data = m.get('ImageData')
        if m.get('ImageURL') is not None:
            self.image_urlobject = m.get('ImageURL')
        return self


class DeepfakeFaceAdvanceRequest(TeaModel):
    def __init__(
        self,
        tasks: List[DeepfakeFaceAdvanceRequestTasks] = None,
    ):
        # This parameter is required.
        self.tasks = tasks

    def validate(self):
        if self.tasks:
            for k in self.tasks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Tasks'] = []
        if self.tasks is not None:
            for k in self.tasks:
                result['Tasks'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tasks = []
        if m.get('Tasks') is not None:
            for k in m.get('Tasks'):
                temp_model = DeepfakeFaceAdvanceRequestTasks()
                self.tasks.append(temp_model.from_map(k))
        return self


class DeepfakeFaceResponseBodyDataElementsResultsRect(TeaModel):
    def __init__(
        self,
        height: int = None,
        left: int = None,
        top: int = None,
        width: int = None,
    ):
        self.height = height
        self.left = left
        self.top = top
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.height is not None:
            result['Height'] = self.height
        if self.left is not None:
            result['Left'] = self.left
        if self.top is not None:
            result['Top'] = self.top
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Left') is not None:
            self.left = m.get('Left')
        if m.get('Top') is not None:
            self.top = m.get('Top')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class DeepfakeFaceResponseBodyDataElementsResults(TeaModel):
    def __init__(
        self,
        confidence: float = None,
        label: str = None,
        message_tips: str = None,
        rect: DeepfakeFaceResponseBodyDataElementsResultsRect = None,
    ):
        self.confidence = confidence
        self.label = label
        self.message_tips = message_tips
        self.rect = rect

    def validate(self):
        if self.rect:
            self.rect.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.confidence is not None:
            result['Confidence'] = self.confidence
        if self.label is not None:
            result['Label'] = self.label
        if self.message_tips is not None:
            result['MessageTips'] = self.message_tips
        if self.rect is not None:
            result['Rect'] = self.rect.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('MessageTips') is not None:
            self.message_tips = m.get('MessageTips')
        if m.get('Rect') is not None:
            temp_model = DeepfakeFaceResponseBodyDataElementsResultsRect()
            self.rect = temp_model.from_map(m['Rect'])
        return self


class DeepfakeFaceResponseBodyDataElements(TeaModel):
    def __init__(
        self,
        face_number: int = None,
        image_url: str = None,
        results: List[DeepfakeFaceResponseBodyDataElementsResults] = None,
        task_id: str = None,
    ):
        self.face_number = face_number
        self.image_url = image_url
        self.results = results
        self.task_id = task_id

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
        if self.face_number is not None:
            result['FaceNumber'] = self.face_number
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FaceNumber') is not None:
            self.face_number = m.get('FaceNumber')
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        self.results = []
        if m.get('Results') is not None:
            for k in m.get('Results'):
                temp_model = DeepfakeFaceResponseBodyDataElementsResults()
                self.results.append(temp_model.from_map(k))
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DeepfakeFaceResponseBodyData(TeaModel):
    def __init__(
        self,
        elements: List[DeepfakeFaceResponseBodyDataElements] = None,
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
                temp_model = DeepfakeFaceResponseBodyDataElements()
                self.elements.append(temp_model.from_map(k))
        return self


class DeepfakeFaceResponseBody(TeaModel):
    def __init__(
        self,
        data: DeepfakeFaceResponseBodyData = None,
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
            temp_model = DeepfakeFaceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeepfakeFaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeepfakeFaceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DeepfakeFaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteFaceRequest(TeaModel):
    def __init__(
        self,
        db_name: str = None,
        face_id: str = None,
    ):
        # This parameter is required.
        self.db_name = db_name
        # This parameter is required.
        self.face_id = face_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.face_id is not None:
            result['FaceId'] = self.face_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('FaceId') is not None:
            self.face_id = m.get('FaceId')
        return self


class DeleteFaceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteFaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteFaceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DeleteFaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteFaceDbRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
    ):
        # This parameter is required.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DeleteFaceDbResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteFaceDbResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteFaceDbResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DeleteFaceDbResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteFaceEntityRequest(TeaModel):
    def __init__(
        self,
        db_name: str = None,
        entity_id: str = None,
    ):
        # This parameter is required.
        self.db_name = db_name
        # This parameter is required.
        self.entity_id = entity_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        return self


class DeleteFaceEntityResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteFaceEntityResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteFaceEntityResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DeleteFaceEntityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteFaceImageTemplateRequest(TeaModel):
    def __init__(
        self,
        template_id: str = None,
    ):
        # This parameter is required.
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class DeleteFaceImageTemplateResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteFaceImageTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteFaceImageTemplateResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DeleteFaceImageTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetectBodyCountRequest(TeaModel):
    def __init__(
        self,
        image_url: str = None,
    ):
        # This parameter is required.
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


class DetectBodyCountAdvanceRequest(TeaModel):
    def __init__(
        self,
        image_urlobject: BinaryIO = None,
    ):
        # This parameter is required.
        self.image_urlobject = image_urlobject

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_urlobject is not None:
            result['ImageURL'] = self.image_urlobject
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_urlobject = m.get('ImageURL')
        return self


class DetectBodyCountResponseBodyData(TeaModel):
    def __init__(
        self,
        person_number: int = None,
    ):
        self.person_number = person_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.person_number is not None:
            result['PersonNumber'] = self.person_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PersonNumber') is not None:
            self.person_number = m.get('PersonNumber')
        return self


class DetectBodyCountResponseBody(TeaModel):
    def __init__(
        self,
        data: DetectBodyCountResponseBodyData = None,
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
            temp_model = DetectBodyCountResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DetectBodyCountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DetectBodyCountResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DetectBodyCountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetectCelebrityRequest(TeaModel):
    def __init__(
        self,
        image_url: str = None,
    ):
        # This parameter is required.
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


class DetectCelebrityAdvanceRequest(TeaModel):
    def __init__(
        self,
        image_urlobject: BinaryIO = None,
    ):
        # This parameter is required.
        self.image_urlobject = image_urlobject

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_urlobject is not None:
            result['ImageURL'] = self.image_urlobject
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_urlobject = m.get('ImageURL')
        return self


class DetectCelebrityResponseBodyDataFaceRecognizeResults(TeaModel):
    def __init__(
        self,
        face_boxes: List[float] = None,
        name: str = None,
    ):
        # 1
        self.face_boxes = face_boxes
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.face_boxes is not None:
            result['FaceBoxes'] = self.face_boxes
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FaceBoxes') is not None:
            self.face_boxes = m.get('FaceBoxes')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DetectCelebrityResponseBodyData(TeaModel):
    def __init__(
        self,
        face_recognize_results: List[DetectCelebrityResponseBodyDataFaceRecognizeResults] = None,
        height: int = None,
        width: int = None,
    ):
        self.face_recognize_results = face_recognize_results
        self.height = height
        self.width = width

    def validate(self):
        if self.face_recognize_results:
            for k in self.face_recognize_results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FaceRecognizeResults'] = []
        if self.face_recognize_results is not None:
            for k in self.face_recognize_results:
                result['FaceRecognizeResults'].append(k.to_map() if k else None)
        if self.height is not None:
            result['Height'] = self.height
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.face_recognize_results = []
        if m.get('FaceRecognizeResults') is not None:
            for k in m.get('FaceRecognizeResults'):
                temp_model = DetectCelebrityResponseBodyDataFaceRecognizeResults()
                self.face_recognize_results.append(temp_model.from_map(k))
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class DetectCelebrityResponseBody(TeaModel):
    def __init__(
        self,
        data: DetectCelebrityResponseBodyData = None,
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
            temp_model = DetectCelebrityResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DetectCelebrityResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DetectCelebrityResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DetectCelebrityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetectFaceRequest(TeaModel):
    def __init__(
        self,
        image_url: str = None,
        landmark: bool = None,
        max_face_number: int = None,
        pose: bool = None,
        quality: bool = None,
    ):
        # This parameter is required.
        self.image_url = image_url
        self.landmark = landmark
        self.max_face_number = max_face_number
        self.pose = pose
        self.quality = quality

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        if self.landmark is not None:
            result['Landmark'] = self.landmark
        if self.max_face_number is not None:
            result['MaxFaceNumber'] = self.max_face_number
        if self.pose is not None:
            result['Pose'] = self.pose
        if self.quality is not None:
            result['Quality'] = self.quality
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        if m.get('Landmark') is not None:
            self.landmark = m.get('Landmark')
        if m.get('MaxFaceNumber') is not None:
            self.max_face_number = m.get('MaxFaceNumber')
        if m.get('Pose') is not None:
            self.pose = m.get('Pose')
        if m.get('Quality') is not None:
            self.quality = m.get('Quality')
        return self


class DetectFaceAdvanceRequest(TeaModel):
    def __init__(
        self,
        image_urlobject: BinaryIO = None,
        landmark: bool = None,
        max_face_number: int = None,
        pose: bool = None,
        quality: bool = None,
    ):
        # This parameter is required.
        self.image_urlobject = image_urlobject
        self.landmark = landmark
        self.max_face_number = max_face_number
        self.pose = pose
        self.quality = quality

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_urlobject is not None:
            result['ImageURL'] = self.image_urlobject
        if self.landmark is not None:
            result['Landmark'] = self.landmark
        if self.max_face_number is not None:
            result['MaxFaceNumber'] = self.max_face_number
        if self.pose is not None:
            result['Pose'] = self.pose
        if self.quality is not None:
            result['Quality'] = self.quality
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_urlobject = m.get('ImageURL')
        if m.get('Landmark') is not None:
            self.landmark = m.get('Landmark')
        if m.get('MaxFaceNumber') is not None:
            self.max_face_number = m.get('MaxFaceNumber')
        if m.get('Pose') is not None:
            self.pose = m.get('Pose')
        if m.get('Quality') is not None:
            self.quality = m.get('Quality')
        return self


class DetectFaceResponseBodyDataQualities(TeaModel):
    def __init__(
        self,
        blur_list: List[float] = None,
        fnf_list: List[float] = None,
        glass_list: List[float] = None,
        illu_list: List[float] = None,
        mask_list: List[float] = None,
        noise_list: List[float] = None,
        pose_list: List[float] = None,
        score_list: List[float] = None,
    ):
        # 1
        self.blur_list = blur_list
        # 1
        self.fnf_list = fnf_list
        # 1
        self.glass_list = glass_list
        # 1
        self.illu_list = illu_list
        # 1
        self.mask_list = mask_list
        # 1
        self.noise_list = noise_list
        # 1
        self.pose_list = pose_list
        # 1
        self.score_list = score_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.blur_list is not None:
            result['BlurList'] = self.blur_list
        if self.fnf_list is not None:
            result['FnfList'] = self.fnf_list
        if self.glass_list is not None:
            result['GlassList'] = self.glass_list
        if self.illu_list is not None:
            result['IlluList'] = self.illu_list
        if self.mask_list is not None:
            result['MaskList'] = self.mask_list
        if self.noise_list is not None:
            result['NoiseList'] = self.noise_list
        if self.pose_list is not None:
            result['PoseList'] = self.pose_list
        if self.score_list is not None:
            result['ScoreList'] = self.score_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BlurList') is not None:
            self.blur_list = m.get('BlurList')
        if m.get('FnfList') is not None:
            self.fnf_list = m.get('FnfList')
        if m.get('GlassList') is not None:
            self.glass_list = m.get('GlassList')
        if m.get('IlluList') is not None:
            self.illu_list = m.get('IlluList')
        if m.get('MaskList') is not None:
            self.mask_list = m.get('MaskList')
        if m.get('NoiseList') is not None:
            self.noise_list = m.get('NoiseList')
        if m.get('PoseList') is not None:
            self.pose_list = m.get('PoseList')
        if m.get('ScoreList') is not None:
            self.score_list = m.get('ScoreList')
        return self


class DetectFaceResponseBodyData(TeaModel):
    def __init__(
        self,
        face_count: int = None,
        face_probability_list: List[float] = None,
        face_rectangles: List[int] = None,
        landmark_count: int = None,
        landmark_score: List[float] = None,
        landmarks: List[float] = None,
        pose_list: List[float] = None,
        pupils: List[float] = None,
        qualities: DetectFaceResponseBodyDataQualities = None,
    ):
        self.face_count = face_count
        # 1
        self.face_probability_list = face_probability_list
        # 1
        self.face_rectangles = face_rectangles
        self.landmark_count = landmark_count
        self.landmark_score = landmark_score
        # 1
        self.landmarks = landmarks
        # 1
        self.pose_list = pose_list
        # 1
        self.pupils = pupils
        self.qualities = qualities

    def validate(self):
        if self.qualities:
            self.qualities.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.face_count is not None:
            result['FaceCount'] = self.face_count
        if self.face_probability_list is not None:
            result['FaceProbabilityList'] = self.face_probability_list
        if self.face_rectangles is not None:
            result['FaceRectangles'] = self.face_rectangles
        if self.landmark_count is not None:
            result['LandmarkCount'] = self.landmark_count
        if self.landmark_score is not None:
            result['LandmarkScore'] = self.landmark_score
        if self.landmarks is not None:
            result['Landmarks'] = self.landmarks
        if self.pose_list is not None:
            result['PoseList'] = self.pose_list
        if self.pupils is not None:
            result['Pupils'] = self.pupils
        if self.qualities is not None:
            result['Qualities'] = self.qualities.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FaceCount') is not None:
            self.face_count = m.get('FaceCount')
        if m.get('FaceProbabilityList') is not None:
            self.face_probability_list = m.get('FaceProbabilityList')
        if m.get('FaceRectangles') is not None:
            self.face_rectangles = m.get('FaceRectangles')
        if m.get('LandmarkCount') is not None:
            self.landmark_count = m.get('LandmarkCount')
        if m.get('LandmarkScore') is not None:
            self.landmark_score = m.get('LandmarkScore')
        if m.get('Landmarks') is not None:
            self.landmarks = m.get('Landmarks')
        if m.get('PoseList') is not None:
            self.pose_list = m.get('PoseList')
        if m.get('Pupils') is not None:
            self.pupils = m.get('Pupils')
        if m.get('Qualities') is not None:
            temp_model = DetectFaceResponseBodyDataQualities()
            self.qualities = temp_model.from_map(m['Qualities'])
        return self


class DetectFaceResponseBody(TeaModel):
    def __init__(
        self,
        data: DetectFaceResponseBodyData = None,
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
            temp_model = DetectFaceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DetectFaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DetectFaceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DetectFaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetectInfraredLivingFaceRequestTasks(TeaModel):
    def __init__(
        self,
        image_url: str = None,
    ):
        # This parameter is required.
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


class DetectInfraredLivingFaceRequest(TeaModel):
    def __init__(
        self,
        tasks: List[DetectInfraredLivingFaceRequestTasks] = None,
    ):
        # This parameter is required.
        self.tasks = tasks

    def validate(self):
        if self.tasks:
            for k in self.tasks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Tasks'] = []
        if self.tasks is not None:
            for k in self.tasks:
                result['Tasks'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tasks = []
        if m.get('Tasks') is not None:
            for k in m.get('Tasks'):
                temp_model = DetectInfraredLivingFaceRequestTasks()
                self.tasks.append(temp_model.from_map(k))
        return self


class DetectInfraredLivingFaceAdvanceRequestTasks(TeaModel):
    def __init__(
        self,
        image_urlobject: BinaryIO = None,
    ):
        # This parameter is required.
        self.image_urlobject = image_urlobject

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_urlobject is not None:
            result['ImageURL'] = self.image_urlobject
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_urlobject = m.get('ImageURL')
        return self


class DetectInfraredLivingFaceAdvanceRequest(TeaModel):
    def __init__(
        self,
        tasks: List[DetectInfraredLivingFaceAdvanceRequestTasks] = None,
    ):
        # This parameter is required.
        self.tasks = tasks

    def validate(self):
        if self.tasks:
            for k in self.tasks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Tasks'] = []
        if self.tasks is not None:
            for k in self.tasks:
                result['Tasks'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tasks = []
        if m.get('Tasks') is not None:
            for k in m.get('Tasks'):
                temp_model = DetectInfraredLivingFaceAdvanceRequestTasks()
                self.tasks.append(temp_model.from_map(k))
        return self


class DetectInfraredLivingFaceResponseBodyDataElementsResultsRect(TeaModel):
    def __init__(
        self,
        height: int = None,
        left: int = None,
        top: int = None,
        width: int = None,
    ):
        self.height = height
        self.left = left
        self.top = top
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.height is not None:
            result['Height'] = self.height
        if self.left is not None:
            result['Left'] = self.left
        if self.top is not None:
            result['Top'] = self.top
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Left') is not None:
            self.left = m.get('Left')
        if m.get('Top') is not None:
            self.top = m.get('Top')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class DetectInfraredLivingFaceResponseBodyDataElementsResults(TeaModel):
    def __init__(
        self,
        label: str = None,
        message_tips: str = None,
        rate: float = None,
        rect: DetectInfraredLivingFaceResponseBodyDataElementsResultsRect = None,
        suggestion: str = None,
    ):
        self.label = label
        self.message_tips = message_tips
        self.rate = rate
        self.rect = rect
        self.suggestion = suggestion

    def validate(self):
        if self.rect:
            self.rect.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label is not None:
            result['Label'] = self.label
        if self.message_tips is not None:
            result['MessageTips'] = self.message_tips
        if self.rate is not None:
            result['Rate'] = self.rate
        if self.rect is not None:
            result['Rect'] = self.rect.to_map()
        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('MessageTips') is not None:
            self.message_tips = m.get('MessageTips')
        if m.get('Rate') is not None:
            self.rate = m.get('Rate')
        if m.get('Rect') is not None:
            temp_model = DetectInfraredLivingFaceResponseBodyDataElementsResultsRect()
            self.rect = temp_model.from_map(m['Rect'])
        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')
        return self


class DetectInfraredLivingFaceResponseBodyDataElements(TeaModel):
    def __init__(
        self,
        face_number: int = None,
        image_url: str = None,
        results: List[DetectInfraredLivingFaceResponseBodyDataElementsResults] = None,
    ):
        self.face_number = face_number
        self.image_url = image_url
        self.results = results

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
        if self.face_number is not None:
            result['FaceNumber'] = self.face_number
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FaceNumber') is not None:
            self.face_number = m.get('FaceNumber')
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        self.results = []
        if m.get('Results') is not None:
            for k in m.get('Results'):
                temp_model = DetectInfraredLivingFaceResponseBodyDataElementsResults()
                self.results.append(temp_model.from_map(k))
        return self


class DetectInfraredLivingFaceResponseBodyData(TeaModel):
    def __init__(
        self,
        elements: List[DetectInfraredLivingFaceResponseBodyDataElements] = None,
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
                temp_model = DetectInfraredLivingFaceResponseBodyDataElements()
                self.elements.append(temp_model.from_map(k))
        return self


class DetectInfraredLivingFaceResponseBody(TeaModel):
    def __init__(
        self,
        data: DetectInfraredLivingFaceResponseBodyData = None,
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
            temp_model = DetectInfraredLivingFaceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DetectInfraredLivingFaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DetectInfraredLivingFaceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DetectInfraredLivingFaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetectLivingFaceRequestTasks(TeaModel):
    def __init__(
        self,
        image_data: str = None,
        image_url: str = None,
    ):
        self.image_data = image_data
        self.image_url = image_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_data is not None:
            result['ImageData'] = self.image_data
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageData') is not None:
            self.image_data = m.get('ImageData')
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        return self


class DetectLivingFaceRequest(TeaModel):
    def __init__(
        self,
        tasks: List[DetectLivingFaceRequestTasks] = None,
    ):
        # This parameter is required.
        self.tasks = tasks

    def validate(self):
        if self.tasks:
            for k in self.tasks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Tasks'] = []
        if self.tasks is not None:
            for k in self.tasks:
                result['Tasks'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tasks = []
        if m.get('Tasks') is not None:
            for k in m.get('Tasks'):
                temp_model = DetectLivingFaceRequestTasks()
                self.tasks.append(temp_model.from_map(k))
        return self


class DetectLivingFaceAdvanceRequestTasks(TeaModel):
    def __init__(
        self,
        image_data: str = None,
        image_urlobject: BinaryIO = None,
    ):
        self.image_data = image_data
        self.image_urlobject = image_urlobject

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_data is not None:
            result['ImageData'] = self.image_data
        if self.image_urlobject is not None:
            result['ImageURL'] = self.image_urlobject
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageData') is not None:
            self.image_data = m.get('ImageData')
        if m.get('ImageURL') is not None:
            self.image_urlobject = m.get('ImageURL')
        return self


class DetectLivingFaceAdvanceRequest(TeaModel):
    def __init__(
        self,
        tasks: List[DetectLivingFaceAdvanceRequestTasks] = None,
    ):
        # This parameter is required.
        self.tasks = tasks

    def validate(self):
        if self.tasks:
            for k in self.tasks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Tasks'] = []
        if self.tasks is not None:
            for k in self.tasks:
                result['Tasks'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tasks = []
        if m.get('Tasks') is not None:
            for k in m.get('Tasks'):
                temp_model = DetectLivingFaceAdvanceRequestTasks()
                self.tasks.append(temp_model.from_map(k))
        return self


class DetectLivingFaceResponseBodyDataElementsResultsFrames(TeaModel):
    def __init__(
        self,
        rate: float = None,
        url: str = None,
    ):
        self.rate = rate
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rate is not None:
            result['Rate'] = self.rate
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Rate') is not None:
            self.rate = m.get('Rate')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class DetectLivingFaceResponseBodyDataElementsResultsRect(TeaModel):
    def __init__(
        self,
        height: int = None,
        left: int = None,
        top: int = None,
        width: int = None,
    ):
        self.height = height
        self.left = left
        self.top = top
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.height is not None:
            result['Height'] = self.height
        if self.left is not None:
            result['Left'] = self.left
        if self.top is not None:
            result['Top'] = self.top
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Left') is not None:
            self.left = m.get('Left')
        if m.get('Top') is not None:
            self.top = m.get('Top')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class DetectLivingFaceResponseBodyDataElementsResults(TeaModel):
    def __init__(
        self,
        frames: List[DetectLivingFaceResponseBodyDataElementsResultsFrames] = None,
        label: str = None,
        message_tips: str = None,
        rate: float = None,
        rect: DetectLivingFaceResponseBodyDataElementsResultsRect = None,
        suggestion: str = None,
    ):
        self.frames = frames
        self.label = label
        self.message_tips = message_tips
        self.rate = rate
        self.rect = rect
        self.suggestion = suggestion

    def validate(self):
        if self.frames:
            for k in self.frames:
                if k:
                    k.validate()
        if self.rect:
            self.rect.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Frames'] = []
        if self.frames is not None:
            for k in self.frames:
                result['Frames'].append(k.to_map() if k else None)
        if self.label is not None:
            result['Label'] = self.label
        if self.message_tips is not None:
            result['MessageTips'] = self.message_tips
        if self.rate is not None:
            result['Rate'] = self.rate
        if self.rect is not None:
            result['Rect'] = self.rect.to_map()
        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.frames = []
        if m.get('Frames') is not None:
            for k in m.get('Frames'):
                temp_model = DetectLivingFaceResponseBodyDataElementsResultsFrames()
                self.frames.append(temp_model.from_map(k))
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('MessageTips') is not None:
            self.message_tips = m.get('MessageTips')
        if m.get('Rate') is not None:
            self.rate = m.get('Rate')
        if m.get('Rect') is not None:
            temp_model = DetectLivingFaceResponseBodyDataElementsResultsRect()
            self.rect = temp_model.from_map(m['Rect'])
        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')
        return self


class DetectLivingFaceResponseBodyDataElements(TeaModel):
    def __init__(
        self,
        face_number: int = None,
        image_url: str = None,
        results: List[DetectLivingFaceResponseBodyDataElementsResults] = None,
        task_id: str = None,
    ):
        self.face_number = face_number
        self.image_url = image_url
        self.results = results
        self.task_id = task_id

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
        if self.face_number is not None:
            result['FaceNumber'] = self.face_number
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FaceNumber') is not None:
            self.face_number = m.get('FaceNumber')
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        self.results = []
        if m.get('Results') is not None:
            for k in m.get('Results'):
                temp_model = DetectLivingFaceResponseBodyDataElementsResults()
                self.results.append(temp_model.from_map(k))
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DetectLivingFaceResponseBodyData(TeaModel):
    def __init__(
        self,
        elements: List[DetectLivingFaceResponseBodyDataElements] = None,
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
                temp_model = DetectLivingFaceResponseBodyDataElements()
                self.elements.append(temp_model.from_map(k))
        return self


class DetectLivingFaceResponseBody(TeaModel):
    def __init__(
        self,
        data: DetectLivingFaceResponseBodyData = None,
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
            temp_model = DetectLivingFaceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DetectLivingFaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DetectLivingFaceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DetectLivingFaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetectPedestrianRequest(TeaModel):
    def __init__(
        self,
        image_url: str = None,
    ):
        # This parameter is required.
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


class DetectPedestrianAdvanceRequest(TeaModel):
    def __init__(
        self,
        image_urlobject: BinaryIO = None,
    ):
        # This parameter is required.
        self.image_urlobject = image_urlobject

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_urlobject is not None:
            result['ImageURL'] = self.image_urlobject
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_urlobject = m.get('ImageURL')
        return self


class DetectPedestrianResponseBodyDataElements(TeaModel):
    def __init__(
        self,
        boxes: List[int] = None,
        score: float = None,
        type: str = None,
    ):
        # 1
        self.boxes = boxes
        self.score = score
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.boxes is not None:
            result['Boxes'] = self.boxes
        if self.score is not None:
            result['Score'] = self.score
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Boxes') is not None:
            self.boxes = m.get('Boxes')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DetectPedestrianResponseBodyData(TeaModel):
    def __init__(
        self,
        elements: List[DetectPedestrianResponseBodyDataElements] = None,
        height: int = None,
        width: int = None,
    ):
        self.elements = elements
        self.height = height
        self.width = width

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
        if self.height is not None:
            result['Height'] = self.height
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.elements = []
        if m.get('Elements') is not None:
            for k in m.get('Elements'):
                temp_model = DetectPedestrianResponseBodyDataElements()
                self.elements.append(temp_model.from_map(k))
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class DetectPedestrianResponseBody(TeaModel):
    def __init__(
        self,
        data: DetectPedestrianResponseBodyData = None,
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
            temp_model = DetectPedestrianResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DetectPedestrianResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DetectPedestrianResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DetectPedestrianResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetectVideoLivingFaceRequest(TeaModel):
    def __init__(
        self,
        video_url: str = None,
    ):
        # This parameter is required.
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


class DetectVideoLivingFaceAdvanceRequest(TeaModel):
    def __init__(
        self,
        video_url_object: BinaryIO = None,
    ):
        # This parameter is required.
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


class DetectVideoLivingFaceResponseBodyDataElements(TeaModel):
    def __init__(
        self,
        face_confidence: float = None,
        live_confidence: float = None,
        rect: List[int] = None,
    ):
        self.face_confidence = face_confidence
        self.live_confidence = live_confidence
        self.rect = rect

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.face_confidence is not None:
            result['FaceConfidence'] = self.face_confidence
        if self.live_confidence is not None:
            result['LiveConfidence'] = self.live_confidence
        if self.rect is not None:
            result['Rect'] = self.rect
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FaceConfidence') is not None:
            self.face_confidence = m.get('FaceConfidence')
        if m.get('LiveConfidence') is not None:
            self.live_confidence = m.get('LiveConfidence')
        if m.get('Rect') is not None:
            self.rect = m.get('Rect')
        return self


class DetectVideoLivingFaceResponseBodyData(TeaModel):
    def __init__(
        self,
        elements: List[DetectVideoLivingFaceResponseBodyDataElements] = None,
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
                temp_model = DetectVideoLivingFaceResponseBodyDataElements()
                self.elements.append(temp_model.from_map(k))
        return self


class DetectVideoLivingFaceResponseBody(TeaModel):
    def __init__(
        self,
        data: DetectVideoLivingFaceResponseBodyData = None,
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
            temp_model = DetectVideoLivingFaceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DetectVideoLivingFaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DetectVideoLivingFaceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DetectVideoLivingFaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnhanceFaceRequest(TeaModel):
    def __init__(
        self,
        image_url: str = None,
    ):
        # This parameter is required.
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


class EnhanceFaceAdvanceRequest(TeaModel):
    def __init__(
        self,
        image_urlobject: BinaryIO = None,
    ):
        # This parameter is required.
        self.image_urlobject = image_urlobject

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_urlobject is not None:
            result['ImageURL'] = self.image_urlobject
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_urlobject = m.get('ImageURL')
        return self


class EnhanceFaceResponseBodyData(TeaModel):
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


class EnhanceFaceResponseBody(TeaModel):
    def __init__(
        self,
        data: EnhanceFaceResponseBodyData = None,
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
            temp_model = EnhanceFaceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class EnhanceFaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EnhanceFaceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = EnhanceFaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExtractFingerPrintRequest(TeaModel):
    def __init__(
        self,
        image_data: str = None,
        image_url: str = None,
    ):
        self.image_data = image_data
        self.image_url = image_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_data is not None:
            result['ImageData'] = self.image_data
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageData') is not None:
            self.image_data = m.get('ImageData')
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        return self


class ExtractFingerPrintAdvanceRequest(TeaModel):
    def __init__(
        self,
        image_data: str = None,
        image_urlobject: BinaryIO = None,
    ):
        self.image_data = image_data
        self.image_urlobject = image_urlobject

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_data is not None:
            result['ImageData'] = self.image_data
        if self.image_urlobject is not None:
            result['ImageURL'] = self.image_urlobject
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageData') is not None:
            self.image_data = m.get('ImageData')
        if m.get('ImageURL') is not None:
            self.image_urlobject = m.get('ImageURL')
        return self


class ExtractFingerPrintResponseBodyData(TeaModel):
    def __init__(
        self,
        finger_print: str = None,
    ):
        self.finger_print = finger_print

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.finger_print is not None:
            result['FingerPrint'] = self.finger_print
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FingerPrint') is not None:
            self.finger_print = m.get('FingerPrint')
        return self


class ExtractFingerPrintResponseBody(TeaModel):
    def __init__(
        self,
        data: ExtractFingerPrintResponseBodyData = None,
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
            temp_model = ExtractFingerPrintResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ExtractFingerPrintResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ExtractFingerPrintResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ExtractFingerPrintResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FaceBeautyRequest(TeaModel):
    def __init__(
        self,
        image_url: str = None,
        sharp: float = None,
        smooth: float = None,
        white: float = None,
    ):
        # This parameter is required.
        self.image_url = image_url
        # This parameter is required.
        self.sharp = sharp
        # This parameter is required.
        self.smooth = smooth
        # This parameter is required.
        self.white = white

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        if self.sharp is not None:
            result['Sharp'] = self.sharp
        if self.smooth is not None:
            result['Smooth'] = self.smooth
        if self.white is not None:
            result['White'] = self.white
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        if m.get('Sharp') is not None:
            self.sharp = m.get('Sharp')
        if m.get('Smooth') is not None:
            self.smooth = m.get('Smooth')
        if m.get('White') is not None:
            self.white = m.get('White')
        return self


class FaceBeautyAdvanceRequest(TeaModel):
    def __init__(
        self,
        image_urlobject: BinaryIO = None,
        sharp: float = None,
        smooth: float = None,
        white: float = None,
    ):
        # This parameter is required.
        self.image_urlobject = image_urlobject
        # This parameter is required.
        self.sharp = sharp
        # This parameter is required.
        self.smooth = smooth
        # This parameter is required.
        self.white = white

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_urlobject is not None:
            result['ImageURL'] = self.image_urlobject
        if self.sharp is not None:
            result['Sharp'] = self.sharp
        if self.smooth is not None:
            result['Smooth'] = self.smooth
        if self.white is not None:
            result['White'] = self.white
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_urlobject = m.get('ImageURL')
        if m.get('Sharp') is not None:
            self.sharp = m.get('Sharp')
        if m.get('Smooth') is not None:
            self.smooth = m.get('Smooth')
        if m.get('White') is not None:
            self.white = m.get('White')
        return self


class FaceBeautyResponseBodyData(TeaModel):
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


class FaceBeautyResponseBody(TeaModel):
    def __init__(
        self,
        data: FaceBeautyResponseBodyData = None,
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
            temp_model = FaceBeautyResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class FaceBeautyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: FaceBeautyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = FaceBeautyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenRealPersonVerificationTokenRequest(TeaModel):
    def __init__(
        self,
        certificate_name: str = None,
        certificate_number: str = None,
        meta_info: str = None,
    ):
        # This parameter is required.
        self.certificate_name = certificate_name
        # This parameter is required.
        self.certificate_number = certificate_number
        # This parameter is required.
        self.meta_info = meta_info

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certificate_name is not None:
            result['CertificateName'] = self.certificate_name
        if self.certificate_number is not None:
            result['CertificateNumber'] = self.certificate_number
        if self.meta_info is not None:
            result['MetaInfo'] = self.meta_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertificateName') is not None:
            self.certificate_name = m.get('CertificateName')
        if m.get('CertificateNumber') is not None:
            self.certificate_number = m.get('CertificateNumber')
        if m.get('MetaInfo') is not None:
            self.meta_info = m.get('MetaInfo')
        return self


class GenRealPersonVerificationTokenResponseBodyData(TeaModel):
    def __init__(
        self,
        verification_token: str = None,
    ):
        self.verification_token = verification_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.verification_token is not None:
            result['VerificationToken'] = self.verification_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VerificationToken') is not None:
            self.verification_token = m.get('VerificationToken')
        return self


class GenRealPersonVerificationTokenResponseBody(TeaModel):
    def __init__(
        self,
        data: GenRealPersonVerificationTokenResponseBodyData = None,
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
            temp_model = GenRealPersonVerificationTokenResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GenRealPersonVerificationTokenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GenRealPersonVerificationTokenResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = GenRealPersonVerificationTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateHumanAnimeStyleRequest(TeaModel):
    def __init__(
        self,
        algo_type: str = None,
        image_url: str = None,
    ):
        self.algo_type = algo_type
        # This parameter is required.
        self.image_url = image_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algo_type is not None:
            result['AlgoType'] = self.algo_type
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlgoType') is not None:
            self.algo_type = m.get('AlgoType')
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        return self


class GenerateHumanAnimeStyleAdvanceRequest(TeaModel):
    def __init__(
        self,
        algo_type: str = None,
        image_urlobject: BinaryIO = None,
    ):
        self.algo_type = algo_type
        # This parameter is required.
        self.image_urlobject = image_urlobject

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algo_type is not None:
            result['AlgoType'] = self.algo_type
        if self.image_urlobject is not None:
            result['ImageURL'] = self.image_urlobject
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlgoType') is not None:
            self.algo_type = m.get('AlgoType')
        if m.get('ImageURL') is not None:
            self.image_urlobject = m.get('ImageURL')
        return self


class GenerateHumanAnimeStyleResponseBodyData(TeaModel):
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


class GenerateHumanAnimeStyleResponseBody(TeaModel):
    def __init__(
        self,
        data: GenerateHumanAnimeStyleResponseBodyData = None,
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
            temp_model = GenerateHumanAnimeStyleResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GenerateHumanAnimeStyleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GenerateHumanAnimeStyleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = GenerateHumanAnimeStyleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateHumanSketchStyleRequest(TeaModel):
    def __init__(
        self,
        image_url: str = None,
        return_type: str = None,
    ):
        # This parameter is required.
        self.image_url = image_url
        self.return_type = return_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        if self.return_type is not None:
            result['ReturnType'] = self.return_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        if m.get('ReturnType') is not None:
            self.return_type = m.get('ReturnType')
        return self


class GenerateHumanSketchStyleAdvanceRequest(TeaModel):
    def __init__(
        self,
        image_urlobject: BinaryIO = None,
        return_type: str = None,
    ):
        # This parameter is required.
        self.image_urlobject = image_urlobject
        self.return_type = return_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_urlobject is not None:
            result['ImageURL'] = self.image_urlobject
        if self.return_type is not None:
            result['ReturnType'] = self.return_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_urlobject = m.get('ImageURL')
        if m.get('ReturnType') is not None:
            self.return_type = m.get('ReturnType')
        return self


class GenerateHumanSketchStyleResponseBodyData(TeaModel):
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


class GenerateHumanSketchStyleResponseBody(TeaModel):
    def __init__(
        self,
        data: GenerateHumanSketchStyleResponseBodyData = None,
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
            temp_model = GenerateHumanSketchStyleResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GenerateHumanSketchStyleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GenerateHumanSketchStyleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = GenerateHumanSketchStyleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFaceEntityRequest(TeaModel):
    def __init__(
        self,
        db_name: str = None,
        entity_id: str = None,
    ):
        # This parameter is required.
        self.db_name = db_name
        # This parameter is required.
        self.entity_id = entity_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        return self


class GetFaceEntityResponseBodyDataFaces(TeaModel):
    def __init__(
        self,
        face_id: str = None,
    ):
        self.face_id = face_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.face_id is not None:
            result['FaceId'] = self.face_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FaceId') is not None:
            self.face_id = m.get('FaceId')
        return self


class GetFaceEntityResponseBodyData(TeaModel):
    def __init__(
        self,
        db_name: str = None,
        entity_id: str = None,
        faces: List[GetFaceEntityResponseBodyDataFaces] = None,
        labels: str = None,
    ):
        self.db_name = db_name
        self.entity_id = entity_id
        self.faces = faces
        self.labels = labels

    def validate(self):
        if self.faces:
            for k in self.faces:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        result['Faces'] = []
        if self.faces is not None:
            for k in self.faces:
                result['Faces'].append(k.to_map() if k else None)
        if self.labels is not None:
            result['Labels'] = self.labels
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        self.faces = []
        if m.get('Faces') is not None:
            for k in m.get('Faces'):
                temp_model = GetFaceEntityResponseBodyDataFaces()
                self.faces.append(temp_model.from_map(k))
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        return self


class GetFaceEntityResponseBody(TeaModel):
    def __init__(
        self,
        data: GetFaceEntityResponseBodyData = None,
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
            temp_model = GetFaceEntityResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetFaceEntityResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetFaceEntityResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = GetFaceEntityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRealPersonVerificationResultRequest(TeaModel):
    def __init__(
        self,
        verification_token: str = None,
    ):
        # This parameter is required.
        self.verification_token = verification_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.verification_token is not None:
            result['VerificationToken'] = self.verification_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VerificationToken') is not None:
            self.verification_token = m.get('VerificationToken')
        return self


class GetRealPersonVerificationResultResponseBodyData(TeaModel):
    def __init__(
        self,
        passed: bool = None,
    ):
        self.passed = passed

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.passed is not None:
            result['Passed'] = self.passed
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Passed') is not None:
            self.passed = m.get('Passed')
        return self


class GetRealPersonVerificationResultResponseBody(TeaModel):
    def __init__(
        self,
        data: GetRealPersonVerificationResultResponseBodyData = None,
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
            temp_model = GetRealPersonVerificationResultResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetRealPersonVerificationResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetRealPersonVerificationResultResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = GetRealPersonVerificationResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class LiquifyFaceRequest(TeaModel):
    def __init__(
        self,
        image_url: str = None,
        slim_degree: float = None,
    ):
        # This parameter is required.
        self.image_url = image_url
        self.slim_degree = slim_degree

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        if self.slim_degree is not None:
            result['SlimDegree'] = self.slim_degree
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        if m.get('SlimDegree') is not None:
            self.slim_degree = m.get('SlimDegree')
        return self


class LiquifyFaceAdvanceRequest(TeaModel):
    def __init__(
        self,
        image_urlobject: BinaryIO = None,
        slim_degree: float = None,
    ):
        # This parameter is required.
        self.image_urlobject = image_urlobject
        self.slim_degree = slim_degree

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_urlobject is not None:
            result['ImageURL'] = self.image_urlobject
        if self.slim_degree is not None:
            result['SlimDegree'] = self.slim_degree
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_urlobject = m.get('ImageURL')
        if m.get('SlimDegree') is not None:
            self.slim_degree = m.get('SlimDegree')
        return self


class LiquifyFaceResponseBodyData(TeaModel):
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


class LiquifyFaceResponseBody(TeaModel):
    def __init__(
        self,
        data: LiquifyFaceResponseBodyData = None,
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
            temp_model = LiquifyFaceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class LiquifyFaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: LiquifyFaceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = LiquifyFaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFaceDbsRequest(TeaModel):
    def __init__(
        self,
        limit: int = None,
        offset: int = None,
    ):
        self.limit = limit
        self.offset = offset

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.offset is not None:
            result['Offset'] = self.offset
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('Offset') is not None:
            self.offset = m.get('Offset')
        return self


class ListFaceDbsResponseBodyDataDbList(TeaModel):
    def __init__(
        self,
        name: str = None,
    ):
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ListFaceDbsResponseBodyData(TeaModel):
    def __init__(
        self,
        db_list: List[ListFaceDbsResponseBodyDataDbList] = None,
    ):
        self.db_list = db_list

    def validate(self):
        if self.db_list:
            for k in self.db_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DbList'] = []
        if self.db_list is not None:
            for k in self.db_list:
                result['DbList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.db_list = []
        if m.get('DbList') is not None:
            for k in m.get('DbList'):
                temp_model = ListFaceDbsResponseBodyDataDbList()
                self.db_list.append(temp_model.from_map(k))
        return self


class ListFaceDbsResponseBody(TeaModel):
    def __init__(
        self,
        data: ListFaceDbsResponseBodyData = None,
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
            temp_model = ListFaceDbsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListFaceDbsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListFaceDbsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ListFaceDbsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFaceEntitiesRequest(TeaModel):
    def __init__(
        self,
        db_name: str = None,
        entity_id_prefix: str = None,
        labels: str = None,
        limit: int = None,
        offset: int = None,
        order: str = None,
        token: str = None,
    ):
        # This parameter is required.
        self.db_name = db_name
        self.entity_id_prefix = entity_id_prefix
        self.labels = labels
        self.limit = limit
        self.offset = offset
        self.order = order
        self.token = token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.entity_id_prefix is not None:
            result['EntityIdPrefix'] = self.entity_id_prefix
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.offset is not None:
            result['Offset'] = self.offset
        if self.order is not None:
            result['Order'] = self.order
        if self.token is not None:
            result['Token'] = self.token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('EntityIdPrefix') is not None:
            self.entity_id_prefix = m.get('EntityIdPrefix')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('Offset') is not None:
            self.offset = m.get('Offset')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        return self


class ListFaceEntitiesResponseBodyDataEntities(TeaModel):
    def __init__(
        self,
        created_at: int = None,
        db_name: str = None,
        entity_id: str = None,
        face_count: int = None,
        labels: str = None,
        updated_at: int = None,
    ):
        self.created_at = created_at
        self.db_name = db_name
        self.entity_id = entity_id
        self.face_count = face_count
        self.labels = labels
        self.updated_at = updated_at

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.face_count is not None:
            result['FaceCount'] = self.face_count
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('FaceCount') is not None:
            self.face_count = m.get('FaceCount')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')
        return self


class ListFaceEntitiesResponseBodyData(TeaModel):
    def __init__(
        self,
        entities: List[ListFaceEntitiesResponseBodyDataEntities] = None,
        token: str = None,
        total_count: int = None,
    ):
        self.entities = entities
        self.token = token
        self.total_count = total_count

    def validate(self):
        if self.entities:
            for k in self.entities:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Entities'] = []
        if self.entities is not None:
            for k in self.entities:
                result['Entities'].append(k.to_map() if k else None)
        if self.token is not None:
            result['Token'] = self.token
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.entities = []
        if m.get('Entities') is not None:
            for k in m.get('Entities'):
                temp_model = ListFaceEntitiesResponseBodyDataEntities()
                self.entities.append(temp_model.from_map(k))
        if m.get('Token') is not None:
            self.token = m.get('Token')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListFaceEntitiesResponseBody(TeaModel):
    def __init__(
        self,
        data: ListFaceEntitiesResponseBodyData = None,
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
            temp_model = ListFaceEntitiesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListFaceEntitiesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListFaceEntitiesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ListFaceEntitiesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MergeImageFaceRequestMergeInfos(TeaModel):
    def __init__(
        self,
        image_url: str = None,
        template_face_id: str = None,
    ):
        self.image_url = image_url
        self.template_face_id = template_face_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        if self.template_face_id is not None:
            result['TemplateFaceID'] = self.template_face_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        if m.get('TemplateFaceID') is not None:
            self.template_face_id = m.get('TemplateFaceID')
        return self


class MergeImageFaceRequest(TeaModel):
    def __init__(
        self,
        add_watermark: bool = None,
        image_url: str = None,
        merge_infos: List[MergeImageFaceRequestMergeInfos] = None,
        model_version: str = None,
        template_id: str = None,
        watermark_type: str = None,
    ):
        self.add_watermark = add_watermark
        self.image_url = image_url
        self.merge_infos = merge_infos
        self.model_version = model_version
        # This parameter is required.
        self.template_id = template_id
        self.watermark_type = watermark_type

    def validate(self):
        if self.merge_infos:
            for k in self.merge_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.add_watermark is not None:
            result['AddWatermark'] = self.add_watermark
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        result['MergeInfos'] = []
        if self.merge_infos is not None:
            for k in self.merge_infos:
                result['MergeInfos'].append(k.to_map() if k else None)
        if self.model_version is not None:
            result['ModelVersion'] = self.model_version
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.watermark_type is not None:
            result['WatermarkType'] = self.watermark_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddWatermark') is not None:
            self.add_watermark = m.get('AddWatermark')
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        self.merge_infos = []
        if m.get('MergeInfos') is not None:
            for k in m.get('MergeInfos'):
                temp_model = MergeImageFaceRequestMergeInfos()
                self.merge_infos.append(temp_model.from_map(k))
        if m.get('ModelVersion') is not None:
            self.model_version = m.get('ModelVersion')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('WatermarkType') is not None:
            self.watermark_type = m.get('WatermarkType')
        return self


class MergeImageFaceAdvanceRequestMergeInfos(TeaModel):
    def __init__(
        self,
        image_url: str = None,
        template_face_id: str = None,
    ):
        self.image_url = image_url
        self.template_face_id = template_face_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        if self.template_face_id is not None:
            result['TemplateFaceID'] = self.template_face_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        if m.get('TemplateFaceID') is not None:
            self.template_face_id = m.get('TemplateFaceID')
        return self


class MergeImageFaceAdvanceRequest(TeaModel):
    def __init__(
        self,
        add_watermark: bool = None,
        image_urlobject: BinaryIO = None,
        merge_infos: List[MergeImageFaceAdvanceRequestMergeInfos] = None,
        model_version: str = None,
        template_id: str = None,
        watermark_type: str = None,
    ):
        self.add_watermark = add_watermark
        self.image_urlobject = image_urlobject
        self.merge_infos = merge_infos
        self.model_version = model_version
        # This parameter is required.
        self.template_id = template_id
        self.watermark_type = watermark_type

    def validate(self):
        if self.merge_infos:
            for k in self.merge_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.add_watermark is not None:
            result['AddWatermark'] = self.add_watermark
        if self.image_urlobject is not None:
            result['ImageURL'] = self.image_urlobject
        result['MergeInfos'] = []
        if self.merge_infos is not None:
            for k in self.merge_infos:
                result['MergeInfos'].append(k.to_map() if k else None)
        if self.model_version is not None:
            result['ModelVersion'] = self.model_version
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.watermark_type is not None:
            result['WatermarkType'] = self.watermark_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddWatermark') is not None:
            self.add_watermark = m.get('AddWatermark')
        if m.get('ImageURL') is not None:
            self.image_urlobject = m.get('ImageURL')
        self.merge_infos = []
        if m.get('MergeInfos') is not None:
            for k in m.get('MergeInfos'):
                temp_model = MergeImageFaceAdvanceRequestMergeInfos()
                self.merge_infos.append(temp_model.from_map(k))
        if m.get('ModelVersion') is not None:
            self.model_version = m.get('ModelVersion')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('WatermarkType') is not None:
            self.watermark_type = m.get('WatermarkType')
        return self


class MergeImageFaceResponseBodyData(TeaModel):
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


class MergeImageFaceResponseBody(TeaModel):
    def __init__(
        self,
        data: MergeImageFaceResponseBodyData = None,
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
            temp_model = MergeImageFaceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class MergeImageFaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: MergeImageFaceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = MergeImageFaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MonitorExaminationRequest(TeaModel):
    def __init__(
        self,
        image_url: str = None,
        type: int = None,
    ):
        # This parameter is required.
        self.image_url = image_url
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class MonitorExaminationAdvanceRequest(TeaModel):
    def __init__(
        self,
        image_urlobject: BinaryIO = None,
        type: int = None,
    ):
        # This parameter is required.
        self.image_urlobject = image_urlobject
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_urlobject is not None:
            result['ImageURL'] = self.image_urlobject
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_urlobject = m.get('ImageURL')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class MonitorExaminationResponseBodyDataFaceInfoPose(TeaModel):
    def __init__(
        self,
        pitch: float = None,
        roll: float = None,
        yaw: float = None,
    ):
        self.pitch = pitch
        self.roll = roll
        self.yaw = yaw

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pitch is not None:
            result['Pitch'] = self.pitch
        if self.roll is not None:
            result['Roll'] = self.roll
        if self.yaw is not None:
            result['Yaw'] = self.yaw
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Pitch') is not None:
            self.pitch = m.get('Pitch')
        if m.get('Roll') is not None:
            self.roll = m.get('Roll')
        if m.get('Yaw') is not None:
            self.yaw = m.get('Yaw')
        return self


class MonitorExaminationResponseBodyDataFaceInfo(TeaModel):
    def __init__(
        self,
        completeness: float = None,
        face_number: int = None,
        pose: MonitorExaminationResponseBodyDataFaceInfoPose = None,
    ):
        self.completeness = completeness
        self.face_number = face_number
        self.pose = pose

    def validate(self):
        if self.pose:
            self.pose.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.completeness is not None:
            result['Completeness'] = self.completeness
        if self.face_number is not None:
            result['FaceNumber'] = self.face_number
        if self.pose is not None:
            result['Pose'] = self.pose.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Completeness') is not None:
            self.completeness = m.get('Completeness')
        if m.get('FaceNumber') is not None:
            self.face_number = m.get('FaceNumber')
        if m.get('Pose') is not None:
            temp_model = MonitorExaminationResponseBodyDataFaceInfoPose()
            self.pose = temp_model.from_map(m['Pose'])
        return self


class MonitorExaminationResponseBodyDataPersonInfoCellPhone(TeaModel):
    def __init__(
        self,
        score: float = None,
        threshold: float = None,
    ):
        self.score = score
        self.threshold = threshold

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.score is not None:
            result['Score'] = self.score
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        return self


class MonitorExaminationResponseBodyDataPersonInfoEarPhone(TeaModel):
    def __init__(
        self,
        score: float = None,
        threshold: float = None,
    ):
        self.score = score
        self.threshold = threshold

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.score is not None:
            result['Score'] = self.score
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        return self


class MonitorExaminationResponseBodyDataPersonInfo(TeaModel):
    def __init__(
        self,
        cell_phone: MonitorExaminationResponseBodyDataPersonInfoCellPhone = None,
        ear_phone: MonitorExaminationResponseBodyDataPersonInfoEarPhone = None,
        person_number: int = None,
    ):
        self.cell_phone = cell_phone
        self.ear_phone = ear_phone
        self.person_number = person_number

    def validate(self):
        if self.cell_phone:
            self.cell_phone.validate()
        if self.ear_phone:
            self.ear_phone.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cell_phone is not None:
            result['CellPhone'] = self.cell_phone.to_map()
        if self.ear_phone is not None:
            result['EarPhone'] = self.ear_phone.to_map()
        if self.person_number is not None:
            result['PersonNumber'] = self.person_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CellPhone') is not None:
            temp_model = MonitorExaminationResponseBodyDataPersonInfoCellPhone()
            self.cell_phone = temp_model.from_map(m['CellPhone'])
        if m.get('EarPhone') is not None:
            temp_model = MonitorExaminationResponseBodyDataPersonInfoEarPhone()
            self.ear_phone = temp_model.from_map(m['EarPhone'])
        if m.get('PersonNumber') is not None:
            self.person_number = m.get('PersonNumber')
        return self


class MonitorExaminationResponseBodyData(TeaModel):
    def __init__(
        self,
        chat_score: float = None,
        face_info: MonitorExaminationResponseBodyDataFaceInfo = None,
        person_info: MonitorExaminationResponseBodyDataPersonInfo = None,
        threshold: float = None,
    ):
        self.chat_score = chat_score
        self.face_info = face_info
        self.person_info = person_info
        self.threshold = threshold

    def validate(self):
        if self.face_info:
            self.face_info.validate()
        if self.person_info:
            self.person_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.chat_score is not None:
            result['ChatScore'] = self.chat_score
        if self.face_info is not None:
            result['FaceInfo'] = self.face_info.to_map()
        if self.person_info is not None:
            result['PersonInfo'] = self.person_info.to_map()
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChatScore') is not None:
            self.chat_score = m.get('ChatScore')
        if m.get('FaceInfo') is not None:
            temp_model = MonitorExaminationResponseBodyDataFaceInfo()
            self.face_info = temp_model.from_map(m['FaceInfo'])
        if m.get('PersonInfo') is not None:
            temp_model = MonitorExaminationResponseBodyDataPersonInfo()
            self.person_info = temp_model.from_map(m['PersonInfo'])
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        return self


class MonitorExaminationResponseBody(TeaModel):
    def __init__(
        self,
        data: MonitorExaminationResponseBodyData = None,
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
            temp_model = MonitorExaminationResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class MonitorExaminationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: MonitorExaminationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = MonitorExaminationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PedestrianDetectAttributeRequest(TeaModel):
    def __init__(
        self,
        image_url: str = None,
    ):
        # This parameter is required.
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


class PedestrianDetectAttributeAdvanceRequest(TeaModel):
    def __init__(
        self,
        image_urlobject: BinaryIO = None,
    ):
        # This parameter is required.
        self.image_urlobject = image_urlobject

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_urlobject is not None:
            result['ImageURL'] = self.image_urlobject
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_urlobject = m.get('ImageURL')
        return self


class PedestrianDetectAttributeResponseBodyDataAttributesAge(TeaModel):
    def __init__(
        self,
        name: str = None,
        score: float = None,
    ):
        self.name = name
        self.score = score

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.score is not None:
            result['Score'] = self.score
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        return self


class PedestrianDetectAttributeResponseBodyDataAttributesBackpack(TeaModel):
    def __init__(
        self,
        name: str = None,
        score: float = None,
    ):
        self.name = name
        self.score = score

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.score is not None:
            result['Score'] = self.score
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        return self


class PedestrianDetectAttributeResponseBodyDataAttributesGender(TeaModel):
    def __init__(
        self,
        name: str = None,
        score: float = None,
    ):
        self.name = name
        self.score = score

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.score is not None:
            result['Score'] = self.score
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        return self


class PedestrianDetectAttributeResponseBodyDataAttributesGlasses(TeaModel):
    def __init__(
        self,
        name: str = None,
        score: float = None,
    ):
        self.name = name
        self.score = score

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.score is not None:
            result['Score'] = self.score
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        return self


class PedestrianDetectAttributeResponseBodyDataAttributesHandbag(TeaModel):
    def __init__(
        self,
        name: str = None,
        score: float = None,
    ):
        self.name = name
        self.score = score

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.score is not None:
            result['Score'] = self.score
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        return self


class PedestrianDetectAttributeResponseBodyDataAttributesHat(TeaModel):
    def __init__(
        self,
        name: str = None,
        score: float = None,
    ):
        self.name = name
        self.score = score

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.score is not None:
            result['Score'] = self.score
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        return self


class PedestrianDetectAttributeResponseBodyDataAttributesLowerColor(TeaModel):
    def __init__(
        self,
        name: str = None,
        score: float = None,
    ):
        self.name = name
        self.score = score

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.score is not None:
            result['Score'] = self.score
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        return self


class PedestrianDetectAttributeResponseBodyDataAttributesLowerWear(TeaModel):
    def __init__(
        self,
        name: str = None,
        score: float = None,
    ):
        self.name = name
        self.score = score

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.score is not None:
            result['Score'] = self.score
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        return self


class PedestrianDetectAttributeResponseBodyDataAttributesOrient(TeaModel):
    def __init__(
        self,
        name: str = None,
        score: float = None,
    ):
        self.name = name
        self.score = score

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.score is not None:
            result['Score'] = self.score
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        return self


class PedestrianDetectAttributeResponseBodyDataAttributesShoulderBag(TeaModel):
    def __init__(
        self,
        name: str = None,
        score: float = None,
    ):
        self.name = name
        self.score = score

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.score is not None:
            result['Score'] = self.score
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        return self


class PedestrianDetectAttributeResponseBodyDataAttributesUpperColor(TeaModel):
    def __init__(
        self,
        name: str = None,
        score: float = None,
    ):
        self.name = name
        self.score = score

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.score is not None:
            result['Score'] = self.score
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        return self


class PedestrianDetectAttributeResponseBodyDataAttributesUpperWear(TeaModel):
    def __init__(
        self,
        name: str = None,
        score: float = None,
    ):
        self.name = name
        self.score = score

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.score is not None:
            result['Score'] = self.score
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        return self


class PedestrianDetectAttributeResponseBodyDataAttributes(TeaModel):
    def __init__(
        self,
        age: PedestrianDetectAttributeResponseBodyDataAttributesAge = None,
        backpack: PedestrianDetectAttributeResponseBodyDataAttributesBackpack = None,
        gender: PedestrianDetectAttributeResponseBodyDataAttributesGender = None,
        glasses: PedestrianDetectAttributeResponseBodyDataAttributesGlasses = None,
        handbag: PedestrianDetectAttributeResponseBodyDataAttributesHandbag = None,
        hat: PedestrianDetectAttributeResponseBodyDataAttributesHat = None,
        lower_color: PedestrianDetectAttributeResponseBodyDataAttributesLowerColor = None,
        lower_wear: PedestrianDetectAttributeResponseBodyDataAttributesLowerWear = None,
        orient: PedestrianDetectAttributeResponseBodyDataAttributesOrient = None,
        shoulder_bag: PedestrianDetectAttributeResponseBodyDataAttributesShoulderBag = None,
        upper_color: PedestrianDetectAttributeResponseBodyDataAttributesUpperColor = None,
        upper_wear: PedestrianDetectAttributeResponseBodyDataAttributesUpperWear = None,
    ):
        self.age = age
        self.backpack = backpack
        self.gender = gender
        self.glasses = glasses
        self.handbag = handbag
        self.hat = hat
        self.lower_color = lower_color
        self.lower_wear = lower_wear
        self.orient = orient
        self.shoulder_bag = shoulder_bag
        self.upper_color = upper_color
        self.upper_wear = upper_wear

    def validate(self):
        if self.age:
            self.age.validate()
        if self.backpack:
            self.backpack.validate()
        if self.gender:
            self.gender.validate()
        if self.glasses:
            self.glasses.validate()
        if self.handbag:
            self.handbag.validate()
        if self.hat:
            self.hat.validate()
        if self.lower_color:
            self.lower_color.validate()
        if self.lower_wear:
            self.lower_wear.validate()
        if self.orient:
            self.orient.validate()
        if self.shoulder_bag:
            self.shoulder_bag.validate()
        if self.upper_color:
            self.upper_color.validate()
        if self.upper_wear:
            self.upper_wear.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.age is not None:
            result['Age'] = self.age.to_map()
        if self.backpack is not None:
            result['Backpack'] = self.backpack.to_map()
        if self.gender is not None:
            result['Gender'] = self.gender.to_map()
        if self.glasses is not None:
            result['Glasses'] = self.glasses.to_map()
        if self.handbag is not None:
            result['Handbag'] = self.handbag.to_map()
        if self.hat is not None:
            result['Hat'] = self.hat.to_map()
        if self.lower_color is not None:
            result['LowerColor'] = self.lower_color.to_map()
        if self.lower_wear is not None:
            result['LowerWear'] = self.lower_wear.to_map()
        if self.orient is not None:
            result['Orient'] = self.orient.to_map()
        if self.shoulder_bag is not None:
            result['ShoulderBag'] = self.shoulder_bag.to_map()
        if self.upper_color is not None:
            result['UpperColor'] = self.upper_color.to_map()
        if self.upper_wear is not None:
            result['UpperWear'] = self.upper_wear.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Age') is not None:
            temp_model = PedestrianDetectAttributeResponseBodyDataAttributesAge()
            self.age = temp_model.from_map(m['Age'])
        if m.get('Backpack') is not None:
            temp_model = PedestrianDetectAttributeResponseBodyDataAttributesBackpack()
            self.backpack = temp_model.from_map(m['Backpack'])
        if m.get('Gender') is not None:
            temp_model = PedestrianDetectAttributeResponseBodyDataAttributesGender()
            self.gender = temp_model.from_map(m['Gender'])
        if m.get('Glasses') is not None:
            temp_model = PedestrianDetectAttributeResponseBodyDataAttributesGlasses()
            self.glasses = temp_model.from_map(m['Glasses'])
        if m.get('Handbag') is not None:
            temp_model = PedestrianDetectAttributeResponseBodyDataAttributesHandbag()
            self.handbag = temp_model.from_map(m['Handbag'])
        if m.get('Hat') is not None:
            temp_model = PedestrianDetectAttributeResponseBodyDataAttributesHat()
            self.hat = temp_model.from_map(m['Hat'])
        if m.get('LowerColor') is not None:
            temp_model = PedestrianDetectAttributeResponseBodyDataAttributesLowerColor()
            self.lower_color = temp_model.from_map(m['LowerColor'])
        if m.get('LowerWear') is not None:
            temp_model = PedestrianDetectAttributeResponseBodyDataAttributesLowerWear()
            self.lower_wear = temp_model.from_map(m['LowerWear'])
        if m.get('Orient') is not None:
            temp_model = PedestrianDetectAttributeResponseBodyDataAttributesOrient()
            self.orient = temp_model.from_map(m['Orient'])
        if m.get('ShoulderBag') is not None:
            temp_model = PedestrianDetectAttributeResponseBodyDataAttributesShoulderBag()
            self.shoulder_bag = temp_model.from_map(m['ShoulderBag'])
        if m.get('UpperColor') is not None:
            temp_model = PedestrianDetectAttributeResponseBodyDataAttributesUpperColor()
            self.upper_color = temp_model.from_map(m['UpperColor'])
        if m.get('UpperWear') is not None:
            temp_model = PedestrianDetectAttributeResponseBodyDataAttributesUpperWear()
            self.upper_wear = temp_model.from_map(m['UpperWear'])
        return self


class PedestrianDetectAttributeResponseBodyDataBoxes(TeaModel):
    def __init__(
        self,
        bottom_right_x: float = None,
        bottom_right_y: float = None,
        score: float = None,
        top_left_x: float = None,
        top_left_y: float = None,
    ):
        self.bottom_right_x = bottom_right_x
        self.bottom_right_y = bottom_right_y
        self.score = score
        self.top_left_x = top_left_x
        self.top_left_y = top_left_y

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bottom_right_x is not None:
            result['BottomRightX'] = self.bottom_right_x
        if self.bottom_right_y is not None:
            result['BottomRightY'] = self.bottom_right_y
        if self.score is not None:
            result['Score'] = self.score
        if self.top_left_x is not None:
            result['TopLeftX'] = self.top_left_x
        if self.top_left_y is not None:
            result['TopLeftY'] = self.top_left_y
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BottomRightX') is not None:
            self.bottom_right_x = m.get('BottomRightX')
        if m.get('BottomRightY') is not None:
            self.bottom_right_y = m.get('BottomRightY')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('TopLeftX') is not None:
            self.top_left_x = m.get('TopLeftX')
        if m.get('TopLeftY') is not None:
            self.top_left_y = m.get('TopLeftY')
        return self


class PedestrianDetectAttributeResponseBodyData(TeaModel):
    def __init__(
        self,
        attributes: List[PedestrianDetectAttributeResponseBodyDataAttributes] = None,
        boxes: List[PedestrianDetectAttributeResponseBodyDataBoxes] = None,
        height: int = None,
        person_number: int = None,
        width: int = None,
    ):
        self.attributes = attributes
        self.boxes = boxes
        self.height = height
        self.person_number = person_number
        self.width = width

    def validate(self):
        if self.attributes:
            for k in self.attributes:
                if k:
                    k.validate()
        if self.boxes:
            for k in self.boxes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Attributes'] = []
        if self.attributes is not None:
            for k in self.attributes:
                result['Attributes'].append(k.to_map() if k else None)
        result['Boxes'] = []
        if self.boxes is not None:
            for k in self.boxes:
                result['Boxes'].append(k.to_map() if k else None)
        if self.height is not None:
            result['Height'] = self.height
        if self.person_number is not None:
            result['PersonNumber'] = self.person_number
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.attributes = []
        if m.get('Attributes') is not None:
            for k in m.get('Attributes'):
                temp_model = PedestrianDetectAttributeResponseBodyDataAttributes()
                self.attributes.append(temp_model.from_map(k))
        self.boxes = []
        if m.get('Boxes') is not None:
            for k in m.get('Boxes'):
                temp_model = PedestrianDetectAttributeResponseBodyDataBoxes()
                self.boxes.append(temp_model.from_map(k))
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('PersonNumber') is not None:
            self.person_number = m.get('PersonNumber')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class PedestrianDetectAttributeResponseBody(TeaModel):
    def __init__(
        self,
        data: PedestrianDetectAttributeResponseBodyData = None,
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
            temp_model = PedestrianDetectAttributeResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class PedestrianDetectAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PedestrianDetectAttributeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = PedestrianDetectAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryFaceImageTemplateRequest(TeaModel):
    def __init__(
        self,
        page_no: int = None,
        page_size: int = None,
        template_id: str = None,
    ):
        self.page_no = page_no
        self.page_size = page_size
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class QueryFaceImageTemplateResponseBodyDataElementsFaceInfosFaceRect(TeaModel):
    def __init__(
        self,
        height: str = None,
        width: str = None,
        x: str = None,
        y: str = None,
    ):
        self.height = height
        self.width = width
        self.x = x
        self.y = y

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.height is not None:
            result['Height'] = self.height
        if self.width is not None:
            result['Width'] = self.width
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        return self


class QueryFaceImageTemplateResponseBodyDataElementsFaceInfos(TeaModel):
    def __init__(
        self,
        face_rect: QueryFaceImageTemplateResponseBodyDataElementsFaceInfosFaceRect = None,
        template_face_id: str = None,
    ):
        self.face_rect = face_rect
        self.template_face_id = template_face_id

    def validate(self):
        if self.face_rect:
            self.face_rect.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.face_rect is not None:
            result['FaceRect'] = self.face_rect.to_map()
        if self.template_face_id is not None:
            result['TemplateFaceID'] = self.template_face_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FaceRect') is not None:
            temp_model = QueryFaceImageTemplateResponseBodyDataElementsFaceInfosFaceRect()
            self.face_rect = temp_model.from_map(m['FaceRect'])
        if m.get('TemplateFaceID') is not None:
            self.template_face_id = m.get('TemplateFaceID')
        return self


class QueryFaceImageTemplateResponseBodyDataElements(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        face_infos: List[QueryFaceImageTemplateResponseBodyDataElementsFaceInfos] = None,
        template_id: str = None,
        template_url: str = None,
        update_time: str = None,
        user_id: str = None,
    ):
        self.create_time = create_time
        self.face_infos = face_infos
        self.template_id = template_id
        self.template_url = template_url
        self.update_time = update_time
        self.user_id = user_id

    def validate(self):
        if self.face_infos:
            for k in self.face_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        result['FaceInfos'] = []
        if self.face_infos is not None:
            for k in self.face_infos:
                result['FaceInfos'].append(k.to_map() if k else None)
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_url is not None:
            result['TemplateURL'] = self.template_url
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        self.face_infos = []
        if m.get('FaceInfos') is not None:
            for k in m.get('FaceInfos'):
                temp_model = QueryFaceImageTemplateResponseBodyDataElementsFaceInfos()
                self.face_infos.append(temp_model.from_map(k))
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateURL') is not None:
            self.template_url = m.get('TemplateURL')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class QueryFaceImageTemplateResponseBodyData(TeaModel):
    def __init__(
        self,
        elements: List[QueryFaceImageTemplateResponseBodyDataElements] = None,
        total: int = None,
    ):
        self.elements = elements
        self.total = total

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
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.elements = []
        if m.get('Elements') is not None:
            for k in m.get('Elements'):
                temp_model = QueryFaceImageTemplateResponseBodyDataElements()
                self.elements.append(temp_model.from_map(k))
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class QueryFaceImageTemplateResponseBody(TeaModel):
    def __init__(
        self,
        data: QueryFaceImageTemplateResponseBodyData = None,
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
            temp_model = QueryFaceImageTemplateResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryFaceImageTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryFaceImageTemplateResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = QueryFaceImageTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeActionRequestURLList(TeaModel):
    def __init__(
        self,
        url: str = None,
        image_data: str = None,
    ):
        self.url = url
        self.image_data = image_data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['URL'] = self.url
        if self.image_data is not None:
            result['imageData'] = self.image_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('URL') is not None:
            self.url = m.get('URL')
        if m.get('imageData') is not None:
            self.image_data = m.get('imageData')
        return self


class RecognizeActionRequest(TeaModel):
    def __init__(
        self,
        type: int = None,
        urllist: List[RecognizeActionRequestURLList] = None,
        video_data: str = None,
        video_url: str = None,
    ):
        # This parameter is required.
        self.type = type
        self.urllist = urllist
        self.video_data = video_data
        self.video_url = video_url

    def validate(self):
        if self.urllist:
            for k in self.urllist:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        result['URLList'] = []
        if self.urllist is not None:
            for k in self.urllist:
                result['URLList'].append(k.to_map() if k else None)
        if self.video_data is not None:
            result['VideoData'] = self.video_data
        if self.video_url is not None:
            result['VideoUrl'] = self.video_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        self.urllist = []
        if m.get('URLList') is not None:
            for k in m.get('URLList'):
                temp_model = RecognizeActionRequestURLList()
                self.urllist.append(temp_model.from_map(k))
        if m.get('VideoData') is not None:
            self.video_data = m.get('VideoData')
        if m.get('VideoUrl') is not None:
            self.video_url = m.get('VideoUrl')
        return self


class RecognizeActionAdvanceRequestURLList(TeaModel):
    def __init__(
        self,
        urlobject: BinaryIO = None,
        image_data: str = None,
    ):
        self.urlobject = urlobject
        self.image_data = image_data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.urlobject is not None:
            result['URL'] = self.urlobject
        if self.image_data is not None:
            result['imageData'] = self.image_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('URL') is not None:
            self.urlobject = m.get('URL')
        if m.get('imageData') is not None:
            self.image_data = m.get('imageData')
        return self


class RecognizeActionAdvanceRequest(TeaModel):
    def __init__(
        self,
        type: int = None,
        urllist: List[RecognizeActionAdvanceRequestURLList] = None,
        video_data: str = None,
        video_url_object: BinaryIO = None,
    ):
        # This parameter is required.
        self.type = type
        self.urllist = urllist
        self.video_data = video_data
        self.video_url_object = video_url_object

    def validate(self):
        if self.urllist:
            for k in self.urllist:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        result['URLList'] = []
        if self.urllist is not None:
            for k in self.urllist:
                result['URLList'].append(k.to_map() if k else None)
        if self.video_data is not None:
            result['VideoData'] = self.video_data
        if self.video_url_object is not None:
            result['VideoUrl'] = self.video_url_object
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        self.urllist = []
        if m.get('URLList') is not None:
            for k in m.get('URLList'):
                temp_model = RecognizeActionAdvanceRequestURLList()
                self.urllist.append(temp_model.from_map(k))
        if m.get('VideoData') is not None:
            self.video_data = m.get('VideoData')
        if m.get('VideoUrl') is not None:
            self.video_url_object = m.get('VideoUrl')
        return self


class RecognizeActionResponseBodyDataElementsBoxes(TeaModel):
    def __init__(
        self,
        box: List[int] = None,
    ):
        self.box = box

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.box is not None:
            result['Box'] = self.box
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Box') is not None:
            self.box = m.get('Box')
        return self


class RecognizeActionResponseBodyDataElements(TeaModel):
    def __init__(
        self,
        boxes: List[RecognizeActionResponseBodyDataElementsBoxes] = None,
        labels: List[str] = None,
        scores: List[float] = None,
        timestamp: int = None,
    ):
        self.boxes = boxes
        self.labels = labels
        self.scores = scores
        self.timestamp = timestamp

    def validate(self):
        if self.boxes:
            for k in self.boxes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Boxes'] = []
        if self.boxes is not None:
            for k in self.boxes:
                result['Boxes'].append(k.to_map() if k else None)
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.scores is not None:
            result['Scores'] = self.scores
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.boxes = []
        if m.get('Boxes') is not None:
            for k in m.get('Boxes'):
                temp_model = RecognizeActionResponseBodyDataElementsBoxes()
                self.boxes.append(temp_model.from_map(k))
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('Scores') is not None:
            self.scores = m.get('Scores')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        return self


class RecognizeActionResponseBodyData(TeaModel):
    def __init__(
        self,
        elements: List[RecognizeActionResponseBodyDataElements] = None,
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
                temp_model = RecognizeActionResponseBodyDataElements()
                self.elements.append(temp_model.from_map(k))
        return self


class RecognizeActionResponseBody(TeaModel):
    def __init__(
        self,
        data: RecognizeActionResponseBodyData = None,
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
            temp_model = RecognizeActionResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RecognizeActionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RecognizeActionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = RecognizeActionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeExpressionRequest(TeaModel):
    def __init__(
        self,
        image_url: str = None,
    ):
        # This parameter is required.
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


class RecognizeExpressionAdvanceRequest(TeaModel):
    def __init__(
        self,
        image_urlobject: BinaryIO = None,
    ):
        # This parameter is required.
        self.image_urlobject = image_urlobject

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_urlobject is not None:
            result['ImageURL'] = self.image_urlobject
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_urlobject = m.get('ImageURL')
        return self


class RecognizeExpressionResponseBodyDataElementsFaceRectangle(TeaModel):
    def __init__(
        self,
        height: int = None,
        left: int = None,
        top: int = None,
        width: int = None,
    ):
        self.height = height
        self.left = left
        self.top = top
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.height is not None:
            result['Height'] = self.height
        if self.left is not None:
            result['Left'] = self.left
        if self.top is not None:
            result['Top'] = self.top
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Left') is not None:
            self.left = m.get('Left')
        if m.get('Top') is not None:
            self.top = m.get('Top')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class RecognizeExpressionResponseBodyDataElements(TeaModel):
    def __init__(
        self,
        expression: str = None,
        face_probability: float = None,
        face_rectangle: RecognizeExpressionResponseBodyDataElementsFaceRectangle = None,
    ):
        self.expression = expression
        self.face_probability = face_probability
        self.face_rectangle = face_rectangle

    def validate(self):
        if self.face_rectangle:
            self.face_rectangle.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expression is not None:
            result['Expression'] = self.expression
        if self.face_probability is not None:
            result['FaceProbability'] = self.face_probability
        if self.face_rectangle is not None:
            result['FaceRectangle'] = self.face_rectangle.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Expression') is not None:
            self.expression = m.get('Expression')
        if m.get('FaceProbability') is not None:
            self.face_probability = m.get('FaceProbability')
        if m.get('FaceRectangle') is not None:
            temp_model = RecognizeExpressionResponseBodyDataElementsFaceRectangle()
            self.face_rectangle = temp_model.from_map(m['FaceRectangle'])
        return self


class RecognizeExpressionResponseBodyData(TeaModel):
    def __init__(
        self,
        elements: List[RecognizeExpressionResponseBodyDataElements] = None,
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
                temp_model = RecognizeExpressionResponseBodyDataElements()
                self.elements.append(temp_model.from_map(k))
        return self


class RecognizeExpressionResponseBody(TeaModel):
    def __init__(
        self,
        data: RecognizeExpressionResponseBodyData = None,
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
            temp_model = RecognizeExpressionResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RecognizeExpressionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RecognizeExpressionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = RecognizeExpressionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeFaceRequest(TeaModel):
    def __init__(
        self,
        age: bool = None,
        beauty: bool = None,
        expression: bool = None,
        gender: bool = None,
        glass: bool = None,
        hat: bool = None,
        image_url: str = None,
        mask: bool = None,
        max_face_number: int = None,
        quality: bool = None,
    ):
        self.age = age
        self.beauty = beauty
        self.expression = expression
        self.gender = gender
        self.glass = glass
        self.hat = hat
        # This parameter is required.
        self.image_url = image_url
        self.mask = mask
        self.max_face_number = max_face_number
        self.quality = quality

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.age is not None:
            result['Age'] = self.age
        if self.beauty is not None:
            result['Beauty'] = self.beauty
        if self.expression is not None:
            result['Expression'] = self.expression
        if self.gender is not None:
            result['Gender'] = self.gender
        if self.glass is not None:
            result['Glass'] = self.glass
        if self.hat is not None:
            result['Hat'] = self.hat
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        if self.mask is not None:
            result['Mask'] = self.mask
        if self.max_face_number is not None:
            result['MaxFaceNumber'] = self.max_face_number
        if self.quality is not None:
            result['Quality'] = self.quality
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Age') is not None:
            self.age = m.get('Age')
        if m.get('Beauty') is not None:
            self.beauty = m.get('Beauty')
        if m.get('Expression') is not None:
            self.expression = m.get('Expression')
        if m.get('Gender') is not None:
            self.gender = m.get('Gender')
        if m.get('Glass') is not None:
            self.glass = m.get('Glass')
        if m.get('Hat') is not None:
            self.hat = m.get('Hat')
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        if m.get('Mask') is not None:
            self.mask = m.get('Mask')
        if m.get('MaxFaceNumber') is not None:
            self.max_face_number = m.get('MaxFaceNumber')
        if m.get('Quality') is not None:
            self.quality = m.get('Quality')
        return self


class RecognizeFaceAdvanceRequest(TeaModel):
    def __init__(
        self,
        age: bool = None,
        beauty: bool = None,
        expression: bool = None,
        gender: bool = None,
        glass: bool = None,
        hat: bool = None,
        image_urlobject: BinaryIO = None,
        mask: bool = None,
        max_face_number: int = None,
        quality: bool = None,
    ):
        self.age = age
        self.beauty = beauty
        self.expression = expression
        self.gender = gender
        self.glass = glass
        self.hat = hat
        # This parameter is required.
        self.image_urlobject = image_urlobject
        self.mask = mask
        self.max_face_number = max_face_number
        self.quality = quality

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.age is not None:
            result['Age'] = self.age
        if self.beauty is not None:
            result['Beauty'] = self.beauty
        if self.expression is not None:
            result['Expression'] = self.expression
        if self.gender is not None:
            result['Gender'] = self.gender
        if self.glass is not None:
            result['Glass'] = self.glass
        if self.hat is not None:
            result['Hat'] = self.hat
        if self.image_urlobject is not None:
            result['ImageURL'] = self.image_urlobject
        if self.mask is not None:
            result['Mask'] = self.mask
        if self.max_face_number is not None:
            result['MaxFaceNumber'] = self.max_face_number
        if self.quality is not None:
            result['Quality'] = self.quality
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Age') is not None:
            self.age = m.get('Age')
        if m.get('Beauty') is not None:
            self.beauty = m.get('Beauty')
        if m.get('Expression') is not None:
            self.expression = m.get('Expression')
        if m.get('Gender') is not None:
            self.gender = m.get('Gender')
        if m.get('Glass') is not None:
            self.glass = m.get('Glass')
        if m.get('Hat') is not None:
            self.hat = m.get('Hat')
        if m.get('ImageURL') is not None:
            self.image_urlobject = m.get('ImageURL')
        if m.get('Mask') is not None:
            self.mask = m.get('Mask')
        if m.get('MaxFaceNumber') is not None:
            self.max_face_number = m.get('MaxFaceNumber')
        if m.get('Quality') is not None:
            self.quality = m.get('Quality')
        return self


class RecognizeFaceResponseBodyDataQualities(TeaModel):
    def __init__(
        self,
        blur_list: List[float] = None,
        fnf_list: List[float] = None,
        glass_list: List[float] = None,
        illu_list: List[float] = None,
        mask_list: List[float] = None,
        noise_list: List[float] = None,
        pose_list: List[float] = None,
        score_list: List[float] = None,
    ):
        # 1
        self.blur_list = blur_list
        # 1
        self.fnf_list = fnf_list
        # 1
        self.glass_list = glass_list
        # 1
        self.illu_list = illu_list
        # 1
        self.mask_list = mask_list
        # 1
        self.noise_list = noise_list
        # 1
        self.pose_list = pose_list
        # 1
        self.score_list = score_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.blur_list is not None:
            result['BlurList'] = self.blur_list
        if self.fnf_list is not None:
            result['FnfList'] = self.fnf_list
        if self.glass_list is not None:
            result['GlassList'] = self.glass_list
        if self.illu_list is not None:
            result['IlluList'] = self.illu_list
        if self.mask_list is not None:
            result['MaskList'] = self.mask_list
        if self.noise_list is not None:
            result['NoiseList'] = self.noise_list
        if self.pose_list is not None:
            result['PoseList'] = self.pose_list
        if self.score_list is not None:
            result['ScoreList'] = self.score_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BlurList') is not None:
            self.blur_list = m.get('BlurList')
        if m.get('FnfList') is not None:
            self.fnf_list = m.get('FnfList')
        if m.get('GlassList') is not None:
            self.glass_list = m.get('GlassList')
        if m.get('IlluList') is not None:
            self.illu_list = m.get('IlluList')
        if m.get('MaskList') is not None:
            self.mask_list = m.get('MaskList')
        if m.get('NoiseList') is not None:
            self.noise_list = m.get('NoiseList')
        if m.get('PoseList') is not None:
            self.pose_list = m.get('PoseList')
        if m.get('ScoreList') is not None:
            self.score_list = m.get('ScoreList')
        return self


class RecognizeFaceResponseBodyData(TeaModel):
    def __init__(
        self,
        age_list: List[int] = None,
        beauty_list: List[float] = None,
        dense_feature_length: int = None,
        dense_features: List[str] = None,
        expressions: List[int] = None,
        face_count: int = None,
        face_probability_list: List[float] = None,
        face_rectangles: List[int] = None,
        gender_list: List[int] = None,
        glasses: List[int] = None,
        hat_list: List[int] = None,
        landmark_count: int = None,
        landmarks: List[float] = None,
        masks: List[int] = None,
        pose_list: List[float] = None,
        pupils: List[float] = None,
        qualities: RecognizeFaceResponseBodyDataQualities = None,
    ):
        # 1
        self.age_list = age_list
        # 1
        self.beauty_list = beauty_list
        self.dense_feature_length = dense_feature_length
        # 1
        self.dense_features = dense_features
        # 1
        self.expressions = expressions
        self.face_count = face_count
        # 1
        self.face_probability_list = face_probability_list
        # 1
        self.face_rectangles = face_rectangles
        # 1
        self.gender_list = gender_list
        # 1
        self.glasses = glasses
        # 1
        self.hat_list = hat_list
        self.landmark_count = landmark_count
        # 1
        self.landmarks = landmarks
        # 1
        self.masks = masks
        # 1
        self.pose_list = pose_list
        # 1
        self.pupils = pupils
        self.qualities = qualities

    def validate(self):
        if self.qualities:
            self.qualities.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.age_list is not None:
            result['AgeList'] = self.age_list
        if self.beauty_list is not None:
            result['BeautyList'] = self.beauty_list
        if self.dense_feature_length is not None:
            result['DenseFeatureLength'] = self.dense_feature_length
        if self.dense_features is not None:
            result['DenseFeatures'] = self.dense_features
        if self.expressions is not None:
            result['Expressions'] = self.expressions
        if self.face_count is not None:
            result['FaceCount'] = self.face_count
        if self.face_probability_list is not None:
            result['FaceProbabilityList'] = self.face_probability_list
        if self.face_rectangles is not None:
            result['FaceRectangles'] = self.face_rectangles
        if self.gender_list is not None:
            result['GenderList'] = self.gender_list
        if self.glasses is not None:
            result['Glasses'] = self.glasses
        if self.hat_list is not None:
            result['HatList'] = self.hat_list
        if self.landmark_count is not None:
            result['LandmarkCount'] = self.landmark_count
        if self.landmarks is not None:
            result['Landmarks'] = self.landmarks
        if self.masks is not None:
            result['Masks'] = self.masks
        if self.pose_list is not None:
            result['PoseList'] = self.pose_list
        if self.pupils is not None:
            result['Pupils'] = self.pupils
        if self.qualities is not None:
            result['Qualities'] = self.qualities.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgeList') is not None:
            self.age_list = m.get('AgeList')
        if m.get('BeautyList') is not None:
            self.beauty_list = m.get('BeautyList')
        if m.get('DenseFeatureLength') is not None:
            self.dense_feature_length = m.get('DenseFeatureLength')
        if m.get('DenseFeatures') is not None:
            self.dense_features = m.get('DenseFeatures')
        if m.get('Expressions') is not None:
            self.expressions = m.get('Expressions')
        if m.get('FaceCount') is not None:
            self.face_count = m.get('FaceCount')
        if m.get('FaceProbabilityList') is not None:
            self.face_probability_list = m.get('FaceProbabilityList')
        if m.get('FaceRectangles') is not None:
            self.face_rectangles = m.get('FaceRectangles')
        if m.get('GenderList') is not None:
            self.gender_list = m.get('GenderList')
        if m.get('Glasses') is not None:
            self.glasses = m.get('Glasses')
        if m.get('HatList') is not None:
            self.hat_list = m.get('HatList')
        if m.get('LandmarkCount') is not None:
            self.landmark_count = m.get('LandmarkCount')
        if m.get('Landmarks') is not None:
            self.landmarks = m.get('Landmarks')
        if m.get('Masks') is not None:
            self.masks = m.get('Masks')
        if m.get('PoseList') is not None:
            self.pose_list = m.get('PoseList')
        if m.get('Pupils') is not None:
            self.pupils = m.get('Pupils')
        if m.get('Qualities') is not None:
            temp_model = RecognizeFaceResponseBodyDataQualities()
            self.qualities = temp_model.from_map(m['Qualities'])
        return self


class RecognizeFaceResponseBody(TeaModel):
    def __init__(
        self,
        data: RecognizeFaceResponseBodyData = None,
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
            temp_model = RecognizeFaceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RecognizeFaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RecognizeFaceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = RecognizeFaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizePublicFaceRequestTask(TeaModel):
    def __init__(
        self,
        image_data: str = None,
        image_url: str = None,
    ):
        self.image_data = image_data
        self.image_url = image_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_data is not None:
            result['ImageData'] = self.image_data
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageData') is not None:
            self.image_data = m.get('ImageData')
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        return self


class RecognizePublicFaceRequest(TeaModel):
    def __init__(
        self,
        task: List[RecognizePublicFaceRequestTask] = None,
    ):
        # 1
        self.task = task

    def validate(self):
        if self.task:
            for k in self.task:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Task'] = []
        if self.task is not None:
            for k in self.task:
                result['Task'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.task = []
        if m.get('Task') is not None:
            for k in m.get('Task'):
                temp_model = RecognizePublicFaceRequestTask()
                self.task.append(temp_model.from_map(k))
        return self


class RecognizePublicFaceAdvanceRequestTask(TeaModel):
    def __init__(
        self,
        image_data: str = None,
        image_urlobject: BinaryIO = None,
    ):
        self.image_data = image_data
        self.image_urlobject = image_urlobject

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_data is not None:
            result['ImageData'] = self.image_data
        if self.image_urlobject is not None:
            result['ImageURL'] = self.image_urlobject
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageData') is not None:
            self.image_data = m.get('ImageData')
        if m.get('ImageURL') is not None:
            self.image_urlobject = m.get('ImageURL')
        return self


class RecognizePublicFaceAdvanceRequest(TeaModel):
    def __init__(
        self,
        task: List[RecognizePublicFaceAdvanceRequestTask] = None,
    ):
        # 1
        self.task = task

    def validate(self):
        if self.task:
            for k in self.task:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Task'] = []
        if self.task is not None:
            for k in self.task:
                result['Task'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.task = []
        if m.get('Task') is not None:
            for k in m.get('Task'):
                temp_model = RecognizePublicFaceAdvanceRequestTask()
                self.task.append(temp_model.from_map(k))
        return self


class RecognizePublicFaceResponseBodyDataElementsResultsSubResultsFaces(TeaModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
        rate: float = None,
    ):
        self.id = id
        self.name = name
        self.rate = rate

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.rate is not None:
            result['Rate'] = self.rate
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Rate') is not None:
            self.rate = m.get('Rate')
        return self


class RecognizePublicFaceResponseBodyDataElementsResultsSubResults(TeaModel):
    def __init__(
        self,
        faces: List[RecognizePublicFaceResponseBodyDataElementsResultsSubResultsFaces] = None,
        h: float = None,
        w: float = None,
        x: float = None,
        y: float = None,
    ):
        self.faces = faces
        self.h = h
        self.w = w
        self.x = x
        self.y = y

    def validate(self):
        if self.faces:
            for k in self.faces:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Faces'] = []
        if self.faces is not None:
            for k in self.faces:
                result['Faces'].append(k.to_map() if k else None)
        if self.h is not None:
            result['H'] = self.h
        if self.w is not None:
            result['W'] = self.w
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.faces = []
        if m.get('Faces') is not None:
            for k in m.get('Faces'):
                temp_model = RecognizePublicFaceResponseBodyDataElementsResultsSubResultsFaces()
                self.faces.append(temp_model.from_map(k))
        if m.get('H') is not None:
            self.h = m.get('H')
        if m.get('W') is not None:
            self.w = m.get('W')
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        return self


class RecognizePublicFaceResponseBodyDataElementsResults(TeaModel):
    def __init__(
        self,
        label: str = None,
        rate: float = None,
        sub_results: List[RecognizePublicFaceResponseBodyDataElementsResultsSubResults] = None,
        suggestion: str = None,
    ):
        self.label = label
        self.rate = rate
        self.sub_results = sub_results
        self.suggestion = suggestion

    def validate(self):
        if self.sub_results:
            for k in self.sub_results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label is not None:
            result['Label'] = self.label
        if self.rate is not None:
            result['Rate'] = self.rate
        result['SubResults'] = []
        if self.sub_results is not None:
            for k in self.sub_results:
                result['SubResults'].append(k.to_map() if k else None)
        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Rate') is not None:
            self.rate = m.get('Rate')
        self.sub_results = []
        if m.get('SubResults') is not None:
            for k in m.get('SubResults'):
                temp_model = RecognizePublicFaceResponseBodyDataElementsResultsSubResults()
                self.sub_results.append(temp_model.from_map(k))
        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')
        return self


class RecognizePublicFaceResponseBodyDataElements(TeaModel):
    def __init__(
        self,
        image_url: str = None,
        results: List[RecognizePublicFaceResponseBodyDataElementsResults] = None,
        task_id: str = None,
    ):
        self.image_url = image_url
        self.results = results
        self.task_id = task_id

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
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        self.results = []
        if m.get('Results') is not None:
            for k in m.get('Results'):
                temp_model = RecognizePublicFaceResponseBodyDataElementsResults()
                self.results.append(temp_model.from_map(k))
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class RecognizePublicFaceResponseBodyData(TeaModel):
    def __init__(
        self,
        elements: List[RecognizePublicFaceResponseBodyDataElements] = None,
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
                temp_model = RecognizePublicFaceResponseBodyDataElements()
                self.elements.append(temp_model.from_map(k))
        return self


class RecognizePublicFaceResponseBody(TeaModel):
    def __init__(
        self,
        data: RecognizePublicFaceResponseBodyData = None,
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
            temp_model = RecognizePublicFaceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RecognizePublicFaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RecognizePublicFaceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = RecognizePublicFaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RetouchSkinRequest(TeaModel):
    def __init__(
        self,
        image_url: str = None,
        retouch_degree: float = None,
        whitening_degree: float = None,
    ):
        # This parameter is required.
        self.image_url = image_url
        self.retouch_degree = retouch_degree
        self.whitening_degree = whitening_degree

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        if self.retouch_degree is not None:
            result['RetouchDegree'] = self.retouch_degree
        if self.whitening_degree is not None:
            result['WhiteningDegree'] = self.whitening_degree
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        if m.get('RetouchDegree') is not None:
            self.retouch_degree = m.get('RetouchDegree')
        if m.get('WhiteningDegree') is not None:
            self.whitening_degree = m.get('WhiteningDegree')
        return self


class RetouchSkinAdvanceRequest(TeaModel):
    def __init__(
        self,
        image_urlobject: BinaryIO = None,
        retouch_degree: float = None,
        whitening_degree: float = None,
    ):
        # This parameter is required.
        self.image_urlobject = image_urlobject
        self.retouch_degree = retouch_degree
        self.whitening_degree = whitening_degree

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_urlobject is not None:
            result['ImageURL'] = self.image_urlobject
        if self.retouch_degree is not None:
            result['RetouchDegree'] = self.retouch_degree
        if self.whitening_degree is not None:
            result['WhiteningDegree'] = self.whitening_degree
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_urlobject = m.get('ImageURL')
        if m.get('RetouchDegree') is not None:
            self.retouch_degree = m.get('RetouchDegree')
        if m.get('WhiteningDegree') is not None:
            self.whitening_degree = m.get('WhiteningDegree')
        return self


class RetouchSkinResponseBodyData(TeaModel):
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


class RetouchSkinResponseBody(TeaModel):
    def __init__(
        self,
        data: RetouchSkinResponseBodyData = None,
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
            temp_model = RetouchSkinResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RetouchSkinResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RetouchSkinResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = RetouchSkinResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchFaceRequest(TeaModel):
    def __init__(
        self,
        db_name: str = None,
        db_names: str = None,
        image_url: str = None,
        limit: int = None,
        max_face_num: int = None,
        quality_score_threshold: float = None,
    ):
        self.db_name = db_name
        self.db_names = db_names
        # This parameter is required.
        self.image_url = image_url
        # This parameter is required.
        self.limit = limit
        self.max_face_num = max_face_num
        self.quality_score_threshold = quality_score_threshold

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.db_names is not None:
            result['DbNames'] = self.db_names
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.max_face_num is not None:
            result['MaxFaceNum'] = self.max_face_num
        if self.quality_score_threshold is not None:
            result['QualityScoreThreshold'] = self.quality_score_threshold
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('DbNames') is not None:
            self.db_names = m.get('DbNames')
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('MaxFaceNum') is not None:
            self.max_face_num = m.get('MaxFaceNum')
        if m.get('QualityScoreThreshold') is not None:
            self.quality_score_threshold = m.get('QualityScoreThreshold')
        return self


class SearchFaceAdvanceRequest(TeaModel):
    def __init__(
        self,
        db_name: str = None,
        db_names: str = None,
        image_url_object: BinaryIO = None,
        limit: int = None,
        max_face_num: int = None,
        quality_score_threshold: float = None,
    ):
        self.db_name = db_name
        self.db_names = db_names
        # This parameter is required.
        self.image_url_object = image_url_object
        # This parameter is required.
        self.limit = limit
        self.max_face_num = max_face_num
        self.quality_score_threshold = quality_score_threshold

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.db_names is not None:
            result['DbNames'] = self.db_names
        if self.image_url_object is not None:
            result['ImageUrl'] = self.image_url_object
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.max_face_num is not None:
            result['MaxFaceNum'] = self.max_face_num
        if self.quality_score_threshold is not None:
            result['QualityScoreThreshold'] = self.quality_score_threshold
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('DbNames') is not None:
            self.db_names = m.get('DbNames')
        if m.get('ImageUrl') is not None:
            self.image_url_object = m.get('ImageUrl')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('MaxFaceNum') is not None:
            self.max_face_num = m.get('MaxFaceNum')
        if m.get('QualityScoreThreshold') is not None:
            self.quality_score_threshold = m.get('QualityScoreThreshold')
        return self


class SearchFaceResponseBodyDataMatchListFaceItems(TeaModel):
    def __init__(
        self,
        confidence: float = None,
        db_name: str = None,
        entity_id: str = None,
        extra_data: str = None,
        face_id: str = None,
        score: float = None,
    ):
        self.confidence = confidence
        self.db_name = db_name
        self.entity_id = entity_id
        self.extra_data = extra_data
        self.face_id = face_id
        self.score = score

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.confidence is not None:
            result['Confidence'] = self.confidence
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.extra_data is not None:
            result['ExtraData'] = self.extra_data
        if self.face_id is not None:
            result['FaceId'] = self.face_id
        if self.score is not None:
            result['Score'] = self.score
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('ExtraData') is not None:
            self.extra_data = m.get('ExtraData')
        if m.get('FaceId') is not None:
            self.face_id = m.get('FaceId')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        return self


class SearchFaceResponseBodyDataMatchListLocation(TeaModel):
    def __init__(
        self,
        height: int = None,
        width: int = None,
        x: int = None,
        y: int = None,
    ):
        self.height = height
        self.width = width
        self.x = x
        self.y = y

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.height is not None:
            result['Height'] = self.height
        if self.width is not None:
            result['Width'] = self.width
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        return self


class SearchFaceResponseBodyDataMatchList(TeaModel):
    def __init__(
        self,
        face_items: List[SearchFaceResponseBodyDataMatchListFaceItems] = None,
        location: SearchFaceResponseBodyDataMatchListLocation = None,
        qualitie_score: float = None,
    ):
        self.face_items = face_items
        self.location = location
        self.qualitie_score = qualitie_score

    def validate(self):
        if self.face_items:
            for k in self.face_items:
                if k:
                    k.validate()
        if self.location:
            self.location.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FaceItems'] = []
        if self.face_items is not None:
            for k in self.face_items:
                result['FaceItems'].append(k.to_map() if k else None)
        if self.location is not None:
            result['Location'] = self.location.to_map()
        if self.qualitie_score is not None:
            result['QualitieScore'] = self.qualitie_score
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.face_items = []
        if m.get('FaceItems') is not None:
            for k in m.get('FaceItems'):
                temp_model = SearchFaceResponseBodyDataMatchListFaceItems()
                self.face_items.append(temp_model.from_map(k))
        if m.get('Location') is not None:
            temp_model = SearchFaceResponseBodyDataMatchListLocation()
            self.location = temp_model.from_map(m['Location'])
        if m.get('QualitieScore') is not None:
            self.qualitie_score = m.get('QualitieScore')
        return self


class SearchFaceResponseBodyData(TeaModel):
    def __init__(
        self,
        match_list: List[SearchFaceResponseBodyDataMatchList] = None,
    ):
        self.match_list = match_list

    def validate(self):
        if self.match_list:
            for k in self.match_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['MatchList'] = []
        if self.match_list is not None:
            for k in self.match_list:
                result['MatchList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.match_list = []
        if m.get('MatchList') is not None:
            for k in m.get('MatchList'):
                temp_model = SearchFaceResponseBodyDataMatchList()
                self.match_list.append(temp_model.from_map(k))
        return self


class SearchFaceResponseBody(TeaModel):
    def __init__(
        self,
        data: SearchFaceResponseBodyData = None,
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
            temp_model = SearchFaceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SearchFaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SearchFaceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = SearchFaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateFaceEntityRequest(TeaModel):
    def __init__(
        self,
        db_name: str = None,
        entity_id: str = None,
        labels: str = None,
    ):
        # This parameter is required.
        self.db_name = db_name
        # This parameter is required.
        self.entity_id = entity_id
        self.labels = labels

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.labels is not None:
            result['Labels'] = self.labels
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        return self


class UpdateFaceEntityResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateFaceEntityResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateFaceEntityResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = UpdateFaceEntityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


