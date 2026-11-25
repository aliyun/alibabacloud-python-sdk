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
        # CSV watermark control parameters. These parameters must be consistent with those used during embedding. Otherwise, the extraction fails.
        self.csv_control = csv_control
        # Document watermark parameter. Specifies whether the file from which the watermark is to be extracted is a screenshot of a document with a background watermark. The service determines whether to use the document background watermark extraction logic based on whether the file is an image file. Therefore, you do not need to set this parameter by default. Valid values:
        # 
        # - **true**: Yes.
        # - **false**: No.
        self.document_is_capture = document_is_capture
        # The URL used to download the file to be fetched. The URL must support public network access.
        # 
        # This parameter is required.
        self.file_url = file_url
        # The name of the file from which the watermark is to be extracted. The backend determines and verifies the file type based on the file name extension.
        # 
        # This parameter is required.
        self.filename = filename
        # Image extraction parameters.
        self.image_extract_params_open_api = image_extract_params_open_api
        # Audio watermark parameter. Specifies whether the watermark is embedded by using the client SDK. Default value: false. Valid values:
        # 
        # - **true**: Yes.
        # - **false**: No.
        self.is_client_embed = is_client_embed
        # Video watermark parameter. Specifies whether to use the long video watermark SDK. Default value: false. Valid values:
        # 
        # - **true**: Yes.
        # - **false**: No.
        self.video_is_long = video_is_long
        # Long video watermark parameter. The video playback speed, represented as a floating-point string. Default value: 1. This value represents the playback speed used when adding the watermark, or the timeline stretching speed after the watermark is added.
        self.video_speed = video_speed
        # The bit width of the watermark information capacity. Default value: 32. This parameter must be consistent during embedding and extraction. For example, if a 40-bit SDK is used for embedding, you must also set this value to 40 for extraction.
        self.wm_info_size = wm_info_size
        # The watermark type. Valid values:
        # - **PureWebappInvisible**: Web page watermark.
        # - **PureAppInvisible**: App watermark.
        # - **PureScreenInvisible**: Screen watermark.
        # - **PureDocument**: Document watermark.
        # - **PureImage**: Image watermark.
        # - **PureAudio**: Audio watermark.
        # - **PureVideo**: Video watermark.
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
        # The original file of the enhanced visible watermark logo in Base64 format. Used to extract the enhanced visible watermark.
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
        # Timestamp watermark parameter. Specifies the amount of information contained in a single timestamp. This parameter must be consistent with the corresponding parameter used during embedding. Otherwise, the extraction fails.
        self.embed_bits_number_in_each_time = embed_bits_number_in_each_time
        # Lossy embedding control parameter. Specifies the column to be modified. This parameter must be consistent with the one used during embedding. Otherwise, the extraction fails.
        self.embed_column = embed_column
        # Lossy embedding control parameter. Specifies the modification precision. This parameter must be consistent with the one used during embedding. Otherwise, the extraction fails.
        self.embed_precision = embed_precision
        # Timestamp watermark parameter. Controls the embedding position of the timestamp watermark. This parameter must be consistent with the corresponding parameter used during embedding. Otherwise, the extraction fails.
        self.embed_time_position = embed_time_position
        # The CSV watermark embedding method. This parameter must be consistent with the one used during embedding. Otherwise, the extraction fails.
        self.method = method
        # Timestamp watermark parameter. Specifies the timestamp format. This parameter must be consistent with the corresponding parameter used during embedding. Otherwise, the extraction fails.
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

