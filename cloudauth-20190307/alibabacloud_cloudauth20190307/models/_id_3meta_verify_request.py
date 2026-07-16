# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class Id3MetaVerifyRequest(DaraModel):
    def __init__(
        self,
        crop: str = None,
        face_file: str = None,
        face_picture: str = None,
        face_url: str = None,
        identify_num: str = None,
        param_type: str = None,
        user_name: str = None,
    ):
        # Specifies whether to allow cropping of the facial photo. By default, cropping is not allowed. Valid values:
        # - T: Cropping is allowed.
        # - F: Cropping is not allowed.
        # 
        # **Note**
        # 
        # If the requested image is not captured by a standard liveness detection SDK, allow cropping of the facial photo. After this feature is enabled, the requested image is first cropped and corrected for the face before the request is sent to the service.
        self.crop = crop
        # The input stream of the ID card portrait side photo. Specify either CertUrl or CertFile.
        self.face_file = face_file
        self.face_picture = face_picture
        # The photo of the ID card portrait side. Specify a publicly accessible HTTP or HTTPS URL. Specify either CertUrl or CertFile.
        self.face_url = face_url
        # The ID card number:
        # - If paramType is set to normal: enter the ID card number in plaintext.
        # - If paramType is set to md5: the first 6 digits of the ID card number (plaintext) + date of birth (ciphertext) + the last 4 digits of the ID card number (plaintext).
        self.identify_num = identify_num
        # The encryption method. Valid values:
        # - normal: plaintext without encryption
        # - md5: MD5 encryption
        # 
        # **Important**
        # 
        # - All encrypted parameter values use 32-character lowercase MD5 strings.
        # - Different MD5 tools may produce different ciphertext. If the API call succeeds with plaintext but fails after encryption, try a different MD5 tool.
        self.param_type = param_type
        # The name:
        # - If paramType is set to normal: enter the name in plaintext.
        # - If paramType is set to md5: the first character of the name (ciphertext) + the remaining characters of the name (plaintext).
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

        if self.face_file is not None:
            result['FaceFile'] = self.face_file

        if self.face_picture is not None:
            result['FacePicture'] = self.face_picture

        if self.face_url is not None:
            result['FaceUrl'] = self.face_url

        if self.identify_num is not None:
            result['IdentifyNum'] = self.identify_num

        if self.param_type is not None:
            result['ParamType'] = self.param_type

        if self.user_name is not None:
            result['UserName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Crop') is not None:
            self.crop = m.get('Crop')

        if m.get('FaceFile') is not None:
            self.face_file = m.get('FaceFile')

        if m.get('FacePicture') is not None:
            self.face_picture = m.get('FacePicture')

        if m.get('FaceUrl') is not None:
            self.face_url = m.get('FaceUrl')

        if m.get('IdentifyNum') is not None:
            self.identify_num = m.get('IdentifyNum')

        if m.get('ParamType') is not None:
            self.param_type = m.get('ParamType')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

