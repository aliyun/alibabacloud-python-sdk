# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, BinaryIO, List


class GetAsyncJobResultRequest(TeaModel):
    def __init__(
        self,
        job_id: str = None,
    ):
        # This parameter is required.
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
        status_code: int = None,
        body: GetAsyncJobResultResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetAsyncJobResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeBankCardRequest(TeaModel):
    def __init__(
        self,
        image_url: str = None,
    ):
        # This parameter is required.
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


class RecognizeBankCardAdvanceRequest(TeaModel):
    def __init__(
        self,
        image_urlobject: BinaryIO = None,
    ):
        # This parameter is required.
        self.image_urlobject = image_urlobject

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_urlobject is not None:
            result['ImageURL'] = self.image_urlobject
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_urlobject = m.get('ImageURL')
        return self


class RecognizeBankCardResponseBodyData(TeaModel):
    def __init__(
        self,
        bank_name: str = None,
        card_number: str = None,
        card_type: str = None,
        valid_date: str = None,
    ):
        self.bank_name = bank_name
        self.card_number = card_number
        self.card_type = card_type
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
        if self.card_type is not None:
            result['CardType'] = self.card_type
        if self.valid_date is not None:
            result['ValidDate'] = self.valid_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BankName') is not None:
            self.bank_name = m.get('BankName')
        if m.get('CardNumber') is not None:
            self.card_number = m.get('CardNumber')
        if m.get('CardType') is not None:
            self.card_type = m.get('CardType')
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
        status_code: int = None,
        body: RecognizeBankCardResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RecognizeBankCardResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeBusinessLicenseRequest(TeaModel):
    def __init__(
        self,
        image_url: str = None,
    ):
        # This parameter is required.
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
        # This parameter is required.
        self.image_urlobject = image_urlobject

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_urlobject is not None:
            result['ImageURL'] = self.image_urlobject
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_urlobject = m.get('ImageURL')
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
        status_code: int = None,
        body: RecognizeBusinessLicenseResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
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
        # This parameter is required.
        self.image_url = image_url
        # This parameter is required.
        self.min_height = min_height
        # This parameter is required.
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
        # This parameter is required.
        self.image_urlobject = image_urlobject
        # This parameter is required.
        self.min_height = min_height
        # This parameter is required.
        self.output_probability = output_probability

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_urlobject is not None:
            result['ImageURL'] = self.image_urlobject
        if self.min_height is not None:
            result['MinHeight'] = self.min_height
        if self.output_probability is not None:
            result['OutputProbability'] = self.output_probability
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_urlobject = m.get('ImageURL')
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
        status_code: int = None,
        body: RecognizeCharacterResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RecognizeCharacterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeDriverLicenseRequest(TeaModel):
    def __init__(
        self,
        image_url: str = None,
        side: str = None,
    ):
        # This parameter is required.
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
        # This parameter is required.
        self.image_urlobject = image_urlobject
        self.side = side

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_urlobject is not None:
            result['ImageURL'] = self.image_urlobject
        if self.side is not None:
            result['Side'] = self.side
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_urlobject = m.get('ImageURL')
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
        birth_date: str = None,
        end_date: str = None,
        gender: str = None,
        issue_date: str = None,
        issue_unit: str = None,
        license_number: str = None,
        name: str = None,
        nationality: str = None,
        start_date: str = None,
        vehicle_type: str = None,
    ):
        self.address = address
        self.birth_date = birth_date
        self.end_date = end_date
        self.gender = gender
        self.issue_date = issue_date
        self.issue_unit = issue_unit
        self.license_number = license_number
        self.name = name
        self.nationality = nationality
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
        if self.birth_date is not None:
            result['BirthDate'] = self.birth_date
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
        if self.nationality is not None:
            result['Nationality'] = self.nationality
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.vehicle_type is not None:
            result['VehicleType'] = self.vehicle_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('BirthDate') is not None:
            self.birth_date = m.get('BirthDate')
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
        if m.get('Nationality') is not None:
            self.nationality = m.get('Nationality')
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
        status_code: int = None,
        body: RecognizeDriverLicenseResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
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
        # This parameter is required.
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
        # This parameter is required.
        self.image_urlobject = image_urlobject
        self.side = side

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_urlobject is not None:
            result['ImageURL'] = self.image_urlobject
        if self.side is not None:
            result['Side'] = self.side
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_urlobject = m.get('ImageURL')
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
        status_code: int = None,
        body: RecognizeDrivingLicenseResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
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
        # This parameter is required.
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
        # This parameter is required.
        self.image_urlobject = image_urlobject
        self.side = side

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_urlobject is not None:
            result['ImageURL'] = self.image_urlobject
        if self.side is not None:
            result['Side'] = self.side
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_urlobject = m.get('ImageURL')
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
        status_code: int = None,
        body: RecognizeIdentityCardResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RecognizeIdentityCardResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeLicensePlateRequest(TeaModel):
    def __init__(
        self,
        image_url: str = None,
    ):
        # This parameter is required.
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
        # This parameter is required.
        self.image_urlobject = image_urlobject

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_urlobject is not None:
            result['ImageURL'] = self.image_urlobject
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_urlobject = m.get('ImageURL')
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
        status_code: int = None,
        body: RecognizeLicensePlateResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RecognizeLicensePlateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizePdfRequest(TeaModel):
    def __init__(
        self,
        file_url: str = None,
    ):
        # This parameter is required.
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
        # This parameter is required.
        self.file_urlobject = file_urlobject

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_urlobject is not None:
            result['FileURL'] = self.file_urlobject
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileURL') is not None:
            self.file_urlobject = m.get('FileURL')
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
        status_code: int = None,
        body: RecognizePdfResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RecognizePdfResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeQrCodeRequestTasks(TeaModel):
    def __init__(
        self,
        image_url: str = None,
    ):
        # This parameter is required.
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
        # 1
        # 
        # This parameter is required.
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


class RecognizeQrCodeAdvanceRequestTasks(TeaModel):
    def __init__(
        self,
        image_urlobject: BinaryIO = None,
    ):
        # This parameter is required.
        self.image_urlobject = image_urlobject

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_urlobject is not None:
            result['ImageURL'] = self.image_urlobject
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_urlobject = m.get('ImageURL')
        return self


class RecognizeQrCodeAdvanceRequest(TeaModel):
    def __init__(
        self,
        tasks: List[RecognizeQrCodeAdvanceRequestTasks] = None,
    ):
        # 1
        # 
        # This parameter is required.
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
                temp_model = RecognizeQrCodeAdvanceRequestTasks()
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
        # 1
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
        status_code: int = None,
        body: RecognizeQrCodeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RecognizeQrCodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeQuotaInvoiceRequest(TeaModel):
    def __init__(
        self,
        image_url: str = None,
    ):
        # This parameter is required.
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
        # This parameter is required.
        self.image_urlobject = image_urlobject

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_urlobject is not None:
            result['ImageURL'] = self.image_urlobject
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_urlobject = m.get('ImageURL')
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
        status_code: int = None,
        body: RecognizeQuotaInvoiceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RecognizeQuotaInvoiceResponseBody()
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
        # This parameter is required.
        self.assure_direction = assure_direction
        # This parameter is required.
        self.has_line = has_line
        # This parameter is required.
        self.image_url = image_url
        # This parameter is required.
        self.output_format = output_format
        # This parameter is required.
        self.skip_detection = skip_detection
        # This parameter is required.
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
        assure_direction: bool = None,
        has_line: bool = None,
        image_urlobject: BinaryIO = None,
        output_format: str = None,
        skip_detection: bool = None,
        use_finance_model: bool = None,
    ):
        # This parameter is required.
        self.assure_direction = assure_direction
        # This parameter is required.
        self.has_line = has_line
        # This parameter is required.
        self.image_urlobject = image_urlobject
        # This parameter is required.
        self.output_format = output_format
        # This parameter is required.
        self.skip_detection = skip_detection
        # This parameter is required.
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
        if self.image_urlobject is not None:
            result['ImageURL'] = self.image_urlobject
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
            self.image_urlobject = m.get('ImageURL')
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
        status_code: int = None,
        body: RecognizeTableResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RecognizeTableResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeTaxiInvoiceRequest(TeaModel):
    def __init__(
        self,
        image_url: str = None,
    ):
        # This parameter is required.
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
        # This parameter is required.
        self.image_urlobject = image_urlobject

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_urlobject is not None:
            result['ImageURL'] = self.image_urlobject
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_urlobject = m.get('ImageURL')
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
        status_code: int = None,
        body: RecognizeTaxiInvoiceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RecognizeTaxiInvoiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeTicketInvoiceRequest(TeaModel):
    def __init__(
        self,
        image_url: str = None,
    ):
        # This parameter is required.
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
        # This parameter is required.
        self.image_urlobject = image_urlobject

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_urlobject is not None:
            result['ImageURL'] = self.image_urlobject
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_urlobject = m.get('ImageURL')
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
        status_code: int = None,
        body: RecognizeTicketInvoiceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RecognizeTicketInvoiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeTrainTicketRequest(TeaModel):
    def __init__(
        self,
        image_url: str = None,
    ):
        # This parameter is required.
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
        # This parameter is required.
        self.image_urlobject = image_urlobject

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_urlobject is not None:
            result['ImageURL'] = self.image_urlobject
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_urlobject = m.get('ImageURL')
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
        status_code: int = None,
        body: RecognizeTrainTicketResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
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
        # This parameter is required.
        self.file_type = file_type
        # This parameter is required.
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
        file_type: str = None,
        file_urlobject: BinaryIO = None,
    ):
        # This parameter is required.
        self.file_type = file_type
        # This parameter is required.
        self.file_urlobject = file_urlobject

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_type is not None:
            result['FileType'] = self.file_type
        if self.file_urlobject is not None:
            result['FileURL'] = self.file_urlobject
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')
        if m.get('FileURL') is not None:
            self.file_urlobject = m.get('FileURL')
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
        item_names: List[int] = None,
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
        # 1
        self.checkers = checkers
        # 1
        self.clerks = clerks
        # 1
        self.invoice_amounts = invoice_amounts
        # 1
        self.invoice_codes = invoice_codes
        # 1
        self.invoice_dates = invoice_dates
        # 1
        self.invoice_fake_codes = invoice_fake_codes
        # 1
        self.invoice_noes = invoice_noes
        # 1
        self.item_names = item_names
        # 1
        self.payee_addresses = payee_addresses
        # 1
        self.payee_bank_names = payee_bank_names
        # 1
        self.payee_names = payee_names
        # 1
        self.payee_register_noes = payee_register_noes
        # 1
        self.payees = payees
        # 1
        self.payer_addresses = payer_addresses
        # 1
        self.payer_bank_names = payer_bank_names
        # 1
        self.payer_names = payer_names
        # 1
        self.payer_register_noes = payer_register_noes
        # 1
        self.sum_amounts = sum_amounts
        # 1
        self.tax_amounts = tax_amounts
        # 1
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
        if self.item_names is not None:
            result['ItemNames'] = self.item_names
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
        if m.get('ItemNames') is not None:
            self.item_names = m.get('ItemNames')
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
        item_name: List[str] = None,
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
        # 1
        self.item_name = item_name
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
        if self.item_name is not None:
            result['ItemName'] = self.item_name
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
        if m.get('ItemName') is not None:
            self.item_name = m.get('ItemName')
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
        status_code: int = None,
        body: RecognizeVATInvoiceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RecognizeVATInvoiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeVINCodeRequest(TeaModel):
    def __init__(
        self,
        image_url: str = None,
    ):
        # This parameter is required.
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
        # This parameter is required.
        self.image_urlobject = image_urlobject

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_urlobject is not None:
            result['ImageURL'] = self.image_urlobject
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_urlobject = m.get('ImageURL')
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
        status_code: int = None,
        body: RecognizeVINCodeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RecognizeVINCodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeVideoCharacterRequest(TeaModel):
    def __init__(
        self,
        video_url: str = None,
    ):
        # This parameter is required.
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


class RecognizeVideoCharacterAdvanceRequest(TeaModel):
    def __init__(
        self,
        video_urlobject: BinaryIO = None,
    ):
        # This parameter is required.
        self.video_urlobject = video_urlobject

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.video_urlobject is not None:
            result['VideoURL'] = self.video_urlobject
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VideoURL') is not None:
            self.video_urlobject = m.get('VideoURL')
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


class RecognizeVideoCharacterResponseBodyDataFramesElements(TeaModel):
    def __init__(
        self,
        score: float = None,
        text: str = None,
        text_rectangles: List[RecognizeVideoCharacterResponseBodyDataFramesElementsTextRectangles] = None,
    ):
        self.score = score
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
        self.frames = frames
        self.height = height
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
        message: str = None,
        request_id: str = None,
    ):
        self.data = data
        self.message = message
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
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = RecognizeVideoCharacterResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RecognizeVideoCharacterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RecognizeVideoCharacterResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RecognizeVideoCharacterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


