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
        # The response code. **200** indicates that the API call is successful.
        self.code = code
        # The response message of the API call.
        # >Notice: This parameter only indicates whether the API call is abnormal.
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
        # The authoritative source verification result. Valid values:
        # 
        # - **1**: Verification is consistent (billable).
        # - **2**: Verification is inconsistent (billable).
        # - **3**: No record found (not billable).
        self.biz_code = biz_code
        # - **verifyScore**: The face comparison score. Value range: 0 to 1000. A higher score indicates a higher probability of the same face. A score >= 700.0 confirms the same person.
        # 
        # - **faceAttack**: Returned when liveness detection is enabled (does not participate in the verification result decision).
        # 
        # - **invokeChannel**: The identifier of the actual invocation channel. 1: authoritative source. 0: comprehensive source.
        self.face_detail = face_detail
        # Indicates whether the whitelist is hit: **Y**.
        self.hit_whitelist = hit_whitelist
        # The authoritative source verification details. Valid values:
        # 
        # - **101**: Authentication passed.
        # 
        # - **201**: Authentication failed. The name does not match the ID card number.
        # 
        # - **202**: Authentication failed. Suspected to be the person.
        # 
        # - **203**: Authentication failed. No photo in the database.
        # 
        # - **204**: Authentication failed. Not the same person.
        # 
        # - **205**: Authentication failed. Modeling of the image to be compared failed.
        # 
        # - **206**: Authentication failed. The image format is incorrect.
        # 
        # - **207**: Authentication failed. The uploaded image is too small. Upload the image again.
        # 
        # - **208**: Authentication failed. The quality of the uploaded portrait photo is poor. Upload the photo again.
        # 
        # - **301**: No record found. The ID number does not exist in the database.
        # 
        # - **302**: No record found. Verification is not possible.
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

