# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class FaceRecognitionCompareRequest(TeaModel):
    def __init__(
        self,
        id_card_image_data: str = None,
        id_card_image_type: str = None,
        id_card_image_url: str = None,
        portrait_image_data: str = None,
        portrait_image_type: str = None,
        portrait_image_url: str = None,
        quality_control: str = None,
    ):
        self.id_card_image_data = id_card_image_data
        self.id_card_image_type = id_card_image_type
        self.id_card_image_url = id_card_image_url
        self.portrait_image_data = portrait_image_data
        self.portrait_image_type = portrait_image_type
        self.portrait_image_url = portrait_image_url
        self.quality_control = quality_control

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id_card_image_data is not None:
            result['idCardImageData'] = self.id_card_image_data
        if self.id_card_image_type is not None:
            result['idCardImageType'] = self.id_card_image_type
        if self.id_card_image_url is not None:
            result['idCardImageUrl'] = self.id_card_image_url
        if self.portrait_image_data is not None:
            result['portraitImageData'] = self.portrait_image_data
        if self.portrait_image_type is not None:
            result['portraitImageType'] = self.portrait_image_type
        if self.portrait_image_url is not None:
            result['portraitImageUrl'] = self.portrait_image_url
        if self.quality_control is not None:
            result['qualityControl'] = self.quality_control
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('idCardImageData') is not None:
            self.id_card_image_data = m.get('idCardImageData')
        if m.get('idCardImageType') is not None:
            self.id_card_image_type = m.get('idCardImageType')
        if m.get('idCardImageUrl') is not None:
            self.id_card_image_url = m.get('idCardImageUrl')
        if m.get('portraitImageData') is not None:
            self.portrait_image_data = m.get('portraitImageData')
        if m.get('portraitImageType') is not None:
            self.portrait_image_type = m.get('portraitImageType')
        if m.get('portraitImageUrl') is not None:
            self.portrait_image_url = m.get('portraitImageUrl')
        if m.get('qualityControl') is not None:
            self.quality_control = m.get('qualityControl')
        return self


class FaceRecognitionCompareResponseBodyData(TeaModel):
    def __init__(
        self,
        match: str = None,
        score: float = None,
    ):
        self.match = match
        self.score = score

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match is not None:
            result['Match'] = self.match
        if self.score is not None:
            result['Score'] = self.score
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Match') is not None:
            self.match = m.get('Match')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        return self


class FaceRecognitionCompareResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: FaceRecognitionCompareResponseBodyData = None,
        http_code: int = None,
        message: str = None,
        ok: bool = None,
        request_id: str = None,
        status: str = None,
    ):
        self.code = code
        self.data = data
        self.http_code = http_code
        self.message = message
        self.ok = ok
        self.request_id = request_id
        self.status = status

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.message is not None:
            result['Message'] = self.message
        if self.ok is not None:
            result['Ok'] = self.ok
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = FaceRecognitionCompareResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Ok') is not None:
            self.ok = m.get('Ok')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class FaceRecognitionCompareResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: FaceRecognitionCompareResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = FaceRecognitionCompareResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FaceToFaceCompareRequest(TeaModel):
    def __init__(
        self,
        portrait_image_data_1: str = None,
        portrait_image_data_2: str = None,
        portrait_image_type_1: str = None,
        portrait_image_type_2: str = None,
        portrait_image_url_1: str = None,
        portrait_image_url_2: str = None,
        quality_control: str = None,
    ):
        self.portrait_image_data_1 = portrait_image_data_1
        self.portrait_image_data_2 = portrait_image_data_2
        self.portrait_image_type_1 = portrait_image_type_1
        self.portrait_image_type_2 = portrait_image_type_2
        self.portrait_image_url_1 = portrait_image_url_1
        self.portrait_image_url_2 = portrait_image_url_2
        self.quality_control = quality_control

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.portrait_image_data_1 is not None:
            result['portraitImageData1'] = self.portrait_image_data_1
        if self.portrait_image_data_2 is not None:
            result['portraitImageData2'] = self.portrait_image_data_2
        if self.portrait_image_type_1 is not None:
            result['portraitImageType1'] = self.portrait_image_type_1
        if self.portrait_image_type_2 is not None:
            result['portraitImageType2'] = self.portrait_image_type_2
        if self.portrait_image_url_1 is not None:
            result['portraitImageUrl1'] = self.portrait_image_url_1
        if self.portrait_image_url_2 is not None:
            result['portraitImageUrl2'] = self.portrait_image_url_2
        if self.quality_control is not None:
            result['qualityControl'] = self.quality_control
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('portraitImageData1') is not None:
            self.portrait_image_data_1 = m.get('portraitImageData1')
        if m.get('portraitImageData2') is not None:
            self.portrait_image_data_2 = m.get('portraitImageData2')
        if m.get('portraitImageType1') is not None:
            self.portrait_image_type_1 = m.get('portraitImageType1')
        if m.get('portraitImageType2') is not None:
            self.portrait_image_type_2 = m.get('portraitImageType2')
        if m.get('portraitImageUrl1') is not None:
            self.portrait_image_url_1 = m.get('portraitImageUrl1')
        if m.get('portraitImageUrl2') is not None:
            self.portrait_image_url_2 = m.get('portraitImageUrl2')
        if m.get('qualityControl') is not None:
            self.quality_control = m.get('qualityControl')
        return self


class FaceToFaceCompareResponseBodyData(TeaModel):
    def __init__(
        self,
        match: str = None,
        score: float = None,
    ):
        self.match = match
        self.score = score

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match is not None:
            result['Match'] = self.match
        if self.score is not None:
            result['Score'] = self.score
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Match') is not None:
            self.match = m.get('Match')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        return self


class FaceToFaceCompareResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: FaceToFaceCompareResponseBodyData = None,
        http_code: int = None,
        message: str = None,
        ok: bool = None,
        request_id: str = None,
        status: str = None,
    ):
        self.code = code
        self.data = data
        self.http_code = http_code
        self.message = message
        self.ok = ok
        self.request_id = request_id
        self.status = status

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.message is not None:
            result['Message'] = self.message
        if self.ok is not None:
            result['Ok'] = self.ok
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = FaceToFaceCompareResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Ok') is not None:
            self.ok = m.get('Ok')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class FaceToFaceCompareResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: FaceToFaceCompareResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = FaceToFaceCompareResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class IdDetectOcrCompareFacesRequest(TeaModel):
    def __init__(
        self,
        ocr: bool = None,
        unrepeat: bool = None,
        card_detect: bool = None,
        country_code: str = None,
        document_type: str = None,
        face_compare: bool = None,
        image_atype: str = None,
        image_btype: str = None,
        image_data_a: str = None,
        image_data_b: str = None,
        image_url_a: str = None,
        image_url_b: str = None,
        portrait_image_data: str = None,
        portrait_image_url: str = None,
        quality_control: str = None,
    ):
        self.ocr = ocr
        self.unrepeat = unrepeat
        self.card_detect = card_detect
        self.country_code = country_code
        self.document_type = document_type
        self.face_compare = face_compare
        self.image_atype = image_atype
        self.image_btype = image_btype
        self.image_data_a = image_data_a
        self.image_data_b = image_data_b
        self.image_url_a = image_url_a
        self.image_url_b = image_url_b
        self.portrait_image_data = portrait_image_data
        self.portrait_image_url = portrait_image_url
        self.quality_control = quality_control

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ocr is not None:
            result['OCR'] = self.ocr
        if self.unrepeat is not None:
            result['Unrepeat'] = self.unrepeat
        if self.card_detect is not None:
            result['cardDetect'] = self.card_detect
        if self.country_code is not None:
            result['countryCode'] = self.country_code
        if self.document_type is not None:
            result['documentType'] = self.document_type
        if self.face_compare is not None:
            result['faceCompare'] = self.face_compare
        if self.image_atype is not None:
            result['imageAType'] = self.image_atype
        if self.image_btype is not None:
            result['imageBType'] = self.image_btype
        if self.image_data_a is not None:
            result['imageDataA'] = self.image_data_a
        if self.image_data_b is not None:
            result['imageDataB'] = self.image_data_b
        if self.image_url_a is not None:
            result['imageUrlA'] = self.image_url_a
        if self.image_url_b is not None:
            result['imageUrlB'] = self.image_url_b
        if self.portrait_image_data is not None:
            result['portraitImageData'] = self.portrait_image_data
        if self.portrait_image_url is not None:
            result['portraitImageUrl'] = self.portrait_image_url
        if self.quality_control is not None:
            result['qualityControl'] = self.quality_control
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OCR') is not None:
            self.ocr = m.get('OCR')
        if m.get('Unrepeat') is not None:
            self.unrepeat = m.get('Unrepeat')
        if m.get('cardDetect') is not None:
            self.card_detect = m.get('cardDetect')
        if m.get('countryCode') is not None:
            self.country_code = m.get('countryCode')
        if m.get('documentType') is not None:
            self.document_type = m.get('documentType')
        if m.get('faceCompare') is not None:
            self.face_compare = m.get('faceCompare')
        if m.get('imageAType') is not None:
            self.image_atype = m.get('imageAType')
        if m.get('imageBType') is not None:
            self.image_btype = m.get('imageBType')
        if m.get('imageDataA') is not None:
            self.image_data_a = m.get('imageDataA')
        if m.get('imageDataB') is not None:
            self.image_data_b = m.get('imageDataB')
        if m.get('imageUrlA') is not None:
            self.image_url_a = m.get('imageUrlA')
        if m.get('imageUrlB') is not None:
            self.image_url_b = m.get('imageUrlB')
        if m.get('portraitImageData') is not None:
            self.portrait_image_data = m.get('portraitImageData')
        if m.get('portraitImageUrl') is not None:
            self.portrait_image_url = m.get('portraitImageUrl')
        if m.get('qualityControl') is not None:
            self.quality_control = m.get('qualityControl')
        return self


class IdDetectOcrCompareFacesResponseBodyDataCompareResultCompareResultData(TeaModel):
    def __init__(
        self,
        match: str = None,
        risks: List[str] = None,
        score: float = None,
    ):
        self.match = match
        self.risks = risks
        self.score = score

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match is not None:
            result['Match'] = self.match
        if self.risks is not None:
            result['Risks'] = self.risks
        if self.score is not None:
            result['Score'] = self.score
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Match') is not None:
            self.match = m.get('Match')
        if m.get('Risks') is not None:
            self.risks = m.get('Risks')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        return self


class IdDetectOcrCompareFacesResponseBodyDataCompareResult(TeaModel):
    def __init__(
        self,
        code: str = None,
        compare_result_data: IdDetectOcrCompareFacesResponseBodyDataCompareResultCompareResultData = None,
        message: str = None,
    ):
        self.code = code
        self.compare_result_data = compare_result_data
        self.message = message

    def validate(self):
        if self.compare_result_data:
            self.compare_result_data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.compare_result_data is not None:
            result['CompareResultData'] = self.compare_result_data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('CompareResultData') is not None:
            temp_model = IdDetectOcrCompareFacesResponseBodyDataCompareResultCompareResultData()
            self.compare_result_data = temp_model.from_map(m['CompareResultData'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class IdDetectOcrCompareFacesResponseBodyDataIdDetectResultIdDetectResultDataAntiSpoofingResult(TeaModel):
    def __init__(
        self,
        passed: bool = None,
        risks: List[str] = None,
    ):
        self.passed = passed
        self.risks = risks

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.passed is not None:
            result['Passed'] = self.passed
        if self.risks is not None:
            result['Risks'] = self.risks
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Passed') is not None:
            self.passed = m.get('Passed')
        if m.get('Risks') is not None:
            self.risks = m.get('Risks')
        return self


class IdDetectOcrCompareFacesResponseBodyDataIdDetectResultIdDetectResultDataDetectionResult(TeaModel):
    def __init__(
        self,
        card_rectangle: List[int] = None,
        height: int = None,
        portrait_rectangle: List[int] = None,
        width: int = None,
    ):
        self.card_rectangle = card_rectangle
        self.height = height
        self.portrait_rectangle = portrait_rectangle
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.card_rectangle is not None:
            result['CardRectangle'] = self.card_rectangle
        if self.height is not None:
            result['Height'] = self.height
        if self.portrait_rectangle is not None:
            result['PortraitRectangle'] = self.portrait_rectangle
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CardRectangle') is not None:
            self.card_rectangle = m.get('CardRectangle')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('PortraitRectangle') is not None:
            self.portrait_rectangle = m.get('PortraitRectangle')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class IdDetectOcrCompareFacesResponseBodyDataIdDetectResultIdDetectResultData(TeaModel):
    def __init__(
        self,
        anti_spoofing_result: IdDetectOcrCompareFacesResponseBodyDataIdDetectResultIdDetectResultDataAntiSpoofingResult = None,
        country_code: str = None,
        detection_result: IdDetectOcrCompareFacesResponseBodyDataIdDetectResultIdDetectResultDataDetectionResult = None,
        document_type: str = None,
        passed: bool = None,
        warning: List[str] = None,
    ):
        self.anti_spoofing_result = anti_spoofing_result
        self.country_code = country_code
        self.detection_result = detection_result
        self.document_type = document_type
        self.passed = passed
        self.warning = warning

    def validate(self):
        if self.anti_spoofing_result:
            self.anti_spoofing_result.validate()
        if self.detection_result:
            self.detection_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.anti_spoofing_result is not None:
            result['AntiSpoofingResult'] = self.anti_spoofing_result.to_map()
        if self.country_code is not None:
            result['CountryCode'] = self.country_code
        if self.detection_result is not None:
            result['DetectionResult'] = self.detection_result.to_map()
        if self.document_type is not None:
            result['DocumentType'] = self.document_type
        if self.passed is not None:
            result['Passed'] = self.passed
        if self.warning is not None:
            result['Warning'] = self.warning
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AntiSpoofingResult') is not None:
            temp_model = IdDetectOcrCompareFacesResponseBodyDataIdDetectResultIdDetectResultDataAntiSpoofingResult()
            self.anti_spoofing_result = temp_model.from_map(m['AntiSpoofingResult'])
        if m.get('CountryCode') is not None:
            self.country_code = m.get('CountryCode')
        if m.get('DetectionResult') is not None:
            temp_model = IdDetectOcrCompareFacesResponseBodyDataIdDetectResultIdDetectResultDataDetectionResult()
            self.detection_result = temp_model.from_map(m['DetectionResult'])
        if m.get('DocumentType') is not None:
            self.document_type = m.get('DocumentType')
        if m.get('Passed') is not None:
            self.passed = m.get('Passed')
        if m.get('Warning') is not None:
            self.warning = m.get('Warning')
        return self


class IdDetectOcrCompareFacesResponseBodyDataIdDetectResult(TeaModel):
    def __init__(
        self,
        code: str = None,
        id_detect_result_data: IdDetectOcrCompareFacesResponseBodyDataIdDetectResultIdDetectResultData = None,
        message: str = None,
    ):
        self.code = code
        self.id_detect_result_data = id_detect_result_data
        self.message = message

    def validate(self):
        if self.id_detect_result_data:
            self.id_detect_result_data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.id_detect_result_data is not None:
            result['IdDetectResultData'] = self.id_detect_result_data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IdDetectResultData') is not None:
            temp_model = IdDetectOcrCompareFacesResponseBodyDataIdDetectResultIdDetectResultData()
            self.id_detect_result_data = temp_model.from_map(m['IdDetectResultData'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class IdDetectOcrCompareFacesResponseBodyDataLivenessResultLivenessResultData(TeaModel):
    def __init__(
        self,
        liveness: str = None,
        risks: List[str] = None,
        score: float = None,
    ):
        self.liveness = liveness
        self.risks = risks
        self.score = score

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.liveness is not None:
            result['Liveness'] = self.liveness
        if self.risks is not None:
            result['Risks'] = self.risks
        if self.score is not None:
            result['Score'] = self.score
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Liveness') is not None:
            self.liveness = m.get('Liveness')
        if m.get('Risks') is not None:
            self.risks = m.get('Risks')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        return self


class IdDetectOcrCompareFacesResponseBodyDataLivenessResult(TeaModel):
    def __init__(
        self,
        code: str = None,
        liveness_result_data: IdDetectOcrCompareFacesResponseBodyDataLivenessResultLivenessResultData = None,
        message: str = None,
    ):
        self.code = code
        self.liveness_result_data = liveness_result_data
        self.message = message

    def validate(self):
        if self.liveness_result_data:
            self.liveness_result_data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.liveness_result_data is not None:
            result['LivenessResultData'] = self.liveness_result_data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('LivenessResultData') is not None:
            temp_model = IdDetectOcrCompareFacesResponseBodyDataLivenessResultLivenessResultData()
            self.liveness_result_data = temp_model.from_map(m['LivenessResultData'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class IdDetectOcrCompareFacesResponseBodyDataOcrResultOcrResultData(TeaModel):
    def __init__(
        self,
        address: str = None,
        address_confidence: float = None,
        address_position: List[int] = None,
        date_of_birth: str = None,
        date_of_birth_confidence: float = None,
        date_of_birth_position: List[int] = None,
        document_number: str = None,
        document_number_2: str = None,
        document_number_2confidence: float = None,
        document_number_2position: List[int] = None,
        document_number_confidence: float = None,
        document_number_position: List[int] = None,
        expiration_date: str = None,
        expiration_date_confidence: float = None,
        expiration_date_position: List[int] = None,
        first_name: str = None,
        first_name_confidence: float = None,
        first_name_position: List[int] = None,
        full_name: str = None,
        full_name_confidence: float = None,
        full_name_position: List[int] = None,
        issued_date: str = None,
        issued_date_confidence: float = None,
        issued_date_position: List[int] = None,
        issuing_authority: str = None,
        issuing_authority_confidence: float = None,
        issuing_authority_position: List[int] = None,
        last_name: str = None,
        last_name_confidence: float = None,
        last_name_position: List[int] = None,
        nationality_code: str = None,
        nationality_code_confidence: float = None,
        nationality_code_position: List[int] = None,
        normalized_date_of_birth: str = None,
        normalized_expiration_date: str = None,
        normalized_issued_date: str = None,
        normalized_nationality_code: str = None,
        normalized_sex: str = None,
        sex: str = None,
        sex_confidence: float = None,
        sex_position: List[int] = None,
    ):
        self.address = address
        self.address_confidence = address_confidence
        self.address_position = address_position
        self.date_of_birth = date_of_birth
        self.date_of_birth_confidence = date_of_birth_confidence
        self.date_of_birth_position = date_of_birth_position
        self.document_number = document_number
        self.document_number_2 = document_number_2
        self.document_number_2confidence = document_number_2confidence
        self.document_number_2position = document_number_2position
        self.document_number_confidence = document_number_confidence
        self.document_number_position = document_number_position
        self.expiration_date = expiration_date
        self.expiration_date_confidence = expiration_date_confidence
        self.expiration_date_position = expiration_date_position
        self.first_name = first_name
        self.first_name_confidence = first_name_confidence
        self.first_name_position = first_name_position
        self.full_name = full_name
        self.full_name_confidence = full_name_confidence
        self.full_name_position = full_name_position
        self.issued_date = issued_date
        self.issued_date_confidence = issued_date_confidence
        self.issued_date_position = issued_date_position
        self.issuing_authority = issuing_authority
        self.issuing_authority_confidence = issuing_authority_confidence
        self.issuing_authority_position = issuing_authority_position
        self.last_name = last_name
        self.last_name_confidence = last_name_confidence
        self.last_name_position = last_name_position
        self.nationality_code = nationality_code
        self.nationality_code_confidence = nationality_code_confidence
        self.nationality_code_position = nationality_code_position
        self.normalized_date_of_birth = normalized_date_of_birth
        self.normalized_expiration_date = normalized_expiration_date
        self.normalized_issued_date = normalized_issued_date
        self.normalized_nationality_code = normalized_nationality_code
        self.normalized_sex = normalized_sex
        self.sex = sex
        self.sex_confidence = sex_confidence
        self.sex_position = sex_position

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.address_confidence is not None:
            result['AddressConfidence'] = self.address_confidence
        if self.address_position is not None:
            result['AddressPosition'] = self.address_position
        if self.date_of_birth is not None:
            result['DateOfBirth'] = self.date_of_birth
        if self.date_of_birth_confidence is not None:
            result['DateOfBirthConfidence'] = self.date_of_birth_confidence
        if self.date_of_birth_position is not None:
            result['DateOfBirthPosition'] = self.date_of_birth_position
        if self.document_number is not None:
            result['DocumentNumber'] = self.document_number
        if self.document_number_2 is not None:
            result['DocumentNumber2'] = self.document_number_2
        if self.document_number_2confidence is not None:
            result['DocumentNumber2Confidence'] = self.document_number_2confidence
        if self.document_number_2position is not None:
            result['DocumentNumber2Position'] = self.document_number_2position
        if self.document_number_confidence is not None:
            result['DocumentNumberConfidence'] = self.document_number_confidence
        if self.document_number_position is not None:
            result['DocumentNumberPosition'] = self.document_number_position
        if self.expiration_date is not None:
            result['ExpirationDate'] = self.expiration_date
        if self.expiration_date_confidence is not None:
            result['ExpirationDateConfidence'] = self.expiration_date_confidence
        if self.expiration_date_position is not None:
            result['ExpirationDatePosition'] = self.expiration_date_position
        if self.first_name is not None:
            result['FirstName'] = self.first_name
        if self.first_name_confidence is not None:
            result['FirstNameConfidence'] = self.first_name_confidence
        if self.first_name_position is not None:
            result['FirstNamePosition'] = self.first_name_position
        if self.full_name is not None:
            result['FullName'] = self.full_name
        if self.full_name_confidence is not None:
            result['FullNameConfidence'] = self.full_name_confidence
        if self.full_name_position is not None:
            result['FullNamePosition'] = self.full_name_position
        if self.issued_date is not None:
            result['IssuedDate'] = self.issued_date
        if self.issued_date_confidence is not None:
            result['IssuedDateConfidence'] = self.issued_date_confidence
        if self.issued_date_position is not None:
            result['IssuedDatePosition'] = self.issued_date_position
        if self.issuing_authority is not None:
            result['IssuingAuthority'] = self.issuing_authority
        if self.issuing_authority_confidence is not None:
            result['IssuingAuthorityConfidence'] = self.issuing_authority_confidence
        if self.issuing_authority_position is not None:
            result['IssuingAuthorityPosition'] = self.issuing_authority_position
        if self.last_name is not None:
            result['LastName'] = self.last_name
        if self.last_name_confidence is not None:
            result['LastNameConfidence'] = self.last_name_confidence
        if self.last_name_position is not None:
            result['LastNamePosition'] = self.last_name_position
        if self.nationality_code is not None:
            result['NationalityCode'] = self.nationality_code
        if self.nationality_code_confidence is not None:
            result['NationalityCodeConfidence'] = self.nationality_code_confidence
        if self.nationality_code_position is not None:
            result['NationalityCodePosition'] = self.nationality_code_position
        if self.normalized_date_of_birth is not None:
            result['NormalizedDateOfBirth'] = self.normalized_date_of_birth
        if self.normalized_expiration_date is not None:
            result['NormalizedExpirationDate'] = self.normalized_expiration_date
        if self.normalized_issued_date is not None:
            result['NormalizedIssuedDate'] = self.normalized_issued_date
        if self.normalized_nationality_code is not None:
            result['NormalizedNationalityCode'] = self.normalized_nationality_code
        if self.normalized_sex is not None:
            result['NormalizedSex'] = self.normalized_sex
        if self.sex is not None:
            result['Sex'] = self.sex
        if self.sex_confidence is not None:
            result['SexConfidence'] = self.sex_confidence
        if self.sex_position is not None:
            result['SexPosition'] = self.sex_position
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('AddressConfidence') is not None:
            self.address_confidence = m.get('AddressConfidence')
        if m.get('AddressPosition') is not None:
            self.address_position = m.get('AddressPosition')
        if m.get('DateOfBirth') is not None:
            self.date_of_birth = m.get('DateOfBirth')
        if m.get('DateOfBirthConfidence') is not None:
            self.date_of_birth_confidence = m.get('DateOfBirthConfidence')
        if m.get('DateOfBirthPosition') is not None:
            self.date_of_birth_position = m.get('DateOfBirthPosition')
        if m.get('DocumentNumber') is not None:
            self.document_number = m.get('DocumentNumber')
        if m.get('DocumentNumber2') is not None:
            self.document_number_2 = m.get('DocumentNumber2')
        if m.get('DocumentNumber2Confidence') is not None:
            self.document_number_2confidence = m.get('DocumentNumber2Confidence')
        if m.get('DocumentNumber2Position') is not None:
            self.document_number_2position = m.get('DocumentNumber2Position')
        if m.get('DocumentNumberConfidence') is not None:
            self.document_number_confidence = m.get('DocumentNumberConfidence')
        if m.get('DocumentNumberPosition') is not None:
            self.document_number_position = m.get('DocumentNumberPosition')
        if m.get('ExpirationDate') is not None:
            self.expiration_date = m.get('ExpirationDate')
        if m.get('ExpirationDateConfidence') is not None:
            self.expiration_date_confidence = m.get('ExpirationDateConfidence')
        if m.get('ExpirationDatePosition') is not None:
            self.expiration_date_position = m.get('ExpirationDatePosition')
        if m.get('FirstName') is not None:
            self.first_name = m.get('FirstName')
        if m.get('FirstNameConfidence') is not None:
            self.first_name_confidence = m.get('FirstNameConfidence')
        if m.get('FirstNamePosition') is not None:
            self.first_name_position = m.get('FirstNamePosition')
        if m.get('FullName') is not None:
            self.full_name = m.get('FullName')
        if m.get('FullNameConfidence') is not None:
            self.full_name_confidence = m.get('FullNameConfidence')
        if m.get('FullNamePosition') is not None:
            self.full_name_position = m.get('FullNamePosition')
        if m.get('IssuedDate') is not None:
            self.issued_date = m.get('IssuedDate')
        if m.get('IssuedDateConfidence') is not None:
            self.issued_date_confidence = m.get('IssuedDateConfidence')
        if m.get('IssuedDatePosition') is not None:
            self.issued_date_position = m.get('IssuedDatePosition')
        if m.get('IssuingAuthority') is not None:
            self.issuing_authority = m.get('IssuingAuthority')
        if m.get('IssuingAuthorityConfidence') is not None:
            self.issuing_authority_confidence = m.get('IssuingAuthorityConfidence')
        if m.get('IssuingAuthorityPosition') is not None:
            self.issuing_authority_position = m.get('IssuingAuthorityPosition')
        if m.get('LastName') is not None:
            self.last_name = m.get('LastName')
        if m.get('LastNameConfidence') is not None:
            self.last_name_confidence = m.get('LastNameConfidence')
        if m.get('LastNamePosition') is not None:
            self.last_name_position = m.get('LastNamePosition')
        if m.get('NationalityCode') is not None:
            self.nationality_code = m.get('NationalityCode')
        if m.get('NationalityCodeConfidence') is not None:
            self.nationality_code_confidence = m.get('NationalityCodeConfidence')
        if m.get('NationalityCodePosition') is not None:
            self.nationality_code_position = m.get('NationalityCodePosition')
        if m.get('NormalizedDateOfBirth') is not None:
            self.normalized_date_of_birth = m.get('NormalizedDateOfBirth')
        if m.get('NormalizedExpirationDate') is not None:
            self.normalized_expiration_date = m.get('NormalizedExpirationDate')
        if m.get('NormalizedIssuedDate') is not None:
            self.normalized_issued_date = m.get('NormalizedIssuedDate')
        if m.get('NormalizedNationalityCode') is not None:
            self.normalized_nationality_code = m.get('NormalizedNationalityCode')
        if m.get('NormalizedSex') is not None:
            self.normalized_sex = m.get('NormalizedSex')
        if m.get('Sex') is not None:
            self.sex = m.get('Sex')
        if m.get('SexConfidence') is not None:
            self.sex_confidence = m.get('SexConfidence')
        if m.get('SexPosition') is not None:
            self.sex_position = m.get('SexPosition')
        return self


class IdDetectOcrCompareFacesResponseBodyDataOcrResult(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        ocr_result_data: IdDetectOcrCompareFacesResponseBodyDataOcrResultOcrResultData = None,
    ):
        self.code = code
        self.message = message
        self.ocr_result_data = ocr_result_data

    def validate(self):
        if self.ocr_result_data:
            self.ocr_result_data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.ocr_result_data is not None:
            result['OcrResultData'] = self.ocr_result_data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('OcrResultData') is not None:
            temp_model = IdDetectOcrCompareFacesResponseBodyDataOcrResultOcrResultData()
            self.ocr_result_data = temp_model.from_map(m['OcrResultData'])
        return self


class IdDetectOcrCompareFacesResponseBodyDataUnrepeatResultCardImageResultCardImageResultData(TeaModel):
    def __init__(
        self,
        dbname: str = None,
        entity_id: str = None,
        extra_data: str = None,
        score: float = None,
    ):
        self.dbname = dbname
        self.entity_id = entity_id
        self.extra_data = extra_data
        self.score = score

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbname is not None:
            result['Dbname'] = self.dbname
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.extra_data is not None:
            result['ExtraData'] = self.extra_data
        if self.score is not None:
            result['Score'] = self.score
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Dbname') is not None:
            self.dbname = m.get('Dbname')
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('ExtraData') is not None:
            self.extra_data = m.get('ExtraData')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        return self


class IdDetectOcrCompareFacesResponseBodyDataUnrepeatResultCardImageResult(TeaModel):
    def __init__(
        self,
        card_image_result_data: IdDetectOcrCompareFacesResponseBodyDataUnrepeatResultCardImageResultCardImageResultData = None,
        code: str = None,
        message: str = None,
    ):
        self.card_image_result_data = card_image_result_data
        self.code = code
        self.message = message

    def validate(self):
        if self.card_image_result_data:
            self.card_image_result_data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.card_image_result_data is not None:
            result['CardImageResultData'] = self.card_image_result_data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CardImageResultData') is not None:
            temp_model = IdDetectOcrCompareFacesResponseBodyDataUnrepeatResultCardImageResultCardImageResultData()
            self.card_image_result_data = temp_model.from_map(m['CardImageResultData'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class IdDetectOcrCompareFacesResponseBodyDataUnrepeatResultPortraitImageResultPortraitImageResultData(TeaModel):
    def __init__(
        self,
        dbname: str = None,
        entity_id: str = None,
        extra_data: str = None,
        score: float = None,
    ):
        self.dbname = dbname
        self.entity_id = entity_id
        self.extra_data = extra_data
        self.score = score

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbname is not None:
            result['Dbname'] = self.dbname
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.extra_data is not None:
            result['ExtraData'] = self.extra_data
        if self.score is not None:
            result['Score'] = self.score
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Dbname') is not None:
            self.dbname = m.get('Dbname')
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('ExtraData') is not None:
            self.extra_data = m.get('ExtraData')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        return self


class IdDetectOcrCompareFacesResponseBodyDataUnrepeatResultPortraitImageResult(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        portrait_image_result_data: IdDetectOcrCompareFacesResponseBodyDataUnrepeatResultPortraitImageResultPortraitImageResultData = None,
    ):
        self.code = code
        self.message = message
        self.portrait_image_result_data = portrait_image_result_data

    def validate(self):
        if self.portrait_image_result_data:
            self.portrait_image_result_data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.portrait_image_result_data is not None:
            result['PortraitImageResultData'] = self.portrait_image_result_data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PortraitImageResultData') is not None:
            temp_model = IdDetectOcrCompareFacesResponseBodyDataUnrepeatResultPortraitImageResultPortraitImageResultData()
            self.portrait_image_result_data = temp_model.from_map(m['PortraitImageResultData'])
        return self


class IdDetectOcrCompareFacesResponseBodyDataUnrepeatResult(TeaModel):
    def __init__(
        self,
        card_image_result: IdDetectOcrCompareFacesResponseBodyDataUnrepeatResultCardImageResult = None,
        portrait_image_result: IdDetectOcrCompareFacesResponseBodyDataUnrepeatResultPortraitImageResult = None,
    ):
        self.card_image_result = card_image_result
        self.portrait_image_result = portrait_image_result

    def validate(self):
        if self.card_image_result:
            self.card_image_result.validate()
        if self.portrait_image_result:
            self.portrait_image_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.card_image_result is not None:
            result['CardImageResult'] = self.card_image_result.to_map()
        if self.portrait_image_result is not None:
            result['PortraitImageResult'] = self.portrait_image_result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CardImageResult') is not None:
            temp_model = IdDetectOcrCompareFacesResponseBodyDataUnrepeatResultCardImageResult()
            self.card_image_result = temp_model.from_map(m['CardImageResult'])
        if m.get('PortraitImageResult') is not None:
            temp_model = IdDetectOcrCompareFacesResponseBodyDataUnrepeatResultPortraitImageResult()
            self.portrait_image_result = temp_model.from_map(m['PortraitImageResult'])
        return self


class IdDetectOcrCompareFacesResponseBodyData(TeaModel):
    def __init__(
        self,
        compare_result: IdDetectOcrCompareFacesResponseBodyDataCompareResult = None,
        id_detect_result: IdDetectOcrCompareFacesResponseBodyDataIdDetectResult = None,
        liveness_result: IdDetectOcrCompareFacesResponseBodyDataLivenessResult = None,
        ocr_result: IdDetectOcrCompareFacesResponseBodyDataOcrResult = None,
        unrepeat_result: IdDetectOcrCompareFacesResponseBodyDataUnrepeatResult = None,
    ):
        self.compare_result = compare_result
        self.id_detect_result = id_detect_result
        self.liveness_result = liveness_result
        self.ocr_result = ocr_result
        self.unrepeat_result = unrepeat_result

    def validate(self):
        if self.compare_result:
            self.compare_result.validate()
        if self.id_detect_result:
            self.id_detect_result.validate()
        if self.liveness_result:
            self.liveness_result.validate()
        if self.ocr_result:
            self.ocr_result.validate()
        if self.unrepeat_result:
            self.unrepeat_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compare_result is not None:
            result['CompareResult'] = self.compare_result.to_map()
        if self.id_detect_result is not None:
            result['IdDetectResult'] = self.id_detect_result.to_map()
        if self.liveness_result is not None:
            result['LivenessResult'] = self.liveness_result.to_map()
        if self.ocr_result is not None:
            result['OcrResult'] = self.ocr_result.to_map()
        if self.unrepeat_result is not None:
            result['UnrepeatResult'] = self.unrepeat_result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompareResult') is not None:
            temp_model = IdDetectOcrCompareFacesResponseBodyDataCompareResult()
            self.compare_result = temp_model.from_map(m['CompareResult'])
        if m.get('IdDetectResult') is not None:
            temp_model = IdDetectOcrCompareFacesResponseBodyDataIdDetectResult()
            self.id_detect_result = temp_model.from_map(m['IdDetectResult'])
        if m.get('LivenessResult') is not None:
            temp_model = IdDetectOcrCompareFacesResponseBodyDataLivenessResult()
            self.liveness_result = temp_model.from_map(m['LivenessResult'])
        if m.get('OcrResult') is not None:
            temp_model = IdDetectOcrCompareFacesResponseBodyDataOcrResult()
            self.ocr_result = temp_model.from_map(m['OcrResult'])
        if m.get('UnrepeatResult') is not None:
            temp_model = IdDetectOcrCompareFacesResponseBodyDataUnrepeatResult()
            self.unrepeat_result = temp_model.from_map(m['UnrepeatResult'])
        return self


class IdDetectOcrCompareFacesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: IdDetectOcrCompareFacesResponseBodyData = None,
        http_code: int = None,
        message: str = None,
        ok: bool = None,
        request_id: str = None,
        status: str = None,
    ):
        self.code = code
        self.data = data
        self.http_code = http_code
        self.message = message
        self.ok = ok
        self.request_id = request_id
        self.status = status

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.message is not None:
            result['Message'] = self.message
        if self.ok is not None:
            result['Ok'] = self.ok
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = IdDetectOcrCompareFacesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Ok') is not None:
            self.ok = m.get('Ok')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class IdDetectOcrCompareFacesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: IdDetectOcrCompareFacesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = IdDetectOcrCompareFacesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class IdDetectionAndScanDocumentRequest(TeaModel):
    def __init__(
        self,
        country_code: str = None,
        document_type: str = None,
        image_atype: str = None,
        image_btype: str = None,
        image_data_a: str = None,
        image_data_b: str = None,
        image_url_a: str = None,
        image_url_b: str = None,
    ):
        self.country_code = country_code
        self.document_type = document_type
        self.image_atype = image_atype
        self.image_btype = image_btype
        self.image_data_a = image_data_a
        self.image_data_b = image_data_b
        self.image_url_a = image_url_a
        self.image_url_b = image_url_b

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.country_code is not None:
            result['countryCode'] = self.country_code
        if self.document_type is not None:
            result['documentType'] = self.document_type
        if self.image_atype is not None:
            result['imageAType'] = self.image_atype
        if self.image_btype is not None:
            result['imageBType'] = self.image_btype
        if self.image_data_a is not None:
            result['imageDataA'] = self.image_data_a
        if self.image_data_b is not None:
            result['imageDataB'] = self.image_data_b
        if self.image_url_a is not None:
            result['imageUrlA'] = self.image_url_a
        if self.image_url_b is not None:
            result['imageUrlB'] = self.image_url_b
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('countryCode') is not None:
            self.country_code = m.get('countryCode')
        if m.get('documentType') is not None:
            self.document_type = m.get('documentType')
        if m.get('imageAType') is not None:
            self.image_atype = m.get('imageAType')
        if m.get('imageBType') is not None:
            self.image_btype = m.get('imageBType')
        if m.get('imageDataA') is not None:
            self.image_data_a = m.get('imageDataA')
        if m.get('imageDataB') is not None:
            self.image_data_b = m.get('imageDataB')
        if m.get('imageUrlA') is not None:
            self.image_url_a = m.get('imageUrlA')
        if m.get('imageUrlB') is not None:
            self.image_url_b = m.get('imageUrlB')
        return self


class IdDetectionAndScanDocumentResponseBodyDataIdDetectResultAntiSpoofingResult(TeaModel):
    def __init__(
        self,
        passed: bool = None,
        risks: List[str] = None,
    ):
        self.passed = passed
        self.risks = risks

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.passed is not None:
            result['Passed'] = self.passed
        if self.risks is not None:
            result['Risks'] = self.risks
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Passed') is not None:
            self.passed = m.get('Passed')
        if m.get('Risks') is not None:
            self.risks = m.get('Risks')
        return self


class IdDetectionAndScanDocumentResponseBodyDataIdDetectResultDetectionResult(TeaModel):
    def __init__(
        self,
        card_rectangle: List[int] = None,
        height: int = None,
        portrait_rectangle: List[int] = None,
        width: int = None,
    ):
        self.card_rectangle = card_rectangle
        self.height = height
        self.portrait_rectangle = portrait_rectangle
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.card_rectangle is not None:
            result['CardRectangle'] = self.card_rectangle
        if self.height is not None:
            result['Height'] = self.height
        if self.portrait_rectangle is not None:
            result['PortraitRectangle'] = self.portrait_rectangle
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CardRectangle') is not None:
            self.card_rectangle = m.get('CardRectangle')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('PortraitRectangle') is not None:
            self.portrait_rectangle = m.get('PortraitRectangle')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class IdDetectionAndScanDocumentResponseBodyDataIdDetectResult(TeaModel):
    def __init__(
        self,
        anti_spoofing_result: IdDetectionAndScanDocumentResponseBodyDataIdDetectResultAntiSpoofingResult = None,
        country_code: str = None,
        detection_result: IdDetectionAndScanDocumentResponseBodyDataIdDetectResultDetectionResult = None,
        document_type: str = None,
        passed: bool = None,
        warning: List[str] = None,
    ):
        self.anti_spoofing_result = anti_spoofing_result
        self.country_code = country_code
        self.detection_result = detection_result
        self.document_type = document_type
        self.passed = passed
        self.warning = warning

    def validate(self):
        if self.anti_spoofing_result:
            self.anti_spoofing_result.validate()
        if self.detection_result:
            self.detection_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.anti_spoofing_result is not None:
            result['AntiSpoofingResult'] = self.anti_spoofing_result.to_map()
        if self.country_code is not None:
            result['CountryCode'] = self.country_code
        if self.detection_result is not None:
            result['DetectionResult'] = self.detection_result.to_map()
        if self.document_type is not None:
            result['DocumentType'] = self.document_type
        if self.passed is not None:
            result['Passed'] = self.passed
        if self.warning is not None:
            result['Warning'] = self.warning
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AntiSpoofingResult') is not None:
            temp_model = IdDetectionAndScanDocumentResponseBodyDataIdDetectResultAntiSpoofingResult()
            self.anti_spoofing_result = temp_model.from_map(m['AntiSpoofingResult'])
        if m.get('CountryCode') is not None:
            self.country_code = m.get('CountryCode')
        if m.get('DetectionResult') is not None:
            temp_model = IdDetectionAndScanDocumentResponseBodyDataIdDetectResultDetectionResult()
            self.detection_result = temp_model.from_map(m['DetectionResult'])
        if m.get('DocumentType') is not None:
            self.document_type = m.get('DocumentType')
        if m.get('Passed') is not None:
            self.passed = m.get('Passed')
        if m.get('Warning') is not None:
            self.warning = m.get('Warning')
        return self


class IdDetectionAndScanDocumentResponseBodyDataOcrResult(TeaModel):
    def __init__(
        self,
        address: str = None,
        address_confidence: float = None,
        address_position: List[int] = None,
        date_of_birth: str = None,
        date_of_birth_confidence: float = None,
        date_of_birth_position: List[int] = None,
        document_number: str = None,
        document_number_2: str = None,
        document_number_2confidence: float = None,
        document_number_2position: List[int] = None,
        document_number_confidence: float = None,
        document_number_position: List[int] = None,
        expiration_date: str = None,
        expiration_date_confidence: float = None,
        expiration_date_position: List[int] = None,
        first_name: str = None,
        first_name_confidence: float = None,
        first_name_position: List[int] = None,
        full_name: str = None,
        full_name_confidence: float = None,
        full_name_position: List[int] = None,
        issued_date: str = None,
        issued_date_confidence: float = None,
        issued_date_position: List[int] = None,
        issuing_authority: str = None,
        issuing_authority_confidence: float = None,
        issuing_authority_position: List[int] = None,
        last_name: str = None,
        last_name_confidence: float = None,
        last_name_position: List[int] = None,
        nationality_code: str = None,
        nationality_code_confidence: float = None,
        nationality_code_position: List[int] = None,
        normalized_date_of_birth: str = None,
        normalized_expiration_date: str = None,
        normalized_issued_date: str = None,
        normalized_nationality_code: str = None,
        normalized_sex: str = None,
        sex: str = None,
        sex_confidence: float = None,
        sex_position: List[int] = None,
    ):
        self.address = address
        self.address_confidence = address_confidence
        self.address_position = address_position
        self.date_of_birth = date_of_birth
        self.date_of_birth_confidence = date_of_birth_confidence
        self.date_of_birth_position = date_of_birth_position
        self.document_number = document_number
        self.document_number_2 = document_number_2
        self.document_number_2confidence = document_number_2confidence
        self.document_number_2position = document_number_2position
        self.document_number_confidence = document_number_confidence
        self.document_number_position = document_number_position
        self.expiration_date = expiration_date
        self.expiration_date_confidence = expiration_date_confidence
        self.expiration_date_position = expiration_date_position
        self.first_name = first_name
        self.first_name_confidence = first_name_confidence
        self.first_name_position = first_name_position
        self.full_name = full_name
        self.full_name_confidence = full_name_confidence
        self.full_name_position = full_name_position
        self.issued_date = issued_date
        self.issued_date_confidence = issued_date_confidence
        self.issued_date_position = issued_date_position
        self.issuing_authority = issuing_authority
        self.issuing_authority_confidence = issuing_authority_confidence
        self.issuing_authority_position = issuing_authority_position
        self.last_name = last_name
        self.last_name_confidence = last_name_confidence
        self.last_name_position = last_name_position
        self.nationality_code = nationality_code
        self.nationality_code_confidence = nationality_code_confidence
        self.nationality_code_position = nationality_code_position
        self.normalized_date_of_birth = normalized_date_of_birth
        self.normalized_expiration_date = normalized_expiration_date
        self.normalized_issued_date = normalized_issued_date
        self.normalized_nationality_code = normalized_nationality_code
        self.normalized_sex = normalized_sex
        self.sex = sex
        self.sex_confidence = sex_confidence
        self.sex_position = sex_position

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.address_confidence is not None:
            result['AddressConfidence'] = self.address_confidence
        if self.address_position is not None:
            result['AddressPosition'] = self.address_position
        if self.date_of_birth is not None:
            result['DateOfBirth'] = self.date_of_birth
        if self.date_of_birth_confidence is not None:
            result['DateOfBirthConfidence'] = self.date_of_birth_confidence
        if self.date_of_birth_position is not None:
            result['DateOfBirthPosition'] = self.date_of_birth_position
        if self.document_number is not None:
            result['DocumentNumber'] = self.document_number
        if self.document_number_2 is not None:
            result['DocumentNumber2'] = self.document_number_2
        if self.document_number_2confidence is not None:
            result['DocumentNumber2Confidence'] = self.document_number_2confidence
        if self.document_number_2position is not None:
            result['DocumentNumber2Position'] = self.document_number_2position
        if self.document_number_confidence is not None:
            result['DocumentNumberConfidence'] = self.document_number_confidence
        if self.document_number_position is not None:
            result['DocumentNumberPosition'] = self.document_number_position
        if self.expiration_date is not None:
            result['ExpirationDate'] = self.expiration_date
        if self.expiration_date_confidence is not None:
            result['ExpirationDateConfidence'] = self.expiration_date_confidence
        if self.expiration_date_position is not None:
            result['ExpirationDatePosition'] = self.expiration_date_position
        if self.first_name is not None:
            result['FirstName'] = self.first_name
        if self.first_name_confidence is not None:
            result['FirstNameConfidence'] = self.first_name_confidence
        if self.first_name_position is not None:
            result['FirstNamePosition'] = self.first_name_position
        if self.full_name is not None:
            result['FullName'] = self.full_name
        if self.full_name_confidence is not None:
            result['FullNameConfidence'] = self.full_name_confidence
        if self.full_name_position is not None:
            result['FullNamePosition'] = self.full_name_position
        if self.issued_date is not None:
            result['IssuedDate'] = self.issued_date
        if self.issued_date_confidence is not None:
            result['IssuedDateConfidence'] = self.issued_date_confidence
        if self.issued_date_position is not None:
            result['IssuedDatePosition'] = self.issued_date_position
        if self.issuing_authority is not None:
            result['IssuingAuthority'] = self.issuing_authority
        if self.issuing_authority_confidence is not None:
            result['IssuingAuthorityConfidence'] = self.issuing_authority_confidence
        if self.issuing_authority_position is not None:
            result['IssuingAuthorityPosition'] = self.issuing_authority_position
        if self.last_name is not None:
            result['LastName'] = self.last_name
        if self.last_name_confidence is not None:
            result['LastNameConfidence'] = self.last_name_confidence
        if self.last_name_position is not None:
            result['LastNamePosition'] = self.last_name_position
        if self.nationality_code is not None:
            result['NationalityCode'] = self.nationality_code
        if self.nationality_code_confidence is not None:
            result['NationalityCodeConfidence'] = self.nationality_code_confidence
        if self.nationality_code_position is not None:
            result['NationalityCodePosition'] = self.nationality_code_position
        if self.normalized_date_of_birth is not None:
            result['NormalizedDateOfBirth'] = self.normalized_date_of_birth
        if self.normalized_expiration_date is not None:
            result['NormalizedExpirationDate'] = self.normalized_expiration_date
        if self.normalized_issued_date is not None:
            result['NormalizedIssuedDate'] = self.normalized_issued_date
        if self.normalized_nationality_code is not None:
            result['NormalizedNationalityCode'] = self.normalized_nationality_code
        if self.normalized_sex is not None:
            result['NormalizedSex'] = self.normalized_sex
        if self.sex is not None:
            result['Sex'] = self.sex
        if self.sex_confidence is not None:
            result['SexConfidence'] = self.sex_confidence
        if self.sex_position is not None:
            result['SexPosition'] = self.sex_position
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('AddressConfidence') is not None:
            self.address_confidence = m.get('AddressConfidence')
        if m.get('AddressPosition') is not None:
            self.address_position = m.get('AddressPosition')
        if m.get('DateOfBirth') is not None:
            self.date_of_birth = m.get('DateOfBirth')
        if m.get('DateOfBirthConfidence') is not None:
            self.date_of_birth_confidence = m.get('DateOfBirthConfidence')
        if m.get('DateOfBirthPosition') is not None:
            self.date_of_birth_position = m.get('DateOfBirthPosition')
        if m.get('DocumentNumber') is not None:
            self.document_number = m.get('DocumentNumber')
        if m.get('DocumentNumber2') is not None:
            self.document_number_2 = m.get('DocumentNumber2')
        if m.get('DocumentNumber2Confidence') is not None:
            self.document_number_2confidence = m.get('DocumentNumber2Confidence')
        if m.get('DocumentNumber2Position') is not None:
            self.document_number_2position = m.get('DocumentNumber2Position')
        if m.get('DocumentNumberConfidence') is not None:
            self.document_number_confidence = m.get('DocumentNumberConfidence')
        if m.get('DocumentNumberPosition') is not None:
            self.document_number_position = m.get('DocumentNumberPosition')
        if m.get('ExpirationDate') is not None:
            self.expiration_date = m.get('ExpirationDate')
        if m.get('ExpirationDateConfidence') is not None:
            self.expiration_date_confidence = m.get('ExpirationDateConfidence')
        if m.get('ExpirationDatePosition') is not None:
            self.expiration_date_position = m.get('ExpirationDatePosition')
        if m.get('FirstName') is not None:
            self.first_name = m.get('FirstName')
        if m.get('FirstNameConfidence') is not None:
            self.first_name_confidence = m.get('FirstNameConfidence')
        if m.get('FirstNamePosition') is not None:
            self.first_name_position = m.get('FirstNamePosition')
        if m.get('FullName') is not None:
            self.full_name = m.get('FullName')
        if m.get('FullNameConfidence') is not None:
            self.full_name_confidence = m.get('FullNameConfidence')
        if m.get('FullNamePosition') is not None:
            self.full_name_position = m.get('FullNamePosition')
        if m.get('IssuedDate') is not None:
            self.issued_date = m.get('IssuedDate')
        if m.get('IssuedDateConfidence') is not None:
            self.issued_date_confidence = m.get('IssuedDateConfidence')
        if m.get('IssuedDatePosition') is not None:
            self.issued_date_position = m.get('IssuedDatePosition')
        if m.get('IssuingAuthority') is not None:
            self.issuing_authority = m.get('IssuingAuthority')
        if m.get('IssuingAuthorityConfidence') is not None:
            self.issuing_authority_confidence = m.get('IssuingAuthorityConfidence')
        if m.get('IssuingAuthorityPosition') is not None:
            self.issuing_authority_position = m.get('IssuingAuthorityPosition')
        if m.get('LastName') is not None:
            self.last_name = m.get('LastName')
        if m.get('LastNameConfidence') is not None:
            self.last_name_confidence = m.get('LastNameConfidence')
        if m.get('LastNamePosition') is not None:
            self.last_name_position = m.get('LastNamePosition')
        if m.get('NationalityCode') is not None:
            self.nationality_code = m.get('NationalityCode')
        if m.get('NationalityCodeConfidence') is not None:
            self.nationality_code_confidence = m.get('NationalityCodeConfidence')
        if m.get('NationalityCodePosition') is not None:
            self.nationality_code_position = m.get('NationalityCodePosition')
        if m.get('NormalizedDateOfBirth') is not None:
            self.normalized_date_of_birth = m.get('NormalizedDateOfBirth')
        if m.get('NormalizedExpirationDate') is not None:
            self.normalized_expiration_date = m.get('NormalizedExpirationDate')
        if m.get('NormalizedIssuedDate') is not None:
            self.normalized_issued_date = m.get('NormalizedIssuedDate')
        if m.get('NormalizedNationalityCode') is not None:
            self.normalized_nationality_code = m.get('NormalizedNationalityCode')
        if m.get('NormalizedSex') is not None:
            self.normalized_sex = m.get('NormalizedSex')
        if m.get('Sex') is not None:
            self.sex = m.get('Sex')
        if m.get('SexConfidence') is not None:
            self.sex_confidence = m.get('SexConfidence')
        if m.get('SexPosition') is not None:
            self.sex_position = m.get('SexPosition')
        return self


class IdDetectionAndScanDocumentResponseBodyData(TeaModel):
    def __init__(
        self,
        id_detect_result: IdDetectionAndScanDocumentResponseBodyDataIdDetectResult = None,
        ocr_result: IdDetectionAndScanDocumentResponseBodyDataOcrResult = None,
    ):
        self.id_detect_result = id_detect_result
        self.ocr_result = ocr_result

    def validate(self):
        if self.id_detect_result:
            self.id_detect_result.validate()
        if self.ocr_result:
            self.ocr_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id_detect_result is not None:
            result['IdDetectResult'] = self.id_detect_result.to_map()
        if self.ocr_result is not None:
            result['OcrResult'] = self.ocr_result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IdDetectResult') is not None:
            temp_model = IdDetectionAndScanDocumentResponseBodyDataIdDetectResult()
            self.id_detect_result = temp_model.from_map(m['IdDetectResult'])
        if m.get('OcrResult') is not None:
            temp_model = IdDetectionAndScanDocumentResponseBodyDataOcrResult()
            self.ocr_result = temp_model.from_map(m['OcrResult'])
        return self


class IdDetectionAndScanDocumentResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: IdDetectionAndScanDocumentResponseBodyData = None,
        http_code: int = None,
        message: str = None,
        ok: bool = None,
        request_id: str = None,
        status: str = None,
    ):
        self.code = code
        self.data = data
        self.http_code = http_code
        self.message = message
        self.ok = ok
        self.request_id = request_id
        self.status = status

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.message is not None:
            result['Message'] = self.message
        if self.ok is not None:
            result['Ok'] = self.ok
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = IdDetectionAndScanDocumentResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Ok') is not None:
            self.ok = m.get('Ok')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class IdDetectionAndScanDocumentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: IdDetectionAndScanDocumentResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = IdDetectionAndScanDocumentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ScanDocumentRequest(TeaModel):
    def __init__(
        self,
        country_code: str = None,
        document_type: str = None,
        image_atype: str = None,
        image_btype: str = None,
        image_data_a: str = None,
        image_data_b: str = None,
        image_url_a: str = None,
        image_url_b: str = None,
    ):
        # The country or region code of the certificate. Specify the code in the ISO 3166 alpha-3 format.
        self.country_code = country_code
        # The type of the certificate.
        # 
        # Valid values:
        # 
        # *   IDENTITY_CARD
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   DRIVER_LICENSE
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   RESIDENCE_CARD
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   PASSPORT
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.document_type = document_type
        # Indicates whether the uploaded front-side image is in an image format or PDF format. The default value is pic.
        self.image_atype = image_atype
        # Indicates whether the uploaded back-side image is in an image format or PDF format. The default value is pic.
        self.image_btype = image_btype
        # The Base64-encoded front-side image of the certificate. Either this parameter or the imageUrlA parameter must be specified.
        self.image_data_a = image_data_a
        # The Base64-encoded back-side image of the certificate.
        self.image_data_b = image_data_b
        # The URL of the front-side image of the certificate. Either this parameter or the imageDataA parameter must be specified.
        self.image_url_a = image_url_a
        # The URL of the back-side image of the certificate.
        self.image_url_b = image_url_b

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.country_code is not None:
            result['countryCode'] = self.country_code
        if self.document_type is not None:
            result['documentType'] = self.document_type
        if self.image_atype is not None:
            result['imageAType'] = self.image_atype
        if self.image_btype is not None:
            result['imageBType'] = self.image_btype
        if self.image_data_a is not None:
            result['imageDataA'] = self.image_data_a
        if self.image_data_b is not None:
            result['imageDataB'] = self.image_data_b
        if self.image_url_a is not None:
            result['imageUrlA'] = self.image_url_a
        if self.image_url_b is not None:
            result['imageUrlB'] = self.image_url_b
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('countryCode') is not None:
            self.country_code = m.get('countryCode')
        if m.get('documentType') is not None:
            self.document_type = m.get('documentType')
        if m.get('imageAType') is not None:
            self.image_atype = m.get('imageAType')
        if m.get('imageBType') is not None:
            self.image_btype = m.get('imageBType')
        if m.get('imageDataA') is not None:
            self.image_data_a = m.get('imageDataA')
        if m.get('imageDataB') is not None:
            self.image_data_b = m.get('imageDataB')
        if m.get('imageUrlA') is not None:
            self.image_url_a = m.get('imageUrlA')
        if m.get('imageUrlB') is not None:
            self.image_url_b = m.get('imageUrlB')
        return self


class ScanDocumentResponseBodyData(TeaModel):
    def __init__(
        self,
        address: str = None,
        address_confidence: float = None,
        address_position: List[int] = None,
        date_of_birth: str = None,
        date_of_birth_confidence: float = None,
        date_of_birth_position: List[int] = None,
        document_number: str = None,
        document_number_2: str = None,
        document_number_2confidence: float = None,
        document_number_2position: List[int] = None,
        document_number_confidence: float = None,
        document_number_position: List[int] = None,
        expiration_date: str = None,
        expiration_date_confidence: float = None,
        expiration_date_position: List[int] = None,
        first_name: str = None,
        first_name_confidence: float = None,
        first_name_position: List[int] = None,
        full_name: str = None,
        full_name_confidence: float = None,
        full_name_position: List[int] = None,
        issued_date: str = None,
        issued_date_confidence: float = None,
        issued_date_position: List[int] = None,
        issuing_authority: str = None,
        issuing_authority_confidence: float = None,
        issuing_authority_position: List[int] = None,
        last_name: str = None,
        last_name_confidence: float = None,
        last_name_position: List[int] = None,
        nationality_code: str = None,
        nationality_code_confidence: float = None,
        nationality_code_position: List[int] = None,
        normalized_date_of_birth: str = None,
        normalized_expiration_date: str = None,
        normalized_issued_date: str = None,
        normalized_nationality_code: str = None,
        normalized_sex: str = None,
        sex: str = None,
        sex_confidence: float = None,
        sex_position: List[int] = None,
    ):
        # The address.
        self.address = address
        # The confidence level of the recognized Address.
        self.address_confidence = address_confidence
        # The coordinates of four vertices of the Address field area in the clockwise sequence: the upper left, upper right, lower right, and lower left.
        self.address_position = address_position
        # The date of birth.
        self.date_of_birth = date_of_birth
        # The confidence level of the recognized DateOfBirth.
        self.date_of_birth_confidence = date_of_birth_confidence
        # The coordinates of four vertices of the DateOfBirth field area in the clockwise sequence: the upper left, upper right, lower right, and lower left.
        self.date_of_birth_position = date_of_birth_position
        # The certificate number.
        self.document_number = document_number
        # The secondary certificate number.
        self.document_number_2 = document_number_2
        # The confidence level of the recognized DocumentNumber2.
        self.document_number_2confidence = document_number_2confidence
        # The coordinates of four vertices of the DocumentNumber2 field area in the clockwise sequence: the upper left, upper right, lower right, and lower left.
        self.document_number_2position = document_number_2position
        # The confidence level of the recognized DocumentNumber.
        self.document_number_confidence = document_number_confidence
        # The coordinates of four vertices of the DocumentNumber field area in the clockwise sequence: the upper left, upper right, lower right, and lower left.
        self.document_number_position = document_number_position
        # The expiration date of the certificate.
        self.expiration_date = expiration_date
        # The confidence level of the recognized ExpirationDate.
        self.expiration_date_confidence = expiration_date_confidence
        # The coordinates of four vertices of the ExpirationDate field area in the clockwise sequence: the upper left, upper right, lower right, and lower left.
        self.expiration_date_position = expiration_date_position
        # The first name.
        self.first_name = first_name
        # The confidence level of the recognized FirstName field.
        self.first_name_confidence = first_name_confidence
        # The coordinates of four vertices of the FirstName field area in the clockwise sequence: the upper left, upper right, lower right, and lower left.
        self.first_name_position = first_name_position
        # The full name.
        self.full_name = full_name
        # The confidence level of the recognized FullName.
        self.full_name_confidence = full_name_confidence
        # The coordinates of four vertices of the FullName field area in the clockwise sequence: the upper left, upper right, lower right, and lower left.
        self.full_name_position = full_name_position
        # The date of issue.
        self.issued_date = issued_date
        # The confidence level of the recognized IssuedDate.
        self.issued_date_confidence = issued_date_confidence
        # The coordinates of four vertices of the IssuedDate field area in the clockwise sequence: the upper left, upper right, lower right, and lower left.
        self.issued_date_position = issued_date_position
        # The organization that issued the certificate.
        self.issuing_authority = issuing_authority
        # The confidence level of the recognized IssuingAuthority.
        self.issuing_authority_confidence = issuing_authority_confidence
        # The coordinates of four vertices of the IssuingAuthority field area in the clockwise sequence: the upper left, upper right, lower right, and lower left.
        self.issuing_authority_position = issuing_authority_position
        # The last name.
        self.last_name = last_name
        # The confidence level of the recognized LastName.
        self.last_name_confidence = last_name_confidence
        # The coordinates of four vertices of the LastName field area in the clockwise sequence: the upper left, upper right, lower right, and lower left.
        self.last_name_position = last_name_position
        # The country or region code on the certificate.
        self.nationality_code = nationality_code
        # The confidence level of the recognized NationalityCode.
        self.nationality_code_confidence = nationality_code_confidence
        # The coordinates of four vertices of the NationalityCode field area in the clockwise sequence: the upper left, upper right, lower right, and lower left.
        self.nationality_code_position = nationality_code_position
        # The date of birth in the format of YYYY/MM/dd.
        self.normalized_date_of_birth = normalized_date_of_birth
        # The expiration date in the format of YYYY/MM/dd.
        self.normalized_expiration_date = normalized_expiration_date
        # The date of issue in the format of YYYY/MM/dd.
        self.normalized_issued_date = normalized_issued_date
        # The country or region code in the ISO 3166 alpha-3 format.
        self.normalized_nationality_code = normalized_nationality_code
        # The gender.
        # 
        # Valid values:
        # 
        # *   null
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   F
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     female
        # 
        #     <!-- -->
        # 
        # *   M
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     male
        # 
        #     <!-- -->
        self.normalized_sex = normalized_sex
        # The gender.
        self.sex = sex
        # The confidence level of the recognized Sex.
        self.sex_confidence = sex_confidence
        # The coordinates of four vertices of the Sex field area in the clockwise sequence: the upper left, upper right, lower right, and lower left.
        self.sex_position = sex_position

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.address_confidence is not None:
            result['AddressConfidence'] = self.address_confidence
        if self.address_position is not None:
            result['AddressPosition'] = self.address_position
        if self.date_of_birth is not None:
            result['DateOfBirth'] = self.date_of_birth
        if self.date_of_birth_confidence is not None:
            result['DateOfBirthConfidence'] = self.date_of_birth_confidence
        if self.date_of_birth_position is not None:
            result['DateOfBirthPosition'] = self.date_of_birth_position
        if self.document_number is not None:
            result['DocumentNumber'] = self.document_number
        if self.document_number_2 is not None:
            result['DocumentNumber2'] = self.document_number_2
        if self.document_number_2confidence is not None:
            result['DocumentNumber2Confidence'] = self.document_number_2confidence
        if self.document_number_2position is not None:
            result['DocumentNumber2Position'] = self.document_number_2position
        if self.document_number_confidence is not None:
            result['DocumentNumberConfidence'] = self.document_number_confidence
        if self.document_number_position is not None:
            result['DocumentNumberPosition'] = self.document_number_position
        if self.expiration_date is not None:
            result['ExpirationDate'] = self.expiration_date
        if self.expiration_date_confidence is not None:
            result['ExpirationDateConfidence'] = self.expiration_date_confidence
        if self.expiration_date_position is not None:
            result['ExpirationDatePosition'] = self.expiration_date_position
        if self.first_name is not None:
            result['FirstName'] = self.first_name
        if self.first_name_confidence is not None:
            result['FirstNameConfidence'] = self.first_name_confidence
        if self.first_name_position is not None:
            result['FirstNamePosition'] = self.first_name_position
        if self.full_name is not None:
            result['FullName'] = self.full_name
        if self.full_name_confidence is not None:
            result['FullNameConfidence'] = self.full_name_confidence
        if self.full_name_position is not None:
            result['FullNamePosition'] = self.full_name_position
        if self.issued_date is not None:
            result['IssuedDate'] = self.issued_date
        if self.issued_date_confidence is not None:
            result['IssuedDateConfidence'] = self.issued_date_confidence
        if self.issued_date_position is not None:
            result['IssuedDatePosition'] = self.issued_date_position
        if self.issuing_authority is not None:
            result['IssuingAuthority'] = self.issuing_authority
        if self.issuing_authority_confidence is not None:
            result['IssuingAuthorityConfidence'] = self.issuing_authority_confidence
        if self.issuing_authority_position is not None:
            result['IssuingAuthorityPosition'] = self.issuing_authority_position
        if self.last_name is not None:
            result['LastName'] = self.last_name
        if self.last_name_confidence is not None:
            result['LastNameConfidence'] = self.last_name_confidence
        if self.last_name_position is not None:
            result['LastNamePosition'] = self.last_name_position
        if self.nationality_code is not None:
            result['NationalityCode'] = self.nationality_code
        if self.nationality_code_confidence is not None:
            result['NationalityCodeConfidence'] = self.nationality_code_confidence
        if self.nationality_code_position is not None:
            result['NationalityCodePosition'] = self.nationality_code_position
        if self.normalized_date_of_birth is not None:
            result['NormalizedDateOfBirth'] = self.normalized_date_of_birth
        if self.normalized_expiration_date is not None:
            result['NormalizedExpirationDate'] = self.normalized_expiration_date
        if self.normalized_issued_date is not None:
            result['NormalizedIssuedDate'] = self.normalized_issued_date
        if self.normalized_nationality_code is not None:
            result['NormalizedNationalityCode'] = self.normalized_nationality_code
        if self.normalized_sex is not None:
            result['NormalizedSex'] = self.normalized_sex
        if self.sex is not None:
            result['Sex'] = self.sex
        if self.sex_confidence is not None:
            result['SexConfidence'] = self.sex_confidence
        if self.sex_position is not None:
            result['SexPosition'] = self.sex_position
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('AddressConfidence') is not None:
            self.address_confidence = m.get('AddressConfidence')
        if m.get('AddressPosition') is not None:
            self.address_position = m.get('AddressPosition')
        if m.get('DateOfBirth') is not None:
            self.date_of_birth = m.get('DateOfBirth')
        if m.get('DateOfBirthConfidence') is not None:
            self.date_of_birth_confidence = m.get('DateOfBirthConfidence')
        if m.get('DateOfBirthPosition') is not None:
            self.date_of_birth_position = m.get('DateOfBirthPosition')
        if m.get('DocumentNumber') is not None:
            self.document_number = m.get('DocumentNumber')
        if m.get('DocumentNumber2') is not None:
            self.document_number_2 = m.get('DocumentNumber2')
        if m.get('DocumentNumber2Confidence') is not None:
            self.document_number_2confidence = m.get('DocumentNumber2Confidence')
        if m.get('DocumentNumber2Position') is not None:
            self.document_number_2position = m.get('DocumentNumber2Position')
        if m.get('DocumentNumberConfidence') is not None:
            self.document_number_confidence = m.get('DocumentNumberConfidence')
        if m.get('DocumentNumberPosition') is not None:
            self.document_number_position = m.get('DocumentNumberPosition')
        if m.get('ExpirationDate') is not None:
            self.expiration_date = m.get('ExpirationDate')
        if m.get('ExpirationDateConfidence') is not None:
            self.expiration_date_confidence = m.get('ExpirationDateConfidence')
        if m.get('ExpirationDatePosition') is not None:
            self.expiration_date_position = m.get('ExpirationDatePosition')
        if m.get('FirstName') is not None:
            self.first_name = m.get('FirstName')
        if m.get('FirstNameConfidence') is not None:
            self.first_name_confidence = m.get('FirstNameConfidence')
        if m.get('FirstNamePosition') is not None:
            self.first_name_position = m.get('FirstNamePosition')
        if m.get('FullName') is not None:
            self.full_name = m.get('FullName')
        if m.get('FullNameConfidence') is not None:
            self.full_name_confidence = m.get('FullNameConfidence')
        if m.get('FullNamePosition') is not None:
            self.full_name_position = m.get('FullNamePosition')
        if m.get('IssuedDate') is not None:
            self.issued_date = m.get('IssuedDate')
        if m.get('IssuedDateConfidence') is not None:
            self.issued_date_confidence = m.get('IssuedDateConfidence')
        if m.get('IssuedDatePosition') is not None:
            self.issued_date_position = m.get('IssuedDatePosition')
        if m.get('IssuingAuthority') is not None:
            self.issuing_authority = m.get('IssuingAuthority')
        if m.get('IssuingAuthorityConfidence') is not None:
            self.issuing_authority_confidence = m.get('IssuingAuthorityConfidence')
        if m.get('IssuingAuthorityPosition') is not None:
            self.issuing_authority_position = m.get('IssuingAuthorityPosition')
        if m.get('LastName') is not None:
            self.last_name = m.get('LastName')
        if m.get('LastNameConfidence') is not None:
            self.last_name_confidence = m.get('LastNameConfidence')
        if m.get('LastNamePosition') is not None:
            self.last_name_position = m.get('LastNamePosition')
        if m.get('NationalityCode') is not None:
            self.nationality_code = m.get('NationalityCode')
        if m.get('NationalityCodeConfidence') is not None:
            self.nationality_code_confidence = m.get('NationalityCodeConfidence')
        if m.get('NationalityCodePosition') is not None:
            self.nationality_code_position = m.get('NationalityCodePosition')
        if m.get('NormalizedDateOfBirth') is not None:
            self.normalized_date_of_birth = m.get('NormalizedDateOfBirth')
        if m.get('NormalizedExpirationDate') is not None:
            self.normalized_expiration_date = m.get('NormalizedExpirationDate')
        if m.get('NormalizedIssuedDate') is not None:
            self.normalized_issued_date = m.get('NormalizedIssuedDate')
        if m.get('NormalizedNationalityCode') is not None:
            self.normalized_nationality_code = m.get('NormalizedNationalityCode')
        if m.get('NormalizedSex') is not None:
            self.normalized_sex = m.get('NormalizedSex')
        if m.get('Sex') is not None:
            self.sex = m.get('Sex')
        if m.get('SexConfidence') is not None:
            self.sex_confidence = m.get('SexConfidence')
        if m.get('SexPosition') is not None:
            self.sex_position = m.get('SexPosition')
        return self


class ScanDocumentResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ScanDocumentResponseBodyData = None,
        http_code: int = None,
        message: str = None,
        ok: bool = None,
        request_id: str = None,
        status: str = None,
    ):
        # The error code. A value of 0 indicates that the request is successful.
        self.code = code
        # The returned data.
        self.data = data
        # The HTTP status code.
        self.http_code = http_code
        # The error messages.
        self.message = message
        # Indicates whether the request is successful.
        # 
        # Valid values:
        # 
        # *   true
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   false
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.ok = ok
        # The ID of the request.
        self.request_id = request_id
        # The status of the request.
        self.status = status

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.message is not None:
            result['Message'] = self.message
        if self.ok is not None:
            result['Ok'] = self.ok
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ScanDocumentResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Ok') is not None:
            self.ok = m.get('Ok')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ScanDocumentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ScanDocumentResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ScanDocumentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class VerifyDocumentRequest(TeaModel):
    def __init__(
        self,
        country_code: str = None,
        det_thickness: bool = None,
        document_type: str = None,
        image_atype: str = None,
        image_btype: str = None,
        image_ctype: str = None,
        image_data_a: str = None,
        image_data_b: str = None,
        image_data_c: str = None,
        image_url_a: str = None,
        image_url_b: str = None,
        image_url_c: str = None,
    ):
        self.country_code = country_code
        self.det_thickness = det_thickness
        self.document_type = document_type
        self.image_atype = image_atype
        self.image_btype = image_btype
        self.image_ctype = image_ctype
        self.image_data_a = image_data_a
        self.image_data_b = image_data_b
        self.image_data_c = image_data_c
        self.image_url_a = image_url_a
        self.image_url_b = image_url_b
        self.image_url_c = image_url_c

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.country_code is not None:
            result['countryCode'] = self.country_code
        if self.det_thickness is not None:
            result['detThickness'] = self.det_thickness
        if self.document_type is not None:
            result['documentType'] = self.document_type
        if self.image_atype is not None:
            result['imageAType'] = self.image_atype
        if self.image_btype is not None:
            result['imageBType'] = self.image_btype
        if self.image_ctype is not None:
            result['imageCType'] = self.image_ctype
        if self.image_data_a is not None:
            result['imageDataA'] = self.image_data_a
        if self.image_data_b is not None:
            result['imageDataB'] = self.image_data_b
        if self.image_data_c is not None:
            result['imageDataC'] = self.image_data_c
        if self.image_url_a is not None:
            result['imageUrlA'] = self.image_url_a
        if self.image_url_b is not None:
            result['imageUrlB'] = self.image_url_b
        if self.image_url_c is not None:
            result['imageUrlC'] = self.image_url_c
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('countryCode') is not None:
            self.country_code = m.get('countryCode')
        if m.get('detThickness') is not None:
            self.det_thickness = m.get('detThickness')
        if m.get('documentType') is not None:
            self.document_type = m.get('documentType')
        if m.get('imageAType') is not None:
            self.image_atype = m.get('imageAType')
        if m.get('imageBType') is not None:
            self.image_btype = m.get('imageBType')
        if m.get('imageCType') is not None:
            self.image_ctype = m.get('imageCType')
        if m.get('imageDataA') is not None:
            self.image_data_a = m.get('imageDataA')
        if m.get('imageDataB') is not None:
            self.image_data_b = m.get('imageDataB')
        if m.get('imageDataC') is not None:
            self.image_data_c = m.get('imageDataC')
        if m.get('imageUrlA') is not None:
            self.image_url_a = m.get('imageUrlA')
        if m.get('imageUrlB') is not None:
            self.image_url_b = m.get('imageUrlB')
        if m.get('imageUrlC') is not None:
            self.image_url_c = m.get('imageUrlC')
        return self


class VerifyDocumentResponseBodyDataAntiSpoofingResult(TeaModel):
    def __init__(
        self,
        passed: bool = None,
        risks: List[str] = None,
    ):
        self.passed = passed
        self.risks = risks

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.passed is not None:
            result['Passed'] = self.passed
        if self.risks is not None:
            result['Risks'] = self.risks
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Passed') is not None:
            self.passed = m.get('Passed')
        if m.get('Risks') is not None:
            self.risks = m.get('Risks')
        return self


class VerifyDocumentResponseBodyDataDetectionResult(TeaModel):
    def __init__(
        self,
        card_rectangle: List[int] = None,
        height: int = None,
        portrait_rectangle: List[int] = None,
        width: int = None,
    ):
        self.card_rectangle = card_rectangle
        self.height = height
        self.portrait_rectangle = portrait_rectangle
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.card_rectangle is not None:
            result['CardRectangle'] = self.card_rectangle
        if self.height is not None:
            result['Height'] = self.height
        if self.portrait_rectangle is not None:
            result['PortraitRectangle'] = self.portrait_rectangle
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CardRectangle') is not None:
            self.card_rectangle = m.get('CardRectangle')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('PortraitRectangle') is not None:
            self.portrait_rectangle = m.get('PortraitRectangle')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class VerifyDocumentResponseBodyData(TeaModel):
    def __init__(
        self,
        anti_spoofing_result: VerifyDocumentResponseBodyDataAntiSpoofingResult = None,
        country_code: str = None,
        detection_result: VerifyDocumentResponseBodyDataDetectionResult = None,
        document_type: str = None,
        passed: bool = None,
    ):
        self.anti_spoofing_result = anti_spoofing_result
        self.country_code = country_code
        self.detection_result = detection_result
        self.document_type = document_type
        self.passed = passed

    def validate(self):
        if self.anti_spoofing_result:
            self.anti_spoofing_result.validate()
        if self.detection_result:
            self.detection_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.anti_spoofing_result is not None:
            result['AntiSpoofingResult'] = self.anti_spoofing_result.to_map()
        if self.country_code is not None:
            result['CountryCode'] = self.country_code
        if self.detection_result is not None:
            result['DetectionResult'] = self.detection_result.to_map()
        if self.document_type is not None:
            result['DocumentType'] = self.document_type
        if self.passed is not None:
            result['Passed'] = self.passed
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AntiSpoofingResult') is not None:
            temp_model = VerifyDocumentResponseBodyDataAntiSpoofingResult()
            self.anti_spoofing_result = temp_model.from_map(m['AntiSpoofingResult'])
        if m.get('CountryCode') is not None:
            self.country_code = m.get('CountryCode')
        if m.get('DetectionResult') is not None:
            temp_model = VerifyDocumentResponseBodyDataDetectionResult()
            self.detection_result = temp_model.from_map(m['DetectionResult'])
        if m.get('DocumentType') is not None:
            self.document_type = m.get('DocumentType')
        if m.get('Passed') is not None:
            self.passed = m.get('Passed')
        return self


class VerifyDocumentResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: VerifyDocumentResponseBodyData = None,
        http_code: int = None,
        message: str = None,
        ok: bool = None,
        request_id: str = None,
        status: str = None,
    ):
        self.code = code
        self.data = data
        self.http_code = http_code
        self.message = message
        self.ok = ok
        self.request_id = request_id
        self.status = status

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.message is not None:
            result['Message'] = self.message
        if self.ok is not None:
            result['Ok'] = self.ok
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = VerifyDocumentResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Ok') is not None:
            self.ok = m.get('Ok')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class VerifyDocumentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: VerifyDocumentResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = VerifyDocumentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


