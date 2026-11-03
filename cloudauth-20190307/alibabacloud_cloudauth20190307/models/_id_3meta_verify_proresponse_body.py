# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cloudauth20190307 import models as main_models
from darabonba.model import DaraModel

class Id3MetaVerifyPROResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result_object: main_models.Id3MetaVerifyPROResponseBodyResultObject = None,
    ):
        # The return code. A value of **200** indicates that the API call is successful.
        self.code = code
        # The message returned for the API call.
        # >Notice: This parameter only indicates whether an exception occurs during the API call.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The returned result.
        self.result_object = result_object

    def validate(self):
        if self.result_object:
            self.result_object.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result_object is not None:
            result['ResultObject'] = self.result_object.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResultObject') is not None:
            temp_model = main_models.Id3MetaVerifyPROResponseBodyResultObject()
            self.result_object = temp_model.from_map(m.get('ResultObject'))

        return self

class Id3MetaVerifyPROResponseBodyResultObject(DaraModel):
    def __init__(
        self,
        biz_code: str = None,
        face_detail: str = None,
        hit_whitelist: str = None,
        sub_code: str = None,
    ):
        # The verification result from the authoritative source. Valid values:
        # 
        # - **1**: Consistent (billed).
        # - **2**: Inconsistent (billed).
        # - **3**: No record found (not billed).
        self.biz_code = biz_code
        # - **verifyScore**: The face comparison score. Valid values: 0 to 1000. A higher score indicates a higher probability that the faces belong to the same person. A score of 700.0 or higher confirms that the faces belong to the same person.
        # 
        # - **faceAttack**: Returned when liveness detection is enabled. This value does not affect the verification result.
        # 
        # - **invokeChannel**: The identifier of the actual invocation channel. Valid values:
        # 1: Authoritative source. 0: Comprehensive source.
        self.face_detail = face_detail
        # Indicates whether the whitelist is hit. Valid value: **Y**.
        self.hit_whitelist = hit_whitelist
        # The verification details from the authoritative source. Valid values:
        # 
        # - **101**: Authentication passed.
        # 
        # - **201**: Authentication failed. The name does not match the ID card number.
        # 
        # - **202**: Authentication failed. The person is suspected to be the ID owner.
        # 
        # - **203**: Authentication failed. No photo is found in the database.
        # 
        # - **204**: Authentication failed. The faces do not belong to the same person.
        # 
        # - **205**: Authentication failed. Image modeling for the image to be compared failed.
        # 
        # - **206**: Authentication failed. The image format is incorrect.
        # 
        # - **207**: Authentication failed. The uploaded image is too small. Upload another image.
        # 
        # - **208**: Authentication failed. The quality of the uploaded face photo is poor. Upload another photo.
        # 
        # - **301**: No record found. The ID card number does not exist in the database.
        # 
        # - **302**: No record found. Verification cannot be performed.
        self.sub_code = sub_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_code is not None:
            result['BizCode'] = self.biz_code

        if self.face_detail is not None:
            result['FaceDetail'] = self.face_detail

        if self.hit_whitelist is not None:
            result['HitWhitelist'] = self.hit_whitelist

        if self.sub_code is not None:
            result['SubCode'] = self.sub_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')

        if m.get('FaceDetail') is not None:
            self.face_detail = m.get('FaceDetail')

        if m.get('HitWhitelist') is not None:
            self.hit_whitelist = m.get('HitWhitelist')

        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')

        return self

