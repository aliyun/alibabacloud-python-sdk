# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import BinaryIO, Dict, List


class DetectCardScreenshotRequest(TeaModel):
    def __init__(
        self,
        image_url: str = None,
    ):
        self.image_url = image_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        return self


class DetectCardScreenshotAdvanceRequest(TeaModel):
    def __init__(
        self,
        image_urlobject: BinaryIO = None,
    ):
        self.image_urlobject = image_urlobject

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        result = dict()
        if self.image_urlobject is not None:
            result['ImageURLObject'] = self.image_urlobject
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURLObject') is not None:
            self.image_urlobject = m.get('ImageURLObject')
        return self


class DetectCardScreenshotResponseBodyDataSpoofResultResultMap(TeaModel):
    def __init__(
        self,
        screen_threshold: float = None,
        screen_score: float = None,
    ):
        self.screen_threshold = screen_threshold
        self.screen_score = screen_score

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.screen_threshold is not None:
            result['ScreenThreshold'] = self.screen_threshold
        if self.screen_score is not None:
            result['ScreenScore'] = self.screen_score
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ScreenThreshold') is not None:
            self.screen_threshold = m.get('ScreenThreshold')
        if m.get('ScreenScore') is not None:
            self.screen_score = m.get('ScreenScore')
        return self


class DetectCardScreenshotResponseBodyDataSpoofResult(TeaModel):
    def __init__(
        self,
        is_spoof: bool = None,
        result_map: DetectCardScreenshotResponseBodyDataSpoofResultResultMap = None,
    ):
        self.is_spoof = is_spoof
        self.result_map = result_map

    def validate(self):
        if self.result_map:
            self.result_map.validate()

    def to_map(self):
        result = dict()
        if self.is_spoof is not None:
            result['IsSpoof'] = self.is_spoof
        if self.result_map is not None:
            result['ResultMap'] = self.result_map.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsSpoof') is not None:
            self.is_spoof = m.get('IsSpoof')
        if m.get('ResultMap') is not None:
            temp_model = DetectCardScreenshotResponseBodyDataSpoofResultResultMap()
            self.result_map = temp_model.from_map(m['ResultMap'])
        return self


class DetectCardScreenshotResponseBodyData(TeaModel):
    def __init__(
        self,
        is_blur: bool = None,
        is_card: bool = None,
        spoof_result: DetectCardScreenshotResponseBodyDataSpoofResult = None,
    ):
        self.is_blur = is_blur
        self.is_card = is_card
        self.spoof_result = spoof_result

    def validate(self):
        if self.spoof_result:
            self.spoof_result.validate()

    def to_map(self):
        result = dict()
        if self.is_blur is not None:
            result['IsBlur'] = self.is_blur
        if self.is_card is not None:
            result['IsCard'] = self.is_card
        if self.spoof_result is not None:
            result['SpoofResult'] = self.spoof_result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsBlur') is not None:
            self.is_blur = m.get('IsBlur')
        if m.get('IsCard') is not None:
            self.is_card = m.get('IsCard')
        if m.get('SpoofResult') is not None:
            temp_model = DetectCardScreenshotResponseBodyDataSpoofResult()
            self.spoof_result = temp_model.from_map(m['SpoofResult'])
        return self


class DetectCardScreenshotResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: DetectCardScreenshotResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = DetectCardScreenshotResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class DetectCardScreenshotResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DetectCardScreenshotResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DetectCardScreenshotResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAsyncJobResultRequest(TeaModel):
    def __init__(
        self,
        async_: bool = None,
        job_id: str = None,
    ):
        self.async_ = async_
        self.job_id = job_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.async_ is not None:
            result['Async'] = self.async_
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Async') is not None:
            self.async_ = m.get('Async')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class GetAsyncJobResultResponseBodyData(TeaModel):
    def __init__(
        self,
        status: str = None,
        error_message: str = None,
        result: str = None,
        error_code: str = None,
        job_id: str = None,
    ):
        self.status = status
        self.error_message = error_message
        self.result = result
        self.error_code = error_code
        self.job_id = job_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.result is not None:
            result['Result'] = self.result
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class GetAsyncJobResultResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: GetAsyncJobResultResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = GetAsyncJobResultResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class GetAsyncJobResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetAsyncJobResultResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = GetAsyncJobResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeAccountPageRequest(TeaModel):
    def __init__(
        self,
        image_type: int = None,
        image_url: str = None,
    ):
        self.image_type = image_type
        self.image_url = image_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.image_type is not None:
            result['ImageType'] = self.image_type
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageType') is not None:
            self.image_type = m.get('ImageType')
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        return self


class RecognizeAccountPageAdvanceRequest(TeaModel):
    def __init__(
        self,
        image_urlobject: BinaryIO = None,
        image_type: int = None,
    ):
        self.image_urlobject = image_urlobject
        self.image_type = image_type

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        result = dict()
        if self.image_urlobject is not None:
            result['ImageURLObject'] = self.image_urlobject
        if self.image_type is not None:
            result['ImageType'] = self.image_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURLObject') is not None:
            self.image_urlobject = m.get('ImageURLObject')
        if m.get('ImageType') is not None:
            self.image_type = m.get('ImageType')
        return self


class RecognizeAccountPageResponseBodyDataTitleArea(TeaModel):
    def __init__(
        self,
        top: int = None,
        width: int = None,
        height: int = None,
        left: int = None,
    ):
        self.top = top
        self.width = width
        self.height = height
        self.left = left

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.top is not None:
            result['Top'] = self.top
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        if self.left is not None:
            result['Left'] = self.left
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Top') is not None:
            self.top = m.get('Top')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Left') is not None:
            self.left = m.get('Left')
        return self


class RecognizeAccountPageResponseBodyDataRegisterStampAreas(TeaModel):
    def __init__(
        self,
        top: int = None,
        width: int = None,
        height: int = None,
        left: int = None,
    ):
        self.top = top
        self.width = width
        self.height = height
        self.left = left

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.top is not None:
            result['Top'] = self.top
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        if self.left is not None:
            result['Left'] = self.left
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Top') is not None:
            self.top = m.get('Top')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Left') is not None:
            self.left = m.get('Left')
        return self


class RecognizeAccountPageResponseBodyDataOtherStampAreas(TeaModel):
    def __init__(
        self,
        top: int = None,
        width: int = None,
        height: int = None,
        left: int = None,
    ):
        self.top = top
        self.width = width
        self.height = height
        self.left = left

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.top is not None:
            result['Top'] = self.top
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        if self.left is not None:
            result['Left'] = self.left
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Top') is not None:
            self.top = m.get('Top')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Left') is not None:
            self.left = m.get('Left')
        return self


class RecognizeAccountPageResponseBodyDataUndertakeStampAreas(TeaModel):
    def __init__(
        self,
        top: int = None,
        width: int = None,
        height: int = None,
        left: int = None,
    ):
        self.top = top
        self.width = width
        self.height = height
        self.left = left

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.top is not None:
            result['Top'] = self.top
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        if self.left is not None:
            result['Left'] = self.left
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Top') is not None:
            self.top = m.get('Top')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Left') is not None:
            self.left = m.get('Left')
        return self


class RecognizeAccountPageResponseBodyDataInvalidStampAreas(TeaModel):
    def __init__(
        self,
        top: int = None,
        width: int = None,
        height: int = None,
        left: int = None,
    ):
        self.top = top
        self.width = width
        self.height = height
        self.left = left

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.top is not None:
            result['Top'] = self.top
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        if self.left is not None:
            result['Left'] = self.left
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Top') is not None:
            self.top = m.get('Top')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Left') is not None:
            self.left = m.get('Left')
        return self


class RecognizeAccountPageResponseBodyData(TeaModel):
    def __init__(
        self,
        gender: str = None,
        title_area: RecognizeAccountPageResponseBodyDataTitleArea = None,
        angle: float = None,
        register_stamp_areas: List[RecognizeAccountPageResponseBodyDataRegisterStampAreas] = None,
        nationality: str = None,
        birth_place: str = None,
        other_stamp_areas: List[RecognizeAccountPageResponseBodyDataOtherStampAreas] = None,
        undertake_stamp_areas: List[RecognizeAccountPageResponseBodyDataUndertakeStampAreas] = None,
        birth_date: str = None,
        relation: str = None,
        native_place: str = None,
        name: str = None,
        idnumber: str = None,
        invalid_stamp_areas: List[RecognizeAccountPageResponseBodyDataInvalidStampAreas] = None,
    ):
        self.gender = gender
        self.title_area = title_area
        self.angle = angle
        self.register_stamp_areas = register_stamp_areas
        self.nationality = nationality
        self.birth_place = birth_place
        self.other_stamp_areas = other_stamp_areas
        self.undertake_stamp_areas = undertake_stamp_areas
        self.birth_date = birth_date
        self.relation = relation
        self.native_place = native_place
        self.name = name
        self.idnumber = idnumber
        self.invalid_stamp_areas = invalid_stamp_areas

    def validate(self):
        if self.title_area:
            self.title_area.validate()
        if self.register_stamp_areas:
            for k in self.register_stamp_areas:
                if k:
                    k.validate()
        if self.other_stamp_areas:
            for k in self.other_stamp_areas:
                if k:
                    k.validate()
        if self.undertake_stamp_areas:
            for k in self.undertake_stamp_areas:
                if k:
                    k.validate()
        if self.invalid_stamp_areas:
            for k in self.invalid_stamp_areas:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.gender is not None:
            result['Gender'] = self.gender
        if self.title_area is not None:
            result['TitleArea'] = self.title_area.to_map()
        if self.angle is not None:
            result['Angle'] = self.angle
        result['RegisterStampAreas'] = []
        if self.register_stamp_areas is not None:
            for k in self.register_stamp_areas:
                result['RegisterStampAreas'].append(k.to_map() if k else None)
        if self.nationality is not None:
            result['Nationality'] = self.nationality
        if self.birth_place is not None:
            result['BirthPlace'] = self.birth_place
        result['OtherStampAreas'] = []
        if self.other_stamp_areas is not None:
            for k in self.other_stamp_areas:
                result['OtherStampAreas'].append(k.to_map() if k else None)
        result['UndertakeStampAreas'] = []
        if self.undertake_stamp_areas is not None:
            for k in self.undertake_stamp_areas:
                result['UndertakeStampAreas'].append(k.to_map() if k else None)
        if self.birth_date is not None:
            result['BirthDate'] = self.birth_date
        if self.relation is not None:
            result['Relation'] = self.relation
        if self.native_place is not None:
            result['NativePlace'] = self.native_place
        if self.name is not None:
            result['Name'] = self.name
        if self.idnumber is not None:
            result['IDNumber'] = self.idnumber
        result['InvalidStampAreas'] = []
        if self.invalid_stamp_areas is not None:
            for k in self.invalid_stamp_areas:
                result['InvalidStampAreas'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Gender') is not None:
            self.gender = m.get('Gender')
        if m.get('TitleArea') is not None:
            temp_model = RecognizeAccountPageResponseBodyDataTitleArea()
            self.title_area = temp_model.from_map(m['TitleArea'])
        if m.get('Angle') is not None:
            self.angle = m.get('Angle')
        self.register_stamp_areas = []
        if m.get('RegisterStampAreas') is not None:
            for k in m.get('RegisterStampAreas'):
                temp_model = RecognizeAccountPageResponseBodyDataRegisterStampAreas()
                self.register_stamp_areas.append(temp_model.from_map(k))
        if m.get('Nationality') is not None:
            self.nationality = m.get('Nationality')
        if m.get('BirthPlace') is not None:
            self.birth_place = m.get('BirthPlace')
        self.other_stamp_areas = []
        if m.get('OtherStampAreas') is not None:
            for k in m.get('OtherStampAreas'):
                temp_model = RecognizeAccountPageResponseBodyDataOtherStampAreas()
                self.other_stamp_areas.append(temp_model.from_map(k))
        self.undertake_stamp_areas = []
        if m.get('UndertakeStampAreas') is not None:
            for k in m.get('UndertakeStampAreas'):
                temp_model = RecognizeAccountPageResponseBodyDataUndertakeStampAreas()
                self.undertake_stamp_areas.append(temp_model.from_map(k))
        if m.get('BirthDate') is not None:
            self.birth_date = m.get('BirthDate')
        if m.get('Relation') is not None:
            self.relation = m.get('Relation')
        if m.get('NativePlace') is not None:
            self.native_place = m.get('NativePlace')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('IDNumber') is not None:
            self.idnumber = m.get('IDNumber')
        self.invalid_stamp_areas = []
        if m.get('InvalidStampAreas') is not None:
            for k in m.get('InvalidStampAreas'):
                temp_model = RecognizeAccountPageResponseBodyDataInvalidStampAreas()
                self.invalid_stamp_areas.append(temp_model.from_map(k))
        return self


class RecognizeAccountPageResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: RecognizeAccountPageResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = RecognizeAccountPageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class RecognizeAccountPageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RecognizeAccountPageResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = RecognizeAccountPageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeBankCardRequest(TeaModel):
    def __init__(
        self,
        image_type: int = None,
        image_url: str = None,
    ):
        self.image_type = image_type
        self.image_url = image_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.image_type is not None:
            result['ImageType'] = self.image_type
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageType') is not None:
            self.image_type = m.get('ImageType')
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        return self


class RecognizeBankCardAdvanceRequest(TeaModel):
    def __init__(
        self,
        image_urlobject: BinaryIO = None,
        image_type: int = None,
    ):
        self.image_urlobject = image_urlobject
        self.image_type = image_type

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        result = dict()
        if self.image_urlobject is not None:
            result['ImageURLObject'] = self.image_urlobject
        if self.image_type is not None:
            result['ImageType'] = self.image_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURLObject') is not None:
            self.image_urlobject = m.get('ImageURLObject')
        if m.get('ImageType') is not None:
            self.image_type = m.get('ImageType')
        return self


class RecognizeBankCardResponseBodyData(TeaModel):
    def __init__(
        self,
        card_number: str = None,
        valid_date: str = None,
        bank_name: str = None,
    ):
        self.card_number = card_number
        self.valid_date = valid_date
        self.bank_name = bank_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.card_number is not None:
            result['CardNumber'] = self.card_number
        if self.valid_date is not None:
            result['ValidDate'] = self.valid_date
        if self.bank_name is not None:
            result['BankName'] = self.bank_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CardNumber') is not None:
            self.card_number = m.get('CardNumber')
        if m.get('ValidDate') is not None:
            self.valid_date = m.get('ValidDate')
        if m.get('BankName') is not None:
            self.bank_name = m.get('BankName')
        return self


class RecognizeBankCardResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: RecognizeBankCardResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = RecognizeBankCardResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class RecognizeBankCardResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RecognizeBankCardResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = RecognizeBankCardResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeBusinessCardRequest(TeaModel):
    def __init__(
        self,
        image_type: int = None,
        image_url: str = None,
    ):
        self.image_type = image_type
        self.image_url = image_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.image_type is not None:
            result['ImageType'] = self.image_type
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageType') is not None:
            self.image_type = m.get('ImageType')
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        return self


class RecognizeBusinessCardAdvanceRequest(TeaModel):
    def __init__(
        self,
        image_urlobject: BinaryIO = None,
        image_type: int = None,
    ):
        self.image_urlobject = image_urlobject
        self.image_type = image_type

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        result = dict()
        if self.image_urlobject is not None:
            result['ImageURLObject'] = self.image_urlobject
        if self.image_type is not None:
            result['ImageType'] = self.image_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURLObject') is not None:
            self.image_urlobject = m.get('ImageURLObject')
        if m.get('ImageType') is not None:
            self.image_type = m.get('ImageType')
        return self


class RecognizeBusinessCardResponseBodyData(TeaModel):
    def __init__(
        self,
        companies: List[str] = None,
        titles: List[str] = None,
        emails: List[str] = None,
        departments: List[str] = None,
        office_phone_numbers: List[str] = None,
        name: str = None,
        cell_phone_numbers: List[str] = None,
        addresses: List[str] = None,
    ):
        self.companies = companies
        self.titles = titles
        self.emails = emails
        self.departments = departments
        self.office_phone_numbers = office_phone_numbers
        self.name = name
        self.cell_phone_numbers = cell_phone_numbers
        self.addresses = addresses

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.companies is not None:
            result['Companies'] = self.companies
        if self.titles is not None:
            result['Titles'] = self.titles
        if self.emails is not None:
            result['Emails'] = self.emails
        if self.departments is not None:
            result['Departments'] = self.departments
        if self.office_phone_numbers is not None:
            result['OfficePhoneNumbers'] = self.office_phone_numbers
        if self.name is not None:
            result['Name'] = self.name
        if self.cell_phone_numbers is not None:
            result['CellPhoneNumbers'] = self.cell_phone_numbers
        if self.addresses is not None:
            result['Addresses'] = self.addresses
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Companies') is not None:
            self.companies = m.get('Companies')
        if m.get('Titles') is not None:
            self.titles = m.get('Titles')
        if m.get('Emails') is not None:
            self.emails = m.get('Emails')
        if m.get('Departments') is not None:
            self.departments = m.get('Departments')
        if m.get('OfficePhoneNumbers') is not None:
            self.office_phone_numbers = m.get('OfficePhoneNumbers')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('CellPhoneNumbers') is not None:
            self.cell_phone_numbers = m.get('CellPhoneNumbers')
        if m.get('Addresses') is not None:
            self.addresses = m.get('Addresses')
        return self


class RecognizeBusinessCardResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: RecognizeBusinessCardResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = RecognizeBusinessCardResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class RecognizeBusinessCardResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RecognizeBusinessCardResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = RecognizeBusinessCardResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeBusinessLicenseRequest(TeaModel):
    def __init__(
        self,
        image_type: int = None,
        image_url: str = None,
    ):
        self.image_type = image_type
        self.image_url = image_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.image_type is not None:
            result['ImageType'] = self.image_type
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageType') is not None:
            self.image_type = m.get('ImageType')
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        return self


class RecognizeBusinessLicenseAdvanceRequest(TeaModel):
    def __init__(
        self,
        image_urlobject: BinaryIO = None,
        image_type: int = None,
    ):
        self.image_urlobject = image_urlobject
        self.image_type = image_type

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        result = dict()
        if self.image_urlobject is not None:
            result['ImageURLObject'] = self.image_urlobject
        if self.image_type is not None:
            result['ImageType'] = self.image_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURLObject') is not None:
            self.image_urlobject = m.get('ImageURLObject')
        if m.get('ImageType') is not None:
            self.image_type = m.get('ImageType')
        return self


class RecognizeBusinessLicenseResponseBodyDataStamp(TeaModel):
    def __init__(
        self,
        top: int = None,
        width: int = None,
        height: int = None,
        left: int = None,
    ):
        self.top = top
        self.width = width
        self.height = height
        self.left = left

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.top is not None:
            result['Top'] = self.top
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        if self.left is not None:
            result['Left'] = self.left
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Top') is not None:
            self.top = m.get('Top')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Left') is not None:
            self.left = m.get('Left')
        return self


class RecognizeBusinessLicenseResponseBodyDataTitle(TeaModel):
    def __init__(
        self,
        top: int = None,
        width: int = None,
        height: int = None,
        left: int = None,
    ):
        self.top = top
        self.width = width
        self.height = height
        self.left = left

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.top is not None:
            result['Top'] = self.top
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        if self.left is not None:
            result['Left'] = self.left
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Top') is not None:
            self.top = m.get('Top')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Left') is not None:
            self.left = m.get('Left')
        return self


class RecognizeBusinessLicenseResponseBodyDataEmblem(TeaModel):
    def __init__(
        self,
        top: int = None,
        width: int = None,
        height: int = None,
        left: int = None,
    ):
        self.top = top
        self.width = width
        self.height = height
        self.left = left

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.top is not None:
            result['Top'] = self.top
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        if self.left is not None:
            result['Left'] = self.left
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Top') is not None:
            self.top = m.get('Top')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Left') is not None:
            self.left = m.get('Left')
        return self


class RecognizeBusinessLicenseResponseBodyDataQRCode(TeaModel):
    def __init__(
        self,
        top: int = None,
        width: int = None,
        height: int = None,
        left: int = None,
    ):
        self.top = top
        self.width = width
        self.height = height
        self.left = left

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.top is not None:
            result['Top'] = self.top
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        if self.left is not None:
            result['Left'] = self.left
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Top') is not None:
            self.top = m.get('Top')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Left') is not None:
            self.left = m.get('Left')
        return self


class RecognizeBusinessLicenseResponseBodyData(TeaModel):
    def __init__(
        self,
        type: str = None,
        stamp: RecognizeBusinessLicenseResponseBodyDataStamp = None,
        establish_date: str = None,
        valid_period: str = None,
        business: str = None,
        angle: float = None,
        register_number: str = None,
        address: str = None,
        capital: str = None,
        title: RecognizeBusinessLicenseResponseBodyDataTitle = None,
        emblem: RecognizeBusinessLicenseResponseBodyDataEmblem = None,
        name: str = None,
        qrcode: RecognizeBusinessLicenseResponseBodyDataQRCode = None,
        legal_person: str = None,
    ):
        self.type = type
        self.stamp = stamp
        self.establish_date = establish_date
        self.valid_period = valid_period
        self.business = business
        self.angle = angle
        self.register_number = register_number
        self.address = address
        self.capital = capital
        self.title = title
        self.emblem = emblem
        self.name = name
        self.qrcode = qrcode
        self.legal_person = legal_person

    def validate(self):
        if self.stamp:
            self.stamp.validate()
        if self.title:
            self.title.validate()
        if self.emblem:
            self.emblem.validate()
        if self.qrcode:
            self.qrcode.validate()

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.stamp is not None:
            result['Stamp'] = self.stamp.to_map()
        if self.establish_date is not None:
            result['EstablishDate'] = self.establish_date
        if self.valid_period is not None:
            result['ValidPeriod'] = self.valid_period
        if self.business is not None:
            result['Business'] = self.business
        if self.angle is not None:
            result['Angle'] = self.angle
        if self.register_number is not None:
            result['RegisterNumber'] = self.register_number
        if self.address is not None:
            result['Address'] = self.address
        if self.capital is not None:
            result['Capital'] = self.capital
        if self.title is not None:
            result['Title'] = self.title.to_map()
        if self.emblem is not None:
            result['Emblem'] = self.emblem.to_map()
        if self.name is not None:
            result['Name'] = self.name
        if self.qrcode is not None:
            result['QRCode'] = self.qrcode.to_map()
        if self.legal_person is not None:
            result['LegalPerson'] = self.legal_person
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Stamp') is not None:
            temp_model = RecognizeBusinessLicenseResponseBodyDataStamp()
            self.stamp = temp_model.from_map(m['Stamp'])
        if m.get('EstablishDate') is not None:
            self.establish_date = m.get('EstablishDate')
        if m.get('ValidPeriod') is not None:
            self.valid_period = m.get('ValidPeriod')
        if m.get('Business') is not None:
            self.business = m.get('Business')
        if m.get('Angle') is not None:
            self.angle = m.get('Angle')
        if m.get('RegisterNumber') is not None:
            self.register_number = m.get('RegisterNumber')
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('Capital') is not None:
            self.capital = m.get('Capital')
        if m.get('Title') is not None:
            temp_model = RecognizeBusinessLicenseResponseBodyDataTitle()
            self.title = temp_model.from_map(m['Title'])
        if m.get('Emblem') is not None:
            temp_model = RecognizeBusinessLicenseResponseBodyDataEmblem()
            self.emblem = temp_model.from_map(m['Emblem'])
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('QRCode') is not None:
            temp_model = RecognizeBusinessLicenseResponseBodyDataQRCode()
            self.qrcode = temp_model.from_map(m['QRCode'])
        if m.get('LegalPerson') is not None:
            self.legal_person = m.get('LegalPerson')
        return self


class RecognizeBusinessLicenseResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: RecognizeBusinessLicenseResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = RecognizeBusinessLicenseResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class RecognizeBusinessLicenseResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RecognizeBusinessLicenseResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = RecognizeBusinessLicenseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeCharacterRequest(TeaModel):
    def __init__(
        self,
        image_type: int = None,
        image_url: str = None,
        min_height: int = None,
        output_probability: bool = None,
    ):
        self.image_type = image_type
        self.image_url = image_url
        self.min_height = min_height
        self.output_probability = output_probability

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.image_type is not None:
            result['ImageType'] = self.image_type
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        if self.min_height is not None:
            result['MinHeight'] = self.min_height
        if self.output_probability is not None:
            result['OutputProbability'] = self.output_probability
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageType') is not None:
            self.image_type = m.get('ImageType')
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        if m.get('MinHeight') is not None:
            self.min_height = m.get('MinHeight')
        if m.get('OutputProbability') is not None:
            self.output_probability = m.get('OutputProbability')
        return self


class RecognizeCharacterAdvanceRequest(TeaModel):
    def __init__(
        self,
        image_urlobject: BinaryIO = None,
        image_type: int = None,
        min_height: int = None,
        output_probability: bool = None,
    ):
        self.image_urlobject = image_urlobject
        self.image_type = image_type
        self.min_height = min_height
        self.output_probability = output_probability

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        result = dict()
        if self.image_urlobject is not None:
            result['ImageURLObject'] = self.image_urlobject
        if self.image_type is not None:
            result['ImageType'] = self.image_type
        if self.min_height is not None:
            result['MinHeight'] = self.min_height
        if self.output_probability is not None:
            result['OutputProbability'] = self.output_probability
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURLObject') is not None:
            self.image_urlobject = m.get('ImageURLObject')
        if m.get('ImageType') is not None:
            self.image_type = m.get('ImageType')
        if m.get('MinHeight') is not None:
            self.min_height = m.get('MinHeight')
        if m.get('OutputProbability') is not None:
            self.output_probability = m.get('OutputProbability')
        return self


class RecognizeCharacterResponseBodyDataResultsTextRectangles(TeaModel):
    def __init__(
        self,
        top: int = None,
        width: int = None,
        height: int = None,
        angle: int = None,
        left: int = None,
    ):
        self.top = top
        self.width = width
        self.height = height
        self.angle = angle
        self.left = left

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.top is not None:
            result['Top'] = self.top
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        if self.angle is not None:
            result['Angle'] = self.angle
        if self.left is not None:
            result['Left'] = self.left
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Top') is not None:
            self.top = m.get('Top')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Angle') is not None:
            self.angle = m.get('Angle')
        if m.get('Left') is not None:
            self.left = m.get('Left')
        return self


class RecognizeCharacterResponseBodyDataResults(TeaModel):
    def __init__(
        self,
        text_rectangles: RecognizeCharacterResponseBodyDataResultsTextRectangles = None,
        text: str = None,
        probability: float = None,
    ):
        self.text_rectangles = text_rectangles
        self.text = text
        self.probability = probability

    def validate(self):
        if self.text_rectangles:
            self.text_rectangles.validate()

    def to_map(self):
        result = dict()
        if self.text_rectangles is not None:
            result['TextRectangles'] = self.text_rectangles.to_map()
        if self.text is not None:
            result['Text'] = self.text
        if self.probability is not None:
            result['Probability'] = self.probability
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TextRectangles') is not None:
            temp_model = RecognizeCharacterResponseBodyDataResultsTextRectangles()
            self.text_rectangles = temp_model.from_map(m['TextRectangles'])
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('Probability') is not None:
            self.probability = m.get('Probability')
        return self


class RecognizeCharacterResponseBodyData(TeaModel):
    def __init__(
        self,
        results: List[RecognizeCharacterResponseBodyDataResults] = None,
    ):
        self.results = results

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.results = []
        if m.get('Results') is not None:
            for k in m.get('Results'):
                temp_model = RecognizeCharacterResponseBodyDataResults()
                self.results.append(temp_model.from_map(k))
        return self


class RecognizeCharacterResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: RecognizeCharacterResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = RecognizeCharacterResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class RecognizeCharacterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RecognizeCharacterResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = RecognizeCharacterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeChinapassportRequest(TeaModel):
    def __init__(
        self,
        image_url: str = None,
    ):
        self.image_url = image_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        return self


class RecognizeChinapassportAdvanceRequest(TeaModel):
    def __init__(
        self,
        image_urlobject: BinaryIO = None,
    ):
        self.image_urlobject = image_urlobject

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        result = dict()
        if self.image_urlobject is not None:
            result['ImageURLObject'] = self.image_urlobject
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURLObject') is not None:
            self.image_urlobject = m.get('ImageURLObject')
        return self


class RecognizeChinapassportResponseBodyData(TeaModel):
    def __init__(
        self,
        type: str = None,
        sex: str = None,
        authority: str = None,
        issue_place_raw: str = None,
        success: bool = None,
        line_one: str = None,
        expiry_date: str = None,
        birth_place: str = None,
        passport_no: str = None,
        birth_place_raw: str = None,
        issue_date: str = None,
        source_country: str = None,
        birth_date: str = None,
        name_chinese_raw: str = None,
        issue_place: str = None,
        name_chinese: str = None,
        line_zero: str = None,
        country: str = None,
        birth_day: str = None,
        expiry_day: str = None,
        name: str = None,
        person_id: str = None,
    ):
        self.type = type
        self.sex = sex
        self.authority = authority
        self.issue_place_raw = issue_place_raw
        self.success = success
        self.line_one = line_one
        self.expiry_date = expiry_date
        self.birth_place = birth_place
        self.passport_no = passport_no
        self.birth_place_raw = birth_place_raw
        self.issue_date = issue_date
        self.source_country = source_country
        self.birth_date = birth_date
        self.name_chinese_raw = name_chinese_raw
        self.issue_place = issue_place
        self.name_chinese = name_chinese
        self.line_zero = line_zero
        self.country = country
        self.birth_day = birth_day
        self.expiry_day = expiry_day
        self.name = name
        self.person_id = person_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.sex is not None:
            result['Sex'] = self.sex
        if self.authority is not None:
            result['Authority'] = self.authority
        if self.issue_place_raw is not None:
            result['IssuePlaceRaw'] = self.issue_place_raw
        if self.success is not None:
            result['Success'] = self.success
        if self.line_one is not None:
            result['LineOne'] = self.line_one
        if self.expiry_date is not None:
            result['ExpiryDate'] = self.expiry_date
        if self.birth_place is not None:
            result['BirthPlace'] = self.birth_place
        if self.passport_no is not None:
            result['PassportNo'] = self.passport_no
        if self.birth_place_raw is not None:
            result['BirthPlaceRaw'] = self.birth_place_raw
        if self.issue_date is not None:
            result['IssueDate'] = self.issue_date
        if self.source_country is not None:
            result['SourceCountry'] = self.source_country
        if self.birth_date is not None:
            result['BirthDate'] = self.birth_date
        if self.name_chinese_raw is not None:
            result['NameChineseRaw'] = self.name_chinese_raw
        if self.issue_place is not None:
            result['IssuePlace'] = self.issue_place
        if self.name_chinese is not None:
            result['NameChinese'] = self.name_chinese
        if self.line_zero is not None:
            result['LineZero'] = self.line_zero
        if self.country is not None:
            result['Country'] = self.country
        if self.birth_day is not None:
            result['BirthDay'] = self.birth_day
        if self.expiry_day is not None:
            result['ExpiryDay'] = self.expiry_day
        if self.name is not None:
            result['Name'] = self.name
        if self.person_id is not None:
            result['PersonId'] = self.person_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Sex') is not None:
            self.sex = m.get('Sex')
        if m.get('Authority') is not None:
            self.authority = m.get('Authority')
        if m.get('IssuePlaceRaw') is not None:
            self.issue_place_raw = m.get('IssuePlaceRaw')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('LineOne') is not None:
            self.line_one = m.get('LineOne')
        if m.get('ExpiryDate') is not None:
            self.expiry_date = m.get('ExpiryDate')
        if m.get('BirthPlace') is not None:
            self.birth_place = m.get('BirthPlace')
        if m.get('PassportNo') is not None:
            self.passport_no = m.get('PassportNo')
        if m.get('BirthPlaceRaw') is not None:
            self.birth_place_raw = m.get('BirthPlaceRaw')
        if m.get('IssueDate') is not None:
            self.issue_date = m.get('IssueDate')
        if m.get('SourceCountry') is not None:
            self.source_country = m.get('SourceCountry')
        if m.get('BirthDate') is not None:
            self.birth_date = m.get('BirthDate')
        if m.get('NameChineseRaw') is not None:
            self.name_chinese_raw = m.get('NameChineseRaw')
        if m.get('IssuePlace') is not None:
            self.issue_place = m.get('IssuePlace')
        if m.get('NameChinese') is not None:
            self.name_chinese = m.get('NameChinese')
        if m.get('LineZero') is not None:
            self.line_zero = m.get('LineZero')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('BirthDay') is not None:
            self.birth_day = m.get('BirthDay')
        if m.get('ExpiryDay') is not None:
            self.expiry_day = m.get('ExpiryDay')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PersonId') is not None:
            self.person_id = m.get('PersonId')
        return self


class RecognizeChinapassportResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: RecognizeChinapassportResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = RecognizeChinapassportResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class RecognizeChinapassportResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RecognizeChinapassportResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = RecognizeChinapassportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeDriverLicenseRequest(TeaModel):
    def __init__(
        self,
        image_type: int = None,
        image_url: str = None,
        side: str = None,
    ):
        self.image_type = image_type
        self.image_url = image_url
        self.side = side

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.image_type is not None:
            result['ImageType'] = self.image_type
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        if self.side is not None:
            result['Side'] = self.side
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageType') is not None:
            self.image_type = m.get('ImageType')
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        if m.get('Side') is not None:
            self.side = m.get('Side')
        return self


class RecognizeDriverLicenseAdvanceRequest(TeaModel):
    def __init__(
        self,
        image_urlobject: BinaryIO = None,
        image_type: int = None,
        side: str = None,
    ):
        self.image_urlobject = image_urlobject
        self.image_type = image_type
        self.side = side

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        result = dict()
        if self.image_urlobject is not None:
            result['ImageURLObject'] = self.image_urlobject
        if self.image_type is not None:
            result['ImageType'] = self.image_type
        if self.side is not None:
            result['Side'] = self.side
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURLObject') is not None:
            self.image_urlobject = m.get('ImageURLObject')
        if m.get('ImageType') is not None:
            self.image_type = m.get('ImageType')
        if m.get('Side') is not None:
            self.side = m.get('Side')
        return self


class RecognizeDriverLicenseResponseBodyDataBackResult(TeaModel):
    def __init__(
        self,
        archive_number: str = None,
    ):
        self.archive_number = archive_number

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.archive_number is not None:
            result['ArchiveNumber'] = self.archive_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArchiveNumber') is not None:
            self.archive_number = m.get('ArchiveNumber')
        return self


class RecognizeDriverLicenseResponseBodyDataFaceResult(TeaModel):
    def __init__(
        self,
        vehicle_type: str = None,
        issue_date: str = None,
        end_date: str = None,
        gender: str = None,
        address: str = None,
        start_date: str = None,
        license_number: str = None,
        name: str = None,
    ):
        self.vehicle_type = vehicle_type
        self.issue_date = issue_date
        self.end_date = end_date
        self.gender = gender
        self.address = address
        self.start_date = start_date
        self.license_number = license_number
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.vehicle_type is not None:
            result['VehicleType'] = self.vehicle_type
        if self.issue_date is not None:
            result['IssueDate'] = self.issue_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.gender is not None:
            result['Gender'] = self.gender
        if self.address is not None:
            result['Address'] = self.address
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.license_number is not None:
            result['LicenseNumber'] = self.license_number
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VehicleType') is not None:
            self.vehicle_type = m.get('VehicleType')
        if m.get('IssueDate') is not None:
            self.issue_date = m.get('IssueDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('Gender') is not None:
            self.gender = m.get('Gender')
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('LicenseNumber') is not None:
            self.license_number = m.get('LicenseNumber')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class RecognizeDriverLicenseResponseBodyData(TeaModel):
    def __init__(
        self,
        back_result: RecognizeDriverLicenseResponseBodyDataBackResult = None,
        face_result: RecognizeDriverLicenseResponseBodyDataFaceResult = None,
    ):
        self.back_result = back_result
        self.face_result = face_result

    def validate(self):
        if self.back_result:
            self.back_result.validate()
        if self.face_result:
            self.face_result.validate()

    def to_map(self):
        result = dict()
        if self.back_result is not None:
            result['BackResult'] = self.back_result.to_map()
        if self.face_result is not None:
            result['FaceResult'] = self.face_result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackResult') is not None:
            temp_model = RecognizeDriverLicenseResponseBodyDataBackResult()
            self.back_result = temp_model.from_map(m['BackResult'])
        if m.get('FaceResult') is not None:
            temp_model = RecognizeDriverLicenseResponseBodyDataFaceResult()
            self.face_result = temp_model.from_map(m['FaceResult'])
        return self


class RecognizeDriverLicenseResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: RecognizeDriverLicenseResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = RecognizeDriverLicenseResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class RecognizeDriverLicenseResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RecognizeDriverLicenseResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = RecognizeDriverLicenseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeDrivingLicenseRequest(TeaModel):
    def __init__(
        self,
        image_type: int = None,
        image_url: str = None,
        side: str = None,
    ):
        self.image_type = image_type
        self.image_url = image_url
        self.side = side

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.image_type is not None:
            result['ImageType'] = self.image_type
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        if self.side is not None:
            result['Side'] = self.side
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageType') is not None:
            self.image_type = m.get('ImageType')
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        if m.get('Side') is not None:
            self.side = m.get('Side')
        return self


class RecognizeDrivingLicenseAdvanceRequest(TeaModel):
    def __init__(
        self,
        image_urlobject: BinaryIO = None,
        image_type: int = None,
        side: str = None,
    ):
        self.image_urlobject = image_urlobject
        self.image_type = image_type
        self.side = side

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        result = dict()
        if self.image_urlobject is not None:
            result['ImageURLObject'] = self.image_urlobject
        if self.image_type is not None:
            result['ImageType'] = self.image_type
        if self.side is not None:
            result['Side'] = self.side
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURLObject') is not None:
            self.image_urlobject = m.get('ImageURLObject')
        if m.get('ImageType') is not None:
            self.image_type = m.get('ImageType')
        if m.get('Side') is not None:
            self.side = m.get('Side')
        return self


class RecognizeDrivingLicenseResponseBodyDataBackResult(TeaModel):
    def __init__(
        self,
        overall_dimension: str = None,
        inspection_record: str = None,
        unladen_mass: str = None,
        file_number: str = None,
        traction_mass: str = None,
        gross_mass: str = None,
        plate_number: str = None,
        approved_passenger_capacity: str = None,
        energy_type: str = None,
        approved_load: str = None,
    ):
        self.overall_dimension = overall_dimension
        self.inspection_record = inspection_record
        self.unladen_mass = unladen_mass
        self.file_number = file_number
        self.traction_mass = traction_mass
        self.gross_mass = gross_mass
        self.plate_number = plate_number
        self.approved_passenger_capacity = approved_passenger_capacity
        self.energy_type = energy_type
        self.approved_load = approved_load

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.overall_dimension is not None:
            result['OverallDimension'] = self.overall_dimension
        if self.inspection_record is not None:
            result['InspectionRecord'] = self.inspection_record
        if self.unladen_mass is not None:
            result['UnladenMass'] = self.unladen_mass
        if self.file_number is not None:
            result['FileNumber'] = self.file_number
        if self.traction_mass is not None:
            result['TractionMass'] = self.traction_mass
        if self.gross_mass is not None:
            result['GrossMass'] = self.gross_mass
        if self.plate_number is not None:
            result['PlateNumber'] = self.plate_number
        if self.approved_passenger_capacity is not None:
            result['ApprovedPassengerCapacity'] = self.approved_passenger_capacity
        if self.energy_type is not None:
            result['EnergyType'] = self.energy_type
        if self.approved_load is not None:
            result['ApprovedLoad'] = self.approved_load
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OverallDimension') is not None:
            self.overall_dimension = m.get('OverallDimension')
        if m.get('InspectionRecord') is not None:
            self.inspection_record = m.get('InspectionRecord')
        if m.get('UnladenMass') is not None:
            self.unladen_mass = m.get('UnladenMass')
        if m.get('FileNumber') is not None:
            self.file_number = m.get('FileNumber')
        if m.get('TractionMass') is not None:
            self.traction_mass = m.get('TractionMass')
        if m.get('GrossMass') is not None:
            self.gross_mass = m.get('GrossMass')
        if m.get('PlateNumber') is not None:
            self.plate_number = m.get('PlateNumber')
        if m.get('ApprovedPassengerCapacity') is not None:
            self.approved_passenger_capacity = m.get('ApprovedPassengerCapacity')
        if m.get('EnergyType') is not None:
            self.energy_type = m.get('EnergyType')
        if m.get('ApprovedLoad') is not None:
            self.approved_load = m.get('ApprovedLoad')
        return self


class RecognizeDrivingLicenseResponseBodyDataFaceResult(TeaModel):
    def __init__(
        self,
        issue_date: str = None,
        model: str = None,
        vehicle_type: str = None,
        owner: str = None,
        engine_number: str = None,
        plate_number: str = None,
        address: str = None,
        use_character: str = None,
        vin: str = None,
        register_date: str = None,
    ):
        self.issue_date = issue_date
        self.model = model
        self.vehicle_type = vehicle_type
        self.owner = owner
        self.engine_number = engine_number
        self.plate_number = plate_number
        self.address = address
        self.use_character = use_character
        self.vin = vin
        self.register_date = register_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.issue_date is not None:
            result['IssueDate'] = self.issue_date
        if self.model is not None:
            result['Model'] = self.model
        if self.vehicle_type is not None:
            result['VehicleType'] = self.vehicle_type
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.engine_number is not None:
            result['EngineNumber'] = self.engine_number
        if self.plate_number is not None:
            result['PlateNumber'] = self.plate_number
        if self.address is not None:
            result['Address'] = self.address
        if self.use_character is not None:
            result['UseCharacter'] = self.use_character
        if self.vin is not None:
            result['Vin'] = self.vin
        if self.register_date is not None:
            result['RegisterDate'] = self.register_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IssueDate') is not None:
            self.issue_date = m.get('IssueDate')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('VehicleType') is not None:
            self.vehicle_type = m.get('VehicleType')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('EngineNumber') is not None:
            self.engine_number = m.get('EngineNumber')
        if m.get('PlateNumber') is not None:
            self.plate_number = m.get('PlateNumber')
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('UseCharacter') is not None:
            self.use_character = m.get('UseCharacter')
        if m.get('Vin') is not None:
            self.vin = m.get('Vin')
        if m.get('RegisterDate') is not None:
            self.register_date = m.get('RegisterDate')
        return self


class RecognizeDrivingLicenseResponseBodyData(TeaModel):
    def __init__(
        self,
        back_result: RecognizeDrivingLicenseResponseBodyDataBackResult = None,
        face_result: RecognizeDrivingLicenseResponseBodyDataFaceResult = None,
    ):
        self.back_result = back_result
        self.face_result = face_result

    def validate(self):
        if self.back_result:
            self.back_result.validate()
        if self.face_result:
            self.face_result.validate()

    def to_map(self):
        result = dict()
        if self.back_result is not None:
            result['BackResult'] = self.back_result.to_map()
        if self.face_result is not None:
            result['FaceResult'] = self.face_result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackResult') is not None:
            temp_model = RecognizeDrivingLicenseResponseBodyDataBackResult()
            self.back_result = temp_model.from_map(m['BackResult'])
        if m.get('FaceResult') is not None:
            temp_model = RecognizeDrivingLicenseResponseBodyDataFaceResult()
            self.face_result = temp_model.from_map(m['FaceResult'])
        return self


class RecognizeDrivingLicenseResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: RecognizeDrivingLicenseResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = RecognizeDrivingLicenseResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class RecognizeDrivingLicenseResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RecognizeDrivingLicenseResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = RecognizeDrivingLicenseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeIdentityCardRequest(TeaModel):
    def __init__(
        self,
        image_type: int = None,
        image_url: str = None,
        side: str = None,
    ):
        self.image_type = image_type
        self.image_url = image_url
        self.side = side

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.image_type is not None:
            result['ImageType'] = self.image_type
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        if self.side is not None:
            result['Side'] = self.side
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageType') is not None:
            self.image_type = m.get('ImageType')
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        if m.get('Side') is not None:
            self.side = m.get('Side')
        return self


class RecognizeIdentityCardAdvanceRequest(TeaModel):
    def __init__(
        self,
        image_urlobject: BinaryIO = None,
        image_type: int = None,
        side: str = None,
    ):
        self.image_urlobject = image_urlobject
        self.image_type = image_type
        self.side = side

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        result = dict()
        if self.image_urlobject is not None:
            result['ImageURLObject'] = self.image_urlobject
        if self.image_type is not None:
            result['ImageType'] = self.image_type
        if self.side is not None:
            result['Side'] = self.side
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURLObject') is not None:
            self.image_urlobject = m.get('ImageURLObject')
        if m.get('ImageType') is not None:
            self.image_type = m.get('ImageType')
        if m.get('Side') is not None:
            self.side = m.get('Side')
        return self


class RecognizeIdentityCardResponseBodyDataBackResult(TeaModel):
    def __init__(
        self,
        end_date: str = None,
        issue: str = None,
        start_date: str = None,
    ):
        self.end_date = end_date
        self.issue = issue
        self.start_date = start_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.issue is not None:
            result['Issue'] = self.issue
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('Issue') is not None:
            self.issue = m.get('Issue')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        return self


class RecognizeIdentityCardResponseBodyDataFrontResultFaceRectangleSize(TeaModel):
    def __init__(
        self,
        width: float = None,
        height: float = None,
    ):
        self.width = width
        self.height = height

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        return self


class RecognizeIdentityCardResponseBodyDataFrontResultFaceRectangleCenter(TeaModel):
    def __init__(
        self,
        y: float = None,
        x: float = None,
    ):
        self.y = y
        self.x = x

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.y is not None:
            result['Y'] = self.y
        if self.x is not None:
            result['X'] = self.x
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Y') is not None:
            self.y = m.get('Y')
        if m.get('X') is not None:
            self.x = m.get('X')
        return self


class RecognizeIdentityCardResponseBodyDataFrontResultFaceRectangle(TeaModel):
    def __init__(
        self,
        size: RecognizeIdentityCardResponseBodyDataFrontResultFaceRectangleSize = None,
        angle: float = None,
        center: RecognizeIdentityCardResponseBodyDataFrontResultFaceRectangleCenter = None,
    ):
        self.size = size
        self.angle = angle
        self.center = center

    def validate(self):
        if self.size:
            self.size.validate()
        if self.center:
            self.center.validate()

    def to_map(self):
        result = dict()
        if self.size is not None:
            result['Size'] = self.size.to_map()
        if self.angle is not None:
            result['Angle'] = self.angle
        if self.center is not None:
            result['Center'] = self.center.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Size') is not None:
            temp_model = RecognizeIdentityCardResponseBodyDataFrontResultFaceRectangleSize()
            self.size = temp_model.from_map(m['Size'])
        if m.get('Angle') is not None:
            self.angle = m.get('Angle')
        if m.get('Center') is not None:
            temp_model = RecognizeIdentityCardResponseBodyDataFrontResultFaceRectangleCenter()
            self.center = temp_model.from_map(m['Center'])
        return self


class RecognizeIdentityCardResponseBodyDataFrontResultFaceRectVertices(TeaModel):
    def __init__(
        self,
        y: float = None,
        x: float = None,
    ):
        self.y = y
        self.x = x

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.y is not None:
            result['Y'] = self.y
        if self.x is not None:
            result['X'] = self.x
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Y') is not None:
            self.y = m.get('Y')
        if m.get('X') is not None:
            self.x = m.get('X')
        return self


class RecognizeIdentityCardResponseBodyDataFrontResultCardAreas(TeaModel):
    def __init__(
        self,
        y: float = None,
        x: float = None,
    ):
        self.y = y
        self.x = x

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.y is not None:
            result['Y'] = self.y
        if self.x is not None:
            result['X'] = self.x
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Y') is not None:
            self.y = m.get('Y')
        if m.get('X') is not None:
            self.x = m.get('X')
        return self


class RecognizeIdentityCardResponseBodyDataFrontResult(TeaModel):
    def __init__(
        self,
        face_rectangle: RecognizeIdentityCardResponseBodyDataFrontResultFaceRectangle = None,
        birth_date: str = None,
        gender: str = None,
        address: str = None,
        face_rect_vertices: List[RecognizeIdentityCardResponseBodyDataFrontResultFaceRectVertices] = None,
        card_areas: List[RecognizeIdentityCardResponseBodyDataFrontResultCardAreas] = None,
        nationality: str = None,
        name: str = None,
        idnumber: str = None,
    ):
        self.face_rectangle = face_rectangle
        self.birth_date = birth_date
        self.gender = gender
        self.address = address
        self.face_rect_vertices = face_rect_vertices
        self.card_areas = card_areas
        self.nationality = nationality
        self.name = name
        self.idnumber = idnumber

    def validate(self):
        if self.face_rectangle:
            self.face_rectangle.validate()
        if self.face_rect_vertices:
            for k in self.face_rect_vertices:
                if k:
                    k.validate()
        if self.card_areas:
            for k in self.card_areas:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.face_rectangle is not None:
            result['FaceRectangle'] = self.face_rectangle.to_map()
        if self.birth_date is not None:
            result['BirthDate'] = self.birth_date
        if self.gender is not None:
            result['Gender'] = self.gender
        if self.address is not None:
            result['Address'] = self.address
        result['FaceRectVertices'] = []
        if self.face_rect_vertices is not None:
            for k in self.face_rect_vertices:
                result['FaceRectVertices'].append(k.to_map() if k else None)
        result['CardAreas'] = []
        if self.card_areas is not None:
            for k in self.card_areas:
                result['CardAreas'].append(k.to_map() if k else None)
        if self.nationality is not None:
            result['Nationality'] = self.nationality
        if self.name is not None:
            result['Name'] = self.name
        if self.idnumber is not None:
            result['IDNumber'] = self.idnumber
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FaceRectangle') is not None:
            temp_model = RecognizeIdentityCardResponseBodyDataFrontResultFaceRectangle()
            self.face_rectangle = temp_model.from_map(m['FaceRectangle'])
        if m.get('BirthDate') is not None:
            self.birth_date = m.get('BirthDate')
        if m.get('Gender') is not None:
            self.gender = m.get('Gender')
        if m.get('Address') is not None:
            self.address = m.get('Address')
        self.face_rect_vertices = []
        if m.get('FaceRectVertices') is not None:
            for k in m.get('FaceRectVertices'):
                temp_model = RecognizeIdentityCardResponseBodyDataFrontResultFaceRectVertices()
                self.face_rect_vertices.append(temp_model.from_map(k))
        self.card_areas = []
        if m.get('CardAreas') is not None:
            for k in m.get('CardAreas'):
                temp_model = RecognizeIdentityCardResponseBodyDataFrontResultCardAreas()
                self.card_areas.append(temp_model.from_map(k))
        if m.get('Nationality') is not None:
            self.nationality = m.get('Nationality')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('IDNumber') is not None:
            self.idnumber = m.get('IDNumber')
        return self


class RecognizeIdentityCardResponseBodyData(TeaModel):
    def __init__(
        self,
        back_result: RecognizeIdentityCardResponseBodyDataBackResult = None,
        front_result: RecognizeIdentityCardResponseBodyDataFrontResult = None,
    ):
        self.back_result = back_result
        self.front_result = front_result

    def validate(self):
        if self.back_result:
            self.back_result.validate()
        if self.front_result:
            self.front_result.validate()

    def to_map(self):
        result = dict()
        if self.back_result is not None:
            result['BackResult'] = self.back_result.to_map()
        if self.front_result is not None:
            result['FrontResult'] = self.front_result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackResult') is not None:
            temp_model = RecognizeIdentityCardResponseBodyDataBackResult()
            self.back_result = temp_model.from_map(m['BackResult'])
        if m.get('FrontResult') is not None:
            temp_model = RecognizeIdentityCardResponseBodyDataFrontResult()
            self.front_result = temp_model.from_map(m['FrontResult'])
        return self


class RecognizeIdentityCardResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: RecognizeIdentityCardResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = RecognizeIdentityCardResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class RecognizeIdentityCardResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RecognizeIdentityCardResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = RecognizeIdentityCardResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeLicensePlateRequest(TeaModel):
    def __init__(
        self,
        image_type: int = None,
        image_url: str = None,
    ):
        self.image_type = image_type
        self.image_url = image_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.image_type is not None:
            result['ImageType'] = self.image_type
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageType') is not None:
            self.image_type = m.get('ImageType')
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        return self


class RecognizeLicensePlateAdvanceRequest(TeaModel):
    def __init__(
        self,
        image_urlobject: BinaryIO = None,
        image_type: int = None,
    ):
        self.image_urlobject = image_urlobject
        self.image_type = image_type

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        result = dict()
        if self.image_urlobject is not None:
            result['ImageURLObject'] = self.image_urlobject
        if self.image_type is not None:
            result['ImageType'] = self.image_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURLObject') is not None:
            self.image_urlobject = m.get('ImageURLObject')
        if m.get('ImageType') is not None:
            self.image_type = m.get('ImageType')
        return self


class RecognizeLicensePlateResponseBodyDataPlatesRoi(TeaModel):
    def __init__(
        self,
        w: int = None,
        h: int = None,
        y: int = None,
        x: int = None,
    ):
        self.w = w
        self.h = h
        self.y = y
        self.x = x

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.w is not None:
            result['W'] = self.w
        if self.h is not None:
            result['H'] = self.h
        if self.y is not None:
            result['Y'] = self.y
        if self.x is not None:
            result['X'] = self.x
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('W') is not None:
            self.w = m.get('W')
        if m.get('H') is not None:
            self.h = m.get('H')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        if m.get('X') is not None:
            self.x = m.get('X')
        return self


class RecognizeLicensePlateResponseBodyDataPlates(TeaModel):
    def __init__(
        self,
        plate_type_confidence: float = None,
        plate_type: str = None,
        confidence: float = None,
        plate_number: str = None,
        roi: RecognizeLicensePlateResponseBodyDataPlatesRoi = None,
    ):
        self.plate_type_confidence = plate_type_confidence
        self.plate_type = plate_type
        self.confidence = confidence
        self.plate_number = plate_number
        self.roi = roi

    def validate(self):
        if self.roi:
            self.roi.validate()

    def to_map(self):
        result = dict()
        if self.plate_type_confidence is not None:
            result['PlateTypeConfidence'] = self.plate_type_confidence
        if self.plate_type is not None:
            result['PlateType'] = self.plate_type
        if self.confidence is not None:
            result['Confidence'] = self.confidence
        if self.plate_number is not None:
            result['PlateNumber'] = self.plate_number
        if self.roi is not None:
            result['Roi'] = self.roi.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PlateTypeConfidence') is not None:
            self.plate_type_confidence = m.get('PlateTypeConfidence')
        if m.get('PlateType') is not None:
            self.plate_type = m.get('PlateType')
        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')
        if m.get('PlateNumber') is not None:
            self.plate_number = m.get('PlateNumber')
        if m.get('Roi') is not None:
            temp_model = RecognizeLicensePlateResponseBodyDataPlatesRoi()
            self.roi = temp_model.from_map(m['Roi'])
        return self


class RecognizeLicensePlateResponseBodyData(TeaModel):
    def __init__(
        self,
        plates: List[RecognizeLicensePlateResponseBodyDataPlates] = None,
    ):
        self.plates = plates

    def validate(self):
        if self.plates:
            for k in self.plates:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Plates'] = []
        if self.plates is not None:
            for k in self.plates:
                result['Plates'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.plates = []
        if m.get('Plates') is not None:
            for k in m.get('Plates'):
                temp_model = RecognizeLicensePlateResponseBodyDataPlates()
                self.plates.append(temp_model.from_map(k))
        return self


class RecognizeLicensePlateResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: RecognizeLicensePlateResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = RecognizeLicensePlateResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class RecognizeLicensePlateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RecognizeLicensePlateResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = RecognizeLicensePlateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizePassportMRZRequest(TeaModel):
    def __init__(
        self,
        image_url: str = None,
    ):
        self.image_url = image_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        return self


class RecognizePassportMRZAdvanceRequest(TeaModel):
    def __init__(
        self,
        image_urlobject: BinaryIO = None,
    ):
        self.image_urlobject = image_urlobject

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        result = dict()
        if self.image_urlobject is not None:
            result['ImageURLObject'] = self.image_urlobject
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURLObject') is not None:
            self.image_urlobject = m.get('ImageURLObject')
        return self


class RecognizePassportMRZResponseBodyDataRegions(TeaModel):
    def __init__(
        self,
        recognition_score: float = None,
        detection_score: float = None,
        name: str = None,
        content: str = None,
        band_boxes: List[float] = None,
    ):
        self.recognition_score = recognition_score
        self.detection_score = detection_score
        self.name = name
        self.content = content
        self.band_boxes = band_boxes

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.recognition_score is not None:
            result['RecognitionScore'] = self.recognition_score
        if self.detection_score is not None:
            result['DetectionScore'] = self.detection_score
        if self.name is not None:
            result['Name'] = self.name
        if self.content is not None:
            result['Content'] = self.content
        if self.band_boxes is not None:
            result['BandBoxes'] = self.band_boxes
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RecognitionScore') is not None:
            self.recognition_score = m.get('RecognitionScore')
        if m.get('DetectionScore') is not None:
            self.detection_score = m.get('DetectionScore')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('BandBoxes') is not None:
            self.band_boxes = m.get('BandBoxes')
        return self


class RecognizePassportMRZResponseBodyData(TeaModel):
    def __init__(
        self,
        regions: List[RecognizePassportMRZResponseBodyDataRegions] = None,
    ):
        self.regions = regions

    def validate(self):
        if self.regions:
            for k in self.regions:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Regions'] = []
        if self.regions is not None:
            for k in self.regions:
                result['Regions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.regions = []
        if m.get('Regions') is not None:
            for k in m.get('Regions'):
                temp_model = RecognizePassportMRZResponseBodyDataRegions()
                self.regions.append(temp_model.from_map(k))
        return self


class RecognizePassportMRZResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: RecognizePassportMRZResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = RecognizePassportMRZResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class RecognizePassportMRZResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RecognizePassportMRZResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = RecognizePassportMRZResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizePoiNameRequest(TeaModel):
    def __init__(
        self,
        image_url: str = None,
    ):
        self.image_url = image_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        return self


class RecognizePoiNameAdvanceRequest(TeaModel):
    def __init__(
        self,
        image_urlobject: BinaryIO = None,
    ):
        self.image_urlobject = image_urlobject

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        result = dict()
        if self.image_urlobject is not None:
            result['ImageURLObject'] = self.image_urlobject
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURLObject') is not None:
            self.image_urlobject = m.get('ImageURLObject')
        return self


class RecognizePoiNameResponseBodyDataSummary(TeaModel):
    def __init__(
        self,
        brand: str = None,
        score: float = None,
    ):
        self.brand = brand
        self.score = score

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.brand is not None:
            result['Brand'] = self.brand
        if self.score is not None:
            result['Score'] = self.score
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Brand') is not None:
            self.brand = m.get('Brand')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        return self


class RecognizePoiNameResponseBodyDataSignboardsTexts(TeaModel):
    def __init__(
        self,
        type: str = None,
        score: float = None,
        tag: str = None,
        label: str = None,
        points: List[int] = None,
    ):
        self.type = type
        self.score = score
        self.tag = tag
        self.label = label
        self.points = points

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.score is not None:
            result['Score'] = self.score
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.label is not None:
            result['Label'] = self.label
        if self.points is not None:
            result['Points'] = self.points
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Points') is not None:
            self.points = m.get('Points')
        return self


class RecognizePoiNameResponseBodyDataSignboards(TeaModel):
    def __init__(
        self,
        texts: List[RecognizePoiNameResponseBodyDataSignboardsTexts] = None,
    ):
        self.texts = texts

    def validate(self):
        if self.texts:
            for k in self.texts:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Texts'] = []
        if self.texts is not None:
            for k in self.texts:
                result['Texts'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.texts = []
        if m.get('Texts') is not None:
            for k in m.get('Texts'):
                temp_model = RecognizePoiNameResponseBodyDataSignboardsTexts()
                self.texts.append(temp_model.from_map(k))
        return self


class RecognizePoiNameResponseBodyData(TeaModel):
    def __init__(
        self,
        summary: RecognizePoiNameResponseBodyDataSummary = None,
        signboards: List[RecognizePoiNameResponseBodyDataSignboards] = None,
    ):
        self.summary = summary
        self.signboards = signboards

    def validate(self):
        if self.summary:
            self.summary.validate()
        if self.signboards:
            for k in self.signboards:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.summary is not None:
            result['Summary'] = self.summary.to_map()
        result['Signboards'] = []
        if self.signboards is not None:
            for k in self.signboards:
                result['Signboards'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Summary') is not None:
            temp_model = RecognizePoiNameResponseBodyDataSummary()
            self.summary = temp_model.from_map(m['Summary'])
        self.signboards = []
        if m.get('Signboards') is not None:
            for k in m.get('Signboards'):
                temp_model = RecognizePoiNameResponseBodyDataSignboards()
                self.signboards.append(temp_model.from_map(k))
        return self


class RecognizePoiNameResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: RecognizePoiNameResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = RecognizePoiNameResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class RecognizePoiNameResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RecognizePoiNameResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = RecognizePoiNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeQrCodeRequestTasks(TeaModel):
    def __init__(
        self,
        image_url: str = None,
    ):
        self.image_url = image_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        return self


class RecognizeQrCodeRequest(TeaModel):
    def __init__(
        self,
        tasks: List[RecognizeQrCodeRequestTasks] = None,
    ):
        self.tasks = tasks

    def validate(self):
        if self.tasks:
            for k in self.tasks:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Tasks'] = []
        if self.tasks is not None:
            for k in self.tasks:
                result['Tasks'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tasks = []
        if m.get('Tasks') is not None:
            for k in m.get('Tasks'):
                temp_model = RecognizeQrCodeRequestTasks()
                self.tasks.append(temp_model.from_map(k))
        return self


class RecognizeQrCodeResponseBodyDataElementsResults(TeaModel):
    def __init__(
        self,
        suggestion: str = None,
        qr_codes_data: List[str] = None,
        label: str = None,
        rate: float = None,
    ):
        self.suggestion = suggestion
        self.qr_codes_data = qr_codes_data
        self.label = label
        self.rate = rate

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion
        if self.qr_codes_data is not None:
            result['QrCodesData'] = self.qr_codes_data
        if self.label is not None:
            result['Label'] = self.label
        if self.rate is not None:
            result['Rate'] = self.rate
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')
        if m.get('QrCodesData') is not None:
            self.qr_codes_data = m.get('QrCodesData')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Rate') is not None:
            self.rate = m.get('Rate')
        return self


class RecognizeQrCodeResponseBodyDataElements(TeaModel):
    def __init__(
        self,
        image_url: str = None,
        task_id: str = None,
        results: List[RecognizeQrCodeResponseBodyDataElementsResults] = None,
    ):
        self.image_url = image_url
        self.task_id = task_id
        self.results = results

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        self.results = []
        if m.get('Results') is not None:
            for k in m.get('Results'):
                temp_model = RecognizeQrCodeResponseBodyDataElementsResults()
                self.results.append(temp_model.from_map(k))
        return self


class RecognizeQrCodeResponseBodyData(TeaModel):
    def __init__(
        self,
        elements: List[RecognizeQrCodeResponseBodyDataElements] = None,
    ):
        self.elements = elements

    def validate(self):
        if self.elements:
            for k in self.elements:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Elements'] = []
        if self.elements is not None:
            for k in self.elements:
                result['Elements'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.elements = []
        if m.get('Elements') is not None:
            for k in m.get('Elements'):
                temp_model = RecognizeQrCodeResponseBodyDataElements()
                self.elements.append(temp_model.from_map(k))
        return self


class RecognizeQrCodeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: RecognizeQrCodeResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = RecognizeQrCodeResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class RecognizeQrCodeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RecognizeQrCodeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = RecognizeQrCodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeStampRequest(TeaModel):
    def __init__(
        self,
        image_type: int = None,
        image_url: str = None,
    ):
        self.image_type = image_type
        self.image_url = image_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.image_type is not None:
            result['ImageType'] = self.image_type
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageType') is not None:
            self.image_type = m.get('ImageType')
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        return self


class RecognizeStampAdvanceRequest(TeaModel):
    def __init__(
        self,
        image_urlobject: BinaryIO = None,
        image_type: int = None,
    ):
        self.image_urlobject = image_urlobject
        self.image_type = image_type

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        result = dict()
        if self.image_urlobject is not None:
            result['ImageURLObject'] = self.image_urlobject
        if self.image_type is not None:
            result['ImageType'] = self.image_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURLObject') is not None:
            self.image_urlobject = m.get('ImageURLObject')
        if m.get('ImageType') is not None:
            self.image_type = m.get('ImageType')
        return self


class RecognizeStampResponseBodyDataResultsText(TeaModel):
    def __init__(
        self,
        confidence: float = None,
        content: str = None,
    ):
        self.confidence = confidence
        self.content = content

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.confidence is not None:
            result['Confidence'] = self.confidence
        if self.content is not None:
            result['Content'] = self.content
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        return self


class RecognizeStampResponseBodyDataResultsRoi(TeaModel):
    def __init__(
        self,
        top: int = None,
        width: int = None,
        height: int = None,
        left: int = None,
    ):
        self.top = top
        self.width = width
        self.height = height
        self.left = left

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.top is not None:
            result['Top'] = self.top
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        if self.left is not None:
            result['Left'] = self.left
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Top') is not None:
            self.top = m.get('Top')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Left') is not None:
            self.left = m.get('Left')
        return self


class RecognizeStampResponseBodyDataResultsGeneralText(TeaModel):
    def __init__(
        self,
        confidence: float = None,
        content: str = None,
    ):
        self.confidence = confidence
        self.content = content

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.confidence is not None:
            result['Confidence'] = self.confidence
        if self.content is not None:
            result['Content'] = self.content
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        return self


class RecognizeStampResponseBodyDataResults(TeaModel):
    def __init__(
        self,
        text: RecognizeStampResponseBodyDataResultsText = None,
        roi: RecognizeStampResponseBodyDataResultsRoi = None,
        general_text: List[RecognizeStampResponseBodyDataResultsGeneralText] = None,
    ):
        self.text = text
        self.roi = roi
        self.general_text = general_text

    def validate(self):
        if self.text:
            self.text.validate()
        if self.roi:
            self.roi.validate()
        if self.general_text:
            for k in self.general_text:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.text is not None:
            result['Text'] = self.text.to_map()
        if self.roi is not None:
            result['Roi'] = self.roi.to_map()
        result['GeneralText'] = []
        if self.general_text is not None:
            for k in self.general_text:
                result['GeneralText'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Text') is not None:
            temp_model = RecognizeStampResponseBodyDataResultsText()
            self.text = temp_model.from_map(m['Text'])
        if m.get('Roi') is not None:
            temp_model = RecognizeStampResponseBodyDataResultsRoi()
            self.roi = temp_model.from_map(m['Roi'])
        self.general_text = []
        if m.get('GeneralText') is not None:
            for k in m.get('GeneralText'):
                temp_model = RecognizeStampResponseBodyDataResultsGeneralText()
                self.general_text.append(temp_model.from_map(k))
        return self


class RecognizeStampResponseBodyData(TeaModel):
    def __init__(
        self,
        results: List[RecognizeStampResponseBodyDataResults] = None,
    ):
        self.results = results

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.results = []
        if m.get('Results') is not None:
            for k in m.get('Results'):
                temp_model = RecognizeStampResponseBodyDataResults()
                self.results.append(temp_model.from_map(k))
        return self


class RecognizeStampResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: RecognizeStampResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = RecognizeStampResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class RecognizeStampResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RecognizeStampResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = RecognizeStampResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeTableRequest(TeaModel):
    def __init__(
        self,
        image_type: int = None,
        image_url: str = None,
        output_format: str = None,
        use_finance_model: bool = None,
        assure_direction: bool = None,
        has_line: bool = None,
        skip_detection: bool = None,
    ):
        self.image_type = image_type
        self.image_url = image_url
        self.output_format = output_format
        self.use_finance_model = use_finance_model
        self.assure_direction = assure_direction
        self.has_line = has_line
        self.skip_detection = skip_detection

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.image_type is not None:
            result['ImageType'] = self.image_type
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        if self.output_format is not None:
            result['OutputFormat'] = self.output_format
        if self.use_finance_model is not None:
            result['UseFinanceModel'] = self.use_finance_model
        if self.assure_direction is not None:
            result['AssureDirection'] = self.assure_direction
        if self.has_line is not None:
            result['HasLine'] = self.has_line
        if self.skip_detection is not None:
            result['SkipDetection'] = self.skip_detection
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageType') is not None:
            self.image_type = m.get('ImageType')
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        if m.get('OutputFormat') is not None:
            self.output_format = m.get('OutputFormat')
        if m.get('UseFinanceModel') is not None:
            self.use_finance_model = m.get('UseFinanceModel')
        if m.get('AssureDirection') is not None:
            self.assure_direction = m.get('AssureDirection')
        if m.get('HasLine') is not None:
            self.has_line = m.get('HasLine')
        if m.get('SkipDetection') is not None:
            self.skip_detection = m.get('SkipDetection')
        return self


class RecognizeTableAdvanceRequest(TeaModel):
    def __init__(
        self,
        image_urlobject: BinaryIO = None,
        image_type: int = None,
        output_format: str = None,
        use_finance_model: bool = None,
        assure_direction: bool = None,
        has_line: bool = None,
        skip_detection: bool = None,
    ):
        self.image_urlobject = image_urlobject
        self.image_type = image_type
        self.output_format = output_format
        self.use_finance_model = use_finance_model
        self.assure_direction = assure_direction
        self.has_line = has_line
        self.skip_detection = skip_detection

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        result = dict()
        if self.image_urlobject is not None:
            result['ImageURLObject'] = self.image_urlobject
        if self.image_type is not None:
            result['ImageType'] = self.image_type
        if self.output_format is not None:
            result['OutputFormat'] = self.output_format
        if self.use_finance_model is not None:
            result['UseFinanceModel'] = self.use_finance_model
        if self.assure_direction is not None:
            result['AssureDirection'] = self.assure_direction
        if self.has_line is not None:
            result['HasLine'] = self.has_line
        if self.skip_detection is not None:
            result['SkipDetection'] = self.skip_detection
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURLObject') is not None:
            self.image_urlobject = m.get('ImageURLObject')
        if m.get('ImageType') is not None:
            self.image_type = m.get('ImageType')
        if m.get('OutputFormat') is not None:
            self.output_format = m.get('OutputFormat')
        if m.get('UseFinanceModel') is not None:
            self.use_finance_model = m.get('UseFinanceModel')
        if m.get('AssureDirection') is not None:
            self.assure_direction = m.get('AssureDirection')
        if m.get('HasLine') is not None:
            self.has_line = m.get('HasLine')
        if m.get('SkipDetection') is not None:
            self.skip_detection = m.get('SkipDetection')
        return self


class RecognizeTableResponseBodyDataTablesTableRowsTableColumns(TeaModel):
    def __init__(
        self,
        end_row: int = None,
        end_column: int = None,
        width: int = None,
        height: int = None,
        texts: List[str] = None,
        start_row: int = None,
        start_column: int = None,
    ):
        self.end_row = end_row
        self.end_column = end_column
        self.width = width
        self.height = height
        self.texts = texts
        self.start_row = start_row
        self.start_column = start_column

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.end_row is not None:
            result['EndRow'] = self.end_row
        if self.end_column is not None:
            result['EndColumn'] = self.end_column
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        if self.texts is not None:
            result['Texts'] = self.texts
        if self.start_row is not None:
            result['StartRow'] = self.start_row
        if self.start_column is not None:
            result['StartColumn'] = self.start_column
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndRow') is not None:
            self.end_row = m.get('EndRow')
        if m.get('EndColumn') is not None:
            self.end_column = m.get('EndColumn')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Texts') is not None:
            self.texts = m.get('Texts')
        if m.get('StartRow') is not None:
            self.start_row = m.get('StartRow')
        if m.get('StartColumn') is not None:
            self.start_column = m.get('StartColumn')
        return self


class RecognizeTableResponseBodyDataTablesTableRows(TeaModel):
    def __init__(
        self,
        table_columns: List[RecognizeTableResponseBodyDataTablesTableRowsTableColumns] = None,
    ):
        self.table_columns = table_columns

    def validate(self):
        if self.table_columns:
            for k in self.table_columns:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['TableColumns'] = []
        if self.table_columns is not None:
            for k in self.table_columns:
                result['TableColumns'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.table_columns = []
        if m.get('TableColumns') is not None:
            for k in m.get('TableColumns'):
                temp_model = RecognizeTableResponseBodyDataTablesTableRowsTableColumns()
                self.table_columns.append(temp_model.from_map(k))
        return self


class RecognizeTableResponseBodyDataTables(TeaModel):
    def __init__(
        self,
        head: List[str] = None,
        tail: List[str] = None,
        table_rows: List[RecognizeTableResponseBodyDataTablesTableRows] = None,
    ):
        self.head = head
        self.tail = tail
        self.table_rows = table_rows

    def validate(self):
        if self.table_rows:
            for k in self.table_rows:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.head is not None:
            result['Head'] = self.head
        if self.tail is not None:
            result['Tail'] = self.tail
        result['TableRows'] = []
        if self.table_rows is not None:
            for k in self.table_rows:
                result['TableRows'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Head') is not None:
            self.head = m.get('Head')
        if m.get('Tail') is not None:
            self.tail = m.get('Tail')
        self.table_rows = []
        if m.get('TableRows') is not None:
            for k in m.get('TableRows'):
                temp_model = RecognizeTableResponseBodyDataTablesTableRows()
                self.table_rows.append(temp_model.from_map(k))
        return self


class RecognizeTableResponseBodyData(TeaModel):
    def __init__(
        self,
        file_content: str = None,
        tables: List[RecognizeTableResponseBodyDataTables] = None,
    ):
        self.file_content = file_content
        self.tables = tables

    def validate(self):
        if self.tables:
            for k in self.tables:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.file_content is not None:
            result['FileContent'] = self.file_content
        result['Tables'] = []
        if self.tables is not None:
            for k in self.tables:
                result['Tables'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileContent') is not None:
            self.file_content = m.get('FileContent')
        self.tables = []
        if m.get('Tables') is not None:
            for k in m.get('Tables'):
                temp_model = RecognizeTableResponseBodyDataTables()
                self.tables.append(temp_model.from_map(k))
        return self


class RecognizeTableResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: RecognizeTableResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = RecognizeTableResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class RecognizeTableResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RecognizeTableResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = RecognizeTableResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeTakeoutOrderRequest(TeaModel):
    def __init__(
        self,
        image_url: str = None,
    ):
        self.image_url = image_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        return self


class RecognizeTakeoutOrderAdvanceRequest(TeaModel):
    def __init__(
        self,
        image_urlobject: BinaryIO = None,
    ):
        self.image_urlobject = image_urlobject

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        result = dict()
        if self.image_urlobject is not None:
            result['ImageURLObject'] = self.image_urlobject
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURLObject') is not None:
            self.image_urlobject = m.get('ImageURLObject')
        return self


class RecognizeTakeoutOrderResponseBodyDataElements(TeaModel):
    def __init__(
        self,
        value: str = None,
        boxes: List[int] = None,
        score: float = None,
        name: str = None,
    ):
        self.value = value
        self.boxes = boxes
        self.score = score
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        if self.boxes is not None:
            result['Boxes'] = self.boxes
        if self.score is not None:
            result['Score'] = self.score
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('Boxes') is not None:
            self.boxes = m.get('Boxes')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class RecognizeTakeoutOrderResponseBodyData(TeaModel):
    def __init__(
        self,
        elements: List[RecognizeTakeoutOrderResponseBodyDataElements] = None,
    ):
        self.elements = elements

    def validate(self):
        if self.elements:
            for k in self.elements:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Elements'] = []
        if self.elements is not None:
            for k in self.elements:
                result['Elements'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.elements = []
        if m.get('Elements') is not None:
            for k in m.get('Elements'):
                temp_model = RecognizeTakeoutOrderResponseBodyDataElements()
                self.elements.append(temp_model.from_map(k))
        return self


class RecognizeTakeoutOrderResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: RecognizeTakeoutOrderResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = RecognizeTakeoutOrderResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class RecognizeTakeoutOrderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RecognizeTakeoutOrderResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = RecognizeTakeoutOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeTaxiInvoiceRequest(TeaModel):
    def __init__(
        self,
        image_type: int = None,
        image_url: str = None,
    ):
        self.image_type = image_type
        self.image_url = image_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.image_type is not None:
            result['ImageType'] = self.image_type
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageType') is not None:
            self.image_type = m.get('ImageType')
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        return self


class RecognizeTaxiInvoiceAdvanceRequest(TeaModel):
    def __init__(
        self,
        image_urlobject: BinaryIO = None,
        image_type: int = None,
    ):
        self.image_urlobject = image_urlobject
        self.image_type = image_type

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        result = dict()
        if self.image_urlobject is not None:
            result['ImageURLObject'] = self.image_urlobject
        if self.image_type is not None:
            result['ImageType'] = self.image_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURLObject') is not None:
            self.image_urlobject = m.get('ImageURLObject')
        if m.get('ImageType') is not None:
            self.image_type = m.get('ImageType')
        return self


class RecognizeTaxiInvoiceResponseBodyDataInvoicesItemsItemRoiSize(TeaModel):
    def __init__(
        self,
        w: float = None,
        h: float = None,
    ):
        self.w = w
        self.h = h

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.w is not None:
            result['W'] = self.w
        if self.h is not None:
            result['H'] = self.h
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('W') is not None:
            self.w = m.get('W')
        if m.get('H') is not None:
            self.h = m.get('H')
        return self


class RecognizeTaxiInvoiceResponseBodyDataInvoicesItemsItemRoiCenter(TeaModel):
    def __init__(
        self,
        y: float = None,
        x: float = None,
    ):
        self.y = y
        self.x = x

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.y is not None:
            result['Y'] = self.y
        if self.x is not None:
            result['X'] = self.x
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Y') is not None:
            self.y = m.get('Y')
        if m.get('X') is not None:
            self.x = m.get('X')
        return self


class RecognizeTaxiInvoiceResponseBodyDataInvoicesItemsItemRoi(TeaModel):
    def __init__(
        self,
        size: RecognizeTaxiInvoiceResponseBodyDataInvoicesItemsItemRoiSize = None,
        angle: float = None,
        center: RecognizeTaxiInvoiceResponseBodyDataInvoicesItemsItemRoiCenter = None,
    ):
        self.size = size
        self.angle = angle
        self.center = center

    def validate(self):
        if self.size:
            self.size.validate()
        if self.center:
            self.center.validate()

    def to_map(self):
        result = dict()
        if self.size is not None:
            result['Size'] = self.size.to_map()
        if self.angle is not None:
            result['Angle'] = self.angle
        if self.center is not None:
            result['Center'] = self.center.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Size') is not None:
            temp_model = RecognizeTaxiInvoiceResponseBodyDataInvoicesItemsItemRoiSize()
            self.size = temp_model.from_map(m['Size'])
        if m.get('Angle') is not None:
            self.angle = m.get('Angle')
        if m.get('Center') is not None:
            temp_model = RecognizeTaxiInvoiceResponseBodyDataInvoicesItemsItemRoiCenter()
            self.center = temp_model.from_map(m['Center'])
        return self


class RecognizeTaxiInvoiceResponseBodyDataInvoicesItems(TeaModel):
    def __init__(
        self,
        item_roi: RecognizeTaxiInvoiceResponseBodyDataInvoicesItemsItemRoi = None,
        text: str = None,
    ):
        self.item_roi = item_roi
        self.text = text

    def validate(self):
        if self.item_roi:
            self.item_roi.validate()

    def to_map(self):
        result = dict()
        if self.item_roi is not None:
            result['ItemRoi'] = self.item_roi.to_map()
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ItemRoi') is not None:
            temp_model = RecognizeTaxiInvoiceResponseBodyDataInvoicesItemsItemRoi()
            self.item_roi = temp_model.from_map(m['ItemRoi'])
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class RecognizeTaxiInvoiceResponseBodyDataInvoicesInvoiceRoi(TeaModel):
    def __init__(
        self,
        w: float = None,
        h: float = None,
        y: float = None,
        x: float = None,
    ):
        self.w = w
        self.h = h
        self.y = y
        self.x = x

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.w is not None:
            result['W'] = self.w
        if self.h is not None:
            result['H'] = self.h
        if self.y is not None:
            result['Y'] = self.y
        if self.x is not None:
            result['X'] = self.x
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('W') is not None:
            self.w = m.get('W')
        if m.get('H') is not None:
            self.h = m.get('H')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        if m.get('X') is not None:
            self.x = m.get('X')
        return self


class RecognizeTaxiInvoiceResponseBodyDataInvoices(TeaModel):
    def __init__(
        self,
        items: List[RecognizeTaxiInvoiceResponseBodyDataInvoicesItems] = None,
        rotate_type: int = None,
        invoice_roi: RecognizeTaxiInvoiceResponseBodyDataInvoicesInvoiceRoi = None,
    ):
        self.items = items
        self.rotate_type = rotate_type
        self.invoice_roi = invoice_roi

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()
        if self.invoice_roi:
            self.invoice_roi.validate()

    def to_map(self):
        result = dict()
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.rotate_type is not None:
            result['RotateType'] = self.rotate_type
        if self.invoice_roi is not None:
            result['InvoiceRoi'] = self.invoice_roi.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = RecognizeTaxiInvoiceResponseBodyDataInvoicesItems()
                self.items.append(temp_model.from_map(k))
        if m.get('RotateType') is not None:
            self.rotate_type = m.get('RotateType')
        if m.get('InvoiceRoi') is not None:
            temp_model = RecognizeTaxiInvoiceResponseBodyDataInvoicesInvoiceRoi()
            self.invoice_roi = temp_model.from_map(m['InvoiceRoi'])
        return self


class RecognizeTaxiInvoiceResponseBodyData(TeaModel):
    def __init__(
        self,
        invoices: List[RecognizeTaxiInvoiceResponseBodyDataInvoices] = None,
    ):
        self.invoices = invoices

    def validate(self):
        if self.invoices:
            for k in self.invoices:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Invoices'] = []
        if self.invoices is not None:
            for k in self.invoices:
                result['Invoices'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.invoices = []
        if m.get('Invoices') is not None:
            for k in m.get('Invoices'):
                temp_model = RecognizeTaxiInvoiceResponseBodyDataInvoices()
                self.invoices.append(temp_model.from_map(k))
        return self


class RecognizeTaxiInvoiceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: RecognizeTaxiInvoiceResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = RecognizeTaxiInvoiceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class RecognizeTaxiInvoiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RecognizeTaxiInvoiceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = RecognizeTaxiInvoiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeTrainTicketRequest(TeaModel):
    def __init__(
        self,
        image_type: int = None,
        image_url: str = None,
    ):
        self.image_type = image_type
        self.image_url = image_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.image_type is not None:
            result['ImageType'] = self.image_type
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageType') is not None:
            self.image_type = m.get('ImageType')
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        return self


class RecognizeTrainTicketAdvanceRequest(TeaModel):
    def __init__(
        self,
        image_urlobject: BinaryIO = None,
        image_type: int = None,
    ):
        self.image_urlobject = image_urlobject
        self.image_type = image_type

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        result = dict()
        if self.image_urlobject is not None:
            result['ImageURLObject'] = self.image_urlobject
        if self.image_type is not None:
            result['ImageType'] = self.image_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURLObject') is not None:
            self.image_urlobject = m.get('ImageURLObject')
        if m.get('ImageType') is not None:
            self.image_type = m.get('ImageType')
        return self


class RecognizeTrainTicketResponseBodyData(TeaModel):
    def __init__(
        self,
        price: float = None,
        destination: str = None,
        departure_station: str = None,
        date: str = None,
        number: str = None,
        seat: str = None,
        name: str = None,
        level: str = None,
    ):
        self.price = price
        self.destination = destination
        self.departure_station = departure_station
        self.date = date
        self.number = number
        self.seat = seat
        self.name = name
        self.level = level

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.price is not None:
            result['Price'] = self.price
        if self.destination is not None:
            result['Destination'] = self.destination
        if self.departure_station is not None:
            result['DepartureStation'] = self.departure_station
        if self.date is not None:
            result['Date'] = self.date
        if self.number is not None:
            result['Number'] = self.number
        if self.seat is not None:
            result['Seat'] = self.seat
        if self.name is not None:
            result['Name'] = self.name
        if self.level is not None:
            result['Level'] = self.level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Price') is not None:
            self.price = m.get('Price')
        if m.get('Destination') is not None:
            self.destination = m.get('Destination')
        if m.get('DepartureStation') is not None:
            self.departure_station = m.get('DepartureStation')
        if m.get('Date') is not None:
            self.date = m.get('Date')
        if m.get('Number') is not None:
            self.number = m.get('Number')
        if m.get('Seat') is not None:
            self.seat = m.get('Seat')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        return self


class RecognizeTrainTicketResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: RecognizeTrainTicketResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = RecognizeTrainTicketResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class RecognizeTrainTicketResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RecognizeTrainTicketResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = RecognizeTrainTicketResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeVATInvoiceRequest(TeaModel):
    def __init__(
        self,
        file_url: str = None,
        file_type: str = None,
    ):
        self.file_url = file_url
        self.file_type = file_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.file_url is not None:
            result['FileURL'] = self.file_url
        if self.file_type is not None:
            result['FileType'] = self.file_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileURL') is not None:
            self.file_url = m.get('FileURL')
        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')
        return self


class RecognizeVATInvoiceAdvanceRequest(TeaModel):
    def __init__(
        self,
        file_urlobject: BinaryIO = None,
        file_type: str = None,
    ):
        self.file_urlobject = file_urlobject
        self.file_type = file_type

    def validate(self):
        self.validate_required(self.file_urlobject, 'file_urlobject')

    def to_map(self):
        result = dict()
        if self.file_urlobject is not None:
            result['FileURLObject'] = self.file_urlobject
        if self.file_type is not None:
            result['FileType'] = self.file_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileURLObject') is not None:
            self.file_urlobject = m.get('FileURLObject')
        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')
        return self


class RecognizeVATInvoiceResponseBodyDataBox(TeaModel):
    def __init__(
        self,
        payer_register_noes: List[float] = None,
        payee_addresses: List[float] = None,
        payee_bank_names: List[float] = None,
        checkers: List[float] = None,
        tax_amounts: List[float] = None,
        sum_amounts: List[float] = None,
        clerks: List[float] = None,
        invoice_noes: List[float] = None,
        invoice_dates: List[float] = None,
        invoice_codes: List[float] = None,
        invoice_fake_codes: List[float] = None,
        payer_names: List[float] = None,
        payer_bank_names: List[float] = None,
        payees: List[float] = None,
        payee_names: List[float] = None,
        invoice_amounts: List[float] = None,
        without_tax_amounts: List[float] = None,
        payer_addresses: List[float] = None,
        payee_register_noes: List[float] = None,
    ):
        self.payer_register_noes = payer_register_noes
        self.payee_addresses = payee_addresses
        self.payee_bank_names = payee_bank_names
        self.checkers = checkers
        self.tax_amounts = tax_amounts
        self.sum_amounts = sum_amounts
        self.clerks = clerks
        self.invoice_noes = invoice_noes
        self.invoice_dates = invoice_dates
        self.invoice_codes = invoice_codes
        self.invoice_fake_codes = invoice_fake_codes
        self.payer_names = payer_names
        self.payer_bank_names = payer_bank_names
        self.payees = payees
        self.payee_names = payee_names
        self.invoice_amounts = invoice_amounts
        self.without_tax_amounts = without_tax_amounts
        self.payer_addresses = payer_addresses
        self.payee_register_noes = payee_register_noes

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.payer_register_noes is not None:
            result['PayerRegisterNoes'] = self.payer_register_noes
        if self.payee_addresses is not None:
            result['PayeeAddresses'] = self.payee_addresses
        if self.payee_bank_names is not None:
            result['PayeeBankNames'] = self.payee_bank_names
        if self.checkers is not None:
            result['Checkers'] = self.checkers
        if self.tax_amounts is not None:
            result['TaxAmounts'] = self.tax_amounts
        if self.sum_amounts is not None:
            result['SumAmounts'] = self.sum_amounts
        if self.clerks is not None:
            result['Clerks'] = self.clerks
        if self.invoice_noes is not None:
            result['InvoiceNoes'] = self.invoice_noes
        if self.invoice_dates is not None:
            result['InvoiceDates'] = self.invoice_dates
        if self.invoice_codes is not None:
            result['InvoiceCodes'] = self.invoice_codes
        if self.invoice_fake_codes is not None:
            result['InvoiceFakeCodes'] = self.invoice_fake_codes
        if self.payer_names is not None:
            result['PayerNames'] = self.payer_names
        if self.payer_bank_names is not None:
            result['PayerBankNames'] = self.payer_bank_names
        if self.payees is not None:
            result['Payees'] = self.payees
        if self.payee_names is not None:
            result['PayeeNames'] = self.payee_names
        if self.invoice_amounts is not None:
            result['InvoiceAmounts'] = self.invoice_amounts
        if self.without_tax_amounts is not None:
            result['WithoutTaxAmounts'] = self.without_tax_amounts
        if self.payer_addresses is not None:
            result['PayerAddresses'] = self.payer_addresses
        if self.payee_register_noes is not None:
            result['PayeeRegisterNoes'] = self.payee_register_noes
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PayerRegisterNoes') is not None:
            self.payer_register_noes = m.get('PayerRegisterNoes')
        if m.get('PayeeAddresses') is not None:
            self.payee_addresses = m.get('PayeeAddresses')
        if m.get('PayeeBankNames') is not None:
            self.payee_bank_names = m.get('PayeeBankNames')
        if m.get('Checkers') is not None:
            self.checkers = m.get('Checkers')
        if m.get('TaxAmounts') is not None:
            self.tax_amounts = m.get('TaxAmounts')
        if m.get('SumAmounts') is not None:
            self.sum_amounts = m.get('SumAmounts')
        if m.get('Clerks') is not None:
            self.clerks = m.get('Clerks')
        if m.get('InvoiceNoes') is not None:
            self.invoice_noes = m.get('InvoiceNoes')
        if m.get('InvoiceDates') is not None:
            self.invoice_dates = m.get('InvoiceDates')
        if m.get('InvoiceCodes') is not None:
            self.invoice_codes = m.get('InvoiceCodes')
        if m.get('InvoiceFakeCodes') is not None:
            self.invoice_fake_codes = m.get('InvoiceFakeCodes')
        if m.get('PayerNames') is not None:
            self.payer_names = m.get('PayerNames')
        if m.get('PayerBankNames') is not None:
            self.payer_bank_names = m.get('PayerBankNames')
        if m.get('Payees') is not None:
            self.payees = m.get('Payees')
        if m.get('PayeeNames') is not None:
            self.payee_names = m.get('PayeeNames')
        if m.get('InvoiceAmounts') is not None:
            self.invoice_amounts = m.get('InvoiceAmounts')
        if m.get('WithoutTaxAmounts') is not None:
            self.without_tax_amounts = m.get('WithoutTaxAmounts')
        if m.get('PayerAddresses') is not None:
            self.payer_addresses = m.get('PayerAddresses')
        if m.get('PayeeRegisterNoes') is not None:
            self.payee_register_noes = m.get('PayeeRegisterNoes')
        return self


class RecognizeVATInvoiceResponseBodyDataContent(TeaModel):
    def __init__(
        self,
        payer_address: str = None,
        payee_register_no: str = None,
        payee_bank_name: str = None,
        invoice_no: str = None,
        payer_register_no: str = None,
        checker: str = None,
        tax_amount: str = None,
        invoice_date: str = None,
        without_tax_amount: str = None,
        invoice_amount: str = None,
        anti_fake_code: str = None,
        payer_name: str = None,
        payee: str = None,
        sum_amount: str = None,
        payer_bank_name: str = None,
        clerk: str = None,
        payee_name: str = None,
        payee_address: str = None,
        invoice_code: str = None,
    ):
        self.payer_address = payer_address
        self.payee_register_no = payee_register_no
        self.payee_bank_name = payee_bank_name
        self.invoice_no = invoice_no
        self.payer_register_no = payer_register_no
        self.checker = checker
        self.tax_amount = tax_amount
        self.invoice_date = invoice_date
        self.without_tax_amount = without_tax_amount
        self.invoice_amount = invoice_amount
        self.anti_fake_code = anti_fake_code
        self.payer_name = payer_name
        self.payee = payee
        self.sum_amount = sum_amount
        self.payer_bank_name = payer_bank_name
        self.clerk = clerk
        self.payee_name = payee_name
        self.payee_address = payee_address
        self.invoice_code = invoice_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.payer_address is not None:
            result['PayerAddress'] = self.payer_address
        if self.payee_register_no is not None:
            result['PayeeRegisterNo'] = self.payee_register_no
        if self.payee_bank_name is not None:
            result['PayeeBankName'] = self.payee_bank_name
        if self.invoice_no is not None:
            result['InvoiceNo'] = self.invoice_no
        if self.payer_register_no is not None:
            result['PayerRegisterNo'] = self.payer_register_no
        if self.checker is not None:
            result['Checker'] = self.checker
        if self.tax_amount is not None:
            result['TaxAmount'] = self.tax_amount
        if self.invoice_date is not None:
            result['InvoiceDate'] = self.invoice_date
        if self.without_tax_amount is not None:
            result['WithoutTaxAmount'] = self.without_tax_amount
        if self.invoice_amount is not None:
            result['InvoiceAmount'] = self.invoice_amount
        if self.anti_fake_code is not None:
            result['AntiFakeCode'] = self.anti_fake_code
        if self.payer_name is not None:
            result['PayerName'] = self.payer_name
        if self.payee is not None:
            result['Payee'] = self.payee
        if self.sum_amount is not None:
            result['SumAmount'] = self.sum_amount
        if self.payer_bank_name is not None:
            result['PayerBankName'] = self.payer_bank_name
        if self.clerk is not None:
            result['Clerk'] = self.clerk
        if self.payee_name is not None:
            result['PayeeName'] = self.payee_name
        if self.payee_address is not None:
            result['PayeeAddress'] = self.payee_address
        if self.invoice_code is not None:
            result['InvoiceCode'] = self.invoice_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PayerAddress') is not None:
            self.payer_address = m.get('PayerAddress')
        if m.get('PayeeRegisterNo') is not None:
            self.payee_register_no = m.get('PayeeRegisterNo')
        if m.get('PayeeBankName') is not None:
            self.payee_bank_name = m.get('PayeeBankName')
        if m.get('InvoiceNo') is not None:
            self.invoice_no = m.get('InvoiceNo')
        if m.get('PayerRegisterNo') is not None:
            self.payer_register_no = m.get('PayerRegisterNo')
        if m.get('Checker') is not None:
            self.checker = m.get('Checker')
        if m.get('TaxAmount') is not None:
            self.tax_amount = m.get('TaxAmount')
        if m.get('InvoiceDate') is not None:
            self.invoice_date = m.get('InvoiceDate')
        if m.get('WithoutTaxAmount') is not None:
            self.without_tax_amount = m.get('WithoutTaxAmount')
        if m.get('InvoiceAmount') is not None:
            self.invoice_amount = m.get('InvoiceAmount')
        if m.get('AntiFakeCode') is not None:
            self.anti_fake_code = m.get('AntiFakeCode')
        if m.get('PayerName') is not None:
            self.payer_name = m.get('PayerName')
        if m.get('Payee') is not None:
            self.payee = m.get('Payee')
        if m.get('SumAmount') is not None:
            self.sum_amount = m.get('SumAmount')
        if m.get('PayerBankName') is not None:
            self.payer_bank_name = m.get('PayerBankName')
        if m.get('Clerk') is not None:
            self.clerk = m.get('Clerk')
        if m.get('PayeeName') is not None:
            self.payee_name = m.get('PayeeName')
        if m.get('PayeeAddress') is not None:
            self.payee_address = m.get('PayeeAddress')
        if m.get('InvoiceCode') is not None:
            self.invoice_code = m.get('InvoiceCode')
        return self


class RecognizeVATInvoiceResponseBodyData(TeaModel):
    def __init__(
        self,
        box: RecognizeVATInvoiceResponseBodyDataBox = None,
        content: RecognizeVATInvoiceResponseBodyDataContent = None,
    ):
        self.box = box
        self.content = content

    def validate(self):
        if self.box:
            self.box.validate()
        if self.content:
            self.content.validate()

    def to_map(self):
        result = dict()
        if self.box is not None:
            result['Box'] = self.box.to_map()
        if self.content is not None:
            result['Content'] = self.content.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Box') is not None:
            temp_model = RecognizeVATInvoiceResponseBodyDataBox()
            self.box = temp_model.from_map(m['Box'])
        if m.get('Content') is not None:
            temp_model = RecognizeVATInvoiceResponseBodyDataContent()
            self.content = temp_model.from_map(m['Content'])
        return self


class RecognizeVATInvoiceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: RecognizeVATInvoiceResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = RecognizeVATInvoiceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class RecognizeVATInvoiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RecognizeVATInvoiceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = RecognizeVATInvoiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeVerificationcodeRequest(TeaModel):
    def __init__(
        self,
        image_url: str = None,
    ):
        self.image_url = image_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        return self


class RecognizeVerificationcodeAdvanceRequest(TeaModel):
    def __init__(
        self,
        image_urlobject: BinaryIO = None,
    ):
        self.image_urlobject = image_urlobject

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        result = dict()
        if self.image_urlobject is not None:
            result['ImageURLObject'] = self.image_urlobject
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURLObject') is not None:
            self.image_urlobject = m.get('ImageURLObject')
        return self


class RecognizeVerificationcodeResponseBodyData(TeaModel):
    def __init__(
        self,
        content: str = None,
    ):
        self.content = content

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        return self


class RecognizeVerificationcodeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: RecognizeVerificationcodeResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = RecognizeVerificationcodeResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class RecognizeVerificationcodeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RecognizeVerificationcodeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = RecognizeVerificationcodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeVINCodeRequest(TeaModel):
    def __init__(
        self,
        image_type: int = None,
        image_url: str = None,
    ):
        self.image_type = image_type
        self.image_url = image_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.image_type is not None:
            result['ImageType'] = self.image_type
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageType') is not None:
            self.image_type = m.get('ImageType')
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        return self


class RecognizeVINCodeAdvanceRequest(TeaModel):
    def __init__(
        self,
        image_urlobject: BinaryIO = None,
        image_type: int = None,
    ):
        self.image_urlobject = image_urlobject
        self.image_type = image_type

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        result = dict()
        if self.image_urlobject is not None:
            result['ImageURLObject'] = self.image_urlobject
        if self.image_type is not None:
            result['ImageType'] = self.image_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURLObject') is not None:
            self.image_urlobject = m.get('ImageURLObject')
        if m.get('ImageType') is not None:
            self.image_type = m.get('ImageType')
        return self


class RecognizeVINCodeResponseBodyData(TeaModel):
    def __init__(
        self,
        vin_code: str = None,
    ):
        self.vin_code = vin_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.vin_code is not None:
            result['VinCode'] = self.vin_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VinCode') is not None:
            self.vin_code = m.get('VinCode')
        return self


class RecognizeVINCodeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: RecognizeVINCodeResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = RecognizeVINCodeResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class RecognizeVINCodeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RecognizeVINCodeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = RecognizeVINCodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TrimDocumentRequest(TeaModel):
    def __init__(
        self,
        file_url: str = None,
        file_type: str = None,
        output_type: str = None,
        async_: bool = None,
    ):
        self.file_url = file_url
        self.file_type = file_type
        self.output_type = output_type
        self.async_ = async_

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.file_url is not None:
            result['FileURL'] = self.file_url
        if self.file_type is not None:
            result['FileType'] = self.file_type
        if self.output_type is not None:
            result['OutputType'] = self.output_type
        if self.async_ is not None:
            result['Async'] = self.async_
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileURL') is not None:
            self.file_url = m.get('FileURL')
        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')
        if m.get('OutputType') is not None:
            self.output_type = m.get('OutputType')
        if m.get('Async') is not None:
            self.async_ = m.get('Async')
        return self


class TrimDocumentAdvanceRequest(TeaModel):
    def __init__(
        self,
        file_urlobject: BinaryIO = None,
        file_type: str = None,
        output_type: str = None,
        async_: bool = None,
    ):
        self.file_urlobject = file_urlobject
        self.file_type = file_type
        self.output_type = output_type
        self.async_ = async_

    def validate(self):
        self.validate_required(self.file_urlobject, 'file_urlobject')

    def to_map(self):
        result = dict()
        if self.file_urlobject is not None:
            result['FileURLObject'] = self.file_urlobject
        if self.file_type is not None:
            result['FileType'] = self.file_type
        if self.output_type is not None:
            result['OutputType'] = self.output_type
        if self.async_ is not None:
            result['Async'] = self.async_
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileURLObject') is not None:
            self.file_urlobject = m.get('FileURLObject')
        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')
        if m.get('OutputType') is not None:
            self.output_type = m.get('OutputType')
        if m.get('Async') is not None:
            self.async_ = m.get('Async')
        return self


class TrimDocumentResponseBodyData(TeaModel):
    def __init__(
        self,
        content: str = None,
    ):
        self.content = content

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        return self


class TrimDocumentResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: TrimDocumentResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = TrimDocumentResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class TrimDocumentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: TrimDocumentResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = TrimDocumentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


