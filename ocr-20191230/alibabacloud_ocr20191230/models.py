# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import BinaryIO, Dict, List, Any


class DetectCardScreenshotRequest(TeaModel):
    def __init__(
        self,
        image_url: str = None,
    ):
        self.image_url = image_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        screen_score: float = None,
        screen_threshold: float = None,
    ):
        self.screen_score = screen_score
        self.screen_threshold = screen_threshold

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.screen_score is not None:
            result['ScreenScore'] = self.screen_score
        if self.screen_threshold is not None:
            result['ScreenThreshold'] = self.screen_threshold
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ScreenScore') is not None:
            self.screen_score = m.get('ScreenScore')
        if m.get('ScreenThreshold') is not None:
            self.screen_threshold = m.get('ScreenThreshold')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        data: DetectCardScreenshotResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DetectCardScreenshotResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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
            temp_model = DetectCardScreenshotResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAsyncJobResultRequest(TeaModel):
    def __init__(
        self,
        job_id: str = None,
    ):
        self.job_id = job_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class GetAsyncJobResultResponseBodyData(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        job_id: str = None,
        result: str = None,
        status: str = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.job_id = job_id
        self.result = result
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.result is not None:
            result['Result'] = self.result
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetAsyncJobResultResponseBody(TeaModel):
    def __init__(
        self,
        data: GetAsyncJobResultResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetAsyncJobResultResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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
            temp_model = GetAsyncJobResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeAccountPageRequest(TeaModel):
    def __init__(
        self,
        image_url: str = None,
    ):
        self.image_url = image_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        return self


class RecognizeAccountPageAdvanceRequest(TeaModel):
    def __init__(
        self,
        image_urlobject: BinaryIO = None,
    ):
        self.image_urlobject = image_urlobject

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_urlobject is not None:
            result['ImageURLObject'] = self.image_urlobject
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURLObject') is not None:
            self.image_urlobject = m.get('ImageURLObject')
        return self


class RecognizeAccountPageResponseBodyDataInvalidStampAreas(TeaModel):
    def __init__(
        self,
        height: int = None,
        left: int = None,
        top: int = None,
        width: int = None,
    ):
        self.height = height
        self.left = left
        self.top = top
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.height is not None:
            result['Height'] = self.height
        if self.left is not None:
            result['Left'] = self.left
        if self.top is not None:
            result['Top'] = self.top
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Left') is not None:
            self.left = m.get('Left')
        if m.get('Top') is not None:
            self.top = m.get('Top')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class RecognizeAccountPageResponseBodyDataOtherStampAreas(TeaModel):
    def __init__(
        self,
        height: int = None,
        left: int = None,
        top: int = None,
        width: int = None,
    ):
        self.height = height
        self.left = left
        self.top = top
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.height is not None:
            result['Height'] = self.height
        if self.left is not None:
            result['Left'] = self.left
        if self.top is not None:
            result['Top'] = self.top
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Left') is not None:
            self.left = m.get('Left')
        if m.get('Top') is not None:
            self.top = m.get('Top')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class RecognizeAccountPageResponseBodyDataRegisterStampAreas(TeaModel):
    def __init__(
        self,
        height: int = None,
        left: int = None,
        top: int = None,
        width: int = None,
    ):
        self.height = height
        self.left = left
        self.top = top
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.height is not None:
            result['Height'] = self.height
        if self.left is not None:
            result['Left'] = self.left
        if self.top is not None:
            result['Top'] = self.top
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Left') is not None:
            self.left = m.get('Left')
        if m.get('Top') is not None:
            self.top = m.get('Top')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class RecognizeAccountPageResponseBodyDataTitleArea(TeaModel):
    def __init__(
        self,
        height: int = None,
        left: int = None,
        top: int = None,
        width: int = None,
    ):
        self.height = height
        self.left = left
        self.top = top
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.height is not None:
            result['Height'] = self.height
        if self.left is not None:
            result['Left'] = self.left
        if self.top is not None:
            result['Top'] = self.top
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Left') is not None:
            self.left = m.get('Left')
        if m.get('Top') is not None:
            self.top = m.get('Top')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class RecognizeAccountPageResponseBodyDataUndertakeStampAreas(TeaModel):
    def __init__(
        self,
        height: int = None,
        left: int = None,
        top: int = None,
        width: int = None,
    ):
        self.height = height
        self.left = left
        self.top = top
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.height is not None:
            result['Height'] = self.height
        if self.left is not None:
            result['Left'] = self.left
        if self.top is not None:
            result['Top'] = self.top
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Left') is not None:
            self.left = m.get('Left')
        if m.get('Top') is not None:
            self.top = m.get('Top')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class RecognizeAccountPageResponseBodyData(TeaModel):
    def __init__(
        self,
        angle: float = None,
        birth_date: str = None,
        birth_place: str = None,
        gender: str = None,
        idnumber: str = None,
        invalid_stamp_areas: List[RecognizeAccountPageResponseBodyDataInvalidStampAreas] = None,
        name: str = None,
        nationality: str = None,
        native_place: str = None,
        other_stamp_areas: List[RecognizeAccountPageResponseBodyDataOtherStampAreas] = None,
        register_stamp_areas: List[RecognizeAccountPageResponseBodyDataRegisterStampAreas] = None,
        relation: str = None,
        title_area: RecognizeAccountPageResponseBodyDataTitleArea = None,
        undertake_stamp_areas: List[RecognizeAccountPageResponseBodyDataUndertakeStampAreas] = None,
    ):
        self.angle = angle
        self.birth_date = birth_date
        self.birth_place = birth_place
        self.gender = gender
        self.idnumber = idnumber
        self.invalid_stamp_areas = invalid_stamp_areas
        self.name = name
        self.nationality = nationality
        self.native_place = native_place
        self.other_stamp_areas = other_stamp_areas
        self.register_stamp_areas = register_stamp_areas
        self.relation = relation
        self.title_area = title_area
        self.undertake_stamp_areas = undertake_stamp_areas

    def validate(self):
        if self.invalid_stamp_areas:
            for k in self.invalid_stamp_areas:
                if k:
                    k.validate()
        if self.other_stamp_areas:
            for k in self.other_stamp_areas:
                if k:
                    k.validate()
        if self.register_stamp_areas:
            for k in self.register_stamp_areas:
                if k:
                    k.validate()
        if self.title_area:
            self.title_area.validate()
        if self.undertake_stamp_areas:
            for k in self.undertake_stamp_areas:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.angle is not None:
            result['Angle'] = self.angle
        if self.birth_date is not None:
            result['BirthDate'] = self.birth_date
        if self.birth_place is not None:
            result['BirthPlace'] = self.birth_place
        if self.gender is not None:
            result['Gender'] = self.gender
        if self.idnumber is not None:
            result['IDNumber'] = self.idnumber
        result['InvalidStampAreas'] = []
        if self.invalid_stamp_areas is not None:
            for k in self.invalid_stamp_areas:
                result['InvalidStampAreas'].append(k.to_map() if k else None)
        if self.name is not None:
            result['Name'] = self.name
        if self.nationality is not None:
            result['Nationality'] = self.nationality
        if self.native_place is not None:
            result['NativePlace'] = self.native_place
        result['OtherStampAreas'] = []
        if self.other_stamp_areas is not None:
            for k in self.other_stamp_areas:
                result['OtherStampAreas'].append(k.to_map() if k else None)
        result['RegisterStampAreas'] = []
        if self.register_stamp_areas is not None:
            for k in self.register_stamp_areas:
                result['RegisterStampAreas'].append(k.to_map() if k else None)
        if self.relation is not None:
            result['Relation'] = self.relation
        if self.title_area is not None:
            result['TitleArea'] = self.title_area.to_map()
        result['UndertakeStampAreas'] = []
        if self.undertake_stamp_areas is not None:
            for k in self.undertake_stamp_areas:
                result['UndertakeStampAreas'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Angle') is not None:
            self.angle = m.get('Angle')
        if m.get('BirthDate') is not None:
            self.birth_date = m.get('BirthDate')
        if m.get('BirthPlace') is not None:
            self.birth_place = m.get('BirthPlace')
        if m.get('Gender') is not None:
            self.gender = m.get('Gender')
        if m.get('IDNumber') is not None:
            self.idnumber = m.get('IDNumber')
        self.invalid_stamp_areas = []
        if m.get('InvalidStampAreas') is not None:
            for k in m.get('InvalidStampAreas'):
                temp_model = RecognizeAccountPageResponseBodyDataInvalidStampAreas()
                self.invalid_stamp_areas.append(temp_model.from_map(k))
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Nationality') is not None:
            self.nationality = m.get('Nationality')
        if m.get('NativePlace') is not None:
            self.native_place = m.get('NativePlace')
        self.other_stamp_areas = []
        if m.get('OtherStampAreas') is not None:
            for k in m.get('OtherStampAreas'):
                temp_model = RecognizeAccountPageResponseBodyDataOtherStampAreas()
                self.other_stamp_areas.append(temp_model.from_map(k))
        self.register_stamp_areas = []
        if m.get('RegisterStampAreas') is not None:
            for k in m.get('RegisterStampAreas'):
                temp_model = RecognizeAccountPageResponseBodyDataRegisterStampAreas()
                self.register_stamp_areas.append(temp_model.from_map(k))
        if m.get('Relation') is not None:
            self.relation = m.get('Relation')
        if m.get('TitleArea') is not None:
            temp_model = RecognizeAccountPageResponseBodyDataTitleArea()
            self.title_area = temp_model.from_map(m['TitleArea'])
        self.undertake_stamp_areas = []
        if m.get('UndertakeStampAreas') is not None:
            for k in m.get('UndertakeStampAreas'):
                temp_model = RecognizeAccountPageResponseBodyDataUndertakeStampAreas()
                self.undertake_stamp_areas.append(temp_model.from_map(k))
        return self


class RecognizeAccountPageResponseBody(TeaModel):
    def __init__(
        self,
        data: RecognizeAccountPageResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = RecognizeAccountPageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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
            temp_model = RecognizeAccountPageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeBankCardRequest(TeaModel):
    def __init__(
        self,
        image_url: str = None,
    ):
        self.image_url = image_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        return self


class RecognizeBankCardResponseBodyData(TeaModel):
    def __init__(
        self,
        bank_name: str = None,
        card_number: str = None,
        valid_date: str = None,
    ):
        self.bank_name = bank_name
        self.card_number = card_number
        self.valid_date = valid_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bank_name is not None:
            result['BankName'] = self.bank_name
        if self.card_number is not None:
            result['CardNumber'] = self.card_number
        if self.valid_date is not None:
            result['ValidDate'] = self.valid_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BankName') is not None:
            self.bank_name = m.get('BankName')
        if m.get('CardNumber') is not None:
            self.card_number = m.get('CardNumber')
        if m.get('ValidDate') is not None:
            self.valid_date = m.get('ValidDate')
        return self


class RecognizeBankCardResponseBody(TeaModel):
    def __init__(
        self,
        data: RecognizeBankCardResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = RecognizeBankCardResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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
            temp_model = RecognizeBankCardResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeBusinessCardRequest(TeaModel):
    def __init__(
        self,
        image_url: str = None,
    ):
        self.image_url = image_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        return self


class RecognizeBusinessCardAdvanceRequest(TeaModel):
    def __init__(
        self,
        image_urlobject: BinaryIO = None,
    ):
        self.image_urlobject = image_urlobject

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_urlobject is not None:
            result['ImageURLObject'] = self.image_urlobject
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURLObject') is not None:
            self.image_urlobject = m.get('ImageURLObject')
        return self


class RecognizeBusinessCardResponseBodyData(TeaModel):
    def __init__(
        self,
        addresses: List[str] = None,
        cell_phone_numbers: List[str] = None,
        companies: List[str] = None,
        departments: List[str] = None,
        emails: List[str] = None,
        name: str = None,
        office_phone_numbers: List[str] = None,
        titles: List[str] = None,
    ):
        self.addresses = addresses
        self.cell_phone_numbers = cell_phone_numbers
        self.companies = companies
        self.departments = departments
        self.emails = emails
        self.name = name
        self.office_phone_numbers = office_phone_numbers
        self.titles = titles

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.addresses is not None:
            result['Addresses'] = self.addresses
        if self.cell_phone_numbers is not None:
            result['CellPhoneNumbers'] = self.cell_phone_numbers
        if self.companies is not None:
            result['Companies'] = self.companies
        if self.departments is not None:
            result['Departments'] = self.departments
        if self.emails is not None:
            result['Emails'] = self.emails
        if self.name is not None:
            result['Name'] = self.name
        if self.office_phone_numbers is not None:
            result['OfficePhoneNumbers'] = self.office_phone_numbers
        if self.titles is not None:
            result['Titles'] = self.titles
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Addresses') is not None:
            self.addresses = m.get('Addresses')
        if m.get('CellPhoneNumbers') is not None:
            self.cell_phone_numbers = m.get('CellPhoneNumbers')
        if m.get('Companies') is not None:
            self.companies = m.get('Companies')
        if m.get('Departments') is not None:
            self.departments = m.get('Departments')
        if m.get('Emails') is not None:
            self.emails = m.get('Emails')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OfficePhoneNumbers') is not None:
            self.office_phone_numbers = m.get('OfficePhoneNumbers')
        if m.get('Titles') is not None:
            self.titles = m.get('Titles')
        return self


class RecognizeBusinessCardResponseBody(TeaModel):
    def __init__(
        self,
        data: RecognizeBusinessCardResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = RecognizeBusinessCardResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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
            temp_model = RecognizeBusinessCardResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeBusinessLicenseRequest(TeaModel):
    def __init__(
        self,
        image_url: str = None,
    ):
        self.image_url = image_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        return self


class RecognizeBusinessLicenseAdvanceRequest(TeaModel):
    def __init__(
        self,
        image_urlobject: BinaryIO = None,
    ):
        self.image_urlobject = image_urlobject

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_urlobject is not None:
            result['ImageURLObject'] = self.image_urlobject
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURLObject') is not None:
            self.image_urlobject = m.get('ImageURLObject')
        return self


class RecognizeBusinessLicenseResponseBodyDataEmblem(TeaModel):
    def __init__(
        self,
        height: int = None,
        left: int = None,
        top: int = None,
        width: int = None,
    ):
        self.height = height
        self.left = left
        self.top = top
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.height is not None:
            result['Height'] = self.height
        if self.left is not None:
            result['Left'] = self.left
        if self.top is not None:
            result['Top'] = self.top
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Left') is not None:
            self.left = m.get('Left')
        if m.get('Top') is not None:
            self.top = m.get('Top')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class RecognizeBusinessLicenseResponseBodyDataQRCode(TeaModel):
    def __init__(
        self,
        height: int = None,
        left: int = None,
        top: int = None,
        width: int = None,
    ):
        self.height = height
        self.left = left
        self.top = top
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.height is not None:
            result['Height'] = self.height
        if self.left is not None:
            result['Left'] = self.left
        if self.top is not None:
            result['Top'] = self.top
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Left') is not None:
            self.left = m.get('Left')
        if m.get('Top') is not None:
            self.top = m.get('Top')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class RecognizeBusinessLicenseResponseBodyDataStamp(TeaModel):
    def __init__(
        self,
        height: int = None,
        left: int = None,
        top: int = None,
        width: int = None,
    ):
        self.height = height
        self.left = left
        self.top = top
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.height is not None:
            result['Height'] = self.height
        if self.left is not None:
            result['Left'] = self.left
        if self.top is not None:
            result['Top'] = self.top
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Left') is not None:
            self.left = m.get('Left')
        if m.get('Top') is not None:
            self.top = m.get('Top')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class RecognizeBusinessLicenseResponseBodyDataTitle(TeaModel):
    def __init__(
        self,
        height: int = None,
        left: int = None,
        top: int = None,
        width: int = None,
    ):
        self.height = height
        self.left = left
        self.top = top
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.height is not None:
            result['Height'] = self.height
        if self.left is not None:
            result['Left'] = self.left
        if self.top is not None:
            result['Top'] = self.top
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Left') is not None:
            self.left = m.get('Left')
        if m.get('Top') is not None:
            self.top = m.get('Top')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class RecognizeBusinessLicenseResponseBodyData(TeaModel):
    def __init__(
        self,
        address: str = None,
        angle: float = None,
        business: str = None,
        capital: str = None,
        emblem: RecognizeBusinessLicenseResponseBodyDataEmblem = None,
        establish_date: str = None,
        legal_person: str = None,
        name: str = None,
        qrcode: RecognizeBusinessLicenseResponseBodyDataQRCode = None,
        register_number: str = None,
        stamp: RecognizeBusinessLicenseResponseBodyDataStamp = None,
        title: RecognizeBusinessLicenseResponseBodyDataTitle = None,
        type: str = None,
        valid_period: str = None,
    ):
        self.address = address
        self.angle = angle
        self.business = business
        self.capital = capital
        self.emblem = emblem
        self.establish_date = establish_date
        self.legal_person = legal_person
        self.name = name
        self.qrcode = qrcode
        self.register_number = register_number
        self.stamp = stamp
        self.title = title
        self.type = type
        self.valid_period = valid_period

    def validate(self):
        if self.emblem:
            self.emblem.validate()
        if self.qrcode:
            self.qrcode.validate()
        if self.stamp:
            self.stamp.validate()
        if self.title:
            self.title.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.angle is not None:
            result['Angle'] = self.angle
        if self.business is not None:
            result['Business'] = self.business
        if self.capital is not None:
            result['Capital'] = self.capital
        if self.emblem is not None:
            result['Emblem'] = self.emblem.to_map()
        if self.establish_date is not None:
            result['EstablishDate'] = self.establish_date
        if self.legal_person is not None:
            result['LegalPerson'] = self.legal_person
        if self.name is not None:
            result['Name'] = self.name
        if self.qrcode is not None:
            result['QRCode'] = self.qrcode.to_map()
        if self.register_number is not None:
            result['RegisterNumber'] = self.register_number
        if self.stamp is not None:
            result['Stamp'] = self.stamp.to_map()
        if self.title is not None:
            result['Title'] = self.title.to_map()
        if self.type is not None:
            result['Type'] = self.type
        if self.valid_period is not None:
            result['ValidPeriod'] = self.valid_period
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('Angle') is not None:
            self.angle = m.get('Angle')
        if m.get('Business') is not None:
            self.business = m.get('Business')
        if m.get('Capital') is not None:
            self.capital = m.get('Capital')
        if m.get('Emblem') is not None:
            temp_model = RecognizeBusinessLicenseResponseBodyDataEmblem()
            self.emblem = temp_model.from_map(m['Emblem'])
        if m.get('EstablishDate') is not None:
            self.establish_date = m.get('EstablishDate')
        if m.get('LegalPerson') is not None:
            self.legal_person = m.get('LegalPerson')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('QRCode') is not None:
            temp_model = RecognizeBusinessLicenseResponseBodyDataQRCode()
            self.qrcode = temp_model.from_map(m['QRCode'])
        if m.get('RegisterNumber') is not None:
            self.register_number = m.get('RegisterNumber')
        if m.get('Stamp') is not None:
            temp_model = RecognizeBusinessLicenseResponseBodyDataStamp()
            self.stamp = temp_model.from_map(m['Stamp'])
        if m.get('Title') is not None:
            temp_model = RecognizeBusinessLicenseResponseBodyDataTitle()
            self.title = temp_model.from_map(m['Title'])
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('ValidPeriod') is not None:
            self.valid_period = m.get('ValidPeriod')
        return self


class RecognizeBusinessLicenseResponseBody(TeaModel):
    def __init__(
        self,
        data: RecognizeBusinessLicenseResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = RecognizeBusinessLicenseResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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
            temp_model = RecognizeBusinessLicenseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeCharacterRequest(TeaModel):
    def __init__(
        self,
        image_url: str = None,
        min_height: int = None,
        output_probability: bool = None,
    ):
        self.image_url = image_url
        self.min_height = min_height
        self.output_probability = output_probability

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        if self.min_height is not None:
            result['MinHeight'] = self.min_height
        if self.output_probability is not None:
            result['OutputProbability'] = self.output_probability
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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
        min_height: int = None,
        output_probability: bool = None,
    ):
        self.image_urlobject = image_urlobject
        self.min_height = min_height
        self.output_probability = output_probability

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_urlobject is not None:
            result['ImageURLObject'] = self.image_urlobject
        if self.min_height is not None:
            result['MinHeight'] = self.min_height
        if self.output_probability is not None:
            result['OutputProbability'] = self.output_probability
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURLObject') is not None:
            self.image_urlobject = m.get('ImageURLObject')
        if m.get('MinHeight') is not None:
            self.min_height = m.get('MinHeight')
        if m.get('OutputProbability') is not None:
            self.output_probability = m.get('OutputProbability')
        return self


class RecognizeCharacterResponseBodyDataResultsTextRectangles(TeaModel):
    def __init__(
        self,
        angle: int = None,
        height: int = None,
        left: int = None,
        top: int = None,
        width: int = None,
    ):
        self.angle = angle
        self.height = height
        self.left = left
        self.top = top
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.angle is not None:
            result['Angle'] = self.angle
        if self.height is not None:
            result['Height'] = self.height
        if self.left is not None:
            result['Left'] = self.left
        if self.top is not None:
            result['Top'] = self.top
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Angle') is not None:
            self.angle = m.get('Angle')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Left') is not None:
            self.left = m.get('Left')
        if m.get('Top') is not None:
            self.top = m.get('Top')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class RecognizeCharacterResponseBodyDataResults(TeaModel):
    def __init__(
        self,
        probability: float = None,
        text: str = None,
        text_rectangles: RecognizeCharacterResponseBodyDataResultsTextRectangles = None,
    ):
        self.probability = probability
        self.text = text
        self.text_rectangles = text_rectangles

    def validate(self):
        if self.text_rectangles:
            self.text_rectangles.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.probability is not None:
            result['Probability'] = self.probability
        if self.text is not None:
            result['Text'] = self.text
        if self.text_rectangles is not None:
            result['TextRectangles'] = self.text_rectangles.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Probability') is not None:
            self.probability = m.get('Probability')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('TextRectangles') is not None:
            temp_model = RecognizeCharacterResponseBodyDataResultsTextRectangles()
            self.text_rectangles = temp_model.from_map(m['TextRectangles'])
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        data: RecognizeCharacterResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = RecognizeCharacterResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        authority: str = None,
        birth_date: str = None,
        birth_day: str = None,
        birth_place: str = None,
        birth_place_raw: str = None,
        country: str = None,
        expiry_date: str = None,
        expiry_day: str = None,
        issue_date: str = None,
        issue_place: str = None,
        issue_place_raw: str = None,
        line_one: str = None,
        line_zero: str = None,
        name: str = None,
        name_chinese: str = None,
        name_chinese_raw: str = None,
        passport_no: str = None,
        person_id: str = None,
        sex: str = None,
        source_country: str = None,
        success: bool = None,
        type: str = None,
    ):
        self.authority = authority
        self.birth_date = birth_date
        self.birth_day = birth_day
        self.birth_place = birth_place
        self.birth_place_raw = birth_place_raw
        self.country = country
        self.expiry_date = expiry_date
        self.expiry_day = expiry_day
        self.issue_date = issue_date
        self.issue_place = issue_place
        self.issue_place_raw = issue_place_raw
        self.line_one = line_one
        self.line_zero = line_zero
        self.name = name
        self.name_chinese = name_chinese
        self.name_chinese_raw = name_chinese_raw
        self.passport_no = passport_no
        self.person_id = person_id
        self.sex = sex
        self.source_country = source_country
        self.success = success
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authority is not None:
            result['Authority'] = self.authority
        if self.birth_date is not None:
            result['BirthDate'] = self.birth_date
        if self.birth_day is not None:
            result['BirthDay'] = self.birth_day
        if self.birth_place is not None:
            result['BirthPlace'] = self.birth_place
        if self.birth_place_raw is not None:
            result['BirthPlaceRaw'] = self.birth_place_raw
        if self.country is not None:
            result['Country'] = self.country
        if self.expiry_date is not None:
            result['ExpiryDate'] = self.expiry_date
        if self.expiry_day is not None:
            result['ExpiryDay'] = self.expiry_day
        if self.issue_date is not None:
            result['IssueDate'] = self.issue_date
        if self.issue_place is not None:
            result['IssuePlace'] = self.issue_place
        if self.issue_place_raw is not None:
            result['IssuePlaceRaw'] = self.issue_place_raw
        if self.line_one is not None:
            result['LineOne'] = self.line_one
        if self.line_zero is not None:
            result['LineZero'] = self.line_zero
        if self.name is not None:
            result['Name'] = self.name
        if self.name_chinese is not None:
            result['NameChinese'] = self.name_chinese
        if self.name_chinese_raw is not None:
            result['NameChineseRaw'] = self.name_chinese_raw
        if self.passport_no is not None:
            result['PassportNo'] = self.passport_no
        if self.person_id is not None:
            result['PersonId'] = self.person_id
        if self.sex is not None:
            result['Sex'] = self.sex
        if self.source_country is not None:
            result['SourceCountry'] = self.source_country
        if self.success is not None:
            result['Success'] = self.success
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Authority') is not None:
            self.authority = m.get('Authority')
        if m.get('BirthDate') is not None:
            self.birth_date = m.get('BirthDate')
        if m.get('BirthDay') is not None:
            self.birth_day = m.get('BirthDay')
        if m.get('BirthPlace') is not None:
            self.birth_place = m.get('BirthPlace')
        if m.get('BirthPlaceRaw') is not None:
            self.birth_place_raw = m.get('BirthPlaceRaw')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('ExpiryDate') is not None:
            self.expiry_date = m.get('ExpiryDate')
        if m.get('ExpiryDay') is not None:
            self.expiry_day = m.get('ExpiryDay')
        if m.get('IssueDate') is not None:
            self.issue_date = m.get('IssueDate')
        if m.get('IssuePlace') is not None:
            self.issue_place = m.get('IssuePlace')
        if m.get('IssuePlaceRaw') is not None:
            self.issue_place_raw = m.get('IssuePlaceRaw')
        if m.get('LineOne') is not None:
            self.line_one = m.get('LineOne')
        if m.get('LineZero') is not None:
            self.line_zero = m.get('LineZero')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NameChinese') is not None:
            self.name_chinese = m.get('NameChinese')
        if m.get('NameChineseRaw') is not None:
            self.name_chinese_raw = m.get('NameChineseRaw')
        if m.get('PassportNo') is not None:
            self.passport_no = m.get('PassportNo')
        if m.get('PersonId') is not None:
            self.person_id = m.get('PersonId')
        if m.get('Sex') is not None:
            self.sex = m.get('Sex')
        if m.get('SourceCountry') is not None:
            self.source_country = m.get('SourceCountry')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class RecognizeChinapassportResponseBody(TeaModel):
    def __init__(
        self,
        data: RecognizeChinapassportResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = RecognizeChinapassportResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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
            temp_model = RecognizeChinapassportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeDriverLicenseRequest(TeaModel):
    def __init__(
        self,
        image_url: str = None,
        side: str = None,
    ):
        self.image_url = image_url
        self.side = side

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        if self.side is not None:
            result['Side'] = self.side
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        if m.get('Side') is not None:
            self.side = m.get('Side')
        return self


class RecognizeDriverLicenseAdvanceRequest(TeaModel):
    def __init__(
        self,
        image_urlobject: BinaryIO = None,
        side: str = None,
    ):
        self.image_urlobject = image_urlobject
        self.side = side

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_urlobject is not None:
            result['ImageURLObject'] = self.image_urlobject
        if self.side is not None:
            result['Side'] = self.side
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURLObject') is not None:
            self.image_urlobject = m.get('ImageURLObject')
        if m.get('Side') is not None:
            self.side = m.get('Side')
        return self


class RecognizeDriverLicenseResponseBodyDataBackResult(TeaModel):
    def __init__(
        self,
        archive_number: str = None,
        card_number: str = None,
        name: str = None,
        record: str = None,
    ):
        self.archive_number = archive_number
        self.card_number = card_number
        self.name = name
        self.record = record

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.archive_number is not None:
            result['ArchiveNumber'] = self.archive_number
        if self.card_number is not None:
            result['CardNumber'] = self.card_number
        if self.name is not None:
            result['Name'] = self.name
        if self.record is not None:
            result['Record'] = self.record
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArchiveNumber') is not None:
            self.archive_number = m.get('ArchiveNumber')
        if m.get('CardNumber') is not None:
            self.card_number = m.get('CardNumber')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Record') is not None:
            self.record = m.get('Record')
        return self


class RecognizeDriverLicenseResponseBodyDataFaceResult(TeaModel):
    def __init__(
        self,
        address: str = None,
        end_date: str = None,
        gender: str = None,
        issue_date: str = None,
        issue_unit: str = None,
        license_number: str = None,
        name: str = None,
        start_date: str = None,
        vehicle_type: str = None,
    ):
        self.address = address
        self.end_date = end_date
        self.gender = gender
        self.issue_date = issue_date
        self.issue_unit = issue_unit
        self.license_number = license_number
        self.name = name
        self.start_date = start_date
        self.vehicle_type = vehicle_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.gender is not None:
            result['Gender'] = self.gender
        if self.issue_date is not None:
            result['IssueDate'] = self.issue_date
        if self.issue_unit is not None:
            result['IssueUnit'] = self.issue_unit
        if self.license_number is not None:
            result['LicenseNumber'] = self.license_number
        if self.name is not None:
            result['Name'] = self.name
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.vehicle_type is not None:
            result['VehicleType'] = self.vehicle_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('Gender') is not None:
            self.gender = m.get('Gender')
        if m.get('IssueDate') is not None:
            self.issue_date = m.get('IssueDate')
        if m.get('IssueUnit') is not None:
            self.issue_unit = m.get('IssueUnit')
        if m.get('LicenseNumber') is not None:
            self.license_number = m.get('LicenseNumber')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('VehicleType') is not None:
            self.vehicle_type = m.get('VehicleType')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        data: RecognizeDriverLicenseResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = RecognizeDriverLicenseResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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
            temp_model = RecognizeDriverLicenseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeDrivingLicenseRequest(TeaModel):
    def __init__(
        self,
        image_url: str = None,
        side: str = None,
    ):
        self.image_url = image_url
        self.side = side

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        if self.side is not None:
            result['Side'] = self.side
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        if m.get('Side') is not None:
            self.side = m.get('Side')
        return self


class RecognizeDrivingLicenseAdvanceRequest(TeaModel):
    def __init__(
        self,
        image_urlobject: BinaryIO = None,
        side: str = None,
    ):
        self.image_urlobject = image_urlobject
        self.side = side

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_urlobject is not None:
            result['ImageURLObject'] = self.image_urlobject
        if self.side is not None:
            result['Side'] = self.side
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURLObject') is not None:
            self.image_urlobject = m.get('ImageURLObject')
        if m.get('Side') is not None:
            self.side = m.get('Side')
        return self


class RecognizeDrivingLicenseResponseBodyDataBackResult(TeaModel):
    def __init__(
        self,
        approved_load: str = None,
        approved_passenger_capacity: str = None,
        energy_type: str = None,
        file_number: str = None,
        gross_mass: str = None,
        inspection_record: str = None,
        overall_dimension: str = None,
        plate_number: str = None,
        traction_mass: str = None,
        unladen_mass: str = None,
    ):
        self.approved_load = approved_load
        self.approved_passenger_capacity = approved_passenger_capacity
        self.energy_type = energy_type
        self.file_number = file_number
        self.gross_mass = gross_mass
        self.inspection_record = inspection_record
        self.overall_dimension = overall_dimension
        self.plate_number = plate_number
        self.traction_mass = traction_mass
        self.unladen_mass = unladen_mass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.approved_load is not None:
            result['ApprovedLoad'] = self.approved_load
        if self.approved_passenger_capacity is not None:
            result['ApprovedPassengerCapacity'] = self.approved_passenger_capacity
        if self.energy_type is not None:
            result['EnergyType'] = self.energy_type
        if self.file_number is not None:
            result['FileNumber'] = self.file_number
        if self.gross_mass is not None:
            result['GrossMass'] = self.gross_mass
        if self.inspection_record is not None:
            result['InspectionRecord'] = self.inspection_record
        if self.overall_dimension is not None:
            result['OverallDimension'] = self.overall_dimension
        if self.plate_number is not None:
            result['PlateNumber'] = self.plate_number
        if self.traction_mass is not None:
            result['TractionMass'] = self.traction_mass
        if self.unladen_mass is not None:
            result['UnladenMass'] = self.unladen_mass
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApprovedLoad') is not None:
            self.approved_load = m.get('ApprovedLoad')
        if m.get('ApprovedPassengerCapacity') is not None:
            self.approved_passenger_capacity = m.get('ApprovedPassengerCapacity')
        if m.get('EnergyType') is not None:
            self.energy_type = m.get('EnergyType')
        if m.get('FileNumber') is not None:
            self.file_number = m.get('FileNumber')
        if m.get('GrossMass') is not None:
            self.gross_mass = m.get('GrossMass')
        if m.get('InspectionRecord') is not None:
            self.inspection_record = m.get('InspectionRecord')
        if m.get('OverallDimension') is not None:
            self.overall_dimension = m.get('OverallDimension')
        if m.get('PlateNumber') is not None:
            self.plate_number = m.get('PlateNumber')
        if m.get('TractionMass') is not None:
            self.traction_mass = m.get('TractionMass')
        if m.get('UnladenMass') is not None:
            self.unladen_mass = m.get('UnladenMass')
        return self


class RecognizeDrivingLicenseResponseBodyDataFaceResult(TeaModel):
    def __init__(
        self,
        address: str = None,
        engine_number: str = None,
        issue_date: str = None,
        model: str = None,
        owner: str = None,
        plate_number: str = None,
        register_date: str = None,
        use_character: str = None,
        vehicle_type: str = None,
        vin: str = None,
    ):
        self.address = address
        self.engine_number = engine_number
        self.issue_date = issue_date
        self.model = model
        self.owner = owner
        self.plate_number = plate_number
        self.register_date = register_date
        self.use_character = use_character
        self.vehicle_type = vehicle_type
        self.vin = vin

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.engine_number is not None:
            result['EngineNumber'] = self.engine_number
        if self.issue_date is not None:
            result['IssueDate'] = self.issue_date
        if self.model is not None:
            result['Model'] = self.model
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.plate_number is not None:
            result['PlateNumber'] = self.plate_number
        if self.register_date is not None:
            result['RegisterDate'] = self.register_date
        if self.use_character is not None:
            result['UseCharacter'] = self.use_character
        if self.vehicle_type is not None:
            result['VehicleType'] = self.vehicle_type
        if self.vin is not None:
            result['Vin'] = self.vin
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('EngineNumber') is not None:
            self.engine_number = m.get('EngineNumber')
        if m.get('IssueDate') is not None:
            self.issue_date = m.get('IssueDate')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('PlateNumber') is not None:
            self.plate_number = m.get('PlateNumber')
        if m.get('RegisterDate') is not None:
            self.register_date = m.get('RegisterDate')
        if m.get('UseCharacter') is not None:
            self.use_character = m.get('UseCharacter')
        if m.get('VehicleType') is not None:
            self.vehicle_type = m.get('VehicleType')
        if m.get('Vin') is not None:
            self.vin = m.get('Vin')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        data: RecognizeDrivingLicenseResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = RecognizeDrivingLicenseResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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
            temp_model = RecognizeDrivingLicenseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeIdentityCardRequest(TeaModel):
    def __init__(
        self,
        image_url: str = None,
        side: str = None,
    ):
        self.image_url = image_url
        self.side = side

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        if self.side is not None:
            result['Side'] = self.side
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        if m.get('Side') is not None:
            self.side = m.get('Side')
        return self


class RecognizeIdentityCardAdvanceRequest(TeaModel):
    def __init__(
        self,
        image_urlobject: BinaryIO = None,
        side: str = None,
    ):
        self.image_urlobject = image_urlobject
        self.side = side

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_urlobject is not None:
            result['ImageURLObject'] = self.image_urlobject
        if self.side is not None:
            result['Side'] = self.side
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURLObject') is not None:
            self.image_urlobject = m.get('ImageURLObject')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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


class RecognizeIdentityCardResponseBodyDataFrontResultCardAreas(TeaModel):
    def __init__(
        self,
        x: float = None,
        y: float = None,
    ):
        self.x = x
        self.y = y

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        return self


class RecognizeIdentityCardResponseBodyDataFrontResultFaceRectVertices(TeaModel):
    def __init__(
        self,
        x: float = None,
        y: float = None,
    ):
        self.x = x
        self.y = y

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        return self


class RecognizeIdentityCardResponseBodyDataFrontResultFaceRectangleCenter(TeaModel):
    def __init__(
        self,
        x: float = None,
        y: float = None,
    ):
        self.x = x
        self.y = y

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        return self


class RecognizeIdentityCardResponseBodyDataFrontResultFaceRectangleSize(TeaModel):
    def __init__(
        self,
        height: float = None,
        width: float = None,
    ):
        self.height = height
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.height is not None:
            result['Height'] = self.height
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class RecognizeIdentityCardResponseBodyDataFrontResultFaceRectangle(TeaModel):
    def __init__(
        self,
        angle: float = None,
        center: RecognizeIdentityCardResponseBodyDataFrontResultFaceRectangleCenter = None,
        size: RecognizeIdentityCardResponseBodyDataFrontResultFaceRectangleSize = None,
    ):
        self.angle = angle
        self.center = center
        self.size = size

    def validate(self):
        if self.center:
            self.center.validate()
        if self.size:
            self.size.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.angle is not None:
            result['Angle'] = self.angle
        if self.center is not None:
            result['Center'] = self.center.to_map()
        if self.size is not None:
            result['Size'] = self.size.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Angle') is not None:
            self.angle = m.get('Angle')
        if m.get('Center') is not None:
            temp_model = RecognizeIdentityCardResponseBodyDataFrontResultFaceRectangleCenter()
            self.center = temp_model.from_map(m['Center'])
        if m.get('Size') is not None:
            temp_model = RecognizeIdentityCardResponseBodyDataFrontResultFaceRectangleSize()
            self.size = temp_model.from_map(m['Size'])
        return self


class RecognizeIdentityCardResponseBodyDataFrontResult(TeaModel):
    def __init__(
        self,
        address: str = None,
        birth_date: str = None,
        card_areas: List[RecognizeIdentityCardResponseBodyDataFrontResultCardAreas] = None,
        face_rect_vertices: List[RecognizeIdentityCardResponseBodyDataFrontResultFaceRectVertices] = None,
        face_rectangle: RecognizeIdentityCardResponseBodyDataFrontResultFaceRectangle = None,
        gender: str = None,
        idnumber: str = None,
        name: str = None,
        nationality: str = None,
    ):
        self.address = address
        self.birth_date = birth_date
        self.card_areas = card_areas
        self.face_rect_vertices = face_rect_vertices
        self.face_rectangle = face_rectangle
        self.gender = gender
        self.idnumber = idnumber
        self.name = name
        self.nationality = nationality

    def validate(self):
        if self.card_areas:
            for k in self.card_areas:
                if k:
                    k.validate()
        if self.face_rect_vertices:
            for k in self.face_rect_vertices:
                if k:
                    k.validate()
        if self.face_rectangle:
            self.face_rectangle.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.birth_date is not None:
            result['BirthDate'] = self.birth_date
        result['CardAreas'] = []
        if self.card_areas is not None:
            for k in self.card_areas:
                result['CardAreas'].append(k.to_map() if k else None)
        result['FaceRectVertices'] = []
        if self.face_rect_vertices is not None:
            for k in self.face_rect_vertices:
                result['FaceRectVertices'].append(k.to_map() if k else None)
        if self.face_rectangle is not None:
            result['FaceRectangle'] = self.face_rectangle.to_map()
        if self.gender is not None:
            result['Gender'] = self.gender
        if self.idnumber is not None:
            result['IDNumber'] = self.idnumber
        if self.name is not None:
            result['Name'] = self.name
        if self.nationality is not None:
            result['Nationality'] = self.nationality
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('BirthDate') is not None:
            self.birth_date = m.get('BirthDate')
        self.card_areas = []
        if m.get('CardAreas') is not None:
            for k in m.get('CardAreas'):
                temp_model = RecognizeIdentityCardResponseBodyDataFrontResultCardAreas()
                self.card_areas.append(temp_model.from_map(k))
        self.face_rect_vertices = []
        if m.get('FaceRectVertices') is not None:
            for k in m.get('FaceRectVertices'):
                temp_model = RecognizeIdentityCardResponseBodyDataFrontResultFaceRectVertices()
                self.face_rect_vertices.append(temp_model.from_map(k))
        if m.get('FaceRectangle') is not None:
            temp_model = RecognizeIdentityCardResponseBodyDataFrontResultFaceRectangle()
            self.face_rectangle = temp_model.from_map(m['FaceRectangle'])
        if m.get('Gender') is not None:
            self.gender = m.get('Gender')
        if m.get('IDNumber') is not None:
            self.idnumber = m.get('IDNumber')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Nationality') is not None:
            self.nationality = m.get('Nationality')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        data: RecognizeIdentityCardResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = RecognizeIdentityCardResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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
            temp_model = RecognizeIdentityCardResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeLicensePlateRequest(TeaModel):
    def __init__(
        self,
        image_url: str = None,
    ):
        self.image_url = image_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        return self


class RecognizeLicensePlateAdvanceRequest(TeaModel):
    def __init__(
        self,
        image_urlobject: BinaryIO = None,
    ):
        self.image_urlobject = image_urlobject

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_urlobject is not None:
            result['ImageURLObject'] = self.image_urlobject
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURLObject') is not None:
            self.image_urlobject = m.get('ImageURLObject')
        return self


class RecognizeLicensePlateResponseBodyDataPlatesPositions(TeaModel):
    def __init__(
        self,
        x: int = None,
        y: int = None,
    ):
        self.x = x
        self.y = y

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        return self


class RecognizeLicensePlateResponseBodyDataPlatesRoi(TeaModel):
    def __init__(
        self,
        h: int = None,
        w: int = None,
        x: int = None,
        y: int = None,
    ):
        self.h = h
        self.w = w
        self.x = x
        self.y = y

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.h is not None:
            result['H'] = self.h
        if self.w is not None:
            result['W'] = self.w
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('H') is not None:
            self.h = m.get('H')
        if m.get('W') is not None:
            self.w = m.get('W')
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        return self


class RecognizeLicensePlateResponseBodyDataPlates(TeaModel):
    def __init__(
        self,
        confidence: float = None,
        plate_number: str = None,
        plate_type: str = None,
        plate_type_confidence: float = None,
        positions: List[RecognizeLicensePlateResponseBodyDataPlatesPositions] = None,
        roi: RecognizeLicensePlateResponseBodyDataPlatesRoi = None,
    ):
        self.confidence = confidence
        self.plate_number = plate_number
        self.plate_type = plate_type
        self.plate_type_confidence = plate_type_confidence
        self.positions = positions
        self.roi = roi

    def validate(self):
        if self.positions:
            for k in self.positions:
                if k:
                    k.validate()
        if self.roi:
            self.roi.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.confidence is not None:
            result['Confidence'] = self.confidence
        if self.plate_number is not None:
            result['PlateNumber'] = self.plate_number
        if self.plate_type is not None:
            result['PlateType'] = self.plate_type
        if self.plate_type_confidence is not None:
            result['PlateTypeConfidence'] = self.plate_type_confidence
        result['Positions'] = []
        if self.positions is not None:
            for k in self.positions:
                result['Positions'].append(k.to_map() if k else None)
        if self.roi is not None:
            result['Roi'] = self.roi.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')
        if m.get('PlateNumber') is not None:
            self.plate_number = m.get('PlateNumber')
        if m.get('PlateType') is not None:
            self.plate_type = m.get('PlateType')
        if m.get('PlateTypeConfidence') is not None:
            self.plate_type_confidence = m.get('PlateTypeConfidence')
        self.positions = []
        if m.get('Positions') is not None:
            for k in m.get('Positions'):
                temp_model = RecognizeLicensePlateResponseBodyDataPlatesPositions()
                self.positions.append(temp_model.from_map(k))
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        data: RecognizeLicensePlateResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = RecognizeLicensePlateResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        band_boxes: List[float] = None,
        content: str = None,
        detection_score: float = None,
        name: str = None,
        recognition_score: float = None,
    ):
        self.band_boxes = band_boxes
        self.content = content
        self.detection_score = detection_score
        self.name = name
        self.recognition_score = recognition_score

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.band_boxes is not None:
            result['BandBoxes'] = self.band_boxes
        if self.content is not None:
            result['Content'] = self.content
        if self.detection_score is not None:
            result['DetectionScore'] = self.detection_score
        if self.name is not None:
            result['Name'] = self.name
        if self.recognition_score is not None:
            result['RecognitionScore'] = self.recognition_score
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BandBoxes') is not None:
            self.band_boxes = m.get('BandBoxes')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('DetectionScore') is not None:
            self.detection_score = m.get('DetectionScore')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RecognitionScore') is not None:
            self.recognition_score = m.get('RecognitionScore')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        data: RecognizePassportMRZResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = RecognizePassportMRZResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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
            temp_model = RecognizePassportMRZResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizePdfRequest(TeaModel):
    def __init__(
        self,
        file_url: str = None,
    ):
        # A short description of struct
        self.file_url = file_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_url is not None:
            result['FileURL'] = self.file_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileURL') is not None:
            self.file_url = m.get('FileURL')
        return self


class RecognizePdfAdvanceRequest(TeaModel):
    def __init__(
        self,
        file_urlobject: BinaryIO = None,
    ):
        self.file_urlobject = file_urlobject

    def validate(self):
        self.validate_required(self.file_urlobject, 'file_urlobject')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_urlobject is not None:
            result['FileURLObject'] = self.file_urlobject
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileURLObject') is not None:
            self.file_urlobject = m.get('FileURLObject')
        return self


class RecognizePdfResponseBodyDataWordsInfoPositions(TeaModel):
    def __init__(
        self,
        x: int = None,
        y: int = None,
    ):
        self.x = x
        self.y = y

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        return self


class RecognizePdfResponseBodyDataWordsInfo(TeaModel):
    def __init__(
        self,
        angle: int = None,
        height: int = None,
        positions: List[RecognizePdfResponseBodyDataWordsInfoPositions] = None,
        width: int = None,
        word: str = None,
        x: int = None,
        y: int = None,
    ):
        self.angle = angle
        self.height = height
        self.positions = positions
        self.width = width
        self.word = word
        self.x = x
        self.y = y

    def validate(self):
        if self.positions:
            for k in self.positions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.angle is not None:
            result['Angle'] = self.angle
        if self.height is not None:
            result['Height'] = self.height
        result['Positions'] = []
        if self.positions is not None:
            for k in self.positions:
                result['Positions'].append(k.to_map() if k else None)
        if self.width is not None:
            result['Width'] = self.width
        if self.word is not None:
            result['Word'] = self.word
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Angle') is not None:
            self.angle = m.get('Angle')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        self.positions = []
        if m.get('Positions') is not None:
            for k in m.get('Positions'):
                temp_model = RecognizePdfResponseBodyDataWordsInfoPositions()
                self.positions.append(temp_model.from_map(k))
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Word') is not None:
            self.word = m.get('Word')
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        return self


class RecognizePdfResponseBodyData(TeaModel):
    def __init__(
        self,
        angle: int = None,
        height: int = None,
        org_height: int = None,
        org_width: int = None,
        page_index: int = None,
        width: int = None,
        words_info: List[RecognizePdfResponseBodyDataWordsInfo] = None,
    ):
        self.angle = angle
        self.height = height
        self.org_height = org_height
        self.org_width = org_width
        self.page_index = page_index
        self.width = width
        self.words_info = words_info

    def validate(self):
        if self.words_info:
            for k in self.words_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.angle is not None:
            result['Angle'] = self.angle
        if self.height is not None:
            result['Height'] = self.height
        if self.org_height is not None:
            result['OrgHeight'] = self.org_height
        if self.org_width is not None:
            result['OrgWidth'] = self.org_width
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.width is not None:
            result['Width'] = self.width
        result['WordsInfo'] = []
        if self.words_info is not None:
            for k in self.words_info:
                result['WordsInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Angle') is not None:
            self.angle = m.get('Angle')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('OrgHeight') is not None:
            self.org_height = m.get('OrgHeight')
        if m.get('OrgWidth') is not None:
            self.org_width = m.get('OrgWidth')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        self.words_info = []
        if m.get('WordsInfo') is not None:
            for k in m.get('WordsInfo'):
                temp_model = RecognizePdfResponseBodyDataWordsInfo()
                self.words_info.append(temp_model.from_map(k))
        return self


class RecognizePdfResponseBody(TeaModel):
    def __init__(
        self,
        data: RecognizePdfResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = RecognizePdfResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RecognizePdfResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RecognizePdfResponseBody = None,
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
            temp_model = RecognizePdfResponseBody()
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_urlobject is not None:
            result['ImageURLObject'] = self.image_urlobject
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURLObject') is not None:
            self.image_urlobject = m.get('ImageURLObject')
        return self


class RecognizePoiNameResponseBodyDataSignboardsTexts(TeaModel):
    def __init__(
        self,
        label: str = None,
        points: List[int] = None,
        score: float = None,
        tag: str = None,
        type: str = None,
    ):
        self.label = label
        self.points = points
        self.score = score
        self.tag = tag
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label is not None:
            result['Label'] = self.label
        if self.points is not None:
            result['Points'] = self.points
        if self.score is not None:
            result['Score'] = self.score
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Points') is not None:
            self.points = m.get('Points')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('Type') is not None:
            self.type = m.get('Type')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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


class RecognizePoiNameResponseBodyData(TeaModel):
    def __init__(
        self,
        signboards: List[RecognizePoiNameResponseBodyDataSignboards] = None,
        summary: RecognizePoiNameResponseBodyDataSummary = None,
    ):
        self.signboards = signboards
        self.summary = summary

    def validate(self):
        if self.signboards:
            for k in self.signboards:
                if k:
                    k.validate()
        if self.summary:
            self.summary.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Signboards'] = []
        if self.signboards is not None:
            for k in self.signboards:
                result['Signboards'].append(k.to_map() if k else None)
        if self.summary is not None:
            result['Summary'] = self.summary.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.signboards = []
        if m.get('Signboards') is not None:
            for k in m.get('Signboards'):
                temp_model = RecognizePoiNameResponseBodyDataSignboards()
                self.signboards.append(temp_model.from_map(k))
        if m.get('Summary') is not None:
            temp_model = RecognizePoiNameResponseBodyDataSummary()
            self.summary = temp_model.from_map(m['Summary'])
        return self


class RecognizePoiNameResponseBody(TeaModel):
    def __init__(
        self,
        data: RecognizePoiNameResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = RecognizePoiNameResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        label: str = None,
        qr_codes_data: List[str] = None,
        rate: float = None,
        suggestion: str = None,
    ):
        self.label = label
        self.qr_codes_data = qr_codes_data
        self.rate = rate
        self.suggestion = suggestion

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label is not None:
            result['Label'] = self.label
        if self.qr_codes_data is not None:
            result['QrCodesData'] = self.qr_codes_data
        if self.rate is not None:
            result['Rate'] = self.rate
        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('QrCodesData') is not None:
            self.qr_codes_data = m.get('QrCodesData')
        if m.get('Rate') is not None:
            self.rate = m.get('Rate')
        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')
        return self


class RecognizeQrCodeResponseBodyDataElements(TeaModel):
    def __init__(
        self,
        image_url: str = None,
        results: List[RecognizeQrCodeResponseBodyDataElementsResults] = None,
        task_id: str = None,
    ):
        self.image_url = image_url
        self.results = results
        self.task_id = task_id

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        self.results = []
        if m.get('Results') is not None:
            for k in m.get('Results'):
                temp_model = RecognizeQrCodeResponseBodyDataElementsResults()
                self.results.append(temp_model.from_map(k))
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        data: RecognizeQrCodeResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = RecognizeQrCodeResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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
            temp_model = RecognizeQrCodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeQuotaInvoiceRequest(TeaModel):
    def __init__(
        self,
        image_url: str = None,
    ):
        self.image_url = image_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        return self


class RecognizeQuotaInvoiceAdvanceRequest(TeaModel):
    def __init__(
        self,
        image_urlobject: BinaryIO = None,
    ):
        self.image_urlobject = image_urlobject

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_urlobject is not None:
            result['ImageURLObject'] = self.image_urlobject
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURLObject') is not None:
            self.image_urlobject = m.get('ImageURLObject')
        return self


class RecognizeQuotaInvoiceResponseBodyDataContent(TeaModel):
    def __init__(
        self,
        invoice_amount: str = None,
        invoice_code: str = None,
        invoice_details: str = None,
        invoice_no: str = None,
        sum_amount: str = None,
    ):
        self.invoice_amount = invoice_amount
        self.invoice_code = invoice_code
        self.invoice_details = invoice_details
        self.invoice_no = invoice_no
        self.sum_amount = sum_amount

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.invoice_amount is not None:
            result['InvoiceAmount'] = self.invoice_amount
        if self.invoice_code is not None:
            result['InvoiceCode'] = self.invoice_code
        if self.invoice_details is not None:
            result['InvoiceDetails'] = self.invoice_details
        if self.invoice_no is not None:
            result['InvoiceNo'] = self.invoice_no
        if self.sum_amount is not None:
            result['SumAmount'] = self.sum_amount
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InvoiceAmount') is not None:
            self.invoice_amount = m.get('InvoiceAmount')
        if m.get('InvoiceCode') is not None:
            self.invoice_code = m.get('InvoiceCode')
        if m.get('InvoiceDetails') is not None:
            self.invoice_details = m.get('InvoiceDetails')
        if m.get('InvoiceNo') is not None:
            self.invoice_no = m.get('InvoiceNo')
        if m.get('SumAmount') is not None:
            self.sum_amount = m.get('SumAmount')
        return self


class RecognizeQuotaInvoiceResponseBodyDataKeyValueInfosValuePositions(TeaModel):
    def __init__(
        self,
        x: int = None,
        y: int = None,
    ):
        self.x = x
        self.y = y

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        return self


class RecognizeQuotaInvoiceResponseBodyDataKeyValueInfos(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
        value_positions: List[RecognizeQuotaInvoiceResponseBodyDataKeyValueInfosValuePositions] = None,
        value_score: float = None,
    ):
        self.key = key
        self.value = value
        self.value_positions = value_positions
        self.value_score = value_score

    def validate(self):
        if self.value_positions:
            for k in self.value_positions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        result['ValuePositions'] = []
        if self.value_positions is not None:
            for k in self.value_positions:
                result['ValuePositions'].append(k.to_map() if k else None)
        if self.value_score is not None:
            result['ValueScore'] = self.value_score
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        self.value_positions = []
        if m.get('ValuePositions') is not None:
            for k in m.get('ValuePositions'):
                temp_model = RecognizeQuotaInvoiceResponseBodyDataKeyValueInfosValuePositions()
                self.value_positions.append(temp_model.from_map(k))
        if m.get('ValueScore') is not None:
            self.value_score = m.get('ValueScore')
        return self


class RecognizeQuotaInvoiceResponseBodyData(TeaModel):
    def __init__(
        self,
        angle: int = None,
        content: RecognizeQuotaInvoiceResponseBodyDataContent = None,
        height: int = None,
        key_value_infos: List[RecognizeQuotaInvoiceResponseBodyDataKeyValueInfos] = None,
        org_height: int = None,
        org_width: int = None,
        width: int = None,
    ):
        self.angle = angle
        self.content = content
        self.height = height
        self.key_value_infos = key_value_infos
        self.org_height = org_height
        self.org_width = org_width
        self.width = width

    def validate(self):
        if self.content:
            self.content.validate()
        if self.key_value_infos:
            for k in self.key_value_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.angle is not None:
            result['Angle'] = self.angle
        if self.content is not None:
            result['Content'] = self.content.to_map()
        if self.height is not None:
            result['Height'] = self.height
        result['KeyValueInfos'] = []
        if self.key_value_infos is not None:
            for k in self.key_value_infos:
                result['KeyValueInfos'].append(k.to_map() if k else None)
        if self.org_height is not None:
            result['OrgHeight'] = self.org_height
        if self.org_width is not None:
            result['OrgWidth'] = self.org_width
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Angle') is not None:
            self.angle = m.get('Angle')
        if m.get('Content') is not None:
            temp_model = RecognizeQuotaInvoiceResponseBodyDataContent()
            self.content = temp_model.from_map(m['Content'])
        if m.get('Height') is not None:
            self.height = m.get('Height')
        self.key_value_infos = []
        if m.get('KeyValueInfos') is not None:
            for k in m.get('KeyValueInfos'):
                temp_model = RecognizeQuotaInvoiceResponseBodyDataKeyValueInfos()
                self.key_value_infos.append(temp_model.from_map(k))
        if m.get('OrgHeight') is not None:
            self.org_height = m.get('OrgHeight')
        if m.get('OrgWidth') is not None:
            self.org_width = m.get('OrgWidth')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class RecognizeQuotaInvoiceResponseBody(TeaModel):
    def __init__(
        self,
        data: RecognizeQuotaInvoiceResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = RecognizeQuotaInvoiceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RecognizeQuotaInvoiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RecognizeQuotaInvoiceResponseBody = None,
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
            temp_model = RecognizeQuotaInvoiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeStampRequest(TeaModel):
    def __init__(
        self,
        image_url: str = None,
    ):
        self.image_url = image_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        return self


class RecognizeStampAdvanceRequest(TeaModel):
    def __init__(
        self,
        image_urlobject: BinaryIO = None,
    ):
        self.image_urlobject = image_urlobject

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_urlobject is not None:
            result['ImageURLObject'] = self.image_urlobject
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURLObject') is not None:
            self.image_urlobject = m.get('ImageURLObject')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        height: int = None,
        left: int = None,
        top: int = None,
        width: int = None,
    ):
        self.height = height
        self.left = left
        self.top = top
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.height is not None:
            result['Height'] = self.height
        if self.left is not None:
            result['Left'] = self.left
        if self.top is not None:
            result['Top'] = self.top
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Left') is not None:
            self.left = m.get('Left')
        if m.get('Top') is not None:
            self.top = m.get('Top')
        if m.get('Width') is not None:
            self.width = m.get('Width')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        general_text: List[RecognizeStampResponseBodyDataResultsGeneralText] = None,
        roi: RecognizeStampResponseBodyDataResultsRoi = None,
        text: RecognizeStampResponseBodyDataResultsText = None,
    ):
        self.general_text = general_text
        self.roi = roi
        self.text = text

    def validate(self):
        if self.general_text:
            for k in self.general_text:
                if k:
                    k.validate()
        if self.roi:
            self.roi.validate()
        if self.text:
            self.text.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['GeneralText'] = []
        if self.general_text is not None:
            for k in self.general_text:
                result['GeneralText'].append(k.to_map() if k else None)
        if self.roi is not None:
            result['Roi'] = self.roi.to_map()
        if self.text is not None:
            result['Text'] = self.text.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.general_text = []
        if m.get('GeneralText') is not None:
            for k in m.get('GeneralText'):
                temp_model = RecognizeStampResponseBodyDataResultsGeneralText()
                self.general_text.append(temp_model.from_map(k))
        if m.get('Roi') is not None:
            temp_model = RecognizeStampResponseBodyDataResultsRoi()
            self.roi = temp_model.from_map(m['Roi'])
        if m.get('Text') is not None:
            temp_model = RecognizeStampResponseBodyDataResultsText()
            self.text = temp_model.from_map(m['Text'])
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        data: RecognizeStampResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = RecognizeStampResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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
            temp_model = RecognizeStampResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeStructuredTaxiInvoicesRequest(TeaModel):
    def __init__(
        self,
        image_url: str = None,
    ):
        self.image_url = image_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        return self


class RecognizeStructuredTaxiInvoicesAdvanceRequest(TeaModel):
    def __init__(
        self,
        image_urlobject: BinaryIO = None,
    ):
        self.image_urlobject = image_urlobject

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_urlobject is not None:
            result['ImageURLObject'] = self.image_urlobject
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURLObject') is not None:
            self.image_urlobject = m.get('ImageURLObject')
        return self


class RecognizeStructuredTaxiInvoicesResponseBodyData(TeaModel):
    def __init__(
        self,
        addresses: List[str] = None,
        cell_phone_numbers: List[str] = None,
        companies: List[str] = None,
        departments: List[str] = None,
        emails: List[str] = None,
        name: str = None,
        office_phone_numbers: List[str] = None,
        titles: List[str] = None,
    ):
        self.addresses = addresses
        self.cell_phone_numbers = cell_phone_numbers
        self.companies = companies
        self.departments = departments
        self.emails = emails
        self.name = name
        self.office_phone_numbers = office_phone_numbers
        self.titles = titles

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.addresses is not None:
            result['Addresses'] = self.addresses
        if self.cell_phone_numbers is not None:
            result['CellPhoneNumbers'] = self.cell_phone_numbers
        if self.companies is not None:
            result['Companies'] = self.companies
        if self.departments is not None:
            result['Departments'] = self.departments
        if self.emails is not None:
            result['Emails'] = self.emails
        if self.name is not None:
            result['Name'] = self.name
        if self.office_phone_numbers is not None:
            result['OfficePhoneNumbers'] = self.office_phone_numbers
        if self.titles is not None:
            result['Titles'] = self.titles
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Addresses') is not None:
            self.addresses = m.get('Addresses')
        if m.get('CellPhoneNumbers') is not None:
            self.cell_phone_numbers = m.get('CellPhoneNumbers')
        if m.get('Companies') is not None:
            self.companies = m.get('Companies')
        if m.get('Departments') is not None:
            self.departments = m.get('Departments')
        if m.get('Emails') is not None:
            self.emails = m.get('Emails')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OfficePhoneNumbers') is not None:
            self.office_phone_numbers = m.get('OfficePhoneNumbers')
        if m.get('Titles') is not None:
            self.titles = m.get('Titles')
        return self


class RecognizeStructuredTaxiInvoicesResponseBody(TeaModel):
    def __init__(
        self,
        data: RecognizeStructuredTaxiInvoicesResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = RecognizeStructuredTaxiInvoicesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RecognizeStructuredTaxiInvoicesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RecognizeStructuredTaxiInvoicesResponseBody = None,
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
            temp_model = RecognizeStructuredTaxiInvoicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeTableRequest(TeaModel):
    def __init__(
        self,
        assure_direction: bool = None,
        has_line: bool = None,
        image_url: str = None,
        output_format: str = None,
        skip_detection: bool = None,
        use_finance_model: bool = None,
    ):
        self.assure_direction = assure_direction
        self.has_line = has_line
        self.image_url = image_url
        self.output_format = output_format
        self.skip_detection = skip_detection
        self.use_finance_model = use_finance_model

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.assure_direction is not None:
            result['AssureDirection'] = self.assure_direction
        if self.has_line is not None:
            result['HasLine'] = self.has_line
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        if self.output_format is not None:
            result['OutputFormat'] = self.output_format
        if self.skip_detection is not None:
            result['SkipDetection'] = self.skip_detection
        if self.use_finance_model is not None:
            result['UseFinanceModel'] = self.use_finance_model
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssureDirection') is not None:
            self.assure_direction = m.get('AssureDirection')
        if m.get('HasLine') is not None:
            self.has_line = m.get('HasLine')
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        if m.get('OutputFormat') is not None:
            self.output_format = m.get('OutputFormat')
        if m.get('SkipDetection') is not None:
            self.skip_detection = m.get('SkipDetection')
        if m.get('UseFinanceModel') is not None:
            self.use_finance_model = m.get('UseFinanceModel')
        return self


class RecognizeTableAdvanceRequest(TeaModel):
    def __init__(
        self,
        image_urlobject: BinaryIO = None,
        assure_direction: bool = None,
        has_line: bool = None,
        output_format: str = None,
        skip_detection: bool = None,
        use_finance_model: bool = None,
    ):
        self.image_urlobject = image_urlobject
        self.assure_direction = assure_direction
        self.has_line = has_line
        self.output_format = output_format
        self.skip_detection = skip_detection
        self.use_finance_model = use_finance_model

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_urlobject is not None:
            result['ImageURLObject'] = self.image_urlobject
        if self.assure_direction is not None:
            result['AssureDirection'] = self.assure_direction
        if self.has_line is not None:
            result['HasLine'] = self.has_line
        if self.output_format is not None:
            result['OutputFormat'] = self.output_format
        if self.skip_detection is not None:
            result['SkipDetection'] = self.skip_detection
        if self.use_finance_model is not None:
            result['UseFinanceModel'] = self.use_finance_model
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURLObject') is not None:
            self.image_urlobject = m.get('ImageURLObject')
        if m.get('AssureDirection') is not None:
            self.assure_direction = m.get('AssureDirection')
        if m.get('HasLine') is not None:
            self.has_line = m.get('HasLine')
        if m.get('OutputFormat') is not None:
            self.output_format = m.get('OutputFormat')
        if m.get('SkipDetection') is not None:
            self.skip_detection = m.get('SkipDetection')
        if m.get('UseFinanceModel') is not None:
            self.use_finance_model = m.get('UseFinanceModel')
        return self


class RecognizeTableResponseBodyDataTablesTableRowsTableColumns(TeaModel):
    def __init__(
        self,
        end_column: int = None,
        end_row: int = None,
        height: int = None,
        start_column: int = None,
        start_row: int = None,
        texts: List[str] = None,
        width: int = None,
    ):
        self.end_column = end_column
        self.end_row = end_row
        self.height = height
        self.start_column = start_column
        self.start_row = start_row
        self.texts = texts
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_column is not None:
            result['EndColumn'] = self.end_column
        if self.end_row is not None:
            result['EndRow'] = self.end_row
        if self.height is not None:
            result['Height'] = self.height
        if self.start_column is not None:
            result['StartColumn'] = self.start_column
        if self.start_row is not None:
            result['StartRow'] = self.start_row
        if self.texts is not None:
            result['Texts'] = self.texts
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndColumn') is not None:
            self.end_column = m.get('EndColumn')
        if m.get('EndRow') is not None:
            self.end_row = m.get('EndRow')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('StartColumn') is not None:
            self.start_column = m.get('StartColumn')
        if m.get('StartRow') is not None:
            self.start_row = m.get('StartRow')
        if m.get('Texts') is not None:
            self.texts = m.get('Texts')
        if m.get('Width') is not None:
            self.width = m.get('Width')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        table_rows: List[RecognizeTableResponseBodyDataTablesTableRows] = None,
        tail: List[str] = None,
    ):
        self.head = head
        self.table_rows = table_rows
        self.tail = tail

    def validate(self):
        if self.table_rows:
            for k in self.table_rows:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.head is not None:
            result['Head'] = self.head
        result['TableRows'] = []
        if self.table_rows is not None:
            for k in self.table_rows:
                result['TableRows'].append(k.to_map() if k else None)
        if self.tail is not None:
            result['Tail'] = self.tail
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Head') is not None:
            self.head = m.get('Head')
        self.table_rows = []
        if m.get('TableRows') is not None:
            for k in m.get('TableRows'):
                temp_model = RecognizeTableResponseBodyDataTablesTableRows()
                self.table_rows.append(temp_model.from_map(k))
        if m.get('Tail') is not None:
            self.tail = m.get('Tail')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        data: RecognizeTableResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = RecognizeTableResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        boxes: List[int] = None,
        name: str = None,
        score: float = None,
        value: str = None,
    ):
        self.boxes = boxes
        self.name = name
        self.score = score
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.boxes is not None:
            result['Boxes'] = self.boxes
        if self.name is not None:
            result['Name'] = self.name
        if self.score is not None:
            result['Score'] = self.score
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Boxes') is not None:
            self.boxes = m.get('Boxes')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('Value') is not None:
            self.value = m.get('Value')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        data: RecognizeTakeoutOrderResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = RecognizeTakeoutOrderResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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
            temp_model = RecognizeTakeoutOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeTaxiInvoiceRequest(TeaModel):
    def __init__(
        self,
        image_url: str = None,
    ):
        self.image_url = image_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        return self


class RecognizeTaxiInvoiceAdvanceRequest(TeaModel):
    def __init__(
        self,
        image_urlobject: BinaryIO = None,
    ):
        self.image_urlobject = image_urlobject

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_urlobject is not None:
            result['ImageURLObject'] = self.image_urlobject
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURLObject') is not None:
            self.image_urlobject = m.get('ImageURLObject')
        return self


class RecognizeTaxiInvoiceResponseBodyDataInvoicesInvoiceRoi(TeaModel):
    def __init__(
        self,
        h: float = None,
        w: float = None,
        x: float = None,
        y: float = None,
    ):
        self.h = h
        self.w = w
        self.x = x
        self.y = y

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.h is not None:
            result['H'] = self.h
        if self.w is not None:
            result['W'] = self.w
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('H') is not None:
            self.h = m.get('H')
        if m.get('W') is not None:
            self.w = m.get('W')
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        return self


class RecognizeTaxiInvoiceResponseBodyDataInvoicesItemsItemRoiCenter(TeaModel):
    def __init__(
        self,
        x: float = None,
        y: float = None,
    ):
        self.x = x
        self.y = y

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        return self


class RecognizeTaxiInvoiceResponseBodyDataInvoicesItemsItemRoiSize(TeaModel):
    def __init__(
        self,
        h: float = None,
        w: float = None,
    ):
        self.h = h
        self.w = w

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.h is not None:
            result['H'] = self.h
        if self.w is not None:
            result['W'] = self.w
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('H') is not None:
            self.h = m.get('H')
        if m.get('W') is not None:
            self.w = m.get('W')
        return self


class RecognizeTaxiInvoiceResponseBodyDataInvoicesItemsItemRoi(TeaModel):
    def __init__(
        self,
        angle: float = None,
        center: RecognizeTaxiInvoiceResponseBodyDataInvoicesItemsItemRoiCenter = None,
        size: RecognizeTaxiInvoiceResponseBodyDataInvoicesItemsItemRoiSize = None,
    ):
        self.angle = angle
        self.center = center
        self.size = size

    def validate(self):
        if self.center:
            self.center.validate()
        if self.size:
            self.size.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.angle is not None:
            result['Angle'] = self.angle
        if self.center is not None:
            result['Center'] = self.center.to_map()
        if self.size is not None:
            result['Size'] = self.size.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Angle') is not None:
            self.angle = m.get('Angle')
        if m.get('Center') is not None:
            temp_model = RecognizeTaxiInvoiceResponseBodyDataInvoicesItemsItemRoiCenter()
            self.center = temp_model.from_map(m['Center'])
        if m.get('Size') is not None:
            temp_model = RecognizeTaxiInvoiceResponseBodyDataInvoicesItemsItemRoiSize()
            self.size = temp_model.from_map(m['Size'])
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
        _map = super().to_map()
        if _map is not None:
            return _map

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


class RecognizeTaxiInvoiceResponseBodyDataInvoices(TeaModel):
    def __init__(
        self,
        invoice_roi: RecognizeTaxiInvoiceResponseBodyDataInvoicesInvoiceRoi = None,
        items: List[RecognizeTaxiInvoiceResponseBodyDataInvoicesItems] = None,
        rotate_type: int = None,
    ):
        self.invoice_roi = invoice_roi
        self.items = items
        self.rotate_type = rotate_type

    def validate(self):
        if self.invoice_roi:
            self.invoice_roi.validate()
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.invoice_roi is not None:
            result['InvoiceRoi'] = self.invoice_roi.to_map()
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.rotate_type is not None:
            result['RotateType'] = self.rotate_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InvoiceRoi') is not None:
            temp_model = RecognizeTaxiInvoiceResponseBodyDataInvoicesInvoiceRoi()
            self.invoice_roi = temp_model.from_map(m['InvoiceRoi'])
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = RecognizeTaxiInvoiceResponseBodyDataInvoicesItems()
                self.items.append(temp_model.from_map(k))
        if m.get('RotateType') is not None:
            self.rotate_type = m.get('RotateType')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        data: RecognizeTaxiInvoiceResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = RecognizeTaxiInvoiceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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
            temp_model = RecognizeTaxiInvoiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeTicketInvoiceRequest(TeaModel):
    def __init__(
        self,
        image_url: str = None,
    ):
        # A short description of struct
        self.image_url = image_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        return self


class RecognizeTicketInvoiceAdvanceRequest(TeaModel):
    def __init__(
        self,
        image_urlobject: BinaryIO = None,
    ):
        self.image_urlobject = image_urlobject

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_urlobject is not None:
            result['ImageURLObject'] = self.image_urlobject
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURLObject') is not None:
            self.image_urlobject = m.get('ImageURLObject')
        return self


class RecognizeTicketInvoiceResponseBodyDataResultsContent(TeaModel):
    def __init__(
        self,
        anti_fake_code: str = None,
        invoice_code: str = None,
        invoice_date: str = None,
        invoice_number: str = None,
        payee_name: str = None,
        payee_register_no: str = None,
        payer_name: str = None,
        payer_register_no: str = None,
        sum_amount: str = None,
    ):
        self.anti_fake_code = anti_fake_code
        self.invoice_code = invoice_code
        self.invoice_date = invoice_date
        self.invoice_number = invoice_number
        self.payee_name = payee_name
        self.payee_register_no = payee_register_no
        self.payer_name = payer_name
        self.payer_register_no = payer_register_no
        self.sum_amount = sum_amount

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.anti_fake_code is not None:
            result['AntiFakeCode'] = self.anti_fake_code
        if self.invoice_code is not None:
            result['InvoiceCode'] = self.invoice_code
        if self.invoice_date is not None:
            result['InvoiceDate'] = self.invoice_date
        if self.invoice_number is not None:
            result['InvoiceNumber'] = self.invoice_number
        if self.payee_name is not None:
            result['PayeeName'] = self.payee_name
        if self.payee_register_no is not None:
            result['PayeeRegisterNo'] = self.payee_register_no
        if self.payer_name is not None:
            result['PayerName'] = self.payer_name
        if self.payer_register_no is not None:
            result['PayerRegisterNo'] = self.payer_register_no
        if self.sum_amount is not None:
            result['SumAmount'] = self.sum_amount
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AntiFakeCode') is not None:
            self.anti_fake_code = m.get('AntiFakeCode')
        if m.get('InvoiceCode') is not None:
            self.invoice_code = m.get('InvoiceCode')
        if m.get('InvoiceDate') is not None:
            self.invoice_date = m.get('InvoiceDate')
        if m.get('InvoiceNumber') is not None:
            self.invoice_number = m.get('InvoiceNumber')
        if m.get('PayeeName') is not None:
            self.payee_name = m.get('PayeeName')
        if m.get('PayeeRegisterNo') is not None:
            self.payee_register_no = m.get('PayeeRegisterNo')
        if m.get('PayerName') is not None:
            self.payer_name = m.get('PayerName')
        if m.get('PayerRegisterNo') is not None:
            self.payer_register_no = m.get('PayerRegisterNo')
        if m.get('SumAmount') is not None:
            self.sum_amount = m.get('SumAmount')
        return self


class RecognizeTicketInvoiceResponseBodyDataResultsKeyValueInfosValuePositions(TeaModel):
    def __init__(
        self,
        x: int = None,
        y: int = None,
    ):
        self.x = x
        self.y = y

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        return self


class RecognizeTicketInvoiceResponseBodyDataResultsKeyValueInfos(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
        value_positions: List[RecognizeTicketInvoiceResponseBodyDataResultsKeyValueInfosValuePositions] = None,
        value_score: float = None,
    ):
        self.key = key
        self.value = value
        self.value_positions = value_positions
        self.value_score = value_score

    def validate(self):
        if self.value_positions:
            for k in self.value_positions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        result['ValuePositions'] = []
        if self.value_positions is not None:
            for k in self.value_positions:
                result['ValuePositions'].append(k.to_map() if k else None)
        if self.value_score is not None:
            result['ValueScore'] = self.value_score
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        self.value_positions = []
        if m.get('ValuePositions') is not None:
            for k in m.get('ValuePositions'):
                temp_model = RecognizeTicketInvoiceResponseBodyDataResultsKeyValueInfosValuePositions()
                self.value_positions.append(temp_model.from_map(k))
        if m.get('ValueScore') is not None:
            self.value_score = m.get('ValueScore')
        return self


class RecognizeTicketInvoiceResponseBodyDataResultsSliceRectangle(TeaModel):
    def __init__(
        self,
        x: int = None,
        y: int = None,
    ):
        self.x = x
        self.y = y

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        return self


class RecognizeTicketInvoiceResponseBodyDataResults(TeaModel):
    def __init__(
        self,
        content: RecognizeTicketInvoiceResponseBodyDataResultsContent = None,
        index: int = None,
        key_value_infos: List[RecognizeTicketInvoiceResponseBodyDataResultsKeyValueInfos] = None,
        slice_rectangle: List[RecognizeTicketInvoiceResponseBodyDataResultsSliceRectangle] = None,
        type: str = None,
    ):
        self.content = content
        self.index = index
        self.key_value_infos = key_value_infos
        self.slice_rectangle = slice_rectangle
        self.type = type

    def validate(self):
        if self.content:
            self.content.validate()
        if self.key_value_infos:
            for k in self.key_value_infos:
                if k:
                    k.validate()
        if self.slice_rectangle:
            for k in self.slice_rectangle:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content.to_map()
        if self.index is not None:
            result['Index'] = self.index
        result['KeyValueInfos'] = []
        if self.key_value_infos is not None:
            for k in self.key_value_infos:
                result['KeyValueInfos'].append(k.to_map() if k else None)
        result['SliceRectangle'] = []
        if self.slice_rectangle is not None:
            for k in self.slice_rectangle:
                result['SliceRectangle'].append(k.to_map() if k else None)
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            temp_model = RecognizeTicketInvoiceResponseBodyDataResultsContent()
            self.content = temp_model.from_map(m['Content'])
        if m.get('Index') is not None:
            self.index = m.get('Index')
        self.key_value_infos = []
        if m.get('KeyValueInfos') is not None:
            for k in m.get('KeyValueInfos'):
                temp_model = RecognizeTicketInvoiceResponseBodyDataResultsKeyValueInfos()
                self.key_value_infos.append(temp_model.from_map(k))
        self.slice_rectangle = []
        if m.get('SliceRectangle') is not None:
            for k in m.get('SliceRectangle'):
                temp_model = RecognizeTicketInvoiceResponseBodyDataResultsSliceRectangle()
                self.slice_rectangle.append(temp_model.from_map(k))
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class RecognizeTicketInvoiceResponseBodyData(TeaModel):
    def __init__(
        self,
        count: int = None,
        height: int = None,
        org_height: int = None,
        org_width: int = None,
        results: List[RecognizeTicketInvoiceResponseBodyDataResults] = None,
        width: int = None,
    ):
        self.count = count
        self.height = height
        self.org_height = org_height
        self.org_width = org_width
        self.results = results
        self.width = width

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.height is not None:
            result['Height'] = self.height
        if self.org_height is not None:
            result['OrgHeight'] = self.org_height
        if self.org_width is not None:
            result['OrgWidth'] = self.org_width
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('OrgHeight') is not None:
            self.org_height = m.get('OrgHeight')
        if m.get('OrgWidth') is not None:
            self.org_width = m.get('OrgWidth')
        self.results = []
        if m.get('Results') is not None:
            for k in m.get('Results'):
                temp_model = RecognizeTicketInvoiceResponseBodyDataResults()
                self.results.append(temp_model.from_map(k))
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class RecognizeTicketInvoiceResponseBody(TeaModel):
    def __init__(
        self,
        data: RecognizeTicketInvoiceResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = RecognizeTicketInvoiceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RecognizeTicketInvoiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RecognizeTicketInvoiceResponseBody = None,
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
            temp_model = RecognizeTicketInvoiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeTrainTicketRequest(TeaModel):
    def __init__(
        self,
        image_url: str = None,
    ):
        self.image_url = image_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        return self


class RecognizeTrainTicketAdvanceRequest(TeaModel):
    def __init__(
        self,
        image_urlobject: BinaryIO = None,
    ):
        self.image_urlobject = image_urlobject

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_urlobject is not None:
            result['ImageURLObject'] = self.image_urlobject
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURLObject') is not None:
            self.image_urlobject = m.get('ImageURLObject')
        return self


class RecognizeTrainTicketResponseBodyData(TeaModel):
    def __init__(
        self,
        date: str = None,
        departure_station: str = None,
        destination: str = None,
        level: str = None,
        name: str = None,
        number: str = None,
        price: float = None,
        seat: str = None,
    ):
        self.date = date
        self.departure_station = departure_station
        self.destination = destination
        self.level = level
        self.name = name
        self.number = number
        self.price = price
        self.seat = seat

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.date is not None:
            result['Date'] = self.date
        if self.departure_station is not None:
            result['DepartureStation'] = self.departure_station
        if self.destination is not None:
            result['Destination'] = self.destination
        if self.level is not None:
            result['Level'] = self.level
        if self.name is not None:
            result['Name'] = self.name
        if self.number is not None:
            result['Number'] = self.number
        if self.price is not None:
            result['Price'] = self.price
        if self.seat is not None:
            result['Seat'] = self.seat
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Date') is not None:
            self.date = m.get('Date')
        if m.get('DepartureStation') is not None:
            self.departure_station = m.get('DepartureStation')
        if m.get('Destination') is not None:
            self.destination = m.get('Destination')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Number') is not None:
            self.number = m.get('Number')
        if m.get('Price') is not None:
            self.price = m.get('Price')
        if m.get('Seat') is not None:
            self.seat = m.get('Seat')
        return self


class RecognizeTrainTicketResponseBody(TeaModel):
    def __init__(
        self,
        data: RecognizeTrainTicketResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = RecognizeTrainTicketResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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
            temp_model = RecognizeTrainTicketResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeVATInvoiceRequest(TeaModel):
    def __init__(
        self,
        file_type: str = None,
        file_url: str = None,
    ):
        self.file_type = file_type
        self.file_url = file_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_type is not None:
            result['FileType'] = self.file_type
        if self.file_url is not None:
            result['FileURL'] = self.file_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')
        if m.get('FileURL') is not None:
            self.file_url = m.get('FileURL')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        checkers: List[float] = None,
        clerks: List[float] = None,
        invoice_amounts: List[float] = None,
        invoice_codes: List[float] = None,
        invoice_dates: List[float] = None,
        invoice_fake_codes: List[float] = None,
        invoice_noes: List[float] = None,
        payee_addresses: List[float] = None,
        payee_bank_names: List[float] = None,
        payee_names: List[float] = None,
        payee_register_noes: List[float] = None,
        payees: List[float] = None,
        payer_addresses: List[float] = None,
        payer_bank_names: List[float] = None,
        payer_names: List[float] = None,
        payer_register_noes: List[float] = None,
        sum_amounts: List[float] = None,
        tax_amounts: List[float] = None,
        without_tax_amounts: List[float] = None,
    ):
        self.checkers = checkers
        self.clerks = clerks
        self.invoice_amounts = invoice_amounts
        self.invoice_codes = invoice_codes
        self.invoice_dates = invoice_dates
        self.invoice_fake_codes = invoice_fake_codes
        self.invoice_noes = invoice_noes
        self.payee_addresses = payee_addresses
        self.payee_bank_names = payee_bank_names
        self.payee_names = payee_names
        self.payee_register_noes = payee_register_noes
        self.payees = payees
        self.payer_addresses = payer_addresses
        self.payer_bank_names = payer_bank_names
        self.payer_names = payer_names
        self.payer_register_noes = payer_register_noes
        self.sum_amounts = sum_amounts
        self.tax_amounts = tax_amounts
        self.without_tax_amounts = without_tax_amounts

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.checkers is not None:
            result['Checkers'] = self.checkers
        if self.clerks is not None:
            result['Clerks'] = self.clerks
        if self.invoice_amounts is not None:
            result['InvoiceAmounts'] = self.invoice_amounts
        if self.invoice_codes is not None:
            result['InvoiceCodes'] = self.invoice_codes
        if self.invoice_dates is not None:
            result['InvoiceDates'] = self.invoice_dates
        if self.invoice_fake_codes is not None:
            result['InvoiceFakeCodes'] = self.invoice_fake_codes
        if self.invoice_noes is not None:
            result['InvoiceNoes'] = self.invoice_noes
        if self.payee_addresses is not None:
            result['PayeeAddresses'] = self.payee_addresses
        if self.payee_bank_names is not None:
            result['PayeeBankNames'] = self.payee_bank_names
        if self.payee_names is not None:
            result['PayeeNames'] = self.payee_names
        if self.payee_register_noes is not None:
            result['PayeeRegisterNoes'] = self.payee_register_noes
        if self.payees is not None:
            result['Payees'] = self.payees
        if self.payer_addresses is not None:
            result['PayerAddresses'] = self.payer_addresses
        if self.payer_bank_names is not None:
            result['PayerBankNames'] = self.payer_bank_names
        if self.payer_names is not None:
            result['PayerNames'] = self.payer_names
        if self.payer_register_noes is not None:
            result['PayerRegisterNoes'] = self.payer_register_noes
        if self.sum_amounts is not None:
            result['SumAmounts'] = self.sum_amounts
        if self.tax_amounts is not None:
            result['TaxAmounts'] = self.tax_amounts
        if self.without_tax_amounts is not None:
            result['WithoutTaxAmounts'] = self.without_tax_amounts
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Checkers') is not None:
            self.checkers = m.get('Checkers')
        if m.get('Clerks') is not None:
            self.clerks = m.get('Clerks')
        if m.get('InvoiceAmounts') is not None:
            self.invoice_amounts = m.get('InvoiceAmounts')
        if m.get('InvoiceCodes') is not None:
            self.invoice_codes = m.get('InvoiceCodes')
        if m.get('InvoiceDates') is not None:
            self.invoice_dates = m.get('InvoiceDates')
        if m.get('InvoiceFakeCodes') is not None:
            self.invoice_fake_codes = m.get('InvoiceFakeCodes')
        if m.get('InvoiceNoes') is not None:
            self.invoice_noes = m.get('InvoiceNoes')
        if m.get('PayeeAddresses') is not None:
            self.payee_addresses = m.get('PayeeAddresses')
        if m.get('PayeeBankNames') is not None:
            self.payee_bank_names = m.get('PayeeBankNames')
        if m.get('PayeeNames') is not None:
            self.payee_names = m.get('PayeeNames')
        if m.get('PayeeRegisterNoes') is not None:
            self.payee_register_noes = m.get('PayeeRegisterNoes')
        if m.get('Payees') is not None:
            self.payees = m.get('Payees')
        if m.get('PayerAddresses') is not None:
            self.payer_addresses = m.get('PayerAddresses')
        if m.get('PayerBankNames') is not None:
            self.payer_bank_names = m.get('PayerBankNames')
        if m.get('PayerNames') is not None:
            self.payer_names = m.get('PayerNames')
        if m.get('PayerRegisterNoes') is not None:
            self.payer_register_noes = m.get('PayerRegisterNoes')
        if m.get('SumAmounts') is not None:
            self.sum_amounts = m.get('SumAmounts')
        if m.get('TaxAmounts') is not None:
            self.tax_amounts = m.get('TaxAmounts')
        if m.get('WithoutTaxAmounts') is not None:
            self.without_tax_amounts = m.get('WithoutTaxAmounts')
        return self


class RecognizeVATInvoiceResponseBodyDataContent(TeaModel):
    def __init__(
        self,
        anti_fake_code: str = None,
        checker: str = None,
        clerk: str = None,
        invoice_amount: str = None,
        invoice_code: str = None,
        invoice_date: str = None,
        invoice_no: str = None,
        payee: str = None,
        payee_address: str = None,
        payee_bank_name: str = None,
        payee_name: str = None,
        payee_register_no: str = None,
        payer_address: str = None,
        payer_bank_name: str = None,
        payer_name: str = None,
        payer_register_no: str = None,
        sum_amount: str = None,
        tax_amount: str = None,
        without_tax_amount: str = None,
    ):
        self.anti_fake_code = anti_fake_code
        self.checker = checker
        self.clerk = clerk
        self.invoice_amount = invoice_amount
        self.invoice_code = invoice_code
        self.invoice_date = invoice_date
        self.invoice_no = invoice_no
        self.payee = payee
        self.payee_address = payee_address
        self.payee_bank_name = payee_bank_name
        self.payee_name = payee_name
        self.payee_register_no = payee_register_no
        self.payer_address = payer_address
        self.payer_bank_name = payer_bank_name
        self.payer_name = payer_name
        self.payer_register_no = payer_register_no
        self.sum_amount = sum_amount
        self.tax_amount = tax_amount
        self.without_tax_amount = without_tax_amount

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.anti_fake_code is not None:
            result['AntiFakeCode'] = self.anti_fake_code
        if self.checker is not None:
            result['Checker'] = self.checker
        if self.clerk is not None:
            result['Clerk'] = self.clerk
        if self.invoice_amount is not None:
            result['InvoiceAmount'] = self.invoice_amount
        if self.invoice_code is not None:
            result['InvoiceCode'] = self.invoice_code
        if self.invoice_date is not None:
            result['InvoiceDate'] = self.invoice_date
        if self.invoice_no is not None:
            result['InvoiceNo'] = self.invoice_no
        if self.payee is not None:
            result['Payee'] = self.payee
        if self.payee_address is not None:
            result['PayeeAddress'] = self.payee_address
        if self.payee_bank_name is not None:
            result['PayeeBankName'] = self.payee_bank_name
        if self.payee_name is not None:
            result['PayeeName'] = self.payee_name
        if self.payee_register_no is not None:
            result['PayeeRegisterNo'] = self.payee_register_no
        if self.payer_address is not None:
            result['PayerAddress'] = self.payer_address
        if self.payer_bank_name is not None:
            result['PayerBankName'] = self.payer_bank_name
        if self.payer_name is not None:
            result['PayerName'] = self.payer_name
        if self.payer_register_no is not None:
            result['PayerRegisterNo'] = self.payer_register_no
        if self.sum_amount is not None:
            result['SumAmount'] = self.sum_amount
        if self.tax_amount is not None:
            result['TaxAmount'] = self.tax_amount
        if self.without_tax_amount is not None:
            result['WithoutTaxAmount'] = self.without_tax_amount
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AntiFakeCode') is not None:
            self.anti_fake_code = m.get('AntiFakeCode')
        if m.get('Checker') is not None:
            self.checker = m.get('Checker')
        if m.get('Clerk') is not None:
            self.clerk = m.get('Clerk')
        if m.get('InvoiceAmount') is not None:
            self.invoice_amount = m.get('InvoiceAmount')
        if m.get('InvoiceCode') is not None:
            self.invoice_code = m.get('InvoiceCode')
        if m.get('InvoiceDate') is not None:
            self.invoice_date = m.get('InvoiceDate')
        if m.get('InvoiceNo') is not None:
            self.invoice_no = m.get('InvoiceNo')
        if m.get('Payee') is not None:
            self.payee = m.get('Payee')
        if m.get('PayeeAddress') is not None:
            self.payee_address = m.get('PayeeAddress')
        if m.get('PayeeBankName') is not None:
            self.payee_bank_name = m.get('PayeeBankName')
        if m.get('PayeeName') is not None:
            self.payee_name = m.get('PayeeName')
        if m.get('PayeeRegisterNo') is not None:
            self.payee_register_no = m.get('PayeeRegisterNo')
        if m.get('PayerAddress') is not None:
            self.payer_address = m.get('PayerAddress')
        if m.get('PayerBankName') is not None:
            self.payer_bank_name = m.get('PayerBankName')
        if m.get('PayerName') is not None:
            self.payer_name = m.get('PayerName')
        if m.get('PayerRegisterNo') is not None:
            self.payer_register_no = m.get('PayerRegisterNo')
        if m.get('SumAmount') is not None:
            self.sum_amount = m.get('SumAmount')
        if m.get('TaxAmount') is not None:
            self.tax_amount = m.get('TaxAmount')
        if m.get('WithoutTaxAmount') is not None:
            self.without_tax_amount = m.get('WithoutTaxAmount')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        data: RecognizeVATInvoiceResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = RecognizeVATInvoiceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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
            temp_model = RecognizeVATInvoiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeVINCodeRequest(TeaModel):
    def __init__(
        self,
        image_url: str = None,
    ):
        self.image_url = image_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        return self


class RecognizeVINCodeAdvanceRequest(TeaModel):
    def __init__(
        self,
        image_urlobject: BinaryIO = None,
    ):
        self.image_urlobject = image_urlobject

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_urlobject is not None:
            result['ImageURLObject'] = self.image_urlobject
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURLObject') is not None:
            self.image_urlobject = m.get('ImageURLObject')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        data: RecognizeVINCodeResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = RecognizeVINCodeResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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
            temp_model = RecognizeVINCodeResponseBody()
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        data: RecognizeVerificationcodeResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = RecognizeVerificationcodeResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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
            temp_model = RecognizeVerificationcodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeVideoCastCrewListRequestParams(TeaModel):
    def __init__(
        self,
        type: str = None,
    ):
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class RecognizeVideoCastCrewListRequest(TeaModel):
    def __init__(
        self,
        params: List[RecognizeVideoCastCrewListRequestParams] = None,
        register_url: str = None,
        video_url: str = None,
    ):
        self.params = params
        self.register_url = register_url
        self.video_url = video_url

    def validate(self):
        if self.params:
            for k in self.params:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Params'] = []
        if self.params is not None:
            for k in self.params:
                result['Params'].append(k.to_map() if k else None)
        if self.register_url is not None:
            result['RegisterUrl'] = self.register_url
        if self.video_url is not None:
            result['VideoUrl'] = self.video_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.params = []
        if m.get('Params') is not None:
            for k in m.get('Params'):
                temp_model = RecognizeVideoCastCrewListRequestParams()
                self.params.append(temp_model.from_map(k))
        if m.get('RegisterUrl') is not None:
            self.register_url = m.get('RegisterUrl')
        if m.get('VideoUrl') is not None:
            self.video_url = m.get('VideoUrl')
        return self


class RecognizeVideoCastCrewListAdvanceRequestParams(TeaModel):
    def __init__(
        self,
        type: str = None,
    ):
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class RecognizeVideoCastCrewListAdvanceRequest(TeaModel):
    def __init__(
        self,
        video_url_object: BinaryIO = None,
        params: List[RecognizeVideoCastCrewListAdvanceRequestParams] = None,
        register_url: str = None,
    ):
        self.video_url_object = video_url_object
        self.params = params
        self.register_url = register_url

    def validate(self):
        self.validate_required(self.video_url_object, 'video_url_object')
        if self.params:
            for k in self.params:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.video_url_object is not None:
            result['VideoUrlObject'] = self.video_url_object
        result['Params'] = []
        if self.params is not None:
            for k in self.params:
                result['Params'].append(k.to_map() if k else None)
        if self.register_url is not None:
            result['RegisterUrl'] = self.register_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VideoUrlObject') is not None:
            self.video_url_object = m.get('VideoUrlObject')
        self.params = []
        if m.get('Params') is not None:
            for k in m.get('Params'):
                temp_model = RecognizeVideoCastCrewListAdvanceRequestParams()
                self.params.append(temp_model.from_map(k))
        if m.get('RegisterUrl') is not None:
            self.register_url = m.get('RegisterUrl')
        return self


class RecognizeVideoCastCrewListShrinkRequest(TeaModel):
    def __init__(
        self,
        params_shrink: str = None,
        register_url: str = None,
        video_url: str = None,
    ):
        self.params_shrink = params_shrink
        self.register_url = register_url
        self.video_url = video_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.params_shrink is not None:
            result['Params'] = self.params_shrink
        if self.register_url is not None:
            result['RegisterUrl'] = self.register_url
        if self.video_url is not None:
            result['VideoUrl'] = self.video_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Params') is not None:
            self.params_shrink = m.get('Params')
        if m.get('RegisterUrl') is not None:
            self.register_url = m.get('RegisterUrl')
        if m.get('VideoUrl') is not None:
            self.video_url = m.get('VideoUrl')
        return self


class RecognizeVideoCastCrewListResponseBodyDataCastResults(TeaModel):
    def __init__(
        self,
        detail_infoes: Dict[str, str] = None,
        end_time: float = None,
        start_time: float = None,
    ):
        self.detail_infoes = detail_infoes
        self.end_time = end_time
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.detail_infoes is not None:
            result['DetailInfoes'] = self.detail_infoes
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DetailInfoes') is not None:
            self.detail_infoes = m.get('DetailInfoes')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class RecognizeVideoCastCrewListResponseBodyDataOcrResultsDetailInfoesPosition(TeaModel):
    def __init__(
        self,
        x: int = None,
        y: int = None,
    ):
        self.x = x
        self.y = y

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        return self


class RecognizeVideoCastCrewListResponseBodyDataOcrResultsDetailInfoes(TeaModel):
    def __init__(
        self,
        boxes: List[int] = None,
        char_probs: List[List[float]] = None,
        frame_index: int = None,
        position: List[RecognizeVideoCastCrewListResponseBodyDataOcrResultsDetailInfoesPosition] = None,
        score: float = None,
        text: str = None,
        text_prob: float = None,
        time_stamp: float = None,
        track_id: int = None,
    ):
        self.boxes = boxes
        self.char_probs = char_probs
        self.frame_index = frame_index
        self.position = position
        self.score = score
        self.text = text
        self.text_prob = text_prob
        self.time_stamp = time_stamp
        self.track_id = track_id

    def validate(self):
        if self.position:
            for k in self.position:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.boxes is not None:
            result['Boxes'] = self.boxes
        if self.char_probs is not None:
            result['CharProbs'] = self.char_probs
        if self.frame_index is not None:
            result['FrameIndex'] = self.frame_index
        result['Position'] = []
        if self.position is not None:
            for k in self.position:
                result['Position'].append(k.to_map() if k else None)
        if self.score is not None:
            result['Score'] = self.score
        if self.text is not None:
            result['Text'] = self.text
        if self.text_prob is not None:
            result['TextProb'] = self.text_prob
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.track_id is not None:
            result['TrackId'] = self.track_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Boxes') is not None:
            self.boxes = m.get('Boxes')
        if m.get('CharProbs') is not None:
            self.char_probs = m.get('CharProbs')
        if m.get('FrameIndex') is not None:
            self.frame_index = m.get('FrameIndex')
        self.position = []
        if m.get('Position') is not None:
            for k in m.get('Position'):
                temp_model = RecognizeVideoCastCrewListResponseBodyDataOcrResultsDetailInfoesPosition()
                self.position.append(temp_model.from_map(k))
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('TextProb') is not None:
            self.text_prob = m.get('TextProb')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('TrackId') is not None:
            self.track_id = m.get('TrackId')
        return self


class RecognizeVideoCastCrewListResponseBodyDataOcrResults(TeaModel):
    def __init__(
        self,
        detail_infoes: List[RecognizeVideoCastCrewListResponseBodyDataOcrResultsDetailInfoes] = None,
        end_time: float = None,
        start_time: float = None,
    ):
        self.detail_infoes = detail_infoes
        self.end_time = end_time
        self.start_time = start_time

    def validate(self):
        if self.detail_infoes:
            for k in self.detail_infoes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DetailInfoes'] = []
        if self.detail_infoes is not None:
            for k in self.detail_infoes:
                result['DetailInfoes'].append(k.to_map() if k else None)
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.detail_infoes = []
        if m.get('DetailInfoes') is not None:
            for k in m.get('DetailInfoes'):
                temp_model = RecognizeVideoCastCrewListResponseBodyDataOcrResultsDetailInfoes()
                self.detail_infoes.append(temp_model.from_map(k))
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class RecognizeVideoCastCrewListResponseBodyDataSubtitlesResults(TeaModel):
    def __init__(
        self,
        subtitles_all_results: Dict[str, str] = None,
        subtitles_all_results_url: str = None,
        subtitles_chinese_results: Dict[str, str] = None,
        subtitles_chinese_results_url: str = None,
        subtitles_english_results: Dict[str, Any] = None,
        subtitles_english_results_url: str = None,
    ):
        self.subtitles_all_results = subtitles_all_results
        self.subtitles_all_results_url = subtitles_all_results_url
        self.subtitles_chinese_results = subtitles_chinese_results
        self.subtitles_chinese_results_url = subtitles_chinese_results_url
        self.subtitles_english_results = subtitles_english_results
        self.subtitles_english_results_url = subtitles_english_results_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.subtitles_all_results is not None:
            result['SubtitlesAllResults'] = self.subtitles_all_results
        if self.subtitles_all_results_url is not None:
            result['SubtitlesAllResultsUrl'] = self.subtitles_all_results_url
        if self.subtitles_chinese_results is not None:
            result['SubtitlesChineseResults'] = self.subtitles_chinese_results
        if self.subtitles_chinese_results_url is not None:
            result['SubtitlesChineseResultsUrl'] = self.subtitles_chinese_results_url
        if self.subtitles_english_results is not None:
            result['SubtitlesEnglishResults'] = self.subtitles_english_results
        if self.subtitles_english_results_url is not None:
            result['SubtitlesEnglishResultsUrl'] = self.subtitles_english_results_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SubtitlesAllResults') is not None:
            self.subtitles_all_results = m.get('SubtitlesAllResults')
        if m.get('SubtitlesAllResultsUrl') is not None:
            self.subtitles_all_results_url = m.get('SubtitlesAllResultsUrl')
        if m.get('SubtitlesChineseResults') is not None:
            self.subtitles_chinese_results = m.get('SubtitlesChineseResults')
        if m.get('SubtitlesChineseResultsUrl') is not None:
            self.subtitles_chinese_results_url = m.get('SubtitlesChineseResultsUrl')
        if m.get('SubtitlesEnglishResults') is not None:
            self.subtitles_english_results = m.get('SubtitlesEnglishResults')
        if m.get('SubtitlesEnglishResultsUrl') is not None:
            self.subtitles_english_results_url = m.get('SubtitlesEnglishResultsUrl')
        return self


class RecognizeVideoCastCrewListResponseBodyDataVideoOcrResultsDetailInfoesPosition(TeaModel):
    def __init__(
        self,
        x: int = None,
        y: int = None,
    ):
        self.x = x
        self.y = y

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        return self


class RecognizeVideoCastCrewListResponseBodyDataVideoOcrResultsDetailInfoes(TeaModel):
    def __init__(
        self,
        boxes: List[int] = None,
        position: List[RecognizeVideoCastCrewListResponseBodyDataVideoOcrResultsDetailInfoesPosition] = None,
        score: float = None,
        text: str = None,
        text_type: int = None,
    ):
        self.boxes = boxes
        self.position = position
        self.score = score
        self.text = text
        self.text_type = text_type

    def validate(self):
        if self.position:
            for k in self.position:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.boxes is not None:
            result['Boxes'] = self.boxes
        result['Position'] = []
        if self.position is not None:
            for k in self.position:
                result['Position'].append(k.to_map() if k else None)
        if self.score is not None:
            result['Score'] = self.score
        if self.text is not None:
            result['Text'] = self.text
        if self.text_type is not None:
            result['TextType'] = self.text_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Boxes') is not None:
            self.boxes = m.get('Boxes')
        self.position = []
        if m.get('Position') is not None:
            for k in m.get('Position'):
                temp_model = RecognizeVideoCastCrewListResponseBodyDataVideoOcrResultsDetailInfoesPosition()
                self.position.append(temp_model.from_map(k))
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('TextType') is not None:
            self.text_type = m.get('TextType')
        return self


class RecognizeVideoCastCrewListResponseBodyDataVideoOcrResults(TeaModel):
    def __init__(
        self,
        detail_infoes: List[RecognizeVideoCastCrewListResponseBodyDataVideoOcrResultsDetailInfoes] = None,
        end_time: float = None,
        start_time: float = None,
    ):
        self.detail_infoes = detail_infoes
        self.end_time = end_time
        self.start_time = start_time

    def validate(self):
        if self.detail_infoes:
            for k in self.detail_infoes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DetailInfoes'] = []
        if self.detail_infoes is not None:
            for k in self.detail_infoes:
                result['DetailInfoes'].append(k.to_map() if k else None)
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.detail_infoes = []
        if m.get('DetailInfoes') is not None:
            for k in m.get('DetailInfoes'):
                temp_model = RecognizeVideoCastCrewListResponseBodyDataVideoOcrResultsDetailInfoes()
                self.detail_infoes.append(temp_model.from_map(k))
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class RecognizeVideoCastCrewListResponseBodyData(TeaModel):
    def __init__(
        self,
        cast_results: List[RecognizeVideoCastCrewListResponseBodyDataCastResults] = None,
        ocr_results: List[RecognizeVideoCastCrewListResponseBodyDataOcrResults] = None,
        subtitles_results: List[RecognizeVideoCastCrewListResponseBodyDataSubtitlesResults] = None,
        video_ocr_results: List[RecognizeVideoCastCrewListResponseBodyDataVideoOcrResults] = None,
    ):
        self.cast_results = cast_results
        self.ocr_results = ocr_results
        self.subtitles_results = subtitles_results
        self.video_ocr_results = video_ocr_results

    def validate(self):
        if self.cast_results:
            for k in self.cast_results:
                if k:
                    k.validate()
        if self.ocr_results:
            for k in self.ocr_results:
                if k:
                    k.validate()
        if self.subtitles_results:
            for k in self.subtitles_results:
                if k:
                    k.validate()
        if self.video_ocr_results:
            for k in self.video_ocr_results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CastResults'] = []
        if self.cast_results is not None:
            for k in self.cast_results:
                result['CastResults'].append(k.to_map() if k else None)
        result['OcrResults'] = []
        if self.ocr_results is not None:
            for k in self.ocr_results:
                result['OcrResults'].append(k.to_map() if k else None)
        result['SubtitlesResults'] = []
        if self.subtitles_results is not None:
            for k in self.subtitles_results:
                result['SubtitlesResults'].append(k.to_map() if k else None)
        result['VideoOcrResults'] = []
        if self.video_ocr_results is not None:
            for k in self.video_ocr_results:
                result['VideoOcrResults'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cast_results = []
        if m.get('CastResults') is not None:
            for k in m.get('CastResults'):
                temp_model = RecognizeVideoCastCrewListResponseBodyDataCastResults()
                self.cast_results.append(temp_model.from_map(k))
        self.ocr_results = []
        if m.get('OcrResults') is not None:
            for k in m.get('OcrResults'):
                temp_model = RecognizeVideoCastCrewListResponseBodyDataOcrResults()
                self.ocr_results.append(temp_model.from_map(k))
        self.subtitles_results = []
        if m.get('SubtitlesResults') is not None:
            for k in m.get('SubtitlesResults'):
                temp_model = RecognizeVideoCastCrewListResponseBodyDataSubtitlesResults()
                self.subtitles_results.append(temp_model.from_map(k))
        self.video_ocr_results = []
        if m.get('VideoOcrResults') is not None:
            for k in m.get('VideoOcrResults'):
                temp_model = RecognizeVideoCastCrewListResponseBodyDataVideoOcrResults()
                self.video_ocr_results.append(temp_model.from_map(k))
        return self


class RecognizeVideoCastCrewListResponseBody(TeaModel):
    def __init__(
        self,
        data: RecognizeVideoCastCrewListResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = RecognizeVideoCastCrewListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RecognizeVideoCastCrewListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RecognizeVideoCastCrewListResponseBody = None,
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
            temp_model = RecognizeVideoCastCrewListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeVideoCharacterRequest(TeaModel):
    def __init__(
        self,
        video_url: str = None,
    ):
        # 视频文件地址
        self.video_url = video_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.video_url is not None:
            result['VideoURL'] = self.video_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VideoURL') is not None:
            self.video_url = m.get('VideoURL')
        return self


class RecognizeVideoCharacterResponseBodyDataFramesElementsTextRectangles(TeaModel):
    def __init__(
        self,
        angle: int = None,
        height: int = None,
        left: int = None,
        top: int = None,
        width: int = None,
    ):
        # 文字区域角度，角度范围[0, 360]
        self.angle = angle
        # 文字区域高度
        self.height = height
        # 文字区域左上角x坐标
        self.left = left
        # 文字区域左上角y坐标
        self.top = top
        # 文字区域宽度
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.angle is not None:
            result['Angle'] = self.angle
        if self.height is not None:
            result['Height'] = self.height
        if self.left is not None:
            result['Left'] = self.left
        if self.top is not None:
            result['Top'] = self.top
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Angle') is not None:
            self.angle = m.get('Angle')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Left') is not None:
            self.left = m.get('Left')
        if m.get('Top') is not None:
            self.top = m.get('Top')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class RecognizeVideoCharacterResponseBodyDataFramesElements(TeaModel):
    def __init__(
        self,
        score: float = None,
        text: str = None,
        text_rectangles: List[RecognizeVideoCharacterResponseBodyDataFramesElementsTextRectangles] = None,
    ):
        # 文字区域概率，概率值的范围为[0.0, 1.0]
        self.score = score
        # 文字内容
        self.text = text
        self.text_rectangles = text_rectangles

    def validate(self):
        if self.text_rectangles:
            for k in self.text_rectangles:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.score is not None:
            result['Score'] = self.score
        if self.text is not None:
            result['Text'] = self.text
        result['TextRectangles'] = []
        if self.text_rectangles is not None:
            for k in self.text_rectangles:
                result['TextRectangles'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        self.text_rectangles = []
        if m.get('TextRectangles') is not None:
            for k in m.get('TextRectangles'):
                temp_model = RecognizeVideoCharacterResponseBodyDataFramesElementsTextRectangles()
                self.text_rectangles.append(temp_model.from_map(k))
        return self


class RecognizeVideoCharacterResponseBodyDataFrames(TeaModel):
    def __init__(
        self,
        elements: List[RecognizeVideoCharacterResponseBodyDataFramesElements] = None,
        timestamp: int = None,
    ):
        self.elements = elements
        # 帧时间戳时间戳，单位秒。
        self.timestamp = timestamp

    def validate(self):
        if self.elements:
            for k in self.elements:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Elements'] = []
        if self.elements is not None:
            for k in self.elements:
                result['Elements'].append(k.to_map() if k else None)
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.elements = []
        if m.get('Elements') is not None:
            for k in m.get('Elements'):
                temp_model = RecognizeVideoCharacterResponseBodyDataFramesElements()
                self.elements.append(temp_model.from_map(k))
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        return self


class RecognizeVideoCharacterResponseBodyData(TeaModel):
    def __init__(
        self,
        frames: List[RecognizeVideoCharacterResponseBodyDataFrames] = None,
        height: int = None,
        input_file: str = None,
        width: int = None,
    ):
        # 视频帧的集合，空信息的帧不列出。
        self.frames = frames
        self.height = height
        # 对应的输入OSS文件 (格式oss://{bucketName}/{object})
        self.input_file = input_file
        self.width = width

    def validate(self):
        if self.frames:
            for k in self.frames:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Frames'] = []
        if self.frames is not None:
            for k in self.frames:
                result['Frames'].append(k.to_map() if k else None)
        if self.height is not None:
            result['Height'] = self.height
        if self.input_file is not None:
            result['InputFile'] = self.input_file
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.frames = []
        if m.get('Frames') is not None:
            for k in m.get('Frames'):
                temp_model = RecognizeVideoCharacterResponseBodyDataFrames()
                self.frames.append(temp_model.from_map(k))
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('InputFile') is not None:
            self.input_file = m.get('InputFile')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class RecognizeVideoCharacterResponseBody(TeaModel):
    def __init__(
        self,
        data: RecognizeVideoCharacterResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = RecognizeVideoCharacterResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RecognizeVideoCharacterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RecognizeVideoCharacterResponseBody = None,
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
            temp_model = RecognizeVideoCharacterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TrimDocumentRequest(TeaModel):
    def __init__(
        self,
        file_type: str = None,
        file_url: str = None,
        output_type: str = None,
    ):
        self.file_type = file_type
        self.file_url = file_url
        self.output_type = output_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_type is not None:
            result['FileType'] = self.file_type
        if self.file_url is not None:
            result['FileURL'] = self.file_url
        if self.output_type is not None:
            result['OutputType'] = self.output_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')
        if m.get('FileURL') is not None:
            self.file_url = m.get('FileURL')
        if m.get('OutputType') is not None:
            self.output_type = m.get('OutputType')
        return self


class TrimDocumentAdvanceRequest(TeaModel):
    def __init__(
        self,
        file_urlobject: BinaryIO = None,
        file_type: str = None,
        output_type: str = None,
    ):
        self.file_urlobject = file_urlobject
        self.file_type = file_type
        self.output_type = output_type

    def validate(self):
        self.validate_required(self.file_urlobject, 'file_urlobject')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_urlobject is not None:
            result['FileURLObject'] = self.file_urlobject
        if self.file_type is not None:
            result['FileType'] = self.file_type
        if self.output_type is not None:
            result['OutputType'] = self.output_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileURLObject') is not None:
            self.file_urlobject = m.get('FileURLObject')
        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')
        if m.get('OutputType') is not None:
            self.output_type = m.get('OutputType')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        data: TrimDocumentResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = TrimDocumentResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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
            temp_model = TrimDocumentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


