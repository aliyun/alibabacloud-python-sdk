# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateWatermarkRequest(DaraModel):
    def __init__(
        self,
        name: str = None,
        watermark_config: str = None,
        watermark_id: str = None,
    ):
        # The new name of the watermark template.
        # - Only Chinese characters, letters, and digits are supported.
        # - The name can be up to 128 bytes in length.
        # - UTF-8 encoding.
        self.name = name
        # The configuration information of the image and text watermark (JSON character string), including the watermark display position and watermark effect. The configuration parameters for image watermarks and text watermarks are different. For details about the parameter structure, see [WatermarkConfig](~~98618#section-h01-44s-2lr~~).
        # >Modifying across templatetypes is not supported. You can invoke the [GetWatermark](~~GetWatermark~~) operation to query the type of the watermark template before modifying the configuration.
        # 
        # This parameter is required.
        self.watermark_config = watermark_config
        # The ID of the image and text watermark template to modify. Only a single watermark template ID is supported. You can obtain the ID by using one of the following methods:
        # - The ID is returned after you call the [AddWatermark](~~AddWatermark~~) operation to add an image and text watermark template.
        # - The ID is returned after you call the [ListWatermark](~~ListWatermark~~) operation to query the list of image and text watermark templates.
        # 
        # This parameter is required.
        self.watermark_id = watermark_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.watermark_config is not None:
            result['WatermarkConfig'] = self.watermark_config

        if self.watermark_id is not None:
            result['WatermarkId'] = self.watermark_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('WatermarkConfig') is not None:
            self.watermark_config = m.get('WatermarkConfig')

        if m.get('WatermarkId') is not None:
            self.watermark_id = m.get('WatermarkId')

        return self

