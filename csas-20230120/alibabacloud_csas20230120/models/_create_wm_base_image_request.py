# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_csas20230120 import models as main_models
from darabonba.model import DaraModel

class CreateWmBaseImageRequest(DaraModel):
    def __init__(
        self,
        height: int = None,
        image_control: main_models.CreateWmBaseImageRequestImageControl = None,
        opacity: int = None,
        scale: int = None,
        width: int = None,
        wm_info_bytes_b64: str = None,
        wm_info_size: int = None,
        wm_info_uint: str = None,
        wm_type: str = None,
        comment: str = None,
    ):
        # Height of the watermark image, in pixels. Valid values: 100 to 5000.
        # 
        # This parameter is required.
        self.height = height
        # Image watermark control parameters.
        self.image_control = image_control
        # Opacity of the watermark image. Valid values: 1 to 255. Higher values mean lower transparency.
        # 
        # This parameter is required.
        self.opacity = opacity
        # Scaling factor of the watermark image.
        # 
        # This parameter is required.
        self.scale = scale
        # Width of the watermark image, in pixels. Valid values: 100 to 5000.
        # 
        # This parameter is required.
        self.width = width
        # Base64-encoded watermark information. Length: 1 to 300 characters. Do not set this parameter if you set WmInfoUint.
        self.wm_info_bytes_b64 = wm_info_bytes_b64
        # Bit width of the watermark information. Default value: 32. This value must be the same during embedding and extraction. For example, if you use a 40-bit SDK to embed the watermark, set this value to 40 when extracting it.
        self.wm_info_size = wm_info_size
        # Decimal-form watermark information. Do not set this parameter if you set WmInfoBytesB64.
        # 
        # The valid range depends on the WmInfoSize value:
        # 
        # - If WmInfoSize is **32**, the valid range is 1 to 4294967295.
        # 
        # - If WmInfoSize is **40**, the valid range is 1 to 1099511627775.
        # 
        # - If WmInfoSize is **64**, the valid range is 1 to 18446744073709551615.
        self.wm_info_uint = wm_info_uint
        # Watermark type. Valid values:
        # 
        # - **PureWebappInvisible**: Web watermark.
        # 
        # - **PureAppInvisible**: App watermark.
        # 
        # - **PureScreenInvisible**: Screen watermark.
        # 
        # - **AigcWebappInvisible**: AIGC web watermark.
        # 
        # - **AigcAppInvisible**: AIGC app watermark.
        # 
        # - **AigcScreenInvisible**: AIGC screen watermark.
        # 
        # This parameter is required.
        self.wm_type = wm_type
        # Comments.
        self.comment = comment

    def validate(self):
        if self.image_control:
            self.image_control.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.height is not None:
            result['Height'] = self.height

        if self.image_control is not None:
            result['ImageControl'] = self.image_control.to_map()

        if self.opacity is not None:
            result['Opacity'] = self.opacity

        if self.scale is not None:
            result['Scale'] = self.scale

        if self.width is not None:
            result['Width'] = self.width

        if self.wm_info_bytes_b64 is not None:
            result['WmInfoBytesB64'] = self.wm_info_bytes_b64

        if self.wm_info_size is not None:
            result['WmInfoSize'] = self.wm_info_size

        if self.wm_info_uint is not None:
            result['WmInfoUint'] = self.wm_info_uint

        if self.wm_type is not None:
            result['WmType'] = self.wm_type

        if self.comment is not None:
            result['comment'] = self.comment

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Height') is not None:
            self.height = m.get('Height')

        if m.get('ImageControl') is not None:
            temp_model = main_models.CreateWmBaseImageRequestImageControl()
            self.image_control = temp_model.from_map(m.get('ImageControl'))

        if m.get('Opacity') is not None:
            self.opacity = m.get('Opacity')

        if m.get('Scale') is not None:
            self.scale = m.get('Scale')

        if m.get('Width') is not None:
            self.width = m.get('Width')

        if m.get('WmInfoBytesB64') is not None:
            self.wm_info_bytes_b64 = m.get('WmInfoBytesB64')

        if m.get('WmInfoSize') is not None:
            self.wm_info_size = m.get('WmInfoSize')

        if m.get('WmInfoUint') is not None:
            self.wm_info_uint = m.get('WmInfoUint')

        if m.get('WmType') is not None:
            self.wm_type = m.get('WmType')

        if m.get('comment') is not None:
            self.comment = m.get('comment')

        return self

class CreateWmBaseImageRequestImageControl(DaraModel):
    def __init__(
        self,
        logo_visible_control: main_models.CreateWmBaseImageRequestImageControlLogoVisibleControl = None,
        text_visible_control: main_models.CreateWmBaseImageRequestImageControlTextVisibleControl = None,
    ):
        # Logo watermark control parameters.
        self.logo_visible_control = logo_visible_control
        # Text watermark control parameters.
        self.text_visible_control = text_visible_control

    def validate(self):
        if self.logo_visible_control:
            self.logo_visible_control.validate()
        if self.text_visible_control:
            self.text_visible_control.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.logo_visible_control is not None:
            result['LogoVisibleControl'] = self.logo_visible_control.to_map()

        if self.text_visible_control is not None:
            result['TextVisibleControl'] = self.text_visible_control.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogoVisibleControl') is not None:
            temp_model = main_models.CreateWmBaseImageRequestImageControlLogoVisibleControl()
            self.logo_visible_control = temp_model.from_map(m.get('LogoVisibleControl'))

        if m.get('TextVisibleControl') is not None:
            temp_model = main_models.CreateWmBaseImageRequestImageControlTextVisibleControl()
            self.text_visible_control = temp_model.from_map(m.get('TextVisibleControl'))

        return self

class CreateWmBaseImageRequestImageControlTextVisibleControl(DaraModel):
    def __init__(
        self,
        angle: int = None,
        font_color: str = None,
        font_size: int = None,
        margin: main_models.CreateWmBaseImageRequestImageControlTextVisibleControlMargin = None,
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
        # Rotation angle of the text watermark, in degrees clockwise. Valid values: 0 to 360.
        self.angle = angle
        # Text watermark color. Format: RGB, such as 0xFFFFFF or #FFFFFF. For example, 0x000000 or #000000 means black.
        self.font_color = font_color
        # Font size of the text watermark. Larger values produce larger fonts.
        self.font_size = font_size
        # Takes effect only when Mode is top-left, top-right, bottom-left, or bottom-right. Margin settings.
        self.margin = margin
        # Text watermark display mode. Valid values:
        # 
        # - **pos**: Fixed position mode.
        # 
        # - **repeat**: Tiled mode.
        self.mode = mode
        # Text watermark opacity. Valid values: 1 to 255. Higher values mean less transparency.
        self.opacity = opacity
        # Horizontal anchor point for the text watermark. Valid values: 0 to 1. When (PosAx, PosAy) is (0, 0), the top-left corner of the text is used as the anchor point. When it is 0.5, the center point is used. When it is (1, 1), the bottom-right corner is used.
        self.pos_ax = pos_ax
        # Vertical anchor point for the text watermark. Valid values: 0 to 1. When (PosAx, PosAy) is (0, 0), the top-left corner of the text is used as the anchor point. When it is 0.5, the center point is used. When it is (1, 1), the bottom-right corner is used.
        self.pos_ay = pos_ay
        # Takes effect only when Mode is pos. Horizontal position of the text watermark, measured in pixels from the top-left corner.
        self.pos_x = pos_x
        # Takes effect only when Mode is pos. Vertical position of the text watermark, measured in pixels from the top-left corner.
        self.pos_y = pos_y
        # Takes effect only when Mode is repeat. Horizontal spacing between repeated text watermarks.
        self.space_x = space_x
        # Takes effect only when Mode is repeat. Vertical spacing between repeated text watermarks.
        self.space_y = space_y
        # Visibility setting:
        # 
        # true: Show the watermark.
        # 
        # false: Hide the watermark.
        self.visible = visible
        # Text watermark content. Format: UTF-8 string.
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
            temp_model = main_models.CreateWmBaseImageRequestImageControlTextVisibleControlMargin()
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

class CreateWmBaseImageRequestImageControlTextVisibleControlMargin(DaraModel):
    def __init__(
        self,
        bottom: float = None,
        left: float = None,
        right: float = None,
        top: float = None,
    ):
        # Takes effect only when Mode is bottom-left or bottom-right. Bottom margin.
        self.bottom = bottom
        # Takes effect only when Mode is top-left or bottom-left. Left margin.
        self.left = left
        # Takes effect only when Mode is top-right or bottom-right. Right margin.
        self.right = right
        # Takes effect only when Mode is top-left or top-right. Top margin.
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

class CreateWmBaseImageRequestImageControlLogoVisibleControl(DaraModel):
    def __init__(
        self,
        angle: int = None,
        enhance: bool = None,
        logo_base_64: str = None,
        margin: main_models.CreateWmBaseImageRequestImageControlLogoVisibleControlMargin = None,
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
        # The clockwise rotation angle of the logo watermark text. Valid values: 1 to 360.
        self.angle = angle
        # Enable enhanced visible logo watermark. If enabled, the logo is converted into a watermark and added to the image.
        self.enhance = enhance
        # Base64-encoded logo watermark. The logo file must be a PNG image encoded in Base64 format.
        self.logo_base_64 = logo_base_64
        # Applies when Mode is top-left, top-right, bottom-left, or bottom-right. Specifies the margin.
        self.margin = margin
        # The display mode for the logo watermark. Valid values:
        # 
        # - **pos**: Fixed position pattern.
        # 
        # - **repeat**: Tile pattern.
        self.mode = mode
        # Logo watermark opacity. Valid values: 1 to 255. A higher value means lower transparency.
        self.opacity = opacity
        # The horizontal anchor point for the logo watermark. Valid values: 0 to 1. When (PosAx, PosAy) is (0, 0), the watermark anchors to the top-left corner of the text. When the value is 0.5, the watermark anchors to the centroid of the text. When (PosAx, PosAy) is (1, 1), the watermark anchors to the bottom-right corner of the text.
        self.pos_ax = pos_ax
        # The vertical anchor point for the logo watermark. The value ranges from 0 to 1. The coordinates (PosAx, PosAy) define the anchor point on the watermark. For example, (0,0) represents the top-left corner, (0.5, 0.5) represents the centroid, and (1,1) represents the bottom-right corner.
        self.pos_ay = pos_ay
        # Takes effect when Mode is set to pos. This parameter controls the horizontal position of a visible watermark, using pixel coordinates with the top-left corner as the origin.
        self.pos_x = pos_x
        # Specifies the vertical position of the visible watermark in pixels. The top-left corner is the origin. This parameter is valid only when Mode is set to pos.
        self.pos_y = pos_y
        # This parameter takes effect when Mode is set to repeat. It specifies the horizontal pitch for the tiled visible watermark.
        self.space_x = space_x
        # Applies only when Mode is set to repeat. Controls the vertical pitch between tiled visible watermarks.
        self.space_y = space_y
        # Visibility:
        # 
        # **true**: Display
        # 
        # **false**: Hide
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
            temp_model = main_models.CreateWmBaseImageRequestImageControlLogoVisibleControlMargin()
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

class CreateWmBaseImageRequestImageControlLogoVisibleControlMargin(DaraModel):
    def __init__(
        self,
        bottom: float = None,
        left: float = None,
        right: float = None,
        top: float = None,
    ):
        # Applies when Mode is bottom-left or bottom-right. The bottom margin.
        self.bottom = bottom
        # Applies when Mode is top-left or bottom-left. The left margin.
        self.left = left
        # The right margin. This parameter is valid only when Mode is set to top-right or bottom-right.
        self.right = right
        # Applies when Mode is top-left or top-right. The top margin.
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

