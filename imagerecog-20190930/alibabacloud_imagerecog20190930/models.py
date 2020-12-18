# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, BinaryIO


class EvaluateCertificateQualityRequest(TeaModel):
    def __init__(
        self,
        image_url: str = None,
        type: str = None,
    ):
        self.image_url = image_url
        self.type = type

    def validate(self):
        self.validate_required(self.image_url, 'image_url')
        self.validate_required(self.type, 'type')

    def to_map(self):
        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class EvaluateCertificateQualityResponseDataElements(TeaModel):
    def __init__(
        self,
        value: str = None,
        pass_: str = None,
        score: str = None,
    ):
        self.value = value
        self.pass_ = pass_
        self.score = score

    def validate(self):
        self.validate_required(self.value, 'value')
        self.validate_required(self.pass_, 'pass_')
        self.validate_required(self.score, 'score')

    def to_map(self):
        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        if self.pass_ is not None:
            result['Pass'] = self.pass_
        if self.score is not None:
            result['Score'] = self.score
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('Pass') is not None:
            self.pass_ = m.get('Pass')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        return self


class EvaluateCertificateQualityResponseData(TeaModel):
    def __init__(
        self,
        elements: List[EvaluateCertificateQualityResponseDataElements] = None,
    ):
        self.elements = elements

    def validate(self):
        self.validate_required(self.elements, 'elements')
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
                temp_model = EvaluateCertificateQualityResponseDataElements()
                self.elements.append(temp_model.from_map(k))
        return self


class EvaluateCertificateQualityResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: EvaluateCertificateQualityResponseData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
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
            temp_model = EvaluateCertificateQualityResponseData()
            self.data = temp_model.from_map(m['Data'])
        return self


class EvaluateCertificateQualityAdvanceRequest(TeaModel):
    def __init__(
        self,
        image_urlobject: BinaryIO = None,
        type: str = None,
    ):
        self.image_urlobject = image_urlobject
        self.type = type

    def validate(self):
        self.validate_required(self.image_urlobject, 'image_urlobject')
        self.validate_required(self.type, 'type')

    def to_map(self):
        result = dict()
        if self.image_urlobject is not None:
            result['ImageURLObject'] = self.image_urlobject
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURLObject') is not None:
            self.image_urlobject = m.get('ImageURLObject')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DetectFruitsRequest(TeaModel):
    def __init__(
        self,
        image_url: str = None,
    ):
        self.image_url = image_url

    def validate(self):
        self.validate_required(self.image_url, 'image_url')

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


class DetectFruitsResponseDataElements(TeaModel):
    def __init__(
        self,
        name: str = None,
        score: float = None,
        box: List[float] = None,
    ):
        self.name = name
        self.score = score
        self.box = box

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.score, 'score')
        self.validate_required(self.box, 'box')

    def to_map(self):
        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.score is not None:
            result['Score'] = self.score
        if self.box is not None:
            result['Box'] = self.box
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('Box') is not None:
            self.box = m.get('Box')
        return self


class DetectFruitsResponseData(TeaModel):
    def __init__(
        self,
        elements: List[DetectFruitsResponseDataElements] = None,
    ):
        self.elements = elements

    def validate(self):
        self.validate_required(self.elements, 'elements')
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
                temp_model = DetectFruitsResponseDataElements()
                self.elements.append(temp_model.from_map(k))
        return self


class DetectFruitsResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: DetectFruitsResponseData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
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
            temp_model = DetectFruitsResponseData()
            self.data = temp_model.from_map(m['Data'])
        return self


class DetectFruitsAdvanceRequest(TeaModel):
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


class ClassifyingRubbishRequest(TeaModel):
    def __init__(
        self,
        image_url: str = None,
    ):
        self.image_url = image_url

    def validate(self):
        self.validate_required(self.image_url, 'image_url')

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


class ClassifyingRubbishResponseDataElements(TeaModel):
    def __init__(
        self,
        category: str = None,
        category_score: float = None,
        rubbish: str = None,
        rubbish_score: float = None,
    ):
        self.category = category
        self.category_score = category_score
        self.rubbish = rubbish
        self.rubbish_score = rubbish_score

    def validate(self):
        self.validate_required(self.category, 'category')
        self.validate_required(self.category_score, 'category_score')
        self.validate_required(self.rubbish, 'rubbish')
        self.validate_required(self.rubbish_score, 'rubbish_score')

    def to_map(self):
        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.category_score is not None:
            result['CategoryScore'] = self.category_score
        if self.rubbish is not None:
            result['Rubbish'] = self.rubbish
        if self.rubbish_score is not None:
            result['RubbishScore'] = self.rubbish_score
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('CategoryScore') is not None:
            self.category_score = m.get('CategoryScore')
        if m.get('Rubbish') is not None:
            self.rubbish = m.get('Rubbish')
        if m.get('RubbishScore') is not None:
            self.rubbish_score = m.get('RubbishScore')
        return self


class ClassifyingRubbishResponseData(TeaModel):
    def __init__(
        self,
        sensitive: bool = None,
        elements: List[ClassifyingRubbishResponseDataElements] = None,
    ):
        self.sensitive = sensitive
        self.elements = elements

    def validate(self):
        self.validate_required(self.sensitive, 'sensitive')
        self.validate_required(self.elements, 'elements')
        if self.elements:
            for k in self.elements:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.sensitive is not None:
            result['Sensitive'] = self.sensitive
        result['Elements'] = []
        if self.elements is not None:
            for k in self.elements:
                result['Elements'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Sensitive') is not None:
            self.sensitive = m.get('Sensitive')
        self.elements = []
        if m.get('Elements') is not None:
            for k in m.get('Elements'):
                temp_model = ClassifyingRubbishResponseDataElements()
                self.elements.append(temp_model.from_map(k))
        return self


class ClassifyingRubbishResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: ClassifyingRubbishResponseData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
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
            temp_model = ClassifyingRubbishResponseData()
            self.data = temp_model.from_map(m['Data'])
        return self


class ClassifyingRubbishAdvanceRequest(TeaModel):
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


class RecognizeVehicleTypeRequest(TeaModel):
    def __init__(
        self,
        image_url: str = None,
    ):
        self.image_url = image_url

    def validate(self):
        self.validate_required(self.image_url, 'image_url')

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


class RecognizeVehicleTypeResponseDataElements(TeaModel):
    def __init__(
        self,
        name: str = None,
        score: float = None,
    ):
        self.name = name
        self.score = score

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.score, 'score')

    def to_map(self):
        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.score is not None:
            result['Score'] = self.score
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        return self


class RecognizeVehicleTypeResponseData(TeaModel):
    def __init__(
        self,
        threshold: float = None,
        elements: List[RecognizeVehicleTypeResponseDataElements] = None,
    ):
        self.threshold = threshold
        self.elements = elements

    def validate(self):
        self.validate_required(self.threshold, 'threshold')
        self.validate_required(self.elements, 'elements')
        if self.elements:
            for k in self.elements:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        result['Elements'] = []
        if self.elements is not None:
            for k in self.elements:
                result['Elements'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        self.elements = []
        if m.get('Elements') is not None:
            for k in m.get('Elements'):
                temp_model = RecognizeVehicleTypeResponseDataElements()
                self.elements.append(temp_model.from_map(k))
        return self


class RecognizeVehicleTypeResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: RecognizeVehicleTypeResponseData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
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
            temp_model = RecognizeVehicleTypeResponseData()
            self.data = temp_model.from_map(m['Data'])
        return self


class RecognizeVehicleTypeAdvanceRequest(TeaModel):
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


class RecognizeLogoRequestTasks(TeaModel):
    def __init__(
        self,
        image_url: str = None,
    ):
        self.image_url = image_url

    def validate(self):
        self.validate_required(self.image_url, 'image_url')

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


class RecognizeLogoRequest(TeaModel):
    def __init__(
        self,
        tasks: List[RecognizeLogoRequestTasks] = None,
    ):
        self.tasks = tasks

    def validate(self):
        self.validate_required(self.tasks, 'tasks')
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
                temp_model = RecognizeLogoRequestTasks()
                self.tasks.append(temp_model.from_map(k))
        return self


class RecognizeLogoResponseDataElementsResultsLogosData(TeaModel):
    def __init__(
        self,
        name: str = None,
        type: str = None,
        x: float = None,
        y: float = None,
        h: float = None,
        w: float = None,
    ):
        self.name = name
        self.type = type
        self.x = x
        self.y = y
        self.h = h
        self.w = w

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.type, 'type')
        self.validate_required(self.x, 'x')
        self.validate_required(self.y, 'y')
        self.validate_required(self.h, 'h')
        self.validate_required(self.w, 'w')

    def to_map(self):
        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        if self.h is not None:
            result['H'] = self.h
        if self.w is not None:
            result['W'] = self.w
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        if m.get('H') is not None:
            self.h = m.get('H')
        if m.get('W') is not None:
            self.w = m.get('W')
        return self


class RecognizeLogoResponseDataElementsResults(TeaModel):
    def __init__(
        self,
        label: str = None,
        suggestion: str = None,
        rate: float = None,
        logos_data: List[RecognizeLogoResponseDataElementsResultsLogosData] = None,
    ):
        self.label = label
        self.suggestion = suggestion
        self.rate = rate
        self.logos_data = logos_data

    def validate(self):
        self.validate_required(self.label, 'label')
        self.validate_required(self.suggestion, 'suggestion')
        self.validate_required(self.rate, 'rate')
        self.validate_required(self.logos_data, 'logos_data')
        if self.logos_data:
            for k in self.logos_data:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.label is not None:
            result['Label'] = self.label
        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion
        if self.rate is not None:
            result['Rate'] = self.rate
        result['LogosData'] = []
        if self.logos_data is not None:
            for k in self.logos_data:
                result['LogosData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')
        if m.get('Rate') is not None:
            self.rate = m.get('Rate')
        self.logos_data = []
        if m.get('LogosData') is not None:
            for k in m.get('LogosData'):
                temp_model = RecognizeLogoResponseDataElementsResultsLogosData()
                self.logos_data.append(temp_model.from_map(k))
        return self


class RecognizeLogoResponseDataElements(TeaModel):
    def __init__(
        self,
        task_id: str = None,
        image_url: str = None,
        results: List[RecognizeLogoResponseDataElementsResults] = None,
    ):
        self.task_id = task_id
        self.image_url = image_url
        self.results = results

    def validate(self):
        self.validate_required(self.task_id, 'task_id')
        self.validate_required(self.image_url, 'image_url')
        self.validate_required(self.results, 'results')
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        self.results = []
        if m.get('Results') is not None:
            for k in m.get('Results'):
                temp_model = RecognizeLogoResponseDataElementsResults()
                self.results.append(temp_model.from_map(k))
        return self


class RecognizeLogoResponseData(TeaModel):
    def __init__(
        self,
        elements: List[RecognizeLogoResponseDataElements] = None,
    ):
        self.elements = elements

    def validate(self):
        self.validate_required(self.elements, 'elements')
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
                temp_model = RecognizeLogoResponseDataElements()
                self.elements.append(temp_model.from_map(k))
        return self


class RecognizeLogoResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: RecognizeLogoResponseData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
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
            temp_model = RecognizeLogoResponseData()
            self.data = temp_model.from_map(m['Data'])
        return self


class TaggingImageRequest(TeaModel):
    def __init__(
        self,
        image_url: str = None,
    ):
        self.image_url = image_url

    def validate(self):
        self.validate_required(self.image_url, 'image_url')

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


class TaggingImageResponseDataTags(TeaModel):
    def __init__(
        self,
        confidence: float = None,
        value: str = None,
    ):
        self.confidence = confidence
        self.value = value

    def validate(self):
        self.validate_required(self.confidence, 'confidence')
        self.validate_required(self.value, 'value')

    def to_map(self):
        result = dict()
        if self.confidence is not None:
            result['Confidence'] = self.confidence
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class TaggingImageResponseData(TeaModel):
    def __init__(
        self,
        tags: List[TaggingImageResponseDataTags] = None,
    ):
        self.tags = tags

    def validate(self):
        self.validate_required(self.tags, 'tags')
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = TaggingImageResponseDataTags()
                self.tags.append(temp_model.from_map(k))
        return self


class TaggingImageResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: TaggingImageResponseData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
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
            temp_model = TaggingImageResponseData()
            self.data = temp_model.from_map(m['Data'])
        return self


class TaggingImageAdvanceRequest(TeaModel):
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


class RecognizeSceneRequest(TeaModel):
    def __init__(
        self,
        image_url: str = None,
    ):
        self.image_url = image_url

    def validate(self):
        self.validate_required(self.image_url, 'image_url')

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


class RecognizeSceneResponseDataTags(TeaModel):
    def __init__(
        self,
        confidence: float = None,
        value: str = None,
    ):
        self.confidence = confidence
        self.value = value

    def validate(self):
        self.validate_required(self.confidence, 'confidence')
        self.validate_required(self.value, 'value')

    def to_map(self):
        result = dict()
        if self.confidence is not None:
            result['Confidence'] = self.confidence
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class RecognizeSceneResponseData(TeaModel):
    def __init__(
        self,
        tags: List[RecognizeSceneResponseDataTags] = None,
    ):
        self.tags = tags

    def validate(self):
        self.validate_required(self.tags, 'tags')
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = RecognizeSceneResponseDataTags()
                self.tags.append(temp_model.from_map(k))
        return self


class RecognizeSceneResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: RecognizeSceneResponseData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
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
            temp_model = RecognizeSceneResponseData()
            self.data = temp_model.from_map(m['Data'])
        return self


class RecognizeSceneAdvanceRequest(TeaModel):
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


class RecognizeImageColorRequest(TeaModel):
    def __init__(
        self,
        url: str = None,
        color_count: int = None,
    ):
        self.url = url
        self.color_count = color_count

    def validate(self):
        self.validate_required(self.url, 'url')

    def to_map(self):
        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        if self.color_count is not None:
            result['ColorCount'] = self.color_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('ColorCount') is not None:
            self.color_count = m.get('ColorCount')
        return self


class RecognizeImageColorResponseDataColorTemplateList(TeaModel):
    def __init__(
        self,
        color: str = None,
        label: str = None,
        percentage: float = None,
    ):
        self.color = color
        self.label = label
        self.percentage = percentage

    def validate(self):
        self.validate_required(self.color, 'color')
        self.validate_required(self.label, 'label')
        self.validate_required(self.percentage, 'percentage')

    def to_map(self):
        result = dict()
        if self.color is not None:
            result['Color'] = self.color
        if self.label is not None:
            result['Label'] = self.label
        if self.percentage is not None:
            result['Percentage'] = self.percentage
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Color') is not None:
            self.color = m.get('Color')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Percentage') is not None:
            self.percentage = m.get('Percentage')
        return self


class RecognizeImageColorResponseData(TeaModel):
    def __init__(
        self,
        color_template_list: List[RecognizeImageColorResponseDataColorTemplateList] = None,
    ):
        self.color_template_list = color_template_list

    def validate(self):
        self.validate_required(self.color_template_list, 'color_template_list')
        if self.color_template_list:
            for k in self.color_template_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['ColorTemplateList'] = []
        if self.color_template_list is not None:
            for k in self.color_template_list:
                result['ColorTemplateList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.color_template_list = []
        if m.get('ColorTemplateList') is not None:
            for k in m.get('ColorTemplateList'):
                temp_model = RecognizeImageColorResponseDataColorTemplateList()
                self.color_template_list.append(temp_model.from_map(k))
        return self


class RecognizeImageColorResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: RecognizeImageColorResponseData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
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
            temp_model = RecognizeImageColorResponseData()
            self.data = temp_model.from_map(m['Data'])
        return self


class RecognizeImageColorAdvanceRequest(TeaModel):
    def __init__(
        self,
        url_object: BinaryIO = None,
        color_count: int = None,
    ):
        self.url_object = url_object
        self.color_count = color_count

    def validate(self):
        self.validate_required(self.url_object, 'url_object')

    def to_map(self):
        result = dict()
        if self.url_object is not None:
            result['UrlObject'] = self.url_object
        if self.color_count is not None:
            result['ColorCount'] = self.color_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UrlObject') is not None:
            self.url_object = m.get('UrlObject')
        if m.get('ColorCount') is not None:
            self.color_count = m.get('ColorCount')
        return self


class DetectImageElementsRequest(TeaModel):
    def __init__(
        self,
        url: str = None,
    ):
        self.url = url

    def validate(self):
        self.validate_required(self.url, 'url')

    def to_map(self):
        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class DetectImageElementsResponseDataElements(TeaModel):
    def __init__(
        self,
        type: str = None,
        x: int = None,
        y: int = None,
        width: int = None,
        height: int = None,
        score: float = None,
    ):
        self.type = type
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.score = score

    def validate(self):
        self.validate_required(self.type, 'type')
        self.validate_required(self.x, 'x')
        self.validate_required(self.y, 'y')
        self.validate_required(self.width, 'width')
        self.validate_required(self.height, 'height')
        self.validate_required(self.score, 'score')

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        if self.score is not None:
            result['Score'] = self.score
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        return self


class DetectImageElementsResponseData(TeaModel):
    def __init__(
        self,
        elements: List[DetectImageElementsResponseDataElements] = None,
    ):
        self.elements = elements

    def validate(self):
        self.validate_required(self.elements, 'elements')
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
                temp_model = DetectImageElementsResponseDataElements()
                self.elements.append(temp_model.from_map(k))
        return self


class DetectImageElementsResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: DetectImageElementsResponseData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
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
            temp_model = DetectImageElementsResponseData()
            self.data = temp_model.from_map(m['Data'])
        return self


class DetectImageElementsAdvanceRequest(TeaModel):
    def __init__(
        self,
        url_object: BinaryIO = None,
    ):
        self.url_object = url_object

    def validate(self):
        self.validate_required(self.url_object, 'url_object')

    def to_map(self):
        result = dict()
        if self.url_object is not None:
            result['UrlObject'] = self.url_object
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UrlObject') is not None:
            self.url_object = m.get('UrlObject')
        return self


class RecognizeImageStyleRequest(TeaModel):
    def __init__(
        self,
        url: str = None,
    ):
        self.url = url

    def validate(self):
        self.validate_required(self.url, 'url')

    def to_map(self):
        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class RecognizeImageStyleResponseData(TeaModel):
    def __init__(
        self,
        styles: List[str] = None,
    ):
        self.styles = styles

    def validate(self):
        self.validate_required(self.styles, 'styles')

    def to_map(self):
        result = dict()
        if self.styles is not None:
            result['Styles'] = self.styles
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Styles') is not None:
            self.styles = m.get('Styles')
        return self


class RecognizeImageStyleResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: RecognizeImageStyleResponseData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
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
            temp_model = RecognizeImageStyleResponseData()
            self.data = temp_model.from_map(m['Data'])
        return self


class RecognizeImageStyleAdvanceRequest(TeaModel):
    def __init__(
        self,
        url_object: BinaryIO = None,
    ):
        self.url_object = url_object

    def validate(self):
        self.validate_required(self.url_object, 'url_object')

    def to_map(self):
        result = dict()
        if self.url_object is not None:
            result['UrlObject'] = self.url_object
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UrlObject') is not None:
            self.url_object = m.get('UrlObject')
        return self


