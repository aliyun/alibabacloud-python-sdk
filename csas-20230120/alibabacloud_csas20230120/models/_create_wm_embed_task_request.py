# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_csas20230120 import models as main_models
from darabonba.model import DaraModel

class CreateWmEmbedTaskRequest(DaraModel):
    def __init__(
        self,
        audio_control: main_models.CreateWmEmbedTaskRequestAudioControl = None,
        csv_control: main_models.CreateWmEmbedTaskRequestCsvControl = None,
        document_control: main_models.CreateWmEmbedTaskRequestDocumentControl = None,
        file_url: str = None,
        filename: str = None,
        image_control: main_models.CreateWmEmbedTaskRequestImageControl = None,
        image_embed_jpeg_quality: int = None,
        image_embed_level: int = None,
        invisible_enable: bool = None,
        video_bitrate: str = None,
        video_control: main_models.CreateWmEmbedTaskRequestVideoControl = None,
        video_is_long: bool = None,
        wm_info_bytes_b64: str = None,
        wm_info_size: int = None,
        wm_info_uint: str = None,
        wm_type: str = None,
    ):
        # The audio control parameters.
        self.audio_control = audio_control
        # The CSV watermark embedding control parameters.
        self.csv_control = csv_control
        # The document watermark control parameters.
        self.document_control = document_control
        # The active URL for downloading the file to be embedded. The URL must support public network access.
        # 
        # This parameter is required.
        self.file_url = file_url
        # The file name of the file to be embedded. The backend determines and verifies the file type based on the file name extension.
        # 
        # This parameter is required.
        self.filename = filename
        # The image watermark control parameters.
        self.image_control = image_control
        # The image watermark parameter that specifies the expected JPEG compression quality factor of the output image. Default value: 95. Valid values: 1 to 100.
        self.image_embed_jpeg_quality = image_embed_jpeg_quality
        # The image watermark parameter that specifies the embedding level. A larger value indicates higher robustness but lower visual quality. Default value: 2. Valid values: 0 to 4.
        self.image_embed_level = image_embed_level
        # Specifies whether to enable invisible watermark embedding. Default value: true. Valid values:
        # - **true**: Yes.
        # - **false**: No.
        self.invisible_enable = invisible_enable
        # The short video watermark parameter that specifies the video bitrate. By default, the system automatically obtains the video bitrate. You can use this parameter to force the bitrate used during extraction. Typically, you do not need to set this parameter.
        self.video_bitrate = video_bitrate
        # The video control parameters.
        self.video_control = video_control
        # The video watermark parameter that specifies whether to use the long video watermark SDK. Default value: false. Valid values:
        # 
        # - **true**: Yes.
        # - **false**: No.
        self.video_is_long = video_is_long
        # The watermark information in Base64-encoded string format. If you set this parameter, you cannot set WmInfoUint.
        self.wm_info_bytes_b64 = wm_info_bytes_b64
        # The capacity bit width of the watermark information. Default value: 32. This parameter must be consistent during embedding and extraction. For example, if a 40-bit SDK is used for embedding, you must also set this value to 40 for extraction.
        self.wm_info_size = wm_info_size
        # The watermark information in decimal numeric format. If you set this parameter, you cannot set WmInfoBytesB64.
        # 
        # The valid value range depends on the WmInfoSize parameter:
        # 
        # - When WmInfoSize is 32, the valid values are 1 to 4294967295.
        # 
        # - When WmInfoSize is 40, the valid values are 1 to 1099511627775.
        # 
        # - When WmInfoSize is 64, the valid values are 1 to 18446744073709551615.
        self.wm_info_uint = wm_info_uint
        # The watermark type. Valid values:
        # - **PureDocument**: Document watermark.
        # - **PureImage**: Image watermark.
        # - **PureAudio**: Audio watermark.
        # - **PureVideo**: Video watermark.
        # - **AigcDocument**: AIGC document watermark.
        # - **AigcImage**: AIGC image watermark.
        # - **AigcAudio**: AIGC audio watermark.
        # - **AigcVideo**: AIGC video watermark.
        # 
        # This parameter is required.
        self.wm_type = wm_type

    def validate(self):
        if self.audio_control:
            self.audio_control.validate()
        if self.csv_control:
            self.csv_control.validate()
        if self.document_control:
            self.document_control.validate()
        if self.image_control:
            self.image_control.validate()
        if self.video_control:
            self.video_control.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audio_control is not None:
            result['AudioControl'] = self.audio_control.to_map()

        if self.csv_control is not None:
            result['CsvControl'] = self.csv_control.to_map()

        if self.document_control is not None:
            result['DocumentControl'] = self.document_control.to_map()

        if self.file_url is not None:
            result['FileUrl'] = self.file_url

        if self.filename is not None:
            result['Filename'] = self.filename

        if self.image_control is not None:
            result['ImageControl'] = self.image_control.to_map()

        if self.image_embed_jpeg_quality is not None:
            result['ImageEmbedJpegQuality'] = self.image_embed_jpeg_quality

        if self.image_embed_level is not None:
            result['ImageEmbedLevel'] = self.image_embed_level

        if self.invisible_enable is not None:
            result['InvisibleEnable'] = self.invisible_enable

        if self.video_bitrate is not None:
            result['VideoBitrate'] = self.video_bitrate

        if self.video_control is not None:
            result['VideoControl'] = self.video_control.to_map()

        if self.video_is_long is not None:
            result['VideoIsLong'] = self.video_is_long

        if self.wm_info_bytes_b64 is not None:
            result['WmInfoBytesB64'] = self.wm_info_bytes_b64

        if self.wm_info_size is not None:
            result['WmInfoSize'] = self.wm_info_size

        if self.wm_info_uint is not None:
            result['WmInfoUint'] = self.wm_info_uint

        if self.wm_type is not None:
            result['WmType'] = self.wm_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AudioControl') is not None:
            temp_model = main_models.CreateWmEmbedTaskRequestAudioControl()
            self.audio_control = temp_model.from_map(m.get('AudioControl'))

        if m.get('CsvControl') is not None:
            temp_model = main_models.CreateWmEmbedTaskRequestCsvControl()
            self.csv_control = temp_model.from_map(m.get('CsvControl'))

        if m.get('DocumentControl') is not None:
            temp_model = main_models.CreateWmEmbedTaskRequestDocumentControl()
            self.document_control = temp_model.from_map(m.get('DocumentControl'))

        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')

        if m.get('Filename') is not None:
            self.filename = m.get('Filename')

        if m.get('ImageControl') is not None:
            temp_model = main_models.CreateWmEmbedTaskRequestImageControl()
            self.image_control = temp_model.from_map(m.get('ImageControl'))

        if m.get('ImageEmbedJpegQuality') is not None:
            self.image_embed_jpeg_quality = m.get('ImageEmbedJpegQuality')

        if m.get('ImageEmbedLevel') is not None:
            self.image_embed_level = m.get('ImageEmbedLevel')

        if m.get('InvisibleEnable') is not None:
            self.invisible_enable = m.get('InvisibleEnable')

        if m.get('VideoBitrate') is not None:
            self.video_bitrate = m.get('VideoBitrate')

        if m.get('VideoControl') is not None:
            temp_model = main_models.CreateWmEmbedTaskRequestVideoControl()
            self.video_control = temp_model.from_map(m.get('VideoControl'))

        if m.get('VideoIsLong') is not None:
            self.video_is_long = m.get('VideoIsLong')

        if m.get('WmInfoBytesB64') is not None:
            self.wm_info_bytes_b64 = m.get('WmInfoBytesB64')

        if m.get('WmInfoSize') is not None:
            self.wm_info_size = m.get('WmInfoSize')

        if m.get('WmInfoUint') is not None:
            self.wm_info_uint = m.get('WmInfoUint')

        if m.get('WmType') is not None:
            self.wm_type = m.get('WmType')

        return self

class CreateWmEmbedTaskRequestVideoControl(DaraModel):
    def __init__(
        self,
        metadata_control: main_models.CreateWmEmbedTaskRequestVideoControlMetadataControl = None,
        text_visible_control: main_models.CreateWmEmbedTaskRequestVideoControlTextVisibleControl = None,
    ):
        # The metadata control parameters.
        self.metadata_control = metadata_control
        # The text watermark control parameters for videos.
        self.text_visible_control = text_visible_control

    def validate(self):
        if self.metadata_control:
            self.metadata_control.validate()
        if self.text_visible_control:
            self.text_visible_control.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.metadata_control is not None:
            result['MetadataControl'] = self.metadata_control.to_map()

        if self.text_visible_control is not None:
            result['TextVisibleControl'] = self.text_visible_control.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MetadataControl') is not None:
            temp_model = main_models.CreateWmEmbedTaskRequestVideoControlMetadataControl()
            self.metadata_control = temp_model.from_map(m.get('MetadataControl'))

        if m.get('TextVisibleControl') is not None:
            temp_model = main_models.CreateWmEmbedTaskRequestVideoControlTextVisibleControl()
            self.text_visible_control = temp_model.from_map(m.get('TextVisibleControl'))

        return self

class CreateWmEmbedTaskRequestVideoControlTextVisibleControl(DaraModel):
    def __init__(
        self,
        font_color: str = None,
        font_size: int = None,
        margin: main_models.CreateWmEmbedTaskRequestVideoControlTextVisibleControlMargin = None,
        mode: str = None,
        opacity: int = None,
        pos_x: int = None,
        pos_y: int = None,
        visible: bool = None,
        visible_text: str = None,
    ):
        # The font color of the text watermark. The value must be in the 0xFFFFFF or #FFFFFF RGB color format.
        self.font_color = font_color
        # The font size. Valid values: **0** to **72**.
        self.font_size = font_size
        # The margin of the text watermark. This parameter takes effect only when Mode is set to top-left, top-right, bottom-left, or bottom-right.
        self.margin = margin
        # The display mode of the text watermark. Valid values:
        # - **pos**: Fixed position mode, with the top-left corner as the origin.
        # - **bottom-right**: Bottom-right mode.
        self.mode = mode
        # The opacity of the text watermark. Valid values: 1 to 255. A larger value indicates lower transparency.
        self.opacity = opacity
        # The horizontal position of the visible watermark. This parameter takes effect only when Mode is set to pos. The value is the pixel position with the top-left corner as the origin.
        self.pos_x = pos_x
        # The vertical position of the visible watermark. This parameter takes effect only when Mode is set to pos. The value is the pixel position with the top-left corner as the origin.
        self.pos_y = pos_y
        # Specifies whether the text watermark is visible. Valid values:
        # - true: Visible.
        # - false: Invisible.
        self.visible = visible
        # The text watermark content. The value must be a UTF-8 string.
        self.visible_text = visible_text

    def validate(self):
        if self.margin:
            self.margin.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.font_color is not None:
            result['FontColor'] = self.font_color

        if self.font_size is not None:
            result['FontSize'] = self.font_size

        if self.margin is not None:
            result['Margin'] = self.margin.to_map()

        if self.mode is not None:
            result['Mode'] = self.mode

        if self.opacity is not None:
            result['Opacity'] = self.opacity

        if self.pos_x is not None:
            result['PosX'] = self.pos_x

        if self.pos_y is not None:
            result['PosY'] = self.pos_y

        if self.visible is not None:
            result['Visible'] = self.visible

        if self.visible_text is not None:
            result['VisibleText'] = self.visible_text

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FontColor') is not None:
            self.font_color = m.get('FontColor')

        if m.get('FontSize') is not None:
            self.font_size = m.get('FontSize')

        if m.get('Margin') is not None:
            temp_model = main_models.CreateWmEmbedTaskRequestVideoControlTextVisibleControlMargin()
            self.margin = temp_model.from_map(m.get('Margin'))

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('Opacity') is not None:
            self.opacity = m.get('Opacity')

        if m.get('PosX') is not None:
            self.pos_x = m.get('PosX')

        if m.get('PosY') is not None:
            self.pos_y = m.get('PosY')

        if m.get('Visible') is not None:
            self.visible = m.get('Visible')

        if m.get('VisibleText') is not None:
            self.visible_text = m.get('VisibleText')

        return self

class CreateWmEmbedTaskRequestVideoControlTextVisibleControlMargin(DaraModel):
    def __init__(
        self,
        bottom: int = None,
        right: int = None,
    ):
        # The bottom margin. This parameter takes effect only when Mode is set to bottom-left or bottom-right.
        self.bottom = bottom
        # The right margin. This parameter takes effect only when Mode is set to top-right or bottom-right.
        self.right = right

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bottom is not None:
            result['Bottom'] = self.bottom

        if self.right is not None:
            result['Right'] = self.right

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bottom') is not None:
            self.bottom = m.get('Bottom')

        if m.get('Right') is not None:
            self.right = m.get('Right')

        return self

class CreateWmEmbedTaskRequestVideoControlMetadataControl(DaraModel):
    def __init__(
        self,
        enable: bool = None,
        xmp_kv_base_64: str = None,
    ):
        # Specifies whether to enable the metadata. Valid values:
        # - **false**: Disabled.
        # - **true**: Enabled.
        self.enable = enable
        # The Base64-encoded metadata. You must encode a string in the format of AIGC={"Label":"1","ContentProducer":"AXXXX","ProduceID":"BXXXX","ReservedCode1":"CXXX","ContentPropagator":"DXXX","PropagateID":"EXXX","ReservedCode2":"FXXXX"} into a Base64 string. Note: 1. The "AIGC=" prefix is required. Otherwise, the metadata cannot be added. Note that the prefix is different from that of image metadata. 2. The Base64 string must be in the standard format and include padding.
        self.xmp_kv_base_64 = xmp_kv_base_64

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable is not None:
            result['Enable'] = self.enable

        if self.xmp_kv_base_64 is not None:
            result['XmpKvBase64'] = self.xmp_kv_base_64

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('XmpKvBase64') is not None:
            self.xmp_kv_base_64 = m.get('XmpKvBase64')

        return self

class CreateWmEmbedTaskRequestImageControl(DaraModel):
    def __init__(
        self,
        logo_visible_control: main_models.CreateWmEmbedTaskRequestImageControlLogoVisibleControl = None,
        metadata_control: main_models.CreateWmEmbedTaskRequestImageControlMetadataControl = None,
        text_visible_control: main_models.CreateWmEmbedTaskRequestImageControlTextVisibleControl = None,
    ):
        # The logo watermark control parameters.
        self.logo_visible_control = logo_visible_control
        # The metadata control parameters. This parameter takes effect only when WmType is set to PureImage or AigcImage.
        self.metadata_control = metadata_control
        # The text watermark control parameters for images.
        self.text_visible_control = text_visible_control

    def validate(self):
        if self.logo_visible_control:
            self.logo_visible_control.validate()
        if self.metadata_control:
            self.metadata_control.validate()
        if self.text_visible_control:
            self.text_visible_control.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.logo_visible_control is not None:
            result['LogoVisibleControl'] = self.logo_visible_control.to_map()

        if self.metadata_control is not None:
            result['MetadataControl'] = self.metadata_control.to_map()

        if self.text_visible_control is not None:
            result['TextVisibleControl'] = self.text_visible_control.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogoVisibleControl') is not None:
            temp_model = main_models.CreateWmEmbedTaskRequestImageControlLogoVisibleControl()
            self.logo_visible_control = temp_model.from_map(m.get('LogoVisibleControl'))

        if m.get('MetadataControl') is not None:
            temp_model = main_models.CreateWmEmbedTaskRequestImageControlMetadataControl()
            self.metadata_control = temp_model.from_map(m.get('MetadataControl'))

        if m.get('TextVisibleControl') is not None:
            temp_model = main_models.CreateWmEmbedTaskRequestImageControlTextVisibleControl()
            self.text_visible_control = temp_model.from_map(m.get('TextVisibleControl'))

        return self

class CreateWmEmbedTaskRequestImageControlTextVisibleControl(DaraModel):
    def __init__(
        self,
        angle: int = None,
        font_color: str = None,
        font_size: int = None,
        margin: main_models.CreateWmEmbedTaskRequestImageControlTextVisibleControlMargin = None,
        mode: str = None,
        opacity: int = None,
        pos_ax: float = None,
        pos_ay: float = None,
        pos_x: int = None,
        pos_y: int = None,
        space_x: int = None,
        space_y: int = None,
        visible: bool = None,
        visible_text: str = None,
    ):
        # The clockwise rotation angle of the text watermark. Valid values: 0 to 360.
        self.angle = angle
        # The font color of the text watermark. The value must be in the 0xFFFFFF or #FFFFFF RGB color format. For example, 0x000000 or #000000 indicates black.
        self.font_color = font_color
        # The font size of the text watermark. A larger value indicates a larger font size.
        self.font_size = font_size
        # The margin of the text watermark. This parameter takes effect only when Mode is set to top-left, top-right, bottom-left, or bottom-right.
        self.margin = margin
        # The display mode of the text watermark. Valid values:
        # - **pos**: Fixed position mode.
        # - **repeat**: Tiled mode.
        # - **top-left**: Top-left mode.
        # - **top-right**: Top-right mode.
        # - **bottom-left**: Bottom-left mode.
        # - **bottom-right**: Bottom-right mode.
        self.mode = mode
        # The opacity of the text watermark. Valid values: 1 to 255. A larger value indicates lower transparency.
        self.opacity = opacity
        # The horizontal anchor point of the text watermark. Valid values: 0 to 1. If PosAx and PosAy are both set to 0, the top-left corner of the text is used as the anchor point. If the value is 0.5, the center of the text is used as the anchor point. If PosAx and PosAy are both set to 1, the bottom-right corner of the text is used as the anchor point.
        self.pos_ax = pos_ax
        # The vertical anchor point of the text watermark. Valid values: 0 to 1. If PosAx and PosAy are both set to 0, the top-left corner of the text is used as the anchor point. If the value is 0.5, the center of the text is used as the anchor point. If PosAx and PosAy are both set to 1, the bottom-right corner of the text is used as the anchor point.
        self.pos_ay = pos_ay
        # The horizontal position of the text watermark. This parameter takes effect only when Mode is set to pos. The value is the pixel position with the top-left corner as the origin.
        self.pos_x = pos_x
        # The vertical position of the text watermark. This parameter takes effect only when Mode is set to pos. The value is the pixel position with the top-left corner as the origin.
        self.pos_y = pos_y
        # The horizontal spacing of the tiled text watermark. This parameter takes effect only when Mode is set to repeat.
        self.space_x = space_x
        # The vertical spacing of the tiled text watermark. This parameter takes effect only when Mode is set to repeat.
        self.space_y = space_y
        # Specifies whether the text watermark is visible. Valid values:
        # - true: Visible.
        # - false: Invisible.
        self.visible = visible
        # The text watermark content. The value must be a UTF-8 string.
        self.visible_text = visible_text

    def validate(self):
        if self.margin:
            self.margin.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.angle is not None:
            result['Angle'] = self.angle

        if self.font_color is not None:
            result['FontColor'] = self.font_color

        if self.font_size is not None:
            result['FontSize'] = self.font_size

        if self.margin is not None:
            result['Margin'] = self.margin.to_map()

        if self.mode is not None:
            result['Mode'] = self.mode

        if self.opacity is not None:
            result['Opacity'] = self.opacity

        if self.pos_ax is not None:
            result['PosAx'] = self.pos_ax

        if self.pos_ay is not None:
            result['PosAy'] = self.pos_ay

        if self.pos_x is not None:
            result['PosX'] = self.pos_x

        if self.pos_y is not None:
            result['PosY'] = self.pos_y

        if self.space_x is not None:
            result['SpaceX'] = self.space_x

        if self.space_y is not None:
            result['SpaceY'] = self.space_y

        if self.visible is not None:
            result['Visible'] = self.visible

        if self.visible_text is not None:
            result['VisibleText'] = self.visible_text

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Angle') is not None:
            self.angle = m.get('Angle')

        if m.get('FontColor') is not None:
            self.font_color = m.get('FontColor')

        if m.get('FontSize') is not None:
            self.font_size = m.get('FontSize')

        if m.get('Margin') is not None:
            temp_model = main_models.CreateWmEmbedTaskRequestImageControlTextVisibleControlMargin()
            self.margin = temp_model.from_map(m.get('Margin'))

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('Opacity') is not None:
            self.opacity = m.get('Opacity')

        if m.get('PosAx') is not None:
            self.pos_ax = m.get('PosAx')

        if m.get('PosAy') is not None:
            self.pos_ay = m.get('PosAy')

        if m.get('PosX') is not None:
            self.pos_x = m.get('PosX')

        if m.get('PosY') is not None:
            self.pos_y = m.get('PosY')

        if m.get('SpaceX') is not None:
            self.space_x = m.get('SpaceX')

        if m.get('SpaceY') is not None:
            self.space_y = m.get('SpaceY')

        if m.get('Visible') is not None:
            self.visible = m.get('Visible')

        if m.get('VisibleText') is not None:
            self.visible_text = m.get('VisibleText')

        return self

class CreateWmEmbedTaskRequestImageControlTextVisibleControlMargin(DaraModel):
    def __init__(
        self,
        bottom: float = None,
        left: float = None,
        right: float = None,
        top: float = None,
    ):
        # The bottom margin. This parameter takes effect only when Mode is set to bottom-left or bottom-right.
        self.bottom = bottom
        # The left margin. This parameter takes effect only when Mode is set to top-left or bottom-left.
        self.left = left
        # The right margin. This parameter takes effect only when Mode is set to top-right or bottom-right.
        self.right = right
        # The top margin. This parameter takes effect only when Mode is set to top-left or top-right.
        self.top = top

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bottom is not None:
            result['Bottom'] = self.bottom

        if self.left is not None:
            result['Left'] = self.left

        if self.right is not None:
            result['Right'] = self.right

        if self.top is not None:
            result['Top'] = self.top

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bottom') is not None:
            self.bottom = m.get('Bottom')

        if m.get('Left') is not None:
            self.left = m.get('Left')

        if m.get('Right') is not None:
            self.right = m.get('Right')

        if m.get('Top') is not None:
            self.top = m.get('Top')

        return self

class CreateWmEmbedTaskRequestImageControlMetadataControl(DaraModel):
    def __init__(
        self,
        enable: bool = None,
        xmp_kv_base_64: str = None,
    ):
        # Specifies whether to enable the metadata. Valid values:
        # - true: Enabled.
        # - false: Disabled.
        self.enable = enable
        # The Base64-encoded metadata. You must encode a string in the format of AIGC:{"Label":"1","ContentProducer":"AXXXX","ProduceID":"BXXXX","ReservedCode1":"CXXX","ContentPropagator":"DXXX","PropagateID":"EXXX","ReservedCode2":"FXXXX"} into a Base64 string. Note: 1. The "AIGC:" prefix is required. Otherwise, the metadata cannot be added. Note that the format is different from that of audio and video. 2. The Base64 string must be in the standard format and include padding.
        self.xmp_kv_base_64 = xmp_kv_base_64

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable is not None:
            result['Enable'] = self.enable

        if self.xmp_kv_base_64 is not None:
            result['XmpKvBase64'] = self.xmp_kv_base_64

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('XmpKvBase64') is not None:
            self.xmp_kv_base_64 = m.get('XmpKvBase64')

        return self

class CreateWmEmbedTaskRequestImageControlLogoVisibleControl(DaraModel):
    def __init__(
        self,
        angle: int = None,
        enhance: bool = None,
        logo_base_64: str = None,
        margin: main_models.CreateWmEmbedTaskRequestImageControlLogoVisibleControlMargin = None,
        mode: str = None,
        opacity: int = None,
        pos_ax: float = None,
        pos_ay: float = None,
        pos_x: int = None,
        pos_y: int = None,
        space_x: int = None,
        space_y: int = None,
        visible: bool = None,
    ):
        # The clockwise rotation angle of the logo watermark. Valid values: 1 to 360.
        self.angle = angle
        # Specifies whether to enable the enhanced visible watermark. After this feature is enabled, the logo is processed, and the embedded information in the logo can be extracted.
        self.enhance = enhance
        # The Base64-encoded logo watermark. The logo file must be a PNG image encoded in Base64 format.
        self.logo_base_64 = logo_base_64
        # The margin of the text watermark. This parameter takes effect only when Mode is set to top-left, top-right, bottom-left, or bottom-right.
        self.margin = margin
        # The display mode of the logo watermark. Valid values:
        # - **pos**: Fixed position mode.
        # - **repeat**: Tiled mode.
        # - **top-left**: Top-left mode.
        # - **top-right**: Top-right mode.
        # - **bottom-left**: Bottom-left mode.
        # - **bottom-right**: Bottom-right mode.
        self.mode = mode
        # The opacity of the logo watermark. Valid values: 1 to 255. A larger value indicates lower transparency.
        self.opacity = opacity
        # The horizontal anchor point of the logo watermark. Valid values: 0 to 1. If PosAx and PosAy are both set to 0, the top-left corner of the logo is used as the anchor point. If the value is 0.5, the center of the logo is used as the anchor point. If PosAx and PosAy are both set to 1, the bottom-right corner of the logo is used as the anchor point.
        self.pos_ax = pos_ax
        # The vertical anchor point of the logo watermark. Valid values: 0 to 1. If PosAx and PosAy are both set to 0, the top-left corner of the logo is used as the anchor point. If the value is 0.5, the center of the logo is used as the anchor point. If PosAx and PosAy are both set to 1, the bottom-right corner of the logo is used as the anchor point.
        self.pos_ay = pos_ay
        # The horizontal position of the visible watermark. This parameter takes effect only when Mode is set to pos. The value is the pixel position with the top-left corner as the origin.
        self.pos_x = pos_x
        # The vertical position of the visible watermark. This parameter takes effect only when Mode is set to pos. The value is the pixel position with the top-left corner as the origin.
        self.pos_y = pos_y
        # The horizontal spacing of the tiled visible watermark. This parameter takes effect only when Mode is set to repeat.
        self.space_x = space_x
        # The vertical spacing of the tiled visible watermark. This parameter takes effect only when Mode is set to repeat.
        self.space_y = space_y
        # Specifies whether the logo watermark is visible. Valid values:
        # - **true**: Visible.
        # - **false**: Invisible.
        self.visible = visible

    def validate(self):
        if self.margin:
            self.margin.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.angle is not None:
            result['Angle'] = self.angle

        if self.enhance is not None:
            result['Enhance'] = self.enhance

        if self.logo_base_64 is not None:
            result['LogoBase64'] = self.logo_base_64

        if self.margin is not None:
            result['Margin'] = self.margin.to_map()

        if self.mode is not None:
            result['Mode'] = self.mode

        if self.opacity is not None:
            result['Opacity'] = self.opacity

        if self.pos_ax is not None:
            result['PosAx'] = self.pos_ax

        if self.pos_ay is not None:
            result['PosAy'] = self.pos_ay

        if self.pos_x is not None:
            result['PosX'] = self.pos_x

        if self.pos_y is not None:
            result['PosY'] = self.pos_y

        if self.space_x is not None:
            result['SpaceX'] = self.space_x

        if self.space_y is not None:
            result['SpaceY'] = self.space_y

        if self.visible is not None:
            result['Visible'] = self.visible

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Angle') is not None:
            self.angle = m.get('Angle')

        if m.get('Enhance') is not None:
            self.enhance = m.get('Enhance')

        if m.get('LogoBase64') is not None:
            self.logo_base_64 = m.get('LogoBase64')

        if m.get('Margin') is not None:
            temp_model = main_models.CreateWmEmbedTaskRequestImageControlLogoVisibleControlMargin()
            self.margin = temp_model.from_map(m.get('Margin'))

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('Opacity') is not None:
            self.opacity = m.get('Opacity')

        if m.get('PosAx') is not None:
            self.pos_ax = m.get('PosAx')

        if m.get('PosAy') is not None:
            self.pos_ay = m.get('PosAy')

        if m.get('PosX') is not None:
            self.pos_x = m.get('PosX')

        if m.get('PosY') is not None:
            self.pos_y = m.get('PosY')

        if m.get('SpaceX') is not None:
            self.space_x = m.get('SpaceX')

        if m.get('SpaceY') is not None:
            self.space_y = m.get('SpaceY')

        if m.get('Visible') is not None:
            self.visible = m.get('Visible')

        return self

class CreateWmEmbedTaskRequestImageControlLogoVisibleControlMargin(DaraModel):
    def __init__(
        self,
        bottom: float = None,
        left: float = None,
        right: float = None,
        top: float = None,
    ):
        # The bottom margin. This parameter takes effect only when Mode is set to bottom-left or bottom-right.
        self.bottom = bottom
        # The left margin. This parameter takes effect only when Mode is set to top-left or bottom-left.
        self.left = left
        # The right margin. This parameter takes effect only when Mode is set to top-right or bottom-right.
        self.right = right
        # The top margin. This parameter takes effect only when Mode is set to top-left or top-right.
        self.top = top

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bottom is not None:
            result['Bottom'] = self.bottom

        if self.left is not None:
            result['Left'] = self.left

        if self.right is not None:
            result['Right'] = self.right

        if self.top is not None:
            result['Top'] = self.top

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bottom') is not None:
            self.bottom = m.get('Bottom')

        if m.get('Left') is not None:
            self.left = m.get('Left')

        if m.get('Right') is not None:
            self.right = m.get('Right')

        if m.get('Top') is not None:
            self.top = m.get('Top')

        return self

class CreateWmEmbedTaskRequestDocumentControl(DaraModel):
    def __init__(
        self,
        background_control: main_models.CreateWmEmbedTaskRequestDocumentControlBackgroundControl = None,
        invisible_anti_all_copy: bool = None,
        invisible_anti_text_copy: bool = None,
    ):
        # The background watermark control parameters.
        self.background_control = background_control
        # Specifies whether to enable component invisible watermarks. Component invisible watermarks can resist document addition, deletion, modification, saving as another format (without changing the format), and selecting all and copying to a new docx document. They cannot resist format conversion attacks. Valid values:
        # 
        # - **true**: Yes.
        # - **false**: No.
        self.invisible_anti_all_copy = invisible_anti_all_copy
        # Specifies whether to enable zero-width character invisible watermarks. Zero-width character invisible watermarks can resist document addition, deletion, modification, saving as another format (without changing the format), partial text copy and paste, and CopytoTxt attacks. They cannot resist format conversion to PDF attacks. Valid values:
        # 
        # - **true**: Yes.
        # - **false**: No.
        self.invisible_anti_text_copy = invisible_anti_text_copy

    def validate(self):
        if self.background_control:
            self.background_control.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.background_control is not None:
            result['BackgroundControl'] = self.background_control.to_map()

        if self.invisible_anti_all_copy is not None:
            result['InvisibleAntiAllCopy'] = self.invisible_anti_all_copy

        if self.invisible_anti_text_copy is not None:
            result['InvisibleAntiTextCopy'] = self.invisible_anti_text_copy

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackgroundControl') is not None:
            temp_model = main_models.CreateWmEmbedTaskRequestDocumentControlBackgroundControl()
            self.background_control = temp_model.from_map(m.get('BackgroundControl'))

        if m.get('InvisibleAntiAllCopy') is not None:
            self.invisible_anti_all_copy = m.get('InvisibleAntiAllCopy')

        if m.get('InvisibleAntiTextCopy') is not None:
            self.invisible_anti_text_copy = m.get('InvisibleAntiTextCopy')

        return self

class CreateWmEmbedTaskRequestDocumentControlBackgroundControl(DaraModel):
    def __init__(
        self,
        bg_add_invisible: bool = None,
        bg_add_visible: bool = None,
        bg_invisible_control: main_models.CreateWmEmbedTaskRequestDocumentControlBackgroundControlBgInvisibleControl = None,
        bg_visible_control: main_models.CreateWmEmbedTaskRequestDocumentControlBackgroundControlBgVisibleControl = None,
    ):
        # Specifies whether to add an invisible background watermark. Valid values:
        # 
        # - **true**: Yes.
        # - **false**: No.
        self.bg_add_invisible = bg_add_invisible
        # Specifies whether to enable visible background watermarks. Valid values:
        # 
        # - **true**: Yes.
        # - **false**: No.
        self.bg_add_visible = bg_add_visible
        # The invisible background watermark control parameters.
        self.bg_invisible_control = bg_invisible_control
        # The visible background watermark control parameters.
        self.bg_visible_control = bg_visible_control

    def validate(self):
        if self.bg_invisible_control:
            self.bg_invisible_control.validate()
        if self.bg_visible_control:
            self.bg_visible_control.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bg_add_invisible is not None:
            result['BgAddInvisible'] = self.bg_add_invisible

        if self.bg_add_visible is not None:
            result['BgAddVisible'] = self.bg_add_visible

        if self.bg_invisible_control is not None:
            result['BgInvisibleControl'] = self.bg_invisible_control.to_map()

        if self.bg_visible_control is not None:
            result['BgVisibleControl'] = self.bg_visible_control.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BgAddInvisible') is not None:
            self.bg_add_invisible = m.get('BgAddInvisible')

        if m.get('BgAddVisible') is not None:
            self.bg_add_visible = m.get('BgAddVisible')

        if m.get('BgInvisibleControl') is not None:
            temp_model = main_models.CreateWmEmbedTaskRequestDocumentControlBackgroundControlBgInvisibleControl()
            self.bg_invisible_control = temp_model.from_map(m.get('BgInvisibleControl'))

        if m.get('BgVisibleControl') is not None:
            temp_model = main_models.CreateWmEmbedTaskRequestDocumentControlBackgroundControlBgVisibleControl()
            self.bg_visible_control = temp_model.from_map(m.get('BgVisibleControl'))

        return self

class CreateWmEmbedTaskRequestDocumentControlBackgroundControlBgVisibleControl(DaraModel):
    def __init__(
        self,
        angle: int = None,
        font_color: str = None,
        font_size: int = None,
        horizontal_number: int = None,
        mode: str = None,
        opacity: int = None,
        pos_x: str = None,
        pos_y: str = None,
        vertical_number: int = None,
        visible_text: str = None,
    ):
        # The counterclockwise rotation angle of the visible watermark text. Valid values: 1 to 360.
        self.angle = angle
        # The color of the visible watermark text. The format is 0xFFFFFF RGB color format. For example, 0x000000 indicates black.
        self.font_color = font_color
        # The font size of the visible watermark text. A larger value indicates a larger font size.
        self.font_size = font_size
        # This parameter takes effect when Mode is set to repeat. The number of times the visible watermark repeats horizontally.
        self.horizontal_number = horizontal_number
        # The visible background watermark mode. Valid values:
        # 
        # - **pos**: Embeds a single visible watermark text at a specific position in the background.
        # - **repeat**: Tiles and embeds multiple visible watermark texts in the document background.
        self.mode = mode
        # The opacity parameter of the visible watermark. Valid values: 1 to 255. A larger value indicates lower transparency.
        self.opacity = opacity
        # This parameter takes effect when Mode is set to pos. The parameter that controls the horizontal position of the visible watermark, with the lower-left corner as the origin. When the value is between 0 and 1, it controls the position by proportion. When the value is greater than 1, it controls the exact pixel position.
        self.pos_x = pos_x
        # This parameter takes effect when Mode is set to pos. The parameter that controls the vertical position of the visible watermark, with the lower-left corner as the origin. When the value is between 0 and 1, it controls the position by proportion. When the value is greater than 1, it controls the exact pixel position.
        self.pos_y = pos_y
        # This parameter takes effect when Mode is set to repeat. The number of times the visible watermark repeats vertically.
        self.vertical_number = vertical_number
        # The text of the visible background watermark. The format is a UTF-8 string.
        self.visible_text = visible_text

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.angle is not None:
            result['Angle'] = self.angle

        if self.font_color is not None:
            result['FontColor'] = self.font_color

        if self.font_size is not None:
            result['FontSize'] = self.font_size

        if self.horizontal_number is not None:
            result['HorizontalNumber'] = self.horizontal_number

        if self.mode is not None:
            result['Mode'] = self.mode

        if self.opacity is not None:
            result['Opacity'] = self.opacity

        if self.pos_x is not None:
            result['PosX'] = self.pos_x

        if self.pos_y is not None:
            result['PosY'] = self.pos_y

        if self.vertical_number is not None:
            result['VerticalNumber'] = self.vertical_number

        if self.visible_text is not None:
            result['VisibleText'] = self.visible_text

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Angle') is not None:
            self.angle = m.get('Angle')

        if m.get('FontColor') is not None:
            self.font_color = m.get('FontColor')

        if m.get('FontSize') is not None:
            self.font_size = m.get('FontSize')

        if m.get('HorizontalNumber') is not None:
            self.horizontal_number = m.get('HorizontalNumber')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('Opacity') is not None:
            self.opacity = m.get('Opacity')

        if m.get('PosX') is not None:
            self.pos_x = m.get('PosX')

        if m.get('PosY') is not None:
            self.pos_y = m.get('PosY')

        if m.get('VerticalNumber') is not None:
            self.vertical_number = m.get('VerticalNumber')

        if m.get('VisibleText') is not None:
            self.visible_text = m.get('VisibleText')

        return self

class CreateWmEmbedTaskRequestDocumentControlBackgroundControlBgInvisibleControl(DaraModel):
    def __init__(
        self,
        opacity: int = None,
    ):
        # The opacity parameter of the invisible background watermark. Valid values: 1 to 13. A larger value indicates lower transparency.
        self.opacity = opacity

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.opacity is not None:
            result['Opacity'] = self.opacity

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Opacity') is not None:
            self.opacity = m.get('Opacity')

        return self

class CreateWmEmbedTaskRequestCsvControl(DaraModel):
    def __init__(
        self,
        embed_bits_number_in_each_time: int = None,
        embed_column: int = None,
        embed_density: str = None,
        embed_precision: int = None,
        embed_time_position: str = None,
        method: str = None,
        time_format: str = None,
    ):
        # The bit width of the timestamp watermark information, which specifies how much information a single timestamp can hold. A larger value theoretically requires fewer rows to extract the information, but the time modification magnitude increases. The magnitude range is the nth power of 2, where n is the value of this parameter.
        self.embed_bits_number_in_each_time = embed_bits_number_in_each_time
        # The specified embedding column. We recommend that you use a string content column. The count starts from 1.
        self.embed_column = embed_column
        # The zero-width character watermark parameter that specifies the embedding density. The value is a floating-point number between 0 and 1. A value of 0 indicates that only the first row is embedded. A value of 1 indicates that all rows are embedded.
        self.embed_density = embed_density
        # The modification precision, which indicates the modification magnitude as the nth power of 10. For example, 0 indicates a modification precision of 10^0, which is the ones place. -1 indicates the first decimal place. 1 indicates the tens place. If the float data does not have this precision part, it is not modified.
        self.embed_precision = embed_precision
        # The timestamp watermark parameter that specifies the watermark embedding position. Valid values: Min (minute), Sec (second), and MilSec (millisecond). You can specify only one of them. The algorithm modifies the data at the specified position.
        self.embed_time_position = embed_time_position
        # The watermark embedding method. Valid values:
        # 
        # - **lossless_row_shift_embed**: Lossless data method.
        # - **lossy_number_embed**: Lossy data method.
        # - **lossy_time_stamp_embed**: Timestamp method.
        # - **lossy_zero_width_embed**: Zero-width character method.
        self.method = method
        # The timestamp watermark parameter that specifies the format string for parsing timestamps in the CSV file. For example, if the timestamp in the CSV file is similar to "2023-10-15 13:20:59:342", the corresponding format string is "Year-Mon-Day Hour:Min:Sec.MilSec". You must enter "Year-Mon-Day Hour:Min:Sec.MilSec" here. After the watermark is embedded, the output still follows this format. If you enter it incorrectly, this method cannot be used. The year, month, day, hour, minute, second, and millisecond in the format string must be written as described above. The connector must be a single non-character English connector, which can generally be ":", "/", "-", or " " (space). "T" and "Z" are also supported as connectors. Other time formats are not supported for parsing.
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

        if self.embed_density is not None:
            result['EmbedDensity'] = self.embed_density

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

        if m.get('EmbedDensity') is not None:
            self.embed_density = m.get('EmbedDensity')

        if m.get('EmbedPrecision') is not None:
            self.embed_precision = m.get('EmbedPrecision')

        if m.get('EmbedTimePosition') is not None:
            self.embed_time_position = m.get('EmbedTimePosition')

        if m.get('Method') is not None:
            self.method = m.get('Method')

        if m.get('TimeFormat') is not None:
            self.time_format = m.get('TimeFormat')

        return self

class CreateWmEmbedTaskRequestAudioControl(DaraModel):
    def __init__(
        self,
        metadata_control: main_models.CreateWmEmbedTaskRequestAudioControlMetadataControl = None,
    ):
        # The audio metadata control parameters.
        self.metadata_control = metadata_control

    def validate(self):
        if self.metadata_control:
            self.metadata_control.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.metadata_control is not None:
            result['MetadataControl'] = self.metadata_control.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MetadataControl') is not None:
            temp_model = main_models.CreateWmEmbedTaskRequestAudioControlMetadataControl()
            self.metadata_control = temp_model.from_map(m.get('MetadataControl'))

        return self

class CreateWmEmbedTaskRequestAudioControlMetadataControl(DaraModel):
    def __init__(
        self,
        enable: bool = None,
        xmp_kv_base_64: str = None,
    ):
        # Specifies whether to enable the metadata. Valid values:
        # - **false**: Disabled.
        # - **true**: Enabled.
        self.enable = enable
        # The Base64-encoded metadata. You must encode a string in the format of AIGC={"Label":"1","ContentProducer":"AXXXX","ProduceID":"BXXXX","ReservedCode1":"CXXX","ContentPropagator":"DXXX","PropagateID":"EXXX","ReservedCode2":"FXXXX"} into a Base64 string. Note: 1. The "AIGC=" prefix is required. Otherwise, the metadata cannot be added. Note that the prefix is different from that of image metadata. 2. The Base64 string must be in the standard format and include padding.
        self.xmp_kv_base_64 = xmp_kv_base_64

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable is not None:
            result['Enable'] = self.enable

        if self.xmp_kv_base_64 is not None:
            result['XmpKvBase64'] = self.xmp_kv_base_64

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('XmpKvBase64') is not None:
            self.xmp_kv_base_64 = m.get('XmpKvBase64')

        return self

