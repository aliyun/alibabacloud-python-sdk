# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_imm20200930 import models as main_models
from darabonba.model import DaraModel

class Spec(DaraModel):
    def __init__(
        self,
        backbone: main_models.CustomParams = None,
        class_num: int = None,
        head: main_models.CustomParams = None,
        input_channel: int = None,
        loss: main_models.CustomParams = None,
        name: str = None,
        neck: main_models.CustomParams = None,
        num_landmarks: int = None,
        pretrained_path: str = None,
    ):
        # The custom parameters for model training.
        self.backbone = backbone
        # The number of output classes of the last layer.
        self.class_num = class_num
        # The custom parameters for model training.
        self.head = head
        # 3
        self.input_channel = input_channel
        # The custom parameters for model training.
        self.loss = loss
        # The name of the model. The available model names vary with the model category.
        # 
        # This parameter is required.
        self.name = name
        # The custom parameters for model training.
        self.neck = neck
        # The number of face landmarks. This parameter is required for face detection. In most cases, you can set the parameter to 5.
        self.num_landmarks = num_landmarks
        # The path to the pretrained model.
        self.pretrained_path = pretrained_path

    def validate(self):
        if self.backbone:
            self.backbone.validate()
        if self.head:
            self.head.validate()
        if self.loss:
            self.loss.validate()
        if self.neck:
            self.neck.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backbone is not None:
            result['Backbone'] = self.backbone.to_map()

        if self.class_num is not None:
            result['ClassNum'] = self.class_num

        if self.head is not None:
            result['Head'] = self.head.to_map()

        if self.input_channel is not None:
            result['InputChannel'] = self.input_channel

        if self.loss is not None:
            result['Loss'] = self.loss.to_map()

        if self.name is not None:
            result['Name'] = self.name

        if self.neck is not None:
            result['Neck'] = self.neck.to_map()

        if self.num_landmarks is not None:
            result['NumLandmarks'] = self.num_landmarks

        if self.pretrained_path is not None:
            result['PretrainedPath'] = self.pretrained_path

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Backbone') is not None:
            temp_model = main_models.CustomParams()
            self.backbone = temp_model.from_map(m.get('Backbone'))

        if m.get('ClassNum') is not None:
            self.class_num = m.get('ClassNum')

        if m.get('Head') is not None:
            temp_model = main_models.CustomParams()
            self.head = temp_model.from_map(m.get('Head'))

        if m.get('InputChannel') is not None:
            self.input_channel = m.get('InputChannel')

        if m.get('Loss') is not None:
            temp_model = main_models.CustomParams()
            self.loss = temp_model.from_map(m.get('Loss'))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Neck') is not None:
            temp_model = main_models.CustomParams()
            self.neck = temp_model.from_map(m.get('Neck'))

        if m.get('NumLandmarks') is not None:
            self.num_landmarks = m.get('NumLandmarks')

        if m.get('PretrainedPath') is not None:
            self.pretrained_path = m.get('PretrainedPath')

        return self

