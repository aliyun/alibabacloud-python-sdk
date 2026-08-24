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
        # The height of the watermark image, in pixels. Valid values: 100 to 5000.
        # 
        # This parameter is required.
        self.height = height
        # The image watermark control parameters.
        self.image_control = image_control
        # The opacity of the watermark image. Valid values: 1 to 255. A larger value indicates lower transparency.
        # 
        # This parameter is required.
        self.opacity = opacity
        # The scaling ratio of the watermark image.
        # 
        # This parameter is required.
        self.scale = scale
        # The width of the watermark image, in pixels. Valid values: 100 to 5000.
        # 
        # This parameter is required.
        self.width = width
        # The watermark information in Base64-encoded string format. The length is 1 to 300 characters. If this parameter is set, the WmInfoUint parameter cannot be set.
        self.wm_info_bytes_b64 = wm_info_bytes_b64
        # The bit width of the watermark information capacity. Default value: 32. This parameter must be consistent between embedding and extraction. For example, if the SDK used for embedding is 40-bit, set this parameter to 40 during extraction as well.
        self.wm_info_size = wm_info_size
        # The watermark information in decimal number format. If this parameter is set, WmInfoBytesB64 cannot be set.
        # 
        # The valid range depends on the WmInfoSize parameter:
        # 
        # - If WmInfoSize is **32**, the valid range is 1 to 4294967295.
        # 
        # - If WmInfoSize is **40**, the valid range is 1 to 1099511627775.
        # 
        # - If WmInfoSize is **64**, the valid range is 1 to 18446744073709551615.
        self.wm_info_uint = wm_info_uint
        # The watermark type. Valid values:
        # - **PureWebappInvisible**: web watermark.
        # - **PureAppInvisible**: App watermark.
        # - **PureScreenInvisible**: screen watermark.
        # - **AigcWebappInvisible**: AIGC web watermark.
        # - **AigcAppInvisible**: AIGC App watermark.
        # - **AigcScreenInvisible**: AIGC screen watermark.
        # 
        # This parameter is required.
        self.wm_type = wm_type
        # The remarks.
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
        # The logo watermark control parameters.
        self.logo_visible_control = logo_visible_control
        # The text watermark control parameters for the image.
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
        # The clockwise rotation angle of the text watermark. Valid values: 0 to 360.
        self.angle = angle
        # The font color of the text watermark. The format is 0xFFFFFF or #FFFFFF RGB color format. For example, 0x000000 or #000000 represents black.
        self.font_color = font_color
        # The font size of the text watermark. A larger value indicates a larger font.
        self.font_size = font_size
        # Takes effect when Mode is set to top-left, top-right, bottom-left, or bottom-right. The margin settings.
        self.margin = margin
        # The text watermark display mode. Valid values:
        # - **pos**: fixed position mode.
        # - **repeat**: tile mode.
        self.mode = mode
        # The opacity of the text watermark. Valid values: 1 to 255. A larger value indicates lower transparency.
        self.opacity = opacity
        # The horizontal anchor point of the text watermark. Valid values: 0 to 1. When (PosAx, PosAy) is set to (0, 0), the text is drawn from the upper-left corner. When set to 0.5, the text is drawn from the center. When set to (1, 1), the text is drawn from the lower-right corner.
        self.pos_ax = pos_ax
        # The vertical anchor point of the text watermark. Valid values: 0 to 1. When (PosAx, PosAy) is set to (0, 0), the text is drawn from the upper-left corner. When set to 0.5, the text is drawn from the center. When set to (1, 1), the text is drawn from the lower-right corner.
        self.pos_ay = pos_ay
        # Takes effect when Mode is set to pos. Specifies the horizontal position of the text watermark in pixels, with the upper-left corner as the origin.
        self.pos_x = pos_x
        # Takes effect when Mode is set to pos. Specifies the vertical position of the text watermark in pixels, with the upper-left corner as the origin.
        self.pos_y = pos_y
        # Takes effect when Mode is set to repeat. Specifies the horizontal spacing for tiled text watermarks.
        self.space_x = space_x
        # Takes effect when Mode is set to repeat. Specifies the vertical spacing for tiled text watermarks.
        self.space_y = space_y
        # The visibility. Valid values:
        # 
        # - **true**: displayed.
        # 
        # - **false**: not displayed.
        self.visible = visible
        # The text watermark content. The format is a UTF-8 string.
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
        # Takes effect when Mode is set to bottom-left or bottom-right. The bottom margin.
        self.bottom = bottom
        # Takes effect when Mode is set to top-left or bottom-left. The left margin.
        self.left = left
        # Takes effect when Mode is set to top-right or bottom-right. The right margin.
        self.right = right
        # Takes effect when Mode is set to top-left or top-right. The top margin.
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
        # The clockwise rotation angle of the logo watermark. Valid values: 1 to 360.
        self.angle = angle
        # Specifies whether to enable enhanced visible watermark. When enabled, the logo is converted to a watermark logo and added to the image.
        self.enhance = enhance
        # The logo watermark in Base64 format. The logo file is a PNG image converted to Base64 format.
        self.logo_base_64 = logo_base_64
        # Takes effect when Mode is set to top-left, top-right, bottom-left, or bottom-right. The margin settings.
        self.margin = margin
        # The logo watermark display mode. Valid values:
        # - **pos**: fixed position mode.
        # - **repeat**: tile mode.
        self.mode = mode
        # The opacity of the logo watermark. Valid values: 1 to 255. A larger value indicates lower transparency.
        self.opacity = opacity
        # The horizontal anchor point of the logo watermark. Valid values: 0 to 1. When (PosAx, PosAy) is set to (0, 0), the logo is drawn from the upper-left corner. When set to 0.5, the logo is drawn from the center. When set to (1, 1), the logo is drawn from the lower-right corner.
        self.pos_ax = pos_ax
        # The vertical anchor point of the logo watermark. Valid values: 0 to 1. When (PosAx, PosAy) is set to (0, 0), the logo is drawn from the upper-left corner. When set to 0.5, the logo is drawn from the center. When set to (1, 1), the logo is drawn from the lower-right corner.
        self.pos_ay = pos_ay
        # Takes effect when Mode is set to pos. Specifies the horizontal position of the visible watermark in pixels, with the upper-left corner as the origin.
        self.pos_x = pos_x
        # Takes effect when Mode is set to pos. Specifies the vertical position of the visible watermark in pixels, with the upper-left corner as the origin.
        self.pos_y = pos_y
        # Takes effect when Mode is set to repeat. Specifies the horizontal spacing for tiled visible watermarks.
        self.space_x = space_x
        # Takes effect when Mode is set to repeat. Specifies the vertical spacing for tiled visible watermarks.
        self.space_y = space_y
        # The visibility. Valid values:
        # 
        # - **true**: displayed.
        # 
        # - **false**: not displayed.
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
        # Takes effect when Mode is set to bottom-left or bottom-right. The bottom margin.
        self.bottom = bottom
        # Takes effect when Mode is set to top-left or bottom-left. The left margin.
        self.left = left
        # Takes effect when Mode is set to top-right or bottom-right. The right margin.
        self.right = right
        # Takes effect when Mode is set to top-left or top-right. The top margin.
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

