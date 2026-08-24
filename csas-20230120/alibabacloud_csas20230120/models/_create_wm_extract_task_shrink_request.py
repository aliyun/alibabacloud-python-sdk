# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateWmExtractTaskShrinkRequest(DaraModel):
    def __init__(
        self,
        csv_control_shrink: str = None,
        document_is_capture: bool = None,
        file_url: str = None,
        filename: str = None,
        image_extract_params_open_api_shrink: str = None,
        is_client_embed: bool = None,
        video_is_long: bool = None,
        video_speed: str = None,
        wm_info_size: int = None,
        wm_type: str = None,
    ):
        # The CSV watermark control parameters. These must be consistent with the parameters used during embedding. Otherwise, extraction fails.
        self.csv_control_shrink = csv_control_shrink
        # The document watermark parameter that specifies whether the file to be extracted is a screenshot of a document with a background watermark. The service determines whether to use the document background watermark extraction logic based on whether the file is an image file. Therefore, this parameter does not need to be set by default. Valid values:
        # 
        # - **true**: Yes.
        # - **false**: No.
        self.document_is_capture = document_is_capture
        # The URL used to download the file from which the watermark is to be fetched. The URL must be accessible over the public network access.
        # 
        # This parameter is required.
        self.file_url = file_url
        # The name of the file from which the watermark is to be extracted. The backend determines and validates the file type based on the file name extension.
        # 
        # This parameter is required.
        self.filename = filename
        # The image extraction parameters.
        self.image_extract_params_open_api_shrink = image_extract_params_open_api_shrink
        # The audio watermark parameter that specifies whether the watermark was embedded by the client SDK. Default value: false. Valid values:
        # 
        # - **true**: Yes.
        # - **false**: No.
        self.is_client_embed = is_client_embed
        # The video watermark parameter that specifies whether to use the long video watermark SDK. Default value: false. Valid values:
        # 
        # - **true**: Yes.
        # - **false**: No.
        self.video_is_long = video_is_long
        # The long video watermark parameter that specifies the video playback speed as a floating-point string. Default value: 1, which indicates the playback speed used when the watermark was added, or the speed at which the video timeline was stretched after the watermark was added.
        self.video_speed = video_speed
        # The bit width of the watermark information capacity. Default value: 32. This parameter must be consistent between embedding and extraction. For example, if the 40-bit SDK was used for embedding, set this value to 40 for extraction.
        self.wm_info_size = wm_info_size
        # The watermark type. Valid values:
        # - **PureWebappInvisible**: web page watermark.
        # - **PureAppInvisible**: app watermark.
        # - **PureScreenInvisible**: screen watermark.
        # - **PureDocument**: document watermark.
        # - **PureImage**: image watermark.
        # - **PureAudio**: audio watermark.
        # - **PureVideo**: video watermark.
        # - **AigcWebappInvisible**: AIGC web page watermark.
        # - **AigcAppInvisible**: AIGC app watermark.
        # - **AigcScreenInvisible**: AIGC screen watermark.
        # - **AigcDocument**: AIGC document watermark.
        # - **AigcImage**: AIGC image watermark.
        # - **AigcAudio**: AIGC audio watermark.
        # - **AigcVideo**: AIGC video watermark.
        # 
        # This parameter is required.
        self.wm_type = wm_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.csv_control_shrink is not None:
            result['CsvControl'] = self.csv_control_shrink

        if self.document_is_capture is not None:
            result['DocumentIsCapture'] = self.document_is_capture

        if self.file_url is not None:
            result['FileUrl'] = self.file_url

        if self.filename is not None:
            result['Filename'] = self.filename

        if self.image_extract_params_open_api_shrink is not None:
            result['ImageExtractParamsOpenApi'] = self.image_extract_params_open_api_shrink

        if self.is_client_embed is not None:
            result['IsClientEmbed'] = self.is_client_embed

        if self.video_is_long is not None:
            result['VideoIsLong'] = self.video_is_long

        if self.video_speed is not None:
            result['VideoSpeed'] = self.video_speed

        if self.wm_info_size is not None:
            result['WmInfoSize'] = self.wm_info_size

        if self.wm_type is not None:
            result['WmType'] = self.wm_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CsvControl') is not None:
            self.csv_control_shrink = m.get('CsvControl')

        if m.get('DocumentIsCapture') is not None:
            self.document_is_capture = m.get('DocumentIsCapture')

        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')

        if m.get('Filename') is not None:
            self.filename = m.get('Filename')

        if m.get('ImageExtractParamsOpenApi') is not None:
            self.image_extract_params_open_api_shrink = m.get('ImageExtractParamsOpenApi')

        if m.get('IsClientEmbed') is not None:
            self.is_client_embed = m.get('IsClientEmbed')

        if m.get('VideoIsLong') is not None:
            self.video_is_long = m.get('VideoIsLong')

        if m.get('VideoSpeed') is not None:
            self.video_speed = m.get('VideoSpeed')

        if m.get('WmInfoSize') is not None:
            self.wm_info_size = m.get('WmInfoSize')

        if m.get('WmType') is not None:
            self.wm_type = m.get('WmType')

        return self

