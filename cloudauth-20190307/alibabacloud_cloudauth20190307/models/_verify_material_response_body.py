# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cloudauth20190307 import models as main_models
from darabonba.model import DaraModel

class VerifyMaterialResponseBody(DaraModel):
    def __init__(
        self,
        authority_comparision_score: float = None,
        id_card_face_comparison_score: float = None,
        material: main_models.VerifyMaterialResponseBodyMaterial = None,
        request_id: str = None,
        verify_status: int = None,
        verify_token: str = None,
    ):
        # The comparison score between the submitted face photo and the authoritative data during the authentication process. Valid values: **0** to **100**.
        # 
        # Refer to the following confidence thresholds:
        # - When the false acceptance rate (FAR) is 0.001%, the corresponding threshold is 95.
        # - When the FAR is 0.01%, the corresponding threshold is 90.
        # - When the FAR is 0.1%, the corresponding threshold is 80.
        # - When the FAR is 1%, the corresponding threshold is 60.
        # 
        # > This field only indicates the comparison result between the face and the authoritative data and serves as a reference score. Do not use this score alone as the pass or fail criterion. For the comprehensive authentication result, refer to the **VerifyStatus** field. The **VerifyStatus** result combines the face and authoritative data comparison with various other strategies to improve the security level.
        self.authority_comparision_score = authority_comparision_score
        # The comparison score between the submitted face photo and the face on the front side of the ID card during the authentication process. Valid values: **0** to **100**.
        # 
        # Refer to the following confidence thresholds:
        # - When the false acceptance rate (FAR) is 0.001%, the corresponding threshold is 95.
        # - When the FAR is 0.01%, the corresponding threshold is 90.
        # - When the FAR is 0.1%, the corresponding threshold is 80.
        # - When the FAR is 1%, the corresponding threshold is 60.
        self.id_card_face_comparison_score = id_card_face_comparison_score
        # The authentication materials.
        self.material = material
        # The request ID.
        self.request_id = request_id
        # The authentication status. Valid values:
        # 
        # - **1**: The authentication is passed.
        # - **2** to **n**: The authentication fails due to various reasons. For detailed descriptions, see **Authentication status description** below.
        self.verify_status = verify_status
        # The token for this authentication. It is used to link various APIs in the authentication request and is valid for 30 minutes.
        self.verify_token = verify_token

    def validate(self):
        if self.material:
            self.material.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.authority_comparision_score is not None:
            result['AuthorityComparisionScore'] = self.authority_comparision_score

        if self.id_card_face_comparison_score is not None:
            result['IdCardFaceComparisonScore'] = self.id_card_face_comparison_score

        if self.material is not None:
            result['Material'] = self.material.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.verify_status is not None:
            result['VerifyStatus'] = self.verify_status

        if self.verify_token is not None:
            result['VerifyToken'] = self.verify_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorityComparisionScore') is not None:
            self.authority_comparision_score = m.get('AuthorityComparisionScore')

        if m.get('IdCardFaceComparisonScore') is not None:
            self.id_card_face_comparison_score = m.get('IdCardFaceComparisonScore')

        if m.get('Material') is not None:
            temp_model = main_models.VerifyMaterialResponseBodyMaterial()
            self.material = temp_model.from_map(m.get('Material'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('VerifyStatus') is not None:
            self.verify_status = m.get('VerifyStatus')

        if m.get('VerifyToken') is not None:
            self.verify_token = m.get('VerifyToken')

        return self

class VerifyMaterialResponseBodyMaterial(DaraModel):
    def __init__(
        self,
        face_global_url: str = None,
        face_image_url: str = None,
        face_mask: str = None,
        face_quality: str = None,
        id_card_info: main_models.VerifyMaterialResponseBodyMaterialIdCardInfo = None,
        id_card_name: str = None,
        id_card_number: str = None,
    ):
        # The global image captured by the camera and collected by the ID Verification SDK.
        # 
        # > This parameter takes effect only after it is configured. If you need to use this parameter, submit a [ticket](https://selfservice.console.aliyun.com/ticket/category/cloudauth/today) to contact us.
        self.face_global_url = face_global_url
        # The HTTP or HTTPS URL of the front-facing portrait photo, which corresponds to the **FaceImageUrl** request parameter. The URL is valid for 5 minutes. Store the image in your own storage to prevent usage issues.
        self.face_image_url = face_image_url
        # Specifies whether the face is wearing a mask. Valid values:
        # - **true**: A mask is worn.
        # - **false**: No mask is worn.
        self.face_mask = face_mask
        # The quality of the front-facing portrait photo. Valid values:
        # - **UNQUALIFIED**: Poor photo quality.
        # - **LOW**: Low.
        # - **NORMAL**: Normal.
        # - **HIGH**: High.
        self.face_quality = face_quality
        # The OCR result of the ID card information.
        # 
        # > If the front and back sides of the ID card are not provided during the authentication process, the OCR result of the ID card information is not returned. Even if the front and back sides of the ID card are provided, the system does not guarantee that all information on the ID card is returned. If OCR fails to recognize certain information due to photo quality issues, the OCR information may be incomplete. Do not strongly rely on the ID card OCR information in your business.
        self.id_card_info = id_card_info
        # The name, which corresponds to the **Name** request parameter.
        self.id_card_name = id_card_name
        # The ID card number, which corresponds to the **IdCardNumber** request parameter.
        self.id_card_number = id_card_number

    def validate(self):
        if self.id_card_info:
            self.id_card_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.face_global_url is not None:
            result['FaceGlobalUrl'] = self.face_global_url

        if self.face_image_url is not None:
            result['FaceImageUrl'] = self.face_image_url

        if self.face_mask is not None:
            result['FaceMask'] = self.face_mask

        if self.face_quality is not None:
            result['FaceQuality'] = self.face_quality

        if self.id_card_info is not None:
            result['IdCardInfo'] = self.id_card_info.to_map()

        if self.id_card_name is not None:
            result['IdCardName'] = self.id_card_name

        if self.id_card_number is not None:
            result['IdCardNumber'] = self.id_card_number

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FaceGlobalUrl') is not None:
            self.face_global_url = m.get('FaceGlobalUrl')

        if m.get('FaceImageUrl') is not None:
            self.face_image_url = m.get('FaceImageUrl')

        if m.get('FaceMask') is not None:
            self.face_mask = m.get('FaceMask')

        if m.get('FaceQuality') is not None:
            self.face_quality = m.get('FaceQuality')

        if m.get('IdCardInfo') is not None:
            temp_model = main_models.VerifyMaterialResponseBodyMaterialIdCardInfo()
            self.id_card_info = temp_model.from_map(m.get('IdCardInfo'))

        if m.get('IdCardName') is not None:
            self.id_card_name = m.get('IdCardName')

        if m.get('IdCardNumber') is not None:
            self.id_card_number = m.get('IdCardNumber')

        return self

class VerifyMaterialResponseBodyMaterialIdCardInfo(DaraModel):
    def __init__(
        self,
        address: str = None,
        authority: str = None,
        back_image_url: str = None,
        birth: str = None,
        end_date: str = None,
        front_image_url: str = None,
        name: str = None,
        nationality: str = None,
        number: str = None,
        start_date: str = None,
    ):
        # The address.
        self.address = address
        # The issuing authority.
        self.authority = authority
        # The HTTP or HTTPS URL of the image for the back side of the ID card. The URL is valid for 5 minutes. Store the image in your own storage to prevent usage issues.
        self.back_image_url = back_image_url
        # The date of birth.
        self.birth = birth
        # The end date of the ID card validity period. Format: yyyymmdd.
        self.end_date = end_date
        # The HTTP or HTTPS URL of the image for the front side of the ID card. The URL is valid for 5 minutes. Store the image in your own storage to prevent usage issues.
        self.front_image_url = front_image_url
        # The name.
        self.name = name
        # The ethnicity.
        self.nationality = nationality
        # The ID card number.
        self.number = number
        # The start date of the ID card validity period. Format: yyyymmdd.
        self.start_date = start_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address is not None:
            result['Address'] = self.address

        if self.authority is not None:
            result['Authority'] = self.authority

        if self.back_image_url is not None:
            result['BackImageUrl'] = self.back_image_url

        if self.birth is not None:
            result['Birth'] = self.birth

        if self.end_date is not None:
            result['EndDate'] = self.end_date

        if self.front_image_url is not None:
            result['FrontImageUrl'] = self.front_image_url

        if self.name is not None:
            result['Name'] = self.name

        if self.nationality is not None:
            result['Nationality'] = self.nationality

        if self.number is not None:
            result['Number'] = self.number

        if self.start_date is not None:
            result['StartDate'] = self.start_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')

        if m.get('Authority') is not None:
            self.authority = m.get('Authority')

        if m.get('BackImageUrl') is not None:
            self.back_image_url = m.get('BackImageUrl')

        if m.get('Birth') is not None:
            self.birth = m.get('Birth')

        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')

        if m.get('FrontImageUrl') is not None:
            self.front_image_url = m.get('FrontImageUrl')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Nationality') is not None:
            self.nationality = m.get('Nationality')

        if m.get('Number') is not None:
            self.number = m.get('Number')

        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')

        return self

