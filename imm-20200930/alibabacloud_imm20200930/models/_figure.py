# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_imm20200930 import models as main_models
from darabonba.model import DaraModel

class Figure(DaraModel):
    def __init__(
        self,
        age: int = None,
        age_sd: float = None,
        attractive: float = None,
        beard: str = None,
        beard_confidence: float = None,
        boundary: main_models.Boundary = None,
        emotion: str = None,
        emotion_confidence: float = None,
        face_quality: float = None,
        figure_cluster_confidence: float = None,
        figure_cluster_id: str = None,
        figure_confidence: float = None,
        figure_id: str = None,
        figure_type: str = None,
        gender: str = None,
        gender_confidence: float = None,
        glasses: str = None,
        glasses_confidence: float = None,
        hat: str = None,
        hat_confidence: float = None,
        head_pose: main_models.HeadPose = None,
        mask: str = None,
        mask_confidence: float = None,
        mouth: str = None,
        mouth_confidence: float = None,
        sharpness: float = None,
    ):
        # The age.
        self.age = age
        # The age standard deviation.
        self.age_sd = age_sd
        # The face attractiveness score. A higher score indicates greater attractiveness. Valid values: 0 to 1.
        self.attractive = attractive
        # Indicates whether the person has a beard.
        self.beard = beard
        # The confidence score for whether the person has a beard. Valid values: 0 (lowest confidence) to 1 (highest confidence).
        self.beard_confidence = beard_confidence
        # The face boundary information.
        self.boundary = boundary
        # The emotion.
        self.emotion = emotion
        # The emotion confidence score. Valid values: 0 (lowest confidence) to 1 (highest confidence).
        self.emotion_confidence = emotion_confidence
        # The face quality score, which evaluates whether the image quality is suitable for face recognition. A higher score indicates better quality. Valid values: 0 to 1.
        self.face_quality = face_quality
        # The clustering confidence score. Valid values: 0 (lowest confidence) to 1 (highest confidence).
        self.figure_cluster_confidence = figure_cluster_confidence
        # The figure cluster ID. The following reserved special cluster ID names are included:
        # 
        # - figure-cluster-id-independent: The face does not currently belong to any suitable group. After new images are added to the dataset and face clustering is performed, the face may be assigned to a group.
        # 
        # - figure-cluster-id-unavailable: The face has not been clustered yet. This means that after new images were added to the dataset, face clustering has not been performed.
        self.figure_cluster_id = figure_cluster_id
        # The confidence score of the figure object. Valid values: 0 (lowest confidence) to 1 (highest confidence).
        self.figure_confidence = figure_confidence
        # The ID of the figure object.
        self.figure_id = figure_id
        # The figure type.
        self.figure_type = figure_type
        # The gender.
        self.gender = gender
        # The gender confidence score. Valid values: 0 (lowest confidence) to 1 (highest confidence).
        self.gender_confidence = gender_confidence
        # Indicates whether the person is wearing glasses.
        self.glasses = glasses
        # The confidence score for whether the person is wearing glasses. Valid values: 0 (lowest confidence) to 1 (highest confidence).
        self.glasses_confidence = glasses_confidence
        # Indicates whether the person is wearing a hat.
        self.hat = hat
        # The confidence score for whether the person is wearing a hat. Valid values: 0 (lowest confidence) to 1 (highest confidence).
        self.hat_confidence = hat_confidence
        # The head pose information.
        self.head_pose = head_pose
        # Indicates whether the person is wearing a mask.
        self.mask = mask
        # The confidence score for whether the person is wearing a mask. Valid values: 0 (lowest confidence) to 1 (highest confidence).
        self.mask_confidence = mask_confidence
        # Indicates whether the mouth is open.
        self.mouth = mouth
        # The confidence score for whether the mouth is open. Valid values: 0 (lowest confidence) to 1 (highest confidence).
        self.mouth_confidence = mouth_confidence
        # The sharpness score. A higher score indicates a clearer face. Valid values: 0 to 1.
        self.sharpness = sharpness

    def validate(self):
        if self.boundary:
            self.boundary.validate()
        if self.head_pose:
            self.head_pose.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.age is not None:
            result['Age'] = self.age

        if self.age_sd is not None:
            result['AgeSD'] = self.age_sd

        if self.attractive is not None:
            result['Attractive'] = self.attractive

        if self.beard is not None:
            result['Beard'] = self.beard

        if self.beard_confidence is not None:
            result['BeardConfidence'] = self.beard_confidence

        if self.boundary is not None:
            result['Boundary'] = self.boundary.to_map()

        if self.emotion is not None:
            result['Emotion'] = self.emotion

        if self.emotion_confidence is not None:
            result['EmotionConfidence'] = self.emotion_confidence

        if self.face_quality is not None:
            result['FaceQuality'] = self.face_quality

        if self.figure_cluster_confidence is not None:
            result['FigureClusterConfidence'] = self.figure_cluster_confidence

        if self.figure_cluster_id is not None:
            result['FigureClusterId'] = self.figure_cluster_id

        if self.figure_confidence is not None:
            result['FigureConfidence'] = self.figure_confidence

        if self.figure_id is not None:
            result['FigureId'] = self.figure_id

        if self.figure_type is not None:
            result['FigureType'] = self.figure_type

        if self.gender is not None:
            result['Gender'] = self.gender

        if self.gender_confidence is not None:
            result['GenderConfidence'] = self.gender_confidence

        if self.glasses is not None:
            result['Glasses'] = self.glasses

        if self.glasses_confidence is not None:
            result['GlassesConfidence'] = self.glasses_confidence

        if self.hat is not None:
            result['Hat'] = self.hat

        if self.hat_confidence is not None:
            result['HatConfidence'] = self.hat_confidence

        if self.head_pose is not None:
            result['HeadPose'] = self.head_pose.to_map()

        if self.mask is not None:
            result['Mask'] = self.mask

        if self.mask_confidence is not None:
            result['MaskConfidence'] = self.mask_confidence

        if self.mouth is not None:
            result['Mouth'] = self.mouth

        if self.mouth_confidence is not None:
            result['MouthConfidence'] = self.mouth_confidence

        if self.sharpness is not None:
            result['Sharpness'] = self.sharpness

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Age') is not None:
            self.age = m.get('Age')

        if m.get('AgeSD') is not None:
            self.age_sd = m.get('AgeSD')

        if m.get('Attractive') is not None:
            self.attractive = m.get('Attractive')

        if m.get('Beard') is not None:
            self.beard = m.get('Beard')

        if m.get('BeardConfidence') is not None:
            self.beard_confidence = m.get('BeardConfidence')

        if m.get('Boundary') is not None:
            temp_model = main_models.Boundary()
            self.boundary = temp_model.from_map(m.get('Boundary'))

        if m.get('Emotion') is not None:
            self.emotion = m.get('Emotion')

        if m.get('EmotionConfidence') is not None:
            self.emotion_confidence = m.get('EmotionConfidence')

        if m.get('FaceQuality') is not None:
            self.face_quality = m.get('FaceQuality')

        if m.get('FigureClusterConfidence') is not None:
            self.figure_cluster_confidence = m.get('FigureClusterConfidence')

        if m.get('FigureClusterId') is not None:
            self.figure_cluster_id = m.get('FigureClusterId')

        if m.get('FigureConfidence') is not None:
            self.figure_confidence = m.get('FigureConfidence')

        if m.get('FigureId') is not None:
            self.figure_id = m.get('FigureId')

        if m.get('FigureType') is not None:
            self.figure_type = m.get('FigureType')

        if m.get('Gender') is not None:
            self.gender = m.get('Gender')

        if m.get('GenderConfidence') is not None:
            self.gender_confidence = m.get('GenderConfidence')

        if m.get('Glasses') is not None:
            self.glasses = m.get('Glasses')

        if m.get('GlassesConfidence') is not None:
            self.glasses_confidence = m.get('GlassesConfidence')

        if m.get('Hat') is not None:
            self.hat = m.get('Hat')

        if m.get('HatConfidence') is not None:
            self.hat_confidence = m.get('HatConfidence')

        if m.get('HeadPose') is not None:
            temp_model = main_models.HeadPose()
            self.head_pose = temp_model.from_map(m.get('HeadPose'))

        if m.get('Mask') is not None:
            self.mask = m.get('Mask')

        if m.get('MaskConfidence') is not None:
            self.mask_confidence = m.get('MaskConfidence')

        if m.get('Mouth') is not None:
            self.mouth = m.get('Mouth')

        if m.get('MouthConfidence') is not None:
            self.mouth_confidence = m.get('MouthConfidence')

        if m.get('Sharpness') is not None:
            self.sharpness = m.get('Sharpness')

        return self

