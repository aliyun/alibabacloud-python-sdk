# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class Id3MetaVerifyPRORequest(DaraModel):
    def __init__(
        self,
        crop: str = None,
        enable_fallback: str = None,
        face_file: str = None,
        face_picture: str = None,
        face_url: str = None,
        identify_num: str = None,
        liveness_check: str = None,
        param_type: str = None,
        user_name: str = None,
    ):
        # Specifies whether to allow cropping of the facial photo. By default, cropping is not allowed. Valid values:
        # - **T**: Cropping is allowed.
        # - **F**: Cropping is not allowed.
        # > If the requested image is not captured by a standard liveness detection SDK, allow cropping of the facial photo.
        # After this feature is enabled, the requested image is first cropped and corrected for the face, and then the request is sent to the service.
        self.crop = crop
        # Specifies whether to allow fallback to a non-public security source. Valid values:
        # 
        # - **N** (default): Disabled.
        # - **Y**: Enabled.
        self.enable_fallback = enable_fallback
        # The input stream of the facial photo.
        self.face_file = face_file
        # The Base64-encoded photo. If you use this method to submit the facial photo, check the photo size and do not submit an excessively large photo.
        self.face_picture = face_picture
        # The URL of the facial photo. The URL must be a publicly accessible HTTP or HTTPS link.
        self.face_url = face_url
        # The ID card number.
        # 
        # - If **paramType** is set to normal: Enter the ID card number in plaintext.
        # 
        # - If **paramType** is set to sm2: Enter the encrypted ID card number.
        # 
        # 
        # > Due to authoritative source limitations, only second-generation resident ID card numbers are supported.
        self.identify_num = identify_num
        # Specifies whether to enable liveness detection. Valid values:
        # 
        # - **N** (default): Liveness detection is disabled.
        # - **Y**: Liveness detection is enabled.
        self.liveness_check = liveness_check
        # The encryption method. Valid values:
        # 
        # - **normal**: Plaintext without encryption.
        # 
        # - **sm2**: SM2 encryption.
        self.param_type = param_type
        # The name.
        # 
        # - If **paramType** is set to normal: Enter the name in plaintext.
        # 
        # - If **paramType** is set to sm2: Enter the encrypted name.
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.crop is not None:
            result['Crop'] = self.crop

        if self.enable_fallback is not None:
            result['EnableFallback'] = self.enable_fallback

        if self.face_file is not None:
            result['FaceFile'] = self.face_file

        if self.face_picture is not None:
            result['FacePicture'] = self.face_picture

        if self.face_url is not None:
            result['FaceUrl'] = self.face_url

        if self.identify_num is not None:
            result['IdentifyNum'] = self.identify_num

        if self.liveness_check is not None:
            result['LivenessCheck'] = self.liveness_check

        if self.param_type is not None:
            result['ParamType'] = self.param_type

        if self.user_name is not None:
            result['UserName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Crop') is not None:
            self.crop = m.get('Crop')

        if m.get('EnableFallback') is not None:
            self.enable_fallback = m.get('EnableFallback')

        if m.get('FaceFile') is not None:
            self.face_file = m.get('FaceFile')

        if m.get('FacePicture') is not None:
            self.face_picture = m.get('FacePicture')

        if m.get('FaceUrl') is not None:
            self.face_url = m.get('FaceUrl')

        if m.get('IdentifyNum') is not None:
            self.identify_num = m.get('IdentifyNum')

        if m.get('LivenessCheck') is not None:
            self.liveness_check = m.get('LivenessCheck')

        if m.get('ParamType') is not None:
            self.param_type = m.get('ParamType')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

