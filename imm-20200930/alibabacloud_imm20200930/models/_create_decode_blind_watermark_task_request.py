# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_imm20200930 import models as main_models
from darabonba.model import DaraModel

class CreateDecodeBlindWatermarkTaskRequest(DaraModel):
    def __init__(
        self,
        image_quality: int = None,
        model: str = None,
        notification: main_models.Notification = None,
        original_image_uri: str = None,
        project_name: str = None,
        source_uri: str = None,
        strength_level: str = None,
        target_uri: str = None,
        watermark_type: str = None,
    ):
        # The quality of the output image. This parameter is also available in the earlier DecodeBlindWatermark operation.
        # 
        # Higher image quality indicates a larger image size and higher watermark resolution quality.
        self.image_quality = image_quality
        # The watermark algorithm model. This parameter is also available in the earlier DecodeBlindWatermark operation. Valid values: FFT, FFT_FULL, DWT, and DWT_IBG. Default value: FFT.
        # 
        # If this parameter is left empty, the CreateDecodeBlindWatermarkTask operation is called. Otherwise, the earlier DecodeBlindWatermark operation is called.
        self.model = model
        # The notification settings. For information about the asynchronous notification format, see [Asynchronous message examples](https://help.aliyun.com/document_detail/2743997.html).
        self.notification = notification
        # The OSS URI of the image before the blind watermark is added. This parameter is also available in the earlier DecodeBlindWatermark operation.
        # 
        # Do not specify this parameter when you set the Model parameter to DWT or DWT_IBG.
        # 
        # Specify the OSS URI in the `oss://<bucket>/<object>` format, where `<bucket>` is the name of the bucket in the same region as the current project and `<object>` is the path of the object with the extension included.
        self.original_image_uri = original_image_uri
        # The name of the project.[](~~478153~~)
        # 
        # >  The project specified in the request must match the one in the EncodeBlindWatermark request to encode the blind watermark.
        # 
        # This parameter is required.
        self.project_name = project_name
        # The OSS URI of the image.
        # 
        # Specify the OSS URI in the `oss://<bucket>/<object>` format, where `<bucket>` is the name of the bucket in the same region as the current project and `<object>` is the path of the object with the extension included.
        # 
        # This parameter is required.
        self.source_uri = source_uri
        # The level of watermark extraction. A higher level indicates a longer time and a higher quality. Valid values:
        # 
        # *   low
        # *   medium
        # *   high
        self.strength_level = strength_level
        # The OSS URI of the output image. This parameter is also available in the earlier DecodeBlindWatermark operation.
        # 
        # Specify the OSS URI in the `oss://<bucket>/<object>` format, where `<bucket>` is the name of the bucket in the same region as the current project and `<object>` is the path of the object with the extension included.
        self.target_uri = target_uri
        # The type of the watermark. Valid value: text.
        # 
        # No image watermarks are supported.
        self.watermark_type = watermark_type

    def validate(self):
        if self.notification:
            self.notification.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image_quality is not None:
            result['ImageQuality'] = self.image_quality

        if self.model is not None:
            result['Model'] = self.model

        if self.notification is not None:
            result['Notification'] = self.notification.to_map()

        if self.original_image_uri is not None:
            result['OriginalImageURI'] = self.original_image_uri

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri

        if self.strength_level is not None:
            result['StrengthLevel'] = self.strength_level

        if self.target_uri is not None:
            result['TargetURI'] = self.target_uri

        if self.watermark_type is not None:
            result['WatermarkType'] = self.watermark_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageQuality') is not None:
            self.image_quality = m.get('ImageQuality')

        if m.get('Model') is not None:
            self.model = m.get('Model')

        if m.get('Notification') is not None:
            temp_model = main_models.Notification()
            self.notification = temp_model.from_map(m.get('Notification'))

        if m.get('OriginalImageURI') is not None:
            self.original_image_uri = m.get('OriginalImageURI')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')

        if m.get('StrengthLevel') is not None:
            self.strength_level = m.get('StrengthLevel')

        if m.get('TargetURI') is not None:
            self.target_uri = m.get('TargetURI')

        if m.get('WatermarkType') is not None:
            self.watermark_type = m.get('WatermarkType')

        return self

