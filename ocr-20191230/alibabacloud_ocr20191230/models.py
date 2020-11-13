# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
try:
    from typing import List, BinaryIO
except ImportError:
    pass


class RecognizePoiNameRequest(TeaModel):
    def __init__(self, image_url=None):
        self.image_url = image_url      # type: str

    def validate(self):
        self.validate_required(self.image_url, 'image_url')

    def to_map(self):
        result = {}
        result['ImageURL'] = self.image_url
        return result

    def from_map(self, map={}):
        self.image_url = map.get('ImageURL')
        return self


class RecognizePoiNameResponse(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id    # type: str
        self.data = data                # type: RecognizePoiNameResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = RecognizePoiNameResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class RecognizePoiNameResponseDataSignboardsTexts(TeaModel):
    def __init__(self, label=None, score=None, tag=None, type=None, points=None):
        self.label = label              # type: str
        self.score = score              # type: float
        self.tag = tag                  # type: str
        self.type = type                # type: str
        self.points = points            # type: List[int]

    def validate(self):
        self.validate_required(self.label, 'label')
        self.validate_required(self.score, 'score')
        self.validate_required(self.tag, 'tag')
        self.validate_required(self.type, 'type')
        self.validate_required(self.points, 'points')

    def to_map(self):
        result = {}
        result['Label'] = self.label
        result['Score'] = self.score
        result['Tag'] = self.tag
        result['Type'] = self.type
        result['Points'] = self.points
        return result

    def from_map(self, map={}):
        self.label = map.get('Label')
        self.score = map.get('Score')
        self.tag = map.get('Tag')
        self.type = map.get('Type')
        self.points = map.get('Points')
        return self


class RecognizePoiNameResponseDataSignboards(TeaModel):
    def __init__(self, texts=None):
        self.texts = texts              # type: List[RecognizePoiNameResponseDataSignboardsTexts]

    def validate(self):
        self.validate_required(self.texts, 'texts')
        if self.texts:
            for k in self.texts:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Texts'] = []
        if self.texts is not None:
            for k in self.texts:
                result['Texts'].append(k.to_map() if k else None)
        else:
            result['Texts'] = None
        return result

    def from_map(self, map={}):
        self.texts = []
        if map.get('Texts') is not None:
            for k in map.get('Texts'):
                temp_model = RecognizePoiNameResponseDataSignboardsTexts()
                self.texts.append(temp_model.from_map(k))
        else:
            self.texts = None
        return self


class RecognizePoiNameResponseDataSummary(TeaModel):
    def __init__(self, brand=None, score=None):
        self.brand = brand              # type: str
        self.score = score              # type: float

    def validate(self):
        self.validate_required(self.brand, 'brand')
        self.validate_required(self.score, 'score')

    def to_map(self):
        result = {}
        result['Brand'] = self.brand
        result['Score'] = self.score
        return result

    def from_map(self, map={}):
        self.brand = map.get('Brand')
        self.score = map.get('Score')
        return self


class RecognizePoiNameResponseData(TeaModel):
    def __init__(self, signboards=None, summary=None):
        self.signboards = signboards    # type: List[RecognizePoiNameResponseDataSignboards]
        self.summary = summary          # type: RecognizePoiNameResponseDataSummary

    def validate(self):
        self.validate_required(self.signboards, 'signboards')
        if self.signboards:
            for k in self.signboards:
                if k:
                    k.validate()
        self.validate_required(self.summary, 'summary')
        if self.summary:
            self.summary.validate()

    def to_map(self):
        result = {}
        result['Signboards'] = []
        if self.signboards is not None:
            for k in self.signboards:
                result['Signboards'].append(k.to_map() if k else None)
        else:
            result['Signboards'] = None
        if self.summary is not None:
            result['Summary'] = self.summary.to_map()
        else:
            result['Summary'] = None
        return result

    def from_map(self, map={}):
        self.signboards = []
        if map.get('Signboards') is not None:
            for k in map.get('Signboards'):
                temp_model = RecognizePoiNameResponseDataSignboards()
                self.signboards.append(temp_model.from_map(k))
        else:
            self.signboards = None
        if map.get('Summary') is not None:
            temp_model = RecognizePoiNameResponseDataSummary()
            self.summary = temp_model.from_map(map['Summary'])
        else:
            self.summary = None
        return self


class RecognizePoiNameAdvanceRequest(TeaModel):
    def __init__(self, image_urlobject=None):
        self.image_urlobject = image_urlobject  # type: BinaryIO

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        result = {}
        result['ImageURLObject'] = self.image_urlobject
        return result

    def from_map(self, map={}):
        self.image_urlobject = map.get('ImageURLObject')
        return self


class DetectCardScreenshotRequest(TeaModel):
    def __init__(self, image_url=None):
        self.image_url = image_url      # type: str

    def validate(self):
        self.validate_required(self.image_url, 'image_url')

    def to_map(self):
        result = {}
        result['ImageURL'] = self.image_url
        return result

    def from_map(self, map={}):
        self.image_url = map.get('ImageURL')
        return self


class DetectCardScreenshotResponse(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id    # type: str
        self.data = data                # type: DetectCardScreenshotResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = DetectCardScreenshotResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class DetectCardScreenshotResponseDataSpoofResultResultMap(TeaModel):
    def __init__(self, screen_score=None, screen_threshold=None):
        self.screen_score = screen_score  # type: float
        self.screen_threshold = screen_threshold  # type: float

    def validate(self):
        self.validate_required(self.screen_score, 'screen_score')
        self.validate_required(self.screen_threshold, 'screen_threshold')

    def to_map(self):
        result = {}
        result['ScreenScore'] = self.screen_score
        result['ScreenThreshold'] = self.screen_threshold
        return result

    def from_map(self, map={}):
        self.screen_score = map.get('ScreenScore')
        self.screen_threshold = map.get('ScreenThreshold')
        return self


class DetectCardScreenshotResponseDataSpoofResult(TeaModel):
    def __init__(self, is_spoof=None, result_map=None):
        self.is_spoof = is_spoof        # type: bool
        self.result_map = result_map    # type: DetectCardScreenshotResponseDataSpoofResultResultMap

    def validate(self):
        self.validate_required(self.is_spoof, 'is_spoof')
        self.validate_required(self.result_map, 'result_map')
        if self.result_map:
            self.result_map.validate()

    def to_map(self):
        result = {}
        result['IsSpoof'] = self.is_spoof
        if self.result_map is not None:
            result['ResultMap'] = self.result_map.to_map()
        else:
            result['ResultMap'] = None
        return result

    def from_map(self, map={}):
        self.is_spoof = map.get('IsSpoof')
        if map.get('ResultMap') is not None:
            temp_model = DetectCardScreenshotResponseDataSpoofResultResultMap()
            self.result_map = temp_model.from_map(map['ResultMap'])
        else:
            self.result_map = None
        return self


class DetectCardScreenshotResponseData(TeaModel):
    def __init__(self, is_card=None, is_blur=None, spoof_result=None):
        self.is_card = is_card          # type: bool
        self.is_blur = is_blur          # type: bool
        self.spoof_result = spoof_result  # type: DetectCardScreenshotResponseDataSpoofResult

    def validate(self):
        self.validate_required(self.is_card, 'is_card')
        self.validate_required(self.is_blur, 'is_blur')
        self.validate_required(self.spoof_result, 'spoof_result')
        if self.spoof_result:
            self.spoof_result.validate()

    def to_map(self):
        result = {}
        result['IsCard'] = self.is_card
        result['IsBlur'] = self.is_blur
        if self.spoof_result is not None:
            result['SpoofResult'] = self.spoof_result.to_map()
        else:
            result['SpoofResult'] = None
        return result

    def from_map(self, map={}):
        self.is_card = map.get('IsCard')
        self.is_blur = map.get('IsBlur')
        if map.get('SpoofResult') is not None:
            temp_model = DetectCardScreenshotResponseDataSpoofResult()
            self.spoof_result = temp_model.from_map(map['SpoofResult'])
        else:
            self.spoof_result = None
        return self


class DetectCardScreenshotAdvanceRequest(TeaModel):
    def __init__(self, image_urlobject=None):
        self.image_urlobject = image_urlobject  # type: BinaryIO

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        result = {}
        result['ImageURLObject'] = self.image_urlobject
        return result

    def from_map(self, map={}):
        self.image_urlobject = map.get('ImageURLObject')
        return self


class GetAsyncJobResultRequest(TeaModel):
    def __init__(self, job_id=None):
        self.job_id = job_id            # type: str

    def validate(self):
        self.validate_required(self.job_id, 'job_id')

    def to_map(self):
        result = {}
        result['JobId'] = self.job_id
        return result

    def from_map(self, map={}):
        self.job_id = map.get('JobId')
        return self


class GetAsyncJobResultResponse(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id    # type: str
        self.data = data                # type: GetAsyncJobResultResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = GetAsyncJobResultResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class GetAsyncJobResultResponseData(TeaModel):
    def __init__(self, error_code=None, error_message=None, job_id=None, result=None, status=None):
        self.error_code = error_code    # type: str
        self.error_message = error_message  # type: str
        self.job_id = job_id            # type: str
        self.result = result            # type: str
        self.status = status            # type: str

    def validate(self):
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.error_message, 'error_message')
        self.validate_required(self.job_id, 'job_id')
        self.validate_required(self.result, 'result')
        self.validate_required(self.status, 'status')

    def to_map(self):
        result = {}
        result['ErrorCode'] = self.error_code
        result['ErrorMessage'] = self.error_message
        result['JobId'] = self.job_id
        result['Result'] = self.result
        result['Status'] = self.status
        return result

    def from_map(self, map={}):
        self.error_code = map.get('ErrorCode')
        self.error_message = map.get('ErrorMessage')
        self.job_id = map.get('JobId')
        self.result = map.get('Result')
        self.status = map.get('Status')
        return self


class TrimDocumentRequest(TeaModel):
    def __init__(self, file_url=None, file_type=None, output_type=None):
        self.file_url = file_url        # type: str
        self.file_type = file_type      # type: str
        self.output_type = output_type  # type: str

    def validate(self):
        self.validate_required(self.file_url, 'file_url')
        self.validate_required(self.file_type, 'file_type')
        self.validate_required(self.output_type, 'output_type')

    def to_map(self):
        result = {}
        result['FileURL'] = self.file_url
        result['FileType'] = self.file_type
        result['OutputType'] = self.output_type
        return result

    def from_map(self, map={}):
        self.file_url = map.get('FileURL')
        self.file_type = map.get('FileType')
        self.output_type = map.get('OutputType')
        return self


class TrimDocumentResponse(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id    # type: str
        self.data = data                # type: TrimDocumentResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = TrimDocumentResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class TrimDocumentResponseData(TeaModel):
    def __init__(self, content=None):
        self.content = content          # type: str

    def validate(self):
        self.validate_required(self.content, 'content')

    def to_map(self):
        result = {}
        result['Content'] = self.content
        return result

    def from_map(self, map={}):
        self.content = map.get('Content')
        return self


class TrimDocumentAdvanceRequest(TeaModel):
    def __init__(self, file_urlobject=None, file_type=None, output_type=None):
        self.file_urlobject = file_urlobject  # type: BinaryIO
        self.file_type = file_type      # type: str
        self.output_type = output_type  # type: str

    def validate(self):
        self.validate_required(self.file_urlobject, 'file_urlobject')
        self.validate_required(self.file_type, 'file_type')
        self.validate_required(self.output_type, 'output_type')

    def to_map(self):
        result = {}
        result['FileURLObject'] = self.file_urlobject
        result['FileType'] = self.file_type
        result['OutputType'] = self.output_type
        return result

    def from_map(self, map={}):
        self.file_urlobject = map.get('FileURLObject')
        self.file_type = map.get('FileType')
        self.output_type = map.get('OutputType')
        return self


class RecognizeChinapassportRequest(TeaModel):
    def __init__(self, image_url=None):
        self.image_url = image_url      # type: str

    def validate(self):
        self.validate_required(self.image_url, 'image_url')

    def to_map(self):
        result = {}
        result['ImageURL'] = self.image_url
        return result

    def from_map(self, map={}):
        self.image_url = map.get('ImageURL')
        return self


class RecognizeChinapassportResponse(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id    # type: str
        self.data = data                # type: RecognizeChinapassportResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = RecognizeChinapassportResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class RecognizeChinapassportResponseData(TeaModel):
    def __init__(self, authority=None, birth_date=None, birth_day=None, birth_place=None, birth_place_raw=None,
                 country=None, expiry_date=None, expiry_day=None, issue_date=None, issue_place=None, issue_place_raw=None,
                 line_zero=None, line_one=None, name=None, name_chinese=None, name_chinese_raw=None, passport_no=None,
                 person_id=None, sex=None, source_country=None, success=None, type=None):
        self.authority = authority      # type: str
        self.birth_date = birth_date    # type: str
        self.birth_day = birth_day      # type: str
        self.birth_place = birth_place  # type: str
        self.birth_place_raw = birth_place_raw  # type: str
        self.country = country          # type: str
        self.expiry_date = expiry_date  # type: str
        self.expiry_day = expiry_day    # type: str
        self.issue_date = issue_date    # type: str
        self.issue_place = issue_place  # type: str
        self.issue_place_raw = issue_place_raw  # type: str
        self.line_zero = line_zero      # type: str
        self.line_one = line_one        # type: str
        self.name = name                # type: str
        self.name_chinese = name_chinese  # type: str
        self.name_chinese_raw = name_chinese_raw  # type: str
        self.passport_no = passport_no  # type: str
        self.person_id = person_id      # type: str
        self.sex = sex                  # type: str
        self.source_country = source_country  # type: str
        self.success = success          # type: bool
        self.type = type                # type: str

    def validate(self):
        self.validate_required(self.authority, 'authority')
        self.validate_required(self.birth_date, 'birth_date')
        self.validate_required(self.birth_day, 'birth_day')
        self.validate_required(self.birth_place, 'birth_place')
        self.validate_required(self.birth_place_raw, 'birth_place_raw')
        self.validate_required(self.country, 'country')
        self.validate_required(self.expiry_date, 'expiry_date')
        self.validate_required(self.expiry_day, 'expiry_day')
        self.validate_required(self.issue_date, 'issue_date')
        self.validate_required(self.issue_place, 'issue_place')
        self.validate_required(self.issue_place_raw, 'issue_place_raw')
        self.validate_required(self.line_zero, 'line_zero')
        self.validate_required(self.line_one, 'line_one')
        self.validate_required(self.name, 'name')
        self.validate_required(self.name_chinese, 'name_chinese')
        self.validate_required(self.name_chinese_raw, 'name_chinese_raw')
        self.validate_required(self.passport_no, 'passport_no')
        self.validate_required(self.person_id, 'person_id')
        self.validate_required(self.sex, 'sex')
        self.validate_required(self.source_country, 'source_country')
        self.validate_required(self.success, 'success')
        self.validate_required(self.type, 'type')

    def to_map(self):
        result = {}
        result['Authority'] = self.authority
        result['BirthDate'] = self.birth_date
        result['BirthDay'] = self.birth_day
        result['BirthPlace'] = self.birth_place
        result['BirthPlaceRaw'] = self.birth_place_raw
        result['Country'] = self.country
        result['ExpiryDate'] = self.expiry_date
        result['ExpiryDay'] = self.expiry_day
        result['IssueDate'] = self.issue_date
        result['IssuePlace'] = self.issue_place
        result['IssuePlaceRaw'] = self.issue_place_raw
        result['LineZero'] = self.line_zero
        result['LineOne'] = self.line_one
        result['Name'] = self.name
        result['NameChinese'] = self.name_chinese
        result['NameChineseRaw'] = self.name_chinese_raw
        result['PassportNo'] = self.passport_no
        result['PersonId'] = self.person_id
        result['Sex'] = self.sex
        result['SourceCountry'] = self.source_country
        result['Success'] = self.success
        result['Type'] = self.type
        return result

    def from_map(self, map={}):
        self.authority = map.get('Authority')
        self.birth_date = map.get('BirthDate')
        self.birth_day = map.get('BirthDay')
        self.birth_place = map.get('BirthPlace')
        self.birth_place_raw = map.get('BirthPlaceRaw')
        self.country = map.get('Country')
        self.expiry_date = map.get('ExpiryDate')
        self.expiry_day = map.get('ExpiryDay')
        self.issue_date = map.get('IssueDate')
        self.issue_place = map.get('IssuePlace')
        self.issue_place_raw = map.get('IssuePlaceRaw')
        self.line_zero = map.get('LineZero')
        self.line_one = map.get('LineOne')
        self.name = map.get('Name')
        self.name_chinese = map.get('NameChinese')
        self.name_chinese_raw = map.get('NameChineseRaw')
        self.passport_no = map.get('PassportNo')
        self.person_id = map.get('PersonId')
        self.sex = map.get('Sex')
        self.source_country = map.get('SourceCountry')
        self.success = map.get('Success')
        self.type = map.get('Type')
        return self


class RecognizeChinapassportAdvanceRequest(TeaModel):
    def __init__(self, image_urlobject=None):
        self.image_urlobject = image_urlobject  # type: BinaryIO

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        result = {}
        result['ImageURLObject'] = self.image_urlobject
        return result

    def from_map(self, map={}):
        self.image_urlobject = map.get('ImageURLObject')
        return self


class RecognizeVerificationcodeRequest(TeaModel):
    def __init__(self, image_url=None):
        self.image_url = image_url      # type: str

    def validate(self):
        self.validate_required(self.image_url, 'image_url')

    def to_map(self):
        result = {}
        result['ImageURL'] = self.image_url
        return result

    def from_map(self, map={}):
        self.image_url = map.get('ImageURL')
        return self


class RecognizeVerificationcodeResponse(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id    # type: str
        self.data = data                # type: RecognizeVerificationcodeResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = RecognizeVerificationcodeResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class RecognizeVerificationcodeResponseData(TeaModel):
    def __init__(self, content=None):
        self.content = content          # type: str

    def validate(self):
        self.validate_required(self.content, 'content')

    def to_map(self):
        result = {}
        result['Content'] = self.content
        return result

    def from_map(self, map={}):
        self.content = map.get('Content')
        return self


class RecognizeVerificationcodeAdvanceRequest(TeaModel):
    def __init__(self, image_urlobject=None):
        self.image_urlobject = image_urlobject  # type: BinaryIO

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        result = {}
        result['ImageURLObject'] = self.image_urlobject
        return result

    def from_map(self, map={}):
        self.image_urlobject = map.get('ImageURLObject')
        return self


class RecognizePassportMRZRequest(TeaModel):
    def __init__(self, image_url=None):
        self.image_url = image_url      # type: str

    def validate(self):
        self.validate_required(self.image_url, 'image_url')

    def to_map(self):
        result = {}
        result['ImageURL'] = self.image_url
        return result

    def from_map(self, map={}):
        self.image_url = map.get('ImageURL')
        return self


class RecognizePassportMRZResponse(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id    # type: str
        self.data = data                # type: RecognizePassportMRZResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = RecognizePassportMRZResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class RecognizePassportMRZResponseDataRegions(TeaModel):
    def __init__(self, name=None, recognition_score=None, content=None, detection_score=None, band_boxes=None):
        self.name = name                # type: str
        self.recognition_score = recognition_score  # type: float
        self.content = content          # type: str
        self.detection_score = detection_score  # type: float
        self.band_boxes = band_boxes    # type: List[float]

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.recognition_score, 'recognition_score')
        self.validate_required(self.content, 'content')
        self.validate_required(self.detection_score, 'detection_score')
        self.validate_required(self.band_boxes, 'band_boxes')

    def to_map(self):
        result = {}
        result['Name'] = self.name
        result['RecognitionScore'] = self.recognition_score
        result['Content'] = self.content
        result['DetectionScore'] = self.detection_score
        result['BandBoxes'] = self.band_boxes
        return result

    def from_map(self, map={}):
        self.name = map.get('Name')
        self.recognition_score = map.get('RecognitionScore')
        self.content = map.get('Content')
        self.detection_score = map.get('DetectionScore')
        self.band_boxes = map.get('BandBoxes')
        return self


class RecognizePassportMRZResponseData(TeaModel):
    def __init__(self, regions=None):
        self.regions = regions          # type: List[RecognizePassportMRZResponseDataRegions]

    def validate(self):
        self.validate_required(self.regions, 'regions')
        if self.regions:
            for k in self.regions:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Regions'] = []
        if self.regions is not None:
            for k in self.regions:
                result['Regions'].append(k.to_map() if k else None)
        else:
            result['Regions'] = None
        return result

    def from_map(self, map={}):
        self.regions = []
        if map.get('Regions') is not None:
            for k in map.get('Regions'):
                temp_model = RecognizePassportMRZResponseDataRegions()
                self.regions.append(temp_model.from_map(k))
        else:
            self.regions = None
        return self


class RecognizePassportMRZAdvanceRequest(TeaModel):
    def __init__(self, image_urlobject=None):
        self.image_urlobject = image_urlobject  # type: BinaryIO

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        result = {}
        result['ImageURLObject'] = self.image_urlobject
        return result

    def from_map(self, map={}):
        self.image_urlobject = map.get('ImageURLObject')
        return self


class RecognizeTakeoutOrderRequest(TeaModel):
    def __init__(self, image_url=None):
        self.image_url = image_url      # type: str

    def validate(self):
        self.validate_required(self.image_url, 'image_url')

    def to_map(self):
        result = {}
        result['ImageURL'] = self.image_url
        return result

    def from_map(self, map={}):
        self.image_url = map.get('ImageURL')
        return self


class RecognizeTakeoutOrderResponse(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id    # type: str
        self.data = data                # type: RecognizeTakeoutOrderResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = RecognizeTakeoutOrderResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class RecognizeTakeoutOrderResponseDataElements(TeaModel):
    def __init__(self, score=None, name=None, value=None, boxes=None):
        self.score = score              # type: float
        self.name = name                # type: str
        self.value = value              # type: str
        self.boxes = boxes              # type: List[int]

    def validate(self):
        self.validate_required(self.score, 'score')
        self.validate_required(self.name, 'name')
        self.validate_required(self.value, 'value')
        self.validate_required(self.boxes, 'boxes')

    def to_map(self):
        result = {}
        result['Score'] = self.score
        result['Name'] = self.name
        result['Value'] = self.value
        result['Boxes'] = self.boxes
        return result

    def from_map(self, map={}):
        self.score = map.get('Score')
        self.name = map.get('Name')
        self.value = map.get('Value')
        self.boxes = map.get('Boxes')
        return self


class RecognizeTakeoutOrderResponseData(TeaModel):
    def __init__(self, elements=None):
        self.elements = elements        # type: List[RecognizeTakeoutOrderResponseDataElements]

    def validate(self):
        self.validate_required(self.elements, 'elements')
        if self.elements:
            for k in self.elements:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Elements'] = []
        if self.elements is not None:
            for k in self.elements:
                result['Elements'].append(k.to_map() if k else None)
        else:
            result['Elements'] = None
        return result

    def from_map(self, map={}):
        self.elements = []
        if map.get('Elements') is not None:
            for k in map.get('Elements'):
                temp_model = RecognizeTakeoutOrderResponseDataElements()
                self.elements.append(temp_model.from_map(k))
        else:
            self.elements = None
        return self


class RecognizeTakeoutOrderAdvanceRequest(TeaModel):
    def __init__(self, image_urlobject=None):
        self.image_urlobject = image_urlobject  # type: BinaryIO

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        result = {}
        result['ImageURLObject'] = self.image_urlobject
        return result

    def from_map(self, map={}):
        self.image_urlobject = map.get('ImageURLObject')
        return self


class RecognizeQrCodeRequest(TeaModel):
    def __init__(self, tasks=None):
        self.tasks = tasks              # type: List[RecognizeQrCodeRequestTasks]

    def validate(self):
        self.validate_required(self.tasks, 'tasks')
        if self.tasks:
            for k in self.tasks:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Tasks'] = []
        if self.tasks is not None:
            for k in self.tasks:
                result['Tasks'].append(k.to_map() if k else None)
        else:
            result['Tasks'] = None
        return result

    def from_map(self, map={}):
        self.tasks = []
        if map.get('Tasks') is not None:
            for k in map.get('Tasks'):
                temp_model = RecognizeQrCodeRequestTasks()
                self.tasks.append(temp_model.from_map(k))
        else:
            self.tasks = None
        return self


class RecognizeQrCodeRequestTasks(TeaModel):
    def __init__(self, image_url=None):
        self.image_url = image_url      # type: str

    def validate(self):
        self.validate_required(self.image_url, 'image_url')

    def to_map(self):
        result = {}
        result['ImageURL'] = self.image_url
        return result

    def from_map(self, map={}):
        self.image_url = map.get('ImageURL')
        return self


class RecognizeQrCodeResponse(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id    # type: str
        self.data = data                # type: RecognizeQrCodeResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = RecognizeQrCodeResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class RecognizeQrCodeResponseDataElementsResults(TeaModel):
    def __init__(self, label=None, suggestion=None, rate=None, qr_codes_data=None):
        self.label = label              # type: str
        self.suggestion = suggestion    # type: str
        self.rate = rate                # type: float
        self.qr_codes_data = qr_codes_data  # type: List[str]

    def validate(self):
        self.validate_required(self.label, 'label')
        self.validate_required(self.suggestion, 'suggestion')
        self.validate_required(self.rate, 'rate')
        self.validate_required(self.qr_codes_data, 'qr_codes_data')

    def to_map(self):
        result = {}
        result['Label'] = self.label
        result['Suggestion'] = self.suggestion
        result['Rate'] = self.rate
        result['QrCodesData'] = self.qr_codes_data
        return result

    def from_map(self, map={}):
        self.label = map.get('Label')
        self.suggestion = map.get('Suggestion')
        self.rate = map.get('Rate')
        self.qr_codes_data = map.get('QrCodesData')
        return self


class RecognizeQrCodeResponseDataElements(TeaModel):
    def __init__(self, task_id=None, image_url=None, results=None):
        self.task_id = task_id          # type: str
        self.image_url = image_url      # type: str
        self.results = results          # type: List[RecognizeQrCodeResponseDataElementsResults]

    def validate(self):
        self.validate_required(self.task_id, 'task_id')
        self.validate_required(self.image_url, 'image_url')
        self.validate_required(self.results, 'results')
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['TaskId'] = self.task_id
        result['ImageURL'] = self.image_url
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        else:
            result['Results'] = None
        return result

    def from_map(self, map={}):
        self.task_id = map.get('TaskId')
        self.image_url = map.get('ImageURL')
        self.results = []
        if map.get('Results') is not None:
            for k in map.get('Results'):
                temp_model = RecognizeQrCodeResponseDataElementsResults()
                self.results.append(temp_model.from_map(k))
        else:
            self.results = None
        return self


class RecognizeQrCodeResponseData(TeaModel):
    def __init__(self, elements=None):
        self.elements = elements        # type: List[RecognizeQrCodeResponseDataElements]

    def validate(self):
        self.validate_required(self.elements, 'elements')
        if self.elements:
            for k in self.elements:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Elements'] = []
        if self.elements is not None:
            for k in self.elements:
                result['Elements'].append(k.to_map() if k else None)
        else:
            result['Elements'] = None
        return result

    def from_map(self, map={}):
        self.elements = []
        if map.get('Elements') is not None:
            for k in map.get('Elements'):
                temp_model = RecognizeQrCodeResponseDataElements()
                self.elements.append(temp_model.from_map(k))
        else:
            self.elements = None
        return self


class RecognizeVATInvoiceRequest(TeaModel):
    def __init__(self, file_url=None, file_type=None):
        self.file_url = file_url        # type: str
        self.file_type = file_type      # type: str

    def validate(self):
        self.validate_required(self.file_url, 'file_url')
        self.validate_required(self.file_type, 'file_type')

    def to_map(self):
        result = {}
        result['FileURL'] = self.file_url
        result['FileType'] = self.file_type
        return result

    def from_map(self, map={}):
        self.file_url = map.get('FileURL')
        self.file_type = map.get('FileType')
        return self


class RecognizeVATInvoiceResponse(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id    # type: str
        self.data = data                # type: RecognizeVATInvoiceResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = RecognizeVATInvoiceResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class RecognizeVATInvoiceResponseDataContent(TeaModel):
    def __init__(self, invoice_code=None, invoice_no=None, invoice_date=None, anti_fake_code=None, payer_name=None,
                 payer_register_no=None, payer_address=None, payer_bank_name=None, without_tax_amount=None, tax_amount=None,
                 sum_amount=None, invoice_amount=None, payee_name=None, payee_register_no=None, payee_address=None,
                 payee_bank_name=None, payee=None, checker=None, clerk=None):
        self.invoice_code = invoice_code  # type: str
        self.invoice_no = invoice_no    # type: str
        self.invoice_date = invoice_date  # type: str
        self.anti_fake_code = anti_fake_code  # type: str
        self.payer_name = payer_name    # type: str
        self.payer_register_no = payer_register_no  # type: str
        self.payer_address = payer_address  # type: str
        self.payer_bank_name = payer_bank_name  # type: str
        self.without_tax_amount = without_tax_amount  # type: str
        self.tax_amount = tax_amount    # type: str
        self.sum_amount = sum_amount    # type: str
        self.invoice_amount = invoice_amount  # type: str
        self.payee_name = payee_name    # type: str
        self.payee_register_no = payee_register_no  # type: str
        self.payee_address = payee_address  # type: str
        self.payee_bank_name = payee_bank_name  # type: str
        self.payee = payee              # type: str
        self.checker = checker          # type: str
        self.clerk = clerk              # type: str

    def validate(self):
        self.validate_required(self.invoice_code, 'invoice_code')
        self.validate_required(self.invoice_no, 'invoice_no')
        self.validate_required(self.invoice_date, 'invoice_date')
        self.validate_required(self.anti_fake_code, 'anti_fake_code')
        self.validate_required(self.payer_name, 'payer_name')
        self.validate_required(self.payer_register_no, 'payer_register_no')
        self.validate_required(self.payer_address, 'payer_address')
        self.validate_required(self.payer_bank_name, 'payer_bank_name')
        self.validate_required(self.without_tax_amount, 'without_tax_amount')
        self.validate_required(self.tax_amount, 'tax_amount')
        self.validate_required(self.sum_amount, 'sum_amount')
        self.validate_required(self.invoice_amount, 'invoice_amount')
        self.validate_required(self.payee_name, 'payee_name')
        self.validate_required(self.payee_register_no, 'payee_register_no')
        self.validate_required(self.payee_address, 'payee_address')
        self.validate_required(self.payee_bank_name, 'payee_bank_name')
        self.validate_required(self.payee, 'payee')
        self.validate_required(self.checker, 'checker')
        self.validate_required(self.clerk, 'clerk')

    def to_map(self):
        result = {}
        result['InvoiceCode'] = self.invoice_code
        result['InvoiceNo'] = self.invoice_no
        result['InvoiceDate'] = self.invoice_date
        result['AntiFakeCode'] = self.anti_fake_code
        result['PayerName'] = self.payer_name
        result['PayerRegisterNo'] = self.payer_register_no
        result['PayerAddress'] = self.payer_address
        result['PayerBankName'] = self.payer_bank_name
        result['WithoutTaxAmount'] = self.without_tax_amount
        result['TaxAmount'] = self.tax_amount
        result['SumAmount'] = self.sum_amount
        result['InvoiceAmount'] = self.invoice_amount
        result['PayeeName'] = self.payee_name
        result['PayeeRegisterNo'] = self.payee_register_no
        result['PayeeAddress'] = self.payee_address
        result['PayeeBankName'] = self.payee_bank_name
        result['Payee'] = self.payee
        result['Checker'] = self.checker
        result['Clerk'] = self.clerk
        return result

    def from_map(self, map={}):
        self.invoice_code = map.get('InvoiceCode')
        self.invoice_no = map.get('InvoiceNo')
        self.invoice_date = map.get('InvoiceDate')
        self.anti_fake_code = map.get('AntiFakeCode')
        self.payer_name = map.get('PayerName')
        self.payer_register_no = map.get('PayerRegisterNo')
        self.payer_address = map.get('PayerAddress')
        self.payer_bank_name = map.get('PayerBankName')
        self.without_tax_amount = map.get('WithoutTaxAmount')
        self.tax_amount = map.get('TaxAmount')
        self.sum_amount = map.get('SumAmount')
        self.invoice_amount = map.get('InvoiceAmount')
        self.payee_name = map.get('PayeeName')
        self.payee_register_no = map.get('PayeeRegisterNo')
        self.payee_address = map.get('PayeeAddress')
        self.payee_bank_name = map.get('PayeeBankName')
        self.payee = map.get('Payee')
        self.checker = map.get('Checker')
        self.clerk = map.get('Clerk')
        return self


class RecognizeVATInvoiceResponseDataBox(TeaModel):
    def __init__(self, invoice_codes=None, invoice_noes=None, invoice_dates=None, invoice_fake_codes=None,
                 payer_names=None, payer_register_noes=None, payer_addresses=None, payer_bank_names=None,
                 without_tax_amounts=None, tax_amounts=None, sum_amounts=None, invoice_amounts=None, payee_names=None,
                 payee_register_noes=None, payee_addresses=None, payee_bank_names=None, payees=None, checkers=None, clerks=None):
        self.invoice_codes = invoice_codes  # type: List[float]
        self.invoice_noes = invoice_noes  # type: List[float]
        self.invoice_dates = invoice_dates  # type: List[float]
        self.invoice_fake_codes = invoice_fake_codes  # type: List[float]
        self.payer_names = payer_names  # type: List[float]
        self.payer_register_noes = payer_register_noes  # type: List[float]
        self.payer_addresses = payer_addresses  # type: List[float]
        self.payer_bank_names = payer_bank_names  # type: List[float]
        self.without_tax_amounts = without_tax_amounts  # type: List[float]
        self.tax_amounts = tax_amounts  # type: List[float]
        self.sum_amounts = sum_amounts  # type: List[float]
        self.invoice_amounts = invoice_amounts  # type: List[float]
        self.payee_names = payee_names  # type: List[float]
        self.payee_register_noes = payee_register_noes  # type: List[float]
        self.payee_addresses = payee_addresses  # type: List[float]
        self.payee_bank_names = payee_bank_names  # type: List[float]
        self.payees = payees            # type: List[float]
        self.checkers = checkers        # type: List[float]
        self.clerks = clerks            # type: List[float]

    def validate(self):
        self.validate_required(self.invoice_codes, 'invoice_codes')
        self.validate_required(self.invoice_noes, 'invoice_noes')
        self.validate_required(self.invoice_dates, 'invoice_dates')
        self.validate_required(self.invoice_fake_codes, 'invoice_fake_codes')
        self.validate_required(self.payer_names, 'payer_names')
        self.validate_required(self.payer_register_noes, 'payer_register_noes')
        self.validate_required(self.payer_addresses, 'payer_addresses')
        self.validate_required(self.payer_bank_names, 'payer_bank_names')
        self.validate_required(self.without_tax_amounts, 'without_tax_amounts')
        self.validate_required(self.tax_amounts, 'tax_amounts')
        self.validate_required(self.sum_amounts, 'sum_amounts')
        self.validate_required(self.invoice_amounts, 'invoice_amounts')
        self.validate_required(self.payee_names, 'payee_names')
        self.validate_required(self.payee_register_noes, 'payee_register_noes')
        self.validate_required(self.payee_addresses, 'payee_addresses')
        self.validate_required(self.payee_bank_names, 'payee_bank_names')
        self.validate_required(self.payees, 'payees')
        self.validate_required(self.checkers, 'checkers')
        self.validate_required(self.clerks, 'clerks')

    def to_map(self):
        result = {}
        result['InvoiceCodes'] = self.invoice_codes
        result['InvoiceNoes'] = self.invoice_noes
        result['InvoiceDates'] = self.invoice_dates
        result['InvoiceFakeCodes'] = self.invoice_fake_codes
        result['PayerNames'] = self.payer_names
        result['PayerRegisterNoes'] = self.payer_register_noes
        result['PayerAddresses'] = self.payer_addresses
        result['PayerBankNames'] = self.payer_bank_names
        result['WithoutTaxAmounts'] = self.without_tax_amounts
        result['TaxAmounts'] = self.tax_amounts
        result['SumAmounts'] = self.sum_amounts
        result['InvoiceAmounts'] = self.invoice_amounts
        result['PayeeNames'] = self.payee_names
        result['PayeeRegisterNoes'] = self.payee_register_noes
        result['PayeeAddresses'] = self.payee_addresses
        result['PayeeBankNames'] = self.payee_bank_names
        result['Payees'] = self.payees
        result['Checkers'] = self.checkers
        result['Clerks'] = self.clerks
        return result

    def from_map(self, map={}):
        self.invoice_codes = map.get('InvoiceCodes')
        self.invoice_noes = map.get('InvoiceNoes')
        self.invoice_dates = map.get('InvoiceDates')
        self.invoice_fake_codes = map.get('InvoiceFakeCodes')
        self.payer_names = map.get('PayerNames')
        self.payer_register_noes = map.get('PayerRegisterNoes')
        self.payer_addresses = map.get('PayerAddresses')
        self.payer_bank_names = map.get('PayerBankNames')
        self.without_tax_amounts = map.get('WithoutTaxAmounts')
        self.tax_amounts = map.get('TaxAmounts')
        self.sum_amounts = map.get('SumAmounts')
        self.invoice_amounts = map.get('InvoiceAmounts')
        self.payee_names = map.get('PayeeNames')
        self.payee_register_noes = map.get('PayeeRegisterNoes')
        self.payee_addresses = map.get('PayeeAddresses')
        self.payee_bank_names = map.get('PayeeBankNames')
        self.payees = map.get('Payees')
        self.checkers = map.get('Checkers')
        self.clerks = map.get('Clerks')
        return self


class RecognizeVATInvoiceResponseData(TeaModel):
    def __init__(self, content=None, box=None):
        self.content = content          # type: RecognizeVATInvoiceResponseDataContent
        self.box = box                  # type: RecognizeVATInvoiceResponseDataBox

    def validate(self):
        self.validate_required(self.content, 'content')
        if self.content:
            self.content.validate()
        self.validate_required(self.box, 'box')
        if self.box:
            self.box.validate()

    def to_map(self):
        result = {}
        if self.content is not None:
            result['Content'] = self.content.to_map()
        else:
            result['Content'] = None
        if self.box is not None:
            result['Box'] = self.box.to_map()
        else:
            result['Box'] = None
        return result

    def from_map(self, map={}):
        if map.get('Content') is not None:
            temp_model = RecognizeVATInvoiceResponseDataContent()
            self.content = temp_model.from_map(map['Content'])
        else:
            self.content = None
        if map.get('Box') is not None:
            temp_model = RecognizeVATInvoiceResponseDataBox()
            self.box = temp_model.from_map(map['Box'])
        else:
            self.box = None
        return self


class RecognizeVATInvoiceAdvanceRequest(TeaModel):
    def __init__(self, file_urlobject=None, file_type=None):
        self.file_urlobject = file_urlobject  # type: BinaryIO
        self.file_type = file_type      # type: str

    def validate(self):
        self.validate_required(self.file_urlobject, 'file_urlobject')
        self.validate_required(self.file_type, 'file_type')

    def to_map(self):
        result = {}
        result['FileURLObject'] = self.file_urlobject
        result['FileType'] = self.file_type
        return result

    def from_map(self, map={}):
        self.file_urlobject = map.get('FileURLObject')
        self.file_type = map.get('FileType')
        return self


class RecognizeCharacterRequest(TeaModel):
    def __init__(self, image_url=None, min_height=None, output_probability=None):
        self.image_url = image_url      # type: str
        self.min_height = min_height    # type: int
        self.output_probability = output_probability  # type: bool

    def validate(self):
        self.validate_required(self.image_url, 'image_url')
        self.validate_required(self.min_height, 'min_height')
        self.validate_required(self.output_probability, 'output_probability')

    def to_map(self):
        result = {}
        result['ImageURL'] = self.image_url
        result['MinHeight'] = self.min_height
        result['OutputProbability'] = self.output_probability
        return result

    def from_map(self, map={}):
        self.image_url = map.get('ImageURL')
        self.min_height = map.get('MinHeight')
        self.output_probability = map.get('OutputProbability')
        return self


class RecognizeCharacterResponse(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id    # type: str
        self.data = data                # type: RecognizeCharacterResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = RecognizeCharacterResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class RecognizeCharacterResponseDataResultsTextRectangles(TeaModel):
    def __init__(self, angle=None, left=None, top=None, width=None, height=None):
        self.angle = angle              # type: int
        self.left = left                # type: int
        self.top = top                  # type: int
        self.width = width              # type: int
        self.height = height            # type: int

    def validate(self):
        self.validate_required(self.angle, 'angle')
        self.validate_required(self.left, 'left')
        self.validate_required(self.top, 'top')
        self.validate_required(self.width, 'width')
        self.validate_required(self.height, 'height')

    def to_map(self):
        result = {}
        result['Angle'] = self.angle
        result['Left'] = self.left
        result['Top'] = self.top
        result['Width'] = self.width
        result['Height'] = self.height
        return result

    def from_map(self, map={}):
        self.angle = map.get('Angle')
        self.left = map.get('Left')
        self.top = map.get('Top')
        self.width = map.get('Width')
        self.height = map.get('Height')
        return self


class RecognizeCharacterResponseDataResults(TeaModel):
    def __init__(self, probability=None, text=None, text_rectangles=None):
        self.probability = probability  # type: float
        self.text = text                # type: str
        self.text_rectangles = text_rectangles  # type: RecognizeCharacterResponseDataResultsTextRectangles

    def validate(self):
        self.validate_required(self.probability, 'probability')
        self.validate_required(self.text, 'text')
        self.validate_required(self.text_rectangles, 'text_rectangles')
        if self.text_rectangles:
            self.text_rectangles.validate()

    def to_map(self):
        result = {}
        result['Probability'] = self.probability
        result['Text'] = self.text
        if self.text_rectangles is not None:
            result['TextRectangles'] = self.text_rectangles.to_map()
        else:
            result['TextRectangles'] = None
        return result

    def from_map(self, map={}):
        self.probability = map.get('Probability')
        self.text = map.get('Text')
        if map.get('TextRectangles') is not None:
            temp_model = RecognizeCharacterResponseDataResultsTextRectangles()
            self.text_rectangles = temp_model.from_map(map['TextRectangles'])
        else:
            self.text_rectangles = None
        return self


class RecognizeCharacterResponseData(TeaModel):
    def __init__(self, results=None):
        self.results = results          # type: List[RecognizeCharacterResponseDataResults]

    def validate(self):
        self.validate_required(self.results, 'results')
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        else:
            result['Results'] = None
        return result

    def from_map(self, map={}):
        self.results = []
        if map.get('Results') is not None:
            for k in map.get('Results'):
                temp_model = RecognizeCharacterResponseDataResults()
                self.results.append(temp_model.from_map(k))
        else:
            self.results = None
        return self


class RecognizeCharacterAdvanceRequest(TeaModel):
    def __init__(self, image_urlobject=None, min_height=None, output_probability=None):
        self.image_urlobject = image_urlobject  # type: BinaryIO
        self.min_height = min_height    # type: int
        self.output_probability = output_probability  # type: bool

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')
        self.validate_required(self.min_height, 'min_height')
        self.validate_required(self.output_probability, 'output_probability')

    def to_map(self):
        result = {}
        result['ImageURLObject'] = self.image_urlobject
        result['MinHeight'] = self.min_height
        result['OutputProbability'] = self.output_probability
        return result

    def from_map(self, map={}):
        self.image_urlobject = map.get('ImageURLObject')
        self.min_height = map.get('MinHeight')
        self.output_probability = map.get('OutputProbability')
        return self


class RecognizeTaxiInvoiceRequest(TeaModel):
    def __init__(self, image_url=None):
        self.image_url = image_url      # type: str

    def validate(self):
        self.validate_required(self.image_url, 'image_url')

    def to_map(self):
        result = {}
        result['ImageURL'] = self.image_url
        return result

    def from_map(self, map={}):
        self.image_url = map.get('ImageURL')
        return self


class RecognizeTaxiInvoiceResponse(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id    # type: str
        self.data = data                # type: RecognizeTaxiInvoiceResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = RecognizeTaxiInvoiceResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class RecognizeTaxiInvoiceResponseDataInvoicesItemsItemRoiCenter(TeaModel):
    def __init__(self, x=None, y=None):
        self.x = x                      # type: float
        self.y = y                      # type: float

    def validate(self):
        self.validate_required(self.x, 'x')
        self.validate_required(self.y, 'y')

    def to_map(self):
        result = {}
        result['X'] = self.x
        result['Y'] = self.y
        return result

    def from_map(self, map={}):
        self.x = map.get('X')
        self.y = map.get('Y')
        return self


class RecognizeTaxiInvoiceResponseDataInvoicesItemsItemRoiSize(TeaModel):
    def __init__(self, h=None, w=None):
        self.h = h                      # type: float
        self.w = w                      # type: float

    def validate(self):
        self.validate_required(self.h, 'h')
        self.validate_required(self.w, 'w')

    def to_map(self):
        result = {}
        result['H'] = self.h
        result['W'] = self.w
        return result

    def from_map(self, map={}):
        self.h = map.get('H')
        self.w = map.get('W')
        return self


class RecognizeTaxiInvoiceResponseDataInvoicesItemsItemRoi(TeaModel):
    def __init__(self, angle=None, center=None, size=None):
        self.angle = angle              # type: float
        self.center = center            # type: RecognizeTaxiInvoiceResponseDataInvoicesItemsItemRoiCenter
        self.size = size                # type: RecognizeTaxiInvoiceResponseDataInvoicesItemsItemRoiSize

    def validate(self):
        self.validate_required(self.angle, 'angle')
        self.validate_required(self.center, 'center')
        if self.center:
            self.center.validate()
        self.validate_required(self.size, 'size')
        if self.size:
            self.size.validate()

    def to_map(self):
        result = {}
        result['Angle'] = self.angle
        if self.center is not None:
            result['Center'] = self.center.to_map()
        else:
            result['Center'] = None
        if self.size is not None:
            result['Size'] = self.size.to_map()
        else:
            result['Size'] = None
        return result

    def from_map(self, map={}):
        self.angle = map.get('Angle')
        if map.get('Center') is not None:
            temp_model = RecognizeTaxiInvoiceResponseDataInvoicesItemsItemRoiCenter()
            self.center = temp_model.from_map(map['Center'])
        else:
            self.center = None
        if map.get('Size') is not None:
            temp_model = RecognizeTaxiInvoiceResponseDataInvoicesItemsItemRoiSize()
            self.size = temp_model.from_map(map['Size'])
        else:
            self.size = None
        return self


class RecognizeTaxiInvoiceResponseDataInvoicesItems(TeaModel):
    def __init__(self, text=None, item_roi=None):
        self.text = text                # type: str
        self.item_roi = item_roi        # type: RecognizeTaxiInvoiceResponseDataInvoicesItemsItemRoi

    def validate(self):
        self.validate_required(self.text, 'text')
        self.validate_required(self.item_roi, 'item_roi')
        if self.item_roi:
            self.item_roi.validate()

    def to_map(self):
        result = {}
        result['Text'] = self.text
        if self.item_roi is not None:
            result['ItemRoi'] = self.item_roi.to_map()
        else:
            result['ItemRoi'] = None
        return result

    def from_map(self, map={}):
        self.text = map.get('Text')
        if map.get('ItemRoi') is not None:
            temp_model = RecognizeTaxiInvoiceResponseDataInvoicesItemsItemRoi()
            self.item_roi = temp_model.from_map(map['ItemRoi'])
        else:
            self.item_roi = None
        return self


class RecognizeTaxiInvoiceResponseDataInvoicesInvoiceRoi(TeaModel):
    def __init__(self, h=None, w=None, x=None, y=None):
        self.h = h                      # type: float
        self.w = w                      # type: float
        self.x = x                      # type: float
        self.y = y                      # type: float

    def validate(self):
        self.validate_required(self.h, 'h')
        self.validate_required(self.w, 'w')
        self.validate_required(self.x, 'x')
        self.validate_required(self.y, 'y')

    def to_map(self):
        result = {}
        result['H'] = self.h
        result['W'] = self.w
        result['X'] = self.x
        result['Y'] = self.y
        return result

    def from_map(self, map={}):
        self.h = map.get('H')
        self.w = map.get('W')
        self.x = map.get('X')
        self.y = map.get('Y')
        return self


class RecognizeTaxiInvoiceResponseDataInvoices(TeaModel):
    def __init__(self, rotate_type=None, items=None, invoice_roi=None):
        self.rotate_type = rotate_type  # type: int
        self.items = items              # type: List[RecognizeTaxiInvoiceResponseDataInvoicesItems]
        self.invoice_roi = invoice_roi  # type: RecognizeTaxiInvoiceResponseDataInvoicesInvoiceRoi

    def validate(self):
        self.validate_required(self.rotate_type, 'rotate_type')
        self.validate_required(self.items, 'items')
        if self.items:
            for k in self.items:
                if k:
                    k.validate()
        self.validate_required(self.invoice_roi, 'invoice_roi')
        if self.invoice_roi:
            self.invoice_roi.validate()

    def to_map(self):
        result = {}
        result['RotateType'] = self.rotate_type
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        else:
            result['Items'] = None
        if self.invoice_roi is not None:
            result['InvoiceRoi'] = self.invoice_roi.to_map()
        else:
            result['InvoiceRoi'] = None
        return result

    def from_map(self, map={}):
        self.rotate_type = map.get('RotateType')
        self.items = []
        if map.get('Items') is not None:
            for k in map.get('Items'):
                temp_model = RecognizeTaxiInvoiceResponseDataInvoicesItems()
                self.items.append(temp_model.from_map(k))
        else:
            self.items = None
        if map.get('InvoiceRoi') is not None:
            temp_model = RecognizeTaxiInvoiceResponseDataInvoicesInvoiceRoi()
            self.invoice_roi = temp_model.from_map(map['InvoiceRoi'])
        else:
            self.invoice_roi = None
        return self


class RecognizeTaxiInvoiceResponseData(TeaModel):
    def __init__(self, invoices=None):
        self.invoices = invoices        # type: List[RecognizeTaxiInvoiceResponseDataInvoices]

    def validate(self):
        self.validate_required(self.invoices, 'invoices')
        if self.invoices:
            for k in self.invoices:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Invoices'] = []
        if self.invoices is not None:
            for k in self.invoices:
                result['Invoices'].append(k.to_map() if k else None)
        else:
            result['Invoices'] = None
        return result

    def from_map(self, map={}):
        self.invoices = []
        if map.get('Invoices') is not None:
            for k in map.get('Invoices'):
                temp_model = RecognizeTaxiInvoiceResponseDataInvoices()
                self.invoices.append(temp_model.from_map(k))
        else:
            self.invoices = None
        return self


class RecognizeTaxiInvoiceAdvanceRequest(TeaModel):
    def __init__(self, image_urlobject=None):
        self.image_urlobject = image_urlobject  # type: BinaryIO

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        result = {}
        result['ImageURLObject'] = self.image_urlobject
        return result

    def from_map(self, map={}):
        self.image_urlobject = map.get('ImageURLObject')
        return self


class RecognizeIdentityCardRequest(TeaModel):
    def __init__(self, image_url=None, side=None):
        self.image_url = image_url      # type: str
        self.side = side                # type: str

    def validate(self):
        self.validate_required(self.image_url, 'image_url')
        self.validate_required(self.side, 'side')

    def to_map(self):
        result = {}
        result['ImageURL'] = self.image_url
        result['Side'] = self.side
        return result

    def from_map(self, map={}):
        self.image_url = map.get('ImageURL')
        self.side = map.get('Side')
        return self


class RecognizeIdentityCardResponse(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id    # type: str
        self.data = data                # type: RecognizeIdentityCardResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = RecognizeIdentityCardResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class RecognizeIdentityCardResponseDataFrontResultCardAreas(TeaModel):
    def __init__(self, x=None, y=None):
        self.x = x                      # type: float
        self.y = y                      # type: float

    def validate(self):
        self.validate_required(self.x, 'x')
        self.validate_required(self.y, 'y')

    def to_map(self):
        result = {}
        result['X'] = self.x
        result['Y'] = self.y
        return result

    def from_map(self, map={}):
        self.x = map.get('X')
        self.y = map.get('Y')
        return self


class RecognizeIdentityCardResponseDataFrontResultFaceRectVertices(TeaModel):
    def __init__(self, x=None, y=None):
        self.x = x                      # type: float
        self.y = y                      # type: float

    def validate(self):
        self.validate_required(self.x, 'x')
        self.validate_required(self.y, 'y')

    def to_map(self):
        result = {}
        result['X'] = self.x
        result['Y'] = self.y
        return result

    def from_map(self, map={}):
        self.x = map.get('X')
        self.y = map.get('Y')
        return self


class RecognizeIdentityCardResponseDataFrontResultFaceRectangleCenter(TeaModel):
    def __init__(self, x=None, y=None):
        self.x = x                      # type: float
        self.y = y                      # type: float

    def validate(self):
        self.validate_required(self.x, 'x')
        self.validate_required(self.y, 'y')

    def to_map(self):
        result = {}
        result['X'] = self.x
        result['Y'] = self.y
        return result

    def from_map(self, map={}):
        self.x = map.get('X')
        self.y = map.get('Y')
        return self


class RecognizeIdentityCardResponseDataFrontResultFaceRectangleSize(TeaModel):
    def __init__(self, height=None, width=None):
        self.height = height            # type: float
        self.width = width              # type: float

    def validate(self):
        self.validate_required(self.height, 'height')
        self.validate_required(self.width, 'width')

    def to_map(self):
        result = {}
        result['Height'] = self.height
        result['Width'] = self.width
        return result

    def from_map(self, map={}):
        self.height = map.get('Height')
        self.width = map.get('Width')
        return self


class RecognizeIdentityCardResponseDataFrontResultFaceRectangle(TeaModel):
    def __init__(self, angle=None, center=None, size=None):
        self.angle = angle              # type: float
        self.center = center            # type: RecognizeIdentityCardResponseDataFrontResultFaceRectangleCenter
        self.size = size                # type: RecognizeIdentityCardResponseDataFrontResultFaceRectangleSize

    def validate(self):
        self.validate_required(self.angle, 'angle')
        self.validate_required(self.center, 'center')
        if self.center:
            self.center.validate()
        self.validate_required(self.size, 'size')
        if self.size:
            self.size.validate()

    def to_map(self):
        result = {}
        result['Angle'] = self.angle
        if self.center is not None:
            result['Center'] = self.center.to_map()
        else:
            result['Center'] = None
        if self.size is not None:
            result['Size'] = self.size.to_map()
        else:
            result['Size'] = None
        return result

    def from_map(self, map={}):
        self.angle = map.get('Angle')
        if map.get('Center') is not None:
            temp_model = RecognizeIdentityCardResponseDataFrontResultFaceRectangleCenter()
            self.center = temp_model.from_map(map['Center'])
        else:
            self.center = None
        if map.get('Size') is not None:
            temp_model = RecognizeIdentityCardResponseDataFrontResultFaceRectangleSize()
            self.size = temp_model.from_map(map['Size'])
        else:
            self.size = None
        return self


class RecognizeIdentityCardResponseDataFrontResult(TeaModel):
    def __init__(self, address=None, name=None, nationality=None, idnumber=None, gender=None, birth_date=None,
                 card_areas=None, face_rect_vertices=None, face_rectangle=None):
        self.address = address          # type: str
        self.name = name                # type: str
        self.nationality = nationality  # type: str
        self.idnumber = idnumber        # type: str
        self.gender = gender            # type: str
        self.birth_date = birth_date    # type: str
        self.card_areas = card_areas    # type: List[RecognizeIdentityCardResponseDataFrontResultCardAreas]
        self.face_rect_vertices = face_rect_vertices  # type: List[RecognizeIdentityCardResponseDataFrontResultFaceRectVertices]
        self.face_rectangle = face_rectangle  # type: RecognizeIdentityCardResponseDataFrontResultFaceRectangle

    def validate(self):
        self.validate_required(self.address, 'address')
        self.validate_required(self.name, 'name')
        self.validate_required(self.nationality, 'nationality')
        self.validate_required(self.idnumber, 'idnumber')
        self.validate_required(self.gender, 'gender')
        self.validate_required(self.birth_date, 'birth_date')
        self.validate_required(self.card_areas, 'card_areas')
        if self.card_areas:
            for k in self.card_areas:
                if k:
                    k.validate()
        self.validate_required(self.face_rect_vertices, 'face_rect_vertices')
        if self.face_rect_vertices:
            for k in self.face_rect_vertices:
                if k:
                    k.validate()
        self.validate_required(self.face_rectangle, 'face_rectangle')
        if self.face_rectangle:
            self.face_rectangle.validate()

    def to_map(self):
        result = {}
        result['Address'] = self.address
        result['Name'] = self.name
        result['Nationality'] = self.nationality
        result['IDNumber'] = self.idnumber
        result['Gender'] = self.gender
        result['BirthDate'] = self.birth_date
        result['CardAreas'] = []
        if self.card_areas is not None:
            for k in self.card_areas:
                result['CardAreas'].append(k.to_map() if k else None)
        else:
            result['CardAreas'] = None
        result['FaceRectVertices'] = []
        if self.face_rect_vertices is not None:
            for k in self.face_rect_vertices:
                result['FaceRectVertices'].append(k.to_map() if k else None)
        else:
            result['FaceRectVertices'] = None
        if self.face_rectangle is not None:
            result['FaceRectangle'] = self.face_rectangle.to_map()
        else:
            result['FaceRectangle'] = None
        return result

    def from_map(self, map={}):
        self.address = map.get('Address')
        self.name = map.get('Name')
        self.nationality = map.get('Nationality')
        self.idnumber = map.get('IDNumber')
        self.gender = map.get('Gender')
        self.birth_date = map.get('BirthDate')
        self.card_areas = []
        if map.get('CardAreas') is not None:
            for k in map.get('CardAreas'):
                temp_model = RecognizeIdentityCardResponseDataFrontResultCardAreas()
                self.card_areas.append(temp_model.from_map(k))
        else:
            self.card_areas = None
        self.face_rect_vertices = []
        if map.get('FaceRectVertices') is not None:
            for k in map.get('FaceRectVertices'):
                temp_model = RecognizeIdentityCardResponseDataFrontResultFaceRectVertices()
                self.face_rect_vertices.append(temp_model.from_map(k))
        else:
            self.face_rect_vertices = None
        if map.get('FaceRectangle') is not None:
            temp_model = RecognizeIdentityCardResponseDataFrontResultFaceRectangle()
            self.face_rectangle = temp_model.from_map(map['FaceRectangle'])
        else:
            self.face_rectangle = None
        return self


class RecognizeIdentityCardResponseDataBackResult(TeaModel):
    def __init__(self, start_date=None, end_date=None, issue=None):
        self.start_date = start_date    # type: str
        self.end_date = end_date        # type: str
        self.issue = issue              # type: str

    def validate(self):
        self.validate_required(self.start_date, 'start_date')
        self.validate_required(self.end_date, 'end_date')
        self.validate_required(self.issue, 'issue')

    def to_map(self):
        result = {}
        result['StartDate'] = self.start_date
        result['EndDate'] = self.end_date
        result['Issue'] = self.issue
        return result

    def from_map(self, map={}):
        self.start_date = map.get('StartDate')
        self.end_date = map.get('EndDate')
        self.issue = map.get('Issue')
        return self


class RecognizeIdentityCardResponseData(TeaModel):
    def __init__(self, front_result=None, back_result=None):
        self.front_result = front_result  # type: RecognizeIdentityCardResponseDataFrontResult
        self.back_result = back_result  # type: RecognizeIdentityCardResponseDataBackResult

    def validate(self):
        self.validate_required(self.front_result, 'front_result')
        if self.front_result:
            self.front_result.validate()
        self.validate_required(self.back_result, 'back_result')
        if self.back_result:
            self.back_result.validate()

    def to_map(self):
        result = {}
        if self.front_result is not None:
            result['FrontResult'] = self.front_result.to_map()
        else:
            result['FrontResult'] = None
        if self.back_result is not None:
            result['BackResult'] = self.back_result.to_map()
        else:
            result['BackResult'] = None
        return result

    def from_map(self, map={}):
        if map.get('FrontResult') is not None:
            temp_model = RecognizeIdentityCardResponseDataFrontResult()
            self.front_result = temp_model.from_map(map['FrontResult'])
        else:
            self.front_result = None
        if map.get('BackResult') is not None:
            temp_model = RecognizeIdentityCardResponseDataBackResult()
            self.back_result = temp_model.from_map(map['BackResult'])
        else:
            self.back_result = None
        return self


class RecognizeIdentityCardAdvanceRequest(TeaModel):
    def __init__(self, image_urlobject=None, side=None):
        self.image_urlobject = image_urlobject  # type: BinaryIO
        self.side = side                # type: str

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')
        self.validate_required(self.side, 'side')

    def to_map(self):
        result = {}
        result['ImageURLObject'] = self.image_urlobject
        result['Side'] = self.side
        return result

    def from_map(self, map={}):
        self.image_urlobject = map.get('ImageURLObject')
        self.side = map.get('Side')
        return self


class RecognizeLicensePlateRequest(TeaModel):
    def __init__(self, image_url=None):
        self.image_url = image_url      # type: str

    def validate(self):
        self.validate_required(self.image_url, 'image_url')

    def to_map(self):
        result = {}
        result['ImageURL'] = self.image_url
        return result

    def from_map(self, map={}):
        self.image_url = map.get('ImageURL')
        return self


class RecognizeLicensePlateResponse(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id    # type: str
        self.data = data                # type: RecognizeLicensePlateResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = RecognizeLicensePlateResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class RecognizeLicensePlateResponseDataPlatesRoi(TeaModel):
    def __init__(self, h=None, w=None, x=None, y=None):
        self.h = h                      # type: int
        self.w = w                      # type: int
        self.x = x                      # type: int
        self.y = y                      # type: int

    def validate(self):
        self.validate_required(self.h, 'h')
        self.validate_required(self.w, 'w')
        self.validate_required(self.x, 'x')
        self.validate_required(self.y, 'y')

    def to_map(self):
        result = {}
        result['H'] = self.h
        result['W'] = self.w
        result['X'] = self.x
        result['Y'] = self.y
        return result

    def from_map(self, map={}):
        self.h = map.get('H')
        self.w = map.get('W')
        self.x = map.get('X')
        self.y = map.get('Y')
        return self


class RecognizeLicensePlateResponseDataPlates(TeaModel):
    def __init__(self, confidence=None, plate_number=None, plate_type=None, plate_type_confidence=None, roi=None):
        self.confidence = confidence    # type: float
        self.plate_number = plate_number  # type: str
        self.plate_type = plate_type    # type: str
        self.plate_type_confidence = plate_type_confidence  # type: float
        self.roi = roi                  # type: RecognizeLicensePlateResponseDataPlatesRoi

    def validate(self):
        self.validate_required(self.confidence, 'confidence')
        self.validate_required(self.plate_number, 'plate_number')
        self.validate_required(self.plate_type, 'plate_type')
        self.validate_required(self.plate_type_confidence, 'plate_type_confidence')
        self.validate_required(self.roi, 'roi')
        if self.roi:
            self.roi.validate()

    def to_map(self):
        result = {}
        result['Confidence'] = self.confidence
        result['PlateNumber'] = self.plate_number
        result['PlateType'] = self.plate_type
        result['PlateTypeConfidence'] = self.plate_type_confidence
        if self.roi is not None:
            result['Roi'] = self.roi.to_map()
        else:
            result['Roi'] = None
        return result

    def from_map(self, map={}):
        self.confidence = map.get('Confidence')
        self.plate_number = map.get('PlateNumber')
        self.plate_type = map.get('PlateType')
        self.plate_type_confidence = map.get('PlateTypeConfidence')
        if map.get('Roi') is not None:
            temp_model = RecognizeLicensePlateResponseDataPlatesRoi()
            self.roi = temp_model.from_map(map['Roi'])
        else:
            self.roi = None
        return self


class RecognizeLicensePlateResponseData(TeaModel):
    def __init__(self, plates=None):
        self.plates = plates            # type: List[RecognizeLicensePlateResponseDataPlates]

    def validate(self):
        self.validate_required(self.plates, 'plates')
        if self.plates:
            for k in self.plates:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Plates'] = []
        if self.plates is not None:
            for k in self.plates:
                result['Plates'].append(k.to_map() if k else None)
        else:
            result['Plates'] = None
        return result

    def from_map(self, map={}):
        self.plates = []
        if map.get('Plates') is not None:
            for k in map.get('Plates'):
                temp_model = RecognizeLicensePlateResponseDataPlates()
                self.plates.append(temp_model.from_map(k))
        else:
            self.plates = None
        return self


class RecognizeLicensePlateAdvanceRequest(TeaModel):
    def __init__(self, image_urlobject=None):
        self.image_urlobject = image_urlobject  # type: BinaryIO

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        result = {}
        result['ImageURLObject'] = self.image_urlobject
        return result

    def from_map(self, map={}):
        self.image_urlobject = map.get('ImageURLObject')
        return self


class RecognizeTableRequest(TeaModel):
    def __init__(self, image_url=None, output_format=None, use_finance_model=None, assure_direction=None,
                 has_line=None, skip_detection=None):
        self.image_url = image_url      # type: str
        self.output_format = output_format  # type: str
        self.use_finance_model = use_finance_model  # type: bool
        self.assure_direction = assure_direction  # type: bool
        self.has_line = has_line        # type: bool
        self.skip_detection = skip_detection  # type: bool

    def validate(self):
        self.validate_required(self.image_url, 'image_url')
        self.validate_required(self.output_format, 'output_format')
        self.validate_required(self.use_finance_model, 'use_finance_model')
        self.validate_required(self.assure_direction, 'assure_direction')
        self.validate_required(self.has_line, 'has_line')
        self.validate_required(self.skip_detection, 'skip_detection')

    def to_map(self):
        result = {}
        result['ImageURL'] = self.image_url
        result['OutputFormat'] = self.output_format
        result['UseFinanceModel'] = self.use_finance_model
        result['AssureDirection'] = self.assure_direction
        result['HasLine'] = self.has_line
        result['SkipDetection'] = self.skip_detection
        return result

    def from_map(self, map={}):
        self.image_url = map.get('ImageURL')
        self.output_format = map.get('OutputFormat')
        self.use_finance_model = map.get('UseFinanceModel')
        self.assure_direction = map.get('AssureDirection')
        self.has_line = map.get('HasLine')
        self.skip_detection = map.get('SkipDetection')
        return self


class RecognizeTableResponse(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id    # type: str
        self.data = data                # type: RecognizeTableResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = RecognizeTableResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class RecognizeTableResponseDataTablesTableRowsTableColumns(TeaModel):
    def __init__(self, start_column=None, start_row=None, end_column=None, end_row=None, height=None, width=None,
                 texts=None):
        self.start_column = start_column  # type: int
        self.start_row = start_row      # type: int
        self.end_column = end_column    # type: int
        self.end_row = end_row          # type: int
        self.height = height            # type: int
        self.width = width              # type: int
        self.texts = texts              # type: List[str]

    def validate(self):
        self.validate_required(self.start_column, 'start_column')
        self.validate_required(self.start_row, 'start_row')
        self.validate_required(self.end_column, 'end_column')
        self.validate_required(self.end_row, 'end_row')
        self.validate_required(self.height, 'height')
        self.validate_required(self.width, 'width')
        self.validate_required(self.texts, 'texts')

    def to_map(self):
        result = {}
        result['StartColumn'] = self.start_column
        result['StartRow'] = self.start_row
        result['EndColumn'] = self.end_column
        result['EndRow'] = self.end_row
        result['Height'] = self.height
        result['Width'] = self.width
        result['Texts'] = self.texts
        return result

    def from_map(self, map={}):
        self.start_column = map.get('StartColumn')
        self.start_row = map.get('StartRow')
        self.end_column = map.get('EndColumn')
        self.end_row = map.get('EndRow')
        self.height = map.get('Height')
        self.width = map.get('Width')
        self.texts = map.get('Texts')
        return self


class RecognizeTableResponseDataTablesTableRows(TeaModel):
    def __init__(self, table_columns=None):
        self.table_columns = table_columns  # type: List[RecognizeTableResponseDataTablesTableRowsTableColumns]

    def validate(self):
        self.validate_required(self.table_columns, 'table_columns')
        if self.table_columns:
            for k in self.table_columns:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['TableColumns'] = []
        if self.table_columns is not None:
            for k in self.table_columns:
                result['TableColumns'].append(k.to_map() if k else None)
        else:
            result['TableColumns'] = None
        return result

    def from_map(self, map={}):
        self.table_columns = []
        if map.get('TableColumns') is not None:
            for k in map.get('TableColumns'):
                temp_model = RecognizeTableResponseDataTablesTableRowsTableColumns()
                self.table_columns.append(temp_model.from_map(k))
        else:
            self.table_columns = None
        return self


class RecognizeTableResponseDataTables(TeaModel):
    def __init__(self, table_rows=None, head=None, tail=None):
        self.table_rows = table_rows    # type: List[RecognizeTableResponseDataTablesTableRows]
        self.head = head                # type: List[str]
        self.tail = tail                # type: List[str]

    def validate(self):
        self.validate_required(self.table_rows, 'table_rows')
        if self.table_rows:
            for k in self.table_rows:
                if k:
                    k.validate()
        self.validate_required(self.head, 'head')
        self.validate_required(self.tail, 'tail')

    def to_map(self):
        result = {}
        result['TableRows'] = []
        if self.table_rows is not None:
            for k in self.table_rows:
                result['TableRows'].append(k.to_map() if k else None)
        else:
            result['TableRows'] = None
        result['Head'] = self.head
        result['Tail'] = self.tail
        return result

    def from_map(self, map={}):
        self.table_rows = []
        if map.get('TableRows') is not None:
            for k in map.get('TableRows'):
                temp_model = RecognizeTableResponseDataTablesTableRows()
                self.table_rows.append(temp_model.from_map(k))
        else:
            self.table_rows = None
        self.head = map.get('Head')
        self.tail = map.get('Tail')
        return self


class RecognizeTableResponseData(TeaModel):
    def __init__(self, file_content=None, tables=None):
        self.file_content = file_content  # type: str
        self.tables = tables            # type: List[RecognizeTableResponseDataTables]

    def validate(self):
        self.validate_required(self.file_content, 'file_content')
        self.validate_required(self.tables, 'tables')
        if self.tables:
            for k in self.tables:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['FileContent'] = self.file_content
        result['Tables'] = []
        if self.tables is not None:
            for k in self.tables:
                result['Tables'].append(k.to_map() if k else None)
        else:
            result['Tables'] = None
        return result

    def from_map(self, map={}):
        self.file_content = map.get('FileContent')
        self.tables = []
        if map.get('Tables') is not None:
            for k in map.get('Tables'):
                temp_model = RecognizeTableResponseDataTables()
                self.tables.append(temp_model.from_map(k))
        else:
            self.tables = None
        return self


class RecognizeTableAdvanceRequest(TeaModel):
    def __init__(self, image_urlobject=None, output_format=None, use_finance_model=None, assure_direction=None,
                 has_line=None, skip_detection=None):
        self.image_urlobject = image_urlobject  # type: BinaryIO
        self.output_format = output_format  # type: str
        self.use_finance_model = use_finance_model  # type: bool
        self.assure_direction = assure_direction  # type: bool
        self.has_line = has_line        # type: bool
        self.skip_detection = skip_detection  # type: bool

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')
        self.validate_required(self.output_format, 'output_format')
        self.validate_required(self.use_finance_model, 'use_finance_model')
        self.validate_required(self.assure_direction, 'assure_direction')
        self.validate_required(self.has_line, 'has_line')
        self.validate_required(self.skip_detection, 'skip_detection')

    def to_map(self):
        result = {}
        result['ImageURLObject'] = self.image_urlobject
        result['OutputFormat'] = self.output_format
        result['UseFinanceModel'] = self.use_finance_model
        result['AssureDirection'] = self.assure_direction
        result['HasLine'] = self.has_line
        result['SkipDetection'] = self.skip_detection
        return result

    def from_map(self, map={}):
        self.image_urlobject = map.get('ImageURLObject')
        self.output_format = map.get('OutputFormat')
        self.use_finance_model = map.get('UseFinanceModel')
        self.assure_direction = map.get('AssureDirection')
        self.has_line = map.get('HasLine')
        self.skip_detection = map.get('SkipDetection')
        return self


class RecognizeDrivingLicenseRequest(TeaModel):
    def __init__(self, image_url=None, side=None):
        self.image_url = image_url      # type: str
        self.side = side                # type: str

    def validate(self):
        self.validate_required(self.image_url, 'image_url')
        self.validate_required(self.side, 'side')

    def to_map(self):
        result = {}
        result['ImageURL'] = self.image_url
        result['Side'] = self.side
        return result

    def from_map(self, map={}):
        self.image_url = map.get('ImageURL')
        self.side = map.get('Side')
        return self


class RecognizeDrivingLicenseResponse(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id    # type: str
        self.data = data                # type: RecognizeDrivingLicenseResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = RecognizeDrivingLicenseResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class RecognizeDrivingLicenseResponseDataFaceResult(TeaModel):
    def __init__(self, plate_number=None, vehicle_type=None, owner=None, use_character=None, address=None,
                 model=None, vin=None, engine_number=None, register_date=None, issue_date=None):
        self.plate_number = plate_number  # type: str
        self.vehicle_type = vehicle_type  # type: str
        self.owner = owner              # type: str
        self.use_character = use_character  # type: str
        self.address = address          # type: str
        self.model = model              # type: str
        self.vin = vin                  # type: str
        self.engine_number = engine_number  # type: str
        self.register_date = register_date  # type: str
        self.issue_date = issue_date    # type: str

    def validate(self):
        self.validate_required(self.plate_number, 'plate_number')
        self.validate_required(self.vehicle_type, 'vehicle_type')
        self.validate_required(self.owner, 'owner')
        self.validate_required(self.use_character, 'use_character')
        self.validate_required(self.address, 'address')
        self.validate_required(self.model, 'model')
        self.validate_required(self.vin, 'vin')
        self.validate_required(self.engine_number, 'engine_number')
        self.validate_required(self.register_date, 'register_date')
        self.validate_required(self.issue_date, 'issue_date')

    def to_map(self):
        result = {}
        result['PlateNumber'] = self.plate_number
        result['VehicleType'] = self.vehicle_type
        result['Owner'] = self.owner
        result['UseCharacter'] = self.use_character
        result['Address'] = self.address
        result['Model'] = self.model
        result['Vin'] = self.vin
        result['EngineNumber'] = self.engine_number
        result['RegisterDate'] = self.register_date
        result['IssueDate'] = self.issue_date
        return result

    def from_map(self, map={}):
        self.plate_number = map.get('PlateNumber')
        self.vehicle_type = map.get('VehicleType')
        self.owner = map.get('Owner')
        self.use_character = map.get('UseCharacter')
        self.address = map.get('Address')
        self.model = map.get('Model')
        self.vin = map.get('Vin')
        self.engine_number = map.get('EngineNumber')
        self.register_date = map.get('RegisterDate')
        self.issue_date = map.get('IssueDate')
        return self


class RecognizeDrivingLicenseResponseDataBackResult(TeaModel):
    def __init__(self, approved_passenger_capacity=None, approved_load=None, file_number=None, gross_mass=None,
                 energy_type=None, inspection_record=None, overall_dimension=None, traction_mass=None, unladen_mass=None,
                 plate_number=None):
        self.approved_passenger_capacity = approved_passenger_capacity  # type: str
        self.approved_load = approved_load  # type: str
        self.file_number = file_number  # type: str
        self.gross_mass = gross_mass    # type: str
        self.energy_type = energy_type  # type: str
        self.inspection_record = inspection_record  # type: str
        self.overall_dimension = overall_dimension  # type: str
        self.traction_mass = traction_mass  # type: str
        self.unladen_mass = unladen_mass  # type: str
        self.plate_number = plate_number  # type: str

    def validate(self):
        self.validate_required(self.approved_passenger_capacity, 'approved_passenger_capacity')
        self.validate_required(self.approved_load, 'approved_load')
        self.validate_required(self.file_number, 'file_number')
        self.validate_required(self.gross_mass, 'gross_mass')
        self.validate_required(self.energy_type, 'energy_type')
        self.validate_required(self.inspection_record, 'inspection_record')
        self.validate_required(self.overall_dimension, 'overall_dimension')
        self.validate_required(self.traction_mass, 'traction_mass')
        self.validate_required(self.unladen_mass, 'unladen_mass')
        self.validate_required(self.plate_number, 'plate_number')

    def to_map(self):
        result = {}
        result['ApprovedPassengerCapacity'] = self.approved_passenger_capacity
        result['ApprovedLoad'] = self.approved_load
        result['FileNumber'] = self.file_number
        result['GrossMass'] = self.gross_mass
        result['EnergyType'] = self.energy_type
        result['InspectionRecord'] = self.inspection_record
        result['OverallDimension'] = self.overall_dimension
        result['TractionMass'] = self.traction_mass
        result['UnladenMass'] = self.unladen_mass
        result['PlateNumber'] = self.plate_number
        return result

    def from_map(self, map={}):
        self.approved_passenger_capacity = map.get('ApprovedPassengerCapacity')
        self.approved_load = map.get('ApprovedLoad')
        self.file_number = map.get('FileNumber')
        self.gross_mass = map.get('GrossMass')
        self.energy_type = map.get('EnergyType')
        self.inspection_record = map.get('InspectionRecord')
        self.overall_dimension = map.get('OverallDimension')
        self.traction_mass = map.get('TractionMass')
        self.unladen_mass = map.get('UnladenMass')
        self.plate_number = map.get('PlateNumber')
        return self


class RecognizeDrivingLicenseResponseData(TeaModel):
    def __init__(self, face_result=None, back_result=None):
        self.face_result = face_result  # type: RecognizeDrivingLicenseResponseDataFaceResult
        self.back_result = back_result  # type: RecognizeDrivingLicenseResponseDataBackResult

    def validate(self):
        self.validate_required(self.face_result, 'face_result')
        if self.face_result:
            self.face_result.validate()
        self.validate_required(self.back_result, 'back_result')
        if self.back_result:
            self.back_result.validate()

    def to_map(self):
        result = {}
        if self.face_result is not None:
            result['FaceResult'] = self.face_result.to_map()
        else:
            result['FaceResult'] = None
        if self.back_result is not None:
            result['BackResult'] = self.back_result.to_map()
        else:
            result['BackResult'] = None
        return result

    def from_map(self, map={}):
        if map.get('FaceResult') is not None:
            temp_model = RecognizeDrivingLicenseResponseDataFaceResult()
            self.face_result = temp_model.from_map(map['FaceResult'])
        else:
            self.face_result = None
        if map.get('BackResult') is not None:
            temp_model = RecognizeDrivingLicenseResponseDataBackResult()
            self.back_result = temp_model.from_map(map['BackResult'])
        else:
            self.back_result = None
        return self


class RecognizeDrivingLicenseAdvanceRequest(TeaModel):
    def __init__(self, image_urlobject=None, side=None):
        self.image_urlobject = image_urlobject  # type: BinaryIO
        self.side = side                # type: str

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')
        self.validate_required(self.side, 'side')

    def to_map(self):
        result = {}
        result['ImageURLObject'] = self.image_urlobject
        result['Side'] = self.side
        return result

    def from_map(self, map={}):
        self.image_urlobject = map.get('ImageURLObject')
        self.side = map.get('Side')
        return self


class RecognizeBankCardRequest(TeaModel):
    def __init__(self, image_url=None):
        self.image_url = image_url      # type: str

    def validate(self):
        self.validate_required(self.image_url, 'image_url')

    def to_map(self):
        result = {}
        result['ImageURL'] = self.image_url
        return result

    def from_map(self, map={}):
        self.image_url = map.get('ImageURL')
        return self


class RecognizeBankCardResponse(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id    # type: str
        self.data = data                # type: RecognizeBankCardResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = RecognizeBankCardResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class RecognizeBankCardResponseData(TeaModel):
    def __init__(self, bank_name=None, card_number=None, valid_date=None):
        self.bank_name = bank_name      # type: str
        self.card_number = card_number  # type: str
        self.valid_date = valid_date    # type: str

    def validate(self):
        self.validate_required(self.bank_name, 'bank_name')
        self.validate_required(self.card_number, 'card_number')
        self.validate_required(self.valid_date, 'valid_date')

    def to_map(self):
        result = {}
        result['BankName'] = self.bank_name
        result['CardNumber'] = self.card_number
        result['ValidDate'] = self.valid_date
        return result

    def from_map(self, map={}):
        self.bank_name = map.get('BankName')
        self.card_number = map.get('CardNumber')
        self.valid_date = map.get('ValidDate')
        return self


class RecognizeBankCardAdvanceRequest(TeaModel):
    def __init__(self, image_urlobject=None):
        self.image_urlobject = image_urlobject  # type: BinaryIO

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        result = {}
        result['ImageURLObject'] = self.image_urlobject
        return result

    def from_map(self, map={}):
        self.image_urlobject = map.get('ImageURLObject')
        return self


class RecognizeTrainTicketRequest(TeaModel):
    def __init__(self, image_url=None):
        self.image_url = image_url      # type: str

    def validate(self):
        self.validate_required(self.image_url, 'image_url')

    def to_map(self):
        result = {}
        result['ImageURL'] = self.image_url
        return result

    def from_map(self, map={}):
        self.image_url = map.get('ImageURL')
        return self


class RecognizeTrainTicketResponse(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id    # type: str
        self.data = data                # type: RecognizeTrainTicketResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = RecognizeTrainTicketResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class RecognizeTrainTicketResponseData(TeaModel):
    def __init__(self, date=None, destination=None, level=None, number=None, name=None, departure_station=None,
                 seat=None, price=None):
        self.date = date                # type: str
        self.destination = destination  # type: str
        self.level = level              # type: str
        self.number = number            # type: str
        self.name = name                # type: str
        self.departure_station = departure_station  # type: str
        self.seat = seat                # type: str
        self.price = price              # type: float

    def validate(self):
        self.validate_required(self.date, 'date')
        self.validate_required(self.destination, 'destination')
        self.validate_required(self.level, 'level')
        self.validate_required(self.number, 'number')
        self.validate_required(self.name, 'name')
        self.validate_required(self.departure_station, 'departure_station')
        self.validate_required(self.seat, 'seat')
        self.validate_required(self.price, 'price')

    def to_map(self):
        result = {}
        result['Date'] = self.date
        result['Destination'] = self.destination
        result['Level'] = self.level
        result['Number'] = self.number
        result['Name'] = self.name
        result['DepartureStation'] = self.departure_station
        result['Seat'] = self.seat
        result['Price'] = self.price
        return result

    def from_map(self, map={}):
        self.date = map.get('Date')
        self.destination = map.get('Destination')
        self.level = map.get('Level')
        self.number = map.get('Number')
        self.name = map.get('Name')
        self.departure_station = map.get('DepartureStation')
        self.seat = map.get('Seat')
        self.price = map.get('Price')
        return self


class RecognizeTrainTicketAdvanceRequest(TeaModel):
    def __init__(self, image_urlobject=None):
        self.image_urlobject = image_urlobject  # type: BinaryIO

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        result = {}
        result['ImageURLObject'] = self.image_urlobject
        return result

    def from_map(self, map={}):
        self.image_urlobject = map.get('ImageURLObject')
        return self


class RecognizeDriverLicenseRequest(TeaModel):
    def __init__(self, image_url=None, side=None):
        self.image_url = image_url      # type: str
        self.side = side                # type: str

    def validate(self):
        self.validate_required(self.image_url, 'image_url')
        self.validate_required(self.side, 'side')

    def to_map(self):
        result = {}
        result['ImageURL'] = self.image_url
        result['Side'] = self.side
        return result

    def from_map(self, map={}):
        self.image_url = map.get('ImageURL')
        self.side = map.get('Side')
        return self


class RecognizeDriverLicenseResponse(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id    # type: str
        self.data = data                # type: RecognizeDriverLicenseResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = RecognizeDriverLicenseResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class RecognizeDriverLicenseResponseDataFaceResult(TeaModel):
    def __init__(self, name=None, license_number=None, vehicle_type=None, start_date=None, end_date=None,
                 issue_date=None, address=None, gender=None):
        self.name = name                # type: str
        self.license_number = license_number  # type: str
        self.vehicle_type = vehicle_type  # type: str
        self.start_date = start_date    # type: str
        self.end_date = end_date        # type: str
        self.issue_date = issue_date    # type: str
        self.address = address          # type: str
        self.gender = gender            # type: str

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.license_number, 'license_number')
        self.validate_required(self.vehicle_type, 'vehicle_type')
        self.validate_required(self.start_date, 'start_date')
        self.validate_required(self.end_date, 'end_date')
        self.validate_required(self.issue_date, 'issue_date')
        self.validate_required(self.address, 'address')
        self.validate_required(self.gender, 'gender')

    def to_map(self):
        result = {}
        result['Name'] = self.name
        result['LicenseNumber'] = self.license_number
        result['VehicleType'] = self.vehicle_type
        result['StartDate'] = self.start_date
        result['EndDate'] = self.end_date
        result['IssueDate'] = self.issue_date
        result['Address'] = self.address
        result['Gender'] = self.gender
        return result

    def from_map(self, map={}):
        self.name = map.get('Name')
        self.license_number = map.get('LicenseNumber')
        self.vehicle_type = map.get('VehicleType')
        self.start_date = map.get('StartDate')
        self.end_date = map.get('EndDate')
        self.issue_date = map.get('IssueDate')
        self.address = map.get('Address')
        self.gender = map.get('Gender')
        return self


class RecognizeDriverLicenseResponseDataBackResult(TeaModel):
    def __init__(self, archive_number=None):
        self.archive_number = archive_number  # type: str

    def validate(self):
        self.validate_required(self.archive_number, 'archive_number')

    def to_map(self):
        result = {}
        result['ArchiveNumber'] = self.archive_number
        return result

    def from_map(self, map={}):
        self.archive_number = map.get('ArchiveNumber')
        return self


class RecognizeDriverLicenseResponseData(TeaModel):
    def __init__(self, face_result=None, back_result=None):
        self.face_result = face_result  # type: RecognizeDriverLicenseResponseDataFaceResult
        self.back_result = back_result  # type: RecognizeDriverLicenseResponseDataBackResult

    def validate(self):
        self.validate_required(self.face_result, 'face_result')
        if self.face_result:
            self.face_result.validate()
        self.validate_required(self.back_result, 'back_result')
        if self.back_result:
            self.back_result.validate()

    def to_map(self):
        result = {}
        if self.face_result is not None:
            result['FaceResult'] = self.face_result.to_map()
        else:
            result['FaceResult'] = None
        if self.back_result is not None:
            result['BackResult'] = self.back_result.to_map()
        else:
            result['BackResult'] = None
        return result

    def from_map(self, map={}):
        if map.get('FaceResult') is not None:
            temp_model = RecognizeDriverLicenseResponseDataFaceResult()
            self.face_result = temp_model.from_map(map['FaceResult'])
        else:
            self.face_result = None
        if map.get('BackResult') is not None:
            temp_model = RecognizeDriverLicenseResponseDataBackResult()
            self.back_result = temp_model.from_map(map['BackResult'])
        else:
            self.back_result = None
        return self


class RecognizeDriverLicenseAdvanceRequest(TeaModel):
    def __init__(self, image_urlobject=None, side=None):
        self.image_urlobject = image_urlobject  # type: BinaryIO
        self.side = side                # type: str

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')
        self.validate_required(self.side, 'side')

    def to_map(self):
        result = {}
        result['ImageURLObject'] = self.image_urlobject
        result['Side'] = self.side
        return result

    def from_map(self, map={}):
        self.image_urlobject = map.get('ImageURLObject')
        self.side = map.get('Side')
        return self


class RecognizeAccountPageRequest(TeaModel):
    def __init__(self, image_url=None):
        self.image_url = image_url      # type: str

    def validate(self):
        self.validate_required(self.image_url, 'image_url')

    def to_map(self):
        result = {}
        result['ImageURL'] = self.image_url
        return result

    def from_map(self, map={}):
        self.image_url = map.get('ImageURL')
        return self


class RecognizeAccountPageResponse(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id    # type: str
        self.data = data                # type: RecognizeAccountPageResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = RecognizeAccountPageResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class RecognizeAccountPageResponseDataInvalidStampAreas(TeaModel):
    def __init__(self, left=None, top=None, height=None, width=None):
        self.left = left                # type: int
        self.top = top                  # type: int
        self.height = height            # type: int
        self.width = width              # type: int

    def validate(self):
        self.validate_required(self.left, 'left')
        self.validate_required(self.top, 'top')
        self.validate_required(self.height, 'height')
        self.validate_required(self.width, 'width')

    def to_map(self):
        result = {}
        result['Left'] = self.left
        result['Top'] = self.top
        result['Height'] = self.height
        result['Width'] = self.width
        return result

    def from_map(self, map={}):
        self.left = map.get('Left')
        self.top = map.get('Top')
        self.height = map.get('Height')
        self.width = map.get('Width')
        return self


class RecognizeAccountPageResponseDataUndertakeStampAreas(TeaModel):
    def __init__(self, left=None, top=None, height=None, width=None):
        self.left = left                # type: int
        self.top = top                  # type: int
        self.height = height            # type: int
        self.width = width              # type: int

    def validate(self):
        self.validate_required(self.left, 'left')
        self.validate_required(self.top, 'top')
        self.validate_required(self.height, 'height')
        self.validate_required(self.width, 'width')

    def to_map(self):
        result = {}
        result['Left'] = self.left
        result['Top'] = self.top
        result['Height'] = self.height
        result['Width'] = self.width
        return result

    def from_map(self, map={}):
        self.left = map.get('Left')
        self.top = map.get('Top')
        self.height = map.get('Height')
        self.width = map.get('Width')
        return self


class RecognizeAccountPageResponseDataRegisterStampAreas(TeaModel):
    def __init__(self, left=None, top=None, height=None, width=None):
        self.left = left                # type: int
        self.top = top                  # type: int
        self.height = height            # type: int
        self.width = width              # type: int

    def validate(self):
        self.validate_required(self.left, 'left')
        self.validate_required(self.top, 'top')
        self.validate_required(self.height, 'height')
        self.validate_required(self.width, 'width')

    def to_map(self):
        result = {}
        result['Left'] = self.left
        result['Top'] = self.top
        result['Height'] = self.height
        result['Width'] = self.width
        return result

    def from_map(self, map={}):
        self.left = map.get('Left')
        self.top = map.get('Top')
        self.height = map.get('Height')
        self.width = map.get('Width')
        return self


class RecognizeAccountPageResponseDataOtherStampAreas(TeaModel):
    def __init__(self, left=None, top=None, height=None, width=None):
        self.left = left                # type: int
        self.top = top                  # type: int
        self.height = height            # type: int
        self.width = width              # type: int

    def validate(self):
        self.validate_required(self.left, 'left')
        self.validate_required(self.top, 'top')
        self.validate_required(self.height, 'height')
        self.validate_required(self.width, 'width')

    def to_map(self):
        result = {}
        result['Left'] = self.left
        result['Top'] = self.top
        result['Height'] = self.height
        result['Width'] = self.width
        return result

    def from_map(self, map={}):
        self.left = map.get('Left')
        self.top = map.get('Top')
        self.height = map.get('Height')
        self.width = map.get('Width')
        return self


class RecognizeAccountPageResponseDataTitleArea(TeaModel):
    def __init__(self, left=None, top=None, height=None, width=None):
        self.left = left                # type: int
        self.top = top                  # type: int
        self.height = height            # type: int
        self.width = width              # type: int

    def validate(self):
        self.validate_required(self.left, 'left')
        self.validate_required(self.top, 'top')
        self.validate_required(self.height, 'height')
        self.validate_required(self.width, 'width')

    def to_map(self):
        result = {}
        result['Left'] = self.left
        result['Top'] = self.top
        result['Height'] = self.height
        result['Width'] = self.width
        return result

    def from_map(self, map={}):
        self.left = map.get('Left')
        self.top = map.get('Top')
        self.height = map.get('Height')
        self.width = map.get('Width')
        return self


class RecognizeAccountPageResponseData(TeaModel):
    def __init__(self, angle=None, name=None, gender=None, relation=None, birth_place=None, nationality=None,
                 native_place=None, birth_date=None, idnumber=None, invalid_stamp_areas=None, undertake_stamp_areas=None,
                 register_stamp_areas=None, other_stamp_areas=None, title_area=None):
        self.angle = angle              # type: float
        self.name = name                # type: str
        self.gender = gender            # type: str
        self.relation = relation        # type: str
        self.birth_place = birth_place  # type: str
        self.nationality = nationality  # type: str
        self.native_place = native_place  # type: str
        self.birth_date = birth_date    # type: str
        self.idnumber = idnumber        # type: str
        self.invalid_stamp_areas = invalid_stamp_areas  # type: List[RecognizeAccountPageResponseDataInvalidStampAreas]
        self.undertake_stamp_areas = undertake_stamp_areas  # type: List[RecognizeAccountPageResponseDataUndertakeStampAreas]
        self.register_stamp_areas = register_stamp_areas  # type: List[RecognizeAccountPageResponseDataRegisterStampAreas]
        self.other_stamp_areas = other_stamp_areas  # type: List[RecognizeAccountPageResponseDataOtherStampAreas]
        self.title_area = title_area    # type: RecognizeAccountPageResponseDataTitleArea

    def validate(self):
        self.validate_required(self.angle, 'angle')
        self.validate_required(self.name, 'name')
        self.validate_required(self.gender, 'gender')
        self.validate_required(self.relation, 'relation')
        self.validate_required(self.birth_place, 'birth_place')
        self.validate_required(self.nationality, 'nationality')
        self.validate_required(self.native_place, 'native_place')
        self.validate_required(self.birth_date, 'birth_date')
        self.validate_required(self.idnumber, 'idnumber')
        self.validate_required(self.invalid_stamp_areas, 'invalid_stamp_areas')
        if self.invalid_stamp_areas:
            for k in self.invalid_stamp_areas:
                if k:
                    k.validate()
        self.validate_required(self.undertake_stamp_areas, 'undertake_stamp_areas')
        if self.undertake_stamp_areas:
            for k in self.undertake_stamp_areas:
                if k:
                    k.validate()
        self.validate_required(self.register_stamp_areas, 'register_stamp_areas')
        if self.register_stamp_areas:
            for k in self.register_stamp_areas:
                if k:
                    k.validate()
        self.validate_required(self.other_stamp_areas, 'other_stamp_areas')
        if self.other_stamp_areas:
            for k in self.other_stamp_areas:
                if k:
                    k.validate()
        self.validate_required(self.title_area, 'title_area')
        if self.title_area:
            self.title_area.validate()

    def to_map(self):
        result = {}
        result['Angle'] = self.angle
        result['Name'] = self.name
        result['Gender'] = self.gender
        result['Relation'] = self.relation
        result['BirthPlace'] = self.birth_place
        result['Nationality'] = self.nationality
        result['NativePlace'] = self.native_place
        result['BirthDate'] = self.birth_date
        result['IDNumber'] = self.idnumber
        result['InvalidStampAreas'] = []
        if self.invalid_stamp_areas is not None:
            for k in self.invalid_stamp_areas:
                result['InvalidStampAreas'].append(k.to_map() if k else None)
        else:
            result['InvalidStampAreas'] = None
        result['UndertakeStampAreas'] = []
        if self.undertake_stamp_areas is not None:
            for k in self.undertake_stamp_areas:
                result['UndertakeStampAreas'].append(k.to_map() if k else None)
        else:
            result['UndertakeStampAreas'] = None
        result['RegisterStampAreas'] = []
        if self.register_stamp_areas is not None:
            for k in self.register_stamp_areas:
                result['RegisterStampAreas'].append(k.to_map() if k else None)
        else:
            result['RegisterStampAreas'] = None
        result['OtherStampAreas'] = []
        if self.other_stamp_areas is not None:
            for k in self.other_stamp_areas:
                result['OtherStampAreas'].append(k.to_map() if k else None)
        else:
            result['OtherStampAreas'] = None
        if self.title_area is not None:
            result['TitleArea'] = self.title_area.to_map()
        else:
            result['TitleArea'] = None
        return result

    def from_map(self, map={}):
        self.angle = map.get('Angle')
        self.name = map.get('Name')
        self.gender = map.get('Gender')
        self.relation = map.get('Relation')
        self.birth_place = map.get('BirthPlace')
        self.nationality = map.get('Nationality')
        self.native_place = map.get('NativePlace')
        self.birth_date = map.get('BirthDate')
        self.idnumber = map.get('IDNumber')
        self.invalid_stamp_areas = []
        if map.get('InvalidStampAreas') is not None:
            for k in map.get('InvalidStampAreas'):
                temp_model = RecognizeAccountPageResponseDataInvalidStampAreas()
                self.invalid_stamp_areas.append(temp_model.from_map(k))
        else:
            self.invalid_stamp_areas = None
        self.undertake_stamp_areas = []
        if map.get('UndertakeStampAreas') is not None:
            for k in map.get('UndertakeStampAreas'):
                temp_model = RecognizeAccountPageResponseDataUndertakeStampAreas()
                self.undertake_stamp_areas.append(temp_model.from_map(k))
        else:
            self.undertake_stamp_areas = None
        self.register_stamp_areas = []
        if map.get('RegisterStampAreas') is not None:
            for k in map.get('RegisterStampAreas'):
                temp_model = RecognizeAccountPageResponseDataRegisterStampAreas()
                self.register_stamp_areas.append(temp_model.from_map(k))
        else:
            self.register_stamp_areas = None
        self.other_stamp_areas = []
        if map.get('OtherStampAreas') is not None:
            for k in map.get('OtherStampAreas'):
                temp_model = RecognizeAccountPageResponseDataOtherStampAreas()
                self.other_stamp_areas.append(temp_model.from_map(k))
        else:
            self.other_stamp_areas = None
        if map.get('TitleArea') is not None:
            temp_model = RecognizeAccountPageResponseDataTitleArea()
            self.title_area = temp_model.from_map(map['TitleArea'])
        else:
            self.title_area = None
        return self


class RecognizeAccountPageAdvanceRequest(TeaModel):
    def __init__(self, image_urlobject=None):
        self.image_urlobject = image_urlobject  # type: BinaryIO

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        result = {}
        result['ImageURLObject'] = self.image_urlobject
        return result

    def from_map(self, map={}):
        self.image_urlobject = map.get('ImageURLObject')
        return self


class RecognizeStampRequest(TeaModel):
    def __init__(self, image_url=None):
        self.image_url = image_url      # type: str

    def validate(self):
        self.validate_required(self.image_url, 'image_url')

    def to_map(self):
        result = {}
        result['ImageURL'] = self.image_url
        return result

    def from_map(self, map={}):
        self.image_url = map.get('ImageURL')
        return self


class RecognizeStampResponse(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id    # type: str
        self.data = data                # type: RecognizeStampResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = RecognizeStampResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class RecognizeStampResponseDataResultsGeneralText(TeaModel):
    def __init__(self, content=None, confidence=None):
        self.content = content          # type: str
        self.confidence = confidence    # type: float

    def validate(self):
        self.validate_required(self.content, 'content')
        self.validate_required(self.confidence, 'confidence')

    def to_map(self):
        result = {}
        result['Content'] = self.content
        result['Confidence'] = self.confidence
        return result

    def from_map(self, map={}):
        self.content = map.get('Content')
        self.confidence = map.get('Confidence')
        return self


class RecognizeStampResponseDataResultsRoi(TeaModel):
    def __init__(self, left=None, top=None, width=None, height=None):
        self.left = left                # type: int
        self.top = top                  # type: int
        self.width = width              # type: int
        self.height = height            # type: int

    def validate(self):
        self.validate_required(self.left, 'left')
        self.validate_required(self.top, 'top')
        self.validate_required(self.width, 'width')
        self.validate_required(self.height, 'height')

    def to_map(self):
        result = {}
        result['Left'] = self.left
        result['Top'] = self.top
        result['Width'] = self.width
        result['Height'] = self.height
        return result

    def from_map(self, map={}):
        self.left = map.get('Left')
        self.top = map.get('Top')
        self.width = map.get('Width')
        self.height = map.get('Height')
        return self


class RecognizeStampResponseDataResultsText(TeaModel):
    def __init__(self, content=None, confidence=None):
        self.content = content          # type: str
        self.confidence = confidence    # type: float

    def validate(self):
        self.validate_required(self.content, 'content')
        self.validate_required(self.confidence, 'confidence')

    def to_map(self):
        result = {}
        result['Content'] = self.content
        result['Confidence'] = self.confidence
        return result

    def from_map(self, map={}):
        self.content = map.get('Content')
        self.confidence = map.get('Confidence')
        return self


class RecognizeStampResponseDataResults(TeaModel):
    def __init__(self, general_text=None, roi=None, text=None):
        self.general_text = general_text  # type: List[RecognizeStampResponseDataResultsGeneralText]
        self.roi = roi                  # type: RecognizeStampResponseDataResultsRoi
        self.text = text                # type: RecognizeStampResponseDataResultsText

    def validate(self):
        self.validate_required(self.general_text, 'general_text')
        if self.general_text:
            for k in self.general_text:
                if k:
                    k.validate()
        self.validate_required(self.roi, 'roi')
        if self.roi:
            self.roi.validate()
        self.validate_required(self.text, 'text')
        if self.text:
            self.text.validate()

    def to_map(self):
        result = {}
        result['GeneralText'] = []
        if self.general_text is not None:
            for k in self.general_text:
                result['GeneralText'].append(k.to_map() if k else None)
        else:
            result['GeneralText'] = None
        if self.roi is not None:
            result['Roi'] = self.roi.to_map()
        else:
            result['Roi'] = None
        if self.text is not None:
            result['Text'] = self.text.to_map()
        else:
            result['Text'] = None
        return result

    def from_map(self, map={}):
        self.general_text = []
        if map.get('GeneralText') is not None:
            for k in map.get('GeneralText'):
                temp_model = RecognizeStampResponseDataResultsGeneralText()
                self.general_text.append(temp_model.from_map(k))
        else:
            self.general_text = None
        if map.get('Roi') is not None:
            temp_model = RecognizeStampResponseDataResultsRoi()
            self.roi = temp_model.from_map(map['Roi'])
        else:
            self.roi = None
        if map.get('Text') is not None:
            temp_model = RecognizeStampResponseDataResultsText()
            self.text = temp_model.from_map(map['Text'])
        else:
            self.text = None
        return self


class RecognizeStampResponseData(TeaModel):
    def __init__(self, results=None):
        self.results = results          # type: List[RecognizeStampResponseDataResults]

    def validate(self):
        self.validate_required(self.results, 'results')
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        else:
            result['Results'] = None
        return result

    def from_map(self, map={}):
        self.results = []
        if map.get('Results') is not None:
            for k in map.get('Results'):
                temp_model = RecognizeStampResponseDataResults()
                self.results.append(temp_model.from_map(k))
        else:
            self.results = None
        return self


class RecognizeStampAdvanceRequest(TeaModel):
    def __init__(self, image_urlobject=None):
        self.image_urlobject = image_urlobject  # type: BinaryIO

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        result = {}
        result['ImageURLObject'] = self.image_urlobject
        return result

    def from_map(self, map={}):
        self.image_urlobject = map.get('ImageURLObject')
        return self


class RecognizeBusinessCardRequest(TeaModel):
    def __init__(self, image_url=None):
        self.image_url = image_url      # type: str

    def validate(self):
        self.validate_required(self.image_url, 'image_url')

    def to_map(self):
        result = {}
        result['ImageURL'] = self.image_url
        return result

    def from_map(self, map={}):
        self.image_url = map.get('ImageURL')
        return self


class RecognizeBusinessCardResponse(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id    # type: str
        self.data = data                # type: RecognizeBusinessCardResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = RecognizeBusinessCardResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class RecognizeBusinessCardResponseData(TeaModel):
    def __init__(self, name=None, companies=None, departments=None, titles=None, cell_phone_numbers=None,
                 office_phone_numbers=None, addresses=None, emails=None):
        self.name = name                # type: str
        self.companies = companies      # type: List[str]
        self.departments = departments  # type: List[str]
        self.titles = titles            # type: List[str]
        self.cell_phone_numbers = cell_phone_numbers  # type: List[str]
        self.office_phone_numbers = office_phone_numbers  # type: List[str]
        self.addresses = addresses      # type: List[str]
        self.emails = emails            # type: List[str]

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.companies, 'companies')
        self.validate_required(self.departments, 'departments')
        self.validate_required(self.titles, 'titles')
        self.validate_required(self.cell_phone_numbers, 'cell_phone_numbers')
        self.validate_required(self.office_phone_numbers, 'office_phone_numbers')
        self.validate_required(self.addresses, 'addresses')
        self.validate_required(self.emails, 'emails')

    def to_map(self):
        result = {}
        result['Name'] = self.name
        result['Companies'] = self.companies
        result['Departments'] = self.departments
        result['Titles'] = self.titles
        result['CellPhoneNumbers'] = self.cell_phone_numbers
        result['OfficePhoneNumbers'] = self.office_phone_numbers
        result['Addresses'] = self.addresses
        result['Emails'] = self.emails
        return result

    def from_map(self, map={}):
        self.name = map.get('Name')
        self.companies = map.get('Companies')
        self.departments = map.get('Departments')
        self.titles = map.get('Titles')
        self.cell_phone_numbers = map.get('CellPhoneNumbers')
        self.office_phone_numbers = map.get('OfficePhoneNumbers')
        self.addresses = map.get('Addresses')
        self.emails = map.get('Emails')
        return self


class RecognizeBusinessCardAdvanceRequest(TeaModel):
    def __init__(self, image_urlobject=None):
        self.image_urlobject = image_urlobject  # type: BinaryIO

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        result = {}
        result['ImageURLObject'] = self.image_urlobject
        return result

    def from_map(self, map={}):
        self.image_urlobject = map.get('ImageURLObject')
        return self


class RecognizeVINCodeRequest(TeaModel):
    def __init__(self, image_url=None):
        self.image_url = image_url      # type: str

    def validate(self):
        self.validate_required(self.image_url, 'image_url')

    def to_map(self):
        result = {}
        result['ImageURL'] = self.image_url
        return result

    def from_map(self, map={}):
        self.image_url = map.get('ImageURL')
        return self


class RecognizeVINCodeResponse(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id    # type: str
        self.data = data                # type: RecognizeVINCodeResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = RecognizeVINCodeResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class RecognizeVINCodeResponseData(TeaModel):
    def __init__(self, vin_code=None):
        self.vin_code = vin_code        # type: str

    def validate(self):
        self.validate_required(self.vin_code, 'vin_code')

    def to_map(self):
        result = {}
        result['VinCode'] = self.vin_code
        return result

    def from_map(self, map={}):
        self.vin_code = map.get('VinCode')
        return self


class RecognizeVINCodeAdvanceRequest(TeaModel):
    def __init__(self, image_urlobject=None):
        self.image_urlobject = image_urlobject  # type: BinaryIO

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        result = {}
        result['ImageURLObject'] = self.image_urlobject
        return result

    def from_map(self, map={}):
        self.image_urlobject = map.get('ImageURLObject')
        return self


class RecognizeBusinessLicenseRequest(TeaModel):
    def __init__(self, image_url=None):
        self.image_url = image_url      # type: str

    def validate(self):
        self.validate_required(self.image_url, 'image_url')

    def to_map(self):
        result = {}
        result['ImageURL'] = self.image_url
        return result

    def from_map(self, map={}):
        self.image_url = map.get('ImageURL')
        return self


class RecognizeBusinessLicenseResponse(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id    # type: str
        self.data = data                # type: RecognizeBusinessLicenseResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = RecognizeBusinessLicenseResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class RecognizeBusinessLicenseResponseDataEmblem(TeaModel):
    def __init__(self, top=None, left=None, height=None, width=None):
        self.top = top                  # type: int
        self.left = left                # type: int
        self.height = height            # type: int
        self.width = width              # type: int

    def validate(self):
        self.validate_required(self.top, 'top')
        self.validate_required(self.left, 'left')
        self.validate_required(self.height, 'height')
        self.validate_required(self.width, 'width')

    def to_map(self):
        result = {}
        result['Top'] = self.top
        result['Left'] = self.left
        result['Height'] = self.height
        result['Width'] = self.width
        return result

    def from_map(self, map={}):
        self.top = map.get('Top')
        self.left = map.get('Left')
        self.height = map.get('Height')
        self.width = map.get('Width')
        return self


class RecognizeBusinessLicenseResponseDataTitle(TeaModel):
    def __init__(self, top=None, left=None, height=None, width=None):
        self.top = top                  # type: int
        self.left = left                # type: int
        self.height = height            # type: int
        self.width = width              # type: int

    def validate(self):
        self.validate_required(self.top, 'top')
        self.validate_required(self.left, 'left')
        self.validate_required(self.height, 'height')
        self.validate_required(self.width, 'width')

    def to_map(self):
        result = {}
        result['Top'] = self.top
        result['Left'] = self.left
        result['Height'] = self.height
        result['Width'] = self.width
        return result

    def from_map(self, map={}):
        self.top = map.get('Top')
        self.left = map.get('Left')
        self.height = map.get('Height')
        self.width = map.get('Width')
        return self


class RecognizeBusinessLicenseResponseDataStamp(TeaModel):
    def __init__(self, top=None, left=None, height=None, width=None):
        self.top = top                  # type: int
        self.left = left                # type: int
        self.height = height            # type: int
        self.width = width              # type: int

    def validate(self):
        self.validate_required(self.top, 'top')
        self.validate_required(self.left, 'left')
        self.validate_required(self.height, 'height')
        self.validate_required(self.width, 'width')

    def to_map(self):
        result = {}
        result['Top'] = self.top
        result['Left'] = self.left
        result['Height'] = self.height
        result['Width'] = self.width
        return result

    def from_map(self, map={}):
        self.top = map.get('Top')
        self.left = map.get('Left')
        self.height = map.get('Height')
        self.width = map.get('Width')
        return self


class RecognizeBusinessLicenseResponseDataQRCode(TeaModel):
    def __init__(self, top=None, left=None, height=None, width=None):
        self.top = top                  # type: int
        self.left = left                # type: int
        self.height = height            # type: int
        self.width = width              # type: int

    def validate(self):
        self.validate_required(self.top, 'top')
        self.validate_required(self.left, 'left')
        self.validate_required(self.height, 'height')
        self.validate_required(self.width, 'width')

    def to_map(self):
        result = {}
        result['Top'] = self.top
        result['Left'] = self.left
        result['Height'] = self.height
        result['Width'] = self.width
        return result

    def from_map(self, map={}):
        self.top = map.get('Top')
        self.left = map.get('Left')
        self.height = map.get('Height')
        self.width = map.get('Width')
        return self


class RecognizeBusinessLicenseResponseData(TeaModel):
    def __init__(self, angle=None, register_number=None, name=None, type=None, legal_person=None,
                 establish_date=None, valid_period=None, address=None, capital=None, business=None, emblem=None, title=None,
                 stamp=None, qrcode=None):
        self.angle = angle              # type: float
        self.register_number = register_number  # type: str
        self.name = name                # type: str
        self.type = type                # type: str
        self.legal_person = legal_person  # type: str
        self.establish_date = establish_date  # type: str
        self.valid_period = valid_period  # type: str
        self.address = address          # type: str
        self.capital = capital          # type: str
        self.business = business        # type: str
        self.emblem = emblem            # type: RecognizeBusinessLicenseResponseDataEmblem
        self.title = title              # type: RecognizeBusinessLicenseResponseDataTitle
        self.stamp = stamp              # type: RecognizeBusinessLicenseResponseDataStamp
        self.qrcode = qrcode            # type: RecognizeBusinessLicenseResponseDataQRCode

    def validate(self):
        self.validate_required(self.angle, 'angle')
        self.validate_required(self.register_number, 'register_number')
        self.validate_required(self.name, 'name')
        self.validate_required(self.type, 'type')
        self.validate_required(self.legal_person, 'legal_person')
        self.validate_required(self.establish_date, 'establish_date')
        self.validate_required(self.valid_period, 'valid_period')
        self.validate_required(self.address, 'address')
        self.validate_required(self.capital, 'capital')
        self.validate_required(self.business, 'business')
        self.validate_required(self.emblem, 'emblem')
        if self.emblem:
            self.emblem.validate()
        self.validate_required(self.title, 'title')
        if self.title:
            self.title.validate()
        self.validate_required(self.stamp, 'stamp')
        if self.stamp:
            self.stamp.validate()
        self.validate_required(self.qrcode, 'qrcode')
        if self.qrcode:
            self.qrcode.validate()

    def to_map(self):
        result = {}
        result['Angle'] = self.angle
        result['RegisterNumber'] = self.register_number
        result['Name'] = self.name
        result['Type'] = self.type
        result['LegalPerson'] = self.legal_person
        result['EstablishDate'] = self.establish_date
        result['ValidPeriod'] = self.valid_period
        result['Address'] = self.address
        result['Capital'] = self.capital
        result['Business'] = self.business
        if self.emblem is not None:
            result['Emblem'] = self.emblem.to_map()
        else:
            result['Emblem'] = None
        if self.title is not None:
            result['Title'] = self.title.to_map()
        else:
            result['Title'] = None
        if self.stamp is not None:
            result['Stamp'] = self.stamp.to_map()
        else:
            result['Stamp'] = None
        if self.qrcode is not None:
            result['QRCode'] = self.qrcode.to_map()
        else:
            result['QRCode'] = None
        return result

    def from_map(self, map={}):
        self.angle = map.get('Angle')
        self.register_number = map.get('RegisterNumber')
        self.name = map.get('Name')
        self.type = map.get('Type')
        self.legal_person = map.get('LegalPerson')
        self.establish_date = map.get('EstablishDate')
        self.valid_period = map.get('ValidPeriod')
        self.address = map.get('Address')
        self.capital = map.get('Capital')
        self.business = map.get('Business')
        if map.get('Emblem') is not None:
            temp_model = RecognizeBusinessLicenseResponseDataEmblem()
            self.emblem = temp_model.from_map(map['Emblem'])
        else:
            self.emblem = None
        if map.get('Title') is not None:
            temp_model = RecognizeBusinessLicenseResponseDataTitle()
            self.title = temp_model.from_map(map['Title'])
        else:
            self.title = None
        if map.get('Stamp') is not None:
            temp_model = RecognizeBusinessLicenseResponseDataStamp()
            self.stamp = temp_model.from_map(map['Stamp'])
        else:
            self.stamp = None
        if map.get('QRCode') is not None:
            temp_model = RecognizeBusinessLicenseResponseDataQRCode()
            self.qrcode = temp_model.from_map(map['QRCode'])
        else:
            self.qrcode = None
        return self


class RecognizeBusinessLicenseAdvanceRequest(TeaModel):
    def __init__(self, image_urlobject=None):
        self.image_urlobject = image_urlobject  # type: BinaryIO

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')

    def to_map(self):
        result = {}
        result['ImageURLObject'] = self.image_urlobject
        return result

    def from_map(self, map={}):
        self.image_urlobject = map.get('ImageURLObject')
        return self
