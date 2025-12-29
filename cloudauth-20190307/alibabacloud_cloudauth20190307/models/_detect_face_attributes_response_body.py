# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudauth20190307 import models as main_models
from darabonba.model import DaraModel

class DetectFaceAttributesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.DetectFaceAttributesResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # HTTP status code.
        self.code = code
        # Returned data.
        self.data = data
        # Error code.
        self.message = message
        # ID of this request.
        self.request_id = request_id
        # Whether the response was successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.DetectFaceAttributesResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DetectFaceAttributesResponseBodyData(DaraModel):
    def __init__(
        self,
        face_infos: main_models.DetectFaceAttributesResponseBodyDataFaceInfos = None,
        img_height: int = None,
        img_width: int = None,
    ):
        # Face detection results.
        self.face_infos = face_infos
        # Original image height, in pixels.
        self.img_height = img_height
        # Original image width, in pixels.
        self.img_width = img_width

    def validate(self):
        if self.face_infos:
            self.face_infos.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.face_infos is not None:
            result['FaceInfos'] = self.face_infos.to_map()

        if self.img_height is not None:
            result['ImgHeight'] = self.img_height

        if self.img_width is not None:
            result['ImgWidth'] = self.img_width

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FaceInfos') is not None:
            temp_model = main_models.DetectFaceAttributesResponseBodyDataFaceInfos()
            self.face_infos = temp_model.from_map(m.get('FaceInfos'))

        if m.get('ImgHeight') is not None:
            self.img_height = m.get('ImgHeight')

        if m.get('ImgWidth') is not None:
            self.img_width = m.get('ImgWidth')

        return self

class DetectFaceAttributesResponseBodyDataFaceInfos(DaraModel):
    def __init__(
        self,
        face_attributes_detect_info: List[main_models.DetectFaceAttributesResponseBodyDataFaceInfosFaceAttributesDetectInfo] = None,
    ):
        self.face_attributes_detect_info = face_attributes_detect_info

    def validate(self):
        if self.face_attributes_detect_info:
            for v1 in self.face_attributes_detect_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['FaceAttributesDetectInfo'] = []
        if self.face_attributes_detect_info is not None:
            for k1 in self.face_attributes_detect_info:
                result['FaceAttributesDetectInfo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.face_attributes_detect_info = []
        if m.get('FaceAttributesDetectInfo') is not None:
            for k1 in m.get('FaceAttributesDetectInfo'):
                temp_model = main_models.DetectFaceAttributesResponseBodyDataFaceInfosFaceAttributesDetectInfo()
                self.face_attributes_detect_info.append(temp_model.from_map(k1))

        return self

class DetectFaceAttributesResponseBodyDataFaceInfosFaceAttributesDetectInfo(DaraModel):
    def __init__(
        self,
        face_attributes: main_models.DetectFaceAttributesResponseBodyDataFaceInfosFaceAttributesDetectInfoFaceAttributes = None,
        face_rect: main_models.DetectFaceAttributesResponseBodyDataFaceInfosFaceAttributesDetectInfoFaceRect = None,
    ):
        # Face attributes.
        self.face_attributes = face_attributes
        # Position of the face in the original image.
        self.face_rect = face_rect

    def validate(self):
        if self.face_attributes:
            self.face_attributes.validate()
        if self.face_rect:
            self.face_rect.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.face_attributes is not None:
            result['FaceAttributes'] = self.face_attributes.to_map()

        if self.face_rect is not None:
            result['FaceRect'] = self.face_rect.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FaceAttributes') is not None:
            temp_model = main_models.DetectFaceAttributesResponseBodyDataFaceInfosFaceAttributesDetectInfoFaceAttributes()
            self.face_attributes = temp_model.from_map(m.get('FaceAttributes'))

        if m.get('FaceRect') is not None:
            temp_model = main_models.DetectFaceAttributesResponseBodyDataFaceInfosFaceAttributesDetectInfoFaceRect()
            self.face_rect = temp_model.from_map(m.get('FaceRect'))

        return self

class DetectFaceAttributesResponseBodyDataFaceInfosFaceAttributesDetectInfoFaceRect(DaraModel):
    def __init__(
        self,
        height: int = None,
        left: int = None,
        top: int = None,
        width: int = None,
    ):
        # Height of the face rectangle.
        self.height = height
        # Distance from the top-left corner of the face rectangle to the left edge of the original image, in pixels.
        self.left = left
        # Distance from the top-left corner of the face rectangle to the top edge of the original image, in pixels.
        self.top = top
        # Width of the face rectangle.
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

class DetectFaceAttributesResponseBodyDataFaceInfosFaceAttributesDetectInfoFaceAttributes(DaraModel):
    def __init__(
        self,
        blur: float = None,
        facequal: float = None,
        facetype: str = None,
        glasses: str = None,
        headpose: main_models.DetectFaceAttributesResponseBodyDataFaceInfosFaceAttributesDetectInfoFaceAttributesHeadpose = None,
        integrity: int = None,
        respirator: str = None,
        smiling: main_models.DetectFaceAttributesResponseBodyDataFaceInfosFaceAttributesDetectInfoFaceAttributesSmiling = None,
    ):
        # Face blur level, with higher values indicating more blurriness. Typically, a value ≥2.0 is considered quite blurry. It is recommended to adjust based on actual business data testing.
        self.blur = blur
        # A score ranging from 0 to 100. The higher the score, the better the quality. It is recommended to consider a score of 50 or above as acceptable quality.
        self.facequal = facequal
        # Whether it is a human face. Values:
        # 
        # - **None**: Not a human face
        # - **Face**: Human face
        # - **Profile**: Profile (head turned left or right by more than 30°)
        # 
        # > If no face is detected, the `faceInfos` in the response will be empty; here, `None` means that a face was detected but is considered to be a cartoon, pet, etc.
        self.facetype = facetype
        # Whether wearing glasses. Values:
        # 
        # - **None**: Not wearing glasses
        # - **Wear**: Wearing regular glasses
        # - **Sunglass**: Wearing sunglasses
        self.glasses = glasses
        # Face pose.
        self.headpose = headpose
        # A score ranging from 0 to 100. The higher the score, the more complete the face. It is recommended to consider a score of 70 or above as acceptable completeness.
        self.integrity = integrity
        # Whether wearing a mask. Values:
        # 
        # - Wear: Wearing a mask.
        # - None: Not wearing a mask.
        self.respirator = respirator
        # Whether smiling.
        self.smiling = smiling

    def validate(self):
        if self.headpose:
            self.headpose.validate()
        if self.smiling:
            self.smiling.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.blur is not None:
            result['Blur'] = self.blur

        if self.facequal is not None:
            result['Facequal'] = self.facequal

        if self.facetype is not None:
            result['Facetype'] = self.facetype

        if self.glasses is not None:
            result['Glasses'] = self.glasses

        if self.headpose is not None:
            result['Headpose'] = self.headpose.to_map()

        if self.integrity is not None:
            result['Integrity'] = self.integrity

        if self.respirator is not None:
            result['Respirator'] = self.respirator

        if self.smiling is not None:
            result['Smiling'] = self.smiling.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Blur') is not None:
            self.blur = m.get('Blur')

        if m.get('Facequal') is not None:
            self.facequal = m.get('Facequal')

        if m.get('Facetype') is not None:
            self.facetype = m.get('Facetype')

        if m.get('Glasses') is not None:
            self.glasses = m.get('Glasses')

        if m.get('Headpose') is not None:
            temp_model = main_models.DetectFaceAttributesResponseBodyDataFaceInfosFaceAttributesDetectInfoFaceAttributesHeadpose()
            self.headpose = temp_model.from_map(m.get('Headpose'))

        if m.get('Integrity') is not None:
            self.integrity = m.get('Integrity')

        if m.get('Respirator') is not None:
            self.respirator = m.get('Respirator')

        if m.get('Smiling') is not None:
            temp_model = main_models.DetectFaceAttributesResponseBodyDataFaceInfosFaceAttributesDetectInfoFaceAttributesSmiling()
            self.smiling = temp_model.from_map(m.get('Smiling'))

        return self

class DetectFaceAttributesResponseBodyDataFaceInfosFaceAttributesDetectInfoFaceAttributesSmiling(DaraModel):
    def __init__(
        self,
        threshold: float = None,
        value: float = None,
    ):
        # Smile threshold.
        self.threshold = threshold
        # Smile score.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.threshold is not None:
            result['Threshold'] = self.threshold

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class DetectFaceAttributesResponseBodyDataFaceInfosFaceAttributesDetectInfoFaceAttributesHeadpose(DaraModel):
    def __init__(
        self,
        pitch_angle: float = None,
        roll_angle: float = None,
        yaw_angle: float = None,
    ):
        # Pitch angle, in degrees.
        self.pitch_angle = pitch_angle
        # Roll angle, in degrees.
        self.roll_angle = roll_angle
        # Yaw angle, in degrees.
        self.yaw_angle = yaw_angle

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.pitch_angle is not None:
            result['PitchAngle'] = self.pitch_angle

        if self.roll_angle is not None:
            result['RollAngle'] = self.roll_angle

        if self.yaw_angle is not None:
            result['YawAngle'] = self.yaw_angle

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PitchAngle') is not None:
            self.pitch_angle = m.get('PitchAngle')

        if m.get('RollAngle') is not None:
            self.roll_angle = m.get('RollAngle')

        if m.get('YawAngle') is not None:
            self.yaw_angle = m.get('YawAngle')

        return self

