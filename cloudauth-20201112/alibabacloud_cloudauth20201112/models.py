# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List, BinaryIO


class CompareFacesRequest(TeaModel):
    def __init__(
        self,
        source_image_url: str = None,
        source_image_base_64: str = None,
        target_image_url: str = None,
        target_image_base_64: str = None,
        biz_id: str = None,
        biz_type: str = None,
    ):
        self.source_image_url = source_image_url
        self.source_image_base_64 = source_image_base_64
        self.target_image_url = target_image_url
        self.target_image_base_64 = target_image_base_64
        self.biz_id = biz_id
        self.biz_type = biz_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_image_url is not None:
            result['SourceImageUrl'] = self.source_image_url
        if self.source_image_base_64 is not None:
            result['SourceImageBase64'] = self.source_image_base_64
        if self.target_image_url is not None:
            result['TargetImageUrl'] = self.target_image_url
        if self.target_image_base_64 is not None:
            result['TargetImageBase64'] = self.target_image_base_64
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceImageUrl') is not None:
            self.source_image_url = m.get('SourceImageUrl')
        if m.get('SourceImageBase64') is not None:
            self.source_image_base_64 = m.get('SourceImageBase64')
        if m.get('TargetImageUrl') is not None:
            self.target_image_url = m.get('TargetImageUrl')
        if m.get('TargetImageBase64') is not None:
            self.target_image_base_64 = m.get('TargetImageBase64')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        return self


class CompareFacesResponseBodyResultObject(TeaModel):
    def __init__(
        self,
        similarity_score: float = None,
        confidence_thresholds: str = None,
    ):
        self.similarity_score = similarity_score
        self.confidence_thresholds = confidence_thresholds

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.similarity_score is not None:
            result['SimilarityScore'] = self.similarity_score
        if self.confidence_thresholds is not None:
            result['ConfidenceThresholds'] = self.confidence_thresholds
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SimilarityScore') is not None:
            self.similarity_score = m.get('SimilarityScore')
        if m.get('ConfidenceThresholds') is not None:
            self.confidence_thresholds = m.get('ConfidenceThresholds')
        return self


class CompareFacesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result_object: CompareFacesResponseBodyResultObject = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result_object = result_object

    def validate(self):
        if self.result_object:
            self.result_object.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = CompareFacesResponseBodyResultObject()
            self.result_object = temp_model.from_map(m['ResultObject'])
        return self


class CompareFacesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CompareFacesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CompareFacesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVerifyResultRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        biz_type: str = None,
    ):
        self.biz_id = biz_id
        self.biz_type = biz_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        return self


class DescribeVerifyResultResponseBodyResultObjectMaterialIdCardInfo(TeaModel):
    def __init__(
        self,
        sex: str = None,
        end_date: str = None,
        authority: str = None,
        address: str = None,
        number: str = None,
        start_date: str = None,
        back_image_url: str = None,
        nationality: str = None,
        birth: str = None,
        name: str = None,
        front_image_url: str = None,
    ):
        self.sex = sex
        self.end_date = end_date
        self.authority = authority
        self.address = address
        self.number = number
        self.start_date = start_date
        self.back_image_url = back_image_url
        self.nationality = nationality
        self.birth = birth
        self.name = name
        self.front_image_url = front_image_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sex is not None:
            result['Sex'] = self.sex
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.authority is not None:
            result['Authority'] = self.authority
        if self.address is not None:
            result['Address'] = self.address
        if self.number is not None:
            result['Number'] = self.number
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.back_image_url is not None:
            result['BackImageUrl'] = self.back_image_url
        if self.nationality is not None:
            result['Nationality'] = self.nationality
        if self.birth is not None:
            result['Birth'] = self.birth
        if self.name is not None:
            result['Name'] = self.name
        if self.front_image_url is not None:
            result['FrontImageUrl'] = self.front_image_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Sex') is not None:
            self.sex = m.get('Sex')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('Authority') is not None:
            self.authority = m.get('Authority')
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('Number') is not None:
            self.number = m.get('Number')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('BackImageUrl') is not None:
            self.back_image_url = m.get('BackImageUrl')
        if m.get('Nationality') is not None:
            self.nationality = m.get('Nationality')
        if m.get('Birth') is not None:
            self.birth = m.get('Birth')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('FrontImageUrl') is not None:
            self.front_image_url = m.get('FrontImageUrl')
        return self


class DescribeVerifyResultResponseBodyResultObjectMaterial(TeaModel):
    def __init__(
        self,
        id_card_number: str = None,
        face_global_url: str = None,
        face_image_url: str = None,
        face_mask: bool = None,
        id_card_name: str = None,
        face_quality: str = None,
        video_urls: List[str] = None,
        id_card_info: DescribeVerifyResultResponseBodyResultObjectMaterialIdCardInfo = None,
    ):
        self.id_card_number = id_card_number
        self.face_global_url = face_global_url
        self.face_image_url = face_image_url
        self.face_mask = face_mask
        self.id_card_name = id_card_name
        self.face_quality = face_quality
        self.video_urls = video_urls
        self.id_card_info = id_card_info

    def validate(self):
        if self.id_card_info:
            self.id_card_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id_card_number is not None:
            result['IdCardNumber'] = self.id_card_number
        if self.face_global_url is not None:
            result['FaceGlobalUrl'] = self.face_global_url
        if self.face_image_url is not None:
            result['FaceImageUrl'] = self.face_image_url
        if self.face_mask is not None:
            result['FaceMask'] = self.face_mask
        if self.id_card_name is not None:
            result['IdCardName'] = self.id_card_name
        if self.face_quality is not None:
            result['FaceQuality'] = self.face_quality
        if self.video_urls is not None:
            result['VideoUrls'] = self.video_urls
        if self.id_card_info is not None:
            result['IdCardInfo'] = self.id_card_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IdCardNumber') is not None:
            self.id_card_number = m.get('IdCardNumber')
        if m.get('FaceGlobalUrl') is not None:
            self.face_global_url = m.get('FaceGlobalUrl')
        if m.get('FaceImageUrl') is not None:
            self.face_image_url = m.get('FaceImageUrl')
        if m.get('FaceMask') is not None:
            self.face_mask = m.get('FaceMask')
        if m.get('IdCardName') is not None:
            self.id_card_name = m.get('IdCardName')
        if m.get('FaceQuality') is not None:
            self.face_quality = m.get('FaceQuality')
        if m.get('VideoUrls') is not None:
            self.video_urls = m.get('VideoUrls')
        if m.get('IdCardInfo') is not None:
            temp_model = DescribeVerifyResultResponseBodyResultObjectMaterialIdCardInfo()
            self.id_card_info = temp_model.from_map(m['IdCardInfo'])
        return self


class DescribeVerifyResultResponseBodyResultObject(TeaModel):
    def __init__(
        self,
        authority_comparision_score: float = None,
        verify_status: int = None,
        face_comparison_score: float = None,
        id_card_face_comparison_score: float = None,
        material: DescribeVerifyResultResponseBodyResultObjectMaterial = None,
    ):
        self.authority_comparision_score = authority_comparision_score
        self.verify_status = verify_status
        self.face_comparison_score = face_comparison_score
        self.id_card_face_comparison_score = id_card_face_comparison_score
        self.material = material

    def validate(self):
        if self.material:
            self.material.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authority_comparision_score is not None:
            result['AuthorityComparisionScore'] = self.authority_comparision_score
        if self.verify_status is not None:
            result['VerifyStatus'] = self.verify_status
        if self.face_comparison_score is not None:
            result['FaceComparisonScore'] = self.face_comparison_score
        if self.id_card_face_comparison_score is not None:
            result['IdCardFaceComparisonScore'] = self.id_card_face_comparison_score
        if self.material is not None:
            result['Material'] = self.material.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorityComparisionScore') is not None:
            self.authority_comparision_score = m.get('AuthorityComparisionScore')
        if m.get('VerifyStatus') is not None:
            self.verify_status = m.get('VerifyStatus')
        if m.get('FaceComparisonScore') is not None:
            self.face_comparison_score = m.get('FaceComparisonScore')
        if m.get('IdCardFaceComparisonScore') is not None:
            self.id_card_face_comparison_score = m.get('IdCardFaceComparisonScore')
        if m.get('Material') is not None:
            temp_model = DescribeVerifyResultResponseBodyResultObjectMaterial()
            self.material = temp_model.from_map(m['Material'])
        return self


class DescribeVerifyResultResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result_object: DescribeVerifyResultResponseBodyResultObject = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result_object = result_object

    def validate(self):
        if self.result_object:
            self.result_object.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = DescribeVerifyResultResponseBodyResultObject()
            self.result_object = temp_model.from_map(m['ResultObject'])
        return self


class DescribeVerifyResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeVerifyResultResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeVerifyResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVerifyTokenRequest(TeaModel):
    def __init__(
        self,
        id_card_back_image_url: str = None,
        biz_type: str = None,
        face_retained_image_url: str = None,
        id_card_front_image_url: str = None,
        user_id: str = None,
        biz_id: str = None,
        name: str = None,
        id_card_number: str = None,
        user_ip: str = None,
        user_phone_number: str = None,
        user_regist_time: int = None,
    ):
        self.id_card_back_image_url = id_card_back_image_url
        self.biz_type = biz_type
        self.face_retained_image_url = face_retained_image_url
        self.id_card_front_image_url = id_card_front_image_url
        self.user_id = user_id
        self.biz_id = biz_id
        self.name = name
        self.id_card_number = id_card_number
        self.user_ip = user_ip
        self.user_phone_number = user_phone_number
        self.user_regist_time = user_regist_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id_card_back_image_url is not None:
            result['IdCardBackImageUrl'] = self.id_card_back_image_url
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.face_retained_image_url is not None:
            result['FaceRetainedImageUrl'] = self.face_retained_image_url
        if self.id_card_front_image_url is not None:
            result['IdCardFrontImageUrl'] = self.id_card_front_image_url
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.name is not None:
            result['Name'] = self.name
        if self.id_card_number is not None:
            result['IdCardNumber'] = self.id_card_number
        if self.user_ip is not None:
            result['UserIp'] = self.user_ip
        if self.user_phone_number is not None:
            result['UserPhoneNumber'] = self.user_phone_number
        if self.user_regist_time is not None:
            result['UserRegistTime'] = self.user_regist_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IdCardBackImageUrl') is not None:
            self.id_card_back_image_url = m.get('IdCardBackImageUrl')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('FaceRetainedImageUrl') is not None:
            self.face_retained_image_url = m.get('FaceRetainedImageUrl')
        if m.get('IdCardFrontImageUrl') is not None:
            self.id_card_front_image_url = m.get('IdCardFrontImageUrl')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('IdCardNumber') is not None:
            self.id_card_number = m.get('IdCardNumber')
        if m.get('UserIp') is not None:
            self.user_ip = m.get('UserIp')
        if m.get('UserPhoneNumber') is not None:
            self.user_phone_number = m.get('UserPhoneNumber')
        if m.get('UserRegistTime') is not None:
            self.user_regist_time = m.get('UserRegistTime')
        return self


class DescribeVerifyTokenResponseBodyResultObject(TeaModel):
    def __init__(
        self,
        verify_page_url: str = None,
        verify_token: str = None,
    ):
        self.verify_page_url = verify_page_url
        self.verify_token = verify_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.verify_page_url is not None:
            result['VerifyPageUrl'] = self.verify_page_url
        if self.verify_token is not None:
            result['VerifyToken'] = self.verify_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VerifyPageUrl') is not None:
            self.verify_page_url = m.get('VerifyPageUrl')
        if m.get('VerifyToken') is not None:
            self.verify_token = m.get('VerifyToken')
        return self


class DescribeVerifyTokenResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result_object: DescribeVerifyTokenResponseBodyResultObject = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result_object = result_object

    def validate(self):
        if self.result_object:
            self.result_object.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = DescribeVerifyTokenResponseBodyResultObject()
            self.result_object = temp_model.from_map(m['ResultObject'])
        return self


class DescribeVerifyTokenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeVerifyTokenResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeVerifyTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetectFaceAttributesRequest(TeaModel):
    def __init__(
        self,
        biz_type: str = None,
        biz_id: str = None,
        image_url: str = None,
        image_file: str = None,
    ):
        self.biz_type = biz_type
        self.biz_id = biz_id
        self.image_url = image_url
        self.image_file = image_file

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.image_file is not None:
            result['ImageFile'] = self.image_file
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('ImageFile') is not None:
            self.image_file = m.get('ImageFile')
        return self


class DetectFaceAttributesAdvanceRequest(TeaModel):
    def __init__(
        self,
        image_file_object: BinaryIO = None,
        biz_type: str = None,
        biz_id: str = None,
        image_url: str = None,
    ):
        self.image_file_object = image_file_object
        self.biz_type = biz_type
        self.biz_id = biz_id
        self.image_url = image_url

    def validate(self):
        self.validate_required(self.image_file_object, 'image_file_object')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_file_object is not None:
            result['ImageFileObject'] = self.image_file_object
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageFileObject') is not None:
            self.image_file_object = m.get('ImageFileObject')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        return self


class DetectFaceAttributesResponseBodyResultObjectFaceInfosFaceAttributesDetectInfoFaceRect(TeaModel):
    def __init__(
        self,
        left: int = None,
        top: int = None,
        width: int = None,
        height: int = None,
    ):
        self.left = left
        self.top = top
        self.width = width
        self.height = height

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.left is not None:
            result['Left'] = self.left
        if self.top is not None:
            result['Top'] = self.top
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Left') is not None:
            self.left = m.get('Left')
        if m.get('Top') is not None:
            self.top = m.get('Top')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        return self


class DetectFaceAttributesResponseBodyResultObjectFaceInfosFaceAttributesDetectInfoFaceAttributesSmiling(TeaModel):
    def __init__(
        self,
        value: float = None,
        threshold: float = None,
    ):
        self.value = value
        self.threshold = threshold

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        return self


class DetectFaceAttributesResponseBodyResultObjectFaceInfosFaceAttributesDetectInfoFaceAttributesHeadpose(TeaModel):
    def __init__(
        self,
        pitch_angle: float = None,
        roll_angle: float = None,
        yaw_angle: float = None,
    ):
        self.pitch_angle = pitch_angle
        self.roll_angle = roll_angle
        self.yaw_angle = yaw_angle

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pitch_angle is not None:
            result['PitchAngle'] = self.pitch_angle
        if self.roll_angle is not None:
            result['RollAngle'] = self.roll_angle
        if self.yaw_angle is not None:
            result['YawAngle'] = self.yaw_angle
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PitchAngle') is not None:
            self.pitch_angle = m.get('PitchAngle')
        if m.get('RollAngle') is not None:
            self.roll_angle = m.get('RollAngle')
        if m.get('YawAngle') is not None:
            self.yaw_angle = m.get('YawAngle')
        return self


class DetectFaceAttributesResponseBodyResultObjectFaceInfosFaceAttributesDetectInfoFaceAttributes(TeaModel):
    def __init__(
        self,
        glasses: str = None,
        facequal: float = None,
        integrity: int = None,
        facetype: str = None,
        respirator: str = None,
        appearance_score: float = None,
        blur: float = None,
        smiling: DetectFaceAttributesResponseBodyResultObjectFaceInfosFaceAttributesDetectInfoFaceAttributesSmiling = None,
        headpose: DetectFaceAttributesResponseBodyResultObjectFaceInfosFaceAttributesDetectInfoFaceAttributesHeadpose = None,
    ):
        self.glasses = glasses
        self.facequal = facequal
        self.integrity = integrity
        self.facetype = facetype
        self.respirator = respirator
        self.appearance_score = appearance_score
        self.blur = blur
        self.smiling = smiling
        self.headpose = headpose

    def validate(self):
        if self.smiling:
            self.smiling.validate()
        if self.headpose:
            self.headpose.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.glasses is not None:
            result['Glasses'] = self.glasses
        if self.facequal is not None:
            result['Facequal'] = self.facequal
        if self.integrity is not None:
            result['Integrity'] = self.integrity
        if self.facetype is not None:
            result['Facetype'] = self.facetype
        if self.respirator is not None:
            result['Respirator'] = self.respirator
        if self.appearance_score is not None:
            result['AppearanceScore'] = self.appearance_score
        if self.blur is not None:
            result['Blur'] = self.blur
        if self.smiling is not None:
            result['Smiling'] = self.smiling.to_map()
        if self.headpose is not None:
            result['Headpose'] = self.headpose.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Glasses') is not None:
            self.glasses = m.get('Glasses')
        if m.get('Facequal') is not None:
            self.facequal = m.get('Facequal')
        if m.get('Integrity') is not None:
            self.integrity = m.get('Integrity')
        if m.get('Facetype') is not None:
            self.facetype = m.get('Facetype')
        if m.get('Respirator') is not None:
            self.respirator = m.get('Respirator')
        if m.get('AppearanceScore') is not None:
            self.appearance_score = m.get('AppearanceScore')
        if m.get('Blur') is not None:
            self.blur = m.get('Blur')
        if m.get('Smiling') is not None:
            temp_model = DetectFaceAttributesResponseBodyResultObjectFaceInfosFaceAttributesDetectInfoFaceAttributesSmiling()
            self.smiling = temp_model.from_map(m['Smiling'])
        if m.get('Headpose') is not None:
            temp_model = DetectFaceAttributesResponseBodyResultObjectFaceInfosFaceAttributesDetectInfoFaceAttributesHeadpose()
            self.headpose = temp_model.from_map(m['Headpose'])
        return self


class DetectFaceAttributesResponseBodyResultObjectFaceInfosFaceAttributesDetectInfo(TeaModel):
    def __init__(
        self,
        face_rect: DetectFaceAttributesResponseBodyResultObjectFaceInfosFaceAttributesDetectInfoFaceRect = None,
        face_attributes: DetectFaceAttributesResponseBodyResultObjectFaceInfosFaceAttributesDetectInfoFaceAttributes = None,
    ):
        self.face_rect = face_rect
        self.face_attributes = face_attributes

    def validate(self):
        if self.face_rect:
            self.face_rect.validate()
        if self.face_attributes:
            self.face_attributes.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.face_rect is not None:
            result['FaceRect'] = self.face_rect.to_map()
        if self.face_attributes is not None:
            result['FaceAttributes'] = self.face_attributes.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FaceRect') is not None:
            temp_model = DetectFaceAttributesResponseBodyResultObjectFaceInfosFaceAttributesDetectInfoFaceRect()
            self.face_rect = temp_model.from_map(m['FaceRect'])
        if m.get('FaceAttributes') is not None:
            temp_model = DetectFaceAttributesResponseBodyResultObjectFaceInfosFaceAttributesDetectInfoFaceAttributes()
            self.face_attributes = temp_model.from_map(m['FaceAttributes'])
        return self


class DetectFaceAttributesResponseBodyResultObjectFaceInfos(TeaModel):
    def __init__(
        self,
        face_attributes_detect_info: List[DetectFaceAttributesResponseBodyResultObjectFaceInfosFaceAttributesDetectInfo] = None,
    ):
        self.face_attributes_detect_info = face_attributes_detect_info

    def validate(self):
        if self.face_attributes_detect_info:
            for k in self.face_attributes_detect_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FaceAttributesDetectInfo'] = []
        if self.face_attributes_detect_info is not None:
            for k in self.face_attributes_detect_info:
                result['FaceAttributesDetectInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.face_attributes_detect_info = []
        if m.get('FaceAttributesDetectInfo') is not None:
            for k in m.get('FaceAttributesDetectInfo'):
                temp_model = DetectFaceAttributesResponseBodyResultObjectFaceInfosFaceAttributesDetectInfo()
                self.face_attributes_detect_info.append(temp_model.from_map(k))
        return self


class DetectFaceAttributesResponseBodyResultObject(TeaModel):
    def __init__(
        self,
        img_height: int = None,
        img_width: int = None,
        face_infos: DetectFaceAttributesResponseBodyResultObjectFaceInfos = None,
    ):
        self.img_height = img_height
        self.img_width = img_width
        self.face_infos = face_infos

    def validate(self):
        if self.face_infos:
            self.face_infos.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.img_height is not None:
            result['ImgHeight'] = self.img_height
        if self.img_width is not None:
            result['ImgWidth'] = self.img_width
        if self.face_infos is not None:
            result['FaceInfos'] = self.face_infos.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImgHeight') is not None:
            self.img_height = m.get('ImgHeight')
        if m.get('ImgWidth') is not None:
            self.img_width = m.get('ImgWidth')
        if m.get('FaceInfos') is not None:
            temp_model = DetectFaceAttributesResponseBodyResultObjectFaceInfos()
            self.face_infos = temp_model.from_map(m['FaceInfos'])
        return self


class DetectFaceAttributesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        result_object: DetectFaceAttributesResponseBodyResultObject = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.result_object = result_object

    def validate(self):
        if self.result_object:
            self.result_object.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
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
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ResultObject') is not None:
            temp_model = DetectFaceAttributesResponseBodyResultObject()
            self.result_object = temp_model.from_map(m['ResultObject'])
        return self


class DetectFaceAttributesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DetectFaceAttributesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DetectFaceAttributesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class LivenessDetectRequest(TeaModel):
    def __init__(
        self,
        biz_type: str = None,
        biz_id: str = None,
        media_category: str = None,
        media_url: str = None,
        media_file: str = None,
    ):
        self.biz_type = biz_type
        self.biz_id = biz_id
        self.media_category = media_category
        self.media_url = media_url
        self.media_file = media_file

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.media_category is not None:
            result['MediaCategory'] = self.media_category
        if self.media_url is not None:
            result['MediaUrl'] = self.media_url
        if self.media_file is not None:
            result['MediaFile'] = self.media_file
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('MediaCategory') is not None:
            self.media_category = m.get('MediaCategory')
        if m.get('MediaUrl') is not None:
            self.media_url = m.get('MediaUrl')
        if m.get('MediaFile') is not None:
            self.media_file = m.get('MediaFile')
        return self


class LivenessDetectAdvanceRequest(TeaModel):
    def __init__(
        self,
        media_file_object: BinaryIO = None,
        biz_type: str = None,
        biz_id: str = None,
        media_category: str = None,
        media_url: str = None,
    ):
        self.media_file_object = media_file_object
        self.biz_type = biz_type
        self.biz_id = biz_id
        self.media_category = media_category
        self.media_url = media_url

    def validate(self):
        self.validate_required(self.media_file_object, 'media_file_object')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.media_file_object is not None:
            result['MediaFileObject'] = self.media_file_object
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.media_category is not None:
            result['MediaCategory'] = self.media_category
        if self.media_url is not None:
            result['MediaUrl'] = self.media_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MediaFileObject') is not None:
            self.media_file_object = m.get('MediaFileObject')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('MediaCategory') is not None:
            self.media_category = m.get('MediaCategory')
        if m.get('MediaUrl') is not None:
            self.media_url = m.get('MediaUrl')
        return self


class LivenessDetectResponseBodyResultObject(TeaModel):
    def __init__(
        self,
        score: float = None,
        frame_url: str = None,
        passed: str = None,
    ):
        self.score = score
        self.frame_url = frame_url
        self.passed = passed

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.score is not None:
            result['Score'] = self.score
        if self.frame_url is not None:
            result['FrameUrl'] = self.frame_url
        if self.passed is not None:
            result['Passed'] = self.passed
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('FrameUrl') is not None:
            self.frame_url = m.get('FrameUrl')
        if m.get('Passed') is not None:
            self.passed = m.get('Passed')
        return self


class LivenessDetectResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result_object: LivenessDetectResponseBodyResultObject = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result_object = result_object

    def validate(self):
        if self.result_object:
            self.result_object.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = LivenessDetectResponseBodyResultObject()
            self.result_object = temp_model.from_map(m['ResultObject'])
        return self


class LivenessDetectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: LivenessDetectResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = LivenessDetectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class VerifyMaterialRequest(TeaModel):
    def __init__(
        self,
        id_card_back_image_url: str = None,
        face_image_url: str = None,
        biz_type: str = None,
        biz_id: str = None,
        name: str = None,
        id_card_number: str = None,
        id_card_front_image_url: str = None,
        user_id: str = None,
    ):
        self.id_card_back_image_url = id_card_back_image_url
        self.face_image_url = face_image_url
        self.biz_type = biz_type
        self.biz_id = biz_id
        self.name = name
        self.id_card_number = id_card_number
        self.id_card_front_image_url = id_card_front_image_url
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id_card_back_image_url is not None:
            result['IdCardBackImageUrl'] = self.id_card_back_image_url
        if self.face_image_url is not None:
            result['FaceImageUrl'] = self.face_image_url
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.name is not None:
            result['Name'] = self.name
        if self.id_card_number is not None:
            result['IdCardNumber'] = self.id_card_number
        if self.id_card_front_image_url is not None:
            result['IdCardFrontImageUrl'] = self.id_card_front_image_url
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IdCardBackImageUrl') is not None:
            self.id_card_back_image_url = m.get('IdCardBackImageUrl')
        if m.get('FaceImageUrl') is not None:
            self.face_image_url = m.get('FaceImageUrl')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('IdCardNumber') is not None:
            self.id_card_number = m.get('IdCardNumber')
        if m.get('IdCardFrontImageUrl') is not None:
            self.id_card_front_image_url = m.get('IdCardFrontImageUrl')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class VerifyMaterialResponseBodyResultObjectMaterialIdCardInfo(TeaModel):
    def __init__(
        self,
        sex: str = None,
        end_date: str = None,
        authority: str = None,
        address: str = None,
        number: str = None,
        start_date: str = None,
        back_image_url: str = None,
        nationality: str = None,
        birth: str = None,
        name: str = None,
        front_image_url: str = None,
    ):
        self.sex = sex
        self.end_date = end_date
        self.authority = authority
        self.address = address
        self.number = number
        self.start_date = start_date
        self.back_image_url = back_image_url
        self.nationality = nationality
        self.birth = birth
        self.name = name
        self.front_image_url = front_image_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sex is not None:
            result['Sex'] = self.sex
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.authority is not None:
            result['Authority'] = self.authority
        if self.address is not None:
            result['Address'] = self.address
        if self.number is not None:
            result['Number'] = self.number
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.back_image_url is not None:
            result['BackImageUrl'] = self.back_image_url
        if self.nationality is not None:
            result['Nationality'] = self.nationality
        if self.birth is not None:
            result['Birth'] = self.birth
        if self.name is not None:
            result['Name'] = self.name
        if self.front_image_url is not None:
            result['FrontImageUrl'] = self.front_image_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Sex') is not None:
            self.sex = m.get('Sex')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('Authority') is not None:
            self.authority = m.get('Authority')
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('Number') is not None:
            self.number = m.get('Number')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('BackImageUrl') is not None:
            self.back_image_url = m.get('BackImageUrl')
        if m.get('Nationality') is not None:
            self.nationality = m.get('Nationality')
        if m.get('Birth') is not None:
            self.birth = m.get('Birth')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('FrontImageUrl') is not None:
            self.front_image_url = m.get('FrontImageUrl')
        return self


class VerifyMaterialResponseBodyResultObjectMaterial(TeaModel):
    def __init__(
        self,
        id_card_number: str = None,
        face_global_url: str = None,
        face_image_url: str = None,
        face_mask: str = None,
        id_card_name: str = None,
        face_quality: str = None,
        id_card_info: VerifyMaterialResponseBodyResultObjectMaterialIdCardInfo = None,
    ):
        self.id_card_number = id_card_number
        self.face_global_url = face_global_url
        self.face_image_url = face_image_url
        self.face_mask = face_mask
        self.id_card_name = id_card_name
        self.face_quality = face_quality
        self.id_card_info = id_card_info

    def validate(self):
        if self.id_card_info:
            self.id_card_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id_card_number is not None:
            result['IdCardNumber'] = self.id_card_number
        if self.face_global_url is not None:
            result['FaceGlobalUrl'] = self.face_global_url
        if self.face_image_url is not None:
            result['FaceImageUrl'] = self.face_image_url
        if self.face_mask is not None:
            result['FaceMask'] = self.face_mask
        if self.id_card_name is not None:
            result['IdCardName'] = self.id_card_name
        if self.face_quality is not None:
            result['FaceQuality'] = self.face_quality
        if self.id_card_info is not None:
            result['IdCardInfo'] = self.id_card_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IdCardNumber') is not None:
            self.id_card_number = m.get('IdCardNumber')
        if m.get('FaceGlobalUrl') is not None:
            self.face_global_url = m.get('FaceGlobalUrl')
        if m.get('FaceImageUrl') is not None:
            self.face_image_url = m.get('FaceImageUrl')
        if m.get('FaceMask') is not None:
            self.face_mask = m.get('FaceMask')
        if m.get('IdCardName') is not None:
            self.id_card_name = m.get('IdCardName')
        if m.get('FaceQuality') is not None:
            self.face_quality = m.get('FaceQuality')
        if m.get('IdCardInfo') is not None:
            temp_model = VerifyMaterialResponseBodyResultObjectMaterialIdCardInfo()
            self.id_card_info = temp_model.from_map(m['IdCardInfo'])
        return self


class VerifyMaterialResponseBodyResultObject(TeaModel):
    def __init__(
        self,
        authority_comparision_score: float = None,
        verify_status: int = None,
        verify_token: str = None,
        id_card_face_comparison_score: float = None,
        material: VerifyMaterialResponseBodyResultObjectMaterial = None,
    ):
        self.authority_comparision_score = authority_comparision_score
        self.verify_status = verify_status
        self.verify_token = verify_token
        self.id_card_face_comparison_score = id_card_face_comparison_score
        self.material = material

    def validate(self):
        if self.material:
            self.material.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authority_comparision_score is not None:
            result['AuthorityComparisionScore'] = self.authority_comparision_score
        if self.verify_status is not None:
            result['VerifyStatus'] = self.verify_status
        if self.verify_token is not None:
            result['VerifyToken'] = self.verify_token
        if self.id_card_face_comparison_score is not None:
            result['IdCardFaceComparisonScore'] = self.id_card_face_comparison_score
        if self.material is not None:
            result['Material'] = self.material.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorityComparisionScore') is not None:
            self.authority_comparision_score = m.get('AuthorityComparisionScore')
        if m.get('VerifyStatus') is not None:
            self.verify_status = m.get('VerifyStatus')
        if m.get('VerifyToken') is not None:
            self.verify_token = m.get('VerifyToken')
        if m.get('IdCardFaceComparisonScore') is not None:
            self.id_card_face_comparison_score = m.get('IdCardFaceComparisonScore')
        if m.get('Material') is not None:
            temp_model = VerifyMaterialResponseBodyResultObjectMaterial()
            self.material = temp_model.from_map(m['Material'])
        return self


class VerifyMaterialResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result_object: VerifyMaterialResponseBodyResultObject = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result_object = result_object

    def validate(self):
        if self.result_object:
            self.result_object.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = VerifyMaterialResponseBodyResultObject()
            self.result_object = temp_model.from_map(m['ResultObject'])
        return self


class VerifyMaterialResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: VerifyMaterialResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = VerifyMaterialResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


