# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudauth20190307 import models as main_models
from darabonba.model import DaraModel

class DescribeVerifyResultResponseBody(DaraModel):
    def __init__(
        self,
        authority_comparision_score: float = None,
        face_comparison_score: float = None,
        id_card_face_comparison_score: float = None,
        material: main_models.DescribeVerifyResultResponseBodyMaterial = None,
        request_id: str = None,
        verify_status: int = None,
    ):
        # The comparison score between the face photo submitted during the verification process and the authoritative data. Valid values: **0** to **100**.
        # 
        # Confidence threshold reference:
        # 
        # - When the false acceptance rate is 0.001%, the corresponding threshold is 95.
        # - When the false acceptance rate is 0.01%, the corresponding threshold is 90.
        # - When the false acceptance rate is 0.1%, the corresponding threshold is 80.
        # - When the false acceptance rate is 1%, the corresponding threshold is 60.
        # 
        # > This field only indicates the comparison result between the face and the authoritative data and is for your reference only. Do not use this value as the sole criterion for determining whether the verification is passed. For the comprehensive verification result, refer to the **VerifyStatus** field. The **VerifyStatus** result combines the face-to-authoritative-data comparison with various other strategies to improve the security level.
        self.authority_comparision_score = authority_comparision_score
        # The comparison score between the face photo submitted during the verification process and the face in the retained face photo. Valid values: **0** to **100**.
        # 
        # Confidence threshold reference:
        # 
        # - When the false acceptance rate is 0.001%, the corresponding threshold is 95.
        # - When the false acceptance rate is 0.01%, the corresponding threshold is 90.
        # - When the false acceptance rate is 0.1%, the corresponding threshold is 80.
        # - When the false acceptance rate is 1%, the corresponding threshold is 60.
        self.face_comparison_score = face_comparison_score
        # The comparison score between the face photo submitted during the verification process and the face in the ID card portrait photo. Valid values: **0** to **100**.
        # 
        # Confidence threshold reference:
        # 
        # - When the false acceptance rate is 0.001%, the corresponding threshold is 95.
        # - When the false acceptance rate is 0.01%, the corresponding threshold is 90.
        # - When the false acceptance rate is 0.1%, the corresponding threshold is 80.
        # - When the false acceptance rate is 1%, the corresponding threshold is 60.
        self.id_card_face_comparison_score = id_card_face_comparison_score
        # The verification materials.
        self.material = material
        # The ID of the request.
        self.request_id = request_id
        # The verification status. Valid values:
        # 
        # - **-1**: Not verified.
        # - **1**: Verification passed.
        # - **2** to **n**: Verification failed due to various reasons. For detailed descriptions, see the verification status description.
        self.verify_status = verify_status

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

        if self.face_comparison_score is not None:
            result['FaceComparisonScore'] = self.face_comparison_score

        if self.id_card_face_comparison_score is not None:
            result['IdCardFaceComparisonScore'] = self.id_card_face_comparison_score

        if self.material is not None:
            result['Material'] = self.material.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.verify_status is not None:
            result['VerifyStatus'] = self.verify_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorityComparisionScore') is not None:
            self.authority_comparision_score = m.get('AuthorityComparisionScore')

        if m.get('FaceComparisonScore') is not None:
            self.face_comparison_score = m.get('FaceComparisonScore')

        if m.get('IdCardFaceComparisonScore') is not None:
            self.id_card_face_comparison_score = m.get('IdCardFaceComparisonScore')

        if m.get('Material') is not None:
            temp_model = main_models.DescribeVerifyResultResponseBodyMaterial()
            self.material = temp_model.from_map(m.get('Material'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('VerifyStatus') is not None:
            self.verify_status = m.get('VerifyStatus')

        return self

class DescribeVerifyResultResponseBodyMaterial(DaraModel):
    def __init__(
        self,
        face_global_url: str = None,
        face_image_url: str = None,
        face_mask: bool = None,
        face_quality: str = None,
        id_card_info: main_models.DescribeVerifyResultResponseBodyMaterialIdCardInfo = None,
        id_card_name: str = None,
        id_card_number: str = None,
        video_urls: List[str] = None,
    ):
        # The global image captured by the camera and collected by the ID Verification SDK.
        # 
        # > This parameter takes effect only after it is configured. If you need to use this parameter, submit a [ticket](https://selfservice.console.aliyun.com/ticket/category/cloudauth/today) to contact us.
        self.face_global_url = face_global_url
        # The HTTP or HTTPS URL of the front-facing face photo. The URL is valid for 5 minutes. Store the image to prevent service interruptions.
        # > If the HTTP or HTTPS URL of the front-facing face photo expires, you can call [DescribeVerifyResult](https://help.aliyun.com/document_detail/154606.html) again to obtain the URL.
        self.face_image_url = face_image_url
        # Indicates whether the face is wearing a mask. Valid values:
        # - **true**: A mask is worn.
        # - **false**: No mask is worn.
        self.face_mask = face_mask
        # The quality of the front-facing face photo. Valid values:
        # - **UNQUALIFIED**: Poor photo quality.
        # - **LOW**: Low.
        # - **NORMAL**: Normal.
        # - **HIGH**: High.
        self.face_quality = face_quality
        # The optical character recognition (OCR) result of the ID card information.
        # > If the front and back images of the ID card are not provided during the verification process, the ID Verification service does not return the OCR result of the ID card. Even if the front and back images are provided, the service does not guarantee that all information on the ID card is returned. If the OCR fails to recognize certain information due to photo quality issues, the OCR information will be incomplete. Do not strongly rely on the ID card OCR information in your business.
        self.id_card_info = id_card_info
        # The name.
        self.id_card_name = id_card_name
        # The ID card number.
        self.id_card_number = id_card_number
        # The URL of the recorded video returned by the legacy RPH5BioOnly solution.
        self.video_urls = video_urls

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

        if self.video_urls is not None:
            result['VideoUrls'] = self.video_urls

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
            temp_model = main_models.DescribeVerifyResultResponseBodyMaterialIdCardInfo()
            self.id_card_info = temp_model.from_map(m.get('IdCardInfo'))

        if m.get('IdCardName') is not None:
            self.id_card_name = m.get('IdCardName')

        if m.get('IdCardNumber') is not None:
            self.id_card_number = m.get('IdCardNumber')

        if m.get('VideoUrls') is not None:
            self.video_urls = m.get('VideoUrls')

        return self

class DescribeVerifyResultResponseBodyMaterialIdCardInfo(DaraModel):
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
        # The HTTP or HTTPS URL of the ID card back image with the national emblem. The URL is valid for 5 minutes. Store the image to prevent service interruptions.
        # > If the HTTP or HTTPS URL of the image expires, you can call DescribeVerifyResult again to obtain the URL.
        self.back_image_url = back_image_url
        # The date of birth.
        self.birth = birth
        # The end date of the validity period of the ID card. Format: yyyymmdd.
        self.end_date = end_date
        # The HTTP or HTTPS URL of the ID card portrait image. The URL is valid for 5 minutes. Store the image to prevent service interruptions.
        # > If the HTTP or HTTPS URL of the image expires, you can call DescribeVerifyResult again to obtain the URL.
        self.front_image_url = front_image_url
        # The name.
        self.name = name
        # The ethnicity.
        self.nationality = nationality
        # The ID card number.
        self.number = number
        # The start date of the validity period of the ID card. Format: yyyymmdd.
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

