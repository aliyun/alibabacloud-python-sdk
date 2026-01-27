# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_csas20230120 import models as main_models
from darabonba.model import DaraModel

class CreateWmExtractTaskRequest(DaraModel):
    def __init__(
        self,
        csv_control: main_models.CreateWmExtractTaskRequestCsvControl = None,
        document_is_capture: bool = None,
        file_url: str = None,
        filename: str = None,
        image_extract_params_open_api: main_models.CreateWmExtractTaskRequestImageExtractParamsOpenApi = None,
        is_client_embed: bool = None,
        video_is_long: bool = None,
        video_speed: str = None,
        wm_info_size: int = None,
        wm_type: str = None,
    ):
        # The CSV watermark control parameter. You must keep the value of this parameter consistent for watermark embedding and watermark extraction. Otherwise, the extraction fails.
        self.csv_control = csv_control
        # The document watermark parameter that specifies whether the file to be extracted is a screenshot of a document with a background watermark added. The system determines whether to use the extraction logic for document background watermarks based on whether the file to be extracted is an image file. By default, you do not need to configure this parameter. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.document_is_capture = document_is_capture
        # The URL used to download the file to be extracted. The URL must be accessible over the Internet.
        # 
        # This parameter is required.
        self.file_url = file_url
        # The name of the file to be extracted. The system needs to check the file type based on the file name extension.
        # 
        # This parameter is required.
        self.filename = filename
        self.image_extract_params_open_api = image_extract_params_open_api
        self.is_client_embed = is_client_embed
        # The watermark parameter for videos that specifies whether to use the long video watermark SDK. Default value: false. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.video_is_long = video_is_long
        # The watermark parameter for long videos that specifies the video speed factor. The value can be a floating-point number or a string. Default value: 1. This parameter indicates the speed at which a watermark is added or the time-stretching rate for videos after a watermark is added.
        self.video_speed = video_speed
        # The watermark information size. Default value: 32. You must keep the value of this parameter consistent for watermark embedding and watermark extraction. For example, if a 40-bit watermark is used for watermark embedding, you must set this parameter to 40 for watermark extraction.
        self.wm_info_size = wm_info_size
        # The watermark type. Valid values:
        # 
        # *   **PureWebappInvisible**: web page watermark
        # *   **PureAppInvisible**: app watermark
        # *   **PureScreenInvisible**: screen watermark
        # *   **PureDocument**: document watermark
        # *   **PureImage**: image watermark
        # *   **PureAudio**: audio watermark
        # *   **PureVideo**: video watermark
        # *   **AigcWebappInvisible**: artificial intelligence generated content (AIGC)-based webpage watermark
        # *   **AigcAppInvisible**: AIGC-based app watermark
        # *   **AigcScreenInvisible**: AIGC-based screen watermark
        # *   **AigcDocument**: AIGC-based document watermark
        # *   **AigcImage**: AIGC-based image watermark
        # *   **AigcAudio**: AIGC-based audio watermark
        # *   **AigcVideo**: AIGC-based video watermark
        # 
        # This parameter is required.
        self.wm_type = wm_type

    def validate(self):
        if self.csv_control:
            self.csv_control.validate()
        if self.image_extract_params_open_api:
            self.image_extract_params_open_api.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.csv_control is not None:
            result['CsvControl'] = self.csv_control.to_map()

        if self.document_is_capture is not None:
            result['DocumentIsCapture'] = self.document_is_capture

        if self.file_url is not None:
            result['FileUrl'] = self.file_url

        if self.filename is not None:
            result['Filename'] = self.filename

        if self.image_extract_params_open_api is not None:
            result['ImageExtractParamsOpenApi'] = self.image_extract_params_open_api.to_map()

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
            temp_model = main_models.CreateWmExtractTaskRequestCsvControl()
            self.csv_control = temp_model.from_map(m.get('CsvControl'))

        if m.get('DocumentIsCapture') is not None:
            self.document_is_capture = m.get('DocumentIsCapture')

        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')

        if m.get('Filename') is not None:
            self.filename = m.get('Filename')

        if m.get('ImageExtractParamsOpenApi') is not None:
            temp_model = main_models.CreateWmExtractTaskRequestImageExtractParamsOpenApi()
            self.image_extract_params_open_api = temp_model.from_map(m.get('ImageExtractParamsOpenApi'))

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

class CreateWmExtractTaskRequestImageExtractParamsOpenApi(DaraModel):
    def __init__(
        self,
        src_logo_base_64: str = None,
    ):
        self.src_logo_base_64 = src_logo_base_64

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.src_logo_base_64 is not None:
            result['SrcLogoBase64'] = self.src_logo_base_64

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SrcLogoBase64') is not None:
            self.src_logo_base_64 = m.get('SrcLogoBase64')

        return self

class CreateWmExtractTaskRequestCsvControl(DaraModel):
    def __init__(
        self,
        embed_bits_number_in_each_time: int = None,
        embed_column: int = None,
        embed_precision: int = None,
        embed_time_position: str = None,
        method: str = None,
        time_format: str = None,
    ):
        # The timestamp watermark parameter that specifies how much information a single timestamp holds. You must keep the value of this parameter consistent for watermark embedding and watermark extraction. Otherwise, the extraction fails.
        self.embed_bits_number_in_each_time = embed_bits_number_in_each_time
        # The lossy embedding control parameter that specifies columns to be modified You must keep the value of this parameter consistent for watermark embedding and watermark extraction. Otherwise, the extraction fails.
        self.embed_column = embed_column
        # The lossy embedding control parameter that specifies the modification precision. You must keep the value of this parameter consistent for watermark embedding and watermark extraction. Otherwise, the extraction fails.
        self.embed_precision = embed_precision
        # The timestamp watermark parameter that specifies the embedding position of the timestamp watermarks. You must keep the value of this parameter consistent for watermark embedding and watermark extraction. Otherwise, the extraction fails.
        self.embed_time_position = embed_time_position
        # The CSV watermark embedding method. You must keep the value of this parameter consistent for watermark embedding and watermark extraction. Otherwise, the extraction fails.
        self.method = method
        # The timestamp watermark parameter that specifies the timestamp format. You must keep the value of this parameter consistent for watermark embedding and watermark extraction. Otherwise, the extraction fails.
        self.time_format = time_format

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.embed_bits_number_in_each_time is not None:
            result['EmbedBitsNumberInEachTime'] = self.embed_bits_number_in_each_time

        if self.embed_column is not None:
            result['EmbedColumn'] = self.embed_column

        if self.embed_precision is not None:
            result['EmbedPrecision'] = self.embed_precision

        if self.embed_time_position is not None:
            result['EmbedTimePosition'] = self.embed_time_position

        if self.method is not None:
            result['Method'] = self.method

        if self.time_format is not None:
            result['TimeFormat'] = self.time_format

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EmbedBitsNumberInEachTime') is not None:
            self.embed_bits_number_in_each_time = m.get('EmbedBitsNumberInEachTime')

        if m.get('EmbedColumn') is not None:
            self.embed_column = m.get('EmbedColumn')

        if m.get('EmbedPrecision') is not None:
            self.embed_precision = m.get('EmbedPrecision')

        if m.get('EmbedTimePosition') is not None:
            self.embed_time_position = m.get('EmbedTimePosition')

        if m.get('Method') is not None:
            self.method = m.get('Method')

        if m.get('TimeFormat') is not None:
            self.time_format = m.get('TimeFormat')

        return self

