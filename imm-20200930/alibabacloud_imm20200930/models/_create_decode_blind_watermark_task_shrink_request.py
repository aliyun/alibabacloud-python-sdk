# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateDecodeBlindWatermarkTaskShrinkRequest(DaraModel):
    def __init__(
        self,
        image_quality: int = None,
        model: str = None,
        notification_shrink: str = None,
        original_image_uri: str = None,
        project_name: str = None,
        source_uri: str = None,
        strength_level: str = None,
        target_uri: str = None,
        watermark_type: str = None,
    ):
        # A parameter from the earlier DecodeBlindWatermark API. It specifies the quality of the output image. The default value is 90. The value must be in the range of 70 to 100.
        # 
        # A higher quality results in a larger image size and better watermark parsing quality.
        self.image_quality = image_quality
        # A parameter from the earlier DecodeBlindWatermark API. It specifies the watermark algorithm model. Valid values include FFT, FFT_FULL, DWT, and DWT_IBG. The default value is FFT.
        # 
        # If this parameter is left empty, the new version of the blind watermarking feature is used. Otherwise, the earlier version is used.
        self.model = model
        # The notification configuration. For more information, click Notification. For the format of asynchronous notification messages, see [Asynchronous notification message format](https://help.aliyun.com/document_detail/2743997.html).
        self.notification_shrink = notification_shrink
        # A parameter from the earlier DecodeBlindWatermark API. It specifies the OSS URI of the image before the blind watermark was added.
        # 
        # This parameter is not required when Model is set to DWT or DWT_IBG.
        # 
        # The OSS URI must be in the `oss://<bucket>/<object>` format. `<bucket>` is the name of the OSS bucket that is in the same region as the current project. `<object>` is the full path of the file, including the file name extension.
        self.original_image_uri = original_image_uri
        # The project name. For information about how to obtain the project name, see [Create a project](https://help.aliyun.com/document_detail/478153.html).
        # >Notice: The project name must be the same as the one used to add the blind watermark with the [EncodeBlindWatermark](https://help.aliyun.com/document_detail/2743655.html) operation. Otherwise, the watermark cannot be extracted.
        # 
        # This parameter is required.
        self.project_name = project_name
        # The Object Storage Service (OSS) URI of the image.
        # 
        # The OSS URI must be in the `oss://<bucket>/<object>` format. `<bucket>` is the name of the OSS bucket that is in the same region as the current project. `<object>` is the full path of the file, including the file name extension.
        # 
        # This parameter is required.
        self.source_uri = source_uri
        # The watermark extraction level, which controls the extraction precision. A higher level indicates a longer processing time and a better extraction effect. Valid values:
        # 
        # - low
        # 
        # - medium
        # 
        # - high
        self.strength_level = strength_level
        # A parameter from the earlier DecodeBlindWatermark API. It specifies the OSS URI where the image is saved after the blind watermark is parsed.
        # 
        # The OSS URI must be in the `oss://<bucket>/<object>` format. `<bucket>` is the name of the OSS bucket that is in the same region as the current project. `<object>` is the full path of the file, including the file name extension.
        self.target_uri = target_uri
        # The type of the embedded watermark. Valid value: text
        # 
        # (Image watermarks are not supported. Therefore, this parameter can only be set to text.)
        self.watermark_type = watermark_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image_quality is not None:
            result['ImageQuality'] = self.image_quality

        if self.model is not None:
            result['Model'] = self.model

        if self.notification_shrink is not None:
            result['Notification'] = self.notification_shrink

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
            self.notification_shrink = m.get('Notification')

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

