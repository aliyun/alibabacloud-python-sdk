# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
try:
    from typing import List
except ImportError:
    pass


class ScanTextRequest(TeaModel):
    def __init__(self, tasks=None, labels=None):
        self.tasks = tasks              # type: List[ScanTextRequestTasks]
        self.labels = labels            # type: List[ScanTextRequestLabels]

    def validate(self):
        self.validate_required(self.tasks, 'tasks')
        if self.tasks:
            for k in self.tasks:
                if k:
                    k.validate()
        self.validate_required(self.labels, 'labels')
        if self.labels:
            for k in self.labels:
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
        result['Labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['Labels'].append(k.to_map() if k else None)
        else:
            result['Labels'] = None
        return result

    def from_map(self, map={}):
        self.tasks = []
        if map.get('Tasks') is not None:
            for k in map.get('Tasks'):
                temp_model = ScanTextRequestTasks()
                self.tasks.append(temp_model.from_map(k))
        else:
            self.tasks = None
        self.labels = []
        if map.get('Labels') is not None:
            for k in map.get('Labels'):
                temp_model = ScanTextRequestLabels()
                self.labels.append(temp_model.from_map(k))
        else:
            self.labels = None
        return self


class ScanTextRequestTasks(TeaModel):
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


class ScanTextRequestLabels(TeaModel):
    def __init__(self, label=None):
        self.label = label              # type: str

    def validate(self):
        self.validate_required(self.label, 'label')

    def to_map(self):
        result = {}
        result['Label'] = self.label
        return result

    def from_map(self, map={}):
        self.label = map.get('Label')
        return self


class ScanTextResponse(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id    # type: str
        self.data = data                # type: ScanTextResponseData

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
            temp_model = ScanTextResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class ScanTextResponseDataElementsResultsDetailsContexts(TeaModel):
    def __init__(self, context=None):
        self.context = context          # type: str

    def validate(self):
        self.validate_required(self.context, 'context')

    def to_map(self):
        result = {}
        result['Context'] = self.context
        return result

    def from_map(self, map={}):
        self.context = map.get('Context')
        return self


class ScanTextResponseDataElementsResultsDetails(TeaModel):
    def __init__(self, label=None, contexts=None):
        self.label = label              # type: str
        self.contexts = contexts        # type: List[ScanTextResponseDataElementsResultsDetailsContexts]

    def validate(self):
        self.validate_required(self.label, 'label')
        self.validate_required(self.contexts, 'contexts')
        if self.contexts:
            for k in self.contexts:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Label'] = self.label
        result['Contexts'] = []
        if self.contexts is not None:
            for k in self.contexts:
                result['Contexts'].append(k.to_map() if k else None)
        else:
            result['Contexts'] = None
        return result

    def from_map(self, map={}):
        self.label = map.get('Label')
        self.contexts = []
        if map.get('Contexts') is not None:
            for k in map.get('Contexts'):
                temp_model = ScanTextResponseDataElementsResultsDetailsContexts()
                self.contexts.append(temp_model.from_map(k))
        else:
            self.contexts = None
        return self


class ScanTextResponseDataElementsResults(TeaModel):
    def __init__(self, label=None, suggestion=None, rate=None, details=None):
        self.label = label              # type: str
        self.suggestion = suggestion    # type: str
        self.rate = rate                # type: float
        self.details = details          # type: List[ScanTextResponseDataElementsResultsDetails]

    def validate(self):
        self.validate_required(self.label, 'label')
        self.validate_required(self.suggestion, 'suggestion')
        self.validate_required(self.rate, 'rate')
        self.validate_required(self.details, 'details')
        if self.details:
            for k in self.details:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Label'] = self.label
        result['Suggestion'] = self.suggestion
        result['Rate'] = self.rate
        result['Details'] = []
        if self.details is not None:
            for k in self.details:
                result['Details'].append(k.to_map() if k else None)
        else:
            result['Details'] = None
        return result

    def from_map(self, map={}):
        self.label = map.get('Label')
        self.suggestion = map.get('Suggestion')
        self.rate = map.get('Rate')
        self.details = []
        if map.get('Details') is not None:
            for k in map.get('Details'):
                temp_model = ScanTextResponseDataElementsResultsDetails()
                self.details.append(temp_model.from_map(k))
        else:
            self.details = None
        return self


class ScanTextResponseDataElements(TeaModel):
    def __init__(self, task_id=None, results=None):
        self.task_id = task_id          # type: str
        self.results = results          # type: List[ScanTextResponseDataElementsResults]

    def validate(self):
        self.validate_required(self.task_id, 'task_id')
        self.validate_required(self.results, 'results')
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['TaskId'] = self.task_id
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        else:
            result['Results'] = None
        return result

    def from_map(self, map={}):
        self.task_id = map.get('TaskId')
        self.results = []
        if map.get('Results') is not None:
            for k in map.get('Results'):
                temp_model = ScanTextResponseDataElementsResults()
                self.results.append(temp_model.from_map(k))
        else:
            self.results = None
        return self


class ScanTextResponseData(TeaModel):
    def __init__(self, elements=None):
        self.elements = elements        # type: List[ScanTextResponseDataElements]

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
                temp_model = ScanTextResponseDataElements()
                self.elements.append(temp_model.from_map(k))
        else:
            self.elements = None
        return self


class ScanImageRequest(TeaModel):
    def __init__(self, task=None, scene=None):
        self.task = task                # type: List[ScanImageRequestTask]
        self.scene = scene              # type: List[str]

    def validate(self):
        self.validate_required(self.task, 'task')
        if self.task:
            for k in self.task:
                if k:
                    k.validate()
        self.validate_required(self.scene, 'scene')

    def to_map(self):
        result = {}
        result['Task'] = []
        if self.task is not None:
            for k in self.task:
                result['Task'].append(k.to_map() if k else None)
        else:
            result['Task'] = None
        result['Scene'] = self.scene
        return result

    def from_map(self, map={}):
        self.task = []
        if map.get('Task') is not None:
            for k in map.get('Task'):
                temp_model = ScanImageRequestTask()
                self.task.append(temp_model.from_map(k))
        else:
            self.task = None
        self.scene = map.get('Scene')
        return self


class ScanImageRequestTask(TeaModel):
    def __init__(self, data_id=None, image_url=None, image_time_millisecond=None, interval=None, max_frames=None):
        self.data_id = data_id          # type: str
        self.image_url = image_url      # type: str
        self.image_time_millisecond = image_time_millisecond  # type: int
        self.interval = interval        # type: int
        self.max_frames = max_frames    # type: int

    def validate(self):
        self.validate_required(self.image_url, 'image_url')

    def to_map(self):
        result = {}
        result['DataId'] = self.data_id
        result['ImageURL'] = self.image_url
        result['ImageTimeMillisecond'] = self.image_time_millisecond
        result['Interval'] = self.interval
        result['MaxFrames'] = self.max_frames
        return result

    def from_map(self, map={}):
        self.data_id = map.get('DataId')
        self.image_url = map.get('ImageURL')
        self.image_time_millisecond = map.get('ImageTimeMillisecond')
        self.interval = map.get('Interval')
        self.max_frames = map.get('MaxFrames')
        return self


class ScanImageResponse(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id    # type: str
        self.data = data                # type: ScanImageResponseData

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
            temp_model = ScanImageResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class ScanImageResponseDataResultsSubResultsFrames(TeaModel):
    def __init__(self, rate=None, url=None):
        self.rate = rate                # type: float
        self.url = url                  # type: str

    def validate(self):
        self.validate_required(self.rate, 'rate')
        self.validate_required(self.url, 'url')

    def to_map(self):
        result = {}
        result['Rate'] = self.rate
        result['URL'] = self.url
        return result

    def from_map(self, map={}):
        self.rate = map.get('Rate')
        self.url = map.get('URL')
        return self


class ScanImageResponseDataResultsSubResultsHintWordsInfoList(TeaModel):
    def __init__(self, context=None):
        self.context = context          # type: str

    def validate(self):
        self.validate_required(self.context, 'context')

    def to_map(self):
        result = {}
        result['Context'] = self.context
        return result

    def from_map(self, map={}):
        self.context = map.get('Context')
        return self


class ScanImageResponseDataResultsSubResultsProgramCodeDataList(TeaModel):
    def __init__(self, x=None, y=None, width=None, height=None):
        self.x = x                      # type: float
        self.y = y                      # type: float
        self.width = width              # type: float
        self.height = height            # type: float

    def validate(self):
        self.validate_required(self.x, 'x')
        self.validate_required(self.y, 'y')
        self.validate_required(self.width, 'width')
        self.validate_required(self.height, 'height')

    def to_map(self):
        result = {}
        result['X'] = self.x
        result['Y'] = self.y
        result['Width'] = self.width
        result['Height'] = self.height
        return result

    def from_map(self, map={}):
        self.x = map.get('X')
        self.y = map.get('Y')
        self.width = map.get('Width')
        self.height = map.get('Height')
        return self


class ScanImageResponseDataResultsSubResultsLogoDataList(TeaModel):
    def __init__(self, type=None, name=None, x=None, y=None, width=None, height=None):
        self.type = type                # type: str
        self.name = name                # type: str
        self.x = x                      # type: float
        self.y = y                      # type: float
        self.width = width              # type: float
        self.height = height            # type: float

    def validate(self):
        self.validate_required(self.type, 'type')
        self.validate_required(self.name, 'name')
        self.validate_required(self.x, 'x')
        self.validate_required(self.y, 'y')
        self.validate_required(self.width, 'width')
        self.validate_required(self.height, 'height')

    def to_map(self):
        result = {}
        result['Type'] = self.type
        result['Name'] = self.name
        result['X'] = self.x
        result['Y'] = self.y
        result['Width'] = self.width
        result['Height'] = self.height
        return result

    def from_map(self, map={}):
        self.type = map.get('Type')
        self.name = map.get('Name')
        self.x = map.get('X')
        self.y = map.get('Y')
        self.width = map.get('Width')
        self.height = map.get('Height')
        return self


class ScanImageResponseDataResultsSubResultsSfaceDataListFaces(TeaModel):
    def __init__(self, name=None, rate=None, id=None):
        self.name = name                # type: str
        self.rate = rate                # type: float
        self.id = id                    # type: str

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.rate, 'rate')
        self.validate_required(self.id, 'id')

    def to_map(self):
        result = {}
        result['Name'] = self.name
        result['Rate'] = self.rate
        result['Id'] = self.id
        return result

    def from_map(self, map={}):
        self.name = map.get('Name')
        self.rate = map.get('Rate')
        self.id = map.get('Id')
        return self


class ScanImageResponseDataResultsSubResultsSfaceDataList(TeaModel):
    def __init__(self, x=None, y=None, width=None, height=None, faces=None):
        self.x = x                      # type: float
        self.y = y                      # type: float
        self.width = width              # type: float
        self.height = height            # type: float
        self.faces = faces              # type: List[ScanImageResponseDataResultsSubResultsSfaceDataListFaces]

    def validate(self):
        self.validate_required(self.x, 'x')
        self.validate_required(self.y, 'y')
        self.validate_required(self.width, 'width')
        self.validate_required(self.height, 'height')
        self.validate_required(self.faces, 'faces')
        if self.faces:
            for k in self.faces:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['X'] = self.x
        result['Y'] = self.y
        result['Width'] = self.width
        result['Height'] = self.height
        result['Faces'] = []
        if self.faces is not None:
            for k in self.faces:
                result['Faces'].append(k.to_map() if k else None)
        else:
            result['Faces'] = None
        return result

    def from_map(self, map={}):
        self.x = map.get('X')
        self.y = map.get('Y')
        self.width = map.get('Width')
        self.height = map.get('Height')
        self.faces = []
        if map.get('Faces') is not None:
            for k in map.get('Faces'):
                temp_model = ScanImageResponseDataResultsSubResultsSfaceDataListFaces()
                self.faces.append(temp_model.from_map(k))
        else:
            self.faces = None
        return self


class ScanImageResponseDataResultsSubResults(TeaModel):
    def __init__(self, label=None, suggestion=None, rate=None, scene=None, frames=None, hint_words_info_list=None,
                 program_code_data_list=None, logo_data_list=None, sface_data_list=None, ocrdata_list=None):
        self.label = label              # type: str
        self.suggestion = suggestion    # type: str
        self.rate = rate                # type: float
        self.scene = scene              # type: str
        self.frames = frames            # type: List[ScanImageResponseDataResultsSubResultsFrames]
        self.hint_words_info_list = hint_words_info_list  # type: List[ScanImageResponseDataResultsSubResultsHintWordsInfoList]
        self.program_code_data_list = program_code_data_list  # type: List[ScanImageResponseDataResultsSubResultsProgramCodeDataList]
        self.logo_data_list = logo_data_list  # type: List[ScanImageResponseDataResultsSubResultsLogoDataList]
        self.sface_data_list = sface_data_list  # type: List[ScanImageResponseDataResultsSubResultsSfaceDataList]
        self.ocrdata_list = ocrdata_list  # type: List[str]

    def validate(self):
        self.validate_required(self.label, 'label')
        self.validate_required(self.suggestion, 'suggestion')
        self.validate_required(self.rate, 'rate')
        self.validate_required(self.scene, 'scene')
        self.validate_required(self.frames, 'frames')
        if self.frames:
            for k in self.frames:
                if k:
                    k.validate()
        self.validate_required(self.hint_words_info_list, 'hint_words_info_list')
        if self.hint_words_info_list:
            for k in self.hint_words_info_list:
                if k:
                    k.validate()
        self.validate_required(self.program_code_data_list, 'program_code_data_list')
        if self.program_code_data_list:
            for k in self.program_code_data_list:
                if k:
                    k.validate()
        self.validate_required(self.logo_data_list, 'logo_data_list')
        if self.logo_data_list:
            for k in self.logo_data_list:
                if k:
                    k.validate()
        self.validate_required(self.sface_data_list, 'sface_data_list')
        if self.sface_data_list:
            for k in self.sface_data_list:
                if k:
                    k.validate()
        self.validate_required(self.ocrdata_list, 'ocrdata_list')

    def to_map(self):
        result = {}
        result['Label'] = self.label
        result['Suggestion'] = self.suggestion
        result['Rate'] = self.rate
        result['Scene'] = self.scene
        result['Frames'] = []
        if self.frames is not None:
            for k in self.frames:
                result['Frames'].append(k.to_map() if k else None)
        else:
            result['Frames'] = None
        result['HintWordsInfoList'] = []
        if self.hint_words_info_list is not None:
            for k in self.hint_words_info_list:
                result['HintWordsInfoList'].append(k.to_map() if k else None)
        else:
            result['HintWordsInfoList'] = None
        result['ProgramCodeDataList'] = []
        if self.program_code_data_list is not None:
            for k in self.program_code_data_list:
                result['ProgramCodeDataList'].append(k.to_map() if k else None)
        else:
            result['ProgramCodeDataList'] = None
        result['LogoDataList'] = []
        if self.logo_data_list is not None:
            for k in self.logo_data_list:
                result['LogoDataList'].append(k.to_map() if k else None)
        else:
            result['LogoDataList'] = None
        result['SfaceDataList'] = []
        if self.sface_data_list is not None:
            for k in self.sface_data_list:
                result['SfaceDataList'].append(k.to_map() if k else None)
        else:
            result['SfaceDataList'] = None
        result['OCRDataList'] = self.ocrdata_list
        return result

    def from_map(self, map={}):
        self.label = map.get('Label')
        self.suggestion = map.get('Suggestion')
        self.rate = map.get('Rate')
        self.scene = map.get('Scene')
        self.frames = []
        if map.get('Frames') is not None:
            for k in map.get('Frames'):
                temp_model = ScanImageResponseDataResultsSubResultsFrames()
                self.frames.append(temp_model.from_map(k))
        else:
            self.frames = None
        self.hint_words_info_list = []
        if map.get('HintWordsInfoList') is not None:
            for k in map.get('HintWordsInfoList'):
                temp_model = ScanImageResponseDataResultsSubResultsHintWordsInfoList()
                self.hint_words_info_list.append(temp_model.from_map(k))
        else:
            self.hint_words_info_list = None
        self.program_code_data_list = []
        if map.get('ProgramCodeDataList') is not None:
            for k in map.get('ProgramCodeDataList'):
                temp_model = ScanImageResponseDataResultsSubResultsProgramCodeDataList()
                self.program_code_data_list.append(temp_model.from_map(k))
        else:
            self.program_code_data_list = None
        self.logo_data_list = []
        if map.get('LogoDataList') is not None:
            for k in map.get('LogoDataList'):
                temp_model = ScanImageResponseDataResultsSubResultsLogoDataList()
                self.logo_data_list.append(temp_model.from_map(k))
        else:
            self.logo_data_list = None
        self.sface_data_list = []
        if map.get('SfaceDataList') is not None:
            for k in map.get('SfaceDataList'):
                temp_model = ScanImageResponseDataResultsSubResultsSfaceDataList()
                self.sface_data_list.append(temp_model.from_map(k))
        else:
            self.sface_data_list = None
        self.ocrdata_list = map.get('OCRDataList')
        return self


class ScanImageResponseDataResults(TeaModel):
    def __init__(self, data_id=None, task_id=None, image_url=None, sub_results=None):
        self.data_id = data_id          # type: str
        self.task_id = task_id          # type: str
        self.image_url = image_url      # type: str
        self.sub_results = sub_results  # type: List[ScanImageResponseDataResultsSubResults]

    def validate(self):
        self.validate_required(self.data_id, 'data_id')
        self.validate_required(self.task_id, 'task_id')
        self.validate_required(self.image_url, 'image_url')
        self.validate_required(self.sub_results, 'sub_results')
        if self.sub_results:
            for k in self.sub_results:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['DataId'] = self.data_id
        result['TaskId'] = self.task_id
        result['ImageURL'] = self.image_url
        result['SubResults'] = []
        if self.sub_results is not None:
            for k in self.sub_results:
                result['SubResults'].append(k.to_map() if k else None)
        else:
            result['SubResults'] = None
        return result

    def from_map(self, map={}):
        self.data_id = map.get('DataId')
        self.task_id = map.get('TaskId')
        self.image_url = map.get('ImageURL')
        self.sub_results = []
        if map.get('SubResults') is not None:
            for k in map.get('SubResults'):
                temp_model = ScanImageResponseDataResultsSubResults()
                self.sub_results.append(temp_model.from_map(k))
        else:
            self.sub_results = None
        return self


class ScanImageResponseData(TeaModel):
    def __init__(self, results=None):
        self.results = results          # type: List[ScanImageResponseDataResults]

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
                temp_model = ScanImageResponseDataResults()
                self.results.append(temp_model.from_map(k))
        else:
            self.results = None
        return self


