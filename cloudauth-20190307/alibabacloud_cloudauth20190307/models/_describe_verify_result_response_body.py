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
        # The comparison score between the face photo submitted during the authentication process and the authoritative data, with a value range of **0** to **100**.
        # Confidence threshold references:
        # - When the false acceptance rate is 0.001%, the corresponding threshold is 95. - When the false acceptance rate is 0.01%, the corresponding threshold is 90. - When the false acceptance rate is 0.1%, the corresponding threshold is 80. - When the false acceptance rate is 1%, the corresponding threshold is 60.
        # > This field only indicates the comparison result between the face and the authoritative data, for your reference only. It is generally not recommended to use this value alone as the standard for whether the authentication passes. For a comprehensive authentication result, please refer to the **VerifyStatus** field. The **VerifyStatus** result integrates the comparison of the face with the authoritative data and various other strategies, which can enhance security levels.
        self.authority_comparision_score = authority_comparision_score
        # The comparison score between the face photo submitted during the authentication process and the face in the retained face image. The value range is **0**~**100**.
        # 
        # Confidence threshold reference:
        # 
        # - When the false recognition rate is 0.001%, the corresponding threshold is 95.
        # - When the false recognition rate is 0.01%, the corresponding threshold is 90.
        # - When the false recognition rate is 0.1%, the corresponding threshold is 80.
        # - When the false recognition rate is 1%, the corresponding threshold is 60.
        self.face_comparison_score = face_comparison_score
        # The comparison score between the face photo submitted during the authentication process and the face on the ID card\\"s face side. The value range is **0**~**100**.
        # 
        # Confidence threshold reference:
        # 
        # - When the false recognition rate is 0.001%, the corresponding threshold is 95.
        # - When the false recognition rate is 0.01%, the corresponding threshold is 90.
        # - When the false recognition rate is 0.1%, the corresponding threshold is 80.
        # - When the false recognition rate is 1%, the corresponding threshold is 60.
        self.id_card_face_comparison_score = id_card_face_comparison_score
        # Authentication materials.
        self.material = material
        # The ID of this request.
        self.request_id = request_id
        # Authentication status, values:
        # - **-1**: Not authenticated - **1**: Authentication passed - **2** to **n**: Authentication failed for various reasons. For detailed descriptions, see the authentication status explanation.
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
        # The global camera image captured by the real-person authentication SDK.
        # 
        # > This parameter will only take effect after configuration. If you need to use this parameter, please submit a [ticket](https://selfservice.console.aliyun.com/ticket/category/cloudauth/today) to contact us.
        self.face_global_url = face_global_url
        # The HTTP or HTTPS link to the frontal face image. The link is valid for 5 minutes, and it is recommended to store it elsewhere to avoid any impact on usage.
        # > If the HTTP or HTTPS link to the frontal face image expires, you can call [DescribeVerifyResult](https://help.aliyun.com/document_detail/154606.html) again to get the link.
        self.face_image_url = face_image_url
        # Whether the face is wearing a mask. Values:
        # - **true**: Wearing a mask
        # - **false**: Not wearing a mask
        self.face_mask = face_mask
        # The quality of the frontal face image. Values:
        # - **UNQUALIFIED**: Poor quality
        # - **LOW**: Low
        # - **NORMAL**: Normal
        # - **HIGH**: High
        self.face_quality = face_quality
        # OCR results of the ID card information.
        # > If there is no front and back information of the ID card during the authentication process, the real-person authentication service will not return the OCR results of the ID card. Even if there is front and back information of the ID card during the authentication process, the real-person authentication service does not guarantee to return all the information on the ID card. Due to issues with ID card photography, the OCR may fail to recognize some information, resulting in incomplete OCR information. It is recommended that your business does not strongly rely on the ID card OCR information.
        self.id_card_info = id_card_info
        # Name.
        self.id_card_name = id_card_name
        # ID number.
        self.id_card_number = id_card_number
        # The URL addresses of the recorded videos returned by the historical RPH5BioOnly solution.
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
        # Address.
        self.address = address
        # Issuing authority.
        self.authority = authority
        # HTTP/HTTPS link to the image of the back side (national emblem side) of the ID card. The link is valid for 5 minutes, and it is recommended to store it for business use to avoid any impact.
        # > If the HTTP/HTTPS link to the front-facing portrait image expires, you can call DescribeVerifyResult again to get the link.
        self.back_image_url = back_image_url
        # Date of birth.
        self.birth = birth
        # The end date of the document\\"s validity period. Format: yyyymmdd.
        self.end_date = end_date
        # HTTP/HTTPS link to the image of the front side (portrait side) of the ID card. The link is valid for 5 minutes, and it is recommended to store it for business use to avoid any impact.
        # > If the HTTP/HTTPS link to the front-facing portrait image expires, you can call DescribeVerifyResult again to get the link.
        self.front_image_url = front_image_url
        # Name.
        self.name = name
        # Nationality.
        self.nationality = nationality
        # ID card number.
        self.number = number
        # Start date of the document\\"s validity. Format: yyyymmdd.
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

